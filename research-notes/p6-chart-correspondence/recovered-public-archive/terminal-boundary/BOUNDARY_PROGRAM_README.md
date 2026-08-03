# Terminal boundary-gluing program: artifact index

## Main mathematical notes

- `terminal_boundary_next_steps_report.md` — consolidated theorem/status report for the completed research cycle.
- `terminal_boundary_gluing_program.tex` / `.md` — universal determinant layer operator, residue adjoint, Riemann--Roch index, contact-degree formula, hypergeometric secondary Belyi transport, filtered one-layer descent, the conditional gluing--descent theorem, and the corrected lattice-gap primary reduction.
- `terminal_primary_belyi_reduction.tex` / `.md` — proof of the lattice-gap quotient theorem for every terminal type-I.b corner, exact quotient passports and counts for the first five post-125 cases, and explicit maps through the max-128 case.
- `F2_degree125_boundary_seed.md` — complete-chain seed for the first degree-125 family, corrected to its unique degree-six lattice quotient.

## Exact verifiers

- `boundary_complex_index.py` — verifies the universal layer/adjoint integration-by-parts identity and the current virtual obstruction excess \(\epsilon_r=r-1\).
- `universal_boundary_transport.py` — verifies the hypergeometric secondary-map ODE, derivative, squarefreeness, degree, and passports.
- `terminal_primary_belyi.py` — verifies the final-corner bracket equation, primitive direction, lattice gap, quotient equation, derivative, passports, and explicit \(F_2\) quotient.
- `count_F2_terminal_dessins.py` — computes the eleven **ambient** degree-30 classes and proves that exactly one, the \(C_5\)-symmetric class, is compatible with the gap-five polynomial lattice.
- `verify_post125_terminal_examples.py` — verifies the first five lattice quotient passports and exact Hurwitz counts; reconstructs the unique degree-6, degree-10, and degree-9 maps and the two conjugate max-128 degree-9 maps.
- `generate_F2_degree30_system.py` — ambient fractional-cover termination scheme; its lattice-compatible locus is explicitly marked as \(a_1=\cdots=a_4=0\), a single nonzero scaling orbit.

- `terminal_face_rigidity.py` — verifies that the explicit reduced degree-6, degree-10, and degree-9 maps have surjective fixed-constant linearization and kernel exactly the source-scaling line.

## Machine-readable outputs

- `F2_terminal_primary_passport.json`
- `F2_terminal_dessin_count.json`
- `post125_terminal_passports.json`
- `F2_degree30_coefficient_system.json`
- `universal_boundary_transport_table.json`
- `next_complete_chain_queue.json`
- `terminal_face_rigidity.json`

## Corrected primary-boundary conclusion

The fractional uniformizing equation for a terminal type-I.b corner is

\[
npq-mzpq'+nzp'q=1,
\]

but polynomial lattice support forces \(p,q\in K[z^g]\), where

\[
g=\operatorname{gap}(\rho,\ell).
\]

The relevant quotient has degree

\[
D=\frac{mnb}{g}
\]

and passport

\[
\left(n^{(mb-1)/g},\frac ng\right),\quad
\left(m^{nb/g}\right),\quad
\left(\frac{(m+n)b-1}{g},1^{D-\frac{(m+n)b-1}{g}}\right).
\]

For \(F_2\), the ambient degree-30 passport has eleven classes, but the gap is five and only one class is lattice-compatible. The reduced boundary map is the unique degree-six map

\[
\bar\tau(u)\doteq
\frac{u(u-1)^5}{(u^2-\frac53u+\frac59)^3}.
\]

## First quotient queue

| Case | quotient degree | classes |
|---|---:|---:|
| \(F_2\), max 125 | 6 | 1 |
| one-step max 126 | 10 | 1 |
| two-step max 126 | 9 | 1 |
| \(F_{24}\), max 128 | 9 | 2 |
| one-step max 132 | 16 | 2 |

## Logical status

Proved in this bundle:

1. universal layer and adjoint formulas;
2. virtual obstruction-index formula and the current specialization \(r-1\);
3. explicit universal secondary Belyi transport;
4. exact one-layer filtered descent criterion;
5. terminal type-I.b uniformizing ODE;
6. lattice-gap quotient theorem and passport;
7. automatic connectedness of the quotient passport;
8. exact first-five quotient counts;
9. explicit maps for the first four rows;
10. infinitesimal rigidity modulo source scaling for all explicit quotient maps through max degree 128.

Not proved:

1. the full Newton line-bundle windows for the new terminal chains;
2. completeness of the finite boundary Kuranishi functor for arbitrary terminal chains;
3. compatibility of layerwise pole reductions across all orders;
4. integration of those reductions to a polynomial approximate-root transformation;
5. the terminal gluing--descent dichotomy;
6. the full plane Jacobian conjecture.

The next exact task is a single \(C_5\)-equivariant normal-neighborhood calculation around the explicit degree-six \(F_2\) quotient, followed by the unique degree-ten and degree-nine cases.
