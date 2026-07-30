---
title: "Program 3 v13 corrigendum"
description: "Proof repairs and corrected evidence boundaries for the v13 Program 3 manuscript."
---

<p class="claim-tag">Program 3 · Corrigendum to v13</p>

# Corrigendum and proof repairs for Program 3

<p class="dek">The degree-seven theorem spine is unchanged. This note repairs two proof-exposition gaps, replaces the converse proof of the degree-eight shear classification, withdraws an unsupported characteristic-zero degree-eight conclusion, and clarifies the dependency of the border presentation.</p>

## Pinned object and review boundary

The reviewed artifact is [*Filtered Rigidity of the Degree-Seven Jacobian Counterexample*, v13](../assets/manuscripts/03-filtered-rigidity-2026-07-29-v13.pdf), SHA-256

```
18f4658390d0a9566056aee505c3fb5039d17969368cb2f544a44e6ba956f427
```

The release metadata date is 29 July 2026; the PDF title page prints 22 July 2026. The audit used exact rational symbolic spot-checks and proof analysis. It is not independent human specialist review and is not a second-CAS reproduction of the large certificates.

The full assessment and replay source are preserved in the repository under `assessments/`.

## 1. Irreducibility in Proposition 2.1

Let

\[
p(v)=cv^3-2v^2+bv-2a\in\mathbb C(a,b,c)[v].
\]

Set \(K=\mathbb C(b,c)\), and let \(\nu_\infty\) be the valuation of \(K(a)\) at \(a=\infty\), normalized by \(\nu_\infty(a)=-1\). Suppose \(r\in K(a)\) were a root, and put \(m=\nu_\infty(r)\in\mathbb Z\).

For \(m\geq0\), the first three terms of \(p(r)\) have nonnegative valuation, while \(-2a\) has valuation \(-1\); the least valuation occurs only once. For \(m<0\), the four valuations are

\[
3m,\qquad 2m,\qquad m,\qquad -1.
\]

The first three are strictly increasing. Cancellation of the least-valuation term would require \(3m=-1\), impossible for integral \(m\). Thus the cubic has no root in \(K(a)\), hence is irreducible. Together with the nonsquare discriminant already calculated in v13, this gives normal-closure group \(S_3\); the corresponding cubic subextension has trivial automorphism group because \(N_{S_3}(S_2)/S_2=1\).

## 2. Finite type versus completion in Theorem 4.3

Let \(X=S\) be the finite-type affine slice at \(G\). Formal implicit elimination gives a torus-equivariant isomorphism

\[
\widehat{\mathcal O}_{X,G}
\simeq
\mathbb C[[u_1,\ldots,u_{10}]]/I_\kappa.
\]

For each positive-, zero-, and negative-weight coordinate subspace \(V_+,V_0,V_-\), completion commutes with the corresponding closed intersection. Proposition 4.2 makes each completed local intersection Artinian. Completion is faithfully flat and preserves Krull dimension for Noetherian local rings, so each finite-type local germ \((X\cap V_\epsilon,G)\) is zero-dimensional. Lemma 4.1 therefore applies to the finite-type slice, and the completed radical is the maximal ideal.

## 3. Replacement proof of Theorem C.2

For a homogeneous quadratic \(f\), put

\[
\phi_f(x,y,z)=(x,y,z+f(x,y)),\qquad G_f=G\circ\phi_f,
\]

and write \(A_\tau=\operatorname{diag}(\tau^{-1},\tau,\tau^2)\).

For nonzero homogeneous quadratics \(f,g\),

\[
G_f\sim_{\mathrm{aff}}G_g
\quad\Longleftrightarrow\quad
 g(x,y)=\tau^2f(\tau x,\tau^{-1}y)
\quad\text{for some }\tau\in\mathbb C^\times.
\]

The displayed relation is induced by conjugation with the stabilizer torus, so it gives affine equivalence. Conversely, suppose affine automorphisms \(\alpha\) of the source and \(\beta\) of the target satisfy

\[
G_f\circ\alpha=\beta\circ G_g.
\]

The maps \(G_f,G_g,G\) have the same image and omitted curve \(\Gamma\), because \(\phi_f\) and \(\phi_g\) are source automorphisms. Hence \(\beta(\Gamma)=\Gamma\), and the target part of Proposition 2.1 gives \(\beta=A_\mu\) for some \(\mu\in\mathbb C^\times\). Equivariance gives

\[
G\circ\phi_f\circ\alpha=G\circ A_\mu\circ\phi_g.
\]

The generic cubic extension of \(G\) has trivial deck group, so

\[
\phi_f\circ\alpha=A_\mu\circ\phi_g.
\]

Consequently

\[
\alpha(x,y,z)=
\left(
\mu^{-1}x,\mu y,
\mu^2z+\mu^2g(x,y)-f(\mu^{-1}x,\mu y)
\right).
\]

The final two terms are homogeneous quadratic. Thus \(\alpha\) is affine exactly when

\[
\mu^2g(x,y)=f(\mu^{-1}x,\mu y).
\]

Putting \(\tau=\mu^{-1}\) gives the stated relation. Conversely, that relation makes the displayed \(\alpha\) linear. On the coefficient basis \((x^2,xy,y^2)\), the torus weights are \((4,2,0)\), so the generic orbit has dimension one and the generic quotient dimension is two.

The v13 sentence asserting that an arbitrary affine equivalence preserves the degree-seven truncation is deleted.

## 4. Corrected degree-eight residual statement

!!! danger "Withdrawal of the v13 characteristic-zero conclusion"
    The final first-normal obstruction conclusion of Theorem C.3 is not established over characteristic zero and is withdrawn. The exact proved boundary is the statement below.

In the named 28-variable residual Kuranishi calculation, the residual tangent weights are \(-2\) and \(-1\). The weight \(-2\) sector is eliminated exactly over \(\mathbb Q\): successive equations include

\[
u_0u_1=0,\qquad 100u_0u_1+9=0.
\]

The weight \(-1\) sector survives through parameter order four over \(\mathbb Q\). Later death calculations are modular evidence only. They do not establish over characteristic zero that every first-normal direction is obstructed, and they do not prove that the reduced residual germ is the union of the known affine, source-shear, and target-shear components.

Accordingly:

- the v13 assertion of exact order-six and order-seven rejection in weight \(-1\) is withdrawn;
- the final conclusion of Theorem C.3 and the claim in Remark C.5 that it is exact are withdrawn;
- [JCG-24C82405](../claims/JCG-24C82405.md) is corrected and superseded by the evidence boundary in [JCG-D3F76EBC](../claims/JCG-D3F76EBC.md) together with the restricted-slice warning [JCG-02C45EB8](../claims/JCG-02C45EB8.md);
- full characteristic-zero orbit saturation remains open, including arcs that bend out of a previously analyzed restricted slice.

## 5. Dependency of Appendix D

Let \(J\) be the border-relation ideal. Commuting multiplication matrices show

\[
\dim_{\mathbb Q}S/J\leq584.
\]

The printed proof obtains \(J\subseteq I_\kappa\) by pairing the border relations against 584 rational inverse-system functionals. This inference is available only after those functionals are known to span the full inverse system \(I_\kappa^\perp\), which in the paper uses the already-established equality \(\dim S/I_\kappa=584\).

Thus Appendix D is a valid exact presentation and consistency check after the length theorem. As written, it is not an independent upper-bound proof. Independence would require direct exact reductions of all border relations into \(I_\kappa\), or an equivalent exact row-space membership certificate that does not use the completed length or fullness of the inverse system.

## Status after repair

| Item | Status |
| --- | --- |
| Degree-seven reduced affine rigidity | Unchanged; computer-assisted, pending independent CAS and specialist review |
| Length 584 and Hilbert function | Unchanged; exact certificate package, pending independent reproduction |
| Type 60 and 36 minimal generators | Unchanged; exact certificate package, pending independent reproduction |
| Proposition C.1 | Unchanged |
| Theorem C.2 | Retained with the replacement proof above |
| Theorem C.3 | Withdrawn beyond exact weight \(-2\) elimination and exact order-four weight \(-1\) persistence |
| Appendix D | Retained as an exact post-length presentation; not independent as printed |

## Remaining release gates

1. Reproduce the degree-seven radical certificate, \(H(6)=86\), and uniqueness of the sextic initial class in Singular or Macaulay2 from independently derived equations.
2. Replace the v13 PDF in a subsequent manuscript release rather than relying indefinitely on this overlay corrigendum.
3. Correct the canonical private claim source for `JCG-24C82405`; this public page is a release hotfix and will otherwise be overwritten by regeneration.
4. Add direct Kuranishi-ideal membership certificates for the border relations before presenting Appendix D as an independent upper bound.

[Back to the Program 3 overview](programs/local-rigidity-and-deformation-algebra.md)
