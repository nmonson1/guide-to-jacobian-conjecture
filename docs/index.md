---
title: Guide to the Jacobian Conjecture
description: What changed in 2026, what has been checked, and what remains open.
hide:
  - navigation
  - toc
---

<section class="hero" markdown>

<div class="hero-copy" markdown>

<p class="eyebrow">A reader’s guide · evidence first</p>

# The Jacobian conjecture changed. The interesting mathematics did not end.

An explicit polynomial map in three variables has constant nonzero Jacobian
determinant but is not one-to-one. The certificate is finite and exact. The
counterexample settles dimensions three and higher; the plane case remains
open.

<div class="hero-actions">
  <a class="md-button md-button--primary" href="counterexample/">See the certificate</a>
  <a class="md-button" href="guide/">Start from the beginning</a>
</div>

</div>

<div class="formula-card" markdown>

<p class="card-kicker">The decisive facts</p>

For an explicit map (F:\mathbb C^3\to\mathbb C^3),

\[
\det JF=-2,
\]

yet three distinct rational points have the same image:

\[
(0,0,-\tfrac14),\quad
(1,-\tfrac32,\tfrac{13}{2}),\quad
(-1,\tfrac32,\tfrac{13}{2}).
\]

<span class="status status-formalized">FORMALIZED</span>
<span class="status status-exact">EXACT CERTIFICATE</span>

</div>

</section>

<section class="verdict-strip" markdown>

<div markdown>
<span class="dimension">1D</span>
<strong>Elementary</strong>
<p>A nonzero constant derivative forces a linear polynomial.</p>
</div>

<div markdown>
<span class="dimension open">2D</span>
<strong>Still open</strong>
<p>The new three-variable mechanism does not settle the plane conjecture.</p>
</div>

<div markdown>
<span class="dimension false">3D+</span>
<strong>False</strong>
<p>The explicit map works in dimension three and stabilizes to every higher dimension.</p>
</div>

</section>

## The logical surprise

<div class="logic-flow" markdown>

<div class="logic-node" markdown>
<span>01</span>
### Constant Jacobian
The derivative is invertible at every point.
</div>

<div class="logic-arrow">→</div>

<div class="logic-node" markdown>
<span>02</span>
### Local inverse
Near each source point, the map is one-to-one.
</div>

<div class="logic-arrow break">↛</div>

<div class="logic-node accent" markdown>
<span>03</span>
### Global inverse
Different local sheets can still map to the same target while other sheets escape to infinity.
</div>

</div>

The conjecture asserted that the first fact forced the third for polynomial
self-maps of affine space. The counterexample exposes the missing global
condition: **properness**.

[Understand the geometry →](geometry.md){ .text-link }

## Three ways to use this guide

<div class="path-grid" markdown>

<a class="path-card" href="guide/">
<span class="path-number">01</span>
<h3>I want the story</h3>
<p>Begin with the conjecture, why it seemed plausible, and exactly what changed.</p>
<span>Read the guide →</span>
</a>

<a class="path-card" href="status/">
<span class="path-number">02</span>
<h3>I want to audit it</h3>
<p>See which assertions are formalized, exact, sourced, under review, or open.</p>
<span>Inspect the evidence →</span>
</a>

<a class="path-card" href="open-questions/">
<span class="path-number">03</span>
<h3>I want to work on it</h3>
<p>Explore the surviving plane problem, degree questions, geometry, and formalization tasks.</p>
<span>Find an open problem →</span>
</a>

</div>

!!! note "Fast-moving record"
    This guide is current as of **21 July 2026**, two days after the public
    announcement. It distinguishes exact verification from historical priority
    and ordinary mathematical review. [Corrections are welcome](contribute.md).

