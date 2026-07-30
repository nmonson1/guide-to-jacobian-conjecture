---
title: "Program 4 six-obligation research packet"
description: "An AI-assisted research packet on exact escape charts, weighted graph boundaries, nonunit resultants, hidden automorphisms, and cross-length Torelli."
---

# Program 4: six proof obligations

**Prepared:** 29 July 2026  
**Status:** unrefereed research packet.  
**Independent review:** none recorded.  
**AI assistance:** GPT-5.6 Pro was used for mathematical exploration, proof drafting, symbolic-program design, and packet preparation. Nathaniel Monson remains responsible for every submitted assertion.

This packet pushes the six obligations identified after the initial weighted-graph sprint to a theorem, an exact counterexample, or a sharply localized remaining gap. It concerns normalized cubic-frame coefficient spaces and the public Program 4 setup. It does **not** claim that the proposed degeneration stack is the fppf orbit quotient or the full unrigidified stable left-right quotient.

## Results

| # | Obligation | Result |
|---:|---|---|
| 1 | Independence of local Hensel/factorization coordinates | Proved on every exact escape stratum: the cluster factor and principal part are canonical in the formal neighborhood and commute with base change. |
| 2 | Coefficient-level representability under arbitrary base change | A fixed, unnormalized, stacky multigraded graph algebra gives a finite-type proper separated coefficient-level object. Normalization is deliberately excluded from the functor. |
| 3 | Scheme-theoretic `N=3` direct-versus-iterated overlap | The hoped-for equality is false: the ordered refinement is `Bl_(u^2,v)` of the direct chart and has exceptional fibre `P^1`. |
| 4 | Nonunit-resultant and relative-Jacobian compatibility | Proved on every exact contact stratum without a unit-resultant hypothesis; arbitrary-family simultaneous flattening remains. |
| 5 | Hidden automorphism kernel | Vanishing is proved conditional on the finite-cover reformulation and boundary exact sequence already stated in the Program 4 technical note. |
| 6 | Cross-length Torelli comparison | Exact-stratum gluing is proved, while injectivity into special-fibre orbit classes is disproved; unframed family-valued descent remains open. |

## Files

1. [Formal coordinate independence](01-formal-coordinate-independence.md)
2. [Coefficient degeneration stack](02-coefficient-degeneration-stack.md)
3. [`N=3` overlap counterexample](03-n3-overlap-counterexample.md)
4. [Nonunit resultants and relative-Jacobian compatibility](04-nonunit-relative-jacobian.md)
5. [Hidden-kernel reduction](05-hidden-kernel.md)
6. [Cross-length Torelli comparison](06-cross-length-torelli.md)

Replay material:

- [Exact SymPy checks](checks.py)
- [Captured successful output](checks-output.txt)
- [SHA-256 manifest](MANIFEST.sha256)

## Main correction

The primary global object should not be a normalized scheme-theoretic image of an iterated weighted blowup. The packet proposes the unnormalized stacky closure of all direct and nested weighted direction maps at once, defined by one fixed multigraded algebra. The first nontrivial two-root calculation shows that direct and ordered iterated charts are related by a nontrivial blowdown rather than equality.

## Verification boundary

The replay script verifies the displayed low-rank polynomial identities, the Hensel Jacobian, the explicit inverse bounded map, the nested `v/u^2` coordinate, the Rees equation, nonunit gauge identities, Fitting ideals, the valuation formula, cusp coordinates, and the one-root noninjectivity family.

It does not independently prove the geometric source results concerning normalization lifting, fixed-frame Torelli, stable-cylinder rigidity, the finite-cover boundary exact sequence, simultaneous flattening, or family-valued descent.

## References

1. Nathaniel Monson, *Boundary Rigidity and Stable Moduli*, version 13, 29 July 2026.
2. Nathaniel Monson, *Finite Triple Covers and Rigidified Moduli*, technical material version 1, July 2026.
3. Program 4 model research brief, *Stable Moduli*.
4. J. Blanc and I. Stampfli, *Automorphisms of the Plane Preserving a Curve*, Algebraic Geometry 2 (2015), 193–213.
5. The Stacks Project, relative Proj and base change; Fitting ideals; normalization and smooth base change.
