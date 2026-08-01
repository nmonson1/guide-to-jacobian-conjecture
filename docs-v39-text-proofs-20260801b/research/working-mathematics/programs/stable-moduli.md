# Stable Moduli

Several explicit families test how fixed-degree, affine, and stable equivalence interact, with boundary geometry providing computable invariants.

This is a generated progress view of retained mathematics. Workflow labels and private source locators are intentionally omitted.

<!-- noncanonical-overlay -->

## Setup and research posture

This program studies intrinsic inequivalence of explicit Keller maps under
polynomial source and target automorphisms and stabilization. Decorated
finite boundary schemes and relative-Jacobian data classify a substantial
fixed-frame locus, including multiplicities. The difficult boundary is what
happens when roots escape to infinity and the finite boundary length changes.

Three quotient-like objects must remain distinct: invariant functions, the
fppf orbit sheaf, and a proposed space of degeneration directions. A
separated graph closure, if it exists, does not become the orbit quotient.
Likewise, rigidified boundary data do not automatically describe the full
unrigidified left-right groupoid.

## Strategy and payoff

Define the degeneration functor before naming its compactification. For each
local wall specify the base, generic quotient coordinate, graph map, closure,
allowed base changes, and retained automorphisms. Then prove overlap maps,
cocycle compatibility, scaling, simultaneous escapes, and behavior when a
resultant ceases to be a unit.

Low-length coefficient and fan calculations are excellent falsification
tools. Use them to test Fitting data, pairwise overlaps, and triple cocycles;
when a test fails, identify whether the failure is representability,
separatedness, finite type, or comparison with intrinsic stable equivalence.

The expanded fixed-frame repairs now cover the empty-boundary branch, common
roots, projective incidence, conductor recovery, formal induction, and the
categorical and fppf wall arguments. Their bounded verifier checks fifteen
finite identities. The remaining gate is specialist review of the geometric
arguments; the exact checks are not a substitute for it.

## Connections

Finite-cover boundary completeness in the cubic-incidence program and stable
boundary reconstruction here are related but not identical. Degree-eight
and degree-eleven deformation questions supply a modulus-onset frontier.
The plane-boundary program offers a parallel warning that local chart
coordinates require a global correspondence theorem.

## Current priorities and research freedom

The current attention order is:

1. obtain specialist review of the expanded fixed-frame classification
   chain and its exact hypotheses;
2. define and prove the one-root graph model precisely;
3. test simultaneous-escape overlaps and hidden automorphisms at low length;
4. compare any degeneration space separately with categorical functions and
   actual stable equivalence; and
5. clear the attribution and independent-reproduction gates for the claimed
   onset of stable moduli.

Other quotient formalisms are welcome when their functor and comparison maps
are explicit.

## Graveyard and scope fences

- Do not identify categorical, orbit, and graph-closure quotients.
- Do not reuse a reflexivity shortcut where the proof needs a support or
  Cohen--Macaulay argument.
- One escaping root does not prove simultaneous gluing.
- Hidden infinitesimal automorphisms must be rigidified or retained as stack
  structure, not silently quotiented away.
- Dimension counts do not prove inequivalence.

## Definitions and constructions

### [Admissible frame](../units/RMU-2B51B0B3.md)

`RMU-2B51B0B3` · `definition`

A pair \(A,B\in\C[c]\) is admissible if
\[
A(0)=0,\quad A'(0)=1,\qquad
B(0)=-2,\quad B'(0)=-2A''(0).
\]
Using
\[
c=2x-3x^2y-x^3z,\qquad
t=y+\frac1x,\qquad r=\frac2x,
\]
define \(G_{A,B}=(a,b,c)\) by
\[
b=r-3A(c)t^2-2B(c)t,\qquad
2a=A(c)t^3+B(c)t^2+tb.
\]

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

## Retained results

### [A collision between two source points persists infinitesimally, and analytically under a…](../units/JCG-EFA8536B.md)

`JCG-EFA8536B` · `assertion`

A collision between two source points persists infinitesimally, and analytically under a small analytic deformation, when the two Jacobians remain invertible.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-002`
  - Does not establish: The locator alone is not an independent proof review.

### [A finite flat cubic completion identifies the reduced nonproperness locus as V(g times Delta).](../units/JCG-AF23BCCD.md)

`JCG-AF23BCCD` · `assertion`

A finite flat cubic completion identifies the reduced nonproperness locus as V(g times Delta).

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#eq:reciprocal-nonproper`
  - Does not establish: The locator alone is not an independent proof review.

### [All members of the lambda-family are pairwise stably inequivalent after separating the…](../units/JCG-0C43F49B.md)

`JCG-0C43F49B` · `assertion`

All members of the lambda-family are pairwise stably inequivalent after separating the generic, zero, and -324 cases.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#thm:reciprocal-stable`
  - Does not establish: The locator alone is not an independent proof review.

### [Assuming the current reduced-rigidity and stable-classification theorems, the normalized degr…](../units/JCG-D1155E99.md)

`JCG-D1155E99` · `assertion`

Assuming the current reduced-rigidity and stable-classification theorems, the normalized degree-seven counterexample G is reduced-isolated in its degree-at-most-seven normalized affine slice but is the special fiber of an algebraic degree-eleven family whose general fibers vary in stable left-right class. Thus the pointed stable-moduli onset through G lies between 8 and 11, and equals 11 within the cubic-frame locus.

### [At a deleted root s of A, B(s)=0 if and only if…](../units/JCG-075712B5.md)

`JCG-075712B5` · `assertion`

At a deleted root s of A, B(s)=0 if and only if the scheme-theoretic intersection of the primitive discriminant with the plane c=s is nonreduced.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:intrinsic-common-planes`
  - Does not establish: The locator alone is not an independent proof review.

### [At a simple escape wall the graph closure is the blowup of…](../units/JCG-62905FD2.md)

`JCG-62905FD2` · `assertion`

At a simple escape wall the graph closure is the blowup of the corresponding weighted ideal, and for an escape of length m the principal-part coordinates give a finite-type projective separated weighted degeneration space with weights (1,...,m,m+1,m,...,2).

Support:

- **source assertion:** construction and scope — [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#subsec:separated-degeneration-spaces`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-subsec-separated-degeneration-spaces)
  - Does not establish: The locator alone is not an independent proof review.

### [At ambient bound N, degree-preserving cubic-frame root translations are exactly the kernel…](../units/JCG-2F2C2F29.md)

`JCG-2F2C2F29` · `assertion`

At ambient bound N, degree-preserving cubic-frame root translations are exactly the kernel pair of (Qhat,P) mapping to (Qhat,z^N P mod Qhat); when roots escape to infinity, P decomposes uniquely into finite-root data plus the translated principal part.

Support:

- **source assertion:** proposition — [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#prop:bounded-root-translation-groupoid`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-prop-bounded-root-translation-groupoid)
  - Does not establish: The locator alone is not an independent proof review.

### [At fixed generic degree five, the analyzed grading-equivariant Keller family contains a…](../units/JCG-1183609D.md)

`JCG-1183609D` · `assertion`

At fixed generic degree five, the analyzed grading-equivariant Keller family contains a one-parameter set distinguished by critical-root configuration under grading-preserving equivalence.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-moduli.tex#prop:degree-five-equivariant-moduli`
  - Does not establish: The locator alone is not an independent proof review.

### [At lambda=-324 the boundary polynomial factors, the Lambda locus has two G_m…](../units/JCG-63A2AFB3.md)

`JCG-63A2AFB3` · `assertion`

At lambda=-324 the boundary polynomial factors, the Lambda locus has two G_m components, Gamma is P1 minus six points, and the omitted locus has three components; the map still has generic degree three and S3 monodromy.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-006`
  - Does not establish: The locator alone is not an independent proof review.

### [Distinct q-families have the same first-order formal tangent and are source-trivial through…](../units/JCG-F7DC2C3B.md)

`JCG-F7DC2C3B` · `assertion`

Distinct q-families have the same first-order formal tangent and are source-trivial through the computed formal orders, while their punctured members remain stably inequivalent; the stable modulus is therefore invisible to this local formal deformation data.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#prop:formal-stable-separation`
  - Does not establish: The locator alone is not an independent proof review.

### [Every degree-at-most-four map in the specified equivariant ansatz satisfying the Keller equat…](../units/JCG-6B34B866.md)

`JCG-6B34B866` · `assertion`

Every degree-at-most-four map in the specified equivariant ansatz satisfying the Keller equations is tame/an automorphism.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-009`
  - Does not establish: The locator alone is not an independent proof review.

### [Every equivariant Keller map of degree at most five in the analyzed family is an automorphism.](../units/JCG-B8EB4A61.md)

`JCG-B8EB4A61` · `assertion`

Every equivariant Keller map of degree at most five in the analyzed family is an automorphism.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-012`
  - Does not establish: The locator alone is not an independent proof review.

### [Every equivariant Keller map of degree at most six in the analyzed…](../units/JCG-AB6E23A3.md)

`JCG-AB6E23A3` · `assertion`

Every equivariant Keller map of degree at most six in the analyzed family is an automorphism, so seven is the sharp threshold in that family.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/02-low-degree/appendices/bounded-and-equivariant.tex#thm:equivariant-threshold`
  - Does not establish: The locator alone is not an independent proof review.

### [Every quartic frame has T^4 coefficient divisible by c^3 and first jet…](../units/JCG-9E1E87CA.md)

`JCG-9E1E87CA` · `assertion`

Every quartic frame has T^4 coefficient divisible by c^3 and first jet satisfying delta+4gamma+12kappa=0; the displayed quartic realizes these conditions with determinant -2, generic degree four, and component degrees (16,15,4).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-016`
  - Does not establish: The locator alone is not an independent proof review.

### [For A=c(c+1), B=-2(c+1)^2, the pulled-back relative Jacobian ideal is generated by (c+1)^2(3c…](../units/JCG-7FB01BFA.md)

`JCG-7FB01BFA` · `assertion`

For A=c(c+1), B=-2(c+1)^2, the pulled-back relative Jacobian ideal is generated by (c+1)^2(3ct-2(c+1))^3, so the exceptional member is uniformly recorded by vertical multiplicity two.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:q-minus-two-weighted-stratum`
  - Does not establish: The locator alone is not an independent proof review.

### [For a fixed target and marked boundary, the logarithmic deformation complex has…](../units/JCG-068E58B0.md)

`JCG-068E58B0` · `assertion`

For a fixed target and marked boundary, the logarithmic deformation complex has the displayed matrix and Fitting/cohomology calculation; eta-directions survive there, although arbitrary target vector fields can kill them.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/logarithmic-deformations.tex#prop:logarithmic-complex`
  - Does not establish: The locator alone is not an independent proof review.

### [For a generic weighted-lift seed p, the normalization of the unique nonnormal…](../units/JCG-0A4149FE.md)

`JCG-0A4149FE` · `assertion`

For a generic weighted-lift seed p, the normalization of the unique nonnormal nonproperness-wall component has ramification divisor equal to the hyperbola arrangement u zeta=r over the critical roots r of p; its critical-root configuration modulo common scaling is invariant under arbitrary polynomial left-right equivalence.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/weighted-lift-moduli.tex#thm:weighted-critical-roots`
  - Does not establish: The locator alone is not an independent proof review.

### [For a kernel-of-an-endomorphism translation action over a Q-algebra, the invariant algebra is…](../units/JCG-66049841.md)

`JCG-66049841` · `assertion`

For a kernel-of-an-endomorphism translation action over a Q-algebra, the invariant algebra is the kernel of the relative differential modulo im(M dual); for the bounded cubic-frame action, global invariants are the contraction of the localization at the single one-root wall q_N=0.

Support:

- **source assertion:** invariant-algebra theorem and proof — [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#thm:categorical-differential-kernel`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-thm-categorical-differential-kernel)
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** one-wall theorem and corrected proof — [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#thm:one-wall-control`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-thm-one-wall-control)
  - Does not establish: The locator alone is not an independent proof review.

### [For admissible cubic frames with nonconstant A/c, stable left-right equivalence, ordinary lef…](../units/JCG-E48F1FF0.md)

`JCG-E48F1FF0` · `assertion`

For admissible cubic frames with nonconstant A/c, stable left-right equivalence, ordinary left-right equivalence, and equality of the decorated Artin schemes (Spec C[c]/(A/c), B mod (A/c)) up to scaling are equivalent, without squarefreeness or coprimality assumptions.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#thm:all-multiplicity-torelli`
  - Does not establish: The locator alone is not an independent proof review.

### [For an admissible cubic frame, the coefficient content of the discriminant in…](../units/JCG-7220CE67.md)

`JCG-7220CE67` · `assertion`

For an admissible cubic frame, the coefficient content of the discriminant in the target variables is chi=gcd(A,B^2), and the primitive nonplane discriminant Delta/chi is irreducible.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:primitive-discriminant-content`
  - Does not establish: The locator alone is not an independent proof review.

### [For every coprime admissible cubic-frame pair, without assuming A squarefree, stable left-rig…](../units/JCG-B858C93E.md)

`JCG-B858C93E` · `assertion`

For every coprime admissible cubic-frame pair, without assuming A squarefree, stable left-right equivalence equals ordinary left-right equivalence and is classified by scaling the decorated finite scheme Z_A=Spec C[c]/(A/c) with its unit-valued jet section B|Z_A.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-017`
  - Does not establish: The locator alone is not an independent proof review.

### [For every generic fiber degree n at least four, the weighted-lift counterexamples…](../units/JCG-517C8B4B.md)

`JCG-517C8B4B` · `assertion`

For every generic fiber degree n at least four, the weighted-lift counterexamples contain an (n-3)-dimensional family of pairwise inequivalent maps under arbitrary polynomial left-right equivalence.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/weighted-lift-moduli.tex#cor:weighted-fixed-degree-moduli`
  - Does not establish: The locator alone is not an independent proof review.

### [For every m>=1, the family A=c(1-c)^m and B=-2+4mc+c^2 sum_{j=0}^{m-1}s_jc^j contains an affi…](../units/JCG-BAD4B378.md)

`JCG-BAD4B378` · `assertion`

For every m>=1, the family A=c(1-c)^m and B=-2+4mc+c^2 sum_{j=0}^{m-1}s_jc^j contains an affine-open m-parameter set of pairwise stably inequivalent three-variable Keller maps with fixed generic degree three and fixed component degrees (4m+7,4m+6,4).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-018`
  - Does not establish: The locator alone is not an independent proof review.

### [For every n at least two, the cubic-frame construction contains a (2n-3)-dimensional…](../units/JCG-C8A7EF37.md)

`JCG-C8A7EF37` · `assertion`

For every n at least two, the cubic-frame construction contains a (2n-3)-dimensional family of pairwise stably inequivalent generic-degree-three Keller maps of ordinary degree 4n+3. In particular, ordinary degree fifteen contains a three-dimensional stable-moduli family, modulo a finite involution.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:growing-cubic-frame-moduli`
  - Does not establish: The locator alone is not an independent proof review.

### [For generic lambda other than 0 and -324, the unique positive-genus omitted…](../units/JCG-4522AD29.md)

`JCG-4522AD29` · `assertion`

For generic lambda other than 0 and -324, the unique positive-genus omitted component and its birational/Albanese data distinguish stable equivalence classes.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-004`
  - Does not establish: The locator alone is not an independent proof review.

### [For squarefree A and marked missing-infinity roots, stabilized isomorphism classes of normali…](../units/JCG-5542AF40.md)

`JCG-5542AF40` · `assertion`

For squarefree A and marked missing-infinity roots, stabilized isomorphism classes of normalized conductor arrangements are exactly classified by affine changes of c, affine-linear changes of t over c, the affine root configuration of A, and the projective vector of conductor values B(rho) modulo induced finite permutations.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:conductor-arrangement-classification`
  - Does not establish: The locator alone is not an independent proof review.

### [For the discriminant surface of A(c)T^3+B(c)T^2+vT-2u with gcd(A,B)=1, the normalization cond…](../units/JCG-AE66472A.md)

`JCG-AE66472A` · `assertion`

For the discriminant surface of A(c)T^3+B(c)T^2+vT-2u with gcd(A,B)=1, the normalization conductor is exactly H^2 C[c,t], where H=3A(c)t+B(c), and its contraction is generated by B^2-3Av and -18Au-Bv.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:cubic-frame-conductor`
  - Does not establish: The locator alone is not an independent proof review.

### [For the quadratic cubic-frame family A=c+alpha c^2 and B=-2-4alpha c+beta c^2, the…](../units/JCG-2FF16912.md)

`JCG-2FF16912` · `assertion`

For the quadratic cubic-frame family A=c+alpha c^2 and B=-2-4alpha c+beta c^2, the arcs alpha=t and beta=q t^2 have constant stable class q away from t=0 and specialize to the base class at t=0. Consequently no separated algebraic space can functorially classify the bare stable left-right orbit set while distinguishing these geometric classes.

### [For the quadratic cubic-frame slice with alpha nonzero, q=beta/alpha^2 is a complete…](../units/JCG-0F9A20C0.md)

`JCG-0F9A20C0` · `assertion`

For the quadratic cubic-frame slice with alpha nonzero, q=beta/alpha^2 is a complete invariant under arbitrary polynomial source-target equivalence and stabilization; the alpha=0 line is gauge-equivalent to the base map.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-014`
  - Does not establish: The locator alone is not an independent proof review.

### [If D_min is the minimum possible maximum ordinary total degree of a…](../units/JCG-6747671C.md)

`JCG-6747671C` · `assertion`

If D_min is the minimum possible maximum ordinary total degree of a coordinate of a complex polynomial Keller counterexample in dimension three, then 4 <= D_min <= 7.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/02-low-degree/appendices/additional-results-and-leads.tex#supp-note-02-032`
  - Does not establish: The locator alone is not an independent proof review.

### [If p=ord_s A0 and d=ord_s rho, then the common-factor multiplicity m is…](../units/JCG-F9D9B3FA.md)

`JCG-F9D9B3FA` · `assertion`

If p=ord_s A0 and d=ord_s rho, then the common-factor multiplicity m is d when p is at least d and (p+d)/2 otherwise.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#lem:common-factor-multiplicity`
  - Does not establish: The locator alone is not an independent proof review.

### [If r is a nonzero boundary point with ord_r A=m and ord_r…](../units/JCG-FD846076.md)

`JCG-FD846076` · `assertion`

If r is a nonzero boundary point with ord_r A=m and ord_r B=n>0, the largest power of c-r dividing the cubic discriminant is (c-r)^{min(m,2n)}.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-020`
  - Does not establish: The locator alone is not an independent proof review.

### [In the analyzed cubic-incidence families, additional boundary roots yield infinitely many sta…](../units/JCG-2DCFC426.md)

`JCG-2DCFC426` · `assertion`

In the analyzed cubic-incidence families, additional boundary roots yield infinitely many stably left-right inequivalent maps, detectable by omitted-boundary components and curve genera.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-001`
  - Does not establish: The locator alone is not an independent proof review.

### [In the primitive linear-rho cubic ansatz, the equations force degree seven.](../units/JCG-9077FE2E.md)

`JCG-9077FE2E` · `assertion`

In the primitive linear-rho cubic ansatz, the equations force degree seven.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-010`
  - Does not establish: The locator alone is not an independent proof review.

### [Inside the normalized family, degree-jumping first-order deformations of the base cubic have…](../units/JCG-69445E34.md)

`JCG-69445E34` · `assertion`

Inside the normalized family, degree-jumping first-order deformations of the base cubic have tangent quotient C[c]/(C plus Cc); imposing degree at most N gives dimension N-1.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-015`
  - Does not establish: The locator alone is not an independent proof review.

### [Let R be a DVR with uniformizer pi and let e >=…](../units/JCG-4D953715.md)

`JCG-4D953715` · `assertion`

Let R be a DVR with uniformizer pi and let e >= 1. The rank-one wall orbit sheaf B/Ann_B(pi^e) fails the strong Rim-Schlessinger pushout condition, so it is not an algebraic space; consequently the free quotient stack and the bounded cubic-frame fppf quotient along the generic one-root wall are not algebraic. At e = 0 the acting group K_0 is trivial and the quotient is algebraic.

Support:

- **source assertion:** theorem and proof — [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#thm:fppf-wall-nonalgebraic`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-thm-fppf-wall-nonalgebraic)
  - Does not establish: The locator alone is not an independent proof review.

### [Natural next problems include classification of generic-degree-three examples, bounded-degree…](../units/JCG-44729E0B.md)

`JCG-44729E0B` · `assertion`

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-038`
  - Does not establish: The locator alone is not an independent proof review.

### [No target reparametrization of the tested bounded degree at most eight lowers…](../units/JCG-531601F7.md)

`JCG-531601F7` · `assertion`

No target reparametrization of the tested bounded degree at most eight lowers the public map below degree seven.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-008`
  - Does not establish: The locator alone is not an independent proof review.

### [Ordinary total degree \(7\) is not known to be minimal in dimension three.](../units/JCG-CA966BD6.md)

`JCG-CA966BD6` · `assertion`

Ordinary total degree \(7\) is not known to be minimal in dimension three.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/02-low-degree/appendices/additional-results-and-leads.tex#supp-note-02-027`
  - Does not establish: The locator alone is not an independent proof review.

### [Over the complex numbers, the omitted set of G_lambda is exactly the…](../units/JCG-FBD62152.md)

`JCG-FBD62152` · `assertion`

Over the complex numbers, the omitted set of G_lambda is exactly the union of the Gamma and Lambda curves, including the p=0 chart.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-003`
  - Does not establish: The locator alone is not an independent proof review.

### [Recover the six decisive obstruction components canonically from the residue pole filtration…](../units/JCG-5EA4BAEE.md)

`JCG-5EA4BAEE` · `assertion`

Recover the six decisive obstruction components canonically from the residue pole filtration or the determinant of cohomology.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-045`
  - Does not establish: The locator alone is not an independent proof review.

### [Replacing the linear parameter by an arbitrary polynomial eta yields a family…](../units/JCG-77C618B1.md)

`JCG-77C618B1` · `assertion`

Replacing the linear parameter by an arbitrary polynomial eta yields a family G_eta with determinant -2, cubic generic degree, generic S3 monodromy, an exact Gamma/Lambda image complement, and boundary curves of arbitrarily large genus.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#prop:reciprocal-pole`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#thm:reciprocal-basic`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#thm:reciprocal-image`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#thm:reciprocal-stable`
  - Does not establish: The locator alone is not an independent proof review.

### [The absolute minimum degree for a positive-genus omitted component is bounded by…](../units/JCG-1B74A298.md)

`JCG-1B74A298` · `assertion`

The absolute minimum degree for a positive-genus omitted component is bounded by 4 <= d <= 20, while the reciprocal class has exact minimum 20.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#sec:reciprocal-degree-moduli`
  - Does not establish: The locator alone is not an independent proof review.

### [The based w20 family has exactly two based equivalence classes, k=0 and…](../units/JCG-10B255A3.md)

`JCG-10B255A3` · `assertion`

The based w20 family has exactly two based equivalence classes, k=0 and k nonzero, while its coefficientwise formal trivializations require unbounded spatial degree.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-moduli.tex#sec:based-parameter`
  - Does not establish: The locator alone is not an independent proof review.

### [The boundary-data quotient B_N=[U_N/G_m] is a smooth Deligne-Mumford stack of dimension 2N-1…](../units/JCG-046E56A8.md)

`JCG-046E56A8` · `assertion`

The boundary-data quotient B_N=[U_N/G_m] is a smooth Deligne-Mumford stack of dimension 2N-1 whose geometric points classify coprime admissible cubic-frame maps of boundary length N; it is a framed or rigidified boundary stack, not the full unrigidified left-right groupoid.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-019`
  - Does not establish: The locator alone is not an independent proof review.

### [The cubic-frame residual coefficient is gauge, every degree-at-most-seven member of that fram…](../units/JCG-295EAAC3.md)

`JCG-295EAAC3` · `assertion`

The cubic-frame residual coefficient is gauge, every degree-at-most-seven member of that framed family is affinely equivalent to the base example, and degree seven is forced there.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-011`
  - Does not establish: The locator alone is not an independent proof review.

### [The delta_a chart of the blowup of the relative Jacobian ideal (delta_a,delta_b)…](../units/JCG-24D147A4.md)

`JCG-24D147A4` · `assertion`

The delta_a chart of the blowup of the relative Jacobian ideal (delta_a,delta_b) is exactly A2 with coordinates (c,t), and the pulled-back ideal is generated by rho(c)H0(c,t)^3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:relative-jacobian-chart`
  - Does not establish: The locator alone is not an independent proof review.

### [The displayed one-parameter family G_lambda has constant determinant, a persistent collision,…](../units/JCG-61073F6B.md)

`JCG-61073F6B` · `assertion`

The displayed one-parameter family G_lambda has constant determinant, a persistent collision, cubic generic degree, and generic S3 monodromy.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#thm:reciprocal-basic`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#sec:reciprocal-collision-line`
  - Does not establish: The locator alone is not an independent proof review.

### [The displayed two-parameter quartic-frame family G_{rho,sigma} consists of polynomial Keller…](../units/JCG-7926F911.md)

`JCG-7926F911` · `assertion`

The displayed two-parameter quartic-frame family G_{rho,sigma} consists of polynomial Keller maps with determinant -2, generic degree four, and component degrees (16,15,4).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-021`
  - Does not establish: The locator alone is not an independent proof review.

### [The eta-family supplies stable moduli with boundary curves of arbitrary genus.](../units/JCG-47917D8B.md)

`JCG-47917D8B` · `assertion`

The eta-family supplies stable moduli with boundary curves of arbitrary genus.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#thm:reciprocal-stable`
  - Does not establish: The locator alone is not an independent proof review.

### [The framed reciprocal-family moduli is naturally described by a quotient stack [V_m/G_m],…](../units/JCG-8FF53FFF.md)

`JCG-8FF53FFF` · `assertion`

The framed reciprocal-family moduli is naturally described by a quotient stack [V_m/G_m], with the stated tangent complex and local logarithmic complex.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#sec:reciprocal-degree-moduli`
  - Does not establish: The locator alone is not an independent proof review.

### [The highest-leverage program is exact reconstruction of the five Belyi maps followed…](../units/JCG-48D5E369.md)

`JCG-48D5E369` · `assertion`

The highest-leverage program is exact reconstruction of the five Belyi maps followed by weight-filtered tests against the two surviving Newton supports, with independent certificate infrastructure in parallel.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-048`
  - Does not establish: The locator alone is not an independent proof review.

### [The intersection C(P,Q,R) with polynomials of degree at most six is spanned…](../units/JCG-C9D20922.md)

`JCG-C9D20922` · `assertion`

The intersection C(P,Q,R) with polynomials of degree at most six is spanned by 1,Q,R, implying that no target automorphism of any degree lowers the public map below degree seven.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-013`
  - Does not establish: The locator alone is not an independent proof review.

### [The lambda=0 member is stably distinct from the generic members by omitted-component count.](../units/JCG-DA4A0F69.md)

`JCG-DA4A0F69` · `assertion`

The lambda=0 member is stably distinct from the generic members by omitted-component count.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-005`
  - Does not establish: The locator alone is not an independent proof review.

### [The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and…](../units/JCG-30AF091E.md)

`JCG-30AF091E` · `assertion`

The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and minimal support remain open.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-047`
  - Does not establish: The locator alone is not an independent proof review.

### [The reciprocal pole-cancellation calculation classifies the relevant denominator as g=1+p^2 eta.](../units/JCG-E16F7D80.md)

`JCG-E16F7D80` · `assertion`

The reciprocal pole-cancellation calculation classifies the relevant denominator as g=1+p^2 eta.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#prop:reciprocal-pole`
  - Does not establish: The locator alone is not an independent proof review.

### [The recorded degree-five and degree-six finite-field scans find no candidates in their…](../units/JCG-68EE8395.md)

`JCG-68EE8395` · `assertion`

The recorded degree-five and degree-six finite-field scans find no candidates in their enumerated strata, and the degree-six F5 candidates have no recorded lifts mod 25.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-023`
  - Does not establish: The locator alone is not an independent proof review.

### [Top priorities are independent certificate reproduction, the full bounded-degree local ring a…](../units/JCG-AF04161C.md)

`JCG-AF04161C` · `assertion`

Top priorities are independent certificate reproduction, the full bounded-degree local ring and degree-growth interface, intrinsic triple-cover defect exclusion, boundary-complete rigidity, the minimum degree-three coordinate bound, improved descendant dimensions/tensor rank, the five-dimensional classification, and explaining the two-dimensional obstruction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-044`
  - Does not establish: The locator alone is not an independent proof review.

### [Within the affine source-target orbit of the public map, total degree seven is minimal.](../units/JCG-0B37D36F.md)

`JCG-0B37D36F` · `assertion`

Within the affine source-target orbit of the public map, total degree seven is minimal.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-007`
  - Does not establish: The locator alone is not an independent proof review.

### [Within the full cubic-frame family, ordinary degree eleven is the first degree…](../units/JCG-CA01A7A7.md)

`JCG-CA01A7A7` · `assertion`

Within the full cubic-frame family, ordinary degree eleven is the first degree at which a genuine positive-dimensional stable modulus can occur.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:cubic-frame-degree-threshold`
  - Does not establish: The locator alone is not an independent proof review.

### [Within the quartic family, stable left-right equivalence holds exactly when (rho,sigma) agree…](../units/JCG-6B08BDE5.md)

`JCG-6B08BDE5` · `assertion`

Within the quartic family, stable left-right equivalence holds exactly when (rho,sigma) agrees; the normalized residual discriminant has intrinsic cusp and double-double strata and conductor divisor 2L+Q, so the family gives an affine plane of fixed-degree stable moduli.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-022`
  - Does not establish: The locator alone is not an independent proof review.

### [Within the reciprocal normal form, linear eta is classified by a weighted…](../units/JCG-9B9E87F1.md)

`JCG-9B9E87F1` · `assertion`

Within the reciprocal normal form, linear eta is classified by a weighted P(2,3) parameter and a j-invariant; degree 20 is the first nonbase member and degree 27 the first positive-dimensional family.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#sec:reciprocal-collision-line`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/reciprocal-family.tex#sec:reciprocal-degree-moduli`
  - Does not establish: The locator alone is not an independent proof review.

### [Arbitrarily large fixed-degree stable moduli](../units/RMU-6EACDABB.md)

`RMU-6EACDABB` · `corollary`

If \(\deg A=N+1\), the generic squarefree orbit space is
\[
\frac{
\{(s_i,v_i)_{i=1}^N\in(\Gm\times\Gm)^N:s_i\ne s_j\}
}{\Gm\times S_N},
\]
where \(\Gm\) scales the \(s_i\) and fixes the \(v_i\).  Its generic
dimension is \(2N-1\).  Fixing a root configuration with no scaling symmetry
leaves an \(N\)-dimensional family of pairwise stably inequivalent maps.
With the canonical interpolating representative for \(B\), every map in
such a family has
\[
\begin{gathered}
\det DG=-2,\qquad \mu(G)=3,\\
(\deg G_1,\deg G_2,\deg G_3)=(4N+7,4N+6,4).
\end{gathered}
\]
Here ``dimension'' means the dimension of the indicated coarse orbit locus;
the quotient notation does not assert that the unrestricted stable
left--right moduli functor is represented by this variety.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex#cor:large-stable-moduli`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md#label-cor-large-stable-moduli)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex#cor:large-stable-moduli`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md#label-cor-large-stable-moduli)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [For all \(q,q'\in\C\), \[ G_q\sim_{\mathrm{stable}}G_{q'} \quad\Longleftrightarrow\quad q=q'. \]](../units/RMU-BCC72317.md)

`RMU-BCC72317` · `corollary`

For all \(q,q'\in\C\),
\[
G_q\sim_{\mathrm{stable}}G_{q'}
\quad\Longleftrightarrow\quad
q=q'.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#cor:q-classification`](../../proof-sources/04-stable-moduli/main.md#label-cor-q-classification)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Multiplicity recovery](../units/RMU-D3C67A64.md)

`RMU-D3C67A64` · `lemma`

The common-factor multiplicity is
\[
m=
\begin{cases}
d,&p\ge d,\\[1mm]
(p+d)/2,&p<d.
\end{cases}
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#lem:common-factor-multiplicity`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-lem-common-factor-multiplicity)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Rigidity of the marked cylinder](../units/RMU-9826858C.md)

`RMU-9826858C` · `lemma`

Let \(q,q'\ne-2\) and \(m\ge0\).  Suppose a polynomial automorphism of
\(\A^{2+m}\) carries
\[
L_q\times\A^m\ \text{to}\ L_{q'}\times\A^m
\quad\text{and}\quad
M\times\A^m\ \text{to}\ M\times\A^m.
\]
Then \(q=q'\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#lem:marked-rigidity`](../../proof-sources/04-stable-moduli/main.md#label-lem-marked-rigidity)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [All-order formal-local versus stable separation](../units/RMU-DA627F3E.md)

`RMU-DA627F3E` · `proposition`

For every \(q\), there is a coefficientwise formal source automorphism
\[
\Phi_s=\id+\sum_{n\ge1}s^nV_n,
\qquad V_n\in\C[x,y,z]^3,
\]
such that \(F_s\circ\Phi_s=F_0\) in \(\C[x,y,z][[s]]^3\).  Thus all
\(q\)-arcs are source-trivial to every formal order, while fibers with
nonzero complex \(s\) and different \(q\) remain pairwise stably
inequivalent.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#prop:formal-stable-separation`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-prop-formal-stable-separation)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Bounded orbit map](../units/RMU-12B6BE0C.md)

`RMU-12B6BE0C` · `proposition`

The degree-preserving root translations form the kernel pair of the map
\[
\Theta_N\colon\operatorname{Tot}(E_N)\longrightarrow
\operatorname{Tot}(E_N),
\qquad
(\widehat Q,P)\longmapsto(\widehat Q,Z^NP).
\]
If \(\widehat Q=z^mQ_d\), with \(Q_d(0)\ne0\), then uniquely
\[
P=z^mP_d+Q_dS,\qquad \deg P_d<d,\quad\deg S<m.
\]
The finite-root decoration is \(P_d\); root translation removes precisely
the principal part \(S/z^m\) supported at infinity.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#prop:bounded-root-translation-groupoid`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-prop-bounded-root-translation-groupoid)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Finite-root chart and weighted divisor](../units/RMU-E2D30D91.md)

`RMU-E2D30D91` · `proposition`

The \(\delta_a\)-chart of \(\mathfrak B_D\) is canonically
\(\A^2_{c,t}\).  On it,
\[
\mathfrak J\mathcal O_{\A^2}
=\bigl(\rho(c)H_0(c,t)^3\bigr).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:relative-jacobian-chart`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-prop-relative-jacobian-chart)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [For every \(\alpha,\beta\in\C\), the map \(G_{\alpha,\beta}\) is polynomial, \[ \det DG_{\alp…](../units/RMU-C933C1F1.md)

`RMU-C933C1F1` · `proposition`

For every \(\alpha,\beta\in\C\), the map \(G_{\alpha,\beta}\) is polynomial,
\[
\det DG_{\alpha,\beta}=-2,
\]
and its generic degree is three.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:basic`](../../proof-sources/04-stable-moduli/main.md#label-prop-basic)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [For every \(\beta\in\C\), \[ G_{0,\beta} = \Xi_{\beta/3}\circ G_{0,0}\circ\Theta_{\beta/3}. \…](../units/RMU-5D10190F.md)

`RMU-5D10190F` · `proposition`

For every \(\beta\in\C\),
\[
G_{0,\beta}
=
\Xi_{\beta/3}\circ G_{0,0}\circ\Theta_{\beta/3}.
\]
In particular, the entire line \(\alpha=0\) is one ordinary left--right
orbit.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:alpha-zero-gauge`](../../proof-sources/04-stable-moduli/main.md#label-prop-alpha-zero-gauge)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [For every \(q\in\C\), \[ S_{G_q}=D_q\cup P. \] These are the two irreducible…](../units/RMU-FF941A1E.md)

`RMU-FF941A1E` · `proposition`

For every \(q\in\C\),
\[
S_{G_q}=D_q\cup P.
\]
These are the two irreducible components.  For \(q\ne-2\), the component
\(D_q\) is singular and \(P\) is smooth.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:NP`](../../proof-sources/04-stable-moduli/main.md#label-prop-np)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Intrinsic common planes](../units/RMU-47458E0D.md)

`RMU-47458E0D` · `proposition`

For a deleted root \(s\) of \(A\),
\[
B(s)=0
\quad\Longleftrightarrow\quad
V(\delta)\cap V(c-s)
\text{ is scheme-theoretically nonreduced}.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:intrinsic-common-planes`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-prop-intrinsic-common-planes)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [No member with \(\alpha=0\) is stably left--right equivalent to a member with \(\alpha\ne0\).](../units/RMU-98BF1795.md)

`RMU-98BF1795` · `proposition`

No member with \(\alpha=0\) is stably left--right equivalent to a member
with \(\alpha\ne0\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:zero-vs-nonzero`](../../proof-sources/04-stable-moduli/main.md#label-prop-zero-vs-nonzero)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [One-root transition](../units/RMU-29697C11.md)

`RMU-29697C11` · `proposition`

On the open part
\[
 q_N=0,\qquad q_{N-1}\operatorname{Res}(Q,B)\ne0,
\]
put
\[
 \kappa=\frac{r_{N-1}}{q_{N-1}},\qquad
 r'_j=r_j-\kappa q_j\quad(0\le j\le N-2),
 \qquad q_0=1.
\]
Then the coefficient change is invertible and equivariant, with \(\kappa\)
of weight two.  The boundary chart is the length-\((N-1)\) chart times
\(\A^1_\kappa\), and the map to polynomial left--right orbit data contracts
the second factor.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:one-root-transition`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-prop-one-root-transition)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Primitive discriminant](../units/RMU-FD5552E4.md)

`RMU-FD5552E4` · `proposition`

Its coefficient content in \(a,b\) is
\[
\chi(c)=\gcd(A(c),B(c)^2),
\]
normalized by \(\chi(0)=1\).  The polynomial
\(\delta=\Delta/\chi\) is irreducible, and
\[
S_{G_{A,B}}
=V(\delta)\cup
\bigcup_{s\in V(Q)_{\mathrm{red}}}V(c-s).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:primitive-discriminant-content`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-prop-primitive-discriminant-content)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [The exceptional weighted stratum](../units/RMU-CE68C0FD.md)

`RMU-CE68C0FD` · `proposition`

For the exceptional quadratic member
\(A=c(c+1)\), \(B=-2(c+1)^2\), one has
\[
\rho=(c+1)^2,\qquad H_0=3ct-2(c+1).
\]
Thus its special behavior is the intrinsic vertical multiplicity two, not
an ad hoc extra orbit invariant.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#prop:q-minus-two-weighted-stratum`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-prop-q-minus-two-weighted-stratum)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [The map \(G_{-2}\) is not stably left--right equivalent to \(G_q\) for any \(q\ne-2\).](../units/RMU-145A81FE.md)

`RMU-145A81FE` · `proposition`

The map \(G_{-2}\) is not stably left--right equivalent to \(G_q\) for any
\(q\ne-2\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:exceptional`](../../proof-sources/04-stable-moduli/main.md#label-prop-exceptional)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [The map \(\nu_q\) is the normalization of \(D_q\). Moreover, \[ \nu_q^{-1}(\Sing D_q)=…](../units/RMU-12969944.md)

`RMU-12969944` · `proposition`

The map \(\nu_q\) is the normalization of \(D_q\).  Moreover,
\[
\nu_q^{-1}(\Sing D_q)=
L_q:=V(H_q).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#prop:normalization`](../../proof-sources/04-stable-moduli/main.md#label-prop-normalization)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Universal cubic frame](../units/RMU-0EE0664D.md)

`RMU-0EE0664D` · `proposition`

For every admissible pair, \(G_{A,B}\) is polynomial and
\[
\det DG_{A,B}=-2.
\]
If \(A\ne0\), its generic degree is three.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex#prop:general-frame`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md#label-prop-general-frame)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [All-multiplicity fixed-frame Torelli](../units/RMU-F7236EAC.md)

`RMU-F7236EAC` · `theorem`

Let \((A,B)\) and \((\widetilde A,\widetilde B)\) be admissible cubic
frames, with \(A/c\) and \(\widetilde A/c\) nonconstant.  The following are
equivalent:
\begin{enumerate}[label=(\roman*)]
\item \(G_{A,B}\) and \(G_{\widetilde A,\widetilde B}\) are stably
left--right equivalent;
\item they are ordinarily polynomially left--right equivalent;
\item there is \(u\in\C^\times\) such that
\[
\widetilde A(uc)=uA(c),\qquad
\widetilde B(uc)-B(c)\in cA(c)\C[c].
\]
\end{enumerate}
No squarefreeness or coprimality hypothesis is required.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#thm:all-multiplicity-torelli`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-thm-all-multiplicity-torelli)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Complete stable classification](../units/RMU-9075E071.md)

`RMU-9075E071` · `theorem`

The stable polynomial left--right orbit set of the family
\(\set{G_{\alpha,\beta}}\) is
\[
\set{\mathcal O_0}
\ \sqcup\
\set{\mathcal O_q:q\in\C},
\]
where
\[
\mathcal O_0=\set{G_{0,\beta}:\beta\in\C}
\]
and
\[
\mathcal O_q=
\set{G_{\alpha,\beta}:
      \alpha\ne0,\ \beta/\alpha^2=q}.
\]
More explicitly:
\begin{enumerate}[label=(\roman*)]
\item all maps \(G_{0,\beta}\) are ordinarily left--right equivalent;
\item no \(G_{0,\beta}\) is stably equivalent to a member with
      \(\alpha\ne0\); and
\item if \(\alpha,\alpha'\ne0\), then
\[
G_{\alpha,\beta}\sim_{\mathrm{stable}}G_{\alpha',\beta'}
\quad\Longleftrightarrow\quad
\frac{\beta}{\alpha^2}=\frac{\beta'}{\alpha'^2}.
\]
\end{enumerate}

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/main.tex#thm:main`](../../proof-sources/04-stable-moduli/main.md#label-thm-main)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#thm:main`](../../proof-sources/04-stable-moduli/main.md#label-thm-main)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Degree threshold inside the cubic frame](../units/RMU-4F11D967.md)

`RMU-4F11D967` · `theorem`

Every polynomial member of ordinary degree at most ten in the full cubic
frame is polynomially source--target equivalent to the degree-seven base
map.  Degree eleven is the first degree at which genuine moduli occur in
this frame.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:cubic-frame-degree-threshold`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-cubic-frame-degree-threshold)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Degree-fifteen stable moduli](../units/RMU-672CA05F.md)

`RMU-672CA05F` · `theorem`

The associated maps are polynomial Keller maps of component degrees
\((15,14,4)\), generic degree three, and generic monodromy \(S_3\).
Their stable equivalence relation is exactly
\[
(s,d_1,d_2)\sim(1/s,d_2,d_1).
\]
Consequently degree fifteen contains a three-dimensional stable-moduli
family, modulo this finite involution.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:degree-fifteen-moduli`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-degree-fifteen-moduli)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Differential description](../units/RMU-441A6E6C.md)

`RMU-441A6E6C` · `theorem`

The invariant algebra is
\[
A^K=\ker\left(
A\xrightarrow{d_{X/R}}
A\otimes_R E^\vee
\longrightarrow
A\otimes_R\operatorname{coker}(M^\vee)
\right).
\]
Equivalently, in homogeneous degree \(r\), it is the kernel of one finite
syzygy map
\[
\operatorname{Sym}^r(E^\vee)\longrightarrow
\operatorname{Sym}^{r-1}(E^\vee)\otimes_R\operatorname{coker}(M^\vee).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#thm:categorical-differential-kernel`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-thm-categorical-differential-kernel)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Exact discriminant conductor](../units/RMU-1D0AD178.md)

`RMU-1D0AD178` · `theorem`

The map
\[
\nu:\A^2_{c,t}\longrightarrow V(\Delta_{A,B}),
\]
\[
v=-3A(c)t^2-2B(c)t,\qquad
u=-A(c)t^3-\frac12B(c)t^2
\]
is the normalization.  If
\[
H(c,t)=3A(c)t+B(c),
\]
then the conductor in \(\C[c,t]\) is exactly
\[
H^2\C[c,t].
\]
Its contraction to the discriminant coordinate ring is generated by
\[
B^2-3Av,\qquad -18Au-Bv.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:cubic-frame-conductor`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-cubic-frame-conductor)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Growing stable moduli](../units/RMU-89D56BE2.md)

`RMU-89D56BE2` · `theorem`

For every \(n\ge2\), the cubic frame contains a coarse stable-moduli locus
of dimension \(2n-3\), represented by generic-degree-three Keller maps of
ordinary degree \(4n+3\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:growing-cubic-frame-moduli`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-growing-cubic-frame-moduli)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [If \(q,q'\ne-2\), then \(G_q\) and \(G_{q'}\) are stably polynomially left--right equivalent…](../units/RMU-1D275DF8.md)

`RMU-1D275DF8` · `theorem`

If \(q,q'\ne-2\), then \(G_q\) and \(G_{q'}\) are stably polynomially
left--right equivalent if and only if \(q=q'\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#thm:stable-nonexceptional`](../../proof-sources/04-stable-moduli/main.md#label-thm-stable-nonexceptional)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [One-wall control](../units/RMU-69047096.md)

`RMU-69047096` · `theorem`

Inside the generic polynomial algebra,
\[
A_N^{K_N}
=
A_N\cap (A_N^{K_N})_{(q_N)}.
\]
Thus simultaneous escapes impose no additional divisorial conditions on
global invariant functions.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#thm:one-wall-control`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-thm-one-wall-control)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Rank-one wall obstruction](../units/RMU-428FCD53.md)

`RMU-428FCD53` · `theorem`

Let \(R\) be a DVR with uniformizer \(\pi\), let \(e\ge 1\), and let
\[
K_e=\operatorname{Spec} R[s]/(\pi^es)
\]
act on \(\mathbb A^1_R\) by translation.  Its fppf orbit sheaf is not an algebraic
space, and the quotient stack is not an algebraic stack.  Consequently the
bounded cubic-frame fppf quotient has the same failure along its generic
one-root wall.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/categorical-boundary-quotient.tex#thm:fppf-wall-nonalgebraic`](../../proof-sources/04-stable-moduli/appendices/categorical-boundary-quotient.md#label-thm-fppf-wall-nonalgebraic)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Stable boundary Torelli on the squarefree locus](../units/RMU-47B48FBA.md)

`RMU-47B48FBA` · `theorem`

Let \((A,B)\) and \((\widetilde A,\widetilde B)\) be admissible squarefree
coprime pairs.  The following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item \(G_{A,B}\) and \(G_{\widetilde A,\widetilde B}\) are stably
polynomially left--right equivalent;
\item they are ordinarily polynomially left--right equivalent;
\item there is \(u\in\C^*\) such that
\[
\widetilde A(uc)=uA(c),\qquad
\widetilde B(uc)-B(c)\in cA(c)\C[c];
\]
\item multiplication by \(u\) identifies the decorated finite schemes
\[
(Z_A^\circ,\sigma_B)
\quad\text{and}\quad
(Z_{\widetilde A}^\circ,\sigma_{\widetilde B}).
\]
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex#thm:general-boundary-torelli`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md#label-thm-general-boundary-torelli)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Stable conductor-arrangement classification](../units/RMU-A7F1B713.md)

`RMU-A7F1B713` · `theorem`

Assume \(A,A'\) are squarefree and
\[
\gcd(A,B)=\gcd(A',B')=1.
\]
Two marked arrangements
\[
\left(\A^2,L_{A,B},\{M_\rho\}_{\rho\in S}\right)
\quad\text{and}\quad
\left(\A^2,L_{A',B'},\{M_{\rho'}\}_{\rho'\in S'}\right)
\]
become isomorphic after multiplication by an affine space if and only if
there exist
\[
\gamma(c)=\lambda c+\mu,\quad \lambda\ne0,\qquad
\nu,\kappa\in\C^*,\qquad h(c)\in\C[c],
\]
such that \(\gamma\) carries the marked roots to the marked roots and
\[
A'(\gamma(c))\nu=\kappa A(c),
\]
\[
B'(\gamma(c))+3A'(\gamma(c))h(c)=\kappa B(c).
\]
Stabilization introduces no additional transformations.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/conductor-arrangements.tex#thm:conductor-arrangement-classification`](../../proof-sources/04-stable-moduli/appendices/conductor-arrangements.md#label-thm-conductor-arrangement-classification)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

## Open frontier

### [Can the marked-cylinder rigidity argument be formulated as a general cancellation theorem…](../units/RMU-B33630FC.md)

`RMU-B33630FC` · `question`

Can the marked-cylinder rigidity argument be formulated as a general
cancellation theorem for pairs \((\A^2,L,M)\)?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/main.tex`](../../proof-sources/04-stable-moduli/main.md)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex`](../../proof-sources/04-stable-moduli/main.md)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Compactification across boundary collisions](../units/RMU-0F24638D.md)

`RMU-0F24638D` · `question`

Can the all-multiplicity finite-root classification of
\cref{thm:all-multiplicity-torelli} be compactified across strata where
deleted roots escape to \(c=\infty\)?  The elementary one-root transition
on the resultant-open locus is the contracted gauge chart of
\cref{prop:one-root-transition}.  The desired object must also handle
simultaneous escapes and the nonunit resultant boundary while retaining the
weighted relative-Jacobian data as the number of finite marked planes
changes.

Dependencies:

- `uses` `RMU-F7236EAC`: Formal statement references thm:all-multiplicity-torelli.
- `uses` `RMU-29697C11`: Formal statement references prop:one-root-transition.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/main.tex#q:compactified-stable-moduli`](../../proof-sources/04-stable-moduli/main.md#label-q-compactified-stable-moduli)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex#q:compactified-stable-moduli`](../../proof-sources/04-stable-moduli/main.md#label-q-compactified-stable-moduli)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Construct a different-filtered source-flow or transferred L-infinity model that independently…](../units/JCG-D9E57688.md)

`JCG-D9E57688` · `question`

Construct a different-filtered source-flow or transferred L-infinity model that independently reproduces the bounded-degree Kuranishi equations and the length-584 Artin algebra.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`
  - Does not establish: The locator alone is not an independent proof review.

### [Extend the finite-root all-multiplicity classification across strata where deleted roots esca…](../units/JCG-4EE846CD.md)

`JCG-4EE846CD` · `question`

Extend the finite-root all-multiplicity classification across strata where deleted roots escape to c=infinity and the number of finite marked planes changes.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#q:all-multiplicity-infinity-gluing`
  - Does not establish: The locator alone is not an independent proof review.

### [For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree…](../units/JCG-4451EE05.md)

`JCG-4451EE05` · `question`

For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree delta_LR(xi)=min{deg H : H is polynomially left-right equivalent to xi} from intrinsic conductor, ramification, valuation, or nonproperness data. A bound of at least seven for every nontrivial generic-degree-three boundary class would supply the missing degree-cost bridge from cubic-cover classification to low-degree exclusion.

### [Gluing at infinity](../units/RMU-70C8596F.md)

`RMU-70C8596F` · `question`

Can \cref{prop:one-root-transition} be extended across simultaneous root
escapes, the nonunit resultant boundary, and the weighted
relative-Jacobian marking to give a full compactification?  This also
includes comparison with the \(\alpha=0\) stratum and remains separate from
the finite-root theorem above.

Dependencies:

- `uses` `RMU-29697C11`: Formal statement references prop:one-root-transition.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#q:all-multiplicity-infinity-gluing`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-q-all-multiplicity-infinity-gluing)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.tex#q:all-multiplicity-infinity-gluing`](../../proof-sources/04-stable-moduli/appendices/all-multiplicity-relative-jacobian.md#label-q-all-multiplicity-infinity-gluing)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [What scheme or stack represents deformations of the maps in \cref{thm:main} modulo…](../units/RMU-476900CB.md)

`RMU-476900CB` · `question`

What scheme or stack represents deformations of the maps in
\cref{thm:main} modulo stable polynomial left--right equivalence?

Dependencies:

- `uses` `RMU-9075E071`: Formal statement references thm:main.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/main.tex`](../../proof-sources/04-stable-moduli/main.md)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex`](../../proof-sources/04-stable-moduli/main.md)
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Which larger finite-dimensional cubic-frame families admit complete stable invariants recover…](../units/RMU-2C302CB2.md)

`RMU-2C302CB2` · `question`

Which larger finite-dimensional cubic-frame families admit complete stable
invariants recovered from their normalized nonproperness divisors?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/04-stable-moduli/main.tex`](../../proof-sources/04-stable-moduli/main.md)
  - Full source and surrounding context: [`manuscripts/04-stable-moduli/main.tex`](../../proof-sources/04-stable-moduli/main.md)
  - Does not establish: Presence in the manuscript is not an independent proof audit.
