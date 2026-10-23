# Lesson 1 pilot build log

Date: 2026-10-23. Status: REVIEW DRAFT; not approved for release or batching.

Requested series: Cell Structure, Lessons 1–3, one PPTX per lesson. Only Lesson 1 has been built. Lessons 2–3 await the pilot gates in AGENTS.md, including native PowerPoint and teacher review. This is a deliberate gate, not a completed three-lesson series.

## Sources and scope

V2 lesson sequence and structured data, Summary Table, Final Explanation and Teacher Key in inputs/v2/Biology/SS1.1_Cell_Structure; complete approved general science manual; the three supplied example decks. Checksums are in qa/Bio_G10_CellStructure_manifest.json. The whole 12-lesson storyline and phase sequence were examined to protect later discoveries. Only the launch lesson is adapted here. The Lesson 1 example supplies the visual layout, logos and existing finger illustrations; it does not override V2 content.

## Changes, decisions and open owner checks

| Lesson / slide | Source or reference issue | Draft treatment and reason | Review status |
| --- | --- | --- | --- |
| L1 / all | Folder, META and lesson labels say 1.1; the UNIT/overview says Sub-Strand 1.3. | Use Cell Structure without a numerical sub-strand claim. Preserve input names and log the conflict; do not silently renumber curriculum content. | Source owner decision needed. |
| L1 / 1, 4–7, 9–17 | Example slide notes contain extra opening minutes, overlapping sequence timing, and ranges. | Set one numeric TIME per slide; absorb the opening into Predict. Phase totals 5 + 10 + 7 + 10 + 5, plus Summary 3 = 40 minutes. Preserve every activity and the full 2-minute silent write, 90-second pair talk and 3-minute baseline drawing. | Teacher to confirm realistic pacing. |
| L1 / 2 | Example routine says to correct ideas in Explain; V2 L1 explicitly gives no causal answers. | Clarify the launch-lesson exception. Do not confirm cell mechanisms today. | Teacher to accept source-specific exception to generic routine. |
| L1 / 3 | Example labels CK-12 as best match and optional videos; actual ARES content is not locally verified and may spoil later learning. | Preview-first/teacher preparation only for CK-12; do not show anatomy/organisation resources today. Copy source URLs exactly, require preview, use narrated drawings as the offline fallback. | Links, offline availability and content untested. |
| L1 / 4 | The manual puts the driving question on the unit map; V2 formally introduces it after pupils post their own questions. | Map says the full question will be revealed after notices/wonders. Display the full source wording on slide 19. Preserve the source reveal sequence. | Teacher to accept source/manual conflict resolution. |
| L1 / 5 | Example lacks key-word definitions. | Add process vocabulary only: observe, predict, model. Do not supply cell anatomy before pupils draw their baseline. | Teacher review. |
| L1 / 7, 12–13, 15–16, 18–20 | Source includes diagnostic observation/listening but example does not label every check or give a response. | Label existing checks; add LOOK FOR and IF… guidance tied to the source prompts. Do not create a new assessment or a correct baseline diagram. | Teacher review of scaffolding. |
| L1 / 9–12 | Example captions disclose future stages while the pictures are covered. | Unrevealed captions ask What changes next? Reveal stage labels only with their drawings. | Corrected. |
| L1 / 9–12, 18 | Example says about a week / completely healed after a few days. Source narrates a sequence over several days. | Use over several days for the final panel and a notice about visible changes. Explicitly label these as illustrative drawings, not photographs or a fixed healing timetable. Retain the source's two-days stage as part of the story, not a promise. | Teacher review of realism. |
| L1 / 18–20 | Generic manual calls for a DQB evidence vote and a next-lesson prediction. V2 L1 instead establishes notice/wonder notes and an uncorrected Version 0 baseline. | Retain the launch-specific tasks. Do not invent a vote claim or extra written assessment. The model has no exemplar biological answer. | Teacher to resolve/accept these manual/source differences before pilot approval. |
| L1 / 21 | Example ending lacks a visible Next lesson teaser. | Add What is a cell? and retain the source Summary Table key and teacher reflections in notes. | Corrected. |
| L1 / all | Local host lacks Calibri. | Keep Calibri specified in PPTX; LibreOffice previews substitute Carlito. No proprietary font has been fetched. | Exact Calibri rendering needs review on a licensed-font/PowerPoint host. |

## Source coverage

- Predict: Amina in Eastleigh slicing onions; independent notebook ideas, no corrections.
- Observe: 90-second partner sharing, four progressively revealed healing drawings, notebook additions, 3–4 pairs sharing and teacher scribing verbatim.
- Explain: the three source questions, 10-second silent think on the third, source bridging statement; no cellular answer.
- Driving Question Board: one yellow notice and blue wonder per pupil, 3-minute writing, posting in groups, clustering, then formal question and 8-second wait.
- Model Building: Version 0 drawn without a supplied diagram; labels reflect prior knowledge; preserve for later comparison.
- Closure: source Summary Table prompts and notes key; next lesson teaser; teacher reflections.
- Later material deliberately withheld: cell theory, prokaryote/eukaryote comparison, organelle functions, microscopy results and specialised healing-cell explanations.

## GPU use and CPU operations

scripts/gpu_image_ops.cu was compiled with nvcc for sm_121 and invoked through scripts/gpu_visual_qa.py on the GB10. CUDA resizes raster previews and counts non-white/dark pixels for visual-QA signals. Missing CUDA or a failed kernel raises an error; there is no CPU fallback. The report records the detected device and driver. No generative model or external artwork was used.

CPU-only operations: DOCX/JSON reading, python-pptx OOXML assembly, ZIP/XML validation, LibreOffice PDF conversion, Poppler rasterisation, image file encoding, text/label layout and contact-sheet compositing. These are explicitly disclosed; the whole pipeline is not represented as running on the GPU. Human/model visual inspection and teacher judgement are separate from CUDA pixel metrics.

## Validation and review gates

- Structural checks passed: 21 slides, 16:9, slides 2–3 hidden, notes on every slide, one TIME per slide totalling 40 minutes, all authored text specified as Calibri, footer on every slide, formative labels with LOOK FOR and IF… notes, no shapes outside the canvas.
- All slides rendered with LibreOffice, including the two teacher-only slides. All rendered pages inspected; modified teacher labels, resource buttons and progressive captions received additional inspection and repair.
- Raster resizing and pixel counting ran on CUDA for all 21 final pages. These signals do not establish semantics, scientific accuracy, text fit, or PowerPoint compatibility.
- Model/source review checked that L1 remains an inquiry launch. No independent teacher/science approval has been recorded.
- Still required: teacher review of this log and source conflicts, realistic timing and local context; ARES preview/link/offline checks; Calibri fidelity; native PowerPoint open, Slide Show and Presenter View; teacher sign-off.

Do not mark the pilot passed, release it, or generate the remaining two decks until the required gate is satisfied or the user explicitly changes project requirements.
