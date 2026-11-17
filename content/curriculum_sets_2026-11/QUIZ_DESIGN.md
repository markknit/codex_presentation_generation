# Periodic comprehension quizzes — design revision quiz-v1

User instruction: add A, B, C, D multiple-choice checks throughout lessons,
placed by the authoring model where they best measure understanding and
reinforce learning. A future server records individual responses for separate
reports; the classroom projector shows class aggregates only. This revision
applies to all newly generated or rebuilt lessons. The current reset
supersedes the pre-quiz draft files for the three active curricula.

## Teaching design

- Use one concise question per checkpoint with exactly four options labelled
  A, B, C, D and one unambiguously correct answer. Derive the answer and
  explanations from reviewed lesson content/source keys; record the source
  file, locator and evidence. Distractors should address plausible mistakes,
  be comparable in form and avoid trick wording or clues from option length.
- The model chooses useful concept transitions after learners have encountered
  the necessary evidence/explanation. Usually include two to four spaced
  checkpoints in a 40-minute instructional lesson, including an end check
  where useful. This is a planning guide, not a fixed slide interval or quota.
  A lesson with fewer than two needs a documented pedagogical exception.
- Record the learning objective, placement reason and why the question does
  not disclose later discoveries. Avoid repeating an identical question as
  apparent evidence of independent transfer. Deliberately distribute answer
  positions across a unit; never randomise labels independently of the server.
- Sequence: individual response → close responses → view class A–D distribution
  → explain the correct answer and reasoning → address the main misconception.
  Keep the question neutral until responses close. Feedback appears on a
  separate subsequent slide, controlled by the teacher; no timed auto-advance.
- Use the actual class distribution to choose a short explanation, a return
  to the relevant representation, or continuation. Never invent class results
  or infer each learner's mastery from an aggregate. Preserve each first
  response if a second attempt follows reinforcement.
- Budget both response and feedback time within the existing lesson and phase
  totals. Identify which existing formative-check/review time is used; never
  silently shorten required individual/practical work or remove source tasks.
  If all required work cannot fit, flag the pacing conflict for review.
- Preserve independent assessments. Do not insert coached polls or answer
  reveals before collection. An assessment may have a documented quiz exception;
  any later reinforcement must occur after collection with explicit time.

## Projected and private information

Project only the question, four options, class counts/percentages for A–D,
participation totals, and the subsequent teaching explanation. No names,
student IDs, individual choices/scores, rankings or per-student histories
appear on the projector. Do not project an individual-report screen.

Keep correct answers, distractor explanations, source evidence and teacher
decisions in private notes and the private answer-key manifest. The teacher
PPTX contains notes and subsequent feedback; it is not a secure student quiz
client and must not be distributed as an unrevealed assessment. Student-facing
exports must exclude notes, keys and premature feedback pages.

## Server integration boundary

No response-collection server or reporting UI is implemented by this change.
The following is the proposed handoff contract; actual URLs, authentication,
devices, API wiring and reporting behaviour require the future server.
Do not fabricate links, QR codes, live charts or response data in the deck.
Without the server, use a teacher-managed paper response record; do not claim
automatic capture or analytics.

Each built lesson exports versioned files under its sub-strand:

- `quizzes/public/<deck>_Questions.json`: lesson ID, revision, question IDs,
  stems, labelled options, objectives, phase and slide positions; no keys.
- `quizzes/private/<deck>_Answer_Key.json`: matching question IDs/version,
  correct choices, reasoning, distractor feedback and source evidence.

Identifiers have the form `essmath_1_1.L02.Q01.v1`; preserve the ID for the
same item and increment its item version when the stem/options/key change.
Both manifests include the deck hash, making report interpretation traceable
to the exact lesson/question version and option order used in class.

The future server should store an authenticated student ID privately with
class/session ID, lesson ID, versioned question ID, attempt ID/number, chosen
A–D value and submission time. It validates against the configured question
version, controls open/closed response windows, deduplicates retries, retains
attempt history and scores using the private key on the server. Treat a
non-response separately from an incorrect choice. Report first-attempt
comprehension separately from attempts after feedback.

The projector receives only aggregate counts/percentages and participation
for the current class, session and question. Show distributions only after
closure to avoid influencing initial choices. Individual standalone reports
belong in a separately authorised teacher/reporting view. The collection,
aggregate and reporting integration must be tested together before claiming
this feature works live.

## Build and review gates

Old decks, previews and packages for the three curricula are invalidated and
deleted as authorised. Keep original curriculum sources, design references,
unrelated Biology review work and historical audit records. Rebuild from the
source-specific specifications after quiz authoring; never copy old pilots
back into the new inventory. All 514 lessons need the new design review.

`scripts/lesson_quizzes.py` validates explicit authored quiz specifications,
renders editable question/feedback slides and exports separated manifests.
Legacy specifications are retained as source-work baselines and fail the new
build gate until their lesson revision, quizzes and timing are authored.

Check source/answer accuracy, single-best-answer clarity, misconception value,
placement/reveal order, exact lesson/phase timing, note completeness, public/
private separation, unique versioned IDs and manifest/slide/hash agreement.
Render and inspect every new question and feedback slide with actual CUDA
raster processing, then apply the usual native PowerPoint and teacher gates.
Re-establish a representative quiz-enabled pilot before batch generation.
Validate the live server separately when it exists. No new curriculum decks
are generated during this design/reset task; the previous pause remains.
