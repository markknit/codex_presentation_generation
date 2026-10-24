# CBE Lesson Plan Presentation Generation

This repository produces teacher-ready PowerPoint presentations from the Kenya CBE Grade 10 lesson-plan sources in `inputs/v2`.

## Priorities

Work in this order:

1. Quality: scientific and mathematical accuracy, engaging visuals, clear student-facing content, useful teacher notes, and reliable PowerPoint rendering.
2. Development cost: reuse validated layouts, local tools, and the `jhm-spark` GPU where they improve quality or reduce repeated work.
3. Speed: optimise throughput only after the quality gates pass.

## Authoritative sources

- `references/instructions/SeaVuria_Science_Lesson_PPT_Build_Manual.docx` controls Biology, Chemistry, and Physics decks.
- `references/templates/*.pptx` are the visual and structural examples.
- `inputs/v2` contains the lesson plans, teacher keys, summary tables, and structured JSON source data.
- The Cells-specific build manual is intentionally excluded and must not be used.

The science manual explicitly excludes Mathematics. Keep the Mathematics source files available, but do not generate Mathematics decks until approved Mathematics-specific guidance is added.

## Working method

1. Run `/restart` before a new session, after a host change, and before bulk generation.
2. Read the complete unit source set before building any lesson in that unit.
3. Build and validate one lesson deck at a time.
4. Render and inspect every slide. Check notes, hidden slides, timings, visual fidelity, accuracy, and PowerPoint compatibility.
5. Complete a teacher review before release.
6. Run `/update` at the end of the session and before a reboot, risky operation, or host handoff.

See `WORKFLOW.md` for the full process and `STATUS.md` for current state.

## Repository layout

- `.agents/skills`: repository-scoped `/restart` and `/update` skills
- `inputs/v2`: Grade 10 CBE source lesson plans
- `references/instructions`: approved build instructions
- `references/templates`: example PowerPoint decks
- `scripts`: environment and repository verification
- `build_logs`: per-deck deviations, corrections, and decisions
- `outputs/drafts`: generated drafts, ignored by Git
- `outputs/final`: teacher-approved final presentations
- `qa`: machine-readable validation reports; rendered preview images are ignored

## Python environment

On `jhm-spark`, run these commands from the repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
```

The pinned packages support PPTX authoring, DOCX reading, and image handling. This environment is ignored by Git. Run `source .venv/bin/activate` in each new shell, or use `.venv/bin/python` directly. GPU frameworks are separate; these document libraries do not become GPU accelerated when installed.

GPU acceleration is required for supported project stages. See `AGENTS.md` and Phase 5 of `WORKFLOW.md` for verification and CPU-only exceptions.

## First commands on a host

```text
python3 scripts/verify_environment.py
python3 scripts/validate_repository.py
```

Use `python3` on `jhm-spark`; on other hosts, use the available Python 3 interpreter.

The verification script reports the available NVIDIA GPU and supporting tools. The Codex model itself runs through OpenAI; local GPU acceleration applies to tools and local models launched by Codex on the host.

## Current review pilot

Cell Structure Lessons 1–3 are built as review drafts. The user explicitly authorised Lessons 2–3 after receiving the pilot, before completion of external pilot checks. Native PowerPoint and teacher approval remain open for all three. See `STATUS.md` and per-deck build logs for pending decisions.

After activating `.venv`, rebuild and check the draft with:

```bash
python scripts/build_biology_cellstructure_l1.py
python scripts/validate_lesson_pilot.py
```

Render with LibreOffice (include hidden slides for teacher review), then run `python scripts/gpu_visual_qa.py <rendered PNG files> --out qa/renders/<review-folder>`. The GPU helper compiles with `/usr/local/cuda/bin/nvcc` for the GB10 `sm_121` target and fails on CUDA errors. It checks raster pixel signals, not science or PowerPoint compatibility. Do not rerun the pilot builder after approval without repeating affected checks; a rebuild changes the output hash recorded in the manifest.

Build and check the explicitly authorised L2–3 drafts with:

```bash
python scripts/build_biology_cellstructure_l2_l3.py
python scripts/validate_lesson_deck.py outputs/drafts/Bio_G10_CellStructure_L2_What_Is_a_Cell.pptx --minutes 80
python scripts/validate_lesson_deck.py outputs/drafts/Bio_G10_CellStructure_L3_Prokaryotic_vs_Eukaryotic_Cells.pptx --minutes 40
```

After rendering and CUDA preview processing, `scripts/package_cellstructure_review.py --out <review-directory>` packages all three drafts, print sheets and a teacher review document. Package creation does not establish release approval. Rebuilds require updated output hashes and review of affected content.

## Windows review copy

The user-authorised handoff snapshot is `outputs/review/CellStructure_Lessons1-3_Drafts.zip`. Pull `main` and extract the ZIP to review all three PowerPoints and supporting files. These are drafts awaiting the recorded review gates; `outputs/final` remains empty.

## Expanded practical pilot

The user added Cell Structure Lesson 6 (Onion Cells Practical) to the pilot. The selected set is L1, L2, L3 and L6. L6 assumes the earlier L4–5 teaching/model and remains subject to the practical-specific decisions in its build log.

```bash
python scripts/build_biology_cellstructure_l6.py
python scripts/validate_lesson_deck.py outputs/drafts/Bio_G10_CellStructure_L6_Onion_Cells_Practical.pptx --minutes 80
python scripts/package_cellstructure_review.py --out <review-directory> --lessons 1 2 3 6
```

After rendering and CUDA processing, use the expanded package `outputs/review/CellStructure_Pilot_Lessons1-2-3-6_Drafts.zip`. It adds the blank L6 observation sheet and teacher review information. The older three-lesson ZIP remains a historical snapshot. None is an approved release.


## Reference-informed version 2 review set

The current design test is Cell Structure **L1, L2, L4 and L6**. Run `.venv/bin/python scripts/build_cellstructure_v2.py` from the repository root. Working decks go to `outputs/drafts/v2`; validation evidence and logs carry `_v2` names. See `content/cellstructure_v2/DESIGN.md` for the reusable component rules, source decisions, visual QA and remaining review gates. Exact contextual-art prompts and original assets are in `assets/cellstructure_v2`.

The user-authorised v2 GitHub handoff snapshot is `outputs/review/CellStructure_Lessons1-2-4-6_v2_Review.zip`. Its README records the checksum and Windows extraction command. Earlier archives are preserved and contain earlier versions. All decks remain review drafts, including L6's unresolved practical-readiness checks.
