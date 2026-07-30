# Boundary Belyi Covers and a Degree-296 Obstruction — Readiness

**Assessment date:** July 24, 2026  
**Author:** Nathaniel Monson  
**Manuscript date:** July 24, 2026, revised proof draft

## Current state

This is a compiled computer-assisted proof draft with a complete exact
supplement for its local terminal-model theorem.  It is not yet a submission
release because the upstream Newton/support/normalization chain has not been
independently audited.

The manuscript now proves, for the explicitly defined systems:

1. the lattice-gap quotient and its Belyi passport;
2. exact Hurwitz counts `1,1,1,2,2` for the first five quotient problems;
3. infinitesimal rigidity of the explicit quotient points modulo source scaling;
4. the universal normal-layer operator and its logarithmic gauge normal form;
5. the filtered principal-part interpretation of every layer left-null vector;
6. reconstruction of the fifteen exact compatibility equations as residue pairings;
7. the boundary-transport derivation of the classical truncated-binomial Shabat family;
8. exact mixed volume `MV(A,B,C,C,C)=296` for the five selected partial-gluing equations;
9. BKK nondegeneracy by exhausting all 344 proper toric faces, including 74 nontrivial saturated Laurent unit-ideal checks;
10. a complete reduced 296-dimensional special algebra at `p=2053, u=216`;
11. characteristic-zero finite-etale lifting of the 296-point partial-gluing scheme; and
12. invertibility of the sixth selected obstruction, hence no common zero of the six exact polynomials.

## Exact replay status

The final replay regenerates and verifies:

- the residue audit through layer 8;
- the mixed-volume and sparse-resultant multidegree certificates;
- all denominators and all 352 selected coefficients at the good split prime;
- the 296-dimensional commuting multiplication algebra;
- the squarefree primitive-element polynomial;
- `det(m_rho)=682 mod 2053`;
- the five conjugate determinants `682,116,337,242,740` and rational norm residue `51`;
- the exact half-space description and full face lattice of `A+B+3C`; and
- all 74 nontrivial toric initial-form unit ideals.

The revised 29-page PDF compiles cleanly without undefined references or
overfull boxes and has been rendered and visually inspected.

## Cleared earlier blockers

The following earlier blockers are now cleared for the exact terminal
six-polynomial theorem:

- the filtered-residue reconstruction;
- the toric-saturation / no-boundary calculation;
- the characteristic-zero lifting argument;
- a clean TeX build; and
- a self-contained replay package with scripts, exact inputs, outputs, and hashes.

## Remaining blockers

- Specialist audit of the complete-chain-to-lattice-gap application.
- Independent audit that the imported support enumeration, layer model,
  normalizations, and saturations cover every terminal vertex-saturated case.
- Independent implementation of the toric face audit and finite algebra in
  another computer-algebra system.
- Audit of the earlier reduction from arbitrary below-125 Keller pairs to the
  terminal model.
- Final literature and priority review before public release.

The honest label is **computer-assisted proof of the exact terminal
six-polynomial no-gluing theorem, conditional Keller interpretation pending
upstream audit**.
