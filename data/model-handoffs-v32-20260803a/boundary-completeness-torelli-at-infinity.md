# Torelli data on the projective resultant boundary

Lane 2 · 2026-08-03

## Scope

Use the now-complete projective normalization of the fixed quintic outer PRS
graph as the first noncoprime model for an all-rank adjacent-block theorem and
a marked-boundary Torelli invariant. The fixed graph has all four product
charts, conductor, and overlaps; the remaining problem is no longer to
discover its infinity charts.

Success identifies the data that survive adjacent PRS merges and proves that
they recover the marked polynomial input on a declared class.

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
- Seven bihomogeneous relations give one finite birational normal algebra on
  all four product charts. Its conductor is \((x,y,z)\); the inverse conductor
  is the double cover
  \[
  \Xi^2=U(U-tV)P(P-tQ),
  \]
  and \(\Xi\) transforms as a section of \(\mathcal O(1,1)\). Thus the fixed
  quintic projective-normalization problem, including the double-infinity
  corner and all overlaps, is complete.
- For abstract adjacent monomial centers \((x^a,y^b)\) and \((y^c,z^d)\),
  common-Cartier-factor removal makes the two orders commute. Full
  exceptional saturation instead gives the two circuit triangulations,
  controlled by
  \(\Delta=a_0(c_0-1)-d_0(b_0-1)\): equality is the flop locus and the sign
  gives the flip direction.
- Applying the adjacent-merge theorem to an actual all-rank PRS graph still
  requires the pivot valuations, merge maps, and an explicit declaration of
  which weak-transform convention is used.

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

Extract from the all-rank PRS construction a schema-valid adjacent-block
packet: the two primitive pivot vectors, their shared valuation, normalized
exponents \(a_0,b_0,c_0,d_0\), the lattice and merge maps, the chosen
weak-transform convention, and the conductor character. Prove that the
abstract adjacent-merge theorem applies, and determine which functions on the
normalized boundary recover the marked input up to the declared marked-pair
isomorphism.

## Tasks

### L2-T1 — Specialize the adjacent-merge theorem to PRS blocks — ready

Inputs: the [complete fixed quintic normalization
packet](lane-2-source-packet.md#source-bde5074568c74356);
the [abstract adjacent-merge theorem and exact
checkers](lane-2-source-packet.md#source-39a1177974f5e030);
the [fail-closed PRS specialization
contract](lane-2-source-packet.md#source-1cb0e52d6cb87b72);
and the all-rank PSC, Hankel, Schur, normal-index, and ordered-composition
conventions linked below.

Deliverable: fill the specialization contract from the actual PRS blocks,
prove that its pivot and lattice data satisfy the abstract hypotheses, state
which transform convention the PRS construction implements, and derive the
resulting flip, flop, or commuting square. Include the conductor character
and every overlap cocycle needed to compare adjacent blocks.

Dependencies: the declared PRS convention and the abstract toric theorem.

Limits: the abstract exponent formula alone is not evidence that a PRS merge
has those exponents or uses that convention.

### L2-T2 — Extract and test a marked-boundary Torelli tuple — ready

Inputs: the fixed ordered ideals \(J_0,J_1\), the complete global
normalization packet, and its \(\mathcal O(1,1)\) conductor generator.

Deliverable: propose a finite tuple of regular or rational functions on the
normalized boundary with an explicit change-of-chart action. Prove that it
recovers the fixed marked pair within a precisely stated family, or give two
nonisomorphic marked pairs with the same tuple. Separate fixed-quintic
evidence from any all-rank conjecture.

Dependencies: the global conductor and overlap maps already supplied.

Limits: success for one family is not a Torelli theorem for arbitrary PRS
inputs.

Alternative connections: a groupoid formulation linked to Lane 9 is welcome
if all arrows, inverses, and cocycles are explicit.

## Limits

The fixed quintic normalization is global, but no general adjacent-PRS
specialization or marked-boundary Torelli theorem follows automatically.

## Direct sources

- [Finite $T=0$ theorem](lane-2-source-packet.md#source-485c3d5f593645a2)
- [Exact normalization checker](lane-2-source-packet.md#source-813098830565c0aa)
- [Actual quintic complete-PRS flag](lane-2-source-packet.md#source-a390d36f88cafaa0)
- [PSC, Hankel, and Schur conventions](lane-2-source-packet.md#source-2af31fd24c3a8d0f)
- [Complete fixed quintic projective normalization](lane-2-source-packet.md#source-bde5074568c74356)
- [Convention-complete adjacent-merge theorem](lane-2-source-packet.md#source-39a1177974f5e030)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-2-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
