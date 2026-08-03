"""CLI orchestration for the Lane 8 validator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile

from .common import CONTRIBUTION_DIR, ValidationError, load_indexed_manifest, require, run_replay
from .manifest import validate_manifest_shape
from .queue import validate_queue
from .replay import validate_replay
from .sources import validate_sources


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replay-output", type=Path,
                        help="optional nonexisting directory in which to retain replay summary output")
    args = parser.parse_args()
    manifest = load_indexed_manifest(CONTRIBUTION_DIR / "stage-manifest.json")
    validate_manifest_shape(manifest)
    validate_sources(manifest)
    if args.replay_output is not None:
        require(not args.replay_output.exists(), f"replay output already exists: {args.replay_output}")
        summary = run_replay(args.replay_output)
    else:
        with tempfile.TemporaryDirectory(prefix="lane8-validation-") as directory:
            summary = run_replay(Path(directory) / "replay")
    validate_replay(manifest, summary)
    validate_queue(manifest)

    edges = manifest["queue"]["edges"]
    covering = sum(bool(edge["covering"]) for edge in edges)
    print("lane8 submission validation: PASS")
    print(f"nodes={len(manifest['queue']['nodes'])}")
    print(f"edges={len(edges)} covering={covering} noncovering={len(edges)-covering}")
    print(f"truncated_rank={summary['truncated']['macaulay_rank']}")
    print(f"truncated_minor_sha256={summary['truncated']['minor_determinant_sha256']}")
    print(f"full_equations={len(summary['full']['equation_manifest'])}")
    print(f"full_equation_sha256={summary['full']['final_equation_sha256']}")
    print(f"terminal_projection_sha256={summary['full']['terminal_projection']['sha256']}")
    print("full_closure_paths=2")
    print("adjacent_terminal=empty_but_unattached")
    print("below_125=relative_to_imported_GGHV_and_toric_theorems")
    return 0


def cli() -> None:
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ValidationError) as exc:
        print(f"validation error: {exc}", file=sys.stderr)
        raise SystemExit(2)
