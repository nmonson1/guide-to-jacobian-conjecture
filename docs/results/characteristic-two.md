---
title: "Huq-Kuruvilla and Mondello (July 2026): the separable conjecture fails in characteristic two"
description: "Explicit generic-degree-three counterexamples in characteristic two, first in dimension three and then in the plane."
---

# Huq-Kuruvilla and Mondello (July 2026): the separable conjecture fails in characteristic two

<p class="byline">Three-dimensional construction by Irit Huq-Kuruvilla,
23 July · plane construction by Romy Mondello, 29 July</p>

## What is true and why

In positive characteristic, the naive Jacobian statement has obvious
inseparable failures: derivatives cannot see \(p\)-th powers. A standard
repair asks that the induced function-field extension be separable, often
also requiring its degree to be prime to the characteristic. These examples
show that even this repair fails in characteristic two—and it already fails
in two variables.

## Precise results

Huq-Kuruvilla constructed an explicit map
\(F\colon\mathbf A_k^3\to\mathbf A_k^3\) over any field \(k\) of
characteristic two with Jacobian determinant one, a separable function-field
extension of degree three, and a collision. Stabilization gives examples in
all dimensions at least three.

Mondello then gave the plane map over \(k=\overline{\mathbf F}_2\)

\[
\begin{aligned}
P&=x+x^2y+x^4+x^6y^2,\\
Q&=y+x^5+x^6y+x^7y^2+x^8y^3.
\end{aligned}
\]

It has Jacobian determinant one, and \((0,1)\), \((1,0)\), and \((1,1)\)
have the same image. Moreover
\([k(x,y):k(P,Q)]=3\), and the extension is separable.

## Discussion

Because \(3\) is prime to \(2\), these are not Frobenius artifacts. Mondello
derives the plane map from a coordinate-permuted form of Huq-Kuruvilla's
three-variable example and proves its degree using a hidden cubic and an
irreducibility argument over the actual target field.

This does **not** affect the characteristic-zero plane conjecture. It does
show that a positive-characteristic transfer argument must preserve much
more than separability and generic degree.

## Sources

- [Irit Huq-Kuruvilla, arXiv:2607.20968](https://arxiv.org/abs/2607.20968)
- [Romy Mondello, arXiv:2608.02634](https://arxiv.org/abs/2608.02634)
