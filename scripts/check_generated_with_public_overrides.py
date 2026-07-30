#!/usr/bin/env python3
"""Prepare and check graph-generated pages plus pinned public corrections."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from generate_living_guide_v2 import PUBLIC_DOCS_DIR, ROOT, expected_outputs


OVERRIDE_DATA_DIR = "public-page-overrides-v1"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_relative(value: str, label: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"unsafe {label} path: {value!r}")
    return path


def apply_manifest(
    root: Path, outputs: dict[Path, str]
) -> tuple[dict[Path, str], dict[Path, tuple[str, str]], int, int]:
    override_root = root / "data" / OVERRIDE_DATA_DIR
    manifest_path = override_root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    required = {
        "schema_version",
        "release_id",
        "override_count",
        "overrides",
        "substitution_count",
        "substitutions",
    }
    if set(manifest) != required or manifest["schema_version"] != 1:
        raise ValueError(f"invalid public override manifest: {manifest_path}")

    entries = manifest["overrides"]
    substitutions = manifest["substitutions"]
    if manifest["override_count"] != len(entries):
        raise ValueError("public override manifest count mismatch")
    if manifest["substitution_count"] != len(substitutions):
        raise ValueError("public substitution manifest count mismatch")

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

    materializations: dict[Path, tuple[str, str]] = {}
    seen_substitutions: set[Path] = set()
    for entry in substitutions:
        if set(entry) != {"target", "old", "new"}:
            raise ValueError("invalid public substitution entry")
        target_rel = _safe_relative(entry["target"], "substitution target")
        target = (docs / target_rel).resolve()
        if not target.is_relative_to(docs):
            raise ValueError(f"substitution target leaves docs tree: {target_rel}")
        if target in seen_substitutions:
            raise ValueError(f"duplicate substitution target: {target_rel}")
        if target not in outputs:
            raise ValueError(f"substitution target is not graph-generated: {target_rel}")
        old = entry["old"]
        new = entry["new"]
        if not isinstance(old, str) or not isinstance(new, str) or not old or not new:
            raise ValueError(f"invalid substitution text for {target_rel}")
        original = outputs[target]
        if original.count(old) != 1:
            raise ValueError(
                f"substitution anchor occurs {original.count(old)} times in {target_rel}"
            )
        patched = original.replace(old, new)
        outputs[target] = patched
        materializations[target] = (original, patched)
        seen_substitutions.add(target)

    return outputs, materializations, len(entries), len(substitutions)


def check(root: Path) -> tuple[list[str], int, int, int]:
    outputs = expected_outputs(root)
    outputs, materializations, override_count, substitution_count = apply_manifest(
        root, outputs
    )
    failures: list[str] = []

    # Large catalogue pages remain graph-generated in the repository. Apply
    # narrow, anchor-checked substitutions in the build workspace so search and
    # deployment expose the corrected statement without copying an entire
    # catalogue into the override release.
    for path, (original, patched) in materializations.items():
        if not path.is_file():
            failures.append(f"missing substitution target: {path.relative_to(root)}")
            continue
        current = path.read_text(encoding="utf-8")
        if current == original:
            path.write_text(patched, encoding="utf-8")
        elif current != patched:
            failures.append(f"stale substitution target: {path.relative_to(root)}")

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
    return failures, len(outputs), override_count, substitution_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        failures, output_count, override_count, substitution_count = check(root)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if failures:
        print("Living-guide generation/override check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Living-guide generation check passed for {output_count} pages with "
        f"{override_count} hash-pinned public overrides and "
        f"{substitution_count} anchored catalogue substitution."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
