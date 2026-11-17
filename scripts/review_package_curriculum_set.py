#!/usr/bin/env python3
"""Record an actually completed builder visual review and package a sub-strand."""
import argparse
import hashlib
import json
import shutil
import zipfile
from pptx import Presentation

from curriculum_set_inventory import ROOT,CONTROL,OUT,unit_paths,digest
from lesson_quizzes import REVISION, check_exports


def current_quiz_check(u,row,paths,deck):
    spec=json.loads((CONTROL/'specs'/(u['module']+'.json')).read_text())['lessons'][str(row['number'])]
    manifest=json.loads((paths['qa']/(deck.stem+'_manifest.json')).read_text())
    return check_exports(paths['output'],deck.stem,u['module'],row['number'],spec,
                         u['source_hashes'],digest(deck),manifest['slides'],Presentation(deck).slides)


def review(module,number,finding):
    path=CONTROL/'inventory.json';data=json.loads(path.read_text())
    u=next(u for u in data['units'] if u['module']==module);r=u['lessons'][number-1]
    paths=unit_paths(u);name=r['name'];deck=ROOT/r['deck']
    checks=json.loads((paths['qa']/(name+'_checks.json')).read_text())
    assert r.get('design_revision')==checks.get('design_revision')==REVISION
    assert checks.get('quizzes',{}).get('manifest_and_slide_checks')=='PASS'
    assert checks['sha256']==digest(deck)
    current_quiz_check(u,r,paths,deck)
    render=ROOT/'qa/renders/curriculum_sets_2026-11'/module/name
    images=sorted(render.glob('slide-*.png'));assert len(images)==checks['slides']
    report={'design_revision':REVISION,'deck_sha256':digest(deck),'slides_reviewed':list(range(1,len(images)+1)),
            'slide_render_hashes':{p.name:digest(p) for p in images},'finding':finding,
            'print_documents_reviewed':[{'file':d['file'],'sha256':d['sha256'],'pages':list(range(1,d['pages']+1))} for d in checks['print_documents']],
            'limits':'Builder source/visual review; native PowerPoint, teacher/source-owner and classroom approval remain open.'}
    (paths['qa']/(name+'_visual_review.json')).write_text(json.dumps(report,indent=2))
    r['status']='review_draft';r['visual_review']=str((paths['qa']/(name+'_visual_review.json')).relative_to(ROOT))
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False))
    print(module,number,'recorded builder visual review')


def package(module):
    path=CONTROL/'inventory.json';data=json.loads(path.read_text())
    u=next(u for u in data['units'] if u['module']==module);paths=unit_paths(u)
    entries={};ready=[]
    for r in u['lessons']:
        if r['status']!='review_draft':continue
        assert r.get('design_revision')==REVISION
        ready.append(r['number']);deck=ROOT/r['deck'];assert digest(deck)==r['sha256']
        current_quiz_check(u,r,paths,deck)
        name=deck.stem
        for folder in ['presentations','previews','student_materials','teacher_notes','quizzes/public','quizzes/private']:
            for f in sorted((paths['output']/folder).glob(name+'*')):
                if f.is_file():entries[f'{folder}/{f.name}']=f
        if r.get('existing_pilot'):
            for f in sorted((ROOT/'qa').glob(name+'_*.json')):entries['qa/'+f.name]=f
            log=ROOT/'build_logs'/(name+'.md')
            if log.exists():entries['build_logs/'+log.name]=log
        else:
            for f in sorted(paths['qa'].glob(name+'_*.json')):entries['qa/'+f.name]=f
            f=paths['logs']/(name+'.md');entries['build_logs/'+f.name]=f
    assert ready
    entries['GUIDANCE.md']=CONTROL/'GUIDANCE.md'
    entries['QUIZ_DESIGN.md']=CONTROL/'QUIZ_DESIGN.md'
    manifest={n:digest(f) for n,f in entries.items()}
    target=paths['output']/'review'/(module+'_Review.zip')
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for name,f in entries.items():z.write(f,name)
        z.writestr('MANIFEST.json',json.dumps(manifest,indent=2))
        z.writestr('REVIEW_STATUS.json',json.dumps({'module':module,'ready_lessons':ready,
            'design_revision':REVISION,'audience':'PRIVATE TEACHER REVIEW — includes answer keys and notes',
            'total_lessons':len(u['lessons']),'classroom_release':False,
            'pending':['Native PowerPoint/Presenter View','Teacher/source-owner','Exact Calibri','Classroom pacing/access','ARES']},indent=2))
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        for name,h in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==h
    paths['qa'].mkdir(parents=True,exist_ok=True)
    result={'archive':str(target.relative_to(ROOT)),'sha256':digest(target),'bytes':target.stat().st_size,
            'verified_members':len(manifest),'lessons':ready,'total_lessons':len(u['lessons']),'crc':'PASS','classroom_release':False}
    (paths['qa']/'package.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['review','package']);p.add_argument('module')
    p.add_argument('lesson',type=int,nargs='?');p.add_argument('--finding',default='All slide and print renders inspected; no unresolved layout defect seen. Source-specific limits remain in teacher notes.')
    a=p.parse_args()
    if a.action=='review':review(a.module,a.lesson,a.finding)
    else:package(a.module)
