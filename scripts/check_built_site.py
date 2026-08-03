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
    load_manuscript_sources,
    load_retained_math,
    load_retained_math_v2,
    retained_corrections,
    retained_v2_compatibility,
    retained_v2_graph,
    retained_v2_is_full,
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
        if 'class="handoff-snapshot"' in text or SITE_STATE["release_id"] in text:
            failures.append(f"model handoff exposes release plumbing: /{route}")
        if text.find("<h1") < 0 or text.find('class="claim-tag"') < text.find("<h1"):
            failures.append(f"model handoff does not lead with its title: /{route}")
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
        if brief.get("kind") == "program" and (
            "Current mathematical corpus" not in text
            or "working-mathematics/programs" not in text
        ):
            failures.append(
                f"program handoff lacks its generated graph view: /{route}"
            )
        if "Sources and release" not in text or "Current proof sources" not in text:
            failures.append(f"model handoff lacks current text proofs: /{route}")
        if "Machine-readable release metadata" not in text:
            failures.append(f"model handoff lacks release metadata footer: /{route}")

    for item in brief_manifest.get("task_inputs", []):
        route = item["route"].removesuffix(".md")
        path = site / route / "index.html"
        if not path.is_file():
            failures.append(f"missing model task-input route: /{route}")
            continue
        text = path.read_text(encoding="utf-8")
        markers_by_id = {
            "LANE7-COLLISION-CHART-V1": (
                "Lane 7 exact collision-chart input",
                "15 primitive integer quintics",
                "Complete Macaulay2 input",
                "Exact evidence boundary",
            ),
            "LANE8-RAW-SUPPORT-RECONSTRUCTION-V1": (
                "Lane 8 exact raw-support reconstruction input",
                "Mathematical contract",
                "Exact quintic-field relations",
                "Exact quintic-field helper",
                "quintic_field_fast.py",
                "Complete reconstruction program",
            ),
        }
        for marker in markers_by_id.get(item.get("input_id"), ()):
            if marker not in text:
                failures.append(f"model task-input lacks {marker!r}: /{route}")

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
    retained_v2 = load_retained_math_v2(ROOT)
    selection_path = site / "research/handoffs/retained-math-v2-pilot.json"
    if retained_v2 is None:
        failures.append("selected release does not pin retained-math v2")
    elif retained_v2_is_full(retained_v2[1]):
        graph_path = site / "research/working-mathematics/graph.json"
        compatibility_path = (
            site
            / "research/working-mathematics/legacy-compatibility.json"
        )
        for path, expected_payload, label in (
            (
                graph_path,
                retained_v2_graph(retained_v2[1]),
                "retained-math v2 graph",
            ),
            (
                compatibility_path,
                retained_v2_compatibility(retained_v2[1]),
                "legacy compatibility map",
            ),
        ):
            if not path.is_file():
                failures.append(f"built {label} is missing")
                continue
            try:
                found_payload = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                failures.append(f"built {label} is invalid JSON")
            else:
                if found_payload != expected_payload:
                    failures.append(f"built {label} disagrees")
        if selection_path.exists():
            failures.append(
                "full retained-math v2 release still serves the obsolete pilot"
            )
    elif not selection_path.is_file():
        failures.append("built retained-math v2 selection is missing")
    else:
        try:
            found_selection = json.loads(selection_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            failures.append("built retained-math v2 selection is invalid JSON")
        else:
            if found_selection != retained_v2[1]:
                failures.append("built retained-math v2 selection disagrees")

    if retained_v2 is not None and not retained_v2_is_full(retained_v2[1]):
        lane_six = (
            site
            / "research/handoffs/homogeneous-realization-compression/index.html"
        )
        lane_six_text = (
            lane_six.read_text(encoding="utf-8") if lane_six.is_file() else ""
        )
        for marker in (
            "Compiler-owned retained result",
            "ARG-RMU5D8E0003-FINITE-PLANE",
            "g(r)=(r-4)(r^2-8r+64)",
            "-1152",
        ):
            if marker not in lane_six_text:
                failures.append(f"built Lane 6 v2 block lacks {marker!r}")

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
    if retained_v2 is not None and retained_v2_is_full(retained_v2[1]):
        compatibility = retained_v2_compatibility(retained_v2[1])
        assert compatibility is not None
        for route in compatibility["routes"]:
            disposition = route["disposition"]
            if disposition not in {
                "replacement",
                "split_replacement",
                "valid_weaker",
            }:
                continue
            tag = route["legacy_unit_id"]
            page = site / "claims" / tag / "index.html"
            text = page.read_text(encoding="utf-8") if page.is_file() else ""
            expected_notice = (
                "A stronger current result is available"
                if disposition == "valid_weaker"
                else "Use the current replacement mathematics"
            )
            if expected_notice not in text:
                failures.append(
                    f"built forward-linked claim lacks its notice: {tag}"
                )
            for target in route["targets"]:
                if target["role"] in {"replacement", "stronger_result"} and (
                    target["unit_id"] not in text
                ):
                    failures.append(
                        f"built forward-linked claim does not link "
                        f"{target['unit_id']}: {tag}"
                    )
    else:
        retained_value = load_retained_math(ROOT)
        if retained_value is not None:
            for tag, correction in retained_corrections(retained_value).items():
                page = site / "claims" / tag / "index.html"
                text = page.read_text(encoding="utf-8") if page.is_file() else ""
                expected_notice = (
                    "Replaced by current working mathematics"
                    if correction["_forward_relation"] in {"corrects", "supersedes"}
                    else "A stronger current result is available"
                )
                if expected_notice not in text:
                    failures.append(
                        f"built forward-linked claim lacks its notice: {tag}"
                    )
                if correction["unit_id"] not in text:
                    failures.append(
                        f"built corrected claim does not link "
                        f"{correction['unit_id']}: {tag}"
                    )
    if len(program_pages) != expected["research_programs"]:
        failures.append(
            "built program routes: expected "
            f"{expected['research_programs']}, found {len(program_pages)}"
        )
    handoff_pages = [
        site / brief["route"].removesuffix(".md") / "index.html"
        for brief in brief_manifest["briefs"]
    ]
    missing_handoffs = [path for path in handoff_pages if not path.is_file()]
    for path in missing_handoffs:
        failures.append(f"missing built model handoff: {path.relative_to(site)}")
    retained_unit_pages = list(
        (site / "research/working-mathematics/units").glob("*/index.html")
    )
    retained_program_pages = list(
        (site / "research/working-mathematics/programs").glob("*/index.html")
    )
    expected_retained_units = SITE_STATE["retained_math"]["expected_units"]
    expected_retained_programs = SITE_STATE["retained_math"]["expected_programs"]
    if retained_v2 is not None and retained_v2_is_full(retained_v2[1]):
        full_graph = retained_v2_graph(retained_v2[1])
        expected_retained_units = full_graph["counts"]["units"]
        expected_retained_programs = full_graph["counts"]["programs"]
    if len(retained_unit_pages) != expected_retained_units:
        failures.append(
            "built retained-unit routes: expected "
            f"{expected_retained_units}, found "
            f"{len(retained_unit_pages)}"
        )
    if len(retained_program_pages) != expected_retained_programs:
        failures.append(
            "built retained-program routes: expected "
            f"{expected_retained_programs}, found "
            f"{len(retained_program_pages)}"
        )
    source_manifest = load_manuscript_sources(ROOT)
    if source_manifest is None:
        failures.append("selected release does not pin manuscript sources")
    else:
        proof_pages = list(
            (site / "research/proof-sources").rglob("index.html")
        )
        expected_proof_pages = SITE_STATE["manuscript_sources"]["expected_files"] + 1
        if len(proof_pages) != expected_proof_pages:
            failures.append(
                "built text-proof routes: expected "
                f"{expected_proof_pages}, found {len(proof_pages)}"
            )
        label_anchors = 0
        for path in proof_pages:
            text = path.read_text(encoding="utf-8")
            label_anchors += len(re.findall(r'id="label-[^"]+"', text))
        if label_anchors != SITE_STATE["manuscript_sources"]["expected_labels"]:
            failures.append(
                "built text-proof label anchors: expected "
                f"{SITE_STATE['manuscript_sources']['expected_labels']}, "
                f"found {label_anchors}"
            )
    for path in handoff_pages:
        text = path.read_text(encoding="utf-8")
        if '<p>title: "Model research brief' in text:
            failures.append(f"handoff renders YAML metadata as prose: {path.name}")
        if "Retained working mathematics" not in text:
            failures.append(f"handoff lacks retained-math link: {path.name}")
        if "Current proof sources" not in text:
            failures.append(f"handoff lacks text-proof link: {path.name}")

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
        if "research/proof-sources/" not in search_text:
            failures.append("text proof sources are missing from internal search")

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
