# Cell Structure Lesson 6 · version 2 build log

Review draft, 24 October 2026. User requested a more engaging, more visual and clearer redesign of L1/L2/L6 and a new L4. Native PowerPoint, Calibri fidelity, ARES and teacher/source-owner approval remain open. No classroom release is claimed.

## Reference comparison and visual changes

All slides of the user-selected three reference decks were rendered and inspected. The new deck uses original contextual illustrations, phase cues, explicit individual/pair/group actions, prompt/reveal pacing and editable science figures. No reference lesson artwork or slide content XML was copied. Existing institutional theme and logos remain. Read `content/cellstructure_v2/DESIGN.md` for the transferable rules, component map and limits, and `assets/cellstructure_v2/provenance.json` for exact imagegen prompts/checksums.

## Source versus draft decisions

| Slide(s) | Source/reference issue | Deck treatment | Reason / review decision |
| --- | --- | --- | --- |
| 13–15 | Previously one long 27-minute practical screen | Split prepare/focus10, record12, measurement/check5 | Same group task; more actionable guidance and unchanged total. |
| 1, 14, 21–22 | Practical drawings could become expected results | Comparison only after pupil recording and CER; current slide number resolved automatically in title notes | Own observations remain primary evidence. |
| 14, 22 | Native schematic must not imply guaranteed membrane/nucleus visibility | Labels only if identifiable; membrane usually not separate; nuclear detail varies | Retains the previous visibility corrections. |
| 17–22 | Light-only and universal chloroplast explanations | Inner bulb epidermis usually non-photosynthetic; avoid purposeful cell choices and treat poor view cautiously | Cell roles differ; light is context, not a universal chloroplast rule. |
| 1, 3, 6 | Source no-goggles/improvised tincture fallbacks and missing concentration | Flag for qualified teacher; retain baseline precautions without inventing concentration or recipe | Local practical is not ready until product, SDS, PPE, waste and risk controls are approved. |
| 12, 15, 23 | Measurement absent from visual reference | Keep measured field diameter, cell count, objective and mm/μm conversion; worked example after own record | No supplied measurement is represented as learner data. |
| All | Folder/META 1.1 versus overview 1.3 | Use Cell Structure without a numerical sub-strand on slides | Source-owner decision remains open. |
| 2–3 | New references use three hidden teacher pages | Keep manual-mandated two hidden pages; put full resource audit in glance notes | Larger resource audit does not need to interrupt student Slide Show. |
| All | Reference graphics/long label lists do not always match V2 | Rebuild visuals from the source and retain previous limited science corrections | Style reference is not source authority. |

## Evidence and computing

Structural, note-order, timing, bounds and font checks: `qa/Bio_G10_CellStructure_L6_Onion_Cells_Practical_v2_validation.json`. Slide manifest: `qa/Bio_G10_CellStructure_L6_Onion_Cells_Practical_v2_manifest.json`. PDF text retention and practical reveal-order checks: `qa/CellStructure_v2_content_checks.json`. CUDA raster report: `qa/Bio_G10_CellStructure_L6_Onion_Cells_Practical_v2_gpu.json`. Human-readable visual review record: `qa/CellStructure_v2_visual_review.json`. Source checksums: `qa/CellStructure_v2_sources.json`.

All 27 slides were rendered, CUDA-processed and visually inspected, including all teacher pages. Repaired contrast, diagram spacing/label endpoints and reusable organelle detail drawings during review. These are builder checks; student engagement is not yet measured. The user/teacher should compare the new samples against the supplied reference decks.

Built-in imagegen supplied original context art. The hosted tool's model, seed and device are not exposed and are not invented. Local raster resize/pixel processing uses verified CUDA sm_121 on NVIDIA GB10 without CPU fallback. Python-pptx assembly and editable-vector creation, document/file layout, image encoding/decoding, LibreOffice export, Poppler rasterisation/text extraction and ZIP operations use CPU code paths. No local inference/vision model is claimed. Previews use Carlito in place of Calibri. A final inherited Aptos notes-theme issue was corrected: notes runs/paragraphs and the notes-master Latin theme now explicitly use Calibri. `qa/CellStructure_v2_notes_font_check.json` proves that the visible slide parts/media were unchanged, so prior PDF/raster evidence remains applicable.

## Remaining gates

Native PowerPoint/Slide Show/Presenter View; Calibri fidelity; ARES link/offline/content fit; source/manual decisions and teacher approval. L6 practical: stain specification/SDS, local risk assessment, PPE, waste, equipment trial, calibration, real visibility and timing.
