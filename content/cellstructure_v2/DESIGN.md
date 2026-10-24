# Cell Structure visual system, version 2

24 October 2026. Review drafts; no classroom release is claimed.

## What was learned from the new references

The user-selected L1/L2/L6 files in `presentations2` were inspected as complete rendered decks (21, 28 and 24 slides). They set a more useful visual target than the earlier examples: inviting illustrated settings, a recognisable phase routine, prominent questions, visible work modes and timers, more space per instruction, and explanation built through successive questions. Their lesson-specific pictures and slide XML were not copied into these new decks. The existing repository template supplies the theme and institutional logos only. V2 lesson plans remain the authority for tasks and content.

The earlier drafts leaned too heavily on similar text cards. Technical correctness and editable shapes did not ensure student engagement. The redesign uses a hierarchy of story, evidence and explanation visuals, with one main student action per screen. Engagement is an intended improvement, not a measured learning outcome; user/teacher feedback is the next test.

## Repeatable authoring rules

1. Read the full unit and identify which discoveries must be withheld. Build the evidence-before-explanation sequence first.
2. Write each student screen as one action or one question. Put preparation, grouping, teaching moves, misconceptions and answer keys in notes. Split a compound task into successive screens without increasing its total time.
3. Choose a visual that does instructional work: a scene establishes context; a labelled diagram supports comparison; an enlarged structure makes a function concrete; a process picture clarifies a physical action. A decorative picture is not evidence.
4. Use the shared phase colours, Calibri, 16:9 canvas, navy/white base, simple plain-English titles and consistent footer. Make timers and individual/pair/group instructions visible. Keep teacher orientation and glance slides 2–3 hidden.
5. Use `lesson_visuals.py` components for prompts, steps, diagrams, organelle details, practical stages, boards and notebooks. Reuse the same structure colours and geometry at whole-cell and detail scales. Labels, connectors, tables and science figures are PowerPoint objects.
6. Use original generated raster scenes only for context. Keep scientific diagrams and labels editable and source checked. Do not generate a fake micrograph or describe an illustration as observed evidence.
7. Explain through a prompt/reveal pair: ask for a reason, wait, hear a pupil, then advance to the confirmed function. L4 uses this same pair for all nine source mappings. State analogy limits, especially light capture versus glucose production, and nucleus versus a thinking owner.
8. Preserve pupil ownership: do not show a completed prediction or an expected microscope result early. Accept uncertainty when an observation does not support a definite claim.
9. Verify slide and phase times; render every screen, check contrast and label endpoints, run structural and PDF text checks, then obtain native PowerPoint and teacher feedback. A CUDA report is not a science or visual-quality sign-off.
10. A new topic needs source-specific content, diagrams and science review. This is a reusable component system, not an automatic guarantee that arbitrary lesson text will become a good deck.

## Components and evidence of reuse

| Component | L1 | L2 | L4 (new transfer lesson) | L6 |
| --- | --- | --- | --- | --- |
| Illustrated story/setting | Amina and healing puzzle | Amina and kitchen analogy | Rift Valley maize farm | Microscope and onion |
| Prediction, independent then pair | Initial healing idea | Shared cell features | Blank outline + shared-feature stars | Onion sketch + chloroplast reason |
| Evidence visual | Four progressively revealed stages | Animal, plant and bacterial diagrams | Same plant diagram enlarged into nine details | Wet-mount stages, field-diameter method |
| Explanation scaffold | Three unresolved questions | Theory, comparison and CER | Nine prompt/reveal pairs, function + structure | Location → light → photosynthesis → role |
| Persistent model/board | Version 0; notice/wonder | Version 1; required core labels | Version 2; nine structures and two sentences | Evidence-based revision; future prediction |

`build_cellstructure_v2.py` holds lesson-specific teaching sequences; `lesson_visuals.py` holds reusable layout and drawing components. Existing L1/L2/L6 notes are stored as source-labelled JSON and are carried forward with explicit per-screen timing/segment changes. The filename “reviewed_notes” means inherited builder-reviewed notes, not teacher approval. L4 is authored directly from its V2 source. Adding L4 exercises the same framework on content absent from the supplied three reference decks. The frame accepts subject, grade, unit, theme and output-directory parameters; a future science unit can reuse its layout primitives with new source-specific content and diagrams. The Cell Structure authoring script intentionally retains this unit’s own lesson sequence and assets.

## Build and inspect

From the repository root:

```bash
.venv/bin/python scripts/build_cellstructure_v2.py
.venv/bin/python scripts/validate_lesson_deck.py outputs/drafts/v2/Bio_G10_CellStructure_L4_Plant_Cell_Ultrastructure_v2.pptx --minutes 80
```

Run LibreOffice export with `ExportHiddenSlides=true` for teacher review, rasterise the PDFs, and run `scripts/gpu_visual_qa.py` on every slide. `scripts/package_cellstructure_v2.py` assembles review materials after validation. The generated package contains full-slide PDFs and a selected-slide quick review PDF.

## Source and science decisions

- Earlier corrections remain binding: platelets are fragments; shared ribosomes; cell-wall exceptions; no premature cell/organelles answers in L1; no expected microscope image before recording; no guaranteed membrane/nucleus visibility.
- L4's diagram is a **generalised photosynthetic plant cell**, not every plant cell. Animal cells do not lack chloroplasts merely because they are shaded. Both plant and animal cells respire.
- The source's “all cells have the same DNA” and “every organelle exists because the cell's job demands it, no more, no less” are not repeated as universal claims. Structure relates to role without implying intention or perfect optimisation.
- “Nine organelles” follows the source's classroom grouping, but wall, membrane and ribosomes are not all membrane-bound organelles. Student goals say nine structures.
- The source asks for optional three actual EM images where available. No verified maize chloroplast/onion vacuole/adjacent-wall EM set was provided. This version uses the source's diagram-only route and explicitly records that limitation; the drawings are never labelled EM. The microscope comparison distinguishes conventional TEM requirements from all electron microscopy.
- L4 timing is fitted to 80 minutes without dropping tasks: opening 1.5; Predict 8; Observe 20; Explain 29; board 7; model 12; summary 2.5. Optional EM display time is not claimed. The conflicting source instructions about prediction scanning are resolved by waiting until pupils commit, then scanning.
- L1 retains the deliberate delayed driving-question reveal (source sequence versus manual map convention). L2 retains V2's one new note and 3–4 required model labels. L4 retains row-assigned one-note prompts and its two summary sentences; no additional assessment is invented. These source/manual differences require owner review.
- L6 keeps every pupil's real record distinct from the schematic. Unusual observations must be investigated, not overwritten. Inner bulb epidermis is generally non-photosynthetic protective tissue; the bulb's fleshy layers store reserves. Poor visibility is not proof of absence. The sample's light environment is contextual, not a universal rule for chloroplast distribution.
- L6 stain product/concentration, local risk assessment, PPE, waste and equipment calibration remain teacher decisions. No improvised tincture dilution or no-goggles fallback is approved by this draft.

Primary background check for L4 structures/functions: [OpenStax Biology 2e, 4.3 Eukaryotic Cells](https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells). The V2 lesson source, rather than this background page, supplies the lesson activity sequence and wording. Earlier science references and detailed corrections are retained in the original per-lesson build logs.

## Computing and limits

Built-in imagegen generated the four original contextual illustrations. Host GPU use is not asserted for that hosted service. All local raster resizing and pixel metrics use verified CUDA on NVIDIA GB10 with no CPU fallback. Python-pptx vector/document assembly, PNG encode/decode, PDF conversion/rasterisation, PDF text extraction, ZIP packaging and file layout have CPU code paths and are explicitly exceptions. No local generative or vision model is claimed. Calibri is specified, but local PDF rendering uses Carlito. Speaker-note runs and the inherited notes-master Latin theme are explicitly normalised to Calibri; the separate notes theme must be checked as well as slide fonts. Native PowerPoint/Presenter View, exact Calibri fidelity, ARES offline/content checks and teacher approval remain open.
