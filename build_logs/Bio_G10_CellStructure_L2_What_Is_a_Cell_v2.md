# Cell Structure Lesson 2 · version 2 build log

Review draft, 24 October 2026. User requested a more engaging, more visual and clearer redesign of L1/L2/L6 and a new L4. Native PowerPoint, Calibri fidelity, ARES and teacher/source-owner approval remain open. No classroom release is claimed.

## Reference comparison and visual changes

All slides of the user-selected three reference decks were rendered and inspected. The new deck uses original contextual illustrations, phase cues, explicit individual/pair/group actions, prompt/reveal pacing and editable science figures. No reference lesson artwork or slide content XML was copied. Existing institutional theme and logos remain. Read `content/cellstructure_v2/DESIGN.md` for the transferable rules, component map and limits, and `assets/cellstructure_v2/provenance.json` for exact imagegen prompts/checksums.

## Source versus draft decisions

| Slide(s) | Source/reference issue | Deck treatment | Reason / review decision |
| --- | --- | --- | --- |
| 6–10, 20–24 | Previously compressed multi-part tasks | Split writing/pairing, kitchen/mapping, CER/sharing, and drawing/limitations into successive screens | Same activities, unchanged 80-minute total. |
| 11–13 | Numbered cell schematics were hard to interpret | Direct editable leader lines and consistent coloured structures | Labels trace to actual features; not micrograph evidence. |
| 22–24 | Reference mandates eight model labels and two notes | Retain V2 three/four core labels and one new question OR understanding note | Source controls student workload. |
| 13, 17, 20–21 | Incorrect shared-feature and CER implications in examples | Shared ribosomes; cell-wall material/animal exception; story appearance is evidence and theory is reasoning | Retains earlier science corrections and their original detailed log. |
| 9–10 | Source kitchen roles | Keep one mapping: door/membrane; recipe-book information/DNA in nucleus; jiko/mitochondria; sufuria, mwiko and board/organelles | Kitchen does not represent every cell; detailed organelle functions follow in L4–5. |
| All | Folder/META 1.1 versus overview 1.3 | Use Cell Structure without a numerical sub-strand on slides | Source-owner decision remains open. |
| 2–3 | New references use three hidden teacher pages | Keep manual-mandated two hidden pages; put full resource audit in glance notes | Larger resource audit does not need to interrupt student Slide Show. |
| All | Reference graphics/long label lists do not always match V2 | Rebuild visuals from the source and retain previous limited science corrections | Style reference is not source authority. |

## Evidence and computing

Structural, note-order, timing, bounds and font checks: `qa/Bio_G10_CellStructure_L2_What_Is_a_Cell_v2_validation.json`. Slide manifest: `qa/Bio_G10_CellStructure_L2_What_Is_a_Cell_v2_manifest.json`. PDF text retention and practical reveal-order checks: `qa/CellStructure_v2_content_checks.json`. CUDA raster report: `qa/Bio_G10_CellStructure_L2_What_Is_a_Cell_v2_gpu.json`. Human-readable visual review record: `qa/CellStructure_v2_visual_review.json`. Source checksums: `qa/CellStructure_v2_sources.json`.

All 25 slides were rendered, CUDA-processed and visually inspected, including all teacher pages. Repaired contrast, diagram spacing/label endpoints and reusable organelle detail drawings during review. These are builder checks; student engagement is not yet measured. The user/teacher should compare the new samples against the supplied reference decks.

Built-in imagegen supplied original context art. The hosted tool's model, seed and device are not exposed and are not invented. Local raster resize/pixel processing uses verified CUDA sm_121 on NVIDIA GB10 without CPU fallback. Python-pptx assembly and editable-vector creation, document/file layout, image encoding/decoding, LibreOffice export, Poppler rasterisation/text extraction and ZIP operations use CPU code paths. No local inference/vision model is claimed. Previews use Carlito in place of Calibri. A final inherited Aptos notes-theme issue was corrected: notes runs/paragraphs and the notes-master Latin theme now explicitly use Calibri. `qa/CellStructure_v2_notes_font_check.json` proves that the visible slide parts/media were unchanged, so prior PDF/raster evidence remains applicable.

## Remaining gates

Native PowerPoint/Slide Show/Presenter View; Calibri fidelity; ARES link/offline/content fit; source/manual decisions and teacher approval. The original per-lesson log remains part of this version’s correction history.
