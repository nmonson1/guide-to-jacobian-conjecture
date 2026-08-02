#!/usr/bin/env python3
"""Prepare a write-once public release from pinned private v4/v5 lane sources."""

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
LANE8_FILES = {
    "belyi_exact_field_relations.json": (
        "a5b5752a5f7b90d50458fe3f3949e6731e0b607981627c56e0c04a1bf89de1c2"
    ),
    "expected_invariants.json": (
        "04c0da97da9974665ca1348bf1b1736ffeb5231a1ff1dc1e3c9dea8a1ec564e0"
    ),
    "rebuild_lower_face_reduction.py": (
        "921ebae8828452dcb535ab81a8561c717ddd61346a04389af568fb9dcafee53f"
    ),
}
LANE8_HELPER = {
    "path": "degree-296-compact/scripts/quintic_field_fast.py",
    "sha256": "b43871c8897512b752c9e8fa8d4f2d80571865d465940e13b36f130d07091942",
}
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

Here *ready* means that the starting objects are displayed on the page or a
direct public input page and that the deliverable can be attempted without an
unpublished artifact.  *Blocked* names the missing input or mathematical
dependency.  In task IDs, `P` identifies the owning program and `L` the lane;
programs and lanes are overlapping views rather than the same numbering.

<a id="lane-1-cubic-flatness"></a>
### Lane 1 — [Cubic flatness and finite normalization defect](cubic-flatness-normalization-defects.md)

Derive a Keller-origin constraint excluding the height-two three-torsion
carrier, or construct a complete local model showing what global input is
missing.  Keep affine-opening recovery separate.

<a id="lane-2-boundary-torelli"></a>
### Lane 2 — [Boundary completeness and Torelli at infinity](boundary-completeness-torelli-at-infinity.md)

Prove the supplied toric adjacent-block theorem.  A PRS-specific noncoprime
chart remains blocked until its pivot and transfer conventions are public.

<a id="lane-3-deformation-moduli"></a>
### Lane 3 — [Bounded-degree deformation and modulus onset](bounded-degree-deformation-modulus-onset.md)

Reconstruct the direct order-five Kuranishi calculation from the displayed
map and slice, producing the public matrices needed for the blocked comparison.

<a id="lane-4-quartic-endgame"></a>
### Lane 4 — [The quartic endgame](quartic-endgame.md)

Build one global theorem-level case tree that routes every quartic map to an
exact proof or certificate, exposing rather than interpolating any missing
leaf.

<a id="lane-5-degree-budgets"></a>
### Lane 5 — [Intrinsic degree and valuative budgets](intrinsic-degree-valuative-budgets.md)

Prove the supplied frame-covariance lemma.  Its application to the fixed map
remains blocked on the certificate semidegree and automorphism table.

<a id="lane-6-homogeneous-compression"></a>
### Lane 6 — [Homogeneous realization and compression](homogeneous-realization-compression.md)

Repackage the selected-plane residual as a section of a cokernel and analyze
its augmented determinantal zero scheme.  The full quotient remains blocked.

<a id="lane-7-collision-geometry"></a>
### Lane 7 — [Five-dimensional collision geometry](five-dimensional-collision-geometry.md)

Give a geometric model of the exact 15-quintic chart; use staged
characteristic-zero saturation as a separate local CAS route.

<a id="lane-8-plane-newton-queue"></a>
### Lane 8 — [Plane Newton queue and terminal certificates](plane-newton-queue-terminal-certificates.md)

Audit the exact public reconstruction program from the two supports to its
terminal equations and expose the first unimplemented complementary branch.

<a id="lane-9-plane-global-attachment"></a>
### Lane 9 — [Plane chart correspondence and global attachment](plane-chart-correspondence-global-attachment.md)

Prove the residue-dual quotient theorem on the displayed finite windows.
Chart-specific subgroup classification and full `F_2` attachment remain blocked.

"""

HUB_TASKS = """| Lane | Current exact on-ramp |
| --- | --- |
| 1 | `P1-T1`: derive a Keller-origin constraint or complete local model |
| 2 | `P4-L2A0`: abstract toric adjacent-block theorem |
| 3 | `P3-L3A0`: direct order-five reconstruction and public matrix package |
| 4 | `P2-L4A`: global leaf accounting |
| 5 | `L5-T1A`: abstract frame-covariance lemma |
| 6 | `P5-L6A0`: selected-plane obstruction-section package |
| 7 | `P5-L7A`: geometric model of the 15-quintic chart |
| 8 | `P6-L8A`: audit the exact reconstruction and expose the first routing gap |
| 9 | `P6-L9A0`: residue-dual quotient theorem |"""


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _prepare_lane7_input(packet_dir: Path) -> tuple[bytes, dict[str, Any]]:
    manifest_path = packet_dir / "manifest.json"
    manifest = _load(manifest_path)
    files = {item["path"]: item for item in manifest.get("files", [])}
    required = {"collision-system.json", "collision-system.m2"}
    if not required.issubset(files):
        raise ValueError("Lane 7 packet is missing its exact system or M2 input")
    for name in required:
        path = packet_dir / name
        payload = path.read_bytes()
        item = files[name]
        if len(payload) != item["bytes"] or _sha256(payload) != item["sha256"]:
            raise ValueError(f"Lane 7 packet file does not match manifest: {path}")

    system = _load(packet_dir / "collision-system.json")
    equations = system.get("equations", [])
    chart = system.get("chart", {})
    variables = chart.get("variables", [])
    if len(equations) != 15 or len(variables) != 16:
        raise ValueError("Lane 7 packet dimensions changed")
    if chart.get("open_condition") != "det(T)*(u3-u4*v3) != 0":
        raise ValueError("Lane 7 open condition changed")
    base_point = system.get("base_point_F11", {})
    if base_point.get("jacobian_rank") != 15:
        raise ValueError("Lane 7 smooth-point rank changed")
    m2 = (packet_dir / "collision-system.m2").read_text(encoding="utf-8")
    page = "\n".join(
        [
            "# Lane 7 exact collision-chart input",
            "",
            "This page is the complete public CAS input for Lane 7.  It is a",
            "model-readable page, not a request to download a private artifact.",
            "",
            "## Exact chart",
            "",
            "The affine normalizations are `a7=1` and `v4=1`.  The polynomial",
            "ring has the following 16 variables:",
            "",
            "```text",
            ",".join(variables),
            "```",
            "",
            "The scheme is cut out by 15 primitive integer quintics on",
            "",
            "```text",
            chart["open_condition"],
            "```",
            "",
            "The two open factors are `det(T)` and `u3-u4*v3`; the complete",
            "expanded determinant is included in the Macaulay2 block below.",
            "",
            "## Exact smooth point",
            "",
            "Over `F_11`, in the variable order above, the point is",
            "",
            "```text",
            ",".join(str(value) for value in base_point["coordinates"]),
            "```",
            "",
            "All 15 equations vanish there.  The Jacobian rank is 15 and the",
            "minor on the first 15 variables is 1 modulo 11.",
            "",
            "## Complete Macaulay2 input",
            "",
            "The following is copied byte-for-byte from the manifest-pinned CAS",
            "input.  It defines the ring, ideal, open factor, and saturation.",
            "",
            "```macaulay2",
            m2.rstrip(),
            "```",
            "",
            "## Exact evidence boundary",
            "",
            system["interpretation"]["proved"],
            "",
            "It does not establish: " + system["interpretation"]["not_proved"],
            "",
            "## Source hashes",
            "",
            f"- Packet manifest: `{_sha256(manifest_path.read_bytes())}`",
            f"- Exact system JSON: `{files['collision-system.json']['sha256']}`",
            f"- Macaulay2 input: `{files['collision-system.m2']['sha256']}`",
            "",
            "[Back to Lane 7](five-dimensional-collision-geometry.md)",
            "",
        ]
    )
    _validate_public(page, source=packet_dir)
    payload = page.encode("utf-8")
    return payload, {
        "input_id": "LANE7-COLLISION-CHART-V1",
        "source": "lane-7-collision-input.md",
        "route": "research/handoffs/lane-7-collision-input.md",
        "sha256": _sha256(payload),
        "bytes": len(payload),
        "words": len(page.split()),
        "source_packet": {
            "release_id": manifest["release_id"],
            "manifest_sha256": _sha256(manifest_path.read_bytes()),
            "collision_system_sha256": files["collision-system.json"]["sha256"],
            "macaulay2_sha256": files["collision-system.m2"]["sha256"],
        },
    }


def _prepare_lane8_input(packet_dir: Path) -> tuple[bytes, dict[str, Any]]:
    payloads: dict[str, bytes] = {}
    for name, expected_sha in LANE8_FILES.items():
        path = packet_dir / name
        if not path.is_file():
            raise ValueError(f"Lane 8 packet is missing {name}")
        payload = path.read_bytes()
        if _sha256(payload) != expected_sha:
            raise ValueError(f"Lane 8 packet digest changed: {path}")
        payloads[name] = payload
    helper_path = (
        packet_dir.parent.parent
        / "degree-296-compact"
        / "scripts"
        / "quintic_field_fast.py"
    )
    helper_payload = helper_path.read_bytes()
    if _sha256(helper_payload) != LANE8_HELPER["sha256"]:
        raise ValueError(f"Lane 8 field helper digest changed: {helper_path}")
    payloads["quintic_field_fast.py"] = helper_payload

    relations = _load(packet_dir / "belyi_exact_field_relations.json")
    expected = _load(packet_dir / "expected_invariants.json")
    if expected.get("truncated", {}).get("support_sizes") != {"P": 25, "Q": 47}:
        raise ValueError("Lane 8 truncated support sizes changed")
    equation_counts = expected.get("full", {}).get("final_equation_counts", {})
    if sum(equation_counts.values()) != 15:
        raise ValueError("Lane 8 full equation count changed")
    if not relations:
        raise ValueError("Lane 8 exact field relations are empty")

    page_parts = [
        "# Lane 8 exact raw-support reconstruction input",
        "",
        "This page is the complete public executable input used to reconstruct",
        "the two normalized Newton supports through their deficiency layers.",
        "It is an input for auditing the generated path; it does not assert that",
        "all complementary queue branches have been routed.",
        "",
        "## Mathematical contract",
        "",
        "The program generates every lattice point of the truncated and full",
        "support polygons shown on Lane 8, applies the displayed Jacobian bracket",
        "formula, reconstructs the exact degree-21 lower face over the pinned",
        "quintic field, and builds the deficiency layers.  It proves the stored",
        "truncated contradiction and regenerates the fifteen full-support",
        "equations.  It does not prove the imported below-125 reduction or supply",
        "a missing saturation complement or rechart unless that branch appears in",
        "the program.",
        "",
        "To replay without a private checkout, place the reconstruction program",
        "and its two JSON files in `degree-twenty-one/raw-support-reconstruction/`,",
        "place the field helper in `degree-296-compact/scripts/` under the same",
        "parent directory, install SymPy, and run",
        "",
        "```text",
        "python degree-twenty-one/raw-support-reconstruction/rebuild_lower_face_reduction.py --case both --output NEW_OUTPUT_DIRECTORY",
        "```",
        "",
        "The program refuses to overwrite an existing output directory.",
        "",
        "## Exact quintic-field relations",
        "",
        "```json",
        payloads["belyi_exact_field_relations.json"].decode("utf-8").rstrip(),
        "```",
        "",
        "## Pinned expected invariants",
        "",
        "```json",
        payloads["expected_invariants.json"].decode("utf-8").rstrip(),
        "```",
        "",
        "## Exact quintic-field helper",
        "",
        "This is the complete nonstandard dependency imported by the",
        "reconstruction program. Its other imports are from the Python standard",
        "library.",
        "",
        "```python",
        payloads["quintic_field_fast.py"].decode("utf-8").rstrip(),
        "```",
        "",
        "## Complete reconstruction program",
        "",
        "```python",
        payloads["rebuild_lower_face_reduction.py"].decode("utf-8").rstrip(),
        "```",
        "",
        "## Source hashes",
        "",
    ]
    page_parts.extend(
        f"- `{name}`: `{expected_sha}`"
        for name, expected_sha in LANE8_FILES.items()
    )
    page_parts.append(
        f"- `{LANE8_HELPER['path']}`: `{LANE8_HELPER['sha256']}`"
    )
    page_parts.extend(["", "[Back to Lane 8](plane-newton-queue-terminal-certificates.md)", ""])
    page = "\n".join(page_parts)
    _validate_public(page, source=packet_dir)
    payload = page.encode("utf-8")
    return payload, {
        "input_id": "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1",
        "source": "lane-8-reconstruction-input.md",
        "route": "research/handoffs/lane-8-reconstruction-input.md",
        "sha256": _sha256(payload),
        "bytes": len(payload),
        "words": len(page.split()),
        "source_packet": {
            "files": [
                {"path": name, "sha256": expected_sha}
                for name, expected_sha in LANE8_FILES.items()
            ]
            + [LANE8_HELPER]
        },
    }


def _validate_public(text: str, *, source: Path) -> None:
    lowered = text.casefold()
    found = [item for item in FORBIDDEN if item.casefold() in lowered]
    if found:
        raise ValueError(f"{source}: forbidden public markers: {found}")
    if "registry/" in text:
        raise ValueError(f"{source}: private registry locator survived sanitization")


def _public_lane_source(
    source: str, *, slug: str, handoff_version: int
) -> str:
    if handoff_version == 4 and slug == "homogeneous-realization-compression":
        if source.count(LANE6_SUMMARY) != 1:
            raise ValueError("Lane 6 selected-plane summary did not match exactly once")
        source = source.replace(LANE6_SUMMARY, f"\n\n{LANE6_MARKER}")
    elif handoff_version == 4 and "retained-math-v2-selection:" in source:
        raise ValueError(f"unexpected retained-math v2 marker in {slug}")
    elif handoff_version == 5:
        expected_markers = 1 if slug == "homogeneous-realization-compression" else 0
        if source.count("retained-math-v2-selection:") != expected_markers:
            raise ValueError(f"{slug}: retained-math v2 marker count changed")

    if handoff_version == 4 and slug == "intrinsic-degree-valuative-budgets":
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
    if handoff_version == 4:
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
    else:
        required = (
            "## Problem and scope",
            "## Setup and notation",
            "## Reusable mathematics",
            "## Exact live problem",
            "## Tasks and deliverables",
            "## Scope cautions",
        )
        missing = [heading for heading in required if heading not in source]
        if missing:
            raise ValueError(f"{slug}: missing v5 sections: {missing}")
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
    tasks_start = source.index("## 6. Tasks\n")
    old_table_start = source.index("| Lane |", tasks_start)
    old_table_end = source.index("\n\nBefore substantial work", old_table_start)
    source = source[:old_table_start] + HUB_TASKS + source[old_table_end:]
    reconstruction_start = source.index("**2 August manual reconstruction.**")
    reconstruction_end = source.index("\n\n## 4. The live frontier", reconstruction_start)
    reconstruction = """**2 August self-containment repair.** The nine focused pages now define their
load-bearing objects, separate examples from general hypotheses, and advertise
a task as ready only when its inputs are public or it is a genuinely quantified
problem.  The six program dossiers remain deeper overlapping views."""
    source = (
        source[:reconstruction_start]
        + reconstruction
        + source[reconstruction_end:]
    )
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
    parser.add_argument(
        "--lane7-packet",
        type=Path,
        help="Manifest-pinned exact collision packet required for v5",
    )
    parser.add_argument(
        "--lane8-packet",
        type=Path,
        help="Pinned raw-support reconstruction directory required for v5",
    )
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
    handoff_version = lane_manifest.get("handoff_version")
    if handoff_version not in {4, 5} or lane_manifest.get("lane_count") != 9:
        raise ValueError("source manifest must select exactly nine v4 or v5 lanes")
    if handoff_version == 5 and (
        args.lane7_packet is None or args.lane8_packet is None
    ):
        raise ValueError("v5 requires --lane7-packet and --lane8-packet")
    if handoff_version == 4 and (
        args.lane7_packet is not None or args.lane8_packet is not None
    ):
        raise ValueError("v4 does not accept Lane 7 or Lane 8 packets")
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
        lane_texts[slug] = _public_lane_source(
            text, slug=slug, handoff_version=handoff_version
        )

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

    task_inputs: list[tuple[bytes, dict[str, Any]]] = []
    if handoff_version == 5:
        assert args.lane7_packet is not None
        assert args.lane8_packet is not None
        task_inputs.append(_prepare_lane7_input(args.lane7_packet.resolve()))
        task_inputs.append(_prepare_lane8_input(args.lane8_packet.resolve()))

    output.mkdir()
    for name, payload, _ in prepared:
        with (output / name).open("xb") as handle:
            handle.write(payload)
    for payload, item in task_inputs:
        with (output / item["source"]).open("xb") as handle:
            handle.write(payload)
    manifest = {
        "schema_version": handoff_version,
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
        "task_input_count": len(task_inputs),
        "task_inputs": [item for _, item in task_inputs],
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
