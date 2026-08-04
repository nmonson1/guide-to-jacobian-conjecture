---
title: "Exact root-divisibility coordinates for the degree-125 F2 linear descent"
description: "For the fixed denominator-five shear in the degree-125 F2 chain (5,20)->(7/5,2), every one of the 76 P-blocks and 126 Q-blocks has exact root-divisibility coordinates: the forbidden terminal-coefficient jet map has full row rank, and the surviving source coefficients give triangular coordinates with an explicit inverse. Thus the linear descent has 533+1440=1973 free coordinates on 4433+12340=16773 allowed positions and exactly 3900+10900=14800 inherited linear relations. The leading common-power multiplicities and the quotient-coordinate determinant operator are compatible with these coordinates."
---

# Exact root-divisibility coordinates for the degree-125 F2 linear descent

`JCG-66D861AF` · `theorem` · statement version `3`

## Exact statement

For the fixed denominator-five shear in the degree-125 F2 chain (5,20)->(7/5,2), every one of the 76 P-blocks and 126 Q-blocks has exact root-divisibility coordinates: the forbidden terminal-coefficient jet map has full row rank, and the surviving source coefficients give triangular coordinates with an explicit inverse. Thus the linear descent has 533+1440=1973 free coordinates on 4433+12340=16773 allowed positions and exactly 3900+10900=14800 inherited linear relations. The leading common-power multiplicities and the quotient-coordinate determinant operator are compatible with these coordinates.

## Hypotheses

- The source and terminal coefficient orders, denominator-five shear, P/Q weight blocks, and forbidden support masks are exactly those in research-notes/lane8-f2-root-divisibility-20260804-v1/block_manifest.json.
- The calculation is over characteristic zero; the displayed Vandermonde witnesses use pairwise distinct integer evaluation points.

## Applies to

- The complete linear root-divisibility stage for all 202 blocks of the fixed F2 shear.
- Exact sparse parametrization of the 14,800 inherited linear relations without materializing a dense relation matrix.

## Limitations

- It does not impose the nonlinear common-power, double-root, determinant, nonvanishing, or support-stratum conditions.
- It does not prove the forward and inverse constructible-locus correspondence or supply adjacent-chart attachment data.
- It is not an obstruction to the existence of the complete F2 chain.

## Arguments

### Root-divisibility gives triangular coordinates on every F2 linear block

`ARG-L8-F2-ROOT-DIVISIBILITY` · `proof`

Each forbidden output tail is one Taylor jet of the source block at the shear parameter; a Vandermonde minor proves full row rank, and the complementary source coefficients give an explicit triangular inverse.

Write a homogeneous source block as C_s(u,v)=sum_j c_(s,j)u^(n_s-j)v^j and substitute the fixed denominator-five shear. For each terminal forbidden interval, the resulting output coefficients are the value and successive derivatives of the associated one-variable polynomial at the shear parameter, up to explicit nonzero binomial and monomial factors. A square minor obtained by evaluating successive monomials at distinct integer points is Vandermonde and nonzero, so every forbidden-block jet map has full row rank. Choose the complementary source columns in the manifest. Ordered by terminal weight, the map from those columns to the allowed output coordinates is triangular with nonzero diagonal; backward substitution gives the displayed inverse. Summing the verified per-block ranks over 76 P-blocks and 126 Q-blocks yields 533 and 1440 free coordinates, while the support masks contain 4433 and 12340 allowed positions. The differences 3900 and 10900 are the inherited linear relation counts. Direct substitution in these coordinates verifies the leading common-power multiplicities and the quotient-coordinate determinant operator.

Does not establish:

- The nonlinear complete-chain locus or its support stratification.
- Any adjacent-chart attachment or global obstruction theorem.

## Evidence and source access

### Exact 202-block root-divisibility certificate

`EVD-L8-F2-ROOT-DIVISIBILITY-20260804` · `certificate`

The independent checker rebuilds every block map and verifies its forbidden rank, triangular inverse, support counts, leading multiplicity, and quotient-operator identities.

**Establishes:** The exact linear statement of JCG-66D861AF version 2 and the proof steps in ARG-L8-F2-ROOT-DIVISIBILITY.

**Source:** [Open the published source](../../handoffs/lane-8-source-packet.md)

Replay commands:

- `uv run python -B research-notes/lane8-f2-root-divisibility-20260804-v1/verify_f2_root_divisibility.py`

Does not establish:

- Nonlinear common-power, double-root, determinant, open, or support-stratum conditions.
- The constructible-locus equivalence or adjacent-chart attachment.

### Exact maximal support and order-520 public bundle

`EVD-L89-F2-SUPPORT-AND-520` · `certificate`

The hash-pinned public bundle contains the full support inventory, exact linear complexes, rational order-520 generator, certificate, and verifier.

**Establishes:** The 4433/12340 support counts, 2681 output layers, first external window 510, and exact cancellation omega510=omega520=0 in the retained weighted slice.

**Source:** [Open the published source](../../handoffs/lane-8-source-packet.md)

Does not establish:

- That the independent-coefficient enlargement is the actual complete-chain chart.

### version-8 supplementary statement with explicit evidence boundary

`SUP-JCG66D861AF-01` · `source_assertion`

version-8 supplementary statement with explicit evidence boundary

**Establishes:** The located source records this statement and its stated evidence boundary.

**Source:** [Open the published source](../../proof-sources/06-plane-boundary/appendices/additional-results-and-leads.md#label-supp-note-06-033)

[Machine-readable graph](../graph.json)
