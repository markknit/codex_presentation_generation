# Project status

Last updated: 2026-10-23

## Active Threads

| Workstream | Status | Evidence or next gate |
| --- | --- | --- |
| Repository scaffold | Done | Checkout on `jhm-spark` at `/home/markk/codex_presentation_generation`, branch `main`; `python3 scripts/validate_repository.py` passed on 2026-10-23. Initial scaffold commit: `8119d93`. |
| Continuity skills | In progress | Repository copies of `restart` and `update` were read and used on `jhm-spark`. Automatic skill discovery in a saved Codex project has not been verified; Windows installation was recorded by the previous session. |
| Approved instructions | Done | General science manual selected. Cells-specific manual excluded. |
| Visual examples | Done | Three example PPTX files identified and rendered for inspection: 21, 21, and 17 slides. |
| V2 source inventory | Done | 425 files total: 340 DOCX and 85 JSON across 85 units. |
| GitHub repository | Done | Cloned via `git@github.com:markknit/codex_presentation_generation.git`; SSH authenticates as `markknit`. `git fetch --quiet` succeeded and `main` matched `origin/main` at `bed61f6` before this continuity update. Repository visibility was not checked. |
| `jhm-spark` connection | Done | Live `hostname` returned `jhm-spark`; Codex commands run locally against `/home/markk/codex_presentation_generation`. Saving this checkout as a Codex project remains unverified. |
| GPU verification | In progress | `python3 scripts/verify_environment.py` succeeded: NVIDIA GB10, driver `580.178.04`, compute capability `12.1`, Linux aarch64, 20 CPUs. `free -h` reported 121 GiB RAM, about 57 GiB available at inspection. GPU memory total was reported as N/A. Compiled CUDA execution is verified. The pilot raster-QA tool now uses CUDA sm_121 for preview resizing and pixel counts on all 21 slides; see `qa/Bio_G10_CellStructure_L1_gpu.json`. No local generative/vision model is configured or claimed. |
| Python authoring environment | Done | `.venv` contains the pinned `requirements.txt` packages; `pip check` passed and all three templates plus the manual loaded successfully. Activate the environment before running authoring tools. |
| Science pilot deck | Awaiting review | Cell Structure L1 review draft built: 21 slides, slides 2–3 hidden, full notes, 40 minutes. Structural validation passed and rendered pages inspected. `qa/Bio_G10_CellStructure_L1_The_Healing_Cut_validation.json` and the per-deck build log record remaining source/manual decisions, font, ARES, native PowerPoint and teacher gates. Draft remains ignored under `outputs/drafts`. |
| Biology Lessons 1–3 | Drafts built; awaiting review | User explicitly instructed Proceed with lessons 2–3 after receiving the pilot, authorising draft continuation before external pilot checks. L1: 21 slides/40 min; L2: 21/80; L3: 20/40. Structural checks passed and all 62 renders inspected with CUDA pixel processing. Native PowerPoint, Calibri/ARES, source-owner decisions and teacher sign-off remain open for all three. |
| Mathematics decks | Blocked | The approved science manual states that Mathematics has separate guidance. Add and approve the Mathematics manual before generation. |

| Windows review handoff | Prepared | User explicitly authorised commit/push of the completed work and review package. Tracked snapshot: `outputs/review/CellStructure_Lessons1-3_Drafts.zip`; its three PPTX hashes match the current validation reports. Drafts are not teacher-approved or released. |

## Known Issues and Lessons Learned

- Git ignores working drafts and renders. For an explicitly requested cross-host review handoff, commit a clearly labelled snapshot under `outputs/review` so a pull actually transfers the presentations; keep approval status and checksums with it.
- Project continuity must live in the repository. Host-local skills alone do not travel to `jhm-spark`, so the two continuity skills are checked into `.agents/skills`.
- A successful package check does not establish visual quality, native PowerPoint behaviour, factual accuracy, practical realism, or safety. Every release needs rendered inspection, a native PowerPoint check, and teacher approval.
- The three examples establish a clean 16:9 visual system with Calibri, phase colours, large student-facing prompts, hidden teacher slides, persistent footers and logos, and restrained diagrams. New decks should reuse this language without copying lesson-specific content.
- Mathematics source files are present, but the science manual is not authoritative for Mathematics.
- Host handoffs can leave control documents stale. Run `/restart` against live Git, paths, and tools on each host, then reconcile both `STATUS.md` and the environment table before generation. Historical session entries describe their original checkpoints, not current blockers.
- On `jhm-spark`, use `python3` (Python 3.12.3); the `python` command is absent. GPU detection through `nvidia-smi` does not prove CUDA application compatibility.
- The Cell Structure source labels disagree: the folder/META/lesson labels say 1.1; the unit overview says 1.3. Keep the numerical sub-strand off the draft and request owner resolution through the build log rather than silently renumbering.
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
