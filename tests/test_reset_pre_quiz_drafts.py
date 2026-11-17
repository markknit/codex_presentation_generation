import contextlib
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
import reset_pre_quiz_drafts as reset


class ResetTests(unittest.TestCase):
    def test_changed_files_stop_before_deletion_and_adjacent_sources_survive(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); drafts = root/'drafts'; drafts.mkdir()
            deck = drafts/'old.pptx'; deck.write_bytes(b'old fixture')
            source = root/'source.docx'; source.write_bytes(b'preserve me')
            with patch.object(reset, 'ROOT', root), patch.object(reset, 'TARGETS', ('drafts',)), \
                    patch.object(reset, 'AUDIT', root/'audit.json'), contextlib.redirect_stdout(io.StringIO()):
                reset.prepare(); deck.write_bytes(b'changed fixture')
                with self.assertRaisesRegex(ValueError, 'Files changed'): reset.apply()
                self.assertTrue(deck.exists())
                deck.write_bytes(b'old fixture'); reset.apply()
                self.assertFalse(deck.exists()); self.assertEqual(source.read_bytes(), b'preserve me')

    def test_symlink_refuses_external_traversal(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/'drafts').mkdir(); outside = root/'source.docx'
            outside.write_bytes(b'preserve'); (root/'drafts/link').symlink_to(outside)
            with patch.object(reset, 'ROOT', root), patch.object(reset, 'TARGETS', ('drafts',)):
                with self.assertRaisesRegex(ValueError, 'symlinks'): reset.inventory()
                self.assertEqual(outside.read_bytes(), b'preserve')


if __name__ == '__main__': unittest.main()
