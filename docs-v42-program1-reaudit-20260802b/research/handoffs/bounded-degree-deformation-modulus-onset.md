---
title: "Model research brief — Bounded-degree deformation and modulus onset"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 3</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v15 · site release <code>living-guide-public-v42-program1-reaudit</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 3: Bounded-degree deformation and modulus onset

## Research objective

Relate the exact degree-seven local algebra of the named map to the first
appearance of genuine stable moduli, and finish the sharply reduced
degree-eight orbit-saturation calculation.  A conceptual explanation of why
rigidity breaks would be more valuable than a list of unrelated rank tests.

This lane overlaps [Program 3](local-rigidity-and-deformation-algebra.md) and
[Program 4](stable-moduli.md).  The newest exact units are the
[two order-six lower-jet exclusions](../working-mathematics/units/RMU-3D8E0001.md)
and the [five-variable universal reduction](../working-mathematics/units/RMU-3D8E0002.md).

## Reusable mathematics

In the normalized degree-at-most-seven coefficient scheme, an eleven-condition
affine slice transverse to the source orbit has a length-584 completed Artin
algebra.  Its Hilbert function is

```text
(1,10,44,108,157,145,86,30,3),
```

its maximal ideal has nilpotence index nine, and its Cohen--Macaulay type is
60.  Torus attractors and the fixed locus prove reduced isolation in the
bounded transverse germ.  This does not exclude degree-increasing families or
known degree-eight source and target shear components.

At the selected exceptional first-normal direction in degree eight, the full
exact characteristic-zero order-six systems at two lower jets—the base and
`c_0=1`—have unit obstruction ideal after all 24 order-five bendings are
included.  Over `F_1000033`, the complete 22-parameter lower-jet calculation
has a fixed 24-dimensional order-five kernel.  All lower-order correction
columns lie in one fixed five-dimensional image, and projection to its
three-dimensional cokernel produces three polynomials in only

```text
c_14, c_19, c_26, t_8, t_15.
```

The corrected universal assembly reproduces all 325 base columns.  An earlier
assembly overflowed because a negative determinant sign was represented as
`p-1` before integer multiplication; do not reuse that version.

The fixed-image containment is proved only modulo `1000033`.  Rank five has
not been proved everywhere, the three polynomials are not yet known to
generate the unit ideal universally, and the result is not a global
degree-eight theorem.

## High-priority next calculations

1. Reduce three suitable columns of the universal matrix modulo the fixed
   two-dimensional tangent image and compute a `3 x 3` determinant
   `Delta_H(c_14,c_19,c_26)`.  A nonzero constant proves constant rank;
   factors give the exact rank-drop strata.
2. Form the `3 x 6` coefficient matrix of the three obstruction polynomials
   against `1,t_8,t_15,t_8^2,t_8*t_15,t_15^2` and find a unit minor or its
   factorization.
3. Reconstruct the sparse identities at several good primes and verify them
   directly over `Q`.
4. Repeat only on the resulting exceptional divisors, then cover the other
   first-normal strata and the quadratic source-shear parameter.
5. Add target-shear and source/target intersection components before making an
   orbit-saturation statement.

In parallel, complete the source-flow/determinant comparison at orders five
through eight and relate the surviving character sectors to the Program 4
`q`-modulus.  The newest tangent packet has rank 439, nullity 44, and a
28-dimensional residual character; an older claim that only weights `-2,-1`
remain is not current.

## Useful deliverable

The immediate theorem-facing result is a characteristic-zero unit certificate
or a finite stratification of its failure locus.  Keep the bounded-degree,
affine-quotiented scope explicit.  A new deformation-theoretic explanation
that replaces the remaining matrix calculations is encouraged; say precisely
which shear and quotient directions it includes.

[Back to the portfolio hub](state-of-the-program.md)
