#!/usr/bin/env python3
"""Hash generated site roots and classify untracked candidates conservatively."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

from inventory_active_tree import generated_root, repository_inventory


ROOT = Path(__file__).resolve().parents[1]


def git_lines(root: Path, *args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def directory_record(path: Path) -> dict[str, object]:
    entries = sorted(
        item for item in path.rglob("*") if item.is_symlink() or item.is_file()
    )
    digest = hashlib.sha256()
    size = 0
    file_count = 0
    symlink_count = 0
    for item in entries:
        relative = item.relative_to(path).as_posix()
        if item.is_symlink():
            kind = "symlink"
            item_size = item.lstat().st_size
            item_digest = hashlib.sha256(item.readlink().as_posix().encode()).hexdigest()
            symlink_count += 1
        else:
            kind = "file"
            item_size = item.stat().st_size
            item_digest = sha256(item)
            file_count += 1
        size += item_size
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(kind.encode())
        digest.update(b"\0")
        digest.update(str(item_size).encode())
        digest.update(b"\0")
        digest.update(item_digest.encode())
        digest.update(b"\n")
    return {
        "file_count": file_count,
        "symlink_count": symlink_count,
        "apparent_size_bytes": size,
        "content_tree_sha256": digest.hexdigest(),
    }


def untracked_generated_roots(root: Path) -> list[str]:
    status = git_lines(root, "status", "--porcelain=v1", "--untracked-files=normal")
    return sorted(
        {
            candidate
            for line in status
            if line.startswith("?? ")
            if (candidate := generated_root(line[3:].rstrip("/"))) is not None
        }
    )


def worktree_state(root: Path, baseline: str) -> dict[str, list[dict[str, object]]]:
    raw = subprocess.run(
        ["git", "worktree", "list", "--porcelain"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    records = []
    current: dict[str, object] = {}
    for line in [*raw.splitlines(), ""]:
        if not line:
            if current:
                path = Path(str(current["path"]))
                current["exists"] = path.exists()
                if path.exists():
                    current["dirty"] = bool(
                        git_lines(path, "status", "--porcelain=v1", "--untracked-files=normal")
                    )
                records.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        if key == "worktree":
            current["path"] = value
        elif key == "HEAD":
            current["head"] = value
        elif key == "branch":
            current["branch"] = value.removeprefix("refs/heads/")
        elif key in {"detached", "prunable", "locked"}:
            current[key] = value or True

    branches = []
    for line in git_lines(
        root,
        "for-each-ref",
        "--format=%(refname:short)|%(objectname)",
        "refs/heads",
    ):
        name, tip = line.split("|", 1)
        ancestor = subprocess.run(
            ["git", "merge-base", "--is-ancestor", tip, baseline],
            cwd=root,
            check=False,
        ).returncode == 0
        left, right = git_lines(
            root,
            "rev-list",
            "--left-right",
            "--count",
            f"{baseline}...{tip}",
        )[0].split()
        branches.append(
            {
                "branch": name,
                "tip": tip,
                "tip_is_ancestor_of_baseline": ancestor,
                "baseline_only_commits": int(left),
                "branch_only_commits": int(right),
            }
        )
    return {"worktrees": records, "branches": sorted(branches, key=lambda item: item["branch"])}


def build_recoverability(root: Path, untracked_root: Path) -> dict:
    active = repository_inventory(root)
    tracked_roots = sorted(active["root_details"])
    tracked_records = {}
    digest_to_tracked: dict[str, list[str]] = {}
    for relative in tracked_roots:
        record = directory_record(root / relative)
        record["git_tree_oid"] = git_lines(root, "rev-parse", f"HEAD:{relative}")[0]
        tracked_records[relative] = record
        digest_to_tracked.setdefault(str(record["content_tree_sha256"]), []).append(relative)

    untracked_records = []
    for relative in untracked_generated_roots(untracked_root):
        record = directory_record(untracked_root / relative)
        duplicates = digest_to_tracked.get(str(record["content_tree_sha256"]), [])
        record.update(
            {
                "path": relative,
                "exact_tracked_duplicates": duplicates,
                "requires_external_archive_before_removal": not duplicates,
            }
        )
        untracked_records.append(record)

    baseline = str(active["baseline_commit"])
    tag = subprocess.run(
        ["git", "rev-parse", "--verify", "refs/tags/pre-compaction-public-v49-20260803^{commit}"],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    return {
        "schema_version": 2,
        "inventory_id": "public-compaction-preflight-f6a353f-20260803-v2",
        "created_on": "2026-08-03",
        "mode": "inventory_only_no_mutation",
        "baseline_commit": baseline,
        "site_release_id": active["site_release_id"],
        "untracked_source_checkout": str(untracked_root),
        "recovery_tag": {
            "name": "pre-compaction-public-v49-20260803",
            "commit": tag.stdout.strip() if tag.returncode == 0 else None,
        },
        "selected_allowlist": {
            "docs_root": active["selected"]["docs_root"],
            "data_roots": active["selected"]["data_roots"],
        },
        "tracked_generated": {
            "root_count": len(tracked_records),
            "selected_root_count": 1 + len(active["selected"]["data_roots"]),
            "inactive_root_count": active["inactive_tracked"]["root_count"],
            "selected_tracked_files": active["selected"]["tracked_files"],
            "inactive_tracked_files": active["inactive_tracked"]["tracked_files"],
            "selected_apparent_size_bytes": active["selected"]["apparent_size_bytes"],
            "inactive_apparent_size_bytes": active["inactive_tracked"]["apparent_size_bytes"],
            "inactive_roots": active["inactive_tracked"]["roots"],
            "root_records": tracked_records,
        },
        "untracked_generated": {
            "root_count": len(untracked_records),
            "unique_root_count": sum(
                bool(item["requires_external_archive_before_removal"])
                for item in untracked_records
            ),
            "roots": untracked_records,
        },
        "worktree_and_branch_state": worktree_state(root, baseline),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--untracked-source-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = build_recoverability(args.root.resolve(), args.untracked_source_root.resolve())
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as handle:
            handle.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
