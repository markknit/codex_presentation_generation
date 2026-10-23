#!/usr/bin/env python3
"""Report host capabilities used by the presentation generation workflow."""

from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> dict[str, object]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, check=False)
        return {
            "available": True,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "error": str(exc)}


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    tools = {name: shutil.which(name) for name in ("git", "node", "python", "nvidia-smi", "ffmpeg")}
    report: dict[str, object] = {
        "repository": str(repo),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python": sys.version,
        "cpu_count": os.cpu_count(),
        "tools": tools,
        "git": run([tools["git"], "-C", str(repo), "status", "--short", "--branch"]) if tools["git"] else None,
        "nvidia_smi": run([tools["nvidia-smi"], "--query-gpu=name,driver_version,memory.total,compute_cap", "--format=csv,noheader"]) if tools["nvidia-smi"] else None,
    }

    try:
        import torch  # type: ignore

        report["torch"] = {
            "version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "cuda_version": torch.version.cuda,
            "device_count": torch.cuda.device_count(),
            "devices": [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())],
        }
    except Exception as exc:  # Torch is optional during initial setup.
        report["torch"] = {"available": False, "error": str(exc)}

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
