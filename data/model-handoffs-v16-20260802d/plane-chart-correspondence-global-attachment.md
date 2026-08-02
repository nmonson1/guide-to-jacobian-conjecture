# Lane 9: Plane chart correspondence and global attachment

## Research objective

Classify normal-layer kernel directions as fixed-chart operations, adjacent
complete-chain rechartings, or genuine attachment parameters.  Then solve the
full two-sided `F_2` attachment problem with every fresh parameter, support
endpoint, and cyclic descent condition retained.

## Reusable mathematics

### Exact normal complex

On one smooth boundary component, the formal change to `(H,W,T)` coordinates
is invertible and turns the determinant equation into

```text
S(d+(r/S)dlog M_0)h_r=((S-r)/S)w_r*omega
```

at every normal order.  The orders decouple over the function field.  The
nonlinearity is exactly the triangular map back to finite Newton windows.
Relevant units: [`RMU-D25775A5`](../working-mathematics/units/RMU-D25775A5.md), [`JCG-3AE328D9`](../working-mathematics/units/JCG-3AE328D9.md).

The filtered residue adjoint represents the dual of every finite-window
cokernel by principal parts.  Matrix left-null vectors and residue
functionals are the same coordinates on this dual.  Relevant occurrence:
[`JCG-D44F2B27`](../working-mathematics/units/JCG-D44F2B27.md).  For the stored `(8,28)` face, the full-support maps are
injective for `r>=5` and have cokernel dimension `r-1` in the displayed range
([`RMU-9E33C04B`](../working-mathematics/units/RMU-9E33C04B.md)).

Ordinary finite formal Jacobian-one jets are polynomially realizable by
linear maps and shears.  This does not prove realization by the smaller
valuation-filtered approximate-root group.

### Lower-face operation gap

At layers `1,...,4`, the determinant-kernel dimensions are `(2,3,3,1)`.
Maximal support-admissible Laurent operations fill all four kernels.  Affine
polynomial operations have ranks `(2,3,2,1)`, whereas the manuscript's
complete-chain fixed-chart ranks are `(1,1,2,0)`.  The one layer-four residual
is the adjacent rechart

```text
Y -> Y+lambda*X^-4.
```

After removing it, the still-unclassified sequence is `(1,2,1,0)`.  These
dimensions are not known moduli or obstructions; they measure a missing
definition or classification of the admissible subgroup.

### The `F_2` branch

For every `m>=2`, the final face polynomial and degree-`2m` alternating Belyi
map are explicit and unique, with monodromy `A_(2m)`.  The local defect
equation has a nontrivial exact finite-support family, so local finite-order
lifting cannot eliminate the branch ([`JCG-C42D615F`](../working-mathematics/units/JCG-C42D615F.md)).  The natural five-band
global lift is impossible ([`JCG-42763317`](../working-mathematics/units/JCG-42763317.md)).

For `m=3`, the exact `C_5`-invariant supported jet reaches order 520.  Fresh
kernel parameters cancel the apparent order-510 and order-520 conditions
([`JCG-2533E53C`](../working-mathematics/units/JCG-2533E53C.md)).  The nonzero order-530 value was computed only on the slice
where newly available parameters vanish.  It is not a global obstruction.

## Tooling boundary

The recovered Lane 9 package proves finite wall-complex, operation-map,
transition, dual-transport, and `C_5` Fourier/Laurent identities and has six
passing structural tests.  The received bundle does not contain the actual
`F_2` matrices and blocks or the archived `C9` replay.  Its synthetic examples
test the interface; they do not prove a new statement about `F_2`.

## Exact live problem

First prove one actual two-chart correspondence theorem.  It must transport:

1. coefficient support windows;
2. the determinant operator and forcing term;
3. fixed-chart operation images;
4. the adjacent rechart tangent; and
5. every residue-adjoint functional.

Then recover the real `F_2` blocks and form the full two-sided Laurent or
block-Toeplitz system, decomposed by `C_5` character, with both support
endpoints and every kernel parameter retained.


## Useful deliverable

Return one self-contained mathematical artifact that advances or sharply
reformulates the exact live problem.  It may solve a listed task, isolate a
smaller exact subproblem, prove that an input is insufficient, produce a
counterexample to the proposed route, or develop a stronger connection with
another lane.  Include the exact statement, a complete argument or
reproducible computation contract, dependencies, and limitations.  A
rigorous partial result is useful; it need not close the whole lane.

## Tasks

### P6-L9A — Complete-chain subgroup in layers 1--4

Actor: `online_model`. Status: ready.

Define the admissible group and explain the fixed-chart ranks `(1,1,2,0)`.
Classify the remaining `(1,2,1,0)` quotient.

### P6-L9B — Actual one-wall theorem

Actor: `online_model`. Status: blocked on P6-L9A.

Instantiate the wall complex on the stored lower face and prove all five
transport statements above.

### P6-L9C — Full two-sided `F_2` attachment

Actor: `online_model`. Status: blocked on recovering the actual blocks.

Solve the global finite-support matching problem or produce a
parameter-independent left-syzygy obstruction.  Include cyclic descent,
affine bands, and adjacent charts.

## Do not do

- Do not call every divergence-free Laurent field an admissible
  complete-chain operation.
- Do not call a rechart fixed-chart gauge.
- Do not use the synthetic toolkit as evidence about the actual branch.
- Do not discard fresh kernel parameters or promote the order-530 slice.
- Do not infer polynomial termination from local formal integration.

The retained-unit and proof-source pages linked above are the public mathematical record for this lane.
