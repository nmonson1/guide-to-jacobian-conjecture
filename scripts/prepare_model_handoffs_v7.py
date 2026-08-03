#!/usr/bin/env python3
"""Build a public, write-once model-handoff package from a v7c-v7j handoff.

The nine focused lane pages and portfolio are taken from the manifest-pinned
private handoff.  The six deeper program dossiers are compact overlays on the
compiler-owned program graph views; they do not repeat theorem statements.
Two specialized exact input pages are inherited from the preceding public
package.  Repository-only links are rewritten to public proof,
retained-mathematics, or lane source-packet routes.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = ("/fss/", "/home/", "chatgpt.com/share", "sandbox:/")
LANES = (
    (1, "cubic-flatness-normalization-defects"),
    (2, "boundary-completeness-torelli-at-infinity"),
    (3, "bounded-degree-deformation-modulus-onset"),
    (4, "quartic-endgame"),
    (5, "intrinsic-degree-valuative-budgets"),
    (6, "homogeneous-realization-compression"),
    (7, "five-dimensional-collision-geometry"),
    (8, "plane-newton-queue-terminal-certificates"),
    (9, "plane-chart-correspondence-global-attachment"),
)
PROGRAM_LANES = {
    "cubic-marked-root-incidence-geometry": (
        (1, "cubic-flatness-normalization-defects"),
    ),
    "minimum-degree-and-quartic-exclusions": ((4, "quartic-endgame"),),
    "local-rigidity-and-deformation-algebra": (
        (3, "bounded-degree-deformation-modulus-onset"),
    ),
    "stable-moduli": (
        (2, "boundary-completeness-torelli-at-infinity"),
        (5, "intrinsic-degree-valuative-budgets"),
    ),
    "homogeneous-descendants": (
        (6, "homogeneous-realization-compression"),
        (7, "five-dimensional-collision-geometry"),
    ),
    "plane-boundary-obstructions": (
        (8, "plane-newton-queue-terminal-certificates"),
        (9, "plane-chart-correspondence-global-attachment"),
    ),
}
TEXT_SUFFIXES = {".csv", ".json", ".m2", ".md", ".py", ".sage", ".tex"}


# Directory entries are deliberately limited to compact, public-useful packets.
# Large historical trees use explicit file lists below.
PACKET_INPUTS: dict[str, tuple[str, ...]] = {
    "cubic-flatness-normalization-defects": (
        "research-notes/lane1-collision-saturation-20260802-v1",
        "research-notes/lane1-collision-saturation-20260803-v2",
        "research-notes/lane1-models-20260803-v1",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane1_marked_root_benchmark.py",
        "manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py",
        "manuscripts/01-cubic-incidence/appendices/common-zero-normalization.tex",
        "manuscripts/01-cubic-incidence/appendices/minimal-smooth-defect.tex",
        "manuscripts/01-cubic-incidence/appendices/moving-hyperplanes.tex",
        "manuscripts/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex",
    ),
    "boundary-completeness-torelli-at-infinity": (
        "research-notes/lane2-projective-normalization-20260803-v1",
        "research-notes/lane2-adjacent-merge-20260803-v1",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_theorem.md",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_saturated_multirees_equations.md",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_checks.py",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_theorem.md",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_checks.py",
        "manuscripts/04-stable-moduli/appendices/additional-moduli.tex",
        "manuscripts/04-stable-moduli/appendices/logarithmic-deformations.tex",
        "manuscripts/04-stable-moduli/appendices/reciprocal-family.tex",
        "manuscripts/04-stable-moduli/appendices/weighted-lift-moduli.tex",
    ),
    "bounded-degree-deformation-modulus-onset": (
        "research-notes/lane3-formal-effectivity",
        "research-notes/lane3-recovery-integration-20260803-v1",
        "research-notes/lane3-order5-recovery-20260803-v1",
    ),
    "quartic-endgame": (
        "research-notes/lane4-f4-contract-20260803-v1/F4_INPUT_CONTRACT.md",
        "research-notes/lane4-f4-contract-20260803-v1/LOCAL_CHART_RECOVERY.md",
        "research-notes/lane4-f4-contract-20260803-v1/q4-f4-local-chart-v1.json",
        "research-notes/lane4-f4-contract-20260803-v1/f4-contract.schema.json",
        "research-notes/lane4-f4-contract-20260803-v1/verify_contract_and_routing.py",
        "research-notes/lane4-f4-contract-20260803-v1/verify_q4_f4_local_chart.py",
        "research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-global-case-tree.md",
        "research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-case-tree.csv",
        "research-notes/lane4-quartic-endgame-20260802-v1/PROOF_CODE_CROSSWALK.md",
        "research-notes/lane4-quartic-endgame-20260802-v1/replay_core.py",
        "research-notes/lane4-quartic-endgame-20260802-v1/proofs/10-structural-repairs-and-z2.tex",
        "manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/quartic_F4_endgame_complete.md",
        "manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/verify_quartic_F4_endgame.replay_fixed.py",
    ),
    "intrinsic-degree-valuative-budgets": (
        "research-notes/lane5-degree-budgets",
        "research-notes/lane5-collision-transport-20260803-v1",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane5_encoded_shear_packet.py",
    ),
    "homogeneous-realization-compression": (
        "research-tools/filtered_operation_complex",
        "research-notes/lane6-transverse-source-obstruction-20260802-v1",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane6_moving_target_pilot.py",
        "manuscripts/05-homogeneous-descendants/appendices/monolith-prolongation.tex",
    ),
    "five-dimensional-collision-geometry": (
        "research-notes/lane7-component-inputs-20260803-v1",
        "research-notes/lane7-projective-kernel-20260803-v1",
        "research-notes/lane7-split-incidence-20260802-v1/lane7-split-incidence-theorem.md",
        "research-notes/lane7-split-incidence-20260802-v1/reconstruct_matrices.py",
        "research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_theorem.py",
        "research-notes/lane7-split-incidence-20260802-v1/verify_split_determinants.py",
        "research-notes/lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json",
        "research-notes/lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json",
        "research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_report.json",
        "research-notes/lane7-split-incidence-20260802-v1/verify_split_determinants_report.json",
    ),
    "plane-newton-queue-terminal-certificates": (
        "research-notes/lane8-f2-support-determinacy-audit-20260803-v1",
        "research-notes/lane8-full-root-closure-20260803-v1",
        "research-notes/lane89-mathematical-recovery-20260803-v1",
        "research-notes/lane8-proof-queue-20260802-v1",
        "research-notes/planar-descent-no-go-20260802-v1",
        "manuscripts/06-plane-boundary/appendices/f2-terminal-boundary.tex",
        "manuscripts/06-plane-boundary/appendices/six-sheet-monodromy.tex",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_boundary_gluing_program.md",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi.py",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_face_rigidity.py",
    ),
    "plane-chart-correspondence-global-attachment": (
        "research-notes/lane89-mathematical-recovery-20260803-v1",
        "research-notes/p6-chart-correspondence/LANE9_F2_PARAMETER_COMPLETE_RECURRENCE_V2.md",
        "research-notes/p6-chart-correspondence/lane9_f2_attachment_recurrence.py",
        "research-notes/lane9-wall-shear-20260802-v1/LANE9_CONTINUATION_V3_REPORT.md",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_GRADING_AUDIT.md",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_OVERLAP_THEOREM.md",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_DUAL_TRIPLE_OVERLAP.md",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/WALL_SHEAR_REES_FLOW.md",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/F2_CYCLIC_WALL_DESCENT.md",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/wall_shear_master_covariance.py",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_jet_transport_audit.py",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_overlap_saturation.py",
        "research-notes/lane9-wall-shear-20260802-v1/research-notes/p6-chart-correspondence/degree21_k4_triple_overlap.py",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane9_wall_groupoid_packet.py",
    ),
}


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _source_anchor(repo_path: str) -> str:
    """Return a compact stable anchor for one canonical source path."""
    return f"source-{_sha256(repo_path.encode('utf-8'))[:16]}"


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _validate_public(text: str, *, source: Path) -> None:
    lowered = text.casefold()
    found = [marker for marker in FORBIDDEN if marker.casefold() in lowered]
    if found:
        raise ValueError(f"{source}: forbidden public markers: {found}")
    if "registry/" in text:
        raise ValueError(f"{source}: private registry locator survived")


def _portable_source_text(text: str) -> tuple[str, bool]:
    """Remove checkout-only locators while preserving the mathematical source."""
    transformed = re.sub(
        r"/(?:fss|home)/[^\s`\"']+",
        "/path/to/versioned-artifact",
        text,
    )
    transformed = re.sub(
        r"https://chatgpt\.com/share/[A-Za-z0-9-]+",
        "[private source conversation]",
        transformed,
    )
    transformed = transformed.replace("sandbox:/", "private-artifact:/")
    transformed = transformed.replace("registry/", "private-source/")
    return transformed, transformed != text


def _selected_files(repo_root: Path, slug: str) -> list[Path]:
    selected: set[Path] = set()
    for repo_path in PACKET_INPUTS[slug]:
        path = repo_root / repo_path
        if path.is_file():
            selected.add(path)
            continue
        if not path.is_dir():
            raise FileNotFoundError(f"missing packet input: {path}")
        for child in path.rglob("*"):
            if child.is_file() and child.suffix in TEXT_SUFFIXES:
                selected.add(child)
    if not selected:
        raise ValueError(f"{slug}: source packet would be empty")
    return sorted(selected, key=lambda path: path.relative_to(repo_root).as_posix())


def _source_packet(
    *, sequence: int, slug: str, repo_root: Path, source_commit: str
) -> tuple[bytes, dict[str, Any], dict[str, str]]:
    paths = _selected_files(repo_root, slug)
    records: list[dict[str, Any]] = []
    payloads: list[tuple[str, str]] = []
    for path in paths:
        repo_path = path.relative_to(repo_root).as_posix()
        payload = path.read_bytes()
        text, transformed = _portable_source_text(payload.decode("utf-8"))
        _validate_public(text, source=path)
        record = {
            "repo_path": repo_path,
            "packet_path": repo_path,
            "packet_anchor": _source_anchor(repo_path),
            "sha256": _sha256(payload),
            "bytes": len(payload),
        }
        if transformed:
            record["public_transform"] = "checkout-only locators replaced by portable placeholders"
        records.append(record)
        payloads.append((repo_path, text))

    parts = [
        f"# Lane {sequence} exact research source packet",
        "",
        "This page exposes the proof notes, computation contracts, programs,",
        "and finite inputs used by the focused lane brief. Each section names",
        "its canonical repository path and source hash. No private checkout or",
        "download is required.",
        "",
        "## Included files",
        "",
    ]
    parts.extend(
        f"- [`{record['repo_path']}`](#{record['packet_anchor']}) — "
        f"`{record['sha256']}`"
        for record in records
    )
    language = {
        ".csv": "csv",
        ".json": "json",
        ".m2": "macaulay2",
        ".md": "markdown",
        ".py": "python",
        ".sage": "python",
        ".tex": "tex",
    }
    for repo_path, source_text in payloads:
        source_anchor = _source_anchor(repo_path)
        normalized = "\n".join(
            line.rstrip() for line in source_text.rstrip().splitlines()
        )
        escaped = (
            html.escape(normalized, quote=False)
            .replace("[", "&#91;")
            .replace("]", "&#93;")
        )
        parts.extend(
            [
                "",
                f'<a id="{source_anchor}"></a>',
                "",
                f"## `{repo_path}`",
                "",
                f'<pre><code class="language-{language.get(Path(repo_path).suffix, "text")}">',
                escaped,
                "</code></pre>",
            ]
        )
    parts.extend(["", f"[Back to Lane {sequence}]({slug}.md)", ""])
    page = "\n".join(parts)
    _validate_public(page, source=Path(f"lane-{sequence}-source-packet.md"))
    payload = page.encode("utf-8")
    item = {
        "input_id": f"LANE{sequence}-RESEARCH-SOURCE-PACKET-V2",
        "source": f"lane-{sequence}-source-packet.md",
        "route": f"research/handoffs/lane-{sequence}-source-packet.md",
        "sha256": _sha256(payload),
        "bytes": len(payload),
        "words": len(page.split()),
        "source_packet": {
            "source_root": "jacobian_repository",
            "source_commit": source_commit,
            "files": records,
        },
    }
    return payload, item, {
        record["repo_path"]: record["packet_anchor"] for record in records
    }


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
UNIT_PATH_RE = re.compile(r"^/fss/.*/units/(?P<unit>(?:RMU|JCG)-[A-Z0-9]+)\.md$")


def _public_lane_source(
    source: str,
    *,
    sequence: int,
    slug: str,
    packet_anchors: dict[str, str],
) -> str:
    footer_links = [
        "[Portfolio](state-of-the-program.md)",
        f"[Exact source packet](lane-{sequence}-source-packet.md)",
    ]
    if sequence == 7:
        footer_links.append(
            "[Exact collision-chart input](lane-7-collision-input.md)"
        )
    if sequence == 8:
        footer_links.append(
            "[Raw-support reconstruction input](lane-8-reconstruction-input.md)"
        )
    footer_links.extend(
        [
            "[Release metadata](release.json)",
            "[Retained mathematics](../working-mathematics/index.md)",
            "[Current proof sources](../proof-sources/index.md)",
        ]
    )
    source, footer_replacements = re.subn(
        r"\n---\n(?:\[Portfolio\]\(\.\./README\.md\)|Successor handoff v7[c-i])[^\n]*\n\Z",
        "\n---\n" + " · ".join(footer_links) + "\n",
        source,
    )
    if footer_replacements != 1:
        raise ValueError(f"{slug}: private v7c-v7i footer changed or is missing")

    def replace_link(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        unit_match = UNIT_PATH_RE.fullmatch(target)
        if unit_match:
            unit = unit_match.group("unit")
            return f"[{label}](../working-mathematics/units/{unit}.md)"
        if target == "../README.md":
            return f"[{label}](state-of-the-program.md)"
        if not target.startswith("../../../"):
            return match.group(0)

        repo_path = target.removeprefix("../../../").rstrip("/")
        if repo_path.startswith("manuscripts/") and repo_path.endswith(".tex"):
            proof_path = Path(repo_path.removeprefix("manuscripts/")).with_suffix(".md")
            return f"[{label}](../proof-sources/{proof_path.as_posix()})"
        anchor = packet_anchors.get(repo_path)
        if anchor is None:
            raise ValueError(
                f"{slug}: linked input missing from source packet: {repo_path}"
            )
        return f"[{label}](lane-{sequence}-source-packet.md#{anchor})"

    source = LINK_RE.sub(replace_link, source)
    if "../../../" in source or "](/fss/" in source:
        raise ValueError(f"{slug}: repository-only link survived transformation")
    required_groups = (
        ("## Scope", "## Why this lane matters"),
        (
            "## Setup and definitions",
            "## Setup and notation",
            "## Newton-root conventions",
            "## Fixed \\(F_2\\) chart and support",
        ),
        (
            "## Results to use",
            "## Reusable mathematics",
            "## Closed mathematics below 125",
        ),
        ("## Live problem",),
        ("## Tasks", "## Ready task ", "## Interface-ready task "),
        ("## Direct sources", "## Exact sources"),
    )
    missing = [
        " or ".join(group)
        for group in required_groups
        if not any(heading in source for heading in group)
    ]
    if missing:
        raise ValueError(f"{slug}: missing v7 section groups: {missing}")
    _validate_public(source, source=Path(slug))
    return source


def _public_portfolio(source: str) -> str:
    if not source.startswith("# Nine research directions around the Jacobian conjecture\n"):
        raise ValueError("portfolio v7 title changed")
    if source.count("Research portfolio · 2026-08-03") != 1:
        raise ValueError("portfolio v7 date line changed")
    source = source.replace(
        "Research portfolio · 2026-08-03", "Updated 3 August 2026", 1
    )
    new_footer = (
        "\n---\n[Release metadata](release.json) · "
        "[Retained mathematics](../working-mathematics/index.md) · "
        "[Current proof sources](../proof-sources/index.md)\n"
    )
    source, footer_replacements = re.subn(
        r"\n---\nSuccessor handoff v7[c-j][^\n]*\n\Z", new_footer, source
    )
    if footer_replacements != 1:
        raise ValueError("portfolio v7 footer changed")
    source = source.replace("lanes/", "")
    _validate_public(source, source=Path("state-of-the-program.md"))
    return source


def _verified_handoff_sources(
    *, lane_source_dir: Path, lane_manifest_path: Path
) -> tuple[dict[str, str], str, str]:
    manifest_payload = lane_manifest_path.read_bytes()
    manifest = _load(lane_manifest_path)
    handoff_version = manifest.get("handoff_version")
    if handoff_version not in {"7c", "7d", "7e", "7f", "7g", "7h", "7i", "7j"} or manifest.get("lane_count") != 9:
        raise ValueError("source manifest must select exactly nine v7c-v7j lanes")
    lanes = manifest.get("lanes")
    if lanes != [{"lane": sequence, "slug": slug} for sequence, slug in LANES]:
        raise ValueError("v7 lane order or membership changed")
    file_entries = {item["path"]: item for item in manifest.get("files", [])}

    sources: dict[str, str] = {}
    portfolio = lane_source_dir / "README.md"
    paths = [("state-of-the-program", portfolio)] + [
        (slug, lane_source_dir / "lanes" / f"{slug}.md") for _, slug in LANES
    ]
    for key, path in paths:
        relative = path.relative_to(lane_source_dir.parent.parent).as_posix()
        item = file_entries.get(relative)
        if item is None:
            raise ValueError(f"v7 manifest does not pin {relative}")
        payload = path.read_bytes()
        text = payload.decode("utf-8")
        if (
            len(payload) != item["byte_count"]
            or len(text.splitlines()) != item["line_count"]
            or _sha256(payload) != item["sha256"]
        ):
            raise ValueError(f"v7 source differs from manifest: {path}")
        sources[key] = text
    return sources, _sha256(manifest_payload), handoff_version


def _program_overlay(
    item: dict[str, Any], retained_graph: dict[str, Any]
) -> bytes:
    slug = item["program_slug"]
    programs = {
        program["slug"]: program for program in retained_graph["programs"]
    }
    if set(programs) != set(PROGRAM_LANES):
        raise ValueError("retained graph program set disagrees with dossier map")
    program = programs[slug]
    lane_lines = [
        f"- [Lane {sequence}: {lane_slug.replace('-', ' ')}]({lane_slug}.md)"
        for sequence, lane_slug in PROGRAM_LANES[slug]
    ]
    text = "\n".join(
        [
            f"# {program['title']}",
            "",
            program["summary"],
            "",
            "## Current mathematical corpus",
            "",
            "The exact current statements, hypotheses, dependencies, arguments,",
            "evidence, and limitations for this subject are compiled from the",
            "retained mathematical graph:",
            "",
            f"[Open the current {program['title']} graph view]"
            f"(../working-mathematics/programs/{slug}.md)",
            "",
            "That generated view is authoritative for reusable mathematics. This",
            "page deliberately does not copy theorem statements or proof chains.",
            "",
            "## Current research entrypoints",
            "",
            *lane_lines,
            "",
            "Each lane defines its objects, separates established results from",
            "examples and open problems, and links the exact source inputs needed",
            "for its advertised tasks.",
            "",
            "## Strategy and connections",
            "",
            "Use this program as an overlapping subject view, not as a partition",
            "of the project. Follow dependencies into other program graph views",
            "when the mathematics crosses a boundary. The listed tasks are useful",
            "next steps, but other sound connections and stronger routes are welcome.",
            "",
            "[Back to the research portfolio](state-of-the-program.md)",
            "",
        ]
    )
    _validate_public(text, source=Path(item["source"]))
    return text.encode("utf-8")


def _write_new(path: Path, payload: bytes) -> None:
    with path.open("xb") as handle:
        handle.write(payload)


def _manifest_item(item: dict[str, Any], payload: bytes, *, title: str | None = None) -> dict[str, Any]:
    text = payload.decode("utf-8")
    result = {
        **item,
        "sha256": _sha256(payload),
        "bytes": len(payload),
        "words": len(text.split()),
    }
    if title is not None:
        result["title"] = title
    return result


def _copy_auxiliary_inputs(base: Path, base_manifest: dict[str, Any]) -> list[tuple[bytes, dict[str, Any]]]:
    keep = {"LANE7-COLLISION-CHART-V1", "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1"}
    prepared: list[tuple[bytes, dict[str, Any]]] = []
    for item in base_manifest.get("task_inputs", []):
        if item.get("input_id") not in keep:
            continue
        payload = (base / item["source"]).read_bytes()
        if len(payload) != item["bytes"] or _sha256(payload) != item["sha256"]:
            raise ValueError(f"base task input differs from manifest: {item['source']}")
        _validate_public(payload.decode("utf-8"), source=base / item["source"])
        prepared.append((payload, item))
    if {item["input_id"] for _, item in prepared} != keep:
        raise ValueError("base package does not contain both specialized exact inputs")
    return prepared


def build(args: argparse.Namespace) -> dict[str, Any]:
    base = args.base_dir.resolve()
    repo_root = args.jacobian_repo.resolve()
    lane_source_dir = args.lane_source_dir.resolve()
    lane_manifest_path = args.lane_manifest.resolve()
    retained_graph_path = args.retained_graph.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")
    if not re.fullmatch(r"[0-9a-f]{40}", args.jacobian_commit):
        raise ValueError("--jacobian-commit must be a full commit hash")

    base_manifest_path = base / "manifest.json"
    base_manifest = _load(base_manifest_path)
    if (
        base_manifest.get("brief_count") != 16
        or base_manifest.get("primary_entrypoint_count") != 10
    ):
        raise ValueError("base package must contain sixteen briefs and ten entrypoints")
    handoff_sources, handoff_manifest_sha, handoff_version = (
        _verified_handoff_sources(
            lane_source_dir=lane_source_dir,
            lane_manifest_path=lane_manifest_path,
        )
    )
    retained_graph_payload = retained_graph_path.read_bytes()
    retained_graph = _load(retained_graph_path)
    if retained_graph.get("schema_version") != 2:
        raise ValueError("program dossiers require retained graph schema v2")

    packet_outputs: dict[
        str, tuple[bytes, dict[str, Any], dict[str, str]]
    ] = {}
    for sequence, slug in LANES:
        packet_outputs[slug] = _source_packet(
            sequence=sequence,
            slug=slug,
            repo_root=repo_root,
            source_commit=args.jacobian_commit,
        )

    prepared_briefs: list[tuple[str, bytes, dict[str, Any]]] = []
    brief_by_slug = {item["program_slug"]: item for item in base_manifest["briefs"]}
    portfolio_item = brief_by_slug["state-of-the-program"]
    portfolio_payload = _public_portfolio(
        handoff_sources["state-of-the-program"]
    ).encode("utf-8")
    prepared_briefs.append(
        (
            portfolio_item["source"],
            portfolio_payload,
            _manifest_item(
                portfolio_item,
                portfolio_payload,
                title="Current Jacobian research portfolio",
            ),
        )
    )

    for item in base_manifest["briefs"]:
        if item["kind"] != "program":
            continue
        payload = _program_overlay(item, retained_graph)
        prepared_briefs.append(
            (item["source"], payload, _manifest_item(item, payload))
        )

    for sequence, slug in LANES:
        item = brief_by_slug[slug]
        packet_anchors = packet_outputs[slug][2]
        text = _public_lane_source(
            handoff_sources[slug],
            sequence=sequence,
            slug=slug,
            packet_anchors=packet_anchors,
        )
        payload = text.encode("utf-8")
        title = text.splitlines()[0].removeprefix("# ")
        prepared_briefs.append(
            (item["source"], payload, _manifest_item(item, payload, title=title))
        )

    prepared_briefs.sort(key=lambda prepared: prepared[2]["display_sequence"])
    auxiliary = _copy_auxiliary_inputs(base, base_manifest)
    task_inputs = [
        (packet_outputs[slug][0], packet_outputs[slug][1]) for _, slug in LANES
    ] + auxiliary

    output.mkdir()
    for name, payload, _ in prepared_briefs:
        _write_new(output / name, payload)
    for payload, item in task_inputs:
        _write_new(output / item["source"], payload)

    manifest = {
        "schema_version": 7,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "base_release": {
            "release_id": base_manifest["release_id"],
            "manifest_sha256": _sha256(base_manifest_path.read_bytes()),
        },
        "source_handoff": {
            "handoff_version": handoff_version,
            "manifest_sha256": handoff_manifest_sha,
            "jacobian_commit": args.jacobian_commit,
        },
        "program_dossiers": {
            "kind": "generated_graph_view_overlays",
            "retained_registry_id": retained_graph["registry_id"],
            "retained_graph_sha256": _sha256(retained_graph_payload),
        },
        "brief_count": len(prepared_briefs),
        "primary_entrypoint_count": sum(
            bool(item["primary_entrypoint"]) for _, _, item in prepared_briefs
        ),
        "task_input_count": len(task_inputs),
        "task_inputs": [item for _, item in task_inputs],
        "retained_math_v2_markers": [],
        "briefs": [item for _, _, item in prepared_briefs],
    }
    manifest_payload = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    _write_new(output / "manifest.json", manifest_payload)
    return {
        "output_dir": str(output),
        "release_id": args.release_id,
        "brief_count": len(prepared_briefs),
        "primary_entrypoint_count": manifest["primary_entrypoint_count"],
        "task_input_count": len(task_inputs),
        "manifest_sha256": _sha256(manifest_payload),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, required=True)
    parser.add_argument("--jacobian-repo", type=Path, required=True)
    parser.add_argument("--lane-source-dir", type=Path, required=True)
    parser.add_argument("--lane-manifest", type=Path, required=True)
    parser.add_argument("--retained-graph", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    parser.add_argument("--jacobian-commit", required=True)
    args = parser.parse_args()
    print(json.dumps(build(args), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
