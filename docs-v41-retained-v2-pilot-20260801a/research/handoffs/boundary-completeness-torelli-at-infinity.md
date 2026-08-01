---
title: "Model research brief — Boundary completeness and Torelli at infinity"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 2</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 1 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v14 · site release <code>living-guide-public-v41-retained-v2-pilot</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current text proofs — preferred"
    Use the [current TeX source and exact label anchors](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 2: Boundary completeness and Torelli at infinity

## Research objective

Determine when a finite marked-root closure remembers its affine opening and
extend fixed-frame Torelli across simultaneous roots escaping to infinity.
The main subjects are the complete polynomial-remainder-sequence base, its
outer inverse graph, and descent over logarithmic root expansions.

This lane overlaps [Program 1](cubic-marked-root-incidence-geometry.md) and
[Program 4](stable-moduli.md).  Exact retained statements are
[ordered-composition cells and Smith exponents](../working-mathematics/units/RMU-4D2E0001.md)
and the [complete PRS graph](../working-mathematics/units/RMU-4D2E0002.md).

## Reusable mathematics

For a monic degree-`m` root polynomial `Q` with nonzero constant term and
`nu >= m`, the southwest Krylov minors of multiplication by `w^nu mod Q`
are the principal subresultant coefficients of `(w^nu,Q)`, up to the stated
sign convention, and are also rectangular Schur polynomials.  The nonzero
normal indices

```text
0=n_0 < n_1 < ... < n_s=m
```

give an ordered composition `d_j=n_j-n_(j-1)`.  The companion--Hankel
rank-profile permutation is the direct sum of reversals of these consecutive
blocks.  Thus there are at most `2^(m-1)` relevant cells, not all Bruhat cells.
After filtered regular operations, the full Smith exponent on block `j` is

```text
nu - m + n_(j-1) + n_j
```

with multiplicity `d_j`.

The normalized graph closure of the complete projective subresultant sequence
defines a canonical complete-PRS space.  It is finite type, projective,
separated, and birational over the strongly regular locus.  On every exact
composition chart the pulled-back outer inverse graph is the normalized
blowup of one explicit monomial ideal and is toroidal.  Euclidean transfer
matrices compose strictly, so the corresponding chart cocycle is literal
associativity.  The deepest cyclotomic cell is etale in characteristic zero.

Earlier one-wall calculations remain useful checks: the coarse one-root graph
is `Bl_(epsilon^(N+2),y)`; the direct and ordered `N=3` charts differ by
`Bl_(u^2,v)`; and the tested coprime triple cocycle passes.  These do not prove
the simultaneous noncoprime boundary theorem.

## Live problem

Prove the PRS boundary theorem: the normalized complete-PRS graph should have
an atlas indexed by ordered compositions, with boundary strata given by block
merges and the Desnanot--Jacobi relations resolved by compatible weighted
quadratic pivots.  The most useful subproblems are:

- handle a genuinely noncoprime triple collision and overlapping block merges;
- prove smoothness or log smoothness of the PRS base across all composition
  closures;
- globalize homogeneous subresultants over the universal logarithmic root
  expansion, including line-bundle characters and stabilizers;
- extend the relative-Jacobian marking and fixed-frame Torelli across the same
  expansion;
- compare the result with logarithmic Quot K-transversalization.

The construction is not yet known to equal logarithmic Quot, and the displayed
global fibre product is still schematic.  Do not retain an open immersion as
part of the data and call reconstruction proved.  Do not replace the actual
companion--Hankel cells by all symmetric or complete-collineation strata unless
the larger space is needed for a proof.

## Useful deliverable

A proof for all adjacent block merges, including triple-overlap compatibility,
would be a major step.  So would a precise counterexample showing that the
complete-PRS graph needs an additional logarithmic modification.  Alternative
compactifications are welcome if they retain canonical subresultant
coordinates and explain how the affine opening is recovered.

[Back to the portfolio hub](state-of-the-program.md)
