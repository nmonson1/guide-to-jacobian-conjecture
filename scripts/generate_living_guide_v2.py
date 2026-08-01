#!/usr/bin/env python3
"""Render the Living Guide from the stable-tag claim graph."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
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
RETAINED_MATH_DATA_DIR = (
    SITE_STATE.get("retained_math", {}).get("data_dir")
)
MANUSCRIPT_SOURCES_DATA_DIR = (
    SITE_STATE.get("manuscript_sources", {}).get("data_dir")
)

MANUSCRIPT_TOKEN_RE = re.compile(r"\{\{MANUSCRIPT_(?P<sequence>[0-9]{2})\}\}")
LITERAL_MANUSCRIPT_LINK_RE = re.compile(
    r"assets/manuscripts/(?P<filename>[^)\s]+\.pdf)"
)

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


def load_retained_math(root: Path) -> tuple[dict[str, Any], dict[str, Any]] | None:
    state = load_site_state(root)
    component = state.get("retained_math")
    if component is None:
        return None
    data = root / "data" / component["data_dir"]
    manifest = _load(data / "manifest.json")
    graph = _load(data / "public-graph.json")
    if manifest.get("source_registry_id") != graph.get("registry_id"):
        raise ValueError("retained-math manifest and public graph disagree")
    if manifest.get("counts") != graph.get("counts"):
        raise ValueError("retained-math manifest and public counts disagree")
    files = manifest.get("files", [])
    if manifest.get("file_count") != len(files):
        raise ValueError("retained-math manifest file count disagrees")
    for item in files:
        path = data / item["path"]
        if not path.is_file():
            raise ValueError(f"missing retained-math source: {item['path']}")
        payload = path.read_bytes()
        if len(payload) != item["size_bytes"]:
            raise ValueError(f"retained-math byte count mismatch: {item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            raise ValueError(f"retained-math digest mismatch: {item['path']}")
    return manifest, graph


def load_manuscript_sources(root: Path) -> dict[str, Any] | None:
    state = load_site_state(root)
    component = state.get("manuscript_sources")
    if component is None:
        return None
    data = root / "data" / component["data_dir"]
    manifest = _load(data / "manifest.json")
    files = manifest.get("files", [])
    if manifest["counts"]["files"] != len(files):
        raise ValueError("manuscript-source file count disagrees")
    if manifest["counts"]["labels"] != len(manifest.get("labels", [])):
        raise ValueError("manuscript-source label count disagrees")
    if len(files) != component["expected_files"]:
        raise ValueError("manuscript-source file count disagrees with site state")
    if len(manifest["labels"]) != component["expected_labels"]:
        raise ValueError("manuscript-source label count disagrees with site state")
    indexed_labels = []
    for item in files:
        path = data / "sources" / item["path"]
        payload = path.read_bytes()
        if len(payload) != item["size_bytes"]:
            raise ValueError(f"manuscript-source byte count mismatch: {item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            raise ValueError(f"manuscript-source digest mismatch: {item['path']}")
        indexed_labels.extend(item["labels"])
    def label_key(item: dict[str, Any]) -> tuple[str, int, str]:
        return item["path"], item["line"], item["label"]

    if sorted(indexed_labels, key=label_key) != sorted(
        manifest["labels"], key=label_key
    ):
        raise ValueError("manuscript-source file labels disagree with global index")
    return manifest


def proof_source_route(path: str) -> Path:
    return Path("research/proof-sources") / Path(path).with_suffix(".md")


def _proof_entrypoint(
    manifest: dict[str, Any], program_sequence: int
) -> dict[str, Any]:
    entry_id = f"program-{program_sequence}"
    return next(
        item for item in manifest["entrypoints"] if item["entrypoint_id"] == entry_id
    )


def render_proof_source_page(item: dict[str, Any], source: str) -> str:
    relative = item["path"]
    language = "bibtex" if relative.endswith(".bib") else "tex"
    back = "../" * len(Path(relative).parent.parts) + "index.md"
    lines = [
        "---",
        f"title: {_yaml('Text proof source — ' + relative)}",
        f"description: {_yaml('Sanitized current source with exact TeX-label anchors.')}",
        "---",
        "",
        "# Text proof source",
        "",
        f"`manuscripts/{relative}`",
        "",
        "This is the current sanitized source text used by the retained working "
        "graph. Comments and private locators are omitted; mathematical content "
        "and line numbering are preserved. PDFs are optional reading copies.",
        "",
        f"Published SHA-256: `{item['sha256']}` · {item['size_bytes']:,} bytes",
        "",
    ]
    if item["labels"]:
        lines.extend(["## Exact label anchors", ""])
        for label in item["labels"]:
            lines.extend(
                [
                    f'<a id="{label["anchor"]}"></a>',
                    f"- `{label['label']}` — source line {label['line']}",
                ]
            )
        lines.append("")
    lines.extend(
        [
            "## Complete source",
            "",
            f"~~~{language}",
            source.rstrip(),
            "~~~",
            "",
            f"[Back to the text-source index]({back})",
            "",
        ]
    )
    return "\n".join(lines)


def render_proof_source_index(manifest: dict[str, Any]) -> str:
    files = {item["path"]: item for item in manifest["files"]}
    lines = [
        "---",
        'title: "Current text proof sources"',
        'description: "Model-friendly TeX sources for the current retained mathematics."',
        "---",
        "",
        "# Current text proof sources",
        "",
        "Give a research model the relevant program entrypoint below. It can "
        "follow `\\input` links, retained-unit source anchors, and technical "
        "records without downloading a PDF.",
        "",
        f"This pinned release contains **{manifest['counts']['files']} files**, "
        f"**{manifest['counts']['labels']} exact label anchors**, and "
        f"{manifest['counts']['size_bytes']:,} bytes of sanitized TeX/BibTeX.",
        "",
        "## Program entrypoints",
        "",
    ]
    for entry in manifest["entrypoints"]:
        path = entry["path"].removeprefix("manuscripts/")
        item = files[path]
        title = entry["entrypoint_id"].replace("-", " ").title()
        route = proof_source_route(path).relative_to("research/proof-sources")
        lines.append(
            f"- [{title}]({route.as_posix()}) — "
            f"{len(entry['selected_files'])} transitive source files, "
            f"{len(item['labels'])} labels in the entrypoint"
        )
    lines.extend(["", "## All published source files", ""])
    for item in manifest["files"]:
        route = proof_source_route(item["path"]).relative_to(
            "research/proof-sources"
        )
        lines.append(
            f"- [`{item['path']}`]({route.as_posix()}) — "
            f"{len(item['labels'])} labels · {item['size_bytes']:,} bytes"
        )
    lines.append("")
    return "\n".join(lines)


def retained_corrections(
    retained: tuple[dict[str, Any], dict[str, Any]] | None,
) -> dict[str, dict[str, Any]]:
    """Map corrected legacy claim tags to their current retained units."""
    if retained is None:
        return {}
    _, graph = retained
    corrections: dict[str, dict[str, Any]] = {}
    for unit in graph["units"]:
        for relation in unit.get("relations", []):
            target = relation.get("target_unit_id", "")
            if relation.get("relation_type") != "corrects" or not target.startswith(
                "JCG-"
            ):
                continue
            if target in corrections:
                raise ValueError(
                    f"legacy claim has multiple retained corrections: {target}"
                )
            corrections[target] = unit
    return corrections


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
    source_manifest = load_manuscript_sources(root)
    if source_manifest is None:
        raise ValueError("selected release does not pin manuscript sources")
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


def resolve_manuscript_links(
    source: str, manuscripts: dict[str, dict[str, Any]]
) -> str:
    literal = LITERAL_MANUSCRIPT_LINK_RE.search(source)
    if literal:
        raise ValueError(
            "model brief source must use a logical manuscript token, not "
            f"{literal.group('filename')}"
        )

    def replace(match: re.Match[str]) -> str:
        sequence = match.group("sequence")
        if sequence not in manuscripts:
            raise ValueError(f"unknown model-brief manuscript token: {sequence}")
        return manuscripts[sequence]["filename"]

    rendered = MANUSCRIPT_TOKEN_RE.sub(replace, source)
    if "{{MANUSCRIPT_" in rendered:
        raise ValueError("malformed model-brief manuscript token")
    return rendered


def _version_label(release_id: str) -> str:
    match = re.search(r"-v(?P<version>[0-9]+[a-z]?)-", release_id)
    if not match:
        raise ValueError(f"release ID has no version label: {release_id}")
    return f"v{match.group('version')}"


def build_release_metadata(root: Path) -> dict[str, Any]:
    state = load_site_state(root)
    manuscript_manifest = _load(
        root / "data" / state["manuscripts"]["data_dir"] / "manifest.json"
    )
    brief_manifest = _load(
        root / "data" / state["model_briefs"]["data_dir"] / "manifest.json"
    )
    source_manifest = load_manuscript_sources(root)
    if source_manifest is None:
        raise ValueError("selected release does not pin manuscript sources")
    versions = {item["version"] for item in manuscript_manifest["manuscripts"]}
    if len(versions) != 1:
        raise ValueError("selected manuscripts do not share one release version")
    manuscripts = []
    for item in manuscript_manifest["manuscripts"]:
        manuscripts.append(
            {
                "sequence": item["filename"][:2],
                "title": item["title"],
                "filename": item["filename"],
                "version": item["version"],
                "pages": item["pages"],
                "sha256": item["sha256"],
            }
        )
    handoffs = []
    for item in sorted(
        brief_manifest["briefs"], key=lambda brief: brief["program_sequence"]
    ):
        handoffs.append(
            {
                "kind": item["kind"],
                "program_sequence": item["program_sequence"],
                "program_slug": item["program_slug"],
                "title": item["title"],
                "route": item["route"].removesuffix(".md") + "/",
                "source_sha256": item["sha256"],
                "source_words": item["words"],
            }
        )
    release = {
        "schema_version": 1,
        "site_release_id": state["release_id"],
        "updated_at": state["updated_at"],
        "timezone": state["timezone"],
        "components": {
            "claim_graph_manifest_sha256": state["claim_graph"]["manifest_sha256"],
            "manuscript_manifest_sha256": state["manuscripts"]["manifest_sha256"],
            "model_brief_manifest_sha256": state["model_briefs"]["manifest_sha256"],
            "manuscript_source_manifest_sha256": state["manuscript_sources"]["manifest_sha256"],
        },
        "counts": state["expected_counts"],
        "manuscript_version": next(iter(versions)),
        "manuscripts": manuscripts,
        "handoff_source": {
            "release_id": brief_manifest["release_id"],
            "version": _version_label(brief_manifest["release_id"]),
            "count": brief_manifest["brief_count"],
        },
        "handoffs": handoffs,
        "manuscript_sources": {
            "release_id": source_manifest["release_id"],
            "source_repository_commit": source_manifest["source_repository_commit"],
            "counts": source_manifest["counts"],
            "index_route": "research/proof-sources/",
        },
    }
    retained = load_retained_math(root)
    if retained is not None:
        manifest, graph = retained
        release["retained_math"] = {
            "release_id": manifest["release_id"],
            "registry_id": graph["registry_id"],
            "counts": graph["counts"],
        }
    return release


def render_model_brief(
    brief: dict[str, Any],
    source: str,
    manuscripts: dict[str, dict[str, Any]],
    release: dict[str, Any],
    proof_sources: dict[str, Any],
) -> str:
    source = resolve_manuscript_links(source, manuscripts)
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
    retained_note: list[str] = []
    if "retained_math" in release:
        retained_target = (
            "../working-mathematics/index.md"
            if cross_program
            else "../working-mathematics/programs/"
            f"{brief['program_slug']}.md"
        )
        retained_note = [
            "",
            '!!! info "Retained working graph"',
            "    Exact reusable units and their deeper support pages are available",
            f"    in the [retained working mathematics view]({retained_target}).",
        ]
    if cross_program:
        source_target = "../proof-sources/index.md"
    else:
        entry = _proof_entrypoint(proof_sources, brief["program_sequence"])
        source_path = entry["path"].removeprefix("manuscripts/")
        source_target = "../proof-sources/" + proof_source_route(
            source_path
        ).relative_to("research/proof-sources").as_posix()
    source_note = [
        "",
        '!!! tip "Current text proofs — preferred"',
        "    Use the [current TeX source and exact label anchors]"
        f"({source_target}) for full proof context. PDFs are optional archival",
        "    reading copies and may predate source repairs.",
    ]
    return "\n".join(
        [
            "---",
            f"title: {_yaml('Model research brief — ' + brief['title'])}",
            "description: \"A self-contained mathematical handoff for a research model.\"",
            "---",
            "",
            f'<p class="claim-tag">{label}</p>',
            (
                '<p class="handoff-snapshot"><strong>Snapshot:</strong> '
                f'{datetime.fromisoformat(release["updated_at"]).strftime("%-d %B %Y")} '
                f'· {release["counts"]["technical_records"]} public claim records '
                f'· {release["counts"]["grouped_pages"]} grouped packages '
                f'· manuscripts v{release["manuscript_version"]} '
                f'· handoff source {release["handoff_source"]["version"]} '
                f'· site release <code>{release["site_release_id"]}</code>.</p>'
            ),
            (
                "[Machine-readable release metadata](release.json)"
                "{ .handoff-release }"
            ),
            *retained_note,
            *source_note,
            source.rstrip(),
            "",
            back_link,
            "",
        ]
    )


def render_claim(
    claim: dict[str, Any],
    collections: dict[str, dict[str, Any]],
    correction: dict[str, Any] | None = None,
) -> str:
    correction_block = []
    if correction is not None:
        unit_id = correction["unit_id"]
        correction_block = [
            '!!! warning "Superseded by current working mathematics"',
            "    This stable-tag statement is retained as publication-pipeline "
            "history. Use the",
            f"    [current corrected unit](../research/working-mathematics/units/{unit_id}.md)",
            "    for research and model handoffs.",
            "",
            "## Current corrected statement",
            "",
            correction["statement"],
            "",
        ]
    lines = [
        "---",
        f"title: {_yaml(claim['title'])}",
        f"description: {_yaml(claim['statement'])}",
        "---",
        "",
        f'<p class="claim-tag">{claim["tag"]}</p>',
        f"# {claim['title']}",
        "",
        *correction_block,
        *(
            []
            if correction is not None
            or claim["statement"].strip() == claim["title"].strip()
            else [f'<p class="dek">{claim["statement"]}</p>', ""]
        ),
        f'<span class="status status-kind">{_human(claim["kind"]).title()}</span> '
        f'<span class="status status-draft">{_status_label(claim["status"])}</span> '
        f'<span class="status">{claim["prominence"].title()}</span>',
        "",
        "## Exact statement",
        "",
        *(
            ["**Superseded legacy wording:**", ""]
            if correction is not None
            else []
        ),
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
    locators = claim.get("locators", [])
    if locators:
        # Manuscript-source anchors from the private coverage audit; plain
        # text only, so no private path or identifier can become a link.
        lines.extend(["", "## Proof locators", ""])
        for locator in locators:
            role = locator["role"].strip()
            suffix = f" ({role})" if role else ""
            lines.append(
                f"- `{locator['anchor']}` in `{locator['repo_path']}`{suffix}"
            )
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
    corrections: dict[str, dict[str, Any]],
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
        correction = corrections.get(tag)
        membership = next(
            item
            for item in claim["memberships"]
            if item["collection_slug"] == page["slug"]
        )
        lines.extend(
            [
                f"### [{claim['tag']} · {claim['title']}](../claims/{claim['tag']}.md)",
                "",
                *(
                    [
                        '!!! warning "Superseded working statement"',
                        "    Use the "
                        f"[current corrected unit](../research/working-mathematics/units/{correction['unit_id']}.md).",
                        "",
                    ]
                    if correction is not None
                    else []
                ),
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


def render_results_index(
    collections: dict[str, dict[str, Any]],
    claims: dict[str, dict[str, Any]],
) -> str:
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
        f"- **{len(claims)}** stable-tag atomic claims",
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


def render_all_claims(
    claims: dict[str, dict[str, Any]],
    corrections: dict[str, dict[str, Any]],
) -> str:
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
        correction = corrections.get(claim["tag"])
        suffix = (
            f"; superseded by `{correction['unit_id']}`"
            if correction is not None
            else ""
        )
        lines.append(
            f"- [`{claim['tag']}`](../claims/{claim['tag']}.md) "
            f"**{claim['title']}** — {_status_label(claim['status'])}{suffix}"
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


def render_corrections(
    claims: dict[str, dict[str, Any]],
    corrections: dict[str, dict[str, Any]],
) -> str:
    selected = [
        claim
        for claim in claims.values()
        if claim["tag"] in corrections
        or any(
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
        correction = corrections.get(claim["tag"])
        lines.extend(
            [
                f"## [{claim['tag']} · {claim['title']}](../claims/{claim['tag']}.md)",
                "",
                claim["statement"],
                "",
                *(
                    [
                        "**Current corrected statement:** "
                        f"[{correction['unit_id']}](../research/working-mathematics/units/{correction['unit_id']}.md)",
                        "",
                        correction["statement"],
                        "",
                    ]
                    if correction is not None
                    else []
                ),
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
    proof_sources: dict[str, Any],
) -> str:
    pages = [collections[slug] for slug in program["collection_slugs"]]
    results = [page for page in pages if page["kind"] == "result"]
    problems = [page for page in pages if page["kind"] == "open_problem"]
    coverage = Counter(page["manuscript_coverage"]["status"] for page in pages)
    manuscript = _manuscript(program, manuscripts)
    entry = _proof_entrypoint(proof_sources, program["sequence"])
    source_path = entry["path"].removeprefix("manuscripts/")
    source_route = proof_source_route(source_path).relative_to("research")
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
            "## Current text proof sources",
            "",
            f"[Open the complete Program {program['sequence']} TeX source]"
            f"(../{source_route.as_posix()})"
            "{ .md-button .md-button--primary }",
            "",
            "The text source is the current model-friendly authority: exact "
            "definitions, statements, proofs, dependencies, and label anchors.",
            "",
            "## Optional PDF reading copy",
            "",
            f"[{manuscript['title']}, v{manuscript['version']}](../../assets/manuscripts/{manuscript['filename']})"
            "{ .md-button }",
            "",
            f"Nathaniel Monson · {manuscript['pages']} pages · dated {manuscript['manuscript_date']} · SHA-256 `{manuscript['sha256']}`",
            "",
            "This PDF predates some August 1 source repairs. Use it for reading, "
            "not as the authority when it differs from the retained graph or text source.",
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
    claims: dict[str, dict[str, Any]],
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
        f"The current candidate incorporates {len(collections)} grouped "
        f"result/problem packages and {len(claims)} stable-tag atomic claims. "
        "Manuscript coverage and independent verification are displayed "
        "separately from mathematical status.",
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
    release = build_release_metadata(root)
    docs = root / PUBLIC_DOCS_DIR
    outputs: dict[Path, str] = {}
    retained = load_retained_math(root)
    proof_sources = load_manuscript_sources(root)
    if proof_sources is None:
        raise ValueError("selected release does not pin manuscript sources")
    if retained is None:
        raise ValueError("selected release does not pin retained mathematics")
    if (
        proof_sources["retained_registry"]["registry_id"]
        != retained[1]["registry_id"]
    ):
        raise ValueError("manuscript sources and retained graph disagree")
    corrections = retained_corrections(retained)
    for claim in claims.values():
        outputs[docs / "claims" / f"{claim['tag']}.md"] = render_claim(
            claim, collections, corrections.get(claim["tag"])
        )
    for page in collections.values():
        outputs[docs / "collections" / f"{page['slug']}.md"] = render_collection(
            page, claims, collections, corrections
        )
    for program in programs.values():
        outputs[
            docs / "research/programs" / f"{program['slug']}.md"
        ] = render_program(
            program, collections, manuscripts, briefs, proof_sources
        )
    for brief in briefs.values():
        source_path = root / "data" / MODEL_BRIEFS_DATA_DIR / brief["source"]
        outputs[docs / brief["route"]] = render_model_brief(
            brief,
            source_path.read_text(encoding="utf-8"),
            manuscripts,
            release,
            proof_sources,
        )
    outputs[docs / "research/handoffs/release.json"] = (
        json.dumps(release, indent=2, sort_keys=True) + "\n"
    )
    outputs[docs / "results/index.md"] = render_results_index(
        collections, claims
    )
    outputs[docs / "results/all-claims.md"] = render_all_claims(
        claims, corrections
    )
    outputs[docs / "results/open-problems.md"] = render_open_problems(
        collections, claims
    )
    outputs[docs / "results/corrections.md"] = render_corrections(
        claims, corrections
    )
    outputs[docs / "research/index.md"] = render_research_index(
        programs, collections, claims, briefs
    )
    outputs[docs / "research/papers.md"] = render_papers(manuscripts)
    outputs[docs / "evidence/index.md"] = render_evidence_index(collections)
    outputs[docs / "evidence/materials.md"] = render_materials(materials)
    source_data = root / "data" / SITE_STATE["manuscript_sources"]["data_dir"]
    outputs[docs / "research/proof-sources/index.md"] = (
        render_proof_source_index(proof_sources)
    )
    for item in proof_sources["files"]:
        source_path = source_data / "sources" / item["path"]
        outputs[docs / proof_source_route(item["path"])] = (
            render_proof_source_page(
                item, source_path.read_text(encoding="utf-8")
            )
        )
    if retained is not None:
        _, retained_graph = retained
        retained_data = root / "data" / SITE_STATE["retained_math"]["data_dir"]
        retained_programs = retained_graph["programs"]
        program_links = "\n".join(
            f"- [{program['title']}](programs/{program['slug']}.md)"
            for program in retained_programs
        )
        retained_counts = retained_graph["counts"]
        outputs[docs / "research/working-mathematics/index.md"] = (
            "# Retained working mathematics\n\n"
            "This view is generated from the retained mathematical graph. It "
            "exposes exact reusable units, supplied support, dependencies, and "
            "scope without private source locators or editorial workflow labels.\n\n"
            f"The current graph contains **{retained_counts['units']} working units** "
            f"across {len(retained_programs)} overlapping program views, with "
            f"{retained_counts['support_objects']} support objects and "
            f"{retained_counts['relations']} typed relations.\n\n"
            f"{program_links}\n\n"
            "This is not the publication-ready subset. Verification, attribution, "
            "deduplication, and dependency repair proceed asynchronously.\n"
        )
        for program in retained_programs:
            relative = Path("programs") / f"{program['slug']}.md"
            outputs[
                docs / "research/working-mathematics" / relative
            ] = (retained_data / relative).read_text(encoding="utf-8")
        for source in sorted((retained_data / "units").glob("*.md")):
            outputs[
                docs / "research/working-mathematics/units" / source.name
            ] = source.read_text(encoding="utf-8")
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
        root / PUBLIC_DOCS_DIR / "research/proof-sources",
        root / PUBLIC_DOCS_DIR / "research/working-mathematics/programs",
        root / PUBLIC_DOCS_DIR / "research/working-mathematics/units",
    ):
        for path in directory.rglob("*.md"):
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
