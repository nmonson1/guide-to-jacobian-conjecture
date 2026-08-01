#!/usr/bin/env python3
"""Build a write-once hub + lane + program handoff release."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

LANES = (
    (
        1,
        "cubic-flatness-normalization-defects",
        "Cubic flatness and finite normalization defects",
        ["cubic-marked-root-incidence-geometry", "stable-moduli"],
    ),
    (
        2,
        "boundary-completeness-torelli-at-infinity",
        "Boundary completeness and Torelli at infinity",
        ["cubic-marked-root-incidence-geometry", "stable-moduli"],
    ),
    (
        3,
        "bounded-degree-deformation-modulus-onset",
        "Bounded-degree deformation and modulus onset",
        ["local-rigidity-and-deformation-algebra", "stable-moduli"],
    ),
    (
        4,
        "quartic-endgame",
        "The quartic endgame",
        ["minimum-degree-and-quartic-exclusions"],
    ),
    (
        5,
        "intrinsic-degree-valuative-budgets",
        "Intrinsic degree and valuative budgets",
        [
            "minimum-degree-and-quartic-exclusions",
            "stable-moduli",
            "plane-boundary-obstructions",
        ],
    ),
    (
        6,
        "homogeneous-realization-compression",
        "Homogeneous realization and compression",
        [
            "homogeneous-descendants",
            "local-rigidity-and-deformation-algebra",
        ],
    ),
    (
        7,
        "five-dimensional-collision-geometry",
        "Five-dimensional collision geometry",
        ["homogeneous-descendants"],
    ),
    (
        8,
        "plane-newton-queue-terminal-certificates",
        "Plane Newton queue and terminal certificates",
        ["plane-boundary-obstructions"],
    ),
    (
        9,
        "plane-chart-correspondence-global-attachment",
        "Plane chart correspondence and global attachment",
        ["plane-boundary-obstructions", "stable-moduli"],
    ),
)

HUB_LINKS = {
    "#lane-1-cubic-flatness": "cubic-flatness-normalization-defects.md",
    "#lane-2-boundary-torelli": "boundary-completeness-torelli-at-infinity.md",
    "#lane-3-deformation-moduli": "bounded-degree-deformation-modulus-onset.md",
    "#lane-4-quartic-endgame": "quartic-endgame.md",
    "#lane-5-degree-budgets": "intrinsic-degree-valuative-budgets.md",
    "#lane-6-homogeneous-compression": "homogeneous-realization-compression.md",
    "#lane-7-collision-geometry": "five-dimensional-collision-geometry.md",
    "#lane-8-plane-newton-queue": "plane-newton-queue-terminal-certificates.md",
    "#lane-9-plane-global-attachment": "plane-chart-correspondence-global-attachment.md",
}

OLD_PR_PARAGRAPH = r"""PR 1's newer head adds an exact Program 5 tangent bridge: dimensions
20 inside 22, quartic value \(1\) on the full affine tangent plane, and a
second-order rank-six section. The repaired exact search over all 66
quadratic tangent parameters gives cubic effect rank 15 and augmented rank
16, certifying an intrinsic cubic obstruction for that selected plane. These
inputs are now retained graph units; none of the four stale generated-site
trees was merged."""

NEW_PR_PARAGRAPH = """PR 1's exact Program 5 continuation now classifies every finite slope in
the selected rank-six plane through its first intrinsic obstruction. Generic
slopes and the rational exceptional slope `r=4` fail at cubic order. The two
conjugate slopes `r=4+-4 sqrt(-3)` have 17-dimensional cubic-lift fibres but
an intrinsic quartic obstruction, with exact certificate pairing `-1152`.
This remains a selected-plane result, not a classification of the full finite
row-base fibre or stable quotient.

Three other bounded advances are now retained: ordered-composition PRS charts
and block-constant Smith exponents in Lane 2; a five-variable universal
order-six system in Lane 3; and the Program 5 five-dimensional polynomial-gauge
core, whose degree-one obstruction is supported on three explicit surfaces.
Each lane page states the exact remaining hypotheses and next calculation.
None of the four stale generated-site trees was merged."""


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def validate_public(text: str, *, source: Path) -> str:
    forbidden = (
        "/fss/",
        "/home/",
        "chatgpt.com/share",
        "INTAKE-",
        "sandbox:/",
    )
    found = [item for item in forbidden if item.casefold() in text.casefold()]
    if found:
        raise ValueError(f"{source}: forbidden public markers: {found}")
    return text


def update_hub(text: str) -> str:
    for old, new in HUB_LINKS.items():
        if text.count(old) != 1:
            raise ValueError(f"hub expected exactly one link target {old}")
        text = text.replace(old, new)
    if text.count(OLD_PR_PARAGRAPH) != 1:
        raise ValueError("hub PR paragraph did not match exactly once")
    text = text.replace(OLD_PR_PARAGRAPH, NEW_PR_PARAGRAPH)
    text = text.replace(
        "## Research freedom and how to use the nine links",
        "## Research freedom and how to use the nine lane pages",
        1,
    )
    text = text.replace(
        "Each link opens this complete portfolio at a suggested frontier",
        "Each lane page opens a suggested frontier",
        1,
    )
    text = text.replace(
        "**Research state:** mathematical checkpoint 29 July 2026. Exact scope,",
        "**Research state:** mathematical checkpoint 1 August 2026. Exact scope,",
        1,
    )
    text = text.replace(
        "Share the whole page, optionally with one of these stable fragments:",
        "Share this portfolio hub or one of these focused lane pages:",
        1,
    )
    return text


def entry(item: dict[str, object], text: str) -> dict[str, object]:
    payload = text.encode("utf-8")
    return {
        **item,
        "sha256": sha256(payload),
        "bytes": len(payload),
        "words": len(text.split()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", type=Path, required=True)
    parser.add_argument("--lane-source-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    parser.add_argument("--updated-at", required=True)
    args = parser.parse_args()

    output = args.output_dir.resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing path: {output}")
    if output.parent != (ROOT / "data").resolve():
        raise ValueError("output directory must be a direct child of site data/")

    base_manifest = json.loads(
        (args.base_dir / "manifest.json").read_text(encoding="utf-8")
    )
    if base_manifest.get("brief_count") != 7:
        raise ValueError("base release must contain the hub and six programs")

    prepared: list[tuple[str, str, dict[str, object]]] = []
    for base in base_manifest["briefs"]:
        source = args.base_dir / base["source"]
        payload = source.read_bytes()
        if len(payload) != base["bytes"] or sha256(payload) != base["sha256"]:
            raise ValueError(f"base source does not match manifest: {source}")
        text = payload.decode("utf-8")
        if base["kind"] == "cross_program":
            text = update_hub(text)
            extra = {
                "primary_entrypoint": True,
                "display_sequence": 0,
                "related_programs": [],
            }
        else:
            extra = {
                "primary_entrypoint": False,
                "display_sequence": 100 + base["program_sequence"],
                "related_programs": [base["program_slug"]],
            }
        text = validate_public(text, source=source)
        prepared.append(
            (
                base["source"],
                text,
                entry({**base, **extra}, text),
            )
        )

    for sequence, slug, title, programs in LANES:
        source = args.lane_source_dir / f"{slug}.md"
        text = validate_public(source.read_text(encoding="utf-8"), source=source)
        if not 350 <= len(text.split()) <= 2000:
            raise ValueError(f"{slug}: lane word count outside 350--2000")
        item = {
            "kind": "lane",
            "lane_sequence": sequence,
            "program_sequence": 10 + sequence,
            "program_slug": slug,
            "title": title,
            "source": f"{slug}.md",
            "route": f"research/handoffs/{slug}.md",
            "primary_entrypoint": True,
            "display_sequence": sequence,
            "related_programs": programs,
        }
        prepared.append((f"{slug}.md", text, entry(item, text)))

    output.mkdir()
    for name, text, _ in prepared:
        (output / name).write_text(text, encoding="utf-8")
    manifest = {
        "schema_version": 2,
        "release_id": args.release_id,
        "updated_at": args.updated_at,
        "brief_count": len(prepared),
        "primary_entrypoint_count": sum(
            bool(item["primary_entrypoint"]) for _, _, item in prepared
        ),
        "briefs": [item for _, _, item in prepared],
    }
    manifest_path = output / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output_dir": str(output),
                "release_id": args.release_id,
                "brief_count": len(prepared),
                "primary_entrypoint_count": manifest["primary_entrypoint_count"],
                "manifest_sha256": sha256(manifest_path.read_bytes()),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
