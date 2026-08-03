# From local normal recurrences to three-chart attachment

Lane 9 · 2026-08-03

## Why this lane matters

A nonzero condition in one chosen coefficient slice is not a geometric
obstruction. It becomes intrinsic only after every fresh parameter, overlap
correction, presentation relation, and adjacent-chart transport has been
included. This lane develops the exact interface needed to make that passage.

## Fixed \(F_2\) chart and support

After the denominator-five shear, write a monomial as \(x^{a/5}y^J\), where
\(a,J\in\mathbf Z\) and \(J\ge0\), put \(w=a-J\), and let
\(\langle w\rangle_5\in\{0,1,2,3,4\}\) be its residue. More explicitly,
a source monomial \(x^iy^j\) contributes, for \(0\le J\le j\), at

\[
(a,J)=(5i-j+J,J),\qquad w=a-J=5i-j.
\]

The maximal Newton-bounded support windows are

\[
S_P=\{(a,J):-60\le w\le15,\ 0\le J\le60-\langle w\rangle_5,\
5a-17J\le3\},
\]

\[
S_Q=\{(a,J):-100\le w\le25,\ 0\le J\le100-\langle w\rangle_5,\
5a-17J\le5\}.
\]

In the terminal chart

\[
x=t^{-25},\qquad y=t^{17}z,\qquad u=z^5,
\]

write

\[
P=t^{-3}\sum_rt^rA_r(z),\qquad
Q=t^{-5}\sum_rt^rB_r(z),
\]

where

\[
A_r=z^{(1-2r)\bmod5}\bar A_r(u),\qquad
B_r=z^{(-2r)\bmod5}\bar B_r(u).
\]

These maximal windows contain \(4433\) \(P\)-coefficients in \(981\)
nonempty layers and \(12340\) \(Q\)-coefficients in \(1663\) layers. They are
an independent-coefficient outer model. The inherited relations selecting
the actual complete-chain chart have not been recovered.

## Parameter-complete finite-order system

Fix a coefficient field \(K\). At normal order \(r\), let
\(V_r^{\mathrm{corr}}\) be the finite-dimensional space of endpoint and
overlap corrections, \(V_r^{\mathrm{fresh}}\) the space of every fresh
parameter, and

\[
W_r
\]

the finite-dimensional equation space with one coordinate for every
determinant, overlap, support, presentation, and cyclic-descent equation at
that order. This \(W_r\) is an equation space, not the scalar series \(W(T)\)
of the exact-normal-linearization coordinates. Put
\(X_r=(x_r,p_r)\in V_r^{\mathrm{corr}}\oplus
V_r^{\mathrm{fresh}}\). After lower orders are fixed, the complete affine
system is

\[
M_rX_r=b_r,\qquad
M_r=[C_r\mid P_r]:
V_r^{\mathrm{corr}}\oplus V_r^{\mathrm{fresh}}\longrightarrow W_r,
\qquad b_r\in W_r.
\]

Here \(C_r\) contains endpoint and overlap correction columns, while \(P_r\)
contains all fresh-parameter columns. The intrinsic obstruction quotient and
forcing class are

\[
\operatorname{Ob}_r=\operatorname{coker}M_r
=W_r/(\operatorname{im}C_r+\operatorname{im}P_r),
\qquad [b_r]\in\operatorname{Ob}_r.
\]

The full system is solvable exactly when \([b_r]=0\), equivalently

\[
b_r\in\operatorname{im}C_r+\operatorname{im}P_r.
\]

Its dual space of obstruction functionals is

\[
\operatorname{Ob}_r^\vee\simeq\ker M_r^t
=\ker C_r^t\cap\ker P_r^t.
\]

Thus a left-null functional \(\lambda^tC_r=0\) from the
fresh-parameter-zero slice is intrinsic only if \(\lambda^tP_r=0\).

For the \(C_5\)-character decomposition, assume
\(\operatorname{char}K\ne5\), that \(K\) contains a chosen primitive fifth
root of unity, and that every displayed space, map, and forcing vector is
\(C_5\)-equivariant. Otherwise make the character decomposition after the
separable extension \(K(\zeta_5)\); finite-system feasibility is unchanged by
that extension. Feasibility must hold in every character block.

## Reusable mathematics

In the retained weighted slice, define the nonlinear order-\(r\) forcing

\[
\Phi_r(z)=\sum_{\substack{i+j=r\\i,j>0}}
\bigl((3-i)A_iB'_j+(j-5)A'_iB_j\bigr).
\]

After the earlier linear equations have been solved through order \(r-10\),
\(\omega_r=[z^0]\Phi_r\). Thus \(\omega_r\) is one constant output
coordinate in that slice; it is not an intrinsic obstruction unless it
descends to the displayed cokernel \(\operatorname{Ob}_r\).

1. The first target coordinate outside the linear image in the maximal-window
   model is the constant coefficient at order \(510\).
2. One exact rational weighted slice uses parameters at orders \(10\), \(260\),
   and \(270\) to cancel \(\omega_{510}\) and \(\omega_{520}\).
3. The formerly nonzero \(\omega_{530}\) set all new coordinates to zero.
   Reopening five order-\(280\) coordinates gives a four-dimensional
   \(\omega_{510}\)-kernel, a three-dimensional joint
   \(\omega_{510},\omega_{520}\)-kernel, and a direction cancelling
   \(\omega_{530}\). The determinant vanishes through order \(530\).
4. This order-\(530\) result is still a slice: it reopens only order \(280\)
   and does not impose the missing inherited complete-chain relations.
5. In lower-face coordinates \(t=Y,z=XY^2\), the **bare \(k=4\) wall** is
   the Laurent shear \(X'=X\), \(Y'=Y+\lambda X^{-4}\). Equivalently,
   \(t'=t(1+h)\), \(z'=z(1+h)^2\), with
   \(h=\lambda t^7z^{-4}\). “Bare” distinguishes this operation from the
   corrected Rees/Kummer candidate. The ambient wall groupoid has \(73\)
   exact replay tests for coefficient, equation, overlap, dual, and quotient
   transport. The bare wall starts at normal order seven and is the identity
   through order six. These ambient transports are not yet the actual
   adjacent \(F_2\) chart.

For the ambient wall model used below, \(E_0\) is the full degree-21
coefficient window through layer 15 and \(T_E(\lambda)\) is the exact wall
transport on that window. Put \(E_\lambda=T_E(\lambda)E_0\); thus
\(E_1\) and \(E_{-1}\) are the transported windows at parameters \(1\) and
\(-1\). Their sum is the minimal three-chart ambient saturation, while
their common intersection is the all-parameter stable core. These are
ambient Laurent-jet charts, not the missing actual adjacent \(F_2\) charts.

## Live problem

Recover the inherited relation ideal and actual adjacent-chart presentation,
then export the first order block in which all actual fresh parameters and
overlap corrections are simultaneously visible. Only that block can support
a global attachment or obstruction conclusion.

## Interface-ready task L9-T1 — an invariant obstruction-transport theorem

This task isolates a useful theorem that does not require the absent actual
\(F_2\) matrices.

**Inputs.** The exact
[parameter-complete recurrence contract](lane-9-source-packet.md#source-89e4eda45b4d5d16),
its [solver](lane-9-source-packet.md#source-2b16e7df7e008983),
the [wall-overlap theorem](lane-9-source-packet.md#source-d6c38a4c865ab7c9),
the [dual and triple-overlap theorem](lane-9-source-packet.md#source-bcb444020cf39f50),
and the [cyclic wall-parameter descent](lane-9-source-packet.md#source-fa8ccec644530dcc).

**Deliverable.** Formulate a three-chart finite-order attachment datum (or
first formulate a two-chart datum and then explicitly adjoin a third chart)
over a field satisfying the displayed \(C_5\) hypothesis. Give filtered
correction, fresh-parameter, equation \(W_r\), forcing, and dual spaces,
together with pairwise forward and inverse overlap maps. Prove necessary and
sufficient identities for each pairwise map to induce an isomorphism

\[
W_r/(\operatorname{im}C_r+\operatorname{im}P_r)
\;\cong\;
W'_r/(\operatorname{im}C'_r+\operatorname{im}P'_r)
\]

that carries the forcing class \([b_r]\) to \([b'_r]\). Dualize these
isomorphisms to the corresponding spaces
\(\ker M_r^t\) and \(\ker {M'_r}^t\) of obstruction functionals. Include the
cocycle law \(T_{jk}T_{ij}=T_{ik}\) on the common triple core and show
explicitly why transporting
coefficients without the equation, fresh-parameter, and dual maps is
insufficient.
Specialize the theorem to the supplied ambient charts
\(E_0,E_1,E_{-1}\) for the \(k=4\) wall data and identify
the exact additional blocks required for an actual \(F_2\) application.

**Dependencies.** Finite-dimensional linear algebra, the displayed
\(C_5\)-grading, and the supplied exact ambient wall maps.

**Limits.** The resulting interface theorem does not itself supply the
missing actual-chain relation ideal or prove global \(F_2\) attachment.

## Non-ready \(F_2\) integrations

The following become executable only after Lane 8 supplies actual normal
windows and the complete-chain presentation supplies inherited relations:

1. export \(M_r=[C_r\mid P_r]\) and \(b_r\) in matching bases;
2. continue the parameter-complete actual system beyond order \(530\);
3. transport it across the actual adjacent chart using L9-T1.

The current zero-new-coordinate and order-\(280\) slices must not be promoted
to those results.

## Exact sources

- [Lane 8/9 recovery audit](lane-9-source-packet.md#source-38ab8bd19d25aff4)
- [Fresh-order-\(280\) exact program](lane-9-source-packet.md#source-151645a0e17f5aa6)
- [Machine-readable evidence](lane-9-source-packet.md#source-ab81932dfb3d4762)
- [Normal-linearization source](../proof-sources/06-plane-boundary/appendices/exact-normal-linearization.md)
- [Ambient wall-overlap theorem](lane-9-source-packet.md#source-d6c38a4c865ab7c9)
- [Dual and triple-overlap theorem](lane-9-source-packet.md#source-bcb444020cf39f50)
- [Cyclic wall-parameter descent](lane-9-source-packet.md#source-fa8ccec644530dcc)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-9-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
