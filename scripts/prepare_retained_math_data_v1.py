#!/usr/bin/env python3
"""Prepare a write-once public retained-mathematics data release."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_PATTERNS = {
    "private filesystem path": re.compile(r"(?:/fss/|/home/|file://)"),
    "conversation locator": re.compile(
        r"(?:chatgpt\.com/share|conversation_id|message_id|artifact_id)",
        re.IGNORECASE,
    ),
    "private workflow identifier": re.compile(r"(?:INTAKE-|JC-CAN-|JC-PKG-)"),
}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


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
    graph_path = source / "public-graph.json"
    source_manifest = _load(source_manifest_path)
    graph = _load(graph_path)
    pinned = {item["path"]: item for item in source_manifest.get("files", [])}
    selected = [
        graph_path,
        *sorted((source / "programs").glob("*.md")),
        *sorted((source / "units").glob("*.md")),
    ]
    if len(selected) != 1 + graph["counts"]["programs"] + graph["counts"]["units"]:
        raise ValueError("public retained-math source count mismatch")

    files: list[dict[str, Any]] = []
    for path in selected:
        relative = path.relative_to(source).as_posix()
        payload = path.read_bytes()
        expected = pinned.get(relative)
        if expected is None or _sha256(payload) != expected["sha256"]:
            raise ValueError(f"source manifest pin failed: {relative}")
        text = payload.decode("utf-8")
        for label, pattern in PRIVATE_PATTERNS.items():
            if pattern.search(text):
                raise ValueError(f"{label} leaked into retained math: {relative}")
        target = output / relative
        _write_once(target, payload)
        files.append(
            {
                "path": relative,
                "sha256": _sha256(payload),
                "size_bytes": len(payload),
            }
        )

    manifest = {
        "schema_version": 1,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "source_registry_id": graph["registry_id"],
        "source_manifest_sha256": _sha256(source_manifest_path.read_bytes()),
        "counts": graph["counts"],
        "file_count": len(files),
        "files": files,
    }
    manifest_payload = (
        json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    ).encode("utf-8")
    _write_once(output / "manifest.json", manifest_payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "registry_id": graph["registry_id"],
                "file_count": len(files),
                "manifest_sha256": _sha256(manifest_payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
