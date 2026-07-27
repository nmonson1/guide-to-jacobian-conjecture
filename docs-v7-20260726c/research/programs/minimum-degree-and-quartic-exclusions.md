---
title: "Minimum Degree and Quartic Exclusions"
description: "The counterexample has degree seven; how small can a counterexample be?"
---

# Minimum Degree and Quartic Exclusions

<p class="dek">The counterexample has degree seven; how small can a counterexample be?</p>

<span class="status status-draft">Working research program</span>

## The mathematical idea

Once dimension three is known to admit counterexamples, degree is the next obvious measure of complexity.  The public example has degree seven, so the first serious frontier is whether degree four can already support a noninjective Keller map.

## For a first reading

The program normalizes a hypothetical collision and studies the highest-degree image in projective space.  Point, line, conic, rational-cubic, and rational-quartic images behave differently; each stratum has its own obstruction and its own remaining cases.

## The proof strategy

Keller-jet equations constrain the leading forms.  Geometric classification of the resulting projective curve then turns the Jacobian condition into finite divisibility, valuation, and elimination problems.  The same invariant-gap method now excludes several fixed-factor conic strata in degrees five and six.

## Scope and current boundary

This is not yet an unrestricted proof that quartic counterexamples do not exist.  The page separates completed exclusions from the balanced and tricuspidal quartic frontiers, the binary quintic overlap, and the primitive sextic conic case that remain open.

## Working manuscript

[Download the versioned PDF](../../assets/manuscripts/02-quartic-keller-maps-2026-07-22-v9.pdf){ .md-button .md-button--primary }

Nathaniel Monson · manuscript dated 2026-07-22 · 19 pages · SHA-256 `d2dbe5df785db567aa6a7d4c43ecc799853a85333df806d692b1bbcd68db3bf5`

[Download the version-8 archival edition](../../assets/manuscripts/02-quartic-keller-maps-2026-07-22-v8.pdf) — complete pre-reader edition · SHA-256 `9174ebba7b85603b8647740a73fbba308f6fc3a1910cedaa9c5109701a86ee0e`

[Open the companion Results and Research Register](../../assets/manuscripts/07-results-and-research-register-2026-07-22-v9.pdf)

The reader PDF contains this program's selected theorem spine. The companion register preserves secondary results, open problems, corrections, and evidence boundaries. Together with the version-8 archival edition, it supplies statement-level coverage for every program-relevant assigned record. Current page-level coverage: complete 13, not applicable 1.

## Computational and technical materials

Exact low-degree, conic, rank-one, fixed-factor, and equivariant calculations used by Program 2.

- [Complete computational supplement](../../assets/technical-materials/02-low-degree-computational-supplement.zip) — 119.7 kB; Exact low-degree, conic, rank-one, fixed-factor, and equivariant calculations used by Program 2. Boundary: The unrestricted quartic problem and the balanced and tricuspidal frontiers remain open. SHA-256 `7d99adca689debfeb9439e11d799bde9221301e307def200105b1cfba025c8fa`
- [Cubic-pencil and x²y² Plücker-boundary calculation](../../assets/technical-materials/02-quartic-plucker-x2y2-boundary-2026-07-26-v1.zip) — 14.5 kB; Exact scripts, outputs, and notes for the x²y² boundary calculation. Boundary: The fixed-component boundary pencil remains unresolved. SHA-256 `88c69f53e11cc1f36a73333979e199f87d52e95d6589fe2de0cb747eb1ac4065`

[Browse all technical materials](../materials.md)

## Results in this program

### [Bounded Degree Keller Scheme](../../results/bounded-degree-keller-scheme.md)

For fixed n,D, normalized determinant-one polynomial maps form a finite-type coefficient scheme K_{n,D}; its tangent equation at F is the coefficientwise vanishing of tr((JF)^{-1} JH), equivalently the differential of det J.

### [Collision Normalized Finite Search](../../results/collision-normalized-finite-search.md)

After collision normalization, fixed-degree Keller counterexample searches become finite coefficient schemes; the message gives concrete variable counts for D=4,5,6 and recommends exact elimination or modular-to-rational computation.

### [Excluding Every Conic Leading Image in Degree Four](../../results/quartic-conic-leading-image-exclusion.md)

No quartic Keller map in three variables has a nondegenerate conic as the projective image of its highest homogeneous part.

### [Excluding Rational-Cubic Leading Images in Degree Four](../../results/quartic-rational-cubic-leading-image-exclusion.md)

No quartic Keller map in three variables has a nondegenerate rational cubic as the projective image of its highest homogeneous part.

### [Fixed-Factor Conic Exclusions in Degrees Five and Six](../../results/degree-five-six-fixed-factor-conics.md)

The invariant-gap method excludes the basepoint-free fixed-factor conic strata of degrees five and six, and a local normal-form argument also excludes the genuine three-variable cubic-factor quintic.

### [Leading Curves and Normal Resonance at Infinity](../../results/quartic-leading-curves-at-infinity.md)

For a quartic Keller deformation of a leading curve, the first nonzero normal coefficient below determinant order nine can occur only at an order divisible by the homogeneous period; in the primitive period-four case the first three normal coefficients vanish.

### [Ramification and the Rational-Quartic Frontier](../../results/quartic-rational-quartic-frontier.md)

Projective duality bounds the ramification degree of a proper rational plane quartic by three; combined with the Keller exclusions, the only remaining rational-quartic leading strata are (deg gamma, tangent-syzygy type)=(2,(2,2)) and (3,(1,2)).

### [Rank One Quartic Theorem](../../results/rank-one-quartic-theorem.md)

If the quartic highest homogeneous part of a degree-at-most-four three-variable Keller map has target span one, then the map is a polynomial automorphism.

### [The Remaining Leading-Line Geometry in Degree Four](../../results/quartic-leading-line-reductions.md)

In the primitive coprime quartic leading-line case, the surviving normal-degree-three valuation pattern is uniquely the partition 2+1, reducing the leading data to H4=(ell^4,q2^2,0) and (H3)3=ell q2 with ell not dividing q2.

## Open problems in this program

### [Can the Tricuspidal Quartic Be a Keller Leading Image?](../../results/tricuspidal-quartic-leading-image-problem.md)

Can the tricuspidal quartic be excluded as the projective leading image of a quartic Keller map by analyzing its explicit type-(1,2) tangent-syzygy basis?

### [Open Problems After the Counterexample](../../results/research-agenda.md)

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

### [The Balanced Rational-Quartic Leading-Image Problem](../../results/balanced-quartic-leading-image-problem.md)

Can the balanced ramification-degree-two tangent-syzygy stratum (2,(2,2)) be excluded as a rational-quartic leading image of a quartic Keller map?

### [The Degree-Five and Degree-Six Conic Frontier](../../results/degree-five-six-conic-frontier.md)

After the fixed-factor exclusions, the conic frontier is concentrated in three explicit boundary problems: the binary cubic-factor quintic, quintic basepoint strata, and the primitive sextic conic.

### [Unrestricted Quartic Open Package](../../results/unrestricted-quartic-open-package.md)

The unrestricted degree-four problem, and hence the exact value of D_min within the public 4-to-7 range, remains open in this conversation.

[Back to Research](../../research.md)
