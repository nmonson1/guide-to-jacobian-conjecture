# Lane 2: Boundary completeness and Torelli at infinity

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

with multiplicity `d_j`. Hence at most `2^(m-1)` Euclidean cells occur.
Unit: [`RMU-4D2E0001`](../working-mathematics/units/RMU-4D2E0001.md).

The normalized graph of the complete projective PRS is finite type,
projective, separated, and birational over the strongly regular locus. On an
exact composition chart its outer inverse graph is the normalized blowup of
an explicit monomial ideal and is toroidal. PRS transfer matrices compose
strictly, so the cocycle where pivots are coprime is literal associativity.
Unit: [`RMU-4D2E0002`](../working-mathematics/units/RMU-4D2E0002.md). Context: [`manuscripts/04-stable-moduli/main.tex`](../proof-sources/04-stable-moduli/main.md) and
the exact statements and support boundaries on the two unit pages.

No standalone public proof body currently supplies the PRS theorem. Treat
the units as recorded structural inputs, not as a black-box global atlas
theorem: the chartwise conclusions and their limitations are exact, while
the noncoprime closure comparison below is to be proved from the definitions.

Exact checks include the one-root graph `Bl_(epsilon^(N+2),y)`, the
`Bl_(u^2,v)` difference between direct and ordered `N=3` charts, and a
coprime triple cocycle. None treats a genuinely noncoprime triple overlap.

## Exact live problem

The source record does not fix enough pseudo-remainder, pivot, and transfer-
matrix conventions to make a concrete noncoprime PRS chart canonical. That
calculation is therefore blocked. The ready problem is the following abstract
adjacent-block model, which is independent of those missing conventions.

Let `k` be a characteristic-zero field, let `A=k[x,y,z]`, and fix positive
integers `a,b,c,d`. Put

```text
I=(x^a,y^b),             J=(y^c,z^d).
```

For a monomial ideal `K`, write

```text
NB(K)=Proj_A(overline( direct_sum_(n>=0) K^n*t^n ))
```

for its normalized blowup. Define `X_(I,J)` by pulling `J` to `NB(I)`,
removing its invertible exceptional factor, blowing up the remaining weak
transform, and normalizing; define `X_(J,I)` symmetrically. The simultaneous
linearity fan is the subdivision of the positive octant into the domains on
which both functions

```text
min(a*u_x,b*u_y),        min(c*u_y,d*u_z)
```

are linear. Determine the toric morphisms from this simultaneous refinement
to `X_(I,J)` and `X_(J,I)`, their exceptional valuations, and exactly when the
two ordered normalized blowups are isomorphic. This is the local toric
adjacent-block theorem needed before a PRS-specific noncoprime comparison can
be stated honestly.

## Tasks and deliverables

### P4-L2A0 — Abstract adjacent-block theorem

Status: ready.

Inputs: the displayed ring, monomial ideals, normalized-blowup convention,
and simultaneous-linearity fan. No unpublished PRS convention is used.

Deliverable: the fans and affine semigroup rings of both ordered blowups, the
minimal common toric refinement, all exceptional divisorial valuations, and
an if-and-only-if criterion in `a,b,c,d` for the two orders to agree. Explain
which conclusion survives after replacing the monomial ideals by ideals with
the same integral closures.

### P4-L2A — Quantified noncoprime adjacent-merge theorem

Status: blocked until the PRS pseudo-remainder normalization, pivot ideals,
transfer matrices, and closure convention are isolated as public inputs.

Inputs: those future PRS inputs, the toric template from P4-L2A0, and the
structural statements on [`RMU-4D2E0001`](../working-mathematics/units/RMU-4D2E0001.md) and [`RMU-4D2E0002`](../working-mathematics/units/RMU-4D2E0002.md).

Deliverable: the weighted pivot modification, exceptional divisors, and
morphisms to the coarse inverse graph for arbitrary adjacent block sizes and
common-factor valuation.

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
