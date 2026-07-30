# Obligation 4: Nonunit resultants and the relative-Jacobian marking

> **Status:** unrefereed, AI-assisted research note; no independent review recorded.  
> **Scope:** Program 4 normalized cubic-frame coefficient spaces. The statements do not identify the construction with the fppf orbit quotient or the full unrigidified stable left-right stack.

[Back to the six-obligation index](index.md)


This obligation can be pushed farther than mere Fitting compatibility.

## Theorem 4.1 — Gauge invariance of the finite zero-scheme package

Suppose

\[
B'=B+Qh
\]

for any polynomial `h`. Then, as ideals in the `c`-line,

\[
(Q,B')=(Q,B),
\qquad
(Q,(B')^2)=(Q,B^2).
\]

Consequently the closed subschemes

\[
G_1=V(Q,B),
\qquad
G_2=V(Q,B^2)
\]

are invariant under every principal-part/root-translation gauge. This statement commutes with arbitrary base change and uses no unit-resultant hypothesis.

### Proof

Modulo `Q`, one has `B'=B` and `(B')^2=B^2`. ∎

For the exact `N=d+m` transition,

\[
R=R_d+Q_dS,
\]

one has

\[
B=B_d+c^2Q_dS
=B_d+3A\phi,
\qquad
\phi=\frac{cS}{3}.
\]

Thus Theorem 4.1 applies with `Q=Q_d`.

## Theorem 4.2 — Exact compatibility of the relative-Jacobian divisor

Let

\[
H_{A,B}(c,t)=3A(c)t+B(c).
\]

Under the exact transition above, set

\[
T=t+\phi(c).
\]

Then

\[
H_{A,B}(c,t)=H_{A,B_d}(c,T).
\]

Moreover, the coefficient-content divisor

\[
\chi=\gcd(A,B^2)
\]

is unchanged, because the ideal `(A,B^2)` is unchanged. Therefore the marked Cartier divisor on the relative-Jacobian normalization chart,

\[
\operatorname{div}(H^3)-\pi^*\operatorname{div}(\chi),
\]

is carried isomorphically to the lower-length marked divisor by the polynomial translation `T=t+phi(c)`.

Equivalently, if

\[
g=\gcd(A,B),
\qquad
A=gA_0,
\qquad
B=gB_0,
\qquad
\rho=\frac{g^3}{\chi},
\]

then

\[
\rho H_0^3=\frac{H^3}{\chi}
\]

is invariant.

This proves exact-stratum compatibility with the weighted relative-Jacobian marking even when `B mod Q` is a zero divisor and the finite root scheme is nonreduced.

### Proof

The identity for `H` is

\[
3At+B_d+3A\phi
=3A(t+\phi)+B_d.
\]

The content equality follows from Theorem 4.1, with `A=cQ_d` and `c` a unit at every deleted finite root. Finally,

\[
H=gH_0
\]

gives

\[
\frac{H^3}{\chi}
=\frac{g^3}{\chi}H_0^3
=\rho H_0^3.
\]

∎

## 4.3 Valuation and Fitting formulation

At a deleted root, write

\[
A=u^r\alpha,
\qquad
B=u^k\beta,
\]

with the displayed unit factors, and put

\[
m=\min(r,k).
\]

Then

\[
G_1=V(u^m),
\qquad
G_2=V(u^{\ell}),
\qquad
\ell=\min(r,2k)=\min(r,2m).
\]

The horizontal and vertical orders in the relative-Jacobian chart are

\[
p=r-m,
\qquad
\mathfrak d=3m-\ell
=3m-\min(r,2m).
\]

Thus the intrinsic multiplicity package is determined by the finite Artin algebra and the zero scheme of the section. The second ideal `(Q,B^2)` records exactly the truncation needed for the vertical multiplicity.

For

\[
\mathcal O_Z=k[\varepsilon]/(\varepsilon^2),
\qquad
\sigma=\sigma_0+\sigma_1\varepsilon,
\]

multiplication by `sigma` has matrix

\[
\begin{pmatrix}
\sigma_0&0\\
\sigma_1&\sigma_0
\end{pmatrix},
\]

so

\[
\operatorname{Fitt}_0(\operatorname{coker}m_\sigma)
=(\sigma_0^2),
\qquad
\operatorname{Fitt}_1(\operatorname{coker}m_\sigma)
=(\sigma_0,\sigma_1).
\]

These Fitting ideals commute with base change.

## 4.4 What remains for arbitrary families

The ideals

\[
\mathcal I_1=(Q,B),
\qquad
\mathcal I_2=(Q,B^2)
\]

are universal and base-change compatible. On each geometric fiber they recover the relative-Jacobian multiplicities exactly. What can fail in a general family is flatness or Cartier behavior of their zero schemes when:

- contact length at infinity changes;
- a finite common factor appears or disappears;
- both happen simultaneously.

A precise global enhancement is therefore:

1. start with `\mathfrak G_N`;
2. over `\mathbb P^1_c\times\mathfrak G_N`, principalize or universally flatten `\mathcal I_1` and `\mathcal I_2` simultaneously;
3. carry the effective marked divisor represented fiberwise by
   \[
   \operatorname{div}(H^3)-\operatorname{div}(\mathcal I_2);
   \]
4. take the resulting stacky flattening/complete-collineation space as
   \[
   \mathfrak G_N^{\mathrm{RJ}}.
   \]

The exact-stratum theorem shows that no mixed equation involving the principal part `S` is needed: the infinity-direction factor and the finite relative-Jacobian package split there.

The remaining lemma is now very specific:

> Prove that the simultaneous flattening of `\mathcal I_1,\mathcal I_2` agrees with the primitive-discriminant relative-Jacobian blowup when contact length and common-factor multiplicity jump in one family.

---
