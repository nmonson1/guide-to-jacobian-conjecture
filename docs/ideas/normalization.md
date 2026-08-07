---
title: "Normalization: the finite cover behind the affine map"
description: "How normalization separates singular branches, canonically completes a quasi-finite map, and exposes the deleted boundary."
---

# Normalization: the finite cover behind the affine map

A singular variety may glue together branches that are distinct away from the
singular point. **Normalization** replaces it by a normal variety with the
same rational functions and a finite map back to the original space.

The cusp

\[
y^2=x^3
\]

is the standard example. Its coordinate ring is
\(\mathbf C[t^2,t^3]\). Adjoining the integral element \(t\) gives
\(\mathbf C[t]\), and the normalization map is

\[
t\longmapsto(t^2,t^3).
\]

The parameter \(t\) supplies the branch coordinate that the singular equation
had hidden.

## From the affine map to its finite completion

Let \(F\colon X\to Y\) be a dominant quasi-finite map of irreducible
varieties. It induces a finite extension of function fields

\[
K(Y)\subset K(X).
\]

Normalize \(Y\) in \(K(X)\). This produces a canonical finite map

\[
Z\longrightarrow Y.
\]

When \(X\) is normal and \(F\) is separated, Zariski's Main Theorem identifies
\(X\) with an open subvariety of \(Z\):

<figure class="math-figure">
  <img src="../assets/images/finite-open-factorization.svg" alt="An affine source X included as an open subset of a normal finite cover Z, followed by a finite map to the target Y.">
  <figcaption>The function field determines the finite cover \(Z\to Y\). The affine presentation also depends on the boundary \(D=Z\setminus X\).</figcaption>
</figure>

For the marked-cubic counterexample, \(Z\) remembers every marked root,
including repeated ones. The source \(X\simeq\mathbf A^3\) is the open part
where the marked root is simple.

## Why this factorization clarifies the example

The polynomial formula mixes together two questions:

1. Which finite cover of the target is determined by the function field?
2. Which boundary must be removed so that the remaining open is affine space
   and the map is étale?

Normalization answers the first canonically. The second contains the special
geometry of the counterexample.

Once \(Z\) is available, intrinsic invariants enter naturally: trace,
discriminant, conductor, ramification, monodromy, and the geometry of the
boundary divisor. These are intrinsic to the finite cover and its boundary.

<div class="mental-model" markdown>

**The decisive shift.** Normalization replaces the coordinate formula by a
finite cover intrinsic to the function field. Recovering the counterexample
then means identifying the affine open whose deleted boundary contains the
ramification locus.

</div>

## The recognition problem

The affine opening requires additional boundary data. Different boundaries
inside the same \(Z\) produce different open varieties, and affineness imposes
a strong global constraint on the complement.

The resulting recognition problem is one of the central questions opened by
the counterexample:

> Which intrinsic conditions on \(Z\to Y\) and a boundary divisor
> \(D\subset Z\) guarantee that \(Z\setminus D\simeq\mathbf A^n\) and that the
> induced map is a Keller map?

Boundary reconstruction, deformation theory, and low-degree classification
all meet at this question.

[Next: Newton--Puiseux expansions read branches at infinity](newton-puiseux.md){ .md-button .md-button--primary }

## Sources

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [David Speyer, Secret Blogging Seminar discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
