---
title: "A transverse local algebra of length 584"
description: "The fixed degree-seven counterexample is reduced-isolated in a bounded slice and surrounded by a precisely computed nilpotent neighborhood."
---

# A transverse local algebra of length 584

<p class="byline">An exact computer-assisted project theorem of Nathaniel
Monson</p>

A point can be isolated after reduction and still carry many infinitesimal
directions. That is what happens to the fixed counterexample inside one
normalized degree-at-most-seven coefficient scheme.

The reduced geometry is a single point. Around it sits a nilpotent
neighborhood of length \(584\).

## The deformation slice

Begin with polynomial maps of degree at most seven satisfying the Keller
equations. Quotient by a normalized affine source action and choose a
transverse slice through the fixed map.

Before the Keller equations are imposed, this affine slice has dimension
\(337\). At the counterexample, its Zariski tangent space has dimension ten.
The completed local ring has a Kuranishi presentation

\[
R\cong\mathbf C[[u_1,\ldots,u_{10}]]/I.
\]

The exact calculation gives

\[
\operatorname{length}R=584,
\qquad
\mathfrak m^9=0\ne\mathfrak m^8.
\]

Its Hilbert--Samuel function is

\[
(1,10,44,108,157,145,86,30,3).
\]

The Kuranishi ideal has 36 minimal generators: 11 quadratic, 13 cubic, 11
quartic, and one sextic. The Macaulay inverse system has 60 minimal
contraction generators. In particular, \(R\) is neither Gorenstein nor level.

## What the number measures

The reduced point says that no actual nearby family appears in this chosen
bounded-degree slice. The ten tangent directions are first-order motions that
survive the linearized equations. Higher-order equations successively obstruct
them, leaving a finite nonreduced local scheme.

The length \(584\) is the scheme-theoretic multiplicity of that infinitesimal
neighborhood. The slice has no other reduced points. The number measures the
nilpotent thickness concentrated at the fixed map.

<div class="mental-model" markdown>

**A useful picture.** The counterexample is an isolated point surrounded by a
thick cloud of infinitesimal motions. The local algebra has nonzero terms
through order eight and none in order nine.

</div>

## How the exact calculation closes

The computation constructs the Kuranishi equations over \(\mathbf Q\), then
uses two complementary descriptions of the local algebra.

1. The inverse-system calculation determines all dual classes through degree
   eight and proves that no degree-nine class survives.
2. A border basis supplies \(584\) standard monomials and ten commuting
   rational multiplication matrices.

The first route gives the upper structure of the dual space. The second gives
a finite exact algebra of the same length and checks the lower bound from the
opposite direction. Agreement between the two presentations is the central
certificate.

## What remains open

The theorem concerns one degree bound, one affine quotient, and one transverse
slice. A coordinate change of unbounded degree or a deformation through maps
of higher degree lies outside this local model.

The broader question is whether an intrinsic deformation theory of the finite
cover and its boundary explains this nilpotent algebra and compares it with
unrestricted polynomial equivalence.

[Proof, exact supplement, and status](evidence-ledger.md#the-length-584-local-algebra){ .evidence-link }
