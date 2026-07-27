---
title: "Local Rigidity and Deformation Algebra"
description: "The counterexample sits in a large formal deformation space; which deformations survive polynomial equivalence?"
---

# Local Rigidity and Deformation Algebra

<p class="dek">The counterexample sits in a large formal deformation space; which deformations survive polynomial equivalence?</p>

<span class="status status-draft">Working research program</span>

## The mathematical idea

A counterexample can be locally rigid as a bounded-degree polynomial map even though étaleness makes its unrestricted formal deformation theory look trivial.  The difference is the high-order incidence of a formal source orbit with a finite degree cutoff.

## For a first reading

This program fixes the degree-seven counterexample, removes the obvious affine symmetries, and asks what infinitesimal directions remain.  It then follows those directions through successive orders until the local parameter algebra closes.

## The proof strategy

A weighted transverse slice reduces the calculation to ten parameters.  Exact Kuranishi equations define a finite local Artin algebra; its Hilbert function, inverse system, socle, and minimal equations encode the residual scheme-theoretic multiplicity.  Root coordinates identify the source-flow complex with a weighted divergence operator.

## Scope and current boundary

The claims concern a specified bounded-degree quotient and do not rule out degree-increasing or unrestricted polynomial deformations. The exact computations are internally reproduced but need an independent computer-algebra implementation and expert review; a different-filtered reconstruction remains an open target.

## Working manuscript

[Download the versioned PDF](../../assets/manuscripts/03-filtered-rigidity-2026-07-22-v9.pdf){ .md-button .md-button--primary }

Nathaniel Monson · manuscript dated 2026-07-22 · 19 pages · SHA-256 `22da71697b659c4fe0938298f0c2e11b38db93e2e0ad322e95e92668943aad00`

[Download the version-8 archival edition](../../assets/manuscripts/03-filtered-rigidity-2026-07-22-v8.pdf) — complete pre-reader edition · SHA-256 `3952e45a73874c0822bc2b691d6c0020b87c498d66bd16bb7a99911bc70c7e49`

[Open the companion Results and Research Register](../../assets/manuscripts/07-results-and-research-register-2026-07-22-v9.pdf)

The reader PDF contains this program's selected theorem spine. The companion register preserves secondary results, open problems, corrections, and evidence boundaries. Together with the version-8 archival edition, it supplies statement-level coverage for every program-relevant assigned record. Current page-level coverage: complete 5.

## Computational and technical materials

Exact reduced-rigidity, border-basis, multiplication, inverse-system, and Koszul data used by Program 3.

- [Complete computational supplement](../../assets/technical-materials/03-local-rigidity-computational-supplement.zip) — 5.6 MB; Exact reduced-rigidity, border-basis, multiplication, inverse-system, and Koszul data used by Program 3. Boundary: This concerns the stated bounded-degree filtered quotient and has not been independently reproduced in a second computer-algebra system. SHA-256 `e2b0a05261d49497eda4d3ca856f948e3e2205768ef4d453a66e546653717782`

[Browse all technical materials](../materials.md)

## Results in this program

### [Degree Eight Deformations](../../results/degree-eight-deformations.md)

For the degree-eight local Kuranishi problem, the residual 28-dimensional slice reduces to weights -2 and -1; weight -2 is eliminated over Q, while weight -1 survives to fourth order and has only modular death evidence at order six.

### [Degree Seven Local Affine Rigidity](../../results/degree-seven-local-affine-rigidity.md)

A torus-stable 337-dimensional slice has ten tangent parameters of weights (-1,2,-3,-2,-1,0,1,1,2,3); exact positive, negative, and fixed-weight obstruction certificates plus a torus-nullcone lemma show that its reduced completed local ring is C. Thus G is reduced-affinely rigid in K_{3,7}, though the local ring is a nonreduced Artin thickening.

### [Degree Seven Local Artin Algebra](../../results/degree-seven-local-artin-algebra.md)

The completed local Artin algebra has length 584, nilpotency m^9=0 with m^8 nonzero, and Hilbert function (1,10,44,108,157,145,86,30,3).

### [Formal Right Triviality And Degree Growth](../../results/formal-right-triviality-and-degree-growth.md)

Every formal polynomial Keller deformation of the fixed map is right-trivial as F composed with a formal source automorphism; bounded-degree obstructions come from the degree filtration, not unrestricted formal deformation theory.

## Open problems in this program

### [Open Problems After the Counterexample](../../results/research-agenda.md)

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

[Back to Research](../../research.md)
