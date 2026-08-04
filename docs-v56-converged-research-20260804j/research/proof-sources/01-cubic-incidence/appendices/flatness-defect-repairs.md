---
title: "Text proof source — 01-cubic-incidence/appendices/flatness-defect-repairs.tex"
description: "Sanitized current source with exact labels when present."
---

# Text proof source

`manuscripts/01-cubic-incidence/appendices/flatness-defect-repairs.tex`

This is the current sanitized source text used by the retained working graph. TeX comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `58fb64db42c81c1bf85b2ed7e99f2e5edb51c4e03cc97749c366fa6c8ee48a95` · 19,552 bytes

## Exact label anchors

<a id="label-app-flatness-defect-repairs"></a>
- `app:flatness-defect-repairs` — source line 2
<a id="label-prop-cubic-ext-defect"></a>
- `prop:cubic-ext-defect` — source line 32
<a id="label-prop-cubic-defect-self-duality"></a>
- `prop:cubic-defect-self-duality` — source line 94
<a id="label-cor-cubic-one-generator-defect"></a>
- `cor:cubic-one-generator-defect` — source line 143
<a id="label-prop-cubic-source-splitting"></a>
- `prop:cubic-source-splitting` — source line 166
<a id="label-cor-cubic-defect-support"></a>
- `cor:cubic-defect-support` — source line 209
<a id="label-thm-exact-resolvent-carrier"></a>
- `thm:exact-resolvent-carrier` — source line 235
<a id="label-cor-formal-cubic-defect"></a>
- `cor:formal-cubic-defect` — source line 305
<a id="label-cor-cubic-defect-fibre-length"></a>
- `cor:cubic-defect-fibre-length` — source line 327
<a id="label-cor-resolvent-defect-curves"></a>
- `cor:resolvent-defect-curves` — source line 352
<a id="label-prop-transverse-ade-filter"></a>
- `prop:transverse-ADE-filter` — source line 384
<a id="label-rem-revised-cubic-task"></a>
- `rem:revised-cubic-task` — source line 545

## Complete source

~~~tex
\section{The finite cubic flatness defect: exact repairs}
\label{app:flatness-defect-repairs}

This appendix replaces the former statement-only flatness package by a
canonical finite defect, proves the attained-value splitting, identifies the
defect exactly on the quadratic resolvent, and records the remaining local
input.  It does not prove that the defect vanishes.

Let
\[
R=\C[y_1,y_2,y_3],\qquad S=\C[x_1,x_2,x_3],
\]
and let
\[
F\colon X=\Spec S\longrightarrow Y=\Spec R
\]
be a Keller map of generic degree three.  Put \(K=\Frac S\), let \(B\) be the
integral closure of \(R\) in \(K\), and write
\[
\pi\colon\overline X=\Spec B\longrightarrow Y.
\]
The field trace splits the unit inclusion:
\[
B=R\oplus E,\qquad E=\ker(\operatorname{Tr}_{B/R}),
\]
where \(E\) has rank two.  Write \(O_F=Y\setminus F(X)\) and let \(S_F\)
denote the reduced nonproperness set.

\subsection{The canonical finite defect}

\begin{proposition}[Canonical Ext defect]
\label{prop:cubic-ext-defect}
The \(R\)-modules \(B\) and \(E\) are reflexive.  Define
\[
\Delta_F:=\operatorname{Ext}^1_R(B,R)
          \simeq\operatorname{Ext}^1_R(E,R).
\]
Then \(\Delta_F\) has finite length and
\[
\operatorname{Supp}\Delta_F
 =\{y\in Y:B_y\text{ is not free over }R_y\}.
\]
Consequently
\[
B\text{ is finite flat over }R
\quad\Longleftrightarrow\quad
\Delta_F=0.
\]
More precisely, at a closed point \(y\), with \(A=R_y\), there is a minimal
free resolution
\[
0\longrightarrow A^b\xrightarrow{\Phi}A^{b+2}
 \longrightarrow E_y\longrightarrow0,
\]
and
\[
(\Delta_F)_y\simeq\operatorname{coker}(\Phi^\vee),
\qquad
\dim_\C (\Delta_F)_y/\mathfrak m_y(\Delta_F)_y=b.
\]
Local duality gives
\[
\operatorname{Hom}_A((\Delta_F)_y,E_A(\C))
 \simeq H^2_{\mathfrak m_y}(E_y).
\]
\end{proposition}

\begin{proof}
The integral closure of a noetherian normal domain in a finite field extension
is a finite reflexive module over the base; equivalently, it is recovered from
its codimension-one localizations inside the field extension.  Hence \(B\) is
reflexive, and the trace splitting makes \(E\) a reflexive direct summand.

If \(\mathfrak p\subset R\) has height at most two, reflexivity gives
\[
\operatorname{depth}_{R_\mathfrak p}E_\mathfrak p
 =\dim R_\mathfrak p.
\]
Auslander--Buchsbaum over the regular local ring \(R_\mathfrak p\) makes
\(E_\mathfrak p\) free.  Thus the nonfree locus is a finite set of closed
points.  At a closed point, reflexivity gives depth at least two, so
\(\operatorname{pd}_A E_y\le1\) and the displayed resolution exists.
Dualizing it gives
\[
(\Delta_F)_y=\operatorname{coker}(\Phi^\vee).
\]
If \(b=0\), then \(E_y\) is free.  If \(b>0\), minimality puts every entry of
\(\Phi\) in \(\mathfrak m_y\), so the cokernel of \(\Phi^\vee\) has exactly
\(b\) minimal generators and is nonzero.  This proves the support and
flatness assertions.  The final identity is local duality in dimension three.
\end{proof}

\begin{proposition}[Alternating self-dual defect resolution]
\label{prop:cubic-defect-self-duality}
At a closed point \(y\), choose an orientation \(\det(E_y)\simeq A\).  The
minimal presentation in \cref{prop:cubic-ext-defect} extends to an exact
complex
\[
0\longrightarrow A^b\xrightarrow{\Phi}A^{b+2}
 \xrightarrow{\Psi}(A^{b+2})^\vee
 \xrightarrow{\Phi^\vee}(A^b)^\vee
 \longrightarrow(\Delta_F)_y\longrightarrow0,
\]
where \(\Psi^\vee=-\Psi\).  Consequently
\[
(\Delta_F)_y\simeq
\operatorname{Ext}^3_A((\Delta_F)_y,A),
\]
so \((\Delta_F)_y\) is Matlis self-dual and
\[
\dim_\C\operatorname{Soc}((\Delta_F)_y)
 =\dim_\C (\Delta_F)_y/\mathfrak m_y(\Delta_F)_y=b.
\]
\end{proposition}

\begin{proof}
The orientation gives the alternating reflexive isomorphism
\[
\theta\colon E_y\xrightarrow{\sim}E_y^\vee,
\qquad \theta^\vee=-\theta.
\]
Let \(\rho\colon A^{b+2}\twoheadrightarrow E_y\) be the presentation map and
put
\[
\Psi=\rho^\vee\theta\rho.
\]
Since \(\rho^\vee\) and \(\theta\) are injective isomorphisms onto their
images,
\[
\ker\Psi=\ker\rho=\operatorname{im}\Phi.
\]
The dual presentation gives
\[
\operatorname{im}\Psi=\rho^\vee(E_y^\vee)=\ker\Phi^\vee,
\]
and the final cokernel is \((\Delta_F)_y\).  Dualizing the resulting free
resolution reproduces it, up to the sign of \(\Psi\), and identifies the third
Ext module with the same final cokernel.  For a finite-length module over a
three-dimensional regular local ring, the third Ext is its Matlis dual.
\end{proof}

\begin{corollary}[The one-generator stratum]
\label{cor:cubic-one-generator-defect}
If \(b=1\), then there is an \(A\)-regular sequence \(f_1,f_2,f_3\) such that
\[
(\Delta_F)_y\simeq A/(f_1,f_2,f_3),
\qquad
E_y\simeq\Omega_A^2(A/(f_1,f_2,f_3)).
\]
After compatible choices of bases, the self-dual resolution is the Koszul
resolution, with Betti numbers \((1,3,3,1)\).
\end{corollary}

\begin{proof}
Write \(\Phi(1)=(f_1,f_2,f_3)^t\).  The finite length of
\(\operatorname{coker}\Phi^\vee\) says that the ideal
\((f_1,f_2,f_3)\) has height three.  Since \(A\) is Cohen--Macaulay, the three
elements form a regular sequence.  The alternating self-dual resolution is
then the Koszul resolution, and its second syzygy is
\(\operatorname{coker}\Phi=E_y\).
\end{proof}

\subsection{Source splitting and the exact support boundary}

\begin{proposition}[Source splitting]
\label{prop:cubic-source-splitting}
There is an \(S\)-algebra decomposition
\[
B\otimes_RS\simeq S\times C,
\]
where \(C\) is a normal quadratic \(S\)-algebra.  After choosing a generator
of its trace-zero summand,
\[
C\simeq S[\eta]/(\eta^2-D)
\]
for some \(D\in S\).  The factor \(S\) is canonical; the generator \(\eta\)
is not, and replacing it by a unit multiple changes \(D\) by a unit square.
Consequently \(B_y\) is free over \(R_y\) for every attained value
\(y\in F(X)\).
\end{proposition}

\begin{proof}
Every element of \(B\) lies in \(S\): it is integral over \(R\), hence over
\(S\), and \(S\) is integrally closed in \(K\).  Thus the open immersion
\(j\colon X\hookrightarrow\overline X\) induces, after base change by the
etale map \(F\), a section of the finite morphism
\[
p\colon\overline X\times_YX\longrightarrow X.
\]
The map \(p\) is etale along the section.  Restricting to the etale locus, a
section of an unramified separated morphism is open and closed.  The section
is also closed in the whole fibre product because \(p\) is finite.  It is
therefore an open-and-closed component, giving
\[
B\otimes_RS\simeq S\times C.
\]

Normalization commutes with smooth base change, so \(C\) is normal.  Its
trace splits it as \(S\oplus L_0\), where \(L_0\) is rank-one reflexive.
Since \(S\) is factorial, \(L_0\) is free.  A trace-zero generator \(\eta\)
satisfies \(\eta^2=D\in S\) by Cayley--Hamilton.

If \(F(x)=y\), then the local etale homomorphism \(R_y\to S_x\) is faithfully
flat, while \(B_y\otimes_{R_y}S_x\) is free by the displayed decomposition.
Faithfully flat descent makes \(B_y\) flat, hence free, over \(R_y\).
\end{proof}

\begin{corollary}[Defect support]
\label{cor:cubic-defect-support}
For every generic-degree-three Keller map,
\[
\operatorname{Supp}\Delta_F\subseteq O_F\subseteq\operatorname{Sing}(S_F).
\]
Thus there is no source point above a defect value at which the splitting
argument can simply be repeated.
\end{corollary}

\begin{proof}
The first inclusion is \cref{prop:cubic-source-splitting}.  The second is the
omitted-values theorem: every smooth point of the reduced nonproperness divisor
is attained by a complex Keller map.
\end{proof}

\subsection{The exact quadratic-resolvent carrier}

Let \(\widetilde K\) be the \(S_3\)-Galois closure of \(K/\Frac R\), let \(T\)
be the integral closure of \(R\) in \(\widetilde K\), choose a transposition
subgroup \(H\), and put \(N=A_3\).  Then
\[
B=T^H,\qquad Q=T^N.
\]
Fix a primitive cube root \(\zeta\in\C\).

\begin{theorem}[Exact resolvent carrier]
\label{thm:exact-resolvent-carrier}
The quadratic resolvent \(Q\) is normal and finite flat of rank two over
\(R\); after a trace-zero choice,
\[
Q\simeq R[w]/(w^2-d)
\]
for some \(d\in R\).  The cover \(T/Q\) is unramified in codimension one and
has character decomposition
\[
T\simeq Q\oplus L\oplus L^{[2]},
\qquad L^{[3]}\simeq Q.
\]
If \(\sigma\) denotes the nontrivial involution of \(Q/R\), then
\[
\sigma^*L\simeq L^{[2]}\simeq L^\vee;
\]
in particular, every local three-torsion class carried by \(L\) is
anti-invariant under the quadratic involution.  As an \(R\)-module, the
cubic trace-zero summand is exactly the eigensheaf:
\[
E\simeq L.
\]
Consequently
\[
\Delta_F\simeq\operatorname{Ext}^1_R(L,R),
\]
and the following are equivalent:
\[
\begin{aligned}
B\text{ is finite flat over }R
&\Longleftrightarrow L\text{ is locally free over }R,\\
&\Longleftrightarrow L\text{ is MCM over }Q.
\end{aligned}
\]
Locally at \(y\in Y\), the defect vanishes if and only if
\(L_\mathfrak q\) is MCM for every \(\mathfrak q\mid y\).
\end{theorem}

\begin{proof}
Invariant subrings of a normal domain under a finite group are normal, so
\(Q\) is normal.  As an \(R\)-module it is reflexive of rank two.  Its trace
splitting is \(Q=R\oplus N_0\) with \(N_0\) rank-one reflexive; factoriality
of \(R\) makes \(N_0\) free and gives the equation \(w^2=d\).

At a target divisor, the corrected inertia list is
\(U_0,U_1,U_2,B\); the inertia in the Galois closure is therefore trivial or
a transposition.  Its intersection with \(N=A_3\) is trivial, so \(T/Q\) is
unramified in codimension one.  The \(N\)-character idempotents split \(T\)
into three reflexive \(Q\)-modules.  Multiplication gives the asserted
reflexive powers because it is an isomorphism at every height-one prime.

Choose \(\sigma\in H\).  Its restriction to \(Q\) is the nontrivial
quadratic involution.  It interchanges the two nontrivial characters, so
\(\sigma^*L\simeq L^{[2]}\simeq L^\vee\).  Taking \(H\)-invariants gives
\[
B=T^H=R\oplus\{\ell+\sigma(\ell):\ell\in L\}.
\]
The map \(\ell\mapsto\ell+\sigma(\ell)\) is an \(R\)-linear isomorphism onto
the second summand.  Its cubic trace is zero because summing over
\(1,\tau,\tau^2\in N\) gives the factor \(1+\zeta+\zeta^2=0\).  Thus the
second summand is \(E\).

Finally, a regular system of parameters of \(R_y\) is a system of parameters
of every \(Q_\mathfrak q\) above it.  Hence \(L_\mathfrak q\) is MCM over
\(Q_\mathfrak q\) exactly when the underlying \(R_y\)-module has depth three.
Auslander--Buchsbaum over \(R_y\) turns that condition into freeness.  Use
\(E\simeq L\) and \cref{prop:cubic-ext-defect}.
\end{proof}

\begin{corollary}[Formal defect branches]
\label{cor:formal-cubic-defect}
Let \(y\in\operatorname{Supp}\Delta_F\) and
\(A=\widehat{R_y}\).  The completed normalization
\(B_y\otimes_{R_y}A\) has one normal local factor of rank three.  Its cubic
fraction-field extension is non-Galois and therefore has \(S_3\)-Galois
closure.
\end{corollary}

\begin{proof}
Excellence decomposes the completed finite algebra into normal local domains
of ranks summing to three.  A rank-one factor is \(A\).  A rank-two factor
splits by trace into \(A\) plus a rank-one reflexive module, which is free
because the complete regular local ring \(A\) is factorial.  Thus a nonfree
completion must have one rank-three factor.

If its cubic field extension were cyclic, the \(C_3\)-character idempotents
would split its integral closure into three rank-one reflexive \(A\)-modules.
All three would be free over the factorial ring \(A\), contradicting the
defect.  Hence the cubic branch is non-Galois.
\end{proof}

\begin{corollary}[Defective fibre length]
\label{cor:cubic-defect-fibre-length}
Let \(y\in\operatorname{Supp}\Delta_F\), and let \(b\) be the presentation
number in \cref{prop:cubic-ext-defect}.  Then \(\pi^{-1}(y)\) is supported at
one point and
\[
\operatorname{length}_\C(B\otimes_R\kappa(y))=b+3\ge4.
\]
The length is four exactly in the one-generator stratum.
\end{corollary}

\begin{proof}
The completed algebra has one local factor by
\cref{cor:formal-cubic-defect}, so the finite fibre has one support point.
Minimality of the presentation gives
\[
\dim_\C B_y/\mathfrak m_yB_y
 =1+\dim_\C E_y/\mathfrak m_yE_y
 =1+(b+2)=b+3.
\]
A defect has \(b\ge1\).
\end{proof}

\subsection{Codimension-two detection and explicit transverse covers}

\begin{corollary}[Resolvent defect curves]
\label{cor:resolvent-defect-curves}
If \((\Delta_F)_y\ne0\), then for some \(\mathfrak q\mid y\) there is a
height-two singular prime \(\mathfrak p\subset Q_\mathfrak q\) such that
\[
[L_\mathfrak p]\ne0
\quad\text{in}\quad
\operatorname{Cl}(Q_\mathfrak p)[3].
\]
For \(Q=R[w]/(w^2-d)\), the singular locus is cut out by
\[
(w,\partial_{y_1}d,\partial_{y_2}d,\partial_{y_3}d).
\]
In particular, a defect requires a singular curve of the quadratic resolvent;
an isolated resolvent singularity cannot carry it.
\end{corollary}

\begin{proof}
Dao's theorem makes the Picard group of the punctured spectrum of a
three-dimensional local hypersurface torsion-free.  It follows that
\[
\operatorname{Cl}(Q_\mathfrak q)[3]\hookrightarrow
\bigoplus_{\substack{\mathfrak p\in\operatorname{Sing}(Q_\mathfrak q)\\
                     \operatorname{ht}\mathfrak p=2}}
\operatorname{Cl}(Q_\mathfrak p)[3].
\]
By \cref{thm:exact-resolvent-carrier}, nonzero defect means that
\(L_\mathfrak q\) is not MCM.  Its class is therefore nonzero, while
\(L^{[3]}\simeq Q\) makes it three-torsion.  The Jacobian ideal of
\(w^2-d\) gives the displayed singular-locus equations.
\end{proof}

\begin{proposition}[Transverse ADE filter and explicit cyclic covers]
\label{prop:transverse-ADE-filter}
Assume that, after strict henselization and completion, every generic
transverse surface singularity at a height-two singular prime is a split
rational double point.  Then only
\[
A_{3r-1}\quad(r\ge1),\qquad E_6
\]
can carry a nonzero localization of the cubic defect class.  Each component
contributes at most one \(\mathbf F_3\)-coordinate.

For a transverse \(A_{3r-1}\) equation
\[
Q_0=k[[u,v,z]]/(uv-z^{3r}),
\]
the two nonzero order-three classes are represented by
\[
I_r=(u,z^r),\qquad I_{2r}=(u,z^{2r}).
\]
For \(j=r,2r\), the matrices
\[
\Phi_j=\begin{pmatrix}v&-z^j\\-z^{3r-j}&u\end{pmatrix},
\qquad
\Psi_j=\begin{pmatrix}u&z^j\\z^{3r-j}&v\end{pmatrix}
\]
satisfy
\[
\Phi_j\Psi_j=\Psi_j\Phi_j=(uv-z^{3r})I_2.
\]
The associated degree-three quasi-etale cyclic cover has transverse equation
\[
UV-z^r=0,
\]
so its type is \(A_{r-1}\), with \(A_0\) interpreted as smooth.

For a transverse \(E_6\) equation
\[
Q_0=k[[x,y,z]]/(x^2+y^3+z^4),
\]
choose \(i^2=-1\), put
\[
a=x+iz^2,\qquad b=x-iz^2,
\]
and set
\[
J_+=(a,y),\qquad J_-=(b,y).
\]
These are the two nonzero classes in \(\operatorname{Cl}(Q_0)\simeq\mathbf Z/3\).
For \(J_+\), an explicit matrix factorization is
\[
\Phi_+=\begin{pmatrix}b&-y\\y^2&a\end{pmatrix},
\qquad
\Psi_+=\begin{pmatrix}a&y\\-y^2&b\end{pmatrix},
\]
with the factorization for \(J_-\) obtained by interchanging \(a\) and \(b\).
The corresponding degree-three cyclic cover is
\[
k[[s,t,z]]/(s^3+t^3-2iz^2),
\]
a \(D_4\) rational double point.  The deck action is
\((s,t,z)\mapsto(\zeta s,\zeta^{-1}t,z)\), and its invariant coordinates are
\[
x=\frac{s^3-t^3}{2},\qquad y=st,\qquad z=z.
\]

Both cyclic covers carry a transposition lifting the quadratic involution and
conjugating the deck transformation to its inverse.  Their cubic
transposition quotients are explicit.  In the \(A_{3r-1}\) case, put
\[
c=U^3+V^3,\qquad \alpha=U+V.
\]
Then the regular base, quadratic resolvent, and cubic subcover are
\[
R_0=k[[c,z]],\qquad
Q_0=R_0[w]/(w^2-c^2+4z^{3r}),
\]
\[
B_0=R_0[\alpha]/(\alpha^3-3z^r\alpha-c)
    \simeq k[[\alpha,z]].
\]
In the \(E_6\) case, with \(\alpha=s+t\), they are
\[
R_0=k[[y,z]],\qquad
Q_0=R_0[x]/(x^2+y^3+z^4),
\]
\[
B_0=R_0[\alpha]/(\alpha^3-3y\alpha-2iz^2).
\]
The discriminants of the two displayed cubic polynomials are, respectively,
\[
-27(c^2-4z^{3r}),\qquad 108(y^3+z^4),
\]
so the displayed double covers are their quadratic resolvents, up to a unit
square.
\end{proposition}

\begin{proof}
The class groups of the split rational double points are the discriminant
groups of their ADE root lattices:
\[
\operatorname{Cl}(A_n)=\mathbf Z/(n+1),
\]
while the \(D_n,E_6,E_7,E_8\) groups have orders \(4,3,2,1\), respectively.
Thus nonzero three-torsion occurs precisely for \(A_{3r-1}\) and \(E_6\), and
the subgroup killed by three is \(\mathbf Z/3\).

For \(A_{3r-1}\), the ideals \((u,z^j)\) represent class \(j\) in
\(\mathbf Z/(3r)\), and direct multiplication gives the displayed matrix
factorizations.  The cyclic cover is obtained from
\[
u=U^3,\qquad v=V^3,\qquad UV=z^r;
\]
its \(C_3\)-invariants recover \(uv=z^{3r}\).

For \(E_6\), one has \(ab+y^3=x^2+y^3+z^4\).  Let
\(\mathfrak m=(x,y,z)\).  The prime \(P_+=(a,y)\) satisfies
\(Q_0/P_+\simeq k[[z]]\), and at its generic point \(b\) is a unit and
\(a=-y^3/b\).  Hence \(\operatorname{div}(a)=3P_+\).  The images of \(a\)
and \(y\) are linearly independent in \(P_+/\mathfrak mP_+\): their initial
linear terms are \(x\) and \(y\).  Thus \(P_+\) needs two generators and is
not principal, so its class has order three; \(J_-\) is the inverse class.
Direct multiplication gives
\[
\Phi_+\Psi_+=\Psi_+\Phi_+=(x^2+y^3+z^4)I_2,
\]
and the row \((a,y)\) gives
\((a,y)\Phi_+=(x^2+y^3+z^4,0)\).  The induced surjection from the
matrix-factorization cokernel to \(J_+\) is an isomorphism: both modules have
rank one, and the source is torsion-free because it is maximal
Cohen--Macaulay over the normal surface.

In the displayed \(D_4\) cover,
\[
\left(\frac{s^3-t^3}{2}\right)^2+(st)^3+z^4
 =\frac{(s^3+t^3)^2}{4}+z^4=0,
\]
and the invariant monomials are generated by \(s^3,t^3,st,z\).  With
\(p=s+t\) and \(q=s-t\), its equation becomes, after multiplying by a unit
and rescaling variables,
\[
z^2+p^3+pq^2=0,
\]
the standard \(D_4\) equation.

For the full group actions, set
\[
\tau(U,V,z)=(\zeta U,\zeta^{-1}V,z),\qquad
\sigma(U,V,z)=(V,U,z)
\]
in type \(A\), and use the same formulas with \((s,t,z)\) in type \(E_6\).
Then \(\sigma\tau\sigma=\tau^{-1}\).  In type \(A\), the full invariants are
\(k[[c,z]]\), while the \(\sigma\)-invariants are generated by
\(\alpha=U+V\) and \(z\), with
\(c=\alpha^3-3z^r\alpha\).  In type \(E_6\), the full invariants are
\(k[[y,z]]\), while the \(\sigma\)-invariants satisfy
\(\alpha^3-3y\alpha-2iz^2=0\).  The standard depressed-cubic discriminant
formula gives the two stated resolvents.  The involution exchanges
\(I_r\) with \(I_{2r}\), and \(J_+\) with \(J_-\), exactly as required by
\(\sigma^*L\simeq L^\vee\).
\end{proof}

\begin{remark}[Revised Lane 1 task]
\label{rem:revised-cubic-task}
The repair does not prove \(\Delta_F=0\).  It reduces the unknown input at a
candidate defect value to:
\begin{enumerate}[label=(\arabic*)]
\item the square class \(d\) defining the normal quadratic resolvent;
\item the height-two primes of its singular locus;
\item a fractional-ideal or finite-presentation representative of \(L\);
\item the local class vector \(([L_\mathfrak p])_\mathfrak p\);
\item a matrix factorization or other depth-three certificate extending the
explicit transverse \(A_{3r-1}\) and \(E_6\) models through the closed point,
or a Keller-specific constraint excluding every nonzero vector.
\end{enumerate}
Under the transverse-ADE hypothesis, every nonzero coordinate has an explicit
local MCM representative and the transverse cubic cover is either
\(A_{r-1}\to A_{3r-1}\) or \(D_4\to E_6\).  The remaining issue is the
three-dimensional extension and compatibility of these models, not their
generic transverse construction.
\end{remark}
~~~

[Back to the text-source index](../../index.md)
