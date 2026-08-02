#!/usr/bin/env python3
"""Reassemble and verify the split Lane 4 source archive."""
from __future__ import annotations

import hashlib
from pathlib import Path

STEM = "lane4-quartic-endgame-repairs-2026-08-02-v1.zip"
EXPECTED_SHA256 = "1880037bc946e81ec064108f0d67f264a45110bfca98c64ac99e5b7878832209"


def main() -> int:
    root = Path(__file__).resolve().parent
    parts = sorted(root.glob(f"{STEM}.part*"))
    if not parts:
        raise SystemExit(f"no {STEM}.part* files found beside this script")
    output = root / STEM
    digest = hashlib.sha256()
    with output.open("wb") as handle:
        for part in parts:
            data = part.read_bytes()
            handle.write(data)
            digest.update(data)
    actual = digest.hexdigest()
    if actual != EXPECTED_SHA256:
        output.unlink(missing_ok=True)
        raise SystemExit(f"SHA-256 mismatch: expected {EXPECTED_SHA256}, got {actual}")
    print(f"PASS: wrote {output.name}")
    print(f"SHA-256 {actual}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
