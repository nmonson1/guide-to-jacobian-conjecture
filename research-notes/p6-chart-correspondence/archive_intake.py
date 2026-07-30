#!/usr/bin/env python3
"""Inventory the public Program 6 supplement without unpacking it wholesale.

The public supplement is a large ZIP.  This tool records a deterministic file
inventory, searches small text payloads for configured terms, and extracts only
explicitly selected or manifest-like text files.  It is intended as an intake
step for the chart-correspondence diagnostic, not as a mathematical verifier.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import shutil
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Sequence

TEXT_SUFFIXES = {
    ".c",
    ".cfg",
    ".csv",
    ".gp",
    ".json",
    ".log",
    ".m",
    ".md",
    ".magma",
    ".maple",
    ".mpl",
    ".py",
    ".sage",
    ".sh",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class SearchHit:
    path: str
    keyword: str
    line: int
    snippet: str

    def as_json(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "keyword": self.keyword,
            "line": self.line,
            "snippet": self.snippet,
        }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_member(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"unsafe archive path: {name!r}")
    return path


def read_config(path: Path | None) -> dict[str, Any]:
    if path is None:
        return {}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("archive intake config must be a JSON object")
    return value


def is_text_candidate(path: PurePosixPath, size: int, max_size: int) -> bool:
    return size <= max_size and path.suffix.casefold() in TEXT_SUFFIXES


def decode_text(payload: bytes) -> tuple[str, str]:
    try:
        return payload.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return payload.decode("utf-8", errors="replace"), "utf-8-replacement"


def compact_snippet(line: str, limit: int = 240) -> str:
    compact = " ".join(line.strip().split())
    return compact if len(compact) <= limit else compact[: limit - 1] + "…"


def compile_keywords(values: Iterable[Any]) -> list[tuple[str, re.Pattern[str]]]:
    patterns: list[tuple[str, re.Pattern[str]]] = []
    for value in values:
        if not isinstance(value, str) or not value:
            raise ValueError("keywords must be nonempty strings")
        patterns.append((value, re.compile(value, re.IGNORECASE)))
    return patterns


def selected_by_glob(name: str, globs: Sequence[str]) -> bool:
    return any(fnmatch.fnmatchcase(name, pattern) for pattern in globs)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--expected-sha256")
    args = parser.parse_args(argv)

    try:
        config = read_config(args.config)
        archive_digest = sha256(args.archive)
        if args.expected_sha256 and archive_digest != args.expected_sha256:
            raise ValueError(
                f"archive SHA-256 mismatch: {archive_digest} != {args.expected_sha256}"
            )

        max_text_size = int(config.get("max_text_file_bytes", 2_000_000))
        max_hits_per_file = int(config.get("max_hits_per_file", 100))
        max_extract_total = int(config.get("max_extract_total_bytes", 4_000_000))
        keywords = compile_keywords(config.get("keywords", []))
        extract_paths = config.get("extract_paths", [])
        extract_globs = config.get("extract_globs", [])
        if not isinstance(extract_paths, list) or not all(
            isinstance(value, str) for value in extract_paths
        ):
            raise ValueError("extract_paths must be a list of strings")
        if not isinstance(extract_globs, list) or not all(
            isinstance(value, str) for value in extract_globs
        ):
            raise ValueError("extract_globs must be a list of strings")
        requested = set(extract_paths)

        if args.output.exists():
            shutil.rmtree(args.output)
        args.output.mkdir(parents=True)

        inventory: list[dict[str, Any]] = []
        hits: list[SearchHit] = []
        keyword_file_counts: dict[str, int] = {keyword: 0 for keyword, _ in keywords}
        candidate_scores: dict[str, int] = {}
        extracted: list[dict[str, Any]] = []
        extraction_bytes = 0
        seen_paths: set[str] = set()

        with zipfile.ZipFile(args.archive) as archive:
            bad_crc = archive.testzip()
            if bad_crc is not None:
                raise ValueError(f"ZIP CRC failure in {bad_crc}")

            for info in sorted(archive.infolist(), key=lambda item: item.filename):
                member = normalized_member(info.filename)
                name = member.as_posix()
                if name in seen_paths:
                    raise ValueError(f"duplicate archive path: {name}")
                seen_paths.add(name)
                record = {
                    "path": name,
                    "is_dir": info.is_dir(),
                    "size": info.file_size,
                    "compressed_size": info.compress_size,
                    "crc32": f"{info.CRC:08x}",
                    "suffix": member.suffix.casefold(),
                }
                inventory.append(record)
                if info.is_dir():
                    continue

                filename_score = sum(
                    1 for keyword, pattern in keywords if pattern.search(name)
                )
                if filename_score:
                    candidate_scores[name] = 10 * filename_score

                text: str | None = None
                encoding: str | None = None
                if is_text_candidate(member, info.file_size, max_text_size):
                    payload = archive.read(info)
                    text, encoding = decode_text(payload)
                    file_hit_count = 0
                    matched_keywords: set[str] = set()
                    for line_number, line in enumerate(text.splitlines(), start=1):
                        for keyword, pattern in keywords:
                            if pattern.search(line):
                                if file_hit_count < max_hits_per_file:
                                    hits.append(
                                        SearchHit(
                                            path=name,
                                            keyword=keyword,
                                            line=line_number,
                                            snippet=compact_snippet(line),
                                        )
                                    )
                                file_hit_count += 1
                                matched_keywords.add(keyword)
                    for keyword in matched_keywords:
                        keyword_file_counts[keyword] += 1
                    if matched_keywords:
                        candidate_scores[name] = candidate_scores.get(name, 0) + len(
                            matched_keywords
                        )

                should_extract = name in requested or selected_by_glob(
                    name, extract_globs
                )
                if should_extract:
                    if not is_text_candidate(member, info.file_size, max_text_size):
                        extracted.append(
                            {
                                "path": name,
                                "status": "skipped-nontext-or-too-large",
                                "size": info.file_size,
                            }
                        )
                        continue
                    if extraction_bytes + info.file_size > max_extract_total:
                        extracted.append(
                            {
                                "path": name,
                                "status": "skipped-total-byte-cap",
                                "size": info.file_size,
                            }
                        )
                        continue
                    if text is None or encoding is None:
                        text, encoding = decode_text(archive.read(info))
                    destination = args.output / "selected" / Path(*member.parts)
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_text(text, encoding="utf-8")
                    extraction_bytes += info.file_size
                    extracted.append(
                        {
                            "path": name,
                            "status": "extracted",
                            "size": info.file_size,
                            "decoded_as": encoding,
                            "output": str(destination.relative_to(args.output)),
                        }
                    )

        missing_requested = sorted(requested - seen_paths)
        if missing_requested:
            raise ValueError(
                "requested archive members are absent: " + ", ".join(missing_requested)
            )

        ranked_candidates = [
            {"path": path, "score": score}
            for path, score in sorted(
                candidate_scores.items(), key=lambda item: (-item[1], item[0])
            )
        ]
        metadata = {
            "schema_version": 1,
            "archive": args.archive.name,
            "archive_sha256": archive_digest,
            "entry_count": len(inventory),
            "file_count": sum(not item["is_dir"] for item in inventory),
            "uncompressed_bytes": sum(item["size"] for item in inventory),
            "keyword_file_counts": keyword_file_counts,
            "hit_count": len(hits),
            "extracted_bytes": extraction_bytes,
        }
        write_json(args.output / "inventory.json", {**metadata, "entries": inventory})
        write_json(
            args.output / "keyword_hits.json",
            {
                **metadata,
                "ranked_candidates": ranked_candidates,
                "hits": [hit.as_json() for hit in hits],
            },
        )
        write_json(
            args.output / "extraction_manifest.json",
            {**metadata, "members": extracted},
        )

        lines = [
            "# Program 6 supplement archive intake",
            "",
            "This report is a deterministic inventory and keyword scan. It is not a",
            "mathematical verification of any payload calculation.",
            "",
            f"- Archive SHA-256: `{archive_digest}`",
            f"- Archive entries: {len(inventory)}",
            f"- Files: {metadata['file_count']}",
            f"- Uncompressed bytes: {metadata['uncompressed_bytes']}",
            f"- Recorded keyword hits: {len(hits)}",
            f"- Extracted text bytes: {extraction_bytes}",
            "",
            "## Highest-ranked candidate files",
            "",
            "| Rank | Score | Archive path |",
            "| ---: | ---: | --- |",
        ]
        for index, item in enumerate(ranked_candidates[:50], start=1):
            lines.append(f"| {index} | {item['score']} | `{item['path']}` |")
        lines.extend(["", "## Extracted members", ""])
        if extracted:
            for item in extracted:
                lines.append(
                    f"- `{item['path']}` — {item['status']} ({item['size']} bytes)"
                )
        else:
            lines.append("No members were selected for extraction.")
        (args.output / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    except (OSError, ValueError, TypeError, zipfile.BadZipFile, json.JSONDecodeError) as exc:
        print(f"archive_intake: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
