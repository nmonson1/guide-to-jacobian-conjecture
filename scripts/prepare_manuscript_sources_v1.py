#!/usr/bin/env python3
"""Import a sanitized write-once manuscript-source release into site data."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRIVATE = re.compile(
    r"(?:/fss/|/home/|file://|chatgpt\.com/share|conversation_id|"
    r"message_id|artifact_id|INTAKE-|JC-CAN-|JC-PKG-)",
    re.IGNORECASE,
)


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _write_once(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(payload)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    source = args.source.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    source_manifest_path = source / "manifest.json"
    source_manifest = _load(source_manifest_path)
    files = []
    for item in source_manifest["files"]:
        relative = Path(item["path"])
        source_path = source / "sources" / relative
        payload = source_path.read_bytes()
        if _sha(payload) != item["content_sha256"]:
            raise ValueError(f"source digest mismatch: {relative}")
        text = payload.decode("utf-8")
        if PRIVATE.search(text):
            raise ValueError(f"private marker in source: {relative}")
        _write_once(output / "sources" / relative, payload)
        files.append(
            {
                "path": relative.as_posix(),
                "sha256": _sha(payload),
                "size_bytes": len(payload),
                "labels": item["labels"],
            }
        )

    retained = source_manifest["retained_registry"]
    manifest = {
        "schema_version": 1,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "source_release_id": source_manifest["release_id"],
        "source_manifest_sha256": _sha(source_manifest_path.read_bytes()),
        "source_repository_commit": source_manifest["source_repository_commit"],
        "source_tree_sha256": source_manifest["source_tree_sha256"],
        "retained_registry": {
            "registry_id": retained["registry_id"],
            "sha256": retained["sha256"],
        },
        "entrypoints": source_manifest["entrypoints"],
        "counts": source_manifest["counts"],
        "files": files,
        "labels": source_manifest["labels"],
    }
    payload = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    if PRIVATE.search(payload.decode("utf-8")):
        raise ValueError("private marker in public source manifest")
    _write_once(output / "manifest.json", payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "file_count": len(files),
                "manifest_sha256": _sha(payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
