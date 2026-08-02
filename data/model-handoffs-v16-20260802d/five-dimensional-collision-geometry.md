# Lane 7: Five-dimensional collision geometry

## Research objective

Determine the characteristic-zero component geometry of the exact
five-dimensional, everywhere-regular Jordan-type `(5)` collision chart and
decide the first-normal obstruction on each component.

This is not the 19-to-18 compression scheme.  It is a separate Program 5
collision-pencil problem.

## Reusable mathematics

For an everywhere-regular type-`(5)` quadratic nilpotent pencil on `P^1`, the
kernel filtration has quotient degrees

```text
(-4,-2,0,2,4).
```

On the full-span chart, regularity is exactly `a_7!=0`.  After putting
`lambda=a_7`, its eight parameters are the principal-`sl_2` module

```text
C*lambda + Sym^6(C^2),
```

and

```text
det T=((lambda^2+4A)^2-96B)/256.
```

The collision and integrability equations have a smooth one-dimensional
characteristic-zero family, obtained by Hensel lifting an explicit smooth
`F_11` point.  Retained occurrence: [`JCG-FFBBD77B`](../working-mathematics/units/JCG-FFBBD77B.md).

The complete `Z_11` residue disk through that point has no first-normal
extension.  The exact adapted system has ranks `(60,61)` and the independent
coordinate-free system ranks `(125,126)`.  Retained occurrence:
[`JCG-64E18DF3`](../working-mathematics/units/JCG-64E18DF3.md).

The normalized full-kernel chart has exactly 15 primitive quintic equations
in 16 variables on

```text
det(T)*(u_3-u_4*v_3) != 0.
```

All 30 rational collision points found over `F_7`, `F_11`, and `F_13` have
nonzero first-normal obstruction ([`JCG-86F5C9FA`](../working-mathematics/units/JCG-86F5C9FA.md)), but this is finite-field
evidence rather than a component theorem.

For any global homogeneous quadratic nilpotent `5 x 5` matrix generically of
type `(5)`, the rank-at-most-three locus has codimension at most two.  If it
extends an everywhere-regular collision line, that locus has codimension
exactly two and misses the line.  Retained occurrence: [`JCG-15D52C7B`](../working-mathematics/units/JCG-15D52C7B.md).

## What is not known

The characteristic-zero radical, components, dimensions, degrees, and
singular loci of the 15-quintic chart are unknown.  The first-normal section
has not been evaluated at the generic points of its components.  Kernel-span
three/four strata and generic Jordan types `(4,1)` and `(3,2)` remain open.

Two monolithic Macaulay2 attempts produced no mathematical result.  The first
failed after about 58 minutes at roughly 9.3 GB; the second hit a four-hour
limit without a dimension, degree, decomposition, or standard output.  Do not
treat them as negative evidence.

## Exact live problem

Run a staged characteristic-zero calculation:

1. saturate by the explicit open factors one at a time;
2. record dimension after each saturation;
3. compute radical membership and equidimensional data;
4. identify components before requesting primary decomposition;
5. evaluate the augmented-rank obstruction over each component function
   field; and
6. only then analyze singular and exceptional loci.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P5-L7A — Staged saturation

Actor: `local_symbolic`. Status: ready.

Use new versioned run paths and save every intermediate ideal and invariant.

### P5-L7B — Componentwise first-normal section

Actor: `local_symbolic`. Status: blocked on P5-L7A.

Compute generic coefficient/augmented ranks on each characteristic-zero
component.

### P5-L7C — Geometric reinterpretation

Actor: `online_model`. Status: ready.

Seek a determinantal, apolar, invariant-theoretic, or incidence description
explaining the 15 quintics and the binary-sextic action.

## Do not do

- Do not repeat a monolithic saturation/decomposition job.
- Do not infer characteristic-zero components from rational finite-field
  points.
- Do not discard a component merely because the first obstruction vanishes;
  it may be a construction locus.
- Do not say the regular type-`(5)` stratum is globally excluded.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.
