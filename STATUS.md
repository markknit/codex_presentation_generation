# Project status

Last updated: 2026-10-27

## Active Threads

| Workstream | Status | Evidence or next gate |
| --- | --- | --- |
| Repository scaffold | Done | Checkout on `jhm-spark` at `/home/markk/codex_presentation_generation`, branch `main`; `python3 scripts/validate_repository.py` passed on 2026-10-23. Initial scaffold commit: `8119d93`. |
| Continuity skills | In progress | Repository copies of `restart` and `update` were read and used on `jhm-spark`. Automatic skill discovery in a saved Codex project has not been verified; Windows installation was recorded by the previous session. |
| Approved instructions | Done | General science manual selected. Cells-specific manual excluded. |
| Visual references | Reviewed; new quality target applied | Original templates remain for theme/logos. User-selected `presentations2` L1/L2/L6 references (21/28/24 slides) were fully rendered and inspected on 2026-10-24. Style evidence and hashes: `qa/CellStructure_v2_sources.json`; reusable rules: `content/cellstructure_v2/DESIGN.md`. |
| V2 source inventory | Done | 425 files total: 340 DOCX and 85 JSON across 85 units. |
| GitHub repository | Review handoffs pushed and verified | On 2026-10-27, `git ls-remote origin refs/heads/main` matched local HEAD at `b1d5515` before this continuity update. Cell Structure and Chemicals of Life review snapshots are tracked under `outputs/review`. The previously identified extracted Cell Structure folder is untracked and intentionally untouched. |
| `jhm-spark` connection | Done | Live `hostname` returned `jhm-spark`; Codex commands run locally against `/home/markk/codex_presentation_generation`. Saving this checkout as a Codex project remains unverified. |
| GPU raster processing | Verified | CUDA sm_121 on NVIDIA GB10 processed all 166 new slide previews, two new published-image assets, 28 print pages and two corrected rubric pages; prior 110 slides/four art assets retain previous evidence. CPU-only assembly/conversion/rasterisation/encoding/layout/ZIP operations are disclosed. No semantic GPU or local inference approval claimed. |
| Python authoring environment | Done | `.venv` contains the pinned `requirements.txt` packages; `pip check` passed and all three templates plus the manual loaded successfully. Activate the environment before running authoring tools. |
| Science pilot design | Revised drafts; user review pending | User found the earlier samples technically correct but visually/pedagogically weak. New version 2 has original contextual art, editable science visuals and smaller explanation steps. No teacher or classroom approval is implied by the technical feedback. |
| Biology L1/L2/L4/L6 redesign | Built; awaiting user and teacher comparison | L1: 21 slides/40 min; L2: 25/80; new L4: 37/80; L6: 27/80, 110 total. Each has hidden teacher slides 2–3 and full notes. Structural, timing and PDF-text/reveal-order checks passed; all slides rendered, CUDA-processed and visually inspected. Four per-deck manifests/validation/GPU reports and `qa/CellStructure_v2_visual_review.json` record evidence. |
| Reusable generation method | Extended across complete unit | Shared frames, native specialised-cell figures, hierarchy/guard-pore/poster models, source-specific builders, renderer, checks and complete packager are implemented. L8 uses credited published microscopy with morphology separated from mechanism. L9 geographic stomata and L10 microscopy are explicitly models; no invented experiment. Teacher/student engagement feedback is still needed. |
| Complete Biology Cell Structure v2 | Built; review gates open | L3 21/40 min; L5 21/80; L7 17/80; L8 27/80; L9 26/80; L10 18/80; L11 14/40; L12 22/80: 166 new slides. With prior L1/L2/L4/L6, all 12 now have v2 drafts: 276 slides / 840 scheduled minutes. All new slides rendered/inspected; structural, notes-font/order, timing, PDF text and CUDA checks passed. See `qa/CellStructure_complete_v2_checks.json`, source hashes, visual/print records and per-lesson logs. Earlier L3 remains historical only. |
| Biology 1.2 Chemicals of Life | Review snapshot pushed for authorised GitHub handoff; review gates open | Six 80-minute decks, 111 slides total; structural and selected sequencing checks pass (`qa/ChemicalsOfLife_checks.json`); all slides rendered and inspected, CUDA previews on GB10. Review snapshot `outputs/review/ChemicalsOfLife_Lessons1-6_Review.zip`: SHA-256 `8ada1ebdb85aa080b12f115a98567e9515b3b334345dc08bf0c007f362587495`; CRC, all 51 manifest member hashes and all six deck hashes verified. Snapshot commit `3e0b8c8` was confirmed on `origin/main`. Native PowerPoint, teacher/source-owner, practical-safety and ARES checks remain open. |
| Chemicals of Life source coverage and practicals | Source-owner and teacher decisions open | The sequence does not clearly supply the stated vitamin C and living-tissue/catalase investigations. L2 flame, L3–4 reagents/allergens and L5 human saliva, controls, reagents and waste require local approval. Case provenance and source assumptions need review; original key/rubric require adaptation to actual results. The five-part assessment needs follow-up time. |
| Biology practical readiness | Teacher safety/equipment review open | L6 stain/product/SDS, local risk/PPE/waste, equipment/calibration/visibility remain open. L5 prerequisite now built. L7 uses the V2 school-approved prepared epithelial-slide alternative; specimen provenance/local controls remain teacher decisions. No learner swabs or staining are used in this draft. |
| Mathematics decks | Blocked | The approved science manual states that Mathematics has separate guidance. Add and approve the Mathematics manual before generation. |
| Windows review handoff | Both unit snapshots pushed; review pending | Cell Structure's twelve-lesson review ZIP and Chemicals of Life's six-lesson review ZIP are tracked under `outputs/review`; see that folder's README for checksums and fresh-folder Windows extraction. Native PowerPoint/Presenter View and teacher reviews remain open; neither snapshot is a classroom release. |

## Known Issues and Lessons Learned

- Food-test source tables can present expected colours as observed results and overstate the evidence of a single case graph. Keep blank results records, label the case provenance, state test limitations, and require teacher review of any adapted key. Source outcomes missing from the lesson sequence need owner resolution, not invented activities.
- Copied Word tables can exceed the destination page width while text extraction still succeeds. Reflow inherited rubric widths, render the actual print document and inspect the final page; preserve criteria and scoring bands when repairing layout.
- Timer graphics can cover board/seedling captions despite all objects being inside the slide canvas. Reserve a clear timer area in the shared layout and inspect rendered captions.

- Slide fonts and speaker-note fonts can come from different theme parts. The inherited notes master used Aptos despite Calibri on slides. Normalise the actual notes-master theme through its relationship and explicitly set notes paragraph/run fonts; validate both.

- Technical validity and editable boxes are insufficient for engaging teaching. Record the user-selected reference version, inspect all its pages and translate the useful visual/pacing patterns into shared components. Keep student engagement as a review question rather than claiming it from automated checks.
- Whole-cell and detail diagrams should use the same geometry/palette. Inspect exact leader-line endpoints and organelle placement at full size; bounds checks cannot detect an organelle drawn outside a cell or a cytoplasm label ending on a chloroplast.
- Contextual AI art must not masquerade as microscopy evidence. Preserve exact prompts/provenance; keep the source-permitted diagram-only route explicit when authenticated EM images are unavailable.

- Git ignores working drafts and renders. For an explicitly requested cross-host review handoff, commit a clearly labelled snapshot under `outputs/review` so a pull actually transfers the presentations; keep approval status and checksums with it.
- Project continuity must live in the repository. Host-local skills alone do not travel to `jhm-spark`, so the two continuity skills are checked into `.agents/skills`.
- A successful package check does not establish visual quality, native PowerPoint behaviour, factual accuracy, practical realism, or safety. Every release needs rendered inspection, a native PowerPoint check, and teacher approval.
- The three examples establish a clean 16:9 visual system with Calibri, phase colours, large student-facing prompts, hidden teacher slides, persistent footers and logos, and restrained diagrams. New decks should reuse this language without copying lesson-specific content.
- Mathematics source files are present, but the science manual is not authoritative for Mathematics.
- Host handoffs can leave control documents stale. Run `/restart` against live Git, paths, and tools on each host, then reconcile both `STATUS.md` and the environment table before generation. Historical session entries describe their original checkpoints, not current blockers.
- On `jhm-spark`, use `python3` (Python 3.12.3); the `python` command is absent. GPU detection through `nvidia-smi` does not prove CUDA application compatibility.
- The Cell Structure source labels disagree: the folder/META/lesson labels say 1.1; the unit overview says 1.3. Keep the numerical sub-strand off the draft and request owner resolution through the build log rather than silently renumbering.
- Practical examples need a source/manual audit for absent measurement tasks, premature outcome disclosure, overconfident visibility claims and unsafe fallbacks. Keep actual observations separate from illustrative references; preserve unresolved safety specifications as teacher decisions instead of inventing a recipe or approving a shortcut.
- The example decks control visual style, not V2 source fidelity. Inherited captions, timings, resource match labels and reveal order need explicit checks; the L1 pilot corrected problems in each.
- The GitHub owner is `markknit` (two k letters). SSH access works; unauthenticated HTTPS and the connected GitHub tool did not provide access during this handoff.

## Updates - 2026-10-23 (Windows setup; historical)

- Confirmed the intended repository path and found it empty and not yet initialised as Git.
- Selected the general SeaVuria Science Lesson PowerPoint Build Manual and excluded the Cells-specific manual.
- Inventoried 425 V2 files across Biology, Chemistry, Core Mathematics, Essential Mathematics, General Science, Maths, and Physics.
- Rendered and inspected all 59 slides in the three example decks.
- Established priorities in this order: quality, development cost, then speed.
- Defined `jhm-spark` as the target execution host and added a GPU verification step.
- Initialised the local Git repository on `main` and passed repository validation.
- Installed the `restart` and `update` skills in the personal Codex skill library and included portable copies in the repository.
- Created initial commit `8119d93` with 443 files and configured the intended GitHub URL as `origin`.
- Confirmed that `markknit/codex_presentation_generation` does not yet exist. GitHub CLI is not installed and browser automation failed twice before opening the site.

Still open:

- Create the empty private GitHub repository and push `main`.
- Connect `jhm-spark`, clone the repository, verify its GPU environment, and hand off the work.
- Obtain Mathematics-specific build guidance.
- Build and approve one pilot science deck before batch generation.

## Updates - 2026-10-23 (jhm-spark restart)

- Cloned `markknit/codex_presentation_generation` over SSH into `/home/markk/codex_presentation_generation`. This is the active checkout, replacing the initially requested `/home/codex_presentation_generation` destination.
- Confirmed host `jhm-spark`, branch `main`, clean checkout, and successful fetch with `HEAD` and `origin/main` at `bed61f6` before the continuity edit. No active `HANDOFF_*.md` was found.
- Re-read the project controls and repository continuity skills. Rigor remains High; no generation or release gates have changed.
- Re-ran the verification scripts with `python3` after the documented `python` commands failed. Repository validation passed with 425 source files (340 DOCX and 85 JSON) and three PPTX templates.
- Verified NVIDIA GB10 detection, driver `580.178.04`, compute capability `12.1`, 20 CPUs, and 121 GiB system RAM. PyTorch is absent; CUDA execution is not verified.
- Confirmed LibreOffice/soffice, Node, FFmpeg, Git, and Python 3.12.3 are available. Native PowerPoint and Presenter View validation remain required on a suitable review host.
- Corrected the Active Threads and workflow environment table: the repository exists and this session is running on `jhm-spark`. Updated documented Linux verification commands to `python3`.
- No decks were generated or approved, and no push was performed.

Still open:

- Save or confirm this checkout as the matching Codex project and verify automatic discovery of the repository skills.
- Select and validate the GPU applications needed by the chosen pilot; basic CUDA kernel execution is verified.
- Read the full approved manual and selected unit, then build and review one representative science pilot.
- Arrange native PowerPoint/Presenter View and teacher approval before release or batching.
- Obtain approved Mathematics-specific build guidance.

## Updates - 2026-10-23 (Python environment and GPU requirement)

- Created repository-local `.venv` with Python 3.12.3 and installed python-pptx 1.0.2, python-docx 1.2.0, Pillow 13.0.0, and their dependencies. Recorded exact versions in `requirements.txt`; ignored `.venv/` in Git.
- `pip check` passed. Opened all three template decks with python-pptx (21, 21, and 17 slides) and the approved manual with python-docx (127 paragraphs and 10 tables). This verifies library loading, not visual fidelity.
- Compiled a CUDA smoke kernel using `/usr/local/cuda/bin/nvcc -arch=sm_121` and executed it on NVIDIA GB10; the computed result was 42 as expected. Test source and binary are session scratch artifacts outside the repository. Basic CUDA execution is now verified; no PyTorch installation or GPU generation pipeline is claimed.
- User requires GPU acceleration throughout the project. Updated `AGENTS.md`, `WORKFLOW.md`, and `README.md` to require GPU execution for supported processing stages and explicit documentation of CPU-only assembly/conversion; silent CPU fallback is prohibited.
- Calibri still resolves to Carlito locally. No decks were generated and nothing was pushed.

Still open:

- Configure and validate GPU tools for actual pilot asset processing and visual QA.
- Resolve Calibri rendering fidelity, build the representative pilot, and complete native PowerPoint and teacher review gates.
- Confirm saved-project skill discovery and obtain Mathematics-specific guidance.

## Updates - 2026-10-23 (Cell Structure Lesson 1 review pilot)

- User selected Cell Structure Lessons 1–3. Built only L1 as required by the pre-batch pilot gate; L2–3 remain pending native PowerPoint and teacher review plus the other recorded gates.
- Used the approved general manual, examined the 12-lesson storyline/phase sequence and supporting sources, and rendered/inspected the three visual examples. Adapted the supplied L1 example with source-specific corrections rather than redesigning the lesson.
- Draft at `outputs/drafts/Bio_G10_CellStructure_L1_The_Healing_Cut.pptx`: 21 slides, two hidden teacher slides, notes on all slides, 40 minutes. Notes preserve uncorrected initial ideas and a Version 0 drawing; later cellular explanations remain withheld.
- Added the build script, structural validator, CUDA image kernel and Python GPU-preview driver. `scripts/validate_lesson_pilot.py` and repository validation passed. CUDA resized and counted pixels on all 21 final renders. All rendered pages were inspected, with additional repairs to teacher labels, progressive captions and resource-button contrast.
- Recorded source hashes, lesson inventory, slide timing, structural checks and GPU evidence under `qa/`; recorded every correction and open decision in the per-deck build log. CPU-only assembly/conversion/rasterisation/file operations are disclosed; no whole-pipeline GPU or semantic QA claim is made.
- Identified 1.1 versus 1.3 source numbering, generic-manual versus launch-lesson differences, local Carlito substitution for Calibri, untested ARES resources and missing native PowerPoint/teacher sign-off as review items. The pilot is not passed or released.
- Review copies are available in `/home/markk/Documents/Codex/2026-10-23/i-x20/outputs`: PPTX, all-slide PDF, teacher review DOCX with thumbnails and speaker notes, build log, and a ZIP bundle. Draft/render files remain outside Git tracking. No push was performed.

Still open:

- Review the L1 pilot in native PowerPoint and Presenter View, resolve build-log decisions and font/ARES checks, and obtain teacher approval.
- After all pilot gates pass, generate Cell Structure L2 and L3 individually using V2 sources, not uncorrected example content.
- Confirm saved-project skill discovery and obtain Mathematics-specific guidance.

## Updates - 2026-10-23 (Lessons 2–3 draft continuation)

- After delivery of L1, the user explicitly instructed “Proceed with lessons 2-3”. Applied that as a limited exception to the pre-generation pilot wait for these drafts. The pilot has not been marked approved; release gates and Mathematics restrictions remain in effect.
- Built separate editable Cell Structure drafts: L2 What Is a Cell? (21 slides, 80 minutes) and L3 Prokaryotic vs. Eukaryotic Cells (20 slides, 40 minutes). Each has hidden teacher slides 2–3 and complete notes in the required order.
- Preserved the V2 kitchen analogy, offline scientist reading and evidence table, 12-card sort, CER, board updates, model Version 1 and comparison add-on, and all five L3 cold-call questions. Diagrams are editable PowerPoint shapes/labels. Build logs list every content/timing correction and source/manual exception.
- Checked limited scientific corrections against OpenStax and CDC: shared ribosomes, bacterial DNA/nuclear envelope, cell walls and category exceptions, E. coli strain distinction, and the limits of the visual evidence. References are in the build logs; no independent teacher science approval is claimed.
- Both generic structural checks and source-inventory validation passed. Rendered and inspected all 41 new slides, repaired diagram markers/label wrapping, and processed all 41 with the CUDA preview/pixel tool on GB10. Final note-only corrections preserved identical visible slide XML; per-deck GPU reports include the hashes.
- Added reproducible build, validation and packaging scripts. Updated the unit inventory to record three built drafts rather than two deferred lessons. Drafts, PDF renders, print sheets and notes remain out of Git; build logs, source manifests, validation and GPU evidence are tracked.
- Packaged all three PPTX drafts, all-slide PDFs, a combined teacher review document, L2/L3 print sheets, build logs and QA evidence in `/home/markk/Documents/Codex/2026-10-23/i-x20/outputs/CellStructure_Lessons1-3_Drafts.zip`. No push or release.

Still open:

- Teacher/source-owner review of all three decks and all logged corrections; resolve 1.1/1.3 numbering and manual/source exceptions.
- Native PowerPoint/Slide Show/Presenter View, licensed Calibri fidelity and ARES link/content/offline checks.
- Teacher sign-off before release or further generation beyond the explicitly authorised L2–3 continuation.
- Saved-project skill discovery and approved Mathematics guidance.

## Updates - 2026-10-23 (GitHub push and Windows handoff)

- User explicitly requested committing and pushing the completed work, followed by Windows sync commands. This authorises transporting these three review drafts to the repository; it does not establish teacher approval or classroom release.
- Confirmed `main` was clean and four commits ahead of `origin/main` after fetching; no remote commits were missing locally.
- The working drafts were intentionally ignored. Added `outputs/review/CellStructure_Lessons1-3_Drafts.zip` and its README as a tracked handoff snapshot so Windows receives the presentations, previews, notes, print sheets, logs and QA evidence when pulling.
- Verified the archive CRC and all three PPTX hashes against their current structural validation reports. The snapshot README records its SHA-256 and review status. The generators, source data and original approval gates remain intact.
- Prepared the snapshot and continuity documentation for the requested commit/push. Confirm current remote synchronisation with Git status/fetch; this entry is written before the push result is known.

Still open:

- Pull `main` on Windows and extract the review snapshot into a fresh directory.
- Complete native PowerPoint/Presenter View, Calibri, ARES, source-owner and teacher reviews before release.

## Updates - 2026-10-23 (Lesson 6 practical pilot extension)

- User requested adding L6 from the same Cell Structure sub-strand to the pilot. Added this selected draft; did not generate L4–5 or imply those prerequisites are taught by the pilot package.
- Startup checks found clean `main` synced to GitHub at `a7e2d0e`; source inventory and NVIDIA GB10 checks passed. High rigor and the existing review gates remain in force.
- Read the complete approved general manual and rechecked V2 L6 and the L6 example against the already reviewed full unit storyline/supporting sources. Built the 80-minute onion microscopy pilot: 22 slides, teacher-only 2–3, five-rule safety slide, real-observation task, cell-size estimate with mm/μm units, CER, board evidence vote, model revision and next-lesson prediction.
- Corrected example omissions and science/pedagogy issues in a per-deck build log: missing cell measurement, unresolved separate cell-membrane visibility, early chloroplast answer, overgeneralised light/storage statements and the distinction between real and schematic evidence. Flagged no-goggles/improvised-stain source fallbacks and missing chemical concentration for qualified local review; no new formulation or replacement practical was invented.
- Structural validation passed at 80 minutes. All 22 slides rendered and visually inspected, with full-size checks of the material list, reasoning and comparison illustration. CUDA processed every preview; teacher, science, risk assessment and native PowerPoint approval remain open.
- Added the L6 builder and blank individual observation sheet. Extended the existing packager with explicit lesson selection, preserving its original three-lesson default. The expanded pilot contains L1/2/3/6 (84 slides), all-slide PDF previews, full teacher notes, printable tasks, build logs and QA evidence.
- Prepared the expanded snapshot under `outputs/review/CellStructure_Pilot_Lessons1-2-3-6_Drafts.zip` for the established repository/Windows handoff, preserving the earlier L1–3 snapshot. Individual deliverables are also in the chat outputs folder. The requested pilot extension continues the prior commit/push review handoff; it is not classroom release.

Still open:

- Qualified teacher approval of the L6 chemical specification, risk controls, source fallbacks, equipment trial, calibration, visibility and practical timing.
- Teacher/source-owner review of the selected pilot, numbering decisions, ARES checks, Calibri and native PowerPoint/Presenter View.
- Obtain Mathematics guidance and verify saved-project skill discovery.


## Updates - 2026-10-24 (Reference-informed redesign and Lesson 4 transfer test)

- Applied the user's new quality feedback as an explicit request for selected review drafts L1/L2/L6 plus L4, before external pilot sign-off. The user described prior samples as technically correct but weak for engagement, graphics and explanation; this is not teacher/classroom approval.
- Startup verification found `main` clean and synced to `origin/main` at `35ed666`; source inventory and GB10 checks remained aligned. Rigor is High. Re-read the project controls/general manual and reviewed the V2 L4 sequence alongside the already reviewed full unit. No unexpected host/source drift was found.
- Rendered and inspected all 73 pages of the newly selected style references (L1 21, L2 28, L6 24). Recorded source hashes. Derived a reusable visual grammar rather than copying their lesson art or slide XML; retained the existing institutional theme/logos.
- Rebuilt separate review decks: L1 21 slides/40 minutes; L2 25/80; new L4 37/80; L6 27/80. Added original Amina, kitchen, farm and microscope contextual illustrations with exact built-in imagegen prompts and provenance. Scientific diagrams, labels, connectors and tables are editable native PowerPoint objects. Prompt/reveal pairs, practical recording stages, timers and clear student actions replace the earlier uniform-card approach.
- L4 exercises the shared frame/diagram/detail components on the nine source farm mappings. Recorded analogy limits, non-universal plant/chloroplast claims, conventional TEM distinctions, the source-permitted diagram-only route and source/manual task/timing decisions. No actual EM set or pupil results are fabricated. Retained and rechecked the V2 kitchen mapping and previous scientific/practical corrections.
- Structural/note-order/bounds/font/timing checks passed for all four. PDF text retention, nine L4 function reveals and L6 observation-before-comparison/warning-number checks passed. All 110 slides were rendered, inspected and processed through CUDA; full-size reviews repaired diagram label endpoints, organelle placement, contrast and spacing. The parameterised frame and speaker-note construction were also exercised with a scratch fixture. Automated checks do not prove science, teaching effectiveness or native PowerPoint fidelity.
- Packaged individual PPTX/full PDFs, a 17-page quick review, four teacher-note documents, L2/L4 reference sheets, L4 blank tasks, L6 blank observation record, design guide, image prompts, logs and QA into `CellStructure_Lessons1-2-4-6_v2_Review.zip` in `/home/markk/Documents/Codex/2026-10-23/i-x20/outputs`. CRC and deck hashes were checked. Generated drafts/renders remain ignored; source assets, scripts, logs and evidence are tracked locally. Previous snapshots are preserved. No v2 push or classroom release is claimed.
- A final font audit found inherited Aptos in the separate notes-master theme. Normalised notes paragraph/run and Latin theme fonts to Calibri. Verified every notes run and proved all visible slide XML/relationships/media unchanged, preserving the rendered-review evidence. See `qa/CellStructure_v2_notes_font_check.json`.
- GPU evidence covers every slide and all four illustration assets. Hosted imagegen device/model/seed are not exposed. CPU-only PowerPoint/vector/document assembly, conversion, rasterisation, encoding/file layout and packaging are disclosed. Calibri is specified; local previews still substitute Carlito.

Still open:

- User comparison of the redesigned L1/L2/L6 and transfer L4 against the new references, especially engagement, explanation clarity and diagram usefulness.
- Native PowerPoint/Slide Show/Presenter View, exact Calibri, ARES offline/content and teacher/source-owner decisions before release.
- L6 local chemical/risk/PPE/waste/equipment/calibration/visibility checks; L4 optional authenticated EM provision and real-class timing.
- New repository/Windows snapshot or push if requested; obtain Mathematics guidance and confirm saved-project skill discovery.


## Updates - 2026-10-24 (Authorised GitHub version 2 handoff)

- User explicitly requested pushing to GitHub. Live fetch found clean `main` one commit ahead of `origin/main`: redesign source/assets commit `b5c9298`, with no incoming changes.
- Added `outputs/review/CellStructure_Lessons1-2-4-6_v2_Review.zip` so Git transport includes the actual four presentations and review materials. Verified archive CRC and each of the four PPTX SHA-256 values against its included passing validation report. Snapshot size 40,776,705 bytes; SHA-256 `6b379f4699bb708da5aee7c90e8dae205617a9a74e60378fbf68e62076da7ced`.
- Updated snapshot README, root README and workflow to identify the current handoff and fresh-folder Windows extraction. Previous snapshots and all pending review gates remain intact. This authorises repository transport, not classroom release.

Still open:

- Windows pull/extraction and the previously recorded user/teacher, native PowerPoint, ARES/font and L6 practical-readiness checks.

## Updates - 2026-10-24 (Complete Cell Structure draft continuation)

- User explicitly requested the remaining presentations for this sub-strand. Applied this as draft-generation authorisation for L3, L5 and L7–12 before external pilot review; no release, teacher approval or broader-subject authorisation is inferred. Startup checks found clean/synced `main` at `8841929`, unchanged 425-file source inventory and verified GB10/CUDA environment. Re-read controls, full-unit source phases/supporting assessment and general-manual requirements.
- Added eight v2 drafts: 166 slides, bringing all twelve to 276 slides and 840 scheduled minutes. The prior four v2 deck bytes are unchanged. L3 now follows the revised style; earlier snapshots remain preserved. Shared editable specialised-cell diagrams carry observations into explanations and model revision; repeated source-specific tasks/times are retained in notes.
- Logged source/science decisions per lesson and in `content/cellstructure_v2/REMAINING_DECISIONS.json`. L7 uses the source-permitted prepared-slide route, preserving observation before the reference comparison. L8 supplies credited published blood-smear and fluorescent rat neural-tissue images (actual provenance/technique disclosed), corrects sperm-as-healing, and separates image morphology from sickling background. L9 uses hypothetical stomatal states, not invented geographical measurements; L10 uses schematic hierarchy evidence rather than fabricated microscopy. L12 corrects fibrin/ribosome, DNA/centrioles and universal-genome claims.
- All new slides rendered and visually inspected, including hidden teacher pages. Fixed timer-caption overlaps; checked full-size diagram labels/hierarchy. Structural/font/note-order/timing/CRC and complete-unit PDF word-retention checks passed. CUDA processed 166 new slide previews and two published assets without CPU fallback. Calibri specified, Carlito preview substitution and CPU-only operations disclosed. `pip check`, script compilation, repository inventory and whitespace checks passed.
- Supplied practical records, blank comparison/organiser/poster sheets, actual L9 15-card materials, L10 two-sided evidence card, and a source-adapted five-section final assessment/corrected teacher guide. Preserved rubric criteria/bands; corrected route/science/visibility assumptions and left original inputs untouched. All 12 new print documents rendered (28 pages initially); source rubric overflow was repaired, and two corrected rubric pages were rendered/inspected. PDF text retention passed; print QA includes final DOCX hashes.
- Complete review files are saved under `/home/markk/Documents/Codex/2026-10-23/i-x20/outputs/CellStructure_Complete_v2`; ZIP is `/home/markk/Documents/Codex/2026-10-23/i-x20/outputs/CellStructure_Complete_Lessons1-12_v2_Review.zip`. Exact final archive size/hash are recorded in `qa/CellStructure_complete_v2_package.json`. These are local deliverables; generated decks/renders remain ignored. Source/assets/scripts/logs/QA/control updates are committed locally; no new push.

Still open:

- Native PowerPoint/Slide Show/Presenter View, exact Calibri, ARES link/content/offline and teacher/source-owner review before classroom release.
- L6 local stain/risk/PPE/waste/calibration/visibility and L7 prepared-slide specimen approval; L9 seedling preparation and L10 optional authentic microscopy provision.
- Schedule supervised follow-up for final assessment Sections 4–5; 25 minutes in L12 begins Sections 1–3. Review adapted paper/key and all logged source decisions, including 1.1/1.3 numbering.
- New repository/Windows snapshot transport if requested; Mathematics guidance and saved-project skill discovery remain open.

## Updates - 2026-10-24 (Authorised complete-unit GitHub handoff)

- User explicitly instructed “OK. Push and commit all of it.” Live fetch found clean `main` one commit ahead at `224f210`, with no incoming changes.
- Added the actual complete twelve-lesson review ZIP to `outputs/review` for Git transport, preserving all earlier snapshots. Working drafts, render caches and `.venv` remain ignored; all source/assets/builders/logs/QA already reside in `224f210`.
- Verified the immutable 79,941,881-byte archive against recorded SHA-256 `27c8518111623de7ea420c1b6d6e3574d1442f91666dc75e5677043acdf7ea24`, CRC, every manifest member hash and all twelve PPTX hashes against passing structural reports. Updated snapshot README, package transport record, root README and workflow with the complete handoff and Windows extraction.
- Pushed source commit `224f210` and snapshot commit `ef91839` to `origin/main`. `git ls-remote origin refs/heads/main` matched local HEAD at `ef91839`, and the checkout was clean after push. This records repository transport, not native PowerPoint or teacher approval. GitHub accepted the 76.24 MiB review ZIP with its advisory large-file warning.

Still open:

- Windows pull/extraction and the previously recorded native PowerPoint/Presenter View, font/resources, teacher/source-owner and practical-readiness checks before classroom release.

## Updates - 2026-10-27 (Chemicals of Life review drafts)

- The user requested all Grade 10 Biology 1.2 presentations in the 1.1 style, authorising these six drafts before the earlier pilot's external approval; no release or push was authorised. Startup verification passed the repository inventory (425 sources, three templates), confirmed `jhm-spark`, `main` and NVIDIA GB10. An existing untracked extracted Cell Structure review folder was identified; the user directed continuation and it was left untouched.
- Built six individual 80-minute decks (20, 17, 19, 19, 19 and 17 slides; 111 total). Reused the phase colours, teacher-only slides, notes, footer and editable PowerPoint diagrams/tables. Used two generated contextual illustrations, with prompts and hashes in `assets/chemicals_of_life/provenance.json`. Source and per-deck changes are tracked in the manifest and build logs.
- The six structural checks and selected reveal/sequence/hash checks passed. All 111 final slide renders and 12 printable pages were inspected and processed by CUDA on GB10; PowerPoint/DOCX assembly, PDF conversion/rasterisation, image encoding and package layout are CPU-only. Calibri is specified but local previews use Carlito; the separate notes runs were checked for Calibri. These checks do not establish external science, safety or teaching approval.
- Added editable case/cards, blank practical records, role cards, an adapted five-part student assessment and teacher review notes. The local review archive has six PPTX, slide PDFs, support documents, logs and QA; CRC and all 51 manifest hashes verified. The adapted assessment requests actual observations and corrects unsupported assumptions; the source teacher key and rubric still need teacher adaptation.
- Identified open source-owner questions: no clear vitamin C or catalase investigation in the six-lesson sequence despite relevant outcome/value statements; supplied case provenance is not independently established; incomplete element-card information; and the full assessment needs supervised time outside the allocated Lesson 6 writing segment. L5 pooled saliva is not endorsed, and all practical safety and equipment decisions remain local teacher decisions.

Still open:

- Native PowerPoint/Slide Show/Presenter View, exact Calibri, ARES, science, pedagogy, teacher and source-owner reviews before release; user comparison with 1.1 style.
- Teacher-approved flame, reagents, concentrations, allergy, human-specimen, controls, equipment, waste and emergency plans. No fabricated results or unapproved replacement practicals.
- Review the assessment and original marking guide/rubric against the actual approved practical route, and resolve the unit coverage gaps. New 1.2 review drafts are local and ignored by Git; cross-host transport requires an explicit authorised handoff.

## Updates - 2026-10-27 (Authorised Chemicals of Life GitHub handoff)

- The user requested committing and pushing the new output. Restart verification found `main` one commit ahead of `origin/main` at `3ba4579`, with no incoming changes after fetch; the source inventory validation passed and the previously identified untracked Cell Structure extraction was left untouched.
- Copied the unchanged 7,052,980-byte local review ZIP to `outputs/review/ChemicalsOfLife_Lessons1-6_Review.zip`. Verified SHA-256 `8ada1ebdb85aa080b12f115a98567e9515b3b334345dc08bf0c007f362587495`, archive CRC, all 51 manifest member hashes and all six PPTX hashes against passing structural reports. Updated review README, root README and workflow with the authorised transport and fresh-folder extraction instructions.
- Pushed source commit `3ba4579` and snapshot commit `3e0b8c8` to `origin/main`. `git ls-remote origin refs/heads/main` matched local HEAD at `3e0b8c8` after the push; the existing untracked Cell Structure extraction remains untouched. The included files remain review drafts and all teacher, source-owner, practical-safety, ARES and native PowerPoint gates remain open.

Still open:

- Pull on the review host and extract to a fresh folder. Review and approval gates for classroom release remain unchanged.

## Updates - 2026-10-27 (Continuity update)

- Re-read the active status, checked Git status, diff and recent commits, and rechecked the Chemicals of Life review ZIP SHA-256: `8ada1ebdb85aa080b12f115a98567e9515b3b334345dc08bf0c007f362587495`. `git ls-remote origin refs/heads/main` matched local `b1d5515` before this update; no tracked changes were pending.
- Refreshed the GitHub and Windows handoff rows to include both units. The previously identified extracted Cell Structure review folder remains untracked and untouched. No new decks, approvals, or source decisions were recorded during this checkpoint.

Still open:

- Extract the review snapshots on the review host and complete native PowerPoint/Presenter View, teacher/source-owner, practical-safety, ARES and other recorded release checks. Resolve the Chemicals of Life source-coverage and assessment decisions; Mathematics guidance remains blocked.
