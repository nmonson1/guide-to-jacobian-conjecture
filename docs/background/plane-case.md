---
title: "The plane case: still open, with degree bound 125"
description: "What survived the three-dimensional counterexample, what the degree-125 bound means, and why slicing does not settle the plane."
---

# The plane case: still open, with degree bound 125

The Jacobian conjecture for
\(F\colon\mathbf C^2\to\mathbf C^2\) remains open. The 2026 construction
uses a three-dimensional marked-root space, and there is no operation that
simply removes its third coordinate while preserving all the required
properties.

## The low-degree theorem

Write \(F=(P,Q)\). The current characteristic-zero bound is:

> **Computer-assisted theorem.** If \(F\) is not a polynomial automorphism,
> then \(\max(\deg P,\deg Q)\ge125\).

The inequality is important: degree \(125\) itself is **not** excluded.

The proof has two layers. A 2022 paper by Jorge A. Guccione, Juan J.
Guccione, Rodrigo Horruitiner, and Christian Valqui reduces every case below
125 to two explicit Newton-support systems in degree pair \((72,108)\), up
to order. On 23 July 2026, MathOverflow user **ratto3423** announced a
computer-assisted calculation eliminating both systems.

This project later produced an independent working proof assembly that starts
from the two published supports, reconstructs their exact characteristic-zero
equations, and exposes terminal unit-ideal certificates and replay data. The
guide credits the earlier announcement for priority while linking the
project's inspectable source. The project manuscript is a working
computer-assisted proof, not a record of journal peer review or independent
reproduction.

[Read the result page and proof ledger](../results/below-125.md){ .md-button .md-button--primary }

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
invertible everywhere, yet with sheets lost at infinity. Compactifying such a
map forces strong arithmetic and combinatorial restrictions on its boundary
curves. Newton polygons, valuations, Puiseux expansions, and dessins encode
different parts of that boundary data.

These restrictions have driven the degree lower bound upward, but they have
not proved that no plane counterexample exists.

## Sources

- [Guccione–Guccione–Horruitiner–Valqui, arXiv:2204.14178](https://arxiv.org/abs/2204.14178)
- [ratto3423, MathOverflow announcement](https://mathoverflow.net/a/513493)
- [Pinned project plane-boundary source](https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/b2d4bb0/data/manuscript-sources-v1-20260803d/sources/06-plane-boundary/main.tex)
