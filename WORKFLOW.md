# Presentation generation workflow

## Environment reference

| Environment | Repository | Purpose | Current state |
| --- | --- | --- | --- |
| Windows workstation | `C:\Users\MRKni\OneDrive\codex_presentation_generation` | Repository assembly, review, and GitHub administration | Initial setup |
| GitHub | `markknit/codex_presentation_generation` | Shared source of truth and transport between hosts | To be created |
| `jhm-spark` | Clone of the same GitHub repository; exact path to be recorded after setup | Primary generation and GPU-accelerated work | Not connected |

The repository and current branch are authoritative. OneDrive is not the transport mechanism to `jhm-spark`; GitHub is.

## Step 0 verification

Run at the start of a session, after switching hosts, and before bulk generation.

```text
git branch --show-current
git log --oneline -5
git status -sb
git fetch --quiet
git status -sb
python scripts/verify_environment.py
python scripts/validate_repository.py
```

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

Prefer the GPU for:

- local generation of lesson-specific illustrations when an approved local image model produces better controllable results
- image upscaling, background removal, and batch media processing
- local vision-model review or OCR as a secondary QA signal
- large batches of rendered-slide similarity, duplicate, and anomaly checks

Keep CPU-based PowerPoint composition and package validation where appropriate. Do not force GPU use when it lowers fidelity or adds fragile dependencies. Record models, versions, prompts or seeds, licences, and source attribution for every generated visual.

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
