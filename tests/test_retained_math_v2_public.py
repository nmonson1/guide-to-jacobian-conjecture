from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_living_guide_v2 import (  # noqa: E402
    render_compatible_claim,
    render_compatible_collection,
    render_retained_v2_unit,
)
from prepare_retained_math_v2_data_v1 import (  # noqa: E402
    _prepare_full_materialization,
)
from retained_math_v2_public import (  # noqa: E402
    compatibility_by_id,
    validate_legacy_compatibility,
    validate_public_v2_graph,
)


SCHEMA = ROOT / "schemas/legacy-compatibility-v1.schema.json"
ZERO_SHA = "0" * 64


def _unit(
    unit_id: str,
    statement: str,
    *,
    relations: list[dict[str, str]] | None = None,
    argument_ids: list[str] | None = None,
    evidence_ids: list[str] | None = None,
) -> dict[str, object]:
    return {
        "unit_id": unit_id,
        "title": f"Current {unit_id}",
        "unit_type": "theorem",
        "statement": statement,
        "statement_version": 2,
        "hypotheses": ["The stated test hypotheses hold."],
        "exact_scope": {
            "applies_to": ["The test setting."],
            "limitations": ["No wider statement is asserted."],
        },
        "argument_ids": argument_ids or [],
        "evidence_ids": evidence_ids or [],
        "obligation_ids": [],
        "relations": relations or [],
        "memberships": {"programs": ["test-program"], "storylines": []},
        "attribution": {"credited_to": ["Test author"], "citations": []},
    }


def _graph() -> dict[str, object]:
    units = [
        _unit(
            "JCG-00000001",
            "Current exact mathematics.",
            argument_ids=["ARG-EXACT-PROOF"],
            evidence_ids=["EVD-EXACT-SOURCE"],
        ),
        _unit("JCG-00000002", "The valid weaker mathematics."),
        _unit(
            "RMU-00000011",
            "The stronger current mathematics.",
            relations=[
                {
                    "relation_type": "strengthens",
                    "target_unit_id": "JCG-00000002",
                }
            ],
        ),
        _unit(
            "RMU-00000012",
            "The corrected replacement mathematics.",
            relations=[
                {
                    "relation_type": "corrects",
                    "target_unit_id": "JCG-00000003",
                },
                {
                    "relation_type": "depends_on",
                    "target_unit_id": "JCG-00000001",
                },
            ],
        ),
        _unit(
            "RMU-00000013",
            "First split replacement.",
            relations=[
                {
                    "relation_type": "corrects",
                    "target_unit_id": "JCG-00000004",
                }
            ],
        ),
        _unit(
            "RMU-00000014",
            "Second split replacement.",
            relations=[
                {
                    "relation_type": "supersedes",
                    "target_unit_id": "JCG-00000004",
                }
            ],
        ),
    ]
    arguments = [
        {
            "argument_id": "ARG-EXACT-PROOF",
            "title": "Exact proof",
            "argument_type": "proof",
            "summary": "The exact summary.",
            "body": "The complete argument body.",
            "conclusion_unit_ids": ["JCG-00000001"],
            "premise_unit_ids": [],
            "depends_on_argument_ids": [],
            "evidence_ids": ["EVD-EXACT-SOURCE"],
            "does_not_establish": ["A converse."],
            "memberships": {"programs": ["test-program"], "storylines": []},
        }
    ]
    evidence = [
        {
            "evidence_id": "EVD-EXACT-SOURCE",
            "title": "Published exact source",
            "kind": "proof",
            "summary": "The source contains the proof.",
            "establishes": "The current exact mathematics.",
            "target_unit_ids": ["JCG-00000001"],
            "target_argument_ids": ["ARG-EXACT-PROOF"],
            "does_not_establish": ["A converse."],
            "locator": {
                "kind": "repo",
                "repo_path": "manuscripts/01-test/main.tex",
                "anchor": "thm:exact",
            },
        }
    ]
    return {
        "schema_version": 2,
        "registry_id": "RETAINED2-test",
        "base_registry": {"registry_id": "RETAINED-test", "sha256": ZERO_SHA},
        "counts": {
            "programs": 1,
            "units": len(units),
            "arguments": len(arguments),
            "evidence": len(evidence),
            "obligations": 0,
            "tasks": 0,
        },
        "programs": [
            {
                "slug": "test-program",
                "title": "Test program",
                "summary": "A test program.",
            }
        ],
        "units": units,
        "arguments": arguments,
        "evidence": evidence,
        "obligations": [],
        "tasks": [],
    }


def _target(
    unit_id: str, role: str, relation_type: str | None = None
) -> dict[str, object]:
    result: dict[str, object] = {
        "unit_id": unit_id,
        "statement_version": 2,
        "role": role,
    }
    if relation_type:
        result["relation_type"] = relation_type
    return result


def _compatibility() -> dict[str, object]:
    routes = [
        {
            "legacy_unit_id": "JCG-00000001",
            "route": "claims/JCG-00000001/",
            "disposition": "exact_current",
            "targets": [_target("JCG-00000001", "current_statement")],
        },
        {
            "legacy_unit_id": "JCG-00000002",
            "route": "claims/JCG-00000002/",
            "disposition": "valid_weaker",
            "targets": [
                _target("JCG-00000002", "current_statement"),
                _target("RMU-00000011", "stronger_result", "strengthens"),
            ],
        },
        {
            "legacy_unit_id": "JCG-00000003",
            "route": "claims/JCG-00000003/",
            "disposition": "replacement",
            "targets": [
                _target("RMU-00000012", "replacement", "corrects")
            ],
        },
        {
            "legacy_unit_id": "JCG-00000004",
            "route": "claims/JCG-00000004/",
            "disposition": "split_replacement",
            "targets": [
                _target("RMU-00000013", "replacement", "corrects"),
                _target("RMU-00000014", "replacement", "supersedes"),
            ],
        },
        {
            "legacy_unit_id": "JCG-00000005",
            "route": "claims/JCG-00000005/",
            "disposition": "archival",
            "targets": [],
        },
    ]
    return {
        "schema_version": 1,
        "map_id": "LEGACY-COMPAT-000000000000",
        "source_registry": {"registry_id": "RETAINED2-test", "sha256": ZERO_SHA},
        "counts": {
            "routes": 5,
            "archival": 1,
            "exact_current": 1,
            "replacement": 1,
            "split_replacement": 1,
            "valid_weaker": 1,
        },
        "routes": routes,
    }


def _claim(tag: str, *, collection: bool = False) -> dict[str, object]:
    membership = (
        [
            {
                "collection_slug": "test-collection",
                "inclusion": "direct",
                "role": "component",
            }
        ]
        if collection
        else []
    )
    return {
        "tag": tag,
        "title": f"Stale title {tag}",
        "statement": f"STALE STATEMENT {tag}",
        "statement_version": 1,
        "kind": "result",
        "status": "proof offered",
        "prominence": "supporting",
        "memberships": membership,
        "proof_access": [],
        "locators": [],
        "verification": {"evidence": []},
        "provenance": {"sources": [], "credited_to": [], "ai_assistance": {}},
    }


def _collection() -> dict[str, object]:
    return {
        "slug": "test-collection",
        "title": "Test collection",
        "description": "Current collection description.",
        "kind": "result",
        "statement": "The package-level current statement.",
        "member_tags": [f"JCG-{value:08d}" for value in range(1, 6)],
        "manuscript_coverage": {
            "status": "complete",
            "coverage_rule": "The exact source is published.",
        },
        "source_treatment": "Evidence is scoped claim by claim.",
        "source": [],
        "credited_to": [],
        "connections": {"depends_on": [], "shares_claims_with": []},
    }


def _proof_sources() -> dict[str, object]:
    return {
        "files": [
            {
                "path": "01-test/main.tex",
                "labels": [
                    {
                        "label": "thm:exact",
                        "anchor": "label-thm-exact",
                        "line": 7,
                        "path": "01-test/main.tex",
                    }
                ],
            }
        ]
    }


class PublicRetainedMathV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = _graph()
        self.compatibility = _compatibility()
        self.units = {item["unit_id"]: item for item in self.graph["units"]}
        self.routes = compatibility_by_id(self.compatibility)

    def test_validates_all_dispositions_and_forward_directions(self) -> None:
        self.assertEqual(
            validate_public_v2_graph(self.graph), self.graph["counts"]
        )
        counts = validate_legacy_compatibility(
            self.compatibility,
            graph=self.graph,
            expected_legacy_ids=set(self.routes),
            schema_path=SCHEMA,
        )
        self.assertEqual(counts, self.compatibility["counts"])

    def test_rejects_non_total_compatibility_map(self) -> None:
        broken = deepcopy(self.compatibility)
        broken["routes"].pop()
        with self.assertRaisesRegex(ValueError, "not total"):
            validate_legacy_compatibility(
                broken,
                graph=self.graph,
                expected_legacy_ids=set(self.routes),
            )

    def test_rejects_stale_compatibility_target_version(self) -> None:
        broken = deepcopy(self.compatibility)
        broken["routes"][0]["targets"][0]["statement_version"] = 1
        with self.assertRaisesRegex(ValueError, "stale statement version"):
            validate_legacy_compatibility(
                broken,
                graph=self.graph,
                expected_legacy_ids=set(self.routes),
            )

    def test_rejects_internal_workflow_fields_from_public_graph(self) -> None:
        broken = deepcopy(self.graph)
        broken["units"][0]["review_state"] = "unchecked"
        with self.assertRaisesRegex(ValueError, "internal workflow fields"):
            validate_public_v2_graph(broken)

    def test_stable_routes_render_current_replacement_and_archival_states(self) -> None:
        exact = render_compatible_claim(
            _claim("JCG-00000001"),
            {},
            self.routes["JCG-00000001"],
            self.units,
        )
        weaker = render_compatible_claim(
            _claim("JCG-00000002"),
            {},
            self.routes["JCG-00000002"],
            self.units,
        )
        replacement = render_compatible_claim(
            _claim("JCG-00000003"),
            {},
            self.routes["JCG-00000003"],
            self.units,
        )
        split = render_compatible_claim(
            _claim("JCG-00000004"),
            {},
            self.routes["JCG-00000004"],
            self.units,
        )
        archival = render_compatible_claim(
            _claim("JCG-00000005"),
            {},
            self.routes["JCG-00000005"],
            self.units,
        )

        self.assertIn("Current exact mathematics.", exact)
        self.assertNotIn("STALE STATEMENT", exact)
        self.assertIn("The valid weaker mathematics.", weaker)
        self.assertIn("A stronger current result is available", weaker)
        self.assertIn("RMU-00000011.md", weaker)
        self.assertNotIn("STALE STATEMENT", replacement)
        self.assertIn("The corrected replacement mathematics.", replacement)
        self.assertIn("First split replacement.", split)
        self.assertIn("Second split replacement.", split)
        self.assertNotIn("STALE STATEMENT", split)
        self.assertIn("Historical claim", archival)
        self.assertNotIn("STALE STATEMENT", archival)

    def test_archival_member_is_absent_from_current_collection(self) -> None:
        claims = {
            tag: _claim(tag, collection=True) for tag in self.routes
        }
        rendered = render_compatible_collection(
            _collection(), claims, {"test-collection": _collection()}, self.routes, self.units
        )
        self.assertNotIn("JCG-00000005", rendered)
        self.assertNotIn("STALE STATEMENT JCG-00000003", rendered)
        self.assertIn("The corrected replacement mathematics.", rendered)
        self.assertIn("The valid weaker mathematics.", rendered)

    def test_current_unit_renders_argument_evidence_and_source_not_history(self) -> None:
        exact = render_retained_v2_unit(
            self.units["JCG-00000001"], self.graph, _proof_sources()
        )
        replacement = render_retained_v2_unit(
            self.units["RMU-00000012"], self.graph, _proof_sources()
        )
        machine = json.dumps(self.graph, sort_keys=True)

        self.assertIn("The complete argument body.", exact)
        self.assertIn("The source contains the proof.", exact)
        self.assertIn(
            "../../proof-sources/01-test/main.md#label-thm-exact", exact
        )
        self.assertIn("`depends_on`", replacement)
        self.assertNotIn("`corrects`", replacement)
        self.assertNotIn("JCG-00000003", replacement)
        self.assertNotIn("review_state", exact)
        self.assertIn('"relation_type": "corrects"', machine)

    def test_full_package_pins_graph_and_total_map(self) -> None:
        graph_payload = (
            json.dumps(self.graph, indent=2, sort_keys=True) + "\n"
        ).encode()
        compatibility_payload = (
            json.dumps(self.compatibility, indent=2, sort_keys=True) + "\n"
        ).encode()
        source_manifest = {
            "registry_id": self.graph["registry_id"],
            "files": [
                {
                    "path": "public-graph.json",
                    "sha256": hashlib.sha256(graph_payload).hexdigest(),
                    "size_bytes": len(graph_payload),
                }
            ],
        }
        source_manifest_payload = (
            json.dumps(source_manifest, sort_keys=True) + "\n"
        ).encode()
        claim_graph = {
            "claims": [{"tag": tag} for tag in sorted(self.routes)]
        }
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            compatibility_path = root / "compatibility.json"
            compatibility_path.write_bytes(compatibility_payload)
            claim_graph_path = root / "claims.json"
            claim_graph_path.write_text(json.dumps(claim_graph), encoding="utf-8")
            output = root / "output"
            result = _prepare_full_materialization(
                graph=self.graph,
                graph_payload=graph_payload,
                source_manifest_payload=source_manifest_payload,
                compatibility_path=compatibility_path,
                legacy_claim_graph_path=claim_graph_path,
                output=output,
                release_id="test-release",
                updated_at="2026-08-03T00:00:00Z",
            )
            manifest = json.loads((output / "manifest.json").read_text())
            self.assertEqual(result["compatibility_counts"]["routes"], 5)
            self.assertEqual(
                {item["path"] for item in manifest["files"]},
                {"public-graph.json", "legacy-compatibility.json"},
            )
            with self.assertRaises(FileExistsError):
                _prepare_full_materialization(
                    graph=self.graph,
                    graph_payload=graph_payload,
                    source_manifest_payload=source_manifest_payload,
                    compatibility_path=compatibility_path,
                    legacy_claim_graph_path=claim_graph_path,
                    output=output,
                    release_id="test-release",
                    updated_at="2026-08-03T00:00:00Z",
                )

    def test_current_claim_contract_has_all_368_stable_urls(self) -> None:
        state = json.loads((ROOT / "site-state.json").read_text())
        claim_graph = json.loads(
            (
                ROOT
                / "data"
                / state["claim_graph"]["data_dir"]
                / "claim-graph.json"
            ).read_text()
        )
        tags = {item["tag"] for item in claim_graph["claims"]}
        self.assertEqual(len(tags), 368)
        self.assertEqual(
            {f"claims/{tag}/" for tag in tags},
            {f"claims/{item['tag']}/" for item in claim_graph["claims"]},
        )


if __name__ == "__main__":
    unittest.main()
