---
title: "The plane case: still open, with an announced degree bound of 125"
description: "What survived the three-dimensional counterexample, what the degree-125 bound means, and why slicing does not settle the plane."
---

# The plane case: still open, with an announced degree bound of 125

The Jacobian conjecture for
\(F\colon\mathbf C^2\to\mathbf C^2\) remains open. The 2026 construction
uses a three-dimensional marked-root space, and there is no operation that
simply removes its third coordinate while preserving all the required
properties.

## The announced low-degree theorem

Write \(F=(P,Q)\). A computer-assisted argument announced by the
MathOverflow user **ratto3423** on 23 July 2026, building on the published
reduction of Jorge A. Guccione, Juan J. Guccione, Rodrigo Horruitiner, and
Christian Valqui, announces:

> **Announced computer-assisted theorem.** A counterexample over characteristic zero must satisfy
> \(\max(\deg P,\deg Q)\ge 125\).

The inequality is important: degree \(125\) itself is **not** excluded.

The 2022 paper had already reduced every case below 125 to the exceptional
degree pair \((72,108)\), up to order. Its Newton-polygon analysis left two
explicit support configurations. The later announcement says its computation
closes both. As of 7 August 2026, the MathOverflow source says that a write-up
is in preparation and does not expose the full terminal certificate. The
statement should therefore be read as the current announced bound, with a
published proof still to be linked.

[Read the result page](../results/below-125.md){ .md-button .md-button--primary }

## Why a slice of the three-dimensional map is not enough

A plane in the source need not map into a plane in the target. Even if one
chooses compatible two-dimensional slices, the restricted derivative is not
the full three-dimensional Jacobian determinant, so its determinant need not
remain constant. Eliminating one variable can also replace a polynomial map
by a rational relation.

The plane problem therefore asks for new geometry, not a smaller display of
the known formula.

## What a plane counterexample would have to do

It would be a nonproper étale polynomial map of the affine plane: locally
invertible everywhere, yet with sheets lost at infinity. Compactifying such
a map forces strong arithmetic and combinatorial restrictions on its
boundary curves. Newton polygons, valuations, Puiseux expansions, and dessins
encode different parts of that boundary data.

These restrictions have driven the degree lower bound upward, but they have
not proved that no plane counterexample exists.

## Sources

- [Guccione–Guccione–Horruitiner–Valqui, arXiv:2204.14178](https://arxiv.org/abs/2204.14178)
- [ratto3423, MathOverflow answer announcing the terminal calculation](https://mathoverflow.net/a/513493)
