---
title: "Normalization: restoring the finite object behind an affine map"
description: "A concrete introduction to integral closure, singular branches, and the finite/open factorization of a Keller map."
---

# Normalization: restoring the finite object behind an affine map

A singular algebraic variety can hide a simpler space with the same generic
rational functions. **Normalization** recovers that space by adjoining every
function that is integral over the original coordinate ring.

For curves, the geometric picture is often simple: a cusp is parametrized,
or branches meeting at a node are pulled apart. In higher dimensions,
normalization remains the natural way to complete a generically finite map to
a finite one.

## Worked example: the cusp

Consider the cusp

\[
C=\{(x,y):y^2=x^3\}.
\]

Its coordinate ring is

\[
A=\mathbf C[x,y]/(y^2-x^3)
 \cong \mathbf C[t^2,t^3]
 \subset \mathbf C[t].
\]

The element \(t\) is not in \(A\), but it satisfies the monic equation

\[
T^2-x=0
\]

over \(A\). It is therefore integral over \(A\). Adjoining it gives

\[
\overline A=\mathbf C[t],
\]

and the normalization map is

\[
\mathbf A^1\longrightarrow C,
\qquad
t\longmapsto(t^2,t^3).
\]

Away from the cusp, this map is an isomorphism. At the singular point it
supplies the missing parameter that remembers how the curve is approached.
The rational function field is unchanged:

\[
\mathbf C(t^2,t^3)=\mathbf C(t).
\]

## The algebraic definition

Let \(A\) be an integral domain with fraction field \(K\). Its normalization
is the integral closure

\[
\overline A=\{u\in K:u\text{ satisfies a monic polynomial over }A\}.
\]

The scheme \(\operatorname{Spec}\overline A\) is normal and has the same
function field as \(\operatorname{Spec}A\). Under standard finiteness
hypotheses, the normalization map is finite.

Normal does not mean smooth. It means, roughly, that codimension-one
singularities and hidden integral functions have been repaired enough for
rational functions to extend in the expected way.

## The finite object behind a polynomial map

A dominant generically finite polynomial map

\[
F\colon U=\mathbf A^n\longrightarrow Y=\mathbf A^n
\]

induces a finite extension of function fields \(\mathbf C(Y)\subset
\mathbf C(U)\). Normalize \(Y\) in \(\mathbf C(U)\). The result is a
canonical finite map

\[
Z_F\longrightarrow Y.
\]

Zariski's Main Theorem places the original source inside it as an open set:

\[
U\hookrightarrow Z_F\longrightarrow Y.
\]

The complement \(D_F=Z_F\setminus U\) records the sheets present in the
finite cover but absent from the affine map.

For the marked-cubic counterexample, \(Z_F\) retains all marked roots,
including repeated ones. The affine source is the simple-root open. This is
why the finite cover ramifies while the polynomial map remains étale.

## What normalization makes available

Once the finite cover is restored, one can use:

- trace and norm;
- the discriminant and different;
- conductors comparing a singular space with its normalization;
- monodromy of the generic fibre;
- fibre products and collision correspondences.

These are intrinsic to the finite extension or to the finite/open pair. They
are less dependent on the particular coordinates in which the polynomial map
was first written.

## The recognition problem remains

Normalization does **not** determine the affine opening for free. One still
has to know:

1. which boundary is removed;
2. why the remaining open is isomorphic to affine space;
3. whether an abstract intermediate cover admits compatible polynomial
   source and target coordinates.

That gap between finite-cover data and affine-space recognition is one of the
main open themes of the post-counterexample landscape.

## Where to read next

| Level | Recommendation | Use it for |
| --- | --- | --- |
| Precise reference | [The Stacks Project, “Normalization”](https://stacks.math.columbia.edu/tag/035E) | Integral closure, finiteness, and normalization in families. |
| Broad graduate treatment | Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, sections on normality and normalization | Geometric intuition together with scheme-theoretic statements. |
| Plane curves | Eduardo Casas-Alvero, *Singularities of Plane Curves* | Normalization, branches, and Puiseux parametrizations in dimension one. |
| This guide | [What the Jacobian condition misses](../start/what-the-jacobian-condition-misses.md) | The finite/open factorization as the guide's organizing perspective. |

[Next: Newton--Puiseux expansions read branches at infinity](newton-puiseux.md){ .md-button }
