# Newton-root closure and the first degree-125 boundary family

Lane 8 · 2026-08-03

## Why this lane matters

The two normalized \((8,28)\) roots below degree \(125\) are closed. The next
geometric problem is no longer to repeat those exclusions, but to understand
the first surviving complete-chain boundary family at degree \(125\) well
enough to build its intrinsic normal-neighborhood obstruction theory.

## Newton-root conventions

For a polynomial pair \((P,Q)\), its **support** is the set of exponent pairs
of nonzero monomials. A Newton root in this project records two exact support
polygons, required nonzero vertices, a selected common lower face, and all
normalization complements. An edge in the Newton queue is valid only when its
closed and open children cover the parent. A terminal certificate proves
emptiness only for the exact finite system and localization factors it names.

In the below-\(125\) calculation, a **normalized root** means one such exact
normalized support locus after the common degree-21 lower face has been
selected, including its required nonzero vertices, localizations, and bracket
equations. It is not a root of a single polynomial.

The notation “the \((8,28)\) case” is the label of the remaining branch in
the cited literature reduction. The reusable objects on this page are its
two explicit normalized support loci; no meaning is assigned here to an
unspecified pair of abstract roots.

For a monomial substitution or approximate-root shear, an **admissible
support chain** retains every transformed exponent allowed by polynomiality,
the relevant Newton inequalities, and the lattice congruence, unless a
coefficient equation proves its cancellation. It also records every vertex
required to remain nonzero.

## Closed mathematics below 125

The imported reduction of Guccione--Guccione--Horruitiner--Valqui
([arXiv:2204.14178v1](https://arxiv.org/abs/2204.14178), Theorem 2.1,
Propositions 4.1 and 4.3, and Corollary 5.7) reduces the relevant
characteristic-zero case below \(125\) to two normalized \((8,28)\) roots,
after its \((9,27)\) exclusion.

The exact reconstruction closes both roots:

- The truncated root has \(25\) possible \(P\)-monomials and \(47\)
  possible \(Q\)-monomials. Its weight-four Macaulay matrix has rank \(14\)
  on all \(14\) weight-four monomials. The required top vertices therefore
  vanish.
- The full root has \(61\) and \(125\) possible monomials. Its layer-four
  condition is a square \(L^2\). The closed child \(L=t_{1,1}=0\) loses the
  required top vertices. On \(t_{1,1}\ne0\), the open child reduces to
  fifteen equations \(F_0,\ldots,F_{14}\) in five variables.
- The six equations with zero-based indices \(4,6,8,9,10,11\) are literally
  the compact toric empty system already proved in Program 6. Since deleting
  generators enlarges a zero set, emptiness of that six-equation system
  closes the fifteen-equation child.

Consequently, relative to the named literature reduction and the compact
toric theorem, there is no characteristic-zero plane Keller counterexample
with \(\max(\deg P,\deg Q)<125\). This is a proof assembly with explicit
dependencies and no novelty claim.

## The first degree-125 family \(F_2\)

\(F_2\) is the name of the first maximum-degree-\(125\) complete-corner-chain
family in the cited table, not the name of a polynomial map. It is fixed on
this page by the following corner, multiplicity, face, and determinant data.

A **complete corner chain** is the finite sequence consisting of a starting
valid edge and the successive child corners and edges produced by the
complete-chain algorithms; it is corner data, not the full post-shear
coefficient support. Here \(A_0,A'_0\) are the endpoints of the starting
common lower edge. After an approximate-root shear, the **child corner** is
the first surviving exponent pair divided by the common \(P\)-power,
equivalently. In the formula below, \((\rho,\sigma)\) is the primitive normal
direction to the starting edge, \(m\) is the common-power exponent of the
leading \(P\)-form, and \(m_\lambda\) is the multiplicity of the selected
root in that leading form:

\[
A_1=A'_0+\frac{m_\lambda}{m}
\left(-\frac{\sigma}{\rho},1\right).
\]

The one-step complete-chain data are

\[
A_0=(5,20),\qquad A'_0=(1,0),\qquad
A_1=(7/5,2),\qquad (m,n)=(3,5).
\]

Thus \((\rho,\sigma)=(5,-1)\), and the child-corner identity gives
\(m_\lambda=6\). Put
\(z=x^{1/5}y\) and \(w=z^5=xy^5\). The common-power theorem gives

\[
\ell(P)=x^3S(w)^3,\qquad
\ell(Q)=x^5S(w)^5,
\]

where \(S\) is a quartic with a distinguished nonzero double root. The
corresponding shear produces the child corner \(A_1\).

At the terminal face, the direction is \((25,-17)\), and the gap-five
condition forces \(p(z)=\bar p(z^5)\), \(q(z)=\bar q(z^5)\). With
\(u=z^5\), the reduced face is uniquely represented by

\[
\bar p(u)=1-u,\qquad
\bar q(u)=\frac15-\frac35u+\frac9{25}u^2,
\]

with degree-six passport

\[
(5,1),\qquad(3^2),\qquad(3,1^3).
\]

The **passport** of a degree-\(D\) Belyi map is the ordered triple of
partitions of \(D\) recording ramification over its three branch values.
For this calculation the ordering of those branch values is immaterial.

With

\[
A_0(z)=z-z^6,\qquad
B_0(z)=\frac15-\frac35z^5+\frac9{25}z^{10},
\]

the normalized determinant equation used by the coefficient calculation is

\[
3AB_z-5A_zB+t(A_zB_t-A_tB_z)=-1,
\]

where \(P=t^{-3}A\) and \(Q=t^{-5}B\). Its order-\(r\) coefficient is

\[
\sum_{i+j=r}\bigl((3-i)A_iB'_j+(j-5)A'_iB_j\bigr).
\]

The ambient degree-thirty face is its \(C_5\)-pullback. The terminal face is
fixed. The complete corner chain itself has one edge; what is missing is the
inherited coefficient-relation system selecting the actual post-shear
support from the much larger independent-coefficient envelope.

## Live problem

Construct the exact inherited coefficient-relation system for the
denominator-five \(F_2\) shear inside the terminal half-space. Use that
system to define a finite constructible stratification of possible actual
post-shear Newton polygons and normal windows. The relation packet is the
missing input for support uniqueness and for an actual, rather than
independent-coefficient, boundary Kuranishi calculation.

## Ready task L8-T1 — inherited coefficient-relation packet for \(F_2\)

**Inputs.** The exact
[degree-125 boundary seed](lane-8-source-packet.md#source-ee3b672b4c13351c),
the [complete-chain terminal construction](lane-8-source-packet.md#source-3b11d78922960385),
the [seed checker](lane-8-source-packet.md#source-2cdc0acae76d0682),
the already-derived
[maximal post-shear support windows](lane-8-source-packet.md#source-38ab8bd19d25aff4),
and the exact
[coefficient-transport audit and checker](lane-8-source-packet.md#source-c897ba0ee0d3d561).

**Deliverable.** Produce one self-contained finite packet that declares all
source and post-shear coefficients; exports the binomial shear block by
block; sets the 53 \(P\) and 136 \(Q\) forbidden terminal coordinates to
zero; and eliminates the source coefficients, or gives an equivalent
presentation, to obtain every inherited linear relation among the 4,433 and
12,340 allowed coordinates. Add the common-power, exact-double-root,
determinant, normalization, required-nonzero, and localization conditions.
In particular, if \(c\ne0\) is the distinguished exact double root of the
quartic \(S(w)\), impose \(S(c)=S'(c)=0\), \(S''(c)\ne0\), choose the
shear parameter \(\lambda\ne0\) with \(\lambda^5=c\), and do not
identify \(c\) with \(\lambda\). List every coefficient and scalar being
inverted; setting \(\lambda=1\) requires a proved scaling equivalence. Use
the displayed normalized determinant equation and terminal face rather than
an unnamed determinant condition.
State how the nonzero shear parameter is treated, prove the forward and
inverse correspondence of constructible loci, and supply a machine-readable
variable order, equation manifest, source hashes, and exact checker.

**Dependencies.** Only the supplied complete-chain definitions, explicit
\(F_2\) seed, displayed binomial coefficient transport, polynomiality,
terminal half-spaces, common-power face, and determinant equation. The
terminal face and its quotient map are fixed inputs, not search variables.

**Limits.** The packet need not solve the nonlinear constructible system or
prove support uniqueness. The maximal windows are an independent-coefficient
enlargement: exact transport leaves dimensions 533 and 1,440 inside the
allowed \(P\)- and \(Q\)-spaces, so the enlargement omits 14,800 linear
descent relations even before the nonlinear constraints.

## Non-ready follow-up — actual support determinacy and boundary operator

After L8-T1, specify an exhaustive finite support-stratification and
equivalence contract, decide all exact support strata, and derive the actual
two-point normal windows. Then construct the determinant layer operators and
pole-filtered residue adjoints while retaining every fresh parameter. Locate
the first intrinsic obstruction or prove solvability through a stated order.
Cross-chart attachment belongs to Lane 9 unless an actual overlap theorem is
supplied.

## Exact sources

- [Complete proof closing the two \((8,28)\) roots](lane-8-source-packet.md#source-08d38befa366c56b)
- [Independent raw-support replay](lane-8-source-packet.md#source-d48d3823ed65bdc1)
- [Proof-carrying queue manifest](lane-8-source-packet.md#source-f2a5a9b855b4c6e5)
- [Lane 8/9 recovery and scope audit](lane-8-source-packet.md#source-38ab8bd19d25aff4)
- [F2 coefficient-transport audit and checker](lane-8-source-packet.md#source-c897ba0ee0d3d561)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-8-source-packet.md) · [Raw-support reconstruction input](lane-8-reconstruction-input.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
