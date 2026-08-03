# Quadratic-frame effectivity staircase and stable non-effectivity

`RMU-3FEF0011` · `theorem`

## Mathematical record

`RMU-3FEF0011` · `theorem`

For A_alpha(c)=c(1+alpha c), B_(alpha,q)(c)=-2-4alpha c+q alpha^2 c^2 over a commutative Q-algebra, a c-fixed framed root translation of c-degree at most D from q to q' exists exactly when (q'-q)alpha^(D+2)=0; it is unique and has residual (-1)^D(q'-q)alpha^(D+2)c^(D+2). For alpha=s modulo s^M and q!=q', the minimal framed degree is M-2. Over C[[s]], all Artin truncations are compatibly ordinarily left-right equivalent, but the complete families are not stably polynomially left-right equivalent. Their unrestricted stable-equivalence complexity diverges, with the explicit lower bounds in the proof.

Hypotheses:

- The cubic-frame maps and framed root-translation groupoid are exactly those defined in the linked theorem.
- The stable generic-fiber separation uses the proved stable q-classification RMU-9075E072.
- The quantitative unrestricted bound uses the cited parametric effective Nullstellensatz of D'Andrea--Krick--Sombra.

Dependencies:

- `depends_on` [`RMU-9075E072`](../units/RMU-9075E072.md): The generic-fiber contradiction uses the complete stable q-classification as a proved theorem.

Support:

- **proof:** Coefficient recursion, orbit cokernel, Artin staircase, finite-type generic-fiber descent and effective Nullstellensatz argument. — `research-notes/lane3-formal-effectivity/formal_effectivity_theorem.md`
  - Does not establish: A universal effectivity theorem outside the displayed family.
- **program:** Main and independent exact staircase computations plus the effective-bound calculation. — `research-notes/lane3-formal-effectivity/verify_formal_effectivity.py`
  - Does not establish: The conventional stable-classification proof.

Limitations:

- The theorem is not a formal-effectivity statement for every Keller-map family.
- The sharp linear unframed degree-growth rate remains open.

## Attribution

- Credit: Model-generated public-site PR 6
- Citation: D'Andrea-Krick-Sombra parametric effective Nullstellensatz as cited in the proof packet
