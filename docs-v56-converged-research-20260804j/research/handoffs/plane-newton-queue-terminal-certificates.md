---
title: "Model research brief — Newton-root closure and the first degree-125 boundary family"
description: "A self-contained mathematical handoff for a research model."
---

# Newton-root closure and the first degree-125 boundary family

<p class="claim-tag">Lane 8 · Updated 4 August 2026</p>

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
the cited complete-chain reduction; the integers are normalized
complete-chain parameters, not exponent coordinates of one root. The
reusable objects on this page are its
two explicit normalized support loci; no meaning is assigned here to an
unspecified pair of abstract roots.

For a monomial substitution or approximate-root shear, an **admissible
support chain** retains every transformed exponent allowed by polynomiality,
the relevant Newton inequalities, and the lattice congruence, unless a
coefficient equation proves its cancellation. It also records every vertex
required to remain nonzero.

## Closed mathematics below 125

After exchanging coordinates if necessary and passing to an algebraic
closure, the imported reduction of Guccione--Guccione--Horruitiner--Valqui
([arXiv:2204.14178v1](https://arxiv.org/abs/2204.14178), Theorem 2.1,
Propositions 4.1 and 4.3, and Corollary 5.7) has this logical scope:
Theorem 2.1 leaves the degree pair \((72,108)\) below \(125\); the
Proposition 4.1/Corollary 5.7 route excludes its \((9,27)\) complete-chain
case; and Proposition 4.3 sends the remaining \((8,28)\) case to exactly the
two normalized support loci below.

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
  the [compact toric empty system](lane-8-source-packet.md#source-598ed8b6db67151f).
  Since deleting
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
the first surviving exponent pair divided by the common \(P\)-power. In the
formula below, \((\rho,\sigma)\) is the primitive normal
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

The corresponding normalized degree-six Belyi map is

\[
\phi_6(u)=
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3},
\]

and the degree-thirty ambient face is its cyclic pullback \(\phi_6(z^5)\).

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
fixed. The complete corner chain itself has one edge.

The inherited **linear** descent is now explicit. At fixed source weight
\(w=5i-j\), write

\[
C_w(Y)=Y^{j_0}H_w(Y^5),\qquad c=\lambda^5.
\]

If \(F_w\) is the length of the initial forbidden terminal Taylor jet, then
terminal admissibility is exactly

\[
H_w(u)=(u-c)^{F_w}E_w(u),\qquad \deg E_w<n_w-F_w.
\]

There are \(76\) \(P\)-blocks and \(126\) \(Q\)-blocks. Their free
dimensions are \(533\) and \(1{,}440\), so the \(14{,}800\) inherited linear
relations among the \(16{,}773\) allowed post-shear coordinates have an
equivalent triangular \(1{,}973\)-parameter presentation. The public
manifest supplies every block and a forward-and-inverse checker. This
settles the linear stage only: common-power, determinant, normalization,
open, nonlinear support-stratification, and adjacent-chart conditions remain.

## Live problem

Continue the actual \(F_2\) coefficient packet using the certified
root-divisibility coordinates.  First define the support object, required
vertices and complements, and root/scaling/rechart equivalence for a finite
exhaustive stratum atlas.  That contract must determine which nonlinear
equations, opens, normal windows, and adjacent-chart exports are required.
Only then is a complete nonlinear equation packet well defined, and only
after both objects exist is the full actual-locus correspondence ready. The
mathematical milestones are:

1. define and prove exhaustive the support-stratum and equivalence contract;
2. impose the common-power and exact-double-root conditions in the leading
   blocks, retaining \(c=\lambda^5\) and every required open factor;
3. express the determinant, normalization, localization, and required-nonzero
   equations lazily in the \(1{,}973\) block coordinates, using the supplied
   \(u=z^5\) determinant operator;
4. prove both directions between source pairs and the resulting nonlinear
   constructible locus; and
5. export the resulting normal windows and matched block contract to Lane 9,
   with a fixed variable order, hashes, and an independent verifier.

Here the distinguished double root \(c\ne0\) and shear parameter
\(\lambda\ne0\) satisfy \(\lambda^5=c\); they must not be identified without
a proved scaling equivalence. The linear packet is already available to Lane
9. Actual normal windows and matched adjacent-chart blocks remain unavailable
until the nonlinear locus and support strata are controlled.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Define the exhaustive actual-F2 support-stratum contract — Ready now

`TSK-L8-F2-SUPPORT-CONTRACT-V2` · proof, exploration · sustained

**Goal.** Fix the actual F2 support object, required vertices and normalization complements, root/scaling/rechart equivalence, and a finite exhaustive stratum rule that determines every nonlinear equation packet and later normal-window input.

**Why it matters.** This gives all downstream claims one precise meaning of complete support stratification before equations or computations are declared exhaustive.

**Public inputs.**

- [Exact root-divisibility coordinates for the degree-125 F2 linear descent](../working-mathematics/units/JCG-66D861AF.md) (retained unit `JCG-66D861AF`).
- [Distinction among full supports, convex polygons, normal windows, required vertices, and equivalence choices.](lane-8-source-packet.md#source-c897ba0ee0d3d561).
- [Fixed complete-corner, face, normalization, and open-condition seed.](lane-8-source-packet.md#source-ee3b672b4c13351c).
- [Exact compact toric empty-system theorem and its raw-support dependency boundary.](lane-8-source-packet.md#source-598ed8b6db67151f).

**Complete when.**

- One support object and equivalence action have a proved finite exhaustive atlas with every required vertex, complement, open factor, and downstream export rule recorded.

**Possible starts.**

- Define the coarsest support invariant that determines every required nonlinear block, open factor, normal window, and adjacent-chart export, then prove the associated strata finite and exhaustive.

**Freedom.**

- A constructible-locus decomposition may replace literal enumeration if its strata have the same explicit coverage theorem.

**Mathematical limits.**

- Do not switch silently among monomial support, convex polygon, and normal-window interval.
- The compact toric theorem closes the named below-125 system; it does not supply the degree-125 F2 support atlas.

### Write the nonlinear F2 equations on the fixed support atlas — Blocked

`TSK-L8-F2-NONLINEAR-EQUATIONS-V5` · computation, proof · sustained

**Goal.** For every stratum in the certified support atlas, express the common-power, distinguished-double-root, determinant, normalization, localization, and required-nonzero conditions in the exact 1,973 root-divisibility coordinates and build an independent evaluator.

**Why it matters.** This produces a complete algebraic equation layer whose scope is fixed before computation rather than chosen afterward.

**Public inputs.**

- [Exact root-divisibility coordinates for the degree-125 F2 linear descent](../working-mathematics/units/JCG-66D861AF.md) (retained unit `JCG-66D861AF`).
- [Proved linear parametrization, inverse, leading blocks, determinant operator, and exact scope.](lane-8-source-packet.md#source-e1384a8451d58dd7).
- [Canonical 202-block variable order and sparse coordinate manifest.](lane-8-source-packet.md#source-ecdf70748a34b462).

**Task dependencies.**

- `TSK-L8-F2-SUPPORT-CONTRACT-V2`

**Blocked on.**

- The actual-support object, equivalence action, exhaustive strata, and required opens have not yet been fixed by the support contract.

**Complete when.**

- Every certified support stratum has fixed equations and opens, exact hashes, a forward evaluator, and an independent equality check.

**Possible starts.**

- After the support contract is fixed, build equations lazily by stratum and compare direct source-coefficient evaluation with triangular-coordinate evaluation.

**Freedom.**

- An equivalent sparse coordinate system is allowed if both maps to the canonical blocks are explicit on every stratum.

**Mathematical limits.**

- Keep lambda^5=c explicit unless a scaling theorem is proved; equations alone do not prove the bidirectional actual-locus correspondence.

### Prove the full actual-F2 constructible-locus correspondence — Blocked

`TSK-L8-F2-ACTUAL-LOCUS-V2` · proof, computation · open ended

**Goal.** Use the certified support atlas and nonlinear packet to prove both directions between source pairs and the resulting actual F2 constructible locus.

**Why it matters.** This supplies Lane 9's actual nonlinear normal-window input without conflating it with the completed linear descent.

**Public inputs.**

- [Exact root-divisibility coordinates for the degree-125 F2 linear descent](../working-mathematics/units/JCG-66D861AF.md) (retained unit `JCG-66D861AF`).
- [Canonical linear coordinate manifest to which both prerequisites attach.](lane-8-source-packet.md#source-ecdf70748a34b462).

**Task dependencies.**

- `TSK-L8-F2-SUPPORT-CONTRACT-V2`
- `TSK-L8-F2-NONLINEAR-EQUATIONS-V5`

**Blocked on.**

- The exhaustive actual-support contract has not been completed.
- The nonlinear equation and open packet on those strata has not been completed.

**Complete when.**

- The exhaustive strata, nonlinear locus, bidirectional proof, exact hashes, Lane 9 export, and independent verifier are public.

**Possible starts.**

- After both prerequisites are complete, state forward and inverse maps stratum by stratum and check every open, identification, and overlap export.

**Freedom.**

- A global constructible equivalence can replace stratumwise proofs if it implies the declared support atlas and exports its normal windows.

**Mathematical limits.**

- The completed linear packet alone is not the actual F2 parameter space.
<!-- RETAINED_TASKS_END -->

## Exact sources

- [Complete proof closing the two \((8,28)\) roots](lane-8-source-packet.md#source-08d38befa366c56b)
- [Independent raw-support replay](lane-8-source-packet.md#source-d48d3823ed65bdc1)
- [Proof-carrying queue manifest](lane-8-source-packet.md#source-f2a5a9b855b4c6e5)
- [Compact six-polynomial toric empty-system theorem and dependency boundary](lane-8-source-packet.md#source-598ed8b6db67151f)
- [Lane 8/9 recovery and scope audit](lane-8-source-packet.md#source-38ab8bd19d25aff4)
- [F2 coefficient-transport audit and checker](lane-8-source-packet.md#source-c897ba0ee0d3d561)
- [Exact root-divisibility coordinates, 202-block manifest, and checker](lane-8-source-packet.md#source-e1384a8451d58dd7)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-8-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
