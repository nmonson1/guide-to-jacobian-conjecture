---
title: "Cubic-homogeneous counterexamples: from 24 variables to 19"
description: "The counterexample reaches the classical cubic-homogeneous normal form, first explicitly in 24 variables and now in 19."
---

# Cubic-homogeneous counterexamples: from 24 variables to 19

<p class="byline">First explicit 24-variable tensor by William Thompson · a
19-variable endpoint independently announced by Harris Chan · rank-sensitive
19-variable construction and exact tensor recorded by this project</p>

!!! info "Reading level"
    The construction below is a suspension: it introduces variables so that
    every nonlinear term becomes homogeneous cubic while preserving the
    original collision.

## Why this normal form matters

Classical reduction theorems made maps of the form

\[
G(U)=U+H(U),
\]

with every nonzero component of \(H\) homogeneous cubic, central to the
Jacobian conjecture. The new counterexample therefore became substantially
more useful once it was placed inside this strict normal form.

William Thompson first supplied a completely explicit 24-variable example
over \(\mathbf Q\), with determinant one, 54 nonzero cubic monomials, and a
displayed rational collision. That remains an important public benchmark
with independent verifier programs.

## The current 19-variable endpoint

There is also an explicit noninjective cubic-homogeneous Keller map

\[
G=I+H\colon\mathbf A^{19}\longrightarrow\mathbf A^{19}
\]

with rational coefficients. Its generic finite cover still has degree three
and monodromy \(S_3\). For the fixed tensor, the nonlinear Jacobian has
generic Jordan type

\[
(18,1).
\]

A 19-variable endpoint was independently announced by Harris Chan on
23 July 2026. The project's contemporaneous homogeneous-descendants
manuscript records that announcement and gives a rank-sensitive suspension
construction reaching the same dimension, together with an exact tensor and
replay data. The original announcement does not currently have a stable post
URL, so the developments ledger keeps the priority record explicit.

## How the rank-sensitive suspension works

Start with a Keller map

\[
K(X)=X+Q(X)+C(X)
\]

on \(\mathbf A^n\), where \(Q\) and \(C\) are homogeneous of degrees two and
three. Suppose the coordinate span of the cubic part has dimension \(r\), and
write

\[
C=Bq
\]

for a vector \(q=(q_1,\ldots,q_r)\) of cubic forms. Introduce \(r\) variables
\(w\) and one homogenizing variable \(t\), and set

\[
G(X,w,t)=
\bigl(X+tQ(X)+t^2Bw,\;w-q(X),\;t\bigr).
\]

Every nonlinear term is now cubic homogeneous, and

\[
\det JG=\det JK(tX).
\]

A collision \(K(p)=K(p')\) lifts to

\[
(p,q(p),1),\qquad(p',q(p'),1).
\]

For the fixed eleven-variable degree-at-most-three descendant, the cubic
coordinate span has dimension \(r=7\). The suspension therefore uses

\[
11+7+1=19
\]

variables. The saving from 24 to 19 comes from the rank of the cubic part,
not from deleting arbitrary coordinates after the fact.

## How small could a cubic-homogeneous example be?

Let \(N_{\min}\) be the least dimension of a cubic-homogeneous Keller
counterexample. The current retained bounds are

\[
\boxed{5\le N_{\min}\le19.}
\]

The upper bound is the construction above. The lower bound comes from the
classification/no-collision result through dimension four. Nineteen is only
minimal inside the displayed factorized suspension model; it is not known to
be globally minimal.

## Sources and verification

- [Thompson's pinned 24-variable repository](https://github.com/wtho704/explicit-cubic-homogeneous-jacobian-counterexample/tree/45a7616fdf5a20c065564f2676190093722696b9)
- [Thompson's archived release](https://doi.org/10.5281/zenodo.21466221)
- [Harris Chan's X profile](https://x.com/SirrahChan)
- [Pinned homogeneous-descendants manuscript source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/05-homogeneous-descendants/main.tex)
- [Pinned homogeneous-descendants PDF](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscripts-v13/05-homogeneous-descendants-2026-07-29-v13.pdf)

The 24-variable result belongs to Thompson. The site records Chan's earlier
19-variable announcement separately from the project's constructional and
verification claims.
