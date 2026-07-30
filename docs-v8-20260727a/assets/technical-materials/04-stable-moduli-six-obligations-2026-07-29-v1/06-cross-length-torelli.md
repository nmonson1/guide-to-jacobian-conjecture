# Obligation 6: Intrinsic comparison across changing lengths

> **Status:** unrefereed, AI-assisted research note; no independent review recorded.  
> **Scope:** Program 4 normalized cubic-frame coefficient spaces. The statements do not identify the construction with the fppf orbit quotient or the full unrigidified stable left-right stack.

[Back to the six-obligation index](index.md)


## Theorem 6.1 — Exact-stratum residual contraction and intrinsic gluing

On the exact `N=d+m` stratum with `q_d` invertible, Euclidean division gives a regular, base-change-compatible map

\[
\rho_{N,d}:(Q,R)\longmapsto(Q_d,R_d).
\]

The associated special cubic-frame map is ordinarily polynomially left-right equivalent to the lower-length map associated with `(Q_d,R_d)`. Under the same equivalence, the normalized relative-Jacobian chart and its marked divisor are carried isomorphically to the lower-length chart.

### Proof

Write

\[
R=R_d+Q_dS.
\]

Then

\[
B=B_d+c^2Q_dS
=B_d+3A\left(\frac{cS}{3}\right).
\]

The polynomial root translation removes the principal part. On the normalized relative-Jacobian chart, the accompanying coordinate change

\[
T=t+\frac{cS}{3}
\]

identifies `H=3At+B` and the content divisor, by Theorem 4.2. ∎

## Corollary 6.2 — Exact overlap cocycle

For a chain of exact escapes

\[
N\to d_1\to d_2,
\]

the direct residual contraction equals the composite contraction, and the relative-Jacobian coordinate changes compose correctly.

### Reason

The coefficient statement is associativity of monic factorization and Euclidean division. The intrinsic statement follows because the root-translation parameters add and `H` is preserved at every step.

## Proposition 6.3 — Fixed-length Torelli sees the special orbit, not the graph direction

Assuming the fixed-frame Torelli theorem, two points on an exact contact stratum have stably equivalent special fibers precisely when their residual lower-length data agree up to the stated scaling and finite-root gauge.

The weighted escape direction is extra degeneration information and is invisible to the special orbit.

## Proposition 6.4 — The comparison is necessarily noninjective

At a one-root wall, consider DVR arcs

\[
\epsilon=\tau,
\qquad
 y=\lambda\tau^{N+2}.
\]

Their graph limits are

\[
[\epsilon^{N+2}:y]=[1:\lambda].
\]

Different `lambda` give different graph-boundary points, but every arc has the same special bounded coefficient point

\[
\epsilon=y=0
\]

and the same residual lower-length special orbit.

The `N=3` blowup from Proposition 3.1 is stronger: an exceptional `P^1` is contracted by the direct and orbit-class comparisons.

Therefore a map from the degeneration stack to a moduli problem whose objects are only special-fiber stable left-right classes cannot be radicial or injective.

## Proposition 6.5 — Fixed-length stacks cannot simply be disjointly united

A connected DVR family whose generic fiber has length `N` and special fiber has length `d<N` cannot map fiberwise to

\[
\coprod_{j=0}^N\mathcal B_j,
\]

because each component of a disjoint union is open and closed. Cross-length moduli requires one stack in which the fixed-length loci are strata, not disconnected components.

## 6.6 Correct framed target

The finite-cover technical note identifies fixed-length coefficient data, modulo residual scaling, with normalized Tschirnhausen-framed finite triple completions. This suggests the following definition:

\[
\mathcal E_N^{\mathrm{fr}}
=
[\mathfrak G_N^{\mathrm{RJ}}/\mathbb G_m].
\]

An object is a normalized framed finite completion together with:

1. all direct and nested weighted root-contact directions;
2. all corresponding principal-part directions;
3. the base-change-compatible ideals `(Q,B)` and `(Q,B^2)`;
4. their relative-Jacobian flattening/marked-divisor data.

At the framed level, this is equivalent by construction to the coefficient multi-graph plus the relative-Jacobian enhancement. It gives a precise intrinsic meaning to the retained degeneration directions.

It is **not** the unrigidified left-right stack. Two obstructions remain:

- graph directions are intentionally finer than special orbit classes;
- the unrigidified stable groupoid has large infinitesimal and inert stabilization automorphisms.

The remaining unframed theorem is therefore:

> Determine whether a family-valued polynomial left-right equivalence lifts, after the stated rigidification, uniquely to an isomorphism of expanded framed completions.

Theorem 5.1 removes the ordinary hidden automorphism ambiguity on the positive-length coprime unit locus. It does not by itself settle family-valued descent or inert stabilization.

---
