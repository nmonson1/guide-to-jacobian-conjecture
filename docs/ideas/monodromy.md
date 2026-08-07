---
title: "Covers and monodromy: how the sheets move"
description: "A conceptual introduction to generic degree, monodromy, and composition-primality for Keller maps."
---

# Covers and monodromy: how the sheets move

Away from exceptional target values, a generically finite polynomial map has
a fixed number \(d\) of preimages. This number is its **generic degree**. For
the marked-cubic counterexample, \(d=3\): the three points correspond to the
three possible marked roots.

Choose a regular target value and label its \(d\) preimages. Move the target
around a loop that avoids the exceptional locus. When the loop returns, the
preimages return too, but their labels may be permuted. All permutations
obtained in this way form the **monodromy group**.

## A toy cover

For \(z\mapsto z^d\), a nonzero target \(w\) has \(d\) roots. Move \(w\)
once around the origin. Each chosen root moves continuously to the next root,
so the labels undergo a \(d\)-cycle. This is monodromy in its simplest form:
the fibers have not collided along the loop, but their labels return
permuted.

## What monodromy remembers

Generic degree only counts sheets. Monodromy records how tightly they are
connected. A transitive group means the cover is connected. The full
symmetric group \(S_d\) means that, from the viewpoint of continuation along
loops, the sheets have no hidden partition.

That last point matters for composition. If a map factors nontrivially as
\(F=G\circ H\), the sheets of \(F\) come in blocks: first choose a preimage
under \(G\), then one under \(H\). Monodromy must preserve this block system.
A primitive monodromy group therefore obstructs nontrivial factorization of
the generic cover.

For Keller self-maps, a degree-one factor is an automorphism. Consequently,

\[
\operatorname{Mon}(F)\text{ primitive}
\quad\Longrightarrow\quad
F\text{ is composition-prime}.
\]

## Full symmetric monodromy in every degree

The every-degree weighted-lift construction can be chosen so that its hidden
one-variable inverse equation is a Morse polynomial. Its simple branch loops
act by transpositions with distinct branch values; connectedness forces those
transpositions to generate \(S_d\).

Thus for every \(d\ge3\), there is a three-dimensional Keller counterexample
with monodromy \(S_d\), and hence a composition-prime example of that generic
degree.

[Read the every-degree result](../results/every-generic-degree.md){ .md-button }

## What monodromy does not remember

Two polynomial maps can define the same abstract function-field extension
while having different affine charts and different behavior at infinity.
Monodromy is powerful, but it cannot by itself recognize which open part of a
finite cover is affine space.

The converse composition problem illustrates the gap. An imprimitive block
system gives an intermediate field and an intermediate normal finite cover.
It does not automatically provide an open subset isomorphic to affine space
or polynomial frames making the two induced maps Keller maps. That is why the
post-counterexample program uses monodromy together with discriminants,
conductors, and boundary data.

## Sources

- [David Speyer, Secret Blogging Seminar discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
- [Shuhong Gao, arXiv:2608.00222](https://arxiv.org/abs/2608.00222)

The all-degree full-symmetric-monodromy theorem is recorded in the current
project contribution `contributions/composition-monodromy-boundary.md`.

[Next: discriminants and actual root collisions](discriminants.md){ .md-button }
