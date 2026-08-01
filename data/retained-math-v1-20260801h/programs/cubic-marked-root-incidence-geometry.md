# Cubic Marked-Root Incidence Geometry

A program about normalized marked-root constructions, cubic covers, lost sheets, moving hyperplanes, and the boundary between a universal mechanism and features special to the known example.

This is a generated progress view of retained mathematics. Workflow labels and private source locators are intentionally omitted.

<!-- noncanonical-overlay -->

## Setup and research posture

This program studies generic-degree-three Keller maps through their finite
cubic normalization, marked-root presentation, conductor, and quadratic
resolvent. The central unresolved distinction is between divisorial control
and isolated nonflatness. The trace-zero module is well constrained away
from finitely many boundary points, but reflexivity by itself does not remove
those points.

Keep two transitions separate. First, a Keller-specific argument must turn
the resolvent eigensheaf or conormal root into a maximal Cohen--Macaulay
object and eliminate the finite defect. Second, a boundary-completeness
argument must recover the required affine opening from the finite cover.
Neither transition is a consequence of the other.

## Strategy and payoff

The highest-leverage route is to formulate the actual conormal-root pushdown
problem intrinsically. Specify the eigensheaf, its overlap maps, conductor
data, and every normality, smoothness, and source-splitting hypothesis. The
corrected comparison theorem makes the remaining input literal: construct a
rank-one reflexive MCM module with the same height-two classes as the cubic
eigensheaf. Dao's codimension-two detection then supplies the comparison,
but not the missing construction.

A partial result is useful when it produces exact divisor, discrepancy, or
intersection data. Those data can turn the remaining depth or cohomology
question into a finite lattice computation. Do not start that computation
before its geometric inputs exist.

An alternative route studies whether local three-torsion classes survive
around the complete boundary. Local algebraization alone is not survival;
the end-to-global compatibility is the substance.

## Connections

The finite-cover and boundary questions connect directly to the stable-moduli
program, while the marked-root formulas feed the deformation program's
source-flow complex. Quartic minimum-degree work may use a completed cubic
classification, but should not import it conditionally without naming both
flatness and boundary-completeness gates.

## Current priorities and research freedom

The current attention order is:

1. construct, or sharply obstruct, the Keller-specific conormal-root MCM
   module required by the corrected comparison criterion;
2. derive any resulting exceptional-lattice inputs exactly;
3. audit the new explicit affine-opening and master-cover repairs while
   keeping finite flatness as a separate dependency node; and
4. investigate global survival or forced death of the residual local
   torsors.

These are optional on-ramps. A stronger structural theorem, a countermodel
showing a proposed hypothesis is insufficient, or a clean connection to
another retained unit is equally valuable when its scope is explicit.

## Graveyard and scope fences

- Projectively compatible theta data need not have commuting linear lifts;
  the Weil-pairing commutator cannot be ignored.
- Normal cubic covers need not be flat, and rank-two reflexive modules on a
  threefold need not be locally free at isolated points.
- A codimension-one sheet-loss taxonomy does not classify isolated defects.
- A local or formal torsor does not automatically extend around the full
  boundary.
- Do not turn the conditional master-cover comparison into an unconditional
  classification.

## Definitions and constructions

### [An \emph{admissible triple} is \[ (A,B,\alpha),\qquad A,B\in\C[c],\quad A\ne0, \] satisfying…](../units/RMU-1514F750.md)

`RMU-1514F750` · `definition`

An \emph{admissible triple} is
\[
(A,B,\alpha),\qquad
A,B\in\C[c],\quad A\ne0,
\]
satisfying \eqref{eq:admissibility}.  We use the representative
\(w=w_{A,B,\alpha}\) displayed in \eqref{eq:w-jet}, with no \(x^3\)
remainder, and write \(F_{A,B,\alpha}\) for the resulting polynomial map.

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#def:admissible`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

## Retained results

### [A generically degree-three Keller map admits a useful normalization picture: a finite…](../units/JCG-26FD089B.md)

`JCG-26FD089B` · `assertion`

A generically degree-three Keller map admits a useful normalization picture: a finite normalization X over the target together with an open embedding of A3, expressible through a finite-flat binary-cubic model.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-012`
  - Does not establish: The locator alone is not an independent proof review.

### [A minimal defect can only occur over an omitted singleton fiber of scheme length at least four.](../units/JCG-DCDBDDDB.md)

`JCG-DCDBDDDB` · `assertion`

A minimal defect can only occur over an omitted singleton fiber of scheme length at least four.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-008`
  - Does not establish: The locator alone is not an independent proof review.

### [A rank-three affine-linear family whose full simple-root incidence is affine three-space lies…](../units/JCG-DBB38171.md)

`JCG-DBB38171` · `assertion`

A rank-three affine-linear family whose full simple-root incidence is affine three-space lies in the tangent-but-not-osculating orbit and recovers the base map up to left-right equivalence.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-005`
  - Does not establish: The locator alone is not an independent proof review.

### [A reduced frame potential of root degree n>=4 has leading coefficient vanishing…](../units/JCG-7C0CF125.md)

`JCG-7C0CF125` · `assertion`

A reduced frame potential of root degree n>=4 has leading coefficient vanishing to order at least floor(n/2)+1 at the retained infinity point; the bound is sharp and yields component degrees (3n+4,3n+3,4) for even n and (3n+2,3n+1,4) for odd n.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-030`
  - Does not establish: The locator alone is not an independent proof review.

### [A=c(c-1)^2, B=2(c-1) gives an exact U2 Keller example whose omission locus is…](../units/JCG-FF7A1933.md)

`JCG-FF7A1933` · `assertion`

A=c(c-1)^2, B=2(c-1) gives an exact U2 Keller example whose omission locus is strictly smaller than the singular locus of the nonproperness set.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/common-zero-normalization.tex#prop:u2-example`
  - Does not establish: The locator alone is not an independent proof review.

### [Algebraize the formal/radial ruling strongly enough to exclude the remaining nonhomogeneous m…](../units/JCG-5716FF00.md)

`JCG-5716FF00` · `assertion`

Algebraize the formal/radial ruling strongly enough to exclude the remaining nonhomogeneous minimal defect.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-037`
  - Does not establish: The locator alone is not an independent proof review.

### [An affine-root incidence component of degree at least two cannot be A2,…](../units/JCG-06EFD647.md)

`JCG-06EFD647` · `assertion`

An affine-root incidence component of degree at least two cannot be A2, and a generically squarefree affine-linear projective coefficient family has no connected full simple-root incidence isomorphic to A2.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-016`
  - Does not establish: The locator alone is not an independent proof review.

### [Assume a zero-dimensional log-canonical resolvent center admits the stated equivariant plt ex…](../units/JCG-FD961DD5.md)

`JCG-FD961DD5` · `assertion`

Assume a zero-dimensional log-canonical resolvent center admits the stated equivariant plt extraction with canonical cyclic cover. Nonneutral conormal residues are maximal Cohen-Macaulay by positivity; if a neutral three-torsion eigensheaf has nonzero H1, S3 symmetry forces its cyclic cover to be an abelian surface. In the multiplicity-six double-plane model the branch tangent sextic is then the nine-cuspidal dual of a smooth plane cubic.

### [At the first possible defect stratum the discriminant has multiplicity at least…](../units/JCG-F9F6311C.md)

`JCG-F9F6311C` · `assertion`

At the first possible defect stratum the discriminant has multiplicity at least six and the exceptional boundary has an elliptic-type constraint.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-010`
  - Does not establish: The locator alone is not an independent proof review.

### [Can the common-root integral-closure theorem and left-right equivalence result be independent…](../units/JCG-E9F3362D.md)

`JCG-E9F3362D` · `assertion`

Can the common-root integral-closure theorem and left-right equivalence result be independently proved or formalized?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-039`
  - Does not establish: The locator alone is not an independent proof review.

### [Does the U1/U2/B trichotomy hold in the claimed generality beyond the normalized family?](../units/JCG-89916A56.md)

`JCG-89916A56` · `assertion`

Does the U1/U2/B trichotomy hold in the claimed generality beyond the normalized family?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-038`
  - Does not establish: The locator alone is not an independent proof review.

### [Escape rates are \(\varepsilon^{-1/2}\) near a smooth discriminant point and \(\varepsilon^{-…](../units/JCG-914949BF.md)

`JCG-914949BF` · `assertion`

Escape rates are \(\varepsilon^{-1/2}\) near a smooth discriminant point and \(\varepsilon^{-2/3}\) near the cusp, with more degenerate arcs allowing larger half-integral exponents.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-019`
  - Does not establish: The locator alone is not an independent proof review.

### [Every Keller map has an infinite-dimensional first-order left-right automorphism space over t…](../units/JCG-931C6D98.md)

`JCG-931C6D98` · `assertion`

Every Keller map has an infinite-dimensional first-order left-right automorphism space over the dual numbers, naturally identified with polynomial vector fields on the target; stabilization also adds inert diagonal affine automorphisms.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-034`
  - Does not establish: The locator alone is not an independent proof review.

### [Every generic-degree-three Keller map factors through a finite normal cubic cover whose…](../units/JCG-C04524CF.md)

`JCG-C04524CF` · `assertion`

Every generic-degree-three Keller map factors through a finite normal cubic cover whose trace-zero module is rank-two reflexive and locally free away from finitely many target points.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-006`
  - Does not establish: The locator alone is not an independent proof review.

### [Every nonzero constant combination of the inverse-Jacobian vector fields is incomplete.](../units/JCG-87B4A2F9.md)

`JCG-87B4A2F9` · `assertion`

Every nonzero constant combination of the inverse-Jacobian vector fields is incomplete.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-020`
  - Does not establish: The locator alone is not an independent proof review.

### [Every nonzero quadratic Hessian contraction with nonzero coefficient is excluded from the…](../units/JCG-A844E87D.md)

`JCG-A844E87D` · `assertion`

Every nonzero quadratic Hessian contraction with nonzero coefficient is excluded from the cubic full-incidence construction: the target hypersurface and full marked-root incidence cannot both be isomorphic to A3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#thm:hessian-exclusion`
  - Does not establish: The locator alone is not an independent proof review.

### [Every quartic frame has T^4 coefficient divisible by c^3 and first jet…](../units/JCG-9E1E87CA.md)

`JCG-9E1E87CA` · `assertion`

Every quartic frame has T^4 coefficient divisible by c^3 and first jet satisfying delta+4gamma+12kappa=0; the displayed quartic realizes these conditions with determinant -2, generic degree four, and component degrees (16,15,4).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-016`
  - Does not establish: The locator alone is not an independent proof review.

### [Flatness of the finite cubic normalization is equivalent to vanishing of a…](../units/JCG-248AD7B9.md)

`JCG-248AD7B9` · `assertion`

Flatness of the finite cubic normalization is equivalent to vanishing of a finite defect module expressible through Ext data.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-007`
  - Does not establish: The locator alone is not an independent proof review.

### [For a complex generic-degree-three Keller map, every target prime divisor has a…](../units/JCG-1D7EF048.md)

`JCG-1D7EF048` · `assertion`

For a complex generic-degree-three Keller map, every target prime divisor has a retained unramified sheet and hence only the U1, U2, or B deleted-sheet type; a deleted three-cycle is impossible, and the generic monodromy is S3.

Support:

- **source assertion:** theorem and proof — `manuscripts/01-cubic-incidence/appendices/cubic-resolvent-defects.tex#prop:cubic-divisorial-trichotomy`
  - Does not establish: The locator alone is not an independent proof review.

### [For a constant nonzero level of the universal marked incidence, a moving…](../units/JCG-82D7FF25.md)

`JCG-82D7FF25` · `assertion`

For a constant nonzero level of the universal marked incidence, a moving tangent hyperplane that remains tangent but nonosculating is polynomially gauge-equivalent to the fixed public hyperplane.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#thm:moving-tangent`
  - Does not establish: The locator alone is not an independent proof review.

### [For a finite normalization of the cubic cover, the trace-zero module is…](../units/JCG-A5938472.md)

`JCG-A5938472` · `assertion`

For a finite normalization of the cubic cover, the trace-zero module is reflexive and the nonflat locus is finite; flatness and the global cubic package require an additional Cohen-Macaulay hypothesis.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-015`
  - Does not establish: The locator alone is not an independent proof review.

### [For all admissible A,B,alpha triples, polynomial left-right equivalence is classified by an…](../units/JCG-221985FF.md)

`JCG-221985FF` · `assertion`

For all admissible A,B,alpha triples, polynomial left-right equivalence is classified by an affine change of c, scalar equality of A, congruence of B modulo A, and preservation of the marked root; no squarefreeness hypothesis is needed.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:equivalence`
  - Does not establish: The locator alone is not an independent proof review.

### [For an omitted value p of a complex Keller map F from…](../units/JCG-E82019D2.md)

`JCG-E82019D2` · `assertion`

For an omitted value p of a complex Keller map F from A3 to A3, the direction map x maps to [F(x)-p] from A3 to P2 is smooth of relative dimension one and has image equal to P2 minus at most finitely many points.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#prop:omitted-direction-map`
  - Does not establish: The locator alone is not an independent proof review.

### [For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t…](../units/JCG-0106262F.md)

`JCG-0106262F` · `assertion`

For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-025`
  - Does not establish: The locator alone is not an independent proof review.

### [For every admissible coprime cubic-frame pair, the homogenized inverse cubic defines a…](../units/JCG-EB1B80E7.md)

`JCG-EB1B80E7` · `assertion`

For every admissible coprime cubic-frame pair, the homogenized inverse cubic defines a smooth finite-flat Gorenstein triple cover of affine three-space with trivial rank-two Tschirnhausen bundle and distinguished homogeneous-root frame.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-032`
  - Does not establish: The locator alone is not an independent proof review.

### [For every complex polynomial Keller map, the omitted-value locus is contained in…](../units/JCG-0A41960D.md)

`JCG-0A41960D` · `assertion`

For every complex polynomial Keller map, the omitted-value locus is contained in the singular locus of the reduced nonproperness set.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/omitted-values.tex#thm:omitted-singular`
  - Does not establish: The locator alone is not an independent proof review.

### [For every coprime admissible cubic-frame pair, the generic function-field extension has no…](../units/JCG-5B09E55B.md)

`JCG-5B09E55B` · `assertion`

For every coprime admissible cubic-frame pair, the generic function-field extension has no nontrivial deck transformation; ordinary source automorphisms over the identity target are therefore trivial.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-036`
  - Does not establish: The locator alone is not an independent proof review.

### [For every coprime normalized cubic-frame pair in the stated family, the inverse…](../units/JCG-504733CF.md)

`JCG-504733CF` · `assertion`

For every coprime normalized cubic-frame pair in the stated family, the inverse cubic is irreducible with nonsquare discriminant over C(a,b,c), so its generic Galois closure and geometric monodromy are S3.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-027`
  - Does not establish: The locator alone is not an independent proof review.

### [For every generic-degree-three Keller normalization, base change to the affine source splits…](../units/JCG-BD8A0F77.md)

`JCG-BD8A0F77` · `assertion`

For every generic-degree-three Keller normalization, base change to the affine source splits the cubic algebra as S times S[eta]/(eta^2-D), implying flatness at every attained target point and a canonical marked-root form on the source.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-023`
  - Does not establish: The locator alone is not an independent proof review.

### [For every integer d at least 3, there is a nonproper Keller…](../units/JCG-D739C229.md)

`JCG-D739C229` · `assertion`

For every integer d at least 3, there is a nonproper Keller map from complex affine 3-space to itself with generic degree d.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-001`
  - Does not establish: The locator alone is not an independent proof review.

### [For every n>=3 the displayed explicit frame potential defines a three-variable polynomial…](../units/JCG-12EBB4BD.md)

`JCG-12EBB4BD` · `assertion`

For every n>=3 the displayed explicit frame potential defines a three-variable polynomial Keller map of generic degree n and determinant -2, attaining the sharp frame-degree bound.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-031`
  - Does not establish: The locator alone is not an independent proof review.

### [For every product of evaluations at two distinct points, the quadratic target…](../units/JCG-BBB01109.md)

`JCG-BBB01109` · `assertion`

For every product of evaluations at two distinct points, the quadratic target hypersurface A2+kappa E_xi E_eta=c is isomorphic to A3, but its full marked-root preimage is never A3; its compactly supported Euler characteristic is never one.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#thm:two-evaluation-exclusion`
  - Does not establish: The locator alone is not an independent proof review.

### [For multiplication-incidence opens from P^a x P^b, the next (2,3) candidate fails…](../units/JCG-292A9B9D.md)

`JCG-292A9B9D` · `assertion`

For multiplication-incidence opens from P^a x P^b, the next (2,3) candidate fails to have the affine-space class/count expected of A^5; the original (1,2) case is singled out within the stated incidence-coordinate class.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-004`
  - Does not establish: The locator alone is not an independent proof review.

### [For positive boundary length, the hidden ordinary complex-point automorphism kernel vanishes…](../units/JCG-1FEDD133.md)

`JCG-1FEDD133` · `assertion`

For positive boundary length, the hidden ordinary complex-point automorphism kernel vanishes and Aut_LR(G_{A,B}) is the finite stabilizer of the decorated boundary scheme (Z_A,B|Z_A).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-035`
  - Does not establish: The locator alone is not an independent proof review.

### [For rank-one pure-square quadratic covariants in the Cartan-square component, exactly one end…](../units/JCG-1B3C86D8.md)

`JCG-1B3C86D8` · `assertion`

For rank-one pure-square quadratic covariants in the Cartan-square component, exactly one endpoint is gauge-equivalent to the base tangent-hyperplane construction and every other classified orbit fails to give a full incidence isomorphic to A3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#thm:rank-one-cartan`
  - Does not establish: The locator alone is not an independent proof review.

### [For squarefree A and marked missing-infinity roots, stabilized isomorphism classes of normali…](../units/JCG-5542AF40.md)

`JCG-5542AF40` · `assertion`

For squarefree A and marked missing-infinity roots, stabilized isomorphism classes of normalized conductor arrangements are exactly classified by affine changes of c, affine-linear changes of t over c, the affine root configuration of A, and the projective vector of conductor values B(rho) modulo induced finite permutations.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:conductor-arrangement-classification`
  - Does not establish: The locator alone is not an independent proof review.

### [For the analyzed minimal smooth defect end, the local sign-three torsor group…](../units/JCG-A9379D6C.md)

`JCG-A9379D6C` · `assertion`

For the analyzed minimal smooth defect end, the local sign-three torsor group is K_loc congruent to C[3] congruent to F_3^2, and its two nonzero directions are represented by algebraic finite covers over the henselian local end.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#thm:local-sign-torsors`
  - Does not establish: The locator alone is not an independent proof review.

### [For the discriminant surface of A(c)T^3+B(c)T^2+vT-2u with gcd(A,B)=1, the normalization cond…](../units/JCG-AE66472A.md)

`JCG-AE66472A` · `assertion`

For the discriminant surface of A(c)T^3+B(c)T^2+vT-2u with gcd(A,B)=1, the normalization conductor is exactly H^2 C[c,t], where H=3A(c)t+B(c), and its contraction is generated by B^2-3Av and -18Au-Bv.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:cubic-frame-conductor`
  - Does not establish: The locator alone is not an independent proof review.

### [For the normalized cubic discriminant, with H=3A(c)t+B(c), the conductor in C[c,t] is…](../units/JCG-0759F9E6.md)

`JCG-0759F9E6` · `assertion`

For the normalized cubic discriminant, with H=3A(c)t+B(c), the conductor in C[c,t] is H^2 and the conductor ideal in the discriminant ring is generated by B^2-3Ab and 18Aa+Bb; transversely the singularity is the ordinary cusp C[H^2,H^3] inside C[H].

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-033`
  - Does not establish: The locator alone is not an independent proof review.

### [For the normalized cubic pole-cancellation family determined by polynomials A(C),B(C), all su…](../units/JCG-DF9F7A0E.md)

`JCG-DF9F7A0E` · `assertion`

For the normalized cubic pole-cancellation family determined by polynomials A(C),B(C), all such maps arise from the stated cancellation equations; when gcd(A,B)=1 the finite-flat geometry, discriminant, nonproperness set, and omission locus admit a complete description.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:pole-cancellation`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:AB-global`
  - Does not establish: The locator alone is not an independent proof review.

### [For the normalized cubic-frame maps, a divisor over a zero of A…](../units/JCG-A514F028.md)

`JCG-A514F028` · `assertion`

For the normalized cubic-frame maps, a divisor over a zero of A has one of four generic behaviors: one unramified sheet is deleted (U1), two unramified sheets are deleted (U2), a ramified pair is deleted (B), or the deleted sheets have generic three-cycle inertia. The last behavior is excluded in the polynomial Keller subfamily under study.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/common-zero-normalization.tex#prop:four-generic-divisor-behaviors`
  - Does not establish: The locator alone is not an independent proof review.

### [For the quadratic resolvent Q of a complex cubic Keller normalization, an…](../units/JCG-79BDB7F6.md)

`JCG-79BDB7F6` · `assertion`

For the quadratic resolvent Q of a complex cubic Keller normalization, an isolated singularity cannot support a nonflat cubic defect; moreover, three-torsion in Cl(Q) is detected at the height-two singular primes.

Support:

- **source assertion:** theorem and proof — `manuscripts/01-cubic-incidence/appendices/cubic-resolvent-defects.tex#thm:isolated-resolvent-exclusion`
  - Does not establish: The locator alone is not an independent proof review.

### [Formal extension of the ruling can hold while Zariski-local algebraization of every…](../units/JCG-AB9F57D0.md)

`JCG-AB9F57D0` · `assertion`

Formal extension of the ruling can hold while Zariski-local algebraization of every lift fails; explicit rational threefold and same-incidence nonalgebraizable lifts refute the proposed general algebraization lemma.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-021`
  - Does not establish: The locator alone is not an independent proof review.

### [If a generic-degree-three Keller map had smooth irreducible nonproperness hypersurface, then…](../units/JCG-BF1A2DBF.md)

`JCG-BF1A2DBF` · `assertion`

If a generic-degree-three Keller map had smooth irreducible nonproperness hypersurface, then it would be surjective, the hypersurface would be isomorphic to A2, and its discriminant double cover would admit a connected etale C3-cover.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-024`
  - Does not establish: The locator alone is not an independent proof review.

### [If a moving-linear full simple-root incidence X_{lambda,f} is isomorphic to A3, then…](../units/JCG-9FF259CA.md)

`JCG-9FF259CA` · `assertion`

If a moving-linear full simple-root incidence X_{lambda,f} is isomorphic to A3, then f is a nonzero constant, lambda(t) is everywhere tangent but nonosculating, and a polynomial SL2[t] gauge reduces it to the fixed tangent hyperplane; the induced map is left-right equivalent to the base counterexample.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#thm:moving-tangent`
  - Does not establish: The locator alone is not an independent proof review.

### [If the cubic normalization is flat, it is the pullback of the…](../units/JCG-2E563312.md)

`JCG-2E563312` · `assertion`

If the cubic normalization is flat, it is the pullback of the universal marked-root master cover; equality with affine three-space additionally requires completeness of the boundary deletion.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#prop:conditional-master`
  - Does not establish: The locator alone is not an independent proof review.

### [In the binary-form multiplication model of the counterexample, the resultant-one double-root…](../units/JCG-C5D74708.md)

`JCG-C5D74708` · `assertion`

In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-003`
  - Does not establish: The locator alone is not an independent proof review.

### [In the stated marked-incidence deformation problem with smooth leading plane cubic, every…](../units/JCG-717B157D.md)

`JCG-717B157D` · `assertion`

In the stated marked-incidence deformation problem with smooth leading plane cubic, every positive first-normal jet lies in the gauge image; the Hesse and Fermat model calculations give the exact determinant and rank certificates used by the global bundle argument.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#thm:smooth-cubic-normal-rigidity`
  - Does not establish: The locator alone is not an independent proof review.

### [Inside the normalized family, degree-jumping first-order deformations of the base cubic have…](../units/JCG-69445E34.md)

`JCG-69445E34` · `assertion`

Inside the normalized family, degree-jumping first-order deformations of the base cubic have tangent quotient C[c]/(C plus Cc); imposing degree at most N gives dimension N-1.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-015`
  - Does not establish: The locator alone is not an independent proof review.

### [Keller hypotheses force the cubic normalization defect to vanish.](../units/JCG-138BEDA2.md)

`JCG-138BEDA2` · `assertion`

Keller hypotheses force the cubic normalization defect to vanish.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#q:flatness`
  - Does not establish: The locator alone is not an independent proof review.

### [Let H be the largest monic polynomial such that H^2 divides A…](../units/JCG-12CFF8C9.md)

`JCG-12CFF8C9` · `assertion`

Let H be the largest monic polynomial such that H^2 divides A and H divides B. For the normalized cubic-frame extension, the integral closure is R plus R times (At/H) plus R times (At^2+Bt), it is finite flat of degree three, and its discriminant is the primitive discriminant divided by H^2.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/common-zero-normalization.tex#thm:common-zero-normalization`
  - Does not establish: The locator alone is not an independent proof review.

### [Let L/K(lambda) be the cubic radial extension at the exceptional marked-root end,…](../units/JCG-4D6F79C6.md)

`JCG-4D6F79C6` · `assertion`

Let L/K(lambda) be the cubic radial extension at the exceptional marked-root end, unramified over lambda=0 with residue degree three and residue field K*. If the geometric radial cover has different degree less than four, or if all geometric inertia groups fix a common sheet, then it is geometrically disconnected and L=K*(lambda); equivalently, the direction map has a rational marked-root lift.

### [Let a complete normal Cohen-Macaulay threefold resolvent germ admit a proper birational…](../units/JCG-69028659.md)

`JCG-69028659` · `assertion`

Let a complete normal Cohen-Macaulay threefold resolvent germ admit a proper birational regular model with one exceptional prime Cartier divisor over a smooth curve and a regular transverse surface slice. If the scheme-theoretic exceptional fiber is a plane cubic C with O_C(-E)=O_C(1), then every rank-one reflexive sheaf L with L^[3]=O is maximal Cohen-Macaulay; under the cubic-resolvent reduction, the associated cubic normalization is flat.

Support:

- **source assertion:** theorem and proof — `manuscripts/01-cubic-incidence/appendices/cubic-resolvent-defects.tex#thm:smooth-cubic-axis-exclusion`
  - Does not establish: The locator alone is not an independent proof review.

### [Modulo triangular target shears, all polynomial root-slope frame potentials admit the stated…](../units/JCG-30497402.md)

`JCG-30497402` · `assertion`

Modulo triangular target shears, all polynomial root-slope frame potentials admit the stated unique torus-weight normal form, with necessary and sufficient layer conditions at weights m<0, m=0, m=1, and m>=2.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-029`
  - Does not establish: The locator alone is not an independent proof review.

### [Natural next problems include classification of generic-degree-three examples, bounded-degree…](../units/JCG-44729E0B.md)

`JCG-44729E0B` · `assertion`

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-038`
  - Does not establish: The locator alone is not an independent proof review.

### [No algebraically homogeneous minimal defect can occur in a Keller normalization.](../units/JCG-62422786.md)

`JCG-62422786` · `assertion`

No algebraically homogeneous minimal defect can occur in a Keller normalization.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-011`
  - Does not establish: The locator alone is not an independent proof review.

### [Normal cubic covers with S3 monodromy need not be flat: an explicit…](../units/JCG-583DA94A.md)

`JCG-583DA94A` · `assertion`

Normal cubic covers with S3 monodromy need not be flat: an explicit minimal nonflat normal cubic algebra supplies a countermodel outside the Keller setting.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-041`
  - Does not establish: The locator alone is not an independent proof review.

### [On a sheet marked by a simple root t_i of a cubic,…](../units/JCG-ADA71038.md)

`JCG-ADA71038` · `assertion`

On a sheet marked by a simple root t_i of a cubic, x_i=2/P'(t_i)=2/[A(c)(t_i-t_j)(t_i-t_k)]; collision of the marked root therefore sends that affine source branch to infinity while the finite completion retains the ramification.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-026`
  - Does not establish: The locator alone is not an independent proof review.

### [Over A(c) nonzero, the normalized cubic discriminant complement is the product of…](../units/JCG-8EF344E1.md)

`JCG-8EF344E1` · `assertion`

Over A(c) nonzero, the normalized cubic discriminant complement is the product of the punctured c-line and the centered three-point configuration space; if A has s distinct roots, its fundamental group is F_s times B_3 and the permutation monodromy is the standard B_3-to-S3 quotient.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-028`
  - Does not establish: The locator alone is not an independent proof review.

### [Recover the six decisive obstruction components canonically from the residue pole filtration…](../units/JCG-5EA4BAEE.md)

`JCG-5EA4BAEE` · `assertion`

Recover the six decisive obstruction components canonically from the residue pole filtration or the determinant of cohomology.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-045`
  - Does not establish: The locator alone is not an independent proof review.

### [The choice A=C(C+1), B=-2-4C produces an exact cubic Keller family with an…](../units/JCG-0A4D8C5B.md)

`JCG-0A4D8C5B` · `assertion`

The choice A=C(C+1), B=-2-4C produces an exact cubic Keller family with an unramified lost sheet, showing that omission need not coincide with ramification.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-013`
  - Does not establish: The locator alone is not an independent proof review.

### [The defect problem admits a resolvent maximal-Cohen–Macaulay reformulation.](../units/JCG-AB57A9B2.md)

`JCG-AB57A9B2` · `assertion`

The defect problem admits a resolvent maximal-Cohen–Macaulay reformulation.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-009`
  - Does not establish: The locator alone is not an independent proof review.

### [The first analyzed genuine rank-two Cartan endpoint, represented by A0^2+rho A3^2 with…](../units/JCG-61450EFE.md)

`JCG-61450EFE` · `assertion`

The first analyzed genuine rank-two Cartan endpoint, represented by A0^2+rho A3^2 with rho nonzero, cannot yield both an affine-three-space target and an affine-three-space full incidence.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#prop:rank-two-cartan-endpoint`
  - Does not establish: The locator alone is not an independent proof review.

### [The first transverse deformation A2+kappa gamma A0=c has compactly supported Euler characteri…](../units/JCG-98E23B8A.md)

`JCG-98E23B8A` · `assertion`

The first transverse deformation A2+kappa gamma A0=c has compactly supported Euler characteristic -5 and therefore does not have affine-three-space source; general A0 deformations reduce to a branch-surface Euler condition.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#thm:first-transverse`
  - Does not establish: The locator alone is not an independent proof review.
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#app:moving-hyperplanes`
  - Does not establish: The locator alone is not an independent proof review.

### [The function-field extension induced by the Alpöge map has degree 3 and…](../units/JCG-1B137277.md)

`JCG-1B137277` · `assertion`

The function-field extension induced by the Alpöge map has degree 3 and an S3 Galois closure, as described by the cited explicit cubic model.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-002`
  - Does not establish: The locator alone is not an independent proof review.

### [The highest-leverage program is exact reconstruction of the five Belyi maps followed…](../units/JCG-48D5E369.md)

`JCG-48D5E369` · `assertion`

The highest-leverage program is exact reconstruction of the five Belyi maps followed by weight-filtered tests against the two surviving Newton supports, with independent certificate infrastructure in parallel.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-048`
  - Does not establish: The locator alone is not an independent proof review.

### [The map is prime under polynomial composition.](../units/JCG-45B208F0.md)

`JCG-45B208F0` · `assertion`

The map is prime under polynomial composition.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-017`
  - Does not establish: The locator alone is not an independent proof review.

### [The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and…](../units/JCG-30AF091E.md)

`JCG-30AF091E` · `assertion`

The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and minimal support remain open.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-047`
  - Does not establish: The locator alone is not an independent proof review.

### [The off-diagonal collision space is a smooth factorial affine threefold with trivial…](../units/JCG-E1F739D1.md)

`JCG-E1F739D1` · `assertion`

The off-diagonal collision space is a smooth factorial affine threefold with trivial Picard group and unit group modulo constants \(\mathbb Z\).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-018`
  - Does not establish: The locator alone is not an independent proof review.

### [The pure Cartan projection C33 defines a nondegenerate affine quadric rather than…](../units/JCG-8C8ADE4E.md)

`JCG-8C8ADE4E` · `assertion`

The pure Cartan projection C33 defines a nondegenerate affine quadric rather than A3; more generally, a nonzero catalecticant determinant excludes the quadratic target hypersurface from being A3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#prop:catalecticant-target`
  - Does not establish: The locator alone is not an independent proof review.

### [The reduced nonproperness set is singular for every admissible map in the…](../units/JCG-BE85CECB.md)

`JCG-BE85CECB` · `assertion`

The reduced nonproperness set is singular for every admissible map in the determinant-neutral A(C),B(C) cubic family.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/omitted-values.tex#app:omitted-values`
  - Does not establish: The locator alone is not an independent proof review.

### [The remaining minimal defect can be organized by a radial fibration and…](../units/JCG-D0FCE306.md)

`JCG-D0FCE306` · `assertion`

The remaining minimal defect can be organized by a radial fibration and an E6-type boundary/discrepancy picture.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-042`
  - Does not establish: The locator alone is not an independent proof review.

### [The resultant-one factor space is isomorphic to SL2 times A1_gamma, and its…](../units/JCG-ECD1CA4E.md)

`JCG-ECD1CA4E` · `assertion`

The resultant-one factor space is isomorphic to SL2 times A1_gamma, and its universal marked-root map to the simple-root binary-cubic locus is etale; ordering the roots gives an S3 torsor.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-022`
  - Does not establish: The locator alone is not an independent proof review.

### [Top priorities are independent certificate reproduction, the full bounded-degree local ring a…](../units/JCG-AF04161C.md)

`JCG-AF04161C` · `assertion`

Top priorities are independent certificate reproduction, the full bounded-degree local ring and degree-growth interface, intrinsic triple-cover defect exclusion, boundary-complete rigidity, the minimum degree-three coordinate bound, improved descendant dimensions/tensor rank, the five-dimensional classification, and explaining the two-dimensional obstruction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-044`
  - Does not establish: The locator alone is not an independent proof review.

### [What is the full polynomial left-right quotient in the nonsquarefree common-root case?](../units/JCG-3ACE11E1.md)

`JCG-3ACE11E1` · `assertion`

What is the full polynomial left-right quotient in the nonsquarefree common-root case?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-040`
  - Does not establish: The locator alone is not an independent proof review.

### [Within the A,B family, the nonproperness set can have arbitrarily many components,…](../units/JCG-F5E7F90C.md)

`JCG-F5E7F90C` · `assertion`

Within the A,B family, the nonproperness set can have arbitrarily many components, with discriminant and unramified-loss components controlled by the roots of explicit coefficient polynomials.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-014`
  - Does not establish: The locator alone is not an independent proof review.

### [Within the binary two-block multiplication-incidence construction U_{a,b,H}, stable affinenes…](../units/JCG-517DA8F4.md)

`JCG-517DA8F4` · `assertion`

Within the binary two-block multiplication-incidence construction U_{a,b,H}, stable affineness, and hence affineness, occurs only for the unordered pair {a,b}={1,2}.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:stable-uniqueness`
  - Does not establish: The locator alone is not an independent proof review.

### [Fiber table](../units/RMU-22A9C59B.md)

`RMU-22A9C59B` · `corollary`

The affine fiber size is three off \(S_F\), one on
\(V(\mathcal D)\setminus(T_3\cup\bigcup C_\beta)\), two on a deleted
plane away from \(V(\mathcal D)\), and zero on \(T_3\) and on every
\(C_\beta\).

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#cor:fiber-table`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [If \(S_F\) is smooth, then \(F\) is surjective.](../units/RMU-62D95304.md)

`RMU-62D95304` · `corollary`

If \(S_F\) is smooth, then \(F\) is surjective.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [The equivalence classes are the \(\operatorname{Aff}_1(\C)\)-orbits of triples \[ (D,\alpha,\…](../units/RMU-C7AF2046.md)

`RMU-C7AF2046` · `corollary`

The equivalence classes are the
\(\operatorname{Aff}_1(\C)\)-orbits of triples
\[
(D,\alpha,\overline B),
\]
where \(D=\operatorname{div}(A)\) is an effective divisor on \(\A^1\),
\(\alpha\) is a marked multiplicity-one point of \(D\), and
\[
\overline B\in\C[c]/(A),\qquad \overline B(\alpha)=-2.
\]
For degree \(d\) in a multiplicity stratum with \(r\ge2\) distinct roots,
the generic dimension is \(d+r-3\); in the squarefree stratum it is
\(2d-3\).

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#cor:moduli-data`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [As a reduced set, \begin{equation} S_F=V(\Delta_{\mathrm{prim}}) \cup\bigcup_{\substack{\beta…](../units/RMU-0E32B3A8.md)

`RMU-0E32B3A8` · `lemma`

As a reduced set,
\begin{equation}

S_F=V(\Delta_{\mathrm{prim}})
\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}V(c-\beta).
\end{equation}
The first component is the unique nonplane irreducible component.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Explicit gluing at the marked infinity section](../units/RMU-296A4FAF.md)

`RMU-296A4FAF` · `lemma`

For an admissible coprime triple, the morphism
\[
\jmath\colon\A^3_{x,y,z}\longrightarrow\widetilde X,
\qquad
(x,y,z)\longmapsto
\bigl(F(x,y,z),[x:1+xy]\bigr)
\]
is an isomorphism onto
\[
\widetilde X\setminus
\left(R\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}E_\beta\right).
\]
In particular, this proves the gluing assertion in
\cref{thm:AB-global}(ii), including a neighborhood of \(x=0\).

Dependencies:

- `uses` `RMU-F908DA7B`: Formal statement references thm:AB-global.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [The polynomial \(\Delta_{\mathrm{prim}}\) is irreducible in \(\C[a,b,c]\).](../units/RMU-9003C2D9.md)

`RMU-9003C2D9` · `lemma`

The polynomial \(\Delta_{\mathrm{prim}}\) is irreducible in
\(\C[a,b,c]\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Classifying map and Cartesian pullback](../units/RMU-BEAA51A5.md)

`RMU-BEAA51A5` · `proposition`

Let \(F\colon\A^3\to\A^3\) be a generic-degree-three Keller map, and let
\(\pi\colon\overline X\to Y=\A^3\) be the normalization of the target in its
function field.  Assume that \(\pi\) is finite flat of degree three.  Then,
after choosing a frame of the trace-zero bundle, there is a morphism
\[
\gamma\colon Y\longrightarrow V
\]
such that, for \(Y^\circ=\gamma^{-1}(V^{\mathrm{sm}})\), the square
\[
\begin{array}{ccc}
\overline X^\circ&\longrightarrow&\mathcal M^{\mathrm{sm}}\\
\big\downarrow&&\big\downarrow m\\
Y^\circ&\xrightarrow{\ \gamma\ }&V^{\mathrm{sm}}
\end{array}
\]
is Cartesian.  In particular, \(\overline X^\circ\to Y^\circ\) is the
pullback of the universal resultant-one marked-root cover over the full
simple-root locus.  This proves the finite-cover assertion of
\cref{prop:conditional-master}; identifying the original affine source still
requires separate boundary data.

Dependencies:

- `uses` `RMU-DD6B3EDC`: Formal statement references prop:conditional-master.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Conditional master-cover statement](../units/RMU-DD6B3EDC.md)

`RMU-DD6B3EDC` · `proposition`

Let \(F\colon\A^3\to\A^3\) be a generic-degree-three Keller map, and let
\(\overline X\to\A^3\) be the normalization of the target in its function
field.  If \(\overline X\to\A^3\) is finite flat of degree three, then over
the simple-root locus it is a pullback of the universal
resultant-one marked-root cover.  Recovering the original affine source from
\(\overline X\) additionally requires a theorem identifying the entire
deleted boundary.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Corrected divisorial classification](../units/RMU-C1DD871B.md)

`RMU-C1DD871B` · `proposition`

At the geometric generic point of every prime divisor \(H\subset Y\), exactly
one of the following types occurs:
\begin{enumerate}[label=\(U_\arabic*\),start=0]
\item all three sheets are unramified and retained;
\item all three sheets are unramified and exactly one is deleted;
\item all three sheets are unramified and exactly two are deleted;
\end{enumerate}
or
\begin{description}
\item[\(B\)] the inertia is a transposition, the ramified point is deleted,
and the unramified point is retained.
\end{description}
Outside \(S_F\) only \(U_0\) occurs, while at the generic point of a divisor
contained in \(S_F\) only \(U_1,U_2,B\) occur.  In particular, a deleted
three-cycle cannot occur.  The Galois closure of the generic cubic extension
has group \(S_3\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Every admissible triple defines a Keller map with \[ \det D F_{A,B,\alpha}=-2.…](../units/RMU-5852A2F8.md)

`RMU-5852A2F8` · `proposition`

Every admissible triple defines a Keller map with
\[
\det D F_{A,B,\alpha}=-2.
\]
Its generic degree is three.  The source plane \(x=0\) maps isomorphically
onto the target plane \(c=\alpha\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Exact comparison criterion](../units/RMU-A4B084FF.md)

`RMU-A4B084FF` · `proposition`

In the quadratic-resolvent setup above, suppose there exists a rank-one
reflexive \(Q\)-module \(M\) such that
\begin{enumerate}[label=(\roman*)]
\item \(M^{[3]}\simeq Q\);
\item \(M\) is maximal Cohen--Macaulay; and
\item for every height-two singular prime \(\mathfrak p\), the classes of
\(M_{\mathfrak p}\) and \(L_{\mathfrak p}\) agree in
\(\Cl(Q_{\mathfrak p})\).
\end{enumerate}
Then \(L\simeq M\), and the cubic normalization \(B\) is finite flat over
\(A\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Marked Vandermonde factorization](../units/RMU-03794DFA.md)

`RMU-03794DFA` · `proposition`

If \(P(T)=(T-t)Q(T)\), then
\[
\Disc(P)=P'(t)^2\Disc(Q).
\]
For
\[
P(T)=A(c)T^3+B(c)T^2+bT-2a,\qquad r=P'(t),
\]
this becomes
\[
\Disc(P)
=r^2\bigl((3A(c)t+B(c))^2-4A(c)r\bigr).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Resolvent MCM criterion](../units/RMU-5D20CFBF.md)

`RMU-5D20CFBF` · `proposition`

If \(L\) is maximal Cohen--Macaulay over \(Q\), then the cubic normalization
\(B\) is finite flat over \(A\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [The cubic incidence open is affine three-space](../units/RMU-FA7978C0.md)

`RMU-FA7978C0` · `proposition`

For every tangent but nonosculating hyperplane \(H\) in the case
\(\{a,b\}=\{1,2\}\), one has
\[
U_{a,b,H}\simeq\A^3.
\]
This supplies the positive direction of \cref{thm:stable-uniqueness} without
an appeal to an unspecified public construction.

Dependencies:

- `uses` `RMU-BA2C2F76`: Formal statement references thm:stable-uniqueness.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Universal root--slope transform](../units/RMU-AEC15A12.md)

`RMU-AEC15A12` · `proposition`

Let \(H(T,c)\in k[T,c]\), where \(2\in k^*\), and define
\[
b=r-H_T(t,c),\qquad
2a=H(t,c)+tb.
\]
Then, for
\[
P_{a,b,c}(T)=H(T,c)+bT-2a,
\]
one has
\[
P_{a,b,c}(t)=0,\qquad P'_{a,b,c}(t)=r,
\]
and
\[
2\,da-t\,db-H_c(t,c)\,dc=r\,dt.
\]
Consequently
\[
\det\frac{\partial(a,b,c)}{\partial(t,r,c)}=\frac r2.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [All-multiplicity equivalence criterion](../units/RMU-101BA49F.md)

`RMU-101BA49F` · `theorem`

Let \((A_i,B_i,\alpha_i)\) be admissible triples.  Then
\(F_{A_1,B_1,\alpha_1}\) and \(F_{A_2,B_2,\alpha_2}\) are polynomially
left--right equivalent if and only if there are an affine map
\(\phi(c)=uc+v\), \(u\ne0\), and a scalar \(\kappa\in\C^*\) such that
\begin{align}
A_2(\phi(c))&=\kappa A_1(c),\\
B_2(\phi(c))&\equiv B_1(c)\pmod{A_1(c)},\\
\phi(\alpha_1)&=\alpha_2.
\end{align}
No squarefreeness hypothesis is required.

When \(A_1\) has at least two distinct roots, every equivalence induces the
root-affine data above.  When \(A_1\) is linear, all members lie in one
equivalence class; we do not assert that the construction below describes
the full self-equivalence group of that class.

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#thm:equivalence`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Dao's torsion exclusion and codimension-two detection](../units/RMU-13177F24.md)

`RMU-13177F24` · `theorem`

Let \((Q,\mathfrak n)\) be a three-dimensional normal local hypersurface over
\(\C\), and put \(U=\Spec Q\setminus\{\mathfrak n\}\).
\begin{enumerate}[label=(\roman*)]
\item If \(Q\) has an isolated singularity, then \(\Cl(Q)[3]=0\).
\item In general, restriction induces an injection
\[
\Cl(Q)[3]\hookrightarrow
\bigoplus_{\substack{\mathfrak p\in\Sing(Q)\\\operatorname{ht}\mathfrak p=2}}
\Cl(Q_{\mathfrak p})[3].
\]
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Generic \(S_3\) monodromy](../units/RMU-A8650DD4.md)

`RMU-A8650DD4` · `theorem`

Assume characteristic zero and generic degree three.  The normal closure of
the normalized cubic extension has Galois group \(S_3\).  Over \(\C\), the
geometric monodromy of the three-sheeted \'{e}tale locus is therefore
\(S_3\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Global geometry of the coprime family](../units/RMU-F908DA7B.md)

`RMU-F908DA7B` · `theorem`

For an admissible triple satisfying \eqref{eq:coprime}:

\begin{enumerate}[label=(\roman*)]
\item the total space \(\widetilde X\) is smooth, and the projection
\(\pi\colon\widetilde X\to\A^3_{a,b,c}\) is finite flat of degree three;
\item there is an isomorphism
\begin{equation}

\A^3_{x,y,z}\simeq
\widetilde X\setminus
\left(R\cup\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}E_\beta\right);
\end{equation}
\item the branch discriminant is
\begin{equation}

\mathcal D=
B(c)^2b^2-4A(c)b^3+8aB(c)^3
-36aA(c)B(c)b-108a^2A(c)^2;
\end{equation}
\item the nonproperness set is
\begin{equation}

S_F=V(\mathcal D)\cup
\bigcup_{\substack{\beta\in Z(A)\\\beta\ne\alpha}}V(c-\beta);
\end{equation}
\item if
\[
T_3=
V\left(3A(c)b-B(c)^2,\,
54A(c)^2a+B(c)^3\right)
\]
and
\[
C_\beta=
V\left(c-\beta,\ b^2+8aB(\beta)\right),
\]
then
\begin{equation}

\A^3\setminus F(\A^3)=
T_3\cup\bigcup_{\beta\ne\alpha}C_\beta
=\Sing(S_F)_{\mathrm{red}}.
\end{equation}
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Omitted values are singular](../units/RMU-C5C8680E.md)

`RMU-C5C8680E` · `theorem`

For every complex polynomial Keller map,
\[
O_F\subseteq\Sing(S_F).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Pole-cancellation theorem](../units/RMU-1D5197B2.md)

`RMU-1D5197B2` · `theorem`

Let \(A\ne0\).  The rational expressions in \eqref{eq:ab-map} are
polynomials if and only if there is \(\alpha\in\C\) such that
\begin{equation}

A(\alpha)=0,\qquad A'(\alpha)\ne0,\qquad B(\alpha)=-2,
\end{equation}
and, modulo \(x^3\C[x,y]\),
\begin{equation}

w(x,y)\equiv
\alpha+\frac{2}{A'(\alpha)}x
+x^2\left(
-\frac{3}{A'(\alpha)}y
-\frac{2A''(\alpha)}{A'(\alpha)^3}
-\frac{B'(\alpha)}{A'(\alpha)^2}
\right).
\end{equation}
The \(x^3\)-remainder is removed by a source shear.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Stable uniqueness](../units/RMU-BA2C2F76.md)

`RMU-BA2C2F76` · `theorem`

Let \(a,b\ge1\) and \(a+b\ge3\).  For every hyperplane \(H\) tangent but
not osculating at the chosen point,
\[
U_{a,b,H}\simeq\A^{a+b}
\quad\Longleftrightarrow\quad
\{a,b\}=\{1,2\}.
\]
More strongly, outside the cubic case,
\[
U_{a,b,H}\times\A^r
\not\simeq\A^{a+b+r}
\qquad\text{for every }r\ge0.
\]

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#thm:stable-uniqueness`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

## Open frontier

### [Boundary Torelli](../units/RMU-F94F448E.md)

`RMU-F94F448E` · `question`

To what extent is a marked-root cover determined, up to polynomial
left--right equivalence, by its deleted boundary together with the induced
normalization, conductor, and incidence data?  In particular, which
hypotheses make the boundary-completeness problem in
\cref{prop:conditional-master} a reconstruction theorem?

Dependencies:

- `uses` `RMU-DD6B3EDC`: Formal statement references prop:conditional-master.

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#q:boundary-torelli`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [Construct a different-filtered source-flow or transferred L-infinity model that independently…](../units/JCG-D9E57688.md)

`JCG-D9E57688` · `question`

Construct a different-filtered source-flow or transferred L-infinity model that independently reproduces the bounded-degree Kuranishi equations and the length-584 Artin algebra.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`
  - Does not establish: The locator alone is not an independent proof review.

### [Cubic flatness](../units/RMU-34FBCB8D.md)

`RMU-34FBCB8D` · `question`

Does the Keller condition force the finite cubic normalization
\(\overline X\to\A^3\) to be flat?

Support:

- **source assertion:** The manuscript records this exact formal statement. — `manuscripts/01-cubic-incidence/main.tex#q:flatness`
  - Does not establish: Presence in the manuscript is not an independent proof audit.

### [For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree…](../units/JCG-4451EE05.md)

`JCG-4451EE05` · `question`

For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree delta_LR(xi)=min{deg H : H is polynomially left-right equivalent to xi} from intrinsic conductor, ramification, valuation, or nonproperness data. A bound of at least seven for every nontrivial generic-degree-three boundary class would supply the missing degree-cost bridge from cubic-cover classification to low-degree exclusion.

### [Show that at least one nonzero class in the local F_3^2 sign-torsor…](../units/JCG-1C1790E5.md)

`JCG-1C1790E5` · `question`

Show that at least one nonzero class in the local F_3^2 sign-torsor space globalizes across the boundary; this would contradict the absence of nontrivial finite etale covers of affine three-space.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#q:end-to-global-sign-torsor`
  - Does not establish: The locator alone is not an independent proof review.
