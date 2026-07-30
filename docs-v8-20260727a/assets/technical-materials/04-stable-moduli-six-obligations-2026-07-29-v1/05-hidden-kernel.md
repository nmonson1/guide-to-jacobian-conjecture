# Obligation 5: Vanishing of the hidden kernel

> **Status:** unrefereed, AI-assisted research note; no independent review recorded.  
> **Scope:** Program 4 normalized cubic-frame coefficient spaces. The statements do not identify the construction with the fppf orbit quotient or the full unrigidified stable left-right stack.

[Back to the six-obligation index](index.md)


This section assumes the finite-cover reformulation stated in the public Program 4 technical note: a hidden left-right automorphism is equivalent to a target automorphism that lifts to the finite triple completion and acts trivially on both the decorated infinity scheme and the doubled conductor on the normalized discriminant.

## Theorem 5.1 — Hidden-kernel vanishing

Let `(A,B)` be a coprime admissible pair over a characteristic-zero algebraically closed field, and assume `A/c` is nonconstant. Under the finite-cover reformulation above,

\[
K_{A,B}=1.
\]

Consequently, conditional on the stated boundary exact sequence,

\[
\operatorname{Aut}_{LR}(G_{A,B})
\simeq
\operatorname{Stab}(Z_A,\sigma_{A,B}).
\]

### Proof

Let `(\Phi,\Psi)` be hidden.

### Step 1: `Psi^*c` is affine in `c`

A left-right self-equivalence preserves the reduced nonproperness set

\[
D_{A,B}\cup
\bigcup_{s\in|Z_A|}P_s,
\qquad
P_s=V(c-s).
\]

The discriminant component is the unique nonplane component, so `Psi` permutes the planes. If

\[
\Psi(P_s)=P_{s'},
\]

then equality of principal prime ideals gives

\[
\Psi^*(c-s')=\lambda(c-s)
\]

for some `lambda in k^*`. Hence

\[
\Psi^*c=\lambda c+\mu
\]

in the full target coordinate ring.

### Step 2: triviality on the conductor forces `c` to be fixed

On the normalized discriminant, the conductor curve is

\[
L=V(H),
\qquad
H=3At+B.
\]

Because `gcd(A,B)=1`, Bezout gives

\[
k[c,t]/(3At+B)\simeq k[c,1/A].
\]

The hidden automorphism acts identically on the doubled conductor `2L`, hence in particular on `L`. Therefore the restriction of `Psi^*c` to `k[c,1/A]` equals `c`. The affine formula then gives

\[
(\lambda-1)c+\mu=0
\]

in `k[c,1/A]`, so

\[
\lambda=1,
\qquad
\mu=0.
\]

Thus

\[
\Psi^*c=c.
\]

### Step 3: the generic discriminant fiber is the standard cusp

Pass to

\[
K=k(c).
\]

Here `A` is a unit. Define affine-linear coordinates on the target `(a,b)`-plane by

\[
X=B^2-3Ab,
\]
\[
Y=BX+\frac{3A}{2}(-18Aa-Bb).
\]

Their linear Jacobian is

\[
\det\frac{\partial(X,Y)}{\partial(a,b)}=-81A^3\ne0.
\]

Direct expansion gives

\[
Y^2-X^3
=-\frac{27}{4}A^2\Delta_{A,B}.
\]

Hence the generic discriminant fiber is affinely the standard cusp

\[
Y^2=X^3.
\]

On its normalization,

\[
X=H^2,
\qquad
Y=H^3.
\]

### Step 4: classify and kill the cusp automorphism

The `K`-automorphism `\Psi_K` preserves the cusp. The classification of affine-plane automorphisms preserving `Y^2=X^3` over a perfect field gives

\[
(X,Y)\longmapsto(\eta^2X,\eta^3Y)
\]

for some `eta in K^*`. On normalization this is

\[
H\longmapsto\eta H.
\]

Triviality on the doubled conductor means identity on

\[
K[H]/(H^2).
\]

Therefore `eta=1`, and `\Psi_K` is the identity.

Since `\Psi` fixes `c`, the differences

\[
\Psi^*a-a,
\qquad
\Psi^*b-b
\]

vanish after localization from `k[c]` to `k(c)`. They therefore vanish in the domain `k[a,b,c]`, so

\[
\Psi=\operatorname{id}.
\]

The no-deck-transformations assertion in the boundary exact sequence then gives

\[
\Phi=\operatorname{id}.
\]

Thus `K_{A,B}=1`. ∎

## Scope of Theorem 5.1

The new argument proves that the subgroup described by the finite-cover reformulation is trivial. It still depends on the source results asserting:

1. every left-right automorphism extends uniquely to the finite completion;
2. hidden elements act trivially on the decorated infinity scheme and on the doubled conductor;
3. the target projection has no deck-transformation kernel.

Those source results remain subject to their own independent audit. No extra “preserve the chosen infinity hyperplane” hypothesis is used.

---
