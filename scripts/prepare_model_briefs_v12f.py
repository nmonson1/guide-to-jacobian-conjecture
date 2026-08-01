#!/usr/bin/env python3
"""Prepare the write-once audit-repair update over model briefs v12e."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from prepare_model_briefs_v12 import _publicize, _validate_public


ROOT = Path(__file__).resolve().parents[1]
UPDATED_SOURCES = {
    "state-of-the-program": "state-of-the-program.md",
    "cubic-marked-root-incidence-geometry": (
        "cubic-marked-root-incidence-geometry.md"
    ),
    "stable-moduli": "stable-moduli.md",
}


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--base-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    output_dir = args.output_dir.resolve()
    if output_dir.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output_dir}")
    if output_dir.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    base = json.loads(args.base_manifest.read_text(encoding="utf-8"))
    if base.get("brief_count") != 7 or len(base.get("briefs", [])) != 7:
        raise ValueError("base manifest must describe exactly seven briefs")

    prepared: list[tuple[Path, str, dict[str, object]]] = []
    for item in base["briefs"]:
        source_name = UPDATED_SOURCES.get(item["program_slug"])
        if source_name is None:
            text = (args.base_manifest.parent / item["source"]).read_text(
                encoding="utf-8"
            )
            _validate_public(text)
        else:
            text = _publicize(
                (args.source_dir / source_name).read_text(encoding="utf-8"),
                cross_program=item["kind"] == "cross_program",
            )
        payload = text.encode("utf-8")
        words = len(text.split())
        if not 2_000 <= words <= 4_000:
            raise ValueError(
                f"{item['program_slug']}: word count {words} is outside 2000–4000"
            )
        prepared.append(
            (
                output_dir / item["source"],
                text,
                {
                    **item,
                    "sha256": _sha256(payload),
                    "bytes": len(payload),
                    "words": words,
                },
            )
        )

    output_dir.mkdir()
    for path, text, _ in prepared:
        path.write_text(text, encoding="utf-8")
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "release_id": args.release_id,
                "updated_at": args.updated_at,
                "brief_count": len(prepared),
                "briefs": [item for _, _, item in prepared],
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
                "brief_count": len(prepared),
                "manifest_sha256": _sha256(manifest_path.read_bytes()),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
