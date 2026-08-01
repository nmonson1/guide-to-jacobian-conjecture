#!/usr/bin/env python3
"""Prepare a write-once docs skeleton for the selected site release."""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

from generate_living_guide_v2 import PUBLIC_DOCS_DIR, expected_outputs


ROOT = Path(__file__).resolve().parents[1]
GENERATED_NAMESPACES = {
    Path("claims"),
    Path("collections"),
    Path("research/programs"),
    Path("research/handoffs"),
    Path("research/working-mathematics/programs"),
    Path("research/working-mathematics/units"),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-docs", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    base = args.base_docs.resolve()
    output = args.output_dir.resolve()
    selected = (ROOT / PUBLIC_DOCS_DIR).resolve()
    if output != selected:
        raise ValueError(f"output must equal selected docs tree: {selected}")
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if not base.is_dir():
        raise ValueError(f"base docs tree does not exist: {base}")

    generated = {
        path.relative_to(selected)
        for path in expected_outputs(ROOT)
    }
    output.mkdir()
    copied = 0
    for source in sorted(base.rglob("*")):
        relative = source.relative_to(base)
        target = output / relative
        if relative in generated or any(
            relative.is_relative_to(namespace)
            for namespace in GENERATED_NAMESPACES
        ):
            continue
        if source.is_symlink():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(os.readlink(source))
        elif source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied += 1
    print(
        f"Prepared {output.name} with {copied} static files; "
        f"reserved {len(generated)} generated paths."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
