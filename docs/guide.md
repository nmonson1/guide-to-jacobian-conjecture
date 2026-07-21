---
title: The conjecture
description: A concise introduction to the Jacobian conjecture and the local-to-global gap.
---

# The conjecture

Let

\[
F=(F_1,\ldots,F_n):\mathbb C^n\longrightarrow\mathbb C^n
\]

be a polynomial map. Its Jacobian matrix (JF) records all first derivatives.
The classical Jacobian conjecture said:

> If \\(\det JF\\) is a nonzero constant, then \\(F\\) has a polynomial inverse.

Such a map is often called a **Keller map**.

## Why the condition is powerful

The complex inverse function theorem says that a nonzero Jacobian determinant
makes (F) locally invertible. Around every source point, there is a small
neighborhood on which (F) has a holomorphic inverse.

The conjecture tried to promote this local fact to a global algebraic one:

| Scale | What the Jacobian condition supplies |
| --- | --- |
| Infinitesimal | No tangent direction is crushed. |
| Local | Every point has an inverse-function neighborhood. |
| Global | **Not guaranteed:** distant source points can share an image. |
| Algebraic | **Not guaranteed:** there need not be a polynomial inverse. |

The failed implication is therefore not “nonzero derivative implies a local
inverse.” That theorem remains true. The failure is the passage from many
compatible-looking local inverses to one global inverse.

## The role of infinity

The counterexample has no critical points in affine space. Instead, its inverse
branches change when points run out toward infinity. A typical target point has
three preimages. On a certain hypersurface, two of those sheets escape to
infinity; on a special curve, the last finite sheet disappears as well.

This is why **properness** is the right missing global condition. A proper
Keller map cannot lose inverse branches at infinity and is a polynomial
automorphism. The new example is not proper.

## Dimension by dimension

- In dimension one, the statement is elementary: constant nonzero derivative
  means the polynomial is linear.
- In dimension two, the Jacobian conjecture remains open.
- In dimension three, the explicit 2026 map is a counterexample.
- In every dimension greater than three, append identity coordinates to the
  three-dimensional map.

## What to read next

The [counterexample page](counterexample.md) gives the exact formula and the two
finite checks that settle the conjecture in dimension three. The
[geometry page](geometry.md) explains why a binary cubic controls every fiber.

### Historical starting points

The conjecture originates with Keller’s 1939 paper. Classical reductions by
Bass–Connell–Wright, Yagzhev, Drużkowski, and others transformed it into several
equivalent or restricted problems. Those theories remain meaningful even after
the conjecture’s failure in dimensions three and higher, and the original
two-dimensional problem survives. See the [source guide](resources.md).

