---
title: The counterexample
description: The explicit three-variable map and its exact determinant-and-collision certificate.
---

# The counterexample

Set (A=1+xy) and define (F=(P,Q,R):\mathbb C^3\to\mathbb C^3) by

\[
\begin{aligned}
P &= A^3z+y^2A(4+3xy),\\
Q &= y+3xA^2z+3xy^2(4+3xy),\\
R &= 2x-3x^2y-x^3z.
\end{aligned}
\]

The formula was [announced by Levent Alpöge](https://x.com/__alpoge__/status/2079028340955197566)
on 19 July 2026; the announcement credits Akhil Mathew for asking the question
and Fable for the work leading to the example. The public [Ulam verification
note](https://www.ulam.ai/research/jacobian.pdf) gives the formula, its global
geometry, and further families.

## Certificate 1: the Jacobian never vanishes

Direct polynomial expansion gives

\[
\boxed{\det JF=-2.}
\]

This is stronger than merely checking many points: it is an identity in
\(\mathbb Q[x,y,z]\). The Ulam note also gives a short structural calculation.
On the dense chart (A\ne0), put (s=x/A). Two coordinate changes have
Jacobian determinants (-A) and (2/A), whose product is (-2). Since
\(\det JF\) is polynomial, the identity extends across (A=0).

<div class="evidence-box" markdown>
<span class="status status-formalized">FORMALIZED</span>
<span class="status status-exact">EXACT CERTIFICATE</span>

Independent Lean developments and exact symbolic implementations check this
identity. See [formal verification](formalization.md).
</div>

## Certificate 2: the map is not injective

The following distinct rational points have one common image:

| Source point | Image under (F) |
| --- | --- |
| ((0,0,-1/4)) | ((-1/4,0,0)) |
| ((1,-3/2,13/2)) | ((-1/4,0,0)) |
| ((-1,3/2,13/2)) | ((-1/4,0,0)) |

Substitution is enough to check this certificate exactly. There are no floating
point approximations and no asymptotic assumptions.

## Why these two checks are decisive

If (F) had an inverse, it would be injective. The collision proves that it is
not. The determinant identity proves that it nevertheless satisfies the
Jacobian hypothesis. Therefore the conjecture is false in dimension three.

For (n>3), the map

\[
(x,y,z,t_4,\ldots,t_n)\longmapsto
(F(x,y,z),t_4,\ldots,t_n)
\]

has the same collision and nonzero constant Jacobian. Thus the conjecture is
false in every dimension (n\ge3).

!!! important "What this does not settle"
    Stabilization only moves upward in dimension. It supplies no
    two-dimensional counterexample, so the plane Jacobian conjecture remains
    open.

## A normalized version

The target-linear change

\[
\widetilde F=(R/2,Q,P)
\]

has determinant (1), fixes the origin, and has identity linear part there.
This is often convenient for comparison with the classical normalized form of
the conjecture. It is the same counterexample up to an invertible linear change
of target coordinates.

[Now see why a cubic controls the fibers →](geometry.md){ .md-button .md-button--primary }

