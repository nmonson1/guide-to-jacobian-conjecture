#!/usr/bin/env python3
"""Refresh only the Program 1 public brief from the selected private source."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

from prepare_model_briefs_v12 import _publicize, _validate_public


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_PRETTY_LINK = re.compile(
    r"(?P<path>\.\./(?:working-mathematics|proof-sources)/[^)#]+?)/"
    r"(?P<anchor>#[^)\s]+)?(?=\))"
)


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--program-1-source", type=Path, required=True)
    parser.add_argument("--base-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")
    base = json.loads(args.base_manifest.read_text(encoding="utf-8"))
    prepared = []
    for item in base["briefs"]:
        if item["program_slug"] == "cubic-marked-root-incidence-geometry":
            text = _publicize(
                args.program_1_source.read_text(encoding="utf-8"),
                cross_program=False,
            )
            text = text.replace("../../research/", "../")
            text = RESEARCH_PRETTY_LINK.sub(
                lambda match: (
                    match.group("path") + ".md" + (match.group("anchor") or "")
                ),
                text,
            )
        else:
            text = (args.base_manifest.parent / item["source"]).read_text(
                encoding="utf-8"
            )
            _validate_public(text)
        payload = text.encode("utf-8")
        words = len(text.split())
        if not 2_000 <= words <= 4_000:
            raise ValueError(
                f"{item['program_slug']}: word count {words} outside 2000–4000"
            )
        prepared.append(
            (
                item["source"],
                payload,
                {
                    **item,
                    "sha256": _sha(payload),
                    "bytes": len(payload),
                    "words": words,
                },
            )
        )
    output.mkdir()
    for name, payload, _ in prepared:
        (output / name).write_bytes(payload)
    manifest = {
        "schema_version": 1,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "brief_count": len(prepared),
        "briefs": [item for _, _, item in prepared],
    }
    payload = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    (output / "manifest.json").write_bytes(payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "brief_count": len(prepared),
                "manifest_sha256": _sha(payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
