# Lane 6: Homogeneous realization and compression

## Research objective

Determine the true homogeneous realization complexity of the fixed
three-sheeted cover and decide whether its 19-variable cubic-homogeneous
presentation compresses to 18 variables.  Separate invariants of the cover
from obstructions attached only to one tensor or operation slice.

The primary reference is [Program 5](homogeneous-descendants.md), with local
deformation input from [Program 3](local-rigidity-and-deformation-algebra.md).
The newest retained units are the
[five-dimensional polynomial-gauge core](../working-mathematics/units/RMU-5D8E0001.md),
its [three residual surfaces](../working-mathematics/units/RMU-5D8E0002.md),
and the [selected-plane cubic/quartic classification](../working-mathematics/units/RMU-5D8E0003.md).

## Reusable mathematics

The rank-sensitive suspension of the fixed degree-at-most-three map gives a
19-variable cubic-homogeneous counterexample.  Its symmetric cotangent double
has 38 variables.  A Druzkowski pairing is known with length at most 110 and
at least 52 for this fixed tensor.  These are realization bounds, not global
minimum dimensions among all maps with the same cover.

In the weight-zero row-killing calculation, the relevant fibre has dimension
20.  Thirteen reconstructed triangular directions and the elementary shear
`b^2 e_h` integrate to polynomial automorphisms.  Their quotient is six
dimensional; imposing the normal cubic Casimir relation leaves the exact core

```text
A=k_14, B=k_19, C=k_23, D=k_67, E=k_85.
```

Eleven rational degree-one dual sections exclude every core point outside
three two-dimensional surfaces:

```text
Z0: A=B=D=0;
Z1: D=0, A=-3B, C^2+36C+50B-104BC=0;
Z2: A=3D, B=-D, C^2+36C+104CD-50D-84D^2=0;
```

In each surface `E` is free.  The result detects the secondary obstruction by
degree-one dual sections.  It does not say the obstruction vanishes on those
surfaces.  A finite higher-order conjugation theorem from the full weight-zero
fibre to the displayed core is also still missing.

A separate exact rank-six plane calculation is now complete through the first
intrinsic obstruction.  Generic finite slopes do not lift cubically.  The
rational exceptional slope `r=4` is intrinsically obstructed at cubic order.
The two conjugate slopes

```text
r = 4 + 4 sqrt(-3),   r = 4 - 4 sqrt(-3)
```

have 17-dimensional cubic-lift fibres but each has an intrinsic quartic
obstruction; the exact coefficient-span certificate pairs to `-1152` at one
conjugate and transfers by field conjugation.  These statements classify the
selected finite plane only, not the full 15-dimensional finite row-base fibre
or the infinity fibre.

## High-priority next work

1. Prove finite triangular-gauge compatibility, transporting every higher
   normal term and the moving cokernel section to the five-dimensional core.
2. Construct degree-two dual sections on `Z0`, `Z1`, and `Z2`; prove their
   evaluation ideals are units or isolate a smaller residual locus.
3. Extend the selected-plane calculation to the complete finite row-base
   fibre and the infinity fibre, retaining all cubic-lift parameters before
   computing the next Kuranishi map.
4. Impose the separate compression functional and the full moving target and
   stable gauges.
5. Seek a conceptual lower bound from collision monoliths or the `sl/sp`
   dichotomy that depends on the cover rather than one presentation.

Moving target gauge can kill fixed quartic functionals, so a single scalar
quartic witness is not a global compression invariant.  Use the cokernel sheaf
and the order/Fitting ideal of the moving obstruction section.  Do not infer
finite nonlinear gauge equivalence from a tangent-space direct sum.

## Useful deliverable

The most direct next theorem is unit detection on all three residual surfaces,
conditional only on a separately stated finite-gauge lemma.  A construction
on a persistent surface is equally important.  Broader structural approaches
are encouraged if they account for all moving gauge directions and say exactly
which realization complexity they bound.
