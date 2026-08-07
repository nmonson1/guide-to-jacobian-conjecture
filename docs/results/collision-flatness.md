---
title: "When collisions detect a hidden flatness defect"
description: "For a three-sheeted Keller opening, one saturation failure in the collision complex measures exactly the nonflatness of the finite normalization."
---

# When collisions detect a hidden flatness defect

!!! info "Reading level"
    The first two sections explain the geometry. The exact statement uses
    local cohomology, Matlis duality, and the standard representation of
    \(S_3\).

## What is true and why

A Keller map is étale on affine space, but its finite normalization can contain
points that are missing from the affine source. At such an omitted target
value, the finite cover need not be flat even though the actual polynomial map
has no critical point.

For a generic three-sheeted opening with monodromy \(S_3\), pass to the
normalized Galois closure. There are three conjugate copies of the source
opening, one for each choice of marked sheet. Their pairwise overlaps are the
off-diagonal collision spaces: pairs of distinct source points with the same
image. Their triple overlap records ordered triples of distinct points in one
fiber.

These overlaps form a small Čech complex. A class in its first cohomology can
look harmless away from the omitted value while surviving only at that point.
The theorem says that this punctual failure is not merely analogous to
nonflatness: it is exactly the dual of the flatness defect, with the natural
\(S_3\)-representation attached.

## Precise result

Let \(A\) be the local ring of the target at an omitted value \(y\), let
\(B\) be the corresponding cubic normalization, and put

\[
\Delta_y=\operatorname{Ext}^1_A(B,A).
\]

Let

\[
C_y^0\xrightarrow{d_0}C_y^1\xrightarrow{d_1}C_y^2
\]

be the collision Čech complex on the three conjugate source openings. Write

\[
K_y=\ker d_1,
\qquad I_y=\operatorname{im}d_0,
\qquad
I_y^{\mathrm{sat}}=I_y:_{K_y}\mathfrak m_y^\infty.
\]

Then

\[
\boxed{
I_y^{\mathrm{sat}}/I_y
\simeq
D_A(\Delta_y)\otimes_{\mathbf C}V_{\mathrm{std}},
}
\]

where \(D_A\) is Matlis duality and \(V_{\mathrm{std}}\) is the
two-dimensional standard representation of \(S_3\). Consequently,

\[
B\text{ is flat over }A
\quad\Longleftrightarrow\quad
I_y^{\mathrm{sat}}=I_y,
\]

and

\[
\operatorname{length}(I_y^{\mathrm{sat}}/I_y)
=2\operatorname{length}(\Delta_y).
\]

## Why the collision complex knows this

On the Galois closure, the Čech complex computes local cohomology at the part
of the boundary missed by all three source charts. The normalized algebra has
an \(S_3\)-isotypic decomposition

\[
T\simeq A\oplus A_{\mathrm{sgn}}
\oplus(E\otimes V_{\mathrm{std}}),
\qquad B\simeq A\oplus E.
\]

The trivial and sign pieces are free. The only punctual contribution comes
from \(E\), and local duality turns that contribution into
\(D_A\operatorname{Ext}^1_A(E,A)\). This is the displayed formula.

The representation factor matters: the collision complex sees the defect
through the three conjugate markings, not as an unlabelled scalar.

## A useful calibration

The fixed marked-root counterexample has a finite-flat cubic normalization,
so its saturation quotient vanishes. Near its ordinary triple-root curve, the
three chart-boundary functions generate \((u,v)^2\), but that visible triple
collision still produces no punctual saturation defect.

Thus “three sheets meet in the compactification” and “the finite
normalization is nonflat” are different statements. The theorem measures the
second one.

## What it does not prove

This does not prove that every cubic Keller normalization is flat. It gives an
exact detector in the generic-degree-three, \(S_3\) setting. Extending the
collision-nerve mechanism to higher degree or proving that the detected defect
must always vanish are separate problems.

## Proof source and status

The canonical theorem is recorded in the project contribution
`contributions/collision-saturation.md`; its full proof is routed to the
Lane-1 collision-saturation research note and exact computation package. A
stable public proof bundle has not yet been linked from this guide. This page
states the theorem and its proof architecture; it is not a substitute for
that source release.

[See the cover-and-collision research front](../fronts/cover-and-collision.md){ .md-button }
