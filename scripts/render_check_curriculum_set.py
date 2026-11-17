#!/usr/bin/env python3
"""Render/check one lesson; CUDA raster processing is mandatory and fail-closed."""
import argparse
import json
import re
import shutil
import subprocess
from collections import Counter,defaultdict
from pathlib import Path

from docx import Document
from pptx import Presentation
from curriculum_set_inventory import ROOT,CONTROL,unit_paths,digest
from lesson_quizzes import REVISION, check_exports


def words(t):return re.findall(r'[^\W_]+',t.replace('\u00ad','').casefold(),re.UNICODE)
def text_of(slide):
    strings=[]
    for sh in slide.shapes:
        if sh.has_text_frame:strings.append(sh.text)
        if sh.has_table:strings.extend(c.text for r in sh.table.rows for c in r.cells)
    return '\n'.join(strings)


def run(module,number):
    data=json.loads((CONTROL/'inventory.json').read_text());u=next(u for u in data['units'] if u['module']==module)
    row=u['lessons'][number-1];name=row['name'];paths=unit_paths(u)
    deck=ROOT/row['deck'];qa=paths['qa'];out=paths['output']
    subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/validate_lesson_deck.py'),str(deck),'--minutes','40'],check=True,stdout=subprocess.DEVNULL)
    tmp=ROOT/'qa'/(name+'_validation.json');tmp.rename(qa/tmp.name)
    render=ROOT/'qa/renders/curriculum_sets_2026-11'/module/name;render.mkdir(parents=True,exist_ok=True)
    subprocess.run(['soffice','-env:UserInstallation=file://'+str(ROOT/'.cache/lo-curriculum-sets'),'--headless',
        '--convert-to','pdf:impress_pdf_Export:{"ExportHiddenSlides":{"type":"boolean","value":"true"}}',
        '--outdir',str(render),str(deck)],check=True,stdout=subprocess.DEVNULL)
    pdf=render/(name+'.pdf')
    subprocess.run(['pdftoppm','-png','-r','110',str(pdf),str(render/'slide')],check=True)
    images=sorted(render.glob('slide-*.png'))
    subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/gpu_visual_qa.py'),*map(str,images),
                    '--out',str(render/'gpu'),'--preview-width','600','--columns','3','--per-sheet','9'],check=True,stdout=subprocess.DEVNULL)
    gpu=json.loads((render/'gpu/gpu_report.json').read_text());assert gpu['backend']=='CUDA sm_121'
    gpu['deck_sha256']=digest(deck);(qa/(name+'_gpu.json')).write_text(json.dumps(gpu,indent=2))
    pres=Presentation(deck);pages=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True).split('\f')
    assert len(gpu['slides'])==len(pres.slides)
    for i,s in enumerate(pres.slides):
        missing=Counter(words(text_of(s)))-Counter(words(pages[i]));assert not missing,(name,i+1,dict(missing))
        assert len([sh for sh in s.shapes if sh.shape_type==13])==2,(name,i+1,'logos')
        assert s.notes_slide.notes_text_frame.text,(name,i+1,'notes')
        for p in s.notes_slide.notes_text_frame.paragraphs:
            for r in p.runs:assert r.font.name=='Calibri'
    meta=json.loads((qa/(name+'_sources.json')).read_text())
    manifest=json.loads((qa/(name+'_manifest.json')).read_text())
    assert meta.get('design_revision')==manifest.get('design_revision')==row.get('design_revision')==REVISION
    spec=json.loads((CONTROL/'specs'/(module+'.json')).read_text())['lessons'][str(number)]
    quiz_check=check_exports(out,name,module,number,spec,u['source_hashes'],digest(deck),manifest['slides'],pres.slides)
    totals=defaultdict(float)
    for r in manifest['slides']:
        phase='Predict' if r['phase'] in ['Today','Unit map'] else r['phase']
        if phase in meta['phase_minutes']:totals[phase]+=r['minutes']
    assert dict(totals)==meta['phase_minutes'],totals
    # Compare total times with the source phase teacher moves, not only the spec.
    source=json.loads(next(Path(u['source_folder']).glob('*_data.json')).read_text())['LESSONS'][number-1]
    expected=[int(re.match(r'\s*(\d+)',f['teacherMoves']).group(1)) for f in source['framework']]
    assert list(meta['phase_minutes'].values())==expected,(module,number,expected,totals)
    shutil.copyfile(pdf,out/'previews'/(name+'_Slides.pdf'))
    docs=[]
    for folder in ['student_materials','teacher_notes']:
        for doc in sorted((out/folder).glob(name+'*.docx')):
            subprocess.run(['soffice','-env:UserInstallation=file://'+str(ROOT/'.cache/lo-curriculum-sets'),'--headless',
                            '--convert-to','pdf','--outdir',str(doc.parent),str(doc)],check=True,stdout=subprocess.DEVNULL)
            dpdf=doc.with_suffix('.pdf');body=Document(doc)
            strings=[p.text for p in body.paragraphs]
            seen=set()
            for t in body.tables:
                for r in t.rows:
                    for c in r.cells:
                        if c._tc not in seen:strings.append(c.text);seen.add(c._tc)
            rendered=subprocess.check_output(['pdftotext','-layout',str(dpdf),'-'],text=True)
            missing=Counter(words('\n'.join(strings)))-Counter(words(rendered));assert not missing,(doc,dict(missing))
            ddir=render/doc.stem;ddir.mkdir(exist_ok=True)
            subprocess.run(['pdftoppm','-png','-r','85',str(dpdf),str(ddir/'page')],check=True)
            pngs=sorted(ddir.glob('page-*.png'))
            preview=['400','4','12'] if folder=='teacher_notes' else ['600','2','4']
            subprocess.run([str(ROOT/'.venv/bin/python'),str(ROOT/'scripts/gpu_visual_qa.py'),*map(str,pngs),
                            '--out',str(ddir/'gpu'),'--preview-width',preview[0],'--columns',preview[1],'--per-sheet',preview[2]],check=True,stdout=subprocess.DEVNULL)
            docs.append({'file':str(doc.relative_to(ROOT)),'sha256':digest(doc),'pdf_sha256':digest(dpdf),
                         'pages':len(pngs),'text_retention':'PASS','gpu_report':str((ddir/'gpu/gpu_report.json').relative_to(ROOT))})
    report={'deck':str(deck.relative_to(ROOT)),'sha256':digest(deck),'slides':len(pres.slides),
            'design_revision':REVISION,'quizzes':quiz_check,
            'phase_minutes':totals,'source_phase_minutes':'PASS','slide_pdf_text':'PASS','print_documents':docs,
            'cuda_backend':gpu['backend'],'device':gpu['device'],'status':'AUTOMATED PASS — VISUAL REVIEW PENDING',
            'pending':['Every-slide builder visual review','Native PowerPoint/Presenter View','Teacher/source-owner approval',
                       'Exact Calibri (local preview uses Carlito)','Classroom pacing/equipment/access','ARES offline/content']}
    (qa/(name+'_checks.json')).write_text(json.dumps(report,indent=2))
    row.update({'status':'automated_pass_visual_pending','sha256':digest(deck),'slides':len(pres.slides)})
    (CONTROL/'inventory.json').write_text(json.dumps(data,indent=2,ensure_ascii=False))
    print(json.dumps({'module':module,'lesson':number,'slides':len(pres.slides),
                      'print_pages':sum(d['pages'] for d in docs),'checks':'PASS','visual_review':'pending','render_folder':str(render)},indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('module');p.add_argument('lesson',type=int);a=p.parse_args();run(a.module,a.lesson)
