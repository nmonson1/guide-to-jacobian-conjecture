# Lane 1: Cubic flatness and finite normalization defects

## Research objective

For a generic-degree-three Keller map, prove that the finite normalization
defect vanishes, or isolate the exact algebraic datum that can support it.  A
successful argument would turn the existing divisorial anatomy into a finite
flat cubic cover and connect the named counterexample to marked-root geometry.

This lane belongs mainly to [Program 1](cubic-marked-root-incidence-geometry.md),
with boundary-completion input from [Program 4](stable-moduli.md).  Read those
program dossiers for notation and complete proof routes.  Current TeX proof
sources are available as text from the [proof-source index](../proof-sources/index.md);
PDFs are optional.

## Reusable mathematics

For the named three-variable Keller map, the inverse cubic gives the exact
`3/1/0` fibre chart: a simple root reconstructs one affine source point, the
discriminant controls the double-root fibre, and the triple-root curve removes
the final affine sheet.  In the normalization of the induced cubic function
field extension, the trace module splits as

```text
O_Y + E,
```

where `E` is rank two and reflexive.  Completed valuations and inertia split
the divisorial behaviour into the established `U1`, `U2`, and `B` sheet-loss
types.  Source splitting gives flatness over every attained target point.
Consequently the possible nonflat locus is finite and supported at omitted
target values.

These statements are about the named map and its finite normalization.  They
do not classify arbitrary cubic covers.  Reflexivity removes codimension-one
pathology but does not remove isolated defects on a threefold.

## Live problem

Prove that the remaining finite defect module is zero.  Three concrete routes
remain credible:

1. Push the conormal-root module to the quadratic resolvent and use the
   resulting maximal Cohen--Macaulay structure.
2. Compute the finite exceptional lattice allowed by the established inertia
   and trace constraints, then exclude every nonzero lattice point.
3. Find a Keller-specific commutative-algebra argument using the source
   splitting, determinant-one condition, and reflexive trace-zero module.

A broader anatomy theorem is welcome if it keeps four notions separate:
branch image, nonproperness, flatness, and classification as a marked-root
cover.  None implies all the others without an additional argument.

## Useful deliverable

The ideal output is a theorem with exact local hypotheses at an omitted value,
a proof that its defect module vanishes, and a short dependency map back to the
known trace and inertia results.  A counterexample module satisfying all known
constraints would also be valuable because it would identify a missing Keller
input.

Do not rederive the inverse cubic or the divisorial sheet taxonomy unless a
new proof genuinely strengthens them.  Feel free to pursue a different
connection or formulation if it has greater leverage; state what it would
establish and which current dependency it replaces.
