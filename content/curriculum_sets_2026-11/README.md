# Six quiz-enabled lessons ready for review

The user authorised Lessons 1–2 from General Science Introduction, Essential
Mathematics Real Numbers and Core Mathematics Real Numbers before the full batch.
All six review drafts are built: **136 slides, 18 A–D quizzes, 240 minutes**.
Each lesson has three question/feedback pairs and remains exactly 40 minutes.

Local review index: `outputs/drafts/curriculum_sets_2026-11/REVIEW_INDEX.md`.
Combined teacher bundle: `outputs/drafts/curriculum_sets_2026-11/review/Six_Lesson_Quiz_Review.zip`.
The index links each PPTX/PDF and lists its quiz question slide numbers.
Files retain curriculum → strand → sub-strand folders and artifact types.

Source/archive, source phase timing, exact arithmetic, font/notes, geometry,
slide/print text, versioned manifests and actual CUDA checks passed. All 136
slides, including hidden teacher slides, and all 119 final print pages were
visually inspected for layout; repaired slides received a final recheck.
Evidence: `qa/Quiz_Review_Pilots_content_checks.json`, per-lesson reports,
visual reviews, `qa/Quiz_Review_Core_title_repair.json` and the combined package
record. CRC and all 105 content-member hashes passed for the combined archive.
These are builder checks, not native PowerPoint or teacher approval.

The **full batch is on hold for user review**. `REVIEW_SCOPE.json` keeps the
builder limited to these six lessons; do not expand that scope without the
user's instruction. Inventory: six review drafts and 508 pending lessons.
Six specifications are quiz-v1; 19 later lesson specifications remain pre-quiz
baselines requiring quiz authoring/timing, with other units unauthored.

Native PowerPoint/Slide Show/Presenter View, exact Calibri (local previews use
Carlito), teacher/source-owner, real-class pacing/access and ARES checks remain
open. Review especially the 30-second response plus 30-second feedback slots,
question difficulty, distractors, placement and reinforcement.

Teacher review files contain private answers/notes. Public questions and private
keys are separated under quizzes/public and quizzes/private. The future server
must capture individual attempts privately and project actual class aggregates
only after closure. No live collection/reporting system or pupil data is
included. Use the private paper response record if the server is unavailable.

Rebuild commands: `build_curriculum_set_lesson.py`, then
`render_check_curriculum_set.py`; inspect changed slides/print pages before
recording review with `review_package_curriculum_set.py`. Package the three
sub-strands, then run `package_quiz_review_pilots.py` for the combined bundle.
`author_quiz_review_pilots.py` reproduces the six source-specific specifications.
All review outputs/renders remain ignored by Git. No push or release requested.

The preceding authorised pre-quiz deletion remains recorded in
`qa/curriculum_quiz_reset_2026-11.json`; it is a historical reset checkpoint,
not the current zero-deck state. Original sources and unrelated Biology work
remain unchanged. Do not reimport deleted pilot drafts or use their old QA.
