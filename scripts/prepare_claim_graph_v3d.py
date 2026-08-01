#!/usr/bin/env python3
"""Prepare a write-once claim-graph correction over v3c."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TAG = "JCG-24C82405"
EXPECTED_STATEMENT = (
    "At the degree-eight base point, after quotienting the affine orbit and "
    "the known quadratic source-shear and target-shear components, no "
    "additional formal branch has a first nonzero normal term transverse to "
    "those two components."
)


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    base_dir = args.base_dir.resolve()
    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output_dir}")
    if output_dir.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    graph_path = base_dir / "claim-graph.json"
    manifest_path = base_dir / "manifest.json"
    graph: dict[str, Any] = json.loads(graph_path.read_text(encoding="utf-8"))
    base_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    matches = [claim for claim in graph["claims"] if claim["tag"] == TAG]
    if len(matches) != 1:
        raise ValueError(f"expected one {TAG} record, found {len(matches)}")
    claim = matches[0]
    if claim["statement"] != EXPECTED_STATEMENT:
        raise ValueError(f"{TAG}: base statement changed unexpectedly")
    if claim["status"] != "certificate offered":
        raise ValueError(f"{TAG}: base status changed unexpectedly")

    claim["status"] = "superseded"
    claim["verification"]["evidence"] = [
        {
            "kind": "correction",
            "scope": (
                "The characteristic-zero weight-minus-one conclusion was "
                "withdrawn. JCG-D3F76EBC retains exact weight-minus-two "
                "elimination and exact weight-minus-one survival through "
                "order four; later death remains modular evidence."
            ),
        }
    ]

    output_dir.mkdir()
    output_graph = output_dir / "claim-graph.json"
    output_graph.write_text(
        json.dumps(graph, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    graph_digest = sha256(output_graph.read_bytes())
    output_manifest = output_dir / "manifest.json"
    output_manifest.write_text(
        json.dumps(
            {
                **base_manifest,
                "release_id": args.release_id,
                "updated_at": args.updated_at,
                "files": [
                    {
                        "path": "claim-graph.json",
                        "sha256": graph_digest,
                    }
                ],
                "patches": [
                    *base_manifest.get("patches", []),
                    (
                        f"{TAG} retained as a stable historical statement but "
                        "marked superseded by the corrected characteristic-zero "
                        "evidence boundary in JCG-D3F76EBC"
                    ),
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output_dir": str(output_dir),
                "release_id": args.release_id,
                "claim_graph_sha256": graph_digest,
                "manifest_sha256": sha256(output_manifest.read_bytes()),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
