#!/usr/bin/env python3
"""Prepare a write-once handoff release with a repaired Lane 1 source."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANE_SLUG = "cubic-flatness-normalization-defects"
FORBIDDEN = ("/fss/", "/home/", "chatgpt.com/share", "INTAKE-", "sandbox:/")
UNIT_RE = re.compile(r"`(?P<unit>RMU-[A-Z0-9]+)`")
MANUSCRIPT_RE = re.compile(r"`manuscripts/(?P<path>[^`]+\.(?:tex|py|bib))`")
PRIVATE_AUDIT_NOTE = (
    "The Program 1 synthesis and precise provenance boundary are recorded in\n"
    "`registry/audit-v1/PROGRAM_1_HOLISTIC_SYNTHESIS_2026-08-02.md`."
)
PUBLIC_AUDIT_NOTE = (
    "The retained-unit pages and complete proof-source pages linked above are "
    "the public mathematical record for this lane."
)
TASK_HEADING = "\n## Tasks\n"
USEFUL_DELIVERABLE = """
## Useful deliverable

Return one self-contained mathematical artifact that either extracts a
genuine item from the five-part resolvent carrier above, proves that the
available hypotheses do not determine it, extends a transverse MCM model
through a closed threefold point, or supplies a Keller-specific vanishing
mechanism. State every added hypothesis and distinguish a local formal,
codimension-two, or computational conclusion from finite flatness and from
boundary completeness. A rigorous partial result on one carrier component is
useful; it need not close the whole lane.

## Tasks
"""


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _validate_public(text: str, *, source: Path) -> None:
    lowered = text.casefold()
    found = [item for item in FORBIDDEN if item.casefold() in lowered]
    if found:
        raise ValueError(f"{source}: forbidden public markers: {found}")


def _public_lane_source(source: str) -> str:
    source = UNIT_RE.sub(
        lambda match: (
            f"[`{match.group('unit')}`]"
            f"(../working-mathematics/units/{match.group('unit')}.md)"
        ),
        source,
    )
    source = MANUSCRIPT_RE.sub(
        lambda match: (
            f"[`manuscripts/{match.group('path')}`]"
            f"(../proof-sources/{Path(match.group('path')).with_suffix('.md').as_posix()})"
        ),
        source,
    )
    if source.count(PRIVATE_AUDIT_NOTE) != 1:
        raise ValueError("Lane 1 private audit note did not match exactly once")
    source = source.replace(PRIVATE_AUDIT_NOTE, PUBLIC_AUDIT_NOTE)
    if source.count(TASK_HEADING) != 1:
        raise ValueError("Lane 1 task heading did not match exactly once")
    return source.replace(TASK_HEADING, f"\n{USEFUL_DELIVERABLE}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, required=True)
    parser.add_argument("--lane1-source", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    base = args.base_dir.resolve()
    lane1_source = args.lane1_source.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    base_manifest_path = base / "manifest.json"
    base_manifest = _load(base_manifest_path)
    if base_manifest.get("brief_count") != 16:
        raise ValueError("base release must contain sixteen handoffs")
    if base_manifest.get("primary_entrypoint_count") != 10:
        raise ValueError("base release must contain ten primary entrypoints")
    briefs = base_manifest.get("briefs", [])
    if sum(item.get("program_slug") == LANE_SLUG for item in briefs) != 1:
        raise ValueError("base release must contain exactly one Lane 1 handoff")

    lane_text = _public_lane_source(lane1_source.read_text(encoding="utf-8"))
    lane_words = len(lane_text.split())
    if not 350 <= lane_words <= 2000:
        raise ValueError(f"Lane 1 word count outside useful handoff range: {lane_words}")

    prepared: list[tuple[str, bytes, dict[str, Any]]] = []
    for item in briefs:
        source_path = base / item["source"]
        base_payload = source_path.read_bytes()
        if (
            len(base_payload) != item["bytes"]
            or _sha256(base_payload) != item["sha256"]
        ):
            raise ValueError(f"base source does not match manifest: {source_path}")
        text = lane_text if item["program_slug"] == LANE_SLUG else base_payload.decode(
            "utf-8"
        )
        _validate_public(text, source=source_path)
        payload = text.encode("utf-8")
        prepared.append(
            (
                item["source"],
                payload,
                {
                    **item,
                    "sha256": _sha256(payload),
                    "bytes": len(payload),
                    "words": len(text.split()),
                },
            )
        )

    expected_markers = base_manifest.get("retained_math_v2_markers", [])
    found_markers = []
    marker_re = re.compile(
        r"<!-- retained-math-v2-selection:(?P<argument_id>[A-Z0-9-]+) -->"
    )
    for _, payload, item in prepared:
        for argument_id in marker_re.findall(payload.decode("utf-8")):
            found_markers.append(
                {
                    "program_slug": item["program_slug"],
                    "argument_id": argument_id,
                }
            )
    if found_markers != expected_markers:
        raise ValueError("retained-math v2 markers changed during Lane 1 repair")

    output.mkdir()
    for name, payload, _ in prepared:
        with (output / name).open("xb") as handle:
            handle.write(payload)
    manifest = {
        "schema_version": 3,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "base_release": {
            "release_id": base_manifest["release_id"],
            "manifest_sha256": _sha256(base_manifest_path.read_bytes()),
        },
        "brief_count": len(prepared),
        "primary_entrypoint_count": sum(
            bool(item["primary_entrypoint"]) for _, _, item in prepared
        ),
        "retained_math_v2_markers": expected_markers,
        "briefs": [item for _, _, item in prepared],
    }
    manifest_payload = (
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    with (output / "manifest.json").open("xb") as handle:
        handle.write(manifest_payload)
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "brief_count": len(prepared),
                "primary_entrypoint_count": manifest["primary_entrypoint_count"],
                "lane1_words": lane_words,
                "manifest_sha256": _sha256(manifest_payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
