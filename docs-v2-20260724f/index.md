---
title: "The Jacobian Conjecture: A Living Guide"
description: "A reader-first guide to the counterexample, its geometry, the surviving plane case, and the research it has opened."
---

<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">Unannounced working draft</p>
    <h1>The Jacobian Conjecture: A Living Guide</h1>
    <p>A reader-first account of the explicit counterexample, the geometry that makes it work, the two-dimensional problem that survives, and the research directions now taking shape.</p>
    <div class="hero-actions">
      <a class="md-button md-button--primary" href="counterexample/">See the counterexample</a>
      <a class="md-button" href="geometry/">Understand the geometry</a>
    </div>
  </div>
  <div class="formula-card">
    <p class="card-kicker">The question in one line</p>
    <p class="display-question">
      \[
      \begin{gathered}
      \det DF\in\mathbf C^\times\\
      \Downarrow\ ?\\
      F^{-1}\text{ polynomial}
      \end{gathered}
      \]
    </p>
    <p>No in dimensions \(n\geq 3\). Still open in dimension \(2\).</p>
  </div>
</section>

<div class="verdict-strip">
  <div>
    <span class="dimension">Dimension 1</span>
    <strong>True</strong>
    <p>A polynomial with nonzero constant derivative is linear.</p>
  </div>
  <div>
    <span class="dimension open">Dimension 2</span>
    <strong>Open</strong>
    <p>The classical plane Jacobian conjecture remains unresolved.</p>
  </div>
  <div>
    <span class="dimension false">Dimensions 3+</span>
    <strong>False</strong>
    <p>An explicit three-variable map stabilizes to every higher dimension.</p>
  </div>
</div>

!!! warning "Working draft"
    This site is public but has not been announced. Its research pages include
    unrefereed proof drafts and may contain errors. Every page is currently
    marked `noindex`; that reduces search-engine discovery but does not make
    the site private.

## Choose a path

<div class="path-grid path-grid-four">
  <a class="path-card" href="counterexample/">
    <span class="path-number">01</span>
    <h3>The exact map</h3>
    <p>Read the polynomial formula, determinant calculation, collision, credit chain, and dimensional consequence.</p>
    <span>Counterexample →</span>
  </a>
  <a class="path-card" href="geometry/">
    <span class="path-number">02</span>
    <h3>Why it works</h3>
    <p>Replace a miraculous formula by a marked-root cover with three generic sheets and a carefully chosen affine source.</p>
    <span>Geometry →</span>
  </a>
  <a class="path-card" href="plane-case/">
    <span class="path-number">03</span>
    <h3>Why the plane survives</h3>
    <p>Separate established literature from current attempts to understand why the three-dimensional mechanism does not descend.</p>
    <span>Plane case →</span>
  </a>
  <a class="path-card" href="research/">
    <span class="path-number">04</span>
    <h3>What comes next</h3>
    <p>Browse six working research programs, 71 result pages, 16 open problems, and six dated manuscripts.</p>
    <span>Research →</span>
  </a>
</div>

## The short version

The Jacobian conjecture asked whether a polynomial map
\(F:\mathbf C^n\to\mathbf C^n\) with nonzero constant Jacobian determinant
must be a polynomial automorphism. In July 2026, an explicit polynomial map
\(\mathbf C^3\to\mathbf C^3\) was announced with determinant \(-2\) and three
distinct points sharing one image. Those two checks disprove the conjecture in
dimension three; adjoining identity coordinates gives counterexamples in every
higher dimension.

The formula is easy to verify but hard to understand in isolation. Its natural
form is a map that remembers a simple root of a binary cubic and then forgets
which root was marked. A generic cubic has three choices. The surprising step
is that one carefully chosen slice of this incidence construction has source
\(\mathbf A^3\).

[Read the complete formula and direct checks](counterexample.md){ .md-button .md-button--primary }

## What is in the guide

The six pages in the main navigation are written for readers. Beneath them is
a generated publication layer with one page for each theorem-level result or
open problem. Each page keeps statement, credit, evidence, source treatment,
and connections separate. The deeper atomic records are available only from
those pages; they are absent from navigation and search.

The six Nathaniel Monson-led research programs are deliberately labeled as
working drafts. Their HTML summaries explain the question, the proof strategy,
and the current gap; their dated PDFs preserve the mathematical detail.

## Latest update

**24 July 2026, Pacific time.** This draft introduces the six-section reading
structure, the sanitized 87-page result catalogue, and freshly compiled
versioned editions of all six research manuscripts.
