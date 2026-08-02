#!/usr/bin/env python3
"""Verify the hash-pinned Lane 3 formal-effectivity source manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.json"


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = data["files"]
    found = sorted(
        path.name
        for path in ROOT.iterdir()
        if path.is_file()
        and path.name != "manifest.json"
        and not path.name.endswith("_report.json")
    )
    listed = sorted(item["path"] for item in expected)
    if found != listed:
        raise SystemExit(f"manifest file set mismatch: found={found}, listed={listed}")
    for item in expected:
        path = ROOT / item["path"]
        payload = path.read_bytes()
        if len(payload) != item["bytes"]:
            raise SystemExit(f"byte-size mismatch: {item['path']}")
        digest = hashlib.sha256(payload).hexdigest()
        if digest != item["sha256"]:
            raise SystemExit(f"SHA-256 mismatch: {item['path']}")
    print(f"LANE 3 MANIFEST OK: {len(expected)} files")


if __name__ == "__main__":
    main()
