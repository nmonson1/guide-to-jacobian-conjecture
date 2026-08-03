"""Manifest-shape and theorem-boundary validation."""
from __future__ import annotations

from typing import Any

from .common import require


def validate_manifest_shape(manifest: dict[str, Any]) -> None:
    require(manifest["schema"] == "jcg-lane8-proof-carrying-queue-v1", "unexpected manifest schema")
    require(manifest["contribution_id"] == "JCG-C-0015", "unexpected contribution ID")
    source_ids = [source["id"] for source in manifest["sources"]]
    require(len(source_ids) == len(set(source_ids)), "duplicate source ID")
    require(len(manifest["checklist"]) == 11, "checklist length changed")
    statuses = {item["item"]: item["status"] for item in manifest["checklist"]}
    require(all(status not in {"open", "not_attempted"} for status in statuses.values()),
            "an item was not attempted")
    require(statuses["Attach the stored adjacent-chart terminal certificate"] == "attempted_not_covering",
            "adjacent-chart result is overstated")
    require(statuses["Prove all full-root children reach an empty terminal node"]
            == "complete_for_direct_queue", "direct full-root closure not recorded")

    stage_ids = [stage["id"] for stage in manifest["stages"]]
    require(len(stage_ids) == len(set(stage_ids)) == 10,
            "stage manifest must contain ten unique stages")
    keys = ("root", "role", "status", "field", "ring", "variables",
            "ideal_or_equations", "denominators", "denominator_zero_complements",
            "saturation_factors", "output", "evidence")
    for stage in manifest["stages"]:
        for key in keys:
            require(key in stage, f"stage {stage['id']} lacks {key}")
        for denominator in stage["denominators"]:
            require("geometric_complement" in denominator,
                    f"stage {stage['id']} denominator lacks complement ledger")

    scheme_lift = manifest["queue"]["closure"]["full"]["scheme_lift"]
    require("full layer-through-eight obstruction scheme" in scheme_lift
            and "layer-four square hypersurface alone is not claimed empty" in scheme_lift,
            "full closure does not state the reduced/scheme-level boundary correctly")
    below = manifest["queue"]["closure"]["below_125"]
    require(below["status"] == "deduced_from_imported_reduction",
            "below-125 boundary is not explicit")
    require(not below["independent_literature_reproof"],
            "manifest falsely claims a literature reproof")
    require("SRC-GGHV-2022" in below["imports"],
            "below-125 deduction lacks the external reduction")
