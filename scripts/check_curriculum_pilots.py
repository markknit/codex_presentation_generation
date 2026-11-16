#!/usr/bin/env python3
"""Review gates and offline review bundle; does not approve classroom release."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document
from pptx import Presentation
from build_curriculum_pilots import CONFIG, OUT, PHASES, ROOT, source


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def words(t):return re.findall(r'[^\W_]+',t.casefold(),re.UNICODE)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--curriculum',choices=list(CONFIG))
    args=parser.parse_args()
    reports=[]
    for key,(_,_,name,_) in CONFIG.items():
        if args.curriculum and key!=args.curriculum:continue
        deck=OUT/(name+'.pptx')
        if not deck.exists():continue
        subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/validate_lesson_deck.py'),str(deck),'--minutes','40'],check=True,stdout=subprocess.DEVNULL)
        d=Presentation(deck)
        manifest=json.loads((ROOT/'qa'/f'{name}_manifest.json').read_text())
        render=ROOT/'qa/renders/curriculum_pilots_2026-11'/name
        gpu=json.loads((ROOT/'qa'/f'{name}_gpu.json').read_text())
        assert gpu['deck_sha256']==digest(deck)
        assert len(gpu['slides'])==len(d.slides)
        pdf=render/(name+'.pdf')
        text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True).split('\f')
        errors=[]
        for i,s in enumerate(d.slides):
            strings=[]
            for sh in s.shapes:
                if sh.has_text_frame:strings.append(sh.text)
                if sh.has_table:strings.extend(c.text for row in sh.table.rows for c in row.cells)
            missing=Counter(words('\n'.join(strings)))-Counter(words(text[i]))
            if missing:errors.append({'slide':i+1,'missing_pdf_words':dict(missing)})
            assert len([sh for sh in s.shapes if sh.shape_type==13])==2,('logos',i+1)
            for p in s.notes_slide.notes_text_frame.paragraphs:
                for r in p.runs:assert r.font.name=='Calibri',('notes font',i+1)
        totals=defaultdict(float)
        for r in manifest['slides']:
            phase=r['phase'] if r['phase'] in PHASES else ('Predict' if r['phase'] in ['Today','Unit map'] else None)
            if phase:totals[phase]+=r['minutes']
        assert list(totals.values())==([4,14,10,4,8] if key=='core' else [4,16,10,4,6]),totals
        path,data=source(key)
        # Verify the actual source artifacts against the current delivery archive.
        archive=ROOT/'final_curriculum_outputs'/('coremath_1_1_Reviewed_RubricFix_2026-11-15.zip' if key=='core' else 'Batch_01_Reviewed.zip')
        matched=[]
        with zipfile.ZipFile(archive) as z:
            for f in sorted(path.glob('*')):
                members=[n for n in z.namelist() if Path(n).name==f.name]
                assert len(members)==1,(f,members)
                assert hashlib.sha256(z.read(members[0])).hexdigest()==digest(f),f
                matched.append(f.name)
        assert not errors,errors
        shutil.copyfile(pdf,OUT/(name+'_Slides.pdf'))
        report={'deck':str(deck.relative_to(ROOT)),'sha256':digest(deck),'slides':len(d.slides),'phase_minutes':totals,
                'pdf_text_retention':'PASS — every slide, including hidden pages and table cells',
                'notes_fonts_and_two_logos':'PASS','source_current_archive_match':matched,
                'cuda_backend':gpu['backend'],'device':gpu['device'],'release_status':'REVIEW DRAFT — approval gates open',
                'pending':['Native PowerPoint / Slide Show / Presenter View','Teacher and source-owner acceptance','Real-class pacing','Exact Calibri','ARES search/offline preview']}
        (ROOT/'qa'/f'{name}_checks.json').write_text(json.dumps(report,indent=2))
        reports.append(report)
    assert reports
    print(json.dumps(reports,indent=2))


if __name__=='__main__':main()
