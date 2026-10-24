# Current review snapshot — Cell Structure version 2

`CellStructure_Lessons1-2-4-6_v2_Review.zip`

The user explicitly requested pushing the redesign to GitHub on 24 October 2026. This tracked snapshot transfers the actual revised presentations as well as the reusable generator/assets in source commit `b5c9298`.

Contains separate L1/L2/L4/L6 PPTX drafts (21/25/37/27 slides; 40/80/80/80 minutes), full PDFs, a 17-slide quick preview, teacher notes, printable tasks, design guide, exact imagegen prompts, build logs and QA evidence. Slides 2–3 are hidden in each Slide Show. These are review drafts, not a classroom release; recorded native PowerPoint/teacher and practical-readiness checks remain open.

Archive CRC and all four deck hashes were verified against their included passing validation reports before committing. Size: 40,776,705 bytes.

SHA-256: `6b379f4699bb708da5aee7c90e8dae205617a9a74e60378fbf68e62076da7ced`

After pulling main, extract into a fresh folder so earlier review annotations remain intact:

```powershell
git pull --ff-only origin main
Expand-Archive -Path ".\outputs\review\CellStructure_Lessons1-2-4-6_v2_Review.zip" -DestinationPath ".\outputs\drafts\CellStructure_v2_Review"
```

The earlier snapshots below are preserved for history.

---

# Cell Structure pilot — Lessons 1, 2, 3 and 6

Current expanded snapshot: `CellStructure_Pilot_Lessons1-2-3-6_Drafts.zip`.

The user requested adding Lesson 6 to the same pilot after the established commit/push Windows handoff. This review snapshot contains four separate PPTX drafts (84 slides total), all-slide PDFs, full teacher notes, printable tasks including a blank L6 observation sheet, build logs and QA evidence. It does not add Lessons 4–5 or imply they have been taught; they remain L6 prerequisites.

L6 has 22 slides / 80 minutes. Structural validation and rendered inspection passed, with CUDA preview/pixel processing. Local practical safety, chemical product/concentration, PPE/source fallbacks, equipment trial/calibration, realistic visibility, teacher/science, native PowerPoint, ARES and font approval remain open. It is not a classroom release.

Extract into a fresh directory to preserve any review annotations. Working drafts/renders stay ignored. The prior L1–3 snapshot below is preserved for history.

Expanded snapshot SHA-256: `31bbdd5b8827106a5ea914cba4d9b599308f5a4b5a7626dc9daeaeb3940d8202`

---

# Cell Structure Lessons 1–3 — Windows review snapshot

This tracked ZIP contains three separate draft PPTX files, all-slide PDF previews, the combined teacher review document, printable activity sheets, build logs and QA evidence. The user explicitly requested committing and pushing this package for Windows sync on 2026-10-23. This is an exception for sharing these review drafts, not approval or release.

Source commit before packaging: `75adc4a`. L1: 21 slides / 40 minutes; L2: 21 / 80; L3: 20 / 40. Teacher slides 2–3 are hidden in each deck. All three still require native PowerPoint/Presenter View, teacher/source-owner, Calibri and ARES review.

`outputs/drafts` and render intermediates remain ignored. This ZIP is an intentional, reviewable handoff snapshot; do not mark the decks final or move them to `outputs/final` without sign-off.

In PowerShell, from an existing Windows checkout on main, run `git pull --ff-only origin main`, then extract this ZIP into a new review directory. Commit or stash any local tracked changes before pulling. Avoid overwriting an extracted copy with edits; extract a fresh copy instead.

SHA-256: `b513c40dacf104b042dadae70fff3f7a52465a4055b87191b28562742bcaf9b2`
