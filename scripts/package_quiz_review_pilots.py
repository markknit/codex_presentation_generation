#!/usr/bin/env python3
"""Combine the three reviewed two-lesson packages without losing their folders."""
import hashlib
import json
from pathlib import Path
import zipfile

from curriculum_set_inventory import ROOT, CONTROL, OUT, unit_paths, digest


def main():
    data=json.loads((CONTROL/'inventory.json').read_text())
    scope=json.loads((CONTROL/'REVIEW_SCOPE.json').read_text())
    entries={};rows=[];lessons=[]
    for module in ['gensci_1_1','essmath_1_1','coremath_1_1']:
        u=next(u for u in data['units'] if u['module']==module);paths=unit_paths(u)
        package=json.loads((paths['qa']/'package.json').read_text())
        assert package['lessons']==scope['modules'][module]==[1,2]
        archive=ROOT/package['archive'];assert digest(archive)==package['sha256']
        prefix=paths['output'].relative_to(OUT).as_posix()
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            manifest=json.loads(z.read('MANIFEST.json'))
            for name,h in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==h
            for name in z.namelist():entries[prefix+'/'+name]=z.read(name)
        for n in [1,2]:
            row=u['lessons'][n-1];assert row['status']=='review_draft'
            deck=ROOT/row['deck'];assert digest(deck)==row['sha256']
            public=json.loads((paths['output']/'quizzes/public'/(row['name']+'_Questions.json')).read_text())
            quiz_slides=', '.join(str(q['question_slide']) for q in public['questions'])
            deck_rel=deck.relative_to(OUT).as_posix()
            pdf_rel=(paths['output']/'previews'/(row['name']+'_Slides.pdf')).relative_to(OUT).as_posix()
            rows.append(f'| {u["subject"]} | {n} · {row["title"]} | [PowerPoint]({deck_rel}) | [PDF]({pdf_rel}) | {quiz_slides} |')
            lessons.append({'module':module,'lesson':n,'deck_sha256':row['sha256'],'slides':row['slides'],'quizzes':3})
    text=['# Six-lesson quiz review set','',
          'Lessons 1–2 from each curriculum. All six are review drafts; the full batch is on hold for your review.','',
          '[Download the complete teacher review bundle](review/Six_Lesson_Quiz_Review.zip).','',
          'Each quiz question is followed by its feedback slide. The question and feedback each have a 30-second allocation; review whether that pacing works for your class. First written exits are saved before the final quiz.','',
          '| Curriculum | Lesson | Editable deck | Slide preview | Quiz question slides |',
          '| --- | --- | --- | --- | --- |',*rows,'',
          'The bundle retains curriculum → strand → sub-strand folders, with student records, private teacher notes and separated public-question/private-key manifests. It contains 136 slides and 18 quizzes across six 40-minute lessons.','',
          'Teacher review only: the deck notes, feedback pages and private manifests contain answers. The static PowerPoint files do not capture live responses. The future server must store individual responses privately and project only class aggregates after closure. Without it, use the private paper response records.','',
          'Review question clarity/difficulty, distractors, placement, reinforcement and pacing. Open the PPTX in PowerPoint and check Slide Show and Presenter View. Native PowerPoint, exact Calibri (local previews use Carlito), teacher/source-owner, classroom access and ARES checks remain open. No classroom release or full-batch approval is implied.','']
    index='\n'.join(text);(OUT/'REVIEW_INDEX.md').write_text(index)
    entries['REVIEW_INDEX.md']=index.replace('[Download the complete teacher review bundle](review/Six_Lesson_Quiz_Review.zip).','This is the extracted teacher review bundle. Open the linked decks or PDFs below.').encode()
    entries['qa/Quiz_Review_Pilots_content_checks.json']=(ROOT/'qa/Quiz_Review_Pilots_content_checks.json').read_bytes()
    entries['qa/Quiz_Review_Core_title_repair.json']=(ROOT/'qa/Quiz_Review_Core_title_repair.json').read_bytes()
    assert len(lessons)==6 and sum(l['slides'] for l in lessons)==136
    manifest={name:hashlib.sha256(payload).hexdigest() for name,payload in entries.items()}
    folder=OUT/'review';folder.mkdir(exist_ok=True);target=folder/'Six_Lesson_Quiz_Review.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for name,payload in entries.items():z.writestr(name,payload)
        z.writestr('MANIFEST.json',json.dumps(manifest,indent=2))
        z.writestr('REVIEW_STATUS.json',json.dumps({'lessons':lessons,'minutes':240,'questions':18,
            'classroom_release':False,'full_batch':'On hold for user review','audience':'Private teacher review'},indent=2))
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        for name,h in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==h
        assert len([name for name in z.namelist() if name.endswith('.pptx')])==6
    report={'archive':str(target.relative_to(ROOT)),'sha256':digest(target),'bytes':target.stat().st_size,
            'verified_members':len(manifest),'crc':'PASS','lessons':lessons,'slides':136,'questions':18,
            'minutes':240,'index':str((OUT/'REVIEW_INDEX.md').relative_to(ROOT)),
            'full_batch':'On hold for user review','classroom_release':False}
    (ROOT/'qa/Quiz_Review_Pilots_package.json').write_text(json.dumps(report,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k!='lessons'},indent=2))


if __name__=='__main__':main()
