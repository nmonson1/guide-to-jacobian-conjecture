---
title: "Quadratic-frame effectivity staircase and stable non-effectivity"
description: "For A_alpha(c)=c(1+alpha c), B_(alpha,q)(c)=-2-4alpha c+q alpha^2 c^2 over a commutative Q-algebra, a c-fixed framed root translation of c-degree at most D from q to q' exists exactly when (q'-q)alpha^(D+2)=0; it is unique and has residual (-1)^D(q'-q)alpha^(D+2)c^(D+2). For alpha=s modulo s^M and q!=q', the minimal framed degree is M-2. Over C[[s]], all Artin truncations are compatibly ordinarily left-right equivalent, but the complete families are not stably polynomially left-right equivalent. Their unrestricted stable-equivalence complexity diverges, with the explicit lower bounds in the proof."
---

# Quadratic-frame effectivity staircase and stable non-effectivity

`RMU-3FEF0011` · `theorem` · statement version `2`

## Exact statement

For A_alpha(c)=c(1+alpha c), B_(alpha,q)(c)=-2-4alpha c+q alpha^2 c^2 over a commutative Q-algebra, a c-fixed framed root translation of c-degree at most D from q to q' exists exactly when (q'-q)alpha^(D+2)=0; it is unique and has residual (-1)^D(q'-q)alpha^(D+2)c^(D+2). For alpha=s modulo s^M and q!=q', the minimal framed degree is M-2. Over C[[s]], all Artin truncations are compatibly ordinarily left-right equivalent, but the complete families are not stably polynomially left-right equivalent. Their unrestricted stable-equivalence complexity diverges, with the explicit lower bounds in the proof.

## Hypotheses

- The cubic-frame maps and framed root-translation groupoid are exactly those defined in the linked theorem.
- The stable generic-fiber separation uses the proved stable q-classification RMU-9075E072.
- The quantitative unrestricted bound uses the cited parametric effective Nullstellensatz of D'Andrea--Krick--Sombra.

## Applies to

- The displayed one-parameter quadratic-modulus cubic-frame family and its framed Artin truncations.
- The unrestricted stable groupoid of the two pointed arcs over C[[s]].

## Limitations

- The theorem is not a formal-effectivity statement for every Keller-map family.
- The sharp linear unframed degree-growth rate remains open.

## Arguments

### Quadratic-frame effectivity staircase and stable non-effectivity

`ARG-L3-FORMAL-EFFECTIVITY` · `proof`

Coefficient recursion gives the exact framed Artin staircase; generic-fibre separation and an effective Nullstellensatz turn it into unrestricted stable non-effectivity and complexity divergence.

For a c-fixed root translation phi, the frame equation is 3c(1+alpha c)phi=(q'-q)alpha^2c^2. Coefficient comparison forces the finite geometric series and leaves the single terminal condition (q'-q)alpha^(D+2)=0, proving existence, uniqueness, the residual formula, and the exact degree M-2 over C[s]/(s^M). These compatible Artin translations do not algebraize over C[[s]] because the stable q-classification separates the two nonzero-alpha generic fibres. If unrestricted stable equivalences had uniformly bounded complexity, a finite coefficient scheme and generic-combination reduction would produce a generic-fibre equivalence; the cited parametric effective Nullstellensatz quantifies this contradiction and yields the recorded lower bounds.

Premise units:

- [`RMU-9075E072`](RMU-9075E072.md)

Does not establish:

- A formal-effectivity theorem for arbitrary Keller-map families.
- A sharp linear lower bound for unrestricted stable-equivalence complexity.

## Evidence and source access

### Exact formal-effectivity identity and finite-grid checks

`EVD-L3-FORMAL-EFFECTIVITY-CHECKS` · `program`

Three independently retained reports verify the symbolic root-translation identities, finite residual and ramification grids, coefficient bookkeeping, and finite effective-bound inequalities.

**Establishes:** The executable algebraic identities and finite combinatorial checks used inside ARG-L3-FORMAL-EFFECTIVITY.

**Source:** [Open the published source](../../handoffs/lane-3-source-packet.md)

Does not establish:

- Generic-fibre stable separation, the generic-combination lemma, or the external Nullstellensatz.

### Complete formal-effectivity proof

`EVD-L3-FORMAL-EFFECTIVITY-PROOF` · `proof`

The theorem note proves the coefficient recursion, orbit cokernel, ramified staircase, complete-base non-effectivity, and quantitative complexity bounds with external dependencies explicit.

**Establishes:** The full statement of RMU-3FEF0011.

**Source:** [Open the published source](../../handoffs/lane-3-source-packet.md)

Does not establish:

- The stable q-classification or external effective Nullstellensatz used as dependencies.

### Coefficient recursion, orbit cokernel, Artin staircase, finite-type generic-fiber descent and effective Nullstellensatz argument.

`SUP-RMU3FEF0011-01` · `proof`

Coefficient recursion, orbit cokernel, Artin staircase, finite-type generic-fiber descent and effective Nullstellensatz argument.

**Establishes:** The exact framed criterion, complete-base stable non-effectivity and quantitative unrestricted complexity bounds.

**Source:** [Open the published source](../../handoffs/lane-3-source-packet.md)

Does not establish:

- A universal effectivity theorem outside the displayed family.

### Main and independent exact staircase computations plus the effective-bound calculation.

`SUP-RMU3FEF0011-02` · `program`

Main and independent exact staircase computations plus the effective-bound calculation.

**Establishes:** The coefficient identities, degree staircase and finite effective estimates.

**Source:** [Open the published source](../../handoffs/lane-3-source-packet.md)

Does not establish:

- The conventional stable-classification proof.

## Mathematical connections

- `depends_on` [`RMU-9075E072`](RMU-9075E072.md) — The generic-fiber contradiction uses the complete stable q-classification as a proved theorem.

## Attribution and citations

- Credit: Model-generated public-site PR 6
- Citation: D'Andrea-Krick-Sombra parametric effective Nullstellensatz as cited in the proof packet

[Machine-readable graph](../graph.json)
