#!/usr/bin/env python3
"""Generate/check the short self-contained overview and exact certificate."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from generate_claim_pages_v3 import load_records


def claim_link(record: dict, label: str | None = None) -> str:
    return f"[{label or record['title']}](claim-v3/{record['slug']}.md)"


def render_index(records: dict[str, dict]) -> str:
    determinant = records["JCG-CLAIM-0002"]
    collision = records["JCG-CLAIM-0003"]
    dimensions = records["JCG-CLAIM-0004"]
    plane = records["JCG-CLAIM-0005"]
    context = determinant["page"].get("context")
    if not context:
        raise ValueError("the determinant claim lacks the displayed-map context")
    return "\n".join(
        [
            "---",
            "title: Guide to the Jacobian Conjecture",
            "description: The conjecture, the three-dimensional counterexample, and a source-linked claim record.",
            "---",
            "",
            "# Guide to the Jacobian Conjecture",
            "",
            "The classical Jacobian conjecture asked whether a polynomial self-map of complex affine space with nonzero constant Jacobian determinant must have a polynomial inverse. A three-dimensional counterexample announced by Levent Alpöge in July 2026 shows that the answer is no in every dimension at least three. The plane case remains open.",
            "",
            "## Status by dimension",
            "",
            "- **Dimension 1:** true. A one-variable polynomial with nonzero constant derivative is linear.",
            f"- **Dimension 2:** {claim_link(plane, 'open')}.",
            f"- **Dimensions 3 and above:** {claim_link(dimensions, 'false')}.",
            "",
            "## The counterexample in one screen",
            "",
            context,
            "",
            f"Two exact facts do the work: {claim_link(determinant, 'the Jacobian determinant is the constant −2')}, and {claim_link(collision, 'three distinct rational points have one common image')}. The second fact prevents injectivity; the first satisfies the Keller hypothesis. Adding identity coordinates gives counterexamples in every higher dimension.",
            "",
            "[Read the exact certificate](certificate.md){ .md-button .md-button--primary }",
            "[Browse the claim inventory](claims-v3.md){ .md-button }",
            "",
            "## What this site records",
            "",
            "The guide separates mathematical claims from the sources that state or support them, the people credited for specific roles, and any independent review or machine check. **Proof offered** means that a linked source supplies an argument. It does not mean this project has independently verified the whole statement.",
            "",
            "The [chronology](chronology-v2.md) links dated events, contribution records, and claims in both directions. Longer methodology and mathematical storylines are intentionally deferred until the underlying record has settled.",
            "",
        ]
    )


def render_certificate(records: dict[str, dict]) -> str:
    determinant = records["JCG-CLAIM-0002"]
    collision = records["JCG-CLAIM-0003"]
    dimensions = records["JCG-CLAIM-0004"]
    plane = records["JCG-CLAIM-0005"]
    context = determinant["page"].get("context")
    if not context:
        raise ValueError("the determinant claim lacks the displayed-map context")
    return "\n".join(
        [
            "---",
            "title: Exact counterexample certificate",
            "description: The displayed map, determinant identity, collision, and dimensional consequence.",
            "---",
            "",
            "# Exact counterexample certificate",
            "",
            "This page isolates the finite algebraic data needed to refute the classical conjecture in dimension three. It is a reading certificate, not a new independent verification.",
            "",
            "## The map",
            "",
            context,
            "",
            "## The two exact checks",
            "",
            f"1. **Constant Jacobian.** {determinant['statement']} [{determinant['title']}](claim-v3/{determinant['slug']}.md)",
            f"2. **Failure of injectivity.** {collision['statement']} [{collision['title']}](claim-v3/{collision['slug']}.md)",
            "",
            "| Input | Common output |",
            "|---|---|",
            "| \\((0,0,-1/4)\\) | \\((-1/4,0,0)\\) |",
            "| \\((1,-3/2,13/2)\\) | \\((-1/4,0,0)\\) |",
            "| \\((-1,3/2,13/2)\\) | \\((-1/4,0,0)\\) |",
            "",
            "Because the determinant is nonzero and constant, the map satisfies the hypothesis. Because the three inputs are distinct, the map is not injective and therefore cannot be a polynomial automorphism.",
            "",
            "## Higher dimensions",
            "",
            "For every \\(n>3\\), take \\(F\\times\\operatorname{id}_{\\mathbb A^{n-3}}\\). Its Jacobian determinant is still \\(-2\\), and the displayed collision remains after appending the same extra coordinates. Thus the conjecture is false in every dimension at least three.",
            "",
            f"See the normalized dimensional claim: [{dimensions['title']}](claim-v3/{dimensions['slug']}.md).",
            "",
            "## Boundary of the certificate",
            "",
            f"- It says nothing against the two-dimensional conjecture, which {claim_link(plane, 'remains open')}.",
            "- It does not establish every geometric, arithmetic, or downstream claim associated with the counterexample.",
            "- Source proofs, executable checks, and Lean formalizations are listed on the individual claim pages. Their presence is distinct from an independent full-scope project verification.",
            "",
            "[Back to the overview](overview-v2.md)",
            "",
        ]
    )


def expected_outputs(root: Path) -> dict[Path, str]:
    records = load_records(root)
    return {
        root / "docs/overview-v2.md": render_index(records),
        root / "docs/certificate.md": render_certificate(records),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        outputs = expected_outputs(root)
    except (OSError, KeyError, ValueError) as exc:
        parser.error(str(exc))
    if args.write:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
        print("Generated the overview and exact certificate.")
        return 0
    failures = [
        path
        for path, expected in outputs.items()
        if not path.is_file() or path.read_text(encoding="utf-8") != expected
    ]
    if failures:
        for path in failures:
            print(f"stale generated page: {path.relative_to(root)}", file=sys.stderr)
        return 1
    print("Generated overview check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
