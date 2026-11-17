# Presentation generation workflow

Current November design: `content/curriculum_sets_2026-11/QUIZ_DESIGN.md`
(`quiz-v1`). The user authorised deleting the pre-quiz drafts and restarting.
Earlier pilot-preservation and continuation entries below are historical; do
not restore those files or run their superseded writers. The reset is complete.
The 17 November authorisation covers all 514 quiz-enabled review drafts and
supersedes the six-lesson hold. External release gates remain open. Current work
is paused at the usage checkpoint documented in `STATUS.md` and
`HANDOFF_2026-11-17_QUIZ_CONTINUATION.md`.
The user’s next-session priority is the efficiency pilot in
`content/efficiency_pilot_2026-11/PLAN.md`, before further production generation.

## Environment reference

| Environment | Repository | Purpose | Current state |
| --- | --- | --- | --- |
| Windows workstation | `C:\Users\MRKni\OneDrive\codex_presentation_generation`, branch `main` | Repository assembly, review, and GitHub administration | Verified 2026-10-27: HTTPS `origin`, complete review ZIP and extracted twelve-deck folder present; Python commands unavailable on PATH. |
| GitHub | `markknit/codex_presentation_generation` | Shared source of truth and transport between hosts | Windows HTTPS fetch verified 2026-10-27; `jhm-spark` SSH access was verified on 2026-10-23. Remote URLs are checkout-specific; check `git remote -v` on the active host. |
| `jhm-spark` | `/home/markk/codex_presentation_generation`, branch `main` | Primary generation and GPU-accelerated work | Verified 2026-11-17: SSH fetch and both Python Step 0 checks passed; GB10 CUDA sm_121 verified for 493 current slides/447 print pages in 23 review drafts. Paused after Core Real Numbers L8; see active handoff. Native PowerPoint/teacher review and saved project registration remain open. |

The repository and current branch are authoritative. OneDrive is not the transport mechanism to `jhm-spark`; GitHub is.

## Step 0 verification

Run at the start of a session, after switching hosts, and before bulk generation.

```text
git branch --show-current
git log --oneline -5
git status -sb
git fetch --quiet
git status -sb
python3 scripts/verify_environment.py
python3 scripts/validate_repository.py
```

On `jhm-spark`, use `python3`; `python` was not installed at the last host check. On other hosts, use an available Python 3 interpreter. On Windows on 2026-10-27, `python`, `python3` and `py` were unavailable on PATH, so the Python checks remain outstanding there; run them on a configured host before relying on their results. LibreOffice was available on `jhm-spark` at the last host check, but native PowerPoint and Presenter View checks still require a suitable review host.

On a non-`main` branch, also run:

```text
git rev-list --count HEAD..main
```

Report drift before changing files. Do not continue bulk work when the source inventory, approved instructions, branch, or hardware state differs from `STATUS.md`.

## Phase 1 repository and host setup

1. Keep all required instructions, templates, and V2 inputs inside this repository.
2. Commit the repository-scoped `restart` and `update` skills under `.agents/skills`.
3. Create the private GitHub repository and push `main`.
4. Configure the `jhm-spark` SSH host, install and authenticate Codex there, then clone the repository.
5. Save the cloned folder as the matching Codex project on `jhm-spark`.
6. Run Step 0 on `jhm-spark` and record the exact clone path plus hardware results in `STATUS.md`.

## Phase 2 pilot

Choose one representative science lesson that exercises normal instruction, speaker notes, formative checks, diagrams, and at least one practical or data activity. Build one deck only.

The pilot establishes:

- reusable imported layouts and theme handling
- speaker-note generation and validation
- local visual asset workflow
- render and overlap checks
- native PowerPoint behaviour
- build-log format
- teacher review turnaround

Do not begin bulk generation until the pilot passes every quality gate in `AGENTS.md`.

Recorded exception, 2026-10-23: after receiving the L1 pilot, the user explicitly instructed “Proceed with lessons 2-3”. Those two Cell Structure drafts were authorised before external pilot review. This is limited to those drafts; it is not pilot approval, release approval or permission for additional lessons. All release checks remain required.

## Phase 3 unit preparation

For each unit:

1. Read all five unit source files and the complete lesson sequence.
2. Record the anchor phenomenon, driving question, lesson titles, lesson duration, practicals, demonstrations, safety needs, later discoveries, and resource placeholders.
3. Create a unit manifest with checksums of the inputs.
4. Confirm the applicable instruction manual. Hold Mathematics units until approved Mathematics guidance exists.

## Phase 4 lesson generation

Build one lesson deck at a time. Follow the source sequence and the approved slide order. Keep student-facing slides concise and visual. Put complete teaching moves, timings, checks, responses, answer keys, misconceptions, and background science in speaker notes.

Use the example decks as the design reference:

- 16:9 layout
- Calibri
- black and white base with the five phase colours
- large plain-language prompts
- clear timers and check-for-understanding labels
- hidden teacher orientation and glance slides
- persistent SeaVuria and ARES footer treatment
- editable illustrations, tables, and diagrams where practical

## Phase 5 GPU-assisted work on `jhm-spark`

The local GPU can accelerate tools that Codex launches, but it does not run the OpenAI-hosted Codex model itself.

GPU acceleration is required for every supported stage, per the user instruction on 2026-10-23. Verify actual GPU execution and fail clearly rather than silently falling back to CPU. CPU-only document assembly and conversion must be identified in build logs.

Use the GPU for:

- local generation of lesson-specific illustrations when an approved local image model produces better controllable results
- image upscaling, background removal, and batch media processing
- local vision-model review or OCR as a secondary QA signal
- large batches of rendered-slide similarity, duplicate, and anomaly checks

PowerPoint assembly with python-pptx and LibreOffice conversion have CPU code paths; installing CUDA does not accelerate them. Record these exceptions explicitly. Select GPU-capable implementations for supported processing stages while maintaining source and visual fidelity. Record models, versions, prompts or seeds, licences, and source attribution for every generated visual.

Before relying on GPU tooling, verify the NVIDIA driver, CUDA visibility, available memory, supported architecture, and the actual toolchain on `jhm-spark`.

## Phase 6 validation

For every deck:

1. Verify source coverage and slide order.
2. Confirm hidden slides, notes, timings, answer keys, formative checks, safety content, and build-log entries.
3. Run package, geometry, overflow, and font checks.
4. Render every slide and inspect it at readable size.
5. Open the deck in native PowerPoint and test Slide Show and Presenter View.
6. Complete the teacher checklist in the approved manual.

Only teacher-approved decks move from `outputs/drafts` to `outputs/final`.

## Phase 7 batching and release

Generate in small subject or unit batches. Stop the batch when a repeated defect appears. Fix the generator or workflow, rerun the affected batch, and record the lesson in `STATUS.md`.

Track final decks, build logs, input manifests, and validation reports. Keep temporary renders, caches, and draft decks out of Git.

## Explicit Windows review handoff

On 2026-10-23 the user requested committing and pushing the completed drafts for Windows sync. `outputs/review/CellStructure_Lessons1-3_Drafts.zip` is the tracked snapshot for that request, with review status and checksum in its README. Working drafts and renders remain ignored; the snapshot is not an approved release. Future review snapshots require explicit handoff authorisation or an updated project policy.

## Lesson 6 pilot extension

The user subsequently requested adding Cell Structure L6 to the same pilot. The selected review set is now L1, L2, L3 and L6; this does not generate or bypass the L4–5 teaching prerequisites. The expanded snapshot is `outputs/review/CellStructure_Pilot_Lessons1-2-3-6_Drafts.zip`, continuing the established repository/Windows handoff. L6 is a practical review draft with open teacher risk-assessment, stain/PPE, calibration and visibility decisions; no classroom release or pilot approval is implied.


## Version 2 design test, 2026-10-24

The user explicitly requested redesigning Cell Structure L1/L2/L6 using the richer `presentations2` reference folder and adding L4 as a transfer test. This authorises those four review drafts before pilot sign-off; it does not approve release or wider generation. That initial selection covered L1/L2/L4/L6 (110 slides). The complete-unit continuation below supersedes the selection; earlier snapshots remain preserved.

Use `content/cellstructure_v2/DESIGN.md`, `scripts/lesson_visuals.py` and `scripts/build_cellstructure_v2.py` for the revised approach. The visual frame accepts subject, grade, unit, theme and output-folder parameters. A new unit still requires full source reading and source-specific diagrams/content. The external reference folder is recorded by hash, while all assets and code needed to rebuild the current four decks are repository-local.

On 24 October 2026 the user explicitly requested pushing the redesign to GitHub. The authorised handoff snapshot is `outputs/review/CellStructure_Lessons1-2-4-6_v2_Review.zip`, with its verified checksum and extraction instructions in that directory’s README. Preserve earlier archives. Scientific and practical corrections remain binding, and student engagement is assessed by review rather than a structural/CUDA pass.


## Complete Cell Structure draft continuation, 2026-10-24

The user explicitly requested “generate the remaining presentations for this sub-strand”. This authorises L3, L5 and L7–12 as review drafts before external pilot sign-off, retaining the revised style. All 12 v2 decks are built (276 slides / 840 scheduled minutes); the old L3 is retained only as history. No classroom release or teacher/native PowerPoint approval follows from this exception.

Use `scripts/build_cellstructure_remaining_v2.py`, `scripts/cell_specialisation_visuals.py`, `scripts/render_cellstructure_remaining_v2.py`, `scripts/check_cellstructure_complete_v2.py` and `scripts/package_cellstructure_complete_v2.py` for this continuation. The complete package includes printable tasks rather than assuming missing card sets exist. The assessment adaptation retains source sections/criteria/bands, corrects science and matches the prepared-slide route. Original inputs are unchanged.

The user subsequently explicitly requested committing and pushing all completed work. The verified complete snapshot is `outputs/review/CellStructure_Complete_Lessons1-12_v2_Review.zip`; its README records hash and Windows extraction. Generated working drafts/renders remain ignored, with this authorised snapshot carrying actual review deliverables. Earlier snapshots and all release gates remain intact.

On 2026-10-27 the complete ZIP and an extracted review folder were found in `outputs/review` on Windows. That extracted folder is untracked and may contain review work; preserve it and use a fresh destination for any new extraction. The ZIP hash and all twelve extracted PPTX hashes matched their recorded values. This verifies transport, not review or approval.

## Chemicals of Life draft continuation, 2026-10-27

The user requested the six Grade 10 Biology 1.2 presentations in the 1.1 style. This authorises the six review drafts before external pilot sign-off; it does not approve classroom release. The user subsequently authorised a GitHub review handoff on 27 October 2026. The tracked snapshot is `outputs/review/ChemicalsOfLife_Lessons1-6_Review.zip`; its checksum and fresh-folder extraction instructions are in `outputs/review/README.md`. The local working package is `outputs/drafts/ChemicalsOfLife_Lessons1-6_Review.zip`. Source hashes, checks and per-lesson logs are in `qa/` and `build_logs/`; `content/chemicals_of_life/README.md` explains open review decisions. Working drafts and renders remain ignored by Git.

Use `scripts/build_chemicals_of_life.py`, `scripts/render_chemicals_of_life.py`, `scripts/log_chemicals_of_life.py`, `scripts/check_chemicals_of_life.py` and `scripts/package_chemicals_of_life.py`. The supplied sequence requires source-owner decisions on missing vitamin C and living-tissue/catalase coverage, and the Lesson 5 human-saliva route requires a teacher/school biosafety decision. Do not invent results or a replacement practical. The final five-part assessment requires supervised follow-up time and review of the adapted paper, original key and rubric.

## Approved Mathematics review pilots, 2026-11-16

The user approved `content/curriculum_pilots_2026-11/MATHEMATICS_PILOT_GUIDANCE.md`
and instructed proceeding with the two Lesson 1 drafts: Essential Mathematics
1.1 Real Numbers and Core Mathematics 1.1 Real Numbers. This is scoped pilot
guidance; the science manual is not Mathematics pedagogy authority. Wider
Mathematics generation still needs appropriately scoped guidance and pilot gates.

Use the current reviewed November curriculum through `final_curriculum_outputs`.
`scripts/build_math_pilots.py` builds one lesson at a time; the render/check/package
commands are in `content/curriculum_pilots_2026-11/README.md`. Read the whole
source unit before authoring, preserve RN1/CRN1 and exact 40-minute phase timings,
and verify actual source hashes against the current delivery archives.

Both drafts and local review ZIP are under `outputs/drafts/curriculum_pilots_2026-11`.
They remain ignored working files. Track code, approved guidance, logs and QA;
any tracked handoff snapshot or push needs its own authorisation. Native
PowerPoint/Presenter View, teacher/source-owner, pacing, font and ARES checks
remain open. No Mathematics module batching or classroom release is implied.

## Three-curriculum draft continuation, 2026-11-16

The user subsequently instructed building the remaining General Science,
Essential Mathematics and Core Mathematics presentation sets. This extends
draft-generation authorisation and the approved presentation guidance to the
current reviewed November collection: 43 sub-strands / 514 lessons, including
the three separately frozen reviewed pilot source units. It does not establish
native PowerPoint, teacher approval, classroom release or push authorisation.

`content/curriculum_sets_2026-11/GUIDANCE.md` controls this continuation.
`scripts/curriculum_set_inventory.py` verifies the current delivery archives and
all 430 source members, preserves current quiz-enabled deliverables without reimporting deleted pre-quiz pilots and creates
`outputs/drafts/curriculum_sets_2026-11/<curriculum>/<strand>/<sub-strand>/`.
Inside each sub-strand use presentations, previews, student_materials,
teacher_notes and review folders. Code, source-specific slide specifications,
inventory, logs and QA stay tracked; working outputs stay ignored.

Build and check one lesson at a time with `build_curriculum_set_lesson.py` and
`render_check_curriculum_set.py`, then inspect every slide/print page and record
the review using `review_package_curriculum_set.py`. Do not mark an automated
pass as a completed visual review. Package reviewed lessons by sub-strand.
The initial three pilot sub-strands have authored source-specific continuation
specifications; other units require full reading and authoring before generation.

User-requested stopping rule: run `scripts/session_usage.py --guard` before new
lessons and at clean batch boundaries. It reads only the calling thread's emitted
usage event, exposing account-window and context-capacity remaining. Use whichever
reaches 5% first. Finish/check the current lesson, apply repository `/update`,
commit continuity and pause; do not start a new lesson at or below that threshold.

## Quiz design reset, 2026-11-16 (17 November UTC)

Periodic A–D comprehension checks are now part of the three-curriculum build
contract. The authoring model selects concept transitions and useful end
checks, records source evidence and placement reasons, and budgets response
plus feedback within the unchanged lesson/phase totals. Quiz answers and
per-student records are private. Project actual class aggregates only, after
responses close. Preserve independent assessment and later discoveries.

The future server is assumed, not implemented here. Each new deck exports
public questions and a private answer-key manifest with stable versioned IDs,
slide positions and the exact deck hash. No fake API URLs, live data or server
claims. Test collection, aggregate projection and standalone reporting when
that system exists. See QUIZ_DESIGN.md for the proposed integration contract.

The user-authorised reset is scoped to the November three-curriculum working
outputs, pilot copies/packages and their render caches. The deletion plan and
hash audit are in `qa/curriculum_quiz_reset_2026-11.json`. Preserve original
curriculum sources, Biology drafts/review work and historical QA/logs. The
inventory builder must never reimport old pilots. All 514 lessons require new
quiz design/review. Old specifications are baselines, not rebuild-ready.

Before resuming, author a complete quiz-v1 lesson specification (including
Lesson 1, which previously used separate pilot writers). Validate quiz
placement, source-derived answers, neutral questions, controlled feedback,
private/public separation and exact timing. Build and review a representative
quiz-enabled pilot before further batching. Existing native PowerPoint and
teacher/release gates still apply. This reset does not resume generation or
change the previously agreed usage stopping rule.

## Six-deck quiz-enabled review set, 2026-11-16 (17 November UTC)

The user authorised two lessons per curriculum before the full batch. Build
Lessons 1–2 of General Science Introduction, Essential Real Numbers and Core
Real Numbers as separate review decks. `REVIEW_SCOPE.json` recorded this historical
limit, superseded by the 17 November full-draft authorisation below. This earlier
instruction resumed six review drafts; it did not authorise classroom release. Use three source-backed
checks per lesson, preserving all source tasks, exact phase totals and private
individual/aggregate-only reporting boundaries. Timings and engagement remain
review questions for the teacher. No live server, push or publication implied.

## Full quiz-enabled draft continuation, 2026-11-17

The user explicitly instructed proceeding with embedded quizzes for all three curricula. This supersedes the six-lesson generation limit and authorises small checked draft batches across all 514 lessons. `REVIEW_SCOPE.json` retains the authoritative module/lesson allow-list. This instruction does not claim native PowerPoint or teacher approval, classroom release, push or live response-server implementation. Check current-thread usage before each lesson and after inspection; stop at 5% account or context remaining, run `/update`, commit exact status and resume steps, then pause for the user to reset.


Current checkpoint: 23 reviewed drafts (General Science L1–7, Essential L1–8,
Core L1–8), 2 authored/unbuilt Core lessons and 489 awaiting quiz design. Current
review links and packages are in
`outputs/drafts/curriculum_sets_2026-11/CURRENT_REVIEW_INDEX.md`; the original
six-deck index/archive remain historical. Refresh current unit packages, then
use `index_curriculum_set_reviews.py`; do not rerun the original six-deck combined
packager on expanded units.

On 17 November context compacted during Core L8 image inspection after the last
emitted reading of 6.56% remaining. Stopped conservatively, completed only that
review and `/update`, and latched the pause in
`qa/Quiz_Continuation_usage_checkpoint.json`. Both the guard and builder reject a
new lesson in that thread (exit 75), regardless of renewed context. A new session
must run `/restart`, read the active handoff and verify live meters. Same-thread
explicit reset/resume requires deliberately clearing that latch; compaction alone
never clears it. Next production build is Core `coremath_1_1` Lesson 9, after
the subsequently authorised efficiency pilot described below.


## GitHub continuity handoff, 2026-11-17

After the usage pause, the user authorised pushing the committed checkpoint
before switching sessions. All eight outstanding commits through `c1d8351` were
pushed to `origin/main`; `git ls-remote` verified the exact remote/local hash.
This supersedes earlier no-push statements for repository continuity work.
The follow-up status/authorisation documentation is pushed with the same scope.
Generation remains paused at Core Real Numbers L9; external release gates stay
open. Working presentations, PDFs, current review ZIPs and render caches remain
ignored on `jhm-spark`; the push transfers tracked controls/specifications/code/
logs/QA, not those generated binaries. Read the active handoff and `/restart` in
the next session before resuming.


## Cost-efficiency pilot and local Spark offload, 2026-11-17

User authorised a bounded efficiency pilot for a new session, prioritising quality,
then total processing cost, then speed. Read `content/efficiency_pilot_2026-11/PLAN.md`
and the active handoff before any further production generation; Core L9 remains
the next production lesson after the assessment. The pilot is planned, not run.

Compare focused context/complete source packets, scripted orchestration and caches,
model-task allocation and optional API batch/caching. Include existing Spark CPU
work and GB10 GPU local text/vision/comparison candidates, recording actual GPU
execution and setup/repair/review costs. Electricity cost is excluded per the
user; no power-cost measurement is required. Current CUDA raster QA is verified;
local inference runtime/model suitability is unmeasured. Host evidence is in
`qa/Efficiency_Pilot_host_snapshot_2026-11-17.json`. No silent CPU fallback or
relaxation of source, every-page visual, native PowerPoint or teacher gates.
Keep existing drafts/sources/packages intact, experiments isolated, the current
thread paused and the 5% stopping rule enforced. Documented priority supersedes
earlier instructions to resume immediately at Core L9.
