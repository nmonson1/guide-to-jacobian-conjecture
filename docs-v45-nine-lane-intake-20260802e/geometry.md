---
title: "Geometry"
description: "The marked-root construction, affine source, fibers, monodromy, discriminant, nonproperness, and arithmetic behavior."
---

# Geometry

<p class="dek">The explicit formula stops looking miraculous when it is read
as a forgetful map from a cubic with one marked simple root to the cubic
itself.</p>

## Start with multiplication

Let \(L\) be a binary linear form and \(Q\) a binary quadratic form. Their
product is a binary cubic:

\[
\operatorname{Sym}^1(\mathbf C^2)\times
\operatorname{Sym}^2(\mathbf C^2)
\longrightarrow
\operatorname{Sym}^3(\mathbf C^2),
\qquad (L,Q)\longmapsto LQ.
\]

After quotienting the obvious rescaling and imposing
\(\operatorname{Res}(L,Q)=1\), the factor \(L\) marks a simple root of the
cubic \(LQ\). A generic cubic has three simple roots, hence three possible
markings. Forgetting \(L\) is therefore generically three-to-one.

The resultant condition does more than normalize scale: it prevents the
marked root from colliding with either root of \(Q\). Locally, the marked root
can be recovered, so the forgetful map is étale.

## Why the source is affine three-space

The four-dimensional resultant-one incidence variety is not affine
four-space. The construction intersects its image with an affine hyperplane
in the four-dimensional space of binary cubics. Up to the projective linear
symmetry, there are three hyperplane types, corresponding to root
multiplicities \((3)\), \((2,1)\), and \((1,1,1)\) in the dual cubic.

The middle, double-root type is exceptional. In normalized coefficients the
source is

\[
X=\left\{(a,b,c,d,e):
a^2e-abd+cb^2=1,\quad ad+bc=1\right\}\subset\mathbf A^5.
\]

On \(X\), the equations force the divisibilities needed to define global
coordinates:

\[
b-1=ay,\qquad
c=1-\frac32 ay+a^2z.
\]

The remaining coordinates \(d,e\) are polynomial in \(a,y,z\), and conversely
\(a,y,z\) are polynomial functions on \(X\). Thus \(X\cong\mathbf A^3\).
This is the geometric heart of the example: the double root supplies exactly
the first- and second-order vanishing required to fill in the boundary by an
affine-plane fiber.

- [Why the Double-Root Slice Is Affine Three-Space](collections/double-root-affine-source.md)
- [An Invariant Characterization of the Double-Root Orbit](collections/double-root-orbit-characterization.md)
- [Tao's coordinate-level exposition](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)

## Fibers, discriminant, and lost sheets

Away from the cubic discriminant, all three roots are simple and the map has
three points in a geometric fiber. As roots collide, some marked branches run
to infinity rather than remaining in the affine source. This is why the map
can be everywhere locally invertible yet fail to be proper.

The nonproperness hypersurface is the cubic discriminant. Its singular
cusp-type curve is also the omitted locus in the displayed example. The
precise strata are best read together, because “three sheets generically”
does not by itself determine the boundary fibers.

<div class="fiber-grid">
  <div class="fiber-card">
    <span class="fiber-count">3</span>
    <h3>Generic fiber</h3>
    <p>Three simple roots, hence three choices of the marked factor.</p>
  </div>
  <div class="fiber-card">
    <span class="fiber-count">1</span>
    <h3>Discriminant behavior</h3>
    <p>One affine marked branch may remain while other sheets escape.</p>
  </div>
  <div class="fiber-card">
    <span class="fiber-count">0</span>
    <h3>Omitted values</h3>
    <p>The singular triple-root curve is not hit by the affine source.</p>
  </div>
</div>

- [Fibers, Image, and Nonproperness](collections/base-map-fibers-image-and-nonproperness.md)
- [Lost-Sheet Local Models](collections/lost-sheet-local-models.md)
- [Escape Rates Near the Discriminant](collections/escape-rates-near-the-discriminant.md)

## Monodromy and deck transformations

Over the generic point, the marked-root construction gives a degree-three
function-field extension. Ordering all three roots produces its \(S_3\)
Galois closure. The generic cover therefore has full symmetric monodromy,
while its rational deck-transformation group is trivial: no nonidentity
automorphism of the degree-three extension preserves the marked sheet.

- [Base-Cover Monodromy and Deck Group](collections/base-cover-monodromy-and-deck-group.md)
- [The Common Cover of the Descendant Ladder](collections/common-cover-of-the-descendant-ladder.md)

## Arithmetic behavior

The same root-count picture works over finite fields, with characteristic
three requiring separate treatment. Rational fibers have sizes \(0\), \(1\),
or \(3\), and exact counts can be expressed through the splitting behavior of
the associated cubic. A rescaled version also gives determinant-one
counterexamples over every field, using a separate collision in
characteristic two.

- [Exact Finite-Field Fibers](collections/finite-field-fibers.md)
- [Characteristic-Three Degeneration](collections/characteristic-three-degeneration.md)
- [A Counterexample Over Every Field](collections/all-fields-counterexample.md)

## Sources and further reading

- [Levent Alpöge's announced map and the binary-cubic analysis](https://www.ulam.ai/research/jacobian.pdf)
- [Terence Tao, “A digestion of the Jacobian conjecture counterexample”](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
- [David Speyer's Secret Blogging Seminar discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
