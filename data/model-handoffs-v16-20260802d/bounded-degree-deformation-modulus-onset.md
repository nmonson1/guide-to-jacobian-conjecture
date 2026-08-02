# Lane 3: Bounded-degree deformation and modulus onset

## Research objective

Explain why the named map is an isolated, length-584 point in the
degree-at-most-seven quotient while genuine source and target shear families
appear in degree eight.  Finish the selected degree-eight saturation only
after quotienting every known operation component.

## Reusable mathematics

In an eleven-condition affine slice transverse to the normalized source
orbit, the completed degree-at-most-seven algebra has

```text
length                         584
Hilbert function               (1,10,44,108,157,145,86,30,3)
nilpotence                     m^9=0 != m^8
Cohen--Macaulay type           60
minimal Kuranishi equations    36 = 11+13+11+1 by orders 2,3,4,6.
```

The reduced germ is a point.  This is bounded-degree, affine-quotiented
rigidity, not unrestricted formal rigidity.  Relevant retained units include
[`RMU-C9E196D6`](../working-mathematics/units/RMU-C9E196D6.md), [`RMU-A815C162`](../working-mathematics/units/RMU-A815C162.md), [`RMU-AF82754A`](../working-mathematics/units/RMU-AF82754A.md), and [`RMU-601F2BED`](../working-mathematics/units/RMU-601F2BED.md).

The direct determinant reconstruction independently agrees with the
marked-root source-flow calculation through parameter order four.  It reaches
order six with `H(5)=145`, no new quintic equation, and the unique primitive
weight-three sextic displayed in the manuscript.  Orders seven and eight have
not been independently reconstructed by that lineage.

At the selected exceptional degree-eight first-normal point, the complete
characteristic-zero order-six ideal is the unit ideal at two lower jets after
all 24 order-five bendings are allowed.  Retained unit: [`RMU-3D8E0001`](../working-mathematics/units/RMU-3D8E0001.md).

Over `F_1000033`, the universal lower-jet calculation has:

```text
fixed order-five kernel        24
fixed correction image         5
obstruction cokernel            3
remaining variables             c_14,c_19,c_26,t_8,t_15.
```

The corrected assembly reproduces all 325 base columns.  Retained unit:
[`RMU-3D8E0002`](../working-mathematics/units/RMU-3D8E0002.md).  The earlier assembly using `p-1` as an integer negative sign
is invalid.

## What is not known

The five-variable reduction is modular.  It does not prove constant rank over
the whole family, a universal unit ideal, a characteristic-zero lift, or full
degree-eight orbit saturation.  Known quadratic source `z`-shears and target
shears are genuine components.  A degree-eight point can therefore be
nonrigid without contradicting the length-584 result.

## Exact live problem

Use three fixed-image columns to form a `3 x 3` determinant
`Delta_H(c_14,c_19,c_26)`.  Then express the three obstruction polynomials
against

```text
1,t_8,t_15,t_8^2,t_8*t_15,t_15^2
```

and compute the `3 x 3` minors.  Lift sparse identities over `Q`; recurse only
on the factors where rank drops.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P3-L3A — Characteristic-zero rank stratification

Actor: `local_symbolic`. Status: ready.

Produce exact determinants, factorization, source hashes, and a finite list of
rank-drop strata.

### P3-L3B — Unit ideal or residual components

Actor: `local_symbolic`. Status: blocked on P3-L3A.

Prove a unit minor on each stratum or return explicit residual equations.

### P3-L3C — All-order complex comparison

Actor: `online_model`. Status: ready.

Extend the marked-root/direct chain map through orders five to eight,
including source and target shear components and nonlinear obstruction maps.

## Do not do

- Do not interpret unrestricted formal right-triviality as bounded rigidity.
- Do not call a modular fixed-image calculation characteristic zero.
- Do not reuse the signed-overflow assembly.
- Do not omit known source and target shear components from saturation.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.
