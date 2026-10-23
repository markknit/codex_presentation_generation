# Project status

Last updated: 2026-10-23

## Active Threads

| Workstream | Status | Evidence or next gate |
| --- | --- | --- |
| Repository scaffold | Done | Git repository initialised on `main` at `C:\Users\MRKni\OneDrive\codex_presentation_generation`; validation passed and initial commit `8119d93` contains 443 files. |
| Continuity skills | In progress | `restart` and `update` are installed in `C:\Users\MRKni\.agents\skills` and included under `.agents/skills`; verify discovery on the next local turn and on `jhm-spark`. |
| Approved instructions | Done | General science manual selected. Cells-specific manual excluded. |
| Visual examples | Done | Three example PPTX files identified and rendered for inspection: 21, 21, and 17 slides. |
| V2 source inventory | Done | 425 files total: 340 DOCX and 85 JSON across 85 units. |
| GitHub repository | Blocked | `origin` is configured as `https://github.com/markknit/codex_presentation_generation.git`, but the repository does not exist. GitHub CLI is unavailable and the browser-control helper failed before opening GitHub. Create the empty private repository, then push `main`. |
| `jhm-spark` connection | Blocked | The host is not currently available to this Codex app. Configure SSH, install and authenticate Codex on the host, then save the matching project. |
| GPU verification | Blocked | Run `python scripts/verify_environment.py` on `jhm-spark`; confirm `nvidia-smi`, GPU model, driver, CUDA access, and available RAM. |
| Science pilot deck | Not started | Build one representative lesson only after the repository is on `jhm-spark`; complete all quality gates before batching. |
| Mathematics decks | Blocked | The approved science manual states that Mathematics has separate guidance. Add and approve the Mathematics manual before generation. |

## Known Issues and Lessons Learned

- Project continuity must live in the repository. Host-local skills alone do not travel to `jhm-spark`, so the two continuity skills are checked into `.agents/skills`.
- A successful package check does not establish visual quality, native PowerPoint behaviour, factual accuracy, practical realism, or safety. Every release needs rendered inspection, a native PowerPoint check, and teacher approval.
- The three examples establish a clean 16:9 visual system with Calibri, phase colours, large student-facing prompts, hidden teacher slides, persistent footers and logos, and restrained diagrams. New decks should reuse this language without copying lesson-specific content.
- Mathematics source files are present, but the science manual is not authoritative for Mathematics.

## Updates - 2026-10-23

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
