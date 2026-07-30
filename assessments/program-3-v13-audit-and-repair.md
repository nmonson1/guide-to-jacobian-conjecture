# Program 3 v13 audit and repair record

## Record

- **Object reviewed:** Nathaniel Monson, *Filtered Rigidity of the Degree-Seven Jacobian Counterexample: A Transverse Algebra of Length 584*.
- **Pinned public artifact:** `03-filtered-rigidity-2026-07-29-v13.pdf`.
- **SHA-256:** `18f4658390d0a9566056aee505c3fb5039d17969368cb2f544a44e6ba956f427`.
- **Release metadata date:** 29 July 2026.
- **Date printed inside the PDF:** 22 July 2026.
- **Assessor:** GPT-5.6 Pro (OpenAI), acting as an AI mathematical auditor.
- **Requested by:** Nathaniel Monson.
- **Assessment date:** 30 July 2026.
- **Review class:** exact rational symbolic spot-check plus proof audit. This is not independent human specialist review and is not a second-CAS reproduction of the large certificates.

## Methods and checked scope

Fresh exact symbolic reconstructions checked the displayed Keller identity, the stabilizer torus, the eleven-dimensional affine-orbit minor, the determinant-linearization rank, the ten tangent coordinates, the eleven-dimensional quadratic obstruction space, the fixed-weight cubic obstruction, the generic-cubic discriminants, the marked-root identities, and the quadratic source-shear formula.

The companion script `program-3-v13-repair-checks.py` replays the elementary identities needed for Appendix C.1 and the replacement proof of Theorem C.2. It does not replay the large radical, inverse-system, Koszul, border-basis, or terminal-order certificates.

## Conclusion

The degree-seven theorem spine survives the audit. No fatal defect was found in the degree-seven argument, and the independently reconstructed exact calculations agreed with the manuscript.

Five repairs are required in the public exposition:

1. add a proof that the generic cubic in Proposition 2.1 is irreducible;
2. state the finite-type/completion bridge used in Theorem 4.3;
3. replace the invalid truncation argument in the converse of Theorem C.2;
4. withdraw the characteristic-zero conclusion of Theorem C.3 beyond exact weight `-2` elimination and exact order-four weight `-1` persistence;
5. state that Appendix D is a post-length exact presentation as proved, not an independent route to the upper bound.

Theorem C.2 remains valid with the replacement proof in the public corrigendum. The v13 formulation of Theorem C.3 does not remain valid as an exact characteristic-zero theorem.

## Repair summary

### Proposition 2.1

For `p(v)=cv^3-2v^2+bv-2a`, use the valuation at `a=infinity`. If a rational root has valuation `m>=0`, the term `-2a` has the unique least valuation. If `m<0`, the four valuations are `3m,2m,m,-1`, and cancellation of the least term would require `3m=-1`, impossible for integral `m`. Thus the cubic is irreducible. Together with the printed nonsquare discriminant, this gives normal-closure group `S_3` and a trivial automorphism group for the cubic subextension.

### Theorem 4.3

Formal implicit elimination identifies the completion of the finite-type slice with the Kuranishi quotient. Completion commutes with the pure-weight closed intersections, is faithfully flat, and preserves Krull dimension. Artinian completed pure-weight intersections therefore imply zero-dimensional finite-type local intersections, to which the torus-nullcone lemma applies.

### Theorem C.2

Write `G_f=G o phi_f`, where `phi_f(x,y,z)=(x,y,z+f(x,y))`. An affine equivalence `G_f o alpha=beta o G_g` preserves the common omitted curve, hence `beta` lies in the target stabilizer torus. Equivariance and the trivial generic deck group imply `phi_f o alpha=A_mu o phi_g`. Consequently

```
alpha(x,y,z)=(mu^-1 x, mu y,
              mu^2 z + mu^2 g(x,y) - f(mu^-1 x,mu y)).
```

This is affine exactly when `mu^2 g(x,y)=f(mu^-1 x,mu y)`, equivalently

```
g(x,y)=tau^2 f(tau x,tau^-1 y).
```

The v13 claim that an arbitrary affine equivalence preserves the degree-seven truncation is deleted.

### Theorem C.3

The exact public boundary is:

- residual weights `-2` and `-1`;
- exact rational elimination of weight `-2`;
- exact persistence of weight `-1` through order four;
- later death calculations are modular evidence only.

The v13 order-six/order-seven characteristic-zero rejection and its first-normal conclusion are withdrawn. Full orbit saturation remains open, including arcs that bend out of a restricted slice.

### Appendix D

Commuting multiplication matrices give `dim S/J <= 584`. The printed inclusion `J subset I_kappa` uses 584 inverse-system functionals as the full inverse system; their fullness uses the already-established length 584. Appendix D is therefore a valid exact post-length presentation and consistency check, but not an independent upper-bound route as written.

## Open objections and release gates

1. Reproduce the degree-seven radical certificate, `H(6)=86`, and uniqueness of the sextic initial class in Singular or Macaulay2 from independently derived equations.
2. Replace the v13 PDF in a subsequent manuscript release, or keep the corrigendum conspicuously attached everywhere v13 is linked.
3. Correct the canonical private claim source for `JCG-24C82405`; changing only generated public pages is not durable.
4. Add direct Kuranishi-ideal membership certificates for the border relations before advertising Appendix D as an independent upper bound.

The reader-facing replacement statements and full proofs are in `docs-v20-20260730a/research/program-3-v13-corrigendum.md`.
