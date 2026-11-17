# Presentation efficiency pilot — approved next-session task

Authorised by the user on 17 November 2026. **Documented, not executed.**
Priority: quality first, processing cost second, speed third. The user explicitly
accepts slower completion when it reduces total cost without reducing quality.
This pilot precedes further production generation. Current drafts remain paused;
Core Real Numbers L9 is the next production lesson after the pilot decision.

## Scope and preserved state

Evaluate a resumable, source-grounded production pipeline for the current three
curricula and eventual additional four mainline STEM curricula. Current verified
scope is 43 units/514 lessons in the three-curriculum collection; the additional
four curricula have not been newly inventoried for this pilot. Do not project a
numerical seven-curriculum total without verifying their sources and scope.

There are 23 builder-reviewed drafts, 493 slides, 63 quizzes, 447 print pages and
920 scheduled minutes. Two Core specs are authored/unbuilt; 489 other lessons
await quiz design. These drafts are references, not teacher-approved ground truth.
Source materials and approved subject guidance remain authoritative.

Preserve existing source files, drafts, hashes, packages and QA. Use an isolated,
Git-ignored experiment directory such as
`outputs/drafts/efficiency_pilot_2026-11`; record tracked manifests, metrics and
findings under `qa/efficiency_pilot_2026-11`. Do not overwrite current production
specs/decks or reintroduce deleted pre-quiz pilots. No bulk generation, release,
change of model defaults or new paid service is part of this documentation step.

## What to test

1. Prepare one indexed full-unit source packet: exact citations, source hashes,
   sequence, phenomenon, all tasks/materials/keys/assessment, source timings,
   dependencies and later-reveal restrictions. Read the whole original unit as
   required; a summary must not silently replace required source/manual reading.
2. Use compact active status and linked historical logs. Propose changes to
   restart/update and status organisation together, retaining all binding
   instructions and history. The 81 KB STATUS observed before this update is a
   concrete overhead candidate. No archival restructuring has happened yet.
3. Use structured source-specific lesson/quiz specifications and reusable,
   editable visual components; let scripts perform routine assembly and checks.
   Existing builders already provide much of this foundation.
4. Add one resumable pilot runner with per-stage evidence/checkpoints, concise
   output and explicit failure status. Cache successful stages against relevant
   source/spec/template/guidance/tool-version dependencies. Rerun affected gates
   when dependencies change. Do not revalidate only the easiest pages.
5. Separate bounded authoring and review contexts; avoid repeating unchanged
   images, whole histories or verbose logs. Inspect all final pages at readable
   size, with enlargements as needed. Image triage must not remove visual gates.
6. Compare Sol Medium with cheaper-model/local candidates for narrowly defined
   tasks. No automatic wholesale authoring downgrade. Measure errors, repairs and
   reviewer effort as part of cost. Independent source/quiz review remains.
7. Evaluate optional API batch processing and prompt caching only as a separate
   costed route, with compatible models/authentication and bounded spend. Batch
   documentation states 50% below equivalent synchronous API requests, within
   24 hours; that is not a claim of 50% total project/Codex savings. Stable shared
   prompts can support caching; record actual hits/write/read costs where exposed.
   No API batch submission or new API billing configuration has occurred.

## Staged sample design — control the pilot's own cost

Use existing reviewed lessons, read the full corresponding units and preserve
independent assessment. Suggested nine-lesson pool:

| Curriculum | Development pool | Held-out final checks |
| --- | --- | --- |
| General Science Introduction | L3 (water evidence), L5 (careers/source chart) | L7 (independent assessment) |
| Essential Real Numbers | L3 (signed operations), L6 (units/models) | L7 (full servings/checks) |
| Core Real Numbers | L4 (mixed-number reciprocal), L6 (actual calculator evidence) | L8 (evidence/advice) |

Freeze and hash the selected source inputs, reference outputs, evaluation rubric,
model/runtime configuration and prompts. Do not tune repeatedly on held-out results.

Start with one lesson per curriculum to measure a controlled baseline and the
script/context improvements using the same model. Historical account-meter changes
are not an accurate per-lesson monetary baseline. Add cheap/local candidates first
on small structured tasks; eliminate failures before running complete decks. Only
the promising workflow advances to the broader pool and held-out checks. Avoid a
full model × lesson × setting experiment matrix. A local model is not mandatory
if deterministic scripts are cheaper and more reliable for a task.

After the initial pilot, separately qualify representative lessons from each
additional STEM curriculum, including diagram/practical/safety complexity as
applicable. Do not assume simple arithmetic/career-slide results establish equal
quality or cost for Chemistry, Physics, Biology or another mainline curriculum.
Full approved manual/source reading and the corresponding pilot gates apply.

## Spark / Blackwell offload assessment

Live read-only inventory: `jhm-spark`, Linux aarch64, NVIDIA GB10, driver
580.178.04, compute capability 12.1 (CUDA sm_121); approximately 121.7 GiB physical
system memory reported. This is shared system memory, not 128 GB of separate GPU
VRAM. See `qa/Efficiency_Pilot_host_snapshot_2026-11-17.json` for exact bytes.
NVIDIA documents Spark's unified-memory Grace Blackwell platform and local
inference recipes. Actual usable memory must be remeasured before any runtime.

Already implemented and executed: CUDA nearest-neighbour preview resizing and
pixel ink/darkness metrics. Existing evidence records all 493 reviewed slides and
447 print pages. These operations do not perform semantic/factual review.

Candidate offloads, in priority order:

- **Local deterministic processing on the CPU:** DOCX/JSON text extraction,
  source indexing, exact arithmetic/symbolic checks, hashes, manifests, PPTX/DOCX
  assembly, packaging, job checkpoints and compact reporting. These tasks avoid
  unnecessary cloud-model calls without requiring a language model. Existing
  python-pptx, LibreOffice and Poppler paths are CPU-only; log them explicitly.
- **GPU text-model inference:** source-grounded extraction/classification and
  structured drafts of notes/questions as experimental candidates. Verify all
  citations and single-answer keys; keep substantive cloud/source-owner review
  until the candidate qualifies. DOCX XML extraction itself needs no LLM/OCR.
- **GPU vision/OCR:** preliminary detection of clipped text, missing symbols,
  table defects and suspicious pages. OCR only where text is raster/scanned;
  native source/PDF text is preferable when available. Specifically test minus
  signs, fractions, exponents, units and scientific notation. Retain inspection
  of every final slide/print page and native PowerPoint/teacher gates.
- **GPU visual comparisons:** batched image differences, duplicate detection or
  similarity search to prioritise review and identify unchanged renders. Validate
  false negatives with controlled defects in labelled experiment copies; never
  treat a similarity score as scientific/teaching approval.
- **GPU embeddings/retrieval:** optional for finding source passages or reusable
  assets across many units; prefer exact lookup where sufficient. Retrieval does
  not replace whole-unit reading or authorise content transfer across curricula.
- **GPU illustration generation:** lower-priority optional experiment only where
  it improves required visuals. Prefer reusable editable scientific diagrams;
  do not substitute generated pictures for scientific evidence or editable text.

The hosted Codex/Sol model does not move onto this GPU. A separately installed,
licensed local model and compatible ARM64/Blackwell runtime are needed for local
inference. NVIDIA provides vLLM/llama.cpp and related Spark recipes; choose a
small task-appropriate supported candidate and verify actual GPU kernels rather
than CPU fallback. Do not choose model size from theoretical capacity alone:
weights, quantisation, context/KV cache and concurrent CPU/GPU jobs share memory.

Currently found: nvcc and Docker binaries. No torch, transformers, vllm or
paddleocr packages in the project .venv; no ollama, llama-server or vllm commands
on PATH. Containers, running endpoints and model weights were not inventoried,
so do not claim there is no containerised model installed. No inference runtime,
weight download, driver change or benchmark was installed/run in this step.

Local inference avoids cloud token charges only for work actually completed
locally. Any cloud orchestration/review remains metered. Include setup, downloads,
local electricity/operating time, retries and review; if no usable power telemetry
exists, label estimates and assumptions. Running every local result through the
same full cloud job may remove the intended saving. Do not weaken review to
manufacture a favourable result. No savings percentage is established yet.

## Measurement, acceptance and handoff

Record task/run IDs, source/spec/template/model/runtime hashes, arm, tokens
(uncached/cached input, output/reasoning where exposed), measured charges/credits
or explicitly labelled estimates, model calls/retries, runtime, setup/reviewer
work, local memory/power data if available, defects and each quality-gate result.
Account allowance percentages are approximate and are not dollar measurements;
context capacity is separate. Report one-time setup separately from repeatable
cost and calculate a break-even range with assumptions rather than promise savings.

Accept a candidate only with source fidelity/content completeness, correct
single-answer quiz keys/distractors, no premature reveals, exact source phase
budgets, complete notes, valid private/public exports and no observed visual
regression. Use source-based independent review and seeded defect tests for QA
candidates. Reject regressions or savings erased by correction/review costs.
Teacher/native PowerPoint gates remain open until separately evidenced; no pilot
result is a classroom release. Do not silently replace every-page visual review
with sampling/local triage.

Deliver a short comparison report, reproducible runner/configuration, raw metrics,
quality findings and a recommended route for approval before wider rollout. No
financial forecast for all seven curricula without defensible per-category data.

The existing 5% account-or-context stopping rule remains. Check before new model/
lesson jobs and after review. On threshold or low-capacity compaction, finish the
in-flight boundary, run repository `/update`, commit/push authorised continuity
and pause. Do not let a background queue continue unbounded after a stop. The
current thread's generation pause is still latched; this plan does not clear it.

## Primary references checked 17 November 2026

- NVIDIA hardware: https://docs.nvidia.com/dgx/dgx-spark/hardware.html
- NVIDIA local inference: https://build.nvidia.com/spark/vllm/advanced
- NVIDIA workloads: https://build.nvidia.com/spark
- Model roles: https://learn.chatgpt.com/docs/models?surface=cli
- API batch: https://developers.openai.com/api/docs/guides/batch
- Prompt caching: https://developers.openai.com/api/docs/guides/prompt-caching
- Account usage: https://learn.chatgpt.com/docs/pricing

Next session: `/restart`, read this plan and the active handoff, verify live
usage/host/GPU/source state, then run the bounded efficiency pilot. **Do not
immediately resume production Core L9.** Its source-specific specification is
ready for production after the pilot decision.
