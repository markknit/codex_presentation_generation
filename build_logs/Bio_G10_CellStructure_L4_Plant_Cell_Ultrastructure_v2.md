# Cell Structure Lesson 4 · version 2 build log

Review draft, 24 October 2026. User requested a more engaging, more visual and clearer redesign of L1/L2/L6 and a new L4. Native PowerPoint, Calibri fidelity, ARES and teacher/source-owner approval remain open. No classroom release is claimed.

## Reference comparison and visual changes

All slides of the user-selected three reference decks were rendered and inspected. The new deck uses original contextual illustrations, phase cues, explicit individual/pair/group actions, prompt/reveal pacing and editable science figures. No reference lesson artwork or slide content XML was copied. Existing institutional theme and logos remain. Read `content/cellstructure_v2/DESIGN.md` for the transferable rules, component map and limits, and `assets/cellstructure_v2/provenance.json` for exact imagegen prompts/checksums.

## Source versus draft decisions

| Slide(s) | Source/reference issue | Deck treatment | Reason / review decision |
| --- | --- | --- | --- |
| All | New lesson absent from the three supplied style references | Reuse the plant diagram, component palette, prompts, timers, model/board layouts; add nine structure/function pairs | Tests transfer of the method instead of copying an existing L4. |
| 8–10 | Optional actual EM set not provided/authenticated | Use source-permitted diagram-only route; comparison table explains light versus conventional TEM | No fabricated micrograph or claim of observed maize/onion EM; teacher may supply verified images. |
| 14–31 | Nine target structures must each receive a cold-call before confirmation | Nine prompt/reveal pairs; one minute each side | Students reason before confirmed function; 18 minutes within 29-minute Explain. |
| 3, all timings | Source has no phase totals and can overrun | Opening 1.5, Predict 8, Observe 20, Explain 29, board 7, model 12, summary 2.5 =80 | All tasks retained; teacher must trial timing for the actual class. |
| 6–7 | Predict instructions conflict about circulating/scanning | Wait for committed predictions, then scan the records | Preserves independent first ideas and the formative indicator. |
| 5, 20–25, 32, 34 | Universal plant/chloroplast and purposeful organelle claims | Generalised photosynthetic cell; functions relate to role; no nucleus that thinks | Correct scientific overgeneralisation; source-owner review needed. |
| 20–25, 32 | Farm solar panels and generator can blur food and energy | Chloroplasts make glucose using light; mitochondria support aerobic respiration; solar analogy is light capture only | Both plant and animal cells respire; energy is transferred, not created. |
| 33–34 | Source provides matching/triad explanation, not a separate CER task | Retain Job Card and triad reasoning; do not insert a new written assessment | Manual/source difference for teacher/source-owner review. |
| 36 | Source early-finisher colour system could imply taxonomic uniqueness | Red means absent in the particular animal comparison, green shared with it | Cell walls/chloroplasts also occur outside plants; large central vacuole is a comparison feature, not a universal test. |
| All | Folder/META 1.1 versus overview 1.3 | Use Cell Structure without a numerical sub-strand on slides | Source-owner decision remains open. |
| 2–3 | New references use three hidden teacher pages | Keep manual-mandated two hidden pages; put full resource audit in glance notes | Larger resource audit does not need to interrupt student Slide Show. |
| All | Reference graphics/long label lists do not always match V2 | Rebuild visuals from the source and retain previous limited science corrections | Style reference is not source authority. |

## Evidence and computing

Structural, note-order, timing, bounds and font checks: `qa/Bio_G10_CellStructure_L4_Plant_Cell_Ultrastructure_v2_validation.json`. Slide manifest: `qa/Bio_G10_CellStructure_L4_Plant_Cell_Ultrastructure_v2_manifest.json`. PDF text retention and practical reveal-order checks: `qa/CellStructure_v2_content_checks.json`. CUDA raster report: `qa/Bio_G10_CellStructure_L4_Plant_Cell_Ultrastructure_v2_gpu.json`. Human-readable visual review record: `qa/CellStructure_v2_visual_review.json`. Source checksums: `qa/CellStructure_v2_sources.json`.

All 37 slides were rendered, CUDA-processed and visually inspected, including all teacher pages. Repaired contrast, diagram spacing/label endpoints and reusable organelle detail drawings during review. These are builder checks; student engagement is not yet measured. The user/teacher should compare the new samples against the supplied reference decks.

Built-in imagegen supplied original context art. The hosted tool's model, seed and device are not exposed and are not invented. Local raster resize/pixel processing uses verified CUDA sm_121 on NVIDIA GB10 without CPU fallback. Python-pptx assembly and editable-vector creation, document/file layout, image encoding/decoding, LibreOffice export, Poppler rasterisation/text extraction and ZIP operations use CPU code paths. No local inference/vision model is claimed. Previews use Carlito in place of Calibri. A final inherited Aptos notes-theme issue was corrected: notes runs/paragraphs and the notes-master Latin theme now explicitly use Calibri. `qa/CellStructure_v2_notes_font_check.json` proves that the visible slide parts/media were unchanged, so prior PDF/raster evidence remains applicable.

## Remaining gates

Native PowerPoint/Slide Show/Presenter View; Calibri fidelity; ARES link/offline/content fit; source/manual decisions and teacher approval. L4: review optional EM provision, comparison language, diagram accuracy and large-class timing.
