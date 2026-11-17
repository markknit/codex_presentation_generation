"""Explicit, source-derived quiz authoring; no server or fabricated responses."""
import json
import math
import re

REVISION = 'quiz-v1'
LABELS = ('A', 'B', 'C', 'D')


def require_revision(spec):
    if spec.get('design_revision') != REVISION:
        raise ValueError('Pre-quiz specification: author quiz-v1 questions, placement and timing before building.')


def validate_quizzes(spec, module, number, source_hashes):
    require_revision(spec)
    if not isinstance(spec.get('quizzes'), list):
        raise ValueError('An explicit quizzes list is required, including for a documented exception.')
    quizzes = spec['quizzes']
    if len(quizzes) < 2 and not str(spec.get('quiz_exception', '')).strip():
        raise ValueError('Fewer than two checkpoints requires a pedagogical quiz_exception.')
    if spec.get('assessment') and quizzes:
        raise ValueError('Independent assessment reinforcement needs a separate post-collection lesson; no coached polls here.')
    ids = set()
    placements = []
    for q in quizzes:
        expected = re.escape(f'{module}.L{number:02}.') + r'Q[0-9]{2}\.v[1-9][0-9]*'
        if not re.fullmatch(expected, q.get('id', '')) or q['id'] in ids:
            raise ValueError('Question IDs must be unique, lesson-scoped and versioned.')
        ids.add(q['id'])
        where = q.get('after_slide')
        if where == 'summary':
            phase = 'Model Building'
            ordinal = len(spec['slides']) + 1
        elif type(where) is int and 1 <= where <= len(spec['slides']):
            phase = spec['slides'][where - 1]['phase']
            ordinal = where
        else:
            raise ValueError('after_slide must identify a source-specific slide or summary.')
        if q.get('phase') != phase:
            raise ValueError('Quiz time must be assigned to its placement phase.')
        placements.append(ordinal)
        for name in ('stem', 'objective', 'placement_reason', 'no_future_content_reason',
                     'timing_source', 'explanation', 'accuracy_check'):
            if not isinstance(q.get(name), str) or not q[name].strip():
                raise ValueError(f'Missing quiz authoring evidence: {name}')
        options = q.get('options', {})
        if not isinstance(options, dict) or set(options) != set(LABELS):
            raise ValueError('Exactly four options A, B, C, D are required.')
        if any(not isinstance(v, str) or not v.strip() for v in options.values()):
            raise ValueError('Every option must be non-empty text.')
        if len({v.strip().casefold() for v in options.values()}) != 4:
            raise ValueError('Options must be distinct.')
        if q.get('correct') not in LABELS:
            raise ValueError('A single correct A–D choice is required.')
        distractors = q.get('distractor_feedback', {})
        if set(distractors) != set(LABELS) - {q['correct']} or any(
                not isinstance(v, str) or not v.strip() for v in distractors.values()):
            raise ValueError('Explain the misconception behind each wrong option privately.')
        if len(q['stem']) > 240 or max(map(len, options.values())) > 105 or len(q['explanation']) > 300:
            raise ValueError('Quiz text exceeds the slide layout; shorten it and retain full guidance privately.')
        for name in ('response_minutes', 'feedback_minutes'):
            value = q.get(name)
            if type(value) not in (int, float) or not math.isfinite(value) or value <= 0:
                raise ValueError('Allocate positive, finite response and feedback minutes explicitly.')
        refs = q.get('source_refs')
        if not isinstance(refs, list) or not refs:
            raise ValueError('Source evidence is required for every key.')
        for ref in refs:
            if ref.get('file') not in source_hashes or any(
                    not isinstance(ref.get(k), str) or not ref[k].strip() for k in ('locator', 'evidence')):
                raise ValueError('Reference a verified source file, exact locator and supporting evidence.')
    if placements != sorted(placements):
        raise ValueError('Author quizzes in teaching order.')
    if len(quizzes) >= 2 and len(set(placements)) < 2 and not spec.get('quiz_exception'):
        raise ValueError('Periodic checks need separate placements, or a documented exception.')
    return quizzes


def render_quiz(lesson, q):
    # CPU-only editable PowerPoint shapes. Raster review is a separate CUDA gate.
    from lesson_visuals import tx, box, INK, MUTED, CREAM
    key = f"{q['id']}\nCorrect: {q['correct']}. {q['options'][q['correct']]}\n{q['explanation']}\n"
    key += '\n'.join(f'{k}: {v}' for k, v in q['distractor_feedback'].items())
    source = '\n'.join(f"{r['file']} — {r['locator']}: {r['evidence']}" for r in q['source_refs'])
    phase = q['phase']
    slide = lesson.slide('Pause and check your understanding', phase, q['response_minutes'],
        'Open the configured question for individual responses. Keep all keys and class results private until closure. '
        'Use the server only if actually configured; otherwise record paper choices privately. '
        'Close the response window before showing aggregates or advancing to feedback. No automatic advance.',
        say='Choose A, B, C or D individually. Keep a reason for your choice.',
        key=key, look='Check participation privately; distinguish non-response from a wrong choice.',
        iff='If access fails, record paper responses privately; do not claim automatic capture.',
        background=f"Objective: {q['objective']}\nPlacement: {q['placement_reason']}\n"
                   f"Later-content protection: {q['no_future_content_reason']}\n"
                   f"Time allocation: {q['timing_source']}\nAccuracy check: {q['accuracy_check']}\n{source}",
        check=True)
    question_slide = len(lesson.b.records)
    lesson.b.records[-1].update({'quiz_id': q['id'], 'quiz_stage': 'question'})
    tx(slide, q['stem'], .8, 2.12, 11.65, 1.3, 26, INK, True)
    for i, label in enumerate(LABELS):
        x = .8 + (i % 2) * 6.0
        y = 3.7 + (i // 2) * 1.3
        box(slide, x, y, 5.72, 1.12, CREAM)
        tx(slide, f"{label}  {q['options'][label]}", x + .18, y + .07, 5.35, .99, 21, INK)
    tx(slide, 'Respond individually. Keep a reason for your choice.', .85, 6.4, 11.5, .45, 19, MUTED)
    slide = lesson.slide('Check the reasoning', phase, q['feedback_minutes'],
        'Only after responses close: switch to the configured class aggregate A–D display, showing no individual data. '
        'Return to this feedback slide. If the server is unavailable, discuss a class tally only if actually collected. '
        'Use the observed distribution to decide whether to revisit the source representation; do not invent results. '
        'Keep any second attempt separate from the first in reports.',
        say='Compare your reason with this explanation. What would you keep or revise?',
        key=key, look='Use actual aggregate misconceptions to guide reinforcement; inspect individual reports privately later.',
        iff='If the main misconception persists, revisit the relevant evidence within the recorded phase time or flag follow-up.',
        background=source, check=True)
    feedback_slide = len(lesson.b.records)
    lesson.b.records[-1].update({'quiz_id': q['id'], 'quiz_stage': 'feedback'})
    tx(slide, f"{q['correct']}  {q['options'][q['correct']]}", .85, 2.2, 11.5, 1.05, 30, INK, True)
    box(slide, .8, 3.55, 11.7, 1.85, CREAM)
    tx(slide, q['explanation'], 1.0, 3.78, 11.25, 1.35, 25, INK)
    tx(slide, 'Explain the reason, then decide whether your first idea needs revising.', .85, 5.85, 11.5, .75, 21, MUTED)
    return {'id': q['id'], 'question_slide': question_slide, 'feedback_slide': feedback_slide}


def manifests(module, number, quizzes, positions, deck_sha256):
    base = {'schema_version': 1, 'design_revision': REVISION,
            'lesson_id': f'{module}.L{number:02}', 'deck_sha256': deck_sha256,
            'capture_status': 'Future server integration required; no responses captured by PowerPoint'}
    by_id = {p['id']: p for p in positions}
    public = {**base, 'questions': []}
    private = {**base, 'visibility': 'PRIVATE TEACHER/SERVER KEY', 'keys': []}
    for q in quizzes:
        public['questions'].append({k: q[k] for k in ('id', 'stem', 'options', 'objective', 'phase')})
        public['questions'][-1].update(by_id[q['id']])
        private['keys'].append({k: q[k] for k in ('id', 'correct', 'explanation', 'distractor_feedback',
                                                  'source_refs', 'accuracy_check', 'placement_reason',
                                                  'no_future_content_reason', 'timing_source')})
    return public, private


def export_manifests(out, name, module, number, quizzes, positions, deck_sha256):
    public, private = manifests(module, number, quizzes, positions, deck_sha256)
    for kind, suffix, payload in [('public', '_Questions.json', public), ('private', '_Answer_Key.json', private)]:
        folder = out/'quizzes'/kind
        folder.mkdir(parents=True, exist_ok=True)
        (folder/(name + suffix)).write_text(json.dumps(payload, indent=2, ensure_ascii=False))


def check_exports(out, name, module, number, spec, source_hashes, deck_sha256, records, slides):
    """Compare manifests with authored truth and slide content; reject stale packages."""
    quizzes = validate_quizzes(spec, module, number, source_hashes)
    positions = []
    earlier = []
    for q in quizzes:
        qr = [r for r in records if r.get('quiz_id') == q['id'] and r.get('quiz_stage') == 'question']
        fr = [r for r in records if r.get('quiz_id') == q['id'] and r.get('quiz_stage') == 'feedback']
        if len(qr) != 1 or len(fr) != 1 or fr[0]['slide'] != qr[0]['slide'] + 1:
            raise ValueError('Each quiz requires one question followed by controlled feedback.')
        if any('authored_slide' in r for r in records):
            anchor = [r for r in records if r.get('authored_slide') == q['after_slide']]
            offset = 2 * sum(prev['after_slide'] == q['after_slide'] for prev in earlier)
            if len(anchor) != 1 or qr[0]['slide'] != anchor[0]['slide'] + 1 + offset:
                raise ValueError('Quiz no longer follows its authored concept transition.')
        for record, expected_time in [(qr[0], q['response_minutes']), (fr[0], q['feedback_minutes'])]:
            if record['phase'] != q['phase'] or record['hidden'] or record['minutes'] != expected_time:
                raise ValueError('Quiz slide metadata does not match authored timing/phase.')
        question_text = '\n'.join(s.text for s in slides[qr[0]['slide'] - 1].shapes if s.has_text_frame)
        if q['stem'] not in question_text or any(f'{k}  {v}' not in question_text for k, v in q['options'].items()):
            raise ValueError('Question stem/options absent from the projected slide.')
        feedback_text = '\n'.join(s.text for s in slides[fr[0]['slide'] - 1].shapes if s.has_text_frame)
        if q['explanation'] not in feedback_text or f"{q['correct']}  {q['options'][q['correct']]}" not in feedback_text:
            raise ValueError('Feedback explanation absent from the subsequent slide.')
        positions.append({'id': q['id'], 'question_slide': qr[0]['slide'], 'feedback_slide': fr[0]['slide']})
        earlier.append(q)
    expected = manifests(module, number, quizzes, positions, deck_sha256)
    for kind, suffix, payload in [('public', '_Questions.json', expected[0]), ('private', '_Answer_Key.json', expected[1])]:
        actual = json.loads((out/'quizzes'/kind/(name + suffix)).read_text())
        if actual != payload:
            raise ValueError('Stale or altered quiz manifest, key or public/private separation.')
    return {'design_revision': REVISION, 'questions': len(quizzes), 'manifest_and_slide_checks': 'PASS',
            'privacy_boundary': 'Public questions and private keys separated; live server unimplemented'}
