# Exact input contract for the `Q4-F4` compatibility problem

## Status

This document specifies the minimum data needed for an auditable elimination
of the surviving Lane 4 terminal system. It is deliberately fail-closed.

The sanitized public sources currently state that the exceptional branch has

\[
r=3,\qquad\text{Hilbert--Burch type }(3,4),
\]

that a generic first-normal determinant contains

\[
9216\tau^3(\tau^2+2\tau+3)(3\tau^2+2\tau+1),
\]

and that the remaining weighted-inflection family must be studied over

\[
\mathbf Q(\tau)[d]/(q_4(d,\tau)).
\]

They do **not** publish, in one reconstructible artifact, the polynomial
\(q_4\), the corresponding normalized forms \(P,Q,R\), the complete gauge
choices, every allowed coefficient of \(H_3,H_2,L\), or every factor inverted
on the `F4` chart. The public manuscript itself says that no attached
auditable program completes the extension-field solve.

Consequently this contribution does not manufacture an `F4` checker from
descriptive prose. An elimination result is admissible only after a complete
instance of `f4-contract.schema.json` has been supplied and independently
reconstructed from the stated geometric normal form.

## 1. Required mathematical payload

A complete instance must contain all of the following.

| Block | Required content |
| --- | --- |
| Provenance | Exact source commit, source paths, SHA-256 digests, and the derivation locator for every displayed formula. |
| Coefficient field | The explicit polynomial \(q_4(d,\tau)\), its variable order, the characteristic-zero base field, and the open set on which the quoted irreducibility/minimal-polynomial statement is used. |
| Leading data | Exact binary forms \(P(\tau,d;x,y)\), \(Q(\tau,d;x,y)\), and \(R(\tau,d;x,y)\), together with direct checks of degrees, \(\gcd(P,Q)=1\), Hilbert--Burch type \((3,4)\), and ramification degree \(3\). |
| Lower layers | The most general \(H_3,H_2\) and linear part \(L\) still allowed after the normalizations. Every coefficient removed by a source or target stabilizer must be listed with the transformation that removes it. |
| Open chart | One product \(S\) containing every pivot, denominator, discriminant, resultant, and rank minor inverted in reaching `F4`. |
| Complements | A named owner or independently saturated system for every irreducible factor of \(S\), including intersections where the rank profile changes. |
| Keller layers | A canonical definition of \(D_j=[\deg j](\det JF-\det L)\), or equivalently the coefficient convention in the determinant arc, and the exact list of layers already solved before `D6`. |
| Reconstruction tests | At least two exact sample parameters, including one already reported obstruction, with expected coefficient vectors and hashes. |

The linear part may be normalized to the identity only if the supplied
source/target actions prove that this normalization preserves the `F4` chart
and all lower-layer freedom. Otherwise \(L\) must remain a general invertible
matrix and the ideal must include an auxiliary equation
\(u\det(L)-1\).

## 2. Canonical ring and symbol order

The intended generic coordinate ring is

\[
R_0=\mathbf Q[\tau,d,\mathbf a,\mathbf b,\boldsymbol\ell,u]/
       (q_4(d,\tau),\,uS\det L-1),
\]

where:

- \(\mathbf a\) are the coefficients not eliminated from \(H_3\);
- \(\mathbf b\) are the coefficients not eliminated from \(H_2\);
- \(\boldsymbol\ell\) are the entries not eliminated from \(L\);
- \(S\) is the full open-factor product.

A contract instance must give one immutable symbol order for polynomial
serialization and Gröbner reduction. All hashes must be computed from that
canonical serialization, not from pretty-printed CAS output.

## 3. Elimination protocol

### Stage A — solve `D6` as a module

Separate the coefficients that occur linearly in `D6` and write

\[
M_6(\tau,d)\,u=b_6(\tau,d).
\]

Compute:

1. the generic rank of \(M_6\);
2. the relevant Fitting ideals controlling rank drops;
3. an exact parametrization
   \[
   u=u_0(\tau,d)+N(\tau,d)\lambda
   \]
   on the stated open set;
4. a substitution check reproducing every coefficient of `D6`.

No pivot division may be hidden. Each pivot factor belongs in \(S\), and its
zero locus is a separate child.

### Stage B — test all `D5` cancellations in the cokernel

After the full `D6` solution is substituted, split

\[
D_5=\omega(\tau,d,\lambda)+T(\tau,d,\lambda)v,
\]

where \(v\) consists of every still-free lower coefficient that could cancel
the reported obstruction. Cancellation is possible exactly when

\[
[\omega]=0\quad\text{in}\quad\operatorname{coker}T.
\]

Preferred certificates are:

- a symbolic left-kernel vector \(\ell T=0\) with
  \(\ell\omega\) invertible on the chart; or
- maximal minors of the augmented matrix \([T\mid\omega]\) proving
  \(\operatorname{rank}[T\mid\omega]>\operatorname{rank}T\).

A coefficient obstruction obtained after setting any allowed component of
\(v\) to zero is not a certificate for the unrestricted branch.

### Stage C — saturation certificate

Let \(I\) be generated by

- \(q_4(d,\tau)\);
- the complete coefficients of `D6` and `D5`;
- the normal-form relations;
- the equation \(uS\det L-1\).

The generic `F4` chart is empty exactly when

\[
1\in I
\]

in this localized presentation, equivalently when some power \(S^N\) lies in
the unlocalized ideal. The final artifact should contain a compact exact
Nullstellensatz or Gröbner-reduction certificate and an independent verifier
that checks the certificate over \(\mathbf Q\).

Finite-field computations are appropriate for discovering ranks, monomial
orders, and certificate support. They are not the final characteristic-zero
proof.

### Stage D — exceptional factors

Every factor of \(S=0\) is recomputed from its own polynomial system. It must
not be obtained by substituting zero into a formula derived after division by
that factor. Intersections of exceptional factors are separate whenever the
matrix rank or stabilizer dimension changes.

### Stage E — a surviving component

If the saturated `D6`/`D5` ideal is not the unit ideal, compute a primary
component or rational univariate representation and continue with
\(D_4,D_3,\ldots\). A solution of the first two remaining layers is only a
candidate jet. It becomes a candidate Keller map only after all determinant
layers, invertibility of \(L\), and every inherited chart hypothesis have
been checked.

## 4. Acceptance checklist

An `F4` elimination PR is ready for mathematical review only when all answers
below are “yes.”

- [ ] Is `q4(d,tau)` printed explicitly and hash-pinned?
- [ ] Are `P,Q,R` printed explicitly and independently reconstructed?
- [ ] Are all unrestricted coefficients of `H3,H2,L` present?
- [ ] Is every gauge removal justified by an explicit invertible action?
- [ ] Is the complete open-factor product `S` printed?
- [ ] Does every factor of `S=0` have a named owner or separate saturation?
- [ ] Is `D6` solved without an unrecorded pivot division?
- [ ] Is the `D5` obstruction tested modulo the image of all cancellation variables?
- [ ] Is the final characteristic-zero certificate independently verified?
- [ ] Are sample values used only as reconstruction tests, not as generic proof?

Until these items are supplied, `Q4-F4` remains an exact research target but
not a publicly reconstructible finite system.
