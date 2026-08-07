---
title: "A modulus at infinity survives stabilization"
description: "A one-parameter family of three-sheeted Keller openings remains distinct after arbitrary polynomial coordinate changes and added identity variables."
---

# A modulus at infinity survives stabilization

<p class="byline">A project theorem of Nathaniel Monson</p>

The first counterexample lies in a two-parameter family of three-sheeted
Keller maps. At the level of formulas, the parameters look vulnerable: one
can change source and target coordinates and append as many unused variables
as desired. Boundary geometry shows that one parameter survives every such
operation.

## The family

Set

\[
A_\alpha(c)=c+\alpha c^2,
\qquad
B_{\alpha,\beta}(c)=-2-4\alpha c+\beta c^2,
\]

and let \(G_{\alpha,\beta}\) be the associated cubic-frame Keller map. Every
member has determinant \(-2\), generic degree three, and a nonproperness
boundary inherited from the marked-cubic construction.

For \(\alpha\ne0\), rescaling normalizes \(\alpha\) and leaves the ratio

\[
q=\frac{\beta}{\alpha^2}.
\]

The question is whether a more general polynomial equivalence—or a stable
equivalence after adding identity coordinates—can erase \(q\).

## The classification

The stable polynomial left--right equivalence classes are

\[
\{\mathcal O_0\}\;\sqcup\;\{\mathcal O_q:q\in\mathbf C\},
\]

where

\[
\mathcal O_0=\{G_{0,\beta}:\beta\in\mathbf C\}
\]

and

\[
\mathcal O_q=
\{G_{\alpha,\beta}:\alpha\ne0,\ \beta/\alpha^2=q\}.
\]

Thus two members with nonzero \(\alpha\) are stably equivalent exactly when
their values of \(q\) agree. Adding affine-space factors creates no new
equivalences.

## How the boundary reads \(q\)

After normalizing \(\alpha=1\), the reduced nonproperness divisor consists of
a plane and a singular component. Normalize the singular component. Two
marked curves remain:

- the preimage of its singular locus;
- the intersection with the plane component.

Their relative position determines \(q\). Any automorphism of the normalized
affine cylinder preserving this marked pair must preserve that parameter.
Normalization commutes with adjoining affine-space factors, so the same
configuration remains visible after stabilization.

At \(q=-2\), the singular component meets the plane singularly. This intrinsic
change identifies the exceptional member without referring to the original
coefficients.

<div class="mental-model" markdown>

**Why stabilization cannot help.** Adding unused variables thickens every
boundary component by an affine-space factor. The marked intersection pattern
that stores \(q\) is still present in each fiber.

</div>

## What the invariant currently classifies

The classification applies to the displayed quadratic cubic-frame family and
to stable polynomial left--right equivalence. It provides a concrete modulus
for three-sheeted Keller openings and a test case for any proposed intrinsic
classification. Extending the invariant beyond this family is a separate
problem.

[Proof, computation, and status](evidence-ledger.md#a-modulus-at-infinity){ .evidence-link }
