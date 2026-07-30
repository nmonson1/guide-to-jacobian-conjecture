#!/usr/bin/env python3
"""Check graph-generated pages plus hash-pinned public correction overrides."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from generate_living_guide_v2 import PUBLIC_DOCS_DIR, ROOT, expected_outputs


OVERRIDE_DATA_DIR = "public-page-overrides-v1"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_relative(value: str, label: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"unsafe {label} path: {value!r}")
    return path


def apply_overrides(root: Path, outputs: dict[Path, str]) -> tuple[dict[Path, str], int]:
    override_root = root / "data" / OVERRIDE_DATA_DIR
    manifest_path = override_root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    required = {"schema_version", "release_id", "override_count", "overrides"}
    if set(manifest) != required or manifest["schema_version"] != 1:
        raise ValueError(f"invalid public override manifest: {manifest_path}")
    entries = manifest["overrides"]
    if manifest["override_count"] != len(entries):
        raise ValueError("public override manifest count mismatch")

    docs = (root / PUBLIC_DOCS_DIR).resolve()
    seen_targets: set[Path] = set()
    seen_sources: set[Path] = set()
    for entry in entries:
        if set(entry) != {"target", "source", "sha256"}:
            raise ValueError("invalid public override entry")
        target_rel = _safe_relative(entry["target"], "override target")
        source_rel = _safe_relative(entry["source"], "override source")
        target = (docs / target_rel).resolve()
        source = (override_root / source_rel).resolve()
        if not target.is_relative_to(docs):
            raise ValueError(f"override target leaves docs tree: {target_rel}")
        if not source.is_relative_to(override_root.resolve()):
            raise ValueError(f"override source leaves data tree: {source_rel}")
        if target in seen_targets:
            raise ValueError(f"duplicate override target: {target_rel}")
        if source in seen_sources:
            raise ValueError(f"duplicate override source: {source_rel}")
        if target not in outputs:
            raise ValueError(f"override target is not graph-generated: {target_rel}")
        if not source.is_file():
            raise ValueError(f"missing override source: {source_rel}")
        found = _sha256(source)
        if found != entry["sha256"]:
            raise ValueError(
                f"override source digest mismatch for {source_rel}: "
                f"expected {entry['sha256']}, found {found}"
            )
        outputs[target] = source.read_text(encoding="utf-8")
        seen_targets.add(target)
        seen_sources.add(source)
    return outputs, len(entries)


def check(root: Path) -> tuple[list[str], int, int]:
    outputs = expected_outputs(root)
    outputs, override_count = apply_overrides(root, outputs)
    failures: list[str] = []
    for path, expected in sorted(outputs.items()):
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(f"stale generated file: {path.relative_to(root)}")

    expected_paths = set(outputs)
    for directory in (
        root / PUBLIC_DOCS_DIR / "claims",
        root / PUBLIC_DOCS_DIR / "collections",
        root / PUBLIC_DOCS_DIR / "research/programs",
        root / PUBLIC_DOCS_DIR / "research/handoffs",
    ):
        for path in directory.glob("*.md"):
            if path not in expected_paths:
                failures.append(f"unexpected generated file: {path.relative_to(root)}")
    return failures, len(outputs), override_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        failures, output_count, override_count = check(root)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if failures:
        print("Living-guide generation/override check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Living-guide generation check passed for {output_count} pages "
        f"with {override_count} hash-pinned public overrides."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
