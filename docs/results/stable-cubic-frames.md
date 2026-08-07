---
title: "A stable classification of a family of cubic frames"
description: "A one-parameter modulus of three-sheeted Keller openings survives arbitrary stabilization."
---

# A stable classification of a family of cubic frames

!!! info "Reading level"
    This is a specialist classification theorem. The first section explains
    the invariant geometrically; the exact family and equivalence relation
    are stated next.

## What is true and why

The first counterexample sits inside a two-parameter family of
three-sheeted Keller maps. One might expect the parameters to disappear
after polynomial coordinate changes or after adding unused variables. They
do not. A number \(q\) is recoverable from how the singular discriminant
component meets the plane at infinity, so it survives arbitrary
stabilization.

## Precise result

For

\[
A_\alpha(c)=c+\alpha c^2,
\qquad
B_{\alpha,\beta}(c)=-2-4\alpha c+\beta c^2,
\]

let \(G_{\alpha,\beta}\) be the associated cubic-frame Keller map. Every
member has determinant \(-2\), generic degree three, and is nonproper.

The stable polynomial left–right equivalence classes are

\[
\{\mathcal O_0\}\;\sqcup\;\{\mathcal O_q:q\in\mathbf C\},
\]

where

\[
\mathcal O_0=\{G_{0,\beta}:\beta\in\mathbf C\},
\qquad
\mathcal O_q=
\{G_{\alpha,\beta}:\alpha\ne0,\ \beta/\alpha^2=q\}.
\]

Thus two nonzero-\(\alpha\) members are stably equivalent exactly when their
values of \(q=\beta/\alpha^2\) agree; adding identity variables creates no
new equivalences.

## Why the invariant works

After normalizing \(\alpha=1\), the reduced nonproperness divisor is a plane
plus a singular component. Normalize the singular component. Two marked
curves remain: one coming from its singular locus, the other from its
intersection with the plane. Any automorphism of an affine cylinder
preserving this marked pair must preserve \(q\). Because normalization
commutes with adding affine-space factors, the same argument detects \(q\)
after stabilization.

At \(q=-2\), the singular component meets the plane singularly; this
intrinsic event separates the exceptional orbit.

## What it does not prove

This classifies the displayed quadratic cubic-frame family, not all
degree-three Keller maps and not all finite three-sheeted openings.

## Proof source and status

- [Working manuscript source, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/04-stable-moduli/main.tex)
- [Working manuscript PDF, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf)

This is a theorem of the project, authored by Nathaniel Monson. The linked
working manuscript contains the proof and exact checks; it is not presented
as journal peer review.
