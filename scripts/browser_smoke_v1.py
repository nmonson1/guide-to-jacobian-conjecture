#!/usr/bin/env python3
"""Browser-level smoke, responsive, theme, math, and accessibility checks."""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import threading
from pathlib import Path

from playwright.sync_api import Page, sync_playwright


V7C_LANE_SEMANTIC_GROUPS = (
    ("purpose", ("Scope", "Why this lane matters")),
    (
        "setup",
        (
            "Setup and definitions",
            "Setup and notation",
            "Newton-root conventions",
            "Fixed ",
        ),
    ),
    (
        "reusable mathematics",
        (
            "Results to use",
            "Reusable mathematics",
            "Closed mathematics below 125",
        ),
    ),
    ("live problem", ("Live problem",)),
    ("ready task", ("Tasks", "Ready task ", "Interface-ready task ")),
    (
        "scope boundary",
        (
            "Limits",
            "Non-ready follow-up",
            "Optional exact-CAS route",
            "Non-ready ",
        ),
    ),
    ("sources", ("Direct sources", "Exact sources")),
)
V7C_PROGRAM_SEMANTIC_GROUPS = (
    ("mathematical corpus", ("Current mathematical corpus",)),
    ("research entrypoints", ("Current research entrypoints",)),
    ("strategy", ("Strategy and connections",)),
)
V7C_PORTFOLIO_SEMANTIC_GROUPS = (
    ("lane entrypoints", ("Choose a lane", "Lane entrypoints")),
    ("connections", ("Connections worth testing",)),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def contrast(page: Page, selector: str) -> float:
    return page.locator(selector).first.evaluate(
        """element => {
          const parse = value => {
            const parts = value.match(/[\\d.]+/g).map(Number);
            return parts.slice(0, 3);
          };
          const luminance = rgb => {
            const values = rgb.map(v => {
              v /= 255;
              return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
            });
            return 0.2126 * values[0] + 0.7152 * values[1] + 0.0722 * values[2];
          };
          const style = getComputedStyle(element);
          let background = style.backgroundColor;
          let current = element;
          while (parse(background).length < 3 || background.endsWith(', 0)')) {
            current = current.parentElement;
            if (!current) break;
            background = getComputedStyle(current).backgroundColor;
          }
          const a = luminance(parse(style.color));
          const b = luminance(parse(background));
          return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
        }"""
    )


def check_page(page: Page, url: str, mobile: bool = False) -> None:
    response = page.goto(url, wait_until="networkidle")
    require(response is not None and response.ok, f"failed to load {url}")
    require(page.locator('meta[name="robots"][content="noindex, nofollow"]').count() == 1,
            f"noindex missing on {url}")
    require(page.locator("main").count() == 1, f"main landmark missing on {url}")
    require(page.locator("nav").count() >= 1, f"navigation landmark missing on {url}")
    require(page.locator("main h1").count() == 1, f"expected one main h1 on {url}")
    levels = page.locator("main h1, main h2, main h3").evaluate_all(
        "els => els.map(el => Number(el.tagName.slice(1)))"
    )
    for previous, current in zip(levels, levels[1:]):
        require(current <= previous + 1, f"heading level skipped on {url}")
    empty_links = page.locator("a[href]").evaluate_all(
        """links => links
          .filter(a => !a.id.startsWith('__codelineno-'))
          .filter(a => !(a.innerText.trim() || a.getAttribute('aria-label')
            || a.getAttribute('title')))
          .map(a => a.getAttribute('href'))"""
    )
    require(not empty_links, f"unlabelled links on {url}: {empty_links[:4]}")
    overflow = page.evaluate(
        "document.documentElement.scrollWidth - window.innerWidth"
    )
    require(overflow <= 2, f"horizontal overflow ({overflow}px) on {url}")
    if mobile:
        toggle = page.locator('label.md-header__button[for="__drawer"]')
        require(toggle.count() == 1, "mobile navigation toggle missing")
        toggle.click()
        require(page.locator("#__drawer").is_checked(), "mobile navigation did not open")


def run(
    site: Path, executable: str | None, screenshots: Path | None
) -> None:
    root = Path(__file__).resolve().parents[1]
    state = json.loads((root / "site-state.json").read_text(encoding="utf-8"))
    manuscript_manifest = json.loads(
        (
            root
            / "data"
            / state["manuscripts"]["data_dir"]
            / "manifest.json"
        ).read_text(encoding="utf-8")
    )
    first_manuscript = manuscript_manifest["manuscripts"][0]["filename"]
    active_manuscripts = {
        item["filename"] for item in manuscript_manifest["manuscripts"]
    }
    materials_manifest = json.loads(
        (
            root
            / "data"
            / state["technical_materials"]["data_dir"]
            / "manifest.json"
        ).read_text(encoding="utf-8")
    )
    model_brief_manifest = json.loads(
        (
            root
            / "data"
            / state["model_briefs"]["data_dir"]
            / "manifest.json"
        ).read_text(encoding="utf-8")
    )
    is_v7_handoff = (
        model_brief_manifest.get("schema_version") == 7
        and model_brief_manifest.get("source_handoff", {}).get(
            "handoff_version"
        )
        in {"7c", "7d", "7e", "7f", "7g", "7h", "7i", "7j"}
    )
    retained_v2_manifest = None
    if state.get("retained_math_v2") is not None:
        retained_v2_manifest = json.loads(
            (
                root
                / "data"
                / state["retained_math_v2"]["data_dir"]
                / "manifest.json"
            ).read_text(encoding="utf-8")
        )
    full_retained_v2 = (
        retained_v2_manifest is not None
        and retained_v2_manifest.get("kind") == "retained-math-v2-full-public"
    )
    first_material = materials_manifest["programs"][0]["artifacts"][0]["filename"]
    handler = functools.partial(
        QuietHandler,
        directory=str(site),
    )
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}/"
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path=executable,
                headless=True,
            )
            desktop = browser.new_page(viewport={"width": 1440, "height": 1000})
            for route in (
                "",
                "counterexample/",
                "geometry/",
                "plane-case/",
                "research/",
                "research/papers/",
                "results/",
                "results/all-claims/",
                "evidence/",
                "evidence/materials/",
                "about/",
                "collections/base-counterexample-and-immediate-consequences/",
                "research/programs/cubic-marked-root-incidence-geometry/",
                "claims/JCG-E4FA4CBB/",
            ):
                check_page(desktop, base + route)

            for brief in model_brief_manifest["briefs"]:
                route = brief["route"].removesuffix(".md") + "/"
                check_page(desktop, base + route)
            for item in model_brief_manifest.get("task_inputs", []):
                route = item["route"].removesuffix(".md") + "/"
                check_page(desktop, base + route)

            desktop.goto(base + "counterexample/", wait_until="networkidle")
            desktop.wait_for_selector("mjx-container", timeout=15_000)
            require(
                desktop.locator("mjx-container").count() >= 3,
                "MathJax did not render the counterexample",
            )
            require(
                desktop.locator(
                    'a[href$="01-cubic-marked-root-covers-2026-07-22-v3.pdf"]'
                ).count()
                == 0,
                "superseded manuscript surfaced on the counterexample page",
            )
            pdf = desktop.context.request.get(
                base
                + "assets/manuscripts/"
                + first_manuscript
            )
            require(pdf.ok, "versioned PDF is not downloadable")
            release_response = desktop.context.request.get(
                base + "research/handoffs/release.json"
            )
            require(
                release_response.ok,
                "machine-readable handoff release is not downloadable",
            )
            require(
                release_response.json()["site_release_id"] == state["release_id"],
                "machine-readable handoff release names the wrong site release",
            )
            release_payload = release_response.json()
            if full_retained_v2:
                assert retained_v2_manifest is not None
                retained_release = release_payload.get("retained_math_v2", {})
                machine_routes = retained_release.get("machine_routes", {})
                require(
                    set(machine_routes)
                    == {"graph", "legacy_compatibility"},
                    "full retained-math v2 machine routes are incomplete",
                )
                graph_response = desktop.context.request.get(
                    base + machine_routes.get("graph", "")
                )
                require(
                    graph_response.ok,
                    "full retained-math v2 graph is not downloadable",
                )
                graph_payload = graph_response.json()
                require(
                    graph_payload.get("registry_id")
                    == retained_v2_manifest["source_registry_id"],
                    "downloaded retained-math v2 graph names the wrong registry",
                )
                require(
                    graph_payload.get("counts")
                    == retained_v2_manifest["graph_counts"],
                    "downloaded retained-math v2 graph has the wrong counts",
                )
                compatibility_response = desktop.context.request.get(
                    base + machine_routes.get("legacy_compatibility", "")
                )
                require(
                    compatibility_response.ok,
                    "retained-math v2 compatibility map is not downloadable",
                )
                compatibility_payload = compatibility_response.json()
                require(
                    compatibility_payload.get("map_id")
                    == retained_v2_manifest["compatibility_map_id"],
                    "downloaded compatibility map has the wrong identity",
                )
                require(
                    compatibility_payload.get("counts")
                    == retained_v2_manifest["compatibility_counts"],
                    "downloaded compatibility map has the wrong counts",
                )
                require(
                    len(compatibility_payload.get("routes", []))
                    == retained_v2_manifest["compatibility_counts"]["routes"],
                    "downloaded compatibility map is not total",
                )
            else:
                v2_response = desktop.context.request.get(
                    base + "research/handoffs/retained-math-v2-pilot.json"
                )
                require(
                    v2_response.ok,
                    "machine-readable retained-math v2 selection is not downloadable",
                )
                require(
                    v2_response.json()["selected_ids"]["arguments"]
                    == ["ARG-RMU5D8E0003-FINITE-PLANE"],
                    "retained-math v2 selection names the wrong pilot argument",
                )
            source_response = desktop.context.request.get(
                base + "research/proof-sources/"
            )
            require(source_response.ok, "text-proof source index is not readable")
            exact_source = desktop.context.request.get(
                base
                + "research/proof-sources/01-cubic-incidence/appendices/"
                + "cubic-resolvent-defects/"
            )
            require(exact_source.ok, "corrected Program 1 source is not readable")
            require(
                'id="label-prop-cubic-divisorial-trichotomy"'
                in exact_source.text(),
                "corrected Program 1 source anchor is missing",
            )
            material = desktop.context.request.get(
                base + "assets/technical-materials/" + first_material
            )
            require(material.ok, "technical-material archive is not downloadable")

            for brief in model_brief_manifest["briefs"]:
                kind = brief.get("kind")
                route = brief["route"].removesuffix(".md") + "/"
                desktop.goto(base + route, wait_until="networkidle")
                require(
                    desktop.locator(".handoff-snapshot").count() == 0,
                    f"model handoff exposes the retired snapshot: {route}",
                )
                require(
                    desktop.locator(
                        'main a[href$="release.json"]:has-text("Machine-readable release metadata")'
                    ).count()
                    == 1,
                    f"model handoff lacks release metadata link: {route}",
                )
                linked_manuscripts = set(
                    desktop.locator(
                        'a[href*="assets/manuscripts/"]'
                    ).evaluate_all(
                        """links => links.map(link =>
                          new URL(link.href).pathname.split('/').pop())"""
                    )
                )
                require(
                    linked_manuscripts <= active_manuscripts,
                    f"model handoff links inactive manuscripts: {route}: "
                    f"{sorted(linked_manuscripts - active_manuscripts)}",
                )
                if kind == "lane":
                    if is_v7_handoff:
                        heading_texts = [
                            text.casefold()
                            for text in desktop.locator("main h2").all_inner_texts()
                        ]
                        for name, alternatives in V7C_LANE_SEMANTIC_GROUPS:
                            require(
                                any(
                                    alternative.casefold() in heading
                                    for heading in heading_texts
                                    for alternative in alternatives
                                ),
                                f"lane handoff lacks v7c semantic group "
                                f"{name}: {route}",
                            )
                    else:
                        require(
                            desktop.locator(
                                'main h2:has-text("Reusable mathematics")'
                            ).count()
                            == 1,
                            f"lane handoff lacks reusable mathematics: {route}",
                        )
                        require(
                            desktop.locator(
                                'main h2:has-text("Tasks and deliverables")'
                            ).count()
                            == 1,
                            f"lane handoff lacks its deliverable boundary: {route}",
                        )
                    deeper_routes = desktop.locator("main a[href]").evaluate_all(
                        """links => links.filter(link =>
                          new URL(link.href).pathname.includes(
                            '/research/handoffs/'
                          )).length"""
                    )
                    require(
                        deeper_routes >= 1,
                        f"lane handoff lacks a deeper program route: {route}",
                    )
                    if (
                        not is_v7_handoff
                        and brief["program_slug"]
                        == "homogeneous-realization-compression"
                    ):
                        for marker in (
                            "Compiler-owned retained result",
                            "ARG-RMU5D8E0003-FINITE-PLANE",
                            "-1152",
                        ):
                            require(
                                marker in desktop.locator("main").inner_text(),
                                f"Lane 6 v2 block lacks {marker}: {route}",
                            )
                elif is_v7_handoff and kind == "program":
                    heading_texts = [
                        text.casefold()
                        for text in desktop.locator("main h2").all_inner_texts()
                    ]
                    for name, alternatives in V7C_PROGRAM_SEMANTIC_GROUPS:
                        require(
                            any(
                                alternative.casefold() in heading
                                for heading in heading_texts
                                for alternative in alternatives
                            ),
                            f"program handoff lacks v7c semantic group "
                            f"{name}: {route}",
                        )
                elif is_v7_handoff and kind == "cross_program":
                    heading_texts = [
                        text.casefold()
                        for text in desktop.locator("main h2").all_inner_texts()
                    ]
                    for name, alternatives in V7C_PORTFOLIO_SEMANTIC_GROUPS:
                        require(
                            any(
                                alternative.casefold() in heading
                                for heading in heading_texts
                                for alternative in alternatives
                            ),
                            f"portfolio lacks v7c semantic group {name}: {route}",
                        )
                else:
                    require(
                        desktop.locator(
                            'main h2:has-text("The live frontier")'
                        ).count()
                        == 1,
                        f"model handoff lacks its live-frontier section: {route}",
                    )
                    require(
                        desktop.locator('a[href*="claims/JCG-"]').count() >= 1,
                        f"model handoff lacks stable claim links: {route}",
                    )
                require(
                    desktop.locator(
                        'main a:has-text("Retained working mathematics")'
                    ).count()
                    >= 1,
                    f"model handoff lacks retained-math footer link: {route}",
                )
                require(
                    desktop.locator(
                        'main a:has-text("Current proof sources")'
                    ).count()
                    >= 1,
                    f"model handoff lacks text-proof footer link: {route}",
                )
                main_text = desktop.locator("main").inner_text()
                require(
                    'title: "Model research brief' not in main_text,
                    f"model handoff exposes YAML metadata: {route}",
                )
                if kind == "cross_program":
                    if is_v7_handoff:
                        lane_routes = {
                            item["route"].removesuffix(".md") + "/"
                            for item in model_brief_manifest["briefs"]
                            if item.get("kind") == "lane"
                        }
                        linked_routes = set(
                            desktop.locator("main a[href]").evaluate_all(
                                """links => links.map(link =>
                                  new URL(link.href).pathname.slice(1))"""
                            )
                        )
                        require(
                            lane_routes <= linked_routes,
                            "v7c portfolio lacks one or more lane routes",
                        )
                    else:
                        require(
                            desktop.locator(
                                'a[href*="#3-reusable-inputs-exact-scope-and-proof-access"]'
                            ).count()
                            >= 6,
                            "cross-program handoff lacks all six proof routes",
                        )
                elif kind == "program":
                    if is_v7_handoff:
                        require(
                            desktop.locator(
                                'main a[href*="working-mathematics/programs/"]'
                            ).count()
                            >= 1,
                            f"v7c program overlay lacks its graph view: {route}",
                        )
                    else:
                        require(
                            bool(linked_manuscripts),
                            f"model handoff lacks an active manuscript: {route}",
                        )
                        proof_locators = desktop.locator(
                            'a[href*="/assets/"][href*=".pdf#page="]'
                        ).count() + desktop.locator(
                            'a[href*="proof-sources/"]'
                        ).count()
                        require(
                            proof_locators >= 8,
                            f"model handoff lacks direct proof/source links: {route}",
                        )
                else:
                    require(
                        desktop.locator('a[href*="proof-sources/"]').count() >= 1,
                        f"lane handoff lacks the current text-proof index: {route}",
                    )

            desktop.goto(base, wait_until="networkidle")
            for scheme in ("jacobian-light", "jacobian-dark"):
                desktop.locator("html").evaluate(
                    "(el, scheme) => el.setAttribute('data-md-color-scheme', scheme)",
                    scheme,
                )
                desktop.wait_for_timeout(500)
                require(
                    desktop.locator(".md-header__title").is_visible(),
                    f"header title disappeared in {scheme}",
                )
                require(
                    desktop.locator(".md-tabs").is_visible(),
                    f"desktop navigation disappeared in {scheme}",
                )
                require(contrast(desktop, ".formula-card") >= 4.5,
                        f"formula-card contrast failed in {scheme}")
                require(contrast(desktop, ".md-header__topic") >= 4.5,
                        f"header title contrast failed in {scheme}")
                if desktop.locator(".status-kind").count():
                    require(contrast(desktop, ".status-kind") >= 4.5,
                            f"kind badge contrast failed in {scheme}")
                if desktop.locator(".status-draft").count():
                    require(contrast(desktop, ".status-draft") >= 4.5,
                            f"draft badge contrast failed in {scheme}")
                if screenshots is not None:
                    desktop.screenshot(
                        path=screenshots / f"home-{scheme}.png",
                        full_page=True,
                    )

            desktop.goto(
                base + "collections/base-counterexample-and-immediate-consequences/",
                wait_until="networkidle",
            )
            for scheme in ("jacobian-light", "jacobian-dark"):
                desktop.locator("html").evaluate(
                    "(el, scheme) => el.setAttribute('data-md-color-scheme', scheme)",
                    scheme,
                )
                desktop.wait_for_timeout(500)
                require(contrast(desktop, ".status-kind") >= 4.5,
                        f"kind badge contrast failed in {scheme}")
                require(
                    contrast(desktop, '.status[class*="coverage-"]') >= 4.5,
                    f"proof-access badge contrast failed in {scheme}",
                )

            desktop.goto(base, wait_until="networkidle")
            desktop.emulate_media(reduced_motion="reduce")
            reduced = desktop.locator(".path-card").first.evaluate(
                """el => ({
                  transition: getComputedStyle(el).transitionDuration,
                  scroll: getComputedStyle(document.documentElement).scrollBehavior
                })"""
            )
            require(
                float(reduced["transition"].removesuffix("s")) <= 0.00002,
                f"reduced-motion transition remains {reduced['transition']}",
            )
            require(reduced["scroll"] == "auto", "reduced-motion smooth scroll remains")

            desktop.keyboard.press("Tab")
            focused = desktop.evaluate(
                """() => {
                  const el = document.activeElement;
                  const style = getComputedStyle(el);
                  return {
                    tag: el.tagName,
                    width: parseFloat(style.outlineWidth),
                    text: el.getAttribute('aria-label') || el.innerText || ''
                  };
                }"""
            )
            require(focused["width"] >= 2, f"keyboard focus is not visible: {focused}")

            mobile = browser.new_page(viewport={"width": 390, "height": 844})
            check_page(mobile, base, mobile=True)
            check_page(mobile, base + "counterexample/", mobile=True)
            for brief in model_brief_manifest["briefs"]:
                route = brief["route"].removesuffix(".md") + "/"
                check_page(mobile, base + route, mobile=True)
            if screenshots is not None:
                mobile.goto(base, wait_until="networkidle")
                mobile.screenshot(
                    path=screenshots / "home-mobile.png",
                    full_page=True,
                )
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-dir", required=True, type=Path)
    parser.add_argument("--executable-path")
    parser.add_argument("--screenshots", type=Path)
    args = parser.parse_args()
    site = args.site_dir.resolve()
    if not site.is_dir():
        parser.error(f"site directory does not exist: {site}")
    screenshots = args.screenshots.resolve() if args.screenshots else None
    if screenshots is not None:
        if screenshots.exists():
            parser.error(f"refusing to overwrite {screenshots}")
        screenshots.mkdir(parents=True)
    run(site, args.executable_path, screenshots)
    print("Browser, responsive, theme, MathJax, PDF, and accessibility checks passed.")


if __name__ == "__main__":
    main()
