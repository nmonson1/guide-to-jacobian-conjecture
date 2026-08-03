#!/usr/bin/env python3
"""Fetch and hash-check the public Program 6 computational supplement.

The archive is a published technical material of the active guide release.
It is downloaded only in CI, checked against the SHA-256 printed on the
technical-materials page, and expanded for comparison with the independently
reconstructed Lane 8 equations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import urllib.request
import zipfile


URL = (
    "https://nmonson1.github.io/guide-to-jacobian-conjecture/"
    "assets/technical-materials/06-plane-boundary-computational-supplement.zip"
)
EXPECTED_SHA256 = "4238149caa6e8a73723368e997b8c714a99258600268f14a008c5e514ecea585"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--listing", type=Path, required=True)
    args = parser.parse_args()

    archive = args.archive.resolve()
    output_dir = args.output_dir.resolve()
    listing_path = args.listing.resolve()
    if output_dir.exists():
        raise FileExistsError(output_dir)
    archive.parent.mkdir(parents=True, exist_ok=True)

    with urllib.request.urlopen(URL, timeout=180) as response, archive.open("wb") as target:
        shutil.copyfileobj(response, target)

    observed = sha256_file(archive)
    if observed != EXPECTED_SHA256:
        raise ValueError(
            f"Program 6 supplement SHA-256 mismatch: expected {EXPECTED_SHA256}, "
            f"observed {observed}"
        )

    with zipfile.ZipFile(archive) as bundle:
        bad_member = next(
            (
                name
                for name in bundle.namelist()
                if Path(name).is_absolute() or ".." in Path(name).parts
            ),
            None,
        )
        if bad_member is not None:
            raise ValueError(f"unsafe archive member: {bad_member}")
        bundle.extractall(output_dir)

    files = []
    for path in sorted(item for item in output_dir.rglob("*") if item.is_file()):
        files.append(
            {
                "path": str(path.relative_to(output_dir)),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    listing_path.parent.mkdir(parents=True, exist_ok=True)
    listing_path.write_text(
        json.dumps(
            {
                "schema": "program6-public-supplement-listing-v1",
                "url": URL,
                "archive_sha256": observed,
                "file_count": len(files),
                "files": files,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"verified {archive}: {observed}")
    print(f"extracted {len(files)} files to {output_dir}")
    print(f"listing -> {listing_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
