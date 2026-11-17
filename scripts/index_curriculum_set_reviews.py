#!/usr/bin/env python3
"""Write a current, verified review index without altering frozen snapshots."""
from collections import Counter
import json
from pathlib import Path
import zipfile

from curriculum_set_inventory import ROOT, CONTROL, OUT, unit_paths, digest


def main():
    inventory=json.loads((CONTROL/'inventory.json').read_text())
    counts=Counter(r['status'] for u in inventory['units'] for r in u['lessons'])
    lines=['# Current quiz-enabled presentation review drafts','',
           'Draft generation for all three curricula authorised 17 November 2026. Native PowerPoint, teacher/source-owner, exact-font, pacing/access and ARES release checks remain open. No live response capture/reporting is implemented.','',
           f'Inventory: {dict(counts)}; {inventory["total_lessons"]} lessons in scope.','',
           'Teacher packages include private keys and notes. Keep them in the teacher review workflow.','',
           '[Original six-lesson checkpoint](review/Six_Lesson_Quiz_Review.zip) remains a frozen historical snapshot; the current lesson and unit links below supersede its earlier generation hold.','',
           '| Curriculum | Sub-strand | Reviewed lessons / total | Current teacher review ZIP |',
           '| --- | --- | ---: | --- |']
    lessons=[];packages=[]
    for u in inventory['units']:
        paths=unit_paths(u);ready=[r for r in u['lessons'] if r['status']=='review_draft']
        if not ready:continue
        package=paths['qa']/'package.json';link='Not refreshed'
        if package.exists():
            p=json.loads(package.read_text());archive=ROOT/p['archive']
            if p['lessons']==[r['number'] for r in ready] and digest(archive)==p['sha256']:
                with zipfile.ZipFile(archive) as z:assert z.testzip() is None
                link=f'[Download]({archive.relative_to(OUT).as_posix()})';packages.append(p)
        lines.append(f'| {u["subject"]} | {u["substrand_folder"]} | {len(ready)} / {len(u["lessons"])} | {link} |')
        for r in ready:
            deck=ROOT/r['deck'];assert digest(deck)==r['sha256']
            checks=json.loads((paths['qa']/(deck.stem+'_checks.json')).read_text())
            review=json.loads((paths['qa']/(deck.stem+'_visual_review.json')).read_text())
            assert checks['sha256']==review['deck_sha256']==digest(deck)
            notes=json.loads((paths['qa']/(deck.stem+'_manifest.json')).read_text())['slides']
            quiz_slides=[s['slide'] for s in notes if s.get('quiz_stage')=='question']
            pdf=paths['output']/'previews'/(deck.stem+'_Slides.pdf');assert pdf.exists()
            lessons.append({'module':u['module'],'lesson':r['number'],'deck':r['deck'],'sha256':r['sha256'],
                            'slides':checks['slides'],'quiz_slides':quiz_slides,'print_pages':sum(x['pages'] for x in checks['print_documents'])})
    lines+=['','| Curriculum / sub-strand | Lesson | PowerPoint | Slide PDF | Quiz question slides |','| --- | ---: | --- | --- | --- |']
    by_module={u['module']:u for u in inventory['units']}
    for r in lessons:
        u=by_module[r['module']];deck=ROOT/r['deck'];paths=unit_paths(u);pdf=paths['output']/'previews'/(deck.stem+'_Slides.pdf')
        quiz=', '.join(map(str,r['quiz_slides'])) or 'Independent assessment exception'
        lines.append(f'| {u["subject"]} · {u["topic"]} | {r["lesson"]} | [PPTX]({deck.relative_to(OUT).as_posix()}) | [PDF]({pdf.relative_to(OUT).as_posix()}) | {quiz} |')
    lines+=['','Grouped folders include student_materials, private teacher_notes and quizzes/public / quizzes/private. The original six-lesson REVIEW_INDEX.md is historical. See CURRENT_REVIEW_INDEX.md for cumulative progress.','']
    (OUT/'CURRENT_REVIEW_INDEX.md').write_text('\n'.join(lines))
    report={'inventory_statuses':dict(counts),'reviewed_lessons':lessons,'packages':packages,
            'slides':sum(r['slides'] for r in lessons),'quizzes':sum(len(r['quiz_slides']) for r in lessons),
            'print_pages':sum(r['print_pages'] for r in lessons),'classroom_release':False}
    (ROOT/'qa/Quiz_Continuation_review_index.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['reviewed_lessons','packages']}))


if __name__=='__main__':main()
