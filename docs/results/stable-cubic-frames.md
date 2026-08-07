---
title: "Infinitely many stably inequivalent cubic-frame families"
description: "A one-parameter modulus of three-sheeted Keller openings survives arbitrary stabilization."
---

# Infinitely many stably inequivalent cubic-frame families

<p class="dek">A boundary invariant distinguishes a continuum of
three-sheeted counterexample families even after arbitrary stabilization.</p>

!!! info "Technical subtitle"
    Stable classification of a quadratic family of cubic frames.

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

The stable polynomial left--right equivalence classes are

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

## Why it matters

The theorem shows that the first counterexample is not a single isolated
formula wearing many coordinate disguises. Even within one controlled
three-sheeted construction, genuinely different stable polynomial types
remain. The boundary at infinity detects distinctions invisible in the
generic degree alone.

## What it does not prove

This classifies the displayed quadratic cubic-frame family, not all
degree-three Keller maps and not all finite three-sheeted openings.

## Public proof route

- [Working manuscript source, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/04-stable-moduli/main.tex) — theorem statements and proof source.
- [Working manuscript PDF, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/04-boundary-rigidity-stable-moduli-2026-07-29-v13.pdf) — reader-facing snapshot dated 29 July 2026.

This is a theorem claimed in the linked project manuscript, authored by
Nathaniel Monson. Its appearance in the guide is not a separate independent
verification of that proof.
