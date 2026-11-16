#!/usr/bin/env python3
"""Package unchanged local review drafts; verify CRC and every member hash."""
import hashlib
import json
import zipfile

from build_curriculum_pilots import ROOT, OUT, CONFIG


def sha(data):return hashlib.sha256(data).hexdigest()


def main():
    entries={}
    for key in ['essential','core']:
        name=CONFIG[key][2]
        qa=json.loads((ROOT/'qa'/f'{name}_checks.json').read_text())
        deck=OUT/(name+'.pptx')
        assert sha(deck.read_bytes())==qa['sha256']
        assert qa['slides']==(19 if key=='essential' else 17)
        for suffix in ['.pptx','_Slides.pdf','_Student_Task.docx','_Student_Task.pdf',
                       '_Teacher_Notes.docx','_Teacher_Notes.pdf']:
            entries[f'{key}/{name}{suffix}']=OUT/(name+suffix)
        for suffix in ['checks','validation','manifest','sources','gpu']:
            entries[f'qa/{name}_{suffix}.json']=ROOT/'qa'/f'{name}_{suffix}.json'
        entries[f'build_logs/{name}.md']=ROOT/'build_logs'/f'{name}.md'
    for n in ['Mathematics_pilots_checks.json','Mathematics_pilots_visual_review.json']:
        entries['qa/'+n]=ROOT/'qa'/n
    folder=ROOT/'content/curriculum_pilots_2026-11'
    for n in ['README.md','MATHEMATICS_PILOT_GUIDANCE.md']:entries[n]=folder/n
    manifest={n:sha(p.read_bytes()) for n,p in entries.items()}
    archive=OUT/'Mathematics_Lesson1_Pilots_Review.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for name,path in entries.items():z.write(path,name)
        z.writestr('MANIFEST.json',json.dumps(manifest,indent=2))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for n,h in manifest.items():assert sha(z.read(n))==h,n
    report={'archive':str(archive.relative_to(ROOT)),'bytes':archive.stat().st_size,
            'sha256':sha(archive.read_bytes()),'verified_members':len(manifest),'crc':'PASS',
            'status':'LOCAL REVIEW DRAFT — no push or release','manifest':manifest}
    (ROOT/'qa/Mathematics_pilots_package.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='manifest'},indent=2))


if __name__=='__main__':main()
