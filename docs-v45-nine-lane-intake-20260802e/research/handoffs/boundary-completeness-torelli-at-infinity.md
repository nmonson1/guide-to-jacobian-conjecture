---
title: "Model research brief — Boundary completeness and Torelli at infinity"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 2: Boundary completeness and Torelli at infinity

<p class="claim-tag">Lane 2 · Updated 2 August 2026</p>

## Problem and scope

For a polynomial Keller map, inverse-root formulas become rational when roots escape to infinity or
acquire common factors. This lane asks for a projective, separated atlas that
records all such degenerations, glues across successive block merges, and
retains enough boundary marking to recover the original affine opening.

The current candidate is the complete polynomial-remainder-sequence graph.
The fractional-Rees inverse graph and common-factor expansion tower are
different local models and are not identified.

## Setup and notation

Let `Q(w)` be monic of degree `m`, with nonzero constant term, and fix
`nu>=m`. Apply the Euclidean algorithm to `Q` and `w^nu mod Q`. The
*complete PRS graph* records the projective coefficient vector of every
nonzero remainder and the pivots needed to pass between divisions.

The nonzero southwest Krylov minors occur at normal indices

```text
0=n_0<n_1<...<n_s=m,
```

and define an ordered-composition chart with block sizes
`d_j=n_j-n_(j-1)`. A *block merge* occurs when a pivot minor vanishes and two
consecutive Euclidean blocks combine. It is *noncoprime* when adjacent pivot
data share a nonunit factor. A *triple overlap* admits both orders of two
successive merges among three consecutive blocks.

## Reusable mathematics

The Krylov minors are, up to the fixed sign convention, principal
subresultant coefficients and rectangular Schur polynomials. The
companion--Hankel rank profile is the direct sum of block reversals, and the
Smith exponent on block `j` is

```text
nu-m+n_(j-1)+n_j
```

with multiplicity `d_j`. Hence at most `2^(m-1)` Euclidean cells occur. The
convention-complete proof identifies the principal subresultant with the
relevant Hankel determinant and rectangular Schur polynomial and proves every
normal-index reversal block by orthogonal residuals and Schur complements.
Unit: [`RMU-4D2E0010`](../working-mathematics/units/RMU-4D2E0010.md); proof packet:
[`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/`](lane-2-source-packet.md).

The normalized graph of the complete projective PRS is finite type,
projective, separated, and birational over the strongly regular locus. On an
exact composition chart its outer inverse graph is the normalized blowup of
an explicit monomial ideal and is toroidal. PRS transfer matrices compose
strictly, so the cocycle where pivots are coprime is literal associativity.
Unit: [`RMU-4D2E0002`](../working-mathematics/units/RMU-4D2E0002.md). Context: [`manuscripts/04-stable-moduli/main.tex`](../proof-sources/04-stable-moduli/main.md) and
the exact statements and support boundaries on the two unit pages.

For the exact quintic chart, all sixteen composition types, the actual
five-by-five PRS flag, and the ordered outer resolution now have exact proof
and replay packets. The unordered finite-coordinate graph has an explicit
saturated Hilbert--Burch model. Across `T=0`, adjoining the displayed
integral element `w` gives a finite birational normalization; its negative
sheet is smooth and its positive sheet is reduced to the packet's Pfaffian
model. These results cover the finite outer coordinates. They do not cover
the projective-infinity charts at `T=0` or identify the PRS atlas with the
fractional-Rees and common-factor towers. Proofs and checkers:
[`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/`](lane-2-source-packet.md),
`lane2-progress-20260802c/`, and `lane2-progress-20260802d/`.

## Exact live problem

Complete the exact quintic normalization at the missing projective-infinity
charts over `T=0`, and prove that the finite-coordinate normalization glues to
them. The affine input is the Hilbert--Burch matrix and five equations
`F_0,...,F_4` in
[`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_theorem.md`](lane-2-source-packet.md).
Homogenize each outer factor separately, compute the integral closure on the
two infinity charts, and compare on overlaps with the `T!=0` cubic-scroll
normalization. The deliverable is a separated normal projective quintic outer
graph, or a precise extra component or conductor showing why that closure is
not the intended PRS atlas.

## Tasks and deliverables

### P4-L2A0 — Projective completion of the quintic outer graph

Status: ready.

Inputs: the ordered, unordered, and `T=0` theorem/checker packets linked
above. They include the finite-coordinate equations and transition to the
`T!=0` cubic-scroll chart.

Deliverable: equations and normality proofs on both outer infinity charts,
their conductor and overlap maps, and a proof of separated gluing with the
finite normalization. Record any additional component before discarding it.

### P4-L2A — Quantified noncoprime adjacent-merge theorem

Status: ready abstract follow-up; PRS-specific specialization remains blocked.

Inputs: `A=k[x,y,z]`, `I=(x^a,y^b)`, `J=(y^c,z^d)`, the normalized weak-
transform blowup convention, their simultaneous-linearity fan, and the
structural statements on [`RMU-4D2E0010`](../working-mathematics/units/RMU-4D2E0010.md) and [`RMU-4D2E0002`](../working-mathematics/units/RMU-4D2E0002.md).

Deliverable: first prove the toric order-comparison criterion in `a,b,c,d`;
then state exactly which additional PRS pivot data are needed to specialize
it to arbitrary adjacent block sizes and common-factor valuation.

### P4-L2B — Triple-overlap compatibility

Status: blocked on P4-L2A.

Inputs: the two chart morphisms produced by P4-L2A.

Deliverable: equality of the transition composites, including transfer
matrices and stabilizer characters, or a precise residual discrepancy.

### P4-L2C — Boundary marking

Status: blocked on the atlas theorem.

Inputs: a completed merge atlas and its exceptional divisors.

Deliverable: extend the relative-Jacobian marking and identify which boundary
components must be deleted to recover the affine source.

## Scope cautions

- Toroidality of individual charts does not prove compatibility of their closures.
- A rechart is an overlap arrow, not an automorphism of one fixed chart.
- A finite graph closure does not remember an affine opening without marked boundary.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
