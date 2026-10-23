# Project instructions

## Required reading

Before substantive work, read `STATUS.md`, `WORKFLOW.md`, and the relevant source files. For Biology, Chemistry, or Physics deck work, also read the complete approved manual at `references/instructions/SeaVuria_Science_Lesson_PPT_Build_Manual.docx` and inspect the example decks in `references/templates`.

Use the repository-scoped `restart` skill at the start of a new or resumed session, after switching hosts, and before bulk generation. Use the `update` skill at the end of a session and before any reboot, risky operation, or handoff.

## Source authority

- The signed-off V2 lesson-plan materials control lesson sequence, activities, anchor phenomena, learning outcomes, and required content.
- The approved general science build manual controls Biology, Chemistry, and Physics presentation structure and pedagogy.
- The example PowerPoints control the intended visual language and quality level.
- Never use or reintroduce the Cells-specific build manual.
- Do not use the science manual to generate Mathematics decks. Mathematics remains blocked until approved Mathematics-specific guidance is present.

## Generation rules

- Read the whole unit before building a lesson so later discoveries are not revealed early.
- Produce one PowerPoint per lesson. Do not combine a unit into one deck.
- Preserve the source sequence and phenomenon. Correct only the limited issues allowed by the manual, and record each correction or deviation in a build log.
- Keep student slides concise and visual. Put complete teacher guidance in speaker notes.
- Use British spelling, Kenyan contexts, CBE terminology, correct scientific notation, and SI units.
- Do not invent facts, resources, links, expected observations, safety guidance, or answer keys.
- Keep all required text, diagrams, tables, and charts editable when practical.
- GPU acceleration is required throughout the project for every stage that supports it, per the user instruction on 2026-10-23. Select GPU-capable tools for local model inference, raster asset processing, and computational visual QA; verify actual GPU execution and do not silently fall back to CPU. Document CPU-only operations (including python-pptx assembly and LibreOffice conversion) explicitly. Hardware use never replaces factual review or teacher sign-off.

## Quality gates

Do not bulk-generate until one representative pilot deck passes all gates:

1. Source fidelity and content completeness
2. Science or mathematics accuracy review
3. Manual and template conformity
4. Slide and speaker-note completeness
5. Rendered visual inspection of every slide
6. Native PowerPoint open and Presenter View check
7. Teacher review and approval

After pilot approval, generate in small batches with the same checks. Quality outranks cost, and cost outranks speed.

## Repository hygiene

- Keep generated drafts and render intermediates out of Git.
- Track final approved decks, build logs, manifests, scripts, and control documents.
- Do not mark work complete without evidence in `STATUS.md`.
- Do not push, publish, or release a deck without the applicable review gate.
