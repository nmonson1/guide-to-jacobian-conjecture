#!/usr/bin/env python3
"""Extract and hash-check the public Lane 8 executable source packets.

The current public handoff stores the small queue programs in HTML-escaped
``<pre><code>`` blocks and the raw-support reconstruction in fenced Markdown blocks.
This helper recovers those sources without copying their mathematics into a
second source of truth.

The packet-level hashes and the per-member hashes below are the values in the
active v20 handoff manifest on the branch point used by this research packet.
A source release change therefore fails loudly and requires an explicit audit.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import sys
from typing import Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

EXPECTED_PACKET_SHA256 = (
    "d32d25c16a30b9c36ae70628e7d7b7060059684b28f459a37b94a232253b3cc6"
)
EXPECTED_RECONSTRUCTION_SHA256 = (
    "8f3f5e262143a2a7b3ff8cbab5a61ecaba37f92a88996f7da411ac19085fb016"
)

QUEUE_PREFIX = "lane8-proof-queue-20260802-v1/"
QUEUE_MEMBERS = {
    QUEUE_PREFIX + "lane8-proof-queue-repair.md": (
        "bdbe6c5557e93c3dbafac75ffbf3c833eb22d5988af9e3f7bfcbdd4b040b94f0"
    ),
    QUEUE_PREFIX + "check_queue.py": (
        "e1b6556645ff74e18ce04600f1d1e5ff7bcbe30e4dfeaa9ec53cadbe7b32320e"
    ),
    QUEUE_PREFIX + "full_early_layer_reduction.py": (
        "ed4a150374eb969e19bf8601f8f4529edae57fb457f9aae9211997fb6f83bd95"
    ),
    QUEUE_PREFIX + "quintic_face_reconstruction.py": (
        "e48869fb09d7afcc3c1ae08a604c7656efadf0c3588c0fca82a42817dfaf8c1f"
    ),
    QUEUE_PREFIX + "truncated_support_certificate.py": (
        "40daac940f6c82e76a3679495e14cd0fcadfe5a926b3053eeff2cab879401da5"
    ),
    QUEUE_PREFIX + "queue.seed.json": (
        "a55e0c1aaf49d834ec0004c14f64e0ba04d8d969d1af9cde5eef01da4ea28743"
    ),
    QUEUE_PREFIX + "truncated_support_certificate.json": (
        "f086c7eca67d51f3c48fd6311c55e8fe5012a8b1373ff6eae4746fd4c3fec6ac"
    ),
}

RAW_SECTIONS = {
    "Exact quintic-field relations": (
        "degree-twenty-one/raw-support-reconstruction/"
        "belyi_exact_field_relations.json"
    ),
    "Pinned expected invariants": (
        "degree-twenty-one/raw-support-reconstruction/"
        "raw_reconstruction_expected.json"
    ),
    "Exact quintic-field helper": (
        "degree-296-compact/scripts/quintic_field_fast.py"
    ),
    "Complete reconstruction program": (
        "degree-twenty-one/raw-support-reconstruction/"
        "rebuild_lower_face_reduction.py"
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def active_model_handoff_dir(repository_root: Path) -> Path:
    state = json.loads((repository_root / "site-state.json").read_text(encoding="utf-8"))
    data_dir = state["model_briefs"]["data_dir"]
    return repository_root / "data" / data_dir


def verify_file_hash(path: Path, expected: str) -> None:
    observed = sha256_bytes(path.read_bytes())
    if observed != expected:
        raise ValueError(
            f"source packet hash mismatch for {path}: expected {expected}, "
            f"observed {observed}"
        )


def newline_variants(decoded: str) -> list[str]:
    """Return the wrapper-induced newline variants used by public packets."""

    variants = [decoded]
    if decoded.startswith("\n"):
        variants.append(decoded[1:])
    else:
        variants.append("\n" + decoded)
    snapshot = list(variants)
    for value in snapshot:
        core = value.rstrip("\n")
        variants.extend([core, core + "\n", core + "\n\n"])
    return list(dict.fromkeys(variants))


def extract_html_member(packet_text: str, member: str, expected_hash: str) -> str:
    heading = f"## `{member}`"
    heading_pos = packet_text.find(heading)
    if heading_pos < 0:
        raise ValueError(f"packet heading not found: {heading}")

    opening = re.search(
        r'<pre><code class="language-[^"]+">', packet_text[heading_pos:]
    )
    if opening is None:
        raise ValueError(f"opening code block not found for {member}")
    content_start = heading_pos + opening.end()
    content_end = packet_text.find("</code></pre>", content_start)
    if content_end < 0:
        raise ValueError(f"closing code block not found for {member}")

    decoded = html.unescape(packet_text[content_start:content_end])
    for candidate in newline_variants(decoded):
        if sha256_text(candidate) == expected_hash:
            return candidate

    observed = [sha256_text(candidate) for candidate in newline_variants(decoded)]
    raise ValueError(
        f"SHA-256 mismatch for {member}: expected {expected_hash}; "
        f"candidate hashes were {observed}"
    )


def extract_fenced_section(page_text: str, heading_text: str) -> str:
    heading = f"## {heading_text}"
    heading_pos = page_text.find(heading)
    if heading_pos < 0:
        raise ValueError(f"reconstruction heading not found: {heading}")

    opening = re.search(r"```[^\n]*\n", page_text[heading_pos:])
    if opening is None:
        raise ValueError(f"opening fenced block not found after {heading}")
    content_start = heading_pos + opening.end()
    content_end = page_text.find("\n```", content_start)
    if content_end < 0:
        raise ValueError(f"closing fenced block not found after {heading}")
    return page_text[content_start:content_end].rstrip("\n") + "\n"


def write_text_exact(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="")


def selected_members(requested: Iterable[str]) -> list[str]:
    values = list(requested)
    return values if values else list(QUEUE_MEMBERS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository-root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "members",
        nargs="*",
        help="optional queue packet members; defaults to every pinned member",
    )
    args = parser.parse_args()

    repository_root = args.repository_root.resolve()
    handoff_dir = active_model_handoff_dir(repository_root)
    packet_path = handoff_dir / "lane-8-source-packet.md"
    reconstruction_path = handoff_dir / "lane-8-reconstruction-input.md"

    verify_file_hash(packet_path, EXPECTED_PACKET_SHA256)
    verify_file_hash(reconstruction_path, EXPECTED_RECONSTRUCTION_SHA256)

    packet_text = packet_path.read_text(encoding="utf-8")
    reconstruction_text = reconstruction_path.read_text(encoding="utf-8")
    output_dir = args.output_dir.resolve()
    manifest: dict[str, object] = {
        "schema": "lane8-public-source-extraction-v1",
        "source_packet": {
            "path": str(packet_path.relative_to(repository_root)),
            "sha256": EXPECTED_PACKET_SHA256,
        },
        "reconstruction_packet": {
            "path": str(reconstruction_path.relative_to(repository_root)),
            "sha256": EXPECTED_RECONSTRUCTION_SHA256,
        },
        "files": [],
    }

    for member in selected_members(args.members):
        if member not in QUEUE_MEMBERS:
            raise KeyError(f"unknown queue member: {member}")
        content = extract_html_member(packet_text, member, QUEUE_MEMBERS[member])
        destination = output_dir / "queue" / Path(member).name
        write_text_exact(destination, content)
        manifest["files"].append(
            {
                "source": member,
                "destination": str(destination.relative_to(output_dir)),
                "sha256": sha256_text(content),
                "bytes": len(content.encode("utf-8")),
            }
        )
        print(f"{member}: {sha256_text(content)} -> {destination}")

    for heading, relative_destination in RAW_SECTIONS.items():
        content = extract_fenced_section(reconstruction_text, heading)
        destination = output_dir / relative_destination
        write_text_exact(destination, content)
        manifest["files"].append(
            {
                "source": f"lane-8-reconstruction-input.md#{heading}",
                "destination": str(destination.relative_to(output_dir)),
                "sha256": sha256_text(content),
                "bytes": len(content.encode("utf-8")),
            }
        )
        print(f"{heading}: {sha256_text(content)} -> {destination}")

    manifest_path = output_dir / "extraction-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )
    print(f"manifest -> {manifest_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
