from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
import zipfile
from io import BytesIO
from pathlib import Path
from unittest import mock

from scripts import prepare_model_handoffs_v7 as handoffs


def _manifest_record(root: Path, path: Path) -> dict[str, object]:
    payload = path.read_bytes()
    text = payload.decode("utf-8")
    return {
        "path": path.relative_to(root).as_posix(),
        "line_count": len(text.splitlines()),
        "byte_count": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


class PrepareModelHandoffsV7Tests(unittest.TestCase):
    def test_lane3_multiplier_is_hash_pinned_binary_input(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "exact-multiplier.bin"
            path.write_bytes(b"KMRAT001" + bytes(range(32)))
            payload, item = handoffs._lane3_multiplier_input(path)

        self.assertTrue(payload.startswith(b"KMRAT001"))
        self.assertEqual(item["input_id"], "LANE3-EXACT-MULTIPLIER-V1")
        self.assertEqual(item["binary_format"], "KMRAT001")
        self.assertEqual(item["bytes"], len(payload))
        self.assertEqual(item["sha256"], hashlib.sha256(payload).hexdigest())

    def test_source_packet_exposes_stable_per_file_anchors(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_path = root / "research-notes" / "exact-proof.md"
            source_path.parent.mkdir(parents=True)
            source_path.write_text("# Exact proof\n\nBody.\n", encoding="utf-8")
            slug = "synthetic-lane"
            with mock.patch.dict(
                handoffs.PACKET_INPUTS,
                {slug: ("research-notes/exact-proof.md",)},
            ):
                (
                    payload,
                    item,
                    anchors,
                    archive_payload,
                    archive_item,
                ) = handoffs._source_packet(
                    sequence=1,
                    slug=slug,
                    repo_root=root,
                    source_commit="a" * 40,
                )

        repo_path = "research-notes/exact-proof.md"
        anchor = handoffs._source_anchor(repo_path)
        text = payload.decode("utf-8")
        self.assertEqual(anchors, {repo_path: anchor})
        self.assertIn(f'<a id="{anchor}"></a>', text)
        self.assertIn(f"](#{anchor})", text)
        record = item["source_packet"]["files"][0]
        self.assertEqual(record["packet_anchor"], anchor)
        self.assertEqual(archive_item["media_type"], "application/zip")
        self.assertTrue(archive_payload.startswith(b"PK\x03\x04"))

    def test_source_archive_is_deterministic_sanitized_repository_tree(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source_path = root / "research-notes" / "run.py"
            source_path.parent.mkdir(parents=True)
            source_path.write_text(
                "artifact = '/fss/private/result.json'\nprint(artifact)\n",
                encoding="utf-8",
            )
            slug = "synthetic-lane"
            with mock.patch.dict(
                handoffs.PACKET_INPUTS,
                {slug: ("research-notes/run.py",)},
            ):
                first = handoffs._source_packet(
                    sequence=2,
                    slug=slug,
                    repo_root=root,
                    source_commit="b" * 40,
                )
                second = handoffs._source_packet(
                    sequence=2,
                    slug=slug,
                    repo_root=root,
                    source_commit="b" * 40,
                )

        self.assertEqual(first[3], second[3])
        self.assertEqual(first[4]["sha256"], hashlib.sha256(first[3]).hexdigest())
        with zipfile.ZipFile(BytesIO(first[3])) as archive:
            self.assertEqual(archive.namelist(), ["research-notes/run.py"])
            info = archive.getinfo("research-notes/run.py")
            self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
            archived = archive.read(info)
        self.assertIn(b"/path/to/versioned-artifact", archived)
        self.assertNotIn(b"/fss/", archived)
        self.assertEqual(
            first[4]["source_tree"]["files"][0]["sha256"],
            hashlib.sha256(archived).hexdigest(),
        )

    def test_lane_links_target_exact_packet_file_and_specialized_routes(
        self,
    ) -> None:
        source = """# Synthetic lane

Lane 7 · 2026-08-03

## Why this lane matters

Reason.

## Setup and notation

Definitions.

## Reusable mathematics

[Exact proof](../../../research-notes/exact-proof.md)
[Exact multiplier](https://nmonson1.github.io/guide-to-jacobian-conjecture/research/inputs/lane3-exact-multiplier.bin)

## Live problem

Problem.

## Ready task L7-T1 — begin

Task.

## Exact sources

[Proof again](../../../research-notes/exact-proof.md)

---
[Portfolio](../README.md) · successor v7c candidate · immutable v7 preserved
"""
        repo_path = "research-notes/exact-proof.md"
        anchor = handoffs._source_anchor(repo_path)
        public = handoffs._public_lane_source(
            source,
            sequence=7,
            slug="synthetic-lane",
            packet_anchors={repo_path: anchor},
        )

        exact_target = f"lane-7-source-packet.md#{anchor}"
        self.assertEqual(public.count(exact_target), 2)
        self.assertIn("(lane-7-collision-input.md)", public)
        self.assertIn("(../inputs/lane-7-source-files.zip)", public)
        self.assertIn("(../inputs/lane3-exact-multiplier.bin)", public)
        self.assertNotIn("https://nmonson1.github.io", public)
        self.assertNotIn("../../../", public)

    def test_lane_8_footer_preserves_raw_reconstruction_route(self) -> None:
        source = """# Synthetic lane

Lane 8 · 2026-08-03

## Why this lane matters
Reason.

## Newton-root conventions
Definitions.

## Closed mathematics below 125
Results.

## Live problem
Problem.

## Ready task L8-T1 — begin
Task.

## Exact sources
Sources.

---
[Portfolio](../README.md) · successor v7c candidate · immutable v7 preserved
"""
        public = handoffs._public_lane_source(
            source,
            sequence=8,
            slug="synthetic-lane",
            packet_anchors={},
        )
        self.assertIn("(lane-8-reconstruction-input.md)", public)

    def test_v7c_manifest_and_sources_are_verified(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            handoff_dir = root / "registry" / "research-handoff-v7c"
            lanes_dir = handoff_dir / "lanes"
            lanes_dir.mkdir(parents=True)
            portfolio = handoff_dir / "README.md"
            portfolio.write_text("# Portfolio\n", encoding="utf-8")
            records = [_manifest_record(root, portfolio)]
            roadmap = handoff_dir / "TASK_ROADMAP.md"
            roadmap.write_text("# Current research-task roadmap\n", encoding="utf-8")
            records.append(_manifest_record(root, roadmap))
            for _, slug in handoffs.LANES:
                lane = lanes_dir / f"{slug}.md"
                lane.write_text(f"# {slug}\n", encoding="utf-8")
                records.append(_manifest_record(root, lane))
            manifest_path = handoff_dir / "manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "handoff_version": "7c",
                        "lane_count": 9,
                        "lanes": [
                            {"lane": sequence, "slug": slug}
                            for sequence, slug in handoffs.LANES
                        ],
                        "files": records,
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            sources, manifest_sha, version = handoffs._verified_handoff_sources(
                lane_source_dir=handoff_dir,
                lane_manifest_path=manifest_path,
            )

        self.assertEqual(version, "7c")
        self.assertEqual(len(sources), 11)
        self.assertRegex(manifest_sha, r"^[0-9a-f]{64}$")

    def test_v7c_portfolio_keeps_math_and_removes_candidate_footer(self) -> None:
        source = """# Nine research directions around the Jacobian conjecture

Research portfolio · 2026-08-03

Mathematical introduction.

[Lane](lanes/example.md)

---
Successor handoff v7c · release and source navigation are supplied by the published footer
"""
        public = handoffs._public_portfolio(source)
        self.assertIn("Updated 3 August 2026", public)
        self.assertIn("[Lane](example.md)", public)
        self.assertNotIn("Successor handoff", public)
        self.assertIn("[Release metadata](release.json)", public)

    def test_portfolio_rewrites_checkout_relative_baseline_verifier(self) -> None:
        source = """# Nine research directions around the Jacobian conjecture

Research portfolio · 2026-08-04

[public verifier](../../research-notes/lane5-degree-budgets/verify_baseline_counterexample.py)

---
Successor handoff v7n · release and source navigation are supplied by the published footer
"""
        public = handoffs._public_portfolio(source)
        self.assertIn(
            "[public verifier](lane-5-source-packet.md#source-9ec82063f46b1a95)",
            public,
        )
        self.assertNotIn("../../research-notes", public)

    def test_task_roadmap_rewrites_lane_and_portfolio_routes(self) -> None:
        source = """# Current research-task roadmap

## Lane 1

[Open the full lane](lanes/cubic-flatness-normalization-defects.md)

---
[Back to the portfolio](README.md)
"""
        public = handoffs._public_task_roadmap(source).decode("utf-8")
        self.assertIn(
            "(../handoffs/cubic-flatness-normalization-defects.md)", public
        )
        self.assertIn(
            "(../handoffs/state-of-the-program.md)", public
        )
        self.assertIn("[Release metadata](../handoffs/release.json)", public)


if __name__ == "__main__":
    unittest.main()
