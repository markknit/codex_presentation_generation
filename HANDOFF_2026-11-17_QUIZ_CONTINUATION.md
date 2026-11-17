# Active handoff — quiz-enabled curriculum continuation

Recorded 17 November 2026 on `jhm-spark`; branch `main` at
`/home/markk/codex_presentation_generation`. **Paused for user session reset.**
Read `STATUS.md` and use the repository `restart` skill before resuming. This
handoff is active until a later documented continuation supersedes it.

## Locked decisions

- User authorises checked review drafts across all 43 units/514 lessons in
  General Science (197), Essential Mathematics (135), Core Mathematics (182).
  This supersedes the old six-deck hold; no need to ask for that authorisation
  again. It does not authorise push, classroom release or waive external gates.
- Periodic neutral A–D quizzes, source-backed keys/distractors, independent
  collection, response closure, then actual class aggregates and reinforcement.
  Keep individual attempts/private reports off the projector. No live server
  exists in this repo. Never fabricate responses, URLs or observations.
- Original source activities, sequence/phenomenon, exact phase totals and full
  teacher guidance control. Read the whole unit including task/key/assessment
  materials before authoring. Use approved Mathematics guidance for Mathematics,
  approved general science manual for General Science; never the Cells manual.
- One editable PPTX per lesson; concise visual student screens, ordered complete
  speaker notes, hidden teacher slides 2–3, Calibri/phase colours/logos/timers.
  Files grouped curriculum → strand → substrand → artifact folders.
- Actual GPU execution is mandatory for supported raster stages, fail closed.
  Current CUDA sm_121/GB10 pipeline works. Document CPU-only stages; no GPU claim
  for python-pptx, LibreOffice, PDF rasterisation, text/arithmetic or packaging.
- Stop at 5% account OR context remaining, whichever is first. Check before each
  lesson and after inspection. Unexpected compaction during low remaining context
  also means stop conservatively. Finish only the in-flight boundary and
  `/update`, commit, then pause. Compaction never grants a fresh generation budget.
- Keep 6.1 Sol Medium for authoring/review. Luna may suit validated bounded
  extraction/packaging; no model configuration was changed in this session.

## Verified checkpoint

| Initial unit | Reviewed lessons | Slides | A–D checks | Print pages |
| --- | --- | ---: | ---: | ---: |
| General Science Introduction `gensci_1_1` | 1–7 of 7 | 149 | 18 | 146 |
| Essential Real Numbers `essmath_1_1` | 1–8 of 8 | 169 | 21 | 153 |
| Core Real Numbers `coremath_1_1` | 1–8 of 10 | 175 | 24 | 148 |
| Total | 23 of 514 | 493 | 63 | 447 |

920 scheduled minutes. Teaching lessons have three response/feedback pairs using
30+30 seconds each within unchanged 40-minute source phase totals. Written exits
are saved before the final feedback. Independent assessment exceptions: GS L7,
Essential L8, authored Core L10, with no coached polls/answers before collection.

All 25 initial-unit specifications are quiz-v1. **Core L9 and L10 are authored,
source/timing validated and unbuilt.** Inventory: 23 `review_draft`,
2 `authored_pending_build`, 489 `pending_quiz_design`. The other 40 units/489
lessons still need complete source reading and source-specific authoring.

Every reviewed final slide and print page was inspected; checks include exact
archive/member/source quotes, arithmetic, phase totals, spec/deck/export hashes,
notes/fonts/geometry and full PDF text retention. Seven tests and the immutable
original six-deck checker pass. Actual CUDA page counts/deck hashes verified for
all current reviewed files. No new CUDA failure this session. Earlier low-memory
CUDA recovery is historical. Local rendering uses Carlito in place of Calibri.

Evidence: `qa/Quiz_Continuation_{content_checks,review_index,environment,usage_checkpoint}.json`,
per-lesson QA under `qa/curriculum_sets_2026-11`, specifications under
`content/curriculum_sets_2026-11/specs`, logs under
`build_logs/curriculum_sets_2026-11`. All 430 source members and their archives
were verified by the inventory tool this session. The initial three units were
read completely; later units have not been read in this continuation.

## Review files and preservation

Current local index:
`outputs/drafts/curriculum_sets_2026-11/CURRENT_REVIEW_INDEX.md`.
It links every current PPTX/PDF, quiz slide positions and unit ZIPs. The ZIPs
include private teacher notes/keys; keep them in the teacher review workflow.

- Core L1–8: `Core_Mathematics/Strand_1.0_Numbers_and_Algebra/SS1.1_Real_Numbers/review/coremath_1_1_Review.zip`;
  SHA-256 `8858f55004c1b7c62aa233e179896b444670cde37e65677aecc9b7a4d0af5d12`.
- Essential L1–8: `Essential_Mathematics/Strand_1.0_Numbers_and_Algebra/SS1.1_Real_Numbers/review/essmath_1_1_Review.zip`;
  SHA-256 `b4b63aa5b755070a002040452ec366a7f681bca73f5fcd22d970839fcfff676d`.
- General Science L1–7: `General_Science/Strand_1.0_Life_Science/SS1.1_Introduction_to_General_Science/review/gensci_1_1_Review.zip`;
  SHA-256 `181c2b79b7b4ca97232f14c782b7906ea897686f5a92a5cc61ae3bcae428ece5`.

Paths above relative to the draft root. CRC and 122/124/109 content member hashes
respectively verified. Original `review/Six_Lesson_Quiz_Review.zip` remains a
frozen six-deck snapshot with SHA-256
`6410c1ed915e982f8960605ca6ba71f61a563dd6288d58d848c346988671d130`.
Its `REVIEW_INDEX.md` hold is historical. Do not rerun
`package_quiz_review_pilots.py` against the expanded unit packages; it intentionally
expects Lessons [1,2]. Use current unit packages and the cumulative index.

Working outputs/renders remain ignored and host-local. This local checkpoint
tracks scripts, specs, controls, build logs and QA; it is not a Git transfer of
PPTX files. No push. Preserve unrelated untracked extracted Cell Structure review
folder and five `qa/GenSci_G10_Introduction_L1_Scientific_Questions_*.json` files.
Do not restore deleted pre-quiz pilots or reuse their superseded QA.

## Why this thread stopped

Initial account 33%/context 93.23%. Last manual check: 9.57% context. Last emitted
pre-compaction event: **6.56% context, 25% account**, 18:19 UTC. At 18:21 UTC context
compacted during Core L8 contact-sheet output. No numerical 5% event was observed
in this generation run. Stopped conservatively; completed only the in-flight
L8 review, package/index and `/update`. Latest account meter during checkpoint:
23%. Both guard and builder refused a new build with exit 75; Core L9 has no PPTX.

`qa/Quiz_Continuation_usage_checkpoint.json` has a thread-specific pause latch.
A new session gets a different thread ID and must verify live meters. If explicitly
resetting/resuming this same thread, deliberately clear the latch after `/restart`;
do not let automatic compaction clear it or simply ignore a guard refusal.
When reviewing images near the limit, emit one or two contact sheets at a time.

## Exact resume sequence

1. Run repository `/restart` and Step 0; read current STATUS/WORKFLOW/this handoff,
   `GUIDANCE.md`, `QUIZ_DESIGN.md` and approved subject guidance. Compare branch,
   source archive hashes, host/GPU and inventory against this checkpoint.
2. Check `.venv/bin/python scripts/session_usage.py --guard`. Exit 75 means do not
   start a lesson; do not infer approval from a refreshed context percentage.
3. Read the complete current Core Real Numbers source unit (paths/hashes in
   inventory); inspect its existing Lesson 9/10 specs. The extracted source copies
   in `.cache/quiz_continuation_sources/coremath_1_1` are ignored scratch aids;
   original archive-verified sources remain authoritative.
4. Build **Core Lesson 9** using the ready quiz-v1 spec:

```bash
.venv/bin/python scripts/session_usage.py --guard
.venv/bin/python scripts/build_curriculum_set_lesson.py coremath_1_1 9
.venv/bin/python scripts/render_check_curriculum_set.py coremath_1_1 9
.venv/bin/python scripts/check_quiz_continuation.py coremath_1_1 9 --built
```

5. Inspect every rendered slide (including hidden teacher slides) and every
   print page; repair only evidenced defects, record deviations, rerun affected
   checks. Then `review_package_curriculum_set.py review coremath_1_1 9 --finding
   '<actual final observations>'`; do not claim visual review without viewing.
6. Recheck usage, package Core, refresh index. Repeat for independent Lesson 10
   only if the guard permits, retaining the assessment exception.

```bash
.venv/bin/python scripts/review_package_curriculum_set.py package coremath_1_1
.venv/bin/python scripts/index_curriculum_set_reviews.py
```

7. Next whole-unit options: GS `gensci_1_2` The Cell (12 lessons); Essential
   `essmath_1_2` Indices (8); Core `coremath_1_2` Indices and Logarithms (14).
   Read the whole chosen unit and prepare source-specific specs/visuals/quizzes;
   existing continuation recipes apply only to initial units. Legacy Biology
   Cell decks are not replacements for General Science source work.
8. Keep small checked batches, update inventory/current index/packages, check
   usage repeatedly; `/update`, commit and pause at the next clean stop.

## Tool repairs and remaining gates

`author_quiz_continuation.py`: GS3–7, Essential3–5, Core3–5 source-specific recipes.
`author_quiz_later_math.py`: Essential6–8 and Core6–10. Both preserve reviewed
pilots. `check_quiz_continuation.py` validates sources/specs and optional built
artifacts. Original six-deck checker is fixed to its immutable six-lesson scope.
Current index generator verifies artifact/review hashes and current ZIP links.
The inventory tool preserves same-revision progress and never reimports pilots.

Final worksheet/rubric repairs are in specs/logs: GS5 separate career evidence
chart; GS7 rubric fresh page, repeated headers, non-splitting criteria; math blank
working row heights/column widths; Core5 decimal-list comma spacing; Essential6
separate BP columns with units and no health interpretation. `RN8` whole-code
assessment checks prevent false positives on legitimate Core `CRN8` references.
No need to rebuild reviewed lessons unless relevant files change.

All 23 files remain builder-reviewed drafts. Native PowerPoint/Slide Show/
Presenter View, exact Calibri, teacher/source-owner accuracy/pacing, practical/
access readiness and ARES remain open. Future server authentication, private
attempt capture/scoring, aggregate-only projection and reports are unimplemented
and require their own validation. Neither automated checks nor CUDA establishes
these external approvals.
