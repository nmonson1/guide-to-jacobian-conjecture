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
    MODEL_BRIEFS_DATA_DIR,
    PUBLIC_DOCS_DIR,
    SITE_STATE,
    TECHNICAL_MATERIALS_DATA_DIR,
    build_release_metadata,
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

    brief_manifest = json.loads(
        (ROOT / "data" / MODEL_BRIEFS_DATA_DIR / "manifest.json").read_text(
            encoding="utf-8"
        )
    )
    manuscript_manifest = json.loads(
        (ROOT / "data" / MANUSCRIPTS_DATA_DIR / "manifest.json").read_text(
            encoding="utf-8"
        )
    )
    active_manuscripts = {
        item["filename"] for item in manuscript_manifest["manuscripts"]
    }
    for brief in brief_manifest["briefs"]:
        route = brief["route"].removesuffix(".md")
        path = site / route / "index.html"
        if not path.is_file():
            failures.append(f"missing model handoff route: /{route}")
            continue
        text = path.read_text(encoding="utf-8")
        if 'class="handoff-snapshot"' not in text:
            failures.append(f"model handoff lacks canonical snapshot: /{route}")
        if SITE_STATE["release_id"] not in text:
            failures.append(f"model handoff names the wrong release: /{route}")
        parser_links = Links()
        parser_links.feed(text)
        linked_manuscripts = {
            Path(urlparse(target).path).name
            for target in parser_links.targets
            if "assets/manuscripts/" in urlparse(target).path
        }
        inactive = linked_manuscripts - active_manuscripts
        if inactive:
            failures.append(
                f"model handoff links inactive manuscript(s): /{route}: "
                f"{', '.join(sorted(inactive))}"
            )
        if brief.get("kind") == "program" and not linked_manuscripts:
            failures.append(f"model handoff lacks an active manuscript: /{route}")

    release_path = site / "research/handoffs/release.json"
    if not release_path.is_file():
        failures.append("built machine-readable handoff release is missing")
    else:
        try:
            found_release = json.loads(release_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            failures.append("built machine-readable handoff release is invalid JSON")
        else:
            if found_release != build_release_metadata(ROOT):
                failures.append(
                    "built machine-readable handoff release disagrees with site state"
                )

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
    retained_unit_pages = list(
        (site / "research/working-mathematics/units").glob("*/index.html")
    )
    retained_program_pages = list(
        (site / "research/working-mathematics/programs").glob("*/index.html")
    )
    if len(retained_unit_pages) != SITE_STATE["retained_math"]["expected_units"]:
        failures.append(
            "built retained-unit routes: expected "
            f"{SITE_STATE['retained_math']['expected_units']}, found "
            f"{len(retained_unit_pages)}"
        )
    if (
        len(retained_program_pages)
        != SITE_STATE["retained_math"]["expected_programs"]
    ):
        failures.append(
            "built retained-program routes: expected "
            f"{SITE_STATE['retained_math']['expected_programs']}, found "
            f"{len(retained_program_pages)}"
        )
    for path in handoff_pages:
        text = path.read_text(encoding="utf-8")
        if '<p>title: "Model research brief' in text:
            failures.append(f"handoff renders YAML metadata as prose: {path.name}")
        if "Retained working graph" not in text:
            failures.append(f"handoff lacks retained graph link: {path.name}")

    search_path = site / "search/search_index.json"
    if not search_path.is_file():
        failures.append("search index is missing")
    else:
        search_text = search_path.read_text(encoding="utf-8")
        if not re.search(r'"location"\s*:\s*"claims/JCG-', search_text):
            failures.append("stable-tag claim pages are missing from internal search")
        for brief in brief_manifest["briefs"]:
            route = brief["route"].removesuffix(".md") + "/"
            if route not in search_text:
                failures.append(f"model handoff is missing from internal search: {route}")
        if "research/working-mathematics/units/" not in search_text:
            failures.append("retained working units are missing from internal search")

    robots = site / "robots.txt"
    if not robots.is_file() or "Disallow: /" not in robots.read_text(encoding="utf-8"):
        failures.append("built robots.txt does not disallow crawling")

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
