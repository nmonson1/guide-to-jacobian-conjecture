---
title: "The characteristic-zero plane degree bound 125"
description: "The published reduction, the earlier external announcement, and an independent inspectable project reconstruction of the terminal calculation."
---

# The characteristic-zero plane degree bound 125

<p class="byline">Global reduction by Jorge A. Guccione, Juan J. Guccione,
Rodrigo Horruitiner, and Christian Valqui · terminal theorem announced earlier
by MathOverflow user ratto3423 · independent proof assembly and exact
certificates in this project's plane-boundary manuscript</p>

!!! info "Credit and status"
    The project does **not** claim priority for the bound. Its contribution is
    a separate, publicly inspectable reconstruction of the two terminal
    support systems and their characteristic-zero certificates.

## What is true

Let

\[
F=(P,Q)\colon\mathbf C^2\longrightarrow\mathbf C^2
\]

satisfy \(\det D(P,Q)\in\mathbf C^\times\). If \(F\) is not a polynomial
automorphism, then

\[
\boxed{\max\{\deg P,\deg Q\}\ge125.}
\]

The inequality excludes degrees **strictly below** 125. It does not exclude a
counterexample of degree exactly 125, and it does not settle the plane
Jacobian conjecture.

## How the proof is assembled

The result has a clean division of labor.

### 1. The published global reduction

The 2022 paper of Guccione, Guccione, Horruitiner, and Valqui proves that a
counterexample below 125 would have degree pair

\[
(72,108)\quad\text{or}\quad(108,72).
\]

Its case table leaves two degree-108 possibilities, labelled \((9,27)\) and
\((8,28)\). The paper eliminates \((9,27)\) and reduces \((8,28)\) to exactly
two normalized Laurent-support configurations.

This global reduction is imported; the project calculation does not reprove
it.

### 2. The earlier terminal announcement

On 23 July 2026, MathOverflow user **ratto3423** announced a
computer-assisted calculation eliminating both remaining support systems and
stated that a full write-up was in preparation. That announcement predates
the project's terminal reconstruction and receives priority for the bound on
this site.

### 3. The project's independent reconstruction

The project starts from the two exact supports in the published reduction and
rebuilds their lower-face equations over the relevant quintic coefficient
field.

For the truncated support, the weight-three and weight-four compatibility
equations force the required top vertices to vanish after saturation, so the
system is empty in characteristic zero.

For the full support, direct layer recursion reaches a perfect-square branch.
One child again loses the required vertices. On the other child, normalization
reduces the problem to fifteen equations in five variables. Six of those
equations already generate the unit ideal in the declared localization. An
independent raw-support replay closes the same support without inferring it
from a modular calculation.

Thus both normalized \((8,28)\) support alternatives are empty in
characteristic zero. Combined with the published reduction, this proves the
stated sub-125 exclusion.

## Why this is more than a numerical update

The terminal calculation is a useful example of how a computer-assisted
algebraic proof should be scoped. The certificate proves emptiness of a named
finite system over a named characteristic-zero field and localization. The
published theorem is what proves that every lower-degree counterexample would
reach one of those systems.

Neither part silently substitutes for the other.

## What this page does not claim

- It does not claim priority over ratto3423's earlier announcement.
- It does not reprove the Guccione–Guccione–Horruitiner–Valqui reduction.
- It does not exclude degree 125.
- It does not prove the plane Jacobian conjecture.
- The project source is a working computer-assisted manuscript, not a record
  of journal peer review or independent reproduction.

## Sources and verification

- [Guccione–Guccione–Horruitiner–Valqui, arXiv:2204.14178](https://arxiv.org/abs/2204.14178)
- [ratto3423, MathOverflow announcement](https://mathoverflow.net/a/513493)
- [Project plane-boundary manuscript source, pinned public revision](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/06-plane-boundary/main.tex)
- [Manifest for the exact computational supplement](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/technical-materials-v4-20260803a/manifest.json)

The pinned manuscript explicitly states the imported dependencies, gives the
separate proof assembly, and makes no priority claim for the degree-125
bound.
