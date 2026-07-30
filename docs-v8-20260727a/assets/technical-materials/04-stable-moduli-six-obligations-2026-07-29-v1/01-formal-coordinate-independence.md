# Obligation 1: Independence of local factorization coordinates

> **Status:** unrefereed, AI-assisted research note; no independent review recorded.  
> **Scope:** Program 4 normalized cubic-frame coefficient spaces. The statements do not identify the construction with the fppf orbit quotient or the full unrigidified stable left-right stack.

[Back to the six-obligation index](index.md)


## Theorem 1.1 — Canonical formal escape chart

Fix `N=d+m`. Invert `q_d`, and complete the source coefficient space along the exact length-`d` locus. There is a unique factorization

\[
\widehat Q_N=\widehat Q_dE_m,
\]

with

\[
E_m(z)=z^m+e_1z^{m-1}+\cdots+e_m,
\qquad E_m\equiv z^m
\]

modulo the ideal of the exact stratum. There is also a unique decomposition

\[
P=E_mP_d+\widehat Q_dS,
\qquad
\deg P_d<d,
\quad
\deg S<m.
\]

Consequently the formal completion has a canonical product presentation

\[
\widehat X_{N,C_d}
\simeq
\widehat X_d
\widehat\times
\operatorname{Spf}
 k[[e_1,\ldots,e_m,s_0,\ldots,s_{m-1}]],
\]

where `S=s_0+s_1z+...+s_{m-1}z^{m-1}`. This construction commutes with arbitrary base change of the completed exact stratum.

### Proof

Let `M_n` denote the affine scheme of monic degree-`n` polynomials. Consider multiplication

\[
\mu:M_d\times M_m\longrightarrow M_N,
\qquad
(F,G)\longmapsto FG.
\]

At `(\widehat Q_d,z^m)`, the tangent map is

\[
(\delta F,\delta G)
\longmapsto
z^m\delta F+\widehat Q_d\delta G.
\]

Modulo `z^m` and modulo `\widehat Q_d`, this is the Chinese-remainder map. Its determinant is the resultant

\[
\operatorname{Res}(\widehat Q_d,z^m)
=\widehat Q_d(0)^m=q_d^m,
\]

which is a unit. Hence `\mu` is etale at the exact stratum. The formal inverse gives the unique Hensel factorization separating the punctual cluster at `z=0` from the residual factor. Uniqueness gives compatibility with all base changes.

The same resultant condition gives the Chinese-remainder decomposition

\[
\mathcal O[z]/(\widehat Q_dE_m)
\simeq
\mathcal O[z]/(\widehat Q_d)
\oplus
\mathcal O[z]/(E_m).
\]

Taking the unique degree-bounded representatives gives

\[
P=E_mP_d+\widehat Q_dS.
\]

Again uniqueness gives base-change compatibility. ∎

## Corollary 1.2 — Canonical weighted normal filtration

The punctual-factor coefficients have normal weights

\[
\operatorname{wt}(e_i)=i,
\qquad 1\le i\le m.
\]

In the `c`-coordinate principal-part convention, the coefficients of `S` have weights

\[
2,3,\ldots,m+1.
\]

After reversing their order to match the `z`-principal-part ordering, the simultaneous direction weights are

\[
(1,2,\ldots,m;\,m+1,m,\ldots,2).
\]

The direct coefficient tails

\[
(q_{d+1},\ldots,q_N;
 r_{N-1},\ldots,r_d)
\]

and the Hensel coordinates

\[
(e_1,\ldots,e_m;
 s_{m-1},\ldots,s_0)
\]

are related by a triangular, filtration-preserving formal coordinate change with invertible diagonal after `q_d` is inverted. Therefore the weighted normal cone and the corresponding stacky weighted projectivization are independent of the local factorization presentation.

## Corollary 1.3 — Exact-stratum cocycles

Whenever a punctual factor further splits into coprime monic factors, the transition maps satisfy every pairwise and triple cocycle identity.

### Reason

All transitions are obtained from the unique factorization of a monic polynomial and the unique Chinese-remainder decomposition of `P`. Associativity of polynomial multiplication and uniqueness of remainder imply the cocycle.

This statement stops at a simultaneous collision, where the subfactors cease to be coprime. Section 3 shows that the direct collision chart and an ordered refinement are then different birational models.

## Low-rank check

For `N=3,d=1,m=2`, let

\[
\widehat Q_d=z+q,
\qquad
E_2=z^2+e_1z+e_2.
\]

Then

\[
\widehat Q_dE_2
=z^3+(q+e_1)z^2+(qe_1+e_2)z+qe_2.
\]

The Jacobian from `(q,e_1,e_2)` to the three monic coefficients has determinant `q^2` at `e_1=e_2=0`, exactly as predicted by the resultant.

---
