#!/usr/bin/env python3
"""Build the public, write-once model-handoff package from private handoff v7.

The nine focused lane pages and portfolio are taken from the manifest-pinned
private handoff.  The six deeper program dossiers and two specialized exact
input pages are inherited byte-for-byte from the preceding public package.
Repository-only links are rewritten to public proof, retained-mathematics, or
lane source-packet routes.
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
TEXT_SUFFIXES = {".csv", ".json", ".m2", ".md", ".py", ".sage", ".tex"}


# Directory entries are deliberately limited to compact, public-useful packets.
# Large historical trees use explicit file lists below.
PACKET_INPUTS: dict[str, tuple[str, ...]] = {
    "cubic-flatness-normalization-defects": (
        "research-notes/lane1-collision-saturation-20260802-v1",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane1_marked_root_benchmark.py",
        "manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py",
    ),
    "boundary-completeness-torelli-at-infinity": (
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_theorem.md",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_saturated_multirees_equations.md",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_checks.py",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_theorem.md",
        "research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_checks.py",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane2_infinity_boundary.py",
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
        "research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-global-case-tree.md",
        "research-notes/lane4-quartic-endgame-20260802-v1/case-tree/lane4-case-tree.csv",
        "manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/quartic_F4_endgame_complete.md",
        "manuscripts/02-low-degree/code/program-2-2026-07-29-v3/f4-marked-chart/verify_quartic_F4_endgame.replay_fixed.py",
    ),
    "intrinsic-degree-valuative-budgets": (
        "research-notes/lane5-degree-budgets",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane5_encoded_shear_packet.py",
    ),
    "homogeneous-realization-compression": (
        "research-tools/filtered_operation_complex",
        "research-notes/lane6-transverse-source-obstruction-20260802-v1",
        "research-notes/finite-diagnostics-20260803-v1/verify_lane6_moving_target_pilot.py",
    ),
    "five-dimensional-collision-geometry": (
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
        "research-notes/lane8-full-root-closure-20260803-v1",
        "research-notes/lane89-mathematical-recovery-20260803-v1",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/F2_degree125_boundary_seed.md",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/verify_F2_degree125_seed.py",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_primary_belyi.py",
        "manuscripts/06-plane-boundary/computational-supplement/terminal-boundary/terminal_face_rigidity.py",
    ),
    "plane-chart-correspondence-global-attachment": (
        "research-notes/lane89-mathematical-recovery-20260803-v1",
        "research-notes/p6-chart-correspondence/LANE9_F2_PARAMETER_COMPLETE_RECURRENCE.md",
        "research-notes/p6-chart-correspondence/lane9_f2_attachment_recurrence.py",
        "research-notes/lane9-wall-shear-20260802-v1/README.md",
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
) -> tuple[bytes, dict[str, Any], set[str]]:
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
        f"- `{record['repo_path']}` — `{record['sha256']}`" for record in records
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
        normalized = "\n".join(
            line.rstrip() for line in source_text.rstrip().splitlines()
        )
        escaped = html.escape(normalized, quote=False).replace("[", "&#91;").replace("]", "&#93;")
        parts.extend(
            [
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
    return payload, item, {record["repo_path"] for record in records}


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
UNIT_PATH_RE = re.compile(r"^/fss/.*/units/(?P<unit>(?:RMU|JCG)-[A-Z0-9]+)\.md$")


def _public_lane_source(
    source: str, *, sequence: int, slug: str, packet_paths: set[str]
) -> str:
    footer = "\n---\n[Portfolio](../README.md) · private v7 candidate · v6h preserved\n"
    if source.count(footer) != 1:
        raise ValueError(f"{slug}: private footer changed or is missing")
    source = source.replace(
        footer,
        "\n---\n[Portfolio](state-of-the-program.md) · "
        f"[Exact source packet](lane-{sequence}-source-packet.md) · "
        "[Release metadata](release.json) · "
        "[Retained mathematics](../working-mathematics/index.md) · "
        "[Current proof sources](../proof-sources/index.md)\n",
    )

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
        if repo_path.endswith((".md", ".py", ".json", ".csv", ".m2", ".sage")):
            if repo_path not in packet_paths:
                raise ValueError(f"{slug}: linked input missing from source packet: {repo_path}")
        else:
            prefix = repo_path + "/"
            if not any(path.startswith(prefix) for path in packet_paths):
                raise ValueError(f"{slug}: linked input directory missing from packet: {repo_path}")
        return f"[{label}](lane-{sequence}-source-packet.md)"

    source = LINK_RE.sub(replace_link, source)
    if "../../../" in source or "](/fss/" in source:
        raise ValueError(f"{slug}: repository-only link survived transformation")
    required = (
        "## Scope",
        "## Setup and definitions",
        "## Results to use",
        "## Live problem",
        "## Tasks",
        "## Limits",
        "## Direct sources",
    )
    missing = [heading for heading in required if heading not in source]
    if missing:
        raise ValueError(f"{slug}: missing v7 sections: {missing}")
    _validate_public(source, source=Path(slug))
    return source


def _public_portfolio(source: str) -> str:
    source = source.replace("# Research handoff v7", "# Current Jacobian research portfolio", 1)
    source = source.replace("Portfolio · 2026-08-03", "Updated 3 August 2026", 1)
    private_intro = """This private, immutable candidate is the model-facing research surface for nine
independent but connected programs. Each lane states the objects before using
them, separates reusable results from examples, and starts its task list at the
actual frontier. Markdown and TeX are the primary mathematical interfaces;
programs are linked only where they replay or construct an exact finite object.

The portfolio does not change any canonical selector, site, release file, or
historical handoff. In particular, v6h remains immutable."""
    public_intro = """These nine independent but connected lanes are the current model-facing
research surface. Each lane defines its objects before use, separates known
results from examples and open problems, and begins at the actual frontier.
Markdown and TeX are the primary mathematical interfaces; programs appear
where they replay or construct an exact finite object."""
    if source.count(private_intro) != 1:
        raise ValueError("portfolio private introduction changed")
    source = source.replace(private_intro, public_intro, 1)
    old_footer = "\n---\nPrivate candidate · v7 · historical sources and selectors unchanged\n"
    new_footer = (
        "\n---\n[Release metadata](release.json) · "
        "[Retained mathematics](../working-mathematics/index.md) · "
        "[Current proof sources](../proof-sources/index.md)\n"
    )
    if source.count(old_footer) != 1:
        raise ValueError("portfolio private footer changed")
    source = source.replace(old_footer, new_footer, 1)
    source = source.replace("lanes/", "")
    _validate_public(source, source=Path("state-of-the-program.md"))
    return source


def _verified_v7_sources(
    *, lane_source_dir: Path, lane_manifest_path: Path
) -> tuple[dict[str, str], str]:
    manifest_payload = lane_manifest_path.read_bytes()
    manifest = _load(lane_manifest_path)
    if manifest.get("handoff_version") != "7" or manifest.get("lane_count") != 9:
        raise ValueError("source manifest must select exactly nine v7 lanes")
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
    return sources, _sha256(manifest_payload)


def _base_payload(base: Path, item: dict[str, Any]) -> bytes:
    payload = (base / item["source"]).read_bytes()
    if len(payload) != item["bytes"] or _sha256(payload) != item["sha256"]:
        raise ValueError(f"base package file differs from manifest: {item['source']}")
    return payload


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
    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")
    if not re.fullmatch(r"[0-9a-f]{40}", args.jacobian_commit):
        raise ValueError("--jacobian-commit must be a full commit hash")

    base_manifest_path = base / "manifest.json"
    base_manifest = _load(base_manifest_path)
    if base_manifest.get("brief_count") != 16 or base_manifest.get("primary_entrypoint_count") != 10:
        raise ValueError("base package must contain sixteen briefs and ten entrypoints")
    v7_sources, v7_manifest_sha = _verified_v7_sources(
        lane_source_dir=lane_source_dir, lane_manifest_path=lane_manifest_path
    )

    packet_outputs: dict[str, tuple[bytes, dict[str, Any], set[str]]] = {}
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
    portfolio_payload = _public_portfolio(v7_sources["state-of-the-program"]).encode("utf-8")
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
        payload = _base_payload(base, item)
        _validate_public(payload.decode("utf-8"), source=base / item["source"])
        prepared_briefs.append((item["source"], payload, item))

    for sequence, slug in LANES:
        item = brief_by_slug[slug]
        packet_paths = packet_outputs[slug][2]
        text = _public_lane_source(
            v7_sources[slug], sequence=sequence, slug=slug, packet_paths=packet_paths
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
            "handoff_version": "7",
            "manifest_sha256": v7_manifest_sha,
            "jacobian_commit": args.jacobian_commit,
        },
        "brief_count": len(prepared_briefs),
        "primary_entrypoint_count": sum(
            bool(item["primary_entrypoint"]) for _, _, item in prepared_briefs
        ),
        "task_input_count": len(task_inputs),
        "task_inputs": [item for _, item in task_inputs],
        "retained_math_v2_markers": base_manifest.get("retained_math_v2_markers", []),
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
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    parser.add_argument("--jacobian-commit", required=True)
    args = parser.parse_args()
    print(json.dumps(build(args), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
