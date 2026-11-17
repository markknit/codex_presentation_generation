"""Meaningful failures for quiz privacy, identity, scheduling and stale exports."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from lesson_quizzes import REVISION, validate_quizzes, render_quiz, export_manifests, check_exports
from lesson_visuals import VisualDeck, note


def fixture():
    q = {'id': 'test_1_1.L01.Q01.v1', 'after_slide': 1, 'phase': 'Explain',
         'stem': 'In this synthetic arithmetic check, what is 2 + 3?',
         'options': {'A': '4', 'B': '5', 'C': '6', 'D': '7'}, 'correct': 'B',
         'objective': 'Check the synthetic arithmetic example.',
         'placement_reason': 'After the example, before a different task.',
         'no_future_content_reason': 'Uses only the preceding synthetic example.',
         'timing_source': 'Use the synthetic fixture review allocation.',
         'response_minutes': .5, 'feedback_minutes': .5,
         'explanation': 'Adding three to two gives five: 2 + 3 = 5.',
         'accuracy_check': 'Count forward three from two: three, four, five.',
         'distractor_feedback': {'A': 'One too few.', 'C': 'One too many.', 'D': 'Two too many.'},
         'source_refs': [{'file': 'fixture.txt', 'locator': 'synthetic example', 'evidence': '2 + 3 = 5'}]}
    q2 = copy.deepcopy(q)
    q2.update({'id': 'test_1_1.L01.Q02.v1', 'after_slide': 'summary', 'phase': 'Model Building'})
    spec = {'design_revision': REVISION, 'slides': [{'phase': 'Explain'}], 'quizzes': [q, q2]}
    return spec, {'fixture.txt': 'synthetic-only'}


def layout_fixture():
    """Short and long text for the separate rendered component inspection."""
    spec, hashes = fixture()
    q = spec['quizzes'][1]
    q['stem'] = ('Synthetic layout stress check. Consider two objects together with three more objects. '
                 'Which of the following statements correctly gives the total and explains what adding the two groups means?')
    for label, value in zip('ABCD', [4, 5, 6, 7]):
        q['options'][label] = (f'The total is {value}; combine the two original objects with the three '
                               'additional objects and count all of them.')
    q['explanation'] = ('There are five objects altogether. Start with two objects, add three further '
                        'objects, then count the combined group: one, two, three, four, five. The same '
                        'relationship is written as 2 + 3 = 5. The question asks for the total number in the combined group.')
    return spec, hashes


class ComponentLesson:
    def __init__(self):
        self.b = VisualDeck(1, 'Quiz_Component_Fixture', subject='Synthetic QA', unit='Quiz component')

    def slide(self, title, phase, minutes, do, **kw):
        notes = note(minutes, do, key=kw.get('key', ''), say=kw.get('say', ''),
                     look=kw.get('look', ''), iff=kw.get('iff', ''), science=kw.get('background', ''))
        return self.b.slide(title, phase, notes, check=True)


class QuizTests(unittest.TestCase):
    def test_pre_quiz_specs_fail_closed(self):
        spec, hashes = fixture()
        del spec['design_revision']
        with self.assertRaisesRegex(ValueError, 'Pre-quiz'):
            validate_quizzes(spec, 'test_1_1', 1, hashes)

    def test_ambiguous_or_untraceable_items_rejected(self):
        for change in ('duplicate_option', 'duplicate_id', 'unknown_source', 'missing_reason', 'bad_time', 'bad_phase'):
            with self.subTest(change=change):
                spec, hashes = fixture(); q = spec['quizzes'][0]
                if change == 'duplicate_option': q['options']['D'] = q['options']['B']
                if change == 'duplicate_id': spec['quizzes'][1]['id'] = q['id']
                if change == 'unknown_source': q['source_refs'][0]['file'] = 'unverified.txt'
                if change == 'missing_reason': del q['no_future_content_reason']
                if change == 'bad_time': q['response_minutes'] = float('nan')
                if change == 'bad_phase': q['phase'] = 'Predict'
                with self.assertRaises(ValueError): validate_quizzes(spec, 'test_1_1', 1, hashes)

    def test_assessment_cannot_be_coached(self):
        spec, hashes = fixture(); spec['assessment'] = True
        with self.assertRaisesRegex(ValueError, 'Independent assessment'):
            validate_quizzes(spec, 'test_1_1', 1, hashes)
        spec.update({'quizzes': [], 'quiz_exception': 'Independent collection; later feedback is a separate lesson.'})
        self.assertEqual(validate_quizzes(spec, 'test_1_1', 1, hashes), [])

    def test_periodic_placement_and_short_lesson_exception(self):
        spec, hashes = fixture(); spec['quizzes'] = spec['quizzes'][:1]
        with self.assertRaisesRegex(ValueError, 'pedagogical'): validate_quizzes(spec, 'test_1_1', 1, hashes)
        spec['quiz_exception'] = 'Synthetic short sequence has one checkpoint.'
        self.assertEqual(len(validate_quizzes(spec, 'test_1_1', 1, hashes)), 1)

    def test_public_manifest_and_stale_key_detection(self):
        spec, hashes = fixture(); lesson = ComponentLesson()
        positions = [render_quiz(lesson, q) for q in validate_quizzes(spec, 'test_1_1', 1, hashes)]
        self.assertEqual(sum(r['minutes'] for r in lesson.b.records), 2)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            export_manifests(out, 'fixture', 'test_1_1', 1, spec['quizzes'], positions, 'deckhash')
            public = out/'quizzes/public/fixture_Questions.json'
            data = json.loads(public.read_text())
            for q in data['questions']:
                self.assertFalse({'correct', 'source_refs', 'explanation', 'distractor_feedback'} & set(q))
            result = check_exports(out, 'fixture', 'test_1_1', 1, spec, hashes, 'deckhash', lesson.b.records, lesson.b.deck.slides)
            self.assertEqual(result['manifest_and_slide_checks'], 'PASS')
            data['questions'][0]['correct'] = 'B'
            public.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'public/private'):
                check_exports(out, 'fixture', 'test_1_1', 1, spec, hashes, 'deckhash', lesson.b.records, lesson.b.deck.slides)
            export_manifests(out, 'fixture', 'test_1_1', 1, spec['quizzes'], positions, 'oldhash')
            with self.assertRaisesRegex(ValueError, 'Stale'):
                check_exports(out, 'fixture', 'test_1_1', 1, spec, hashes, 'deckhash', lesson.b.records, lesson.b.deck.slides)


if __name__ == '__main__':
    unittest.main()
