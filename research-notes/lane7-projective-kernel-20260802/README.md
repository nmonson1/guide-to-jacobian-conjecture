# Lane 7 projective-kernel interface and exact CAS harness

This note records the marking-open condition on the projective kernel incidence
and provides a reproducible route from the hash-pinned public packet to exact
computer-algebra inputs. It does **not** promote any of the unresolved
component or first-normal claims without exact certificates.

Throughout, indices run from `0` to `4`. Let

\[
A_0=\mathbf Q[a_0,\ldots,a_6],\qquad
M\in\operatorname{Mat}_{10\times5}(A_0),\qquad d=\det T.
\]

The split-incidence theorem in the public Lane 7 packet gives, on `D(d)`,

\[
M(a)u=0,\qquad v=-d^{-1}C(a)A(a)u.
\]

Put

\[
B(a)=C(a)A(a)\in\operatorname{Mat}_{5\times5}(A_0).
\]

## Transport of the marking-open condition

For a pair of marking vectors define the Pluecker coordinates

\[
\eta_{ij}=u_i v_j-u_j v_i,\qquad 0\le i<j\le4.
\]

The formerly normalized chart has `v_4=1`. Its published open factor is

\[
u_3-u_4v_3=\eta_{34}.
\]

On the projective kernel incidence define the homogeneous quadratic forms

\[
\Phi_{ij}(a,u)=u_i(B(a)u)_j-u_j(B(a)u)_i.
\]

Substitution of the exact reconstruction formula gives the polynomial identity

\[
\boxed{d\,\eta_{ij}=-\Phi_{ij}}.
\]

Consequently, on `D(d)`,

\[
D(\eta_{ij})=D(\Phi_{ij}).
\]

In particular, the marking-open condition from the published `v_4=1` chart
transports to

\[
D(d)\cap D(\Phi_{34})
\]

inside the projective kernel incidence `P(ker M)`.

## Complete chart cover

The pair `(u,v)` is independent exactly when `u wedge v` is nonzero, equivalently
when at least one of the ten coordinates `eta_ij` is nonzero. Hence every
independent marking pair belongs to at least one member of the unconditional
cover

\[
\bigcup_{0\le i<j\le4}D(\eta_{ij})
 =
\bigcup_{0\le i<j\le4}D(\Phi_{ij})
\qquad\text{on }D(d).
\]

On `D(eta_ij)` the standard normalized basis of the marked plane is

\[
p_r=\frac{\eta_{rj}}{\eta_{ij}},\qquad
q_r=\frac{\eta_{ir}}{\eta_{ij}},
\]

so that `p_i=1`, `p_j=0`, `q_i=0`, and `q_j=1`. The five quadratic
Grassmann--Pluecker relations hold automatically because the coordinates arise
from `u wedge v`.

This ten-chart cover is sufficient. No change of basis of `(u,v)` is asserted
to preserve the full collision equations, and no unrecorded ambient symmetry
is used to identify different coordinate-pair charts. A reduction to one chart
would require a separately verified symmetry acting transitively on the ten
pairs.

## Reproduction

Extract the exact matrices from the public packet and verify their printed
SHA-256 values:

```bash
python research-notes/lane7-projective-kernel-20260802/extract_embedded_sources.py \
  --output-dir build/lane7-sources \
  lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json \
  lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json
```

Verify all ten chart formulas and the reconstruction transport:

```bash
python -m pip install 'sympy==1.14.0'
python research-notes/lane7-projective-kernel-20260802/test_plucker_transport.py
```

Generate a standalone Macaulay2 input over `QQ` or a finite field:

```bash
python research-notes/lane7-projective-kernel-20260802/generate_macaulay2_input.py \
  build/lane7-sources build/lane7-qq-local.m2 --with-localizer
```

The auxiliary variable `z` imposes `z*d-1`, so computations in the generated
ring take place on `D(d)` without replacing saturation by an undocumented
heuristic.
