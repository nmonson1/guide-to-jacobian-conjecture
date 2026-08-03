from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "data" / "model-handoffs-v31-20260803a"
EXPECTED_SOURCE_COMMIT = "e23eef3f4b4450f504edaca64a4fd5ab3f0f72df"
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
SEMANTIC_GROUPS = {
    "purpose": ("## Scope", "## Why this lane matters"),
    "setup": (
        "## Setup and definitions",
        "## Setup and notation",
        "## Newton-root conventions",
        "## Fixed \\(F_2\\) chart and support",
    ),
    "reusable mathematics": (
        "## Results to use",
        "## Reusable mathematics",
        "## Closed mathematics below 125",
    ),
    "live problem": ("## Live problem",),
    "ready task": ("## Tasks", "## Ready task ", "## Interface-ready task "),
    "sources": ("## Direct sources", "## Exact sources"),
}


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class ModelHandoffsV31Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            (PACKAGE / "manifest.json").read_text(encoding="utf-8")
        )

    def test_manifest_identity_and_payload_hashes(self) -> None:
        manifest = self.manifest
        self.assertEqual(manifest["schema_version"], 7)
        self.assertEqual(
            manifest["release_id"], "model-handoff-v31a-final-accepted"
        )
        self.assertEqual(manifest["source_handoff"]["handoff_version"], "7i")
        self.assertEqual(
            manifest["source_handoff"]["jacobian_commit"],
            EXPECTED_SOURCE_COMMIT,
        )
        self.assertEqual(manifest["brief_count"], 16)
        self.assertEqual(manifest["primary_entrypoint_count"], 10)
        self.assertEqual(manifest["task_input_count"], 11)
        for item in [*manifest["briefs"], *manifest["task_inputs"]]:
            payload = (PACKAGE / item["source"]).read_bytes()
            self.assertEqual(len(payload), item["bytes"], item["source"])
            self.assertEqual(sha256(payload), item["sha256"], item["source"])

    def test_lane_contract_and_all_local_packet_links(self) -> None:
        lanes = [
            item for item in self.manifest["briefs"] if item["kind"] == "lane"
        ]
        self.assertEqual([item["lane_sequence"] for item in lanes], list(range(1, 10)))
        for item in lanes:
            source = PACKAGE / item["source"]
            text = source.read_text(encoding="utf-8")
            for name, alternatives in SEMANTIC_GROUPS.items():
                self.assertTrue(
                    any(heading in text for heading in alternatives),
                    f"{item['source']}: missing {name}",
                )
            packet = f"lane-{item['lane_sequence']}-source-packet.md"
            anchored = [
                target
                for label, target in LINK_RE.findall(text)
                if target.startswith(f"{packet}#") and label != "Exact source packet"
            ]
            self.assertTrue(anchored, item["source"])
            for _, target in LINK_RE.findall(text):
                if target.startswith(("http://", "https://", "../proof-sources/", "../working-mathematics/")):
                    continue
                path, _, fragment = target.partition("#")
                if path == "release.json":
                    continue
                destination = source if not path else PACKAGE / path
                self.assertTrue(destination.is_file(), f"{source.name}: {target}")
                if fragment:
                    self.assertIn(
                        f'id="{fragment}"',
                        destination.read_text(encoding="utf-8"),
                        f"{source.name}: {target}",
                    )

    def test_source_packets_have_unique_exact_anchors(self) -> None:
        packets = [
            item
            for item in self.manifest["task_inputs"]
            if item["input_id"].endswith("RESEARCH-SOURCE-PACKET-V2")
        ]
        self.assertEqual(len(packets), 9)
        for item in packets:
            text = (PACKAGE / item["source"]).read_text(encoding="utf-8")
            anchors = [
                record["packet_anchor"] for record in item["source_packet"]["files"]
            ]
            self.assertEqual(len(anchors), len(set(anchors)), item["source"])
            for anchor in anchors:
                self.assertRegex(anchor, r"^source-[0-9a-f]{16}$")
                self.assertEqual(text.count(f'id="{anchor}"'), 1)

    def test_repaired_lane_inputs_and_scopes_are_public(self) -> None:
        lane2 = (PACKAGE / "boundary-completeness-torelli-at-infinity.md").read_text()
        lane7 = (PACKAGE / "five-dimensional-collision-geometry.md").read_text()
        lane8 = (PACKAGE / "plane-newton-queue-terminal-certificates.md").read_text()
        lane9 = (PACKAGE / "plane-chart-correspondence-global-attachment.md").read_text()
        portfolio = (PACKAGE / "state-of-the-program.md").read_text()
        self.assertIn("plane case remains open", portfolio)
        self.assertIn("9. Three-chart attachment", portfolio)
        self.assertNotIn("9. Two-chart attachment", portfolio)
        self.assertIn(r"U_{\infty\infty}=D(L_1R_1)", lane2)
        self.assertNotIn("Projective-input boundary audit", lane2)
        self.assertIn("component and Plücker bundle", lane7)
        self.assertIn("14,800 linear", lane8)
        self.assertIn(r"3AB_z-5A_zB+t(A_zB_t-A_tB_z)=-1", lane8)
        self.assertIn(r"\operatorname{Ob}_r=\operatorname{coker}M_r", lane9)
        self.assertIn(r"\operatorname{Ob}_r^\vee\simeq\ker M_r^t", lane9)
        self.assertIn("three-chart finite-order attachment datum", lane9)
        self.assertNotIn("Lane 9 repair bundle", lane9)

        lane2_packet = (PACKAGE / "lane-2-source-packet.md").read_text()
        lane9_packet = (PACKAGE / "lane-9-source-packet.md").read_text()
        self.assertNotIn("verify_lane2_infinity_boundary.py", lane2_packet)
        self.assertNotIn("## Apply the core patch", lane9_packet)

    def test_display_math_and_baseline_regressions(self) -> None:
        portfolio = (PACKAGE / "state-of-the-program.md").read_text()
        lane2 = (PACKAGE / "boundary-completeness-torelli-at-infinity.md").read_text()
        lane5 = (PACKAGE / "intrinsic-degree-valuative-budgets.md").read_text()
        lane6 = (PACKAGE / "homogeneous-realization-compression.md").read_text()
        self.assertIn("baseline counterexample", portfolio)
        self.assertIn("## Baseline counterexample", lane5)
        self.assertIn("F_0(0,0,-1/4)", lane5)
        self.assertIn(r"carrying \(J_0\) to \(J'_0\)", lane2)
        self.assertIn(r"map \(F_0=(P,Q,R)\)", lane5)
        self.assertIn(r"over \(\mathbf Q\), hence over", lane5)
        self.assertIn(r"form \(I+H\)", lane6)
        self.assertIn(r"\(H=(tQ+t^2Bw,-q,0)\)", lane6)

        lane1 = (PACKAGE / "cubic-flatness-normalization-defects.md").read_text()
        lane8 = (PACKAGE / "plane-newton-queue-terminal-certificates.md").read_text()
        lane9 = (PACKAGE / "plane-chart-correspondence-global-attachment.md").read_text()
        self.assertIn(r"\(L^{[n]}=(L^{\otimes n})^{\vee\vee}\)", lane1)
        self.assertIn(r"\(m_\lambda=6\)", lane8)
        self.assertIn(r"\(E_\lambda=T_E(\lambda)E_0\)", lane9)
        self.assertIn("## Interface-ready task L9-T1", lane9)

        lane_items = [
            item for item in self.manifest["briefs"] if item["kind"] == "lane"
        ]
        for item in lane_items:
            source = PACKAGE / item["source"]
            lines = source.read_text(encoding="utf-8").splitlines()
            for index, line in enumerate(lines):
                if line == r"\[":
                    self.assertTrue(
                        index == 0 or not lines[index - 1].strip(),
                        f"{source}:{index + 1}: display opener follows prose",
                    )
                if line == r"\]":
                    self.assertTrue(
                        index + 1 == len(lines) or not lines[index + 1].strip(),
                        f"{source}:{index + 1}: display closer precedes prose",
                    )


if __name__ == "__main__":
    unittest.main()
