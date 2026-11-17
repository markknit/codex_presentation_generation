# Quiz-enabled three-curriculum draft continuation

User authorisation dated 17 November 2026 covers checked review drafts for all
43 sub-strands / 514 lessons across General Science, Essential Mathematics
and Core Mathematics. It supersedes the previous six-lesson hold. Original
sources, source sequence, approved subject guidance and release gates remain.

## Current checkpoint — paused for session reset

- General Science Introduction (`gensci_1_1`): Lessons 1–7 reviewed drafts.
- Essential Real Numbers (`essmath_1_1`): Lessons 1–8 reviewed drafts.
- Core Real Numbers (`coremath_1_1`): Lessons 1–8 reviewed drafts; 9–10 authored
  and source/timing validated, awaiting build.
- Total: **23 reviewed drafts, 493 slides, 63 A–D quizzes, 920 minutes and
  447 visually inspected print pages**. Inventory: 23 `review_draft`,
  2 `authored_pending_build`, 489 `pending_quiz_design`.
- All 25 specifications in these three initial units are quiz-v1. Other
  40 units/489 lessons require complete source reading and authoring.

Current local links: `outputs/drafts/curriculum_sets_2026-11/CURRENT_REVIEW_INDEX.md`.
That index links PPTX/PDF files, quiz slide positions and the three verified
current teacher ZIPs. Keep curriculum → strand → sub-strand folders and
presentations / previews / student_materials / teacher_notes / quizzes/public /
quizzes/private / review artifact types. The original `REVIEW_INDEX.md` and
`review/Six_Lesson_Quiz_Review.zip` remain frozen historical six-lesson snapshots;
their earlier generation hold is superseded. Do not rerun the [1,2]-only combined
packager against expanded current unit packages.

The last emitted pre-compaction context reading was 6.56% remaining, account
25%, on 17 November at 18:19 UTC. Compaction occurred during Core L8 inspection
at 18:21 UTC. No numerical 5% event was observed in this run; generation stopped
conservatively at compaction. Only the in-flight review and continuity were
completed. The saved pause applies to that thread even after context refresh;
`session_usage.py --guard` and the builder both refused a further build (exit 75).
Account remaining during the checkpoint was 23%.

Resume in a new session with the repository `restart` skill, `STATUS.md` and
`HANDOFF_2026-11-17_QUIZ_CONTINUATION.md`. Next: **Core Lesson 9**, then independent
Lesson 10. New sessions must verify live meters/source archives and read the
whole unit before building. At 5% account or context remaining, stop at a clean
boundary, run repository `update`, commit status and resume steps, then pause.
Unexpected compaction during low remaining capacity is also a stopping boundary.
Never treat compaction as permission to continue this paused thread.

## Evidence and boundaries

Source/archive, verbatim quiz evidence, exact arithmetic, phase timing,
notes/fonts/geometry, specification/deck/export hashes and slide/print PDF
retention checks passed. Every final slide/print page was inspected. Actual
GB10 CUDA sm_121 execution and page counts are recorded for all reviewed files;
CPU-only assembly/conversion/text/archive stages remain disclosed. Seven tests
pass. Evidence: `qa/Quiz_Continuation_content_checks.json`,
`qa/Quiz_Continuation_review_index.json`, `qa/Quiz_Continuation_environment.json`,
`qa/Quiz_Continuation_usage_checkpoint.json` and per-lesson QA/build logs.
The original six-deck checker still passes and those pilot hashes are preserved.

Teaching lessons use three 30-second response/30-second feedback pairs within
unchanged 40-minute source phase totals. General Science L7, Essential L8 and
authored Core L10 preserve independent assessment with documented no-coaching
quiz exceptions. Teacher/source-owner approval, native PowerPoint/Presenter View,
exact Calibri (local Carlito substitution), classroom pacing/access/practical
readiness and ARES checks remain open. These are review drafts.

Public questions and private key manifests have versioned IDs and exact deck
hashes. Teacher files include private answers/notes. The future server must
capture individual attempts privately, close responses, project only actual class
aggregates, and provide separately authorised individual reports. No live server,
dashboard, student reports or pupil data are included. Private paper first-response
records are provided. Static files cannot enforce server privacy by themselves.

## Continuation tools

Use `author_quiz_review_pilots.py` only to reproduce original pilot specifications;
`author_quiz_continuation.py` and `author_quiz_later_math.py` contain the explicit
source-specific continuation recipes for the three initial units. New units need
new source work; these recipes are not generic curriculum writers.

For a new authorised lesson: check usage, build using
`build_curriculum_set_lesson.py`, render/check using
`render_check_curriculum_set.py`, verify source content with
`check_quiz_continuation.py --built`, inspect every slide/print page, then record
review and package using `review_package_curriculum_set.py`. Refresh the cumulative
index with `index_curriculum_set_reviews.py`. Working drafts and render caches stay
ignored; track scripts, source-specific specs, build logs, QA and controls. No push
or release is authorised.

The pre-quiz reset remains historical in `qa/curriculum_quiz_reset_2026-11.json`.
Do not reimport deleted pilots or treat their old QA as current. Preserve unrelated
Biology work, original sources and the five untracked historical General Science
pilot QA files.
