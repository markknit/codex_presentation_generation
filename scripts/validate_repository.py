#!/usr/bin/env python3
"""Validate the portable source inventory and required project controls."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys


EXPECTED = {
    ".docx": 340,
    ".json": 85,
}


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    required = [
        repo / "AGENTS.md",
        repo / "CLAUDE.md",
        repo / "STATUS.md",
        repo / "WORKFLOW.md",
        repo / ".agents/skills/restart/SKILL.md",
        repo / ".agents/skills/update/SKILL.md",
        repo / "references/instructions/SeaVuria_Science_Lesson_PPT_Build_Manual.docx",
    ]
    templates = sorted((repo / "references/templates").glob("*.pptx"))
    source_files = [path for path in (repo / "inputs/v2").rglob("*") if path.is_file()]
    counts = Counter(path.suffix.lower() for path in source_files)

    errors: list[str] = []
    for path in required:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(repo)}")
    if len(templates) != 3:
        errors.append(f"expected 3 template PPTX files, found {len(templates)}")
    if len(source_files) != 425:
        errors.append(f"expected 425 V2 source files, found {len(source_files)}")
    for suffix, expected in EXPECTED.items():
        if counts[suffix] != expected:
            errors.append(f"expected {expected} {suffix} source files, found {counts[suffix]}")
    forbidden = [path for path in repo.rglob("*") if path.is_file() and "cells docx" in path.name.lower()]
    if forbidden:
        errors.extend(f"forbidden Cells-specific manual present: {path.relative_to(repo)}" for path in forbidden)

    print(f"V2 source files: {len(source_files)}")
    print(f"V2 extensions: {dict(sorted(counts.items()))}")
    print(f"Template PPTX files: {len(templates)}")
    if errors:
        print("VALIDATION FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
