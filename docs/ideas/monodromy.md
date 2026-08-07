---
title: "Covers and monodromy: how the sheets move"
description: "A worked introduction to generic degree, continuation of roots, block systems, and what monodromy cannot see."
---

# Covers and monodromy: how the sheets move

Away from exceptional target values, a generically finite polynomial map has
a fixed number \(d\) of preimages. This number is its **generic degree**. It
counts the sheets of the map, but not how those sheets fit together.

Monodromy records the missing information. Choose a regular target value,
label its preimages, and move the target around a loop that avoids the
exceptional locus. The preimages move continuously. When the loop returns,
the same points are present, but their labels may have been permuted.

## Worked example: the three cube roots

Consider

\[
\pi(z)=z^3\colon \mathbf C^\times\longrightarrow \mathbf C^\times.
\]

At the target value \(w=1\), label the three roots

\[
1,\qquad \omega=e^{2\pi i/3},\qquad \omega^2.
\]

Move the target once counterclockwise around the origin:

\[
w(t)=e^{2\pi i t},\qquad 0\le t\le1.
\]

One continuous choice of cube root is \(z(t)=e^{2\pi i t/3}\). It begins at
\(1\) and ends at \(\omega\). The other roots move in parallel, so the loop
acts by the cycle

\[
(1\ \omega\ \omega^2).
\]

No roots collide along the loop. The permutation is produced by global
continuation, not by a critical point encountered on the path.

## From loops to a group

All permutations obtained from all loops form the **monodromy group**, a
subgroup of the symmetric group \(S_d\). Three basic features are worth
separating.

- **Degree** counts the sheets.
- **Transitivity** says that continuation can move any sheet to any other;
  equivalently, the generic cover is connected.
- **Primitivity** says there is no nontrivial partition of the sheets into
  blocks preserved by every continuation.

The marked-cubic counterexample has generic degree three. Its monodromy is
\(S_3\), so its three root-markings are connected as strongly as possible.

## Composition creates blocks

Suppose a finite cover factors as

\[
X\xrightarrow{H} Z\xrightarrow{G}Y.
\]

To choose a point of a generic fibre of \(G\circ H\), first choose a point of
\(G^{-1}(y)\), then choose one of the points above it under \(H\). The full
fibre is therefore partitioned into \(H\)-fibres, and monodromy preserves
that partition.

For a toy example, write

\[
z^6=(z^2)^3.
\]

Over a generic \(w\), the six sixth roots come in three pairs
\(\{z,-z\}\), one pair above each cube root of \(w\). Continuation may
permute the three pairs, and may exchange the two members of a pair, but it
cannot forget the block structure imposed by the factorization.

Thus primitive monodromy rules out a nontrivial factorization of the generic
finite cover.

## What monodromy does not remember

Monodromy is an invariant of the cover over a dense open part of the target.
It does not remember which boundary points were deleted from an affine
presentation. Two maps can have the same function-field extension and the
same generic monodromy while using different affine openings and having
different behavior at infinity.

This is a central caution in the Jacobian problem. An imprimitive monodromy
group gives an intermediate field and an intermediate normal finite cover.
It does **not** automatically produce an intermediate affine space or a
factorization by polynomial Keller maps.

## How it appears in the guide

- The first counterexample has three sheets corresponding to three marked
  roots.
- [Every generic degree](../results/every-generic-degree.md) occurs in
  dimension three, so degree is not a rigid fingerprint of the first map.
- The cover-and-collision front asks which monodromy and collision data can
  recognize an affine Keller opening.

## Where to read next

| Level | Recommendation | Use it for |
| --- | --- | --- |
| First encounter | [Allen Hatcher, *Algebraic Topology*, §1.3](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) | Covering spaces, lifting, and the action of loops on fibres. |
| Graduate geometry | Rick Miranda, *Algebraic Curves and Riemann Surfaces*, chapters on branched covers | The analytic and algebraic geometry of finite maps of curves. |
| This counterexample | [David Speyer's structural discussion](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/) | Function fields, fibres, and monodromy in the new example. |
| New families | [Shuhong Gao, arXiv:2608.00222](https://arxiv.org/abs/2608.00222) | Geometric constructions with larger generic degree. |
