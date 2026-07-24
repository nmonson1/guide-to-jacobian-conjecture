#!/usr/bin/env python3
"""Generate the public chronology and contribution table from structured records."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from generate_claim_pages_v3 import load_records


EVENT_STATUS = {
    "audited-through-refereed-historical-study": "Audited through the cited refereed historical study",
    "bibliographic-source-recorded": "Bibliographic source recorded",
    "source-identified-theorem-normalization-pending": "Source identified; theorem normalization pending",
    "source-audited": "Source audited",
    "reported-context-not-proof-evidence": "Reported context; not proof evidence",
    "exact-certificate-publicly-announced": "Exact certificate publicly announced",
    "artifact-audited-no-project-assessment": "Artifact audited; no independent project assessment",
    "open-pr-status-checked-2026-07-22": "Open pull-request status checked 22 July 2026",
    "provenance-artifact-audited-not-a-transcript": "Provenance artifact audited; not a transcript",
    "mixed-working-analysis-no-project-assessment": "Mixed public working analysis; no independent project assessment",
    "exact-public-construction-no-project-assessment": "Exact public construction; no independent project assessment",
    "exact-public-certificate-no-project-assessment": "Exact public certificate; no independent project assessment",
    "source-note-audited-su3-inference-withheld": "Source note audited; fixed-dimensional SU(3) inference withheld",
    "artifact-indexed-no-normalized-claim": "Artifact indexed; no normalized claim",
    "closed-unmerged-status-checked-2026-07-22": "Closed unmerged status checked 22 July 2026",
    "pinned-formalization-source-audited": "Pinned formalization source audited",
    "correction-recorded": "Correction incorporated into the active claim",
    "exact-public-package-no-project-assessment": "Exact public package; no independent project assessment",
    "social-observation-not-mathematical-evidence": "Social observation; not mathematical evidence",
}


def display_date(value: Any) -> str:
    if isinstance(value, date):
        value = value.isoformat()
    value = str(value)
    if len(value) == 4 and value.isdigit():
        return value
    if len(value) == 10 and value[4] == "-" and value[7] == "-":
        year, month, day = value.split("-")
        names = [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
        ]
        return f"{int(day)} {names[int(month) - 1]} {year}"
    special = {
        "2026-07-19 Pacific": "19 Jul 2026 (Pacific time)",
        "2026-07-07 through 2026-07-11": "7–11 Jul 2026",
        "2026-07-20 (repository commit)": "20 Jul 2026 (repository commit)",
    }
    return special.get(value, value)


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def source_links(items: list[dict[str, Any]]) -> str:
    return "; ".join(f"[{item['title']}]({item['url']})" for item in items)


def claim_links(claim_ids: list[str], claims: dict[str, dict[str, Any]]) -> str:
    links = []
    for claim_id in claim_ids:
        if claim_id not in claims:
            links.append("withheld record")
            continue
        record = claims[claim_id]
        links.append(f"[{record['title']}](claim-v3/{record['slug']}.md)")
    return "; ".join(links) if links else "—"


def contribution_credit(record: dict[str, Any]) -> str:
    values = []
    for contributor in record.get("contributors", []):
        roles = ", ".join(role.replace("-", " ") for role in contributor["roles"])
        values.append(f"{contributor['name']} ({roles})")
    reported = record.get("reported_attribution")
    if reported:
        values.extend(
            [
                f"{reported['formula_announced_by']} (formula announced)",
                f"{reported['question_credited_to']} (question)",
                f"{reported['work_leading_to_example_credited_to']} (reported assistance)",
            ]
        )
    return "; ".join(values) if values else "No named contributor in the record"


def render(root: Path) -> str:
    events = [
        yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted((root / "events").glob("JCG-E-*.yml"))
    ]
    contributions = [
        yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted((root / "contributions").glob("JCG-C-*/metadata.yml"))
    ]
    claims = load_records(root)
    contribution_index = {item["id"]: item for item in contributions}
    events_by_contribution: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        for contribution_id in event.get("related_contributions", []):
            events_by_contribution[contribution_id].append(event)

    lines = [
        "---",
        "title: Chronology and contributions",
        "description: A dated event record and stable contribution list.",
        "---",
        "",
        "# Chronology and contributions",
        "",
        f"This page is generated from {len(events)} structured event records and {len(contributions)} contribution records. Events are sorted by historical date in Pacific time; repository entry sequence never establishes priority.",
        "",
        "`Source status` describes this guide's treatment of the source. It does not turn linked evidence into an independent verification.",
        "",
        "## Dated events",
        "",
        "| Date | Event | What entered the record | Source status |",
        "|---|---|---|---|",
    ]
    for event in sorted(events, key=lambda item: (str(item["sort_date"]), item["sequence"])):
        anchor = f'<span id="event-{event["id"].lower()}"></span>'
        related = []
        for contribution_id in event.get("related_contributions", []):
            contribution = contribution_index.get(contribution_id)
            if contribution:
                related.append(
                    f"[{contribution['title']}](#contribution-{contribution_id.lower()})"
                )
        claims_text = claim_links(event.get("related_claims", []), claims)
        if claims_text != "—":
            related.append(claims_text)
        details = escape_table(event["summary"])
        details += f"<br>Sources: {escape_table(source_links(event['sources']))}"
        if related:
            details += f"<br>Related: {escape_table('; '.join(related))}"
        status = EVENT_STATUS.get(
            event["record_status"], event["record_status"].replace("-", " ").capitalize()
        )
        lines.append(
            f"| {escape_table(display_date(event['event_date']))} | {anchor}{escape_table(event['title'])} | {details} | {escape_table(status)} |"
        )

    lines.extend(
        [
            "",
            "[Browse the structured event records](https://github.com/nmonson1/guide-to-jacobian-conjecture/tree/main/events)",
            "",
            "## Contributions",
            "",
            "| Work and credit | Source date and status | Claims and events |",
            "|---|---|---|",
        ]
    )
    for contribution in sorted(contributions, key=lambda item: item["sequence"]):
        anchor = f'<span id="contribution-{contribution["id"].lower()}"></span>'
        artifact = contribution["artifacts"][0]
        work = (
            f"{anchor}[{escape_table(contribution['title'])}]({artifact['url']})"
            f"<br>Credited to: {escape_table(contribution_credit(contribution))}"
        )
        source_status = contribution["publication_state"].replace("-", " ")
        source = (
            f"{escape_table(display_date(contribution['source_date']))}"
            f"<br>{escape_table(source_status.capitalize())}"
        )
        links = [claim_links(contribution.get("addresses_claims", []), claims)]
        for event in sorted(
            events_by_contribution.get(contribution["id"], []),
            key=lambda item: (str(item["sort_date"]), item["sequence"]),
        ):
            links.append(f"[{event['title']}](#event-{event['id'].lower()})")
        relation = "<br>".join(escape_table(value) for value in links if value != "—")
        lines.append(f"| {work} | {source} | {relation or '—'} |")

    lines.extend(
        [
            "",
            "[Browse the structured contribution records](https://github.com/nmonson1/guide-to-jacobian-conjecture/tree/main/contributions)",
            "",
            "## Editorial notes",
            "",
            "- The all-characteristic theorem is in the pinned standalone Lean repository, not in the recorded head of Formal Conjectures PR 4474.",
            "- The cited MathOverflow page for an independent all-degree family is currently deleted. The all-degree record instead relies on the Ulam note and the pinned JacobianFun construction.",
            "- The S3 and trivial-deck-group statements remain working claims: their MathOverflow post asks for correctness checking, has no answer, and was closed.",
            "- Public papers, scripts, and Lean code count as evidence present. A source's publication status is not a project verification.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    destination = root / "docs/chronology-v2.md"
    try:
        expected = render(root)
    except (OSError, KeyError, ValueError, yaml.YAMLError) as exc:
        parser.error(str(exc))
    if args.write:
        destination.write_text(expected, encoding="utf-8")
        print("Generated docs/chronology-v2.md.")
        return 0
    if not destination.is_file() or destination.read_text(encoding="utf-8") != expected:
        print("Generated chronology check failed: docs/chronology-v2.md is missing or stale.", file=sys.stderr)
        return 1
    print("Generated chronology check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
