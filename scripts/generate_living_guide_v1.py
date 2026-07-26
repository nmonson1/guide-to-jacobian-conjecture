#!/usr/bin/env python3
"""Generate public result, technical, and research-program pages."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from site_state import load_site_state


PROGRAM_PROSE = {
    "cubic-marked-root-incidence-geometry": {
        "idea": (
            "The known counterexample is most transparent as a forgetful map: "
            "start with a cubic together with a marked simple root, then forget "
            "which root was marked.  Three sheets are visible generically; the "
            "affine source is obtained by choosing exactly the boundary that "
            "turns the marked-root incidence space into affine three-space."
        ),
        "first": (
            "This program asks how much of that picture is forced.  It studies "
            "normalized cubic families, their finite completions, the divisors "
            "where sheets disappear, and the changes of coordinates that can "
            "or cannot disguise the construction."
        ),
        "line": (
            "Pole cancellation reduces the normalized family to one-variable "
            "polynomials.  The completed root-incidence cover then exposes the "
            "branch divisor and deleted boundary.  Class-group, motivic, and "
            "moving-hyperplane arguments test whether the same affine source "
            "can occur elsewhere."
        ),
        "limit": (
            "The marked-root interpretation of the original map, its basic "
            "fiber geometry, and the static hyperplane-orbit picture are "
            "credited background.  The reader manuscript contains the cover "
            "classification, equivalence, stable uniqueness, monodromy, and "
            "omitted-value results.  Formal normal rigidity and the local "
            "sign-torsor calculation remain proof-bearing companion "
            "developments; extending a local torsor globally remains open."
        ),
    },
    "minimum-degree-and-quartic-exclusions": {
        "idea": (
            "Once dimension three is known to admit counterexamples, degree is "
            "the next obvious measure of complexity.  The public example has "
            "degree seven, so the first serious frontier is whether degree four "
            "can already support a noninjective Keller map."
        ),
        "first": (
            "The program normalizes a hypothetical collision and studies the "
            "highest-degree image in projective space.  Point, line, conic, "
            "rational-cubic, and rational-quartic images behave differently; "
            "each stratum has its own obstruction and its own remaining cases."
        ),
        "line": (
            "Keller-jet equations constrain the leading forms.  Geometric "
            "classification of the resulting projective curve then turns the "
            "Jacobian condition into finite divisibility, valuation, and "
            "elimination problems.  The same invariant-gap method now excludes "
            "several fixed-factor conic strata in degrees five and six."
        ),
        "limit": (
            "This is not yet an unrestricted proof that quartic counterexamples "
            "do not exist.  The page separates completed exclusions from the "
            "balanced and tricuspidal quartic frontiers, the binary quintic "
            "overlap, and the primitive sextic conic case that remain open."
        ),
    },
    "local-rigidity-and-deformation-algebra": {
        "idea": (
            "A counterexample can be locally rigid as a bounded-degree "
            "polynomial map even though étaleness makes its unrestricted formal "
            "deformation theory look trivial.  The difference is the high-order "
            "incidence of a formal source orbit with a finite degree cutoff."
        ),
        "first": (
            "This program fixes the degree-seven counterexample, removes the "
            "obvious affine symmetries, and asks what infinitesimal directions "
            "remain.  It then follows those directions through successive "
            "orders until the local parameter algebra closes."
        ),
        "line": (
            "A weighted transverse slice reduces the calculation to ten "
            "parameters.  Exact Kuranishi equations define a finite local Artin "
            "algebra; its Hilbert function, inverse system, socle, and minimal "
            "equations encode the residual scheme-theoretic multiplicity.  "
            "Root coordinates identify the source-flow complex with a weighted "
            "divergence operator."
        ),
        "limit": (
            "The claims concern a specified bounded-degree quotient and do not "
            "rule out degree-increasing or unrestricted polynomial deformations. "
            "The exact computations are internally reproduced but need an "
            "independent computer-algebra implementation and expert review; a "
            "different-filtered reconstruction remains an open target."
        ),
    },
    "stable-moduli": {
        "idea": (
            "The counterexample belongs to explicit families.  The hard "
            "question is whether different parameters describe genuinely "
            "different polynomial maps, even after adding unused coordinates "
            "and allowing arbitrary polynomial changes on source and target."
        ),
        "first": (
            "Boundary geometry supplies the invariant.  A map's nonproperness "
            "set and deleted infinity data survive equivalence more rigidly than "
            "its displayed formula, so they can separate maps that look "
            "formally similar."
        ),
        "line": (
            "The program reconstructs decorated boundary schemes from the "
            "map, computes how the parameters transform, and tests which "
            "features persist after affine stabilization.  A relative-Jacobian "
            "blowup now recovers arbitrary common-root multiplicities and gives "
            "an all-multiplicity fixed-frame Torelli theorem."
        ),
        "limit": (
            "The stable-separation statements are presented with proofs using "
            "boundary and conductor invariants.  The finite-root classification "
            "now includes repeated roots; gluing it across strata where deleted "
            "roots escape to infinity remains open."
        ),
    },
    "homogeneous-descendants": {
        "idea": (
            "Many classical reductions replace a general Keller map by a "
            "cubic-homogeneous one in more variables.  After a counterexample "
            "exists, the natural quantitative question is how economically "
            "that replacement can be performed."
        ),
        "first": (
            "This program starts from a public degree-at-most-three descendant "
            "and measures the span of its cubic coordinates.  That rank, rather "
            "than the raw number of monomials, controls a collision-preserving "
            "suspension and the size of the resulting homogeneous map."
        ),
        "line": (
            "The same tensor is then studied through nilpotent Jordan type, "
            "Hessian constructions, square-zero pairings, Waring bounds, and "
            "equivariant compression obstructions.  A companion development "
            "asks how collision minimality produces a monolith whose "
            "multiplication algebra lies in a special-linear or symplectic "
            "prolongation."
        ),
        "limit": (
            "The manuscript credits the classical homogeneous reductions and "
            "the public low-dimensional inputs.  Its numerical bounds are for "
            "the displayed construction or stated symmetry class, not universal "
            "minimality theorems.  The five-dimensional frontier and "
            "monolith/prolongation theory remain in the companion register; "
            "the extension problem E(N) is open."
        ),
    },
    "plane-boundary-obstructions": {
        "idea": (
            "Dimension two remains open because the three-dimensional "
            "marked-root mechanism does not simply restrict to a plane.  A "
            "hypothetical plane counterexample must instead satisfy a tightly "
            "coupled boundary problem at infinity."
        ),
        "first": (
            "This program studies that boundary through Puiseux expansions, "
            "log geometry, Newton faces, Belyi maps, dessins, and normal jets. "
            "Each language sees a different part of the same compatibility "
            "problem between local branches and one global polynomial map."
        ),
        "line": (
            "A primitive Newton face produces a quotient cover and a finite "
            "passport problem.  A universal linear boundary operator and its "
            "residue adjoint then propagate constraints through the normal "
            "layers.  Exact formal coordinates decouple the determinant equation "
            "before the nonlinear Newton-support restriction is restored."
        ),
        "limit": (
            "The public degree-125 conclusion is credited to ratto3423, not "
            "claimed here.  The manuscript offers independently auditable "
            "boundary descriptions and terminal certificates.  Realizing the "
            "needed finite jets inside the filtered approximate-root subgroup "
            "and completing the global attachment remain open."
        ),
    },
}
ROOT = Path(__file__).resolve().parents[1]
SITE_STATE = load_site_state(ROOT)
PUBLICATION_DATA_DIR = SITE_STATE["publication"]["data_dir"]
MANUSCRIPTS_DATA_DIR = SITE_STATE["manuscripts"]["data_dir"]
PUBLIC_DOCS_DIR = SITE_STATE["docs_dir"]


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(root: Path) -> tuple[
    dict[str, Any],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    data_root = root / "data" / PUBLICATION_DATA_DIR
    export = _load_json(data_root / "public-export.json")
    manifest = _load_json(data_root / "manifest.json")
    for entry in manifest["files"]:
        path = data_root / entry["path"]
        if not path.is_file() or _sha256(path) != entry["sha256"]:
            raise ValueError(f"publication digest mismatch: {entry['path']}")
    pages = {
        item["slug"]: item for item in export["pages"]
    }
    technical = {
        item["slug"]: item
        for item in _load_json(data_root / "registry.json")["technical_records"]
    }
    programs = {
        item["slug"]: item for item in export["research_programs"]
    }
    manuscript_manifest = _load_json(
        root / "data" / MANUSCRIPTS_DATA_DIR / "manifest.json"
    )
    manuscripts: dict[str, dict[str, Any]] = {}
    for item in manuscript_manifest["manuscripts"]:
        sequence = item["filename"].split("-", 1)[0]
        path = root / PUBLIC_DOCS_DIR / "assets/manuscripts" / item["filename"]
        if not path.is_file() or _sha256(path) != item["sha256"]:
            raise ValueError(f"manuscript digest mismatch: {item['filename']}")
        manuscripts[sequence] = item
    return export, pages, technical, programs, manuscripts


def _yaml(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _credit_line(page: dict[str, Any]) -> str:
    credits = _grouped_credits(page["credited_to"])
    if not credits:
        return (
            "Credit assignment is still under source review for this working-draft page."
        )
    role_order = {
        "problem suggestion": 0,
        "discovery": 1,
        "construction": 1,
        "proof": 2,
        "exposition": 3,
        "formalization": 4,
        "research direction": 5,
    }
    credits.sort(
        key=lambda item: (
            min((role_order.get(role, 9) for role in item["roles"]), default=9),
            item["name"].casefold(),
        )
    )
    visible = [
        f"{item['name']} ({', '.join(item['roles'])})" for item in credits[:4]
    ]
    suffix = "" if len(credits) <= 4 else f", and {len(credits) - 4} others"
    return "Credited to " + "; ".join(visible) + suffix + "."


def _grouped_credits(credits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for credit in credits:
        entry = grouped.setdefault(
            credit["name"],
            {
                "name": credit["name"],
                "roles": [],
                "bases": [],
                "scopes": [],
            },
        )
        for role in credit["roles"]:
            if role not in entry["roles"]:
                entry["roles"].append(role)
        basis = credit["attribution_basis"].replace("_", " ")
        if basis not in entry["bases"]:
            entry["bases"].append(basis)
        if credit.get("scope") and credit["scope"] not in entry["scopes"]:
            entry["scopes"].append(credit["scope"])
    return list(grouped.values())


def _central_idea(page: dict[str, Any]) -> str:
    if page["kind"] == "open_problem":
        return (
            f"The problem is organized around one precise obstruction: "
            f"{page['statement']}  The supporting records separate known "
            "constraints from the remaining global step."
        )
    return (
        f"The theorem-level package is centered on the following mechanism: "
        f"{page['statement']}  Its supporting records isolate the ingredients "
        "that establish the statement and the qualifications that control its scope."
    )


def _first_reading(page: dict[str, Any]) -> str:
    if page["kind"] == "open_problem":
        return (
            "This is a genuine unresolved question, not a theorem with a missing "
            "citation.  The page groups the strongest current reductions so a "
            "reader can see exactly which part is known and which step is still open."
        )
    return (
        "Begin with the precise statement, then use the component statements as a "
        "map of the argument.  They separate the main assertion from proof "
        "ingredients, examples, qualifications, and corrections without requiring "
        "the reader to reconstruct the development from a claim ledger."
    )


def _manuscript_for_program(
    program: dict[str, Any], manuscripts: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    sequence = f"{program['sequence']:02d}"
    return manuscripts[sequence]


def _coverage_for_manuscript(
    page: dict[str, Any], manuscript_id: str
) -> dict[str, Any]:
    for item in page["manuscript_coverage"]["manuscripts"]:
        if item["manuscript"] == manuscript_id:
            return item
    return {"manuscript": manuscript_id, "status": "not_applicable"}


def _coverage_link_label(status: str) -> str:
    return {
        "complete": (
            "the version-9 reader-and-register release records the current "
            "statement and evidence boundary for the claims placed here"
        ),
        "manuscript_attached": "contains this result or its supporting argument",
        "not_applicable": "broader context only",
    }[status]


def _source_links(page: dict[str, Any]) -> list[str]:
    lines = []
    seen: set[str] = set()
    for source in page["source"]:
        label = source["title"]
        if source.get("authors"):
            label += " — " + ", ".join(source["authors"])
        if source.get("url"):
            key = source["url"]
            if key in seen:
                continue
            seen.add(key)
            if label.startswith(("http://", "https://")):
                host = urlparse(source["url"]).netloc.removeprefix("www.")
                label = f"Pinned source on {host}"
            lines.append(f"- [{label}]({source['url']})")
        elif source.get("citation"):
            key = source["citation"]
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- {label}: {source['citation']}")
    return lines


def render_result(
    page: dict[str, Any],
    pages: dict[str, dict[str, Any]],
    programs: dict[str, dict[str, Any]],
    manuscripts: dict[str, dict[str, Any]],
) -> str:
    kind = "Result" if page["kind"] == "result" else "Open problem"
    release = (
        "Established public record"
        if page["release_state"] == "public"
        else "Working draft"
    )
    lines = [
        "---",
        f"title: {_yaml(page['title'])}",
        f"description: {_yaml(page['description'])}",
        "---",
        "",
        f"# {page['title']}",
        "",
        f"<p class=\"dek\">{page['description']}</p>",
        "",
        f"<span class=\"status status-kind\">{kind}</span> "
        f"<span class=\"status status-draft\">{release}</span>",
        "",
        f"**{_credit_line(page)}**",
        "",
        f"**Source coverage:** {page['source_treatment']}",
        "",
        "## The central idea",
        "",
        _central_idea(page),
        "",
        "## For a first reading",
        "",
        _first_reading(page),
        "",
        "## Precise statement",
        "",
        page["statement"],
        "",
    ]
    if page["kind"] == "result":
        lines.extend(["## Proof idea and technical structure", ""])
    else:
        lines.extend(["## Known structure and remaining work", ""])
    for member in page["members"]:
        role = member["role"].replace("_", " ").title()
        inclusion = member["inclusion"].title()
        lines.extend(
            [
                f"### {member['title']}",
                "",
                member["statement"],
                "",
                f"*{inclusion} · {role} · {member['assessment'].replace('_', ' ')}*",
                "",
                f"[Open the deeper technical record](../technical/{member['technical_slug']}.md)",
                "",
            ]
        )
    lines.extend(["## Manuscripts and external links", ""])
    linked = False
    register_linked = False
    for program_slug in page["research_programs"]:
        program = programs[program_slug]
        manuscript = _manuscript_for_program(program, manuscripts)
        coverage = _coverage_for_manuscript(page, program["manuscript"])
        lines.append(
            f"- [{manuscript['title']}](../assets/manuscripts/"
            f"{manuscript['filename']}) — Nathaniel Monson, "
            f"{manuscript['manuscript_date']}; working manuscript; "
            f"{_coverage_link_label(coverage['status'])}; "
            f"SHA-256 `{manuscript['sha256']}`"
        )
        linked = True
        if (
            not register_linked
            and coverage["status"] == "complete"
            and "07" in manuscripts
        ):
            register = manuscripts["07"]
            lines.append(
                f"- [{register['title']}](../assets/manuscripts/"
                f"{register['filename']}) — companion statement and "
                f"evidence-boundary catalogue; SHA-256 `{register['sha256']}`"
            )
            register_linked = True
    source_lines = _source_links(page)
    lines.extend(source_lines)
    linked |= bool(source_lines)
    if not linked:
        lines.append(
            "- No public manuscript or external source has yet been assigned; "
            "source review is ongoing."
        )
    lines.append("")
    connections = sorted(
        set(page["connections"]["depends_on"])
        | set(page["connections"]["shares_claims_with"])
    )
    if connections:
        lines.extend(["## Connects to", ""])
        for slug in connections:
            related = pages[slug]
            lines.append(f"- [{related['title']}]({slug}.md)")
        lines.append("")
    lines.extend(
        [
            "## Evidence, review, and detailed credit",
            "",
            (
                "**Evidence present:** "
                if page["kind"] == "result"
                else "**Evidence for the known supporting results:** "
            )
            + (
                ", ".join(page["evidence_present"])
                if page["evidence_present"]
                else "no public evidence summary recorded"
            )
            + ".",
            "",
            "**Independent review:**",
            "",
        ]
    )
    for review in page["independent_review"]:
        lines.append(f"- {review['level'].title()}: {review['scope']}")
    lines.extend(["", "**Detailed credit:**", ""])
    if page["credited_to"]:
        for credit in sorted(
            _grouped_credits(page["credited_to"]),
            key=lambda item: item["name"].casefold(),
        ):
            roles = ", ".join(credit["roles"])
            basis = ", ".join(credit["bases"])
            scope = (
                " — " + "; ".join(credit["scopes"])
                if credit["scopes"]
                else ""
            )
            lines.append(
                f"- {credit['name']}: {roles}; {basis}{scope}"
            )
    else:
        lines.append("- No individual credit assignment is yet published.")
    if page["ai_assistance"]["present"]:
        lines.extend(["", "**AI assistance:**", ""])
        for item in page["ai_assistance"]["systems"]:
            lines.append(
                f"- {item['system']}: {', '.join(item['roles'])}; "
                f"{item['purpose']}"
            )
        humans = page["ai_assistance"]["responsible_humans"]
        if humans:
            lines.append(f"- Responsible human(s): {', '.join(humans)}")
    lines.extend(
        [
            "",
            '??? info "Registry details"',
            f"    Release state: `{page['release_state']}`",
            "",
            f"    Visibility: `{page['visibility']}`",
            "",
            f"    Source form: {', '.join(page['source_form']) or 'not yet assigned'}",
            "",
            f"    Manuscript coverage: `{page['manuscript_coverage']['status']}`",
            "",
            "    `complete` means that every program-relevant defining claim "
            "has an exact manuscript location. It does not mean independent "
            "proof review or machine verification.",
            "",
            f"    Grouped members: {page['metadata']['member_count']}",
            "",
            f"    Canonical registry: v{page['metadata']['canonical_registry_version']}",
            "",
            "[Back to all results and open problems](../research.md)",
            "",
        ]
    )
    return "\n".join(lines)


def render_research_index(
    pages: dict[str, dict[str, Any]],
    programs: dict[str, dict[str, Any]],
    manuscripts: dict[str, dict[str, Any]],
) -> str:
    results = sorted(
        (page for page in pages.values() if page["kind"] == "result"),
        key=lambda item: item["title"].casefold(),
    )
    open_problems = sorted(
        (page for page in pages.values() if page["kind"] == "open_problem"),
        key=lambda item: item["title"].casefold(),
    )
    lines = [
        "---",
        'title: "Research"',
        'description: "Six working research programs and the complete result and open-problem index."',
        "---",
        "",
        "# Research",
        "",
        '<p class="dek">Six questions opened by the counterexample, followed by '
        f"the complete public catalogue of {len(results)} results and "
        f"{len(open_problems)} open problems.</p>",
        "",
        "The six programs are working mathematical manuscripts, not refereed "
        "papers. The shorter version-9 PDFs contain their selected theorem "
        "spines. Secondary results, open problems, corrections, and research "
        "leads are preserved in a separate companion register.",
        "",
        (
            "[Download the Results and Research Register, v"
            f"{manuscripts['07']['version']}](assets/manuscripts/"
            f"{manuscripts['07']['filename']})"
            "{ .md-button .md-button--primary }"
        ),
        "",
        (
            f"Companion register · {manuscripts['07']['pages']} pages · "
            f"SHA-256 `{manuscripts['07']['sha256']}`"
        ),
        "",
        "## Six research programs",
        "",
    ]
    for program in sorted(programs.values(), key=lambda item: item["sequence"]):
        manuscript = _manuscript_for_program(program, manuscripts)
        lines.extend(
            [
                f"### {program['sequence']}. "
                f"[{program['title']}](research/programs/{program['slug']}.md)",
                "",
                f"**{program['question']}**",
                "",
                program["summary"],
                "",
                f"[Read the program](research/programs/{program['slug']}.md)"
                f" · [PDF, v{manuscript['version']}](assets/manuscripts/"
                f"{manuscript['filename']})",
                "",
            ]
        )
    for heading, selected, anchor_class in (
        ("All results", results, "result"),
        ("All open problems", open_problems, "open"),
    ):
        lines.extend(
            [
                f"## {heading}",
                "",
                f'<div class="catalogue catalogue-{anchor_class}" markdown>',
                "",
            ]
        )
        for page in selected:
            release = (
                "established public record"
                if page["release_state"] == "public"
                else "working draft"
            )
            lines.extend(
                [
                    f"### [{page['title']}](results/{page['slug']}.md)",
                    "",
                    page["description"],
                    "",
                    f"*{release}*",
                    "",
                ]
            )
        lines.extend(["</div>", ""])
    return "\n".join(lines)


def render_technical(
    record: dict[str, Any], pages: dict[str, dict[str, Any]]
) -> str:
    lines = [
        "---",
        f"title: {_yaml(record['title'])}",
        f"description: {_yaml(record['statement'])}",
        "robots: noindex, nofollow",
        "search:",
        "  exclude: true",
        "---",
        "",
        f"# {record['title']}",
        "",
        record["statement"],
        "",
        "This is a deeper technical record. It is intentionally absent from "
        "the site navigation and internal search.",
        "",
        "## Appears in",
        "",
    ]
    for membership in record["memberships"]:
        lines.append(
            f"- [{membership['page_title']}](../results/"
            f"{membership['page_slug']}.md) — "
            f"{membership['inclusion']}, {membership['role']}"
        )
    lines.extend(
        [
            "",
            "## Record summary",
            "",
            f"- Assessment: {record['assessment']}",
            f"- Release state: {record['release_state']}",
            f"- Evidence entries: {len(record['evidence_present'])}",
            f"- Public sources: {len(record['source'])}",
            "",
        ]
    )
    if record["source"]:
        lines.extend(["## Public sources", "", *_source_links(record), ""])
    if record["credited_to"]:
        lines.extend(["## Credit", ""])
        for credit in record["credited_to"]:
            lines.append(
                f"- {credit['name']}: {', '.join(credit['roles'])}; "
                f"{credit['attribution_basis'].replace('_', ' ')}"
            )
        lines.append("")
    if record["evidence_present"]:
        lines.extend(["## Evidence present", ""])
        for evidence in record["evidence_present"]:
            lines.append(f"- {evidence['kind']}: {evidence['scope']}")
        lines.append("")
    return "\n".join(lines)


def render_program(
    program: dict[str, Any],
    pages: dict[str, dict[str, Any]],
    manuscripts: dict[str, dict[str, Any]],
) -> str:
    prose = PROGRAM_PROSE[program["slug"]]
    manuscript = _manuscript_for_program(program, manuscripts)
    register = manuscripts["07"]
    result_pages = [
        pages[slug]
        for slug in program["page_slugs"]
        if pages[slug]["kind"] == "result"
    ]
    open_pages = [
        pages[slug]
        for slug in program["page_slugs"]
        if pages[slug]["kind"] == "open_problem"
    ]
    coverage_counts: dict[str, int] = defaultdict(int)
    for page in result_pages + open_pages:
        status = _coverage_for_manuscript(
            page, program["manuscript"]
        )["status"]
        coverage_counts[status] += 1
    lines = [
        "---",
        f"title: {_yaml(program['title'])}",
        f"description: {_yaml(program['question'])}",
        "---",
        "",
        f"# {program['title']}",
        "",
        f"<p class=\"dek\">{program['question']}</p>",
        "",
        '<span class="status status-draft">Working research program</span>',
        "",
        "## The mathematical idea",
        "",
        prose["idea"],
        "",
        "## For a first reading",
        "",
        prose["first"],
        "",
        "## The proof strategy",
        "",
        prose["line"],
        "",
        "## Scope and current boundary",
        "",
        prose["limit"],
        "",
        "## Working manuscript",
        "",
        f"[Download the versioned PDF](../../assets/manuscripts/"
        f"{manuscript['filename']}){{ .md-button .md-button--primary }}",
        "",
        f"Nathaniel Monson · manuscript dated {manuscript['manuscript_date']} · "
        f"{manuscript['pages']} pages · SHA-256 `{manuscript['sha256']}`",
        "",
        f"[Open the companion Results and Research Register](../../assets/manuscripts/"
        f"{register['filename']})",
        "",
        "The reader PDF contains this program's selected theorem spine. The "
        "companion register preserves secondary results, open problems, "
        "corrections, and evidence boundaries. Together with the version-8 "
        "archival edition, it supplies statement-level coverage for every "
        "program-relevant assigned record. Current page-level coverage: "
        + ", ".join(
            f"{status.replace('_', ' ')} {count}"
            for status, count in sorted(coverage_counts.items())
        )
        + ".",
        "",
    ]
    for heading, selected in (
        ("Results in this program", result_pages),
        ("Open problems in this program", open_pages),
    ):
        if not selected:
            continue
        lines.extend([f"## {heading}", ""])
        for page in sorted(selected, key=lambda item: item["title"].casefold()):
            lines.extend(
                [
                    f"### [{page['title']}](../../results/{page['slug']}.md)",
                    "",
                    page["description"],
                    "",
                ]
            )
    lines.extend(["[Back to Research](../../research.md)", ""])
    return "\n".join(lines)


def expected_outputs(
    root: Path,
    pages: dict[str, dict[str, Any]],
    technical: dict[str, dict[str, Any]],
    programs: dict[str, dict[str, Any]],
    manuscripts: dict[str, dict[str, Any]],
) -> dict[Path, str]:
    outputs: dict[Path, str] = {}
    for page in pages.values():
        outputs[
            root / PUBLIC_DOCS_DIR / "results" / f"{page['slug']}.md"
        ] = render_result(
            page, pages, programs, manuscripts
        )
    for record in technical.values():
        outputs[
            root / PUBLIC_DOCS_DIR / "technical" / f"{record['slug']}.md"
        ] = render_technical(record, pages)
    for program in programs.values():
        outputs[
            root
            / PUBLIC_DOCS_DIR
            / "research/programs"
            / f"{program['slug']}.md"
        ] = render_program(program, pages, manuscripts)
    outputs[root / PUBLIC_DOCS_DIR / "research.md"] = render_research_index(
        pages, programs, manuscripts
    )
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        _, pages, technical, programs, manuscripts = load(root)
        outputs = expected_outputs(
            root, pages, technical, programs, manuscripts
        )
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.write:
        for path, content in sorted(outputs.items()):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(
            f"Generated {len(pages)} result/open-problem pages, "
            f"{len(technical)} technical pages, and "
            f"{len(programs)} research-program pages."
        )
        return 0

    failures = []
    for path, expected in sorted(outputs.items()):
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(f"stale generated file: {path.relative_to(root)}")
    expected_paths = set(outputs)
    for directory in (
        root / PUBLIC_DOCS_DIR / "results",
        root / PUBLIC_DOCS_DIR / "technical",
        root / PUBLIC_DOCS_DIR / "research/programs",
    ):
        for path in directory.glob("*.md"):
            if path not in expected_paths:
                failures.append(
                    f"unexpected generated file: {path.relative_to(root)}"
                )
    if failures:
        print("Living-guide generation check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Living-guide generation check passed for {len(outputs)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
