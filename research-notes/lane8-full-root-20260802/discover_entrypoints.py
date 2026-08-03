#!/usr/bin/env python3
"""Probe extracted Lane 8 programs and record their executable interfaces.

This first-pass harness is intentionally conservative: it records help text and
no-argument exit codes instead of guessing command-line contracts. The exact
runner is tightened after the artifact exposes those contracts.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


def run(command: list[str], cwd: Path) -> dict[str, object]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
        timeout=600,
    )
    return {
        "command": command,
        "cwd": str(cwd),
        "returncode": completed.returncode,
        "output": completed.stdout,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source_dir = args.source_dir.resolve()
    queue_dir = source_dir / "queue"
    raw_script = (
        source_dir
        / "degree-twenty-one"
        / "raw-support-reconstruction"
        / "rebuild_lower_face_reduction.py"
    )
    scripts = [
        queue_dir / "check_queue.py",
        queue_dir / "full_early_layer_reduction.py",
        queue_dir / "quintic_face_reconstruction.py",
        queue_dir / "truncated_support_certificate.py",
        raw_script,
    ]

    report: dict[str, object] = {
        "schema": "lane8-entrypoint-discovery-v1",
        "python": sys.version,
        "probes": [],
    }
    for script in scripts:
        if not script.is_file():
            raise FileNotFoundError(script)
        relative = str(script.relative_to(source_dir))
        for suffix in (["--help"], []):
            report["probes"].append(
                {
                    "script": relative,
                    **run([sys.executable, script.name, *suffix], script.parent),
                }
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    for probe in report["probes"]:
        print(
            f"{probe['script']} {probe['command'][2:]}: "
            f"exit={probe['returncode']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
