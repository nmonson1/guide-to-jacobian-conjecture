# Local Rigidity and Deformation Algebra

Formal right-triviality, weighted residual directions, and a finite local Artin algebra turn a global equivalence problem into exact local algebra.

This is a generated progress view of retained mathematics. Workflow labels and private source locators are intentionally omitted.

<!-- noncanonical-overlay -->

## Setup and research posture

This program studies the degree-bounded, affine-quotiented deformation germ
of the normalized degree-seven map. Unrestricted formal right-triviality and
bounded affine rigidity are different statements: the formal source change
may have unbounded degree, while the bounded slice retains a large
nonreduced intersection.

The useful objects are the torus-weighted Kuranishi ideal, its finite Artin
algebra, an inverse system, and a border presentation. Separate constructions
of the equations currently agree only through a finite parameter order. The
degree-eight problem is also separate because explicit source and target
shears already give positive-dimensional families.

## Strategy and payoff

The finite computational priority is an independent reconstruction of the
last Kuranishi layers using an evolving quotient basis. Whenever a new
generator enters, update the standard monomials before computing the next
rank. Full-rank modular minors and exact rational nullspaces prove different
rank directions and must be recorded separately.

The conceptual priority is an all-order comparison between the direct
determinant complex and the marked-root source-flow/Rees complex. A useful
comparison maps generators, gauge, differentials, and obstruction spaces;
matching Hilbert numbers alone is not enough.

Independent CAS work should rederive the equations it checks. Re-entering a
certificate in another program is valuable consistency evidence but is not
an independent derivation of the deformation problem.

## Connections

The source-flow model connects to the marked-root incidence program. The
question of when stable moduli first appear connects the rigid degree-seven
germ to degree-eight shear components and to the stable-moduli program. The
finite algebra also offers a clean testbed for repository-wide computation
contracts: coefficient domains, bases, rank directions, and limitations can
all be made exact.

## Current priorities and research freedom

The current attention order is:

1. finish a second exact reconstruction of the terminal layers;
2. extend or prove the source-flow/determinant comparison;
3. obtain a genuinely independent derivation and reproduction of the core
   rigidity system; and
4. formulate degree-eight orbit saturation using all known shear components
   and the complete residual sector.

These are research coordinates rather than mandatory capsules. Preserve any
unexpected generator, surviving weight, component, or contradiction as a
first-class result.

## Graveyard and scope fences

- Formal right-triviality does not settle a degree-bounded quotient.
- Tangent dimensions do not determine reduced components.
- A restricted slice cannot control arcs that bend into omitted directions.
- Good-prime ranks do not give both characteristic-zero inequalities.
- A border presentation obtained after the length theorem is not an
  independent upper bound without direct membership certificates.
- Degree-eight rigidity cannot mean an isolated point because explicit
  shear families exist.

## Definitions and constructions

### [The slice](../units/RMU-2B8185BE.md)

`RMU-2B8185BE` · `definition`

For a perturbation \(H-G\), set the coefficients of the following eleven
component--monomial pairs to zero:
\[
\begin{array}{c|l}
\text{component}&\text{monomials}\\ \hline
1&y^2,\ xz,\ xy,\ x^2,\ x^3\\
2&y^2,\ xz,\ xy,\ x^2\\
3&y^2,\ xy.
\end{array}
\]
Let \(A_{\mathrm{sl}}\) be the resulting 337-dimensional affine subspace and
put
\[
S=K_{3,7}\cap A_{\mathrm{sl}}.
\]

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/main.tex#def:slice`](../../proof-sources/03-local-rigidity/main.md#label-def-slice)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#def:slice`](../../proof-sources/03-local-rigidity/main.md#label-def-slice)

## Retained results

### [A local standard-basis computation produces pure powers u0^2,u1^4,u2^5,u3^2,u4^5,u5^4,u6^6,u7…](../units/JCG-7A91920F.md)

`JCG-7A91920F` · `assertion`

A local standard-basis computation produces pure powers u0^2,u1^4,u2^5,u3^2,u4^5,u5^4,u6^6,u7^3,u8^3,u9^2 in an initial ideal, making it m-primary and yielding set-theoretic formal/analytic isolation of the degree-seven transverse germ.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-003`

### [A six-jet initial monomial quotient at degree seven has length 656 and…](../units/JCG-D4C5AD93.md)

`JCG-D4C5AD93` · `assertion`

A six-jet initial monomial quotient at degree seven has length 656 and Hilbert function (1,10,44,108,157,145,86,53,36,16), with matching initial data at two primes.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-016`

### [A torus-stable 337-dimensional slice has ten tangent parameters of weights (-1,2,-3,-2,-1,0,1…](../units/JCG-A6010D1B.md)

`JCG-A6010D1B` · `assertion`

A torus-stable 337-dimensional slice has ten tangent parameters of weights (-1,2,-3,-2,-1,0,1,1,2,3); exact positive, negative, and fixed-weight obstruction certificates plus a torus-nullcone lemma show that its reduced completed local ring is C. Thus G is reduced-affinely rigid in K_{3,7}, though the local ring is a nonreduced Artin thickening.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#sec:kuranishi`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#prop:pure-weight`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#thm:reduced`

### [Assuming the current reduced-rigidity and stable-classification theorems, the normalized degr…](../units/JCG-D1155E99.md)

`JCG-D1155E99` · `assertion`

Assuming the current reduced-rigidity and stable-classification theorems, the normalized degree-seven counterexample G is reduced-isolated in its degree-at-most-seven normalized affine slice but is the special fiber of an algebraic degree-eleven family whose general fibers vary in stable left-right class. Thus the pointed stable-moduli onset through G lies between 8 and 11, and equals 11 within the cubic-frame locus.

### [At degree eight, the determinant linearization has kernel dimension 44, hence 33…](../units/JCG-891B0275.md)

`JCG-891B0275` · `assertion`

At degree eight, the determinant linearization has kernel dimension 44, hence 33 directions after the same eleven-dimensional affine orbit, and at least five explicit coordinate families occur (three source quadratic z-shears and two target shears).

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-004`

### [At each of the three stated good primes, all 234 torus-weight blocks…](../units/JCG-5D1C1BA6.md)

`JCG-5D1C1BA6` · `assertion`

At each of the three stated good primes, all 234 torus-weight blocks of the Koszul homology agree and give Betti vector (1,36,354,1565,3937,6216,6432,4403,1942,506,60).

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/border-basis-and-betti.tex#thm:three-prime-betti`

### [At the degree-eight base point, after quotienting the affine orbit and the…](../units/JCG-24C82405.md)

`JCG-24C82405` · `assertion`

At the degree-eight base point, after quotienting the affine orbit and the known quadratic source-shear and target-shear components, no additional formal branch has a first nonzero normal term transverse to those two components.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/degree-eight.tex#thm:degree-eight-transverse`

### [At two primes, the order-eight quotient contribution is predicted to have dimension…](../units/JCG-6B717AA1.md)

`JCG-6B717AA1` · `assertion`

At two primes, the order-eight quotient contribution is predicted to have dimension three with character z^-1+1+z, suggesting cumulative truncated length 584; over Q only 581 <= L8 <= 584 was established in the conversation.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-017`

### [Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic…](../units/JCG-ECF242AB.md)

`JCG-ECF242AB` · `assertion`

Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic f gives a three-parameter source-shear family, and F_f and F_g are affinely equivalent exactly when g(x,y)=tau^2 f(tau x,tau^-1 y) within this family.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/degree-eight.tex#prop:quadratic-shears`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/degree-eight.tex#thm:shear-classification`

### [Every formal polynomial Keller deformation of the fixed map is right-trivial as…](../units/JCG-30FC31CC.md)

`JCG-30FC31CC` · `assertion`

Every formal polynomial Keller deformation of the fixed map is right-trivial as F composed with a formal source automorphism; bounded-degree obstructions come from the degree filtration, not unrestricted formal deformation theory.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#prop:formal-orbit`

### [Exact filtered computations for degree bounds E=2,...,7 give tangent/kernel/affine-orbit dime…](../units/JCG-AF5BE0A3.md)

`JCG-AF5BE0A3` · `assertion`

Exact filtered computations for degree bounds E=2,...,7 give tangent/kernel/affine-orbit dimensions; at E=7 the ambient normalized dimension is 348, determinant rank 327, kernel 21, affine image 11, quotient tangent 10, and quadratic obstruction rank 11.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-006`

### [For any Keller map F, the first-order kernel of the determinant equation…](../units/JCG-41FFDBEF.md)

`JCG-41FFDBEF` · `assertion`

For any Keller map F, the first-order kernel of the determinant equation consists of JF times divergence-free vector fields; with the correct output filtration the computed first-order quotient vanishes, source reparametrizations are formally trivial, and the calculation stabilizes in the tested range.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-010`

### [For the degree-eight local Kuranishi problem, the residual 28-dimensional slice reduces to…](../units/JCG-D3F76EBC.md)

`JCG-D3F76EBC` · `assertion`

For the degree-eight local Kuranishi problem, the residual 28-dimensional slice reduces to weights -2 and -1; weight -2 is eliminated over Q, while weight -1 survives to fourth order and has only modular death evidence at order six.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/degree-eight.tex#thm:degree-eight-transverse`

### [For the normalized degree-seven counterexample, an independently constructed marked-root weig…](../units/JCG-E4FFD82B.md)

`JCG-E4FFD82B` · `assertion`

For the normalized degree-seven counterexample, an independently constructed marked-root weighted-divergence/Rees complex agrees over Q with the direct determinant complex through parameter order four, giving Hilbert prefix (1,10,44,108,157) and filtered generator counts 11,13,11.

Support:

- **source assertion:** theorem and exact-computation proof — [`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex#thm:source-flow-reconstruction`](../../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md#label-thm-source-flow-reconstruction)

### [For the normalized degree-seven map, the exact determinant linearization has 348 variables,…](../units/JCG-7F0D894D.md)

`JCG-7F0D894D` · `assertion`

For the normalized degree-seven map, the exact determinant linearization has 348 variables, rank 327, kernel dimension 21; the normalized affine orbit has dimension 11, leaving ten transverse tangent directions.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-001`

### [In a degree-seven transverse deformation tower, the ten-dimensional tangent space reduces to…](../units/JCG-E5D7C792.md)

`JCG-E5D7C792` · `assertion`

In a degree-seven transverse deformation tower, the ten-dimensional tangent space reduces to a five-space at second order and a two-plane at third order; all nonzero first-order transverse directions are obstructed by order at most five.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-002`

### [In the marked-root coordinates (A,B,s), with delta=1-Bs+3As^2, the source volume form is…](../units/JCG-2FCDA5F0.md)

`JCG-2FCDA5F0` · `assertion`

In the marked-root coordinates (A,B,s), with delta=1-Bs+3As^2, the source volume form is -delta dA dB ds and the volume-preserving vector fields satisfy partial_A(delta a)+partial_B(delta b)+partial_s(delta c)=0.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/root-coordinate-source-flow.tex#prop:root-coordinate-divergence`

### [It remains open to certify the intermediate rational Betti numbers beta_2 through…](../units/JCG-CB4F1C73.md)

`JCG-CB4F1C73` · `assertion`

It remains open to certify the intermediate rational Betti numbers beta_2 through beta_9 of the length-584 Artin algebra and to obtain a genuinely independent second-system reproduction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-014`

### [Natural next problems include classification of generic-degree-three examples, bounded-degree…](../units/JCG-44729E0B.md)

`JCG-44729E0B` · `assertion`

Natural next problems include classification of generic-degree-three examples, bounded-degree local moduli, minimum coordinate degree, nonproperness divisors, optimized cubic reduction, the plane case, and possible universality of the marked-root construction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-038`

### [On the five explicit degree-eight coordinate directions, the corrected quadratic/cubic equati…](../units/JCG-0632B2B1.md)

`JCG-0632B2B1` · `assertion`

On the five explicit degree-eight coordinate directions, the corrected quadratic/cubic equations lift precisely along the pure source-shear or pure target-shear sectors; a residual four-dimensional tangent survives to order three in a larger complement, and the full degree-four modular calculation remains exploratory.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-005`

### [Recover the six decisive obstruction components canonically from the residue pole filtration…](../units/JCG-5EA4BAEE.md)

`JCG-5EA4BAEE` · `assertion`

Recover the six decisive obstruction components canonically from the residue pole filtration or the determinant of cohomology.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-045`

### [The completed local Artin algebra has length 584, nilpotency m^9=0 with m^8…](../units/JCG-DD13AC0E.md)

`JCG-DD13AC0E` · `assertion`

The completed local Artin algebra has length 584, nilpotency m^9=0 with m^8 nonzero, and Hilbert function (1,10,44,108,157,145,86,30,3).

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#thm:main`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#cor:hilbert`

### [The completed local algebra at the affine-slice point has an exact characteristic-zero…](../units/JCG-F4C59FA0.md)

`JCG-F4C59FA0` · `assertion`

The completed local algebra at the affine-slice point has an exact characteristic-zero border presentation with 584 standard monomials, 2654 border relations, and ten commuting 584 by 584 rational multiplication matrices containing 24402 nonzero entries; the border ideal equals the Kuranishi ideal.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/border-basis-and-betti.tex#thm:exact-border-basis`

### [The earlier inference from a restricted five-dimensional slice to isolation in the…](../units/JCG-02C45EB8.md)

`JCG-02C45EB8` · `assertion`

The earlier inference from a restricted five-dimensional slice to isolation in the full transverse space is invalid because higher-order arcs can bend out of the slice.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-015`

### [The exact rational Hilbert-Samuel data through order six are (1,10,44,108,157,145,86), with c…](../units/JCG-D1903700.md)

`JCG-D1903700` · `assertion`

The exact rational Hilbert-Samuel data through order six are (1,10,44,108,157,145,86), with cumulative dimensions (1,11,55,163,320,465,551); exact order seven adds h7=30 and gives cumulative length 581 through order seven.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-009`

### [The family is formally conjugate coefficient by coefficient while no conjugacy of…](../units/JCG-B3286203.md)

`JCG-B3286203` · `assertion`

The family is formally conjugate coefficient by coefficient while no conjugacy of uniformly bounded polynomial degree follows.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-011`

### [The full normalized affine stabilizer of G is exactly the torus diag(tau^-1,tau,tau^2),…](../units/JCG-5284E9D8.md)

`JCG-5284E9D8` · `assertion`

The full normalized affine stabilizer of G is exactly the torus diag(tau^-1,tau,tau^2), not merely its identity component.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-007`

### [The highest-leverage program is exact reconstruction of the five Belyi maps followed…](../units/JCG-48D5E369.md)

`JCG-48D5E369` · `assertion`

The highest-leverage program is exact reconstruction of the five Belyi maps followed by weight-filtered tests against the two surviving Newton supports, with independent certificate infrastructure in parallel.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-048`

### [The inverse system has 60 minimal contraction generators in degrees 5 through…](../units/JCG-6FA7D42B.md)

`JCG-6FA7D42B` · `assertion`

The inverse system has 60 minimal contraction generators in degrees 5 through 8, so the local algebra has socle dimension and type 60 and is neither Gorenstein, level, nor a complete intersection.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#thm:inverse`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#cor:socle`

### [The literal weight-20 coefficient in the public cubic boundary frame is moved…](../units/JCG-7058A7C2.md)

`JCG-7058A7C2` · `assertion`

The literal weight-20 coefficient in the public cubic boundary frame is moved by translation and is therefore gauge rather than a modulus.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-012`

### [The map has a weighted \(\mathbb C^\times\)-symmetry.](../units/JCG-D10C308D.md)

`JCG-D10C308D` · `assertion`

The map has a weighted \(\mathbb C^\times\)-symmetry.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-013`

### [The minimal Kuranishi ideal has exactly 36 generators, with initial orders 11…](../units/JCG-525A42DB.md)

`JCG-525A42DB` · `assertion`

The minimal Kuranishi ideal has exactly 36 generators, with initial orders 11 quadratic, 13 cubic, 11 quartic, and one sextic; the endpoint Betti counts are beta_1=36 and beta_10=60.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#thm:equations`
- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/main.tex#cor:betti`

### [The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and…](../units/JCG-30AF091E.md)

`JCG-30AF091E` · `assertion`

The minimal ordinary degree in dimension three, minimal homogeneous-reduction dimension, and minimal support remain open.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-047`

### [The reciprocal boundary stratum has the stated cubic-frame normal form, with only…](../units/JCG-B3CD96D4.md)

`JCG-B3CD96D4` · `assertion`

The reciprocal boundary stratum has the stated cubic-frame normal form, with only the kappa coefficient before the residual y-translation is quotiented out.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/04-stable-moduli/appendices/additional-moduli.tex#prop:based-kappa-normal-form`

### [The residual cubic coefficient w20=lambda in the chosen birational-frame normal form is…](../units/JCG-9E239454.md)

`JCG-9E239454` · `assertion`

The residual cubic coefficient w20=lambda in the chosen birational-frame normal form is entirely affine gauge, with an explicit identity F_lambda = beta_lambda composed with F_0 composed with alpha_lambda.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/additional-results-and-leads.tex#supp-note-03-008`

### [Top priorities are independent certificate reproduction, the full bounded-degree local ring a…](../units/JCG-AF04161C.md)

`JCG-AF04161C` · `assertion`

Top priorities are independent certificate reproduction, the full bounded-degree local ring and degree-growth interface, intrinsic triple-cover defect exclusion, boundary-complete rigidity, the minimum degree-three coordinate bound, improved descendant dimensions/tensor rank, the five-dimensional classification, and explaining the two-dimensional obstruction.

Support:

- **source assertion:** version-8 supplementary statement with explicit evidence boundary — `papers-release-2026-07-26-v8/06-plane-boundary/appendices/additional-results-and-leads.tex#supp-note-06-044`

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

### [Exact order-six exclusion at two exceptional lower jets](../units/RMU-3D8E0001.md)

`RMU-3D8E0001` · `computational_result`

At the selected degree-eight exceptional first-normal direction with u_3=-1/3, u_5=3, and u_14=1, the complete characteristic-zero order-six obstruction ideal at the base point of the reduced 22-dimensional order-four lower-jet space is the unit ideal after all 24 order-five bending parameters and the next tangent coefficient are included. The same exact calculation at the adjacent lower jet c_0=1 gives the same reduced equations. Hence neither of these two lower jets extends through order six in the pinned bounded-degree deformation model.

Hypotheses:

- The degree-at-most-eight Kuranishi model, selected first-normal direction, lower-jet equations, and parameter conventions are those of the pinned source message.
- All 24 order-five bending parameters are included.
- The two stated certificates are reconstructed over the rational numbers.

Support:

- **certificate:** Exact characteristic-zero coefficient-row reduction of the complete order-six system with all order-five bendings. — No public locator supplied.
  - Does not establish: Uniform exclusion over the complete lower-jet family.
  - Does not establish: A global orbit-saturation theorem.

Limitations:

- This does not exclude every point of the 22-dimensional lower-jet family.
- It does not handle other first-normal strata, quadratic source-shear variation, target shears, or their intersections.
- It is not a global degree-eight rigidity theorem.

### [Five-variable universal order-six reduction](../units/RMU-3D8E0002.md)

`RMU-3D8E0002` · `computational_result`

Over F_1000033, the order-five compatibility matrix over the complete 22-parameter lower-jet family at the selected exceptional first-normal direction has a fixed 24-dimensional kernel. Every polynomial coefficient vector in the 27 lower-order correction columns of the universal order-six system lies in one fixed five-dimensional image. After projection to its three-dimensional cokernel, the obstruction consists of three polynomials depending only on c_14,c_19,c_26,t_8,t_15; the corrected universal assembly reproduces all 325 columns of the exact base system.

Hypotheses:

- The finite field is F_1000033.
- The selected first-normal direction and reduced 22-parameter lower-jet family are those of RMU-3D8E0001.
- The repaired accumulator retains determinant signs as plus or minus one until modular reduction.

Support:

- **program:** Corrected modular universal-system construction, coefficient-span reduction, and complete 325-column base comparison. — No public locator supplied.
  - Does not establish: Constant rank or a universal unit certificate.
  - Does not establish: Characteristic-zero validity away from the two exact sample jets.

Limitations:

- Constant rank five of the image over the whole lower-jet scheme has not been proved.
- The three five-variable polynomials have not yet been shown to generate the unit ideal universally.
- Multi-prime rational reconstruction and direct verification over Q remain open.
- The reduction is not a local or global degree-eight exclusion by itself.

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

### [Extremal Betti numbers](../units/RMU-94882795.md)

`RMU-94882795` · `corollary`

For the minimal \(S_0\)-free resolution of \(R\),
\[
\beta_1^{S_0}(R)=36,\qquad
\beta_{10}^{S_0}(R)=60.
\]
The ring is not a complete intersection.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#cor:betti`](../../proof-sources/03-local-rigidity/main.md#label-cor-betti)

### [Hilbert--Samuel function](../units/RMU-1EB4596D.md)

`RMU-1EB4596D` · `corollary`

The ring \(R\) has length \(584\), Loewy length nine, and Hilbert--Samuel
function
\[
(1,10,44,108,157,145,86,30,3).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#cor:hilbert`](../../proof-sources/03-local-rigidity/main.md#label-cor-hilbert)

### [Local product and multiplicity](../units/RMU-A815C162.md)

`RMU-A815C162` · `corollary`

There is a noncanonical formal isomorphism
\[
\widehat{\mathcal O}_{K_{3,7},G}
\cong
\C[[t_1,\ldots,t_{11}]]
\widehat\otimes_\C\mathcal R.
\]
Once \(\mathcal R_{\mathrm{red}}=\C\) is proved below, the reduced local
component is the normalized affine orbit and its scheme-theoretic
transverse multiplicity is
\[
\operatorname{length}\mathcal R=584.
\]
The formal local quotient stack is
\[
[\operatorname{Spf}\mathcal R/\Gm].
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#cor:local-product`](../../proof-sources/03-local-rigidity/main.md#label-cor-local-product)

### [Socle](../units/RMU-AF82754A.md)

`RMU-AF82754A` · `corollary`

The Cohen--Macaulay type is
\[
\dim_\mathbb Q\operatorname{Soc}(R)=60.
\]
The associated-graded socle dimensions occur as
\[
\dim\frac{\operatorname{Soc}(R)\cap\mathfrak m^d}
{\operatorname{Soc}(R)\cap\mathfrak m^{d+1}}
=
\begin{cases}
2,&d=5,\\
33,&d=6,\\
22,&d=7,\\
3,&d=8,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, \(R\) is neither Gorenstein nor level.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#cor:socle`](../../proof-sources/03-local-rigidity/main.md#label-cor-socle)

### [Source-flow proof of reduced affine rigidity](../units/RMU-601F2BED.md)

`RMU-601F2BED` · `corollary`

In the specified degree-seven affine slice,
\[
\sqrt I=(u_1,\ldots,u_{10}).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex#cor:source-flow-reduced-rigidity`](../../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md#label-cor-source-flow-reduced-rigidity)

### [Torus nullcone](../units/RMU-08E3EA3C.md)

`RMU-08E3EA3C` · `lemma`

Let \(X\) be an affine finite-type \(\Gm\)-scheme with a fixed point \(0\),
equivariantly embedded in
\[
V=V_-\oplus V_0\oplus V_+.
\]
If the reduced germs at zero of
\[
X\cap V_-,\qquad X\cap V_0,\qquad X\cap V_+
\]
are all zero-dimensional, then the reduced germ
\((X_{\mathrm{red}},0)\) is zero-dimensional.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#lem:nullcone`](../../proof-sources/03-local-rigidity/main.md#label-lem-nullcone)

### [Current residual evidence boundary](../units/RMU-1BC2872E.md)

`RMU-1BC2872E` · `proposition`

In the named \(28\)-variable residual Kuranishi calculation, only tangent
weights \(-2\) and \(-1\) occur.  In weight \(-2\), exact rational
elimination yields at successive orders the
incompatible conditions
\[
u_0u_1=0,\qquad 100u_0u_1+9=0.
\]
Thus no nonzero weight-\(-2\) initial direction lifts.  The weight \(-1\)
sector survives through parameter order four over \(\mathbb Q\).  Later
death calculations are modular evidence only: they do not establish over
characteristic zero that every first-normal direction is obstructed, and
they do not prove that the reduced residual germ is the union of the known
affine, source-shear, and target-shear components.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/appendices/degree-eight.tex#thm:degree-eight-transverse`](../../proof-sources/03-local-rigidity/appendices/degree-eight.md#label-thm-degree-eight-transverse)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/degree-eight.tex#thm:degree-eight-transverse`](../../proof-sources/03-local-rigidity/appendices/degree-eight.md#label-thm-degree-eight-transverse)

### [Exact fifth-order calculation](../units/RMU-40375935.md)

`RMU-40375935` · `proposition`

At parameter order five the direct model has Macaulay rank \(1857\), so
\[
H(5)=2002-1857=145.
\]
There is no new minimal quintic generator.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex#prop:source-flow-order-five`](../../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md#label-prop-source-flow-order-five)

### [Exact pure-weight certificates](../units/RMU-7F7F01FC.md)

`RMU-7F7F01FC` · `proposition`

For the Kuranishi germ of \eqref{eq:kuranishi-ring}, the following hold.
\begin{enumerate}[label=(\roman*)]
\item On the positive locus, with parameters
\[
(p_1,p_2,p_3,p_4,p_5)=(u_7,u_8,u_2,u_9,u_{10}),
\]
the eliminated ideal contains
\[
p_1^6,\quad p_2^6,\quad p_3^3,\quad p_4^3,\quad p_5^2.
\]
\item On the negative locus, with parameters
\[
(n_1,n_2,n_3,n_4)=(u_1,u_5,u_4,u_3),
\]
the eliminated ideal contains
\[
n_1^4,\quad n_2^4,\quad n_3^4,\quad n_4^3.
\]
\item The weight-zero locus has one tangent parameter \(q=u_6\).  Its first
nonzero compatibility equation occurs in order three and has coefficient
\[
\frac{212135552}{304438725}q^3.
\]
\end{enumerate}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:pure-weight`](../../proof-sources/03-local-rigidity/main.md#label-prop-pure-weight)

### [Formal source-orbit theorem](../units/RMU-3F0AA851.md)

`RMU-3F0AA851` · `proposition`

Let \(A\) be a local Artin \(\C\)-algebra, and let \(H_A\) be a normalized
Keller deformation of \(G\) over \(A\) reducing to \(G\).  There is a unique
normalized formal \(A\)-automorphism of \(\widehat{\A}^3_0\),
\(\phi_A\equiv\id\pmod{\mathfrak m_A}\) such that
\[
H_A=G\circ\phi_A.
\]
Moreover, \(\det J\phi_A=1\).  Consequently the degree-\(\le7\)
deformation functor is the subfunctor of volume-preserving source
reparametrizations cut out by
\[
\deg(G\circ\phi_A)\le7.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:formal-orbit`](../../proof-sources/03-local-rigidity/main.md#label-prop-formal-orbit)

### [Normalized affine stabilizer](../units/RMU-4A713512.md)

`RMU-4A713512` · `proposition`

The stabilizer of \(G\) under \eqref{eq:rho} is
\[
\operatorname{Stab}_{\operatorname{Aff}_3}(G)
=\set{A_\tau:\tau\in\Gm}\cong\Gm.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:stabilizer`](../../proof-sources/03-local-rigidity/main.md#label-prop-stabilizer)

### [Order-nine integrability certificate](../units/RMU-EC26BB3F.md)

`RMU-EC26BB3F` · `proposition`

One has
\[
\mathfrak m^9=0.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:order-nine`](../../proof-sources/03-local-rigidity/main.md#label-prop-order-nine)

### [Quadratic shear family](../units/RMU-8DD676DE.md)

`RMU-8DD676DE` · `proposition`

If \(f\) is a nonzero homogeneous quadratic, then \(G_f\) has ordinary degree
eight.  More explicitly,
\[
G_f
=G+f\left(-\frac{x^3}{2},\,
          3x(1+xy)^2,\,
          (1+xy)^3\right),
\]
and its degree-eight homogeneous part is
\[
\bigl(0,0,x^3y^3f(x,y)\bigr).
\]
In particular, \(G_f\) is not affinely equivalent to the degree-seven map
\(G\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/degree-eight.tex#prop:quadratic-shears`](../../proof-sources/03-local-rigidity/appendices/degree-eight.md#label-prop-quadratic-shears)

### [The three terminal classes](../units/RMU-48A05BD8.md)

`RMU-48A05BD8` · `proposition`

The order-seven quotient has dimension \(581\).  The degree-eight dual layer
has dimension three, with one class in each torus weight \(-1,0,1\).
Consequently
\[
\dim_\mathbb Q R/\mathfrak m^9=584
\]
and
\[
\operatorname{ch}(\mathfrak m^8/\mathfrak m^9)=z^{-1}+1+z.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:terminal`](../../proof-sources/03-local-rigidity/main.md#label-prop-terminal)

### [Transversality](../units/RMU-05F65C7D.md)

`RMU-05F65C7D` · `proposition`

The slice is torus-stable.  The selected \(11\times11\) affine-orbit minor
has determinant \(-23328\).  In particular,
\[
\operatorname{Aff}_3\times^{\Gm}S\longrightarrow K_{3,7}
\]
is \'{e}tale at \([1,G]\).

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#prop:transversality`](../../proof-sources/03-local-rigidity/main.md#label-prop-transversality)

### [Weighted divergence in root coordinates](../units/RMU-276143E2.md)

`RMU-276143E2` · `proposition`

In the marked-root chart,
\[
dx\wedge dy\wedge dz
=-\delta\,dA\wedge dB\wedge ds.
\]
Consequently a vector field
\[
X=a\,\partial_A+b\,\partial_B+c\,\partial_s
\]
preserves source volume if and only if
\[
\partial_A(\delta a)+\partial_B(\delta b)+\partial_s(\delta c)=0.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/root-coordinate-source-flow.tex#prop:root-coordinate-divergence`](../../proof-sources/03-local-rigidity/appendices/root-coordinate-source-flow.md#label-prop-root-coordinate-divergence)

### [Affine classification inside the shear family](../units/RMU-6463F54E.md)

`RMU-6463F54E` · `theorem`

For nonzero homogeneous quadratics \(f,g\),
\[
G_f\sim_{\mathrm{aff}}G_g
\quad\Longleftrightarrow\quad
g(x,y)=\tau^2f(\tau x,\tau^{-1}y)
\quad\text{for some }\tau\in\C^\times .
\]
Consequently the generic affine quotient of the three-parameter quadratic
shear family has dimension two.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/degree-eight.tex#thm:shear-classification`](../../proof-sources/03-local-rigidity/appendices/degree-eight.md#label-thm-shear-classification)

### [Exact rational border basis](../units/RMU-5135EABE.md)

`RMU-5135EABE` · `theorem`

There is an explicitly recorded monomial order ideal
\(\mathcal B\) of cardinality \(584\) whose residue classes form a
\(\mathbb Q\)-basis of \(R\).  Its degree distribution is the displayed
Hilbert--Samuel function, and its torus-weight distribution is
\[
\begin{array}{c|rrrrrrrrrrrrr}
w&-7&-6&-5&-4&-3&-2&-1&0&1&2&3&4&5\\ \hline
\#\mathcal B_w&1&4&12&28&47&74&94&96&86&67&45&23&7.
\end{array}
\]
The corresponding border has \(2654\) monomials.  Its exact rational
relations generate \(I_\kappa\).  Equivalently, the ten multiplication
matrices
\[
M_i\in\operatorname{Mat}_{584}(\mathbb Q)
\]
commute, contain \(24402\) nonzero entries in total, preserve the weight and
\(\mathfrak m\)-adic filtrations, annihilate degree eight after one further
multiplication, and make the class of \(1\) cyclic.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/border-basis-and-betti.tex#thm:exact-border-basis`](../../proof-sources/03-local-rigidity/appendices/border-basis-and-betti.md#label-thm-exact-border-basis)

### [Minimal inverse-system generators](../units/RMU-308B1323.md)

`RMU-308B1323` · `theorem`

The quotient \(D/\mathfrak mD\) has dimension \(60\).  Its top-degree and
torus-refined generating polynomial is
\begin{align*}
\mathcal S(t,z)={}&t^5(z^{-1}+z^3)\\
&+t^6(z^{-4}+z^{-3}+5z^{-2}+11z^{-1}+8+6z+z^2)\\
&+t^7(z^{-4}+2z^{-3}+3z^{-2}+7z^{-1}+3+3z+2z^2+z^3)\\
&+t^8(z^{-1}+1+z).
\end{align*}

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#thm:inverse`](../../proof-sources/03-local-rigidity/main.md#label-thm-inverse)

### [Quadratic-frame effectivity staircase and conditional stable non-effectivity](../units/RMU-3FEF0010.md)

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

### [Reduced affine rigidity](../units/RMU-AD557E97.md)

`RMU-AD557E97` · `theorem`

The reduced completed slice is a point:
\[
\mathcal R_{\mathrm{red}}\cong\C.
\]
Equivalently,
\[
\sqrt{I_\kappa}=(u_1,\ldots,u_{10}).
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#thm:reduced`](../../proof-sources/03-local-rigidity/main.md#label-thm-reduced)

### [Source-flow reconstruction](../units/RMU-9E711A93.md)

`RMU-9E711A93` · `theorem`

The direct determinant complex and the marked-root weighted-divergence
complex give the same filtered transverse Kuranishi ideal through parameter
order four over \(\mathbb Q\).  In particular they give
\[
H(0),\ldots,H(4)=(1,10,44,108,157)
\]
and filtered minimal-generator counts
\[
11\text{ quadratic},\qquad
13\text{ cubic},\qquad
11\text{ quartic}.
\]

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/source-flow-reconstruction-progress.tex#thm:source-flow-reconstruction`](../../proof-sources/03-local-rigidity/appendices/source-flow-reconstruction-progress.md#label-thm-source-flow-reconstruction)

### [Thirty-six minimal equations](../units/RMU-400F1EBA.md)

`RMU-400F1EBA` · `theorem`

The conormal space of the Kuranishi ideal has dimension
\[
\mu(I_\kappa)
=\dim_\mathbb Q I_\kappa/\mathfrak mI_\kappa=36.
\]
Its initial-order distribution is
\[
11,\ 13,\ 11,\ 0,\ 1
\]
in orders \(2,3,4,5,6\), respectively.  The corresponding torus characters
are
\begin{align*}
E_2(z)={}&z^{-6}+z^{-5}+z^{-2}+z+z^2+z^3+2z^4+2z^5+z^6,\\
E_3(z)={}&z^{-3}+2z^{-2}+2z^{-1}+1+2z+z^2+z^3+z^5+2z^6,\\
E_4(z)={}&z^{-8}+z^{-7}+2z^{-6}+2z^{-5}+z^{-4}+z^{-3}+z^{-2}+2z^5,\\
E_6(z)={}&z^3.
\end{align*}
No new minimal generator first appears in orders seven, eight, or nine.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#thm:equations`](../../proof-sources/03-local-rigidity/main.md#label-thm-equations)

### [Three exact finite-field Betti tables](../units/RMU-C8D99888.md)

`RMU-C8D99888` · `theorem`

For each
\[
p\in\{1000003,\ 1000033,\ 1000001011\},
\]
all \(234\) nonzero torus-weight blocks of the Koszul complex give the same
minimal-resolution Betti vector:
\[
\boxed{
(1,36,354,1565,3937,6216,6432,4403,1942,506,60).
}
\]
The character-valued Euler identity holds in every case.

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/border-basis-and-betti.tex#thm:three-prime-betti`](../../proof-sources/03-local-rigidity/appendices/border-basis-and-betti.md#label-thm-three-prime-betti)

### [Transverse local algebra](../units/RMU-C9E196D6.md)

`RMU-C9E196D6` · `theorem`

For the slice \(S\) of \cref{def:slice}, the following hold.
\begin{enumerate}[label=(\roman*)]
\item The reduced completed local ring is a point:
\[
\mathcal R_{\mathrm{red}}\cong\C.
\]
\item If \(\mathfrak m\) is the maximal ideal, then
\[
\operatorname{length}\mathcal R=584,\qquad
\mathfrak m^9=0\ne\mathfrak m^8,
\]
and
\[
\bigl(\dim_\C\mathfrak m^d/\mathfrak m^{d+1}\bigr)_{d=0}^8
=(1,10,44,108,157,145,86,30,3).
\]
\item The Macaulay inverse system of \(\mathcal R\) has 60 minimal
contraction generators.  Their top divided-power degrees are distributed as
\[
\begin{array}{c|rrrr}
\text{degree}&5&6&7&8\\ \hline
\text{number}&2&33&22&3.
\end{array}
\]
Consequently
\(\dim_\C\operatorname{Soc}(\mathcal R)=60\).
\item The Kuranishi ideal has 36 minimal generators, distributed by initial
order as
\[
\begin{array}{c|rrrr}
\text{order}&2&3&4&6\\ \hline
\text{number}&11&13&11&1.
\end{array}
\]
For the minimal resolution over
\(\C[[u_1,\ldots,u_{10}]]\), the extremal Betti numbers are
\(\beta_1=36\) and \(\beta_{10}=60\).
\end{enumerate}

Dependencies:

- `uses` [`RMU-2B8185BE`](../units/RMU-2B8185BE.md): Formal statement references def:slice.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/main.tex#thm:main`](../../proof-sources/03-local-rigidity/main.md#label-thm-main)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#thm:main`](../../proof-sources/03-local-rigidity/main.md#label-thm-main)

## Open frontier

### [Can the complete local algebra be recovered conceptually from the marked-root geometry,…](../units/RMU-60228097.md)

`RMU-60228097` · `question`

Can the complete local algebra be recovered conceptually from the
marked-root geometry, rather than by coefficient elimination?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/main.tex`](../../proof-sources/03-local-rigidity/main.md)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex`](../../proof-sources/03-local-rigidity/main.md)

### [Construct a different-filtered source-flow or transferred L-infinity model that independently…](../units/JCG-D9E57688.md)

`JCG-D9E57688` · `question`

Construct a different-filtered source-flow or transferred L-infinity model that independently reproduces the bounded-degree Kuranishi equations and the length-584 Artin algebra.

Support:

- **source assertion:** exact version-8 statement — `papers-release-2026-07-26-v8/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`

### [Different-filtered reconstruction](../units/RMU-9523BCAD.md)

`RMU-9523BCAD` · `question`

Can a different-filtered source-flow complex, or an equivalent transferred
\(L_\infty\)-model, recover the bounded-degree Kuranishi ideal and its
length \(584\) independently of coefficient elimination?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`](../../proof-sources/03-local-rigidity/appendices/root-coordinate-source-flow.md#label-q-different-filtered-reconstruction)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/root-coordinate-source-flow.tex#q:different-filtered-reconstruction`](../../proof-sources/03-local-rigidity/appendices/root-coordinate-source-flow.md#label-q-different-filtered-reconstruction)

### [For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree…](../units/JCG-4451EE05.md)

`JCG-4451EE05` · `question`

For a realized decorated boundary class xi, bound the orbit-minimal ordinary degree delta_LR(xi)=min{deg H : H is polynomially left-right equivalent to xi} from intrinsic conductor, ramification, valuation, or nonproperness data. A bound of at least seven for every nontrivial generic-degree-three boundary class would supply the missing degree-cost bridge from cubic-cover classification to low-degree exclusion.

### [How does the Artin algebra change under polynomial, rather than affine, left--right…](../units/RMU-59738A85.md)

`RMU-59738A85` · `question`

How does the Artin algebra change under polynomial, rather than affine,
left--right equivalence or after stabilization?

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/main.tex`](../../proof-sources/03-local-rigidity/main.md)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex`](../../proof-sources/03-local-rigidity/main.md)

### [Independent source-flow verification](../units/RMU-77F76FF6.md)

`RMU-77F76FF6` · `question`

Can one derive the finite overflow and Kuranishi equations directly from
volume-preserving flows on the source?  In view of
\cref{prop:root-coordinate-divergence}, the sharper target is an independent
construction using the different filtration or transferred
\(L_\infty\)-data.  Agreement would test the source-orbit interpretation of
the local Artin algebra.

Dependencies:

- `uses` [`RMU-276143E2`](../units/RMU-276143E2.md): Formal statement references prop:root-coordinate-divergence.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/main.tex#q:source-flow-verifier`](../../proof-sources/03-local-rigidity/main.md#label-q-source-flow-verifier)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex#q:source-flow-verifier`](../../proof-sources/03-local-rigidity/main.md#label-q-source-flow-verifier)

### [Is the radical of the completed residual ideal exactly the union of…](../units/RMU-6413E00D.md)

`RMU-6413E00D` · `question`

Is the radical of the completed residual ideal exactly the union of the
known affine, source-shear, and target-shear components?  This requires a
characteristic-zero treatment of the surviving weight-\(-1\) sector,
including branches tangent to a known component before leaving it.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/appendices/degree-eight.tex`](../../proof-sources/03-local-rigidity/appendices/degree-eight.md)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/degree-eight.tex`](../../proof-sources/03-local-rigidity/appendices/degree-eight.md)

### [Rational Betti certification](../units/RMU-C76886E8.md)

`RMU-C76886E8` · `question`

Produce exact rational rank or homology certificates for the intermediate
Koszul blocks.  The border presentation reduces this to a finite
weight-by-weight calculation independent of the original Kuranishi
elimination.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/appendices/border-basis-and-betti.tex#q:rational-betti`](../../proof-sources/03-local-rigidity/appendices/border-basis-and-betti.md#label-q-rational-betti)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/appendices/border-basis-and-betti.tex#q:rational-betti`](../../proof-sources/03-local-rigidity/appendices/border-basis-and-betti.md#label-q-rational-betti)

### [What is the reduced deformation germ when ordinary degree eight is allowed?…](../units/RMU-72CB84EA.md)

`RMU-72CB84EA` · `question`

What is the reduced deformation germ when ordinary degree eight is allowed?
Existing calculations give a mixture of exact and modular finite-order
evidence, but not a characteristic-zero radical theorem.

Support:

- **source assertion:** The manuscript records this exact formal statement. — [`manuscripts/03-local-rigidity/main.tex`](../../proof-sources/03-local-rigidity/main.md)
  - Full source and surrounding context: [`manuscripts/03-local-rigidity/main.tex`](../../proof-sources/03-local-rigidity/main.md)
