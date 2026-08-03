---
title: "Model research brief — Flatness defects after cubic normalization"
description: "A self-contained mathematical handoff for a research model."
---

# Flatness defects after cubic normalization

<p class="claim-tag">Lane 1 · Updated 3 August 2026</p>

Lane 1 · 2026-08-03

## Scope

Study the finite normalization of the generic cubic Keller incidence and locate
the first source-chart locus where flatness can fail. The target is a local
algebra theorem or counterexample, not another derivation of the already known
normalization and collision formulas.

## Setup and definitions

Work over a characteristic-zero field. Let $F=(P,Q)$ be a degree-three
Keller map, let $A\to B$ be the finite normalization algebra in the framed
generic incidence, and let $V_{\mathrm{std}}$ be the standard two-dimensional
representation of the three-sheet permutation group.

The flatness-defect module is

\[
\Delta_F=\operatorname{Ext}^1_A(B,A).
\]

For a collision ideal $I\subset R$ in a source chart, write
$I^{\mathrm{sat}}$ for saturation by the declared chart-open factor. The
collision theorem identifies the embedded correction by

\[
I^{\mathrm{sat}}/I\simeq
\operatorname{MatlisDual}(\Delta_F)\otimes V_{\mathrm{std}}.
\]

## Results to use

- The cubic frame, resolvent normalization, source splitting, and ADE local
  matrix factorizations are exact in their stated opens.
- The displayed saturation/defect identity is exact; in particular,
  $\Delta_F=0$ implies no hidden embedded collision contribution on that
  chart.
- For the normalized benchmark $A(c)=c$, $B(c)=-2$, exact replay gives
  coordinate degrees $(7,6,4)$, Jacobian $-2$, the inverse cubic and marked
  slope identities, a finite-flat rank-three completion, the finite-chart
  different, and the two cusp-conductor pullbacks. It does not construct the
  integral quadratic resolvent or its eigensheaf.
- These statements do not prove global flatness of every source chart or
  identify the first nonzero defect.

## Example: ADE replay

The stored matrices for the simple local models multiply to the defining
hypersurface equation. This is an example of the local algebra interface; it
does not show that every cubic collision germ is ADE.

## Live problem

Determine the first actual source-chart saturation defect. A useful answer
must compare $I$ and $I^{\mathrm{sat}}$ in the native cubic chart and then
interpret the quotient through $\Delta_F$, including its support and length.

## Tasks

### L1-T1 — Compute one complete source-chart defect

Inputs: the framed cubic equations and resolvent in
[the main TeX source](../proof-sources/01-cubic-incidence/main.md), the
[flatness proof](../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md),
the [collision-saturation packet](lane-1-source-packet.md),
and the [exact marked-root benchmark](lane-1-source-packet.md).

Deliverable: an explicit chart ring, ideal $I$, open factor, generators for
$I^{\mathrm{sat}}/I$, and a proof identifying that module with the stated
Matlis-dual defect. If it vanishes, give the exact certificate and move to the
next chart in the same atlas.

Dependencies: finite normalization and the declared chart localization.

Limits: a tangent-space dimension or set-theoretic equality is not a module
isomorphism; no statement may cross a chart boundary without its complement.

Alternative connections: a filtration or valuative interpretation linked to
Lane 5 is welcome if it still computes this same module.

## Limits

The current theory is generic and chart-local. It does not assert that every
cubic incidence normalization is flat, reduced, or globally covered by the
one collision chart.

## Direct sources

- [Retained defect/collision theorem RMU-1A8D0010](../working-mathematics/units/RMU-1A8D0010.md)
- [ADE matrix checker](lane-1-source-packet.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-1-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
