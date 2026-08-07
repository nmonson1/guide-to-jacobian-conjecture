---
title: "The separable conjecture fails in characteristic two"
description: "Explicit generic-degree-three counterexamples in characteristic two, first in dimension three and then in the plane."
---

# The separable conjecture fails in characteristic two

<p class="byline">Three-dimensional construction by Irit Huq-Kuruvilla,
23 July 2026 · plane construction by Romy Mondello, 29 July 2026</p>

Positive characteristic changes the meaning of the Jacobian condition. The
derivative cannot see \(p\)-th powers, so maps involving Frobenius give
immediate inseparable failures. A natural repair is to require the induced
function-field extension to be separable, often with degree prime to the
characteristic.

Characteristic two defeats that repair as well.

## Why separability looked promising

For a dominant map \(F\colon\mathbf A^n_k\to\mathbf A^n_k\), a nonzero
Jacobian determinant implies that the induced extension of function fields is
separable. Requiring separability removes the most obvious Frobenius
pathologies and restores much of the differential intuition familiar from
characteristic zero.

One might therefore hope that a separable Keller map of degree prime to
\(p\) has the global rigidity of a finite étale cover. The new examples
remain étale at finite points while losing properness at infinity.

## Two explicit counterexamples

Huq-Kuruvilla constructed a map

\[
F\colon\mathbf A_k^3\longrightarrow\mathbf A_k^3
\]

over every field \(k\) of characteristic two with Jacobian determinant one,
a separable function-field extension of degree three, and an explicit
collision. Stabilization gives examples in all dimensions at least three.

Mondello then produced the plane map over
\(k=\overline{\mathbf F}_2\):

\[
\begin{aligned}
P&=x+x^2y+x^4+x^6y^2,\\
Q&=y+x^5+x^6y+x^7y^2+x^8y^3.
\end{aligned}
\]

It satisfies

\[
\det D(P,Q)=1,
\]

and the three points

\[
(0,1),\qquad(1,0),\qquad(1,1)
\]

have the same image. Moreover,

\[
[k(x,y):k(P,Q)]=3,
\]

and the extension is separable. The striking number is three: it is prime to
two, so the ordinary Frobenius mechanism cannot account for the sheets.

## What characteristic two teaches

Mondello derives the plane example from a coordinate-permuted form of the
three-variable construction and proves its degree through a hidden cubic and
an irreducibility argument over the actual target field. The same global
mechanism appears again: local differential regularity coexists with several
sheets and nonproper behavior.

The characteristic-zero plane problem remains separate; its compactification
and arithmetic constraints are different. The positive-characteristic
examples show, however, that a transfer argument must control the boundary
geometry itself. Separability and generic degree alone carry too little
global information.

[Proof, sources, and verification](evidence-ledger.md#characteristic-two-counterexamples){ .evidence-link }
