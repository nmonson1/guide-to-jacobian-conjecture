#!/usr/bin/env python3
"""Render the Living Guide from the stable-tag claim graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from site_state import load_site_state


ROOT = Path(__file__).resolve().parents[1]
SITE_STATE = load_site_state(ROOT)
PUBLIC_DOCS_DIR = SITE_STATE["docs_dir"]
CLAIM_GRAPH_DATA_DIR = SITE_STATE["claim_graph"]["data_dir"]
PUBLICATION_DATA_DIR = SITE_STATE["publication"]["data_dir"]
MANUSCRIPTS_DATA_DIR = SITE_STATE["manuscripts"]["data_dir"]
TECHNICAL_MATERIALS_DATA_DIR = SITE_STATE["technical_materials"]["data_dir"]
MODEL_BRIEFS_DATA_DIR = SITE_STATE["model_briefs"]["data_dir"]

NEW_COLLECTIONS = (
    "cubic-resolvent-defect-exclusions",
    "quartic-target-span-two-ramification-filtration",
    "triple-ramification-and-fixed-component-endgame",
    "marked-root-source-flow-reconstruction",
    "categorical-cubic-frame-quotient",
    "full-kernel-regular-pencil-geometry",
    "nineteen-to-eighteen-compression-obstructions",
    "stored-degree-twenty-one-terminal-no-gluing",
)


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _human(value: str) -> str:
    return value.replace("_", " ").strip()


def _status_label(value: str) -> str:
    return {
        "proof offered": "Proof offered — review pending",
        "certificate offered": "Certificate offered — review pending",
        "open": "Open",
        "recorded": "Recorded",
    }.get(value, value.title())


def _coverage_label(value: str) -> str:
    return {
        "complete": "Exact manuscript location",
        "partial": "Locator audit incomplete",
        "manuscript_attached": "Manuscript attached",
        "not_applicable": "No program manuscript claimed",
        "not_in_manuscript": "Not in program manuscript",
        "locator_audit_needed": "Locator audit needed",
    }.get(value, _human(value).title())


def _source_lines(sources: list[dict[str, Any]]) -> list[str]:
    lines: list[str] = []
    seen: set[str] = set()
    for source in sources:
        url = source.get("url")
        citation = source.get("citation")
        key = url or citation or source.get("title", "")
        if not key or key in seen:
            continue
        seen.add(key)
        title = source.get("title", "Public source")
        authors = source.get("authors", [])
        if authors:
            title += " — " + ", ".join(authors)
        if url:
            lines.append(f"- [{title}]({url})")
        elif citation:
            lines.append(f"- {title}: {citation}")
    return lines


def _credit_lines(credits: list[dict[str, Any]]) -> list[str]:
    lines = []
    for credit in credits:
        roles = ", ".join(_human(role) for role in credit.get("roles", []))
        basis = _human(
            credit.get("attribution_basis", credit.get("basis", "recorded"))
        )
        scope = f" — {credit['scope']}" if credit.get("scope") else ""
        lines.append(f"- {credit['name']}: {roles}; {basis}{scope}")
    return lines


def load(root: Path) -> tuple[
    dict[str, Any],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, Any],
    dict[str, dict[str, Any]],
]:
    state = load_site_state(root)
    graph = _load(
        root / "data" / state["claim_graph"]["data_dir"] / "claim-graph.json"
    )
    claims = {item["tag"]: item for item in graph["claims"]}
    collections = {item["slug"]: item for item in graph["collections"]}
    programs = {item["slug"]: item for item in graph["programs"]}
    manuscript_manifest = _load(
        root / "data" / state["manuscripts"]["data_dir"] / "manifest.json"
    )
    manuscripts = {
        item["filename"][:2]: item for item in manuscript_manifest["manuscripts"]
    }
    materials = _load(
        root
        / "data"
        / state["technical_materials"]["data_dir"]
        / "manifest.json"
    )
    brief_manifest = _load(
        root / "data" / state["model_briefs"]["data_dir"] / "manifest.json"
    )
    if brief_manifest["brief_count"] != len(brief_manifest["briefs"]):
        raise ValueError("model brief manifest count mismatch")
    briefs = {item["program_slug"]: item for item in brief_manifest["briefs"]}
    if len(briefs) != state["model_briefs"]["expected_count"]:
        raise ValueError("model brief count disagrees with site-state.json")
    for brief in briefs.values():
        source = root / "data" / state["model_briefs"]["data_dir"] / brief["source"]
        if not source.is_file():
            raise ValueError(f"missing model brief source: {source}")
        payload = source.read_bytes()
        if len(payload) != brief["bytes"]:
            raise ValueError(f"model brief byte count mismatch: {source}")
        if hashlib.sha256(payload).hexdigest() != brief["sha256"]:
            raise ValueError(f"model brief digest mismatch: {source}")
    expected = state["expected_counts"]
    if graph["counts"] != {
        "claims": expected["technical_records"],
        "collections": expected["grouped_pages"],
        "programs": expected["research_programs"],
        "memberships": expected["memberships"],
    }:
        raise ValueError("claim graph counts disagree with site-state.json")
    if len(claims) != len(graph["claims"]):
        raise ValueError("duplicate public claim tag")
    return graph, claims, collections, programs, manuscripts, materials, briefs


def render_model_brief(brief: dict[str, Any], source: str) -> str:
    cross_program = brief.get("kind") == "cross_program"
    label = (
        "Model research brief · Cross-program"
        if cross_program
        else f'Model research brief · Program {brief["program_sequence"]}'
    )
    back_link = (
        "[Back to the research overview](../index.md)"
        if cross_program
        else f'[Back to the Program {brief["program_sequence"]} overview]'
        f'(../programs/{brief["program_slug"]}.md)'
    )
    return "\n".join(
        [
            "---",
            f"title: {_yaml('Model research brief — ' + brief['title'])}",
            "description: \"A self-contained mathematical handoff for a research model.\"",
            "---",
            "",
            f'<p class="claim-tag">{label}</p>',
            source.rstrip(),
            "",
            back_link,
            "",
        ]
    )


def render_claim(
    claim: dict[str, Any], collections: dict[str, dict[str, Any]]
) -> str:
    lines = [
        "---",
        f"title: {_yaml(claim['title'])}",
        f"description: {_yaml(claim['statement'])}",
        "---",
        "",
        f'<p class="claim-tag">{claim["tag"]}</p>',
        f"# {claim['title']}",
        "",
        f'<p class="dek">{claim["statement"]}</p>',
        "",
        f'<span class="status status-kind">{_human(claim["kind"]).title()}</span> '
        f'<span class="status status-draft">{_status_label(claim["status"])}</span> '
        f'<span class="status">{claim["prominence"].title()}</span>',
        "",
        "## Exact statement",
        "",
        claim["statement"],
        "",
        f"Statement version `{claim['statement_version']}`. The public tag is stable; "
        "statement revisions increment the version rather than replacing the tag.",
        "",
        "## Appears in",
        "",
    ]
    for membership in claim["memberships"]:
        collection = collections[membership["collection_slug"]]
        lines.append(
            f"- [{collection['title']}](../collections/{collection['slug']}.md) — "
            f"{_human(membership['inclusion'])}, {_human(membership['role'])}"
        )
    if not claim["memberships"]:
        lines.append("- No grouped public page currently contains this record.")
    lines.extend(["", "## Proof access and evidence boundary", ""])
    for access in claim["proof_access"]:
        collection = collections[access["collection_slug"]]
        lines.append(
            f"- [{collection['title']}](../collections/{collection['slug']}.md): "
            f"**{_coverage_label(access['status'])}**"
        )
    if not claim["proof_access"]:
        lines.append("- No program-manuscript location is claimed for this record.")
    reviews = claim["verification"].get("independent_review", [])
    lines.extend(["", "**Independent review**", ""])
    for review in reviews:
        lines.append(f"- {_human(review['level']).title()}: {review['scope']}")
    if not reviews:
        lines.append("- None recorded.")
    evidence = claim["verification"].get("evidence", [])
    precise_evidence = [
        item
        for item in evidence
        if isinstance(item, dict)
        and (
            item.get("links")
            or not item.get("scope", "").startswith(
                ("A proof is present", "Supporting checks are present")
            )
        )
    ]
    if precise_evidence:
        lines.extend(["", "**Recorded evidence**", ""])
        for item in precise_evidence:
            lines.append(f"- {_human(item['kind']).title()}: {item['scope']}")
    provenance = claim["provenance"]
    sources = _source_lines(provenance.get("sources", []))
    if sources:
        lines.extend(["", "## Public sources", "", *sources])
    credits = _credit_lines(provenance.get("credited_to", []))
    if credits:
        lines.extend(["", "## Credit", "", *credits])
    assistance = provenance.get("ai_assistance", {})
    if assistance.get("present"):
        lines.extend(["", "## AI assistance", ""])
        for item in assistance.get("systems", []):
            lines.append(
                f"- {item['system']}: {', '.join(_human(role) for role in item['roles'])}; "
                f"{item['purpose']}"
            )
        humans = assistance.get("responsible_humans", [])
        if humans:
            lines.append(f"- Responsible human(s): {', '.join(humans)}")
    lines.extend(["", "[Browse all claims](../results/all-claims.md)", ""])
    return "\n".join(lines)


def render_collection(
    page: dict[str, Any],
    claims: dict[str, dict[str, Any]],
    collections: dict[str, dict[str, Any]],
) -> str:
    coverage = page["manuscript_coverage"]["status"]
    lines = [
        "---",
        f"title: {_yaml(page['title'])}",
        f"description: {_yaml(page['description'])}",
        "---",
        "",
        f"# {page['title']}",
        "",
        f'<p class="dek">{page["description"]}</p>',
        "",
        f'<span class="status status-kind">{_human(page["kind"]).title()}</span> '
        f'<span class="status status-draft">{_human(page["public"]["release_state"]).title()}</span> '
        f'<span class="status coverage-{coverage}">{_coverage_label(coverage)}</span>',
        "",
        "## Precise statement",
        "",
        page["statement"],
        "",
        "## Claims in this result package",
        "",
    ]
    for tag in page["member_tags"]:
        claim = claims[tag]
        membership = next(
            item
            for item in claim["memberships"]
            if item["collection_slug"] == page["slug"]
        )
        lines.extend(
            [
                f"### [{claim['tag']} · {claim['title']}](../claims/{claim['tag']}.md)",
                "",
                claim["statement"],
                "",
                f"*{_human(membership['inclusion']).title()} · "
                f"{_human(membership['role']).title()} · {_status_label(claim['status'])}*",
                "",
            ]
        )
    lines.extend(
        [
            "## Evidence and manuscript boundary",
            "",
            page["source_treatment"],
            "",
            page["manuscript_coverage"]["coverage_rule"],
            "",
        ]
    )
    if page["source"]:
        lines.extend(["### Public sources", "", *_source_lines(page["source"]), ""])
    reviews = page["verification"].get("independent_review", [])
    lines.extend(["### Independent review", ""])
    for review in reviews:
        lines.append(f"- {_human(review['level']).title()}: {review['scope']}")
    if not reviews:
        lines.append("- None recorded.")
    if page["credited_to"]:
        lines.extend(["", "## Credit", "", *_credit_lines(page["credited_to"]), ""])
    connected = sorted(
        set(page["connections"].get("depends_on", []))
        | set(page["connections"].get("shares_claims_with", []))
    )
    if connected:
        lines.extend(["## Connections", ""])
        for slug in connected:
            if slug in collections:
                lines.append(
                    f"- [{collections[slug]['title']}](../collections/{slug}.md)"
                )
        lines.append("")
    lines.extend(["[Back to Results](../results/index.md)", ""])
    return "\n".join(lines)


def render_results_index(collections: dict[str, dict[str, Any]]) -> str:
    highlights = [
        page
        for page in collections.values()
        if page["public"]["release_state"] == "public" or page["slug"] in NEW_COLLECTIONS
    ]
    lines = [
        "---",
        'title: "Results and open problems"',
        'description: "A reader-facing map into the complete tagged claim graph."',
        "---",
        "",
        "# Results and open problems",
        "",
        '<p class="dek">Start with landmark results and the newest research packages, '
        "then move into the complete stable-tag claim graph.</p>",
        "",
        '<div class="metric-grid" markdown>',
        "",
        f"- **{sum(p['kind'] == 'result' for p in collections.values())}** grouped results",
        f"- **{sum(p['kind'] == 'open_problem' for p in collections.values())}** open-problem packages",
        "- **355** stable-tag atomic claims",
        "",
        "</div>",
        "",
        "[Browse every tagged claim](all-claims.md){ .md-button .md-button--primary }",
        "[See open problems](open-problems.md){ .md-button }",
        "[Open the proof index](../evidence/index.md){ .md-button }",
        "",
        "## Highlights",
        "",
        '<div class="record-grid" markdown>',
        "",
    ]
    for page in sorted(highlights, key=lambda item: item["title"].casefold()):
        lines.extend(
            [
                f"### [{page['title']}](../collections/{page['slug']}.md)",
                "",
                page["description"],
                "",
                f"*{_human(page['kind'])} · {_coverage_label(page['manuscript_coverage']['status'])}*",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


def render_all_claims(claims: dict[str, dict[str, Any]]) -> str:
    counts = Counter(claim["prominence"] for claim in claims.values())
    lines = [
        "---",
        'title: "All claims"',
        'description: "The complete searchable stable-tag claim catalogue."',
        "---",
        "",
        "# All claims",
        "",
        '<p class="dek">Every public atomic statement has one stable tag. Tags remain fixed when wording evolves; statement versions record revisions.</p>',
        "",
        f"{counts['headline']} headline · {counts['core']} core · {counts['supporting']} supporting",
        "",
        '<div class="claim-list" markdown>',
        "",
    ]
    for claim in sorted(claims.values(), key=lambda item: item["tag"]):
        lines.append(
            f"- [`{claim['tag']}`](../claims/{claim['tag']}.md) "
            f"**{claim['title']}** — {_status_label(claim['status'])}"
        )
    lines.extend(["", "</div>", ""])
    return "\n".join(lines)


def render_open_problems(
    collections: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]
) -> str:
    pages = sorted(
        (p for p in collections.values() if p["kind"] == "open_problem"),
        key=lambda item: item["title"].casefold(),
    )
    atomic = sorted(
        (c for c in claims.values() if c["kind"] == "open_problem"),
        key=lambda item: item["tag"],
    )
    lines = [
        "---",
        'title: "Open problems"',
        'description: "Unresolved questions separated from proved reductions and computational evidence."',
        "---",
        "",
        "# Open problems",
        "",
        f'<p class="dek">{len(pages)} grouped frontiers and {len(atomic)} atomic open-question records. Each page separates what is known from the step that remains.</p>',
        "",
    ]
    for page in pages:
        lines.extend(
            [
                f"## [{page['title']}](../collections/{page['slug']}.md)",
                "",
                page["description"],
                "",
                f"**Open statement:** {page['statement']}",
                "",
            ]
        )
    return "\n".join(lines)


def render_corrections(claims: dict[str, dict[str, Any]]) -> str:
    selected = [
        claim
        for claim in claims.values()
        if any(
            word in (claim["title"] + " " + claim["statement"]).casefold()
            for word in ("correction", "corrected", "proof gap", "failed extension")
        )
    ]
    lines = [
        "---",
        'title: "Corrections and scope changes"',
        'description: "Tagged records that correct, narrow, or explicitly retire an earlier line of argument."',
        "---",
        "",
        "# Corrections and scope changes",
        "",
        '<p class="dek">Corrections live in the same claim graph as results. They are not buried in release notes.</p>',
        "",
    ]
    for claim in sorted(selected, key=lambda item: item["tag"]):
        lines.extend(
            [
                f"## [{claim['tag']} · {claim['title']}](../claims/{claim['tag']}.md)",
                "",
                claim["statement"],
                "",
            ]
        )
    return "\n".join(lines)


def _manuscript(program: dict[str, Any], manuscripts: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return manuscripts[program["manuscript"][:2]]


def render_program(
    program: dict[str, Any],
    collections: dict[str, dict[str, Any]],
    manuscripts: dict[str, dict[str, Any]],
    briefs: dict[str, dict[str, Any]],
) -> str:
    pages = [collections[slug] for slug in program["collection_slugs"]]
    results = [page for page in pages if page["kind"] == "result"]
    problems = [page for page in pages if page["kind"] == "open_problem"]
    coverage = Counter(page["manuscript_coverage"]["status"] for page in pages)
    manuscript = _manuscript(program, manuscripts)
    lines = [
        "---",
        f"title: {_yaml(program['title'])}",
        f"description: {_yaml(program['question'])}",
        "---",
        "",
        f'<p class="claim-tag">Program {program["sequence"]}</p>',
        f"# {program['title']}",
        "",
        f'<p class="dek">{program["question"]}</p>',
        "",
        program["summary"],
        "",
        '<div class="metric-grid" markdown>',
        "",
        f"- **{len(results)}** result packages",
        f"- **{len(problems)}** open-problem packages",
        f"- **{coverage.get('complete', 0)}** exact-coverage pages",
        "",
        "</div>",
        "",
    ]
    if program["slug"] in briefs:
        brief = briefs[program["slug"]]
        lines.extend(
            [
                "## Model research brief",
                "",
                f"[Give a research model this one page](../handoffs/{program['slug']}.md)"
                "{ .md-button .md-button--primary }",
                "",
                "The brief is self-contained: setup, proved results with stable claim links, live frontier, failed approaches, tasks, evidence boundaries, and scope fences. No ZIP or private replay access is required.",
                "",
                f"Research state {brief['updated_at'] if brief.get('updated_at') else '29 July 2026'} · {brief['words']} words",
                "",
            ]
        )
    lines.extend(
        [
            "## Working paper",
            "",
            f"[{manuscript['title']}, v{manuscript['version']}](../../assets/manuscripts/{manuscript['filename']})"
            "{ .md-button .md-button--primary }",
            "",
            f"Nathaniel Monson · {manuscript['pages']} pages · dated {manuscript['manuscript_date']} · SHA-256 `{manuscript['sha256']}`",
            "",
            "The PDF is a working manuscript. Exact manuscript location, evidence, and independent review remain separate fields in the claim graph.",
            "",
        ]
    )
    for heading, selected in (("Results", results), ("Open problems", problems)):
        if not selected:
            continue
        lines.extend([f"## {heading}", ""])
        for page in sorted(selected, key=lambda item: item["title"].casefold()):
            lines.extend(
                [
                    f"### [{page['title']}](../../collections/{page['slug']}.md)",
                    "",
                    page["description"],
                    "",
                    f"*{_coverage_label(page['manuscript_coverage']['status'])}*",
                    "",
                ]
            )
    lines.extend(["[Back to research state](../index.md)", ""])
    return "\n".join(lines)


def render_research_index(
    programs: dict[str, dict[str, Any]],
    collections: dict[str, dict[str, Any]],
    briefs: dict[str, dict[str, Any]],
) -> str:
    lines = [
        "---",
        'title: "State of the research program"',
        'description: "Six working programs, their strongest reductions, and their exact open boundaries."',
        "---",
        "",
        "# State of the research program",
        "",
        '<p class="dek">The counterexample is settled; the surrounding classification, minimality, moduli, homogeneous reduction, and plane-boundary questions are not.</p>',
        "",
        "The current candidate incorporates 102 grouped result/problem packages and 355 stable-tag atomic claims. Eight packages are new in this release. Manuscript coverage and independent verification are displayed separately from mathematical status.",
        "",
        "## Model-ready handoffs",
        "",
        "A model-ready handoff is a single self-contained web page, not a download bundle. It records enough setup, known results, dead ends, tasks, and evidence boundaries to begin useful work without access to private conversations.",
        "",
    ]
    for brief in sorted(briefs.values(), key=lambda item: item["program_sequence"]):
        label = (
            brief["title"]
            if brief.get("kind") == "cross_program"
            else f"Program {brief['program_sequence']}: {brief['title']}"
        )
        lines.extend(
            [
                f"- [{label}](handoffs/{brief['program_slug']}.md) — {brief['words']} words; research state 29 July 2026.",
                "",
            ]
        )
    lines.extend(
        [
            "## Six programs",
            "",
            '<div class="record-grid" markdown>',
            "",
        ]
    )
    for program in sorted(programs.values(), key=lambda item: item["sequence"]):
        pages = [collections[slug] for slug in program["collection_slugs"]]
        open_count = sum(page["kind"] == "open_problem" for page in pages)
        lines.extend(
            [
                f"### [{program['sequence']}. {program['title']}](programs/{program['slug']}.md)",
                "",
                f"**{program['question']}**",
                "",
                program["summary"],
                "",
                f"*{len(pages)} packages · {open_count} open*",
                "",
            ]
        )
    lines.extend(["</div>", "", "## New in this candidate", ""])
    for slug in NEW_COLLECTIONS:
        page = collections[slug]
        lines.append(f"- [{page['title']}](../collections/{slug}.md) — {page['description']}")
    lines.extend(["", "[Browse the papers](papers.md){ .md-button }", ""])
    return "\n".join(lines)


def render_papers(manuscripts: dict[str, dict[str, Any]]) -> str:
    version = max(int(item["version"]) for item in manuscripts.values())
    lines = [
        "---",
        'title: "Working papers"',
        'description: "Six reader manuscripts and the companion results-and-research register."',
        "---",
        "",
        "# Working papers",
        "",
        f'<p class="dek">Version {version} of the six-program reader set. These are working manuscripts.</p>',
        "",
    ]
    for key, item in sorted(manuscripts.items()):
        lines.extend(
            [
                f"## [{item['title']}](../assets/manuscripts/{item['filename']})",
                "",
                f"Version {item['version']} · {item['pages']} pages · {item['manuscript_date']} · `{item['kind']}`",
                "",
                f"SHA-256 `{item['sha256']}`",
                "",
            ]
        )
    return "\n".join(lines)


def render_evidence_index(collections: dict[str, dict[str, Any]]) -> str:
    counts = Counter(page["manuscript_coverage"]["status"] for page in collections.values())
    lines = [
        "---",
        'title: "Proof and evidence index"',
        'description: "Claim-by-claim manuscript coverage and review boundaries."',
        "---",
        "",
        "# Proof and evidence index",
        "",
        '<p class="dek">Where a statement is written down is not the same as whether it has been independently checked.</p>',
        "",
        '<div class="metric-grid" markdown>',
        "",
        f"- **{counts['complete']}** exact manuscript coverage",
        f"- **{counts['partial']}** locator audits incomplete",
        f"- **{counts['not_applicable']}** no program manuscript claimed",
        "",
        "</div>",
        "",
        "| Result or problem package | Kind | Manuscript coverage |",
        "| --- | --- | --- |",
    ]
    for page in sorted(collections.values(), key=lambda item: item["title"].casefold()):
        lines.append(
            f"| [{page['title']}](../collections/{page['slug']}.md) | "
            f"{_human(page['kind'])} | {_coverage_label(page['manuscript_coverage']['status'])} |"
        )
    lines.append("")
    return "\n".join(lines)


def render_materials(materials: dict[str, Any]) -> str:
    lines = [
        "---",
        'title: "Technical materials"',
        'description: "Hash-pinned public computations, source bundles, and technical notes."',
        "---",
        "",
        "# Technical materials",
        "",
        f'<p class="dek">{materials["artifact_count"]} sanitized artifacts across {materials["program_count"]} programs.</p>',
        "",
        "Artifacts document exact calculations and reproducibility boundaries. They are not substitutes for proof or independent review.",
        "",
    ]
    for program in sorted(materials["programs"], key=lambda item: item["sequence"]):
        lines.extend([f"## {program['sequence']}. {program['title']}", "", program["scope"], ""])
        for item in program["artifacts"]:
            lines.extend(
                [
                    f"### [{item['title']}](../assets/technical-materials/{item['filename']})",
                    "",
                    item["scope"],
                    "",
                    f"**Boundary:** {item['limitations']}",
                    "",
                    f"SHA-256 `{item['sha256']}`",
                    "",
                ]
            )
    return "\n".join(lines)


def expected_outputs(root: Path) -> dict[Path, str]:
    _, claims, collections, programs, manuscripts, materials, briefs = load(root)
    docs = root / PUBLIC_DOCS_DIR
    outputs: dict[Path, str] = {}
    for claim in claims.values():
        outputs[docs / "claims" / f"{claim['tag']}.md"] = render_claim(
            claim, collections
        )
    for page in collections.values():
        outputs[docs / "collections" / f"{page['slug']}.md"] = render_collection(
            page, claims, collections
        )
    for program in programs.values():
        outputs[
            docs / "research/programs" / f"{program['slug']}.md"
        ] = render_program(program, collections, manuscripts, briefs)
    for brief in briefs.values():
        source_path = root / "data" / MODEL_BRIEFS_DATA_DIR / brief["source"]
        outputs[docs / brief["route"]] = render_model_brief(
            brief, source_path.read_text(encoding="utf-8")
        )
    outputs[docs / "results/index.md"] = render_results_index(collections)
    outputs[docs / "results/all-claims.md"] = render_all_claims(claims)
    outputs[docs / "results/open-problems.md"] = render_open_problems(
        collections, claims
    )
    outputs[docs / "results/corrections.md"] = render_corrections(claims)
    outputs[docs / "research/index.md"] = render_research_index(
        programs, collections, briefs
    )
    outputs[docs / "research/papers.md"] = render_papers(manuscripts)
    outputs[docs / "evidence/index.md"] = render_evidence_index(collections)
    outputs[docs / "evidence/materials.md"] = render_materials(materials)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        outputs = expected_outputs(root)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if args.write:
        for path, content in sorted(outputs.items()):
            if path.exists():
                raise FileExistsError(f"refusing to overwrite generated page: {path}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(f"Generated {len(outputs)} graph-native pages.")
        return 0
    failures = []
    for path, expected in sorted(outputs.items()):
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(f"stale generated file: {path.relative_to(root)}")
    expected_paths = set(outputs)
    for directory in (
        root / PUBLIC_DOCS_DIR / "claims",
        root / PUBLIC_DOCS_DIR / "collections",
        root / PUBLIC_DOCS_DIR / "research/programs",
        root / PUBLIC_DOCS_DIR / "research/handoffs",
    ):
        for path in directory.glob("*.md"):
            if path not in expected_paths:
                failures.append(f"unexpected generated file: {path.relative_to(root)}")
    if failures:
        print("Living-guide v2 generation check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Living-guide v2 generation check passed for {len(outputs)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
