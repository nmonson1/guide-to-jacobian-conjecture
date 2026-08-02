#!/usr/bin/env python3
"""Extract hash-pinned Lane 7 source files embedded in the public packet.

The public packet stores source files as HTML-escaped code blocks. This helper
recovers their exact bytes and verifies the SHA-256 values printed in the
packet header. It deliberately reads the published packet instead of copying
large polynomial matrices into a second source of truth.
"""

from __future__ import annotations

import argparse
import hashlib
import html
from pathlib import Path
import re
import sys

PACKET = Path("data/model-handoffs-v19-20260802a/lane-7-source-packet.md")
PREFIX = "lane7-split-incidence-20260802-v1/"
EXPECTED_SHA256 = {
    PREFIX + "lane7-split-incidence-theorem.md": "c94402f0c8850490ccc0e9cadeeffc2d400b5dd24de4e0672b59db436fb02f1e",
    PREFIX + "reconstruct_matrices.py": "b6bbbbec46eeffc89f1f535cfb859d3bcb1f10b1debe39217af49b7e76fd824f",
    PREFIX + "verify_split_incidence_theorem.py": "dadd947874d8b1967a39e55e39c64b4c549574d32523d0440c4cb6ef09369495",
    PREFIX + "verify_split_determinants.py": "ca1c168da85e42dc27a19bbf40c93b5e4185f19b3ecadb2899d5f1375ebc0319",
    PREFIX + "collision_residual_matrix_M.json": "4e1a014a6616a990ac50d255fb7426a9f8ae1d06cbf5066ba52c8415da63cbda",
    PREFIX + "Hv10_split_matrix_factorization.json": "a251278a145ab0cfcf249809267edb2d6529738684b5136ec5faef62c7aa3dfb",
    PREFIX + "verify_split_incidence_report.json": "f0a78dce8f1f7f65a92f0d22267dfe143cc1828fbe6f2f435644276b8f505264",
    PREFIX + "verify_split_determinants_report.json": "e5b108357cbb96c0b0e979f0242dd8f6c308cd521eb7f01827a8cd8dc6ca9421",
}


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _candidate_exact_blocks(decoded: str) -> list[str]:
    """Return newline variants introduced by the packet's HTML wrapper."""
    core = decoded
    variants = [core]
    if core.startswith("\n"):
        variants.append(core[1:])
    else:
        variants.append("\n" + core)
    snapshot = list(variants)
    for value in snapshot:
        variants.extend(
            [
                value.rstrip("\n"),
                value.rstrip("\n") + "\n",
                value.rstrip("\n") + "\n\n",
            ]
        )
    return list(dict.fromkeys(variants))


def extract_member(packet_text: str, member: str) -> str:
    if member not in EXPECTED_SHA256:
        raise KeyError(f"unknown packet member: {member}")

    heading = f"## `{member}`"
    heading_pos = packet_text.find(heading)
    if heading_pos < 0:
        raise ValueError(f"packet heading not found: {heading}")

    open_match = re.search(
        r'<pre><code class="language-[^"]+">', packet_text[heading_pos:]
    )
    if open_match is None:
        raise ValueError(f"opening code block not found for {member}")
    content_start = heading_pos + open_match.end()
    content_end = packet_text.find("</code></pre>", content_start)
    if content_end < 0:
        raise ValueError(f"closing code block not found for {member}")

    decoded = html.unescape(packet_text[content_start:content_end])
    expected = EXPECTED_SHA256[member]
    for candidate in _candidate_exact_blocks(decoded):
        if _sha256(candidate) == expected:
            return candidate

    observed = [_sha256(candidate) for candidate in _candidate_exact_blocks(decoded)]
    raise ValueError(
        f"SHA-256 mismatch for {member}: expected {expected}; "
        f"newline-variant hashes were {observed}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=Path, default=PACKET)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument(
        "members",
        nargs="*",
        default=list(EXPECTED_SHA256),
        help="packet members to extract; defaults to all Lane 7 members",
    )
    args = parser.parse_args()

    packet_text = args.packet.read_text(encoding="utf-8")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for member in args.members:
        content = extract_member(packet_text, member)
        destination = args.output_dir / Path(member).name
        destination.write_text(content, encoding="utf-8", newline="")
        print(f"{member}: {_sha256(content)} -> {destination}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
