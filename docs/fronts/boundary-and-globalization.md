---
title: "Reconstructing the map from infinity"
description: "Why global noninvertibility lives at the boundary and what a local-to-global reconstruction theorem would have to prove."
---

# Reconstructing the map from infinity

<p class="dek">A Keller map has no finite branch point that can explain a
collision. Any global failure must be carried by nonproperness, and
compactification turns that failure into boundary geometry.</p>

## The escape mechanism

Let

\[
F\colon X=\mathbf A^n\longrightarrow Y=\mathbf A^n
\]

have constant nonzero Jacobian. Near every finite source point, \(F\) is an
analytic isomorphism. If \(F\) is noninjective, it must also be nonproper:
there is a sequence \(x_k\) escaping to infinity while \(F(x_k)\) remains
bounded.

Choose the finite normalization of the target and write

\[
X\hookrightarrow Z\xrightarrow{\pi}Y,
\qquad
D=Z\setminus X.
\]

Because \(Z\to Y\) is finite and therefore proper, a subsequence of \(x_k\)
converges in \(Z\). Its limit lies in \(D\): the finite cover contains the
point that the affine source has omitted.

<figure class="math-figure">
  <img src="../assets/images/escape-to-infinity.svg" alt="A sequence in the affine source approaching a deleted boundary while its images remain bounded in the target.">
  <figcaption>The finite completion converts escape to infinity into an ordinary limit on the boundary.</figcaption>
</figure>

This is the precise sense in which global noninvertibility lives at infinity.
The boundary records which sheets can leave the affine chart and how they
meet in the finite completion.

## The marked-cubic model

For the first counterexample, \(Z\) is the full marked-root cover and \(D\)
contains the repeated marked roots. The discriminant normalization and the
curves marked by the boundary retain information that survives polynomial
coordinate changes and stabilization.

In a family of cubic-frame openings, this boundary data recovers a modulus
\(q\). Adjoining identity variables adds affine factors to the normalization
and boundary. The marked configuration from which \(q\) is read remains in
every fiber.

The lesson is concrete: a parameter that looks removable in the polynomial
formula may be rigidly recorded by the way boundary components meet.

## From local branches to a global polynomial map

The plane problem begins with valuations and Puiseux branches at infinity.
Their leading terms determine Newton faces, and some face equations produce
Belyi maps and dessins. These are powerful local models of the boundary.

Globalization asks for more. The local branches must fit together on one
compactification, satisfy every later compatibility equation, and arise from
global polynomials \(P\) and \(Q\). A valid leading face can fail at a later
Puiseux layer. Several locally consistent charts can fail to glue. A rational
construction can fail to be polynomial.

The current work below degree \(125\) displays this chain clearly:

\[
\text{global degree reduction}
\longrightarrow
\text{two Newton supports}
\longrightarrow
\text{five leading dessins}
\longrightarrow
\text{terminal compatibility equations}.
\]

Each arrow is a theorem that must preserve every remaining global candidate.

## Where to see the mechanism

- [Discriminants](../ideas/discriminants.md)
- [Normalization](../ideas/normalization.md)
- [Newton--Puiseux expansions](../ideas/newton-puiseux.md)
- [Dessins d'enfants](../ideas/dessins.md)
- [Stable cubic-frame classification](../results/stable-cubic-frames.md)

## The missing local-to-global theorem

The natural theorem would start from a finite collection of boundary data—
valuations, conductors, intersection numbers, local equations, and gluing
maps—and decide whether they determine an affine opening

\[
Z\setminus D\simeq\mathbf A^n
\]

with a polynomial Keller map to \(\mathbf A^n\).

Such a theorem would explain the three-dimensional example intrinsically and
turn plane exclusions into failures of a stated reconstruction criterion.
It would also identify the exact stage at which affineness or polynomiality
enters, making those global conditions visible in the theorem statement. It
would turn “behavior at infinity” from a slogan into a reconstruction
criterion.

