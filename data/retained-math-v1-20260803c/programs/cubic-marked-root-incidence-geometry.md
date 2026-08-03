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

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#def:admissible`](../../proof-sources/01-cubic-incidence/main.md#label-def-admissible)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#def:admissible`](../../proof-sources/01-cubic-incidence/main.md#label-def-admissible)

### [Elliptic-cone model realizes a non-MCM cubic resolvent carrier](../units/RMU-1B8F0002.md)

`RMU-1B8F0002` · `example`

The Fermat-cubic ordered-root construction gives a normal S3 cubic cone whose trace-zero module has a finite defect, whose quadratic resolvent has nine transverse A2 carrier curves, and whose cubic eigensheaf is not maximal Cohen-Macaulay. The standard collision axes alone have zero punctual saturation, while their global elliptic gluing contributes a length-two standard-representation quotient.

Hypotheses:

- The construction and grading are exactly those in elliptic-cone-negative-model.md.

Support:

- **proof:** Construction, depth calculation, transverse class computation, and global Cech quotient. — `research-notes/lane1-models-20260803-v1/elliptic-cone-negative-model.md`
  - Does not establish: Existence of a Keller realization.

Limitations:

- The model is not a polynomial Keller map and does not realize an omitted Keller value.

## Retained results

### [A generically degree-three Keller map admits a useful normalization picture: a finite…](../units/JCG-26FD089B.md)

`JCG-26FD089B` · `assertion`

A generically degree-three Keller map admits a useful normalization picture: a finite normalization X over the target together with an open embedding of A3, expressible through a finite-flat binary-cubic model.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-012`

### [A rank-three affine-linear family whose full simple-root incidence is affine three-space lies…](../units/JCG-DBB38171.md)

`JCG-DBB38171` · `assertion`

A rank-three affine-linear family whose full simple-root incidence is affine three-space lies in the tangent-but-not-osculating orbit and recovers the base map up to left-right equivalence.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-005`

### [A reduced frame potential of root degree n>=4 has leading coefficient vanishing…](../units/JCG-7C0CF125.md)

`JCG-7C0CF125` · `assertion`

A reduced frame potential of root degree n>=4 has leading coefficient vanishing to order at least floor(n/2)+1 at the retained infinity point; the bound is sharp and yields component degrees (3n+4,3n+3,4) for even n and (3n+2,3n+1,4) for odd n.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-030`

### [A=c(c-1)^2, B=2(c-1) gives an exact U2 Keller example whose omission locus is…](../units/JCG-FF7A1933.md)

`JCG-FF7A1933` · `assertion`

A=c(c-1)^2, B=2(c-1) gives an exact U2 Keller example whose omission locus is strictly smaller than the singular locus of the nonproperness set.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/common-zero-normalization.tex#prop:u2-example`

### [Algebraize the formal/radial ruling strongly enough to exclude the remaining nonhomogeneous m…](../units/JCG-5716FF00.md)

`JCG-5716FF00` · `assertion`

Algebraize the formal/radial ruling strongly enough to exclude the remaining nonhomogeneous minimal defect.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-037`

### [An affine-root incidence component of degree at least two cannot be A2,…](../units/JCG-06EFD647.md)

`JCG-06EFD647` · `assertion`

An affine-root incidence component of degree at least two cannot be A2, and a generically squarefree affine-linear projective coefficient family has no connected full simple-root incidence isomorphic to A2.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-016`

### [Assume a zero-dimensional log-canonical resolvent center admits the stated equivariant plt ex…](../units/JCG-FD961DD5.md)

`JCG-FD961DD5` · `assertion`

Assume a zero-dimensional log-canonical resolvent center admits the stated equivariant plt extraction with canonical cyclic cover. Nonneutral conormal residues are maximal Cohen-Macaulay by positivity; if a neutral three-torsion eigensheaf has nonzero H1, S3 symmetry forces its cyclic cover to be an abelian surface. In the multiplicity-six double-plane model the branch tangent sextic is then the nine-cuspidal dual of a smooth plane cubic.

### [At the first possible defect stratum the discriminant has multiplicity at least…](../units/JCG-F9F6311C.md)

`JCG-F9F6311C` · `assertion`

At the first possible defect stratum the discriminant has multiplicity at least six and the exceptional boundary has an elliptic-type constraint.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-010`

### [Can the common-root integral-closure theorem and left-right equivalence result be independent…](../units/JCG-E9F3362D.md)

`JCG-E9F3362D` · `assertion`

Can the common-root integral-closure theorem and left-right equivalence result be independently proved or formalized?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-039`

### [Escape rates are \(\varepsilon^{-1/2}\) near a smooth discriminant point and \(\varepsilon^{-…](../units/JCG-914949BF.md)

`JCG-914949BF` · `assertion`

Escape rates are \(\varepsilon^{-1/2}\) near a smooth discriminant point and \(\varepsilon^{-2/3}\) near the cusp, with more degenerate arcs allowing larger half-integral exponents.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-019`

### [Every Keller map has an infinite-dimensional first-order left-right automorphism space over t…](../units/JCG-931C6D98.md)

`JCG-931C6D98` · `assertion`

Every Keller map has an infinite-dimensional first-order left-right automorphism space over the dual numbers, naturally identified with polynomial vector fields on the target; stabilization also adds inert diagonal affine automorphisms.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-034`

### [Every generic-degree-three Keller map factors through a finite normal cubic cover whose…](../units/JCG-C04524CF.md)

`JCG-C04524CF` · `assertion`

Every generic-degree-three Keller map factors through a finite normal cubic cover whose trace-zero module is rank-two reflexive and locally free away from finitely many target points.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-006`

### [Every nonzero constant combination of the inverse-Jacobian vector fields is incomplete.](../units/JCG-87B4A2F9.md)

`JCG-87B4A2F9` · `assertion`

Every nonzero constant combination of the inverse-Jacobian vector fields is incomplete.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-020`

### [Every nonzero quadratic Hessian contraction with nonzero coefficient is excluded from the…](../units/JCG-A844E87D.md)

`JCG-A844E87D` · `assertion`

Every nonzero quadratic Hessian contraction with nonzero coefficient is excluded from the cubic full-incidence construction: the target hypersurface and full marked-root incidence cannot both be isomorphic to A3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#thm:hessian-exclusion`

### [Every quartic frame has T^4 coefficient divisible by c^3 and first jet…](../units/JCG-9E1E87CA.md)

`JCG-9E1E87CA` · `assertion`

Every quartic frame has T^4 coefficient divisible by c^3 and first jet satisfying delta+4gamma+12kappa=0; the displayed quartic realizes these conditions with determinant -2, generic degree four, and component degrees (16,15,4).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-016`

### [For a constant nonzero level of the universal marked incidence, a moving…](../units/JCG-82D7FF25.md)

`JCG-82D7FF25` · `assertion`

For a constant nonzero level of the universal marked incidence, a moving tangent hyperplane that remains tangent but nonosculating is polynomially gauge-equivalent to the fixed public hyperplane.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#thm:moving-tangent`

### [For all admissible A,B,alpha triples, polynomial left-right equivalence is classified by an…](../units/JCG-221985FF.md)

`JCG-221985FF` · `assertion`

For all admissible A,B,alpha triples, polynomial left-right equivalence is classified by an affine change of c, scalar equality of A, congruence of B modulo A, and preservation of the marked root; no squarefreeness hypothesis is needed.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:equivalence`

### [For an omitted value p of a complex Keller map F from…](../units/JCG-E82019D2.md)

`JCG-E82019D2` · `assertion`

For an omitted value p of a complex Keller map F from A3 to A3, the direction map x maps to [F(x)-p] from A3 to P2 is smooth of relative dimension one and has image equal to P2 minus at most finitely many points.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#prop:omitted-direction-map`

### [For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t…](../units/JCG-0106262F.md)

`JCG-0106262F` · `assertion`

For any polynomial potential H(T,c), the marked-root and slope equations b=r-H_T(t,c), 2a=H(t,c)+tb have Jacobian r/2; composing with t=y+1/x, r=2/x, c=w(x,y)-x^3z has Jacobian -2 whenever the formulas extend polynomially, and generic degree deg_T H.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-025`

### [For every admissible coprime cubic-frame pair, the homogenized inverse cubic defines a…](../units/JCG-EB1B80E7.md)

`JCG-EB1B80E7` · `assertion`

For every admissible coprime cubic-frame pair, the homogenized inverse cubic defines a smooth finite-flat Gorenstein triple cover of affine three-space with trivial rank-two Tschirnhausen bundle and distinguished homogeneous-root frame.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-032`

### [For every complex polynomial Keller map, the omitted-value locus is contained in…](../units/JCG-0A41960D.md)

`JCG-0A41960D` · `assertion`

For every complex polynomial Keller map, the omitted-value locus is contained in the singular locus of the reduced nonproperness set.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/omitted-values.tex#thm:omitted-singular`

### [For every coprime admissible cubic-frame pair, the generic function-field extension has no…](../units/JCG-5B09E55B.md)

`JCG-5B09E55B` · `assertion`

For every coprime admissible cubic-frame pair, the generic function-field extension has no nontrivial deck transformation; ordinary source automorphisms over the identity target are therefore trivial.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-036`

### [For every coprime normalized cubic-frame pair in the stated family, the inverse…](../units/JCG-504733CF.md)

`JCG-504733CF` · `assertion`

For every coprime normalized cubic-frame pair in the stated family, the inverse cubic is irreducible with nonsquare discriminant over C(a,b,c), so its generic Galois closure and geometric monodromy are S3.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-027`

### [For every integer d at least 3, there is a nonproper Keller…](../units/JCG-D739C229.md)

`JCG-D739C229` · `assertion`

For every integer d at least 3, there is a nonproper Keller map from complex affine 3-space to itself with generic degree d.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-001`

### [For every n>=3 the displayed explicit frame potential defines a three-variable polynomial…](../units/JCG-12EBB4BD.md)

`JCG-12EBB4BD` · `assertion`

For every n>=3 the displayed explicit frame potential defines a three-variable polynomial Keller map of generic degree n and determinant -2, attaining the sharp frame-degree bound.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-031`

### [For every product of evaluations at two distinct points, the quadratic target…](../units/JCG-BBB01109.md)

`JCG-BBB01109` · `assertion`

For every product of evaluations at two distinct points, the quadratic target hypersurface A2+kappa E_xi E_eta=c is isomorphic to A3, but its full marked-root preimage is never A3; its compactly supported Euler characteristic is never one.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#thm:two-evaluation-exclusion`

### [For multiplication-incidence opens from P^a x P^b, the next (2,3) candidate fails…](../units/JCG-292A9B9D.md)

`JCG-292A9B9D` · `assertion`

For multiplication-incidence opens from P^a x P^b, the next (2,3) candidate fails to have the affine-space class/count expected of A^5; the original (1,2) case is singled out within the stated incidence-coordinate class.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-004`

### [For positive boundary length, the hidden ordinary complex-point automorphism kernel vanishes…](../units/JCG-1FEDD133.md)

`JCG-1FEDD133` · `assertion`

For positive boundary length, the hidden ordinary complex-point automorphism kernel vanishes and Aut_LR(G_{A,B}) is the finite stabilizer of the decorated boundary scheme (Z_A,B|Z_A).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-035`

### [For rank-one pure-square quadratic covariants in the Cartan-square component, exactly one end…](../units/JCG-1B3C86D8.md)

`JCG-1B3C86D8` · `assertion`

For rank-one pure-square quadratic covariants in the Cartan-square component, exactly one endpoint is gauge-equivalent to the base tangent-hyperplane construction and every other classified orbit fails to give a full incidence isomorphic to A3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#thm:rank-one-cartan`

### [For squarefree A and marked missing-infinity roots, stabilized isomorphism classes of normali…](../units/JCG-5542AF40.md)

`JCG-5542AF40` · `assertion`

For squarefree A and marked missing-infinity roots, stabilized isomorphism classes of normalized conductor arrangements are exactly classified by affine changes of c, affine-linear changes of t over c, the affine root configuration of A, and the projective vector of conductor values B(rho) modulo induced finite permutations.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:conductor-arrangement-classification`

### [For the analyzed minimal smooth defect end, the local sign-three torsor group…](../units/JCG-A9379D6C.md)

`JCG-A9379D6C` · `assertion`

For the analyzed minimal smooth defect end, the local sign-three torsor group is K_loc congruent to C[3] congruent to F_3^2, and its two nonzero directions are represented by algebraic finite covers over the henselian local end.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#thm:local-sign-torsors`

### [For the discriminant surface of A(c)T^3+B(c)T^2+vT-2u with gcd(A,B)=1, the normalization cond…](../units/JCG-AE66472A.md)

`JCG-AE66472A` · `assertion`

For the discriminant surface of A(c)T^3+B(c)T^2+vT-2u with gcd(A,B)=1, the normalization conductor is exactly H^2 C[c,t], where H=3A(c)t+B(c), and its contraction is generated by B^2-3Av and -18Au-Bv.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/conductor-arrangements.tex#thm:cubic-frame-conductor`

### [For the normalized cubic discriminant, with H=3A(c)t+B(c), the conductor in C[c,t] is…](../units/JCG-0759F9E6.md)

`JCG-0759F9E6` · `assertion`

For the normalized cubic discriminant, with H=3A(c)t+B(c), the conductor in C[c,t] is H^2 and the conductor ideal in the discriminant ring is generated by B^2-3Ab and 18Aa+Bb; transversely the singularity is the ordinary cusp C[H^2,H^3] inside C[H].

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-033`

### [For the normalized cubic pole-cancellation family determined by polynomials A(C),B(C), all su…](../units/JCG-DF9F7A0E.md)

`JCG-DF9F7A0E` · `assertion`

For the normalized cubic pole-cancellation family determined by polynomials A(C),B(C), all such maps arise from the stated cancellation equations; when gcd(A,B)=1 the finite-flat geometry, discriminant, nonproperness set, and omission locus admit a complete description.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:pole-cancellation`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:AB-global`

### [For the normalized cubic-frame maps, a divisor over a zero of A…](../units/JCG-A514F028.md)

`JCG-A514F028` · `assertion`

For the normalized cubic-frame maps, a divisor over a zero of A has one of four generic behaviors: one unramified sheet is deleted (U1), two unramified sheets are deleted (U2), a ramified pair is deleted (B), or the deleted sheets have generic three-cycle inertia. The last behavior is excluded in the polynomial Keller subfamily under study.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/common-zero-normalization.tex#prop:four-generic-divisor-behaviors`

### [Formal extension of the ruling can hold while Zariski-local algebraization of every…](../units/JCG-AB9F57D0.md)

`JCG-AB9F57D0` · `assertion`

Formal extension of the ruling can hold while Zariski-local algebraization of every lift fails; explicit rational threefold and same-incidence nonalgebraizable lifts refute the proposed general algebraization lemma.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-021`

### [If a generic-degree-three Keller map had smooth irreducible nonproperness hypersurface, then…](../units/JCG-BF1A2DBF.md)

`JCG-BF1A2DBF` · `assertion`

If a generic-degree-three Keller map had smooth irreducible nonproperness hypersurface, then it would be surjective, the hypersurface would be isomorphic to A2, and its discriminant double cover would admit a connected etale C3-cover.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-024`

### [If a moving-linear full simple-root incidence X_{lambda,f} is isomorphic to A3, then…](../units/JCG-9FF259CA.md)

`JCG-9FF259CA` · `assertion`

If a moving-linear full simple-root incidence X_{lambda,f} is isomorphic to A3, then f is a nonzero constant, lambda(t) is everywhere tangent but nonosculating, and a polynomial SL2[t] gauge reduces it to the fixed tangent hyperplane; the induced map is left-right equivalent to the base counterexample.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#thm:moving-tangent`

### [If the cubic normalization is flat, it is the pullback of the…](../units/JCG-2E563312.md)

`JCG-2E563312` · `assertion`

If the cubic normalization is flat, it is the pullback of the universal marked-root master cover; equality with affine three-space additionally requires completeness of the boundary deletion.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#prop:conditional-master`

### [In the binary-form multiplication model of the counterexample, the resultant-one double-root…](../units/JCG-C5D74708.md)

`JCG-C5D74708` · `assertion`

In the binary-form multiplication model of the counterexample, the resultant-one double-root slice is polynomially isomorphic to affine three-space.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-003`

### [In the stated marked-incidence deformation problem with smooth leading plane cubic, every…](../units/JCG-717B157D.md)

`JCG-717B157D` · `assertion`

In the stated marked-incidence deformation problem with smooth leading plane cubic, every positive first-normal jet lies in the gauge image; the Hesse and Fermat model calculations give the exact determinant and rank certificates used by the global bundle argument.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#thm:smooth-cubic-normal-rigidity`

### [Inside the normalized family, degree-jumping first-order deformations of the base cubic have…](../units/JCG-69445E34.md)

`JCG-69445E34` · `assertion`

Inside the normalized family, degree-jumping first-order deformations of the base cubic have tangent quotient C[c]/(C plus Cc); imposing degree at most N gives dimension N-1.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-results-and-leads.tex#supp-note-04-015`

### [Let H be the largest monic polynomial such that H^2 divides A…](../units/JCG-12CFF8C9.md)

`JCG-12CFF8C9` · `assertion`

Let H be the largest monic polynomial such that H^2 divides A and H divides B. For the normalized cubic-frame extension, the integral closure is R plus R times (At/H) plus R times (At^2+Bt), it is finite flat of degree three, and its discriminant is the primitive discriminant divided by H^2.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/common-zero-normalization.tex#thm:common-zero-normalization`

### [Let L/K(lambda) be the cubic radial extension at the exceptional marked-root end,…](../units/JCG-4D6F79C6.md)

`JCG-4D6F79C6` · `assertion`

Let L/K(lambda) be the cubic radial extension at the exceptional marked-root end, unramified over lambda=0 with residue degree three and residue field K*. If the geometric radial cover has different degree less than four, or if all geometric inertia groups fix a common sheet, then it is geometrically disconnected and L=K*(lambda); equivalently, the direction map has a rational marked-root lift.

### [Modulo triangular target shears, all polynomial root-slope frame potentials admit the stated…](../units/JCG-30497402.md)

`JCG-30497402` · `assertion`

Modulo triangular target shears, all polynomial root-slope frame potentials admit the stated unique torus-weight normal form, with necessary and sufficient layer conditions at weights m<0, m=0, m=1, and m>=2.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-029`

### [Natural next problems include classification of generic-degree-three examples, bounded-degree…](../units/JCG-44729E0B.md)

`JCG-44729E0B` · `assertion`

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-038`

### [No algebraically homogeneous minimal defect can occur in a Keller normalization.](../units/JCG-62422786.md)

`JCG-62422786` · `assertion`

No algebraically homogeneous minimal defect can occur in a Keller normalization.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-011`

### [Normal cubic covers with S3 monodromy need not be flat: an explicit…](../units/JCG-583DA94A.md)

`JCG-583DA94A` · `assertion`

Normal cubic covers with S3 monodromy need not be flat: an explicit minimal nonflat normal cubic algebra supplies a countermodel outside the Keller setting.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-041`

### [On a sheet marked by a simple root t_i of a cubic,…](../units/JCG-ADA71038.md)

`JCG-ADA71038` · `assertion`

On a sheet marked by a simple root t_i of a cubic, x_i=2/P'(t_i)=2/[A(c)(t_i-t_j)(t_i-t_k)]; collision of the marked root therefore sends that affine source branch to infinity while the finite completion retains the ramification.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-026`

### [Over A(c) nonzero, the normalized cubic discriminant complement is the product of…](../units/JCG-8EF344E1.md)

`JCG-8EF344E1` · `assertion`

Over A(c) nonzero, the normalized cubic discriminant complement is the product of the punctured c-line and the centered three-point configuration space; if A has s distinct roots, its fundamental group is F_s times B_3 and the permutation monodromy is the standard B_3-to-S3 quotient.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-028`

### [Recover the six decisive obstruction components canonically from the residue pole filtration…](../units/JCG-5EA4BAEE.md)

`JCG-5EA4BAEE` · `assertion`

Recover the six decisive obstruction components canonically from the residue pole filtration or the determinant of cohomology.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-045`

### [The choice A=C(C+1), B=-2-4C produces an exact cubic Keller family with an…](../units/JCG-0A4D8C5B.md)

`JCG-0A4D8C5B` · `assertion`

The choice A=C(C+1), B=-2-4C produces an exact cubic Keller family with an unramified lost sheet, showing that omission need not coincide with ramification.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-013`

### [The first analyzed genuine rank-two Cartan endpoint, represented by A0^2+rho A3^2 with…](../units/JCG-61450EFE.md)

`JCG-61450EFE` · `assertion`

The first analyzed genuine rank-two Cartan endpoint, represented by A0^2+rho A3^2 with rho nonzero, cannot yield both an affine-three-space target and an affine-three-space full incidence.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#prop:rank-two-cartan-endpoint`

### [The first transverse deformation A2+kappa gamma A0=c has compactly supported Euler characteri…](../units/JCG-98E23B8A.md)

`JCG-98E23B8A` · `assertion`

The first transverse deformation A2+kappa gamma A0=c has compactly supported Euler characteristic -5 and therefore does not have affine-three-space source; general A0 deformations reduce to a branch-surface Euler condition.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#thm:first-transverse`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/moving-hyperplanes.tex#app:moving-hyperplanes`

### [The function-field extension induced by the Alpöge map has degree 3 and…](../units/JCG-1B137277.md)

`JCG-1B137277` · `assertion`

The function-field extension induced by the Alpöge map has degree 3 and an S3 Galois closure, as described by the cited explicit cubic model.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-002`

### [The highest-leverage program is exact reconstruction of the five Belyi maps followed…](../units/JCG-48D5E369.md)

`JCG-48D5E369` · `assertion`

The highest-leverage program is exact reconstruction of the five Belyi maps followed by weight-filtered tests against the two surviving Newton supports, with independent certificate infrastructure in parallel.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-048`

### [The map is prime under polynomial composition.](../units/JCG-45B208F0.md)

`JCG-45B208F0` · `assertion`

The map is prime under polynomial composition.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-017`

### [The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and…](../units/JCG-30AF091E.md)

`JCG-30AF091E` · `assertion`

The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and minimal support remain open.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-047`

### [The off-diagonal collision space is a smooth factorial affine threefold with trivial…](../units/JCG-E1F739D1.md)

`JCG-E1F739D1` · `assertion`

The off-diagonal collision space is a smooth factorial affine threefold with trivial Picard group and unit group modulo constants \(\mathbb Z\).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-018`

### [The pure Cartan projection C33 defines a nondegenerate affine quadric rather than…](../units/JCG-8C8ADE4E.md)

`JCG-8C8ADE4E` · `assertion`

The pure Cartan projection C33 defines a nondegenerate affine quadric rather than A3; more generally, a nonzero catalecticant determinant excludes the quadratic target hypersurface from being A3.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex#prop:catalecticant-target`

### [The reduced nonproperness set is singular for every admissible map in the…](../units/JCG-BE85CECB.md)

`JCG-BE85CECB` · `assertion`

The reduced nonproperness set is singular for every admissible map in the determinant-neutral A(C),B(C) cubic family.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/omitted-values.tex#app:omitted-values`

### [The remaining minimal defect can be organized by a radial fibration and…](../units/JCG-D0FCE306.md)

`JCG-D0FCE306` · `assertion`

The remaining minimal defect can be organized by a radial fibration and an E6-type boundary/discrepancy picture.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-042`

### [The resultant-one factor space is isomorphic to SL2 times A1_gamma, and its…](../units/JCG-ECD1CA4E.md)

`JCG-ECD1CA4E` · `assertion`

The resultant-one factor space is isomorphic to SL2 times A1_gamma, and its universal marked-root map to the simple-root binary-cubic locus is etale; ordering the roots gives an S3 torsor.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-022`

### [Top priorities are independent certificate reproduction, the full bounded-degree local ring a…](../units/JCG-AF04161C.md)

`JCG-AF04161C` · `assertion`

Top priorities are independent certificate reproduction, the full bounded-degree local ring and degree-growth interface, intrinsic triple-cover defect exclusion, boundary-complete rigidity, the minimum degree-three coordinate bound, improved descendant dimensions/tensor rank, the five-dimensional classification, and explaining the two-dimensional obstruction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-044`

### [What is the full polynomial left-right quotient in the nonsquarefree common-root case?](../units/JCG-3ACE11E1.md)

`JCG-3ACE11E1` · `assertion`

What is the full polynomial left-right quotient in the nonsquarefree common-root case?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-040`

### [Within the A,B family, the nonproperness set can have arbitrarily many components,…](../units/JCG-F5E7F90C.md)

`JCG-F5E7F90C` · `assertion`

Within the A,B family, the nonproperness set can have arbitrarily many components, with discriminant and unramified-loss components controlled by the roots of explicit coefficient polynomials.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/additional-results-and-leads.tex#supp-note-01-014`

### [Within the binary two-block multiplication-incidence construction U_{a,b,H}, stable affinenes…](../units/JCG-517DA8F4.md)

`JCG-517DA8F4` · `assertion`

Within the binary two-block multiplication-incidence construction U_{a,b,H}, stable affineness, and hence affineness, occurs only for the unordered pair {a,b}={1,2}.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/main.tex#thm:stable-uniqueness`

### [Degree-six image-algebra bounds for elementary and separated tame words](../units/RMU-5DB60010.md)

`RMU-5DB60010` · `computational_result`

For the fixed degree-seven Keller map and the exact degree-at-most-six image-algebra slice in the packet, every single pure monomial elementary source shear has the stated span: at zero shear parameter it is generated by 1,Q,R, while at nonzero parameter it is generated by 1,sigma R when the transformed degree is at most six and otherwise contains only constants. The standard slice has rank 81 with the pinned nonzero minor. The same transcendence-degree-at-most-two obstruction persists for the packet's one-sided high-weight compositions and mixed-sign separated reduced words. Thus none of these explicitly classified tame families produces three algebraically independent image functions of ordinary degree at most six.

Hypotheses:

- The map, degree-six filtered slice, weights and elementary shear conventions are exactly those in the retained PR 5 packet.
- The word results apply only to the one-sided and separated reduced-word classes stated in the proof notes.
- All exact rank and coefficient calculations are over characteristic zero.

Support:

- **proof:** Weight separation and reduced-word leading-term arguments paired with exact finite rank certificates. — `research-notes/lane5-degree-budgets/REDUCED_WORD_SEPARATION.md`
  - Does not establish: The same bound for arbitrary automorphisms.
- **program:** Six exact standard, elementary, resonant, lacunary and reduced-word replays. — `research-notes/lane5-degree-budgets/all_elementary_monomial_shears.py`
  - Does not establish: Coverage outside the encoded operation families.

Limitations:

- It does not classify arbitrary polynomial source automorphisms, wild automorphisms or unrestricted mixed words.
- It is not yet an orbit-wide lower bound for intrinsic coordinate degree.

### [Exact marked-root benchmark has no punctual collision defect](../units/RMU-1B8F0001.md)

`RMU-1B8F0001` · `computational_result`

For R=C[a,b,c] and P(T)=cT^3-2T^2+bT-2a, the ordered-root normalization is finite flat, its discriminant and quadratic resolvent have the displayed exact formulas, and the standard triple-collision complement ideal is (u(u+v),uv,v(u+v))=(u,v)^2. In the associated Cech module the closed-point saturation quotient is zero.

Hypotheses:

- The coefficient field is C and the marked cubic is exactly cT^3-2T^2+bT-2a.
- Saturation is taken inside the kernel module by the closed-point maximal ideal.

Support:

- **proof:** Exact formulas and the local-cohomology proof of saturation vanishing. — `research-notes/lane1-models-20260803-v1/explicit-marked-root-collision-saturation.tex`
  - Does not establish: Vanishing for a hypothetical omitted Keller defect.

Limitations:

- It is a benchmark, not an arbitrary cubic Keller normalization and not a proof that every collision quotient vanishes.

### [Explicit type-IV triple-plane test object and cone module](../units/RMU-1B8F0004.md)

`RMU-1B8F0004` · `computational_result`

The displayed cross-product quartic net has a reduced length-13 base scheme and resolves to a finite flat degree-three type-IV cover. Over Q its degree-nine ramification and degree-ten branch polynomials are irreducible; the branch has 21 geometric A2 cusps. The affine cone has a length-one Ext defect and a four-by-four matrix factorization of its quadratic-resolvent module, with normalization-index Fitting ideal equal to the branch polynomial times (a,b,c).

Hypotheses:

- The three displayed cubic forms and induced quartic net are used exactly.
- Irreducibility is asserted over Q, not geometrically.

Dependencies:

- `depends_on` [`RMU-1B8F0003`](../units/RMU-1B8F0003.md): Uses the type-IV smooth homogeneous gate as its geometric context.

Support:

- **program:** Exact reconstruction of the net, branch/cusp scheme, Hessian identities, matrix factorization, and Fitting ideal. — `research-notes/lane1-models-20260803-v1/README.md`
  - Does not establish: A polynomial Keller realization or a Keller omitted value.

Limitations:

- It is not a Keller map.
- The calculation does not supply three affine source openings, the Keller collision Cech quotient, or the full vertex conductor.

### [Completed defect branch and exact defective-fibre length](../units/RMU-1A8D0005.md)

`RMU-1A8D0005` · `corollary`

At a point y in Supp(Delta_F), completion of the cubic normalization has one normal local factor of rank three. Its cubic fraction-field extension is non-Galois and therefore has S_3 Galois closure. If b is the presentation number from RMU-1A8D0001, then the finite normalization fibre is supported at one point and has scheme length b+3, hence at least four; length four is exactly the one-generator stratum.

Hypotheses:

- The setup and notation are those of RMU-1A8D0001.
- The target local ring is completed at a point in the support of the defect.

Dependencies:

- `depends_on` [`RMU-1A8D0001`](../units/RMU-1A8D0001.md): Uses the presentation number b and the defect/nonfree equivalence.

Support:

- **proof:** Rank-one and rank-two completed normal factors are free; a cyclic rank-three factor is free by character decomposition; minimality then computes the fibre length. — [`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex#cor:formal-cubic-defect`](../../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md#label-cor-formal-cubic-defect)
  - Does not establish: Nonexistence of a defect branch.

Limitations:

- The result supplies necessary structure but does not exclude such a branch.
- The fibre length is the scheme length of the finite normalization fibre, not the number of source points.

### [Fiber table](../units/RMU-22A9C59B.md)

`RMU-22A9C59B` · `corollary`

The affine fiber size is three off \(S_F\), one on
\(V(\mathcal D)\setminus(T_3\cup\bigcup C_\beta)\), two on a deleted
plane away from \(V(\mathcal D)\), and zero on \(T_3\) and on every
\(C_\beta\).

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#cor:fiber-table`](../../proof-sources/01-cubic-incidence/main.md#label-cor-fiber-table)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#cor:fiber-table`](../../proof-sources/01-cubic-incidence/main.md#label-cor-fiber-table)

### [If \(S_F\) is smooth, then \(F\) is surjective.](../units/RMU-62D95304.md)

`RMU-62D95304` · `corollary`

If \(S_F\) is smooth, then \(F\) is surjective.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/omitted-values.tex#cor:smooth-nonproper-surjective`](../../proof-sources/01-cubic-incidence/appendices/omitted-values.md#label-cor-smooth-nonproper-surjective)

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

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#cor:moduli-data`](../../proof-sources/01-cubic-incidence/main.md#label-cor-moduli-data)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#cor:moduli-data`](../../proof-sources/01-cubic-incidence/main.md#label-cor-moduli-data)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#lem:nonproper-general`](../../proof-sources/01-cubic-incidence/main.md#label-lem-nonproper-general)

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

- `uses` [`RMU-F908DA7B`](../units/RMU-F908DA7B.md): Formal statement references thm:AB-global.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/audit-repairs.tex#lem:retained-infinity-gluing`](../../proof-sources/01-cubic-incidence/appendices/audit-repairs.md#label-lem-retained-infinity-gluing)

### [The polynomial \(\Delta_{\mathrm{prim}}\) is irreducible in \(\C[a,b,c]\).](../units/RMU-9003C2D9.md)

`RMU-9003C2D9` · `lemma`

The polynomial \(\Delta_{\mathrm{prim}}\) is irreducible in
\(\C[a,b,c]\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#lem:primitive-disc`](../../proof-sources/01-cubic-incidence/main.md#label-lem-primitive-disc)

### [Alternating self-duality and the one-generator defect stratum](../units/RMU-1A8D0002.md)

`RMU-1A8D0002` · `proposition`

At a closed defect point, choose an orientation of the rank-two trace-zero module E_y. Its minimal presentation extends to an alternating self-dual free resolution of (Delta_F)_y, so the finite-length defect is Matlis self-dual and has equal generator and socle dimensions b. If b=1, then (Delta_F)_y=A/(f_1,f_2,f_3) for an A-regular sequence, E_y is its second syzygy, and the resolution is Koszul with Betti numbers (1,3,3,1).

Hypotheses:

- The setup and notation are those of RMU-1A8D0001.
- A=R_y is the three-dimensional regular local ring at a closed point.
- An orientation det(E_y)=A is chosen.

Dependencies:

- `depends_on` [`RMU-1A8D0001`](../units/RMU-1A8D0001.md): Uses the minimal local presentation of the canonical defect.

Support:

- **proof:** The wedge pairing on the oriented reflexive rank-two module produces the alternating middle map; dualizing gives Matlis self-duality and the b=1 Koszul case. — [`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex#prop:cubic-defect-self-duality`](../../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md#label-prop-cubic-defect-self-duality)
  - Does not establish: Nonexistence of the one-generator stratum in a Keller normalization.

Limitations:

- Self-duality constrains a defect but does not exclude one.
- No Keller-specific multiplication or boundary condition is imposed by this unit alone.

### [Canonical finite Ext defect for a cubic Keller normalization](../units/RMU-1A8D0001.md)

`RMU-1A8D0001` · `proposition`

Let R=C[y_1,y_2,y_3], let B be the finite normalization attached to a generic-degree-three Keller map, and write B=R direct-sum E by trace. Then B and E are reflexive and Delta_F=Ext^1_R(B,R)=Ext^1_R(E,R) has finite length. Its support is exactly the locus where B is not free over R. Consequently B is finite flat over R if and only if Delta_F=0. At a closed point y, a minimal resolution 0 -> A^b -> A^(b+2) -> E_y -> 0 over A=R_y presents (Delta_F)_y as the cokernel of the dual matrix, with b minimal generators.

Hypotheses:

- The ground field is C.
- F:A^3->A^3 is a Keller map with separable generic degree three.
- B is the integral closure of the target coordinate ring in the source function field.

Support:

- **proof:** Conventional reflexivity, Auslander-Buchsbaum, minimal-resolution, and local-duality proof. — [`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex#prop:cubic-ext-defect`](../../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md#label-prop-cubic-ext-defect)
  - Does not establish: Vanishing of the defect for Keller maps.

Limitations:

- The proposition identifies and localizes the defect but does not prove that it vanishes.

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

- `uses` [`RMU-DD6B3EDC`](../units/RMU-DD6B3EDC.md): Formal statement references prop:conditional-master.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/audit-repairs.tex#prop:master-cover-cartesian`](../../proof-sources/01-cubic-incidence/appendices/audit-repairs.md#label-prop-master-cover-cartesian)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#prop:conditional-master`](../../proof-sources/01-cubic-incidence/main.md#label-prop-conditional-master)

### [Conditional transverse ADE filter for cubic resolvent defects](../units/RMU-1A8D0006.md)

`RMU-1A8D0006` · `proposition`

A nonzero cubic defect class is detected at a height-two singular prime of the quadratic resolvent. If, after strict henselization and completion, every generic transverse surface singularity at such a prime is a split rational double point, then only A_(3r-1) and E6 can carry a nonzero class killed by three, and each singular-curve component contributes at most one F_3 coordinate. The two nonzero classes have explicit two-by-two matrix factorizations; their cyclic covers are transverse A_(r-1) and D4 covers, with explicit transposition quotients back to regular-base cubic equations.

Hypotheses:

- The exact resolvent carrier is RMU-1A8D0004.
- Dao's codimension-two detection theorem is RMU-13177F24.
- Every relevant generic transverse surface singularity is, after strict henselization and completion, a split rational double point.

Dependencies:

- `depends_on` [`RMU-1A8D0004`](../units/RMU-1A8D0004.md): Uses the exact order-three resolvent eigensheaf carrying the defect.
- `depends_on` [`RMU-13177F24`](../units/RMU-13177F24.md): Dao detection places a nonzero class at a height-two singular prime.

Support:

- **proof:** ADE class groups give the killed-by-three filter, while explicit ideals, matrix factorizations, invariant rings, and transposition actions give the local models. — [`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex#prop:transverse-ADE-filter`](../../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md#label-prop-transverse-ade-filter)
  - Does not establish: That every relevant transverse singularity is rational double point type.
  - Does not establish: Extension of the local models through the closed threefold point.
- **program:** Exact SymPy replay for the A_(3r-1) and E6 matrix factorizations, ideal presentations, invariant equations, and D4-to-E6 identity. — [`manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`](../../proof-sources/01-cubic-incidence/code/verify_ade_matrix_factorizations.md)
  - Does not establish: The conventional ADE class-group facts.
  - Does not establish: The RDP hypothesis, three-dimensional extension, or Keller compatibility.

Limitations:

- The rational-double-point hypothesis is not proved for an actual Keller defect.
- The explicit transverse MCM modules are not extended through the closed three-dimensional point.
- The exact script verifies polynomial identities and presentations, not the geometric hypothesis or global compatibility.

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/cubic-resolvent-defects.tex#prop:cubic-divisorial-trichotomy`](../../proof-sources/01-cubic-incidence/appendices/cubic-resolvent-defects.md#label-prop-cubic-divisorial-trichotomy)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#prop:keller-degree`](../../proof-sources/01-cubic-incidence/main.md#label-prop-keller-degree)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/cubic-resolvent-defects.tex#prop:smooth-axis-comparison`](../../proof-sources/01-cubic-incidence/appendices/cubic-resolvent-defects.md#label-prop-smooth-axis-comparison)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/root-slope-geometry.tex#prop:marked-vandermonde`](../../proof-sources/01-cubic-incidence/appendices/root-slope-geometry.md#label-prop-marked-vandermonde)

### [Source splitting and the exact attained-value boundary](../units/RMU-1A8D0003.md)

`RMU-1A8D0003` · `proposition`

For every generic-degree-three complex Keller normalization, base change to the affine source gives B tensor_R S isomorphic to S times C, where the S-factor is the canonical marked section and C is a normal quadratic S-algebra. After choosing a generator eta of its trace-zero summand, C is isomorphic to S[eta]/(eta^2-D). The generator and D are choice-dependent. The normalization is free over every attained target value, and Supp(Delta_F) is contained in the omitted-value locus, hence in the singular locus of the reduced nonproperness set.

Hypotheses:

- The setup and notation are those of RMU-1A8D0001.
- The omitted-values theorem RMU-C5C8680E is used for the final containment.

Dependencies:

- `depends_on` [`RMU-1A8D0001`](../units/RMU-1A8D0001.md): Uses the canonical defect to state its exact support boundary.
- `depends_on` [`RMU-C5C8680E`](../units/RMU-C5C8680E.md): Uses that omitted values are singular points of the reduced nonproperness set.

Support:

- **proof:** The source section is open and closed after etale base change; normality and factoriality identify the residual quadratic algebra, and faithfully flat descent proves attained-value flatness. — [`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex#prop:cubic-source-splitting`](../../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md#label-prop-cubic-source-splitting)
  - Does not establish: A canonical choice of eta or D.
  - Does not establish: Flatness at an omitted target value.

Limitations:

- The splitting has a canonical section but no canonical trace-zero generator or canonical displayed polynomial.
- Source splitting cannot be applied at a defect value because every such value is omitted.
- The proposition does not prove target flatness at omitted values.

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

- `uses` [`RMU-BA2C2F76`](../units/RMU-BA2C2F76.md): Formal statement references thm:stable-uniqueness.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/audit-repairs.tex#prop:cubic-positive-internal`](../../proof-sources/01-cubic-incidence/appendices/audit-repairs.md#label-prop-cubic-positive-internal)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/root-slope-geometry.tex#prop:root-slope-transform`](../../proof-sources/01-cubic-incidence/appendices/root-slope-geometry.md#label-prop-root-slope-transform)

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

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#thm:equivalence`](../../proof-sources/01-cubic-incidence/main.md#label-thm-equivalence)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#thm:equivalence`](../../proof-sources/01-cubic-incidence/main.md#label-thm-equivalence)

### [Collision idempotents and the saturation carrier of a cubic flatness defect](../units/RMU-1A8D0010.md)

`RMU-1A8D0010` · `theorem`

Let T be the S_3-Galois normalization of a generic-degree-three Keller extension at an omitted value y, and cover its attained part by the three conjugate source charts. For a divided-difference matrix F(X)-F(X')=M(X,X')(X-X'), put q=det(M) and c=det(JF). Then q(q-c)=0 and q/c is the diagonal idempotent. The product of the three off-diagonal idempotents selects pairwise-distinct triples. If K_y=ker(d_1), I_y=im(d_0) in the resulting affine Cech complex and I_y^sat=I_y:_(K_y)m_y^infinity, then I_y^sat/I_y is MatlisDual(Delta_y) tensor V_std as an A[S_3]-module. Hence B_y is flat exactly when I_y is saturated, and length(I_y^sat/I_y)=2 length(Delta_y). In the standard ordered-root triple collision the chart-complement ideal is (u(u+v),uv,v(u+v))=(u,v)^2 and its saturation quotient vanishes.

Hypotheses:

- The ground field has characteristic zero and the generic cubic extension has S_3 Galois closure.
- Delta_y is the local finite Ext defect of RMU-1A8D0001.
- The Cech rings and their saturation are exactly those defined in the linked proof packet.

Dependencies:

- `depends_on` [`RMU-1A8D0001`](../units/RMU-1A8D0001.md): Uses the canonical local Ext defect.

Support:

- **proof:** Equivariant Cech and local-duality argument with explicit diagonal and off-diagonal collision idempotents. — `research-notes/lane1-collision-saturation-20260802-v1/flatness-defect-repairs.tex`
  - Does not establish: Saturation for the actual unknown non-product boundary of an arbitrary cubic Keller map.
- **program:** Exact divided-difference and standard-root identity checks. — `research-notes/lane1-collision-saturation-20260802-v1/verify_collision_idempotent.py`
  - Does not establish: The general local-duality argument.

Limitations:

- The theorem does not prove saturation for every non-equivariant Keller boundary.
- It does not prove flatness of every cubic Keller normalization.

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/cubic-resolvent-defects.tex#thm:dao-codim-two`](../../proof-sources/01-cubic-incidence/appendices/cubic-resolvent-defects.md#label-thm-dao-codim-two)

### [Exact quadratic-resolvent carrier of the cubic flatness defect](../units/RMU-1A8D0004.md)

`RMU-1A8D0004` · `theorem`

Let T be the normalization in the S_3 Galois closure, Q=T^(A_3), and L the nontrivial cubic eigensheaf. Then Q is a normal finite-flat quadratic R-algebra, T=Q direct-sum L direct-sum L^[2], L^[3]=Q, and the quadratic involution satisfies sigma^*L=L^[2]=L^dual. As an R-module, the cubic trace-zero summand E is isomorphic to L. Hence Delta_F=Ext^1_R(L,R), and B is finite flat over R if and only if L is maximal Cohen-Macaulay over Q.

Hypotheses:

- The setup and notation are those of RMU-1A8D0001.
- The generic Galois closure is S_3 and the corrected divisorial inertia types are those of RMU-C1DD871B.

Dependencies:

- `depends_on` [`RMU-1A8D0001`](../units/RMU-1A8D0001.md): Identifies the same canonical defect on the quadratic resolvent.
- `depends_on` [`RMU-C1DD871B`](../units/RMU-C1DD871B.md): The corrected divisorial inertia list makes T/Q unramified in codimension one.

Support:

- **proof:** Invariant-ring normality, the codimension-one character decomposition, transposition invariants, and Auslander-Buchsbaum give the exact carrier and equivalence. — [`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex#thm:exact-resolvent-carrier`](../../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md#label-thm-exact-resolvent-carrier)
  - Does not establish: The MCM property for the eigensheaf of an actual Keller defect.

Limitations:

- The theorem does not prove that L is maximal Cohen-Macaulay.
- It does not identify the square class, conductor, singular primes, or local class vector for a hypothetical actual defect.

### [Generic \(S_3\) monodromy](../units/RMU-A8650DD4.md)

`RMU-A8650DD4` · `theorem`

Assume characteristic zero and generic degree three.  The normal closure of
the normalized cubic extension has Galois group \(S_3\).  Over \(\C\), the
geometric monodromy of the three-sheeted \'{e}tale locus is therefore
\(S_3\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/root-slope-geometry.tex#thm:generic-S3`](../../proof-sources/01-cubic-incidence/appendices/root-slope-geometry.md#label-thm-generic-s3)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#thm:AB-global`](../../proof-sources/01-cubic-incidence/main.md#label-thm-ab-global)

### [Omitted values are singular](../units/RMU-C5C8680E.md)

`RMU-C5C8680E` · `theorem`

For every complex polynomial Keller map,
\[
O_F\subseteq\Sing(S_F).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/appendices/omitted-values.tex#thm:omitted-singular`](../../proof-sources/01-cubic-incidence/appendices/omitted-values.md#label-thm-omitted-singular)

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
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#thm:pole-cancellation`](../../proof-sources/01-cubic-incidence/main.md#label-thm-pole-cancellation)

### [Smooth homogeneous one-generator defects reduce to type IV](../units/RMU-1B8F0003.md)

`RMU-1B8F0003` · `theorem`

Let a connected normal graded cubic C[a,b,c]-algebra have trace-zero presentation 0→A(-d)→A(1-d)^3→M→0 with map (a,b,c)^t, and suppose its projectivized cubic cover is smooth and its affine cone contains a dense open A3. Stable-rationality invariants and the cubic building-section bounds force d=4. The resulting smooth triple plane is the type-IV blowup of P2 at the length-13 zero scheme of a section of T_P2(2), with polarization 4L-sum E_i.

Hypotheses:

- The projectivized cover is smooth.
- The affine cone contains a dense open isomorphic to A3.
- The stated one-generator graded presentation holds.

Support:

- **proof:** Cohomological reduction, stable-birational obstruction, and type-IV classification. — `research-notes/lane1-models-20260803-v1/TYPEIV_GATE.md#1-the-smooth-projective-reduction`
  - Does not establish: Any singular-projectivization case or affine Keller opening.

Limitations:

- Singular projectivizations are not covered without additional resolution hypotheses.
- The theorem does not produce a Keller realization.

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

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#thm:stable-uniqueness`](../../proof-sources/01-cubic-incidence/main.md#label-thm-stable-uniqueness)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#thm:stable-uniqueness`](../../proof-sources/01-cubic-incidence/main.md#label-thm-stable-uniqueness)

## Open frontier

### [Boundary Torelli](../units/RMU-F94F448E.md)

`RMU-F94F448E` · `question`

To what extent is a marked-root cover determined, up to polynomial
left--right equivalence, by its deleted boundary together with the induced
normalization, conductor, and incidence data?  In particular, which
hypotheses make the boundary-completeness problem in
\cref{prop:conditional-master} a reconstruction theorem?

Dependencies:

- `uses` [`RMU-DD6B3EDC`](../units/RMU-DD6B3EDC.md): Formal statement references prop:conditional-master.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#q:boundary-torelli`](../../proof-sources/01-cubic-incidence/main.md#label-q-boundary-torelli)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#q:boundary-torelli`](../../proof-sources/01-cubic-incidence/main.md#label-q-boundary-torelli)

### [Construct a different-filtered source-flow or transferred L-infinity model that independently…](../units/JCG-D9E57688.md)

`JCG-D9E57688` · `question`

Construct a different-filtered source-flow or transferred L-infinity model that independently reproduces the bounded-degree Kuranishi equations and the length-584 Artin algebra.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`

### [Cubic flatness](../units/RMU-34FBCB8D.md)

`RMU-34FBCB8D` · `question`

Does the Keller condition force the finite cubic normalization
\(\overline X\to\A^3\) to be flat?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/01-cubic-incidence/main.tex#q:flatness`](../../proof-sources/01-cubic-incidence/main.md#label-q-flatness)
  - Full source and surrounding context: [`manuscripts/01-cubic-incidence/main.tex#q:flatness`](../../proof-sources/01-cubic-incidence/main.md#label-q-flatness)

### [For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree…](../units/JCG-4451EE05.md)

`JCG-4451EE05` · `question`

For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree delta_LR(xi)=min{deg H : H is polynomially left-right equivalent to xi} from intrinsic conductor, ramification, valuation, or nonproperness data. A bound of at least seven for every nontrivial generic-degree-three boundary class would supply the missing degree-cost bridge from cubic-cover classification to low-degree exclusion.

### [Show that at least one nonzero class in the local F_3^2 sign-torsor…](../units/JCG-1C1790E5.md)

`JCG-1C1790E5` · `question`

Show that at least one nonzero class in the local F_3^2 sign-torsor space globalizes across the boundary; this would contradict the absence of nontrivial finite etale covers of affine three-space.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/01-cubic-incidence/appendices/minimal-smooth-defect.tex#q:end-to-global-sign-torsor`
