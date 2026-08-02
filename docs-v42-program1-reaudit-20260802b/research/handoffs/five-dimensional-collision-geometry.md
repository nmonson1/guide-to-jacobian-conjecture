---
title: "Model research brief — Five-dimensional collision geometry"
description: "A self-contained mathematical handoff for a research model."
---

<p class="claim-tag">Model research brief · Lane 7</p>
<p class="handoff-snapshot"><strong>Snapshot:</strong> 2 August 2026 · 368 public claim records · 104 grouped packages · manuscripts v13 · handoff source v15 · site release <code>living-guide-public-v42-program1-reaudit</code>.</p>
[Machine-readable release metadata](release.json){ .handoff-release }

!!! info "Retained working graph"
    Exact reusable units and their deeper support pages are available
    in the [retained working mathematics view](../working-mathematics/index.md).

!!! tip "Current proof sources — preferred"
    Use the [current source text and exact labels](../proof-sources/index.md) for full proof context. PDFs are optional archival
    reading copies and may predate source repairs.
# Lane 7: Five-dimensional collision geometry

## Research objective

Determine the characteristic-zero geometry of the exact 15-equation
five-dimensional collision chart.  The goal is a component-level description
that supports either global first-normal obstructions or explicit persistent
construction loci.

This is a Program 5 problem; use the full
[Homogeneous Descendants dossier](homogeneous-descendants.md) for the tensor,
open-locus factors, and first-normal conventions.  It interacts with
[Lane 6](homogeneous-realization-compression.md), but the collision chart and
the 19-to-18 operation quotient are not the same scheme.

## Reusable mathematics

On the regular open set, a full-kernel nilpotent quadratic pencil in dimension
five has an affine collision chart cut out by 15 explicit primitive quintics
in 16 variables.  Its parameter representation is a scalar plus the binary
sextic module

```text
C*lambda + Sym^6(C^2),
```

with an explicit determinant invariant.  The equations and open-locus factors
are exact.  Thirty finite-field samples and one residue-disk calculation give
useful diagnostics for first-normal behaviour, but they do not determine the
characteristic-zero irreducible components or generic obstruction on each
component.

Two prior monolithic Macaulay2 attempts returned no mathematical result.  They
should not be treated as negative evidence about the geometry.  The failure
was computational organization: full saturation, radical decomposition, and
singular-locus work were asked for at once without staged elimination or a
verified intermediate invariant.

## Staged computation

Proceed in a versioned sequence whose intermediate outputs are independently
checkable:

1. Saturate by the explicit regular-open factors one at a time, recording
   dimension and whether each saturation changes the ideal.
2. Compute radical membership tests and an equidimensional decomposition
   before requesting a full primary decomposition.
3. For every candidate component, record generators, dimension, degree, and a
   rational or number-field sample point when available.
4. Compute the singular locus inside the regular open chart, component by
   component.
5. Pass the first-normal obstruction to each component's function field and
   decide generic vanishing there.
6. Only then study exceptional divisors or intersections where the generic
   function-field calculation degenerates.

Modular calculations may guide term orders and component guesses, but lift
components to characteristic zero before interpreting them.  Preserve all
open-locus saturations; an affine component supported entirely on an excluded
factor is not a component of the target chart.

## Mathematical alternatives

A geometric reformulation is preferable to brute force if one exists.  Useful
possibilities include invariant theory of the binary-sextic module, a
determinantal or incidence presentation, apolarity, or a quotient that exposes
the collision line before elimination.  Explain how the 15 quintics arise in
the proposed geometry and how the regular-open determinant is represented.

Persistent components are possible construction loci, not failed exclusions.
If the first-normal class vanishes generically on a component, retain it and
compute the next obstruction rather than discarding it.

## Useful deliverable

A credible first result is a characteristic-zero radical/equidimensional
decomposition with exact dimensions and degrees, even if primary decomposition
remains unfinished.  A theorem identifying the chart with a familiar moduli or
determinantal space would be stronger.  Do not repeat the two monolithic runs;
use their lack of output only to motivate the staged design.

[Back to the portfolio hub](state-of-the-program.md)
