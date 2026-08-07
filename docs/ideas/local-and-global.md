---
title: "Local invertibility is not global invertibility"
description: "What an invertible Jacobian matrix controls, why properness forces one sheet, and how the counterexample escapes through infinity."
---

# Local invertibility is not global invertibility

If \(\det DF(p)\ne0\), the inverse-function theorem gives a neighborhood of
\(p\) on which \(F\) is one-to-one. When the determinant never vanishes, this
is true near every source point.

The theorem compares nearby points. A global collision compares points that
may lie very far apart.

<figure class="math-figure">
  <img src="../assets/images/local-sheets.svg" alt="Three disjoint source neighborhoods mapping isomorphically onto the same target neighborhood.">
  <figcaption>Three local inverse branches can coexist over one target neighborhood.</figcaption>
</figure>

If \(F(p)=F(q)\) with \(p\ne q\), choose disjoint neighborhoods of \(p\) and
\(q\). Each may map isomorphically onto the same small neighborhood of the
common image. No local folding is required.

## Properness forces the sheets to stay

A map is proper when inverse images of compact sets are compact. For a
polynomial map of complex affine space, properness prevents a sequence from
running to infinity while its image remains in a bounded region.

A proper local homeomorphism is a covering map. Since \(\mathbf C^n\) is
simply connected, every connected covering of \(\mathbf C^n\) has one sheet.
For a Keller map, properness would therefore force global invertibility.

The implication is a practical diagnostic:

\[
\text{noninvertible Keller map}
\quad\Longrightarrow\quad
\text{nonproper map}.
\]

## How a sheet disappears

In the three-dimensional example, a typical target value has three
preimages. Near an exceptional target value, one or more of those preimages
can move farther and farther out in the affine source. Their images
converge, while the source points have no affine limit.

After compactifying the source, the escaping sequence approaches the boundary:

<figure class="math-figure">
  <img src="../assets/images/escape-to-infinity.svg" alt="A sequence in affine space approaching the boundary of a compactification while its images converge to a finite target point.">
  <figcaption>Nonproperness lets a finite target value be approached by source points escaping to infinity.</figcaption>
</figure>

The finite completion restores the missing limit point. In the marked-root
model, that point is a repeated marked root, and the completed finite cover
ramifies there. The affine source omits it, so the affine derivative remains
invertible everywhere.

<div class="mental-model" markdown>

**The useful reformulation.** Constant Jacobian controls local geometry.
Global invertibility depends on whether the sheets remain inside the affine
chart.

</div>

## Why this changes the subject

Before the counterexample, it was natural to search for ever stronger local
consequences of the Jacobian identity. The example redirects attention to
objects that record infinity: compactifications, nonproperness loci,
boundary divisors, valuations, and discriminants.

The first invariant to study is monodromy. Before any sheet reaches the
boundary, continuation around loops records how the generic sheets are
connected.

[Next: covers and monodromy](monodromy.md){ .md-button .md-button--primary }

## Sources

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Shuhong Gao, “Counterexamples to the Jacobian conjecture in dimensions greater than two”](https://arxiv.org/abs/2608.00222)
