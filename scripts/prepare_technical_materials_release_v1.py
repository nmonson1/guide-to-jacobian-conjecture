#!/usr/bin/env python3
"""Stage a write-once technical-material release for the public guide."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-release", type=Path, required=True)
    parser.add_argument("--data-output", type=Path, required=True)
    parser.add_argument("--assets-output", type=Path, required=True)
    args = parser.parse_args()

    source = args.source_release.resolve()
    data_output = args.data_output.resolve()
    assets_output = args.assets_output.resolve()
    for output in (data_output, assets_output):
        if output.exists():
            raise FileExistsError(f"refusing to overwrite existing path: {output}")

    manifest_path = source / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    artifacts = [
        item
        for program in manifest["programs"]
        for item in program["artifacts"]
    ]
    if manifest["artifact_count"] != len(artifacts):
        raise ValueError("technical-material artifact count mismatch")
    names = [item["filename"] for item in artifacts]
    if len(names) != len(set(names)):
        raise ValueError("duplicate technical-material filename")
    for item in artifacts:
        path = source / item["filename"]
        if not path.is_file():
            raise FileNotFoundError(path)
        if path.stat().st_size != item["bytes"]:
            raise ValueError(f"byte count mismatch: {path.name}")
        if sha256(path) != item["sha256"]:
            raise ValueError(f"digest mismatch: {path.name}")

    data_output.mkdir(parents=True)
    assets_output.mkdir(parents=True)
    shutil.copy2(manifest_path, data_output / "manifest.json")
    for item in artifacts:
        shutil.copy2(source / item["filename"], assets_output / item["filename"])
    print(
        f"Staged {len(artifacts)} technical materials in "
        f"{data_output} and {assets_output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
