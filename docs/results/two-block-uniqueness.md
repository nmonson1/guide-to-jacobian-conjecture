---
title: "Why the cubic two-block chart is uniquely affine"
description: "Among tangent two-block multiplication-incidence opens, only the cubic linear-times-quadratic chart becomes affine space, even after stabilization."
---

# Why the cubic two-block chart is uniquely affine

!!! info "Reading level"
    The first section explains the recognition problem geometrically. The
    precise theorem uses divisor class groups, contact order, and
    Hodge–Deligne polynomials.

## What is true and why

The marked-cubic construction multiplies a linear binary form by a quadratic
one, then removes two bad loci: the resultant divisor, where the factors share
a root, and the pullback of a hyperplane tangent to the rational normal curve.
For one particular tangency, the remaining incidence space is
\(\mathbf A^3\).

The same recipe works formally for block sizes \((a,b)\). Most of the
resulting open varieties are not affine space, even after multiplying by an
unused affine-space factor. The theorem shows that the successful cubic chart
is not one lucky member of a large hidden family: it is the unique stably
affine case in the entire tangent two-block construction.

## Precise result

Let \(V_d\) be the vector space of binary forms of degree \(d\), and consider

\[
\mu_{a,b}\colon
\mathbf P(V_a)\times\mathbf P(V_b)
\longrightarrow\mathbf P(V_{a+b}),
\qquad ([L],[Q])\longmapsto[LQ].
\]

Delete the resultant divisor and the pullback of a hyperplane \(H\) tangent
to the rational normal curve. Let \(m(H)\ge2\) be its contact order, and call
the resulting open \(U_{a,b,H}\).

Then

\[
\boxed{
U_{a,b,H}\times\mathbf A^r
\simeq\mathbf A^{a+b+r}
\quad\Longleftrightarrow\quad
\{a,b\}=\{1,2\}\text{ and }m(H)=2.
}
\]

The surviving case is already \(\mathbf A^3\) without stabilization.

## Why the other cases fail

The proof uses three different obstructions, each adapted to a different
part of the family.

1. The two deleted divisors have classes \((b,a)\) and \((1,1)\). Their
   quotient in the class group rules out nonadjacent block sizes.
2. For larger adjacent blocks, a codimension-two deficit in the
   Hodge–Deligne polynomial survives multiplication by every affine-space
   factor. This handles the nonosculating and almost-osculating cases.
3. In the fully osculating case, the resultant becomes a nonconstant unit on
   the open. A stabilization of affine space has no such unit.

For \((a,b)=(1,2)\) and contact order two, an explicit coordinate
trivialization identifies the open with \(\mathbf A^3\), including the
retained section at infinity.

The argument is scheme-theoretic; it does not assume that the binary forms
have simple roots.

## Why this is a recognition theorem

An abstract finite cubic cover is not enough to produce a Keller map. One
also needs an affine opening isomorphic to polynomial affine space. This
theorem explains why the tangent linear-times-quadratic incidence chart passes
that recognition test and why its natural higher-block analogues do not.

## What it does not prove

This is uniqueness inside the two-block multiplication-incidence
construction. It is not a uniqueness theorem for all cubic Keller
presentations, all affine openings of cubic covers, or all methods of
constructing counterexamples.

## Proof source and status

- [Pinned cubic-incidence manuscript source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/01-cubic-incidence/main.tex)
- [Pinned cubic-incidence manuscript PDF](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/01-cubic-marked-root-covers-2026-07-29-v13.pdf)

The pinned manuscript proves the central nonosculating theorem. The complete
contact-order statement, including the almost-osculating and fully
osculating endpoints, is recorded in the current project contribution
`contributions/two-block-stable-uniqueness.md` and should be included in the
next public source bundle.
