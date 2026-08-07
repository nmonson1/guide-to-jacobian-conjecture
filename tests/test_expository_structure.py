from __future__ import annotations

import json
import re
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NAVIGATION = json.loads(
    (ROOT / "editorial" / "navigation.json").read_text(encoding="utf-8")
)
REVIEWS = json.loads(
    (ROOT / "editorial" / "reviews.json").read_text(encoding="utf-8")
)["pages"]
NAV_PAGES = {
    page["path"]: page
    for section in NAVIGATION["sections"]
    for page in section["pages"]
}
NAV_PAGES[NAVIGATION["review_page"]["path"]] = NAVIGATION["review_page"]


class ExpositoryStructureTests(unittest.TestCase):
    def test_new_pages_begin_unread_and_are_placed(self) -> None:
        for path in {
            "background/background-reading.md",
            "start/three-views.md",
            "results/evidence-ledger.md",
        }:
            self.assertIn(path, NAV_PAGES)
            self.assertIn(path, REVIEWS)
            self.assertEqual(REVIEWS[path]["status"], "unread")

    def test_review_ledger_matches_navigation_inventory(self) -> None:
        self.assertEqual(set(REVIEWS), set(NAV_PAGES))
        self.assertTrue(
            all(record["status"] == "unread" for record in REVIEWS.values())
        )

    def test_result_pages_use_specific_headings(self) -> None:
        banned = {
            "What is true and why",
            "Precise result",
            "Discussion",
            "What it does not prove",
            "Proof source and status",
        }
        for path in sorted((DOCS / "results").glob("*.md")):
            if path.name == "evidence-ledger.md":
                continue
            text = path.read_text(encoding="utf-8")
            headings = set(
                re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
            )
            self.assertFalse(
                headings & banned,
                f"{path.relative_to(ROOT)} uses generic headings: "
                f"{headings & banned}",
            )

    def test_major_result_pages_link_to_evidence_ledger(self) -> None:
        pages = [
            "every-generic-degree.md",
            "cubic-homogeneous.md",
            "characteristic-two.md",
            "below-125.md",
            "stable-cubic-frames.md",
            "two-block-uniqueness.md",
            "degree-21-dessins.md",
            "length-584.md",
        ]
        for name in pages:
            text = (DOCS / "results" / name).read_text(encoding="utf-8")
            self.assertIn("evidence-ledger.md", text, name)
            self.assertIn(".evidence-link", text, name)

    def test_referenced_diagrams_exist_and_have_accessible_text(self) -> None:
        references = 0
        files: set[Path] = set()
        pattern = re.compile(
            r'<img\s+src="([^"]+\.svg)"\s+alt="([^"]+)"'
        )
        for path in DOCS.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for src, alt in pattern.findall(text):
                references += 1
                target = (path.parent / src).resolve()
                files.add(target)
                self.assertTrue(target.exists(), f"missing diagram {src} in {path}")
                self.assertGreater(len(alt.strip()), 20, f"weak alt text in {path}")
        for target in files:
            root = ElementTree.parse(target).getroot()
            ns = {"svg": "http://www.w3.org/2000/svg"}
            self.assertIsNotNone(root.find("svg:title", ns), target)
            self.assertIsNotNone(root.find("svg:desc", ns), target)
        self.assertGreaterEqual(references, 10)
        self.assertGreaterEqual(len(files), 7)

    def test_exposition_stylesheet_is_loaded(self) -> None:
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertIn("assets/stylesheets/exposition.css", config)

    def test_start_path_contains_the_expository_spine(self) -> None:
        start = [page["path"] for page in NAVIGATION["sections"][0]["pages"]]
        self.assertLess(
            start.index("start/conjecture.md"),
            start.index("start/counterexample.md"),
        )
        self.assertLess(
            start.index("start/counterexample.md"),
            start.index("start/three-views.md"),
        )
        self.assertLess(
            start.index("start/three-views.md"),
            start.index("background/marked-root-geometry.md"),
        )

    def test_research_pages_pose_a_concrete_problem(self) -> None:
        phrases = {
            "cover-and-collision.md": "A specimen problem",
            "boundary-and-globalization.md": "The escape mechanism",
            "deformation-and-transport.md": "A specimen tangent question",
            "framing-and-degree.md": "Six notions of size",
        }
        for name, phrase in phrases.items():
            text = (DOCS / "fronts" / name).read_text(encoding="utf-8")
            self.assertIn(phrase, text, name)

    def test_audited_prose_has_no_tabs_or_generic_metadiscourse(self) -> None:
        metadiscourse = re.compile(
            r"\b(?:this page|this front|this result|the concrete target|"
            r"the grouping)\b",
            re.IGNORECASE,
        )
        excluded = {
            "start/tao-digestion.md",
            "developments/index.md",
            "results/evidence-ledger.md",
        }
        for path in sorted(DOCS.rglob("*.md")):
            source = path.relative_to(DOCS).as_posix()
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("\t", text, source)
            if source not in excluded:
                self.assertIsNone(metadiscourse.search(text), source)


if __name__ == "__main__":
    unittest.main()
