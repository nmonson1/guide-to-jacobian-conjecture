---
title: "Five degree-21 dessins on the last supports below 125"
description: "How the two surviving Newton supports force one Belyi passport with exactly five connected dessins."
---

# Five degree-21 dessins on the last supports below 125

<p class="byline">A project theorem of Nathaniel Monson</p>

The two Newton supports left by the published degree-below-125 reduction force
the same leading-face differential equation. That equation can be integrated
into a Belyi map. The resulting ramification passport is rigid enough to
classify every connected dessin.

## From the Jacobian equation to a Belyi map

For either support, the leading faces have the form

\[
P_{\mathrm{face}}=Xp(z),
\qquad
Q_{\mathrm{face}}=X^2Yq(z),
\qquad
z=XY^2,
\]

with

\[
\deg p=7,
\qquad
\deg q=10.
\]

The constant-Jacobian equation on the face becomes

\[
pq+2zpq'-3zp'q=1.
\]

Now set

\[
\tau(z)=z\frac{q(z)^2}{p(z)^3}.
\]

The revealing calculation is logarithmic:

\[
\frac{\tau'}{\tau}
=\frac1z+2\frac{q'}q-3\frac{p'}p
=\frac{pq+2zpq'-3zp'q}{zpq}
=\frac1{zpq}.
\]

Hence

\[
\tau'=\frac{q}{p^4}.
\]

This one identity contains the ramification data. Comparing vanishing
orders on the two sides shows first that every root of \(p\) and \(q\) is
simple. The roots of \(q\) give double zeros of \(\tau\), the roots of
\(p\) give triple poles, and \(z=0\) supplies one additional simple zero.
At \(z=\infty\), the derivative vanishes to order sixteen in the local
coordinate \(1/z\), so
the ramification index is seventeen. After scaling the third branch value to
\(1\), the passport is

\[
(2^{10}1),
\qquad
(3^7),
\qquad
(17\,1^4).
\]

The coefficient problem has become a finite permutation problem.

## The five dessins

There are exactly five connected dessins with this passport. They have:

- trivial deck group;
- monodromy group \(A_{21}\);
- one arithmetic orbit over an irreducible quintic field.

The enumeration is exhaustive: every transitive permutation triple with the
stated cycle data appears and belongs to this single orbit.

## Why the compression matters

Before the Belyi reformulation, one faces polynomial coefficients in two
Newton supports and a nonlinear differential identity. Afterward, the leading
boundary layer is represented by five discrete objects.

This is precisely the kind of compression one hopes for in the plane problem:
continuous coefficient data become finite combinatorics, and exact arithmetic
reconstructs the corresponding maps.

## The remaining globalization problem

Each dessin controls the forced leading face. To globalize it, one must solve
every higher Puiseux layer and fill out the full polynomial supports. The five
dessins are therefore exact inputs to the terminal equations; globalization
still requires all later compatibility conditions.

The announced degree-bound computation states that the two full supports have
no solutions. The dessin theorem explains the leading geometry inside those
supports and supplies a finite list on which later equations can act.

[Proof, certificates, and status](evidence-ledger.md#five-degree-21-dessins){ .evidence-link }
