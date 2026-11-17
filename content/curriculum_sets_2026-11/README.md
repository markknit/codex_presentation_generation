# Paused curriculum draft checkpoint

Paused by the user's usage rule on 16 November 2026 (17 November UTC).
Context remaining reached **4.62%** at 01:33:16 UTC; weekly account remaining
was 47%. Context compaction subsequently reset its displayed percentage.
That reset does not authorise continuing: await the user's resume instruction.

## Saved files and counts

Local output index: `outputs/drafts/curriculum_sets_2026-11/README.md`.
Folders: curriculum → strand → sub-strand → artifact type.
All 43 sub-strand folders exist; the inventory contains 514 lessons and 430
archive-verified source members. Three preserved pilot PPTX files plus seven
new PPTX files exist; **504 lessons remain unbuilt**.

The seven new files have automated passes, not completed visual reviews:

| Module | Lessons | Slides | Final print pages |
| --- | --- | ---: | ---: |
| General Science 1.1 Introduction | 2–7 | 96 | 95 |
| Essential Mathematics 1.1 Real Numbers | 2 | 17 | 14 |

The General Science Introduction now has seven draft files / 115 slides /
280 minutes including its preserved L1 pilot. No new unit review ZIP was made.
Existing pilot paths, deck hashes and the Mathematics pilot review ZIP remain
unchanged. Native PowerPoint, teacher/source-owner and classroom gates are open.

## Resume at final visual inspection

Do not rebuild completed decks merely to restart. Use the current final renders
under `qa/renders/curriculum_sets_2026-11/<module>/<deck-name>/`. The per-deck
`*_checks.json` files identify every final print document, page count and hash.

- General Science L2: earlier 17-slide inspection preceded the final title/
  summary anchor addition; check those final pages and the caption/timer fix.
  All teacher pages were inspected. Check the final two reflowed student pages.
- General Science L3: earlier 17-slide inspection preceded the final anchor
  addition; check final title/summary. All 15 final print pages were inspected.
- General Science L4: earlier 17-slide inspection preceded final anchor and
  Predict input repair; inspect those final changes. All 15 print pages remain.
- General Science L5: all 17 final slides inspected, including voluntary
  question sharing/private career choice. All 18 print pages remain.
- General Science L6: earlier 17-slide inspection preceded final anchor
  addition; inspect final title/summary. All 15 print pages remain.
- General Science L7: all 11 final slides inspected, including the independent
  assessment routine. All 18 print pages remain, including six original prompt
  pages. Do not disclose private keys before collection.
- Essential L2: all 17 final slides and 14 print pages remain to inspect.

Until those checks finish, keep the seven inventory rows as
`automated_pass_visual_pending`. Only after actually inspecting every final
slide and print page, record each review with:

```bash
.venv/bin/python scripts/review_package_curriculum_set.py review gensci_1_1 2 --finding 'Describe actual final inspection and any remaining limits.'
```

Use the corresponding lesson/module for each inspected lesson. Package a
sub-strand only after confirming its intended lesson set is fully reviewed:

```bash
.venv/bin/python scripts/review_package_curriculum_set.py package gensci_1_1
```

## Continue generation after review and explicit resume

Read repository `restart` instructions first. Source-specific specifications
are ready for Essential Real Numbers L2–8, Core Real Numbers L2–10 and General
Science Introduction L2–7. Essential L2 already exists; the next unbuilt
initial-unit lesson is Essential L3 (Core L2 is also authored).

```bash
python3 scripts/session_usage.py --guard
.venv/bin/python scripts/build_curriculum_set_lesson.py essmath_1_1 3
.venv/bin/python scripts/render_check_curriculum_set.py essmath_1_1 3
```

Inspect actual slide and print renders before recording review. Other source
units require full-unit reading and authored source-specific specifications.
Never use the science manual as Mathematics pedagogy authority. Preserve exact
source activity order, access requirements and assessment independence.

`--support-only` regenerates support documents from an existing PPTX/manifest;
any changed document requires fresh print render checks and inspection. Do not
mark an old render valid after changing its source file.

Generated outputs and render caches remain ignored by Git. Control documents,
specifications, scripts, QA and logs are tracked. Existing untracked Biology
review extraction and five General Science pilot QA files are preserved.
