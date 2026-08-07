---
title: "The Jacobian conjecture"
description: "What the classical conjecture said, why the Jacobian condition is local, and what remains open after 2026."
---

# The Jacobian conjecture

Let

\[
F=(F_1,\ldots,F_n)\colon \mathbf C^n\longrightarrow\mathbf C^n
\]

be a polynomial map. Its Jacobian matrix \(DF\) records the first-order
change of the output when the input moves. If \(\det DF\) never vanishes,
the inverse-function theorem gives a local inverse near every point.

The classical conjecture asked whether this local condition forces a single
global polynomial inverse:

> **Classical Jacobian conjecture.** If \(\det DF\) is a nonzero constant,
> then \(F\) is a polynomial automorphism.

The words *nonzero constant* are not an extra restriction over \(\mathbf C\):
if the determinant of a polynomial Jacobian never vanishes, it is already a
nonzero constant.

## Why the question was plausible

An everywhere-invertible derivative rules out ordinary folding and
ramification. In one variable it settles the problem immediately: a
polynomial with nonzero constant derivative is linear. Many important
special classes in higher dimensions are also known to be invertible.

What the derivative does **not** control is behavior at infinity. Distinct
points can have the same image without a finite critical point if sheets of
the map separate and reconnect through infinity. That is precisely the
loophole used by the three-dimensional counterexample.

## The status now

- The conjecture is **false for every \(n\ge 3\)**: take the explicit
  three-dimensional counterexample and add unused coordinates.
- The conjecture is **open for \(n=2\)**.
- It is true for \(n=1\).

So there is no longer one Jacobian conjecture with a uniform yes-or-no
answer. There is a solved negative problem in dimensions at least three and
a surviving plane problem with its own geometry.

[See the counterexample](counterexample.md){ .md-button .md-button--primary }
[Continue to the plane case](../background/plane-case.md){ .md-button }

## Sources

- [Ott-Heinrich Keller, “Ganze Cremona-Transformationen” (1939)](https://doi.org/10.1007/BF01695502)
- [Unbylined Ulam technical note on the 2026 counterexample](https://www.ulam.ai/research/jacobian.pdf)
- [Lázaro Orlando Rodríguez Díaz, “On the origin of the Jacobian conjecture” (2026)](https://doi.org/10.5802/crmath.831)
