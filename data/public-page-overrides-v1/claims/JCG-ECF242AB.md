---
title: "Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic f gives a three-parameter source-shear family, and F_f and F_g are affinely equivalent exactly when g(x,y)=tau^2 f(tau x,tau^-1 y) within this family."
description: "Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic f gives a three-parameter source-shear family, and F_f and F_g are affinely equivalent exactly when g(x,y)=tau^2 f(tau x,tau^-1 y) within this family."
---

<p class="claim-tag">JCG-ECF242AB</p>
# Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic f gives a three-parameter source-shear family, and F_f and F_g are affinely equivalent exactly when g(x,y)=tau^2 f(tau x,tau^-1 y) within this family.

<p class="dek">Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic f gives a three-parameter source-shear family, and F_f and F_g are affinely equivalent exactly when g(x,y)=tau^2 f(tau x,tau^-1 y) within this family.</p>

<span class="status status-kind">Claim</span> <span class="status status-draft">Proof offered — review pending</span> <span class="status">Core</span>

## Exact statement

Degree-eight affine rigidity fails: composing G with z -> z+f(x,y) for quadratic f gives a three-parameter source-shear family, and F_f and F_g are affinely equivalent exactly when g(x,y)=tau^2 f(tau x,tau^-1 y) within this family.

Statement version `1`. The public tag is stable; the proof below replaces one invalid sentence in the v13 proof without changing the statement.

## Repaired proof

For a homogeneous quadratic `f`, write

\[
\phi_f(x,y,z)=(x,y,z+f(x,y)),\qquad G_f=G\circ\phi_f,
\]

and let \(A_\tau=\operatorname{diag}(\tau^{-1},\tau,\tau^2)\). Conjugation by the stabilizer torus proves the reverse implication directly.

For the converse, suppose affine automorphisms \(\alpha\) of the source and \(\beta\) of the target satisfy

\[
G_f\circ\alpha=\beta\circ G_g.
\]

Because \(\phi_f\) and \(\phi_g\) are source automorphisms, \(G_f,G_g\), and \(G\) have the same image and omitted curve \(\Gamma\). Hence \(\beta(\Gamma)=\Gamma\), so the target-stabilizer result gives \(\beta=A_\mu\) for some \(\mu\in\mathbb C^\times\). Equivariance and the trivial generic deck group give

\[
\phi_f\circ\alpha=A_\mu\circ\phi_g.
\]

Thus

\[
\alpha(x,y,z)=
\left(
\mu^{-1}x,\mu y,
\mu^2z+\mu^2g(x,y)-f(\mu^{-1}x,\mu y)
\right).
\]

The last two terms are homogeneous quadratic, so \(\alpha\) is affine exactly when

\[
\mu^2g(x,y)=f(\mu^{-1}x,\mu y).
\]

With \(\tau=\mu^{-1}\), this is

\[
g(x,y)=\tau^2f(\tau x,\tau^{-1}y).
\]

The converse follows from the same displayed formula. The coefficient weights on \((x^2,xy,y^2)\) are \((4,2,0)\), so the generic quotient dimension is two.

The v13 sentence claiming that an arbitrary affine equivalence preserves the degree-seven truncation is deleted; source translations of degree-eight terms can create degree-seven terms.

## Appears in

- [Degree Eight Deformations](../collections/degree-eight-deformations.md) — defining, supporting result

## Proof access and evidence boundary

- [Program 3 v13 corrigendum](../research/program-3-v13-corrigendum.md): replacement proof and exact symbolic replay boundary.
- The statement remains proof-offered and has no recorded independent specialist review.

**Independent review**

- None Recorded: No independent review is represented in this public record.

[Browse all claims](../results/all-claims.md)
