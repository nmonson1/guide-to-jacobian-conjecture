---
title: "Local invertibility is not global invertibility"
description: "The precise gap between an invertible Jacobian matrix and a polynomial inverse."
---

# Local invertibility is not global invertibility

If \(\det DF(p)\ne0\), the inverse-function theorem says that \(F\) is
one-to-one near \(p\) and has a local analytic inverse near \(F(p)\). If the
determinant is nonzero everywhere, this is true near every source point.

None of that compares two far-apart source points. A global collision
\(F(p)=F(q)\) with \(p\ne q\) is compatible with local invertibility as long
as the two local sheets remain separate near \(p\) and \(q\).

## Why properness bridges the gap

A map is proper when inverse images of compact sets are compact. For
polynomial maps of complex affine space, properness prevents points in a
bounded target region from being reached by source points running off to
infinity.

A proper local homeomorphism is a covering map. Because \(\mathbf C^n\) is
simply connected, a connected covering of \(\mathbf C^n\) has one sheet. In
the polynomial setting, that one-sheeted map has a polynomial inverse.

Thus a noninvertible Keller map must fail properness. In the 2026 example,
the generic fiber has three points, and exceptional fibers lose points
through infinity. There is no finite critical point to announce the loss.

## A useful reformulation

After the counterexample, “constant Jacobian” should be heard as a statement
about **local geometry**. The missing global hypothesis is control at
infinity. This reformulation points directly toward compactifications,
nonproperness loci, discriminants, and boundary valuations.

## Sources

- [Unbylined Ulam technical note](https://www.ulam.ai/research/jacobian.pdf)
- [Shuhong Gao, “Counterexamples to the Jacobian conjecture in dimensions greater than two”](https://arxiv.org/abs/2608.00222)
