#!/usr/bin/env python3
"""Recover the public Lane 9/F2 text packet from the Program 6 ZIP archive.

The archive is already committed in the public repository but is too large for
ordinary code browsing.  This utility performs a deterministic, hash-pinned
scan and extracts only small UTF-8 text members relevant to Lane 9.  It never
constructs matrices that are not present in the archive.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

TEXT_SUFFIXES = {
    ".py",
    ".sage",
    ".m",
    ".md",
    ".tex",
    ".txt",
    ".json",
    ".log",
    ".csv",
    ".tsv",
}
MAX_TEXT_BYTES = 2_000_000

CONTENT_PATTERNS: Mapping[str, re.Pattern[str]] = {
    "f2": re.compile(r"\bF_?2\b|degree[-_ ]?125", re.I),
    "c5": re.compile(r"\bC_?5\b|cyclic\s+(?:quotient|descent|character)", re.I),
    "complete_chain": re.compile(r"complete[-_ ]?chain", re.I),
    "wall_shear": re.compile(r"wall[-_ ]?shear|chart[-_ ]?correspondence", re.I),
    "quotient_translation": re.compile(r"Q\s*(?:\\mapsto|->|→)\s*Q\s*\+\s*16", re.I),
    "order_510_520_530": re.compile(r"(?:order|layer|weight)[-_ ]?(?:510|520|530)|\b(?:510|520|530)\b", re.I),
    "fresh_parameter": re.compile(r"fresh\s+parameters?|new\s+parameters?", re.I),
    "matrix_block": re.compile(r"(?:matrix|support)[-_ ]?(?:block|blocks)|block[-_ ]?matrix", re.I),
    "parameter_names": re.compile(r"PARAMETER_NAMES|t1_0|t4_0", re.I),
}

KNOWN_TERMINAL_BASENAMES = {
    "BOUNDARY_PROGRAM_README.md",
    "F2_degree125_boundary_seed.md",
    "F2_degree30_coefficient_system.json",
    "count_F2_terminal_dessins.py",
    "generate_F2_degree30_system.py",
    "next_complete_chain_queue.json",
    "terminal_boundary_gluing_program.md",
    "terminal_primary_belyi.py",
    "terminal_primary_belyi_reduction.md",
    "verify_post125_terminal_examples.py",
}
HIGH_ORDER_LABELS = {
    "order_510_520_530",
    "fresh_parameter",
    "wall_shear",
    "quotient_translation",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_relative_path(member: str) -> PurePosixPath:
    path = PurePosixPath(member)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"unsafe archive member: {member!r}")
    marker = "computational-supplement"
    if marker in path.parts:
        index = path.parts.index(marker)
        path = PurePosixPath(*path.parts[index + 1 :])
    return path


def line_and_snippet(text: str, start: int, end: int) -> tuple[int, str]:
    line = text.count("\n", 0, start) + 1
    left = max(0, start - 100)
    right = min(len(text), end + 300)
    snippet = " ".join(text[left:right].split())
    return line, snippet


def scan_text(text: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for label, pattern in CONTENT_PATTERNS.items():
        matches = list(pattern.finditer(text))
        if not matches:
            continue
        line, snippet = line_and_snippet(text, matches[0].start(), matches[0].end())
        hits.append(
            {
                "label": label,
                "count": len(matches),
                "first_line": line,
                "first_snippet": snippet,
            }
        )
    return hits


def should_extract(member: str, hits: Sequence[Mapping[str, Any]]) -> tuple[bool, list[str]]:
    path = PurePosixPath(member)
    reasons: list[str] = []
    terminal = "terminal-boundary" in path.parts
    basename = path.name
    if terminal and (basename in KNOWN_TERMINAL_BASENAMES or re.search(r"F_?2", basename, re.I)):
        reasons.append("named_terminal_F2_source")
    hit_labels = {str(hit["label"]) for hit in hits}
    for label in sorted(hit_labels & HIGH_ORDER_LABELS):
        reasons.append(f"content:{label}")
    if {"f2", "matrix_block"} <= hit_labels:
        reasons.append("content:f2+matrix_block")
    return bool(reasons), reasons


def is_endpoint_candidate(record: Mapping[str, Any]) -> bool:
    hit_labels = {str(hit["label"]) for hit in record["hits"]}
    return bool(
        {"order_510_520_530", "fresh_parameter"} & hit_labels
        or {"f2", "matrix_block"} <= hit_labels
    )


def recover(
    archive: Path,
    output_dir: Path,
    manifest_path: Path,
    expected_sha256: str | None = None,
) -> dict[str, Any]:
    archive_sha = sha256_file(archive)
    if expected_sha256 and archive_sha != expected_sha256:
        raise ValueError(
            f"archive SHA-256 mismatch: expected {expected_sha256}, got {archive_sha}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    matched: list[dict[str, Any]] = []
    extracted: list[dict[str, Any]] = []
    scanned_text_members = 0
    archive_member_count = 0

    with zipfile.ZipFile(archive) as handle:
        infos = sorted(handle.infolist(), key=lambda info: info.filename)
        archive_member_count = len(infos)
        for info in infos:
            if info.is_dir():
                continue
            path = PurePosixPath(info.filename)
            if path.suffix.lower() not in TEXT_SUFFIXES or info.file_size > MAX_TEXT_BYTES:
                continue
            scanned_text_members += 1
            raw = handle.read(info)
            text = raw.decode("utf-8", errors="replace")
            hits = scan_text(text)
            name_hit = bool(re.search(r"F_?2|lane[-_ ]?9|wall[-_ ]?shear", path.name, re.I))
            if not hits and not name_hit:
                continue
            extract, reasons = should_extract(info.filename, hits)
            record: dict[str, Any] = {
                "path": info.filename,
                "bytes": info.file_size,
                "sha256": sha256_bytes(raw),
                "hits": hits,
                "selected_for_extraction": extract,
                "selection_reasons": reasons,
            }
            matched.append(record)
            if extract:
                relative = safe_relative_path(info.filename)
                target = output_dir / Path(*relative.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
                extracted.append(
                    {
                        "archive_path": info.filename,
                        "output_path": target.relative_to(manifest_path.parent).as_posix(),
                        "bytes": info.file_size,
                        "sha256": sha256_bytes(raw),
                        "selection_reasons": reasons,
                    }
                )

    high_order_members = [
        str(record["path"]) for record in matched if is_endpoint_candidate(record)
    ]
    report = {
        "schema_version": 1,
        "archive": str(archive),
        "archive_sha256": archive_sha,
        "archive_member_count": archive_member_count,
        "scanned_text_member_count": scanned_text_members,
        "matched_member_count": len(matched),
        "extracted_member_count": len(extracted),
        "high_order_endpoint_candidate_count": len(high_order_members),
        "high_order_endpoint_candidate_members": high_order_members,
        "matched_members": matched,
        "extracted_members": extracted,
        "interpretation": (
            "Presence in this manifest means present in the pinned public ZIP. "
            "Absence means only that the declared filename/content scan found no "
            "small UTF-8 text member; it is not evidence about private sources."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-sha256")
    args = parser.parse_args(argv)
    try:
        recover(
            args.archive,
            args.output_dir,
            args.manifest,
            expected_sha256=args.expected_sha256,
        )
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"recover_lane9_public_archive: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
