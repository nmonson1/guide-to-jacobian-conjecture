---
title: "The announced plane degree bound 125"
description: "How geometry at infinity reduces every lower-degree plane candidate to two explicit supports, followed by an announced terminal calculation."
---

# The announced plane degree bound 125

<p class="byline">Global reduction by Jorge A. Guccione, Juan J. Guccione,
Rodrigo Horruitiner, and Christian Valqui · terminal calculation announced by
MathOverflow user ratto3423</p>

A plane counterexample of bounded degree has only finitely many possible
shapes at infinity. The degree-bound argument turns that principle into a
chain of exact reductions, ending with two explicit Newton-support systems.
An announced computer calculation eliminates those last systems.

## From degree to boundary shape

Let

\[
F=(P,Q)\colon\mathbf C^2\longrightarrow\mathbf C^2
\]

satisfy \(\det D(P,Q)\in\mathbf C^\times\). If \(F\) is nonproper, an
escaping branch at infinity produces valuations and Newton polygons for
\(P\) and \(Q\). The Jacobian identity constrains their leading faces.

The published 2022 analysis shows that every counterexample with

\[
\max\{\deg P,\deg Q\}<125
\]

would have degree pair

\[
(72,108)\quad\text{or}\quad(108,72).
\]

Its case analysis eliminates the \((9,27)\) possibility and reduces the
remaining \((8,28)\) case to two precise Laurent-support configurations.
This is the global part of the theorem: every lower-degree candidate is
forced into one of two terminal systems.

## The announced terminal step

On 23 July 2026, ratto3423 announced that a computer-assisted calculation
eliminates both remaining supports. The resulting statement is:

> **Announced theorem.** If a characteristic-zero plane Keller map is not a
> polynomial automorphism, then
> \[
> \max\{\deg P,\deg Q\}\ge125.
> \]

The threshold begins at \(125\); the statement excludes degrees strictly
below it.

## Why the architecture matters

A terminal contradiction proves a degree bound only after the global
reduction has shown that every candidate reaches the terminal equations. The
argument therefore has two qualitatively different parts:

1. geometry at infinity compresses all maps in the degree range to two
   supports;
2. a terminal exact calculation must show that neither support admits the
   required later layers.

The global reduction is published, and the terminal elimination has been
publicly announced. The [proof and evidence
ledger](evidence-ledger.md#the-announced-plane-degree-bound-125) records the
source form and present evidence for each stage.

## The frontier after 125

Even a complete proof of the announced theorem would leave the plane
conjecture open. It rules out a large finite degree range and clarifies the
shape of the obstruction machinery. A full solution must either construct a
boundary configuration at some higher degree or find an invariant that
excludes all degrees at once.

The [degree-21 dessins](degree-21-dessins.md) arise inside the same two
supports and show how sharply the leading boundary layer can already be
classified.

[Proof, sources, and current status](evidence-ledger.md#the-announced-plane-degree-bound-125){ .evidence-link }
