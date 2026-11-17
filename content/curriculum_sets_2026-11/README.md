# Quiz design reset — generation paused

Current design: **quiz-v1**. Read `QUIZ_DESIGN.md` and `GUIDANCE.md`.
The user requested deleting the pre-quiz drafts and starting over with periodic
A–D comprehension checks. This task updates the process and resets the working
files; it does not resume curriculum generation or implement the future server.

The deletion audit is `qa/curriculum_quiz_reset_2026-11.json` (repository root).
At the pre-deletion checkpoint it contains 782 planned files in four explicit
working-output/render roots. Sources, unrelated Biology review work and
historical QA/logs are preserved. Original pilot drafts must not be reimported.

The collection has 43 sub-strands / 514 lessons and 430 verified source files.
After reset, all 514 lessons require quiz-v1 design and fresh review. The 22
continuation lesson specifications under `specs` are source-work baselines;
they intentionally fail the new build gate until lesson-level revision,
questions, placement/source evidence and response/feedback timing are authored.
Lesson 1 must also be converted to the organised specification format.

On explicit resume, read the repository restart skill and the complete chosen
source unit. Author a representative quiz-enabled pilot, preserving required
content and phase/lesson totals. Each quiz needs the fields validated by
`scripts/lesson_quizzes.py`; `tests/test_lesson_quizzes.py` provides synthetic
schema/layout examples, not curriculum questions. Do not copy their test items
into teaching material. A documented independent-assessment exception is valid.

Build one lesson with `build_curriculum_set_lesson.py`, run
`render_check_curriculum_set.py`, inspect every final slide/print page, then
record review/package using `review_package_curriculum_set.py`. Those stages
reject the old revision and stale/altered quiz manifests. All native PowerPoint,
teacher and classroom release gates remain. Working outputs/renders stay ignored.

Public questions go under `quizzes/public`, private teacher/server keys under
`quizzes/private`. IDs, option order, slide positions and deck hashes link the
future response reports to exact question versions. The live collection,
aggregate projector and individual-report integration still require a server.
