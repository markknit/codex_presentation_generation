#!/usr/bin/env python3
"""Verified source inventory and curriculum/strand/sub-strand draft folders."""
import hashlib
import json
import re
import zipfile
from collections import defaultdict
from pathlib import Path
from lesson_quizzes import REVISION

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'final_curriculum_outputs'
UPSTREAM=SOURCE.resolve().parents[1]
OUT=ROOT/'outputs/drafts/curriculum_sets_2026-11'
CONTROL=ROOT/'content/curriculum_sets_2026-11'


def slug(value):return re.sub(r'[^\w.]+','_',value,flags=re.UNICODE).strip('_')
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def unit_paths(unit):
    relative=Path(unit['curriculum'])/unit['strand_folder']/unit['substrand_folder']
    return {'output':OUT/relative,'qa':ROOT/'qa/curriculum_sets_2026-11'/relative,
            'logs':ROOT/'build_logs/curriculum_sets_2026-11'/relative}


def main():
    delivery=json.loads((SOURCE/'FINAL_DELIVERY_INDEX.json').read_text())
    old_path=CONTROL/'inventory.json'
    old=json.loads(old_path.read_text()) if old_path.exists() else {}
    old_units={u['module']:u for u in old.get('units',[])}
    archives={a['path']:a for a in delivery['current_archives']}
    units=[];counts=defaultdict(lambda:{'units':0,'lessons':0})
    for entry in delivery['unit_index']:
        curriculum=entry['subject'].replace(' ','_')
        base=UPSTREAM/'data/codex_pilot_2026-11' if entry['origin']=='frozen_reviewed_pilot' else SOURCE
        candidates=list((base/'outputs/v2'/curriculum).glob('*/*_data.json'))
        matches=[p for p in candidates if json.loads(p.read_text())['META']['substrand_name']==entry['topic']]
        assert len(matches)==1,(entry['module'],matches)
        datafile=matches[0];data=json.loads(datafile.read_text());path=datafile.parent
        assert len(data['LESSONS'])==entry['lessons']
        archive=UPSTREAM/entry['archive'];expected=archives[entry['archive']]['sha256']
        assert digest(archive)==expected,archive
        hashes={}
        with zipfile.ZipFile(archive) as z:
            for f in sorted(path.iterdir()):
                if not f.is_file():continue
                members=[n for n in z.namelist() if Path(n).name==f.name]
                assert len(members)==1,(f,members)
                h=digest(f);assert hashlib.sha256(z.read(members[0])).hexdigest()==h,f
                hashes[f.name]=h
        # Use a stable canonical strand spelling while retaining source text.
        strand=data['UNIT']['strand'].replace('Measurements and Geometry','Measurement and Geometry')
        u={'module':entry['module'],'curriculum':curriculum,'subject':entry['subject'],
           'strand':data['UNIT']['strand'],'strand_folder':'Strand_'+slug(strand),
           'substrand_folder':path.name,'topic':entry['topic'],'source_folder':str(path),
           'source_archive':str(archive),'source_archive_sha256':expected,'source_hashes':hashes,
           'origin':entry['origin'],'lessons':[]}
        previous={l['number']:l for l in old_units.get(entry['module'],{}).get('lessons',[])}
        for l in data['LESSONS']:
            row={'number':l['number'],'title':l['title'],'duration':l['duration'],
                 'status':'pending_quiz_design','design_revision':REVISION}
            prior=previous.get(l['number'],{})
            if prior.get('design_revision')==REVISION:row.update(prior)
            u['lessons'].append(row)
        paths=unit_paths(u)
        for sub in ['presentations','previews','student_materials','teacher_notes','review','quizzes/public','quizzes/private']:
            (paths['output']/sub).mkdir(parents=True,exist_ok=True)
        units.append(u);counts[curriculum]['units']+=1;counts[curriculum]['lessons']+=len(u['lessons'])
    CONTROL.mkdir(parents=True,exist_ok=True)
    report={'design_revision':REVISION,'source_delivery_index_sha256':digest(SOURCE/'FINAL_DELIVERY_INDEX.json'),
            'total_units':len(units),'total_lessons':sum(x['lessons'] for x in counts.values()),
            'by_curriculum':dict(counts),'units':units,'status':'Review drafts; external approval gates open'}
    old_path.write_text(json.dumps(report,indent=2,ensure_ascii=False))
    text=['# Curriculum presentation drafts','', 'Review drafts — teacher and native PowerPoint checks remain open.','',
          'Design: quiz-v1. Old pre-quiz drafts are superseded; all lessons require quiz design and fresh review.','',
          'Folders: curriculum → strand → sub-strand → presentations / previews / student_materials / teacher_notes / quizzes/public / quizzes/private / review.','',
          '| Curriculum | Strand | Sub-strand | Lessons | Built |','| --- | --- | --- | ---: | ---: |']
    for u in units:
        paths=unit_paths(u);rel=paths['output'].relative_to(OUT)
        built=sum(bool(l.get('deck')) and (ROOT/l['deck']).is_file() for l in u['lessons'])
        text.append(f'| {u["subject"]} | {u["strand"]} | [{u["substrand_folder"]}]({rel.as_posix()}/) | {len(u["lessons"])} | {built} |')
    (OUT/'README.md').write_text('\n'.join(text)+'\n')
    print(json.dumps({'units':len(units),'lessons':report['total_lessons'],'by_curriculum':dict(counts),
                      'built':sum(bool(l.get('deck')) and (ROOT/l['deck']).is_file() for u in units for l in u['lessons']),
                      'index':str(OUT/'README.md')},indent=2))


if __name__=='__main__':main()
