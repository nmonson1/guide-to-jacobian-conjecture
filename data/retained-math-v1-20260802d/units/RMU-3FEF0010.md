# Quadratic-frame effectivity staircase and conditional stable non-effectivity

`RMU-3FEF0010` · `theorem`

## Mathematical record

`RMU-3FEF0010` · `theorem`

For A_alpha(c)=c(1+alpha c), B_(alpha,q)(c)=-2-4alpha c+q alpha^2 c^2 over a commutative Q-algebra, a c-fixed framed root translation of c-degree at most D from q to q' exists exactly when (q'-q)alpha^(D+2)=0; it is unique and is the displayed truncated geometric series, with exact residual (-1)^D(q'-q)alpha^(D+2)c^(D+2). For alpha=s modulo s^M and q!=q', the minimal framed degree is M-2. Over C[[s]], all Artin truncations are compatibly equivalent but no polynomial framed equivalence exists. Assuming the recorded stable q-classification of nonzero-alpha fibers, no stable polynomial left-right equivalence exists on the generic fiber; with the cited effective Nullstellensatz, unrestricted equivalence complexity diverges and obeys the stated logarithmic lower bound.

Hypotheses:

- The cubic-frame maps and framed root-translation groupoid are those defined in the linked theorem.
- The exact annihilator and degree law is unconditional over a commutative Q-algebra.
- The unframed stable conclusion assumes the separately recorded stable q-classification; the quantitative unrestricted bound also uses the cited parametric effective Nullstellensatz.

Support:

- **proof:** Coefficient recursion, orbit-cokernel calculation, Artin staircase and conditional generic-fiber/effective argument. — `research-notes/lane3-formal-effectivity/formal_effectivity_theorem.md`
  - Does not establish: The stable q-classification or effective Nullstellensatz used as inputs.
- **program:** Main and independent exact staircase computations plus the effective-bound calculation. — `research-notes/lane3-formal-effectivity/verify_formal_effectivity.py`
  - Does not establish: The external classification and literature theorem.

Limitations:

- The theorem is not a formal-effectivity result for every Keller-map family.
- Its strongest unframed conclusions are conditional on named external mathematical inputs, not on the CAS replay alone.

## Attribution

- Credit: Model-generated public-site PR 6
- Citation: D'Andrea-Krick-Sombra parametric effective Nullstellensatz as cited in the proof packet
