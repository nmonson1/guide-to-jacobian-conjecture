from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "data" / "model-handoffs-v24-20260803b"
BASE = ROOT / "data" / "model-handoffs-v23-20260803a"
FORBIDDEN = ("/fss/", "/home/", "chatgpt.com/share", "sandbox:", "registry/")
LANE_SECTIONS = (
    "## Scope",
    "## Setup and definitions",
    "## Results to use",
    "## Live problem",
    "## Tasks",
    "## Limits",
    "## Direct sources",
)


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class ModelHandoffsV24Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads((PACKAGE / "manifest.json").read_text())
        cls.base_manifest = json.loads((BASE / "manifest.json").read_text())

    def test_manifest_and_all_payload_hashes(self) -> None:
        manifest = self.manifest
        self.assertEqual(manifest["schema_version"], 7)
        self.assertEqual(manifest["source_handoff"]["handoff_version"], "7")
        self.assertEqual(manifest["brief_count"], 16)
        self.assertEqual(manifest["primary_entrypoint_count"], 10)
        self.assertEqual(manifest["task_input_count"], 11)
        for item in [*manifest["briefs"], *manifest["task_inputs"]]:
            payload = (PACKAGE / item["source"]).read_bytes()
            self.assertEqual(len(payload), item["bytes"], item["source"])
            self.assertEqual(_sha256(payload), item["sha256"], item["source"])

    def test_six_program_dossiers_are_compact_graph_overlays(self) -> None:
        current = {
            item["program_slug"]: item
            for item in self.manifest["briefs"]
            if item["kind"] == "program"
        }
        self.assertEqual(len(current), 6)
        dossier_source = self.manifest["program_dossiers"]
        self.assertEqual(
            dossier_source["kind"], "generated_graph_view_overlays"
        )
        for slug, item in current.items():
            text = (PACKAGE / item["source"]).read_text()
            self.assertIn(
                f"../working-mathematics/programs/{slug}.md", text
            )
            self.assertIn("## Current research entrypoints", text)
            self.assertIn("does not copy theorem statements", text)
            self.assertNotIn("Reusable inputs", text)
            self.assertNotIn("Proof-signature index", text)
            self.assertNotIn("../../claims/", text)
            self.assertNotIn("{{MANUSCRIPT_", text)

    def test_focused_pages_have_v7_structure_and_public_footer(self) -> None:
        lanes = [item for item in self.manifest["briefs"] if item["kind"] == "lane"]
        self.assertEqual(len(lanes), 9)
        for item in lanes:
            text = (PACKAGE / item["source"]).read_text()
            lines = text.splitlines()
            self.assertTrue(lines[0].startswith("# "), item["source"])
            self.assertRegex(lines[2], r"^Lane [1-9] · 2026-08-03$")
            for heading in LANE_SECTIONS:
                self.assertIn(heading, text, item["source"])
            self.assertIn("[Exact source packet](lane-", text)
            self.assertIn("[Release metadata](release.json)", text)
            self.assertIn("[Retained mathematics](../working-mathematics/index.md)", text)
            self.assertIn("[Current proof sources](../proof-sources/index.md)", text)

    def test_source_packet_metadata_maps_canonical_repo_paths(self) -> None:
        packets = [
            item
            for item in self.manifest["task_inputs"]
            if item["input_id"].endswith("RESEARCH-SOURCE-PACKET-V2")
        ]
        self.assertEqual(len(packets), 9)
        for item in packets:
            metadata = item["source_packet"]
            self.assertEqual(metadata["source_root"], "jacobian_repository")
            self.assertRegex(metadata["source_commit"], r"^[0-9a-f]{40}$")
            text = (PACKAGE / item["source"]).read_text()
            self.assertTrue(metadata["files"], item["source"])
            for record in metadata["files"]:
                repo_path = record["repo_path"]
                self.assertEqual(record["packet_path"], repo_path)
                self.assertFalse(Path(repo_path).is_absolute(), repo_path)
                self.assertNotIn("..", Path(repo_path).parts)
                self.assertRegex(record["sha256"], r"^[0-9a-f]{64}$")
                self.assertIn(f"## `{repo_path}`", text)
                self.assertIn(record["sha256"], text)

    def test_public_package_has_no_private_locator(self) -> None:
        for path in PACKAGE.iterdir():
            if not path.is_file():
                continue
            text = path.read_text()
            lowered = text.casefold()
            for marker in FORBIDDEN:
                self.assertNotIn(marker.casefold(), lowered, f"{marker}: {path.name}")

    def test_handoff_local_links_resolve_or_are_generated_routes(self) -> None:
        link_re = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")
        for item in self.manifest["briefs"]:
            text = (PACKAGE / item["source"]).read_text()
            for target in link_re.findall(text):
                if target.startswith(("http://", "https://", "../", "../../")):
                    continue
                if target == "release.json":
                    continue
                self.assertTrue((PACKAGE / target).is_file(), f"{item['source']}: {target}")


if __name__ == "__main__":
    unittest.main()
