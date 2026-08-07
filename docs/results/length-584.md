---
title: "A transverse local algebra of length 584"
description: "The bounded degree-seven deformation slice is reduced-isolated but carries a precisely computed nonreduced thickening."
---

# A transverse local algebra of length 584

!!! info "Reading level"
    This is a specialist, computer-assisted result about the local geometry
    of a bounded coefficient scheme. The conceptual point is in the first
    and third sections; the numerical statement uses local algebra.

## What is true and why

To ask whether the fixed counterexample belongs to a nearby family, one must
say which degrees and coordinate changes are allowed. In the scheme of
degree-at-most-seven Keller maps, quotient by the normalized affine source
action and take a transverse slice through the fixed map. The reduced slice
is a single point, but its equations meet there with high multiplicity.

## Precise result

Before imposing the Keller equations, the chosen affine slice has dimension
337. At the fixed map its Zariski tangent space has dimension ten, and the
completed local ring has a Kuranishi presentation

\[
R\cong \mathbf C[[u_1,\ldots,u_{10}]]/I.
\]

Then

\[
\operatorname{length}R=584,
\qquad
\mathfrak m^9=0\ne\mathfrak m^8,
\]

and its Hilbert–Samuel function is

\[
(1,10,44,108,157,145,86,30,3).
\]

The Macaulay inverse system has 60 minimal contraction generators. The
Kuranishi ideal has 36 minimal generators: 11 quadratic, 13 cubic, 11
quartic, and one sextic. In particular, \(R\) is neither Gorenstein nor
level.

## What the number means

The reduced point says there is no genuine nearby family in this normalized
bounded-degree slice. The nilpotents record infinitesimal deformations that
survive for several orders before the equations obstruct them. The number
584 is the scheme-theoretic transverse multiplicity—not a count of nearby
maps and not a global count of counterexamples.

## Proof architecture

The calculation constructs the Kuranishi equations exactly over
\(\mathbf Q\), determines the inverse system through degree eight, and
proves that no degree-nine dual class exists. A border basis with 584
standard monomials and ten commuting rational multiplication matrices gives
a finite exact presentation and checks the lower-bound calculation from the
opposite direction.

## What it does not prove

The result is local, degree-bounded, and relative to a specified affine
quotient and slice. It does not say that the counterexample is isolated under
arbitrary polynomial equivalence or among maps of unbounded degree.

## Proof source and status

- [Working manuscript source, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/03-local-rigidity/main.tex)
- [Working manuscript PDF, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/03-filtered-rigidity-2026-07-29-v13.pdf)
- [Exact computational supplement, pinned ZIP](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/docs-v56-converged-research-20260804j/assets/technical-materials/03-local-rigidity-computational-supplement.zip)

This is an exact computer-assisted theorem of the project, authored by
Nathaniel Monson. The linked manuscript states the slice conventions and
certificate contract. In the ZIP, begin with `COMPUTATION.md`; the independent
border-basis replay is documented in
`code/border-basis/REPRODUCIBILITY.md`. This is not presented as journal peer
review.
