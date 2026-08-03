# Torelli data on the projective resultant boundary

Lane 2 · 2026-08-03

## Scope

Normalize the projective-infinity boundary of the quintic outer PRS graph and
glue it to its known finite atlas.  The boundary has three standard affine
product charts, including the double-infinity corner.  The projective object
is fixed below as a multi-Rees graph closure, so the task is not to guess a
compactification from an affine denominator clearing.

Success completes the outer projective boundary on this quintic chart and
tests which marked polynomial data survive normalization.

## Setup and definitions

The surrounding principal-remainder-sequence (PRS) construction starts with
a monic polynomial \(Q(w)\) and the polynomial remainder
\(R(w)=w^\nu\bmod Q(w)\). Here **PRS** means the sequence of polynomial
subresultants
\(\operatorname{Sres}_{m-1}(w^\nu,Q),\ldots,
\operatorname{Sres}_0(w^\nu,Q)\), with signs fixed by the displayed
Sylvester convention. For \(1\le k\le m\), the displayed **principal
subresultant coefficient**
\(\operatorname{psc}^{\mathrm{disp}}_{m-k}(Q,R)\) is the determinant of the
\((2k-1)\)-square coefficient matrix whose ordered rows are

\[
w^{k-2}Q,\ldots,Q,\quad w^{k-1}R,\ldots,R
\]

and whose ordered columns take the coefficients of
\(w^{m+k-2},w^{m+k-3},\ldots,w^{m-k}\). Replacing \(R\) by \(w^\nu\) gives
the same determinant after Sylvester elimination. The normal indices are the
sizes \(n\) at which the leading Hankel determinant
\(\det(s_{i+j+1})_{0\le i,j<n}\), equivalently the corresponding displayed
PSC, is nonzero.  These conventions explain the quintic flag and fix its
signs; they are not extra variables in the projective graph below.

On the \(\mathsf Z\)-chart of the actual \((m,\nu)=(5,5)\) flag, work in
\(X=\operatorname{Spec}k[x,y,z,t]\), where
\((x,y,z,t)=(C,D,u,v)\), over a characteristic-zero field. (The finite
normalization calculation itself only needs \(2\) invertible.) Write the two
exact outer generator pairs without renaming their
entries:

\[
J_0=(f_0,g_0)=(xz,yz+xt),
\]

\[
J_1=(f_1,g_1)=((x-y^2)(z+x+yt),xt+yz+2xy-y^3).
\]

Let $[L_0:L_1]$ and $[R_0:R_1]$ be homogeneous coordinates on two copies of
\(\mathbf P^1\), with the exact convention

\[
[L_0:L_1]=[f_0:g_0],\qquad [R_0:R_1]=[f_1:g_1].
\]

The simultaneous projective graph is the closure of

\[
X\dashrightarrow\mathbf P^1_L\times\mathbf P^1_R,
\qquad p\mapsto([f_0(p):g_0(p)],[f_1(p):g_1(p)]),
\]

equivalently the relative multi-Proj

\[
\mathcal G=\operatorname{MultiProj}_X
\bigoplus_{a,b\ge0}J_0^aJ_1^b s^a q^b.
\]

More explicitly, its bihomogeneous ideal is the kernel of

\[
k[x,y,z,t,L_0,L_1,R_0,R_1]
 \longrightarrow k[x,y,z,t,s,q],
\]

\[
(L_0,L_1,R_0,R_1)\longmapsto(f_0s,g_0s,f_1q,g_1q),
\]

with the usual irrelevant-ideal saturation.  This verifies that the
multi-Rees object is the same graph whose finite normalization is linked
below; it is not an independently chosen compactification.

Explicitly, the Cox irrelevant ideal is
\(\mathfrak b=(L_0,L_1)(R_0,R_1)\); “irrelevant-ideal saturation” means
\(I:\mathfrak b^\infty\). The **conductor** requested below is the conductor
ideal \(\operatorname{Ann}_{\mathcal O_{\mathcal G}}
(\nu_*\mathcal O_{\mathcal G^\nu}/\mathcal O_{\mathcal G})\) of a chart
ring into its normalization.

On the finite--finite chart \(D(L_0R_0)\), set

\[
\lambda=L_1/L_0=g_0/f_0,\qquad
\rho=R_1/R_0=g_1/f_1,\qquad T=t-\lambda z.
\]

The two incidence equations are
\(g_0-\lambda f_0=xT+yz=0\) and
\(g_1-\rho f_1=0\). The actual graph ideal on this chart is

\[
(xT+yz,g_1-\rho f_1):(f_0f_1)^\infty=I_2(M_{\lambda,\rho}),
\]

not the unsaturated two-equation ideal.  The linked finite theorem normalizes
exactly this chart.

The complement of \(D(L_0R_0)\) needs three standard product charts:

\[
U_{\infty0}=D(L_1R_0),\quad
U_{0\infty}=D(L_0R_1),\quad
U_{\infty\infty}=D(L_1R_1).
\]

Their affine ratios are respectively
\((\lambda_\infty=L_0/L_1,\rho)\),
\((\lambda,\rho_\infty=R_0/R_1)\), and
\((\lambda_\infty,\rho_\infty)\). Here the **marked input** is the ordered
pair of two-generated ideals \((J_0,J_1)\) in the fixed affine ring
\(k[x,y,z,t]\). A marked-input isomorphism is an automorphism of that ring
carrying \(J_0\) to \(J'_0\) and \(J_1\) to \(J'_1\), without interchanging
the two labels. A global normalization theorem must cover all three charts
and include conductors and overlap maps. A **Torelli refinement** would then
specify a finite tuple of regular or rational functions on the normalized
boundary, with its allowed change-of-chart action, and prove that equality
of those tuples is equivalent to marked-input isomorphism. No such recovery
tuple is assumed in the chart-normalization task.

## Results to use

- The all-rank principal-subresultant, Hankel, and Schur identities fix the
  sign, order, and composition conventions used by the PRS flag.
- On the finite--finite chart, setting
  $\lambda=L_1/L_0$, $\rho=R_1/R_0$, and $T=t-\lambda z$ gives the saturated Hilbert--Burch graph
  $I_2(M_{\lambda,\rho})$ displayed in the finite theorem.
- Adjoining the integral element $w$ gives its exact normalization. At the
  positive $T=0$ sheet its completed local normal form is
  $k[[x,R,z,\Delta,\lambda]]/(xR+\Delta z^2)$; the negative sheet is smooth.
- The finite theorem glues to the previously known $T\ne0$ cubic-scroll
  normalization. It explicitly does not cover either outer chart.
- No current result gives the multi-Rees kernels, normalizations, conductors,
  or overlap maps on the three non-finite product charts.

## Example: the known finite boundary germ

On the positive finite $T=0$ sheet the exact normal form

\[
xR+\Delta z^2=0
\]

has singular locus $V(x,R,z)$ with $(\Delta,\lambda)$ free. For
$\Delta\ne0$ its transverse surface is $A_1$; at $\Delta=0$ the fibre is
$xR=0$ while the total space remains normal. This is the finite--finite
boundary model, not an infinity chart.

## Live problem

Compute the multi-Rees graph on
\(U_{\infty0},U_{0\infty},U_{\infty\infty}\) directly from \(J_0,J_1\),
normalize each chart, and prove that the transition maps agree with the finite
normalization and with one another on every nonempty overlap.

## Tasks

### L2-T1 — Normalize the fixed multi-Rees infinity boundary

Inputs: the exact pairs $J_0,J_1$ above; the
[saturated finite multi-Rees equations](lane-2-source-packet.md#source-794624f89288ba28);
the [finite $T=0$ normalization theorem](lane-2-source-packet.md#source-485c3d5f593645a2);
and the [ordered outer resolution](lane-2-source-packet.md#source-26cddbd8db58d696).

Deliverable: for each of
\(D(L_1R_0),D(L_0R_1),D(L_1R_1)\), give the saturated multi-Rees ideal, its
integral closure, a proof of normality, and the conductor. Give forward and
inverse formulas on every overlap, including the finite chart's overlaps
with both single-infinity charts and the double-infinity chart. Then, if
the calculation identifies a natural finite recovery tuple in the preceding
sense, state and prove the exact marked-pair recovery result it supports, or
exhibit distinct marked inputs with identical tuples. Producing that Torelli
refinement is a secondary deliverable: the chart ideals, normalizations,
conductors, and gluing form the complete required output.

Dependencies: the fixed homogeneous graph $\mathcal G$, the PSC conventions,
and the established finite normalization.

Limits: normality chart by chart does not imply separated gluing; clearing
denominators without irrelevant-ideal saturation is not the multi-Rees graph.

Alternative connections: a groupoid formulation linked to Lane 9 is welcome
if all arrows, inverses, and cocycles are explicit.

## Limits

The finite--finite $T=0$ theorem is complete only on $D(L_0R_0)$. No global
Torelli or properness conclusion is available until the full infinity
boundary, including the double-infinity corner, and all overlaps are proved.

## Direct sources

- [Finite $T=0$ theorem](lane-2-source-packet.md#source-485c3d5f593645a2)
- [Exact normalization checker](lane-2-source-packet.md#source-813098830565c0aa)
- [Actual quintic complete-PRS flag](lane-2-source-packet.md#source-a390d36f88cafaa0)
- [PSC, Hankel, and Schur conventions](lane-2-source-packet.md#source-2af31fd24c3a8d0f)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-2-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
