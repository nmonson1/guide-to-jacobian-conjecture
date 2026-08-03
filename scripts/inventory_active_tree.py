#!/usr/bin/env python3
"""Inventory selected and inactive generated site-release trees."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from site_state import load_site_state


ROOT = Path(__file__).resolve().parents[1]


def selected_roots(state: dict[str, Any]) -> tuple[str, set[str]]:
    """Return the selected docs root and selected data roots."""
    docs_root = state["docs_dir"]
    data_roots = {
        f"data/{value['data_dir']}"
        for value in state.values()
        if isinstance(value, dict) and isinstance(value.get("data_dir"), str)
    }
    return docs_root, data_roots


def generated_root(path: str) -> str | None:
    """Map a repository path to its generated docs or data tree."""
    parts = Path(path).parts
    if not parts:
        return None
    if parts[0].startswith("docs-v"):
        return parts[0]
    if len(parts) >= 2 and parts[0] == "data":
        return "/".join(parts[:2])
    return None


def build_inventory(
    *,
    state: dict[str, Any],
    commit: str,
    tracked_paths: Iterable[str],
    untracked_paths: Iterable[str],
    sizes: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Build a deterministic compaction inventory from repository paths."""
    docs_root, data_roots = selected_roots(state)
    selected = {docs_root, *data_roots}
    counts: Counter[str] = Counter()
    byte_counts: Counter[str] = Counter()
    for path in tracked_paths:
        root = generated_root(path)
        if root is None:
            continue
        counts[root] += 1
        if sizes is not None:
            byte_counts[root] += sizes.get(path, 0)

    tracked_roots = set(counts)
    missing_selected = sorted(selected - tracked_roots)
    if missing_selected:
        raise ValueError(f"selected generated roots are not tracked: {missing_selected}")

    untracked_roots = sorted(
        {
            root
            for path in untracked_paths
            if (root := generated_root(path)) is not None
        }
    )
    inactive = sorted(tracked_roots - selected)
    return {
        "schema_version": 1,
        "baseline_commit": commit,
        "site_release_id": state["release_id"],
        "selected": {
            "docs_root": docs_root,
            "data_roots": sorted(data_roots),
            "tracked_files": sum(counts[root] for root in selected),
            "apparent_size_bytes": sum(byte_counts[root] for root in selected),
        },
        "inactive_tracked": {
            "roots": inactive,
            "root_count": len(inactive),
            "tracked_files": sum(counts[root] for root in inactive),
            "apparent_size_bytes": sum(byte_counts[root] for root in inactive),
        },
        "untracked_generated_candidates": {
            "roots": untracked_roots,
            "root_count": len(untracked_roots),
        },
        "root_details": {
            root: {
                "selected": root in selected,
                "tracked_files": counts[root],
                "apparent_size_bytes": byte_counts[root],
            }
            for root in sorted(tracked_roots)
        },
        "policy": {
            "retain_on_main": "Only the selected docs root and selected data roots.",
            "archive": "Inactive tracked roots remain recoverable through the baseline tag and Git history.",
            "remove_after_review": "Untracked generated candidates may be removed only after confirming that no active lane owns them.",
        },
    }


def git_lines(root: Path, *args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def repository_inventory(root: Path) -> dict[str, Any]:
    state = load_site_state(root)
    tracked = git_lines(root, "ls-files")
    status = git_lines(root, "status", "--porcelain=v1", "--untracked-files=normal")
    untracked = [line[3:].rstrip("/") for line in status if line.startswith("?? ")]
    sizes = {
        path: (root / path).stat().st_size
        for path in tracked
        if (root / path).is_file()
    }
    commit = git_lines(root, "rev-parse", "HEAD")[0]
    return build_inventory(
        state=state,
        commit=commit,
        tracked_paths=tracked,
        untracked_paths=untracked,
        sizes=sizes,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    inventory = repository_inventory(args.root.resolve())
    rendered = json.dumps(inventory, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        if args.output.exists():
            raise FileExistsError(f"refusing to overwrite {args.output}")
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
