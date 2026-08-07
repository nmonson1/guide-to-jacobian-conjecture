---
title: "Alpöge and Fable (July 2026): a three-dimensional counterexample"
description: "The explicit map, a structural determinant computation, the collision, and the geometry already visible in the formula."
---

# Alpöge and Fable (July 2026): a three-dimensional counterexample

<p class="byline">Question suggested by Akhil Mathew · construction produced
by Fable · map announced by Levent Alpöge</p>

<p class="dek">The verification fits on a page. The idea behind it is a
three-sheeted marked-root cover with its ramification boundary removed.</p>

## The map and the collision

Set \(u=1+xy\) and define
\(F=(P,Q,R)\colon\mathbf C^3\to\mathbf C^3\) by

\[
\begin{aligned}
P&=u^3z+y^2u(4+3xy),\\
Q&=y+3xu^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z.
\end{aligned}
\]

The three distinct points

\[
(0,0,-1/4),\qquad (1,-3/2,13/2),\qquad (-1,3/2,13/2)
\]

all map to

\[
(-1/4,0,0).
\]

Thus one exact substitution already proves that \(F\) is not injective. The
remaining check is that its derivative is invertible everywhere.

## Why the determinant collapses to \(-2\)

A direct expansion verifies the determinant. One change of variables explains
the cancellation. On the open set \(u\ne0\), put

\[
s=\frac{x}{u},
\qquad
B=u^2z+y^2(4+3xy).
\]

Then

\[
P=uB,
\qquad
Q=y+3Ps,
\qquad
R=2s-ys^2-Ps^3.
\]

The map factors through the intermediate coordinates \((P,y,s)\). Its two
Jacobian determinants are

\[
\det\frac{\partial(P,y,s)}{\partial(x,y,z)}=-u
\]

and

\[
\det\frac{\partial(P,Q,R)}{\partial(P,y,s)}
=2(1-ys)=\frac{2}{u}.
\]

Multiplying them gives

\[
\det DF=-2
\]

where \(u\ne0\). Both sides are polynomial functions, so the identity holds
on all of \(\mathbf C^3\).

<div class="mental-model" markdown>

**Where the cancellation comes from.** On the chart \(u\ne0\), the displayed
degree-seven map factors through two simpler coordinate maps. Their Jacobian
factors are \(-u\) and \(2/u\), so the large cancellation is built into the
construction.

</div>

## The marked root already hidden in the coordinates

The target point \((P,Q,R)\) determines the binary cubic

\[
f_{P,Q,R}(S,T)=RT^3-2ST^2+QS^2T-2PS^3.
\]

The source coordinates satisfy

\[
f_{P,Q,R}(x,u)=0.
\]

So the projective point \([x:u]\) is a root of the cubic attached to the
image. A generic cubic has three roots, hence three possible marked points.
Forgetting the mark produces the three sheets of \(F\).

Once a root is marked, the three-sheeted cover is elementary. The ingenious
step is the tangent chart that identifies its simple-root locus with
\(\mathbf A^3\). In that chart, each chosen root moves locally without
ramification while the three global choices remain distinct.

[See the three viewpoints side by side](three-views.md){ .md-button .md-button--primary }
[Read the marked-root construction](../background/marked-root-geometry.md){ .md-button }

## What the example settles

The constant determinant makes \(F\) locally invertible at every source
point. The explicit collision makes it noninvertible. For every \(n>3\),

\[
F\times\operatorname{id}_{\mathbf C^{n-3}}
\]

is a counterexample in dimension \(n\).

The construction leaves the plane problem open. A plane in the source need
not map to a plane in the target, and restricting the derivative does not
preserve the full three-dimensional Jacobian identity.

[Proof, sources, formal checks, and credit](../results/evidence-ledger.md#the-three-dimensional-counterexample){ .evidence-link }
