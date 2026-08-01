# Program 5 third-order rank-six audit

## Question

The deterministic formal-arc calculation sets the 22-dimensional tangent
kernel in each quadratic coefficient to zero and finds a nonzero cubic
residual.  This audit asks the stronger question: can any of the resulting

\[
22\dim \operatorname{Sym}^2\langle u,v\rangle=66
\]

quadratic tangent parameters remove that residual for the selected
two-dimensional first-order plane?

The selected directions are

\[
\theta_u=\eta_0+\xi_4,
\qquad
\theta_v=\eta_1+4\xi_0-24\xi_1-4\xi_4.
\]

Here \(\xi_i\) are the exported row-killing tangent vectors and
\(\eta_0,\eta_1\) are the explicit complement vectors constructed by the
tangent bridge.

## Exact calculation

On the fixed Schur chart, write the cubic-coordinate matrix in blocks and use

\[
F=D-CA^{-1}B.
\]

At parameter order three, the forcing is the sum of the five possible terms

\[
C_1G_0B_2+C_1G_1B_1+C_1G_2B_0+C_2G_0B_1+C_2G_1B_0,
\qquad G=A^{-1}.
\]

The adapter first constructs one quadratic solution for each of
\(v^2,uv,u^2\), then adds a general element of the 22-dimensional tangent
kernel to each.  After exact cokernel projection, only 24 scalar equations can
be nonzero.  The linear effect of the 66 free coefficients has

\[
\operatorname{rank}E=15,
\qquad
\operatorname{rank}[E\mid b]=16.
\]

Consequently \(Ex=b\) has no solution.  The implementation also recomputes
the full cubic forcing after each of the 66 individual tangent additions and
checks that every resulting column agrees with the closed bilinear formula.

## Exact obstruction certificate

The output includes a left-null vector \(w\) satisfying

\[
w^TE=0,
\qquad
w^Tb=-\frac{256}{3}\ne0.
\]

In the emitted coordinate convention, its only nonzero entries are

| parameter monomial | Schur row | Schur column | coefficient |
|---|---:|---:|---:|
| \(v^3\) | \(q\) | \(adq\) | \(1\) |
| \(v^3\) | \(k\) | \(bds\) | \(-8/3\) |

The normalized witness SHA-256 is
`8fcd1d848258112da813c47f4878cdacbecb59c9dd44ec80f44fb4636390c679`.

## Conclusion and boundary

The selected first-order plane does **not** extend through cubic parameter
order inside the modeled local rank-at-most-six Schur chart, even after all
quadratic tangent freedom is allowed.  This repairs the earlier deterministic
calculation's open logical gap: the cubic residual is intrinsic for this
plane.

This does not address other first-order tangent planes, a quartic equation,
all-order integration or convergence, the true source/target/stable operation
quotient, or a global noncompression theorem.  It is an exact computational
result for the 115-dimensional source-field operation model and the pinned
input whose SHA-256 is
`a2ec1fb45cc42b527958f3c881b8a9bb8c0ce093aa553c846806ab868513a2d8`.
It has automated exact-arithmetic regression coverage; it is not represented
as independent human-specialist review.

## Reproduction

With SymPy 1.14.0:

```bash
PYTHONPATH=research-tools python -m \
  filtered_operation_complex.adapters.program5_rank_six_third_order_lift \
  --output /tmp/program5-rank-six-third-order-lift.json

PYTHONPATH=research-tools python -m unittest discover \
  -s research-tools/filtered_operation_complex/symbolic_tests \
  -p 'test_*.py' -v
```
