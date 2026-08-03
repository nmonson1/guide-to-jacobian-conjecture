#!/usr/bin/env python3
"""Prepare a write-once docs skeleton for the selected site release."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from generate_living_guide_v2 import PUBLIC_DOCS_DIR, expected_outputs


ROOT = Path(__file__).resolve().parents[1]
GENERATED_NAMESPACES = {
    Path("claims"),
    Path("collections"),
    Path("research/programs"),
    Path("research/handoffs"),
    Path("research/proof-sources"),
    Path("research/working-mathematics/programs"),
    Path("research/working-mathematics/units"),
}


def copy_static_entry(source: Path, target: Path) -> int:
    """Copy one scaffold entry without retaining checkout-relative symlinks."""
    if source.is_symlink():
        resolved = source.resolve(strict=True)
        target.parent.mkdir(parents=True, exist_ok=True)
        if resolved.is_dir():
            shutil.copytree(resolved, target, symlinks=False, copy_function=shutil.copy2)
            return sum(item.is_file() for item in target.rglob("*"))
        shutil.copy2(resolved, target)
        return 1
    if source.is_dir():
        target.mkdir(parents=True, exist_ok=True)
        return 0
    if source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        return 1
    return 0


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
        copied += copy_static_entry(source, target)
    print(
        f"Prepared {output.name} with {copied} static files; "
        f"reserved {len(generated)} generated paths."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
