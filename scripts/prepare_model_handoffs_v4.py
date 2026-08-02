#!/usr/bin/env python3
"""Prepare a write-once public release from the nine private v4 lane sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = ("/fss/", "/home/", "chatgpt.com/share", "INTAKE-", "sandbox:/")
UNIT_RE = re.compile(r"`(?P<unit>(?:RMU|JCG)-[A-Z0-9]+)`")
MANUSCRIPT_RE = re.compile(r"`manuscripts/(?P<path>[^`]+\.(?:tex|py|bib))`")
TASK_HEADING = "\n## Tasks\n"
PRIVATE_NOTES = (
    (
        "The Program 1 synthesis and precise provenance boundary are recorded in\n"
        "`registry/audit-v1/PROGRAM_1_HOLISTIC_SYNTHESIS_2026-08-02.md`.",
        "The retained-unit pages and complete proof-source pages linked above "
        "are the public mathematical record for this lane.",
    ),
    (
        "The manual reconciliation is in\n"
        "`registry/audit-v1/LANES_2_9_HOLISTIC_SYNTHESIS_2026-08-02.md`.",
        "The retained-unit and proof-source pages linked above are the public "
        "mathematical record for this lane.",
    ),
)
USEFUL_DELIVERABLE = """
## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks
"""
LANE6_SUMMARY = """  In the finite-slope classification, generic slopes and
`r=4` fail cubically.  The two slopes `4+-4sqrt(-3)` have 17-dimensional
cubic-lift fibres but fail quartically, with exact pairing `-1152`
(`RMU-5D8E0003`)."""
LANE6_MARKER = (
    "<!-- retained-math-v2-selection:ARG-RMU5D8E0003-FINITE-PLANE -->"
)
EXPECTED_V2_MARKERS = [
    {
        "program_slug": "homogeneous-realization-compression",
        "argument_id": "ARG-RMU5D8E0003-FINITE-PLANE",
    }
]
LANE5_OBJECTIVE_END = (
    "equivalence.  A budget for one determinant-arc presentation is not enough."
)
LANE5_PUBLIC_ROUTES = """

This lane overlaps the [low-degree program](minimum-degree-and-quartic-exclusions.md),
[stable moduli](stable-moduli.md), and
[plane boundary obstructions](plane-boundary-obstructions.md).  Those deeper
dossiers supply the surrounding proof and computation routes; the focused
page below gives the corrected finite frontier.
"""

LANES = (
    (1, "cubic-flatness-normalization-defects", "Cubic flatness and finite normalization defects"),
    (2, "boundary-completeness-torelli-at-infinity", "Boundary completeness and Torelli at infinity"),
    (3, "bounded-degree-deformation-modulus-onset", "Bounded-degree deformation and modulus onset"),
    (4, "quartic-endgame", "The quartic endgame"),
    (5, "intrinsic-degree-valuative-budgets", "Intrinsic degree and valuative budgets"),
    (6, "homogeneous-realization-compression", "Homogeneous realization and compression"),
    (7, "five-dimensional-collision-geometry", "Five-dimensional collision geometry"),
    (8, "plane-newton-queue-terminal-certificates", "Plane Newton queue and terminal certificates"),
    (9, "plane-chart-correspondence-global-attachment", "Plane chart correspondence and global attachment"),
)

HUB_FRONTIER = """## 4. The live frontier

The nine lanes partition attention, not mathematics.  The focused pages are
the current research briefs; the summaries here only identify each lane's
present gate.  Follow the focused page for its exact known mathematics,
hypotheses, dependencies, and deliverable contract.

<a id="lane-1-cubic-flatness"></a>
### Lane 1 — [Cubic flatness and finite normalization defect](cubic-flatness-normalization-defects.md)

Extract the actual quadratic-resolvent carrier at an omitted defect value,
then extend or exclude the transverse MCM models.  Keep finite flatness and
recovery of the affine opening separate.

<a id="lane-2-boundary-torelli"></a>
### Lane 2 — [Boundary completeness and Torelli at infinity](boundary-completeness-torelli-at-infinity.md)

Prove the first genuinely noncoprime adjacent-block merge and its
triple-overlap compatibility in the complete PRS atlas.

<a id="lane-3-deformation-moduli"></a>
### Lane 3 — [Bounded-degree deformation and modulus onset](bounded-degree-deformation-modulus-onset.md)

Lift the five-variable order-six reduction to characteristic zero and
stratify the exact rank-drop locus before attempting full saturation.

<a id="lane-4-quartic-endgame"></a>
### Lane 4 — [The quartic endgame](quartic-endgame.md)

Build one global theorem-level case tree that routes every quartic map to an
exact proof or certificate, exposing rather than interpolating any missing
leaf.

<a id="lane-5-degree-budgets"></a>
### Lane 5 — [Intrinsic degree and valuative budgets](intrinsic-degree-valuative-budgets.md)

Establish the transformation law for the semidegree, corrected normal
operator, and Wronskian, then resolve the unramified `delta(Q)>=10` branch.

<a id="lane-6-homogeneous-compression"></a>
### Lane 6 — [Homogeneous realization and compression](homogeneous-realization-compression.md)

Prove finite gauge compatibility for the five-dimensional core and decide
the obstruction on each residual surface before drawing global compression
conclusions.

<a id="lane-7-collision-geometry"></a>
### Lane 7 — [Five-dimensional collision geometry](five-dimensional-collision-geometry.md)

Replace failed monolithic elimination with staged characteristic-zero
saturation and evaluate the first-normal section at each component's generic
point.

<a id="lane-8-plane-newton-queue"></a>
### Lane 8 — [Plane Newton queue and terminal certificates](plane-newton-queue-terminal-certificates.md)

Reconstruct the complete Newton queue as an exhaustive finite DAG whose
edges carry exact routing proofs and whose leaves carry exact certificates.

<a id="lane-9-plane-global-attachment"></a>
### Lane 9 — [Plane chart correspondence and global attachment](plane-chart-correspondence-global-attachment.md)

Define the admissible complete-chain subgroup, prove one actual wall
correspondence theorem, and only then assemble the full two-sided `F_2`
attachment system.

"""

HUB_TASKS = """| Lane | Current exact on-ramp |
| --- | --- |
| 1 | `P1-T1A`: extract the actual resolvent carrier; then `P1-T1B` |
| 2 | `P4-L2A`: noncoprime adjacent merge; then the triple overlap |
| 3 | `P3-L3A`: characteristic-zero rank stratification |
| 4 | `P2-L4A`: global leaf accounting |
| 5 | `L5-T1`: transformation law; then the bounded-Wronskian branch |
| 6 | `P5-L6A`: finite gauge theorem; then residual-surface obstruction |
| 7 | `P5-L7A`: staged saturation; then componentwise obstruction |
| 8 | `P6-L8A`: mathematical queue reconstruction |
| 9 | `P6-L9A`: complete-chain subgroup; then one-wall transport |"""


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
    if "registry/" in text:
        raise ValueError(f"{source}: private registry locator survived sanitization")


def _public_lane_source(source: str, *, slug: str) -> str:
    if slug == "homogeneous-realization-compression":
        if source.count(LANE6_SUMMARY) != 1:
            raise ValueError("Lane 6 selected-plane summary did not match exactly once")
        source = source.replace(LANE6_SUMMARY, f"\n\n{LANE6_MARKER}")
    elif "retained-math-v2-selection:" in source:
        raise ValueError(f"unexpected retained-math v2 marker in {slug}")

    if slug == "intrinsic-degree-valuative-budgets":
        if source.count(LANE5_OBJECTIVE_END) != 1:
            raise ValueError("Lane 5 objective endpoint did not match exactly once")
        source = source.replace(
            LANE5_OBJECTIVE_END,
            LANE5_OBJECTIVE_END + LANE5_PUBLIC_ROUTES,
            1,
        )

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
    replacements = 0
    for private, public in PRIVATE_NOTES:
        count = source.count(private)
        source = source.replace(private, public)
        replacements += count
    if replacements != 1:
        raise ValueError(f"{slug}: expected exactly one private reconciliation note")
    if source.count(TASK_HEADING) != 1:
        raise ValueError(f"{slug}: expected exactly one task heading")
    source = source.replace(TASK_HEADING, f"\n{USEFUL_DELIVERABLE}")
    _validate_public(source, source=Path(slug))
    return source


def _update_hub(source: str) -> str:
    old_start = source.index("## 4. The live frontier\n")
    old_end = source.index("## 5. Graveyard", old_start)
    source = source[:old_start] + HUB_FRONTIER + source[old_end:]
    source = source.replace(
        "**Research state:** mathematical checkpoint 1 August 2026.",
        "**Research state:** mathematical checkpoint 2 August 2026.",
        1,
    )
    old_table_start = source.index("| Lane | Existing exact task capsules |")
    old_table_end = source.index("\n\nBefore substantial work", old_table_start)
    source = source[:old_table_start] + HUB_TASKS + source[old_table_end:]
    marker = "are unmerged and qualified.\n"
    if source.count(marker) != 1:
        raise ValueError("hub PR-assimilation endpoint did not match exactly once")
    reconstruction = """

**2 August manual reconstruction.** Every user message in the relevant source
conversations was triaged, the high-signal mathematical passages were read
against the durable proofs and computations, and all nine focused lane pages
were rebuilt around the strongest exact results and the actual remaining
gate.  These pages replace the earlier short lane snapshots for research
assignment; the six program dossiers remain deeper overlapping views.
"""
    source = source.replace(marker, marker + reconstruction, 1)
    _validate_public(source, source=Path("state-of-the-program.md"))
    return source


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, required=True)
    parser.add_argument("--lane-source-dir", type=Path, required=True)
    parser.add_argument("--lane-manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    base = args.base_dir.resolve()
    lane_source_dir = args.lane_source_dir.resolve()
    lane_manifest_path = args.lane_manifest.resolve()
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

    lane_manifest = _load(lane_manifest_path)
    if lane_manifest.get("handoff_version") != 4 or lane_manifest.get("lane_count") != 9:
        raise ValueError("source manifest must select exactly nine v4 lanes")
    source_entries = {item["slug"]: item for item in lane_manifest["lanes"]}
    expected_slugs = [slug for _, slug, _ in LANES]
    if list(source_entries) != expected_slugs:
        raise ValueError("source v4 lane order or membership changed")

    lane_texts: dict[str, str] = {}
    for sequence, slug, expected_title in LANES:
        item = source_entries[slug]
        if item["lane"] != sequence:
            raise ValueError(f"{slug}: lane sequence changed")
        path = lane_source_dir / f"{slug}.md"
        payload = path.read_bytes()
        text = payload.decode("utf-8")
        if (
            len(payload) != item["byte_count"]
            or len(text.splitlines()) != item["line_count"]
            or _sha256(payload) != item["sha256"]
        ):
            raise ValueError(f"source v4 lane does not match manifest: {path}")
        if text.splitlines()[0] != f"# Lane {sequence}: {expected_title}":
            raise ValueError(f"{slug}: title changed")
        lane_texts[slug] = _public_lane_source(text, slug=slug)

    prepared: list[tuple[str, bytes, dict[str, Any]]] = []
    for item in base_manifest["briefs"]:
        base_source = base / item["source"]
        base_payload = base_source.read_bytes()
        if len(base_payload) != item["bytes"] or _sha256(base_payload) != item["sha256"]:
            raise ValueError(f"base source does not match manifest: {base_source}")
        if item["kind"] == "lane":
            text = lane_texts[item["program_slug"]]
        elif item["kind"] == "cross_program":
            text = _update_hub(base_payload.decode("utf-8"))
        else:
            text = base_payload.decode("utf-8")
            _validate_public(text, source=base_source)
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

    found_markers: list[dict[str, str]] = []
    marker_re = re.compile(
        r"<!-- retained-math-v2-selection:(?P<argument_id>[A-Z0-9-]+) -->"
    )
    for _, payload, item in prepared:
        for argument_id in marker_re.findall(payload.decode("utf-8")):
            found_markers.append(
                {"program_slug": item["program_slug"], "argument_id": argument_id}
            )
    if found_markers != EXPECTED_V2_MARKERS:
        raise ValueError("retained-math v2 marker selection changed")

    output.mkdir()
    for name, payload, _ in prepared:
        with (output / name).open("xb") as handle:
            handle.write(payload)
    manifest = {
        "schema_version": 4,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "base_release": {
            "release_id": base_manifest["release_id"],
            "manifest_sha256": _sha256(base_manifest_path.read_bytes()),
        },
        "source_handoff": {
            "handoff_version": lane_manifest["handoff_version"],
            "manifest_sha256": _sha256(lane_manifest_path.read_bytes()),
        },
        "brief_count": len(prepared),
        "primary_entrypoint_count": sum(
            bool(item["primary_entrypoint"]) for _, _, item in prepared
        ),
        "retained_math_v2_markers": EXPECTED_V2_MARKERS,
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
                "lane_count": len(lane_texts),
                "manifest_sha256": _sha256(manifest_payload),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
