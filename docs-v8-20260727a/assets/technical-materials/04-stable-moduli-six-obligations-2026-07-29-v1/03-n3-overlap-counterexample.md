# Obligation 3: Exact `N=3` direct-versus-iterated overlap

> **Status:** unrefereed, AI-assisted research note; no independent review recorded.  
> **Scope:** Program 4 normalized cubic-frame coefficient spaces. The statements do not identify the construction with the fppf orbit quotient or the full unrigidified stable left-right stack.

[Back to the six-obligation index](index.md)


The hoped-for equality of direct and iterated charts fails already for a two-root escape.

## 3.1 Direct two-root chart

Let

\[
E_2(z)=z^2+\beta z+\gamma,
\qquad
S(z)=s_0+s_1z.
\]

The direct simultaneous exceptional factor is

\[
\mathbb P(1,2,3,2)
\]

with coordinates `(beta,gamma,s_0,s_1)`. On its `beta` chart, write

\[
\gamma=\beta^2u,
\qquad
s_0=\beta^3v,
\qquad
s_1=\beta^2w.
\]

After suppressing the common scale, the direct chart is

\[
D=\operatorname{Spec}k[u,v,w].
\]

## 3.2 Derivation of the nested coordinate

At `u=0`,

\[
E_2=z(z+\beta).
\]

Decompose the principal polynomial uniquely as

\[
s_0+s_1z
=z\,p+(z+\beta)g.
\]

Solving gives

\[
g=\frac{s_0}{\beta},
\qquad
p=s_1-\frac{s_0}{\beta}.
\]

Under the direct-chart scaling,

\[
g=\beta^2v,
\qquad
p=\beta^2(w-v).
\]

Thus `w-v` is the residual lower-length decoration and `v` is the normalized one-root gauge.

The small root of

\[
z^2+\beta z+\beta^2u
\]

is

\[
z_{\mathrm{small}}=-\beta u+O(u^2).
\]

Hence `u` is the small-root scale relative to `beta`. Since the gauge has weight two, the nested direction is

\[
\frac{v}{u^2}.
\]

## Proposition 3.1 — The iterated chart is a nontrivial blowup

The graph closure of the nested direction

\[
[u^2:v]
\]

is

\[
\widetilde D
=
\operatorname{Bl}_{(u^2,v)}D.
\]

It is the closed subscheme of

\[
D\times\mathbb P^1_{[U:V]}
\]

with equation

\[
Uv-Vu^2=0.
\]

The map

\[
\pi:\widetilde D\longrightarrow D
\]

is an isomorphism away from `V(u,v)`, while its fiber over every point of `V(u,v)` is `P^1`. Therefore the direct and iterated charts are not scheme-theoretically isomorphic.

### Proof

The ideal `(u^2,v)` is a complete intersection. Its Rees algebra is

\[
k[u,v,w,U,V]/(Uv-Vu^2).
\]

After setting `u=v=0`, the relation disappears, so the homogeneous fiber is

\[
\operatorname{Proj}k[U,V]=\mathbb P^1.
\]

The direct affine chart has one point over the same base point. ∎

## Corollary 3.2 — Correct overlap statement

The direct simultaneous compactification and the ordered refinement agree only away from the nested center. The correct relation is a contraction

\[
\widetilde D\longrightarrow D,
\]

not equality.

The multi-graph `\mathfrak G_N` retains both factors. Projection to the direct factor is the blowdown; retaining the nested factor gives the common refinement.

This is a structural counterexample to the original overlap claim, not a failure of separatedness or representability of the corrected object.

---
