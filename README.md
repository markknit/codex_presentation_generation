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

## First commands on a host

```text
python3 scripts/verify_environment.py
python3 scripts/validate_repository.py
```

Use `python3` on `jhm-spark`; on other hosts, use the available Python 3 interpreter.

The verification script reports the available NVIDIA GPU and supporting tools. The Codex model itself runs through OpenAI; local GPU acceleration applies to tools and local models launched by Codex on the host.
