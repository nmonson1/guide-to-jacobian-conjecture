#!/usr/bin/env python3
"""Generate the public claim inventory and one page per v2 claim record."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


ROLE_DISPLAY = {
    "conjecture_statement": "conjecture statement",
    "problem_suggestion": "problem suggestion",
    "research_assistance": "research assistance",
}

ROLE_PRIORITY = {
    "discovery": 0,
    "conjecture_statement": 1,
    "construction": 2,
    "proof": 3,
    "derivation": 4,
    "computation": 5,
    "formalization": 6,
    "verification": 7,
    "exposition": 8,
    "problem_suggestion": 9,
    "research_assistance": 10,
    "unspecified": 11,
}

STORYLINES: list[tuple[str | None, str]] = [
    ("counterexample-and-global-geometry", "Counterexample and global geometry"),
    ("finite-normalization-and-defect", "Finite normalization and defect"),
    ("deformations-families-and-equivalence", "Deformations, families, and equivalence"),
    ("reductions-to-special-forms", "Reductions to special forms"),
    ("two-dimensional-problem", "The two-dimensional problem"),
    (None, "Consequences and neighboring conjectures"),
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_records(root: Path) -> dict[str, dict[str, Any]]:
    data_root = root / "data/claims-v2"
    manifest = json.loads((data_root / "manifest.json").read_text(encoding="utf-8"))
    records: dict[str, dict[str, Any]] = {}
    for entry in manifest["files"]:
        path = data_root / entry["path"]
        actual = sha256(path)
        if actual != entry["sha256"]:
            raise ValueError(f"digest mismatch for {path.relative_to(root)}")
        record = json.loads(path.read_text(encoding="utf-8"))
        records[record["id"]] = record
    if len(records) != manifest["counts"]["total"]:
        raise ValueError("manifest count does not match the loaded records")
    return records


def primary_source(record: dict[str, Any]) -> dict[str, Any]:
    return next(source for source in record["sources"] if source["primary_for_display"])


def display_name(credit: dict[str, Any]) -> str:
    entity = credit["entity"]
    return entity.get("display_name", entity["name"])


def credit_sort_key(credit: dict[str, Any], source_id: str) -> tuple[Any, ...]:
    return (
        credit["basis_source_id"] != source_id,
        min(ROLE_PRIORITY.get(role, 99) for role in credit["roles"]),
        display_name(credit).casefold(),
    )


def credit_summary(record: dict[str, Any], maximum_people: int = 3) -> str:
    if not record["credited_to"]:
        return "Credit not yet assigned"
    source_id = primary_source(record)["id"]
    people = sorted(
        [credit for credit in record["credited_to"] if credit["entity"]["entity_type"] != "ai_system"],
        key=lambda credit: credit_sort_key(credit, source_id),
    )
    systems = sorted(
        display_name(credit)
        for credit in record["credited_to"]
        if credit["entity"]["entity_type"] == "ai_system"
    )
    shown = [display_name(credit) for credit in people[:maximum_people]]
    parts = [", ".join(shown)] if shown else []
    if systems:
        parts.append(f"AI assistance: {', '.join(systems)}")
    remaining = len(people) - len(shown)
    if remaining:
        parts.append(f"+{remaining} more")
    return "; ".join(parts)


def evidence_status(item: dict[str, Any]) -> str:
    if item["sufficiency"] == "no_proof_claim":
        return "Context only"
    if item["sufficiency"] == "partial_support":
        return "Partial support"
    if item["relation"] == "refutes":
        return "Full refutation offered"
    return "Full proof offered"


def evidence_kind(kind: str) -> str:
    return {
        "formalization": "Lean formalization",
        "exact_certificate": "Exact certificate",
        "literature_result": "Published or historical result",
        "status_report": "Status report",
    }.get(kind, kind.replace("_", " ").title())


def render_index(records: dict[str, dict[str, Any]]) -> str:
    lines = [
        "---",
        "title: Claims",
        "description: A source-linked inventory of Jacobian-conjecture claims and questions.",
        "---",
        "",
        "# Claim inventory",
        "",
        "Each row gives the claim, its primary source, concise credit, and current review status. Follow the claim link for evidence, limitations, and full attribution.",
        "",
        "!!! info \"How to read the status column\"",
        "    **Proof offered** means a source supplies an argument; it does not mean this guide has independently verified it. **Verified** is reserved for a qualifying review recorded against the exact statement and source version.",
        "",
    ]
    grouped: dict[str | None, list[dict[str, Any]]] = {}
    for record in records.values():
        grouped.setdefault(record.get("storyline"), []).append(record)
    known = {key for key, _ in STORYLINES}
    ordered = [*STORYLINES]
    ordered.extend(
        (key, str(key).replace("-", " ").title())
        for key in sorted(grouped, key=lambda value: str(value))
        if key not in known
    )
    for storyline, heading in ordered:
        if storyline not in grouped:
            continue
        lines.extend(
            [
                f"## {heading}",
                "",
                '<div class="claim-table" markdown="1">',
                "",
                "| Claim | Primary source | Credited to | Status |",
                "|---|---|---|---|",
            ]
        )
        for record in sorted(grouped[storyline], key=lambda item: item["id"]):
            source = primary_source(record)
            destination = source.get("url", source.get("citation", ""))
            source_link = f"[{source['title']}]({destination})"
            claim_link = f"[{record['title']}](claim/{record['slug']}.md)"
            statement = record["statement"].replace("|", "\\|").replace("\n", " ")
            credit = credit_summary(record).replace("|", "\\|")
            lines.append(
                f"| {claim_link}<br>{statement} | {source_link} | {credit} | {record['assessment']['label']} |"
            )
        lines.extend(["", "</div>", ""])
    return "\n".join(lines)


def render_page(record: dict[str, Any]) -> str:
    source = primary_source(record)
    destination = source.get("url", source.get("citation", ""))
    lines = [
        "---",
        f"title: {json.dumps(record['title'], ensure_ascii=False)}",
        f"description: {json.dumps(record['statement'], ensure_ascii=False)}",
        "---",
        "",
        f"# {record['title']}",
        "",
        record["statement"],
        "",
        f"**Status:** {record['assessment']['label']}<br>",
        f"**Primary source:** [{source['title']}]({destination})<br>",
        f"**Reviewed:** {record['assessment']['reviewed_on']}",
        "",
    ]
    if record.get("scope"):
        lines.extend(["## Scope", "", record["scope"], ""])
    lines.extend(["## Credit", "", credit_summary(record), ""])
    if record["credited_to"]:
        lines.extend(["<details>", "<summary>Full credit and attribution basis</summary>", ""])
        for credit in record["credited_to"]:
            roles = ", ".join(ROLE_DISPLAY.get(role, role.replace("_", " ")) for role in credit["roles"])
            ai = " (AI system)" if credit["entity"]["entity_type"] == "ai_system" else ""
            basis = {
                "explicit_self_credit": "explicit self-credit",
                "presumed_from_source": "presumed same as source",
                "attributed_by_source": "credited by the source",
                "documented_authorship": "documented authorship",
                "unknown": "basis not yet resolved",
            }[credit["basis"]]
            lines.append(
                f"- **{display_name(credit)}**{ai} — {roles}; {basis}. {credit.get('scope', '')}".rstrip()
            )
        lines.extend(["", "</details>", ""])
    else:
        lines.extend(["No claim-level credit has yet been assigned.", ""])
    lines.extend(["## Evidence", ""])
    if not record["evidence"]:
        lines.extend(["No evidence has yet been linked.", ""])
    for item in record["evidence"]:
        lines.extend(
            [
                f"### {evidence_kind(item['kind'])}",
                "",
                f"**{evidence_status(item)}.** {item['summary']}",
                "",
            ]
        )
        for artifact in item["artifacts"]:
            lines.append(f"- [{artifact['label']}]({artifact['url']})")
        if item["artifacts"]:
            lines.append("")
        if item["limitations"]:
            lines.extend(["What this evidence does not settle:", ""])
            lines.extend(f"- {value}" for value in item["limitations"])
            lines.append("")
    lines.extend(["## Review record", ""])
    if record["verification"]:
        for check in record["verification"]:
            lines.append(
                f"- **{check['method'].replace('_', ' ').title()} recorded:** {check['scope']}"
            )
    else:
        lines.append("This guide has not yet recorded an independent expert or machine check covering the whole claim.")
    if record["page"]["limitations"]:
        lines.extend(["", "## Limitations", ""])
        lines.extend(f"- {value}" for value in record["page"]["limitations"])
    if record["page"]["notes"]:
        lines.extend(["", "## Notes", ""])
        lines.extend(f"- {value}" for value in record["page"]["notes"])
    lines.extend(["", "## Sources", ""])
    for item in record["sources"]:
        marker = " — primary" if item["primary_for_display"] else ""
        item_destination = item.get("url", item.get("citation", ""))
        lines.append(f"- [{item['title']}]({item_destination}){marker}")
    lines.extend(["", "[Back to the claim inventory](../claims.md)", ""])
    return "\n".join(lines)


def expected_outputs(root: Path, records: dict[str, dict[str, Any]]) -> dict[Path, str]:
    outputs = {root / "docs/claims.md": render_index(records)}
    for record in records.values():
        outputs[root / "docs/claim" / f"{record['slug']}.md"] = render_page(record)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true", help="write generated Markdown instead of checking it")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        records = load_records(root)
        outputs = expected_outputs(root, records)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if args.write:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        print(f"Generated {len(records)} claim pages and the claim inventory.")
        return 0

    failures = []
    for path, expected in outputs.items():
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(root)}")
        elif path.read_text(encoding="utf-8") != expected:
            failures.append(f"stale generated file: {path.relative_to(root)}")
    expected_pages = {path for path in outputs if path.parent == root / "docs/claim"}
    actual_pages = set((root / "docs/claim").glob("*.md")) if (root / "docs/claim").is_dir() else set()
    for path in sorted(actual_pages - expected_pages):
        failures.append(f"unexpected generated page: {path.relative_to(root)}")
    if failures:
        print("Generated-claim check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Generated-claim check passed for {len(records)} claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
