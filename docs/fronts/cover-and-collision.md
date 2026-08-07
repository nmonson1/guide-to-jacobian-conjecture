---
title: "The cover behind the formula"
description: "How normalization, monodromy, and collision spaces extract the intrinsic finite cover from a polynomial presentation."
---

# The cover behind the formula

<p class="dek">The displayed map is one coordinate presentation of a
three-sheeted finite cover with a boundary removed. Which parts of that cover
can be recognized without remembering the coordinates?</p>

## A specimen problem

Start with a Keller map

\[
F\colon X=\mathbf A^n\longrightarrow Y=\mathbf A^n
\]

which is étale, hence quasi-finite. Normalize \(Y\) in the extension
\(K(Y)\subset K(X)\), obtaining

\[
X\hookrightarrow Z\xrightarrow{\pi}Y.
\]

Suppose one is given only the finite map \(\pi\colon Z\to Y\), together with
its intrinsic algebra. Can one recover the open subset \(X\subset Z\) that
was affine space? A satisfactory answer would identify the deleted boundary
without returning to the binary-cubic coordinates that produced the first
example.

## What the finite cover remembers

Over a regular target value, the points of \(Z\) are the sheets of the map.
Monodromy records how those sheets permute along loops. The discriminant marks
where the completed cover ramifies. Trace and conductor ideals compare the
finite algebra with the target.

Collisions are encoded by the fiber product

\[
Z\times_Y Z.
\]

Its diagonal records a point paired with itself. The off-diagonal part records
two distinct sheets over the same target point. For the cubic cover, this
collision space is explicit, and the generic monodromy is \(S_3\).

Near a triple-root point, the local collision algebra carries more than the
set of colliding sheets. Nilpotents and multiplicities measure how the
collision degenerates. These local algebras feed directly into flatness,
defect, and deformation calculations.

## What the affine opening adds

The finite cover alone includes the repeated marked roots. The Keller source
removes them. This boundary choice is responsible for both properties that
make the example unusual:

- the remaining map is étale everywhere;
- the remaining open is still affine space.

Ramification detects étaleness locally. Affineness is global and much more
rigid: an affine-space complement imposes strong constraints on the divisor,
the class group, and the topology of the finite cover.

<div class="mental-model" markdown>

**The key distinction.** The cover tells us how many sheets there are and how
they collide. The opening tells us which limiting sheets have been removed
and whether the complement is affine space.

</div>

## Concrete test cases

- [Covers and monodromy](../ideas/monodromy.md)
- [Normalization](../ideas/normalization.md)
- [The marked-root construction](../background/marked-root-geometry.md)
- [Keller maps of every generic degree](../results/every-generic-degree.md)

## An intrinsic recognition problem

The theorem one wants is an intrinsic criterion on

\[
(\pi\colon Z\to\mathbf A^n,\,D\subset Z)
\]

that is necessary and sufficient for

\[
Z\setminus D\simeq\mathbf A^n
\]

and for the induced map to have constant nonzero Jacobian. The criterion
should recover the marked-cubic opening and distinguish examples that share
generic monodromy while carrying different boundary geometry.

Progress toward such a theorem can be tested on families where the cover,
discriminant, conductor, and collision algebra are all computable. The first
counterexample supplies the benchmark; maps of other generic degrees supply
the first genuinely different tests. A successful criterion would make the
affine opening as intrinsic as the finite cover itself.

