# November Mathematics review pilots

User-approved scope: Essential Mathematics 1.1 Real Numbers Lesson 1 and Core
Mathematics 1.1 Real Numbers Lesson 1 only. See `MATHEMATICS_PILOT_GUIDANCE.md`.
The reviewed November Mathematics sources control content and teaching sequence.
The science manual is not Mathematics pedagogy guidance.

Local deliverables: `outputs/drafts/curriculum_pilots_2026-11/`.
Each pilot includes a PPTX, all-slide PDF (including hidden teacher slides),
editable student task with blank record, student PDF, and private teacher notes
in DOCX/PDF. The local `Mathematics_Lesson1_Pilots_Review.zip` includes both
pilots, logs, guidance and QA. These working files remain ignored by Git.

Rebuild one at a time, then render and check:

```bash
.venv/bin/python scripts/build_math_pilots.py essential
.venv/bin/python scripts/render_curriculum_pilots.py EssMath
.venv/bin/python scripts/build_math_pilots.py core
.venv/bin/python scripts/render_curriculum_pilots.py CoreMath
.venv/bin/python scripts/check_math_pilots.py
.venv/bin/python scripts/package_math_pilots.py
```

The shared frame/document utilities live in `build_curriculum_pilots.py` and
`lesson_visuals.py`. Only the first script's `science` command builds General
Science; the Mathematics rebuild commands do not modify that draft.
Current source files are read through `final_curriculum_outputs` and verified
against the named delivery archives, including Core's 15 November rubric fix.

No native PowerPoint, teacher approval, classroom release or wider Mathematics
generation follows from structural/CUDA checks. Local previews use Carlito as
a Calibri substitute. CPU and GPU operations are disclosed in each build log.
