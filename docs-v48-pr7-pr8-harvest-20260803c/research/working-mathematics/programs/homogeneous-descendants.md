# Homogeneous Descendants

Rank-sensitive suspensions, pairing constructions, sparse obstructions, and low-dimensional Jordan forms organize the search for smaller homogeneous descendants.

This is a generated progress view of retained mathematics. Workflow labels and private source locators are intentionally omitted.

<!-- noncanonical-overlay -->

## Setup and research posture

This program studies homogeneous and Drużkowski presentations descended from
a fixed nonhomogeneous Keller counterexample, and asks how far those
presentations can be compressed. Distinguish intrinsic cover data from
presentation-relative tensor data. Jordan types, Waring lengths, pairing
bounds, and row-killing spaces may be exact for one tensor without becoming
universal lower bounds.

The two active geometric fronts are a dimension-five full-kernel collision
chart and compression of the fixed cubic-homogeneous presentation by one
variable. In the first, finite-field samples do not replace characteristic-
zero component geometry. In the second, source coupling is substantially
controlled, but moving target gauge can cancel primary quartic functionals;
the secondary class is the live object.

## Strategy and payoff

For the dimension-five chart, eliminate solvable variables before expensive
saturation. Stage saturation by every open factor, checkpoint intermediate
ideals, and obtain components, dimensions, degrees, and singular loci before
normalization. A component on which the obstruction vanishes is a
construction lead, not a failed exclusion.

For compression, formulate the moving source/target quotient intrinsically.
Classify all allowed primary cancellations and transport the first surviving
secondary class through that family. Reconstruct missing packet inputs from
the equations rather than treating saved fragments as complete receipts.

Every computation should report the coefficient domain, denominators,
component, generic rank, and the exact assertion it establishes. Failed
large-CAS processes carry no mathematical conclusion beyond the absence of
an output.

## Connections

All descendant presentations retain the same three-sheeted function-field
cover, linking this program to cubic incidence and stable moduli. The local
deformation program provides a model for separating tangent, obstruction,
and nonlinear saturation statements. Collision geometry also offers a
possible representation-theoretic route through monolith and prolongation
structure.

## Current priorities and research freedom

The current attention order is:

1. compute the staged characteristic-zero geometry of the regular
   full-kernel chart;
2. decide the first-normal obstruction on each resulting component;
3. prove secondary obstruction survival under arbitrary moving target and
   stable cancellation, or reconstruct an explicit compression locus; and
4. seek structural realization lower bounds from boundary or cover data.

Unexpected low-dimensional components, cancellations, or alternative
presentations are high-value outputs when returned with reconstruction data.

## Graveyard and scope fences

- Finite-field nonvanishing is not characteristic-zero nowhere-vanishing.
- A collision-line chart is not a global homogeneous counterexample.
- Repeating an unchanged timed-out saturation is not progress.
- Row-killing directions are not automatically polynomial automorphisms.
- Fixed-tensor pairing bounds are not universal.
- A primary obstruction on one transversal does not survive arbitrary
  moving target gauge without a secondary-class argument.

## Definitions and constructions

### [Five-chart presentation of the Lane 7 projective kernel incidence](../units/RMU-5C7E0012.md)

`RMU-5C7E0012` · `construction`

For the stored Lane 7 residual matrix $M(a)$ and accepted-open determinant $d(a)$, the projective kernel incidence $M(a)u=0$ on $D(d)$ is covered by the five affine charts $u_i=1$. Each chart is presented exactly by the ten equations $M(a)u=0$ and the localizer equation $z d(a)-1$. The harvested generators reconstruct these ideals from the pinned source matrices over prime fields or over $\mathbf Q$; they do not assert their dimensions.

Hypotheses:

- The matrix M(a), determinant d(a), row denominator units, and variable order are exactly those in research-notes/lane7-split-incidence-20260802-v1/.
- In a prime field, the characteristic does not divide a denominator-clearing row multiplier.

Dependencies:

- `depends_on` [`RMU-5C7E0011`](../units/RMU-5C7E0011.md): The split-incidence theorem defines M, d, and the intrinsic Pluecker marking open to which these charts belong.

Support:

- **program:** Independent exact chart generators for Macaulay2 and Singular, with denominator clearing by row units and localization by z*d-1. — `research-notes/lane7-projective-kernel-20260803-v1/README.md`
  - Does not establish: Any dimension, grade, corank, or component result before a CAS run is preserved and checked.

Limitations:

- No chart dimension or codimension has been promoted.
- The construction alone does not prove carrier grade six, absolute component decomposition, or nonemptiness of the genuine Pluecker marking open on every component.

## Retained results

### [A dimension-minimal cubic-homogeneous collision algebra is generated by its collision midpoin…](../units/JCG-08AE5516.md)

`JCG-08AE5516` · `assertion`

A dimension-minimal cubic-homogeneous collision algebra is generated by its collision midpoint and difference, has d in A^3 and dim A/A^3 at most one, every nonzero proper ideal contains d, its minimal ideal D has nonzero internal cubic product, and dim D is at least ceil((n-1)/2).

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/monolith-prolongation.tex#prop:collision-monolith`

### [A full-rank square-zero Gorni-Zampieri pairing H=B(Dz)^{*3}, BD=0, is triangularly right-equi…](../units/JCG-99288D5E.md)

`JCG-99288D5E` · `assertion`

A full-rank square-zero Gorni-Zampieri pairing H=B(Dz)^{*3}, BD=0, is triangularly right-equivalent to the paired cubic map times an identity factor; the 110-variable Druzkowski map is therefore a stable presentation of the 19-variable cubic map.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-019`

### [A second counterexample \(G:\mathbb C^4\to\mathbb C^4\) has determinant \(4\) and generic deg…](../units/JCG-10BD21D3.md)

`JCG-10BD21D3` · `assertion`

A second counterexample \(G:\mathbb C^4\to\mathbb C^4\) has determinant \(4\) and generic degree \(8\).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-013`

### [A second issue occurs in Zwart’s fixed-highest-weight-vector proof.](../units/JCG-E2F31533.md)

`JCG-E2F31533` · `assertion`

A second issue occurs in Zwart’s fixed-highest-weight-vector proof.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-040`

### [A straightforward explicit reduction produced a cubic-homogeneous map in \(79\) variables and…](../units/JCG-B7744F4C.md)

`JCG-B7744F4C` · `assertion`

A straightforward explicit reduction produced a cubic-homogeneous map in \(79\) variables and a Drużkowski cubic-linear map in \(426\) variables.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-014`

### [Although every JH(z) is nilpotent, the product JH(e_d)JH(e_t) has characteristic polynomial l…](../units/JCG-95F70298.md)

`JCG-95F70298` · `assertion`

Although every JH(z) is nilpotent, the product JH(e_d)JH(e_t) has characteristic polynomial lambda^18(lambda+3); hence the polynomial-matrix family is not strongly nilpotent and has no common constant triangularizing basis.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-022`

### [An everywhere-regular five-dimensional quadratic nilpotent line pencil whose kernel map spans…](../units/JCG-3FB0B6BB.md)

`JCG-3FB0B6BB` · `assertion`

An everywhere-regular five-dimensional quadratic nilpotent line pencil whose kernel map spans P4 has saturated filtration degrees (-4,-2,0,2,4); every successive map is an isomorphism and the kernel map is the rational normal quartic.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-031`

### [An exact row-defect theorem holds in the two-matrix square-zero family; the accompanying…](../units/JCG-8F25FC7B.md)

`JCG-8F25FC7B` · `assertion`

An exact row-defect theorem holds in the two-matrix square-zero family; the accompanying finite-field search found no better example in the tested range.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-012`

### [An explicit pair \(f,g\) on \(SU(24)\) or \(SU(79)\) has been written down.](../units/JCG-78845CD5.md)

`JCG-78845CD5` · `assertion`

An explicit pair \(f,g\) on \(SU(24)\) or \(SU(79)\) has been written down.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-041`

### [An explicit smooth Z11 residue disk in the regular Jordan-type-(5) collision-line locus…](../units/JCG-64E18DF3.md)

`JCG-64E18DF3` · `assertion`

An explicit smooth Z11 residue disk in the regular Jordan-type-(5) collision-line locus cannot extend even to first normal order to a global homogeneous quadratic nilpotent 5 by 5 Jacobian; transformed and coordinate-free exact systems have ranks (60,61) and (125,126), respectively.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/dimension-five.tex#thm:n5-first-normal`

### [An explicit square-zero Druzkowski pairing of the 19D cubic gives a 135D…](../units/JCG-0378B011.md)

`JCG-0378B011` · `assertion`

An explicit square-zero Druzkowski pairing of the 19D cubic gives a 135D Druzkowski counterexample with collision.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-004`

### [Any global homogeneous quadratic nilpotent 5 by 5 Jacobian extending an everywhere-regular…](../units/JCG-15D52C7B.md)

`JCG-15D52C7B` · `assertion`

Any global homogeneous quadratic nilpotent 5 by 5 Jacobian extending an everywhere-regular collision line must have a rank-at-most-three locus of codimension exactly two away from that line.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/dimension-five.tex#thm:n5-rank-drop`

### [At the specified rank-six compression point, quadratic source fields contain a 109-dimensiona…](../units/JCG-F245F636.md)

`JCG-F245F636` · `assertion`

At the specified rank-six compression point, quadratic source fields contain a 109-dimensional row-killing affine family with constant quartic obstruction, including a 75-dimensional family of triangular polynomial automorphisms; the remaining tangent quotient has dimension 20 and is generically second-order obstructed.

Support:

- **source assertion:** proposition and exact-computation proof — [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#prop:row-killing-families`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-prop-row-killing-families)

### [Every quadratic matrix annihilating the Veronese kernel k_m factors uniquely as N=L_mS_m;…](../units/JCG-C992885C.md)

`JCG-C992885C` · `assertion`

Every quadratic matrix annihilating the Veronese kernel k_m factors uniquely as N=L_mS_m; iterated Hilbert-Burch descent preserves regular nilpotence, and a fully compatible canonical descent chain is necessarily a common scalar multiple of the principal chain.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-032`

### [For a general five-dimensional quadratic pencil, integrable markings lie on the proper…](../units/JCG-566A5F84.md)

`JCG-566A5F84` · `assertion`

For a general five-dimensional quadratic pencil, integrable markings lie on the proper discriminant det Phi_N=0, and normalized collisions lie on the determinantal locus rank Theta_N<=9 together with the open independence condition on the recovered marking vectors.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-034`

### [For a global regular-type five-dimensional nilpotent quadratic tensor with full-span collisio…](../units/JCG-A82581C7.md)

`JCG-A82581C7` · `assertion`

For a global regular-type five-dimensional nilpotent quadratic tensor with full-span collision-line kernel, the saturated rank-one defects are nested and have total codimension-two class 20H^2, combined Hilbert polynomial 10n^2+50n+81, and weighted effective increments 5Delta_1+4Delta_2+3Delta_3+2Delta_4+Delta_5=20H^2.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-035`

### [For an n-dimensional degree-at-most-three map whose quadratic span has rank r, a…](../units/JCG-27AF15AA.md)

`JCG-27AF15AA` · `assertion`

For an n-dimensional degree-at-most-three map whose quadratic span has rank r, a block-determinant suspension produces a cubic-homogeneous map in dimension n+r+1.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-006`

### [For any Keller map F, the symmetric double (F(x),JF(x)^T y) is polynomially…](../units/JCG-301AAE68.md)

`JCG-301AAE68` · `assertion`

For any Keller map F, the symmetric double (F(x),JF(x)^T y) is polynomially right-equivalent to F times the identity, so the 38-variable gradient descendant has the same generic degree and monodromy as the 19-variable cubic map.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-018`

### [For the 19D example, the generic Jacobian perturbation JH has Jordan type…](../units/JCG-7AFFFF85.md)

`JCG-7AFFFF85` · `assertion`

For the 19D example, the generic Jacobian perturbation JH has Jordan type (18,1); nonzero scalar fibers are conjugate and the zero fiber is an automorphism degeneration.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-007`

### [For the displayed 19-dimensional block tensor H(X,w,t)=(tQ(X)+t^2Bw,-q(X),0), the weak symmet…](../units/JCG-BC2FDB8E.md)

`JCG-BC2FDB8E` · `assertion`

For the displayed 19-dimensional block tensor H(X,w,t)=(tQ(X)+t^2Bw,-q(X),0), the weak symmetric-dilation invariant is at most 37-dim(w), hence at most 36.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-027`

### [For the displayed 19-variable tensor A=U plus kt, A^3=U of dimension 18,…](../units/JCG-5CA10BFA.md)

`JCG-5CA10BFA` · `assertion`

For the displayed 19-variable tensor A=U plus kt, A^3=U of dimension 18, U^3=W of dimension 7, mu(W,U,U)=0, the all-layer associative closure on U is M18, and the multiplication Lie algebra is sl18; the symplectic alternative is excluded by a full-rank 153-variable certificate.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/monolith-prolongation.tex#prop:fixed-sl18-core`

### [For the fixed 38-variable Hessian quartic, Delta^m(Q^{m+1}) is nonzero for every m>=1;…](../units/JCG-D55D3D6A.md)

`JCG-D55D3D6A` · `assertion`

For the fixed 38-variable Hessian quartic, Delta^m(Q^{m+1}) is nonzero for every m>=1; an explicit two-parameter inverse ray removes the earlier parity gap and ties every nonzero coefficient to a sheet escaping at the discriminant.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-021`

### [For the minimal ideal D of a dimension-minimal cubic-homogeneous collision algebra over…](../units/JCG-30DB849B.md)

`JCG-30DB849B` · `assertion`

For the minimal ideal D of a dimension-minimal cubic-homogeneous collision algebra over an algebraically closed characteristic-zero field, the Lie algebra generated by partial multiplications is sl(D) or sp(D,omega).

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/monolith-prolongation.tex#thm:monolith-prolongation`

### [For the principal sl2 conic on Sym^m(k^2), the integrability operator has determinant…](../units/JCG-B449567D.md)

`JCG-B449567D` · `assertion`

For the principal sl2 conic on Sym^m(k^2), the integrability operator has determinant -m^{m+2}(m+2)^m; no direct sum of principal conics supports a noncollinear normalized collision.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-030`

### [If an n-dimensional homogeneous map has a k-dimensional partial-gradient block, it admits…](../units/JCG-0934E7C3.md)

`JCG-0934E7C3` · `assertion`

If an n-dimensional homogeneous map has a k-dimensional partial-gradient block, it admits a weak symmetric dilation in dimension at most 2n-k; in particular every polynomial map has weak symmetric-dilation dimension at most 2n-1.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-026`

### [In the displayed six-dimensional transversal, the exact rank-six cone is the reduced…](../units/JCG-24F172FB.md)

`JCG-24F172FB` · `assertion`

In the displayed six-dimensional transversal, the exact rank-six cone is the reduced union V(u3,u5) union V(u0,u3) union V(u2,u5); every point integrates to an exact cubic rank-six jet, but the universal quartic cokernel functional Gamma_4 is identically -1, so no member lifts through quartic order.

Support:

- **source assertion:** theorem and exact-computation proof — [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#thm:transverse-cone-no-lift`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-thm-transverse-cone-no-lift)

### [In the five-dimensional square-zero two-matrix ansatz with a coordinate collision, exactly th…](../units/JCG-D49A43DC.md)

`JCG-D49A43DC` · `assertion`

In the five-dimensional square-zero two-matrix ansatz with a coordinate collision, exactly three active rows, one directed support edge in each active row, and all five vertices used by the three edges, the Keller equations have no solution.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/dimension-five.tex#thm:n5-sparse`

### [In the scalar-w block case, a 35-dimensional weak dilation extending the evident…](../units/JCG-A7F02148.md)

`JCG-A7F02148` · `assertion`

In the scalar-w block case, a 35-dimensional weak dilation extending the evident (w,t)-compression exists exactly when there is a nonzero vector a satisfying a^TB=0, a^TQ(X)=0, and D_a q(X)=0 identically.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-029`

### [Natural next problems include classification of generic-degree-three examples, bounded-degree…](../units/JCG-44729E0B.md)

`JCG-44729E0B` · `assertion`

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-038`

### [No cover-all-five, three-row, one-off-diagonal-edge-per-row map in the specified coordinate-c…](../units/JCG-033B78BD.md)

`JCG-033B78BD` · `assertion`

No cover-all-five, three-row, one-off-diagonal-edge-per-row map in the specified coordinate-collision sparse N=5 ansatz is Keller.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/dimension-five.tex#thm:n5-sparse`

### [On det(T) nonzero, the five-dimensional full-kernel pencil has Jordan type (5) everywhere…](../units/JCG-2EC7F92F.md)

`JCG-2EC7F92F` · `assertion`

On det(T) nonzero, the five-dimensional full-kernel pencil has Jordan type (5) everywhere exactly when a7 is nonzero; after setting lambda=a7, its parameter space is the principal sl2-module C lambda plus Sym^6(C^2), with det(T)=((lambda^2+4A)^2-96B)/256.

Support:

- **source assertion:** proposition, proof, and invariant-theory continuation — [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#prop:full-kernel-regularity`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-prop-full-kernel-regularity)

### [Recover the six decisive obstruction components canonically from the residue pole filtration…](../units/JCG-5EA4BAEE.md)

`JCG-5EA4BAEE` · `assertion`

Recover the six decisive obstruction components canonically from the residue pole filtration or the determinant of cohomology.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-045`

### [Starting from the public 11D counterexample, rank-sensitive cubic suspension yields an explic…](../units/JCG-38CAAB66.md)

`JCG-38CAAB66` · `assertion`

Starting from the public 11D counterexample, rank-sensitive cubic suspension yields an explicit 19D cubic-homogeneous Keller counterexample with collision.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-003`

### [The admissible symmetric-overlap index kappa gives the lower bound sigma_sym(H)>=2n-kappa_ov(…](../units/JCG-122FC9F6.md)

`JCG-122FC9F6` · `assertion`

The admissible symmetric-overlap index kappa gives the lower bound sigma_sym(H)>=2n-kappa_ov(H); when the overlap form is nondegenerate, the partial-gradient construction gives the matching upper bound 2n-kappa_nd(H).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-028`

### [The cited dimension-varying implication does not establish that the Mathieu conjecture for…](../units/JCG-266D9E33.md)

`JCG-266D9E33` · `assertion`

The cited dimension-varying implication does not establish that the Mathieu conjecture for the fixed group SU(3) is false.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-038`

### [The cited explicit map has the form G(U)=U+H(U) over Q^24, with every…](../units/JCG-4BB50BB3.md)

`JCG-4BB50BB3` · `assertion`

The cited explicit map has the form G(U)=U+H(U) over Q^24, with every nonzero component of H homogeneous cubic, determinant 1, 54 nonzero cubic monomials, and a displayed collision of two distinct rational points.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-002`

### [The cited map from complex affine 11-space to itself has total degree…](../units/JCG-A39E3CCD.md)

`JCG-A39E3CCD` · `assertion`

The cited map from complex affine 11-space to itself has total degree 3, 52 nonzero monomial terms, constant Jacobian determinant -2, and three displayed distinct rational inputs with one common image.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-001`

### [The direct Euclidean 36-dimensional partial-gradient potential is not Keller when B is…](../units/JCG-E1675EDD.md)

`JCG-E1675EDD` · `assertion`

The direct Euclidean 36-dimensional partial-gradient potential is not Keller when B is nonzero; obtaining a 36-dimensional Keller or cover-preserving realization is a separate self-adjoint nilpotent matrix-completion problem.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-042`

### [The earlier 26D cubic-homogeneous and 158D Druzkowski constructions remain valid explicit exa…](../units/JCG-48D22F23.md)

`JCG-48D22F23` · `assertion`

The earlier 26D cubic-homogeneous and 158D Druzkowski constructions remain valid explicit examples but are superseded as upper bounds by the later 19D and 135D examples.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-005`

### [The equivariant cubic rank-six compression condition has a 20-dimensional affine slice, and…](../units/JCG-978BC8D0.md)

`JCG-978BC8D0` · `assertion`

The equivariant cubic rank-six compression condition has a 20-dimensional affine slice, and the quartic obstruction functional is identically one on that slice; modulo two target-row directions this is the natural transverse compression space.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-023`

### [The everywhere-regular Jordan-type (5) collision-line equations in dimension five have a smoo…](../units/JCG-FFBBD77B.md)

`JCG-FFBBD77B` · `assertion`

The everywhere-regular Jordan-type (5) collision-line equations in dimension five have a smooth one-dimensional characteristic-zero family, obtained from an explicit smooth F11 point and Hensel lift.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/dimension-five.tex#thm:n5-regular-family`

### [The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous…](../units/JCG-0EDD5AE2.md)

`JCG-0EDD5AE2` · `assertion`

The explicit constructions give the upper bound N_min <= 19 for cubic-homogeneous counterexamples; the conversation uses the elementary no-collinear-collision argument for the lower bound N_min >= 5.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-008`

### [The explicit pairing dictionary gives a 110D Druzkowski construction, while the derivative-sp…](../units/JCG-263402AA.md)

`JCG-263402AA` · `assertion`

The explicit pairing dictionary gives a 110D Druzkowski construction, while the derivative-space zero-block and equality-case argument give the model-relative bound 52 <= pairing rank <= 110 for the fixed 19D tensor.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-010`

### [The five-attacks package constructs a 38D Hessian quartic with Hessian Jordan type…](../units/JCG-57051B08.md)

`JCG-57051B08` · `assertion`

The five-attacks package constructs a 38D Hessian quartic with Hessian Jordan type (35,2,1) and derives exact central-binomial inverse-ray coefficients with infinitely many nonzero Laplacian terms in the stated parity class.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-009`

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

### [The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and…](../units/JCG-30AF091E.md)

`JCG-30AF091E` · `assertion`

The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and minimal support remain open.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-047`

### [The n+r+1 cubic suspension is coordinate-free on V plus the dual of…](../units/JCG-F701E994.md)

`JCG-F701E994` · `assertion`

The n+r+1 cubic suspension is coordinate-free on V plus the dual of the output-mode span plus one scalar, and r=rank(C^flat) is the minimum possible auxiliary dimension for any factorization of the cubic tensor through an intermediate vector space.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-024`

### [The new 24-variable map improves this to \(\mathrm{MC}(SU(N))\) false for all \(N\ge24\).](../units/JCG-9DC03A22.md)

`JCG-9DC03A22` · `assertion`

The new 24-variable map improves this to \(\mathrm{MC}(SU(N))\) false for all \(N\ge24\).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-016`

### [The normalized full-kernel collision system has 6, 11, and 13 rational points…](../units/JCG-86F5C9FA.md)

`JCG-86F5C9FA` · `assertion`

The normalized full-kernel collision system has 6, 11, and 13 rational points over F7, F11, and F13 respectively, and the computed first-normal obstruction is nonzero at all thirty points.

Support:

- **source assertion:** computational proposition and proof — [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#prop:full-kernel-finite-field-samples`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-prop-full-kernel-finite-field-samples)

### [The original three-variable map has the displayed invariant quotient cubic theta^3-2theta^2+B…](../units/JCG-8AA6A8C5.md)

`JCG-8AA6A8C5` · `assertion`

The original three-variable map has the displayed invariant quotient cubic theta^3-2theta^2+Btheta-2A, whose irreducibility and nonsquare discriminant give generic Galois group S3; the descendant ladder presents this same three-sheeted cover.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-020`

### [The rank-sensitive cubic suspension is triangularly left-right equivalent to (X,v,t) mapped b…](../units/JCG-D1EB696A.md)

`JCG-D1EB696A` · `assertion`

The rank-sensitive cubic suspension is triangularly left-right equivalent to (X,v,t) mapped by (t^{-1}K(tX),v,t); it preserves generic degree and the geometric Galois closure after adjoining transcendental variables.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-017`

### [The unique scalar-monomial quadratic shift lowering the cubic jet from rank seven…](../units/JCG-488CE7D0.md)

`JCG-488CE7D0` · `assertion`

The unique scalar-monomial quadratic shift lowering the cubic jet from rank seven to six is P2=-d^2 e_a, and its quartic error is detected by an exact 13-term functional outside the cubic homological image; the natural quadratic target cleanup also fails.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-011`

### [Top priorities are independent certificate reproduction, the full bounded-degree local ring a…](../units/JCG-AF04161C.md)

`JCG-AF04161C` · `assertion`

Top priorities are independent certificate reproduction, the full bounded-degree local ring and degree-growth interface, intrinsic triple-cover defect exclusion, boundary-complete rigidity, the minimum degree-three coordinate bound, improved descendant dimensions/tensor rank, the five-dimensional classification, and explaining the two-dimensional obstruction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-044`

### [What is the exact minimal square-zero Druzkowski pairing rank for the 19D cubic?](../units/JCG-72A99572.md)

`JCG-72A99572` · `assertion`

What is the exact minimal square-zero Druzkowski pairing rank for the 19D cubic?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-037`

### [What is the true smallest dimension of a cubic-homogeneous counterexample?](../units/JCG-DDAF375F.md)

`JCG-DDAF375F` · `assertion`

What is the true smallest dimension of a cubic-homogeneous counterexample?

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-036`

### [With the quartic kernel fixed at the principal point, the nilpotent-pencil tangent…](../units/JCG-154408D7.md)

`JCG-154408D7` · `assertion`

With the quartic kernel fixed at the principal point, the nilpotent-pencil tangent space has dimension 16 and sl2 type V0+V2+V4+V6; fixing the descended cubic kernel leaves only scalar rescaling, so the other 15 directions are exactly relative descended-cubic motion.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-033`

### [Within a zero-diagonal five-by-five sparse matrix ansatz with at most four nonzero…](../units/JCG-0B4E8503.md)

`JCG-0B4E8503` · `assertion`

Within a zero-diagonal five-by-five sparse matrix ansatz with at most four nonzero entries, no Keller map in the specified H_C family realizes the normalized collision.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-039`

### [Within the fixed 38-dimensional symmetric double, there is no proper nondegenerate invariant…](../units/JCG-FE704029.md)

`JCG-FE704029` · `assertion`

Within the fixed 38-dimensional symmetric double, there is no proper nondegenerate invariant linear slice surjecting onto the original variables; any smaller realization must change the realization mechanism rather than delete such a slice.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-025`

### [\(\mathrm{MC}(SU(79))\) is false.](../units/JCG-D60DDF45.md)

`JCG-D60DDF45` · `assertion`

\(\mathrm{MC}(SU(79))\) is false.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/additional-results-and-leads.tex#supp-note-05-015`

### [Cubic and quartic obstructions on the selected finite rank-six plane](../units/RMU-5D8E0003.md)

`RMU-5D8E0003` · `computational_result`

For the selected finite two-dimensional rank-six plane in the pinned Program 5 operation model, generic finite slope ratios admit no cubic lift. The exceptional rational ratio r=4 has effect rank 5 and augmented rank 6 and is intrinsically obstructed at cubic order. The two conjugate ratios r=4+4 sqrt(-3) and r=4-4 sqrt(-3) have effect and augmented rank 5, hence 17-dimensional affine fibres of cubic lifts, but the full algebraic order-four Kuranishi map has a nonzero intrinsic obstruction on each; at the first conjugate an exact coefficient-span certificate pairs to -1152, and field conjugation gives the second.

Hypotheses:

- The tensors, Schur chart, tangent splitting, selected finite plane, and slope parameter are exactly those at GitHub PR 1 head fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0.
- The order-three and order-four systems retain the complete tangent-kernel freedom implemented at that head.
- All calculations use exact arithmetic over Q or Q(sqrt(-3)) under SymPy 1.14.0.

Support:

- **program:** Exact exceptional-line cubic ranks and algebraic fourth-order Kuranishi computation at the pinned PR head. — <https://github.com/nmonson1/guide-to-jacobian-conjecture/tree/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex>
  - Does not establish: A classification beyond the selected finite plane.
  - Does not establish: A global compression theorem.
- **certificate:** Coefficient-span separator for the order-four Kuranishi image over Q(sqrt(-3)). — <https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/fd9e29f5c2ee24acdfee8e3165d7b9da0df859f0/research-tools/filtered_operation_complex/adapters/program5_rank_six_algebraic_fourth_order_kuranishi.py>
  - Does not establish: Any statement about untested planes or the full row-base fibre.

Limitations:

- The result does not classify the full 15-dimensional finite row-base fibre or the infinity fibre.
- It does not impose the separate compression functional or quotient by every source, target, and stable operation.
- It does not prove convergence, algebraization, or a global 19-to-18 noncompression theorem.

### [Degree-one obstruction reduces the compression core to three surfaces](../units/RMU-5D8E0002.md)

`RMU-5D8E0002` · `computational_result`

On the five-dimensional Program 5 core of RMU-5D8E0001, eleven exact rational degree-one dual sections of the moving degree-five cokernel sheaf have common zero locus exactly Z_0 union Z_1 union Z_2, where Z_0 is A=B=D=0; Z_1 is D=0, A=-3B, C^2+36C+50B-104BC=0; and Z_2 is A=3D, B=-D, C^2+36C+104CD-50D-84D^2=0. In each stratum E is free. Thus the degree-one secondary obstruction excludes every core point outside these three two-dimensional surfaces.

Hypotheses:

- The five-dimensional linear core and moving degree-five source-homological and quartic-null transfer matrices are those of RMU-5D8E0001.
- The eleven dual sections and their Groebner basis are computed exactly over the rational numbers.

Dependencies:

- `depends_on` [`RMU-5D8E0001`](../units/RMU-5D8E0001.md): The dual-section calculation is carried out on the five-dimensional core constructed there.

Support:

- **certificate:** Eleven exact rational dual sections, their evaluations, and an exact Groebner-basis case decomposition. — No public locator supplied.
  - Does not establish: Absence or presence of the intrinsic obstruction on the three residual surfaces.
  - Does not establish: A global 19-to-18 noncompression theorem.

Limitations:

- Vanishing of all eleven evaluations on Z_0, Z_1, or Z_2 does not prove that the secondary obstruction itself vanishes there.
- Degree-two dual sections on the three surfaces remain to be computed.
- The finite higher-order gauge compatibility required to identify the full exceptional fibre with the core remains open.

### [Intrinsic cubic obstruction for the selected rank-six plane](../units/RMU-5A110523.md)

`RMU-5A110523` · `computational_result`

For the selected Program 5 first-order plane theta_u=eta_0+xi_4 and theta_v=eta_1+4xi_0-24xi_1-4xi_4 in the pinned 115-dimensional source-field operation model, allow an arbitrary element of the 22-dimensional rank-six tangent kernel in each of the three quadratic coefficients v^2, uv, and u^2. The exact cubic compatibility system for these 66 parameters has 24 possibly nonzero compressed equations, effect rank 15, and augmented rank 16. An exact left-null witness w satisfies w^T E=0 and w^T b=-256/3. Hence no quadratic tangent-kernel choice lifts this selected plane through cubic parameter order in the local rank-at-most-six Schur chart.

Hypotheses:

- The tensors, weights, operation basis, base point P0=-d^2 e_a, tangent splitting, and Schur chart are those of RMU-5A110520 and PR 1 repaired head ca42e65fa644e3d06736bf8c0edfe3aa1d104a32.
- The first-order plane is the explicit two-dimensional section of RMU-5A110521 with theta_u=eta_0+xi_4 and theta_v=eta_1+4xi_0-24xi_1-4xi_4.
- Each quadratic coefficient may vary in the full 115-dimensional ambient operation space; all order-two solutions differ by the complete 22-dimensional tangent kernel used in the calculation.
- All ranks, projections, and the obstruction witness are computed exactly over the rational numbers.

Dependencies:

- `depends_on` [`RMU-5A110520`](../units/RMU-5A110520.md): The calculation uses the exact 20+2 tangent splitting and fixed rank-six Schur chart.
- `depends_on` [`RMU-5A110521`](../units/RMU-5A110521.md): The obstructed plane is the explicit second-order-compatible section constructed there.

Support:

- **program:** Pinned SymPy 1.14.0 cubic-lifting calculation with direct replay of all 66 tangent-effect columns. — <https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/ca42e65fa644e3d06736bf8c0edfe3aa1d104a32/research-tools/filtered_operation_complex/adapters/program5_rank_six_third_order_lift.py>
  - Does not establish: An obstruction for any other first-order plane.
  - Does not establish: Compatibility with the full operation-group quotient or stable changes.
  - Does not establish: A global compression theorem.
- **certificate:** Exact two-coordinate left-null witness for the inconsistent cubic lifting system. — <https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/ca42e65fa644e3d06736bf8c0edfe3aa1d104a32/research-tools/filtered_operation_complex/PROGRAM5_THIRD_ORDER_AUDIT.md>
  - Does not establish: An obstruction outside the pinned first-order plane.

Limitations:

- The result does not classify or obstruct other two-dimensional tangent planes.
- It does not impose the separate quartic equation Lambda_4=0; RMU-5A110520 independently gives Lambda_4=1 on the tested affine tangent plane.
- It does not prove an all-order obstruction, convergence, algebraization, a quotient by all source/target/stable operations, or a global 19-to-18 noncompression theorem.

### [Rank-six tangent bridge and quartic exclusion](../units/RMU-5A110520.md)

`RMU-5A110520` · `computational_result`

For the displayed Program 5 eleven-variable tensors Q and C at P0=-d^2 e_a, the space of weight-preserving quadratic source fields has dimension 115. The affine equations killing the a,d,q,h,k cubic rows have rank 95 and direction space K_row of dimension 20. The tangent space K_rank to the rank-at-most-six cubic-coordinate locus has dimension 22, and K_row is contained in K_rank. On the full affine plane P0+K_rank, the exact quartic functional Lambda_4(O_4(P)) is identically 1.

Hypotheses:

- Q, C, the eleven coordinates, weights, and Lambda_4 are exactly those in the pinned Program 5 extensions verifier at public-site PR 1 head 8e9cf4795842140c55da2a9891db60765ed09894.
- The rank-at-most-six locus is expressed in the local Schur-complement chart at P0=-d^2 e_a.
- All linear algebra and polynomial identities are over the rational numbers.

Support:

- **program:** Exact SymPy tangent-bridge computation and twelve-test package replay. — <https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/8e9cf4795842140c55da2a9891db60765ed09894/research-tools/filtered_operation_complex/PROGRAM5_TANGENT_BRIDGE.md>
  - Does not establish: Nonlinear integrability of K_rank.
  - Does not establish: The true operation-group quotient.
  - Does not establish: A compression of the fixed tensor.

Limitations:

- The affine tangent plane is not proved to lie in the nonlinear rank-at-most-six locus.
- The calculation is not a quotient by all source, target, and stable-presentation operations.
- It does not produce a 19-to-18 compression; Lambda_4=1 excludes the whole tested affine tangent plane from satisfying the displayed quartic equation.

### [Stratified transverse cone and tame source-coupled quartic obstruction](../units/RMU-5C6E0010.md)

`RMU-5C6E0010` · `computational_result`

At the fixed rank-six point in the Program 5 operation coordinates, the exact transverse equations decompose into the middle and deepest strata listed in the packet, including the displayed residual rational curve; the compression functional has constant value one on that residual family. After adjoining all 60 exact tame source directions and transporting divergence, the full weight-space and polarization calculation still evaluates the pinned quartic obstruction to 1728, a nonzero scalar. Therefore the fixed-lower-target tame source-coupled family does not solve the quartic lifting equation.

Hypotheses:

- The fixed tensor, rank-six point, weights, lower-target normalization and obstruction functional are exactly those in the Lane 6 packet.
- The 60 source directions are the complete encoded tame source space, not every stable source-target presentation.
- The rational residual family is interpreted only on its stated parameter open set.

Support:

- **proof:** Stratum-by-stratum exact elimination and source-coupled obstruction derivation. — `research-notes/lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/TAME_SOURCE_COUPLED_QUARTIC_OBSTRUCTION.md`
  - Does not establish: Stable presentation invariance or global nonexistence of an 18-variable realization.
- **program:** Exact stratum, residual-curve, divergence, weight-space and polarization replay suite. — `research-notes/lane6-transverse-source-obstruction-20260802-v1/tame-source-coupled/verify_residual_source_target_obstruction.py`
  - Does not establish: Completeness of the true stable operation group.

Limitations:

- It is not invariant under all source, target and stable-coordinate operations.
- It does not rule out an 18-variable realization in another presentation.

### [Uniform second-order rank-six section](../units/RMU-5A110521.md)

`RMU-5A110521` · `computational_result`

In the same Program 5 rank-six Schur chart, the tangent map has rank 93 and kernel dimension 22. Its quadratic Kuranishi projection has obstruction-coefficient rank six. Writing K_rank=K_row+span(eta_0,eta_1), the linear section s_0=4v, s_1=-24v, s_3=0, s_4=u-4v, s_5=0, with all other displayed row coordinates zero, makes all six quadratic obstruction equations vanish identically. Thus this two-dimensional tangent section, which projects isomorphically to span(eta_0,eta_1), admits rank-six lifts through second order.

Hypotheses:

- The hypotheses and exact tensors of RMU-5A110520.
- Rank at most six is imposed only through the displayed local Schur-complement equations.
- Second-order correction fields may use the full 115-dimensional ambient operation space.

Dependencies:

- `depends_on` [`RMU-5A110520`](../units/RMU-5A110520.md): The second-order calculation uses the 20+2 adapted tangent splitting.

Support:

- **program:** Exact construction and cokernel projection of the quadratic Schur-complement forcing. — <https://github.com/nmonson1/guide-to-jacobian-conjecture/blob/8e9cf4795842140c55da2a9891db60765ed09894/research-tools/filtered_operation_complex/adapters/program5_rank_six_second_order.py>
  - Does not establish: Third-order or all-order compatibility.
  - Does not establish: Compatibility with Lambda_4=0.
  - Does not establish: A true quotient-space deformation.

Limitations:

- This does not assert that the unadjusted eta_0,eta_1 complement itself is second-order compatible.
- It does not give an all-order formal arc, convergence, polynomial realization, or an operation-group quotient.
- It does not impose the quartic equation; RMU-5A110520 shows Lambda_4=1 on the entire ambient affine tangent plane.

### [Weight-zero polynomial gauge and five-dimensional compression core](../units/RMU-5D8E0001.md)

`RMU-5D8E0001` · `computational_result`

In the pinned Program 5 row-killing model, the relevant equivariant fibre is the 20-dimensional weight-zero summand. A reconstructed 13-dimensional weight-zero triangular family and the independent elementary shear b^2 e_h integrate to polynomial automorphisms, leaving a six-dimensional nontriangular quotient. Imposing the normal cubic Casimir condition gives a five-dimensional affine core with coordinates A=k_14, B=k_19, C=k_23, D=k_67, and E=k_85.

Hypotheses:

- The tensors, weights, row-killing equations, and triangular variable order x,y,a,h,k,d,z,b,c,q,s are those of the pinned source message.
- Only the weight-zero equivariant degree-five complex is used.

Support:

- **program:** Exact character decomposition and reconstruction of the 75-dimensional triangular family and its 13-dimensional weight-zero part. — No public locator supplied.
  - Does not establish: Finite higher-order gauge compatibility.
  - Does not establish: A complete nonlinear operation-group quotient.

Limitations:

- A finite conjugation theorem transporting every higher-order representative to the displayed core has not been proved.
- The remaining directions are not asserted to represent the complete quotient by all source, target, or stable operations.

### [For the fixed tensor \(H\), the minimum length of a full-rank square-zero…](../units/RMU-01949A68.md)

`RMU-01949A68` · `corollary`

For the fixed tensor \(H\), the minimum length of a full-rank square-zero
pairing satisfies
\[
52\le N_{\mathrm{pair}}\le110.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#cor:pair-interval`](../../proof-sources/05-homogeneous-descendants/main.md#label-cor-pair-interval)

### [Isotropic terminal vector](../units/RMU-089C892F.md)

`RMU-089C892F` · `lemma`

Let $A$ have Jordan type $(m,1)$, let
$\ker A=\langle v_1,v_2\rangle$, and suppose
$\operatorname{im}A^{m-1}=\langle v_2\rangle$.  Let $L=L^T$ and
\[
N=\begin{pmatrix}A&0\\L&A^T\end{pmatrix}.
\]
Define the symmetric form
\[
\beta(u,v)=u^TLv\qquad(u,v\in\ker A).
\]
If $\beta$ has rank one with radical $\langle v_2\rangle$, if
$N^{2m-2}\ne0$, and if $\beta(v_2,v_2)=0$, then $N$ has Jordan type
$(2m-1,2,1)$.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#lem:self-dual-extension`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-lem-self-dual-extension)

### [The map \(\widetilde K\) is polynomially stably left--right equivalent to \(K\).](../units/RMU-EB6A96DB.md)

`RMU-EB6A96DB` · `lemma`

The map \(\widetilde K\) is polynomially stably left--right equivalent to
\(K\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#lem:stable-identity`](../../proof-sources/05-homogeneous-descendants/main.md#label-lem-stable-identity)

### [A full-rank square-zero pairing is stably right-equivalent](../units/RMU-A93DB097.md)

`RMU-A93DB097` · `proposition`

Suppose
\[
H(z)=B(Dz)^{*3},\qquad BD=0,
\]
where $B:W\to V$ is surjective and $D:V\to W$ is injective.  Put $A=DB$ and
$F_A(w)=w+(Aw)^{*3}$.  Choose a right inverse $C$ of $B$ and write
$W=C(V)\oplus E$, where $E=\ker B$.  Set
\[
\rho(z)=(Dz)^{*3}-CH(z)\in E.
\]
In the coordinates $w=Cz+\eta$, one has
\[
F_A(z,\eta)=\bigl(G(z),\eta+\rho(z)\bigr),
\qquad G=I+H.
\]
Precomposition by $(z,\eta)\mapsto(z,\eta-\rho(z))$ therefore changes $F_A$
into $G\times\id_E$.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md)

### [A positive-dimensional obstructed compression family](../units/RMU-ED4B653B.md)

`RMU-ED4B653B` · `proposition`

For every $\sigma\in\Sigma_{-2}$, the cubic jet
$C+[Q,P_\sigma]$ is supported only in the six output coordinates
$x,y,z,b,c,s$, and therefore has coordinate-span rank at most six.  Nevertheless,
\[
\Lambda_4\bigl(\mathcal O_4(P_\sigma)\bigr)=1.
\]
Hence no cubic source correction removes the quartic term anywhere in this
$12$-parameter formal family.  Excluding the two monomials involving $s$
gives a $10$-parameter family of actual triangular polynomial automorphisms.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#prop:compression-family`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-prop-compression-family)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#prop:compression-family`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-prop-compression-family)

### [A two-point obstruction to strong nilpotence](../units/RMU-63DC07DA.md)

`RMU-63DC07DA` · `proposition`

Although $A(Z)$ is nilpotent for every $Z$, the family is not strongly
nilpotent and is not simultaneously strictly triangularizable.  Indeed,
\[
A(e_d)A(e_t)|_{\langle e_{w_3},e_{w_6}\rangle}
 =\begin{pmatrix}-1&1\\2&-2\end{pmatrix},
\]
and all other entries of the product vanish.  Hence
\[
\chi_{A(e_d)A(e_t)}(\lambda)=\lambda^{18}(\lambda+3).
\]

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#prop:not-strongly-nilpotent`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-prop-not-strongly-nilpotent)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#prop:not-strongly-nilpotent`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-prop-not-strongly-nilpotent)

### [Every vector-Waring decomposition of \(H\) has length at least 52.](../units/RMU-F89ADC34.md)

`RMU-F89ADC34` · `proposition`

Every vector-Waring decomposition of \(H\) has length at least 52.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:waring52`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-waring52)

### [Exact regularity criterion](../units/RMU-9734A9D7.md)

`RMU-9734A9D7` · `proposition`

On \(\det T\ne0\), the pencil \(M(s,t)\) has Jordan type \((5)\) at every
point of \(\PP^1\) if and only if \(a_7\ne0\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#prop:full-kernel-regularity`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-prop-full-kernel-regularity)

### [Finite-field sample audit](../units/RMU-E05ECB4A.md)

`RMU-E05ECB4A` · `proposition`

An exhaustive \(\mathbf F_{13}\)-calculation finds thirteen rational points
of this normalized collision system.  Together with the previously checked
six points over \(\mathbf F_7\) and eleven over \(\mathbf F_{11}\), all
thirty sampled points have nonzero first-normal obstruction.  This is exact
finite-field evidence, not a proof that the obstruction section is nowhere
zero on the characteristic-zero collision curve.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#prop:full-kernel-finite-field-samples`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-prop-full-kernel-finite-field-samples)

### [For every cubic vector field \(P_3\), \[ \Lambda_4([Q,P_3])=0, \qquad \Lambda_4(D_4)=1. \] Th…](../units/RMU-B2D3B17A.md)

`RMU-B2D3B17A` · `proposition`

For every cubic vector field \(P_3\),
\[
\Lambda_4([Q,P_3])=0,
\qquad
\Lambda_4(D_4)=1.
\]
Thus \(D_4\notin\operatorname{im}[Q,-]\).

Moreover, among the 605 shifts
\[
P_2=\lambda m e_j,
\]
where \(m\) is a quadratic monomial not involving \(X_j\), the shift
\(-d^2e_a\) is the unique one that lowers the cubic span to six.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:compression`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-compression)

### [Large row-killing families](../units/RMU-CEE867BF.md)

`RMU-CEE867BF` · `proposition`

The affine space of quadratic source fields has dimension \(726\).
There is a \(109\)-dimensional affine family on which five prescribed cubic
output rows vanish and the remaining coordinate span has rank at most six.
The quartic obstruction functional is identically one on this family.
Inside it, a specified \(75\)-dimensional family consists of triangular
polynomial automorphisms.  The full rank-six tangent space at the base point
has dimension \(129\), leaving a \(20\)-dimensional quotient by the
row-killing directions; a nonempty Zariski-open subset of that quotient is
obstructed at second order.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#prop:row-killing-families`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-prop-row-killing-families)

### [Over \(\mathbb Q(Z)\), the matrix \(A\) has Jordan type \((18,1)\).](../units/RMU-DF26626A.md)

`RMU-DF26626A` · `proposition`

Over \(\mathbb Q(Z)\), the matrix \(A\) has Jordan type \((18,1)\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:jordan19`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-jordan19)

### [Rees presentation of the rank-sensitive suspension](../units/RMU-894DE5DF.md)

`RMU-894DE5DF` · `proposition`

Let $K=X+Q+C$, let $C=Bq$, and let
\[
G(X,w,t)=\bigl(X+tQ(X)+t^2Bw,\;w-q(X),\;t\bigr).
\]
Define triangular automorphisms
\[
S(X,v,t)=(X,v+q(X),t),\qquad
T(Y,v,t)=(Y-t^2Bv,v,t).
\]
Then
\[
T\circ G\circ S=(K_t\times\id)(X,v,t),
\qquad
K_t(X)=X+tQ(X)+t^2C(X)=t^{-1}K(tX).
\]
Consequently, after inverting $t$, the function-field extension induced by $G$
is obtained from that induced by $K$ by adjoining independent transcendental
variables.  In particular, generic degree and geometric monodromy are
preserved.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#prop:rees-presentation`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-prop-rees-presentation)

### [The generic Jordan type of \(\operatorname{Hess}\mathcal Q\) is \[ (35,2,1). \]](../units/RMU-B8FB65CD.md)

`RMU-B8FB65CD` · `proposition`

The generic Jordan type of \(\operatorname{Hess}\mathcal Q\) is
\[
(35,2,1).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:hessian-jordan`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-hessian-jordan)

### [The map \(F_A\colon\A^{110}\to\A^{110}\) is a noninjective Keller map. It is Gorni--Zampieri…](../units/RMU-948C51DB.md)

`RMU-948C51DB` · `proposition`

The map \(F_A\colon\A^{110}\to\A^{110}\) is a noninjective Keller map.
It is Gorni--Zampieri paired with \(G=I+H\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:pair110`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-pair110)

### [The symmetric double is a stable presentation](../units/RMU-D1D912B7.md)

`RMU-D1D912B7` · `proposition`

Let $F=X+H$ be Keller and put
\[
\Phi_F(x,y)=\bigl(F(x),JF(x)^Ty\bigr).
\]
Then the polynomial automorphism
\[
S_F(x,y)=\bigl(x,JF(x)^Ty\bigr)
\]
satisfies
\[
\Phi_F=(F\times\id)\circ S_F.
\]
Hence the symmetric double, and therefore its linear gradient twist, induces
the same function-field extension as $F$ after adjoining $\dim F$ independent
variables.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md)

### [Use the quadratic output corrections generated by the four outputs \(d,q,h,k\), which…](../units/RMU-A7E40CD2.md)

`RMU-A7E40CD2` · `proposition`

Use the quadratic output corrections generated by the four outputs
\(d,q,h,k\), which have degree at most two after the conjugacy.  Their ten
quadratic products create a ten-dimensional quartic image.
The \(z\)- and \(c\)-components of \(D_4\) lie outside this image.  The
\(a\)-component has the unique preimage \(-Y_d^2\), but applying it restores
cubic coordinate-span rank seven.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#prop:target-cleanup`](../../proof-sources/05-homogeneous-descendants/main.md#label-prop-target-cleanup)

### [Equivariant compression obstruction](../units/RMU-C8DF04DB.md)

`RMU-C8DF04DB` · `theorem`

Let \(V\) be the space of quadratic source fields that preserve the weights;
it has dimension \(115\).  The locus in \(V\) killing five specified cubic
output rows contains a natural affine slice of dimension \(20\).  Each point
on that slice has at most six linearly independent cubic coordinate
functions.  The same functional, supported on \(13\) terms, takes the value
\(1\) on its quartic obstruction.  Thus no point lifts through quartic order
in the stated equivariant conjugacy model.  The original \(605\)-shift
statement is a sparse corollary.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex#thm:intro-obstruction`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-intro-obstruction)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#thm:intro-obstruction`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-intro-obstruction)

### [Exact inverse-ray family](../units/RMU-3A571053.md)

`RMU-3A571053` · `theorem`

For all $\alpha,\beta$,
\[
\bigl(\widehat G^{-1}_0(sY_{\alpha,\beta})\bigr)_x
 =\frac{(1-2\alpha s^4+2\beta s^6)^{-1/2}-1}{s^3},
\]
where the square root is the branch with constant term $1$.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#thm:inverse-ray-family`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-thm-inverse-ray-family)

### [For every \(r\ge2\), \[ \partial_{u_1}\Delta^{2r-3} \bigl(\mathcal Q^{2r-2}\bigr)(\bar W) = \…](../units/RMU-8CCF21A4.md)

`RMU-8CCF21A4` · `theorem`

For every \(r\ge2\),
\[
\partial_{u_1}\Delta^{2r-3}
\bigl(\mathcal Q^{2r-2}\bigr)(\bar W)
=
\frac{(2r-3)!(2r-2)!}{16}\binom{2r}{r}\ne0.
\]
In particular,
\[
\partial_{u_1}\Delta(\mathcal Q^2)(\bar W)=\frac34.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#thm:laplacian`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-laplacian)

### [Nonvanishing at every Laplacian order](../units/RMU-E643F9B9.md)

`RMU-E643F9B9` · `theorem`

For every $m\ge1$ and every positive rational $\alpha,\beta$,
\[
\partial_{u_1}\Delta^m\bigl(\mathcal Q^{m+1}\bigr)
   (W_{\alpha,\beta})
 =2^{m-1}m!(m+1)!\,c_{m+3}(\alpha,\beta)>0.
\]
Thus the same quartic violates the eventual-vanishing condition at every
order, not merely along an infinite parity class.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/structural-extensions.tex#thm:all-order-laplacian`](../../proof-sources/05-homogeneous-descendants/appendices/structural-extensions.md#label-thm-all-order-laplacian)

### [Rank-sensitive suspension](../units/RMU-062BD85C.md)

`RMU-062BD85C` · `theorem`

Let \(K=X+Q+C\colon\A^n\to\A^n\) be Keller over a characteristic-zero
field, with \(Q\) quadratic homogeneous and \(C\) cubic homogeneous.  Put
\[
r=\dim\operatorname{span}\set{C_1,\ldots,C_n}.
\]
Then \(K\) admits a cubic-homogeneous Keller suspension in dimension
\(n+r+1\).  Every collision of \(K\) lifts explicitly to a collision of the
suspension.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex#thm:intro-suspension`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-intro-suspension)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#thm:intro-suspension`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-intro-suspension)

### [Split collision incidence with intrinsic marking-open condition](../units/RMU-5C7E0011.md)

`RMU-5C7E0011` · `theorem`

For the Lane 7 homogeneous collision chart, every genuine collision vector pair u,v with u!=0 is automatically linearly independent. The marking equations admit the polynomial split and determinant-boundary matrix factorization of RMU-5C7E0010, reducing on D(d) to M(a)u=0 and v=-d^(-1)C(a)A(a)u with rank(Theta)=5+rank(M). If w=CAu, the genuine projective marking incidence is the union of the opens eta_ij=u_i w_j-u_j w_i!=0 inside P(ker M). Thus a component calculation on V(I_5(M)) alone must retain this Pluecker-open condition or prove it is generically nonempty on every component used.

Hypotheses:

- F=X+H is cubic homogeneous and Keller, and u!=0 satisfies F(v+u)=F(v).
- The fifteen quintics, normalization a_7=1, determinant d and matrices are exactly those in the split-incidence packet.
- The residual-matrix formulas are restricted to D(d).

Support:

- **proof:** Nilpotence proof of collision-vector independence and exact Pluecker transport through the split incidence. — [`manuscripts/05-homogeneous-descendants/appendices/dimension-five.tex#lem:n5-collision-independent`](../../proof-sources/05-homogeneous-descendants/appendices/dimension-five.md#label-lem-n5-collision-independent)
  - Does not establish: Nonemptiness of the marking open on every determinantal component.
- **proof:** Block elimination, exact matrix factorization and projective marking-open reconstruction. — `research-notes/lane7-split-incidence-20260802-v1/lane7-split-incidence-theorem.md`
  - Does not establish: The unresolved saturation, grade and componentwise obstruction calculations.
- **program:** Standalone reconstruction and exact matrix identity/determinant checkers. — `research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_theorem.py`
  - Does not establish: The conventional collision-independence proof or unresolved global geometry.

Limitations:

- It does not prove I_4(M):d^infinity=(1), grade six, absolute component decomposition or a global first-normal obstruction.
- It does not prove that every determinantal component meets the genuine marking open.

### [The fixed 19-variable tensor](../units/RMU-F2DFB848.md)

`RMU-F2DFB848` · `theorem`

For the tensor \(H\) of \cref{sec:fixed-tensor}:
\begin{enumerate}[label=(\roman*)]
\item \(I+H\) is a noninjective cubic-homogeneous Keller map in 19 variables;
\item the generic Jordan type of \(JH\) is \((18,1)\);
\item the associated 38-variable quartic \(\mathcal Q\) is Hessian nilpotent,
has generic Hessian type \((35,2,1)\), and violates Zhao's eventual
vanishing condition at every order; and
\item the vector-Waring length of \(H\) is at least 52, while \(H\) has a
full-rank square-zero pairing of length 110.
\end{enumerate}

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex#thm:intro-fixed`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-intro-fixed)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#thm:intro-fixed`](../../proof-sources/05-homogeneous-descendants/main.md#label-thm-intro-fixed)

### [Transverse no-lift](../units/RMU-25A1F543.md)

`RMU-25A1F543` · `theorem`

In this six-dimensional transversal, the second-order rank-six cone is the
reduced scheme
\[
V(u_0u_5,u_2u_3,u_3u_5)
=
V(u_3,u_5)\cup V(u_0,u_3)\cup V(u_2,u_5).
\]
There is an explicit polynomial family \(P(u)\) such that
\[
\operatorname{rank}(C+[Q,P(u)])\le6
\quad\Longleftrightarrow\quad
u_0u_5=u_2u_3=u_3u_5=0.
\]
Every point of the cone is therefore integrated to an exact cubic jet of
coordinate span six.  Nevertheless no member lifts through quartic order.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.tex#thm:transverse-cone-no-lift`](../../proof-sources/05-homogeneous-descendants/appendices/full-kernel-and-compression-progress.md#label-thm-transverse-cone-no-lift)

## Open frontier

### [Can one improve the rank-sensitive complexity \[ \dim K+\dim\operatorname{span}\set{(K_3)_i}…](../units/RMU-EC855EF2.md)

`RMU-EC855EF2` · `question`

Can one improve the rank-sensitive complexity
\[
\dim K+\dim\operatorname{span}\set{(K_3)_i}
\]
by choosing a different degree-at-most-three stable representative?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex`](../../proof-sources/05-homogeneous-descendants/main.md)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex`](../../proof-sources/05-homogeneous-descendants/main.md)

### [Can the \(\mathfrak{sl}_{18}\) collision-monolith structure recorded in the companion researc…](../units/RMU-3A916178.md)

`RMU-3A916178` · `question`

Can the \(\mathfrak{sl}_{18}\) collision-monolith structure recorded in the
companion research register be used to derive the Jordan types
\((18,1)\) and \((35,2,1)\) without coefficient calculation?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex`](../../proof-sources/05-homogeneous-descendants/main.md)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex`](../../proof-sources/05-homogeneous-descendants/main.md)

### [Construct a different-filtered source-flow or transferred L-infinity model that independently…](../units/JCG-D9E57688.md)

`JCG-D9E57688` · `question`

Construct a different-filtered source-flow or transferred L-infinity model that independently reproduces the bounded-degree Kuranishi equations and the length-584 Artin algebra.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`

### [For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree…](../units/JCG-4451EE05.md)

`JCG-4451EE05` · `question`

For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree delta_LR(xi)=min{deg H : H is polynomially left-right equivalent to xi} from intrinsic conductor, ramification, valuation, or nonproperness data. A bound of at least seven for every nontrivial generic-degree-three boundary class would supply the missing degree-cost bridge from cubic-cover classification to low-degree exclusion.

### [Intrinsic tensor and pairing ranks](../units/RMU-A5A4CEF5.md)

`RMU-A5A4CEF5` · `question`

What are the exact vector-Waring length, pairing rank, and square-zero
realization rank of the fixed \(19\)-variable cubic tensor?  In particular,
can the present vector-Waring interval between \(52\) and \(110\) be closed
without committing to one reduction algorithm?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex#q:intrinsic-ranks`](../../proof-sources/05-homogeneous-descendants/main.md#label-q-intrinsic-ranks)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#q:intrinsic-ranks`](../../proof-sources/05-homogeneous-descendants/main.md#label-q-intrinsic-ranks)

### [Minimum homogeneous dimension](../units/RMU-84BB8F66.md)

`RMU-84BB8F66` · `question`

What is the minimum dimension of a cubic-homogeneous counterexample?  The
fixed \(19\)-variable construction gives an upper bound, while known
low-dimensional classifications and the five-dimensional restrictions
collected in the companion research register leave a substantial gap.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/05-homogeneous-descendants/main.tex#q:min-homogeneous-dimension`](../../proof-sources/05-homogeneous-descendants/main.md#label-q-min-homogeneous-dimension)
  - Full source and surrounding context: [`manuscripts/05-homogeneous-descendants/main.tex#q:min-homogeneous-dimension`](../../proof-sources/05-homogeneous-descendants/main.md#label-q-min-homogeneous-dimension)

### [Prove that the first-normal obstruction covariant Omega is nowhere zero on the…](../units/JCG-87A24226.md)

`JCG-87A24226` · `question`

Prove that the first-normal obstruction covariant Omega is nowhere zero on the full-kernel regular collision-line curve, thereby excluding the entire regular Jordan-type-(5) line stratum rather than one residue disk.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/dimension-five.tex#q:n5-global-first-normal`

### [Prove the extension statement E(N): no sl_r or sp_r prolongation extension of…](../units/JCG-35542BB2.md)

`JCG-35542BB2` · `question`

Prove the extension statement E(N): no sl_r or sp_r prolongation extension of total dimension at most N satisfies the Engel, irreducibility, collision, and minimal-monolith conditions; E(16) gives a lower bound 17 and E(18) gives 19.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/05-homogeneous-descendants/appendices/monolith-prolongation.tex#q:prolongation-extension-theorem`
