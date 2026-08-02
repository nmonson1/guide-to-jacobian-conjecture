#!/usr/bin/env python3
"""Reassemble and optionally extract the Lane 2 source bundle."""
from __future__ import annotations

import argparse
import base64
import hashlib
from pathlib import Path
import zipfile

EXPECTED_SHA256 = "c77588de647cb2bfff5b9a080252144ea99e934c70b1eea9faafad5a91c424bf"
ARCHIVE_NAME = "lane2-prs-boundary-2026-08-02-v1.zip"
PART_GLOB = ARCHIVE_NAME + ".b64.part-*"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extract", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    parts = sorted(root.glob(PART_GLOB))
    if not parts:
        raise SystemExit(f"no parts matched {PART_GLOB}")

    encoded = b"".join(path.read_bytes() for path in parts)
    payload = base64.b64decode(encoded, validate=True)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"SHA-256 mismatch: expected {EXPECTED_SHA256}, got {digest}")

    archive = root / ARCHIVE_NAME
    archive.write_bytes(payload)
    print(f"wrote {archive.name} ({len(payload)} bytes)")
    print(f"sha256 {digest}")

    if args.extract:
        with zipfile.ZipFile(archive) as zf:
            bad = zf.testzip()
            if bad is not None:
                raise SystemExit(f"corrupt archive member: {bad}")
            zf.extractall(root)
        print("archive integrity passed and contents extracted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
