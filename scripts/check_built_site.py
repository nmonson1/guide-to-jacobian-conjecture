#!/usr/bin/env python3
"""Validate noindex, routes, search hiding, PDFs, and internal links after build."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

from generate_living_guide_v2 import (
    MANUSCRIPTS_DATA_DIR,
    PUBLIC_DOCS_DIR,
    SITE_STATE,
    TECHNICAL_MATERIALS_DATA_DIR,
)


ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag not in {"a", "link", "script", "img"}:
            return
        wanted = "href" if tag in {"a", "link"} else "src"
        for key, value in attrs:
            if key == wanted and value:
                self.targets.append(value)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _resolve(site: Path, html_path: Path, target: str) -> Path | None:
    parsed = urlparse(target)
    if parsed.scheme or parsed.netloc or target.startswith(("#", "mailto:", "data:")):
        return None
    clean = unquote(parsed.path)
    if not clean:
        return html_path
    if clean.startswith("/guide-to-jacobian-conjecture/"):
        clean = clean.removeprefix("/guide-to-jacobian-conjecture/")
        candidate = site / clean
    elif clean.startswith("/"):
        return None
    else:
        candidate = html_path.parent / clean
    if clean.endswith("/"):
        candidate /= "index.html"
    return candidate.resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    args = parser.parse_args()
    site = args.site.resolve()
    failures: list[str] = []
    html_files = sorted(site.rglob("*.html"))
    if not html_files:
        parser.error(f"no HTML files found under {site}")

    for path in html_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(site)
        if '<meta name="robots" content="noindex, nofollow">' not in text:
            failures.append(f"{relative}: missing global noindex")
        parser_links = Links()
        parser_links.feed(text)
        for target in parser_links.targets:
            resolved = _resolve(site, path, target)
            if resolved is not None and not resolved.exists():
                failures.append(f"{relative}: broken internal asset/link {target!r}")

    for route in (
        "",
        "counterexample",
        "geometry",
        "plane-case",
        "research",
        "research/papers",
        "research/handoffs/minimum-degree-and-quartic-exclusions",
        "results",
        "results/all-claims",
        "results/open-problems",
        "results/corrections",
        "evidence",
        "evidence/materials",
        "about",
    ):
        path = site / route / "index.html" if route else site / "index.html"
        if not path.is_file():
            failures.append(f"missing main route: /{route}")

    result_pages = list((site / "collections").glob("*/index.html"))
    claim_pages = list((site / "claims").glob("*/index.html"))
    program_pages = list((site / "research/programs").glob("*/index.html"))
    expected = SITE_STATE["expected_counts"]
    if len(result_pages) != expected["grouped_pages"]:
        failures.append(
            "built result routes: expected "
            f"{expected['grouped_pages']}, found {len(result_pages)}"
        )
    if len(claim_pages) != expected["technical_records"]:
        failures.append(
            "built claim routes: expected "
            f"{expected['technical_records']}, found {len(claim_pages)}"
        )
    if len(program_pages) != expected["research_programs"]:
        failures.append(
            "built program routes: expected "
            f"{expected['research_programs']}, found {len(program_pages)}"
        )
    handoff_pages = list((site / "research/handoffs").glob("*/index.html"))
    if len(handoff_pages) != SITE_STATE["model_briefs"]["expected_count"]:
        failures.append(
            "built model handoff routes: expected "
            f"{SITE_STATE['model_briefs']['expected_count']}, found "
            f"{len(handoff_pages)}"
        )

    search_path = site / "search/search_index.json"
    if not search_path.is_file():
        failures.append("search index is missing")
    else:
        search_text = search_path.read_text(encoding="utf-8")
        if not re.search(r'"location"\s*:\s*"claims/JCG-', search_text):
            failures.append("stable-tag claim pages are missing from internal search")
        if "research/handoffs/minimum-degree-and-quartic-exclusions/" not in search_text:
            failures.append("model handoff is missing from internal search")

    robots = site / "robots.txt"
    if not robots.is_file() or "Disallow: /" not in robots.read_text(encoding="utf-8"):
        failures.append("built robots.txt does not disallow crawling")

    manuscript_manifest = json.loads(
        (ROOT / "data" / MANUSCRIPTS_DATA_DIR / "manifest.json").read_text(
            encoding="utf-8"
        )
    )
    for item in manuscript_manifest["manuscripts"]:
        path = site / "assets/manuscripts" / item["filename"]
        if not path.is_file() or _sha256(path) != item["sha256"]:
            failures.append(f"built manuscript mismatch: {item['filename']}")

    materials_manifest = json.loads(
        (
            ROOT
            / "data"
            / TECHNICAL_MATERIALS_DATA_DIR
            / "manifest.json"
        ).read_text(encoding="utf-8")
    )
    for program in materials_manifest["programs"]:
        for item in program["artifacts"]:
            path = site / "assets/technical-materials" / item["filename"]
            if not path.is_file() or _sha256(path) != item["sha256"]:
                failures.append(f"built technical material mismatch: {item['filename']}")

    source_docs = ROOT / PUBLIC_DOCS_DIR
    if not source_docs.is_dir():
        failures.append(f"configured source tree is missing: {source_docs}")

    if failures:
        print("Built-site checks failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(
        f"Built-site checks passed for {len(html_files)} HTML pages, "
        f"{len(result_pages)} result routes, and {len(claim_pages)} "
        f"stable-tag claim routes, with {materials_manifest['artifact_count']} "
        "technical artifacts."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
