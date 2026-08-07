---
title: "Formal equivalence can outrun polynomial degree"
description: "Two Keller families can agree to every finite order while every polynomial equivalence escapes to larger and larger degree."
---

# Formal equivalence can outrun polynomial degree

!!! info "Reading level"
    This page is about a familiar local-to-global trap: solving every finite
    truncation does not help if the complexity of the solution grows with the
    truncation order.

## What is true and why

Suppose two polynomial families become equivalent modulo \(s^M\) for every
\(M\), and suppose the equivalences can be chosen compatibly as \(M\) grows.
It is tempting to conclude that one polynomial change of coordinates works
over the complete ring \(\mathbf C[[s]]\).

That conclusion is false without a uniform degree bound. In an explicit
family of three-sheeted Keller maps, the unique coordinate correction at
order \(M\) is a longer truncation of a geometric series. Every finite order
has a polynomial solution, but the required degree grows without bound. The
compatible limit is a formal power series in the source coordinate, not a
polynomial in that coordinate.

## The family and the exact threshold

Consider cubic frames

\[
A_\alpha(c)=c(1+\alpha c),
\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2.
\]

Changing \(q\) to \(q'\) by a root translation of \(c\)-degree at most
\(D\) is possible exactly when

\[
\boxed{(q'-q)\alpha^{D+2}=0.}
\]

When it exists, the translating polynomial is forced:

\[
\phi_D(c)=
\frac{q'-q}{3}\alpha^2c
\sum_{j=0}^{D-1}(-\alpha c)^j.
\]

Its first omitted term is the obstruction at the next order.

Now work over \(\mathbf C[[s]]/(s^M)\) and take \(\alpha=s\). In this
root-translation model, the least possible degree is

\[
D_M=\max(0,M-2).
\]

Thus every Artin truncation is equivalent, but the degrees needed for those
equivalences grow linearly with \(M\).

## The endpoint theorem

For \(q\ne q'\), the two complete \(\mathbf C[[s]]\)-families are compatibly
polynomially equivalent modulo every \(s^M\), but they are not stably
polynomially equivalent over \(\mathbf C[[s]]\).

The incompatibility is detected after passing to \(\mathbf C((s))\), where
the stable cubic-frame classification separates the two values of \(q\).
The order-by-order equivalences therefore cannot be replaced by one
polynomial equivalence of bounded complexity.

## Why this does not contradict bounded effectivity

Fix a stabilization width and a degree bound \(K\) for the source and target
automorphisms and their inverses. Their coefficients live in a finite affine
space, and the equations saying that they are inverse transformations and
intertwine the two maps are finitely presented. Completeness then gives

\[
\operatorname{Eq}_{K,r}(\mathbf C[[s]])
\simeq
\varprojlim_M
\operatorname{Eq}_{K,r}(\mathbf C[[s]]/(s^M)).
\]

So a compatible tower inside one fixed bounded presentation stage is
polynomially effective. The example escapes precisely because no fixed stage
contains all of its truncations.

This is also why the theorem is not a contradiction to Artin approximation:
the finite systems themselves grow as the permitted polynomial degree grows.

## Why it matters beyond this family

Many deformation calculations produce equivalences, gauges, or normal forms
order by order. This example shows that a useful theorem must control not only
existence at each order but also the complexity of the transformations.
“Formal equivalence” and “effective polynomial equivalence” are genuinely
different endpoints.

## What it does not prove

The theorem concerns an explicit cubic-frame family. It does not say that all
formal equivalences are ineffective, or that the displayed root translation
is the only possible coordinate strategy in every setting. Stronger bounds
for broader filtered presentation classes are known in the project, while
rectifying arbitrary stable polynomial equivalences into those classes
remains open.

## Proof source and status

The stable separation used at the end is proved in the pinned public
[stable-moduli manuscript](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/04-stable-moduli/main.tex).
The exact finite-level threshold and the compatible-truncation theorem are
recorded in the current project contribution
`contributions/formal-effectivity-threshold.md`. A pinned public bundle for
the strengthened threshold theorem should be added before final editorial
approval.

[Read the stable cubic-frame classification](stable-cubic-frames.md){ .md-button }
