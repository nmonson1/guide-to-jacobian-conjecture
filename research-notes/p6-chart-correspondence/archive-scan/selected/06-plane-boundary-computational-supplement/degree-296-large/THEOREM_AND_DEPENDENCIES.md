# Exact theorem and dependency boundary

## Unconditional theorem for the six displayed polynomials

Let

\[
K=\mathbf Q(u),\qquad u^5-u^4+3u^3+3u^2+26=0,
\]

and let

\[
\rho=F_4,\qquad (g_1,g_2,g_3,g_4,g_5)=(F_6,F_8,F_9,F_{10},F_{11})
\]

be the six exact polynomials in `inputs/handoff-lite/layer-calculation/full_exact_fivevar_w8.json`.
At the prime `p=2053`, with `u=216`, the five equations `g_1,...,g_5` are
BKK-nondegenerate: every one of the 344 proper faces of the Minkowski sum
has root-free initial system in the algebraic torus.  The mixed volume is 296.
The resulting special algebra is reduced of dimension 296, every coordinate
is invertible, and multiplication by `rho` has determinant 682.

Localizing the coefficient ring at `(2053,u-216)` therefore gives a finite
etale scheme of rank 296, and `rho` is a unit on it.  Consequently

\[
V(\rho,g_1,g_2,g_3,g_4,g_5)(\overline K)=\varnothing.
\]

This characteristic-zero conclusion does not depend on a heuristic modular
lift: the projective toric compactification is proper, the full special fiber
is the reduced 296-point torus scheme, all boundary initial systems are
root-free, and the etale locus containing the special fiber must be the entire
finite scheme over the local DVR.

## Imported dependencies for the Keller interpretation

The exact polynomial theorem above does **not** by itself establish that every
terminal `(8,28)` Keller gluing is covered.  That interpretation additionally
uses the imported claims that:

1. the lower-face reconstruction and first four normal-layer reductions are exhaustive;
2. the vertex-saturated normalization covers the relevant terminal case;
3. the fifteen equations reconstructed by the residue audit are the complete
   normal-jet compatibility coordinates after those normalizations; and
4. the chosen six equations are a valid contradiction subsystem of that full model.

The package does not audit the earlier reduction from an arbitrary below-125
Keller pair to this terminal model, and it does not prove the degree-125 theorem
or the plane Jacobian conjecture.
