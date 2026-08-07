---
title: "A cubic-homogeneous counterexample in 24 variables"
description: "William Thompson's explicit counterexample in the classical normal form U plus a homogeneous cubic map."
---

# A cubic-homogeneous counterexample in 24 variables

<p class="byline">Construction, exact certificate package, and verifier
programs by William Thompson · 21 July 2026</p>

Classical reduction theorems made maps of the form

\[
G(U)=U+H(U),
\]

with \(H\) homogeneous cubic, central to the Jacobian conjecture. Before the
counterexample, this normal form concentrated the general problem into a
highly structured class. Thompson showed that the new failure survives the
reduction explicitly.

## Why the normal form matters

For \(G=I+H\) with \(H\) homogeneous cubic, the Jacobian matrix is

\[
DG=I+DH,
\]

and \(DH\) is homogeneous quadratic. Scaling \(U\) by \(\lambda\) scales
\(DH(U)\) by \(\lambda^2\). Hence the identity
\(\det(I+DH)=1\) gives

\[
\det(I+tDH(U))=1
\]

for every \(t\in\mathbf C\). The nonconstant coefficients of this determinant
are the elementary symmetric functions of the eigenvalues of \(DH(U)\); all
of them vanish, so \(DH(U)\) is nilpotent. Cubic-linear reductions and
connections with Hessian maps are now visible directly in the coordinates.

The normal form is therefore more than a degree bound. It is the coordinate
language in which much of the classical theory was developed.

## The 24-variable map

There is an explicit polynomial map

\[
G(U)=U+H(U)\colon\mathbf Q^{24}\longrightarrow\mathbf Q^{24}
\]

such that every nonzero component of \(H\) is homogeneous of degree three,

\[
\det DG=1,
\]

and two displayed distinct rational points have the same image. The map has
54 nonzero cubic monomials.

The determinant and collision are certified by exact arithmetic and verifier
programs. Thus the counterexample lies inside the strict cubic-homogeneous
class used by the Bass--Connell--Wright and Yagzhev reductions.

## What becomes possible

A concrete normal-form example can be used as a test object for questions
that were previously posed only under the conjectural assumption that every
such map was invertible. One can now examine:

- the nilpotent structure of \(DH\);
- further cubic-linear compression;
- minimal dimension in cubic-homogeneous form;
- stable equivalence between different reductions;
- consequences for neighboring Hessian and unipotent-Jacobian problems.

The dimension \(24\) is an upper bound produced by this construction. Smaller
cubic-homogeneous presentations may exist, and their minimum dimension is a
natural framing problem.

[Proof, sources, and verification](evidence-ledger.md#the-24-variable-cubic-homogeneous-map){ .evidence-link }
