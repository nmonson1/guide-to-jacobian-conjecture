#!/usr/bin/env python3
"""Copy unique untracked generated roots to a new verified run archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def records(root: Path, paths: list[str]) -> list[dict[str, object]]:
    result = []
    for relative_root in sorted(paths):
        directory = root / relative_root
        if not directory.is_dir():
            raise FileNotFoundError(directory)
        entries = sorted(
            item for item in directory.rglob("*") if item.is_symlink() or item.is_file()
        )
        for path in entries:
            if path.is_symlink():
                result.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "kind": "symlink",
                        "size_bytes": path.lstat().st_size,
                        "target": path.readlink().as_posix(),
                    }
                )
            else:
                result.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "kind": "file",
                        "size_bytes": path.stat().st_size,
                        "sha256": sha256(path),
                    }
                )
    return result


def tree_sha256(items: list[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for item in items:
        digest.update(str(item["path"]).encode())
        digest.update(b"\0")
        digest.update(str(item["kind"]).encode())
        digest.update(b"\0")
        digest.update(str(item["size_bytes"]).encode())
        digest.update(b"\0")
        digest.update(str(item.get("sha256", item.get("target"))).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def archive(
    *,
    inventory_path: Path,
    source_root: Path,
    destination: Path,
    archive_id: str | None = None,
) -> dict:
    if destination.exists():
        raise FileExistsError(destination)
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    paths = [
        item["path"]
        for item in inventory["untracked_generated"]["roots"]
        if item["requires_external_archive_before_removal"]
    ]
    if len(paths) != inventory["untracked_generated"]["unique_root_count"]:
        raise ValueError("inventory unique-root count does not match its records")
    source_records = records(source_root, paths)
    destination.mkdir(parents=True)
    for relative in paths:
        shutil.copytree(source_root / relative, destination / relative, symlinks=True)
    copied_records = records(destination, paths)
    if copied_records != source_records:
        raise RuntimeError("copied generated archive does not match its source")
    manifest = {
        "schema_version": 1,
        "archive_id": archive_id or f"{inventory['inventory_id']}-archive",
        "created_on": "2026-08-03",
        "source_repository": str(source_root),
        "source_baseline_commit": inventory["baseline_commit"],
        "source_inventory_id": inventory["inventory_id"],
        "source_inventory_sha256": sha256(inventory_path),
        "copied_roots": paths,
        "root_count": len(paths),
        "file_count": len(source_records),
        "regular_file_count": sum(item["kind"] == "file" for item in source_records),
        "symlink_count": sum(item["kind"] == "symlink" for item in source_records),
        "apparent_size_bytes": sum(int(item["size_bytes"]) for item in source_records),
        "content_tree_sha256": tree_sha256(source_records),
        "files": source_records,
    }
    with (destination / "manifest.json").open("x", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--archive-id")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = archive(
        inventory_path=args.inventory.resolve(),
        source_root=args.source_root.resolve(),
        destination=args.destination,
        archive_id=args.archive_id,
    )
    print(json.dumps({key: value for key, value in manifest.items() if key != "files"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
