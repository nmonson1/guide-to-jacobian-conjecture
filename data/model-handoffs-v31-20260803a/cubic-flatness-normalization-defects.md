# Flatness defects after cubic normalization

Lane 1 · 2026-08-03

## Scope

Study the finite normalization of a generic-degree-three Keller map at an
omitted target value. The known theory identifies the exact finite defect and
its quadratic-resolvent and collision-cohomology carriers. The frontier is to
exclude those carriers or construct one satisfying all stated local
constraints.

Success would remove the only possible nonflat points of a cubic
normalization; it would not by itself recover the affine source opening.

## Setup and definitions

Work over \(\mathbf C\). This is the coefficient field of the recovered
proof: its local-duality, local-Picard, logarithmic, and \(S_3\)-isotypic
statements are proved there. No descent or base-change theorem to an
arbitrary characteristic-zero field is being assumed here. Let

\[
F:\operatorname{Spec}S\longrightarrow\operatorname{Spec}R,
\qquad R=\mathbf C[y_1,y_2,y_3],\quad
S=\mathbf C[x_1,x_2,x_3],
\]

be a Keller map whose function-field extension has degree three. Let $B$ be
the integral closure of $R$ in $\operatorname{Frac}S$. Its canonical finite
flatness defect is

\[
\Delta_F=\operatorname{Ext}^1_R(B,R).
\]

At a closed value $y$, put $A=R_y$ and $\Delta_y=(\Delta_F)_y$. Let $T$ be
the normalization in the $S_3$-Galois closure. On the attained part of
$\operatorname{Spec}T$, the three conjugate source openings $U_1,U_2,U_3$
give an affine Cech complex

\[
C_y^0\xrightarrow{d_0}C_y^1\xrightarrow{d_1}C_y^2,
\qquad K_y=\ker d_1,\quad I_y=\operatorname{im}d_0.
\]

Here $I_y$ is a submodule of $K_y$, not an ideal in a source-chart ring. Its
closed-point saturation is

\[
I_y^{\mathrm{sat}}=I_y:_{K_y}\mathfrak m_y^\infty.
\]

If $V_{\mathrm{std}}$ is the two-dimensional complex standard representation
of $S_3$, the collision theorem gives

\[
I_y^{\mathrm{sat}}/I_y\simeq
\operatorname{MatlisDual}(\Delta_y)\otimes_{\mathbf C} V_{\mathrm{std}}.
\]

Here \(\operatorname{MatlisDual}(N)=\operatorname{Hom}_A(N,E_A(\mathbf C))\),
where \(E_A(\mathbf C)\) is the injective hull of the residue field of the
local ring \(A\). This definition does not require replacing \(A=R_y\) by its
completion.

## Results to use

- $B=R\oplus E$ with $E$ reflexive of rank two, and
  $\operatorname{Supp}\Delta_F$ is exactly the nonfree locus of $B$.
  Moreover, every attained target value is outside this support.
- For the quadratic resolvent $Q=T^{A_3}$ there is a rank-one reflexive
  eigensheaf $L$ with $T=Q\oplus L\oplus L^{[2]}$,
  $L^{[3]}\simeq Q$, and $\sigma^*L\simeq L^\vee$. The cubic normalization
  is flat at $y$ exactly when every $L_{\mathfrak q}$ above $y$ is maximal
  Cohen--Macaulay. Here \(L^{[n]}=(L^{\otimes n})^{\vee\vee}\) denotes the
  reflexive tensor power.
- The displayed Cech-saturation identity is the equivalent collision
  formulation. It uses saturation by $\mathfrak m_y$ inside $K_y$; it does
  not assert that a missing source-chart ideal has been computed.
- The standard ordered-root triple collision has complement ideal
  $(u(u+v),uv,v(u+v))=(u,v)^2$ and zero punctual saturation quotient.
- These results neither prove $\Delta_F=0$ in general nor supply an actual
  omitted-value local equation for an arbitrary map.

## Example: an explicit transverse carrier

For an integer \(r\ge1\), let

\[
Q_0=\mathbf C[[u,v,z]]/(uv-z^{3r}),\qquad I_r=(u,z^r),
\]

the matrices

\[
\Phi_r=\begin{pmatrix}v&-z^r\\-z^{2r}&u\end{pmatrix},\qquad
\Psi_r=\begin{pmatrix}u&z^r\\z^{2r}&v\end{pmatrix}
\]

satisfy $\Phi_r\Psi_r=\Psi_r\Phi_r=(uv-z^{3r})I_2$. This realizes a
nonzero three-torsion transverse class. It is a boundary model, not evidence
that a three-dimensional Keller defect exists.

## Live problem

Let $A$ be a complete regular local \(\mathbf C\)-algebra of dimension three, let
$Q=A[w]/(w^2-d)$ be normal, and let $L$ be rank-one reflexive with
$L^{[3]}\simeq Q$ and $\sigma^*L\simeq L^\vee$. Find checkable hypotheses on
$d$ and the local class of $L$ that force $L$ to be maximal
Cohen--Macaulay, or construct an explicit non-MCM pair $(Q,L)$ satisfying
these constraints. Then identify exactly which additional condition would
be needed to realize such a pair as a cubic Keller normalization defect.

## Tasks

### L1-T1 — Classify the quadratic-resolvent carrier

Inputs: the [complete recovered collision proof](lane-1-source-packet.md#source-195de0d23627037b),
especially `thm:collision-cech-saturation`; the separate
[exact resolvent and transverse-ADE proof](lane-1-source-packet.md#source-31b28e4d427212ea),
especially `thm:exact-resolvent-carrier` and
`prop:transverse-ADE-filter`; the
[collision idempotent checker](lane-1-source-packet.md#source-9425e75cd188cddb);
and the [standard collision checker](lane-1-source-packet.md#source-915e7bbeb67e7bc2).

Deliverable: a theorem with explicit local hypotheses implying that $L$ is
MCM, or an explicit normal double hypersurface and non-MCM three-torsion
rank-one reflexive $L$ with its presentation, class, depth, and Ext module.
For an abstract pair \((Q,L)\), state the corresponding predicted dual defect;
the Čech saturation quotient is not defined until a Keller realization and
its three source openings are supplied. If the construction includes such a
realization, define those openings and then compute the quotient and explain
whether it vanishes.

Dependencies: normality of $Q$, the order-three and anti-invariance identities
for $L$, and the exact Ext/Cech comparison above.

Limits: an arbitrary double cover is not automatically a Keller resolvent;
a transverse matrix factorization does not settle extension through the
closed threefold point.

Alternative connections: a filtration from Lane 5 is welcome if it yields a
proof about this same rank-one reflexive module.

## Limits

The problem is local at a hypothetical omitted defect value. Source splitting
already proves flatness at attained values. The marked-root benchmark and ADE
models are examples and do not identify an actual defect value.

## Direct sources

- [Complete Lane 1 proof source](lane-1-source-packet.md#source-195de0d23627037b)
- [Exact resolvent and transverse-ADE source](lane-1-source-packet.md#source-31b28e4d427212ea)
- [Recovery manifest](lane-1-source-packet.md#source-d8d50dd353502656)
- [Canonical Ext appendix](../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-1-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
