---
title: "Model research brief — Boundary completeness and Torelli at infinity"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 2</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v16d · site release <code>living-guide-public-v43d-nine-lane-reconstruction</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 2: Boundary completeness and Torelli at infinity

## Research objective

Compactify the inverse-root construction when several roots escape to
infinity, prove compatibility across overlapping degeneration charts, and
recover the affine opening and fixed-frame Torelli data from the boundary.

The current canonical working object is the complete polynomial-remainder-
sequence graph.  The fractional-Rees inverse graph and the common-factor
expansion tower are different local constructions and should not be merged.

## Reusable mathematics

Let `Q(w)` be monic of degree `m`, with nonzero constant term, and let
`nu>=m`.  The southwest Krylov minors for multiplication by `w^nu mod Q` are,
up to the recorded sign convention, both principal subresultant coefficients
and rectangular Schur polynomials.  If

```text
0=n_0<n_1<...<n_s=m,       d_j=n_j-n_(j-1),
```

are the normal indices and ordered-composition blocks, then the
companion--Hankel rank profile is the direct sum of the block reversals.  The
full Smith exponent on block `j` is

```text
nu-m+n_(j-1)+n_j
```

with multiplicity `d_j`.  There are at most `2^(m-1)` relevant Euclidean
cells.  Retained unit: [`RMU-4D2E0001`](../working-mathematics/units/RMU-4D2E0001.md).

The normalized graph of the complete projective subresultant sequence is an
explicit finite-type, projective, separated space, birational over the
strongly regular locus.  On every exact composition chart the outer inverse
graph is the normalized blowup of one explicit monomial ideal and is
toroidal.  PRS transfer matrices compose strictly, so their triple-overlap
cocycle is literal associativity.  Retained unit: [`RMU-4D2E0002`](../working-mathematics/units/RMU-4D2E0002.md).

Useful local checks are also exact:

- the coarse one-root graph is `Bl_(epsilon^(N+2),y)`;
- the direct and ordered `N=3` charts differ by `Bl_(u^2,v)`;
- the tested coprime triple transition satisfies the cocycle identity; and
- the deepest cyclotomic cell is etale in characteristic zero.

## What is not known

No current source proves:

- normal or log smooth crossing for every closure of an ordered-composition
  cell;
- the noncoprime triple-overlap theorem;
- homogeneous subresultant descent, including line-bundle characters and
  stabilizers, over the universal logarithmic root expansion;
- extension of the relative-Jacobian marking and fixed-frame Torelli across
  every block merge;
- equality with logarithmic Quot; or
- recovery of the affine opening merely from the finite graph closure.

## Exact live problem

Prove the adjacent-block-merge theorem.  Start with one three-block
composition in which two successive merges have a nonunit common factor.
Write both normalized chart rings, resolve the Desnanot--Jacobi pivot by an
explicit weighted modification, and compare the two iterated transitions on
the triple overlap.  The result should either prove the existing PRS atlas is
closed under the merge or identify the additional logarithmic blowup needed.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P4-L2A — Noncoprime adjacent merge

Actor: `online_model`. Status: ready.

Give exact chart equations, normalizations, exceptional divisors, and the
map to the coarse inverse graph for the smallest genuinely noncoprime merge.

### P4-L2B — Triple-overlap cocycle

Actor: `online_model`. Status: blocked on P4-L2A.

Compare both merge orders, including transfer matrices, subresultant
coordinates, and stabilizer characters.

### P4-L2C — Boundary marking and affine opening

Actor: `online_model`. Status: blocked on the atlas theorem.

Transport the relative-Jacobian decoration and state exactly which deleted
boundary divisors recover the affine source.

## Do not do

- Do not identify the fractional-Rees graph with the common-factor tower.
- Do not use every Bruhat cell when the exact Euclidean cells suffice.
- Do not infer global log smoothness from toroidality of individual charts.
- Do not call the opening reconstructed unless the deleted boundary and its
  overlap data are part of the theorem.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.

[Back to the portfolio hub](state-of-the-program.md)
