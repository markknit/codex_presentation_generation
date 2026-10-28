# Presentation generation workflow

## Environment reference

| Environment | Repository | Purpose | Current state |
| --- | --- | --- | --- |
| Windows workstation | `C:\Users\MRKni\OneDrive\codex_presentation_generation` | Repository assembly, review, and GitHub administration | Original assembly host; not re-verified from this session |
| GitHub | `markknit/codex_presentation_generation` | Shared source of truth and transport between hosts | SSH clone and fetch verified on 2026-10-23; origin uses `git@github.com:markknit/codex_presentation_generation.git` |
| `jhm-spark` | `/home/markk/codex_presentation_generation`, branch `main` | Primary generation and GPU-accelerated work | Local execution and CUDA raster-QA verified; native PowerPoint/teacher pilot review and saved Codex project registration remain open |

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

On `jhm-spark`, use `python3`; `python` is not installed. On other hosts, use the available Python 3 interpreter. LibreOffice is available locally, but native PowerPoint and Presenter View checks still require a suitable review host.

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

## Chemicals of Life draft continuation, 2026-10-27

The user requested the six Grade 10 Biology 1.2 presentations in the 1.1 style. This authorises the six review drafts before external pilot sign-off; it does not approve classroom release. The user subsequently authorised a GitHub review handoff on 27 October 2026. The tracked snapshot is `outputs/review/ChemicalsOfLife_Lessons1-6_Review.zip`; its checksum and fresh-folder extraction instructions are in `outputs/review/README.md`. The local working package is `outputs/drafts/ChemicalsOfLife_Lessons1-6_Review.zip`. Source hashes, checks and per-lesson logs are in `qa/` and `build_logs/`; `content/chemicals_of_life/README.md` explains open review decisions. Working drafts and renders remain ignored by Git.

Use `scripts/build_chemicals_of_life.py`, `scripts/render_chemicals_of_life.py`, `scripts/log_chemicals_of_life.py`, `scripts/check_chemicals_of_life.py` and `scripts/package_chemicals_of_life.py`. The supplied sequence requires source-owner decisions on missing vitamin C and living-tissue/catalase coverage, and the Lesson 5 human-saliva route requires a teacher/school biosafety decision. Do not invent results or a replacement practical. The final five-part assessment requires supervised follow-up time and review of the adapted paper, original key and rubric.
