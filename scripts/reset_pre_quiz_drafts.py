#!/usr/bin/env python3
"""Audited reset of the explicitly superseded three-curriculum working files."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ('outputs/drafts/curriculum_sets_2026-11',
           'outputs/drafts/curriculum_pilots_2026-11',
           'qa/renders/curriculum_sets_2026-11',
           'qa/renders/curriculum_pilots_2026-11')
AUDIT = ROOT/'qa/curriculum_quiz_reset_2026-11.json'


def stamp(): return datetime.now(timezone.utc).isoformat()
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory():
    files = {}
    for relative in TARGETS:
        base = ROOT/relative
        paths = [base, *base.rglob('*')] if base.exists() else []
        for p in paths:
            if p.is_symlink(): raise ValueError(f'Reset refuses symlinks: {p}')
            if p.is_file():
                if not p.resolve().is_relative_to(base.resolve()): raise ValueError(p)
                files[str(p.relative_to(ROOT))] = {'sha256': digest(p), 'bytes': p.stat().st_size}
    return files


def prepare():
    if AUDIT.exists(): raise ValueError('Audit already exists; inspect rather than replacing the deletion record.')
    files = inventory()
    report = {'state': 'planned', 'created_at': stamp(), 'design_revision': 'quiz-v1',
              'authorisation': 'User requested deleting completed drafts and restarting with periodic A–D quizzes.',
              'scope': list(TARGETS), 'files': files,
              'count': len(files), 'bytes': sum(f['bytes'] for f in files.values()),
              'extensions': dict(Counter(Path(p).suffix for p in files)),
              'preserved': ['Curriculum source files and reviewed source archives',
                            'Biology drafts, tracked review snapshots and extracted review work',
                            'Authoring/source specifications, historical logs and QA evidence']}
    AUDIT.write_text(json.dumps(report, indent=2))
    print(json.dumps({k: v for k, v in report.items() if k != 'files'}, indent=2))


def apply():
    report = json.loads(AUDIT.read_text())
    if report['state'] != 'planned' or report['scope'] != list(TARGETS):
        raise ValueError('Reset is already applied or its allowlist differs.')
    # Verify the complete set before any deletion. New/changed files require review.
    if inventory() != report['files']:
        raise ValueError('Files changed after the plan; do not delete an unreviewed set.')
    for relative, expected in report.get('preserved_output_hashes', {}).items():
        if digest(ROOT/relative) != expected:
            raise ValueError('An unrelated output changed after the checkpoint; inspect before reset.')
    for relative in report['files']:
        path = ROOT/relative
        if not any(path.resolve().is_relative_to((ROOT/r).resolve()) for r in TARGETS):
            raise ValueError('Path outside authorised reset scope.')
        path.unlink()
    for relative in TARGETS:
        base = ROOT/relative
        for p in sorted(base.rglob('*'), key=lambda p: len(p.parts), reverse=True):
            if p.is_dir(): p.rmdir()
    if inventory(): raise ValueError('Reset left unexpected files.')
    for relative, expected in report.get('preserved_output_hashes', {}).items():
        if digest(ROOT/relative) != expected:
            raise ValueError('Preserved-output verification failed.')
    report.update({'state': 'applied', 'applied_at': stamp(), 'deleted_files_verified': len(report['files'])})
    AUDIT.write_text(json.dumps(report, indent=2))
    print(f"Deleted and verified {report['deleted_files_verified']} pre-quiz working files; sources and unrelated work preserved.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['prepare', 'apply'])
    args = parser.parse_args()
    {'prepare': prepare, 'apply': apply}[args.action]()
