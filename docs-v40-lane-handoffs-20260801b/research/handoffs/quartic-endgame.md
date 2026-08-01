---
title: "Model research brief — The quartic endgame"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 4</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 1 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v13 · site release <code>living-guide-public-v40-lane-handoffs</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current text proofs — preferred"
    Use the [current TeX source and exact label anchors](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 4: The quartic endgame

## Research objective

Finish the ordinary-degree-four case in three variables or identify the exact
surviving construction.  This lane currently has the shortest path to a major
theorem, but the missing step is global routing rather than another isolated
normal-form calculation.

The complete reference view is [Program 2](minimum-degree-and-quartic-exclusions.md).
Use its exact hypotheses and text proof links.  The unconditional public bound
remains

```text
4 <= D_min <= 7.
```

Do not state `D_min >= 5` without the remaining global case-tree hypothesis.

## Reusable mathematics

The scaled determinant arc routes leading target span one and two into explicit
ramification and fixed-component strata.  The current exact archive replays
the generic degree-three ramification chart; the supplied higher-ramification,
dependent-syzygy, quadratic-exceptional, fixed-component, and zero-normal
charts; and the displayed specializations `tau=0`, `tau=-1`, `tau^2+1`, and
`c=0`.  Its stored deterministic outputs match fresh replays.

An independent companion/Jordan-chain lens gives a divisor budget.  In the
quartic target-span-two setup its moment equations force

```text
deg gcd(grad(P) cross grad(Q)) >= 4
```

under the exact determinant-arc hypotheses.  The associated v2--v4 programs
route or exclude several high-ramification and `H=4` charts.  This is a
presentation-specific audit lens, not an invariant of every left-right
representative.

There are important proof-access boundaries.  The active paper directly
supports the original four invariant-field conic orbits, but complete proof
access for three later conic orbits and the rational-cubic exclusion is still
incomplete.  A high-ramification checker also imports a complete-specialization
claim whose source proof must be mapped exactly.  Existing chart certificates
remain useful; they do not supply missing branch exhaustiveness.

A newer degree-five/six packet is not a quartic proof.  Its structural portion
replays a squarefree binary-cubic quintic exclusion and two sextic cores under
their stated kernel hypotheses, while an aligned quintic specialization stays
open.  An older exploratory verifier has a wrong `tau=0` resultant expectation
and a wrong 28-minor count; the exact counts are 19 generically and on `tau=0`,
and 14 on the minimal-syzygy chart.

## Live problem

Write one global quartic case tree whose leaves are exactly the proved or
certified charts.  For every edge, record:

- the exact hypotheses entering the branch;
- saturation, normalization, and specialization assumptions;
- the paper statement or retained unit that justifies the edge;
- the checker or proof body that closes the leaf;
- the boundary if the leaf is only conditional.

Then audit the complete-specialization theorem and the three later conic
orbits.  Reproduce a small selection of decisive certificates through a
genuinely separate derivation, not merely a second wrapper around the same
SymPy formulas.  If the tree has an uncovered leaf, describe its normal form
as a candidate rather than forcing it into a nearby certificate.

## Useful deliverable

The best outcome is a readable theorem proof in which the global routing and
terminal calculations can be checked separately.  A precise counterexample to
the claimed exhaustiveness is equally valuable.  Do not spend context
recomputing already replayed terminal outputs unless the computation tests a
specific disputed edge.  Alternative global invariants or reductions are
welcome if they strictly replace a part of the case tree.

[Back to the portfolio hub](state-of-the-program.md)
