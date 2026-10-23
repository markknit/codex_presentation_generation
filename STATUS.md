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
| GPU verification | In progress | `python3 scripts/verify_environment.py` succeeded: NVIDIA GB10, driver `580.178.04`, compute capability `12.1`, Linux aarch64, 20 CPUs. `free -h` reported 121 GiB RAM, about 57 GiB available at inspection. GPU memory total was reported as N/A; PyTorch is absent, so CUDA execution and application compatibility remain unverified. |
| Science pilot deck | Not started | Repository is now on `jhm-spark`. Read the complete approved science manual and chosen unit, inspect example decks, then build one representative lesson and complete all quality gates before batching. |
| Mathematics decks | Blocked | The approved science manual states that Mathematics has separate guidance. Add and approve the Mathematics manual before generation. |

## Known Issues and Lessons Learned

- Project continuity must live in the repository. Host-local skills alone do not travel to `jhm-spark`, so the two continuity skills are checked into `.agents/skills`.
- A successful package check does not establish visual quality, native PowerPoint behaviour, factual accuracy, practical realism, or safety. Every release needs rendered inspection, a native PowerPoint check, and teacher approval.
- The three examples establish a clean 16:9 visual system with Calibri, phase colours, large student-facing prompts, hidden teacher slides, persistent footers and logos, and restrained diagrams. New decks should reuse this language without copying lesson-specific content.
- Mathematics source files are present, but the science manual is not authoritative for Mathematics.
- Host handoffs can leave control documents stale. Run `/restart` against live Git, paths, and tools on each host, then reconcile both `STATUS.md` and the environment table before generation. Historical session entries describe their original checkpoints, not current blockers.
- On `jhm-spark`, use `python3` (Python 3.12.3); the `python` command is absent. GPU detection through `nvidia-smi` does not prove CUDA application compatibility.
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
- Validate a compatible CUDA application/toolchain before relying on GPU-assisted work.
- Read the full approved manual and selected unit, then build and review one representative science pilot.
- Arrange native PowerPoint/Presenter View and teacher approval before release or batching.
- Obtain approved Mathematics-specific build guidance.
