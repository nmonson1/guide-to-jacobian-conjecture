#!/usr/bin/env python3
"""Create a write-once Living Guide scaffold for a new generated docs tree."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

STATIC_FILES = (
    "about.md",
    "counterexample.md",
    "geometry.md",
    "index.md",
    "plane-case.md",
    "robots.txt",
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-docs", type=Path, required=True)
    parser.add_argument("--output-docs", type=Path, required=True)
    parser.add_argument("--omit-technical-materials", action="store_true")
    args = parser.parse_args()

    source = args.source_docs.resolve()
    output = args.output_docs.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    missing = [
        name for name in (*STATIC_FILES, "assets") if not (source / name).exists()
    ]
    if missing:
        raise FileNotFoundError(f"source scaffold is incomplete: {missing}")

    output.mkdir()
    for name in STATIC_FILES:
        shutil.copy2(source / name, output / name)
    ignore = None
    if args.omit_technical_materials:
        ignore = shutil.ignore_patterns("technical-materials")
    shutil.copytree(
        source / "assets",
        output / "assets",
        symlinks=True,
        copy_function=shutil.copy2,
        ignore=ignore,
    )
    print(f"Prepared static scaffold at {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
