# Lane 1 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`manuscripts/01-cubic-incidence/appendices/common-zero-normalization.tex`](#source-10ae5c3c67da2719) — `9d8b12dea23b9a893162d75b2a54dfdb7bc37e5e5b91fccd5bfbc45eb4f6a6e8`
- [`manuscripts/01-cubic-incidence/appendices/minimal-smooth-defect.tex`](#source-3407c8647c683185) — `5702f46bd66987866a88995e8f612b09cb806205d87aba108de95186e178ef55`
- [`manuscripts/01-cubic-incidence/appendices/moving-hyperplanes.tex`](#source-8c8d23e973cf6889) — `15858376d140e430c9e0957f1f05e5066443c57a50a8c157fb75003de0c1d35d`
- [`manuscripts/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex`](#source-2a89eeb089e26d9e) — `1d5968d312f3dcb6f77a33f2b74dbf26791908f7b3b5c676654d2d83efbde69c`
- [`manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`](#source-340482aba615ef8a) — `c85a7462c73f776676897468ff3d421efb7d1b828fa84b1fd90c400cf225cb71`
- [`research-notes/finite-diagnostics-20260803-v1/verify_lane1_marked_root_benchmark.py`](#source-6f60cc42cc5e64fc) — `8a8f19d6685f9e40af06d1a27ee6f1f3f03e0750f1dc4afbf02b2377107bb99d`
- [`research-notes/lane1-collision-saturation-20260802-v1/INTEGRATION-v8.md`](#source-9f90a471b9d6c6af) — `d454c71f9cd4c2fe4bdb19544a636592ccad52a768f45e6ba1a0d11a5761a58e`
- [`research-notes/lane1-collision-saturation-20260802-v1/cubic-flatness-normalization-defects.md`](#source-f5239a257b61f4d8) — `a3d9ccebc6cc7b36dd30c30e9c36736e15d8cb4fc45f2f256b8b1be8c3054904`
- [`research-notes/lane1-collision-saturation-20260802-v1/flatness-defect-repairs.tex`](#source-31b28e4d427212ea) — `cfd9064969c8a42a85ae1701c234afb0dd80c7ae76c20ee609ae92206cd2560b`
- [`research-notes/lane1-collision-saturation-20260802-v1/lane1-collision-v8-manifest.json`](#source-3f54e773a7d88aaf) — `247bf32b22350cf724573eb52492e424a643d3a2279c675ec3aad604f6ffbb2b`
- [`research-notes/lane1-collision-saturation-20260802-v1/verify_collision_idempotent.py`](#source-9425e75cd188cddb) — `80e9117af525529b12dd8d36dac6c07c71e77cecec6d1819b289f65cc3fac842`
- [`research-notes/lane1-collision-saturation-20260802-v1/verify_standard_collision_model.py`](#source-915e7bbeb67e7bc2) — `75f47234d04b0123f850ab42ba6c94a11d6aac7426b09edd914d12cfd26c31c5`
- [`research-notes/lane1-collision-saturation-20260803-v2/README.md`](#source-c8ccaa464f51cbd5) — `daf64d1902bb3ca28882e06faec4fa9d15accb4e7097c8e773d0e92686db9e3f`
- [`research-notes/lane1-collision-saturation-20260803-v2/flatness-defect-repairs-full.tex`](#source-195de0d23627037b) — `4b468e00f6c83f158c89e90a8819858b91a1d1f4dfd7c582915204236efdb60c`
- [`research-notes/lane1-collision-saturation-20260803-v2/manifest.json`](#source-d8d50dd353502656) — `468b8fd9ed5d4e2f690416148224b8d4cdde3a9cfd6070d839d028db82ecba6e`
- [`research-notes/lane1-models-20260803-v1/README.md`](#source-aef55c7c330abe18) — `955bf681d1c881101c2b690404ca787f6b0785c192a812ca9b967d25cacf3c1d`
- [`research-notes/lane1-models-20260803-v1/TYPEIV_GATE.md`](#source-69caa73289f1610d) — `fc6262ba417a993a28af714cd230503f031677aacc8d138e0d369088be1f0681`
- [`research-notes/lane1-models-20260803-v1/elliptic-cone-negative-model.md`](#source-ecb5fca02f9c9fd5) — `0bb0d29186b80874f2d72c8b54e7d2c0be7bda6b1c8760f0a363dee2bfa6b9e5`
- [`research-notes/lane1-models-20260803-v1/explicit-marked-root-benchmark.tex`](#source-de0db01cd5a38c2c) — `132e8a415bf2eb89419d2207bf4c4c1bc869bcbf0b17e4a939cb1629f3eca441`
- [`research-notes/lane1-models-20260803-v1/explicit-marked-root-collision-saturation.tex`](#source-87c7cf6aee0542db) — `d7499b377097c7a830a53c2a21cc0aebedb8234d71b1a7e1228f62c506a5bd6f`
- [`research-notes/lane1-models-20260803-v1/typeiv-explicit-net-data.json`](#source-192a60b955e4b3a2) — `ecc1248b165e14040c564e822133d83211288f72427e56d17958537bde064731`
- [`research-notes/lane1-models-20260803-v1/typeiv-hessian-eigensheaf-data.json`](#source-091293c487a1bfdf) — `1e4f68d7e622bfe4f1e3f1d31c59a0811bccc23e946089f8dafe06ff9fdec3df`
- [`research-notes/lane1-models-20260803-v1/verify_elliptic_cone_model.py`](#source-e961b52492bf9fdf) — `ff28a4aa4d4a7da25761566bbd64bf5b6872660dfe6fde26abd04cce29132463`
- [`research-notes/lane1-models-20260803-v1/verify_homogeneous_typeiv.py`](#source-4878f853b11d07dd) — `c788ee4012b418396ec9dc7a90469d9a4e72ffefdd1b899fc21045658406f505`
- [`research-notes/lane1-models-20260803-v1/verify_marked_root_benchmark.py`](#source-eb2e6a9bd27953e2) — `61dfcabb24af8be43112948484599d392aceb0214909efb7cc08b15904a85c6d`
- [`research-notes/lane1-models-20260803-v1/verify_marked_root_collision_saturation.py`](#source-31b4a29aadab18de) — `59724e6cbb60e8ea9503a0542543997d01c2843fd980888c6e3e0ff058267341`
- [`research-notes/lane1-models-20260803-v1/verify_typeiv_explicit_net.py`](#source-0de51d18f6967859) — `e55d331aee6a2b609f522deca8c4ec61f703b0fd1d4bfe203e8d0fd6788d20c5`
- [`research-notes/lane1-models-20260803-v1/verify_typeiv_hessian_eigensheaf.py`](#source-a63fd62f849645df) — `350fd7f95f4234ed0bfeb82947913953e8c1df73c7682e1c2f66cd6820c463fb`

<a id="source-10ae5c3c67da2719"></a>

## `manuscripts/01-cubic-incidence/appendices/common-zero-normalization.tex`

<pre><code class="language-tex">
\section{Common zeros, maximal cubic orders, and the missing local model}
\label{app:common-zero-normalization}

The squarefree and coprime locus already suffices for the principal
classification in the body.  When \(A\) and \(B\) have a common zero,
however, the primitive root coordinate need not give the finite
normalization.  This appendix gives the correction and an explicit example
with two unramified sheets deleted along one divisor.

\subsection{The corrected cubic order}

Let
\&#91;
R=\C&#91;a,b,c&#93;,\qquad
P(T)=A(c)T^3+B(c)T^2+bT-2a,
\&#93;
and let \(t\) denote a root of \(P\) in the generic cubic extension.  Put
\&#91;
\omega=A(c)t,\qquad
\theta=A(c)t^2+B(c)t.
\&#93;
Then
\begin{equation}
\label{eq:primitive-cubic-order}
\omega^2=A\theta-B\omega,\qquad
\omega\theta=2Aa-b\omega,\qquad
\theta^2=2aB+2a\omega-b\theta.
\end{equation}
Thus \(R\oplus R\omega\oplus R\theta\) is the primitive finite cubic order.

For every zero \(\beta\) of \(A\), write
\&#91;
m_\beta=\ord_\beta A,\qquad n_\beta=\ord_\beta B
\&#93;
and set
\&#91;
k_\beta=\min\set{n_\beta,\left\lfloor m_\beta/2\right\rfloor},
\qquad
H(c)=\prod_{\beta\in Z(A)}(c-\beta)^{k_\beta}.
\&#93;
Equivalently, \(H\) is the largest monic polynomial such that
\&#91;
H^2\mid A,\qquad H\mid B.
\&#93;
Write
\&#91;
\overline A=A/H^2,\qquad \overline B=B/H,\qquad q=\omega/H.
\&#93;

\begin{theorem}&#91;Maximal-order correction&#93;
\label{thm:common-zero-normalization}
The integral closure of \(R\) in the generic cubic extension is
\&#91;
\mathcal C^{\mathrm{nor}}=R\oplus Rq\oplus R\theta,
\&#93;
with multiplication
\begin{align}
q^2&amp;=\overline A\theta-\overline Bq,\label{eq:nor-q2}\\
q\theta&amp;=2aH\overline A-bq,\label{eq:nor-qt}\\
\theta^2&amp;=2aH\overline B+2aHq-b\theta.\label{eq:nor-t2}
\end{align}
It is finite flat of degree three over \(R\).  If \(\mathscr D\) is the
primitive binary-cubic discriminant, then
\&#91;
\Disc(\mathcal C^{\mathrm{nor}})=\mathscr D/H^2.
\&#93;
\end{theorem}

\begin{proof}
The identities \eqref{eq:nor-q2}--\eqref{eq:nor-t2} follow from
\eqref{eq:primitive-cubic-order}; hence the displayed module is a finite
free cubic order.  The change from the basis \((1,q,\theta)\) to
\((1,\omega,\theta)\) has determinant \(H\), giving the discriminant
formula.

It remains to prove maximality.  At a zero \(\beta\) of \(A\), the
\((c-\beta)\)-content of
\&#91;
\mathscr D
=B^2b^2-4Ab^3+8aB^3-36aABb-108a^2A^2
\&#93;
has order
\&#91;
\delta_\beta=\min(m_\beta,2n_\beta).
\&#93;
After division by \(H^2\), the residual exponent is
\&#91;
\delta_\beta-2k_\beta=
\begin{cases}
1,&amp;m_\beta&lt;2n_\beta\text{ and }m_\beta\text{ is odd},\\
0,&amp;\text{otherwise}.
\end{cases}
\&#93;
The nonvertical factor is also reduced: as a quadratic in \(a\), its
discriminant is
\&#91;
-64(3Ab-B^2)^3,
\&#93;
which is not a square in \(\C(c,b)\).  Thus
\(\mathscr D/H^2\) is squarefree.

For a cubic order over a discrete valuation ring, the discriminant of a
proper suborder differs from that of the maximal order by the square of its
index.  The squarefree discriminant therefore makes every height-one
localization of \(\mathcal C^{\mathrm{nor}}\) maximal.  The algebra is free
over the regular ring \(R\), hence satisfies \(S_2\); height-one maximality
and Serre's criterion show that it is normal.  It is consequently the
integral closure.
\end{proof}

\subsection{The four generic divisor behaviors}

\begin{proposition}&#91;Four generic divisor behaviors&#93;
\label{prop:four-generic-divisor-behaviors}
Let \(\beta\ne\alpha\) be a zero of \(A\), and retain the notation
\((m_\beta,n_\beta)\).  The generic behavior over the plane \(c=\beta\) is
as follows:
\begin{center}
\small
\begin{tabular}{@{}p{0.26\textwidth}p{0.40\textwidth}cc@{}}
\textbf{Condition}&amp;\textbf{Completed fiber}&amp;
\textbf{Affine size}&amp;\textbf{Inertia}\\ \hline
\(B(\beta)\ne0\)&amp;
one simple infinity root deleted&amp;2&amp;1\\
\(B(\beta)=0,\ m_\beta&lt;2n_\beta\), with \(m_\beta\) odd&amp;
one ramified pair deleted&amp;1&amp;\((12)\)\\
\(B(\beta)=0\), otherwise&amp;
two unramified sheets deleted&amp;1&amp;1
\end{tabular}
\end{center}
Together with the excluded generic three-cycle behavior, these are the four
generic divisor types stated in \cref{rem:lost-sheet-types}.
\end{proposition}

\begin{proof}
In the reciprocal coordinate \(u=1/t\), the two roots approaching
infinity satisfy
\&#91;
A_0s^{m_\beta}+B_0s^{n_\beta}u+bu^2-2au^3=0,
\qquad s=c-\beta.
\&#93;
If \(m_\beta&lt;2n_\beta\), both valuations are \(m_\beta/2\), and the pair
ramifies exactly when \(m_\beta\) is odd.  If \(m_\beta=2n_\beta\), the
residual quadratic after \(u=s^{n_\beta}v\) is
\&#91;
bv^2+B_0v+A_0.
\&#93;
If \(m_\beta&gt;2n_\beta\), the two valuations are \(n_\beta\) and
\(m_\beta-n_\beta\).  This proves the table and, in particular, separates
the one-sheet and two-sheet unramified cases.
\end{proof}

\subsection{An explicit two-sheet-loss example}

\begin{proposition}&#91;A \(U_2\) Keller map&#93;
\label{prop:u2-example}
Take
\&#91;
A(c)=c(c-1)^2,\qquad B(c)=2(c-1),\qquad \alpha=0,
\&#93;
and
\&#91;
c=2x+(6-3y)x^2-x^3z,\qquad t=y+\frac1x.
\&#93;
Define
\&#91;
b=\frac2x-3c(c-1)^2t^2-4(c-1)t
\&#93;
and
\&#91;
2a=\frac{2t}{x}-2c(c-1)^2t^3-2(c-1)t^2.
\&#93;
The apparent poles cancel.  The map \(F=(a,b,c)\) is polynomial of
component degrees \((15,14,4)\), has
\&#91;
\det DF=-2,
\&#93;
and has the collision
\&#91;
F(0,4,-22)=F(1,-1,11)=F(-1,2,2)=(0,2,0).
\&#93;
Along \(c=1\), the finite normalization has one retained sheet and two
generically unramified deleted sheets.
\end{proposition}

\begin{proof}
Here \(H=c-1\), \(\overline A=c\), and \(\overline B=2\).  The normalized
binary cubic is
\&#91;
cT^3+2ST^2+bS^2T-2a(c-1)S^3.
\&#93;
At \(c=1\) it becomes
\&#91;
T(T^2+2ST+bS^2).
\&#93;
The root \(T=0\) is the retained affine sheet, while the quadratic factor
gives two distinct sheets for generic \(b\).  Direct expansion gives the
polynomiality, degrees, determinant, and displayed collision.
\end{proof}

For this example the normalized discriminant is
\&#91;
\mathscr D_{\mathrm{nor}}
=-4\bigl(
27a^2c^4-54a^2c^3+27a^2c^2+18abc^2-18abc
-16ac+16a+b^3c-b^2
\bigr),
\&#93;
and
\&#91;
\mathscr D_{\mathrm{nor}}|_{c=1}=-4b^2(b-1).
\&#93;
Consequently
\&#91;
S_F=V(\mathscr D_{\mathrm{nor}})\cup V(c-1).
\&#93;
The line \(V(c-1,b)\) is omitted, whereas \(V(c-1,b-1)\) is a
branch/plane intersection that is not omitted.  Hence
\&#91;
\A^3\setminus F(\A^3)\subsetneq\Sing(S_F).
\&#93;
This shows that the equality between omission and the singular locus seen
in the base map is not a general feature of the cubic frame.

\begin{remark}
The all-multiplicity ordinary left--right classification is already
\cref{thm:equivalence}.  Stable recovery in the presence of common roots
requires the weighted relative-Jacobian package developed in the stable
moduli companion paper \cite{monson2026stablemoduli}.
\end{remark}
</code></pre>

<a id="source-3407c8647c683185"></a>

## `manuscripts/01-cubic-incidence/appendices/minimal-smooth-defect.tex`

<pre><code class="language-tex">
\section{The minimal smooth defect: formal rigidity and sign torsors}
\label{app:minimal-smooth-defect}

This appendix records what can be proved about the first possible nonflat
cubic normalization.  It does not exclude that defect: the final
end-to-global step remains open.

Assume that the local defect has length one, that the discriminant has its
minimal multiplicity six, and that the resulting leading plane cubic
\(C_\phi\subset\PP^2\) is smooth.  On the exceptional plane
\(E=\PP^2\), let \(Q\) be the rank-two quotient bundle and put
\&#91;
 W_k=H^0\!\left(E,\Sym^3 Q(k)\right).
\&#93;
The order-\(k\) coordinate-and-frame gauge space is
\&#91;
 A_k=H^0\!\left(E,\operatorname{At}(\Omega^1_E)(k)\right).
\&#93;
For the leading cubic \(\phi\), the infinitesimal action is
\&#91;
 \delta_{\phi,k}(A)
 =
 \left&#91;
 \sum_{i,j}A_{ij}(x)q_i\frac{\partial\phi}{\partial q_j}
 \right&#93;\in W_k.
\&#93;

\begin{theorem}&#91;Formal normal rigidity&#93;
\label{thm:smooth-cubic-normal-rigidity}
If \(C_\phi\) is smooth, then
\&#91;
\delta_{\phi,k}\colon A_k\longrightarrow W_k
\&#93;
is surjective for every \(k\geq1\).  Consequently every normalized formal
datum
\&#91;
\eta=s^2\bigl(\phi+s\psi_1+s^2\psi_2+\cdots\bigr)
\&#93;
is formally gauge-equivalent, with its leading cubic fixed, to \(s^2\phi\).
\end{theorem}

\begin{proof}
There is a natural bundle map
\&#91;
V^\vee\otimes Q\longrightarrow\Sym^3Q.
\&#93;
On a line \(H\), its image is the product of the binary linear forms with
the span of the restrictions of the three partial derivatives of \(\phi\).
Those binary quadratics have no common zero when \(C_\phi\) is smooth, and
therefore generate every binary cubic after multiplication by linear forms.
The bundle map is consequently surjective.

If \(K_\phi\) is its kernel, an exact Hesse-form calculation at twist one
gives
\&#91;
\det\delta_{\phi_\lambda,1}
=-3^{24}(\lambda^3-1)^6.
\&#93;
The determinant is nonzero precisely on the smooth Hesse locus.  Together
with the Chern classes of \(K_\phi\), the resulting cohomology vanishing
identifies \(K_\phi\simeq\Omega^1_{\PP^2}\).  Thus
\&#91;
0\longrightarrow\Omega^1_{\PP^2}
\longrightarrow\operatorname{At}(\Omega^1_{\PP^2})
\xrightarrow{\delta_\phi}\Sym^3Q
\longrightarrow0.
\&#93;
After twisting, \(H^1(\PP^2,\Omega^1(k))=0\) for \(k\geq1\), which proves
surjectivity.  Removing \(\psi_k\) successively gives the formal
normalization.  The exact script
\texttt{cubic\_jet\_rank\_check.py}, stored under
\texttt{code/minimal-smooth-defect/}, checks the Hesse determinant and the
first Fermat ranks over \(\mathbb Q\).
\end{proof}

\begin{remark}
At \(k=0\), the cokernel is
\(H^1(\PP^2,\Omega^1)\simeq\C\), the expected modulus of a plane cubic.
Thus the formal normal direction introduces no additional modulus.  The
statement is formal on the blown-up incidence model; compatibility with the
unsaturated Rees lattice is part of any later descent through the blowdown.
\end{remark}

We next pass to the \(S_3\)-Galois closure.  Its exceptional surface is
\&#91;
A=C_\phi\times C_\phi.
\&#93;
Using ordered collinear triples
\((p_1,p_2,p_3)\), with \(p_1+p_2+p_3=0\), the three
transposition-fixed collision curves are
\&#91;
\Gamma_{12}=(t,t),\qquad
\Gamma_{23}=(-2t,t),\qquad
\Gamma_{31}=(t,-2t).
\&#93;

\begin{theorem}&#91;Local sign-\(3\) torsors&#93;
\label{thm:local-sign-torsors}
The \(3\)-torsion line bundles on \(A\) that restrict trivially to all three
collision curves form
\&#91;
K_{\mathrm{loc}}
=
\ker\!\left(
\operatorname{Pic}^0(A)&#91;3&#93;\longrightarrow
\prod_{i&lt;j}\operatorname{Pic}^0(\Gamma_{ij})&#91;3&#93;
\right)
\simeq C_\phi&#91;3&#93;\simeq\F_3^2.
\&#93;
The subgroup \(A_3\subset S_3\) fixes \(K_{\mathrm{loc}}\), while a
transposition acts by inversion.  Each class is represented by an algebraic
finite étale cover of the proper henselian local Galois end.
\end{theorem}

\begin{proof}
Write a degree-zero line bundle as
\&#91;
L_{\alpha,\beta}
=\operatorname{pr}_1^*P_\alpha\otimes
 \operatorname{pr}_2^*P_\beta.
\&#93;
Its three restrictions correspond respectively to
\&#91;
\alpha+\beta,\qquad -2\alpha+\beta,\qquad \alpha-2\beta.
\&#93;
They vanish simultaneously exactly when
\(\beta=-\alpha\) and \(3\alpha=0\), proving the first assertion.  A
three-cycle fixes \(L_{\alpha,-\alpha}\), whereas a transposition sends it
to its inverse.

For nonzero \(\alpha\), the algebra
\&#91;
\mathcal O_A\oplus L_\alpha\oplus L_\alpha^{\otimes2}
\&#93;
is a connected finite étale \(\mu_3\)-torsor.  Finite étale covers of a
proper scheme over a henselian local ring are equivalent to finite étale
covers of its closed fiber, so these torsors extend uniquely over the
henselian local Galois completion.
\end{proof}

\begin{question}&#91;End-to-global sign torsor&#93;
\label{q:end-to-global-sign-torsor}
Does at least one nonzero class of \(K_{\mathrm{loc}}\) extend across the
global Keller boundary with the required sign equivariance and split
transposition inertia?  Such a class would descend to a nontrivial finite
étale degree-three cover of \(\A^3\), which is impossible.
\end{question}

The omitted value itself gives a useful global fibration.

\begin{proposition}&#91;Direction fibration from an omitted value&#93;
\label{prop:omitted-direction-map}
Let \(F\colon\A^3\to\A^3\) be a complex Keller map and
\(p\notin F(\A^3)\).  Then
\&#91;
g_p\colon\A^3\longrightarrow\PP^2,\qquad
x\longmapsto&#91;F(x)-p&#93;
\&#93;
is smooth of relative dimension one, and its image is the complement of at
most finitely many points.
\end{proposition}

\begin{proof}
The differential of projectivization is the quotient by the line
\(\langle F(x)-p\rangle\).  Composing it with the invertible matrix \(DF_x\)
has rank two, so \(g_p\) is smooth.  Its image is open.  If its complement
contained a curve \(V(H)\), the polynomial \(H(F-p)\) would be nowhere zero
on affine space and hence constant.  The injectivity of
\(F^*\colon\C&#91;a,b,c&#93;\to\C&#91;x,y,z&#93;\) would then make the nonconstant
homogeneous polynomial \(H(a-p)\) constant, a contradiction.
\end{proof}

The remaining obstruction in \cref{q:end-to-global-sign-torsor} is therefore
carried by the horizontal boundary of a smooth curve fibration over a
cofinite open subset of \(\PP^2\), not by complicated base monodromy.
</code></pre>

<a id="source-8c8d23e973cf6889"></a>

## `manuscripts/01-cubic-incidence/appendices/moving-hyperplanes.tex`

<pre><code class="language-tex">
\section{Discriminant-dependent hyperplanes}
\label{app:moving-hyperplanes}

This appendix treats the first nonlinear deformations of the hyperplane
that cuts out the marked-root model.  It is logically independent of the
classification in the body of the paper and is retained as a self-contained
working argument.

Write
\&#91;
L=aX+bY,\qquad M=-qX+pY,\qquad ap+bq=1,
\&#93;
and
\&#91;
\Phi_{G,\gamma}=L(M^2+\gamma L^2).
\&#93;
The normalized factor space is \(SL_2\times\A^1_\gamma\), and its coefficient
map to binary cubics is
\&#91;
\begin{aligned}
A_0&amp;=a^3\gamma+aq^2,\\
A_1&amp;=3a^2b\gamma-2apq+bq^2,\\
A_2&amp;=3ab^2\gamma+ap^2-2bpq,\\
A_3&amp;=b^3\gamma+bp^2.
\end{aligned}
\&#93;
Its discriminant is \(\Disc(\Phi_{G,\gamma})=-4\gamma\).

Let \(\lambda(t)\) be a polynomial family of nonzero covectors whose generic
projective class is tangent but not osculating to the twisted cubic.  For
\(f\in\C&#91;t&#93;\), define the full marked-simple-root incidence by
\&#91;
X_{\lambda,f}=
\set{(G,\gamma):
 \lambda(\gamma)(\Phi_{G,\gamma})=f(\gamma)}.
\&#93;

\begin{theorem}&#91;Moving-tangent rigidity&#93;
\label{thm:moving-tangent}
If \(X_{\lambda,f}\simeq\A^3\), then \(f\) is a nonzero constant,
\(\lambda(t)\) has tangent nonosculating type for every \(t\), and there is
an \(h(t)\in SL_2(\C&#91;t&#93;)\) carrying \(\lambda(t)\) to a fixed tangent
normal.  The resulting incidence projection is polynomially left--right
equivalent to the original marked-root map.  Conversely, these conditions
give that class.
\end{theorem}

\begin{proof}
At a fixed value \(t=\gamma\), put the normal into tangent form \(A_2\) or
osculating form \(A_3\).  Stratification of the corresponding hypersurface
in \(SL_2\) gives the compactly supported Euler table
\&#91;
\begin{array}{c|rrrr}
&amp;t\ne0,\ c\ne0&amp;t\ne0,\ c=0&amp;t=0,\ c\ne0&amp;t=0,\ c=0\\
\hline
\text{tangent }(2,1)&amp;3&amp;0&amp;1&amp;0\\
\text{osculating }(3)&amp;-3&amp;0&amp;0&amp;0\\
\text{zero normal}&amp;0&amp;0&amp;0&amp;0.
\end{array}
\&#93;
For example, in tangent form
\&#91;
A_2=3a(p^2+b^2t)-2p.
\&#93;
The stratum \(b=0\) contributes one when the level is nonzero.  On
\(b\ne0\), the divisor \(p^2+b^2t=0\) consists, for \(t\ne0\), of two
copies of \(\Gm\); the two exceptional centers are replaced by affine
lines, giving the remaining contribution two.  In osculating form,
\&#91;
A_3=b(p^2+b^2t),
\&#93;
and the nonzero-level fiber is \(\A^1\) times a genus-one double cover of
\(\PP^1_b\) with three punctures, hence has Euler characteristic \(-3\).

Euler integration over \(\A^1_t\) now gives
\(\cchi(X_{\lambda,f})\le1\).  Equality is possible only when \(f\) has no
zero, the normal never degenerates, and the fiber over \(t=0\) is tangent
at nonzero level.  Thus \(f\in\C^*\) and every specialization has type
\((2,1)\).

Represent the normal as a binary cubic
\(\Lambda(t;U,V)\).  Since it has type \((2,1)\) everywhere, Gauss's lemma
factors it as
\&#91;
\Lambda=rL^2M
\&#93;
with polynomial linear forms \(L,M\), where \(r\) and
\(\det(L,M)\) are nonzero constants.  Their coefficient rows therefore
give \(h(t)\in SL_2(\C&#91;t&#93;)\).  The target transformation
\&#91;
\Psi_h(\Phi)=h\!\left(-\Disc(\Phi)/4\right)\cdot\Phi
\&#93;
is a polynomial automorphism because the discriminant is \(SL_2\)-invariant.
Equivariance supplies the matching source automorphism and reduces the
equation to a fixed tangent hyperplane at nonzero constant level.
\end{proof}

The infinitesimal \(SL_2\)-orbit of the tangent normal \(A_2\) spans
\(A_1,A_2,A_3\); the first transverse coefficient is \(A_0\).  The first
nonlinear transverse family is therefore
\&#91;
X_\kappa=
\set{A_2+\kappa\gamma A_0=c}
\subset SL_2\times\A^1,
\qquad \kappa,c\in\C^*.
\&#93;

\begin{theorem}&#91;First transverse obstruction&#93;
\label{thm:first-transverse}
For every \(\kappa,c\ne0\),
\&#91;
\cchi(X_\kappa)=-5.
\&#93;
In particular, \(X_\kappa\not\simeq\A^3\).
\end{theorem}

\begin{proof}
On \(a=0\), one has \(bq=1\), \(A_0=0\), and \(A_2=-2p\); this stratum is
\(\Gm\times\A^1\) and contributes zero.  On \(a\ne0\), set
\&#91;
s=b/a,\qquad z=aq,\qquad u=3s^2+\kappa t.
\&#93;
After multiplying by \(a\), the equation is quadratic in \(z\):
\&#91;
uz^2-4sz+1+a^4tu-ac=0.
\&#93;
The locus \(u=0\) contributes one.  On \(u\ne0\), the quadratic cover has
base Euler characteristic zero, so its contribution is minus that of its
branch surface.  After putting \(w=a^2u/\sqrt\kappa\), the branch equation
is controlled inside \((\Gm)^2_{a,w}\) by
\&#91;
D_A=V(4+3w^2),\qquad D_C=V(1-ac+w^2).
\&#93;
Here
\&#91;
\cchi(D_A)=0,\qquad
\cchi(D_C)=-2,\qquad
\cchi(D_A\cap D_C)=2.
\&#93;
The two-sheet, one-sheet, empty, and affine-line fibers over the four
resulting strata give branch-surface Euler characteristic \(6\).
Consequently \(\cchi(X_\kappa)=1-6=-5\).
\end{proof}

For a general polynomial \(r(t)\), the same calculation reduces
\&#91;
\set{A_2+r(\gamma)A_0=c}
\&#93;
to an explicit branch-surface Euler problem.  If \(n(r)\) is the number of
distinct roots of \(r\), a necessary condition for affine-three-space
source is
\&#91;
\cchi(\mathcal B_r)=n(r)-1.
\&#93;
Determining whether any higher \(r\) satisfies this condition remains open.
</code></pre>

<a id="source-2a89eeb089e26d9e"></a>

## `manuscripts/01-cubic-incidence/appendices/quadratic-covariant-rigidity.tex`

<pre><code class="language-tex">
\section{Quadratic covariant rigidity}
\label{app:quadratic-covariant-rigidity}

We retain the universal marked-root coordinates
\&#91;
G=\begin{pmatrix}a&amp;b\\-q&amp;p\end{pmatrix}\in\operatorname{SL}_2,
\qquad
L=aX+bY,\qquad M=-qX+pY,
\&#93;
and
\&#91;
\Phi_{G,t}=L(M^2+tL^2)
=A_0X^3+A_1X^2Y+A_2XY^2+A_3Y^3.
\&#93;
Thus
\begin{align*}
A_0&amp;=a^3t+aq^2,\\
A_1&amp;=3a^2bt-2apq+bq^2,\\
A_2&amp;=3ab^2t+ap^2-2bpq,\\
A_3&amp;=b^3t+bp^2,
\end{align*}
and \(\Disc(\Phi_{G,t})=-4t\).  The base construction is the full
incidence over \(A_2=c\), with \(c\ne0\).

\subsection{The Hessian summand}

Write, up to a common nonzero scalar,
\&#91;
\operatorname{Hess}(\Phi)=H_0X^2+H_1XY+H_2Y^2,
\&#93;
where
\&#91;
H_0=3A_0A_2-A_1^2,\quad
H_1=9A_0A_3-A_1A_2,\quad
H_2=3A_1A_3-A_2^2.
\&#93;
For \(\eta=(\eta_0,\eta_1,\eta_2)\), put
\&#91;
Q_\eta=\eta_0H_0+\eta_1H_1+\eta_2H_2.
\&#93;

\begin{theorem}&#91;Hessian exclusion&#93;
\label{thm:hessian-exclusion}
For \(\eta\ne0\) and \(\kappa\ne0\), the target
\&#91;
Y_{\eta,\kappa,c}=V(A_2+\kappa Q_\eta-c)
\&#93;
and its full marked-root incidence preimage cannot both be isomorphic to
\(\A^3\).
\end{theorem}

\begin{proof}
As a quadratic form on the four-dimensional coefficient space,
\&#91;
\det Q_\eta=\frac{81}{16}(\eta_0\eta_2-\eta_1^2)^2.
\&#93;
If this determinant is nonzero, translation removes the linear term
\(A_2\), leaving a smooth affine quadric or a singular quadric cone, never
\(\A^3\).  If \(\eta_0\eta_2-\eta_1^2=0\), write
\(\eta=(u^2,uv,v^2)\).  The kernel is generated by
\&#91;
(-v^3,3uv^2,-3u^2v,u^3).
\&#93;
When \(uv=0\), the target is a cylinder over an affine quadric surface.  It
remains only to consider \(uv\ne0\), for which the stabilizer of \(A_2\)
reduces to \(\eta=(1,1,1)\).

Set
\&#91;
\ell=a+b,\quad r=b,\quad m=p-q,\quad s=p,
\qquad \ell s-rm=1.
\&#93;
The incidence equation is linear in \(t\), with coefficient
\&#91;
3D,\qquad D=r^2(\ell-r)+\kappa\ell^2.
\&#93;
On \(D\ne0\), \(t\) is unique.  On \(D=0\), put \(x=r/\ell\); then
\&#91;
\ell=-\frac{\kappa}{x^2(1-x)},\qquad
x\in\A^1\setminus\{0,1\}.
\&#93;
The compatibility equation is quadratic in \(m\), with discriminant
\&#91;
-4\kappa^2(3x^4-4x^3+4\kappa c).
\&#93;
If \(\nu\) is the number of roots of the quartic away from \(0,1\),
Euler integration gives
\&#91;
\cchi(X_{\eta,\kappa,c})=-1-\nu.
\&#93;
It is therefore never \(1=\cchi(\A^3)\).
\end{proof}

\subsection{Rank-one squares}

The quadratic representation decomposes as
\&#91;
\Sym^2(\Sym^3\C^2)
\simeq \Sym^6\C^2\oplus\Sym^2\C^2.
\&#93;
The second summand is the Hessian component.  The rank-one locus in the
Cartan component consists of squares \(E_\xi(\Phi)^2\), where
\(E_\xi(\Phi)=\Phi(\xi)\).

\begin{theorem}&#91;Rank-one square classification&#93;
\label{thm:rank-one-cartan}
For
\&#91;
A_2+\kappa E_\xi(\Phi)^2=c,
\&#93;
one endpoint orbit is polynomially gauge-equivalent to the base construction
from a tangent hyperplane.  The other endpoint has incidence Euler
characteristic \(-1\) or \(0\).  The open orbit has Euler
characteristic \(-1\) or \(-2\).  Hence no inequivalent full-incidence
\(\A^3\) occurs.
\end{theorem}

\begin{proof}
For the endpoint \(E_\xi=A_3\), the target shear
\&#91;
\Phi(X,Y)\longmapsto\Phi\left(X,Y+\frac{\kappa A_3}{3}X\right)
\&#93;
sends \(A_2\) to \(A_2+\kappa A_3^2\) and lifts to the factor frame.
For the endpoint \(E_\xi=A_0\), the incidence equation is quadratic in
\(t\).  Its branch equation is
\&#91;
4\kappa c\ell^4-16\kappa\ell^3mr-4\kappa\ell^3+9r^4=0,
\&#93;
which gives \(\cchi=-1\) for \(c\ne0\) and \(0\) for \(c=0\).
For the open orbit, adapted coordinates reduce the branch equation to one
generic stratum and the two exceptional values \(x=0,2/3\), giving
\&#91;
\cchi=-\mathbf 1_{\{c\ne0\}}
-\mathbf 1_{\{81\kappa c+4\ne0\}}.
\&#93;
\end{proof}

\subsection{Products of distinct evaluations}

\begin{theorem}&#91;Two-evaluation exclusion&#93;
\label{thm:two-evaluation-exclusion}
For distinct \(\xi,\eta\in\PP^1\), every \(\kappa\ne0\), and every \(c\),
\&#91;
Y_{\xi,\eta}=V(A_2+\kappa E_\xi E_\eta-c)\simeq\A^3,
\&#93;
but its full marked-root preimage \(X_{\xi,\eta}\) is never \(\A^3\).
\end{theorem}

\begin{proof}
The linear forms \(A_2,E_\xi,E_\eta\) are independent.  Indeed, a binary
cubic tangent to, but not osculating, the rational normal curve cannot be a
sum of two cubes.  Thus the target equation solves for \(A_2\).

The stabilizer of \(A_2\) has four types of unordered distinct pairs:
\&#91;
\{0,\infty\},\quad\{0,1\},\quad\{\infty,1\},\quad
\{1,\lambda\},\ \lambda\notin\{0,1\}.
\&#93;
Exact Euler integration in adapted determinant-one frames gives
\&#91;
\cchi(X_{0,\infty})=0,
\&#93;
\&#91;
\cchi(X_{0,1})=
\begin{cases}
-2,&amp;\kappa c=1/2,\\
-3,&amp;\kappa c=0\text{ or }64/3,\\
-4,&amp;\text{otherwise},
\end{cases}
\&#93;
and
\&#91;
\cchi(X_{\infty,1})=
\begin{cases}
0,&amp;\kappa c=-1/3,\\
-1,&amp;\text{otherwise}.
\end{cases}
\&#93;
For the open pair, the final branch curve has the form
\&#91;
lP_{\lambda,\kappa c}(x)=\kappa xQ_\lambda(x),
\&#93;
with both \(P\) and \(Q\) nonzero, and
\&#91;
\cchi(X_{1,\lambda})
=-\#\bigl(Z(PQ)\cap\C^*\bigr)\le0.
\&#93;
None of these values is \(1\).
\end{proof}

\begin{remark}&#91;Representation-theoretic correction&#93;
The raw product \(E_\xi E_\eta\) generally has components in both
irreducible summands.  For example,
\&#91;
10A_0A_3=(A_0A_3+A_1A_2)+(9A_0A_3-A_1A_2).
\&#93;
Thus \cref{thm:two-evaluation-exclusion} is a natural quadratic-layer
classification, not a classification of the pure Cartan secant variety.
\end{remark}

\subsection{The pure Cartan boundary}

\begin{proposition}&#91;Catalecticant target obstruction&#93;
\label{prop:catalecticant-target}
The pure Cartan element
\&#91;
C_{3,3}=A_0A_3+A_1A_2
\&#93;
gives a nondegenerate affine quadric, not \(\A^3\).  More generally, a pure
Cartan quadratic whose middle catalecticant is nonsingular is excluded at
the target level.
\end{proposition}

\begin{proof}
After replacing \(A_1\) by \(A_1+1/\kappa\), the equation
\&#91;
A_2+\kappa C_{3,3}=c
\&#93;
becomes
\&#91;
\kappa(A_0A_3+A_1A_2)=c.
\&#93;
For \(c\ne0\) this is a smooth affine quadric threefold, of compactly
supported Euler characteristic zero; for \(c=0\) it is singular.  The same
argument applies whenever the associated quadratic form, equivalently the
middle catalecticant, is nonsingular.
\end{proof}

\begin{proposition}&#91;First rank-two Cartan endpoint&#93;
\label{prop:rank-two-cartan-endpoint}
For \(\rho\kappa\ne0\), the full incidence over
\&#91;
A_2+\kappa(A_0^2+\rho A_3^2)=c
\&#93;
is not \(\A^3\).
\end{proposition}

\begin{proof}
On the chart \(a\ne0\), put
\&#91;
s=b/a,\qquad z=aq,\qquad U=z^2+a^4t.
\&#93;
The equation is quadratic in \(a\):
\&#91;
-ca^2+B(s,z,U)a+\kappa R(s,z,U)=0,
\&#93;
where
\&#91;
B=1-4sz+3s^2U,\qquad
R=U^2+\rho s^2(1-2sz+s^2U)^2.
\&#93;
For \(c\ne0\), the discriminant fibers degenerate at the nonempty zero set
of
\&#91;
\rho s^6+4c\kappa\rho s^2+4.
\&#93;
If \(n_H\) is the number of its distinct roots, inclusion--exclusion gives
\&#91;
\cchi(X)=-1-n_H\le-2.
\&#93;
For \(c=0\), the equation is linear in \(a\) and the corresponding
calculation gives \(\cchi(X)=-6\).
\end{proof}

\begin{question}&#91;Remaining Cartan strata&#93;
\label{q:remaining-cartan-strata}
Classify the remaining rank-two Cartan secant orbits and the rank-three
catalecticant stratum.  The calculations above settle the full
moving-linear layer and the principal low-rank quadratic strata, but do not
classify arbitrary nonlinear hypersurfaces in the coefficient space.
\end{question}
</code></pre>

<a id="source-340482aba615ef8a"></a>

## `manuscripts/01-cubic-incidence/code/verify_ade_matrix_factorizations.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact symbolic replay for the transverse ADE templates in the Lane 1 repair.

Checks:
  * A_(3r-1) order-three matrix factorizations and ideal presentations;
  * the A_(r-1) degree-three cyclic-cover invariant equations;
  * the two E6 order-three ideals and their matrix factorizations;
  * the explicit D4 -&gt; E6 cyclic-cover invariant equation.
"""

from __future__ import annotations

import argparse
import sys

import sympy as sp


def zero_matrix(matrix: sp.Matrix) -&gt; bool:
    return matrix.applyfunc(sp.expand) == sp.zeros(*matrix.shape)


def verify_a_type(r: int) -&gt; None:
    if r &lt; 1:
        raise ValueError("r must be positive")

    u, v, z, U, V = sp.symbols("u v z U V")
    n = 3 * r
    f = u * v - z**n

    for j in (r, 2 * r):
        phi = sp.Matrix(&#91;&#91;v, -(z**j)&#93;, &#91;-(z ** (n - j)), u&#93;&#93;)
        psi = sp.Matrix(&#91;&#91;u, z**j&#93;, &#91;z ** (n - j), v&#93;&#93;)
        if not zero_matrix(phi * psi - f * sp.eye(2)):
            raise AssertionError(f"A-type left factorization failed: r={r}, j={j}")
        if not zero_matrix(psi * phi - f * sp.eye(2)):
            raise AssertionError(f"A-type right factorization failed: r={r}, j={j}")

        generators = sp.Matrix(&#91;&#91;u, z**j&#93;&#93;)
        if (generators * phi).applyfunc(sp.expand) != sp.Matrix(&#91;&#91;f, 0&#93;&#93;):
            raise AssertionError(f"A-type ideal presentation failed: r={r}, j={j}")

    cover_relation = U * V - z**r
    invariant_relation = U**3 * V**3 - z ** (3 * r)
    quotient = (U * V) ** 2 + U * V * z**r + z ** (2 * r)
    if sp.expand(invariant_relation - cover_relation * quotient) != 0:
        raise AssertionError(f"A-type cyclic cover identity failed: r={r}")

    print(
        f"PASS A_(3r-1), r={r}: both order-three classes and "
        f"A_(r-1) cyclic cover"
    )


def verify_e6() -&gt; None:
    x, y, z, s, t = sp.symbols("x y z s t")
    ii = sp.I
    f = x**2 + y**3 + z**4
    a = x + ii * z**2
    b = x - ii * z**2

    for name, left, right in (("J+", a, b), ("J-", b, a)):
        phi = sp.Matrix(&#91;&#91;right, -y&#93;, &#91;y**2, left&#93;&#93;)
        psi = sp.Matrix(&#91;&#91;left, y&#93;, &#91;-y**2, right&#93;&#93;)
        if not zero_matrix(phi * psi - f * sp.eye(2)):
            raise AssertionError(f"E6 left factorization failed for {name}")
        if not zero_matrix(psi * phi - f * sp.eye(2)):
            raise AssertionError(f"E6 right factorization failed for {name}")
        generators = sp.Matrix(&#91;&#91;left, y&#93;&#93;)
        if (generators * phi).applyfunc(sp.expand) != sp.Matrix(&#91;&#91;f, 0&#93;&#93;):
            raise AssertionError(f"E6 ideal presentation failed for {name}")

    cover = s**3 + t**3 - 2 * ii * z**2
    x_inv = (s**3 - t**3) / 2
    y_inv = s * t
    pullback = sp.expand(x_inv**2 + y_inv**3 + z**4)
    conjugate = s**3 + t**3 + 2 * ii * z**2
    if sp.expand(4 * pullback - cover * conjugate) != 0:
        raise AssertionError("D4 -&gt; E6 invariant identity failed")

    print("PASS E6: both order-three ideals, matrix factorizations, and D4 cyclic cover")


def main(argv: list&#91;str&#93;) -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=12)
    args = parser.parse_args(argv)
    if args.max_r &lt; 1:
        parser.error("--max-r must be positive")

    for r in range(1, args.max_r + 1):
        verify_a_type(r)
    verify_e6()
    print("ALL LANE-1 TRANSVERSE ADE CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv&#91;1:&#93;))
</code></pre>

<a id="source-6f60cc42cc5e64fc"></a>

## `research-notes/finite-diagnostics-20260803-v1/verify_lane1_marked_root_benchmark.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact bounded benchmark for the normalized marked-root cubic example.

This checks the polynomial map with ``A(c)=c`` and ``B(c)=-2``, the marked
root and Jacobian identities, the discriminant and its pullback, and the
normalization/conductor identities on the repeated-root divisor.  It does
not construct the integral quadratic-resolvent algebra or its eigensheaf.
"""

from __future__ import annotations

import hashlib
import json

import sympy as sp


def main() -&gt; int:
    x, y, z, root = sp.symbols("x y z root")

    # The canonical pole-cancelling representative for A(c)=c, B(c)=-2.
    w = 2 * x - 3 * x**2 * y
    c = sp.expand(w - x**3 * z)
    t = y + 1 / x
    r = 2 / x
    b = sp.factor(sp.cancel(r - 3 * c * t**2 + 4 * t))
    a = sp.factor(sp.cancel(t / x - c * t**3 + t**2))

    for coordinate in (a, b, c):
        if not sp.denom(coordinate) == 1:
            raise AssertionError("pole cancellation did not produce a polynomial")

    expected_a = (
        x**3 * y**3 * z
        + 3 * x**2 * y**4
        + 3 * x**2 * y**2 * z
        + 7 * x * y**3
        + 3 * x * y * z
        + 4 * y**2
        + z
    )
    expected_b = (
        3 * x**3 * y**2 * z
        + 9 * x**2 * y**3
        + 6 * x**2 * y * z
        + 12 * x * y**2
        + 3 * x * z
        + y
    )
    expected_c = -x**3 * z - 3 * x**2 * y + 2 * x
    if any(
        sp.expand(left - right) != 0
        for left, right in zip((a, b, c), (expected_a, expected_b, expected_c))
    ):
        raise AssertionError("explicit normalized map changed")

    jacobian = sp.factor(sp.Matrix(&#91;a, b, c&#93;).jacobian(&#91;x, y, z&#93;).det())
    if jacobian != -2:
        raise AssertionError(f"Jacobian changed: {jacobian}")

    inverse_cubic = c * root**3 - 2 * root**2 + b * root - 2 * a
    if sp.factor(sp.cancel(inverse_cubic.subs(root, t))) != 0:
        raise AssertionError("marked-root identity failed")
    if sp.factor(sp.cancel(sp.diff(inverse_cubic, root).subs(root, t) - r)) != 0:
        raise AssertionError("marked-slope identity failed")

    discriminant = sp.factor(sp.discriminant(inverse_cubic, root))
    expected_discriminant = sp.expand(
        4 * b**2 - 4 * c * b**3 - 64 * a + 72 * a * c * b - 108 * a**2 * c**2
    )
    if sp.expand(discriminant - expected_discriminant) != 0:
        raise AssertionError("cubic discriminant formula failed")
    residual = sp.expand((3 * c * t - 2) ** 2 - 4 * c * r)
    if sp.factor(sp.cancel(discriminant - r**2 * residual)) != 0:
        raise AssertionError("marked Vandermonde factorization failed")

    # Parametrize the repeated-root divisor by setting r=0.
    s = sp.symbols("s")
    branch_b = -3 * c * s**2 + 4 * s
    branch_a = -c * s**3 + s**2
    h = 3 * c * s - 2
    conductor_generator_1 = sp.expand(4 - 3 * c * branch_b)
    conductor_generator_2 = sp.expand(18 * c * branch_a - 2 * branch_b)
    if sp.expand(conductor_generator_1 - h**2) != 0:
        raise AssertionError("first discriminant-conductor identity failed")
    if sp.expand(conductor_generator_2 + 2 * s * h**2) != 0:
        raise AssertionError("second discriminant-conductor identity failed")

    result = {
        "schema_version": 1,
        "name": "Lane 1 normalized marked-root benchmark",
        "status": "pass",
        "frame": {"A(c)": "c", "B(c)": "-2", "alpha": "0"},
        "map": {"a": str(sp.expand(a)), "b": str(sp.expand(b)), "c": str(c)},
        "coordinate_degrees": {
            name: sp.Poly(value, x, y, z).total_degree()
            for name, value in (("a", a), ("b", b), ("c", c))
        },
        "jacobian": str(jacobian),
        "inverse_cubic": "c*T^3-2*T^2+b*T-2*a",
        "generic_quadratic_resolvent": "K(sqrt(Delta))/K",
        "discriminant": "4*b^2-4*c*b^3-64*a+72*a*c*b-108*a^2*c^2",
        "marked_pullback": "Delta=r^2*((3*c*t-2)^2-4*c*r)",
        "finite_completion": {
            "equation": "c*T^3-2*S*T^2+b*S^2*T-2*a*S^3=0",
            "flat_rank": 3,
            "smoothness_check": (
                "d/da=-2*S^3; on S=0 the derivative d/dS=-2*T^2 is a unit"
            ),
            "ext_defect": "zero because the displayed completion is finite flat",
        },
        "different": (
            "On the finite marked-root chart the monogenic different is generated "
            "by P'(t)=r; globally the ramification Cartier divisor is r=0."
        ),
        "discriminant_conductor": {
            "normalization_parameter": "(c,s)",
            "H": "3*c*s-2",
            "target_generators": &#91;"4-3*c*b", "18*c*a-2*b"&#93;,
            "pullbacks": &#91;"H^2", "-2*s*H^2"&#93;,
            "normalization_conductor": "(H^2)",
        },
        "does_not_establish": &#91;
            "an integral presentation or normalization of the quadratic resolvent",
            "the rank-one cubic eigensheaf on that resolvent",
            "a flatness theorem for an arbitrary degree-three Keller normalization",
            "recovery of the affine opening from the finite completion",
        &#93;,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-9f90a471b9d6c6af"></a>

## `research-notes/lane1-collision-saturation-20260802-v1/INTEGRATION-v8.md`

<pre><code class="language-markdown">
# Lane 1 collision-saturation packet: integration notes

This is an AI-assisted source-level research packet. It is not a regenerated
public release and has not undergone independent specialist review.

## Main new theorem

Let `T` be the `S_3`-Galois normalization of a generic-degree-three Keller
extension at an omitted value `y`. The attained part of `Spec(T)` is covered
by the three conjugate source charts `U_1,U_2,U_3`. Their pair and triple
intersections are explicit affine collision spaces.

For a divided-difference matrix

```text
F(X)-F(X') = M(X,X')(X-X')
```

put `q=det(M)` and `c=det(JF)`. In `S tensor_R S`,

```text
q(q-c)=0,
e_Delta=q/c,
e_Delta^2=e_Delta.
```

Thus `e_Delta` cuts out the diagonal and `1-e_Delta` cuts out the smooth
off-diagonal collision component. Pairwise-distinct triples are selected by

```text
e_dist=(1-e_12)(1-e_13)(1-e_23).
```

Form the three-chart affine Cech complex and write

```text
K_y = ker(d_1),
I_y = im(d_0),
I_y^sat = I_y :_(K_y) m_y^infinity.
```

Then

```text
I_y^sat/I_y = MatlisDual(Delta_y) tensor V_std
```

as an `A&#91;S_3&#93;`-module. Consequently

```text
B_y is flat  &lt;=&gt;  I_y^sat=I_y,
length(I_y^sat/I_y)=2 length(Delta_y).
```

A minimal defect is exactly one copy of the two-dimensional standard
representation, killed by the closed-point ideal.

## Product and standard-root consequences

If the complete Galois opening and all three source charts are formally
constant along a carrier parameter, the product vector field acts on the Cech
complex and eliminates every punctual submodule. Hence the normalization is
flat.

For the standard ordered-root triple collision, with

```text
u=r_1-r_2,
v=r_2-r_3,
```

the chart-complement ideal is

```text
(u(u+v),uv,v(u+v))=(u,v)^2.
```

Its collision cohomology is transverse local cohomology tensored with the
smooth-axis ring, so the saturation quotient vanishes. Therefore a defect
requires a genuinely non-product deformation of the complete source-chart
gluing, not merely the universal triple-root arrangement.

## Exact checks

- `verify_collision_idempotent.py` constructs the divided-difference matrix
  for the announced cubic map and verifies the fibre-ideal certificate for
  `q(q-c)` exactly over `Q`.
- `verify_standard_collision_model.py` verifies the ordered-root ideal
  identity exactly.
- Existing exact scripts continue to check the equivariant weights,
  transverse ADE matrix factorizations, and the minimal nine-cusp formulas.

## Suggested repository placement

- replace
  `data/model-handoffs-v14-20260801a/cubic-flatness-normalization-defects.md`;
- add
  `data/manuscript-sources-v1-20260801b/sources/01-cubic-incidence/appendices/flatness-defect-repairs.tex`;
- add `\input{appendices/flatness-defect-repairs}` after the current cubic
  resolvent appendix in Program 1 `main.tex`;
- place the exact scripts in a scoped Lane 1 research-tools directory;
- retain `lane1-collision-saturation-v8.pdf` only as an optional reading copy.

## Required regeneration

The selected site release is hash-pinned. After accepting the mathematics,
regenerate the manuscript-source manifest and proof pages, the Program 1
entrypoint, the handoff manifest, generated docs, release metadata, and
`site-state.json`. Then rerun source, privacy, strict MkDocs, PDF, browser,
and deployed-site checks.

## Scope

The packet gives an exact necessary-and-sufficient collision-saturation
criterion and proves it for product/equisingular collision families and the
standard triple-root model. It does not prove saturation for every
non-equivariant Keller boundary. The unresolved calculation is now the
closed-point standard-isotypic saturation of the actual pair/triple collision
rings.
</code></pre>

<a id="source-f5239a257b61f4d8"></a>

## `research-notes/lane1-collision-saturation-20260802-v1/cubic-flatness-normalization-defects.md`

<pre><code class="language-markdown">
# Lane 1: cubic flatness and finite normalization defects

**Portfolio role:** settle the intrinsic finite-cover problem for generic-degree-three Keller maps before attempting boundary reconstruction.

## Research objective

Let

```text
F : X = A^3_C -&gt; Y = A^3_C
```

be a Keller map of generic degree three. Let `B` be the normalization of
`R=O(Y)` in `C(X)`, and write

```text
pi : Xbar = Spec(B) -&gt; Y.
```

Lane 1 asks whether `pi` is finite flat. This is a general degree-three Keller
question, not a statement restricted to the named counterexample or the
explicit normalized `A,B` family.

The affine opening is a separate gate. Even after flatness, recovering the
original `A^3` inside `Xbar` requires boundary completeness. Do not merge Lane
1 with the boundary/Torelli lane.

## Reusable mathematics

Write

```text
R = C&#91;y1,y2,y3&#93;,   S = C&#91;x1,x2,x3&#93;,
B = R ⊕ E,         E = ker Tr_(B/R).
```

The following statements are the repaired reusable core.

### 1. The defect is a canonical finite Ext module

Define

```text
Delta_F := Ext^1_R(B,R) = Ext^1_R(E,R).
```

The modules `B` and the rank-two trace-zero module `E` are reflexive. Hence
`E` is free at every prime of height at most two, `Delta_F` has finite length,
and

```text
Supp(Delta_F) = { y in Y : B_y is not free over R_y }.
B is finite flat over R  &lt;=&gt;  Delta_F = 0.
```

At a possible defect point `y`, with `A=R_y`, a minimal presentation is

```text
0 -&gt; A^b --Phi--&gt; A^(b+2) -&gt; E_y -&gt; 0,
Delta_(F,y) = coker(Phi^dual).
```

The integer `b` is the minimal number of generators of `Delta_(F,y)`. Local
duality identifies its Matlis dual with `H^2_m(E_y)`.

An orientation of `E_y` extends this presentation to an alternating self-dual
free resolution

```text
0 -&gt; A^b -&gt; A^(b+2) -&gt; A^(b+2)^dual -&gt; A^b^dual
  -&gt; Delta_(F,y) -&gt; 0.
```

Thus `Delta_(F,y)` is Matlis self-dual and its socle dimension is also `b`.
Any proposed defect must satisfy this finite certificate.

The first stratum is explicit. If `b=1`, then

```text
Delta_(F,y) = A/(f1,f2,f3),
E_y = Omega_A^2(Delta_(F,y)),
```

for an `A`-regular sequence, and the resolution is Koszul with Betti numbers
`(1,3,3,1)`.

### 2. Source splitting is proved and its direct scope is exhausted

Base change to the affine source has a canonical marked factor:

```text
B tensor_R S = S × C,
C = S&#91;eta&#93;/(eta^2-D).
```

The factor `S` is canonical. The trace-zero generator `eta` is a choice, and
`D` changes by a unit square when the generator changes.

Consequently `B_y` is free for every attained value `y in F(X)`. Together with
the omitted-values theorem,

```text
Supp(Delta_F) ⊆ O_F ⊆ Sing(S_F),
```

where `O_F` is the omitted set and `S_F` is the reduced nonproperness set.
There is no source point above a defect value, so “apply source splitting
again” is not a local strategy. Any further source input must pass through the
boundary, conductor, duality, or monodromy.

### 3. The quadratic resolvent carries exactly the same defect

Let `T` be the normalization in the `S_3` Galois closure, let `N=A_3`, and let
`H` be the transposition subgroup corresponding to the cubic field. Then

```text
B = T^H,
Q = T^N = R&#91;w&#93;/(w^2-d),
T = Q ⊕ L ⊕ L^&#91;2&#93;,
L^&#91;3&#93; = Q.
```

The corrected divisorial list `U0/U1/U2/B` implies that `T/Q` is unramified in
codimension one. Taking `H`-invariants gives an exact `R`-module
identification

```text
E ≅ L,       ell |-&gt; ell + sigma(ell).
```

Therefore

```text
Delta_F = Ext^1_R(L,R),
B flat over R  &lt;=&gt;  L locally free over R  &lt;=&gt;  L MCM over Q.
```

This is an equivalence, not merely the former one-way MCM criterion.

### 4. A completed defect branch is genuinely non-Galois cubic

At `y in Supp(Delta_F)`, completion over `A=R_y^` decomposes the normalization
into normal local factors of total rank three. Rank-one factors equal `A`.
Rank-two normal factors are free because their trace-zero summands are
rank-one reflexive modules over the regular local UFD `A`. A cyclic rank-three
factor is also free by its `C_3` character decomposition.

Hence a defect has one rank-three normal local factor, and that cubic field is
non-Galois with `S_3` closure. The normalization fibre is supported at one
point and has scheme length

```text
length(B tensor_R k(y)) = b + 3 &gt;= 4.
```

Length four is exactly the one-generator complete-intersection stratum.

### 5. Dao detection localizes every remaining class on singular curves

For a three-dimensional normal local hypersurface `Q0`, Dao’s punctured-Picard
theorem gives

```text
Cl(Q0)&#91;3&#93; -&gt; direct_sum_{height-two singular p} Cl((Q0)_p)&#91;3&#93;
```

injectively. Thus a nonzero defect requires a height-two singular prime of the
quadratic resolvent carrying a nonzero localization of `&#91;L&#93;`. For

```text
Q = R&#91;w&#93;/(w^2-d),
```

the singular locus is cut out by

```text
(w, d_y1, d_y2, d_y3).
```

An isolated resolvent singularity cannot carry the defect.

## New finite transverse filter

Assume, only for this subsection, that the generic transverse surface type at
each singular curve is a split rational double point. Three-torsion occurs
only for

```text
A_(3r-1)  and  E6.
```

Each curve contributes at most one coordinate in `F_3`.

For `A_(3r-1)` with equation `uv-z^(3r)`, the two nonzero classes are

```text
I_r=(u,z^r),   I_2r=(u,z^(2r)).
```

They have explicit two-by-two matrix factorizations. Their degree-three cyclic
cover has equation `UV-z^r`, so the transverse cover type is `A_(r-1)`.

For `E6` with equation `x^2+y^3+z^4`, put

```text
a=x+i z^2,   b=x-i z^2,
J+=(a,y),    J-=(b,y).
```

These are the two nonzero classes in `Z/3` and have explicit two-by-two matrix
factorizations. The associated cyclic cover is

```text
s^3+t^3-2 i z^2 = 0,
```

which is a `D4` singularity, with invariant coordinates

```text
x=(s^3-t^3)/2,   y=s*t,   z=z.
```

Thus every coordinate in the conditional ADE vector has an explicit generic
transverse MCM representative. The unresolved step is extending and gluing
those factorizations through the closed threefold point.

## Useful deliverable

### Exact live problem

The remaining unknown at a candidate omitted value is the following finite
package:

1. the square class `d` defining the normal quadratic resolvent;
2. every height-two prime in its singular locus;
3. a fractional-ideal or finite-presentation representative of `L`;
4. the local class vector `(&#91;L_p&#93;)_p`;
5. a matrix factorization or other depth-three certificate extending the
   explicit transverse models through the closed point, or a Keller-specific
   argument excluding every nonzero vector.

A useful returned result must state whether it is local, completed, formal,
divisorial, or global, and identify the exact boundary or conductor data it
uses.

## Recommended work order

### P1-T1A — Extract the exact resolvent carrier

**Status:** ready.

**Input:** the actual Keller normalization and boundary, not a schematic
elliptic picture.

**Done when:** `d`, the singular height-two primes, a presentation of `L`, the
conductor/different, and the local class vector are explicit and checkable.

### P1-T1B — Extend the transverse MCM models

**Status:** blocked on P1-T1A.

**Attack:** build a matrix factorization over the three-dimensional resolvent
whose generic restrictions are the displayed `A_(3r-1)` or `E6` templates;
alternatively prove a Keller-specific vanishing of the class vector.

**Done when:** the resulting module has depth three and its codimension-two
classes agree with `L` at every singular curve.

### P1-T2 — Compute the finite class/intersection obstruction

**Status:** blocked on P1-T1A.

Do not invent the lattice. Its intersection matrix, discrepancy vector, and
class coordinates must be derived from the actual resolvent model and then
hash-pinned for exact replay.

### P1-T3 — Keep boundary completeness separate

Finite flatness gives a binary-cubic/marked-root finite cover. Identifying the
original affine source inside it still requires a separate theorem specifying
all deleted ramified and unramified sheets.

## Do not do

- Do not state that normal `S_3` cubic covers are automatically flat.
- Do not replace `Delta_F` by an unnamed defect or treat reflexivity as local freeness.
- Do not use the old `U1/U2/B` list; the complete list is `U0/U1/U2/B`.
- Do not call the quadratic generator in source splitting canonical.
- Do not infer a global MCM module from a smooth cubic-axis picture without a
  matrix factorization and codimension-two comparison.
- Do not run an exceptional-lattice computation before the actual primes and
  eigensheaf class are known.
- Do not infer boundary completeness from flatness.

## Proof access

The accompanying repair appendix supplies the conventional proofs. Existing
Program 1 text sources remain necessary for the corrected divisorial
classification and omitted-values theorem. Optional PDFs may predate this
repair.

&#91;Back to the portfolio hub&#93;(state-of-the-program.md)
</code></pre>

<a id="source-31b28e4d427212ea"></a>

## `research-notes/lane1-collision-saturation-20260802-v1/flatness-defect-repairs.tex`

<pre><code class="language-tex">
\section{The finite cubic flatness defect: exact repairs}
\label{app:flatness-defect-repairs}

This appendix replaces the former statement-only flatness package by a
canonical finite defect, proves the attained-value splitting, identifies the
defect exactly on the quadratic resolvent, and records the remaining local
input.  It does not prove that the defect vanishes.

Let
\&#91;
R=\C&#91;y_1,y_2,y_3&#93;,\qquad S=\C&#91;x_1,x_2,x_3&#93;,
\&#93;
and let
\&#91;
F\colon X=\Spec S\longrightarrow Y=\Spec R
\&#93;
be a Keller map of generic degree three.  Put \(K=\Frac S\), let \(B\) be the
integral closure of \(R\) in \(K\), and write
\&#91;
\pi\colon\overline X=\Spec B\longrightarrow Y.
\&#93;
The field trace splits the unit inclusion:
\&#91;
B=R\oplus E,\qquad E=\ker(\operatorname{Tr}_{B/R}),
\&#93;
where \(E\) has rank two.  Write \(O_F=Y\setminus F(X)\) and let \(S_F\)
denote the reduced nonproperness set.

\subsection{The canonical finite defect}

\begin{proposition}&#91;Canonical Ext defect&#93;
\label{prop:cubic-ext-defect}
The \(R\)-modules \(B\) and \(E\) are reflexive.  Define
\&#91;
\Delta_F:=\operatorname{Ext}^1_R(B,R)
          \simeq\operatorname{Ext}^1_R(E,R).
\&#93;
Then \(\Delta_F\) has finite length and
\&#91;
\operatorname{Supp}\Delta_F
 =\{y\in Y:B_y\text{ is not free over }R_y\}.
\&#93;
Consequently
\&#91;
B\text{ is finite flat over }R
\quad\Longleftrightarrow\quad
\Delta_F=0.
\&#93;
More precisely, at a closed point \(y\), with \(A=R_y\), there is a minimal
free resolution
\&#91;
0\longrightarrow A^b\xrightarrow{\Phi}A^{b+2}
 \longrightarrow E_y\longrightarrow0,
\&#93;
and
\&#91;
(\Delta_F)_y\simeq\operatorname{coker}(\Phi^\vee),
\qquad
\dim_\C (\Delta_F)_y/\mathfrak m_y(\Delta_F)_y=b.
\&#93;
Local duality gives
\&#91;
\operatorname{Hom}_A((\Delta_F)_y,E_A(\C))
 \simeq H^2_{\mathfrak m_y}(E_y).
\&#93;
\end{proposition}

\begin{proof}
The integral closure of a noetherian normal domain in a finite field extension
is a finite reflexive module over the base; equivalently, it is recovered from
its codimension-one localizations inside the field extension.  Hence \(B\) is
reflexive, and the trace splitting makes \(E\) a reflexive direct summand.

If \(\mathfrak p\subset R\) has height at most two, reflexivity gives
\&#91;
\operatorname{depth}_{R_\mathfrak p}E_\mathfrak p
 =\dim R_\mathfrak p.
\&#93;
Auslander--Buchsbaum over the regular local ring \(R_\mathfrak p\) makes
\(E_\mathfrak p\) free.  Thus the nonfree locus is a finite set of closed
points.  At a closed point, reflexivity gives depth at least two, so
\(\operatorname{pd}_A E_y\le1\) and the displayed resolution exists.
Dualizing it gives
\&#91;
(\Delta_F)_y=\operatorname{coker}(\Phi^\vee).
\&#93;
If \(b=0\), then \(E_y\) is free.  If \(b&gt;0\), minimality puts every entry of
\(\Phi\) in \(\mathfrak m_y\), so the cokernel of \(\Phi^\vee\) has exactly
\(b\) minimal generators and is nonzero.  This proves the support and
flatness assertions.  The final identity is local duality in dimension three.
\end{proof}

\begin{proposition}&#91;Alternating self-dual defect resolution&#93;
\label{prop:cubic-defect-self-duality}
At a closed point \(y\), choose an orientation \(\det(E_y)\simeq A\).  The
minimal presentation in \cref{prop:cubic-ext-defect} extends to an exact
complex
\&#91;
0\longrightarrow A^b\xrightarrow{\Phi}A^{b+2}
 \xrightarrow{\Psi}(A^{b+2})^\vee
 \xrightarrow{\Phi^\vee}(A^b)^\vee
 \longrightarrow(\Delta_F)_y\longrightarrow0,
\&#93;
where \(\Psi^\vee=-\Psi\).  Consequently
\&#91;
(\Delta_F)_y\simeq
\operatorname{Ext}^3_A((\Delta_F)_y,A),
\&#93;
so \((\Delta_F)_y\) is Matlis self-dual and
\&#91;
\dim_\C\operatorname{Soc}((\Delta_F)_y)
 =\dim_\C (\Delta_F)_y/\mathfrak m_y(\Delta_F)_y=b.
\&#93;
\end{proposition}

\begin{proof}
The orientation gives the alternating reflexive isomorphism
\&#91;
\theta\colon E_y\xrightarrow{\sim}E_y^\vee,
\qquad \theta^\vee=-\theta.
\&#93;
Let \(\rho\colon A^{b+2}\twoheadrightarrow E_y\) be the presentation map and
put
\&#91;
\Psi=\rho^\vee\theta\rho.
\&#93;
Since \(\rho^\vee\) and \(\theta\) are injective isomorphisms onto their
images,
\&#91;
\ker\Psi=\ker\rho=\operatorname{im}\Phi.
\&#93;
The dual presentation gives
\&#91;
\operatorname{im}\Psi=\rho^\vee(E_y^\vee)=\ker\Phi^\vee,
\&#93;
and the final cokernel is \((\Delta_F)_y\).  Dualizing the resulting free
resolution reproduces it, up to the sign of \(\Psi\), and identifies the third
Ext module with the same final cokernel.  For a finite-length module over a
three-dimensional regular local ring, the third Ext is its Matlis dual.
\end{proof}

\begin{corollary}&#91;The one-generator stratum&#93;
\label{cor:cubic-one-generator-defect}
If \(b=1\), then there is an \(A\)-regular sequence \(f_1,f_2,f_3\) such that
\&#91;
(\Delta_F)_y\simeq A/(f_1,f_2,f_3),
\qquad
E_y\simeq\Omega_A^2(A/(f_1,f_2,f_3)).
\&#93;
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

\begin{proposition}&#91;Source splitting&#93;
\label{prop:cubic-source-splitting}
There is an \(S\)-algebra decomposition
\&#91;
B\otimes_RS\simeq S\times C,
\&#93;
where \(C\) is a normal quadratic \(S\)-algebra.  After choosing a generator
of its trace-zero summand,
\&#91;
C\simeq S&#91;\eta&#93;/(\eta^2-D)
\&#93;
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
\&#91;
p\colon\overline X\times_YX\longrightarrow X.
\&#93;
The map \(p\) is etale along the section.  Restricting to the etale locus, a
section of an unramified separated morphism is open and closed.  The section
is also closed in the whole fibre product because \(p\) is finite.  It is
therefore an open-and-closed component, giving
\&#91;
B\otimes_RS\simeq S\times C.
\&#93;

Normalization commutes with smooth base change, so \(C\) is normal.  Its
trace splits it as \(S\oplus L_0\), where \(L_0\) is rank-one reflexive.
Since \(S\) is factorial, \(L_0\) is free.  A trace-zero generator \(\eta\)
satisfies \(\eta^2=D\in S\) by Cayley--Hamilton.

If \(F(x)=y\), then the local etale homomorphism \(R_y\to S_x\) is faithfully
flat, while \(B_y\otimes_{R_y}S_x\) is free by the displayed decomposition.
Faithfully flat descent makes \(B_y\) flat, hence free, over \(R_y\).
\end{proof}

\begin{corollary}&#91;Defect support&#93;
\label{cor:cubic-defect-support}
For every generic-degree-three Keller map,
\&#91;
\operatorname{Supp}\Delta_F\subseteq O_F\subseteq\operatorname{Sing}(S_F).
\&#93;
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
\&#91;
B=T^H,\qquad Q=T^N.
\&#93;
Fix a primitive cube root \(\zeta\in\C\).

\begin{theorem}&#91;Exact resolvent carrier&#93;
\label{thm:exact-resolvent-carrier}
The quadratic resolvent \(Q\) is normal and finite flat of rank two over
\(R\); after a trace-zero choice,
\&#91;
Q\simeq R&#91;w&#93;/(w^2-d)
\&#93;
for some \(d\in R\).  The cover \(T/Q\) is unramified in codimension one and
has character decomposition
\&#91;
T\simeq Q\oplus L\oplus L^{&#91;2&#93;},
\qquad L^{&#91;3&#93;}\simeq Q.
\&#93;
If \(\sigma\) denotes the nontrivial involution of \(Q/R\), then
\&#91;
\sigma^*L\simeq L^{&#91;2&#93;}\simeq L^\vee;
\&#93;
in particular, every local three-torsion class carried by \(L\) is
anti-invariant under the quadratic involution.  As an \(R\)-module, the
cubic trace-zero summand is exactly the eigensheaf:
\&#91;
E\simeq L.
\&#93;
Consequently
\&#91;
\Delta_F\simeq\operatorname{Ext}^1_R(L,R),
\&#93;
and the following are equivalent:
\&#91;
\begin{aligned}
B\text{ is finite flat over }R
&amp;\Longleftrightarrow L\text{ is locally free over }R,\\
&amp;\Longleftrightarrow L\text{ is MCM over }Q.
\end{aligned}
\&#93;
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
\(\sigma^*L\simeq L^{&#91;2&#93;}\simeq L^\vee\).  Taking \(H\)-invariants gives
\&#91;
B=T^H=R\oplus\{\ell+\sigma(\ell):\ell\in L\}.
\&#93;
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

\begin{corollary}&#91;Formal defect branches&#93;
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

\begin{corollary}&#91;Defective fibre length&#93;
\label{cor:cubic-defect-fibre-length}
Let \(y\in\operatorname{Supp}\Delta_F\), and let \(b\) be the presentation
number in \cref{prop:cubic-ext-defect}.  Then \(\pi^{-1}(y)\) is supported at
one point and
\&#91;
\operatorname{length}_\C(B\otimes_R\kappa(y))=b+3\ge4.
\&#93;
The length is four exactly in the one-generator stratum.
\end{corollary}

\begin{proof}
The completed algebra has one local factor by
\cref{cor:formal-cubic-defect}, so the finite fibre has one support point.
Minimality of the presentation gives
\&#91;
\dim_\C B_y/\mathfrak m_yB_y
 =1+\dim_\C E_y/\mathfrak m_yE_y
 =1+(b+2)=b+3.
\&#93;
A defect has \(b\ge1\).
\end{proof}

\subsection{Codimension-two detection and explicit transverse covers}

\begin{corollary}&#91;Resolvent defect curves&#93;
\label{cor:resolvent-defect-curves}
If \((\Delta_F)_y\ne0\), then for some \(\mathfrak q\mid y\) there is a
height-two singular prime \(\mathfrak p\subset Q_\mathfrak q\) such that
\&#91;
&#91;L_\mathfrak p&#93;\ne0
\quad\text{in}\quad
\operatorname{Cl}(Q_\mathfrak p)&#91;3&#93;.
\&#93;
For \(Q=R&#91;w&#93;/(w^2-d)\), the singular locus is cut out by
\&#91;
(w,\partial_{y_1}d,\partial_{y_2}d,\partial_{y_3}d).
\&#93;
In particular, a defect requires a singular curve of the quadratic resolvent;
an isolated resolvent singularity cannot carry it.
\end{corollary}

\begin{proof}
Dao's theorem makes the Picard group of the punctured spectrum of a
three-dimensional local hypersurface torsion-free.  It follows that
\&#91;
\operatorname{Cl}(Q_\mathfrak q)&#91;3&#93;\hookrightarrow
\bigoplus_{\substack{\mathfrak p\in\operatorname{Sing}(Q_\mathfrak q)\\
                     \operatorname{ht}\mathfrak p=2}}
\operatorname{Cl}(Q_\mathfrak p)&#91;3&#93;.
\&#93;
By \cref{thm:exact-resolvent-carrier}, nonzero defect means that
\(L_\mathfrak q\) is not MCM.  Its class is therefore nonzero, while
\(L^{&#91;3&#93;}\simeq Q\) makes it three-torsion.  The Jacobian ideal of
\(w^2-d\) gives the displayed singular-locus equations.
\end{proof}

\begin{proposition}&#91;Transverse ADE filter and explicit cyclic covers&#93;
\label{prop:transverse-ADE-filter}
Assume that, after strict henselization and completion, every generic
transverse surface singularity at a height-two singular prime is a split
rational double point.  Then only
\&#91;
A_{3r-1}\quad(r\ge1),\qquad E_6
\&#93;
can carry a nonzero localization of the cubic defect class.  Each component
contributes at most one \(\mathbf F_3\)-coordinate.

For a transverse \(A_{3r-1}\) equation
\&#91;
Q_0=k&#91;&#91;u,v,z&#93;&#93;/(uv-z^{3r}),
\&#93;
the two nonzero order-three classes are represented by
\&#91;
I_r=(u,z^r),\qquad I_{2r}=(u,z^{2r}).
\&#93;
For \(j=r,2r\), the matrices
\&#91;
\Phi_j=\begin{pmatrix}v&amp;-z^j\\-z^{3r-j}&amp;u\end{pmatrix},
\qquad
\Psi_j=\begin{pmatrix}u&amp;z^j\\z^{3r-j}&amp;v\end{pmatrix}
\&#93;
satisfy
\&#91;
\Phi_j\Psi_j=\Psi_j\Phi_j=(uv-z^{3r})I_2.
\&#93;
The associated degree-three quasi-etale cyclic cover has transverse equation
\&#91;
UV-z^r=0,
\&#93;
so its type is \(A_{r-1}\), with \(A_0\) interpreted as smooth.

For a transverse \(E_6\) equation
\&#91;
Q_0=k&#91;&#91;x,y,z&#93;&#93;/(x^2+y^3+z^4),
\&#93;
choose \(i^2=-1\), put
\&#91;
a=x+iz^2,\qquad b=x-iz^2,
\&#93;
and set
\&#91;
J_+=(a,y),\qquad J_-=(b,y).
\&#93;
These are the two nonzero classes in \(\operatorname{Cl}(Q_0)\simeq\mathbf Z/3\).
For \(J_+\), an explicit matrix factorization is
\&#91;
\Phi_+=\begin{pmatrix}b&amp;-y\\y^2&amp;a\end{pmatrix},
\qquad
\Psi_+=\begin{pmatrix}a&amp;y\\-y^2&amp;b\end{pmatrix},
\&#93;
with the factorization for \(J_-\) obtained by interchanging \(a\) and \(b\).
The corresponding degree-three cyclic cover is
\&#91;
k&#91;&#91;s,t,z&#93;&#93;/(s^3+t^3-2iz^2),
\&#93;
a \(D_4\) rational double point.  The deck action is
\((s,t,z)\mapsto(\zeta s,\zeta^{-1}t,z)\), and its invariant coordinates are
\&#91;
x=\frac{s^3-t^3}{2},\qquad y=st,\qquad z=z.
\&#93;

Both cyclic covers carry a transposition lifting the quadratic involution and
conjugating the deck transformation to its inverse.  Their cubic
transposition quotients are explicit.  In the \(A_{3r-1}\) case, put
\&#91;
c=U^3+V^3,\qquad \alpha=U+V.
\&#93;
Then the regular base, quadratic resolvent, and cubic subcover are
\&#91;
R_0=k&#91;&#91;c,z&#93;&#93;,\qquad
Q_0=R_0&#91;w&#93;/(w^2-c^2+4z^{3r}),
\&#93;
\&#91;
B_0=R_0&#91;\alpha&#93;/(\alpha^3-3z^r\alpha-c)
    \simeq k&#91;&#91;\alpha,z&#93;&#93;.
\&#93;
In the \(E_6\) case, with \(\alpha=s+t\), they are
\&#91;
R_0=k&#91;&#91;y,z&#93;&#93;,\qquad
Q_0=R_0&#91;x&#93;/(x^2+y^3+z^4),
\&#93;
\&#91;
B_0=R_0&#91;\alpha&#93;/(\alpha^3-3y\alpha-2iz^2).
\&#93;
The discriminants of the two displayed cubic polynomials are, respectively,
\&#91;
-27(c^2-4z^{3r}),\qquad 108(y^3+z^4),
\&#93;
so the displayed double covers are their quadratic resolvents, up to a unit
square.
\end{proposition}

\begin{proof}
The class groups of the split rational double points are the discriminant
groups of their ADE root lattices:
\&#91;
\operatorname{Cl}(A_n)=\mathbf Z/(n+1),
\&#93;
while the \(D_n,E_6,E_7,E_8\) groups have orders \(4,3,2,1\), respectively.
Thus nonzero three-torsion occurs precisely for \(A_{3r-1}\) and \(E_6\), and
its three-primary subgroup is \(\mathbf Z/3\).

For \(A_{3r-1}\), the ideals \((u,z^j)\) represent class \(j\) in
\(\mathbf Z/(3r)\), and direct multiplication gives the displayed matrix
factorizations.  The cyclic cover is obtained from
\&#91;
u=U^3,\qquad v=V^3,\qquad UV=z^r;
\&#93;
its \(C_3\)-invariants recover \(uv=z^{3r}\).

For \(E_6\), one has \(ab+y^3=x^2+y^3+z^4\).  Let
\(\mathfrak m=(x,y,z)\).  The prime \(P_+=(a,y)\) satisfies
\(Q_0/P_+\simeq k&#91;&#91;z&#93;&#93;\), and at its generic point \(b\) is a unit and
\(a=-y^3/b\).  Hence \(\operatorname{div}(a)=3P_+\).  The images of \(a\)
and \(y\) are linearly independent in \(P_+/\mathfrak mP_+\): their initial
linear terms are \(x\) and \(y\).  Thus \(P_+\) needs two generators and is
not principal, so its class has order three; \(J_-\) is the inverse class.
Direct multiplication gives
\&#91;
\Phi_+\Psi_+=\Psi_+\Phi_+=(x^2+y^3+z^4)I_2,
\&#93;
and the row \((a,y)\) gives
\((a,y)\Phi_+=(x^2+y^3+z^4,0)\).  The induced surjection from the
matrix-factorization cokernel to \(J_+\) is an isomorphism: both modules have
rank one, and the source is torsion-free because it is maximal
Cohen--Macaulay over the normal surface.

In the displayed \(D_4\) cover,
\&#91;
\left(\frac{s^3-t^3}{2}\right)^2+(st)^3+z^4
 =\frac{(s^3+t^3)^2}{4}+z^4=0,
\&#93;
and the invariant monomials are generated by \(s^3,t^3,st,z\).  With
\(p=s+t\) and \(q=s-t\), its equation becomes, after multiplying by a unit
and rescaling variables,
\&#91;
z^2+p^3+pq^2=0,
\&#93;
the standard \(D_4\) equation.

For the full group actions, set
\&#91;
\tau(U,V,z)=(\zeta U,\zeta^{-1}V,z),\qquad
\sigma(U,V,z)=(V,U,z)
\&#93;
in type \(A\), and use the same formulas with \((s,t,z)\) in type \(E_6\).
Then \(\sigma\tau\sigma=\tau^{-1}\).  In type \(A\), the full invariants are
\(k&#91;&#91;c,z&#93;&#93;\), while the \(\sigma\)-invariants are generated by
\(\alpha=U+V\) and \(z\), with
\(c=\alpha^3-3z^r\alpha\).  In type \(E_6\), the full invariants are
\(k&#91;&#91;y,z&#93;&#93;\), while the \(\sigma\)-invariants satisfy
\(\alpha^3-3y\alpha-2iz^2=0\).  The standard depressed-cubic discriminant
formula gives the two stated resolvents.  The involution exchanges
\(I_r\) with \(I_{2r}\), and \(J_+\) with \(J_-\), exactly as required by
\(\sigma^*L\simeq L^\vee\).
\end{proof}

\begin{remark}&#91;Revised Lane 1 task&#93;
\label{rem:revised-cubic-task}
The repair does not prove \(\Delta_F=0\).  It reduces the unknown input at a
candidate defect value to:
\begin{enumerate}&#91;label=(\arabic*)&#93;
\item the square class \(d\) defining the normal quadratic resolvent;
\item the height-two primes of its singular locus;
\item a fractional-ideal or finite-presentation representative of \(L\);
\item the local class vector \((&#91;L_\mathfrak p&#93;)_\mathfrak p\);
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
</code></pre>

<a id="source-3f54e773a7d88aaf"></a>

## `research-notes/lane1-collision-saturation-20260802-v1/lane1-collision-v8-manifest.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "packet": "lane1-collision-saturation-v8",
  "date": "2026-08-02",
  "mathematical_scope": &#91;
    "exact collision Cech saturation criterion for the cubic flatness defect",
    "divided-difference diagonal/off-diagonal idempotent",
    "formal collision-product flatness",
    "standard triple-root collision saturation"
  &#93;,
  "does_not_establish": &#91;
    "unconditional flatness for every generic-degree-three Keller map",
    "boundary completeness or recovery of the affine opening from a flat cover",
    "independent specialist verification"
  &#93;,
  "source_validation": {
    "labels": 52,
    "unique_labels": 52,
    "missing_references": &#91;&#93;
  },
  "files": &#91;
    {
      "path": "flatness-defect-repairs.tex",
      "bytes": 85987,
      "sha256": "4b468e00f6c83f158c89e90a8819858b91a1d1f4dfd7c582915204236efdb60c"
    },
    {
      "path": "cubic-flatness-normalization-defects.md",
      "bytes": 13516,
      "sha256": "f64182b6d9dee30b8bdd5c8e14db376a336b519b3be32be8418d29b646ce2ad3"
    },
    {
      "path": "lane1-collision-saturation-v8.tex",
      "bytes": 3131,
      "sha256": "51762052fdcb33ac7e8c9dbc0bb5ed8bbceb90b518ccc66f90ef92ccb82fee39"
    },
    {
      "path": "lane1-collision-saturation-v8.pdf",
      "bytes": 476635,
      "sha256": "b3422c1002aae131f0ffd6ca312b65e7f1ca0ef3f564313bf27228cb9a16ee76"
    },
    {
      "path": "verify_collision_idempotent.py",
      "bytes": 3474,
      "sha256": "80e9117af525529b12dd8d36dac6c07c71e77cecec6d1819b289f65cc3fac842"
    },
    {
      "path": "collision-idempotent-verification-output.txt",
      "bytes": 455,
      "sha256": "a4d48863cdf5348bd00088df4edd9343026650aa85704f42e778eb42f152131a"
    },
    {
      "path": "verify_standard_collision_model.py",
      "bytes": 935,
      "sha256": "75f47234d04b0123f850ab42ba6c94a11d6aac7426b09edd914d12cfd26c31c5"
    },
    {
      "path": "standard-collision-verification-output.txt",
      "bytes": 465,
      "sha256": "8f3ee07bc44ca3aa0a7740e16aae2e32ada1d03aef73dce7f5c7e21665f747b2"
    },
    {
      "path": "verify_equivariant_flatness_example.py",
      "bytes": 3310,
      "sha256": "5c70f0118f392d95a66930b7adb1d7691ee578374cafc867e0b084a54e185399"
    },
    {
      "path": "equivariant-flatness-verification-output-v8.txt",
      "bytes": 676,
      "sha256": "cab978f86179f75f3bc98bb5b9b279112a50ee28c39cde82561fbb1a13fbde4b"
    },
    {
      "path": "verify_ade_matrix_factorizations.py",
      "bytes": 7687,
      "sha256": "2a087f4eb2897e42b930d5c5498127089f534f61a783cebb44494dc437dc590b"
    },
    {
      "path": "verification-output-v8.txt",
      "bytes": 1208,
      "sha256": "f45fde85fac15ecfef4dbd467755dc2abf82d3b413d946626907c9b362e151a8"
    },
    {
      "path": "verify_minimal_defect_sextic.py",
      "bytes": 12495,
      "sha256": "40ffa4dd4b9cd7aeac8783abb95741893a1e80d93d456f2b2b2bacc919c1d6ca"
    },
    {
      "path": "minimal-defect-verification-output-v8.txt",
      "bytes": 508,
      "sha256": "dc944450d4f91dc72afc78bceded75dba41d9e7ac2421c056ccb300d4c93415f"
    },
    {
      "path": "lane1-collision-v8.patch",
      "bytes": 110814,
      "sha256": "c75c4b57613ee97abede503e725276f46c3bfd94ef05da580eab392957672302"
    },
    {
      "path": "INTEGRATION-v8.md",
      "bytes": 3708,
      "sha256": "d454c71f9cd4c2fe4bdb19544a636592ccad52a768f45e6ba1a0d11a5761a58e"
    }
  &#93;
}
</code></pre>

<a id="source-9425e75cd188cddb"></a>

## `research-notes/lane1-collision-saturation-20260802-v1/verify_collision_idempotent.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact divided-difference certificate for the cubic Keller collision idempotent.

The script uses the announced degree-three Keller map.  It constructs a
polynomial divided-difference matrix M with F(X)-F(X')=M(X-X'), verifies the
constant Jacobian, and checks the explicit certificate

    q(q-c) = 0 in S tensor_R S,  q=det(M), c=det(JF),

by expressing q(q-c) in the ideal generated by the three fibre-difference
equations.  Hence e=q/c is the diagonal idempotent and 1-e cuts out the
off-diagonal collision component.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import sympy as sp

x, y, z, X, Y, Z = sp.symbols("x y z X Y Z")
left = (x, y, z)
right = (X, Y, Z)

def keller_map(a, b, c):
    p = (1 + a*b)**3*c + b**2*(1 + a*b)*(4 + 3*a*b)
    q = b + 3*a*(1 + a*b)**2*c + 3*a*b**2*(4 + 3*a*b)
    r = 2*a - 3*a**2*b - a**3*c
    return tuple(sp.expand(v) for v in (p, q, r))

F = keller_map(*left)
Fp = keller_map(*right)

def exact_quotient(num: sp.Expr, den: sp.Expr) -&gt; sp.Expr:
    poly_num = sp.Poly(sp.expand(num), x, y, z, X, Y, Z, domain=sp.QQ)
    poly_den = sp.Poly(den, x, y, z, X, Y, Z, domain=sp.QQ)
    quo, rem = sp.div(poly_num, poly_den)
    assert rem.is_zero
    return sp.expand(quo.as_expr())

# Sequential telescoping in the left variables.
Mrows = &#91;&#93;
for f in F:
    f_X = sp.expand(f.subs(x, X))
    f_XY = sp.expand(f_X.subs(y, Y))
    f_XYZ = sp.expand(f_XY.subs(z, Z))
    assert sp.expand(f_XYZ - Fp&#91;len(Mrows)&#93;) == 0
    m1 = exact_quotient(f - f_X, x - X)
    m2 = exact_quotient(f_X - f_XY, y - Y)
    m3 = exact_quotient(f_XY - f_XYZ, z - Z)
    Mrows.append((m1, m2, m3))
M = sp.Matrix(Mrows)
delta = sp.Matrix(&#91;x-X, y-Y, z-Z&#93;)
fibre_diff = sp.Matrix(&#91;sp.expand(a-b) for a, b in zip(F, Fp)&#93;)
assert all(sp.expand(v) == 0 for v in M*delta - fibre_diff)

J = sp.Matrix(F).jacobian(left)
c = sp.expand(J.det())
assert c == -2
q = sp.expand(M.det())
q_diag = sp.expand(q.subs({x:X, y:Y, z:Z}, simultaneous=True))
assert q_diag == c

# q-c = a_1(x-X)+a_2(y-Y)+a_3(z-Z), again by telescoping.
q_X = sp.expand(q.subs(x, X))
q_XY = sp.expand(q_X.subs(y, Y))
q_XYZ = sp.expand(q_XY.subs(z, Z))
assert sp.expand(q_XYZ-c) == 0
a = sp.Matrix(&#91;
    exact_quotient(q-q_X, x-X),
    exact_quotient(q_X-q_XY, y-Y),
    exact_quotient(q_XY-q_XYZ, z-Z),
&#93;)
assert sp.expand((a.dot(delta)) - (q-c)) == 0

adj = M.adjugate()
qdelta_certificate = adj*fibre_diff
assert all(sp.expand(v-q*d) == 0 for v, d in zip(qdelta_certificate, delta))

# This is the explicit fibre-ideal certificate for q(q-c).
coefficients = (a.T*adj)&#91;0, :&#93;
certificate_rhs = sum(coefficients&#91;j&#93;*fibre_diff&#91;j&#93; for j in range(3))
assert sp.expand(q*(q-c)-certificate_rhs) == 0

# e=q/c then satisfies e^2-e=0 modulo the fibre equations.
print("constant Jacobian c =", c)
print("degrees of divided-difference entries =", &#91;&#91;sp.Poly(M&#91;i,j&#93;, *left, *right).total_degree() for j in range(3)&#93; for i in range(3)&#93;)
print("degree(q) =", sp.Poly(q, *left, *right).total_degree())
print("terms(q) =", len(sp.Poly(q, *left, *right).terms()))
print("verified F-F' = M (X-X')")
print("verified q|_diagonal = c")
print("verified q(X-X') = adj(M)(F-F')")
print("verified q(q-c) lies in (F_1-F'_1,F_2-F'_2,F_3-F'_3)")
print("therefore e=q/c is the diagonal idempotent in S tensor_R S")
print("and 1-e cuts out the off-diagonal collision algebra")

path = Path(__file__)
print("script_sha256 =", hashlib.sha256(path.read_bytes()).hexdigest())
</code></pre>

<a id="source-915e7bbeb67e7bc2"></a>

## `research-notes/lane1-collision-saturation-20260802-v1/verify_standard_collision_model.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact algebra for the standard ordered-root triple-collision model."""
from __future__ import annotations
import hashlib
from pathlib import Path
import sympy as sp
u,v=sp.symbols('u v')
f1=sp.expand(u*(u+v)); f2=sp.expand(u*v); f3=sp.expand(v*(u+v))
assert sp.expand(f1-f2-u**2)==0
assert sp.expand(f3-f2-v**2)==0
# Conversely f1,f3 are in (u^2,uv,v^2), so the ideals are equal.
G1=sp.groebner(&#91;f1,f2,f3&#93;,u,v,order='lex')
G2=sp.groebner(&#91;u**2,u*v,v**2&#93;,u,v,order='lex')
assert G1==G2
print('collision generators =',f1,f2,f3)
print('Groebner basis =',list(G1.polys))
print('verified (u(u+v),uv,v(u+v)) = (u,v)^2')
print('the common complement is the triple-root axis V(u,v)')
print('a formal axis parameter t acts injectively on H^2_(u,v)(C&#91;&#91;u,v,t&#93;&#93;)')
print('therefore the closed-point collision saturation quotient vanishes')
print('script_sha256 =',hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
</code></pre>

<a id="source-c8ccaa464f51cbd5"></a>

## `research-notes/lane1-collision-saturation-20260803-v2/README.md`

<pre><code class="language-markdown">
# Recovered complete Lane 1 proof source

This packet restores the complete `flatness-defect-repairs.tex` supplied by
the Lane 1 collision-saturation contribution. The earlier tracked packet
retained a 562-line excerpt and the original unified patch, but its manifest
described an 85,987-byte, 2,336-line proof source that was not materialized as
a standalone file.

`flatness-defect-repairs-full.tex` was extracted mechanically from the
`/dev/null` addition in
`research-notes/lane1-collision-saturation-20260802-v1/lane1-collision-v8.patch`.
Its SHA-256 is
`4b468e00f6c83f158c89e90a8819858b91a1d1f4dfd7c582915204236efdb60c`,
exactly the digest recorded for `flatness-defect-repairs.tex` in the original
packet manifest.

The collision-saturation theorem and proof begin at label
`thm:collision-cech-saturation`. In that theorem, `I_y` is the image of the
first differential inside the kernel of the second differential in a
three-chart affine Cech complex; it is not a source-chart ideal. Its
saturation is closed-point saturation by `m_y^infinity` inside that kernel.

This recovery establishes access to the supplied proof body. It does not add
an independent proof of the theorem or strengthen its mathematical scope.
</code></pre>

<a id="source-195de0d23627037b"></a>

## `research-notes/lane1-collision-saturation-20260803-v2/flatness-defect-repairs-full.tex`

<pre><code class="language-tex">
\section{The formal Picard obstruction and Kummer-toroidal flatness}
\label{app:flatness-defect-repairs}

This appendix sharpens Lane~1 without asserting an unconditional cubic
flatness theorem.  Its main point is that the remaining finite Ext defect has
three exact incarnations:
\&#91;
\operatorname{Ext}^1_A(B,A),\qquad
D_A H^2_{\mathfrak m}(B),\qquad
D_A H^1_{\mathfrak m}(S_A/B).
\&#93;
The middle group is the Lie algebra of Boutot's local Picard scheme.  Thus a
nonflat point forces a positive-dimensional family of Henselian or
\'{e}tale-local line bundles, and after completion it forces an uncountable,
non-torsion jump in the local divisor class group.  This yields useful formal
criteria---notably analytic \(\mathbf Q\)-factoriality---that eliminate a
defect.

A second result proves that every connected algebraic symmetry confines the
defect to its target fixed locus; in particular, every weighted
\(\mathbf G_m\)-equivariant cubic Keller map with no zero target weight has
flat normalization.  Its infinitesimal analogue is stronger locally: a
logarithmic derivation of the reduced branch divisor extends to the
normalization and acts on the Ext defect, so a nonflat point must be a
zero-dimensional logarithmic branch stratum.  Formal-product and
logarithmically equisingular branch germs are flat.

The new collision theorem passes to the \(S_3\)-Galois closure and covers its
attained part by the three conjugate affine source charts.  An explicit
divided-difference idempotent cuts the diagonal from the pair-collision
algebra.  The punctual first cohomology of the resulting three-chart
\v{C}ech complex is canonically
\&#91;
 D_A\Delta_y\otimes V_{\mathrm{std}}.
\&#93;
Thus flatness is equivalent to one exact saturation equality in the pair- and
triple-collision rings.  We also convert the infinite boundary-pole
filtration into a finite certificate: every nonzero defect is detected by
finitely many explicit \(\operatorname{Ext}^2\) surface-deficiency modules
of elementary deleted-sheet pole steps.

Further criteria prove flatness whenever the finite cover is
Kummer-trivializable along its boundary, whenever the actual deleted boundary
is Cartier--Cohen--Macaulay after a tame cover, or whenever the quadratic
resolvent is klt.  Hence any surviving Keller defect is simultaneously
non-\(\mathbf Q\)-factorial after completion, non-Kummer-toroidal, supported
at a bad deleted boundary, located at a zero-dimensional logarithmic stratum,
and carried by a non-klt quadratic-resolvent branch pair.

\subsection{Ordinary and \texorpdfstring{\'{e}tale}{etale}-local Picard groups}

Let \((z,Z)\) be a normal complex threefold germ and put
\&#91;
U_z=\Spec\mathcal O_{Z,z}\setminus\{z\}.
\&#93;
The ordinary local Picard group is \(\Pic(U_z)\).  Boutot's local Picard
scheme represents a different functor: one Henselizes after base change and
then sheafifies in the \'{e}tale topology.  Over an algebraically closed field
its complex points are the \'{e}tale-local group
\&#91;
\Pic^{\mathrm{et-loc}}(z,Z)
 =\Pic\bigl(\Spec\mathcal O^h_{Z,z}\setminus\{z\}\bigr),
\&#93;
not, in general, \(\Pic(U_z)\).  The natural map
\&#91;
\Pic(U_z)\longrightarrow\Pic^{\mathrm{et-loc}}(z,Z)
\&#93;
can be far from surjective.  In particular, factoriality of
\(\mathcal O_{Z,z}\) does not by itself imply Cohen--Macaulayness unless one
also controls the Henselian or completed local class group.

A precise reference is Koll\'ar,
\href{https://arxiv.org/abs/1407.5108}{\emph{Maps between local Picard
groups}}, Definitions~19--22 and (23.1)--(23.3).  The distinction is the
reason the tempting argument ``the boundary class group is finitely generated,
therefore the defect vanishes'' is invalid.

\subsection{The Ext defect as a Picard Lie algebra}

Let \((A,\mathfrak m,k)\) be a three-dimensional regular local
\(\C\)-algebra essentially of finite type, with \(k=\C\).  Let \(B\) be a
finite, torsion-free, normal \(A\)-algebra of pure dimension three, and put
\&#91;
X=\Spec B,
\qquad
x=V(\mathfrak mB)\subset X.
\&#93;
Thus \(x\) is a zero-dimensional closed subscheme, possibly with several
closed points.  Define
\&#91;
\Delta(B/A)=\operatorname{Ext}^1_A(B,A).
\&#93;
Write \(D_A(-)=\operatorname{Hom}_A(-,E_A(k))\) for Matlis duality.

\begin{theorem}&#91;Picard--Lie realization of the finite defect&#93;
\label{thm:picard-lie-defect}
In the setup above:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item \(B\) is finite free away from \(\mathfrak m\), and
      \(\Delta(B/A)\) has finite length;
\item Boutot's local Picard scheme
\&#91;
\mathbf{Pic}^{\mathrm{loc}}(x,X)
\&#93;
exists and is locally of finite type over \(\C\);
\item there are canonical identifications
\&#91;
\operatorname{Lie}\mathbf{Pic}^{\mathrm{loc}}(x,X)
 \simeq H^2_x(X,\mathcal O_X)
 \simeq D_A\Delta(B/A);
\&#93;
\item if \(G=\mathbf{Pic}^{\mathrm{loc},\circ}(x,X)\), then
\&#91;
\boxed{\ \dim G=\operatorname{length}_A\Delta(B/A)\ };
\&#93;
\item the following are equivalent:
\begin{enumerate}&#91;label=(\alph*)&#93;
\item \(B\) is finite flat over \(A\);
\item \(B\) is Cohen--Macaulay;
\item \(\Delta(B/A)=0\);
\item \(G\) is trivial;
\item \(\Pic^{\mathrm{et-loc}}(x,X)
       :=\mathbf{Pic}^{\mathrm{loc}}(x,X)(\C)\) is countable;
\item \(\Pic^{\mathrm{et-loc}}(x,X)\) is finitely generated.
\end{enumerate}
\end{enumerate}
\end{theorem}

\begin{proof}
At every height-one prime of \(A\), a finite torsion-free module is free.  At
a height-two prime, the local factors of \(B\) are normal two-dimensional
local rings and hence Cohen--Macaulay by Serre's \(S_2\) condition.  A system
of parameters from the regular base remains a system of parameters in each
finite local factor, so miracle flatness makes these factors free.  Thus the
nonfree locus is supported at \(\mathfrak m\), and \(\Delta(B/A)\) has finite
length.

The pair \((x,X)\) satisfies Boutot's hypotheses: \(X\) is \(S_2\), pure of
dimension three, and \(x\) is zero-dimensional.  Local duality shows that
\(H^2_x(X,\mathcal O_X)\) is finite-dimensional.  Hence the local Picard
functor is represented, and its tangent space at the identity is
\&#91;
T_e\mathbf{Pic}^{\mathrm{loc}}(x,X)
 \simeq H^2_x(X,\mathcal O_X).
\&#93;
Since \(V(\mathfrak mB)=x\), local duality over the regular local ring \(A\)
gives
\&#91;
H^2_{\mathfrak m}(B)
 \simeq D_A\operatorname{Ext}^1_A(B,A).
\&#93;
This proves (ii)--(iii).

The identity component \(G\) is a connected algebraic group of finite type.
Every locally algebraic group scheme over a characteristic-zero field is
smooth.  Therefore
\&#91;
\dim G=\dim_\C T_eG
      =\dim_\C D_A\Delta(B/A)
      =\operatorname{length}_A\Delta(B/A),
\&#93;
proving (iv).

Normality gives \(\operatorname{depth}_A B\ge2\).  Thus
\(\Delta(B/A)=0\), equivalently \(H^2_{\mathfrak m}(B)=0\), is equivalent to
\(\operatorname{depth}_A B=3\).  Auslander--Buchsbaum over \(A\) then makes
\(B\) free.  This proves (a)--(d).

Finally, in characteristic zero the local N\'eron--Severi group
\&#91;
\operatorname{NS}^{\mathrm{loc}}(x,X)
 =\mathbf{Pic}^{\mathrm{loc}}(x,X)/G
\&#93;
is finitely generated.  If \(G\) is trivial, the group of complex points is
therefore finitely generated.  If \(G\) is positive-dimensional, then
\(G(\C)\), and hence the full \'{e}tale-local Picard group, is uncountable.
This proves (e)--(f).
\end{proof}

\begin{corollary}&#91;The one-dimensional defect alternative&#93;
\label{cor:one-dimensional-picard-defect}
If \(\operatorname{length}_A\Delta(B/A)=1\), then
\(\mathbf{Pic}^{\mathrm{loc},\circ}(x,X)\) is a smooth connected
one-dimensional commutative algebraic group.  Hence it is isomorphic to one
of
\&#91;
\mathbf G_a,\qquad \mathbf G_m,\qquad\text{or an elliptic curve}.
\&#93;
\end{corollary}

\subsection{The affine opening and the completion jump}

\begin{lemma}&#91;Boundary class group of an affine-space opening&#93;
\label{lem:affine-opening-class-group}
Let \(Z\) be a normal integral affine variety and suppose
\(U\subset Z\) is a dense open subscheme isomorphic to \(\A^n_\C\).  Let
\(D_1,\ldots,D_r\) be the codimension-one irreducible components of
\(Z\setminus U\).  Then
\&#91;
\Cl(Z)\simeq\bigoplus_{i=1}^r\mathbf Z&#91;D_i&#93;.
\&#93;
In particular, for every finite set of closed points \(x\subset Z\), the
ordinary Zariski-local Picard group
\&#91;
\Pic^{\mathrm{Zar-loc}}(x,Z)
 :=\Pic\bigl(\Spec\mathcal O_{Z,x}\setminus x\bigr)
\&#93;
is finitely generated.
\end{lemma}

\begin{proof}
The divisor localization sequence is
\&#91;
\bigoplus_i\mathbf Z&#91;D_i&#93;\longrightarrow\Cl(Z)
 \longrightarrow\Cl(U)\longrightarrow0.
\&#93;
Since \(U\simeq\A^n\), its class group is zero.  If a divisor supported on
the \(D_i\) is principal, its defining rational function restricts to a unit
on \(U\).  The only units on affine space are nonzero constants, so its
divisor is zero.  The first arrow is therefore also injective.

The class group of the semilocal ring \(\mathcal O_{Z,x}\) is a quotient of
\(\Cl(Z)\), and a line bundle on its punctured spectrum extends uniquely as
a rank-one reflexive module.  Thus \(\Pic^{\mathrm{Zar-loc}}(x,Z)\) injects
into a finitely generated group.
\end{proof}

\begin{theorem}&#91;Completed class-group criterion and jump&#93;
\label{thm:completed-class-group-jump}
Let \((C,\mathfrak n)\) be an excellent normal three-dimensional local
\(\C\)-algebra that is finite over a regular local \(\C\)-algebra of
dimension three, and let \(\widehat C\) be its completion.
\begin{enumerate}&#91;label=(\roman*)&#93;
\item If \(\Cl(\widehat C)\) is countable, then \(C\) is
      Cohen--Macaulay.
\item If \(\widehat C\) is \(\mathbf Q\)-factorial, then \(C\) is
      Cohen--Macaulay.
\item If \(C\) is not Cohen--Macaulay, then
\&#91;
\Pic\bigl(\Spec\widehat C\setminus\{\widehat{\mathfrak n}\}\bigr)
\quad\text{and}\quad
\Cl(\widehat C)
\&#93;
are uncountable and contain elements of infinite order.
\item If, in addition, \(C=\mathcal O_{Z,z}\) for a normal affine
threefold \(Z\) containing \(\A^3\) as a dense open, then the completion map
\&#91;
\Cl(C)\longrightarrow\Cl(\widehat C)
\&#93;
has uncountable cokernel whenever \(C\) is not Cohen--Macaulay.
\end{enumerate}
\end{theorem}

\begin{proof}
Excellence and normality imply that \(\widehat C\) is normal, and completion
preserves depth.  Apply Boutot's construction to the complete local scheme
\(\Spec\widehat C\).  Its local Picard identity component has tangent space
\(H^2_{\widehat{\mathfrak n}}(\widehat C)\), which is nonzero exactly when
\(C\) has depth two.  Because \(\widehat C\) is complete, Koll\'ar's
comparison (23.3) identifies the ordinary punctured Picard group with the
complex points of this local Picard scheme.

A line bundle on the punctured spectrum extends reflexively, giving an
injection
\&#91;
\Pic\bigl(\Spec\widehat C\setminus\{\widehat{\mathfrak n}\}\bigr)
 \hookrightarrow\Cl(\widehat C).
\&#93;
If \(C\) is not Cohen--Macaulay, the Picard identity component is a
positive-dimensional connected algebraic group.  Its complex points are
uncountable and include elements of infinite order.  This proves (iii), and
immediately rules out a countable completed class group.

If \(\widehat C\) is \(\mathbf Q\)-factorial, then its local divisor class
group is torsion: a \(\mathbf Q\)-Cartier divisor has a Cartier multiple, and
Cartier divisors on a local scheme are principal.  This is incompatible with
the non-torsion points of a positive-dimensional connected algebraic group,
proving (ii).

For (iv), \cref{lem:affine-opening-class-group} makes \(\Cl(C)\) countable.
If \(C\) is not Cohen--Macaulay, the target is uncountable by (iii), so the
cokernel is uncountable.
\end{proof}

\begin{corollary}&#91;Henselian or analytic \(\mathbf Q\)-factoriality forces flatness&#93;
\label{cor:analytic-qfactorial-flatness}
In the setup of \cref{thm:picard-lie-defect}, suppose that for every closed
point \(z\in x\), either the Henselization
\(\mathcal O^h_{X,z}\) or the completed local ring
\(\widehat{\mathcal O}_{X,z}\) is \(\mathbf Q\)-factorial.  Then \(B\) is
finite free over \(A\).

More generally, it is enough that every Henselian or completed local class
group under consideration be countable or finitely generated.
\end{corollary}

\begin{proof}
For a Henselian factor, its punctured Picard group is the complex-point group
of Boutot's local Picard scheme.  A positive-dimensional identity component
contains uncountably many elements of infinite order, contradicting either
countability or \(\mathbf Q\)-factoriality.  Hence every such factor is
Cohen--Macaulay by \cref{thm:picard-lie-defect}.  For completed factors apply
\cref{thm:completed-class-group-jump}.  Faithfully flat descent from the
Henselization or completion gives the assertion for the original local
factors, and \cref{thm:picard-lie-defect} finishes the proof.
\end{proof}

\begin{theorem}&#91;\'{E}tale boundary-algebraization criterion&#93;
\label{thm:etale-boundary-algebraization}
Let \(Z\) be a normal affine complex threefold containing
\(U\simeq\A^3\) as a dense open subscheme, and let \(x\subset Z\) be a
finite set of closed points.  Consider the natural map
\&#91;
\alpha_x:\Pic^{\mathrm{Zar-loc}}(x,Z)
 \longrightarrow\Pic^{\mathrm{et-loc}}(x,Z).
\&#93;
Then the following are equivalent:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item \(Z\) is Cohen--Macaulay at every point of \(x\);
\item the identity component of
      \(\mathbf{Pic}^{\mathrm{loc}}(x,Z)\) is trivial;
\item \(\operatorname{coker}(\alpha_x)\) is countable;
\item \(\operatorname{coker}(\alpha_x)\) is finitely generated.
\end{enumerate}
If these conditions fail, the cokernel is uncountable.  More precisely, it
contains the image of a positive-dimensional connected algebraic group
modulo its countable intersection with the ordinary local Picard group.
\end{theorem}

\begin{proof}
The equivalence of (i) and (ii) follows pointwise from
\cref{thm:picard-lie-defect}.  By \cref{lem:affine-opening-class-group}, the
source of \(\alpha_x\) is finitely generated and hence countable.  If the
identity component is trivial, the \'{e}tale-local Picard group is its
finitely generated local N\'eron--Severi group, so the cokernel is finitely
generated.  If the identity component has positive dimension, its complex
points are uncountable; quotienting by the countable ordinary local Picard
group leaves an uncountable cokernel.
\end{proof}

\subsection{Keller principal parts}

Let
\&#91;
F:X=\A^3_\C\longrightarrow Y=\A^3_\C
\&#93;
be a generically finite Keller map.  Put
\&#91;
R=\mathcal O(Y),\qquad S=\mathcal O(X),
\&#93;
and let \(B\) be the normalization of \(R\) in \(\operatorname{Frac}S\).
Write \(\pi:\overline X=\Spec B\to Y\).  For \(y\in Y\), set
\&#91;
A=R_y,\qquad B_y=B\otimes_R A,\qquad S_A=S\otimes_R A,
\&#93;
and let \(x_y=V(\mathfrak m_yB_y)\).

\begin{theorem}&#91;Picard--principal-parts form of the Keller defect&#93;
\label{thm:keller-picard-principal-parts}
Assume \(y\notin F(X)\), and put
\&#91;
P_y=S_A/B_y.
\&#93;
Then there are canonical identifications
\&#91;
\boxed{
\operatorname{Lie}\mathbf{Pic}^{\mathrm{loc}}(x_y,\Spec B_y)
 \simeq H^1_{\mathfrak m_y}(P_y)
 \simeq D_A\operatorname{Ext}^1_A(B_y,A).
}
\&#93;
Consequently the following are equivalent:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item the normalization is flat over \(y\);
\item \(H^1_{\mathfrak m_y}(S_A/B_y)=0\);
\item the local Picard identity component is trivial;
\item the \'{e}tale-local line bundles near \(x_y\), modulo ordinary
      Zariski-local boundary classes, form a countable group.
\end{enumerate}
Moreover
\&#91;
\dim\mathbf{Pic}^{\mathrm{loc},\circ}(x_y,\Spec B_y)
 =\operatorname{length}_A\operatorname{Ext}^1_A(B_y,A).
\&#93;
\end{theorem}

\begin{proof}
Zariski's Main Theorem gives the open immersion
\(X\hookrightarrow\overline X\), hence the inclusion \(B_y\subset S_A\).
Because \(y\) is omitted, \(\mathfrak m_yS_A=S_A\), so
\&#91;
H^i_{\mathfrak m_y}(S_A)=0
\quad\text{for every }i.
\&#93;
The exact sequence
\&#91;
0\longrightarrow B_y\longrightarrow S_A\longrightarrow P_y
\longrightarrow0
\&#93;
and normality of \(B_y\) give
\&#91;
H^1_{\mathfrak m_y}(P_y)
 \simeq H^2_{\mathfrak m_y}(B_y).
\&#93;
Apply local duality and \cref{thm:picard-lie-defect}.  The final equivalences
use \cref{thm:etale-boundary-algebraization}, since
\(\overline X\) contains \(X\simeq\A^3\) as a dense open subscheme.
\end{proof}



\subsection{Degree-three omitted carrier curves}

Assume now that the Keller map has generic degree three.  Let
\(\widetilde K\) be the \(S_3\)-Galois closure of its cubic function-field
extension, let \(T\) be the normalization of the target in \(\widetilde K\),
and put
\&#91;
 Q=T^{A_3},\qquad B=T^{C_2}.
\&#93;
The corrected divisorial inertia classification makes \(T\to Q\) \'{e}tale
in codimension one.  Hence, for a nontrivial character of \(A_3\),
\&#91;
 T\simeq Q\oplus L\oplus L^{&#91;2&#93;},
 \qquad L^{&#91;3&#93;}\simeq Q,
\&#93;
Let \(\sigma\) be a transposition.  It interchanges \(L\) and
\(L^{&#91;2&#93;}\), and taking \(\langle\sigma\rangle\)-invariants gives
\&#91;
 B=R\oplus\{\ell+\sigma(\ell):\ell\in L\}.
\&#93;
The second summand is the cubic trace-zero module, and
\(\ell\mapsto\ell+\sigma(\ell)\) is an \(R\)-linear isomorphism.
Thus the cubic defect vanishes exactly when \(L\) is maximal
Cohen--Macaulay over \(Q\).

\begin{theorem}&#91;Omitted carrier-curve theorem&#93;
\label{thm:omitted-carrier-curve}
Let
\&#91;
 Y^{\mathrm{att}}=F(X),\qquad Q^{\mathrm{att}}=Q\times_Y Y^{\mathrm{att}}.
\&#93;
Then:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item the eigensheaf \(L\) is locally free on \(Q^{\mathrm{att}}\);
\item if the cubic normalization has a nonzero defect at a closed point
      \(y\), there are a height-two singular prime
      \(\mathfrak p\subset Q\) and its contraction
      \(\mathfrak r=\mathfrak p\cap R\), also of height two, such that
\&#91;
 &#91;L_{\mathfrak p}&#93;\ne0
 \quad\text{in}\quad
 \Cl(Q_{\mathfrak p})&#91;3&#93;,
 \qquad
 V(\mathfrak r)\subseteq O_F;
\&#93;
\item consequently, if the omitted set has no one-dimensional irreducible
      component, then the finite cubic normalization is flat.  In particular,
      flatness follows if \(\operatorname{Sing}(S_F)\) is zero-dimensional,
      and hence if the reduced nonproperness surface \(S_F\) is normal.
\end{enumerate}
\end{theorem}

\begin{proof}
The map \(X\to Y^{\mathrm{att}}\) is surjective and \'{e}tale.  Its base
change
\&#91;
 C=Q\times_YX\longrightarrow Q^{\mathrm{att}}
\&#93;
is therefore faithfully flat and \'{e}tale.  The quadratic and cubic
subfields of an \(S_3\)-extension are linearly disjoint, so the generic field
of \(C\) is \(\widetilde K\).  The normal algebra
\(T\times_QC\) has generic fibre
\&#91;
 \widetilde K\otimes_{\operatorname{Frac}Q}\widetilde K
 \simeq \widetilde K^{\times3}.
\&#93;
The three generic idempotents are integral, hence extend across the normal
base change.  Each component is finite and birational over the normal domain
\(C\), and is therefore \(C\).  Thus
\&#91;
 T\times_QC\simeq C^{\times3},
 \qquad L\otimes_QC\simeq C.
\&#93;
Local freeness descends through the faithfully flat map, proving (i).

Suppose the defect at \(y\) is nonzero.  Then for some point
\(\mathfrak q\in Q\) above \(y\), the rank-one reflexive module
\(L_{\mathfrak q}\) is not maximal Cohen--Macaulay, so its three-torsion
class is nonzero.  Dao's torsion theorem for the punctured spectrum of a
three-dimensional local hypersurface
(\href{https://doi.org/10.1112/S0010437X11005513}{Compos. Math. 148 (2012), 145--152}) gives an injection
\&#91;
 \Cl(Q_{\mathfrak q})&#91;3&#93;\hookrightarrow
 \bigoplus_{\substack{\mathfrak p\in\operatorname{Sing}(Q_{\mathfrak q})\\
                       \operatorname{ht}\mathfrak p=2}}
 \Cl(Q_{\mathfrak p})&#91;3&#93;.
\&#93;
Hence some height-two singular prime \(\mathfrak p\) has the asserted
nonzero localization.  Its contraction \(\mathfrak r\) has height two because
\(Q/R\) is finite.  By (i), the generic point of \(V(\mathfrak r)\) is not
attained.  The omitted set is closed, so the whole curve is omitted.  This
proves (ii).

The first assertion of (iii) is immediate.  The omitted-values theorem gives
\(O_F\subseteq\operatorname{Sing}(S_F)\).  A normal surface has
zero-dimensional singular locus, proving the remaining statements.
\end{proof}


\subsection{Connected symmetries force cubic flatness}

The finite-support character of the defect interacts strongly with algebraic
symmetries.  This gives an unconditional flatness theorem for the entire
graded or quasi-torus class, without using an explicit marked-root
compactification.

\begin{lemma}&#91;Attained-point flatness in generic degree three&#93;
\label{lem:attained-point-flatness}
Let \(F:X=\A^3_\C\to Y=\A^3_\C\) be a generic-degree-three Keller map, and
let \(B\) be the finite normalization algebra.  Then \(B\) is flat at every
point of \(F(X)\).
\end{lemma}

\begin{proof}
Let \(j:X\hookrightarrow\overline X=\Spec B\) be the open immersion from
Zariski's Main Theorem.  Base change the finite normalization by \(F\):
\&#91;
 p:\overline X\times_YX\longrightarrow X.
\&#93;
The diagonal lift \(x\mapsto(j(x),x)\) is a section.  The map \(p\) is
\'{e}tale along this section because \(\pi|_X=F\) is \'{e}tale.  A section
of a separated \'{e}tale morphism is open and closed; finiteness makes its
image closed in the whole base change.  Hence
\&#91;
 B\otimes_RS\simeq S\times C
\&#93;
for a finite normal rank-two \(S\)-algebra \(C\), where
\(S=\C&#91;x_1,x_2,x_3&#93;\).

The field trace splits
\&#91;
 C\simeq S\oplus L_0
\&#93;
with \(L_0\) rank-one reflexive.  Since \(S\) is factorial,
\(L_0\simeq S\); thus \(B\otimes_RS\) is free of rank three over \(S\).
If \(x\in X\) maps to \(y\), the local \'{e}tale homomorphism
\(R_y\to S_x\) is faithfully flat.  Freeness after this base change descends,
so \(B_y\) is finite free over \(R_y\).
\end{proof}

\begin{theorem}&#91;Connected-symmetry support theorem&#93;
\label{thm:connected-symmetry-support}
Let a connected complex algebraic group \(G\) act algebraically on
\(X=\A^3\) and \(Y=\A^3\), and let
\(F:X\to Y\) be a \(G\)-equivariant generic-degree-three Keller map.  Then
\&#91;
 \boxed{
 \operatorname{Supp}\Delta_F\subseteq Y^G\cap O_F.
 }
\&#93;
Consequently, if every target fixed point is attained,
\&#91;
 Y^G\subseteq F(X),
\&#93;
then the finite cubic normalization is flat.
\end{theorem}

\begin{proof}
The compatible actions on \(R=\mathcal O(Y)\) and
\(K=\operatorname{Frac}\mathcal O(X)\) preserve the integral closure \(B\).
Equivalently, the action lifts uniquely to the finite normalization.  Hence
its nonflat locus, or the support of \(\Delta_F\), is \(G\)-stable.

Normality makes \(B\) reflexive over the regular threefold \(Y\), so the
nonflat locus is finite.  The orbit of any point in this finite set is a
connected finite algebraic set because \(G\) is connected; it is therefore a
single point.  Thus every defect point lies in \(Y^G\).  By
\cref{lem:attained-point-flatness}, no attained point can support the defect,
which gives the displayed containment and the final assertion.
\end{proof}

\begin{corollary}&#91;Equivariant cubic flatness&#93;
\label{cor:equivariant-cubic-flatness}
Suppose \(F:\A^3\to\A^3\) is a generic-degree-three Keller map equivariant
for diagonal weighted \(\mathbf G_m\)-actions, and every target weight is
nonzero.  Then the finite cubic normalization is flat.

More generally, the same conclusion holds whenever \(F\) is polynomially
left--right equivalent to such an equivariant map.
\end{corollary}

\begin{proof}
A diagonal \(\mathbf G_m\)-action with no zero target weight has the unique
fixed point \(0\).  The source origin is fixed, so equivariance gives
\(F(0)=0\).  Apply \cref{thm:connected-symmetry-support}.  Flatness is
preserved by polynomial left--right equivalence.
\end{proof}

\begin{corollary}&#91;The Alp\"oge normalization is flat by symmetry&#93;
\label{cor:alpoge-equivariant-flatness}
For the announced three-dimensional counterexample
\&#91;
\begin{aligned}
a&amp;=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
b&amp;=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
c&amp;=2x-3x^2y-x^3z,
\end{aligned}
\&#93;
the finite cubic normalization is flat.
\end{corollary}

\begin{proof}
The map has generic degree three and is equivariant for source weights
\((1,-1,-2)\) and target weights \((-2,-1,1)\); see
\href{https://arxiv.org/abs/2607.20210}{T.~Shaska, \emph{Graded Keller maps
and the Jacobian Conjecture}, Section~2 and Proposition~4.3}.  All target
weights are nonzero, so \cref{cor:equivariant-cubic-flatness} applies.
\end{proof}

\begin{remark}&#91;Symmetry breaking is necessary for a defect&#93;
\label{rem:defect-breaks-connected-symmetry}
For any connected algebraic symmetry group of a cubic Keller map, every
possible defect point must be fixed by that group.  In particular, a complete
\(\mathbf G_a\)-symmetry with no target fixed points rules out the defect,
and a complete \(\mathbf G_m\)-symmetry reduces it to the target fixed locus.
This statement uses completeness of the symmetry action; the generally
incomplete inverse-Jacobian vector fields do not by themselves define such an
action.
\end{remark}


\subsection{Infinitesimal logarithmic propagation}

The connected-symmetry theorem has a local infinitesimal analogue.  It does
not require an algebraic group action: a single nonvanishing vector field
which is logarithmic along the divisorial branch locus already kills the
punctual Ext defect.

Let \((A,\mathfrak m,k)\) be a regular local \(\C\)-algebra of dimension
three, either essentially of finite type or complete, and let \(B\) be a
finite normal \(A\)-algebra which is generically separable.  Let
\&#91;
 D_{\mathrm{br}}\subset\Spec A
\&#93;
be the reduced union of the height-one primes at which \(B/A\) is ramified.
Since \(A\) is factorial, write \(D_{\mathrm{br}}=V(h)\) with \(h\)
squarefree, and put
\&#91;
 \operatorname{Der}_{\C}(A)(-\log D_{\mathrm{br}})
 =\{\delta\in\operatorname{Der}_{\C}(A):\delta(h)\in(h)\}.
\&#93;
Equivalently, \(\delta\) preserves every prime component of
\(D_{\mathrm{br}}\).

\begin{proposition}&#91;Logarithmic extension and the defect connection&#93;
\label{prop:logarithmic-extension-defect-connection}
Every
\(\delta\in\operatorname{Der}_{\C}(A)(-\log D_{\mathrm{br}})\)
extends uniquely to a \(\C\)-derivation of the total quotient algebra of
\(B\), preserves \(B\), and induces a \(\delta\)-connection on
\&#91;
 \Delta(B/A)=\operatorname{Ext}^1_A(B,A).
\&#93;
Consequently the annihilator
\(\operatorname{Ann}_A\Delta(B/A)\) is stable under every logarithmic
\(\delta\).
\end{proposition}

\begin{proof}
A derivation of \(\operatorname{Frac}A\) extends uniquely through every finite
separable field extension.  Preservation of the integral closure is exactly
the liftability statement for logarithmic derivations.  More precisely,
purity of the branch locus over the regular base
(Stacks Project, Tag~\href{https://stacks.math.columbia.edu/tag/0BMB}{0BMB})
makes the reduced discriminant set equal to the reduced divisorial branch
locus \(D_{\mathrm{br}}\).  K\"allstr\"om's theorem applies to the finite dominant
morphism \(\Spec B\to\Spec A\): the source is Krull, the residue extensions
at the height-one critical points are algebraic, and all divisorial
ramification is tame in characteristic zero.  It identifies the liftable
derivations with those preserving the reduced discriminant ideal.  Therefore
\&#91;
 \operatorname{Der}_{\C}(A)(-\log D_{\mathrm{br}})
 =\operatorname{Der}_{\C}(A)^{\mathrm{lift}},
\&#93;
and every displayed logarithmic derivation preserves \(B\).  See
\href{https://arxiv.org/abs/math/0604559}{R.~K\"allstr\"om,
\emph{Liftable derivations for generically separably algebraic morphisms of
schemes}, Theorem~2.2.1(L2)}.

Normality gives \(\operatorname{pd}_A B\le1\).  Choose a finite free
resolution
\&#91;
 0\longrightarrow F_1\xrightarrow{d}F_0\longrightarrow B\longrightarrow0.
\&#93;
Lift the \(\delta\)-connection on \(B\) to a \(\delta\)-connection
\(\nabla_0\) on \(F_0\).  The kernel of \(F_0\to B\) is stable, so there is
a unique \(\delta\)-connection \(\nabla_1\) on \(F_1\) for which \(d\) is
horizontal.  On the dual complex use
\&#91;
 \nabla_i^\vee(\phi)=\delta\circ\phi-\phi\circ\nabla_i.
\&#93;
This commutes with the dual differential and hence descends to
\(\operatorname{Ext}^1_A(B,A)\).

Finally, if \(a\Delta=0\), then for \(m\in\Delta\),
\&#91;
 0=\nabla(am)=\delta(a)m+a\nabla(m)=\delta(a)m.
\&#93;
Thus \(\delta(a)\) also annihilates \(\Delta\).
\end{proof}

\begin{lemma}&#91;A punctual module has no transverse connection&#93;
\label{lem:no-punctual-transverse-connection}
Let \((A,\mathfrak m)\) be a regular local \(\C\)-algebra and let \(M\) be a
finite-length \(A\)-module carrying a \(\delta\)-connection.  If the value of
\(\delta\) at the closed point is nonzero, equivalently
\&#91;
 \delta(\mathfrak m)\not\subseteq\mathfrak m,
\&#93;
then \(M=0\).
\end{lemma}

\begin{proof}
Let \(I=\operatorname{Ann}_A(M)\).  The connection makes \(I\)
\(\delta\)-stable.  If \(M\ne0\), then \(I\) is \(\mathfrak m\)-primary.
Choose \(x\in\mathfrak m\) such that \(\delta(x)\) is a unit and choose
\(N\) with \(x^N\in I\).  Stability gives \(\delta^N(x^N)\in I\).  Modulo
\(\mathfrak m\), repeated Leibniz differentiation gives
\&#91;
 \delta^N(x^N)\equiv N!\,\delta(x)^N\pmod{\mathfrak m};
\&#93;
all other terms retain a factor of \(x\).  The displayed element is a unit,
contradicting \(I\subseteq\mathfrak m\).
\end{proof}

Define the logarithmic zero locus \(Z_{\log}(D_{\mathrm{br}})\) to be the set
of points \(y\in\Spec A\) at which the evaluation map
\&#91;
 \operatorname{Der}_{\C}(A)(-\log D_{\mathrm{br}})\otimes_A k(y)
 \longrightarrow T_y\Spec A
\&#93;
is zero.

\begin{theorem}&#91;Logarithmic support theorem&#93;
\label{thm:logarithmic-support}
In the setup above,
\&#91;
 \boxed{
 \operatorname{Supp}\Delta(B/A)
 \subseteq Z_{\log}(D_{\mathrm{br}}).
 }
\&#93;
In particular, if there is a logarithmic derivation whose value at the closed
point is nonzero, then \(B\) is finite free over \(A\).
\end{theorem}

\begin{proof}
Localize at a point outside \(Z_{\log}(D_{\mathrm{br}})\).  By
\cref{prop:logarithmic-extension-defect-connection}, the punctual defect has
a connection for a derivation nonzero at that point.  Apply
\cref{lem:no-punctual-transverse-connection}.
\end{proof}

\begin{corollary}&#91;Formal-product and logarithmic-equisingularity flatness&#93;
\label{cor:formal-product-branch-flatness}
Suppose that, after completion at the closed point, there are regular
parameters \((u,v,t)\) for which the reduced divisorial branch equation is
\&#91;
 h=\varepsilon\,h_0(u,v)
\&#93;
with \(\varepsilon\) a unit.  Then \(B\) is finite free over \(A\).
More generally, flatness follows whenever the closed point lies on a
positive-dimensional logarithmic stratum of the reduced branch divisor.
\end{corollary}

\begin{proof}
The derivation \(\partial_t\) satisfies
\(\partial_t(h)=(\partial_t\varepsilon/\varepsilon)h\), so it is logarithmic
and nonzero at the closed point.  Apply
\cref{thm:logarithmic-support} to the completion.  Freeness of the completion
descends to \(A\).
\end{proof}

\begin{proposition}&#91;Relative Tjurina--Kodaira--Spencer criterion&#93;
\label{prop:relative-tjurina-flatness}
Assume after completion that
\&#91;
 A=\C&#91;&#91;u,v,t&#93;&#93;,
 \qquad C=V(u,v)
\&#93;
is a smooth candidate carrier curve and that the reduced branch divisor has
equation \(h=0\).  Define its relative Tjurina module and axial
Kodaira--Spencer class by
\&#91;
 \mathcal T_{h/C}
 =A/(h,\partial_u h,\partial_v h),
 \qquad
 \kappa_C(h)=&#91;\partial_t h&#93;\in\mathcal T_{h/C}.
\&#93;
Then the following are equivalent:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item \(\kappa_C(h)=0\);
\item there is a logarithmic derivation
\&#91;
 \delta=\partial_t+a\partial_u+b\partial_v
\&#93;
whose component along \(C\) is a unit.
\end{enumerate}
Either condition forces \(B\) to be finite free over \(A\).  Consequently,
a cubic defect on a smooth omitted carrier curve forces
\&#91;
 \boxed{\kappa_C(h)\ne0.}
\&#93;
The vanishing or nonvanishing is invariant under formal coordinate changes
preserving the carrier curve and multiplication of \(h\) by a unit.
\end{proposition}

\begin{proof}
The equality \(\kappa_C(h)=0\) means that for some \(a,b,g\in A\),
\&#91;
 \partial_t h=-a\partial_u h-b\partial_v h+gh.
\&#93;
Thus \(\delta=\partial_t+a\partial_u+b\partial_v\) satisfies
\(\delta(h)=gh\) and is logarithmic with nonzero value along \(C\).  The
converse is the same identity read in the relative Tjurina quotient.  Apply
\cref{thm:logarithmic-support}.  The final invariance follows from the chain
rule: coordinate changes preserving \(C\) alter \(\partial_t h\) only by a
unit multiple and by elements of
\((h,\partial_u h,\partial_v h)\).
\end{proof}

\begin{corollary}&#91;Logarithmically equisingular cubic flatness&#93;
\label{cor:log-equisingular-cubic-flatness}
Let \(F:\A^3\to\A^3\) be a generic-degree-three Keller map and let
\(D_{\mathrm{br}}\) be the reduced divisorial branch locus of its finite
normalization.  Then
\&#91;
 \boxed{
 \operatorname{Supp}\Delta_F
 \subseteq \operatorname{Curv}(O_F)\cap Z_{\log}(D_{\mathrm{br}}).
 }
\&#93;
Consequently the finite normalization is flat if the branch germ is formally
a product along every omitted curve, or more generally if every point of an
omitted curve lies on a positive-dimensional logarithmic stratum of
\(D_{\mathrm{br}}\).
\end{corollary}

\begin{proof}
Combine \cref{thm:omitted-carrier-curve,thm:logarithmic-support}.
\end{proof}

\begin{corollary}&#91;Euler--logarithmic flatness&#93;
\label{cor:euler-logarithmic-flatness}
Suppose the reduced branch divisor admits a logarithmic derivation
\(\delta\) whose zero locus is contained in the attained image \(F(X)\).
Then the finite cubic normalization is flat.

In particular, this holds if, in polynomial target coordinates
\(y_1,y_2,y_3\), a reduced branch equation is weighted homogeneous for
nonzero weights \(w_1,w_2,w_3\), the associated Euler field
\&#91;
 E=\sum_iw_i y_i\partial_{y_i}
\&#93;
has no zero except the origin, and \(0\in F(X)\).
\end{corollary}

\begin{proof}
The support is contained in the zero locus of every logarithmic derivation by
\cref{thm:logarithmic-support}, while attained points are excluded by
\cref{lem:attained-point-flatness}.
\end{proof}

\begin{corollary}&#91;Saito-matrix certificate&#93;
\label{cor:saito-matrix-certificate}
Assume the reduced branch germ is a free divisor and let \(M\) be a Saito
matrix whose columns form a basis of
\(\operatorname{Der}_{\C}(A)(-\log D_{\mathrm{br}})\).  Then
\&#91;
 \operatorname{Supp}\Delta(B/A)
 \subseteq V(I_1(M)),
\&#93;
where \(I_1(M)\) is the ideal generated by all entries of \(M\).  Thus the
entries of a Saito matrix give an exact symbolic flatness certificate.
\end{corollary}

\begin{proof}
The evaluation map of the logarithmic tangent module is zero exactly where
all coefficients of a basis vanish.  Apply \cref{thm:logarithmic-support}.
\end{proof}

\begin{remark}&#91;Cusp product&#93;
\label{ex:cusp-product-saito}
For the cusp-axis equation
\&#91;
 h=4p^3+27q^2
\&#93;
in coordinates \((p,q,c)\), the logarithmic fields
\&#91;
 \partial_c,\qquad
 2p\partial_p+3q\partial_q,\qquad
 9q\partial_p-2p^2\partial_q
\&#93;
have coefficient determinant \(-4p^3-27q^2=-h\).  They form a Saito basis
and \(I_1(M)=A\) because of the coefficient of \(\partial_c\).  Hence an
actual cusp product along a smooth axis cannot support a defect.  This does
not follow from a merely set-theoretic smooth singular axis: the product, or
an equivalent nonvanishing logarithmic field, is the essential hypothesis.
\end{remark}


\begin{remark}&#91;Alternative certificate for the announced cubic map&#93;
\label{rem:alpoge-euler-certificate}
For the announced map in \cref{cor:alpoge-equivariant-flatness}, the inverse
cubic has discriminant homogeneous for target weights \((-2,-1,1)\).  Its
Euler field vanishes only at the origin, and the origin is attained.  Thus
\cref{cor:euler-logarithmic-flatness} gives a second proof of flatness which
uses only the branch equation and not completeness of the
\(\mathbf G_m\)-action.
\end{remark}

\subsection{A divisorial pole filtration from the affine opening}

Retain the omitted-value setup of
\cref{thm:keller-picard-principal-parts}.  Put
\&#91;
 Z=\Spec B_y,
 \qquad U=\Spec S_A\subset Z,
 \qquad Z\setminus U=\bigcup_{i=1}^sD_i,
\&#93;
where the \(D_i\) are the prime boundary divisors.  For
\(\mathbf n=(n_1,\ldots,n_s)\in\mathbf N^s\), define the divisorial pole
module
\&#91;
 M(\mathbf n)=
 \Gamma\!\left(Z,\mathcal O_Z\!\left(\sum_i n_iD_i\right)\right)
 \subset\operatorname{Frac}(B_y).
\&#93;

\begin{theorem}&#91;Boundary pole-filtration criterion&#93;
\label{thm:boundary-pole-filtration}
The polynomial opening has the exact valuation filtration
\&#91;
 S_A=\bigcup_{\mathbf n\in\mathbf N^s}M(\mathbf n),
 \qquad
 P_y=S_A/B_y=
 \varinjlim_{\mathbf n}M(\mathbf n)/B_y.
\&#93;
Suppose that for every \(\mathbf n\in\mathbf N^s\) and every \(i\), the
finite \(A\)-module
\&#91;
 M(\mathbf n+\mathbf e_i)/M(\mathbf n)
\&#93;
has depth at least two at every point above \(\mathfrak m\).  Then
\&#91;
 \Delta_y=0,
\&#93;
so \(B_y\) is finite free over \(A\).
\end{theorem}

\begin{proof}
Since \(Z\) is normal, a rational function is regular on \(U\) exactly when
its valuation is nonnegative at every prime divisor not contained in
\(Z\setminus U\).  Its finitely many negative valuations along the \(D_i\)
are bounded by some \(\mathbf n\).  This proves the union and colimit.

Choose a monotone lattice path from \(\mathbf0\) to any \(\mathbf n\).  It
filters \(M(\mathbf n)/B_y\) by the displayed elementary pole quotients.  The
depth hypothesis makes \(H^0_{\mathfrak m}\) and
\(H^1_{\mathfrak m}\) vanish on every elementary quotient, hence on each
finite filtered quotient.  Local cohomology commutes with filtered colimits
(for example from its Cech-complex construction), so
\&#91;
 H^1_{\mathfrak m}(P_y)=0.
\&#93;
Now apply \cref{thm:keller-picard-principal-parts}.
\end{proof}


\begin{theorem}&#91;Finite pole-step defect certificate&#93;
\label{thm:finite-pole-step-certificate}
For \(\mathbf n\in\mathbf N^s\) and \(i\in\{1,\ldots,s\}\), put
\&#91;
 Q(\mathbf n,i)
 =M(\mathbf n+\mathbf e_i)/M(\mathbf n),
 \qquad
 \mathfrak D(\mathbf n,i)
 =\operatorname{Ext}^2_A(Q(\mathbf n,i),A).
\&#93;
After replacing \(A\) and the finite pole modules by their
\(\mathfrak m\)-adic completions, there are a multi-index
\(\mathbf n_*\) and a monotone lattice path
\&#91;
 \mathbf0=\mathbf n^{(0)},\mathbf n^{(1)},\ldots,
 \mathbf n^{(N)}=\mathbf n_*
\&#93;
such that \(\Delta_y\) is a subquotient of a finite iterated extension of
\&#91;
 \mathfrak D_j
 =\mathfrak D(\mathbf n^{(j-1)},i_j),
 \qquad
 \mathbf n^{(j)}-\mathbf n^{(j-1)}=\mathbf e_{i_j}.
\&#93;
In particular,
\&#91;
 \Delta_y\ne0
 \quad\Longrightarrow\quad
 \mathfrak D(\mathbf n,i)\ne0
\&#93;
for at least one finite pole step.

If, for such a pole step, \(\overline Q=Q/H^0_{\mathfrak m}(Q)\) is
Cohen--Macaulay on the punctured spectrum and has finite \(S_2\)-hull
\&#91;
 Q^\dagger=\Gamma(\Spec A\setminus\{\mathfrak m\},\widetilde{\overline Q}),
\&#93;
then
\&#91;
 0\longrightarrow\overline Q\longrightarrow Q^\dagger
 \longrightarrow H^1_{\mathfrak m}(Q)\longrightarrow0
\&#93;
and
\&#91;
 \boxed{
 \mathfrak D(\mathbf n,i)
 \simeq D_A(Q^\dagger/\overline Q).
 }
\&#93;
Thus every nonzero cubic defect admits a finite certificate made from explicit
surface \(S_2\)-hull discrepancies of elementary deleted-sheet pole steps.
\end{theorem}

\begin{proof}
Completion is faithfully flat, commutes with the finite modules in every
fixed pole step, and preserves both nonvanishing and length of the punctual
defect.  We therefore work over the completed regular local ring.  Put
\(P(\mathbf n)=M(\mathbf n)/B_y\).  Local cohomology commutes with the
directed colimit and
\&#91;
 H^1_{\mathfrak m}(P_y)=D_A\Delta_y
\&#93;
has finite length.  Choose finitely many generators and represent them at a
common stage \(\mathbf n_*\).  Then
\&#91;
 H^1_{\mathfrak m}(P(\mathbf n_*))
 \longrightarrow H^1_{\mathfrak m}(P_y)
\&#93;
is surjective.

Choose a monotone path to \(\mathbf n_*\).  At its \(j\)-th step there is an
exact sequence
\&#91;
 0\longrightarrow P(\mathbf n^{(j-1)})
 \longrightarrow P(\mathbf n^{(j)})
 \longrightarrow Q(\mathbf n^{(j-1)},i_j)
 \longrightarrow0.
\&#93;
The long local-cohomology sequence shows inductively that
\(H^1_{\mathfrak m}(P(\mathbf n_*))\) belongs to the Serre subcategory
generated by the finitely many modules
\(H^1_{\mathfrak m}(Q(\mathbf n^{(j-1)},i_j))\).  Its quotient
\(D_A\Delta_y\) does also.  Matlis duality is exact, and local duality over the
completed regular ring gives
\&#91;
 D_AH^1_{\mathfrak m}(Q(\mathbf n,i))
 \simeq\operatorname{Ext}^2_A(Q(\mathbf n,i),A).
\&#93;
This proves the finite subquotient assertion.

For the last statement, the standard punctured-spectrum local-cohomology
sequence is
\&#91;
 0\to H^0_{\mathfrak m}(Q)\to Q\to
 \Gamma(\Spec A\setminus\{\mathfrak m\},\widetilde Q)
 \to H^1_{\mathfrak m}(Q)\to0.
\&#93;
After quotienting by \(H^0_{\mathfrak m}(Q)\), the middle map is the inclusion
of \(\overline Q\) into its finite \(S_2\)-hull.  Dualize and apply local
duality.
\end{proof}

\begin{corollary}&#91;Minimal-defect boundary witness&#93;
\label{cor:minimal-defect-boundary-witness}
If \(\operatorname{length}_A\Delta_y=1\), then some finite elementary pole
step has nonzero surface-deficiency module
\&#91;
 \operatorname{Ext}^2_A
 \bigl(M(\mathbf n+\mathbf e_i)/M(\mathbf n),A\bigr).
\&#93;
Under the finite-hull hypotheses in
\cref{thm:finite-pole-step-certificate}, the corresponding hull discrepancy
has a nonzero residue at the closed fibre.  Hence a minimal defect cannot be
hidden only in the infinite tail of the pole filtration: it is witnessed at a
finite, explicitly computable deleted-sheet step.
\end{corollary}

\begin{corollary}&#91;Cartier--Cohen--Macaulay boundary flatness&#93;
\label{cor:cartier-CM-boundary-flatness}
Assume that, in a neighborhood of the finite fibre over \(y\), every prime
boundary component \(D_i\) is Cartier and Cohen--Macaulay.  Then
\&#91;
 \Delta_y=0.
\&#93;
It is enough that all \(D_i\) be Cartier and normal.  In particular, a simple
normal-crossings boundary on the finite normalization cannot support a cubic
flatness defect.
\end{corollary}

\begin{proof}
Every \(E_{\mathbf n}=\sum_jn_jD_j\) is Cartier.  For each \(i\) there is an
exact sequence
\&#91;
0\longrightarrow\mathcal O_Z(E_{\mathbf n})
\longrightarrow\mathcal O_Z(E_{\mathbf n}+D_i)
\longrightarrow
\mathcal O_{D_i}(E_{\mathbf n}+D_i)
\longrightarrow0.
\&#93;
The scheme \(Z\) is affine, so global sections identify the elementary pole
quotient with the module of sections of the invertible sheaf on the right.
A line bundle on a Cohen--Macaulay surface has depth two.  Since
\(D_i\to\Spec A\) is finite, the same depth is measured with respect to
\(\mathfrak m\).  Apply \cref{thm:boundary-pole-filtration}.  A normal
surface is Cohen--Macaulay, proving the second assertion.
\end{proof}


\begin{theorem}&#91;Tame boundary-Cartierization criterion&#93;
\label{thm:tame-boundary-cartierization}
Retain the local affine-opening setup of
\cref{thm:boundary-pole-filtration}.  Suppose there is a finite Galois
morphism
\&#91;
 g\colon Z'\longrightarrow Z
\&#93;
with group \(G\), where \(|G|\) is invertible, such that \(Z'\) is normal and
every prime component of
\&#91;
 D'=Z'\setminus g^{-1}(U)
\&#93;
is Cartier and Cohen--Macaulay.  Then \(B_y/A\) is finite flat.

In particular, a quotient-toroidal deleted boundary obtained from a
Cartier-normal boundary by a finite linearly reductive group cannot support a
Keller normalization defect.
\end{theorem}

\begin{proof}
For a Weil divisor \(E\) supported on \(D\), its divisorial module is recovered
from the Galois cover by
\&#91;
 \mathcal O_Z(E)
 =\left(g_*\mathcal O_{Z'}(g^*E)\right)^G.
\&#93;
Indeed, both sides consist of the invariant rational functions whose
valuations along every prime above \(D\) satisfy the same pulled-back
inequalities.  Since the prime components of \(D'\) are Cartier, every
\(g^*E\) is Cartier.

For an elementary increment \(E\mapsto E+D_i\), exactness of invariants gives
\&#91;
 \frac{\mathcal O_Z(E+D_i)}{\mathcal O_Z(E)}
 \simeq
 \left(
  g_*\frac{\mathcal O_{Z'}(g^*E+g^*D_i)}
               {\mathcal O_{Z'}(g^*E)}
 \right)^G.
\&#93;
Filter the quotient upstairs by adding, with multiplicity, the Cartier prime
components of \(g^*D_i\).  Every successive quotient is an invertible sheaf
on a Cohen--Macaulay surface, and therefore has target depth two.  The whole
upstairs quotient has depth two.  Its invariant part is an \(A\)-direct
summand by the Reynolds operator, so it also has depth at least two.  Apply
\cref{thm:boundary-pole-filtration}.
\end{proof}

\begin{corollary}&#91;Boundary-geometric support of every defect&#93;
\label{cor:defect-boundary-bad-locus}
Let \(D_i\) be the prime components of
\(\overline X\setminus X\).  Then
\&#91;
 \operatorname{Supp}\Delta_F\subseteq O_F\cap
 \pi\!\left(
  \bigcup_i\left(
   \operatorname{NonCartier}_{\overline X}(D_i)
   \cup\operatorname{NonCM}(D_i)
  \right)
 \right).
\&#93;
In particular, at a defect point at least one boundary component through the
normalization fibre is non-Cartier or nonnormal.  Thus every surviving defect
is forced simultaneously into the non-toroidal target locus and a special
failure of the actual deleted-sheet boundary.
\end{corollary}

\begin{proof}
If all boundary components through the fibre were Cartier and
Cohen--Macaulay, \cref{cor:cartier-CM-boundary-flatness} would eliminate the
defect.  The first containment also uses source splitting, which places the
defect over \(O_F\).  Finally, a normal surface is Cohen--Macaulay.
\end{proof}

\subsection{Cartier slices and the finite-flat surface hull}

Let the notation be as in \cref{thm:picard-lie-defect}.  Choose a regular
parameter \(t\in\mathfrak m\setminus\mathfrak m^2\), and put
\&#91;
\overline A=A/tA,
\qquad
C=B/tB,
\&#93;
and let \(x_C=V(\mathfrak mC)\).  Since \(B\) is torsion-free over \(A\),
\(t\) is \(B\)-regular.

\begin{theorem}&#91;Cartier-slice flat hull and defect reduction&#93;
\label{thm:cartier-slice-flat-hull}
Let
\&#91;
C^{\dagger}
 =\Gamma\bigl(\Spec C\setminus x_C,\mathcal O\bigr)
\&#93;
be the \(S_2\)-ification of \(C\).  Then:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item \(C\) is \(S_1\), is Cohen--Macaulay away from \(x_C\), and
      \(C^{\dagger}\) is a finite \(C\)-algebra;
\item \(C^{\dagger}\) is a finite free \(\overline A\)-algebra of the same
      generic rank as \(B/A\);
\item there is a canonical exact sequence
\&#91;
0\longrightarrow C\longrightarrow C^{\dagger}
 \longrightarrow H^1_{x_C}(C)\longrightarrow0;
\&#93;
\item Matlis duality over \(\overline A\) gives
\&#91;
\boxed{
D_{\overline A}(C^{\dagger}/C)
 \simeq \Delta(B/A)/t\Delta(B/A).
}
\&#93;
Consequently the following conditions are equivalent:
\begin{enumerate}&#91;label=(\alph*)&#93;
\item \(B\) is finite flat over \(A\);
\item \(C\) is Cohen--Macaulay for some regular parameter \(t\in\mathfrak m\setminus\mathfrak m^2\);
\item \(C\) is \(S_2\) for some regular parameter \(t\in\mathfrak m\setminus\mathfrak m^2\);
\item \(C=C^{\dagger}\) for some regular parameter \(t\in\mathfrak m\setminus\mathfrak m^2\);
\item the corresponding condition holds for every regular parameter
      \(t\in\mathfrak m\setminus\mathfrak m^2\).
\end{enumerate}
If \(C\) is \(R_1\), then \(C^{\dagger}\) is the normalization of \(C\).
\end{enumerate}
\end{theorem}

\begin{proof}
Normality gives \(\operatorname{depth}_A B\ge2\), so the regular element
\(t\) makes \(C\) an \(S_1\) ring.  Away from the closed fibre, \(B\) is
finite free over \(A\); hence \(C\) is Cohen--Macaulay away from \(x_C\).
For an excellent two-dimensional \(S_1\) ring whose failure of \(S_2\) is
zero-dimensional, the displayed ring of punctured regular functions is the
finite \(S_2\)-ification.  The local-cohomology sequence is therefore
\&#91;
0\to H^0_{x_C}(C)\to C\to C^{\dagger}
  \to H^1_{x_C}(C)\to0.
\&#93;
Here \(H^0_{x_C}(C)=0\), proving (i) and (iii).

The ring \(C^{\dagger}\) is \(S_2\) of pure dimension two, hence is
Cohen--Macaulay.  It is finite over the two-dimensional regular local ring
\(\overline A\), so miracle flatness makes it finite free, proving (ii).

The local-cohomology sequence of
\&#91;
0\longrightarrow B\xrightarrow{\ t\ }B\longrightarrow C\longrightarrow0
\&#93;
gives
\&#91;
H^1_{x_C}(C)=0:_{H^2_x(B)}t.
\&#93;
Dualizing and using \cref{thm:picard-lie-defect} yields
\&#91;
D_{\overline A}H^1_{x_C}(C)
 \simeq D_AH^2_x(B)/tD_AH^2_x(B)
 \simeq \Delta(B/A)/t\Delta(B/A),
\&#93;
which is (iv).  If the quotient vanishes for one \(t\in\mathfrak m\),
Nakayama's lemma gives \(\Delta(B/A)=0\); the equivalences now follow from
\cref{thm:picard-lie-defect}.  Finally, an \(S_2\), \(R_1\) finite birational
extension is normal, proving the last assertion.
\end{proof}

\begin{corollary}&#91;Minimal defects are elementary cubic pinchings&#93;
\label{cor:minimal-cubic-pinching}
Assume that \(k=\C\), that the closed fibre of \(C^{\dagger}\) is local, and
that
\&#91;
\Delta(B/A)\simeq k.
\&#93;
Then, for every regular parameter \(t\in\mathfrak m\setminus\mathfrak m^2\),
\&#91;
C^{\dagger}/C\simeq k,
\qquad
\dim_k(C/\mathfrak mC)=\operatorname{rank}_A B+1.
\&#93;
If the generic rank is three, write
\&#91;
V=C^{\dagger}/\mathfrak mC^{\dagger},
\qquad
W=C/\mathfrak mC^{\dagger}\subset V.
\&#93;
Then \(V\) is a local length-three \(k\)-algebra and \(W\) is a unital
codimension-one subalgebra.  Exactly one of the following occurs:
\begin{enumerate}&#91;label=(\alph*)&#93;
\item
\&#91;
V\simeq k&#91;\epsilon&#93;/(\epsilon^3),
\qquad
W=k\oplus k\epsilon^2;
\&#93;
\item
\&#91;
V\simeq k\oplus M,
\qquad M^2=0,
\qquad
W=k\oplus\ell
\&#93;
for a line \(\ell\subset M\).
\end{enumerate}
Thus every transverse surface slice of a minimal cubic defect is obtained by
pinching one codimension-one subalgebra in the special fibre of a finite-flat
cubic surface algebra.  Its scheme-theoretic fibre has length four.
\end{corollary}

\begin{proof}
Since \(t\in\mathfrak m\) kills the residue field,
\cref{thm:cartier-slice-flat-hull}(iv) gives
\(C^{\dagger}/C\simeq k\).  This quotient is annihilated by
\(\mathfrak m\), so \(\mathfrak mC^{\dagger}\subset C\) and \(W\subset V\)
is a unital codimension-one subalgebra.  Tensoring
\&#91;
0\to C\to C^{\dagger}\to k\to0
\&#93;
with \(k\) over the two-dimensional regular local ring \(\overline A\)
gives
\&#91;
0\to\operatorname{Tor}^{\overline A}_1(k,k)
 \to C/\mathfrak mC\to V\to k\to0.
\&#93;
Since \(\dim_k\operatorname{Tor}_1^{\overline A}(k,k)=2\), the fibre length
is \(2+\operatorname{rank}_A B-1=\operatorname{rank}_A B+1\).

A local commutative length-three algebra has either one-dimensional maximal
ideal modulo its square, in which case it is \(k&#91;\epsilon&#93;/(\epsilon^3)\),
or two-dimensional maximal ideal, in which case that ideal has square zero.
In the first case closure under multiplication forces the unique
codimension-one unital subalgebra to be \(k\oplus k\epsilon^2\).  In the
second case every line in the square-zero maximal ideal gives, and exhausts,
a codimension-one unital subalgebra.
\end{proof}

\begin{definition}&#91;The split principal-parts class&#93;
\label{def:split-principal-parts}
Let \((A,\mathfrak m)\) be a regular local ring of dimension three.  Let
\(\mathscr P_A\) be the smallest class of \(A\)-modules that
\begin{enumerate}&#91;label=(\alph*)&#93;
\item contains every module \(N_f/N\), where \(N\) is a finite free
      \(A\)-module and \(0\ne f\in\mathfrak m\);
\item is closed under finite extensions, direct summands, and filtered
      colimits.
\end{enumerate}
\end{definition}

\begin{theorem}&#91;Split principal-parts flatness criterion&#93;
\label{thm:split-principal-parts-flatness}
In the setup of \cref{thm:keller-picard-principal-parts}, if
\&#91;
P_y=S_A/B_y\in\mathscr P_A,
\&#93;
then the finite normalization is flat over \(y\).
\end{theorem}

\begin{proof}
For \(Q=N_f/N\) as in \cref{def:split-principal-parts}, the modules \(N\)
and \(N_f\) satisfy
\&#91;
H^0_{\mathfrak m}(N)=H^1_{\mathfrak m}(N)=H^2_{\mathfrak m}(N)=0,
\qquad
H^i_{\mathfrak m}(N_f)=0\ \text{for all }i.
\&#93;
The long exact sequence therefore gives
\&#91;
H^0_{\mathfrak m}(Q)=H^1_{\mathfrak m}(Q)=0.
\&#93;
The simultaneous vanishing of \(H^0\) and \(H^1\) is preserved under finite
extensions and direct summands.  Local cohomology is computed by a finite
\v Cech complex and hence commutes with filtered colimits.  Therefore every
module in \(\mathscr P_A\) has vanishing first local cohomology.  Apply
\cref{thm:keller-picard-principal-parts}.
\end{proof}

\begin{remark}&#91;What the affine opening contributes&#93;
\label{rem:affine-opening-contribution}
The abstract resolvent pair \((Q,L)\) detects the local Ext class but does not
remember which principal parts are allowed by the polynomial source.  The
module \(P_y=S_A/B_y\) records exactly that information.  Thus the most
direct Keller-specific target is the concrete vanishing
\&#91;
H^1_{\mathfrak m_y}(S_A/B_y)=0.
\&#93;
Theorem~\ref{thm:split-principal-parts-flatness} makes one usable version of
that target precise: derive from the actual \(U_1,U_2,B\) deleted sheets a
filtration built from principal localizations of finite free \emph{target}
modules.  Freeness over the target, not merely over the normalization, is the
essential hypothesis.
\end{remark}

\subsection{Kummer-toroidal flatness}

\begin{definition}&#91;Kummer-trivializable boundary&#93;
\label{def:kummer-trivializable}
Let \((A,\mathfrak m)\) be a regular local \(\C\)-algebra and let \(B\) be a
finite normal \(A\)-algebra, generically \'{e}tale.  We say that \(B/A\) is
\emph{Kummer-trivializable at \(\mathfrak m\)} if, after strict
Henselization, there are parameters \(x_1,\ldots,x_r\), an integer \(N&gt;0\),
and the regular finite free extension
\&#91;
A'=A&#91;t_1,\ldots,t_r&#93;/(t_1^N-x_1,\ldots,t_r^N-x_r)
\&#93;
localized at its closed point, such that the normalization of \(A'\) in the
compositum with a Galois closure of \(\operatorname{Frac}B/\operatorname{Frac}A\)
is finite \'{e}tale over \(A'\).
\end{definition}

\begin{theorem}&#91;Kummer-toroidal flatness&#93;
\label{thm:kummer-toroidal-flatness}
If \(B/A\) is Kummer-trivializable, then \(B\) is finite free over \(A\).
\end{theorem}

\begin{proof}
Flatness is \'{e}tale-local and descends under faithful flatness, so work over
the strict Henselization.  Let \(L/K\) be a finite Galois closure and let
\(T\) be the normalization of \(A\) in \(L\).  Let \(K'=\operatorname{Frac}A'\),
\(M=LK'\), and let \(T'\) be the normalization of \(A'\) in \(M\).  By
hypothesis \(T'/A'\) is finite \'{e}tale.  Since \(A'\) is strictly
Henselian,
\&#91;
T'\simeq (A')^{\oplus s}
\&#93;
for some \(s\); in particular \(T'\) is finite free over \(A\).

Let \(H=\operatorname{Gal}(M/L)\).  The group \(H\) preserves \(A'\) and
\(T'\), and
\&#91;
T=(T')^H.
\&#93;
Indeed, the invariant fraction field is \(L\), and invariants in \(T'\) are
integral over \(A\).  Reynolds averaging makes \(T\) an \(A\)-direct summand
of \(T'\), so \(T\) is finite projective, hence free.  The original normal
algebra \(B\) is a product of invariant intermediate algebras \(T^J\); each
is again a Reynolds direct summand of \(T\) and is therefore free over the
local ring \(A\).
\end{proof}

\begin{corollary}&#91;Tame normal-crossings flatness&#93;
\label{cor:normal-crossings-flatness}
Let \((A,\mathfrak m)\) be a regular local \(\C\)-algebra and let \(B\) be a
finite normal \(A\)-algebra, generically \'{e}tale.  Suppose there is a normal
crossings divisor \(D\subset\Spec A\) such that the cover is finite
\'{e}tale over \(\Spec A\setminus D\).  Then \(B\) is finite free over
\(A\).
\end{corollary}

\begin{proof}
After strict Henselization, \(D\) is cut out by part of a regular system of
parameters.  Characteristic zero makes all divisorial ramification tame.
The normal-crossings form of Abhyankar's lemma
(SGA~1, Exp.~XIII, Prop.~5.2) says that adjoining sufficiently divisible
roots of these parameters makes the normalized Galois pullback unramified in
codimension one.  Purity of the branch locus makes it finite \'{e}tale.
Thus the cover is Kummer-trivializable, and
\cref{thm:kummer-toroidal-flatness} applies.
\end{proof}

\begin{corollary}&#91;Normal-crossings exclusion for Keller defects&#93;
\label{cor:keller-normal-crossings-exclusion}
Let \(F:\A^3\to\A^3\) be a generically finite complex Keller map and let
\(S_F\) be its reduced nonproperness set.  If, near \(y\), the set \(S_F\)
is a normal crossings divisor, then the finite normalization is flat over
\(y\).

For a generic-degree-three map with canonical defect \(\Delta_F\),
\&#91;
\boxed{
\operatorname{Supp}\Delta_F
 \subseteq O_F\cap\operatorname{NonNC}(S_F),
}
\&#93;
where \(\operatorname{NonNC}(S_F)\) is the locus at which the reduced
nonproperness divisor is not normal crossings.  In particular, smooth points
and ordinary transverse crossing points cannot support a defect.
\end{corollary}

\begin{proof}
Outside \(S_F\), the finite normalization agrees with the finite \'{e}tale
cover supplied by the Keller map.  Apply
\cref{cor:normal-crossings-flatness}.  The support inclusion also uses source
splitting, which places every nonflat point among the omitted values.
\end{proof}

\subsection{The klt quadratic-resolvent exclusion}

Assume now the local cubic \(S_3\)-resolvent setup.  Let \(A\) be a complete
regular local \(\C\)-algebra of dimension three, let \(T\) be the normal
\(S_3\)-Galois closure, put
\&#91;
Q=T^{A_3},\qquad B=T^{C_2},
\&#93;
and assume, as supplied by the corrected divisorial classification, that
\(T\to Q\) is \'{e}tale in codimension one.

\begin{theorem}&#91;Klt-resolvent flatness&#93;
\label{thm:klt-resolvent-flatness}
If \(Q\) is klt, then \(B\) is finite free over \(A\).  Since \(Q\) is a
Gorenstein hypersurface, it is enough that \(Q\) be canonical; in particular,
a compound Du Val quadratic-resolvent germ cannot support a defect.
\end{theorem}

\begin{proof}
The finite morphism \(\Spec T\to\Spec Q\) is quasi-\'{e}tale.  The finite-cover
discrepancy formula preserves klt singularities under such a cover, so \(T\)
is klt.  Klt singularities over \(\C\) are rational and therefore
Cohen--Macaulay.  A system of parameters of \(A\) is consequently
\(T\)-regular, and Auslander--Buchsbaum makes \(T\) free over \(A\).
Finally, \(B=T^{C_2}\) is a Reynolds direct summand of \(T\), hence is free.
\end{proof}

\begin{corollary}&#91;Branch-pair threshold&#93;
\label{cor:branch-pair-threshold}
Write the normal quadratic resolvent as
\&#91;
Q=A&#91;w&#93;/(w^2-d)
\&#93;
with reduced divisorial branch \(D=V(d)\).  If
\&#91;
(\Spec A,\tfrac12D)
\&#93;
is klt at \(y\), then the cubic normalization is flat at \(y\).  Hence a
defect forces
\&#91;
\operatorname{lct}_y(D)\le\frac12.
\&#93;
\end{corollary}

\begin{proof}
The double-cover canonical-divisor formula is
\&#91;
K_Q=\pi^*(K_{\Spec A}+\tfrac12D).
\&#93;
Thus the displayed pair is klt exactly when the normal double cover is klt.
Apply \cref{thm:klt-resolvent-flatness}.
\end{proof}

\subsection{The minimal Galois Picard representation}

Let \(V\) denote the standard two-dimensional representation of \(S_3\), and
let \(E\) be the rank-two trace-zero summand of \(B=A\oplus E\).

\begin{proposition}&#91;Standard-isotypic Picard tangent&#93;
\label{prop:standard-picard-tangent}
There is an \(A&#91;S_3&#93;\)-module decomposition
\&#91;
T\simeq A\oplus A_{\mathrm{sgn}}\oplus(E\otimes_\C V).
\&#93;
Consequently
\&#91;
\operatorname{Lie}\mathbf{Pic}^{\mathrm{loc},\circ}(t,\Spec T)
 \simeq D_A\operatorname{Ext}^1_A(E,A)\otimes_\C V.
\&#93;
If the cubic defect has length one, then the Galois local Picard identity
component is a two-dimensional connected commutative algebraic group with
standard \(S_3\)-tangent representation.  It is necessarily one of:
\begin{enumerate}&#91;label=(\alph*)&#93;
\item \(\mathbf G_a^2\), with the standard linear action;
\item a two-dimensional algebraic torus with its rank-two \(S_3\)-lattice;
\item an abelian surface carrying an \(S_3\)-action whose tangent
      representation is standard.
\end{enumerate}
\end{proposition}

\begin{proof}
The trivial isotypic summand of \(T\) is \(A=T^{S_3}\).  The sign summand is
the trace-zero part of \(Q=T^{A_3}\); as a rank-one reflexive module over the
regular local UFD \(A\), it is free.  Write the standard isotypic part as
\(M\otimes V\).  Taking invariants under a transposition gives
\&#91;
B=T^{C_2}\simeq A\oplus M,
\&#93;
so \(M\simeq E\).  Applying \(\operatorname{Ext}^1_A(-,A)\) and local
duality gives the tangent representation.

In the length-one case this tangent representation is irreducible.  The
maximal connected linear subgroup in Chevalley's decomposition, and within
it the unipotent radical, are characteristic and therefore \(S_3\)-stable.
Their tangent spaces must consequently have dimension zero or two.  Thus the
group is either entirely abelian, entirely unipotent, or a torus.  Over
characteristic zero a two-dimensional connected commutative unipotent group
is \(\mathbf G_a^2\), giving the list.
\end{proof}

\subsection{The collision \v{C}ech saturation criterion}

The polynomial affine opening supplies a second exact model of the defect.
Instead of studying one cubic normalization in isolation, pass to its
\(S_3\)-Galois closure and cover the attained part by the three conjugate
source charts.  The resulting \v{C}ech cohomology records precisely the
failure of the three retained-root charts to glue through the omitted set.
Its punctual standard-isotypic part is the cubic flatness defect.

\begin{lemma}&#91;Divided-difference collision idempotent&#93;
\label{lem:collision-idempotent}
Let
\&#91;
 F=(F_1,F_2,F_3):X=\Spec S=\A^3_\C\longrightarrow
 Y=\Spec R=\A^3_\C
\&#93;
be a Keller map with constant Jacobian determinant \(c\in\C^*\).  In
independent source coordinates \(\mathbf x=(x_1,x_2,x_3)\) and
\(\mathbf x'=(x'_1,x'_2,x'_3)\), choose a polynomial divided-difference
matrix \(M(\mathbf x,\mathbf x')\) satisfying
\&#91;
 F(\mathbf x)-F(\mathbf x')
 =M(\mathbf x,\mathbf x')(\mathbf x-\mathbf x').
\&#93;
Put \(q=\det M\).  In
\&#91;
 A_2=S\otimes_R S=\mathcal O(X\times_YX)
\&#93;
one has
\&#91;
 q(q-c)=0.
\&#93;
Consequently
\&#91;
 e_\Delta=\frac qc\in A_2
\&#93;
is an idempotent, and there is a canonical product decomposition
\&#91;
 \boxed{
 S\otimes_RS\simeq S\times C_2,
 \qquad
 C_2=(1-e_\Delta)(S\otimes_RS).
 }
\&#93;
The first factor is the diagonal.  The second factor is the coordinate ring
of the off-diagonal collision space
\&#91;
 W=(X\times_YX)\setminus\Delta_X.
\&#93;
It is a smooth affine threefold, \(W\to X\) is \'{e}tale, and, when the
generic cubic has \(S_3\)-Galois closure \(\widetilde K\), \(W\) is integral
with function field \(\widetilde K\).

In the triple fibre product, let \(e_{ij}\) be the pullback of
\(e_\Delta\) from factors \(i,j\).  Then
\&#91;
 e_{\mathrm{dist}}
 =(1-e_{12})(1-e_{13})(1-e_{23})
\&#93;
is the idempotent cutting out the affine scheme of ordered, pairwise-distinct
source triples in one fibre.
\end{lemma}

\begin{proof}
Write \(\delta=\mathbf x-\mathbf x'\).  In \(A_2\), the fibre equations give
\&#91;
 M\delta=0.
\&#93;
Multiplication by the adjugate matrix gives
\&#91;
 q\delta=0.
\&#93;
On the diagonal, \(M(\mathbf x,\mathbf x)=JF(\mathbf x)\), so
\(q|_\Delta=c\).  Hence there are polynomials \(a_i\) with
\&#91;
 q-c=\sum_i a_i\delta_i.
\&#93;
It follows in \(A_2\) that
\&#91;
 q(q-c)=\sum_i a_iq\delta_i=0,
\&#93;
which proves idempotence.  The resulting idempotent is independent of the
chosen divided-difference matrix, since it is characterized as the unique
idempotent whose factor is the diagonal component.

Moreover \(e_\Delta\delta_i=0\).  Thus the two copies of \(S\) coincide in
\(e_\Delta A_2\), and multiplication along the diagonal identifies this
factor with \(S\).  The complementary idempotent gives \(C_2\).  Since
\(X\times_YX\to X\) is a base change of the \'{e}tale morphism \(F\), both
open-and-closed factors are \'{e}tale over \(X\); in particular \(W\) is
smooth and affine.  Generically, for an irreducible cubic with Galois group
\(S_3\),
\&#91;
 K(X)\otimes_{K(Y)}K(X)
 \simeq K(X)\times\widetilde K.
\&#93;
Therefore the off-diagonal generic algebra is the field \(\widetilde K\).
Every nonempty component of an \'{e}tale scheme over the integral scheme
\(X\) dominates \(X\), so \(W\) is integral.  The assertion for three
factors follows by multiplying the three commuting complementary diagonal
idempotents.
\end{proof}

Now let \(F\) have generic degree three and generic Galois group \(S_3\).
Fix an omitted value \(y\), put
\&#91;
 A=\mathcal O_{Y,y},\qquad S_A=S\otimes_RA,
\&#93;
and let \(T\) be the normalization of \(A\) in the Galois closure
\(\widetilde K\).  Label the three transposition subgroups by
\(H_1,H_2,H_3\), put
\&#91;
 B_i=T^{H_i},
\&#93;
and let \(S_i\subset\operatorname{Frac}(B_i)\) be the corresponding
Galois-conjugate affine source algebra.  Thus every \(S_i\) is an
\(A\)-algebra isomorphic to \(S_A\), and
\(\Spec S_i\hookrightarrow\Spec B_i\) is the conjugate source opening.
Define affine opens of \(\mathcal T=\Spec T\) by
\&#91;
 \mathcal U_i
 =\mathcal T\times_{\Spec B_i}\Spec S_i.
\&#93;
Let
\&#91;
 Y_A^{\mathrm{att}}=F(X)\cap\Spec A,
 \qquad
 \mathcal V=\mathcal T\times_{\Spec A}Y_A^{\mathrm{att}}.
\&#93;
Then
\&#91;
 \mathcal V=\mathcal U_1\cup\mathcal U_2\cup\mathcal U_3.
\&#93;
All nonempty intersections are affine.  After choosing the labelling above,
the pair intersections are conjugate copies of the off-diagonal collision
space in \cref{lem:collision-idempotent}; the triple intersection is the
pairwise-distinct ordered-triple component.

Let
\&#91;
 C^0_y=\bigoplus_i\Gamma(\mathcal U_i,\mathcal O),
 \qquad
 C^1_y=\bigoplus_{i&lt;j}
       \Gamma(\mathcal U_i\cap\mathcal U_j,\mathcal O),
 \qquad
 C^2_y=\Gamma(\mathcal U_1\cap\mathcal U_2\cap\mathcal U_3,\mathcal O),
\&#93;
with the usual alternating \v{C}ech differentials
\&#91;
 C^0_y\xrightarrow{d_0}C^1_y\xrightarrow{d_1}C^2_y.
\&#93;
Put
\&#91;
 \mathcal H_y=H^1(C^\bullet_y),
 \qquad
 K_y=\ker d_1,
 \qquad
 I_y=\operatorname{im}d_0.
\&#93;
The permutation of the three source charts makes this an
\(S_3\)-equivariant complex.

\begin{theorem}&#91;Collision saturation realizes the cubic defect&#93;
\label{thm:collision-cech-saturation}
Let
\&#91;
 \Delta_y=\operatorname{Ext}^1_A(B_1,A)
\&#93;
be the cubic flatness defect.  Let \(V_{\mathrm{std}}\) denote the standard
two-dimensional complex representation of \(S_3\).  There is a canonical
\(A&#91;S_3&#93;\)-module isomorphism
\&#91;
 \boxed{
 H^0_{\mathfrak m_y}(\mathcal H_y)
 \simeq D_A\Delta_y\otimes_\C V_{\mathrm{std}}.
 }
\&#93;
Equivalently, define the closed-point saturation
\&#91;
 I_y^{\mathrm{sat}}
 =I_y:_{K_y}\mathfrak m_y^\infty
 =\{u\in K_y:\mathfrak m_y^Nu\subseteq I_y
                    \text{ for some }N\}.
\&#93;
Then
\&#91;
 \boxed{
 I_y^{\mathrm{sat}}/I_y
 \simeq D_A\Delta_y\otimes_\C V_{\mathrm{std}}.
 }
\&#93;
In particular:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item the cubic normalization is flat over \(y\) if and only if
\&#91;
 I_y^{\mathrm{sat}}=I_y;
\&#93;
\item
\&#91;
 \operatorname{length}_A(I_y^{\mathrm{sat}}/I_y)
 =2\operatorname{length}_A\Delta_y;
\&#93;
\item a nonzero defect is exactly an embedded closed-point,
standard-isotypic submodule of the collision \v{C}ech cohomology; the
one-dimensional generic cohomology along an omitted carrier curve is not by
itself a flatness defect.
\end{enumerate}
\end{theorem}

\begin{proof}
First note that every \(\mathcal U_i\) is affine and finite flat of rank two
over \(\Spec S_i\).  Indeed,
\&#91;
 T_i=T\otimes_{B_i}S_i
\&#93;
is an open base change of the normal algebra \(T\), hence is normal, and it
is finite of generic rank two over \(S_i\).  The quadratic trace splitting
writes \(T_i\simeq S_i\oplus N_i\), where \(N_i\) is rank-one
reflexive.  The ring \(S_i\) is a localization of a polynomial ring and is
factorial, so \(N_i\simeq S_i\).  Thus \(T_i\) is finite free of rank
two.

The equality \(\mathcal V=\bigcup_i\mathcal U_i\) follows from Galois
transitivity.  If a target point is attained, choose a retained source point
and a point of \(\mathcal T\) above it.  Every other point of the Galois fibre
is a translate of this point and hence belongs to one of the three conjugate
source opens.  The converse is immediate.  Since \(\mathcal T\) is separated,
all finite intersections of these affine opens are affine.

For \(i\ne j\), the two quotient maps induce a finite morphism
\&#91;
 \mathcal U_i\cap\mathcal U_j
 \longrightarrow
 (\Spec S_i\times_{\Spec A}\Spec S_j)_{\mathrm{off}}.
\&#93;
Both sides are normal: the right side is an open-and-closed factor of an
\'{e}tale fibre product, and the left side is open in the normal scheme
\(\mathcal T\).  Their generic algebras are both \(\widetilde K\), so the
map is finite birational and hence an isomorphism.  The identical argument
with three quotient maps identifies the triple intersection with the
pairwise-distinct ordered-triple component.  Therefore the above
\v{C}ech complex computes
\&#91;
 \mathcal H_y\simeq H^1(\mathcal V,\mathcal O_{\mathcal V}).
\&#93;

Let
\&#91;
 Z=\mathcal T\setminus\mathcal V.
\&#93;
The omitted set has codimension at least two, and the finite morphism
\(\mathcal T\to\Spec A\) preserves this codimension bound.  Since \(T\) is
normal, hence \(S_2\),
\&#91;
 H_Z^0(T)=H_Z^1(T)=0.
\&#93;
The local-cohomology sequence for
\(\mathcal V=\mathcal T\setminus Z\) gives
\&#91;
 H^1(\mathcal V,\mathcal O_{\mathcal V})\simeq H_Z^2(T).
\&#93;
Because \(y\) is omitted, the closed fibre
\(V(\mathfrak m_yT)\) is contained in \(Z\).  The spectral sequence for
local cohomology with nested supports,
\&#91;
 H^p_{\mathfrak m_y}\bigl(H_Z^q(T)\bigr)
 \Longrightarrow H^{p+q}_{\mathfrak m_y}(T),
\&#93;
and the preceding vanishing give a canonical isomorphism
\&#91;
 H^0_{\mathfrak m_y}(\mathcal H_y)
 \simeq H^2_{\mathfrak m_y}(T).
\&#93;

Because \(6\) is invertible, the \(S_3\)-representation on \(T\) splits
isotypically.  As in \cref{prop:standard-picard-tangent},
\&#91;
 T\simeq A\oplus A_{\mathrm{sgn}}
       \oplus(E\otimes_\C V_{\mathrm{std}}),
\&#93;
where \(A_{\mathrm{sgn}}\) is free of rank one and
\(B_1\simeq A\oplus E\).  Since \(A\) is regular of dimension three,
\&#91;
 H^2_{\mathfrak m_y}(A)
 =H^2_{\mathfrak m_y}(A_{\mathrm{sgn}})=0.
\&#93;
Local duality therefore yields
\&#91;
 H^2_{\mathfrak m_y}(T)
 \simeq H^2_{\mathfrak m_y}(E)\otimes_\C V_{\mathrm{std}}
 \simeq D_A\operatorname{Ext}^1_A(E,A)
           \otimes_\C V_{\mathrm{std}}
 \simeq D_A\Delta_y\otimes_\C V_{\mathrm{std}}.
\&#93;
This proves the first boxed isomorphism.

Finally,
\&#91;
 H^0_{\mathfrak m_y}(K_y/I_y)
 =\frac{I_y:_{K_y}\mathfrak m_y^\infty}{I_y},
\&#93;
which proves the saturation statement.  Matlis duality preserves length, and
\(\dim_\C V_{\mathrm{std}}=2\), giving (i)--(iii).
\end{proof}


\begin{theorem}&#91;Flat collision presentation and Tor signature&#93;
\label{thm:collision-flat-presentation}
Retain the notation of \cref{thm:collision-cech-saturation}, and suppose that
an omitted curve passes through \(y\).  This hypothesis is automatic if
\(\Delta_y\ne0\).  Then:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item
\&#91;
 H^2(\mathcal V,\mathcal O_{\mathcal V})=0,
\&#93;
so the last \v{C}ech differential
\&#91;
 d_1:C^1_y\longrightarrow C^2_y
\&#93;
is surjective;
\item every term \(C^j_y\) is flat over \(A\), and
\&#91;
 \mathfrak m_y C^j_y=C^j_y;
\&#93;
\item the module
\&#91;
 K_y=\ker(d_1)
\&#93;
is flat over \(A\), and there is an exact collision presentation
\&#91;
 0\longrightarrow T\longrightarrow C^0_y
 \xrightarrow{\ d_0\ }K_y
 \longrightarrow\mathcal H_y\longrightarrow0;
\&#93;
\item in the derived category of \(k(y)\)-vector spaces there is a canonical
isomorphism
\&#91;
 \mathcal H_y\otimes_A^{\mathbf L}k(y)
 \simeq
 \bigl(T\otimes_A^{\mathbf L}k(y)\bigr)&#91;2&#93;.
\&#93;
Equivalently,
\&#91;
 \operatorname{Tor}^A_i(\mathcal H_y,k(y))=0
 \quad(i=0,1),
\&#93;
and, for \(i\ge2\),
\&#91;
 \boxed{
 \operatorname{Tor}^A_i(\mathcal H_y,k(y))
 \simeq
 \operatorname{Tor}^A_{i-2}(T,k(y)).
 }
\&#93;
\end{enumerate}
If the trace-zero cubic module has a minimal presentation
\&#91;
 0\longrightarrow A^b\longrightarrow A^{b+2}\longrightarrow E\longrightarrow0,
\&#93;
then
\&#91;
 \dim_k\operatorname{Tor}^A_2(\mathcal H_y,k)=2b+6,
 \qquad
 \dim_k\operatorname{Tor}^A_3(\mathcal H_y,k)=2b,
\&#93;
and all higher Tor groups vanish.  In the first possible defect stratum
\(b=1\), the collision signature is therefore
\&#91;
 (\beta_2,\beta_3)=(8,2).
\&#93;
\end{theorem}

\begin{proof}
Let \(Z=\mathcal T\setminus\mathcal V\).  At every maximal ideal
\(\mathfrak q\subset T\) above \(\mathfrak m_y\), going down supplies a
height-two prime below \(\mathfrak q\) lying over the omitted carrier curve.
Thus
\&#91;
 \dim\bigl(\operatorname{Supp}(T_{\mathfrak q}/I_ZT_{\mathfrak q})\bigr)
 \ge1.
\&#93;
Hartshorne--Lichtenbaum vanishing, after completion if necessary, gives
\&#91;
 H^3_{ZT_{\mathfrak q}}(T_{\mathfrak q})=0.
\&#93;
Hence \(H^3_Z(T)=0\), and the affine-complement local-cohomology sequence
identifies
\&#91;
 H^2(\mathcal V,\mathcal O_{\mathcal V})\simeq H^3_Z(T)=0.
\&#93;
The \v{C}ech complex therefore has surjective last differential.  See Stacks
Project, Proposition~51.16.6,
Tag~\href{https://stacks.math.columbia.edu/tag/0EB6}{0EB6}.

Each \(S_i\) is an \(A\)-flat algebra because it is obtained by base change
from the \'{e}tale source map.  As observed in the proof of
\cref{thm:collision-cech-saturation}, the coordinate ring of
\(\mathcal U_i\) is finite free over \(S_i\).  Pair and triple intersections
are open-and-closed components of iterated base changes of the source
\'{e}tale morphism, hence are also \(A\)-flat.  Since \(y\) is omitted,
\(\mathfrak m_yS_i=S_i\), and the same equality holds for all the displayed
coordinate rings.  This proves (ii).

Now
\&#91;
 0\longrightarrow K_y\longrightarrow C^1_y
 \xrightarrow{d_1}C^2_y\longrightarrow0
\&#93;
is exact with the last two modules flat.  The long Tor sequence makes
\(K_y\) flat.  Normality of \(T\) and
\(\operatorname{codim}_{\mathcal T}Z\ge2\) give
\(\Gamma(\mathcal V,\mathcal O)=T\), so the augmented \v{C}ech complex gives
(iii).

The flat complex \(C^\bullet_y\) has cohomology only
\&#91;
 H^0(C^\bullet_y)=T,
 \qquad
 H^1(C^\bullet_y)=\mathcal H_y.
\&#93;
Termwise tensoring it with \(k(y)\) gives the zero complex because
\(\mathfrak m_yC^j_y=C^j_y\).  The truncation triangle therefore yields
\&#91;
 \mathcal H_y\otimes_A^{\mathbf L}k(y)
 \simeq
 \bigl(T\otimes_A^{\mathbf L}k(y)\bigr)&#91;2&#93;,
\&#93;
which proves (iv).

Finally,
\&#91;
 T\simeq A\oplus A_{\mathrm{sgn}}
       \oplus(E\otimes_\C V_{\mathrm{std}}).
\&#93;
The two one-dimensional isotypic summands are free, while
\(E\otimes V_{\mathrm{std}}\) is two copies of \(E\) as an \(A\)-module.
Thus
\&#91;
 \dim_k(T/\mathfrak mT)=2+2(b+2)=2b+6,
 \qquad
 \dim_k\operatorname{Tor}_1^A(T,k)=2b.
\&#93;
Since \(\operatorname{pd}_AT\le1\), there are no further Tor groups.
\end{proof}

\begin{corollary}&#91;Minimal collision witness&#93;
\label{cor:minimal-collision-witness}
If \(\operatorname{length}_A\Delta_y=1\), then
\&#91;
 I_y^{\mathrm{sat}}/I_y\simeq V_{\mathrm{std}}
\&#93;
as an \(S_3\)-representation; in particular it is killed by
\(\mathfrak m_y\) and has complex dimension two.  Thus the first possible
cubic defect has a unique representation-theoretic signature in the
collision complex.
\end{corollary}

\begin{corollary}&#91;Collision-purity flatness criterion&#93;
\label{cor:collision-purity-flatness}
The cubic normalization is flat over \(y\) whenever the collision cohomology
\(\mathcal H_y\) has no nonzero submodule supported at the closed point.
Equivalently, it is enough to prove that the image of \(d_0\) is
\(\mathfrak m_y\)-saturated in \(\ker d_1\).

Together with \cref{thm:finite-pole-step-certificate}, any failure of this
saturation is detected after finitely many deleted-sheet pole steps.  Hence
the remaining Lane~1 calculation can be organized as a finite saturation
certificate on the explicit pair- and triple-collision rings.
\end{corollary}



\begin{corollary}&#91;Collision-product flatness&#93;
\label{cor:collision-product-flatness}
Assume that, after completion at \(y\), there are a complete two-dimensional
local \(\C\)-algebra \(T_0\), affine opens \(U_{1,0},U_{2,0},U_{3,0}\), and
a regular parameter \(t\in\mathfrak m_y\) for which the Galois opening is a
formal product:
\&#91;
 \widehat T\simeq T_0&#91;&#91;t&#93;&#93;,
 \qquad
 \widehat{\mathcal U_i}\simeq U_{i,0}\widehat\times\operatorname{Spf}\C&#91;&#91;t&#93;&#93;,
\&#93;
compatibly on every pair and triple intersection.  Then the finite cubic
normalization is flat over \(y\).
\end{corollary}

\begin{proof}
The product vector field \(\partial_t\) preserves all three completed source
charts and every pair and triple intersection.  It therefore acts by a
connection on the collision \v{C}ech complex and on its first cohomology.
The closed-point submodule
\(H^0_{\mathfrak m_y}(\mathcal H_y)\) is stable under this connection.
Since \(\partial_t\) is nonzero at the closed point,
\cref{lem:no-punctual-transverse-connection} makes this finite-length
submodule zero.  Apply \cref{thm:collision-cech-saturation} and descend
flatness from the completion.
\end{proof}

\begin{corollary}&#91;The standard triple-root collision is saturated&#93;
\label{cor:standard-root-collision-saturated}
Let
\&#91;
 T=\C&#91;&#91;r_1,r_2,r_3&#93;&#93;
\&#93;
be the ordered-root algebra over the symmetric invariant ring, and let
\(\mathcal U_i\) be the locus on which the \(i\)-th root is simple.  Then
the collision saturation quotient is zero.

More explicitly, with
\&#91;
 u=r_1-r_2,\qquad v=r_2-r_3,
\&#93;
the three opens are
\&#91;
 D\bigl(u(u+v)\bigr),\qquad D(uv),\qquad D\bigl(v(u+v)\bigr),
\&#93;
and their complement has ideal
\&#91;
 \bigl(u(u+v),uv,v(u+v)\bigr)
 =(u^2,uv,v^2)=(u,v)^2.
\&#93;
The first collision cohomology is therefore the transverse local-cohomology
module \(H^2_{(u,v)}(T)\).  A third parameter along the triple-root curve
acts injectively, so this module has no closed-point submodule.
\end{corollary}

\begin{proof}
The ideal identity is immediate by subtracting the middle generator from the
first and third.  The three-open \v{C}ech complex computes local cohomology
with support in its radical \((u,v)\).  Writing
\&#91;
 T\simeq\C&#91;&#91;u,v&#93;&#93;&#91;&#91;t&#93;&#93;
\&#93;
for a parameter \(t\) along the common-root curve shows that
\&#91;
 H^2_{(u,v)}(T)
 \simeq H^2_{(u,v)}(\C&#91;&#91;u,v&#93;&#93;)\widehat\otimes_\C\C&#91;&#91;t&#93;&#93;.
\&#93;
Multiplication by \(t\) is injective.  Now apply
\cref{cor:collision-product-flatness}.
\end{proof}

\subsection{A sharp theorem-facing reduction}

\begin{theorem}&#91;Lane~1 flatness exclusion theorem&#93;
\label{thm:lane-one-flatness-exclusion}
Let \(F:\A^3_\C\to\A^3_\C\) be a generic-degree-three Keller map, and let
\(y\) be an omitted value.  Each of the following conditions is sufficient
for flatness of the finite cubic normalization over \(y\):
\begin{enumerate}&#91;label=(\roman*)&#93;
\item every completed local normalization ring above \(y\) is
      \(\mathbf Q\)-factorial;
\item every such completed local class group is countable or finitely
      generated;
\item the reduced nonproperness divisor is normal crossings near \(y\);
\item the cover is Kummer-trivializable near \(y\);
\item the quadratic resolvent is klt (equivalently, in the Gorenstein case,
      canonical);
\item the branch pair \((\Spec A,\tfrac12D)\) is klt;
\item one smooth target Cartier surface section through \(y\), cut by a
      regular parameter, is \(S_2\) (equivalently, Cohen--Macaulay);
\item every elementary quotient in the actual divisorial boundary pole
      filtration has depth at least two;
\item every prime component of the normalization boundary over \(y\) is
      Cartier and Cohen--Macaulay (in particular, Cartier and normal);
\item the deleted boundary becomes Cartier with Cohen--Macaulay prime
      components on a finite Galois cover of order invertible in \(\C\);
\item the boundary principal-parts module \(S_A/B_y\) belongs to
      \(\mathscr P_A\);
\item the cokernel
\&#91;
\Pic^{\mathrm{Zar-loc}}\longrightarrow\Pic^{\mathrm{et-loc}}
\&#93;
is countable;
\item a connected algebraic symmetry group of \(F\) has every target fixed
      point in \(F(X)\); in particular, \(F\) is equivariant for a weighted
      \(\mathbf G_m\)-action with no zero target weight;
\item the reduced divisorial branch locus admits a logarithmic derivation
      nonzero at \(y\); in particular, its completed germ is a formal product
      with a smooth curve through \(y\);
\item the omitted set has no one-dimensional irreducible component; in
      particular, the reduced nonproperness surface is normal, or its singular
      locus is zero-dimensional;
\item in the collision \v{C}ech complex of
      \cref{thm:collision-cech-saturation}, the image of \(d_0\) is
      \(\mathfrak m_y\)-saturated in \(\ker d_1\), equivalently the
      collision cohomology has no nonzero closed-point submodule.
\end{enumerate}

Conversely, if a nonzero defect \(\Delta_y\) exists, then:
\begin{enumerate}&#91;label=(\alph*)&#93;
\item
\&#91;
D_A\Delta_y
 \simeq H^1_{\mathfrak m_y}(S_A/B_y)
 \simeq\operatorname{Lie}\mathbf{Pic}^{\mathrm{loc}}(x_y,\Spec B_y);
\&#93;
\item the defect length is the dimension of the local Picard identity
      component;
\item the completed local class group at some point above \(y\) is
      uncountable, contains elements of infinite order, and is not torsion;
      in particular that completion is not \(\mathbf Q\)-factorial;
\item the ordinary-to-completed class-group map has uncountable cokernel;
\item the nonproperness boundary is not normal crossings and the cover is not
      Kummer-trivializable;
\item the quadratic resolvent is not klt, and its reduced branch divisor has
      local log-canonical threshold at most \(1/2\);
\item every smooth target Cartier surface section through \(y\), cut by a
      regular parameter, fails \(S_2\); its
      finite-flat \(S_2\)-hull has pinching quotient Matlis dual to
      \(\Delta_y/t\Delta_y\);
\item \(S_A/B_y\notin\mathscr P_A\);
\item at least one prime deleted-sheet boundary component through the fibre is
      non-Cartier or non-Cohen--Macaulay; in particular it is non-Cartier or
      nonnormal;
\item no finite linearly reductive boundary cover simultaneously Cartierizes
      the deleted components and makes their prime pullbacks
      Cohen--Macaulay;
\item \(y\) lies in the logarithmic zero locus of the reduced divisorial
      branch locus; in particular, the branch germ is not formally a product
      along the omitted carrier curve at \(y\);
\item some finite elementary deleted-sheet pole step has nonzero deficiency
      module
      \&#91;
      \operatorname{Ext}^2_A
      \bigl(M(\mathbf n+\mathbf e_i)/M(\mathbf n),A\bigr);
      \&#93;
\item the point \(y\) is fixed by every connected algebraic symmetry group
      of \(F\);
\item an entire omitted curve passes through \(y\), and a height-two singular
      prime of the quadratic resolvent above that curve carries a nonzero
      class in \(\Cl(-)&#91;3&#93;\);
\item the collision saturation quotient is nonzero and has the exact
      standard-isotypic form
      \&#91;
      I_y^{\mathrm{sat}}/I_y
       \simeq D_A\Delta_y\otimes_\C V_{\mathrm{std}},
      \&#93;
      of length \(2\operatorname{length}_A\Delta_y\).
\end{enumerate}
\end{theorem}

\begin{proof}
The sufficient conditions are
\cref{cor:analytic-qfactorial-flatness,cor:keller-normal-crossings-exclusion,thm:kummer-toroidal-flatness,thm:klt-resolvent-flatness,cor:branch-pair-threshold,thm:cartier-slice-flat-hull,thm:boundary-pole-filtration,cor:cartier-CM-boundary-flatness,thm:tame-boundary-cartierization,thm:split-principal-parts-flatness,thm:etale-boundary-algebraization,thm:connected-symmetry-support,thm:logarithmic-support,thm:omitted-carrier-curve,cor:collision-purity-flatness}.
The necessary conclusions are their contrapositives together with
\cref{thm:picard-lie-defect,thm:completed-class-group-jump,thm:keller-picard-principal-parts,thm:cartier-slice-flat-hull,cor:defect-boundary-bad-locus,thm:finite-pole-step-certificate,thm:connected-symmetry-support,thm:logarithmic-support,thm:omitted-carrier-curve,thm:collision-cech-saturation}.
\end{proof}

\begin{corollary}&#91;Geometric intersection supporting every cubic defect&#93;
\label{cor:cubic-defect-support-intersection}
Let \(\operatorname{Curv}(O_F)\) be the union of the one-dimensional
components of the omitted set, let \(\operatorname{NonNC}(S_F)\) be the
non-normal-crossings locus of the reduced nonproperness divisor, and put
\&#91;
 \operatorname{Bad}_{\partial}
 =\bigcup_i\left(
   \operatorname{NonCartier}_{\overline X}(D_i)
   \cup\operatorname{NonCM}(D_i)
  \right).
\&#93;
Let \(\operatorname{NonKLT}(Q/Y)\) denote the target points above which some
quadratic-resolvent germ is not klt, and let
\(Z_{\log}(D_{\mathrm{br}})\) be the logarithmic zero locus of the reduced
divisorial branch locus of the finite normalization.  If \(G\) is any
connected algebraic symmetry group of \(F\), then
\&#91;
\boxed{
 \operatorname{Supp}\Delta_F
 \subseteq
 \operatorname{Curv}(O_F)
 \cap\operatorname{NonNC}(S_F)
 \cap\pi(\operatorname{Bad}_{\partial})
 \cap\operatorname{NonKLT}(Q/Y)
 \cap Z_{\log}(D_{\mathrm{br}})
 \cap Y^G.
}
\&#93;
Thus a defect is forced into the simultaneous intersection of six visibly
special loci: an omitted curve, a non-toroidal target boundary point, a bad
prime component of the actual deleted boundary, a non-klt quadratic
resolvent, a zero-dimensional logarithmic branch stratum, and the fixed locus
of every connected symmetry.
\end{corollary}

\begin{proof}
Combine
\cref{thm:omitted-carrier-curve,cor:keller-normal-crossings-exclusion,cor:defect-boundary-bad-locus,thm:klt-resolvent-flatness,thm:logarithmic-support,thm:connected-symmetry-support}.
\end{proof}

\begin{remark}&#91;What remains&#93;
\label{rem:lane-one-status-after-formal-picard}
The theorem is a strong exclusion result, not an unconditional proof of cubic
flatness.  It replaces an unspecified isolated defect by a concrete and
highly constrained object: a positive-dimensional formal Picard component
whose tangent is the local cohomology of the actual polynomial boundary
principal parts.  A surviving example must simultaneously exhibit a
completion class-group jump, a non-Kummer boundary interaction, and a
non-klt quadratic-resolvent branch pair.

The most direct remaining route is now a collision saturation calculation.
Construct the pair- and triple-collision rings using
\cref{lem:collision-idempotent}, form the three-chart \v{C}ech maps, and prove
\&#91;
 (\operatorname{im}d_0:_{\ker d_1}\mathfrak m_y^\infty)
 =\operatorname{im}d_0.
\&#93;
A failure has a forced standard \(S_3\)-signature and length exactly twice
the cubic defect.  Formal constancy of the complete collision opening along
the carrier curve already makes the saturation automatic; the universal
triple-root arrangement is the basic example.  By the pole-filtration theorem
this calculation is still finite: at a point in the logarithmic zero locus,
compute the
surface-deficiency modules
\&#91;
 \operatorname{Ext}^2_A
 \bigl(M(\mathbf n+\mathbf e_i)/M(\mathbf n),A\bigr)
\&#93;
for the finitely many pole steps supplied by
\cref{thm:finite-pole-step-certificate}.  Showing that their relevant
subquotient vanishes closes Lane~1 at the chosen omitted value.  Equivalently,
one may place the complete principal-parts module in \(\mathscr P_A\), or
prove directly that the Henselian local class group is torsion or countable.

Finite flatness and recovery of the affine opening remain separate gates.
\end{remark}
</code></pre>

<a id="source-d8d50dd353502656"></a>

## `research-notes/lane1-collision-saturation-20260803-v2/manifest.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "packet_id": "lane1-collision-saturation-full-proof-20260803-v2",
  "created_on": "2026-08-03",
  "source_patch": "research-notes/lane1-collision-saturation-20260802-v1/lane1-collision-v8.patch",
  "source_patch_sha256": "c75c4b57613ee97abede503e725276f46c3bfd94ef05da580eab392957672302",
  "file": {
    "path": "flatness-defect-repairs-full.tex",
    "byte_count": 85987,
    "line_count": 2336,
    "sha256": "4b468e00f6c83f158c89e90a8819858b91a1d1f4dfd7c582915204236efdb60c"
  },
  "theorem_label": "thm:collision-cech-saturation",
  "does_not_establish": &#91;
    "independent verification of the supplied proof",
    "flatness for every cubic Keller normalization"
  &#93;
}
</code></pre>

<a id="source-aef55c7c330abe18"></a>

## `research-notes/lane1-models-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 1 explicit models and homogeneous gate

This versioned packet records three separate pieces of reusable mathematics:

- an exact marked-root benchmark whose finite completion is flat and whose closed-point collision-saturation quotient vanishes;
- an elliptic-cone example showing that normal cubic data, source splitting, and transverse \(A_2\) carriers do not by themselves force the collision quotient to vanish; and
- the smooth homogeneous one-generator reduction, its surviving type-IV triple-plane family, and an explicit type-IV test object.

The latter two are not polynomial Keller maps. They are boundary and necessity tests for the Lane 1 problem.

## Exact sources

- `explicit-marked-root-benchmark.tex`
- `explicit-marked-root-collision-saturation.tex`
- `elliptic-cone-negative-model.md`
- `TYPEIV_GATE.md`

The Python files replay the polynomial, matrix-factorization, conductor, branch, cusp, and collision identities. The immutable replay record is `/path/to/versioned-artifact`.

## Literature input

The type-IV identification uses D. Faenzi, F. Polizzi, and J. Vallès, *Triple planes with \(p_g=q=0\)*, especially Proposition 3.7 and Proposition 2.4, together with R. Miranda, *Triple covers in algebraic geometry* for the cubic-cover construction.

## Scope boundary

The explicit marked-root benchmark proves vanishing only for that completed family. The elliptic and type-IV cones are not Keller realizations. The type-IV reduction assumes that the projectivized cubic cover is smooth; singular projectivizations require a separate analysis.
</code></pre>

<a id="source-69caa73289f1610d"></a>

## `research-notes/lane1-models-20260803-v1/TYPEIV_GATE.md`

<pre><code class="language-markdown">
# Smooth homogeneous one-generator defects and the type-IV gate

Work over \(\mathbf C\). Let \(A=\mathbf C&#91;a,b,c&#93;\) with its standard grading and suppose a connected normal graded cubic \(A\)-algebra has trace decomposition

\&#91;
B=A\oplus M
\&#93;

and a one-generator defect supported at \((a,b,c)\). After a linear change of target variables, assume

\&#91;
0\longrightarrow A(-d)
\xrightarrow{(a,b,c)^t}
A(1-d)^3\longrightarrow M\longrightarrow0.
\tag{1}
\&#93;

This note isolates what follows from (1), what comes from the classification of smooth triple planes, and what the explicit calculation proves. None of the projective or conical examples below is asserted to be a polynomial Keller map.

## 1. The smooth projective reduction

Sheafifying (1) gives

\&#91;
\widetilde M\simeq T_{\mathbf P^2}(-d)
\simeq\Omega^1_{\mathbf P^2}(3-d).
\tag{2}
\&#93;

If \(f:X\to\mathbf P^2\) is the corresponding smooth projectivized cubic cover, then

\&#91;
f_*\mathcal O_X
=\mathcal O_{\mathbf P^2}\oplus\Omega^1_{\mathbf P^2}(3-d).
\&#93;

Consequently

\&#91;
q(X)=
\begin{cases}
1,&amp;d=3,\\
0,&amp;d\ne3,
\end{cases}
\qquad
p_g(X)=h^0\!\left(\mathbf P^2,T_{\mathbf P^2}(d-6)\right).
\&#93;

The cubic building-section space vanishes for \(d&lt;3\), while \(p_g(X)&gt;0\) for \(d\ge5\). If the normalized affine cone over \((X,H=f^*\mathcal O(1))\) contained a dense open \(\mathbf A^3\), then \(\mathbf C(X)(t)\) would be rational, so the smooth projective surface \(X\) would be stably rational. The stable-birational invariance of \(p_g\) and \(q\) therefore leaves exactly

\&#91;
\boxed{d=4}
\&#93;

among smooth projectivized one-generator defects.

This conclusion does not cover singular projectivizations unless their resolutions preserve the required trace-free cohomology, for example under suitable rational-singularity hypotheses.

## 2. Identification with type IV

For \(d=4\), the trace-zero bundle is \(T_{\mathbf P^2}(-4)\). The classification of smooth general triple planes identifies this case with type IV. The source surface is

\&#91;
X=\operatorname{Bl}_{Z}\check{\mathbf P}^{\,2},
\qquad
H=4L-\sum_{i=1}^{13}E_i,
\tag{3}
\&#93;

where \(Z\) is the length-13 zero scheme of a section of
\(T_{\check{\mathbf P}^{\,2}}(2)\). In particular

\&#91;
H^2=3,\quad
K_X=-3L+\sum E_i,\quad
R_f=K_X+3H=9L-2\sum E_i,
\&#93;

and

\&#91;
K_X^2=-4,\quad H\cdot K_X=1,\quad
H\cdot R_f=10,\quad R_f^2=29,\quad g(R_f)=15.
\tag{4}
\&#93;

The classification and cusp count are the literature inputs: Faenzi--Polizzi--Vallès, Proposition 3.7 and Proposition 2.4, using Miranda's construction of triple covers. The formulas in (3)--(4) are direct intersection calculations.

## 3. An explicit type-IV net

In homogeneous coordinates \(&#91;x:y:z&#93;\), take

\&#91;
\begin{aligned}
P&amp;=x^3+2y^3+3z^3+xyz+y^2z,\\
Q&amp;=2x^3-y^3+z^3+x^2z+xy^2,\\
R&amp;=x^3+y^3-2z^3+xz^2+yz^2+x^2y.
\end{aligned}
\&#93;

The cross-product quartics

\&#91;
(q_1,q_2,q_3)=(yR-zQ,\ zP-xR,\ xQ-yP)
\&#93;

define a rational map \(\mathbf P^2\dashrightarrow\mathbf P^2\). The exact checker proves:

1. their projective base scheme is reduced of length \(13\) and has no point on \(z=0\);
2. after blowing up those points, no target fibre contains a curve and no exceptional divisor is contracted;
3. the resulting morphism is finite flat of degree \(3\);
4. the source-plane ramification polynomial has degree \(9\) and is irreducible over \(\mathbf Q\);
5. the target branch polynomial has degree \(10\), is irreducible over \(\mathbf Q\), and has a Jacobian scheme of length \(42\) on \(21\) geometric support points;
6. at each support point the quadratic term is nonzero and the local Jacobian length is \(2\), hence every singularity is an ordinary \(A_2\) cusp.

The complete equations are in
`typeiv-explicit-net-data.json`; `verify_typeiv_explicit_net.py`
reconstructs them instead of trusting the stored file.

## 4. The cone defect and the resolvent module

Let \(B=\bigoplus_{n\ge0}H^0(X,\mathcal O_X(nH))\). Its trace-zero summand has the graded presentation

\&#91;
0\longrightarrow A(-4)
\xrightarrow{(a,b,c)^t}
A(-3)^3\longrightarrow M\longrightarrow0.
\tag{5}
\&#93;

Dualizing (5) gives

\&#91;
\operatorname{Ext}^1_A(B,A)
\simeq A/(a,b,c)(4).
\tag{6}
\&#93;

Thus the cone has a length-one finite defect at its vertex and its closed fibre has scheme length \(4\). Its quadratic resolvent is

\&#91;
Q_{\mathrm{res}}
=\mathbf Q&#91;a,b,c,\rho&#93;/(\rho^2+3\mathcal B),
\tag{7}
\&#93;

where \(\mathcal B\) is the branch decic. The \(21\) cusps cone to \(21\) height-two singular lines. Transversely (7) is \(UV=v^3\), so each line has local class group \(\mathbf Z/3\), and the two cubic eigensheaves give the two nonzero classes.

The Hessian checker constructs a \(3\times3\) matrix \(W\), a row \(r\), and \(v=(a,b,c)^t\) satisfying

\&#91;
Wv=0,\qquad
W^2+3\mathcal B I_3=vr,\qquad
rW=0,\qquad
rv=3\mathcal B.
\tag{8}
\&#93;

It then verifies the \(4\times4\) matrix factorization

\&#91;
\Phi=
\begin{pmatrix}
\rho I_3-W&amp;v\\
-r&amp;\rho
\end{pmatrix},
\qquad
\Psi=
\begin{pmatrix}
\rho I_3+W&amp;-v\\
r&amp;\rho
\end{pmatrix},
\&#93;

\&#91;
\Phi\Psi=\Psi\Phi=(\rho^2+3\mathcal B)I_4.
\tag{9}
\&#93;

Therefore \(\operatorname{coker}\Phi\) is a rank-two maximal Cohen--Macaulay module through the cone vertex. Projection to the \(3\times3\) Hessian eigensheaf gives an extension by the residue-field module at the vertex. The same calculation recovers the universal ordered-root conductor and Kähler different on the punctured cubic cover, and computes the normalization-index Fitting ideal as

\&#91;
\operatorname{Fitt}_0(T/C)=\mathcal B\,(a,b,c).
\tag{10}
\&#93;

Equations (8)--(10) are exact identities. They do not supply the three affine source openings needed to define the Keller collision Čech quotient.

## 5. Two Keller-specific rejection tests

First, no grading-invariant open of the punctured cone is \(\mathbf A^3\). Such an open has a fixed-point-free \(\mathbf G_m\)-action, so its compactly supported Euler characteristic is zero, whereas \(e_c(\mathbf A^3)=1\).

Second, let \(F:\mathbf A^3\to\mathbf A^3\) be a polynomial map with \(\det JF=c\ne0\). The target Euler field has the polynomial lift

\&#91;
D=(JF)^{-1}F,\qquad D(F_i)=F_i,\qquad\operatorname{div}D=3.
\tag{11}
\&#93;

If \(0\notin F(\mathbf A^3)\), then \(D\) is nowhere zero. It cannot be locally finite: otherwise its locally nilpotent Jordan part vanishes on the finite separable extension \(\mathbf C(x_1,x_2,x_3)/\mathbf C(F_1,F_2,F_3)\), so \(D\) is semisimple and integrates to an algebraic torus action on \(\mathbf A^3\). Torus localization gives a fixed point, where \(D\) vanishes, a contradiction.

Thus a type-IV Keller realization, if one exists, needs a genuinely non-grading-invariant affine opening and a nowhere-zero, divergence-three, non-locally-finite Euler lift.

## 6. What remains open

For the explicit type-IV cone, the following are still unavailable:

- a polynomial Keller realization;
- a non-grading-invariant affine open isomorphic to \(\mathbf A^3\);
- three conjugate source charts and their exact Čech gluing;
- the full conductor and different at the vertex in the eigensheaf presentation; and
- the collision-saturation quotient for an actual Keller opening.

The explicit cone is therefore a fixed equation-level test object and a sharp homogeneous gate, not a solution of the general Lane 1 flatness problem.
</code></pre>

<a id="source-ecb5fca02f9c9fd5"></a>

## `research-notes/lane1-models-20260803-v1/elliptic-cone-negative-model.md`

<pre><code class="language-markdown">
# P1-T1 research attempt: an elliptic-cone model with nonzero standard saturation

## Status

This note constructs a **complete negative local model in the category of normal
finite \(S_3\)-algebras with three conjugate affine simple-root charts**.
It has

\&#91;
I^{\mathrm{sat}}/I\cong V_{\mathrm{std}}\neq 0,
\qquad
\Delta_B\cong \mathbf C,
\&#93;

and supplies the cubic algebra, its \(S_3\)-Galois closure, multiplication,
involutions, source-base-change splitting, quadratic resolvent, singular
height-two primes, eigensheaf, and local class vector.

It is **not** a Keller counterexample: the affine source chart constructed below
is smooth and étale over its image but is not identified with \(\mathbf A^3\),
and no polynomial coordinate system with constant Jacobian is supplied.
Consequently, the construction shows that the normal \(S_3\) algebra and
source-splitting identities alone do not force saturation. Any proof for Keller
maps must use genuinely global \(\mathbf A^3\) input.

---

## 1. The ordered-root surface

Let

\&#91;
E=V(x^3+y^3+z^3)\subset \mathbf P^2_{\mathbf C}
\&#93;

be the Fermat cubic, with a flex chosen as the origin \(0_E\). Then
\(\mathcal O_E(1)\simeq \mathcal O_E(3\cdot 0_E)\), and the dual plane

\&#91;
Y=|\mathcal O_E(1)|\simeq \mathbf P^2
\&#93;

parametrizes line sections of \(E\).

Define

\&#91;
Z=\{(p_1,p_2,p_3)\in E^3:p_1+p_2+p_3=0_E\}.
\&#93;

The map \((p_1,p_2)\mapsto(p_1,p_2,-p_1-p_2)\) identifies \(Z\) with the
abelian surface \(E^2\). The group \(G=S_3\) acts by permuting the three
coordinates. Sending an ordered triple to its line section gives a finite
quotient map

\&#91;
\pi:Z\longrightarrow Z/S_3=Y.
\&#93;

Indeed, an effective divisor \(p_1+p_2+p_3\) is cut by a line precisely when it
is linearly equivalent to \(3\cdot0_E\), equivalently when
\(p_1+p_2+p_3=0_E\).

Let \(H_i\leq S_3\) be the transposition subgroup stabilizing the label \(i\).
Then

\&#91;
X_i:=Z/H_i
\&#93;

is the marked-root incidence surface

\&#91;
X_i\simeq\{(p,\ell)\in E\times Y:p\in \ell\}.
\&#93;

It is a \(\mathbf P^1\)-bundle over \(E\), hence smooth, and the map
\(f_i:X_i\to Y\) is finite flat of degree three.

Put \(M=\pi^*\mathcal O_Y(1)\), and form the full section rings

\&#91;
A_0=\bigoplus_{n\geq0}H^0(Y,\mathcal O_Y(n))=\mathbf C&#91;a,b,c&#93;,
\&#93;

\&#91;
T_0=\bigoplus_{n\geq0}H^0(Z,M^n),
\qquad
B_{i,0}=T_0^{H_i},
\qquad
Q_0=T_0^{A_3}.
\&#93;

These are finite normal graded \(A_0\)-algebras, with generic ranks
\(6,3,2\), respectively, and

\&#91;
T_0^{S_3}=A_0.
\&#93;

Normality follows because the full section ring of a Cartier divisor on a
normal variety is an intersection of the corresponding divisorial valuation
rings inside \(\mathbf C(Z)&#91;t,t^{-1}&#93;\).

Let \(\mathfrak m=(a,b,c)\), let \(\mathfrak n=T_{0,+}\), and complete the
localizations at the cone vertices:

\&#91;
A=\widehat{(A_0)_{\mathfrak m}}\simeq\mathbf C&#91;&#91;a,b,c&#93;&#93;,
\quad
T=\widehat{(T_0)_{\mathfrak n}},
\quad
B_i=T^{H_i},
\quad
Q=T^{A_3}.
\&#93;

The generic extension \(\operatorname{Frac}(T)/\operatorname{Frac}(A)\) is
Galois with group \(S_3\), and \(B_i\) is the corresponding non-Galois cubic
subalgebra.

---

## 2. The cubic algebra and its minimal defect

Let \(X=X_i\), \(f=f_i\). The incidence divisor in \(E\times Y\) is cut by the
universal section of
\(\mathcal O_E(1)\boxtimes\mathcal O_Y(1)\), so

\&#91;
0\to
\mathcal O_E(-1)\boxtimes\mathcal O_Y(-1)
\to\mathcal O_{E\times Y}
\to\mathcal O_X\to0.
\&#93;

Push forward to \(Y\). Since

\&#91;
h^0(E,\mathcal O_E(-1))=0,
\quad
h^1(E,\mathcal O_E(-1))=3,
\quad
h^0(E,\mathcal O_E)=h^1(E,\mathcal O_E)=1,
\&#93;

and \(f\) is finite, the resulting exact sequence is

\&#91;
0\to\mathcal O_Y\to f_*\mathcal O_X
\to\mathcal O_Y(-1)^3\xrightarrow{(a,b,c)}\mathcal O_Y\to0.
\&#93;

The kernel of the displayed Euler map is \(\Omega_Y^1\). The trace splits the
unit inclusion, hence

\&#91;
f_*\mathcal O_X\simeq\mathcal O_Y\oplus\Omega_Y^1.
\&#93;

Consequently, as a graded \(A_0\)-module,

\&#91;
B_{i,0}\simeq A_0\oplus N,
\qquad
N=\bigoplus_{n\geq0}H^0(Y,\Omega_Y^1(n)).
\&#93;

The Euler sequence identifies

\&#91;
N=\ker\bigl(A_0(-1)^3\xrightarrow{(a,b,c)}A_0\bigr)
  =\Omega^2_{A_0}(\mathbf C),
\&#93;

and the Koszul complex gives the minimal presentation

\&#91;
0\to A_0(-3)\longrightarrow A_0(-2)^3\longrightarrow N\to0.
\&#93;

After completion and forgetting grading, the trace-zero module \(E_i\) of
\(B_i=A\oplus E_i\) therefore has a presentation

\&#91;
0\to A\xrightarrow{\Phi}A^3\to E_i\to0,
\&#93;

where, after choosing a Koszul basis, \(\Phi\) is a column formed by the regular
parameters \(a,b,c\). Dualizing gives

\&#91;
\operatorname{Ext}^1_A(E_i,A)
 \simeq A/(a,b,c)\simeq\mathbf C.
\&#93;

Thus

\&#91;
\boxed{\Delta_{B_i}=\operatorname{Ext}^1_A(B_i,A)\simeq\mathbf C.}
\&#93;

This is the one-generator defect stratum. In particular,

\&#91;
\dim_{\mathbf C}(B_i/\mathfrak mB_i)=4,
\&#93;

and the trace-zero part of the closed fibre is a three-dimensional square-zero
ideal. The algebra is free away from the vertex and is nonflat only there.

The multiplication is not being specified by an abstract module ansatz. It is
the ordinary section-ring multiplication. Equivalently, if

\&#91;
0\to K\to H^0(E,\mathcal O_E(1))\otimes\mathcal O_E
   \xrightarrow{\mathrm{ev}}\mathcal O_E(1)\to0,
\&#93;

then the marked-root affine incidence space is the total space of \(K\), and

\&#91;
B_{i,0}=\Gamma\bigl(E,\operatorname{Sym}K^\vee\bigr)
\&#93;

with its usual symmetric-algebra multiplication. This gives a complete,
algorithmic algebra definition.

---

## 3. Equivariant decomposition and the quadratic resolvent

The generic fibre of \(\pi_*\mathcal O_Z\) is the regular representation of
\(S_3\). Equivariant idempotents split it as

\&#91;
\pi_*\mathcal O_Z
\simeq
\mathcal O_Y\otimes\mathbf 1
\oplus \mathcal F_{\mathrm{sgn}}\otimes\mathrm{sgn}
\oplus \Omega_Y^1\otimes V_{\mathrm{std}}.
\&#93;

The standard multiplicity bundle is \(\Omega_Y^1\) because taking
\(H_i\)-invariants must recover
\(\mathcal O_Y\oplus\Omega_Y^1\).

The quotient \(Z/A_3\to Y\) is a double cover branched along the dual sextic
\(E^\vee\). Hence

\&#91;
\mathcal F_{\mathrm{sgn}}\simeq\mathcal O_Y(-3).
\&#93;

For the Fermat cubic, the dual sextic has equation

\&#91;
d(a,b,c)=a^6+b^6+c^6
 -2a^3b^3-2a^3c^3-2b^3c^3.
\&#93;

Indeed, the tangent line at \(&#91;x:y:z&#93;\in E\) has dual coordinates
\(&#91;x^2:y^2:z^2&#93;\), and

\&#91;
d(x^2,y^2,z^2)=
(x^3-y^3-z^3)(x^3-y^3+z^3)
(x^3+y^3-z^3)(x^3+y^3+z^3).
\&#93;

Therefore

\&#91;
\boxed{Q\simeq A&#91;w&#93;/(w^2-d),}
\&#93;

up to rescaling \(w\) by a unit.

As an \(A_0&#91;S_3&#93;\)-module,

\&#91;
T_0\simeq
A_0\otimes\mathbf1
\oplus A_0(-3)\otimes\mathrm{sgn}
\oplus N\otimes V_{\mathrm{std}}.
\&#93;

Restricting \(V_{\mathrm{std}}\) to \(A_3=C_3\) gives the two nontrivial
characters \(\chi,\chi^{-1}\). Thus

\&#91;
T=Q\oplus L\oplus L^{&#91;2&#93;},
\qquad
L^{&#91;3&#93;}\simeq Q,
\&#93;

where, as an \(A\)-module, each of \(L,L^{&#91;2&#93;}\) is isomorphic to the completed
module \(N\). In particular,

\&#91;
0\to A\to A^3\to L\to0,
\qquad
\operatorname{Ext}^1_A(L,A)\simeq\mathbf C,
\&#93;

so \(L\) has depth two and is not maximal Cohen--Macaulay over \(Q\).
A transposition interchanges \(L\) and \(L^{&#91;2&#93;}\), giving
\(\sigma^*L\simeq L^\vee\).

### The nine singular curves

The derivatives of \(d\) are

\&#91;
\begin{aligned}
 d_a&amp;=6a^2(a^3-b^3-c^3),\\
 d_b&amp;=-6b^2(a^3-b^3+c^3),\\
 d_c&amp;=-6c^2(a^3+b^3-c^3).
\end{aligned}
\&#93;

The projective singular points of \(E^\vee\) are

\&#91;
&#91;1:\rho:0&#93;,\quad&#91;1:0:\rho&#93;,\quad&#91;0:1:\rho&#93;,
\qquad \rho^3=1.
\&#93;

Hence the height-two singular primes of the completed threefold \(Q\) are

\&#91;
\begin{aligned}
\mathfrak p_{ab,\rho}&amp;=(w,c,b-\rho a),\\
\mathfrak p_{ac,\rho}&amp;=(w,b,c-\rho a),\\
\mathfrak p_{bc,\rho}&amp;=(w,a,c-\rho b),
\end{aligned}
\qquad \rho^3=1.
\&#93;

At the generic point of each curve the transverse equation is \(A_2\): after
choosing a unit parameter along the curve, the branch equation begins with
\(9u^2-4v^3\), so the double cover is analytically equivalent to

\&#91;
UV-v^3=0.
\&#93;

The \(A_3\)-fixed points on \(Z\) are the nine triples \((p,p,p)\) with
\(3p=0_E\). On the tangent plane, a generator of \(A_3\) has eigenvalues
\(\zeta,\zeta^{-1}\). Thus the two eigensheaves localize to the two nonzero
classes of

\&#91;
\operatorname{Cl}(A_2)\simeq\mathbf Z/3.
\&#93;

After choosing the \(\chi\)-orientation consistently, the local class vector is

\&#91;
\boxed{(&#91;L_{\mathfrak p}&#93;)_{\mathfrak p}=(1,1,1,1,1,1,1,1,1)
\in(\mathbf Z/3)^9,}
\&#93;

while \(L^{&#91;2&#93;}\) has the negative vector.

The extension \(T/Q\) is unramified in codimension one: the fixed locus of
\(A_3\) on \(Z\) is finite, so on the affine cone it consists of the nine
height-two curves above.

---

## 4. Three conjugate affine source charts

Write

\&#91;
\Delta_{ij}=\{p_i=p_j\}\subset Z.
\&#93;

For the chart in which root \(i\) is marked, ramification occurs exactly when
that root collides with one of the other two. Define

\&#91;
D_1=\Delta_{12}+\Delta_{13},\qquad
D_2=\Delta_{12}+\Delta_{23},\qquad
D_3=\Delta_{13}+\Delta_{23}.
\&#93;

The divisors are permuted by \(S_3\), and \(D_i\) is invariant under \(H_i\).
The two elliptic curves occurring in each \(D_i\) meet transversely in the nine
points \((p,p,p)\), \(p\in E&#91;3&#93;\). Hence

\&#91;
D_i^2=2\cdot9=18&gt;0,
\&#93;

and the sum of the two elliptic subgroup divisors is ample. Therefore
\(Z\setminus|D_i|\) is affine.

Let \(T^\times\) be the punctured affine cone. Its map to \(Z\) is the
\(\mathbf G_m\)-bundle associated with \(M^{-1}\). Define

\&#91;
U_i=T^\times\big|_{Z\setminus|D_i|}.
\&#93;

Each \(U_i\) is affine, the three are \(S_3\)-conjugate, and

\&#91;
X_i^\circ:=U_i/H_i
\&#93;

is an affine open in the cubic quotient. Let

\&#91;
\widetilde S_i=\Gamma(U_i,\mathcal O),
\qquad
S_i=\widetilde S_i^{H_i}=\Gamma(X_i^\circ,\mathcal O).
\&#93;

On \(X_i^\circ\), the marked root is simple, so the diagonal is open and
closed in the base change of the cubic cover. Consequently the complete
source-base-change identity is

\&#91;
\boxed{B_i\otimes_A S_i\simeq S_i\times\widetilde S_i.}
\&#93;

The first factor is the marked root. The second factor is the normal quadratic
algebra ordering the two residual roots; it may ramify when the two unmarked
roots collide. The transposition in \(H_i\) is its involution.

For \(i\neq j\),

\&#91;
U_i\cap U_j
=T^\times\big|_{Z\setminus
 (\Delta_{12}\cup\Delta_{13}\cup\Delta_{23})},
\&#93;

because two different marked roots can both be simple only when all three
roots are distinct. Thus all pair intersections, and the triple intersection,
are the same fully ordered distinct-root algebra. They are affine because the
complement is an ample divisor.

At the level of finite collision algebras, the standard double-coset
calculation gives

\&#91;
\boxed{(B_i\widehat\otimes_A B_i)^\nu\simeq B_i\times T.}
\&#93;

The first factor is the diagonal pair and the second is the off-diagonal
ordered pair. The normalization of the pairwise-distinct component of
\(B_i^{\widehat\otimes_A3}\) is \(T\). The factor-swap involution on a pair is
root exchange, and the \(S_3\)-action on the triple factor is ordinary
permutation of the ordered roots.

This identifies both the pair and triple collision carriers. The raw collision
rings are the corresponding finite tensor-product subalgebras of
\(B_i\times T\) and \(T\); all multiplication maps are inherited from the
section rings above.

---

## 5. The local collision ideal is the standard one

The common intersection of the supports of \(D_1,D_2,D_3\) is

\&#91;
\Delta_{12}\cap\Delta_{13}
=\{(p,p,p):p\in E&#91;3&#93;\},
\&#93;

so there are nine triple-collision points on \(Z\), hence nine collision axes
in the affine cone.

At one such point, use the characteristic-zero formal logarithm on \(E\) so
that the local group law is additive. Put

\&#91;
u=t_1-t_2,\qquad v=t_2-t_3.
\&#93;

Up to units, local equations for the three chart complements are

\&#91;
 f_1=u(u+v),\qquad
 f_2=uv,\qquad
 f_3=v(u+v).
\&#93;

They generate

\&#91;
(f_1,f_2,f_3)=(u^2,uv,v^2)=(u,v)^2.
\&#93;

Thus every generic collision axis is exactly the standard ordered-root model.
In particular, no defect is created by any one axis separately. The nonzero
closed-point class below comes from the global way the nine axes are glued
through the cone vertex.

---

## 6. Direct computation of the saturation quotient

Let

\&#91;
W=\overline{\{\text{the nine triple-collision axes}\}}
\subset\operatorname{Spec}T,
\qquad
U=U_1\cup U_2\cup U_3=\operatorname{Spec}T\setminus W.
\&#93;

All nonempty intersections of the \(U_i\) are affine, so their affine Cech
complex computes \(H^1(U,\mathcal O_U)\). Write

\&#91;
K=\ker(d_1),\qquad I=\operatorname{im}(d_0).
\&#93;

Then

\&#91;
K/I=H^1(U,\mathcal O_U).
\&#93;

Because \(T\) is normal and \(W\) has pure codimension two,

\&#91;
H_W^0(T)=H_W^1(T)=0,
\&#93;

and the localization sequence gives

\&#91;
K/I\simeq H_W^2(T).
\&#93;

Let \(\mathfrak n\) be the cone maximal ideal. Since
\(\sqrt{\mathfrak mT}=\mathfrak n\), saturation by \(\mathfrak m\) is the same
as saturation by \(\mathfrak n\), and

\&#91;
I^{\mathrm{sat}}/I
=H^0_{\mathfrak n}(K/I)
=H^0_{\mathfrak n}(H_W^2(T)).
\&#93;

The support spectral sequence

\&#91;
H^p_{\mathfrak n}(H^q_W(T))\Longrightarrow H^{p+q}_{\mathfrak n}(T)
\&#93;

has no terms with \(q&lt;2\). Its total-degree-two edge map is therefore an
isomorphism:

\&#91;
H^0_{\mathfrak n}(H_W^2(T))\simeq H^2_{\mathfrak n}(T).
\&#93;

For a section ring of an ample line bundle on a projective surface,

\&#91;
&#91;H^2_{\mathfrak n}(T_0)&#93;_q\simeq H^1(Z,M^q).
\&#93;

Since \(Z\) is an abelian surface, \(K_Z\simeq\mathcal O_Z\). Kodaira vanishing
for \(q&gt;0\), followed by Serre duality for \(q&lt;0\), gives

\&#91;
H^1(Z,M^q)=0\quad(q\neq0),
\qquad
H^1(Z,\mathcal O_Z)\simeq\mathbf C^2.
\&#93;

Hence \(H^2_{\mathfrak n}(T)\) is a length-two module killed by
\(\mathfrak n\).

The \(S_3\)-representation on it is standard. Indeed,
\(Z=\ker(E^3\xrightarrow{+}E)\), so \(H^1(Z,\mathcal O_Z)\) is the quotient of
the three-dimensional permutation representation by its diagonal trivial
line. Therefore

\&#91;
\boxed{
I^{\mathrm{sat}}/I
\simeq H^1(Z,\mathcal O_Z)
\simeq V_{\mathrm{std}}.
}
\&#93;

In particular,

\&#91;
\boxed{\operatorname{length}_A(I^{\mathrm{sat}}/I)=2.}
\&#93;

Taking \(H_i\)-invariants gives a one-dimensional fixed line:

\&#91;
(I^{\mathrm{sat}}/I)^{H_i}\simeq\mathbf C
\simeq\operatorname{MatlisDual}(\Delta_{B_i}),
\&#93;

exactly matching

\&#91;
I^{\mathrm{sat}}/I
\simeq\operatorname{MatlisDual}(\Delta_{B_i})
\otimes V_{\mathrm{std}}
\&#93;

in this model.

---

## 7. What this does and does not settle

### Established by the model

1. A normal rank-six \(S_3\)-algebra over \(A=\mathbf C&#91;&#91;a,b,c&#93;&#93;\).
2. A normal non-Galois cubic quotient \(B_i\) with the minimal defect
   \(\Delta_{B_i}\simeq\mathbf C\).
3. A quadratic resolvent
   \(Q=A&#91;w&#93;/(w^2-d)\) with nine explicit height-two \(A_2\) curves.
4. A rank-one reflexive eigensheaf \(L\), its finite presentation, involution,
   and local class vector \((1,\ldots,1)\).
5. Three \(S_3\)-conjugate affine simple-root source charts.
6. The full diagonal/off-diagonal source-base-change splitting.
7. Pair and pairwise-distinct triple collision normalizations.
8. Standard local collision ideals \((u,v)^2\) along every collision axis.
9. A nonzero closed-point standard-isotypic saturation quotient
   \(V_{\mathrm{std}}\).

### Not established

The chart \(X_i^\circ\) is not shown to be \(\mathbf A^3\), and the map to the
base is not supplied by three polynomial coordinates with constant nonzero
Jacobian. Thus this is not a Keller map and does not refute saturation in the
Keller category.

The conclusion is narrower but useful:

&gt; Normality, \(S_3\)-monodromy, codimension-one unramifiedness of the cyclic
&gt; resolvent cover, the canonical marked-root factor, and the complete
&gt; three-chart simple-root algebra do not by themselves force
&gt; \(I^{\mathrm{sat}}=I\).

A Keller-specific proof must use at least one additional global property of the
actual source \(\mathbf A^3\), such as its factoriality, unit group, boundary
incidence, or a consequence of the constant-Jacobian condition that excludes
this elliptic-cone gluing.

---

## 8. Reproducibility note about the public packet

The public Lane 1 page says that the linked packet defines the collision Cech
complex and proves the saturation-carrier theorem. In the currently published
packet, however, the displayed `flatness-defect-repairs.tex` ends with the
resolvent/ADE task, and the remaining two files are the idempotent and standard
local-model checkers. The exact Cech definitions do not appear in the public
text. Accordingly, the construction above uses the natural affine Cech complex
of the three conjugate simple-root charts and independently computes its
closed-point saturation quotient. Matching notation line-by-line to the
private proof packet requires publication of the omitted Cech definition.
</code></pre>

<a id="source-de0db01cd5a38c2c"></a>

## `research-notes/lane1-models-20260803-v1/explicit-marked-root-benchmark.tex`

<pre><code class="language-tex">
\section{The explicit marked-root completion and its resolvent}
\label{app:explicit-marked-root-benchmark}

This appendix carries out the explicit benchmark requested by the Lane~1
flatness program.  It concerns the normalized marked-root cubic
\begin{equation}
\label{eq:explicit-benchmark-cubic}
 P(T)=cT^3-2T^2+bT-2a
\end{equation}
over
\&#91;
 R=\C&#91;a,b,c&#93;.
\&#93;
It is a test case for the general cubic theory, not a normal form for an
arbitrary degree-three Keller map.

We use three different notions that are sometimes all called a conductor or a
different.  The completion-to-source conductor is the ideal
\((B:S)=\{q\in B:qS\subseteq B\}\).  The branch conductor is the conductor of
the discriminant hypersurface into its normalization.  Every different below
is the K\"ahler/Fitting different
\(\operatorname{Fitt}^0\Omega\), except where the phrase ``divisorial
different'' is used explicitly.

\subsection{The finite completion and its global cubic algebra}

Let
\begin{equation}
\label{eq:explicit-projective-completion}
 \widetilde X=
 V\!\left(cT^3-2ST^2+bS^2T-2aS^3\right)
 \subset \operatorname{Spec}(R)\times\mathbf P^1_{&#91;S:T&#93;},
\end{equation}
and let \(\pi\colon\widetilde X\to\operatorname{Spec}(R)\) be projection.

\begin{proposition}&#91;Global cubic algebra&#93;
\label{prop:explicit-global-cubic-algebra}
The scheme \(\widetilde X\) is smooth, integral, and finite flat of degree
three over \(R\).  Its ring of global functions is the integral closure of
\(R\) in the marked-root cubic function field.  If \(t=T/S\) on \(S\ne0\),
then
\&#91;
 \omega=-ct,
 \qquad
 \theta=-ct^2+2t-b
\&#93;
extend to global functions and
\begin{equation}
\label{eq:explicit-global-basis}
 B:=\Gamma(\widetilde X,\mathcal O_{\widetilde X})
   =R\oplus R\omega\oplus R\theta.
\end{equation}
Their multiplication is
\begin{equation}
\label{eq:explicit-multiplication-table}
\begin{aligned}
 \omega^2&amp;=-bc-2\omega-c\theta,\\
 \omega\theta&amp;=2ac,\\
 \theta^2&amp;=-4a-2a\omega-b\theta.
\end{aligned}
\end{equation}
\end{proposition}

\begin{proof}
The homogeneous equation in \eqref{eq:explicit-projective-completion} is not
identically zero on any geometric fibre, because its \(ST^2\)-coefficient is
\(-2\).  It is therefore a relative effective Cartier divisor of degree three
in \(\mathbf P^1_R\).  Its fibres are zero-dimensional of length three, so the
proper morphism \(\pi\) is quasi-finite and hence finite.  Fibrewise
injectivity of multiplication by the cubic in
\&#91;
 0\longrightarrow\mathcal O_{\mathbf P^1_R}(-3)
 \longrightarrow\mathcal O_{\mathbf P^1_R}
 \longrightarrow\mathcal O_{\widetilde X}
 \longrightarrow0
\&#93;
gives flatness.

On \(S\ne0\), the equation solves for \(a\), so this chart is
\(\Spec\C&#91;b,c,t&#93;\).  On \(T\ne0\), with \(s=S/T\), the equation is
\&#91;
 c-2s+bs^2-2as^3=0,
\&#93;
which solves for \(c\), so this chart is \(\Spec\C&#91;a,b,s&#93;\).  Their nonempty
overlap is obtained by \(s=t^{-1}\); hence the two integral charts glue to an
integral scheme.  Differentiation with respect to \(a\) on the first chart and
with respect to \(c\) on the second gives respectively \(-2\) and \(1\), so
\(\widetilde X\) is smooth.  Its generic function field is
\(\Frac(R)(t)/(P(t))\).  Since \(\widetilde X\) is finite and normal over
\(\Spec R\), its global algebra is the integral closure of \(R\) in this
marked-root cubic field.  For the normalized polynomial map this is the source
field by \eqref{eq:root-identities} and \eqref{eq:reconstruction}.

It remains to prove the global basis, including the fibre \(c=0\).  On the
infinity chart one has
\&#91;
 c=2s-bs^2+2as^3,
 \qquad
 \omega=-2+bs-2as^2,
 \qquad
 \theta=-2as,
\&#93;
so \(\omega\) and \(\theta\) are global.  Pushforward of the preceding exact
sequence gives
\&#91;
 0\longrightarrow R\longrightarrow B
 \xrightarrow{\partial}H^1(\mathbf P^1_R,\mathcal O(-3))
 \longrightarrow0.
\&#93;
In the standard two-chart Cech description,
\&#91;
 H^1(\mathbf P^1_R,\mathcal O(-3))
   =Rt^{-1}\oplus Rt^{-2}.
\&#93;
The finite- and infinity-chart lifts satisfy
\&#91;
 -ct-\left(-2+\frac b t-\frac{2a}{t^2}\right)
   =-\frac{P(t)}{t^2},
\&#93;
and
\&#91;
 \left(-ct^2+2t-b\right)-\left(-\frac{2a}{t}\right)
   =-\frac{P(t)}t.
\&#93;
Consequently
\&#91;
 \partial(\omega)=-t^{-2},
 \qquad
 \partial(\theta)=-t^{-1},
\&#93;
which proves \eqref{eq:explicit-global-basis}.  Reduction modulo \(P(t)\)
gives \eqref{eq:explicit-multiplication-table}.
\end{proof}

The traces are
\&#91;
 \operatorname{Tr}(\omega)=-2,
 \qquad
 \operatorname{Tr}(\theta)=-b.
\&#93;
Thus the trace-zero summand has the global basis
\begin{equation}
\label{eq:explicit-trace-zero-basis}
 E=Re_1\oplus Re_2,
 \qquad
 e_1=3\omega+2,
 \qquad
 e_2=3\theta+b.
\end{equation}
The trace-pairing matrix in the basis \(1,\omega,\theta\) is
\begin{equation}
\label{eq:explicit-trace-pairing}
 G=
 \begin{pmatrix}
 3&amp;-2&amp;-b\\
 -2&amp;4-2bc&amp;6ac\\
 -b&amp;6ac&amp;b^2-8a
 \end{pmatrix}.
\end{equation}
Its determinant is \(4\delta\), where
\begin{equation}
\label{eq:explicit-delta}
 \delta=b^2-b^3c-16a+18abc-27a^2c^2.
\end{equation}
Equivalently, \(4\delta=\operatorname{disc}_T(P)\).

\subsection{The quadratic resolvent}

Rescaling the usual discriminant generator by a nonzero complex constant, put
\begin{equation}
\label{eq:explicit-quadratic-resolvent}
 Q=R&#91;\varpi&#93;/(\varpi^2+3\delta).
\end{equation}
Define
\begin{equation}
\label{eq:explicit-covariants}
 p=4-3bc,
 \qquad
 h=8-9bc+27ac^2.
\end{equation}
A direct identity is
\begin{equation}
\label{eq:explicit-cusp-identity}
 p^3-h^2=27c^2\delta.
\end{equation}
On \(D(c)\), set
\&#91;
 u=h+3c\varpi,
 \qquad
 v=h-3c\varpi.
\&#93;
Then
\begin{equation}
\label{eq:explicit-A2-resolvent}
 Q&#91;c^{-1}&#93;
 \simeq
 \C&#91;c^{\pm1},p,u,v&#93;/(uv-p^3).
\end{equation}
The inverse coordinate change is
\&#91;
 b=\frac{4-p}{3c},
 \qquad
 h=\frac{u+v}{2},
 \qquad
 a=\frac{h+4-3p}{27c^2},
 \qquad
 \varpi=\frac{u-v}{6c}.
\&#93;

\begin{proposition}&#91;Resolvent singular curve&#93;
\label{prop:explicit-resolvent-singular-curve}
The quadratic resolvent is normal and
\&#91;
 \operatorname{Sing}(Q)=V(\varpi,p,h).
\&#93;
This curve maps isomorphically to
\begin{equation}
\label{eq:explicit-triple-root-curve}
 \Gamma=V(3bc-4,\,54c^2a-8)\subset\operatorname{Spec}(R).
\end{equation}
Transversely to \(\Gamma\), the resolvent has type \(A_2\).
\end{proposition}

\begin{proof}
The Jacobian ideal of \(\varpi^2+3\delta\) is contained in
\((\varpi,p,h)\).  Conversely, \(\varpi\) and \(h=-\frac12\partial_a\delta\)
belong to the Jacobian ideal, and \eqref{eq:explicit-cusp-identity} shows that
\(p^3\) belongs to it.  Hence the radicals agree.  Modulo \((p,h)\), one has
\(bc=4/3\), so \(c\) is a unit and the quotient is \(\C&#91;c,c^{-1}&#93;\).  The
singular locus therefore has codimension two.  Since \(Q\) is a hypersurface,
it is Cohen--Macaulay and regular in codimension one, hence normal.  The local
equation \(uv=p^3\) gives the transverse \(A_2\) type.
\end{proof}

\subsection{The cubic character eigensheaf}

On \(D(c)\), the full \(S_3\)-normalization is
\begin{equation}
\label{eq:explicit-galois-cover}
 T_c=\C&#91;c^{\pm1},U,V&#93;,
 \qquad
 p=UV,
 \quad
 u=U^3,
 \quad
 v=V^3.
\end{equation}
For a primitive cube root \(\zeta\), let
\&#91;
 \tau(U,V)=(\zeta U,\zeta^{-1}V),
 \qquad
 \sigma(U,V)=(V,U).
\&#93;
Then \(T_c^{\langle\tau\rangle}=Q&#91;c^{-1}&#93;\), and the full invariant ring is
\(R&#91;c^{-1}&#93;\).  The marked depressed root
\&#91;
 \alpha=U+V=3ct-2
\&#93;
satisfies
\begin{equation}
\label{eq:explicit-depressed-cubic}
 \alpha^3-3p\alpha-2h=0.
\end{equation}

Choose the \(\zeta\)-eigensheaf
\&#91;
 L_\zeta=QU+QV^2.
\&#93;
Multiplication by \(U^2\) identifies it with the reflexive ideal
\begin{equation}
\label{eq:explicit-local-eigensheaf}
 L_\zeta\simeq(u,p^2),
 \qquad
 L_{\zeta^2}\simeq(u,p)\simeq L_\zeta^\vee.
\end{equation}
At the generic point of \(\Gamma\), these are the two nonzero classes in the
transverse class group \(\mathbf Z/3\).

The following presentation closes the extension through \(c=0\) and through
every closed point of \(\Gamma\).

\begin{proposition}&#91;Global eigensheaf presentation&#93;
\label{prop:explicit-global-eigensheaf}
Put
\&#91;
 m=9ac-b,
 \qquad
 n=b^2-12a,
 \qquad
 M=
 \begin{pmatrix}
 m&amp;n\\
 -p&amp;-m
 \end{pmatrix}.
\&#93;
Then
\begin{equation}
\label{eq:explicit-M-square}
 M^2=-3\delta I_2.
\end{equation}
Under the canonical resolvent identification of
\cref{thm:exact-resolvent-carrier}, the trace-zero cubic summand is a
character eigensheaf, and \(\varpi\) acts on the basis
\eqref{eq:explicit-trace-zero-basis} by \(M\).  Consequently
\begin{equation}
\label{eq:explicit-eigensheaf-presentation}
 L\simeq\operatorname{coker}_Q(\varpi I_2-M),
\end{equation}
and
\&#91;
 (\varpi I_2-M)(\varpi I_2+M)
   =(\varpi^2+3\delta)I_2.
\&#93;
In particular, \(L\) is maximal Cohen--Macaulay over \(Q\), although it is
not locally free as a \(Q\)-module along \(\Gamma\).
\end{proposition}

\begin{proof}
The identity \eqref{eq:explicit-M-square} is direct.  To identify the action,
work first on \(D(c)\).  The canonical \(R\)-linear map from the chosen
character summand to the cubic trace-zero summand is
\&#91;
 \ell\longmapsto\ell+\sigma(\ell).
\&#93;
It sends \(U\) and \(V^2\) to
\&#91;
 \alpha=U+V,
 \qquad
 \beta=U^2+V^2=\alpha^2-2p.
\&#93;
Transporting multiplication by \(\varpi\), rather than multiplying inside the
cubic subring, gives
\&#91;
 3c(\varpi\star\alpha)=h\alpha-p\beta,
 \qquad
 3c(\varpi\star\beta)=p^2\alpha-h\beta.
\&#93;
Thus the transported action in the basis \((\alpha,\beta)\) is
\&#91;
 \frac1{3c}
 \begin{pmatrix}
 h&amp;p^2\\
 -p&amp;-h
 \end{pmatrix}.
\&#93;
Since
\&#91;
 \alpha=-e_1,
 \qquad
 \beta=-2e_1-3ce_2,
\&#93;
conjugating by
\(\begin{psmallmatrix}-1&amp;-2\\0&amp;-3c\end{psmallmatrix}\)
gives \(M\).

By \cref{thm:exact-resolvent-carrier}, the actual transported
resolvent action is an element of
\(\operatorname{End}_R(E)=M_2(R)\).  It agrees with \(M\) after inverting
\(c\), hence agrees globally because \(M_2(R)\) is torsion-free.  This proves
\eqref{eq:explicit-eigensheaf-presentation}.  Its underlying \(R\)-module is
\(R^2\), so it has depth three; the displayed matrix factorization is the
corresponding explicit MCM certificate.
\end{proof}

After the basis change in the proof,
\&#91;
 3c(\varpi I-M)=
 \begin{pmatrix}
 -v&amp;-p^2\\
 p&amp;u
 \end{pmatrix}.
\&#93;
The row \((u,p^2)\) kills this matrix modulo \(uv-p^3\), and its kernel is
generated by the two columns.  Indeed, if
\(xu+yp^2=z(uv-p^3)\) in \(\C&#91;p,u,v&#93;\), then
\&#91;
 u(x-zv)+p^2(y+zp)=0.
\&#93;
Since \(u\) and \(p\) are coprime, there is a polynomial \(q\) such that
\&#91;
 x-zv=-p^2q,
 \qquad
 y+zp=uq.
\&#93;
This proves the local identification with \((u,p^2)\) in
\eqref{eq:explicit-local-eigensheaf}.

\subsection{Conductors}

Let \(S=\mathcal O(X)\simeq\C&#91;x,y,z&#93;\) be the affine source ring.  By \cref{thm:AB-global,eq:source-open}, in this normalized example
the affine source is the complement of the repeated-root divisor
\(\mathcal R\) in \(\widetilde X\).  On the finite-root chart,
\&#91;
 r=P'(t)=3ct^2-4t+b,
 \qquad
 x=\frac2r.
\&#93;
At the generic point of \(\mathcal R\), the function \(r\) is a uniformizer.
For nonzero \(q\in B\), choose \(N&gt;v_{\mathcal R}(q)\).  Then
\(qx^N\notin B\), so
\begin{equation}
\label{eq:explicit-zero-open-conductor}
 (B:S)=0.
\end{equation}
The completion itself is smooth and normal, so its conductor into its own
normalization is the unit ideal.

Let \(\mathcal D=V(\delta)\) be the branch hypersurface.  Its normalization is
the repeated-root divisor
\&#91;
 \mathcal R\simeq\mathbf A^2_{t,c},
 \qquad
 b=4t-3ct^2,
 \qquad
 a=t^2-ct^3.
\&#93;
Put \(z=3ct-2\).  Then
\begin{equation}
\label{eq:explicit-branch-cusp}
 p=z^2,
 \qquad
 h=-z^3.
\end{equation}
On \(D(c)\), the normalization is therefore
\&#91;
 \C&#91;c^{\pm1},z^2,z^3&#93;
 \subset
 \C&#91;c^{\pm1},z&#93;.
\&#93;
On \(D(p)\), the normalization is already an isomorphism, because the double
root is
\&#91;
 t=\frac{b-9ac}{p}.
\&#93;
The two opens cover the branch.  Hence its global conductor is
\begin{equation}
\label{eq:explicit-branch-conductor}
 \mathfrak c_{\mathcal D}=(p,h),
 \qquad
 \mathfrak c_{\mathcal D}\mathcal O_{\mathcal R}=(z^2).
\end{equation}
Its support is precisely \(\Gamma\).

\subsection{Differents}

Using the presentation \eqref{eq:explicit-multiplication-table}, the Jacobian
matrix with respect to \((\omega,\theta)\) is
\&#91;
 J=
 \begin{pmatrix}
 2\omega+2&amp;c\\
 \theta&amp;\omega\\
 2a&amp;2\theta+b
 \end{pmatrix}.
\&#93;
Its maximal minors give
\begin{equation}
\label{eq:explicit-cubic-different}
 \mathfrak D_{B/R}
 =\operatorname{Fitt}^0_B\Omega_{B/R}
 =(d_1,d_2,d_3),
\end{equation}
where
\begin{align*}
 d_1&amp;=-2\omega-3c\theta-2bc,\\
 d_2&amp;=6ac+2b\omega+4\theta+2b,\\
 d_3&amp;=-8a-6a\omega-b\theta.
\end{align*}
On the finite-root chart,
\begin{equation}
\label{eq:explicit-different-factorization}
 d_1=cr,
 \qquad
 d_2=(ct-2)r,
 \qquad
 d_3=-\theta r.
\end{equation}
Since \(c\) and \(ct-2\) generate the unit ideal there, the different cuts out
exactly the repeated-root divisor.  At the infinity point over \(c=0\), one
has \(\omega=-2\), \(\theta=0\), and \(d_1=4\), so there is no hidden
ramification component.

At a triple-root fibre, write
\&#91;
 t=\frac2{3c}+\varepsilon.
\&#93;
Then \(r=3c\varepsilon^2\), and the fibrewise different is
\&#91;
 (\varepsilon^2)\subset\C&#91;\varepsilon&#93;/(\varepsilon^3).
\&#93;
For the quadratic resolvent,
\begin{equation}
\label{eq:explicit-quadratic-different}
 \mathfrak D_{Q/R}=(2\varpi)=(\varpi).
\end{equation}
For the branch normalization, one has
\&#91;
 \Omega_{\C&#91;c^{\pm1},z&#93;/\C&#91;c^{\pm1},z^2,z^3&#93;}
 \simeq \C&#91;c^{\pm1},z&#93;/(z)\,dz,
\&#93;
so its K\"ahler different is \((z)\), whose square is the extended conductor
\((z^2)\).  Finally, the cyclic cover \(T/Q\) has fixed locus
\(U=V=0\), of codimension two, and therefore has trivial divisorial different.

\subsection{Omitted values and the absence of a flatness defect}

The omitted locus is the triple-root curve \(\Gamma\) in
\eqref{eq:explicit-triple-root-curve}.  Along it,
\&#91;
 b=\frac4{3c},
 \qquad
 a=\frac4{27c^2},
\&#93;
and
\begin{equation}
\label{eq:explicit-triple-root-factorization}
 P(T)=c\left(T-\frac2{3c}\right)^3.
\end{equation}
Thus the completed finite fibre is
\&#91;
 \operatorname{Spec}\C&#91;\varepsilon&#93;/(\varepsilon^3),
\&#93;
of scheme length three.  Its support lies entirely in the repeated-root
divisor deleted from the affine source, so the affine fibre is empty.  This is
boundary deletion, not loss of rank in the finite completion.

\begin{corollary}&#91;Benchmark flatness&#93;
\label{cor:explicit-benchmark-flatness}
For the normalized marked-root example,
\&#91;
 \Delta_F=\operatorname{Ext}^1_R(B,R)=0.
\&#93;
The resolvent nevertheless carries a nonzero transverse order-three divisor
class along \(\Gamma\).
\end{corollary}

\begin{proof}
The first assertion follows immediately from
\(B=R\oplus R\omega\oplus R\theta\).  Equivalently, the global eigensheaf in
\cref{prop:explicit-global-eigensheaf} is MCM.  The local identification
\(L\simeq(u,p^2)\) gives the nonzero \(A_2\) class.  Hence nontrivial local
three-torsion records monodromy here but does not create a finite flatness
defect.
\end{proof}

The exact checker
\path{code/verify_marked_root_benchmark.py} verifies the displayed
polynomial identities, the elimination presentation of \(B\), the resolvent
singular radical, the matrix factorization, the local ideal syzygies, the
branch parametrization, and the Fitting-minor formulas.  The geometric
arguments about normality, Cech cohomology, valuations, and depth remain reader
proofs.
</code></pre>

<a id="source-87c7cf6aee0542db"></a>

## `research-notes/lane1-models-20260803-v1/explicit-marked-root-collision-saturation.tex`

<pre><code class="language-tex">
\section{Actual collision saturation in the marked-root example}
\label{app:explicit-marked-root-collision-saturation}

This appendix computes the actual three-chart collision complex at every
omitted value of the normalized marked-root example.  Unlike the universal
ordered-root calculation, the argument first identifies the source charts
coming from the global polynomial map.  The result is that the actual opening
is the product standard model and its closed-point saturation quotient
vanishes.

Retain the notation of
\cref{app:explicit-marked-root-benchmark}.  Let
\(y_0\in\Gamma\) be arbitrary, write its \(c\)-coordinate as \(c_0\), and put
\&#91;
 \lambda=c-c_0.
\&#93;
The equations of \(\Gamma\) imply \(c_0\ne0\).

\subsection{Completed base and Galois ring}

The covariants
\&#91;
 p=4-3bc,
 \qquad
 h=8-9bc+27ac^2
\&#93;
together with \(c\) form local coordinates near \(y_0\): the Jacobian of
\((p,h,c)\) with respect to \((a,b,c)\) has determinant \(81c^3\).  Hence
\begin{equation}
\label{eq:explicit-collision-base}
 A:=\widehat{\mathcal O}_{Y,y_0}
   \simeq\C&#91;&#91;p,h,\lambda&#93;&#93;.
\end{equation}

Let \(\alpha_1,\alpha_2,\alpha_3\) be the ordered roots of the depressed cubic
\&#91;
 g(X)=X^3-3pX-2h.
\&#93;
Put
\&#91;
 u=\alpha_1-\alpha_2,
 \qquad
 v=\alpha_2-\alpha_3.
\&#93;
Since \(\alpha_1+\alpha_2+\alpha_3=0\),
\begin{equation}
\label{eq:explicit-ordered-roots}
 \alpha_1=\frac{2u+v}{3},
 \qquad
 \alpha_2=\frac{-u+v}{3},
 \qquad
 \alpha_3=\frac{-u-2v}{3}.
\end{equation}
The invariant map is
\begin{equation}
\label{eq:explicit-root-difference-invariants}
 p=\frac{u^2+uv+v^2}{9},
 \qquad
 h=\frac{(u-v)(u+2v)(2u+v)}{54}.
\end{equation}
Thus the completed \(S_3\)-normalization at the point above \(y_0\) is
\begin{equation}
\label{eq:explicit-completed-galois-ring}
 \widehat T=\C&#91;&#91;u,v,\lambda&#93;&#93;.
\end{equation}
The transposition \((12)\) and cycle \((123)\) act by
\begin{equation}
\label{eq:explicit-standard-action}
 s(u,v)=(-u,u+v),
 \qquad
 \rho(u,v)=(v,-u-v),
\end{equation}
which is the standard two-dimensional representation of \(S_3\); the axis
parameter \(\lambda\) is fixed.

\subsection{The actual source charts}

The marked roots of the original cubic are
\&#91;
 t_i=\frac{\alpha_i+2}{3c}.
\&#93;
Differentiating the identity
\&#91;
 27c^2P\!\left(\frac{X+2}{3c}\right)=g(X)
\&#93;
gives
\&#91;
 P'(t_i)=\frac{g'(\alpha_i)}{9c}.
\&#93;
Using \eqref{eq:explicit-ordered-roots}, one obtains
\begin{equation}
\label{eq:explicit-three-root-slopes}
\begin{aligned}
 g'(\alpha_1)&amp;=u(u+v)=:q_1,\\
 g'(\alpha_2)&amp;=-uv=:q_2,\\
 g'(\alpha_3)&amp;=v(u+v)=:q_3.
\end{aligned}
\end{equation}
Since \(c\) is a unit in the completed neighbourhood, inverting
\(P'(t_i)\) is equivalent to inverting \(q_i\).

The following is the point where the global marked-root map is essential.  The
root--slope reconstruction \eqref{eq:reconstruction} gives
\&#91;
 x=\frac2{P'(t)},
\&#93;
and \cref{thm:AB-global,eq:source-open} identifies the affine source with the
complement of the repeated-root divisor, with no additional deleted infinity
section in this normalized example.  Therefore the three conjugate source
charts in the complete \(S_3\)-opening are exactly
\begin{equation}
\label{eq:explicit-source-charts}
 U_i=\operatorname{Spec}\widehat T&#91;q_i^{-1}&#93;,
 \qquad i=1,2,3.
\end{equation}
A normal \(S_3\)-algebra by itself does not determine this opening; it is the
global reconstruction and boundary theorem that supplies
\eqref{eq:explicit-source-charts}.

For each pair, the completed collision component selected by the relevant
off-diagonal idempotent is
\begin{equation}
\label{eq:explicit-pair-collision-rings}
 C_{ij}=\widehat T&#91;(q_iq_j)^{-1}&#93;,
 \qquad 1\le i&lt;j\le3,
\end{equation}
and the completed ordered triple-collision component is
\begin{equation}
\label{eq:explicit-triple-collision-ring}
 C_{123}=\widehat T&#91;(q_1q_2q_3)^{-1}&#93;.
\end{equation}
The other ordered components are their \(S_3\)-translates.  Explicitly,
\&#91;
 q_1q_2q_3=-u^2v^2(u+v)^2.
\&#93;

\subsection{The Cech kernel, image, and saturation}

Let
\&#91;
 C^0=\bigoplus_{i=1}^3\widehat T&#91;q_i^{-1}&#93;,
 \qquad
 C^1=\bigoplus_{1\le i&lt;j\le3}C_{ij},
 \qquad
 C^2=C_{123}
\&#93;
with the alternating Cech differentials.  Put
\&#91;
 I_{y_0}=\operatorname{im}(C^0\to C^1),
 \qquad
 K_{y_0}=\ker(C^1\to C^2).
\&#93;
The three chart-complement equations satisfy
\begin{equation}
\label{eq:explicit-chart-complement-ideal}
 (q_1,q_2,q_3)
 =\bigl(u(u+v),uv,v(u+v)\bigr)
 =(u,v)^2.
\end{equation}
Indeed,
\&#91;
 q_1+q_2=u^2,
 \qquad
 q_3+q_2=v^2,
\&#93;
and every \(q_i\) is quadratic in \(u,v\).

Consequently the union of the three actual source charts is
\&#91;
 U=\operatorname{Spec}\widehat T\setminus V(u,v).
\&#93;
Since \(\widehat T\) is regular and \((u,v)\) has depth two, the local
cohomology sequence and the affine Cech complex give
\begin{equation}
\label{eq:explicit-cech-local-cohomology}
 K_{y_0}/I_{y_0}
 \simeq H^1(U,\mathcal O_U)
 \simeq H^2_{(u,v)}(\widehat T).
\end{equation}
The two-generator Cech model gives
\begin{equation}
\label{eq:explicit-local-cohomology-basis}
 H^2_{(u,v)}(\widehat T)
 \simeq
 \widehat T_{uv}/(\widehat T_u+\widehat T_v)
 \simeq
 \bigoplus_{i,j\ge1}
 \C&#91;&#91;\lambda&#93;&#93;\,u^{-i}v^{-j}.
\end{equation}
In particular, multiplication by \(\lambda\) is injective.

Let \(\mathfrak m_{y_0}=(p,h,\lambda)\subset A\).  Its pullback to
\(\widehat T\) has radical \((u,v,\lambda)\).  For example,
\((u,v)^4\subset(p,h)\) follows directly from
\eqref{eq:explicit-root-difference-invariants}.  Define saturation inside the
Cech kernel by
\&#91;
 I_{y_0}^{\mathrm{sat}}
 =I_{y_0}:_{K_{y_0}}\mathfrak m_{y_0}^{\infty}.
\&#93;
Then
\&#91;
 \frac{I_{y_0}^{\mathrm{sat}}}{I_{y_0}}
 =H^0_{\mathfrak m_{y_0}}(K_{y_0}/I_{y_0}).
\&#93;
If an element on the right were nonzero and killed by a power of
\(\mathfrak m_{y_0}\), it would in particular be killed by a power of
\(\lambda\), contradicting \eqref{eq:explicit-local-cohomology-basis}.
Therefore
\begin{equation}
\label{eq:explicit-saturation-vanishing}
 I_{y_0}^{\mathrm{sat}}=I_{y_0}.
\end{equation}

\begin{theorem}&#91;Actual marked-root saturation&#93;
\label{thm:explicit-marked-root-saturation}
For every omitted value \(y_0\in\Gamma\) of the normalized marked-root Keller
map,
\&#91;
 \left(I_{y_0}^{\mathrm{sat}}/I_{y_0}\right)_{\mathrm{std}}=0.
\&#93;
In fact, the entire saturation quotient vanishes.
\end{theorem}

\begin{proof}
Equation \eqref{eq:explicit-saturation-vanishing} proves the stronger
statement.  Taking the standard isotypic summand preserves zero.
\end{proof}

\subsection{Scope of the calculation}

The formal cover
\&#91;
 \C&#91;&#91;u,v,\lambda&#93;&#93;/\C&#91;&#91;p,h,\lambda&#93;&#93;
\&#93;
with its \(S_3\)-action, together with the root-difference and slope
identities, is a local consequence of the ordered cubic roots.  The
following inputs are specific to the global polynomial map:
\begin{enumerate}
\item the source chart attached to the \(i\)-th root is exactly
      \(D(P'(t_i))\), by the reconstruction formula;
\item the affine source deletes exactly the repeated-root divisor near
      \(\Gamma\), with no extra boundary component;
\item the parameter \(\lambda=c-c_0\) is a genuine transverse product
      parameter along the whole omitted curve.
\end{enumerate}
Without these global inputs, the same normal \(S_3\)-algebra may be equipped
with a different non-product opening, and the calculation does not settle the
general Lane~1 saturation problem.

The exact checker
\path{code/verify_marked_root_collision_saturation.py} verifies the invariant
map, ordered roots, root slopes, \(S_3\)-action, equality
\((q_1,q_2,q_3)=(u,v)^2\), triple denominator, and radical certificate.  The
injectivity of \(\lambda\) on the displayed local-cohomology module is the
reader proof of the saturation step.
</code></pre>

<a id="source-192a60b955e4b3a2"></a>

## `research-notes/lane1-models-20260803-v1/typeiv-explicit-net-data.json`

<pre><code class="language-json">
{
  "branch_affine_c_eq_1": "-984*a**10 + 356*a**9*b + 332*a**9 + 1245*a**8*b**2 - 1122*a**8*b + 1273*a**8 + 1044*a**7*b**3 - 1260*a**7*b**2 - 1444*a**7*b + 868*a**7 + 1684*a**6*b**4 + 568*a**6*b**3 - 104*a**6*b**2 + 1004*a**6*b + 364*a**6 - 606*a**5*b**5 - 126*a**5*b**4 - 1096*a**5*b**3 - 888*a**5*b**2 + 1474*a**5*b - 558*a**5 - 2100*a**4*b**6 + 2856*a**4*b**5 - 2518*a**4*b**4 - 34*a**4*b**3 - 1444*a**4*b**2 + 1230*a**4*b - 998*a**4 - 1920*a**3*b**7 + 3060*a**3*b**6 - 1900*a**3*b**5 + 2072*a**3*b**4 + 112*a**3*b**3 + 100*a**3*b**2 + 520*a**3*b - 756*a**3 - 1743*a**2*b**8 + 912*a**2*b**7 - 780*a**2*b**6 - 188*a**2*b**5 + 1538*a**2*b**4 - 232*a**2*b**3 + 788*a**2*b**2 - 140*a**2*b - 423*a**2 - 768*a*b**9 + 1164*a*b**8 + 1678*a*b**7 + 184*a*b**6 + 560*a*b**5 - 670*a*b**4 - 406*a*b**3 + 392*a*b**2 - 164*a*b - 170*a - 112*b**10 + 368*b**9 + 188*b**8 - 952*b**7 - 247*b**6 + 284*b**5 - 404*b**4 - 202*b**3 + 72*b**2 - 32*b - 31",
  "branch_homogeneous_degree_10": "-984*a**10 + 356*a**9*b + 332*a**9*c + 1245*a**8*b**2 - 1122*a**8*b*c + 1273*a**8*c**2 + 1044*a**7*b**3 - 1260*a**7*b**2*c - 1444*a**7*b*c**2 + 868*a**7*c**3 + 1684*a**6*b**4 + 568*a**6*b**3*c - 104*a**6*b**2*c**2 + 1004*a**6*b*c**3 + 364*a**6*c**4 - 606*a**5*b**5 - 126*a**5*b**4*c - 1096*a**5*b**3*c**2 - 888*a**5*b**2*c**3 + 1474*a**5*b*c**4 - 558*a**5*c**5 - 2100*a**4*b**6 + 2856*a**4*b**5*c - 2518*a**4*b**4*c**2 - 34*a**4*b**3*c**3 - 1444*a**4*b**2*c**4 + 1230*a**4*b*c**5 - 998*a**4*c**6 - 1920*a**3*b**7 + 3060*a**3*b**6*c - 1900*a**3*b**5*c**2 + 2072*a**3*b**4*c**3 + 112*a**3*b**3*c**4 + 100*a**3*b**2*c**5 + 520*a**3*b*c**6 - 756*a**3*c**7 - 1743*a**2*b**8 + 912*a**2*b**7*c - 780*a**2*b**6*c**2 - 188*a**2*b**5*c**3 + 1538*a**2*b**4*c**4 - 232*a**2*b**3*c**5 + 788*a**2*b**2*c**6 - 140*a**2*b*c**7 - 423*a**2*c**8 - 768*a*b**9 + 1164*a*b**8*c + 1678*a*b**7*c**2 + 184*a*b**6*c**3 + 560*a*b**5*c**4 - 670*a*b**4*c**5 - 406*a*b**3*c**6 + 392*a*b**2*c**7 - 164*a*b*c**8 - 170*a*c**9 - 112*b**10 + 368*b**9*c + 188*b**8*c**2 - 952*b**7*c**3 - 247*b**6*c**4 + 284*b**5*c**5 - 404*b**4*c**6 - 202*b**3*c**7 + 72*b**2*c**8 - 32*b*c**9 - 31*c**10",
  "canonical_sha256": "4d21565e944d5619288e1525be2219a0353b839ff0bebc6f452ddcec9e557b9d",
  "certificates": {
    "base_length": 13,
    "base_reduced": true,
    "base_standard_monomials": &#91;
      &#91;
        0,
        0
      &#93;,
      &#91;
        0,
        1
      &#93;,
      &#91;
        0,
        2
      &#93;,
      &#91;
        0,
        3
      &#93;,
      &#91;
        0,
        4
      &#93;,
      &#91;
        0,
        5
      &#93;,
      &#91;
        1,
        0
      &#93;,
      &#91;
        1,
        1
      &#93;,
      &#91;
        1,
        2
      &#93;,
      &#91;
        1,
        3
      &#93;,
      &#91;
        2,
        0
      &#93;,
      &#91;
        2,
        1
      &#93;,
      &#91;
        3,
        0
      &#93;
    &#93;,
    "branch_cusp_count": 21,
    "branch_irreducible_over_Q": true,
    "branch_local_jacobian_multiplicity": 2,
    "branch_singular_jacobian_length": 42,
    "branch_singular_support_degree": 21,
    "generic_degree": 3,
    "ramification_irreducible_over_Q": true,
    "resolved_map_finite": true,
    "support_polynomial_in_b": "b**21 - 45118*b**20/1587 + 448736*b**19/1587 - 50743969*b**18/42849 + 211204315*b**17/128547 + 460911452*b**16/128547 - 60297178121*b**15/3470769 + 66363455426*b**14/3470769 - 642019895486*b**13/31236921 - 9211257658952*b**12/281132289 + 4069855876469*b**11/93710763 + 909745667302*b**10/93710763 + 646569296981*b**9/281132289 + 36860533436*b**8/4074381 - 146333840606*b**7/93710763 + 70361228155*b**6/93710763 + 6265354604*b**5/31236921 + 11892192811*b**4/93710763 - 1214126008*b**3/93710763 - 11251888*b**2/3470769 + 43538951*b/31236921 - 34759331/281132289"
  },
  "quartic_net": {
    "q1": "x**3*y - 2*x**3*z + x**2*y**2 - x**2*z**2 - x*y**2*z + x*y*z**2 + y**4 + y**3*z + y**2*z**2 - 2*y*z**3 - z**4",
    "q2": "-x**4 - x**3*y + x**3*z - x**2*z**2 - x*y**3 + 2*x*z**3 + 2*y**3*z + y**2*z**2 + 3*z**4",
    "q3": "2*x**4 - x**3*y + x**3*z + x**2*y**2 - x*y**3 - x*y**2*z + x*z**3 - 2*y**4 - y**3*z - 3*y*z**3"
  },
  "ramification_degree_9": "3*x**9 - 10*x**8*y + 10*x**8*z + 21*x**7*y**2 + 8*x**7*y*z - 19*x**7*z**2 - 2*x**6*y**3 - 19*x**6*y**2*z - 13*x**6*y*z**2 + 6*x**6*z**3 + 13*x**5*y**4 + 25*x**5*y**3*z + 9*x**5*y**2*z**2 - 47*x**5*y*z**3 - 7*x**5*z**4 + x**4*y**5 - 28*x**4*y**4*z - 15*x**4*y**3*z**2 - 3*x**4*y**2*z**3 + 21*x**4*y*z**4 + x**4*z**5 - 13*x**3*y**6 - 20*x**3*y**5*z + 47*x**3*y**4*z**2 - 25*x**3*y**3*z**3 - 32*x**3*y**2*z**4 - 43*x**3*y*z**5 + 74*x**3*z**6 - 13*x**2*y**7 + x**2*y**6*z + 57*x**2*y**5*z**2 - 13*x**2*y**4*z**3 + 33*x**2*y**3*z**4 + 15*x**2*y**2*z**5 - 43*x**2*y*z**6 + 71*x**2*z**7 - 9*x*y**8 - 12*x*y**7*z + 5*x*y**6*z**2 - 52*x*y**5*z**3 + 2*x*y**4*z**4 + 34*x*y**3*z**5 + 15*x*y**2*z**6 - 4*x*y*z**7 + 21*x*z**8 + y**9 + 4*y**8*z + 21*y**7*z**2 + 34*y**6*z**3 + 60*y**5*z**4 - 20*y**4*z**5 - 57*y**3*z**6 - 26*y**2*z**7 - 17*y*z**8",
  "restricted_cubic_c_eq_1": "-3*a**4*t**3 - a**3*b*t**3 - 9*a**3*b*t**2 + 2*a**3*t**3 - 3*a**2*b**2*t**2 - 9*a**2*b**2*t + 6*a**2*b*t**2 + a**2*t**3 - a**2*t - 3*a*b**3*t - 3*a*b**3 + 6*a*b**2*t - a*b*t**3 + 2*a*b*t**2 + a*b*t - a*b + a*t**3 + 2*a - b**4 + 2*b**3 - b**2*t**2 + b**2*t + b**2 + 2*b*t**3 + b*t - b + t**3 + t**2 + 1",
  "sample_fibre_1_2_3": {
    "cubic_equation": "53*y**3 + 251*y**2 + 387*y + 208",
    "discriminant": -14858267,
    "linear_equation": "x + 2*y + 3"
  },
  "schema_version": 1,
  "section_TP2_2": {
    "P": "x**3 + x*y*z + 2*y**3 + y**2*z + 3*z**3",
    "Q": "2*x**3 + x**2*z + x*y**2 - y**3 + z**3",
    "R": "x**3 + x**2*y + x*z**2 + y**3 + y*z**2 - 2*z**3"
  },
  "variables": {
    "source": &#91;
      "x",
      "y",
      "z"
    &#93;,
    "target": &#91;
      "a",
      "b",
      "c"
    &#93;
  }
}
</code></pre>

<a id="source-091293c487a1bfdf"></a>

## `research-notes/lane1-models-20260803-v1/typeiv-hessian-eigensheaf-data.json`

<pre><code class="language-json">
{
  "base_field": "Q",
  "canonical_sha256": "098855025c65b6e4fc62cdd41a0ba8d3a9e3acc8e0cc2e4d1c5c63d96e16042c",
  "certificates": {
    "W_square_mod_radial": true,
    "W_target_degree": 5,
    "Wv_zero": true,
    "chart_binary_hessian_identity": true,
    "h_source_degree": 2,
    "h_target_degree": 4,
    "index_fitting_identity": true,
    "kahler_different_identity": true,
    "local_A2_class_nonfree": true,
    "matrix_factorization_both_orders": true,
    "normalization_conductor_presentation": true,
    "rW_zero": true,
    "r_target_degree": 9,
    "rv_equals_3_branch": true,
    "trace_W_zero": true,
    "universal_binary_hessian_identity": true,
    "universal_conductor_identity": true
  },
  "hessian_covariant": {
    "W": &#91;
      &#91;
        "-a**4*c - 9*a**3*b**2 + 6*a**3*c**2 - 30*a**2*b**3 + 28*a**2*b**2*c - 23*a**2*b*c**2 + 23*a**2*c**3 - 63*a*b**4 - 6*a*b**3*c - 15*a*b**2*c**2 + 9*a*b*c**3 + 27*a*c**4 - 18*b**5 + 28*b**4*c + 37*b**3*c**2 - 10*b**2*c**3 + 8*b*c**4 + 9*c**5",
        "9*a**4*b + a**4*c + 30*a**3*b**2 - 26*a**3*b*c + 3*a**3*c**2 + 63*a**2*b**3 + 3*a**2*b**2*c + 14*a**2*b*c**2 + 2*a**2*c**3 + 18*a*b**4 - 28*a*b**3*c - 19*a*b**2*c**2 + 2*b**4*c - 12*b**3*c**2 - 22*b**2*c**3 - 6*b*c**4 + 2*c**5",
        "a**5 - a**4*b - 6*a**4*c - 2*a**3*b**2 + 20*a**3*b*c - 23*a**3*c**2 + 3*a**2*b**3 + a**2*b**2*c - 11*a**2*b*c**2 - 27*a**2*c**3 - 18*a*b**3*c + 10*a*b**2*c**2 - 8*a*b*c**3 - 9*a*c**4 - 2*b**5 + 12*b**4*c + 22*b**3*c**2 + 6*b**2*c**3 - 2*b*c**4"
      &#93;,
      &#91;
        "-54*a**4*b - 2*a**4*c + 9*a**3*b**2 + 12*a**3*b*c + 27*a**2*b**3 - 30*a**2*b**2*c + 34*a**2*b*c**2 + 6*a*b**4 - 18*a*b**3*c - 15*a*b**2*c**2 + a*b*c**3 + 12*a*c**4 - 4*b**4*c + 7*b**3*c**2 - b**2*c**3 - 6*b*c**4 + 6*c**5",
        "54*a**5 - 9*a**4*b - 9*a**4*c - 27*a**3*b**2 + 29*a**3*b*c - 36*a**3*c**2 - 6*a**2*b**3 + 16*a**2*b**2*c + 33*a**2*b*c**2 - 28*a**2*c**3 + 5*a*b**3*c - 2*a*b**2*c**2 - 12*a*b*c**3 - 27*a*c**4 - 8*b**3*c**2 + 14*b**2*c**3 - 8*b*c**4 - 9*c**5",
        "2*a**5 - 3*a**4*b + a**3*b**2 + 2*a**3*b*c + 2*a**2*b**3 - 18*a**2*b**2*c + 27*a**2*b*c**2 - 12*a**2*c**3 - a*b**4 - 5*a*b**3*c + 13*a*b**2*c**2 + 33*a*b*c**3 - 6*a*c**4 + 8*b**4*c - 14*b**3*c**2 + 8*b**2*c**3 + 9*b*c**4"
      &#93;,
      &#91;
        "-18*a**4*b + 54*a**4*c + 12*a**3*b**2 + 3*a**3*b*c - 10*a**3*c**2 + 6*a**2*b**3 - 39*a**2*b**2*c + 34*a**2*b*c**2 - 30*a**2*c**3 - 18*a*b**4 - 6*a*b**3*c + 10*a*b**2*c**2 + 13*a*b*c**3 - 5*a*c**4 - 6*b**5 + 12*b**4*c + 10*b**3*c**2 - 7*b**2*c**3 + b*c**4",
        "18*a**5 - 12*a**4*b - 12*a**4*c - 6*a**3*b**2 + 3*a**3*b*c - 5*a**3*c**2 + 18*a**2*b**3 - 30*a**2*b**2*c + 34*a**2*b*c**2 - 3*a**2*c**3 + 6*a*b**4 - 75*a*b**3*c - 11*a*b**2*c**2 - 10*a*b*c**3 - 4*a*c**4 - 18*b**4*c + 28*b**3*c**2 + 29*b**2*c**3 + 4*b*c**4",
        "-54*a**5 + 9*a**4*b + 10*a**4*c + 36*a**3*b**2 - 29*a**3*b*c + 30*a**3*c**2 + 36*a**2*b**3 - 44*a**2*b**2*c - 10*a**2*b*c**2 + 5*a**2*c**3 + 63*a*b**4 + a*b**3*c + 17*a*b**2*c**2 + 3*a*b*c**3 + 18*b**5 - 28*b**4*c - 29*b**3*c**2 - 4*b**2*c**3"
      &#93;
    &#93;,
    "correction_row_r": &#91;
      "-2952*a**9 + 1050*a**8*b + 1050*a**8*c + 3279*a**7*b**2 - 3381*a**7*b*c + 3484*a**7*c**2 + 1623*a**6*b**3 - 2883*a**6*b**2*c - 2910*a**6*b*c**2 + 1374*a**6*c**3 + 2142*a**5*b**4 + 1734*a**5*b**3*c - 981*a**5*b**2*c**2 + 2454*a**5*b*c**3 + 25*a**5*c**4 - 783*a**4*b**5 + 414*a**4*b**4*c - 2511*a**4*b**3*c**2 - 1594*a**4*b**2*c**3 + 2668*a**4*b*c**4 - 936*a**4*c**5 - 2127*a**3*b**6 + 3372*a**3*b**5*c - 2763*a**3*b**4*c**2 - 330*a**3*b**3*c**3 - 1285*a**3*b**2*c**4 + 1387*a**3*b*c**5 - 1106*a**3*c**6 - 858*a**2*b**7 + 2844*a**2*b**6*c - 1204*a**2*b**5*c**2 + 1067*a**2*b**4*c**3 - 60*a**2*b**3*c**4 + 201*a**2*b**2*c**5 + 483*a**2*b*c**6 - 471*a**2*c**7 - 102*a*b**8 + 618*a*b**7*c - 441*a*b**6*c**2 - 877*a*b**5*c**3 - 73*a*b**4*c**4 - 105*a*b**3*c**5 + 437*a*b**2*c**6 + 116*a*b*c**7 - 69*a*c**8 + 24*b**8*c - 58*b**7*c**2 - 38*b**6*c**3 + 113*b**5*c**4 + 17*b**4*c**5 + 10*b**3*c**6 + 95*b**2*c**7 + 33*b*c**8",
      "18*a**9 + 456*a**8*b - 66*a**8*c + 1509*a**7*b**2 - 1056*a**7*b*c - 195*a**7*c**2 + 2910*a**6*b**3 + 126*a**6*b**2*c + 607*a**6*b*c**2 - 135*a**6*c**3 - 1035*a**5*b**4 - 654*a**5*b**3*c - 2167*a**5*b**2*c**2 + 606*a**5*b*c**3 + 176*a**5*c**4 - 4173*a**4*b**5 + 4959*a**4*b**4*c - 3657*a**4*b**3*c**2 + 613*a**4*b**2*c**3 - 1161*a**4*b*c**4 + 369*a**4*c**5 - 4902*a**3*b**6 + 6222*a**3*b**5*c - 2890*a**3*b**4*c**2 + 2309*a**3*b**3*c**3 + 1336*a**3*b**2*c**4 - 739*a**3*b*c**5 + 188*a**3*c**6 - 5127*a**2*b**7 + 2199*a**2*b**6*c - 1702*a**2*b**5*c**2 - 1300*a**2*b**4*c**3 + 2066*a**2*b**3*c**4 + 193*a**2*b**2*c**5 + 182*a**2*b*c**6 + 75*a**2*c**7 - 2304*a*b**8 + 3498*a*b**7*c + 4542*a*b**6*c**2 + 995*a*b**5*c**3 + 1330*a*b**4*c**4 - 463*a*b**3*c**5 - 628*a*b**2*c**6 + 70*a*b*c**7 + 26*a*c**8 - 336*b**9 + 1104*b**8*c + 412*b**7*c**2 - 2318*b**6*c**3 - 979*b**5*c**4 + 186*b**4*c**5 - 404*b**3*c**6 - 313*b**2*c**7 - 34*b*c**8",
      "-54*a**9 + 81*a**8*b + 335*a**8*c + 159*a**7*b**2 - 1227*a**7*b*c + 1230*a**7*c**2 - 156*a**6*b**3 + 62*a**6*b**2*c + 693*a**6*b*c**2 + 1067*a**6*c**3 - 138*a**5*b**4 + 1390*a**5*b**3*c - 1676*a**5*b**2*c**2 + 1578*a**5*b*c**3 - 738*a**5*c**4 + 237*a**4*b**5 - 1134*a**4*b**4*c - 385*a**4*b**3*c**2 - 1886*a**4*b**2*c**3 + 1934*a**4*b*c**4 - 1888*a**4*c**5 + 114*a**3*b**6 - 1606*a**3*b**5*c + 2840*a**3*b**4*c**2 - 940*a**3*b**3*c**3 + 838*a**3*b**2*c**4 + 889*a**3*b*c**5 - 1797*a**3*c**6 - 81*a**2*b**7 - 197*a**2*b**6*c + 1613*a**2*b**5*c**2 + 2621*a**2*b**4*c**3 - 784*a**2*b**3*c**4 + 1745*a**2*b**2*c**5 - 611*a**2*b*c**6 - 1200*a**2*c**7 - 30*a*b**8 + 550*a*b**7*c - 405*a*b**6*c**2 + 237*a*b**5*c**3 - 1564*a*b**4*c**4 - 600*a*b**3*c**5 + 1011*a*b**2*c**6 - 551*a*b*c**7 - 510*a*c**8 + 152*b**8*c - 538*b**7*c**2 + 238*b**6*c**3 + 666*b**5*c**4 - 808*b**4*c**5 - 293*b**3*c**6 + 250*b**2*c**7 - 96*b*c**8 - 93*c**9"
    &#93;,
    "definition": "h=-(1/4)*v^T*adj(Hess_x(aP+bQ+cR))*v; S=(1/2)*Hess_x(h); W=-2*S*K_v",
    "h": "a**4*x**2/4 + a**4*x*y + a**4*y**2 - 54*a**4*y*z - 9*a**4*z**2 - a**3*b*x*y/2 - 9*a**3*b*x*z - a**3*b*y**2 + 9*a**3*b*y*z + 6*a**3*b*z**2 - 6*a**3*c*x*y - a**3*c*x*z/2 + 10*a**3*c*y*z + 6*a**3*c*z**2 - a**2*b**2*x**2 - 2*a**2*b**2*x*y - 30*a**2*b**2*x*z + a**2*b**2*y**2/4 + 27*a**2*b**2*y*z + 3*a**2*b**2*z**2 + 2*a**2*b*c*x**2 + 20*a**2*b*c*x*y + 26*a**2*b*c*x*z - 2*a**2*b*c*y**2 - 59*a**2*b*c*y*z/2 - 6*a**2*b*c*z**2 - a**2*c**2*x**2 - 23*a**2*c**2*x*y - 3*a**2*c**2*x*z + 30*a**2*c**2*y*z + 9*a**2*c**2*z**2/4 + a*b**3*x*y - 63*a*b**3*x*z + 6*a*b**3*y*z - 9*a*b**3*z**2 + 5*a*b**2*c*x**2 + 5*a*b**2*c*x*y - 5*a*b**2*c*x*z + a*b**2*c*y**2 - 18*a*b**2*c*y*z + 2*a*b*c**2*x**2 - 13*a*b*c**2*x*y - 10*a*b*c**2*x*z + 2*a*b*c**2*y**2 - 13*a*b*c**2*y*z - 4*a*b*c**2*z**2 - 27*a*c**3*x*y - 4*a*c**3*x*z - 6*a*c**3*y**2 + 5*a*c**3*y*z + b**4*x**2 - 18*b**4*x*z - 3*b**4*z**2 - 6*b**3*c*x**2 - 8*b**3*c*x*y + 28*b**3*c*x*z - 4*b**3*c*y*z + 6*b**3*c*z**2 - 11*b**2*c**2*x**2 + 14*b**2*c**2*x*y + 29*b**2*c**2*x*z + 7*b**2*c**2*y*z + 3*b**2*c**2*z**2 - 3*b*c**3*x**2 - 8*b*c**3*x*y + 4*b*c**3*x*z + 3*b*c**3*y**2 - b*c**3*y*z + c**4*x**2 - 9*c**4*x*y - 3*c**4*y**2"
  },
  "index_fitting": {
    "Q_scalar_conductor": "(rho)",
    "annihilator": "(branch)",
    "ideal": "branch*(a,b,c)",
    "maximal_minors": &#91;
      "0",
      "-2952*a**11 + 1068*a**10*b + 996*a**10*c + 3735*a**9*b**2 - 3366*a**9*b*c + 3819*a**9*c**2 + 3132*a**8*b**3 - 3780*a**8*b**2*c - 4332*a**8*b*c**2 + 2604*a**8*c**3 + 5052*a**7*b**4 + 1704*a**7*b**3*c - 312*a**7*b**2*c**2 + 3012*a**7*b*c**3 + 1092*a**7*c**4 - 1818*a**6*b**5 - 378*a**6*b**4*c - 3288*a**6*b**3*c**2 - 2664*a**6*b**2*c**3 + 4422*a**6*b*c**4 - 1674*a**6*c**5 - 6300*a**5*b**6 + 8568*a**5*b**5*c - 7554*a**5*b**4*c**2 - 102*a**5*b**3*c**3 - 4332*a**5*b**2*c**4 + 3690*a**5*b*c**5 - 2994*a**5*c**6 - 5760*a**4*b**7 + 9180*a**4*b**6*c - 5700*a**4*b**5*c**2 + 6216*a**4*b**4*c**3 + 336*a**4*b**3*c**4 + 300*a**4*b**2*c**5 + 1560*a**4*b*c**6 - 2268*a**4*c**7 - 5229*a**3*b**8 + 2736*a**3*b**7*c - 2340*a**3*b**6*c**2 - 564*a**3*b**5*c**3 + 4614*a**3*b**4*c**4 - 696*a**3*b**3*c**5 + 2364*a**3*b**2*c**6 - 420*a**3*b*c**7 - 1269*a**3*c**8 - 2304*a**2*b**9 + 3492*a**2*b**8*c + 5034*a**2*b**7*c**2 + 552*a**2*b**6*c**3 + 1680*a**2*b**5*c**4 - 2010*a**2*b**4*c**5 - 1218*a**2*b**3*c**6 + 1176*a**2*b**2*c**7 - 492*a**2*b*c**8 - 510*a**2*c**9 - 336*a*b**10 + 1104*a*b**9*c + 564*a*b**8*c**2 - 2856*a*b**7*c**3 - 741*a*b**6*c**4 + 852*a*b**5*c**5 - 1212*a*b**4*c**6 - 606*a*b**3*c**7 + 216*a*b**2*c**8 - 96*a*b*c**9 - 93*a*c**10",
      "2952*a**10*b - 1068*a**9*b**2 - 996*a**9*b*c - 3735*a**8*b**3 + 3366*a**8*b**2*c - 3819*a**8*b*c**2 - 3132*a**7*b**4 + 3780*a**7*b**3*c + 4332*a**7*b**2*c**2 - 2604*a**7*b*c**3 - 5052*a**6*b**5 - 1704*a**6*b**4*c + 312*a**6*b**3*c**2 - 3012*a**6*b**2*c**3 - 1092*a**6*b*c**4 + 1818*a**5*b**6 + 378*a**5*b**5*c + 3288*a**5*b**4*c**2 + 2664*a**5*b**3*c**3 - 4422*a**5*b**2*c**4 + 1674*a**5*b*c**5 + 6300*a**4*b**7 - 8568*a**4*b**6*c + 7554*a**4*b**5*c**2 + 102*a**4*b**4*c**3 + 4332*a**4*b**3*c**4 - 3690*a**4*b**2*c**5 + 2994*a**4*b*c**6 + 5760*a**3*b**8 - 9180*a**3*b**7*c + 5700*a**3*b**6*c**2 - 6216*a**3*b**5*c**3 - 336*a**3*b**4*c**4 - 300*a**3*b**3*c**5 - 1560*a**3*b**2*c**6 + 2268*a**3*b*c**7 + 5229*a**2*b**9 - 2736*a**2*b**8*c + 2340*a**2*b**7*c**2 + 564*a**2*b**6*c**3 - 4614*a**2*b**5*c**4 + 696*a**2*b**4*c**5 - 2364*a**2*b**3*c**6 + 420*a**2*b**2*c**7 + 1269*a**2*b*c**8 + 2304*a*b**10 - 3492*a*b**9*c - 5034*a*b**8*c**2 - 552*a*b**7*c**3 - 1680*a*b**6*c**4 + 2010*a*b**5*c**5 + 1218*a*b**4*c**6 - 1176*a*b**3*c**7 + 492*a*b**2*c**8 + 510*a*b*c**9 + 336*b**11 - 1104*b**10*c - 564*b**9*c**2 + 2856*b**8*c**3 + 741*b**7*c**4 - 852*b**6*c**5 + 1212*b**5*c**6 + 606*b**4*c**7 - 216*b**3*c**8 + 96*b**2*c**9 + 93*b*c**10",
      "-2952*a**10*c + 1068*a**9*b*c + 996*a**9*c**2 + 3735*a**8*b**2*c - 3366*a**8*b*c**2 + 3819*a**8*c**3 + 3132*a**7*b**3*c - 3780*a**7*b**2*c**2 - 4332*a**7*b*c**3 + 2604*a**7*c**4 + 5052*a**6*b**4*c + 1704*a**6*b**3*c**2 - 312*a**6*b**2*c**3 + 3012*a**6*b*c**4 + 1092*a**6*c**5 - 1818*a**5*b**5*c - 378*a**5*b**4*c**2 - 3288*a**5*b**3*c**3 - 2664*a**5*b**2*c**4 + 4422*a**5*b*c**5 - 1674*a**5*c**6 - 6300*a**4*b**6*c + 8568*a**4*b**5*c**2 - 7554*a**4*b**4*c**3 - 102*a**4*b**3*c**4 - 4332*a**4*b**2*c**5 + 3690*a**4*b*c**6 - 2994*a**4*c**7 - 5760*a**3*b**7*c + 9180*a**3*b**6*c**2 - 5700*a**3*b**5*c**3 + 6216*a**3*b**4*c**4 + 336*a**3*b**3*c**5 + 300*a**3*b**2*c**6 + 1560*a**3*b*c**7 - 2268*a**3*c**8 - 5229*a**2*b**8*c + 2736*a**2*b**7*c**2 - 2340*a**2*b**6*c**3 - 564*a**2*b**5*c**4 + 4614*a**2*b**4*c**5 - 696*a**2*b**3*c**6 + 2364*a**2*b**2*c**7 - 420*a**2*b*c**8 - 1269*a**2*c**9 - 2304*a*b**9*c + 3492*a*b**8*c**2 + 5034*a*b**7*c**3 + 552*a*b**6*c**4 + 1680*a*b**5*c**5 - 2010*a*b**4*c**6 - 1218*a*b**3*c**7 + 1176*a*b**2*c**8 - 492*a*b*c**9 - 510*a*c**10 - 336*b**10*c + 1104*b**9*c**2 + 564*b**8*c**3 - 2856*b**7*c**4 - 741*b**6*c**5 + 852*b**5*c**6 - 1212*b**4*c**7 - 606*b**3*c**8 + 216*b**2*c**9 - 96*b*c**10 - 93*c**11"
    &#93;,
    "presentation": "coker(&#91;v|W&#93;)"
  },
  "input_file": "typeiv-explicit-net-data.json",
  "input_sha256": "ecc1248b165e14040c564e822133d83211288f72427e56d17958537bde064731",
  "local_models": {
    "A2_coordinates": {
      "U": "-9*q + rho",
      "V": "9*q + rho",
      "equation": "U*V=12*p^3"
    },
    "W_depressed": &#91;
      &#91;
        "9*q",
        "-6*p"
      &#93;,
      &#91;
        "-2*p**2",
        "-9*q"
      &#93;
    &#93;,
    "binary_hessian_coefficients": {
      "H0": "B^2-3*A*C",
      "H1": "B*C-9*A*D",
      "H2": "C^2-3*B*D"
    },
    "binary_hessian_matrix": "&#91;&#91;-H1,2*H0&#93;,&#91;-2*H2,H1&#93;&#93;",
    "conductor_order_in_normalization": "(rho,3*t^2+p)",
    "depressed_cubic": "t^3+p*t+q",
    "discriminant": "-4*p**3 - 27*q**2",
    "kahler_different_T_over_Q": "(u^3,v^3,u^2*v^2)"
  },
  "matrix_factorization": {
    "Phi": &#91;
      &#91;
        "a**4*c + 9*a**3*b**2 - 6*a**3*c**2 + 30*a**2*b**3 - 28*a**2*b**2*c + 23*a**2*b*c**2 - 23*a**2*c**3 + 63*a*b**4 + 6*a*b**3*c + 15*a*b**2*c**2 - 9*a*b*c**3 - 27*a*c**4 + 18*b**5 - 28*b**4*c - 37*b**3*c**2 + 10*b**2*c**3 - 8*b*c**4 - 9*c**5 + rho",
        "-9*a**4*b - a**4*c - 30*a**3*b**2 + 26*a**3*b*c - 3*a**3*c**2 - 63*a**2*b**3 - 3*a**2*b**2*c - 14*a**2*b*c**2 - 2*a**2*c**3 - 18*a*b**4 + 28*a*b**3*c + 19*a*b**2*c**2 - 2*b**4*c + 12*b**3*c**2 + 22*b**2*c**3 + 6*b*c**4 - 2*c**5",
        "-a**5 + a**4*b + 6*a**4*c + 2*a**3*b**2 - 20*a**3*b*c + 23*a**3*c**2 - 3*a**2*b**3 - a**2*b**2*c + 11*a**2*b*c**2 + 27*a**2*c**3 + 18*a*b**3*c - 10*a*b**2*c**2 + 8*a*b*c**3 + 9*a*c**4 + 2*b**5 - 12*b**4*c - 22*b**3*c**2 - 6*b**2*c**3 + 2*b*c**4",
        "a"
      &#93;,
      &#91;
        "54*a**4*b + 2*a**4*c - 9*a**3*b**2 - 12*a**3*b*c - 27*a**2*b**3 + 30*a**2*b**2*c - 34*a**2*b*c**2 - 6*a*b**4 + 18*a*b**3*c + 15*a*b**2*c**2 - a*b*c**3 - 12*a*c**4 + 4*b**4*c - 7*b**3*c**2 + b**2*c**3 + 6*b*c**4 - 6*c**5",
        "-54*a**5 + 9*a**4*b + 9*a**4*c + 27*a**3*b**2 - 29*a**3*b*c + 36*a**3*c**2 + 6*a**2*b**3 - 16*a**2*b**2*c - 33*a**2*b*c**2 + 28*a**2*c**3 - 5*a*b**3*c + 2*a*b**2*c**2 + 12*a*b*c**3 + 27*a*c**4 + 8*b**3*c**2 - 14*b**2*c**3 + 8*b*c**4 + 9*c**5 + rho",
        "-2*a**5 + 3*a**4*b - a**3*b**2 - 2*a**3*b*c - 2*a**2*b**3 + 18*a**2*b**2*c - 27*a**2*b*c**2 + 12*a**2*c**3 + a*b**4 + 5*a*b**3*c - 13*a*b**2*c**2 - 33*a*b*c**3 + 6*a*c**4 - 8*b**4*c + 14*b**3*c**2 - 8*b**2*c**3 - 9*b*c**4",
        "b"
      &#93;,
      &#91;
        "18*a**4*b - 54*a**4*c - 12*a**3*b**2 - 3*a**3*b*c + 10*a**3*c**2 - 6*a**2*b**3 + 39*a**2*b**2*c - 34*a**2*b*c**2 + 30*a**2*c**3 + 18*a*b**4 + 6*a*b**3*c - 10*a*b**2*c**2 - 13*a*b*c**3 + 5*a*c**4 + 6*b**5 - 12*b**4*c - 10*b**3*c**2 + 7*b**2*c**3 - b*c**4",
        "-18*a**5 + 12*a**4*b + 12*a**4*c + 6*a**3*b**2 - 3*a**3*b*c + 5*a**3*c**2 - 18*a**2*b**3 + 30*a**2*b**2*c - 34*a**2*b*c**2 + 3*a**2*c**3 - 6*a*b**4 + 75*a*b**3*c + 11*a*b**2*c**2 + 10*a*b*c**3 + 4*a*c**4 + 18*b**4*c - 28*b**3*c**2 - 29*b**2*c**3 - 4*b*c**4",
        "54*a**5 - 9*a**4*b - 10*a**4*c - 36*a**3*b**2 + 29*a**3*b*c - 30*a**3*c**2 - 36*a**2*b**3 + 44*a**2*b**2*c + 10*a**2*b*c**2 - 5*a**2*c**3 - 63*a*b**4 - a*b**3*c - 17*a*b**2*c**2 - 3*a*b*c**3 - 18*b**5 + 28*b**4*c + 29*b**3*c**2 + 4*b**2*c**3 + rho",
        "c"
      &#93;,
      &#91;
        "2952*a**9 - 1050*a**8*b - 1050*a**8*c - 3279*a**7*b**2 + 3381*a**7*b*c - 3484*a**7*c**2 - 1623*a**6*b**3 + 2883*a**6*b**2*c + 2910*a**6*b*c**2 - 1374*a**6*c**3 - 2142*a**5*b**4 - 1734*a**5*b**3*c + 981*a**5*b**2*c**2 - 2454*a**5*b*c**3 - 25*a**5*c**4 + 783*a**4*b**5 - 414*a**4*b**4*c + 2511*a**4*b**3*c**2 + 1594*a**4*b**2*c**3 - 2668*a**4*b*c**4 + 936*a**4*c**5 + 2127*a**3*b**6 - 3372*a**3*b**5*c + 2763*a**3*b**4*c**2 + 330*a**3*b**3*c**3 + 1285*a**3*b**2*c**4 - 1387*a**3*b*c**5 + 1106*a**3*c**6 + 858*a**2*b**7 - 2844*a**2*b**6*c + 1204*a**2*b**5*c**2 - 1067*a**2*b**4*c**3 + 60*a**2*b**3*c**4 - 201*a**2*b**2*c**5 - 483*a**2*b*c**6 + 471*a**2*c**7 + 102*a*b**8 - 618*a*b**7*c + 441*a*b**6*c**2 + 877*a*b**5*c**3 + 73*a*b**4*c**4 + 105*a*b**3*c**5 - 437*a*b**2*c**6 - 116*a*b*c**7 + 69*a*c**8 - 24*b**8*c + 58*b**7*c**2 + 38*b**6*c**3 - 113*b**5*c**4 - 17*b**4*c**5 - 10*b**3*c**6 - 95*b**2*c**7 - 33*b*c**8",
        "-18*a**9 - 456*a**8*b + 66*a**8*c - 1509*a**7*b**2 + 1056*a**7*b*c + 195*a**7*c**2 - 2910*a**6*b**3 - 126*a**6*b**2*c - 607*a**6*b*c**2 + 135*a**6*c**3 + 1035*a**5*b**4 + 654*a**5*b**3*c + 2167*a**5*b**2*c**2 - 606*a**5*b*c**3 - 176*a**5*c**4 + 4173*a**4*b**5 - 4959*a**4*b**4*c + 3657*a**4*b**3*c**2 - 613*a**4*b**2*c**3 + 1161*a**4*b*c**4 - 369*a**4*c**5 + 4902*a**3*b**6 - 6222*a**3*b**5*c + 2890*a**3*b**4*c**2 - 2309*a**3*b**3*c**3 - 1336*a**3*b**2*c**4 + 739*a**3*b*c**5 - 188*a**3*c**6 + 5127*a**2*b**7 - 2199*a**2*b**6*c + 1702*a**2*b**5*c**2 + 1300*a**2*b**4*c**3 - 2066*a**2*b**3*c**4 - 193*a**2*b**2*c**5 - 182*a**2*b*c**6 - 75*a**2*c**7 + 2304*a*b**8 - 3498*a*b**7*c - 4542*a*b**6*c**2 - 995*a*b**5*c**3 - 1330*a*b**4*c**4 + 463*a*b**3*c**5 + 628*a*b**2*c**6 - 70*a*b*c**7 - 26*a*c**8 + 336*b**9 - 1104*b**8*c - 412*b**7*c**2 + 2318*b**6*c**3 + 979*b**5*c**4 - 186*b**4*c**5 + 404*b**3*c**6 + 313*b**2*c**7 + 34*b*c**8",
        "54*a**9 - 81*a**8*b - 335*a**8*c - 159*a**7*b**2 + 1227*a**7*b*c - 1230*a**7*c**2 + 156*a**6*b**3 - 62*a**6*b**2*c - 693*a**6*b*c**2 - 1067*a**6*c**3 + 138*a**5*b**4 - 1390*a**5*b**3*c + 1676*a**5*b**2*c**2 - 1578*a**5*b*c**3 + 738*a**5*c**4 - 237*a**4*b**5 + 1134*a**4*b**4*c + 385*a**4*b**3*c**2 + 1886*a**4*b**2*c**3 - 1934*a**4*b*c**4 + 1888*a**4*c**5 - 114*a**3*b**6 + 1606*a**3*b**5*c - 2840*a**3*b**4*c**2 + 940*a**3*b**3*c**3 - 838*a**3*b**2*c**4 - 889*a**3*b*c**5 + 1797*a**3*c**6 + 81*a**2*b**7 + 197*a**2*b**6*c - 1613*a**2*b**5*c**2 - 2621*a**2*b**4*c**3 + 784*a**2*b**3*c**4 - 1745*a**2*b**2*c**5 + 611*a**2*b*c**6 + 1200*a**2*c**7 + 30*a*b**8 - 550*a*b**7*c + 405*a*b**6*c**2 - 237*a*b**5*c**3 + 1564*a*b**4*c**4 + 600*a*b**3*c**5 - 1011*a*b**2*c**6 + 551*a*b*c**7 + 510*a*c**8 - 152*b**8*c + 538*b**7*c**2 - 238*b**6*c**3 - 666*b**5*c**4 + 808*b**4*c**5 + 293*b**3*c**6 - 250*b**2*c**7 + 96*b*c**8 + 93*c**9",
        "rho"
      &#93;
    &#93;,
    "Phi_block_form": "&#91;&#91;rho*I-W, v&#93;,&#91;-r,rho&#93;&#93;",
    "Psi": &#91;
      &#91;
        "-a**4*c - 9*a**3*b**2 + 6*a**3*c**2 - 30*a**2*b**3 + 28*a**2*b**2*c - 23*a**2*b*c**2 + 23*a**2*c**3 - 63*a*b**4 - 6*a*b**3*c - 15*a*b**2*c**2 + 9*a*b*c**3 + 27*a*c**4 - 18*b**5 + 28*b**4*c + 37*b**3*c**2 - 10*b**2*c**3 + 8*b*c**4 + 9*c**5 + rho",
        "9*a**4*b + a**4*c + 30*a**3*b**2 - 26*a**3*b*c + 3*a**3*c**2 + 63*a**2*b**3 + 3*a**2*b**2*c + 14*a**2*b*c**2 + 2*a**2*c**3 + 18*a*b**4 - 28*a*b**3*c - 19*a*b**2*c**2 + 2*b**4*c - 12*b**3*c**2 - 22*b**2*c**3 - 6*b*c**4 + 2*c**5",
        "a**5 - a**4*b - 6*a**4*c - 2*a**3*b**2 + 20*a**3*b*c - 23*a**3*c**2 + 3*a**2*b**3 + a**2*b**2*c - 11*a**2*b*c**2 - 27*a**2*c**3 - 18*a*b**3*c + 10*a*b**2*c**2 - 8*a*b*c**3 - 9*a*c**4 - 2*b**5 + 12*b**4*c + 22*b**3*c**2 + 6*b**2*c**3 - 2*b*c**4",
        "-a"
      &#93;,
      &#91;
        "-54*a**4*b - 2*a**4*c + 9*a**3*b**2 + 12*a**3*b*c + 27*a**2*b**3 - 30*a**2*b**2*c + 34*a**2*b*c**2 + 6*a*b**4 - 18*a*b**3*c - 15*a*b**2*c**2 + a*b*c**3 + 12*a*c**4 - 4*b**4*c + 7*b**3*c**2 - b**2*c**3 - 6*b*c**4 + 6*c**5",
        "54*a**5 - 9*a**4*b - 9*a**4*c - 27*a**3*b**2 + 29*a**3*b*c - 36*a**3*c**2 - 6*a**2*b**3 + 16*a**2*b**2*c + 33*a**2*b*c**2 - 28*a**2*c**3 + 5*a*b**3*c - 2*a*b**2*c**2 - 12*a*b*c**3 - 27*a*c**4 - 8*b**3*c**2 + 14*b**2*c**3 - 8*b*c**4 - 9*c**5 + rho",
        "2*a**5 - 3*a**4*b + a**3*b**2 + 2*a**3*b*c + 2*a**2*b**3 - 18*a**2*b**2*c + 27*a**2*b*c**2 - 12*a**2*c**3 - a*b**4 - 5*a*b**3*c + 13*a*b**2*c**2 + 33*a*b*c**3 - 6*a*c**4 + 8*b**4*c - 14*b**3*c**2 + 8*b**2*c**3 + 9*b*c**4",
        "-b"
      &#93;,
      &#91;
        "-18*a**4*b + 54*a**4*c + 12*a**3*b**2 + 3*a**3*b*c - 10*a**3*c**2 + 6*a**2*b**3 - 39*a**2*b**2*c + 34*a**2*b*c**2 - 30*a**2*c**3 - 18*a*b**4 - 6*a*b**3*c + 10*a*b**2*c**2 + 13*a*b*c**3 - 5*a*c**4 - 6*b**5 + 12*b**4*c + 10*b**3*c**2 - 7*b**2*c**3 + b*c**4",
        "18*a**5 - 12*a**4*b - 12*a**4*c - 6*a**3*b**2 + 3*a**3*b*c - 5*a**3*c**2 + 18*a**2*b**3 - 30*a**2*b**2*c + 34*a**2*b*c**2 - 3*a**2*c**3 + 6*a*b**4 - 75*a*b**3*c - 11*a*b**2*c**2 - 10*a*b*c**3 - 4*a*c**4 - 18*b**4*c + 28*b**3*c**2 + 29*b**2*c**3 + 4*b*c**4",
        "-54*a**5 + 9*a**4*b + 10*a**4*c + 36*a**3*b**2 - 29*a**3*b*c + 30*a**3*c**2 + 36*a**2*b**3 - 44*a**2*b**2*c - 10*a**2*b*c**2 + 5*a**2*c**3 + 63*a*b**4 + a*b**3*c + 17*a*b**2*c**2 + 3*a*b*c**3 + 18*b**5 - 28*b**4*c - 29*b**3*c**2 - 4*b**2*c**3 + rho",
        "-c"
      &#93;,
      &#91;
        "-2952*a**9 + 1050*a**8*b + 1050*a**8*c + 3279*a**7*b**2 - 3381*a**7*b*c + 3484*a**7*c**2 + 1623*a**6*b**3 - 2883*a**6*b**2*c - 2910*a**6*b*c**2 + 1374*a**6*c**3 + 2142*a**5*b**4 + 1734*a**5*b**3*c - 981*a**5*b**2*c**2 + 2454*a**5*b*c**3 + 25*a**5*c**4 - 783*a**4*b**5 + 414*a**4*b**4*c - 2511*a**4*b**3*c**2 - 1594*a**4*b**2*c**3 + 2668*a**4*b*c**4 - 936*a**4*c**5 - 2127*a**3*b**6 + 3372*a**3*b**5*c - 2763*a**3*b**4*c**2 - 330*a**3*b**3*c**3 - 1285*a**3*b**2*c**4 + 1387*a**3*b*c**5 - 1106*a**3*c**6 - 858*a**2*b**7 + 2844*a**2*b**6*c - 1204*a**2*b**5*c**2 + 1067*a**2*b**4*c**3 - 60*a**2*b**3*c**4 + 201*a**2*b**2*c**5 + 483*a**2*b*c**6 - 471*a**2*c**7 - 102*a*b**8 + 618*a*b**7*c - 441*a*b**6*c**2 - 877*a*b**5*c**3 - 73*a*b**4*c**4 - 105*a*b**3*c**5 + 437*a*b**2*c**6 + 116*a*b*c**7 - 69*a*c**8 + 24*b**8*c - 58*b**7*c**2 - 38*b**6*c**3 + 113*b**5*c**4 + 17*b**4*c**5 + 10*b**3*c**6 + 95*b**2*c**7 + 33*b*c**8",
        "18*a**9 + 456*a**8*b - 66*a**8*c + 1509*a**7*b**2 - 1056*a**7*b*c - 195*a**7*c**2 + 2910*a**6*b**3 + 126*a**6*b**2*c + 607*a**6*b*c**2 - 135*a**6*c**3 - 1035*a**5*b**4 - 654*a**5*b**3*c - 2167*a**5*b**2*c**2 + 606*a**5*b*c**3 + 176*a**5*c**4 - 4173*a**4*b**5 + 4959*a**4*b**4*c - 3657*a**4*b**3*c**2 + 613*a**4*b**2*c**3 - 1161*a**4*b*c**4 + 369*a**4*c**5 - 4902*a**3*b**6 + 6222*a**3*b**5*c - 2890*a**3*b**4*c**2 + 2309*a**3*b**3*c**3 + 1336*a**3*b**2*c**4 - 739*a**3*b*c**5 + 188*a**3*c**6 - 5127*a**2*b**7 + 2199*a**2*b**6*c - 1702*a**2*b**5*c**2 - 1300*a**2*b**4*c**3 + 2066*a**2*b**3*c**4 + 193*a**2*b**2*c**5 + 182*a**2*b*c**6 + 75*a**2*c**7 - 2304*a*b**8 + 3498*a*b**7*c + 4542*a*b**6*c**2 + 995*a*b**5*c**3 + 1330*a*b**4*c**4 - 463*a*b**3*c**5 - 628*a*b**2*c**6 + 70*a*b*c**7 + 26*a*c**8 - 336*b**9 + 1104*b**8*c + 412*b**7*c**2 - 2318*b**6*c**3 - 979*b**5*c**4 + 186*b**4*c**5 - 404*b**3*c**6 - 313*b**2*c**7 - 34*b*c**8",
        "-54*a**9 + 81*a**8*b + 335*a**8*c + 159*a**7*b**2 - 1227*a**7*b*c + 1230*a**7*c**2 - 156*a**6*b**3 + 62*a**6*b**2*c + 693*a**6*b*c**2 + 1067*a**6*c**3 - 138*a**5*b**4 + 1390*a**5*b**3*c - 1676*a**5*b**2*c**2 + 1578*a**5*b*c**3 - 738*a**5*c**4 + 237*a**4*b**5 - 1134*a**4*b**4*c - 385*a**4*b**3*c**2 - 1886*a**4*b**2*c**3 + 1934*a**4*b*c**4 - 1888*a**4*c**5 + 114*a**3*b**6 - 1606*a**3*b**5*c + 2840*a**3*b**4*c**2 - 940*a**3*b**3*c**3 + 838*a**3*b**2*c**4 + 889*a**3*b*c**5 - 1797*a**3*c**6 - 81*a**2*b**7 - 197*a**2*b**6*c + 1613*a**2*b**5*c**2 + 2621*a**2*b**4*c**3 - 784*a**2*b**3*c**4 + 1745*a**2*b**2*c**5 - 611*a**2*b*c**6 - 1200*a**2*c**7 - 30*a*b**8 + 550*a*b**7*c - 405*a*b**6*c**2 + 237*a*b**5*c**3 - 1564*a*b**4*c**4 - 600*a*b**3*c**5 + 1011*a*b**2*c**6 - 551*a*b*c**7 - 510*a*c**8 + 152*b**8*c - 538*b**7*c**2 + 238*b**6*c**3 + 666*b**5*c**4 - 808*b**4*c**5 - 293*b**3*c**6 + 250*b**2*c**7 - 96*b*c**8 - 93*c**9",
        "rho"
      &#93;
    &#93;,
    "Psi_block_form": "&#91;&#91;rho*I+W,-v&#93;,&#91;r,rho&#93;&#93;",
    "determinant": "8714304*a**20 - 6305472*a**19*b - 5880384*a**19*c - 20910816*a**18*b**2 + 22000320*a**18*b*c - 21555360*a**18*c**2 - 10513368*a**17*b**3 + 22567464*a**17*b**2*c + 27028440*a**17*b*c**2 - 7766568*a**17*c**3 - 9186831*a**16*b**4 - 37039572*a**16*b**3*c + 24917022*a**16*b**2*c**2 - 46559556*a**16*b*c**3 + 13324761*a**16*c**4 + 44920584*a**15*b**5 - 33386184*a**15*b**4*c + 39149424*a**15*b**3*c**2 + 41283648*a**15*b**2*c**3 - 68393016*a**15*b*c**4 + 31947912*a**15*c**5 + 80859816*a**14*b**6 - 99973440*a**14*b**5*c + 48760632*a**14*b**4*c**2 + 75038760*a**14*b**3*c**3 + 14292216*a**14*b**2*c**4 - 23459544*a**14*b*c**5 + 29463480*a**14*c**6 + 38615508*a**13*b**7 - 66551220*a**13*b**6*c - 59924772*a**13*b**5*c**2 - 19843884*a**13*b**4*c**3 + 10059732*a**13*b**3*c**4 - 101116404*a**13*b**2*c**5 + 43015068*a**13*b*c**6 + 327348*a**13*c**7 - 14357592*a**12*b**8 + 126989280*a**12*b**7*c - 144536868*a**12*b**6*c**2 + 152133588*a**12*b**5*c**3 - 7758252*a**12*b**4*c**4 + 25250328*a**12*b**3*c**5 - 121461516*a**12*b**2*c**6 + 93194100*a**12*b*c**7 - 27419580*a**12*c**8 - 98425800*a**11*b**9 + 173444976*a**11*b**8*c - 268527384*a**11*b**7*c**2 + 46385208*a**11*b**6*c**3 + 31051080*a**11*b**5*c**4 + 63620856*a**11*b**4*c**5 - 18288720*a**11*b**3*c**6 - 38315664*a**11*b**2*c**7 + 71272008*a**11*b*c**8 - 36088560*a**11*c**9 - 138428946*a**10*b**10 + 219515076*a**10*b**9*c - 147756402*a**10*b**8*c**2 - 24898824*a**10*b**7*c**3 + 76955940*a**10*b**6*c**4 - 114694128*a**10*b**5*c**5 + 42300324*a**10*b**4*c**6 - 98931096*a**10*b**3*c**7 + 59722182*a**10*b**2*c**8 + 6824988*a**10*b*c**9 - 25707834*a**10*c**10 - 5904*a**10*rho**2 - 85975272*a**9*b**11 + 146688336*a**9*b**10*c + 49568508*a**9*b**9*c**2 - 58591080*a**9*b**8*c**3 + 142692300*a**9*b**7*c**4 + 45347940*a**9*b**6*c**5 - 23264748*a**9*b**5*c**6 + 30761172*a**9*b**4*c**7 - 94625460*a**9*b**3*c**8 + 108811980*a**9*b**2*c**9 - 40995648*a**9*b*c**10 + 2136*a**9*b*rho**2 - 5618988*a**9*c**11 + 1992*a**9*c*rho**2 - 9142632*a**8*b**12 - 77355648*a**8*b**11*c + 228507624*a**8*b**10*c**2 - 316562904*a**8*b**9*c**3 + 91748718*a**8*b**8*c**4 - 43960212*a**8*b**7*c**5 + 29604654*a**8*b**6*c**6 + 54880668*a**8*b**5*c**7 + 9968760*a**8*b**4*c**8 - 37377612*a**8*b**3*c**9 + 83701278*a**8*b**2*c**10 + 7470*a**8*b**2*rho**2 - 54189396*a**8*b*c**11 - 6732*a**8*b*c*rho**2 + 10419390*a**8*c**12 + 7638*a**8*c**2*rho**2 + 66204324*a**7*b**13 - 183479580*a**7*b**12*c + 419276016*a**7*b**11*c**2 - 326619072*a**7*b**10*c**3 + 224177796*a**7*b**9*c**4 - 94248540*a**7*b**8*c**5 + 37130760*a**7*b**7*c**6 - 103166136*a**7*b**6*c**7 + 62619084*a**7*b**5*c**8 - 56458116*a**7*b**4*c**9 + 19077768*a**7*b**3*c**10 + 6264*a**7*b**3*rho**2 + 27081000*a**7*b**2*c**11 - 7560*a**7*b**2*c*rho**2 - 39736980*a**7*b*c**12 - 8664*a**7*b*c**2*rho**2 + 16231212*a**7*c**13 + 5208*a**7*c**3*rho**2 + 104045400*a**6*b**14 - 230776704*a**6*b**13*c + 309182508*a**6*b**12*c**2 - 295669260*a**6*b**11*c**3 + 64775664*a**6*b**10*c**4 - 5752476*a**6*b**9*c**5 - 17248428*a**6*b**8*c**6 + 49588848*a**6*b**7*c**7 - 75472992*a**6*b**6*c**8 + 45312264*a**6*b**5*c**9 - 75432996*a**6*b**4*c**10 + 10104*a**6*b**4*rho**2 + 45097812*a**6*b**3*c**11 + 3408*a**6*b**3*c*rho**2 - 10807560*a**6*b**2*c**12 - 624*a**6*b**2*c**2*rho**2 - 17559540*a**6*b*c**13 + 6024*a**6*b*c**3*rho**2 + 14246964*a**6*c**14 + 2184*a**6*c**4*rho**2 + 90490176*a**5*b**15 - 214763832*a**5*b**14*c + 167343912*a**5*b**13*c**2 - 101153808*a**5*b**12*c**3 - 82554516*a**5*b**11*c**4 + 90387684*a**5*b**10*c**5 - 139362192*a**5*b**9*c**6 + 124120800*a**5*b**8*c**7 - 34994412*a**5*b**7*c**8 + 49662180*a**5*b**6*c**9 + 130788*a**5*b**5*c**10 - 3636*a**5*b**5*rho**2 - 38827980*a**5*b**4*c**11 - 756*a**5*b**4*c*rho**2 + 34829208*a**5*b**3*c**12 - 6576*a**5*b**3*c**2*rho**2 - 20125800*a**5*b**2*c**13 - 5328*a**5*b**2*c**3*rho**2 - 3372948*a**5*b*c**14 + 8844*a**5*b*c**4*rho**2 + 9121428*a**5*c**15 - 3348*a**5*c**5*rho**2 + 58118121*a**4*b**16 - 130810464*a**4*b**15*c + 81232488*a**4*b**14*c**2 + 39746520*a**4*b**13*c**3 - 116044884*a**4*b**12*c**4 + 153975888*a**4*b**11*c**5 - 39757140*a**4*b**10*c**6 + 44449812*a**4*b**9*c**7 + 26462718*a**4*b**8*c**8 - 48663756*a**4*b**7*c**9 + 57903228*a**4*b**6*c**10 - 12600*a**4*b**6*rho**2 - 28853064*a**4*b**5*c**11 + 17136*a**4*b**5*c*rho**2 - 3846960*a**4*b**4*c**12 - 15108*a**4*b**4*c**2*rho**2 + 14410260*a**4*b**3*c**13 - 204*a**4*b**3*c**3*rho**2 - 14194944*a**4*b**2*c**14 - 8664*a**4*b**2*c**4*rho**2 + 1594980*a**4*b*c**15 + 7380*a**4*b*c**5*rho**2 + 4480605*a**4*c**16 - 5988*a**4*c**6*rho**2 + 27965952*a**3*b**17 - 68013864*a**3*b**16*c - 5152068*a**3*b**15*c**2 + 34522992*a**3*b**14*c**3 - 100138608*a**3*b**13*c**4 + 74073708*a**3*b**12*c**5 + 26493300*a**3*b**11*c**6 - 25728048*a**3*b**10*c**7 + 66332376*a**3*b**9*c**8 - 47285244*a**3*b**8*c**9 - 15901164*a**3*b**7*c**10 - 11520*a**3*b**7*rho**2 + 10131120*a**3*b**6*c**11 + 18360*a**3*b**6*c*rho**2 - 21933864*a**3*b**5*c**12 - 11400*a**3*b**5*c**2*rho**2 + 10179036*a**3*b**4*c**13 + 12432*a**3*b**4*c**3*rho**2 + 3789828*a**3*b**3*c**14 + 672*a**3*b**3*c**4*rho**2 - 6317784*a**3*b**2*c**15 + 600*a**3*b**2*c**5*rho**2 + 1822392*a**3*b*c**16 + 3120*a**3*b*c**6*rho**2 + 1716228*a**3*c**17 - 4536*a**3*c**7*rho**2 + 8822304*a**2*b**18 - 29475360*a**2*b**17*c - 9287352*a**2*b**16*c**2 + 60780384*a**2*b**15*c**3 + 6590790*a**2*b**14*c**4 + 36973080*a**2*b**13*c**5 + 34899552*a**2*b**12*c**6 - 57391812*a**2*b**11*c**7 - 2313396*a**2*b**10*c**8 + 1159632*a**2*b**9*c**9 - 22055562*a**2*b**8*c**10 - 10458*a**2*b**8*rho**2 + 10860768*a**2*b**7*c**11 + 5472*a**2*b**7*c*rho**2 - 6645186*a**2*b**6*c**12 - 4680*a**2*b**6*c**2*rho**2 - 7691616*a**2*b**5*c**13 - 1128*a**2*b**5*c**3*rho**2 + 8513460*a**2*b**4*c**14 + 9228*a**2*b**4*c**4*rho**2 + 1117332*a**2*b**3*c**15 - 1392*a**2*b**3*c**5*rho**2 - 1864728*a**2*b**2*c**16 + 4728*a**2*b**2*c**6*rho**2 + 823608*a**2*b*c**17 - 840*a**2*b*c**7*rho**2 + 496134*a**2*c**18 - 2538*a**2*c**8*rho**2 + 1548288*a*b**19 - 7433856*a*b**18*c + 1728576*a*b**17*c**2 + 27843552*a*b**16*c**3 - 10763568*a*b**15*c**4 - 32172552*a*b**14*c**5 - 802692*a*b**13*c**6 - 13255344*a*b**12*c**7 - 5944752*a*b**11*c**8 + 7893324*a*b**10*c**9 - 12826908*a*b**9*c**10 - 4608*a*b**9*rho**2 - 124776*a*b**8*c**11 + 6984*a*b**8*c*rho**2 + 10718172*a*b**7*c**12 + 10068*a*b**7*c**2*rho**2 - 2750508*a*b**6*c**13 + 1104*a*b**6*c**3*rho**2 - 1554480*a*b**5*c**14 + 3360*a*b**5*c**4*rho**2 + 2948292*a*b**4*c**15 - 4020*a*b**4*c**5*rho**2 + 406332*a*b**3*c**16 - 2436*a*b**3*c**6*rho**2 - 344592*a*b**2*c**17 + 2352*a*b**2*c**7*rho**2 + 189432*a*b*c**18 - 984*a*b*c**8*rho**2 + 94860*a*c**19 - 1020*a*c**9*rho**2 + 112896*b**20 - 741888*b**19*c + 839808*b**18*c**2 + 3164544*b**17*c**3 - 5490000*b**16*c**4 - 5430240*b**15*c**5 + 10016568*b**14*c**6 + 2924784*b**13*c**7 - 7167879*b**12*c**8 + 5518152*b**11*c**9 + 6077736*b**10*c**10 - 672*b**10*rho**2 - 2714580*b**9*c**11 + 2208*b**9*c*rho**2 + 559656*b**8*c**12 + 1128*b**8*c**2*rho**2 + 2510496*b**7*c**13 - 5712*b**7*c**3*rho**2 - 182106*b**6*c**14 - 1482*b**6*c**4*rho**2 - 187560*b**5*c**15 + 1704*b**5*c**5*rho**2 + 388440*b**4*c**16 - 2424*b**4*c**6*rho**2 + 71244*b**3*c**17 - 1212*b**3*c**7*rho**2 - 30960*b**2*c**18 + 432*b**2*c**8*rho**2 + 17856*b*c**19 - 192*b*c**9*rho**2 + 8649*c**20 - 186*c**10*rho**2 + rho**4",
    "determinant_identity": "det(Phi)=hypersurface**2",
    "hypersurface": "-2952*a**10 + 1068*a**9*b + 996*a**9*c + 3735*a**8*b**2 - 3366*a**8*b*c + 3819*a**8*c**2 + 3132*a**7*b**3 - 3780*a**7*b**2*c - 4332*a**7*b*c**2 + 2604*a**7*c**3 + 5052*a**6*b**4 + 1704*a**6*b**3*c - 312*a**6*b**2*c**2 + 3012*a**6*b*c**3 + 1092*a**6*c**4 - 1818*a**5*b**5 - 378*a**5*b**4*c - 3288*a**5*b**3*c**2 - 2664*a**5*b**2*c**3 + 4422*a**5*b*c**4 - 1674*a**5*c**5 - 6300*a**4*b**6 + 8568*a**4*b**5*c - 7554*a**4*b**4*c**2 - 102*a**4*b**3*c**3 - 4332*a**4*b**2*c**4 + 3690*a**4*b*c**5 - 2994*a**4*c**6 - 5760*a**3*b**7 + 9180*a**3*b**6*c - 5700*a**3*b**5*c**2 + 6216*a**3*b**4*c**3 + 336*a**3*b**3*c**4 + 300*a**3*b**2*c**5 + 1560*a**3*b*c**6 - 2268*a**3*c**7 - 5229*a**2*b**8 + 2736*a**2*b**7*c - 2340*a**2*b**6*c**2 - 564*a**2*b**5*c**3 + 4614*a**2*b**4*c**4 - 696*a**2*b**3*c**5 + 2364*a**2*b**2*c**6 - 420*a**2*b*c**7 - 1269*a**2*c**8 - 2304*a*b**9 + 3492*a*b**8*c + 5034*a*b**7*c**2 + 552*a*b**6*c**3 + 1680*a*b**5*c**4 - 2010*a*b**4*c**5 - 1218*a*b**3*c**6 + 1176*a*b**2*c**7 - 492*a*b*c**8 - 510*a*c**9 - 336*b**10 + 1104*b**9*c + 564*b**8*c**2 - 2856*b**7*c**3 - 741*b**6*c**4 + 852*b**5*c**5 - 1212*b**4*c**6 - 606*b**3*c**7 + 216*b**2*c**8 - 96*b*c**9 - 93*c**10 + rho**2"
  },
  "module_presentations": {
    "L": "Qrho(-4) plus Qrho(-8)^3 --&#91;v | rho*I-W&#93;--&gt; Qrho(-3)^3 --&gt; L --&gt; 0",
    "M": "A(-4) --(a,b,c)^T--&gt; A(-3)^3 --&gt; M --&gt; 0",
    "P": "coker(Phi), with Phi: Qrho(-8)^3 plus Qrho(-4) -&gt; Qrho(-3)^3 plus Qrho(1)",
    "extension": "0 --&gt; Qrho(1) --&gt; P --&gt; L --&gt; 0",
    "normalization_index": "T/(Qrho tensor_A B) is isomorphic as an A-module to M/W*M"
  },
  "resolvent_coordinate": {
    "equation": "-2952*a**10 + 1068*a**9*b + 996*a**9*c + 3735*a**8*b**2 - 3366*a**8*b*c + 3819*a**8*c**2 + 3132*a**7*b**3 - 3780*a**7*b**2*c - 4332*a**7*b*c**2 + 2604*a**7*c**3 + 5052*a**6*b**4 + 1704*a**6*b**3*c - 312*a**6*b**2*c**2 + 3012*a**6*b*c**3 + 1092*a**6*c**4 - 1818*a**5*b**5 - 378*a**5*b**4*c - 3288*a**5*b**3*c**2 - 2664*a**5*b**2*c**3 + 4422*a**5*b*c**4 - 1674*a**5*c**5 - 6300*a**4*b**6 + 8568*a**4*b**5*c - 7554*a**4*b**4*c**2 - 102*a**4*b**3*c**3 - 4332*a**4*b**2*c**4 + 3690*a**4*b*c**5 - 2994*a**4*c**6 - 5760*a**3*b**7 + 9180*a**3*b**6*c - 5700*a**3*b**5*c**2 + 6216*a**3*b**4*c**3 + 336*a**3*b**3*c**4 + 300*a**3*b**2*c**5 + 1560*a**3*b*c**6 - 2268*a**3*c**7 - 5229*a**2*b**8 + 2736*a**2*b**7*c - 2340*a**2*b**6*c**2 - 564*a**2*b**5*c**3 + 4614*a**2*b**4*c**4 - 696*a**2*b**3*c**5 + 2364*a**2*b**2*c**6 - 420*a**2*b*c**7 - 1269*a**2*c**8 - 2304*a*b**9 + 3492*a*b**8*c + 5034*a*b**7*c**2 + 552*a*b**6*c**3 + 1680*a*b**5*c**4 - 2010*a*b**4*c**5 - 1218*a*b**3*c**6 + 1176*a*b**2*c**7 - 492*a*b*c**8 - 510*a*c**9 - 336*b**10 + 1104*b**9*c + 564*b**8*c**2 - 2856*b**7*c**3 - 741*b**6*c**4 + 852*b**5*c**5 - 1212*b**4*c**6 - 606*b**3*c**7 + 216*b**2*c**8 - 96*b*c**9 - 93*c**10 + rho**2",
    "lambda": "zeta_3-zeta_3**2",
    "lambda_square": "-3",
    "rho": "lambda*w",
    "rho_degree": 5
  },
  "schema_version": 2,
  "splitting_field": "Q(zeta_3)"
}
</code></pre>

<a id="source-e961b52492bf9fdf"></a>

## `research-notes/lane1-models-20260803-v1/verify_elliptic_cone_model.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact symbolic checks for the elliptic-cone P1-T1 negative model.

This script verifies the explicit Fermat dual sextic, its singular lines and
local cusp leading form, and the standard triple-collision ideal.
It does not attempt to machine-check the sheaf-cohomology or local-duality
arguments in the accompanying note.
"""
from __future__ import annotations

import sympy as sp


a, b, c, w = sp.symbols("a b c w")
x, y, z = sp.symbols("x y z")
u, v = sp.symbols("u v")

# Dual sextic of x^3+y^3+z^3=0.
d = (
    a**6 + b**6 + c**6
    - 2*a**3*b**3 - 2*a**3*c**3 - 2*b**3*c**3
)

# Tangent line at &#91;x:y:z&#93; has dual coordinates &#91;x^2:y^2:z^2&#93;.
tangent_pullback = sp.factor(d.subs({a: x**2, b: y**2, c: z**2}))
expected = sp.factor(
    (x**3-y**3-z**3)
    * (x**3-y**3+z**3)
    * (x**3+y**3-z**3)
    * (x**3+y**3+z**3)
)
assert sp.expand(tangent_pullback - expected) == 0

# Gradient formulas.
derivatives = &#91;sp.factor(sp.diff(d, q)) for q in (a, b, c)&#93;
assert derivatives == &#91;
    6*a**2*(a**3-b**3-c**3),
    -6*b**2*(a**3-b**3+c**3),
    -6*c**2*(a**3+b**3-c**3),
&#93;

# One cusp chart: a=1, b=1+u, c=v.  The lowest part is 9u^2-4v^3.
local = sp.Poly(sp.expand(d.subs({a: 1, b: 1+u, c: v})), u, v)
lowest_degree = min(sum(mon) for mon, _ in local.terms())
lowest = sum(
    coeff * u**mon&#91;0&#93; * v**mon&#91;1&#93;
    for mon, coeff in local.terms()
    if sum(mon) == lowest_degree
)
assert lowest_degree == 2
assert sp.expand(lowest - 9*u**2) == 0
# The first term transverse to the double tangent is -4v^3.
assert local.coeff_monomial(v**3) == -4

# Standard ordered-root collision ideal.
f1 = sp.expand(u*(u+v))
f2 = sp.expand(u*v)
f3 = sp.expand(v*(u+v))
G_collision = sp.groebner(&#91;f1, f2, f3&#93;, u, v, order="lex")
G_square = sp.groebner(&#91;u**2, u*v, v**2&#93;, u, v, order="lex")
assert G_collision == G_square

# Standard representation: a transposition has a one-dimensional fixed space;
# a 3-cycle has no fixed vectors.
transposition = sp.Matrix(&#91;&#91;0, 1&#93;, &#91;1, 0&#93;&#93;)
# A convenient rational matrix of order 3 with characteristic polynomial t^2+t+1.
three_cycle = sp.Matrix(&#91;&#91;0, -1&#93;, &#91;1, -1&#93;&#93;)
I2 = sp.eye(2)
assert (transposition - I2).rank() == 1
assert (three_cycle - I2).rank() == 2
assert three_cycle**3 == I2

print("dual sextic d =", d)
print("verified tangent parametrization of the dual sextic")
print("gradient =", derivatives)
print("verified cusp leading terms 9*u^2 - 4*v^3 + higher terms")
print("verified (u(u+v), uv, v(u+v)) = (u,v)^2")
print("verified standard-representation fixed-space dimensions: H-fixed 1, A3-fixed 0")
</code></pre>

<a id="source-4878f853b11d07dd"></a>

## `research-notes/lane1-models-20260803-v1/verify_homogeneous_typeiv.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for the P1-T1 homogeneous/type-IV reduction.

The script verifies:
  * graded one-generator numerical formulas;
  * the stable-birational d=4 survivor table;
  * type-IV intersection, ramification, and genus data;
  * the 13-element boundary basis and canonical coordinates;
  * boundary/nonproperness component lower bounds;
  * the Hodge-polynomial failure of the natural invariant opening.

Optionally, a JSON file can supply 13 candidate boundary classes in the
Picard basis &#91;L,E1,...,E13&#93;. The verifier checks that they form a basis of
Pic(X)/Z H and, when ramification data are supplied, that their weighted
ramified sum equals R modulo H.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp


N_EXCEPTIONAL = 13
RANK_PIC = 1 + N_EXCEPTIONAL


def col(values: list&#91;int&#93;) -&gt; sp.Matrix:
    if len(values) != RANK_PIC:
        raise ValueError(f"expected {RANK_PIC} coordinates, got {len(values)}")
    return sp.Matrix(values)


def intersection(x: sp.Matrix, y: sp.Matrix) -&gt; sp.Integer:
    """Intersection form diag(1,-1,...,-1) on Bl_13(P^2)."""
    return sp.Integer(x&#91;0&#93; * y&#91;0&#93; - sum(x&#91;i&#93; * y&#91;i&#93; for i in range(1, RANK_PIC)))


def h0_projective_O(n: int) -&gt; int:
    return math.comb(n + 2, 2) if n &gt;= 0 else 0


def h0_tangent(n: int) -&gt; int:
    """h^0(P^2,T(n)), from 0 -&gt; O(n) -&gt; O(n+1)^3 -&gt; T(n) -&gt; 0."""
    return 3 * h0_projective_O(n + 1) - h0_projective_O(n)


def graded_row(d: int) -&gt; dict&#91;str, int&#93;:
    if d &lt; 3:
        building = 0
    else:
        building = 2 * (d + 2) * (d - 2)
    q = 1 if d == 3 else 0
    pg = h0_tangent(d - 6)
    return {
        "d": d,
        "defect_weight": d - 3,
        "c1": 2 * d - 3,
        "c2": d * d - 3 * d + 3,
        "branch_degree": 4 * d - 6,
        "building_dimension": building,
        "q": q,
        "pg": pg,
        "K2": 5 * d * d - 39 * d + 72,
    }


def quotient_coordinates(
    vector: sp.Matrix, H: sp.Matrix, boundary: list&#91;sp.Matrix&#93;
) -&gt; tuple&#91;int, list&#91;int&#93;&#93;:
    """Solve vector = h_coeff*H + sum boundary_coeff_i*D_i over Z."""
    matrix = sp.Matrix.hstack(H, *boundary)
    solution = matrix.inv() * vector
    if any(not entry.is_Integer for entry in solution):
        raise AssertionError(f"non-integral coordinates: {list(solution)}")
    return int(solution&#91;0&#93;), &#91;int(entry) for entry in solution&#91;1:&#93;&#93;


def verify_candidate(path: Path, H: sp.Matrix, R: sp.Matrix) -&gt; None:
    data: dict&#91;str, Any&#93; = json.loads(path.read_text(encoding="utf-8"))
    raw_classes = data.get("boundary_classes")
    if not isinstance(raw_classes, list) or len(raw_classes) != 13:
        raise ValueError("candidate JSON must contain exactly 13 boundary_classes")
    boundary = &#91;col(&#91;int(v) for v in raw&#93;) for raw in raw_classes&#93;
    matrix = sp.Matrix.hstack(H, *boundary)
    determinant = int(matrix.det())
    if abs(determinant) != 1:
        raise AssertionError(
            "candidate classes do not form a Z-basis of Pic(X)/Z H; "
            f"augmented determinant is {determinant}"
        )

    ramified_indices = data.get("ramified_indices")
    if ramified_indices is not None:
        if not isinstance(ramified_indices, list):
            raise ValueError("ramified_indices must be a list")
        multiplicities = data.get("ramification_multiplicities", &#91;1&#93; * len(ramified_indices))
        if len(multiplicities) != len(ramified_indices):
            raise ValueError("ramification multiplicities have wrong length")
        ram_sum = sp.zeros(RANK_PIC, 1)
        for index, multiplicity in zip(ramified_indices, multiplicities, strict=True):
            index = int(index)
            if not 0 &lt;= index &lt; 13:
                raise ValueError(f"ramified index {index} is outside &#91;0,12&#93;")
            ram_sum += int(multiplicity) * boundary&#91;index&#93;
        _, coords = quotient_coordinates(ram_sum - R, H, boundary)
        if any(coords):
            raise AssertionError("weighted ramified sum is not R modulo H")

    print(f"candidate {path}: PASS (det={determinant})")


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--candidate",
        type=Path,
        help="optional JSON candidate with 13 boundary classes",
    )
    args = parser.parse_args()

    # Picard basis &#91;L,E1,...,E13&#93;.
    L = col(&#91;1&#93; + &#91;0&#93; * N_EXCEPTIONAL)
    exceptional = &#91;
        col(&#91;0&#93; + &#91;1 if j == i else 0 for j in range(N_EXCEPTIONAL)&#93;)
        for i in range(N_EXCEPTIONAL)
    &#93;
    H = 4 * L - sum(exceptional, sp.zeros(RANK_PIC, 1))
    K = -3 * L + sum(exceptional, sp.zeros(RANK_PIC, 1))
    R = K + 3 * H

    # Graded table and stable-birational survivor.
    rows = &#91;graded_row(d) for d in range(3, 9)&#93;
    assert rows&#91;0&#93;&#91;"building_dimension"&#93; == 10
    assert rows&#91;1&#93;&#91;"building_dimension"&#93; == 24
    survivors = &#91;row&#91;"d"&#93; for row in rows if row&#91;"q"&#93; == 0 and row&#91;"pg"&#93; == 0&#93;
    assert survivors == &#91;4&#93;, survivors

    # Type-IV intersection data.
    assert intersection(H, H) == 3
    assert intersection(K, K) == -4
    assert intersection(H, K) == 1
    assert R == 9 * L - 2 * sum(exceptional, sp.zeros(RANK_PIC, 1))
    assert intersection(H, R) == 10
    assert intersection(R, R) == 29
    assert intersection(K, R) == -1
    genus_H = 1 + (intersection(H, H) + intersection(H, K)) // 2
    genus_R = 1 + (intersection(R, R) + intersection(R, K)) // 2
    assert genus_H == 3
    assert genus_R == 15
    assert math.comb(10 - 1, 2) - 21 == genus_R  # decic with 21 cusps

    # Effective boundary basis &#91;R,E1,...,E12&#93;.
    natural_boundary = &#91;R, *exceptional&#91;:12&#93;&#93;
    augmented = sp.Matrix.hstack(H, *natural_boundary)
    determinant = int(augmented.det())
    assert determinant == 1
    h_coeff_R, coords_R = quotient_coordinates(R, H, natural_boundary)
    h_coeff_K, coords_K = quotient_coordinates(K, H, natural_boundary)
    assert h_coeff_R == 0 and coords_R == &#91;1&#93; + &#91;0&#93; * 12
    assert h_coeff_K == -3 and coords_K == &#91;1&#93; + &#91;0&#93; * 12
    assert all(intersection(H, E) == 1 for E in exceptional)
    assert all(intersection(R, E) == 2 for E in exceptional)

    # Boundary count and corrected U1/U2/B count.
    class_rank = 13
    max_ramification_components = intersection(H, R)  # every component has positive H-degree
    min_unramified = class_rank - max_ramification_components
    assert min_unramified == 3
    component_bounds = {
        b: b + math.ceil((class_rank - b) / 2)
        for b in range(1, max_ramification_components + 1)
    }
    assert min(component_bounds.values()) == 7
    assert component_bounds&#91;1&#93; == 7

    # Hodge polynomial of the natural invariant opening.
    u, v = sp.symbols("u v")
    q_uv = u * v
    E_X = 1 + 14 * q_uv + q_uv**2
    E_R = 1 - 15 * (u + v) + q_uv
    E_P1 = 1 + q_uv
    E_boundary = sp.expand(E_R + 12 * E_P1 - 24)
    E_X_open = sp.expand(E_X - E_boundary)
    expected_X_open = sp.expand(q_uv**2 + q_uv + 12 + 15 * (u + v))
    assert sp.expand(E_X_open - expected_X_open) == 0
    E_cone_open = sp.expand((q_uv - 1) * E_X_open)
    assert sp.expand(E_cone_open - q_uv**3) != 0
    assert E_cone_open.subs({u: 1, v: 1}) == 0
    assert (q_uv**3).subs({u: 1, v: 1}) == 1

    print("graded one-generator table")
    for row in rows:
        print(
            "  d={d}: weight={defect_weight}, h0(build)={building_dimension}, "
            "branch={branch_degree}, q={q}, pg={pg}, K2={K2}".format(**row)
        )
    print("stable-birational survivor: d=4")
    print(
        "type IV: H^2=3, K^2=-4, H.K=1, H.R=10, "
        "R^2=29, g(H)=3, g(R)=15"
    )
    print("natural boundary basis determinant:", determinant)
    print("canonical coordinates in &#91;R,E1,...,E12&#93;:", coords_K)
    print("minimum unramified boundary divisors:", min_unramified)
    print("minimum nonproperness hypersurface components:", min(component_bounds.values()))
    print("natural invariant opening E-polynomial:", E_cone_open)
    print("all built-in checks: PASS")

    if args.candidate is not None:
        verify_candidate(args.candidate, H, R)


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-eb2e6a9bd27953e2"></a>

## `research-notes/lane1-models-20260803-v1/verify_marked_root_benchmark.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact certificates for the normalized marked-root cubic benchmark.

This script checks polynomial identities, elimination ideals, Jacobian/Fitting
calculations, the quadratic-resolvent singular locus up to radical, the global
matrix factorization, and the local presentation of the cubic-character
module.  It uses exact rational arithmetic only.

Mathematical scope:
  * checked: all displayed polynomial and Groebner-basis certificates;
  * not replaced by computation: geometric normality, the Cech basis argument,
    valuation-theoretic conductor proof, and the MCM/depth interpretation.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import sympy as sp


def assert_zero(expr: sp.Expr, message: str = "") -&gt; None:
    value = sp.factor(sp.cancel(sp.expand(expr)))
    if value != 0:
        raise AssertionError(message or f"expected zero, got {value}")


def assert_matrix_zero(matrix: sp.Matrix, message: str = "") -&gt; None:
    for entry in matrix:
        assert_zero(entry, message)


def mutual_ideal_containment(
    generators_a: list&#91;sp.Expr&#93;,
    generators_b: list&#91;sp.Expr&#93;,
    variables: tuple&#91;sp.Symbol, ...&#93;,
) -&gt; None:
    """Check equality of two ideals by exact Groebner reduction."""
    ga = sp.groebner(generators_a, *variables, order="lex", domain=sp.QQ)
    gb = sp.groebner(generators_b, *variables, order="lex", domain=sp.QQ)
    for f in generators_a:
        remainder = gb.reduce(sp.expand(f))&#91;1&#93;
        assert_zero(remainder, f"first ideal is not contained in second: {f}")
    for f in generators_b:
        remainder = ga.reduce(sp.expand(f))&#91;1&#93;
        assert_zero(remainder, f"second ideal is not contained in first: {f}")


def main() -&gt; None:
    a, b, c, t = sp.symbols("a b c t")
    omega, theta = sp.symbols("omega theta")
    varpi = sp.symbols("varpi")

    P = c * t**3 - 2 * t**2 + b * t - 2 * a
    delta = b**2 - b**3 * c - 16 * a + 18 * a * b * c - 27 * a**2 * c**2

    # ------------------------------------------------------------------
    # 1. Cubic algebra and the global Cech-basis certificate.
    # ------------------------------------------------------------------
    assert_zero(sp.discriminant(P, t) - 4 * delta, "cubic discriminant")

    omega_t = -c * t
    theta_t = -c * t**2 + 2 * t - b

    def mod_p(expr: sp.Expr) -&gt; sp.Expr:
        return sp.factor(sp.rem(sp.expand(expr), P, t))

    relation_1_t = omega_t**2 + b * c + 2 * omega_t + c * theta_t
    relation_2_t = omega_t * theta_t - 2 * a * c
    relation_3_t = theta_t**2 + 4 * a + 2 * a * omega_t + b * theta_t
    assert_zero(mod_p(relation_1_t), "omega^2 relation")
    assert_zero(mod_p(relation_2_t), "omega theta relation")
    assert_zero(mod_p(relation_3_t), "theta^2 relation")

    # On the infinity chart s=1/t, the two global functions are
    # omega=-2+b/t-2a/t^2 and theta=-2a/t.  Their lift differences are
    # -P/t^2 and -P/t, the standard basis of H^1(P^1,O(-3)).
    omega_infinity_as_t = -2 + b / t - 2 * a / t**2
    theta_infinity_as_t = -2 * a / t
    assert_zero(
        t**2 * (omega_t - omega_infinity_as_t) + P,
        "Cech connecting class for omega",
    )
    assert_zero(
        t * (theta_t - theta_infinity_as_t) + P,
        "Cech connecting class for theta",
    )

    # Eliminate t from P, omega+ct, theta+ct^2-2t+b.  The resulting kernel
    # is generated by the three multiplication relations.
    graph_ideal = &#91;P, omega + c * t, theta + c * t**2 - 2 * t + b&#93;
    graph_gb = sp.groebner(
        graph_ideal,
        t,
        omega,
        theta,
        a,
        b,
        c,
        order="lex",
        domain=sp.QQ,
    )
    eliminated = &#91;
        poly.as_expr() for poly in graph_gb.polys if not poly.as_expr().has(t)
    &#93;
    relation_1 = omega**2 + b * c + 2 * omega + c * theta
    relation_2 = omega * theta - 2 * a * c
    relation_3 = theta**2 + 4 * a + 2 * a * omega + b * theta
    mutual_ideal_containment(
        eliminated,
        &#91;relation_1, relation_2, relation_3&#93;,
        (omega, theta, a, b, c),
    )

    # Trace-pairing determinant.
    gram = sp.Matrix(
        &#91;
            &#91;3, -2, -b&#93;,
            &#91;-2, 4 - 2 * b * c, 6 * a * c&#93;,
            &#91;-b, 6 * a * c, b**2 - 8 * a&#93;,
        &#93;
    )
    assert_zero(gram.det() - 4 * delta, "trace-pairing determinant")

    # ------------------------------------------------------------------
    # 2. Quadratic resolvent and its singular locus.
    # ------------------------------------------------------------------
    p = 4 - 3 * b * c
    h = 8 - 9 * b * c + 27 * a * c**2
    assert_zero(p**3 - h**2 - 27 * c**2 * delta, "resolvent cusp identity")

    alpha = sp.symbols("alpha")
    depressed = sp.expand(27 * c**2 * P.subs(t, (alpha + 2) / (3 * c)))
    assert_zero(
        depressed - (alpha**3 - 3 * p * alpha - 2 * h),
        "depressed cubic",
    )

    f_q = varpi**2 + 3 * delta
    jacobian_ideal = &#91;f_q&#93; + &#91;sp.diff(f_q, x) for x in (a, b, c, varpi)&#93;
    singular_prime = &#91;varpi, p, h&#93;

    # J_sing is contained in (varpi,p,h).
    g_prime = sp.groebner(
        singular_prime, varpi, a, b, c, order="lex", domain=sp.QQ
    )
    for generator in jacobian_ideal:
        assert_zero(
            g_prime.reduce(sp.expand(generator))&#91;1&#93;,
            "Jacobian ideal not contained in proposed singular prime",
        )

    # Conversely varpi,h are in J_sing and p^3 is in J_sing, proving equality
    # of radicals once (varpi,p,h) is identified with C&#91;c,c^{-1}&#93;.
    g_jac = sp.groebner(
        jacobian_ideal, varpi, a, b, c, order="grevlex", domain=sp.QQ
    )
    for generator in (varpi, h, p**3):
        assert_zero(
            g_jac.reduce(sp.expand(generator))&#91;1&#93;,
            "proposed singular radical not contained in Jacobian radical",
        )
    # c is a unit modulo (p,h): c*(3b/4)=1.
    assert_zero(
        g_prime.reduce(sp.expand(c * (sp.Rational(3, 4) * b) - 1))&#91;1&#93;,
        "c should be invertible along the singular curve",
    )

    # ------------------------------------------------------------------
    # 3. Global eigensheaf matrix factorization.
    # ------------------------------------------------------------------
    m = 9 * a * c - b
    n = b**2 - 12 * a
    M = sp.Matrix(&#91;&#91;m, n&#93;, &#91;-p, -m&#93;&#93;)
    assert_matrix_zero(M**2 + 3 * delta * sp.eye(2), "M^2=-3delta")

    phi = varpi * sp.eye(2) - M
    psi = varpi * sp.eye(2) + M
    assert_matrix_zero(
        phi * psi - (varpi**2 + 3 * delta) * sp.eye(2),
        "matrix factorization",
    )
    assert_matrix_zero(
        psi * phi - (varpi**2 + 3 * delta) * sp.eye(2),
        "reverse matrix factorization",
    )

    # Basis change from (alpha,beta) to the global trace-zero basis (e1,e2).
    transported = sp.Matrix(&#91;&#91;h, p**2&#93;, &#91;-p, -h&#93;&#93;) / (3 * c)
    basis_change = sp.Matrix(&#91;&#91;-1, -2&#93;, &#91;0, -3 * c&#93;&#93;)
    assert_matrix_zero(
        basis_change * transported * basis_change.inv() - M,
        "transported resolvent action",
    )

    # Local A_2 presentation: coker(&#91;&#91;-v,-p^2&#93;,&#91;p,u&#93;&#93;) -&gt; (u,p^2).
    p0, u0, v0 = sp.symbols("p0 u0 v0")
    local_matrix = sp.Matrix(&#91;&#91;-v0, -p0**2&#93;, &#91;p0, u0&#93;&#93;)
    ideal_row = sp.Matrix(&#91;&#91;u0, p0**2&#93;&#93;)
    local_relation = u0 * v0 - p0**3
    row_product = ideal_row * local_matrix
    assert_zero(row_product&#91;0&#93; + local_relation, "first local syzygy modulo uv-p^3")
    assert_zero(row_product&#91;1&#93;, "second local syzygy")
    assert_zero(local_matrix.det() + local_relation, "local determinant")

    # ------------------------------------------------------------------
    # 4. Branch normalization and conductor identities.
    # ------------------------------------------------------------------
    a_ram = t**2 - c * t**3
    b_ram = 4 * t - 3 * c * t**2
    z = 3 * c * t - 2
    assert_zero(delta.subs({a: a_ram, b: b_ram}), "branch parametrization")
    assert_zero(p.subs({a: a_ram, b: b_ram}) - z**2, "p=z^2")
    assert_zero(h.subs({a: a_ram, b: b_ram}) + z**3, "h=-z^3")

    # On D(p), the double root is already in the branch ring.  The displayed
    # identity is asserted in the branch quotient, so verify it after the
    # normalization parametrization.
    assert_zero(
        (p * t - (b - 9 * a * c)).subs({a: a_ram, b: b_ram}),
        "double-root formula on the branch",
    )

    # Numerical-semigroup conductor: &lt;2,3&gt; contains every exponent &gt;=2 but not 1.
    representable = {
        2 * i + 3 * j for i in range(12) for j in range(12)
    }
    assert 1 not in representable
    assert all(exponent in representable for exponent in range(2, 20))

    # ------------------------------------------------------------------
    # 5. Kähler/Fitting differents.
    # ------------------------------------------------------------------
    jac = sp.Matrix(
        &#91;
            &#91;2 * omega + 2, c&#93;,
            &#91;theta, omega&#93;,
            &#91;2 * a, 2 * theta + b&#93;,
        &#93;
    )
    minors = &#91;
        sp.expand(jac.extract(rows, &#91;0, 1&#93;).det())
        for rows in ((0, 1), (0, 2), (1, 2))
    &#93;
    relation_gb = sp.groebner(
        &#91;relation_1, relation_2, relation_3&#93;,
        omega,
        theta,
        a,
        b,
        c,
        order="lex",
        domain=sp.QQ,
    )
    d1 = -2 * omega - 3 * c * theta - 2 * b * c
    d2 = 6 * a * c + 2 * b * omega + 4 * theta + 2 * b
    d3 = -8 * a - 6 * a * omega - b * theta
    for actual, expected in zip(minors, (d1, d2, d3)):
        assert_zero(
            relation_gb.reduce(sp.expand(actual - expected))&#91;1&#93;,
            "Fitting-minor reduction",
        )

    r = sp.diff(P, t)
    assert_zero(mod_p(d1.subs({omega: omega_t, theta: theta_t}) - c * r))
    assert_zero(
        mod_p(d2.subs({omega: omega_t, theta: theta_t}) - (c * t - 2) * r)
    )
    assert_zero(mod_p(d3.subs({omega: omega_t, theta: theta_t}) + theta_t * r))

    # Triple-root specialization and fibrewise different.
    t0 = 2 / (3 * c)
    a0 = 4 / (27 * c**2)
    b0 = 4 / (3 * c)
    eps = sp.symbols("eps")
    assert_zero(P.subs({a: a0, b: b0}) - c * (t - t0) ** 3)
    assert_zero(r.subs({b: b0, t: t0 + eps}) - 3 * c * eps**2)

    print("verified: global multiplication relations and elimination kernel")
    print("verified: Cech connecting classes -t^-2 and -t^-1")
    print("verified: discriminant, resolvent A_2 identity, and singular radical")
    print("verified: global eigensheaf matrix factorization and local ideal syzygies")
    print("verified: branch normalization, conductor semigroup, and differents")
    print("all marked-root benchmark certificates passed")
    path = Path(__file__)
    print("script_sha256 =", hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-31b4a29aadab18de"></a>

## `research-notes/lane1-models-20260803-v1/verify_marked_root_collision_saturation.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact root-difference certificates for the marked-root P1-T1 model.

At any omitted value on the triple-root curve, the completed S_3 normalization
is C&#91;&#91;u,v,lambda&#93;&#93;.  This script verifies the invariant map, the three root
slopes, the S_3 permutation action, and the equality of the chart-complement
ideal with (u,v)^2.

The final saturation statement uses the reader proof that
H^2_(u,v)(C&#91;&#91;u,v,lambda&#93;&#93;) is lambda-torsion-free; that local-cohomology fact
is recorded but is not replaced by a finite computation.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import sympy as sp


def assert_zero(expr: sp.Expr, message: str = "") -&gt; None:
    value = sp.factor(sp.cancel(sp.expand(expr)))
    if value != 0:
        raise AssertionError(message or f"expected zero, got {value}")


def substitute_linear(expr: sp.Expr, image_u: sp.Expr, image_v: sp.Expr) -&gt; sp.Expr:
    u, v = sp.symbols("u v")
    return sp.expand(expr.subs({u: image_u, v: image_v}, simultaneous=True))


def main() -&gt; None:
    u, v, lam, x = sp.symbols("u v lambda x")

    # Ordered depressed roots: u=alpha_1-alpha_2, v=alpha_2-alpha_3.
    alpha_1 = sp.Rational(1, 3) * (2 * u + v)
    alpha_2 = sp.Rational(1, 3) * (-u + v)
    alpha_3 = sp.Rational(1, 3) * (-u - 2 * v)
    roots = (alpha_1, alpha_2, alpha_3)
    assert_zero(sum(roots), "root sum")

    p = sp.factor(-(alpha_1 * alpha_2 + alpha_1 * alpha_3 + alpha_2 * alpha_3) / 3)
    h = sp.factor(alpha_1 * alpha_2 * alpha_3 / 2)
    assert_zero(p - (u**2 + u * v + v**2) / 9, "p invariant")
    assert_zero(
        h - (u - v) * (u + 2 * v) * (2 * u + v) / 54,
        "h invariant",
    )

    cubic = x**3 - 3 * p * x - 2 * h
    for index, root in enumerate(roots, start=1):
        assert_zero(cubic.subs(x, root), f"root alpha_{index}")

    # The three source-sheet boundary functions are the root derivatives,
    # up to the common unit 9c.
    q_1 = sp.factor(3 * (alpha_1**2 - p))
    q_2 = sp.factor(3 * (alpha_2**2 - p))
    q_3 = sp.factor(3 * (alpha_3**2 - p))
    assert_zero(q_1 - u * (u + v), "first root slope")
    assert_zero(q_2 + u * v, "second root slope")
    assert_zero(q_3 - v * (u + v), "third root slope")

    # The actual chart-complement ideal is exactly the square of the transverse
    # maximal ideal.
    g_chart = sp.groebner(&#91;q_1, q_2, q_3&#93;, u, v, order="lex", domain=sp.QQ)
    g_square = sp.groebner(&#91;u**2, u * v, v**2&#93;, u, v, order="lex", domain=sp.QQ)
    assert g_chart == g_square
    assert_zero(q_1 + q_2 - u**2, "u^2 certificate")
    assert_zero(q_3 + q_2 - v**2, "v^2 certificate")

    # Triple-intersection denominator and discriminant.
    product = sp.factor(q_1 * q_2 * q_3)
    assert_zero(product + u**2 * v**2 * (u + v) ** 2, "triple denominator")
    discriminant = sp.discriminant(cubic, x)
    assert_zero(
        discriminant - u**2 * v**2 * (u + v) ** 2,
        "ordered-root discriminant",
    )

    # S_3 on the standard root-difference plane.
    # s=(12): (u,v)-&gt;(-u,u+v)
    # r=(123): (u,v)-&gt;(v,-u-v)
    s_u, s_v = -u, u + v
    r_u, r_v = v, -u - v

    # Relations s^2=r^3=1 and srs=r^{-1}.
    S = sp.Matrix(&#91;&#91;-1, 0&#93;, &#91;1, 1&#93;&#93;)
    R = sp.Matrix(&#91;&#91;0, 1&#93;, &#91;-1, -1&#93;&#93;)
    identity = sp.eye(2)
    assert S**2 == identity
    assert R**3 == identity
    assert S * R * S == R.inv()

    ss_u = substitute_linear(s_u, s_u, s_v)
    ss_v = substitute_linear(s_v, s_u, s_v)
    assert_zero(ss_u - u, "s^2 on u")
    assert_zero(ss_v - v, "s^2 on v")

    rr_u = substitute_linear(r_u, r_u, r_v)
    rr_v = substitute_linear(r_v, r_u, r_v)
    rrr_u = substitute_linear(rr_u, r_u, r_v)
    rrr_v = substitute_linear(rr_v, r_u, r_v)
    assert_zero(rrr_u - u, "r^3 on u")
    assert_zero(rrr_v - v, "r^3 on v")

    # Invariants p,h are fixed by both generators.
    for name, invariant in (("p", p), ("h", h)):
        assert_zero(substitute_linear(invariant, s_u, s_v) - invariant, f"s fixes {name}")
        assert_zero(substitute_linear(invariant, r_u, r_v) - invariant, f"r fixes {name}")

    # The three slope functions are permuted exactly as the source charts.
    assert_zero(substitute_linear(q_1, s_u, s_v) - q_2, "s(q1)=q2")
    assert_zero(substitute_linear(q_2, s_u, s_v) - q_1, "s(q2)=q1")
    assert_zero(substitute_linear(q_3, s_u, s_v) - q_3, "s(q3)=q3")
    assert_zero(substitute_linear(q_1, r_u, r_v) - q_2, "r(q1)=q2")
    assert_zero(substitute_linear(q_2, r_u, r_v) - q_3, "r(q2)=q3")
    assert_zero(substitute_linear(q_3, r_u, r_v) - q_1, "r(q3)=q1")

    # The target maximal ideal (p,h,lambda) pulls back to an ideal whose radical
    # is (u,v,lambda).  A finite certificate is (u,v)^4 subset (p,h).
    p_integral = sp.expand(9 * p)
    h_integral = sp.expand(54 * h)
    g_invariants = sp.groebner(
        &#91;p_integral, h_integral&#93;, u, v, order="lex", domain=sp.QQ
    )
    for i in range(5):
        monomial = u**i * v ** (4 - i)
        assert_zero(
            g_invariants.reduce(monomial)&#91;1&#93;,
            f"degree-four radical certificate for {monomial}",
        )

    # The Cech quotient is H^2_(u,v)(C&#91;&#91;u,v,lambda&#93;&#93;) and has the monomial
    # decomposition direct_sum_{i,j&gt;=1} C&#91;&#91;lambda&#93;&#93; u^{-i}v^{-j}.  Therefore
    # multiplication by lambda is injective, so its (p,h,lambda)-power torsion
    # vanishes.  This establishes I^sat/I=0 in the reader proof.

    print("completed Galois ring = C&#91;&#91;u,v,lambda&#93;&#93;")
    print("root slopes =", q_1, q_2, q_3)
    print("verified chart ideal = (u,v)^2")
    print("verified pair/triple chart denominators and S_3 permutation action")
    print("verified radical pullback: (u,v)^4 is contained in (p,h)")
    print("reader proof: lambda is injective on H^2_(u,v), hence I^sat/I=0")
    print("therefore the closed-point standard-isotypic saturation quotient is zero")
    path = Path(__file__)
    print("script_sha256 =", hashlib.sha256(path.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-0de51d18f6967859"></a>

## `research-notes/lane1-models-20260803-v1/verify_typeiv_explicit_net.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Construct and exactly verify an explicit type-IV quartic net.

Requires SymPy 1.14 or compatible.  All calculations are over Q.

The section of T_{P^2}(2) is represented by a cubic triple (P,Q,R),
modulo radial triples h(x,y,z)(x,y,z).  Its zero scheme is the base locus
of the quartic cross-product net

    (q1,q2,q3) = (yR-zQ, zP-xR, xQ-yP).

The checker proves for the chosen triple:
  * the projective base scheme is reduced, has length 13, and misses z=0;
  * no target line divides its associated cubic, so the resolved map is finite;
  * a sample target fibre consists of three distinct points;
  * the ramification determinant is an irreducible degree-9 curve;
  * the branch equation is an irreducible homogeneous decic;
  * its singular Jacobian scheme has length 42, supported at exactly
    21 points, each of local Jacobian length 2;
  * no branch singularity lies on c=0 and the quadratic term never vanishes,
    so the 21 singularities are ordinary A2 cusps.

Use --write-json PATH to save all explicit equations and exact metadata.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

import sympy as sp


def standard_monomials_length(gb: sp.GroebnerBasis) -&gt; tuple&#91;int, list&#91;tuple&#91;int, ...&#93;&#93;&#93;:
    """Count standard monomials of a zero-dimensional monomial initial ideal."""
    n = len(gb.gens)
    leading = &#91;tuple(poly.LM(order=gb.order).exponents) for poly in gb.polys&#93;
    bounds: list&#91;int&#93; = &#91;&#93;
    for axis in range(n):
        pure = &#91;exp&#91;axis&#93; for exp in leading if all(exp&#91;j&#93; == 0 for j in range(n) if j != axis)&#93;
        if not pure:
            raise AssertionError(f"no pure-power leading monomial in axis {axis}: {leading}")
        bounds.append(min(pure))

    standard: list&#91;tuple&#91;int, ...&#93;&#93; = &#91;&#93;
    ranges = &#91;range(bound) for bound in bounds&#93;
    import itertools

    for exponent in itertools.product(*ranges):
        if not any(all(exponent&#91;j&#93; &gt;= lm&#91;j&#93; for j in range(n)) for lm in leading):
            standard.append(exponent)
    return len(standard), standard


def common_univariate_gcd(expressions: Iterable&#91;sp.Expr&#93;, variable: sp.Symbol) -&gt; sp.Poly:
    polys = &#91;sp.Poly(sp.expand(expr), variable, domain=sp.QQ) for expr in expressions&#93;
    gcd = polys&#91;0&#93;
    for poly in polys&#91;1:&#93;:
        gcd = sp.gcd(gcd, poly)
    return gcd.monic()


def sha256_text(text: str) -&gt; str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -&gt; None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path, help="write explicit equations and metadata")
    args = parser.parse_args()

    x, y, z = sp.symbols("x y z")
    a, b, c = sp.symbols("a b c")
    t = sp.symbols("t")

    # A deliberately small integral representative of a generic section of T(2).
    P = x**3 + 2 * y**3 + 3 * z**3 + x * y * z + y**2 * z
    Q = 2 * x**3 - y**3 + z**3 + x**2 * z + x * y**2
    R = x**3 + y**3 - 2 * z**3 + x * z**2 + y * z**2 + x**2 * y

    q1 = sp.expand(y * R - z * Q)
    q2 = sp.expand(z * P - x * R)
    q3 = sp.expand(x * Q - y * P)
    quartics = &#91;q1, q2, q3&#93;
    assert all(sp.Poly(q, x, y, z).total_degree() == 4 for q in quartics)
    assert sp.gcd(sp.gcd(sp.Poly(q1, x, y, z), sp.Poly(q2, x, y, z)), sp.Poly(q3, x, y, z)).total_degree() == 0

    # ------------------------------------------------------------------
    # Base scheme: all points lie in z=1; quotient length is 13.
    # ------------------------------------------------------------------
    affine_quartics = &#91;sp.expand(q.subs(z, 1)) for q in quartics&#93;
    base_gb = sp.groebner(affine_quartics, x, y, order="grevlex")
    assert base_gb.is_zero_dimensional
    base_length, base_standard = standard_monomials_length(base_gb)
    assert base_length == 13
    expected_base_leading = {(0, 6), (1, 4), (4, 0), (3, 1), (2, 2)}
    assert {tuple(poly.LM(order=base_gb.order).exponents) for poly in base_gb.polys} == expected_base_leading

    # No base point on z=0.  Check the y=1 chart and the point &#91;1:0&#93;.
    infinity_chart = &#91;sp.expand(q.subs({z: 0, y: 1})) for q in quartics&#93;
    assert common_univariate_gcd(infinity_chart, x).degree() == 0
    assert any(sp.expand(q.subs({x: 1, y: 0, z: 0})) != 0 for q in quartics)

    # Reducedness: no base point has Jacobian rank &lt; 2.
    base_jacobian = sp.Matrix(affine_quartics).jacobian(&#91;x, y&#93;)
    jacobian_minors = &#91;
        sp.expand(base_jacobian&#91;i, 0&#93; * base_jacobian&#91;j, 1&#93; - base_jacobian&#91;i, 1&#93; * base_jacobian&#91;j, 0&#93;)
        for i in range(3)
        for j in range(i + 1, 3)
    &#93;
    reduced_test = sp.groebner(affine_quartics + jacobian_minors, x, y, order="grevlex")
    assert list(reduced_test) == &#91;1&#93;

    # ------------------------------------------------------------------
    # Finiteness of the resolved quartic-net morphism.
    # ------------------------------------------------------------------
    # A target &#91;a:b:c&#93; has fibre away from the base scheme cut out by
    #
    #       a*x+b*y+c*z = 0,
    #       a*P+b*Q+c*R = 0.
    #
    # A positive-dimensional fibre therefore occurs exactly when the first
    # line divides the second cubic. Check that this never happens on the
    # target charts c=1, c=0,b=1, and at &#91;1:0:0&#93;.
    restricted_cubic_c1 = sp.expand((a * P + b * Q + R).subs(z, -a * x - b * y))
    restricted_cubic_c1_poly = sp.Poly(restricted_cubic_c1, x, y)
    divisibility_coeffs_c1 = &#91;
        restricted_cubic_c1_poly.coeff_monomial(x**i * y ** (3 - i))
        for i in range(4)
    &#93;
    assert list(sp.groebner(divisibility_coeffs_c1, a, b, order="grevlex")) == &#91;1&#93;

    restricted_cubic_c0_b1 = sp.Poly(sp.expand((a * P + Q).subs(y, -a * x)), x, z)
    divisibility_coeffs_c0_b1 = &#91;
        restricted_cubic_c0_b1.coeff_monomial(x**i * z ** (3 - i))
        for i in range(4)
    &#93;
    assert list(sp.groebner(divisibility_coeffs_c0_b1, a, order="grevlex")) == &#91;1&#93;
    assert sp.expand(P.subs(x, 0)) != 0  # target &#91;1:0:0&#93;

    # ------------------------------------------------------------------
    # Sample fibre over &#91;1:2:3&#93;.  Saturate by q3 in the z=1 chart.
    # ------------------------------------------------------------------
    saturation_variable = sp.symbols("s")
    fibre_eq1 = sp.expand(3 * affine_quartics&#91;0&#93; - affine_quartics&#91;2&#93;)
    fibre_eq2 = sp.expand(3 * affine_quartics&#91;1&#93; - 2 * affine_quartics&#91;2&#93;)
    fibre_sat = sp.groebner(
        &#91;fibre_eq1, fibre_eq2, 1 - saturation_variable * affine_quartics&#91;2&#93;&#93;,
        saturation_variable,
        x,
        y,
        order="lex",
    )
    fibre_elimination = &#91;
        sp.expand(poly.as_expr())
        for poly in fibre_sat.polys
        if not poly.as_expr().has(saturation_variable)
    &#93;
    assert len(fibre_elimination) == 2
    assert x + 2 * y + 3 in fibre_elimination
    fibre_cubic = next(expr for expr in fibre_elimination if not expr.has(x))
    fibre_cubic = sp.Poly(fibre_cubic, y, domain=sp.QQ).primitive()&#91;1&#93;.as_expr()
    assert sp.Poly(fibre_cubic, y).degree() == 3
    fibre_discriminant = int(sp.discriminant(fibre_cubic, y))
    assert fibre_discriminant == -14858267

    # ------------------------------------------------------------------
    # Ramification in the source plane.
    # ------------------------------------------------------------------
    ramification = sp.expand(sp.Matrix(quartics).jacobian(&#91;x, y, z&#93;).det())
    assert sp.Poly(ramification, x, y, z).total_degree() == 9
    ram_constant, ram_factors = sp.factor_list(ramification)
    assert ram_constant == -4
    assert len(ram_factors) == 1 and ram_factors&#91;0&#93;&#91;1&#93; == 1
    assert sp.Poly(ram_factors&#91;0&#93;&#91;0&#93;, x, y, z).total_degree() == 9

    # ------------------------------------------------------------------
    # Branch decic.  A target &#91;a:b:c&#93; corresponds to the line
    # a*x+b*y+c*z=0.  On c=1 use z=-a*x-b*y and restrict aP+bQ+R.
    # Its binary-cubic discriminant is the branch equation.
    # ------------------------------------------------------------------
    restricted_binary_cubic = sp.expand((a * P + b * Q + R).subs(z, -a * x - b * y))
    restricted_univariate = sp.expand(restricted_binary_cubic.subs({x: t, y: 1}))
    assert sp.Poly(restricted_univariate, t).degree() == 3
    branch_affine = sp.Poly(sp.discriminant(restricted_univariate, t), a, b, domain=sp.QQ).primitive()&#91;1&#93;.as_expr()
    branch_affine = sp.expand(branch_affine)
    assert sp.Poly(branch_affine, a, b).total_degree() == 10
    branch = sp.Poly(branch_affine, a, b).homogenize(c).as_expr()
    branch = sp.expand(branch)
    assert sp.Poly(branch, a, b, c).total_degree() == 10
    branch_constant, branch_factors = sp.factor_list(branch)
    assert len(branch_factors) == 1 and branch_factors&#91;0&#93;&#91;1&#93; == 1
    assert sp.Poly(branch_factors&#91;0&#93;&#91;0&#93;, a, b, c).total_degree() == 10

    # ------------------------------------------------------------------
    # Singular scheme of the branch in c=1.
    # ------------------------------------------------------------------
    branch_a = sp.expand(branch.subs(c, 1))
    singular_ideal = &#91;branch_a, sp.diff(branch_a, a), sp.diff(branch_a, b)&#93;
    singular_gb = sp.groebner(singular_ideal, a, b, order="grevlex")
    assert singular_gb.is_zero_dimensional
    singular_length, singular_standard = standard_monomials_length(singular_gb)
    assert singular_length == 42

    # FGLM gives a shape basis.  The univariate polynomial is the square of
    # a squarefree degree-21 polynomial: 21 support points, Jacobian length 2 each.
    singular_lex = singular_gb.fglm(order="lex")
    assert len(singular_lex.polys) == 2
    assert sorted(tuple(poly.LM(order=singular_lex.order).exponents) for poly in singular_lex.polys) == &#91;(0, 42), (1, 0)&#93;
    univariate = next(poly for poly in singular_lex.polys if not poly.as_expr().has(a))
    univariate_poly = sp.Poly(univariate.as_expr(), b, domain=sp.QQ)
    squarefree_data = univariate_poly.sqf_list()&#91;1&#93;
    assert len(squarefree_data) == 1
    support_polynomial, multiplicity = squarefree_data&#91;0&#93;
    assert support_polynomial.degree() == 21 and multiplicity == 2
    assert sp.gcd(support_polynomial, support_polynomial.diff()).degree() == 0

    # No singularity on c=0: check b=1 plus &#91;1:0&#93;.
    branch_derivatives = &#91;branch, sp.diff(branch, a), sp.diff(branch, b), sp.diff(branch, c)&#93;
    infinity_singular_chart = &#91;sp.expand(expr.subs({c: 0, b: 1})) for expr in branch_derivatives&#93;
    assert common_univariate_gcd(infinity_singular_chart, a).degree() == 0
    assert any(sp.expand(expr.subs({a: 1, b: 0, c: 0})) != 0 for expr in branch_derivatives)

    # The quadratic term is nonzero at every singular point.  Combined with
    # local Jacobian length 2, this identifies every point as an A2 cusp.
    second_derivatives = &#91;
        sp.diff(branch_a, a, 2),
        sp.diff(branch_a, a, b),
        sp.diff(branch_a, b, 2),
    &#93;
    zero_quadratic_test = sp.groebner(singular_ideal + second_derivatives, a, b, order="grevlex")
    assert list(zero_quadratic_test) == &#91;1&#93;

    # Numerical consistency with type IV.
    assert 16 - base_length == 3  # (4L-sum E_i)^2
    assert math.comb(9, 2) - 21 == 15  # genus of normalization of a 21-cuspidal decic

    print("explicit type-IV quartic net")
    print("  base scheme: reduced length 13, no point at infinity")
    print("  sample fibre &#91;1:2:3&#93;: 3 distinct points")
    print("  fibre cubic:", fibre_cubic)
    print("  ramification: irreducible degree 9")
    print("  branch: irreducible degree 10 with", len(sp.Poly(branch, a, b, c).terms()), "terms")
    print("  branch singular scheme: length 42 on 21 support points")
    print("  singularities: 21 ordinary A2 cusps")
    print("all explicit-net checks: PASS")

    if args.write_json is not None:
        payload = {
            "schema_version": 1,
            "variables": {
                "source": &#91;"x", "y", "z"&#93;,
                "target": &#91;"a", "b", "c"&#93;,
            },
            "section_TP2_2": {
                "P": str(P),
                "Q": str(Q),
                "R": str(R),
            },
            "quartic_net": {
                "q1": str(q1),
                "q2": str(q2),
                "q3": str(q3),
            },
            "restricted_cubic_c_eq_1": str(restricted_univariate),
            "sample_fibre_1_2_3": {
                "linear_equation": "x + 2*y + 3",
                "cubic_equation": str(fibre_cubic),
                "discriminant": fibre_discriminant,
            },
            "ramification_degree_9": str(ram_factors&#91;0&#93;&#91;0&#93;),
            "branch_affine_c_eq_1": str(branch_affine),
            "branch_homogeneous_degree_10": str(branch),
            "certificates": {
                "base_length": base_length,
                "base_standard_monomials": &#91;list(exp) for exp in base_standard&#93;,
                "base_reduced": True,
                "resolved_map_finite": True,
                "generic_degree": 3,
                "ramification_irreducible_over_Q": True,
                "branch_irreducible_over_Q": True,
                "branch_singular_jacobian_length": singular_length,
                "branch_singular_support_degree": support_polynomial.degree(),
                "branch_local_jacobian_multiplicity": multiplicity,
                "branch_cusp_count": 21,
                "support_polynomial_in_b": str(support_polynomial.as_expr()),
            },
        }
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        payload&#91;"canonical_sha256"&#93; = sha256_text(canonical)
        args.write_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("wrote", args.write_json)
        print("canonical data sha256:", payload&#91;"canonical_sha256"&#93;)


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-a63fd62f849645df"></a>

## `research-notes/lane1-models-20260803-v1/verify_typeiv_hessian_eigensheaf.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checker for the Hessian-resolvent continuation of the explicit type-IV cone.

The input is p1t1_typeIV_explicit_net_data.json from the preceding continuation.
The script reconstructs the Hessian covariant W, the correction row r, the global
rank-one resolvent module over Q(zeta_3), and a 4x4 matrix factorization through
the cone vertex.  It also verifies the universal depressed-cubic conductor and
Kahler-different formulas used in the accompanying note.

Requires: Python 3.10+ and SymPy.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


def canonical_sha256(payload: dict&#91;str, Any&#93;) -&gt; str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def assert_zero(expr: sp.Expr, label: str) -&gt; None:
    if sp.expand(expr) != 0:
        raise AssertionError(f"{label}: expected zero, got {sp.factor(expr)}")


def assert_zero_matrix(mat: sp.Matrix, label: str) -&gt; None:
    for i in range(mat.rows):
        for j in range(mat.cols):
            assert_zero(mat&#91;i, j&#93;, f"{label}&#91;{i},{j}&#93;")


def homogeneous_degree(expr: sp.Expr, variables: Iterable&#91;sp.Symbol&#93;) -&gt; int:
    poly = sp.Poly(sp.expand(expr), *variables)
    degrees = {sum(monomial) for monomial, coeff in poly.terms() if coeff != 0}
    if len(degrees) != 1:
        raise AssertionError(f"polynomial is not homogeneous in {tuple(variables)}: {degrees}")
    return next(iter(degrees))


def matrix_to_strings(mat: sp.Matrix) -&gt; list&#91;list&#91;str&#93;&#93;:
    return &#91;&#91;str(sp.expand(mat&#91;i, j&#93;)) for j in range(mat.cols)&#93; for i in range(mat.rows)&#93;


def parse_args() -&gt; argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    here = Path(__file__).resolve().parent
    parser.add_argument(
        "--input-json",
        type=Path,
        default=here / "typeiv-explicit-net-data.json",
        help="preceding explicit-net JSON certificate",
    )
    parser.add_argument("--write-json", type=Path, help="write reconstructed certificate")
    parser.add_argument("--check-json", type=Path, help="compare reconstructed certificate byte-for-byte")
    return parser.parse_args()


def build_certificate(input_path: Path) -&gt; dict&#91;str, Any&#93;:
    input_bytes = input_path.read_bytes()
    source = json.loads(input_bytes)

    a, b, c = sp.symbols("a b c")
    x, y, z = sp.symbols("x y z")
    rho = sp.symbols("rho")
    target_vars = (a, b, c)
    source_vars = (x, y, z)

    local_env = {name: symbol for name, symbol in zip("abcxyz", (a, b, c, x, y, z))}
    P = sp.sympify(source&#91;"section_TP2_2"&#93;&#91;"P"&#93;, locals=local_env)
    Q = sp.sympify(source&#91;"section_TP2_2"&#93;&#91;"Q"&#93;, locals=local_env)
    R = sp.sympify(source&#91;"section_TP2_2"&#93;&#91;"R"&#93;, locals=local_env)
    branch = sp.sympify(
        source&#91;"branch_homogeneous_degree_10"&#93;, locals={"a": a, "b": b, "c": c}
    )

    # Ternary cubic on the fibre line v.x=0.
    v = sp.Matrix(&#91;a, b, c&#93;)
    G = sp.expand(a * P + b * Q + c * R)
    hessian_G = sp.hessian(G, source_vars)

    # Quadratic Hessian covariant on the fibre line and its polar matrix.
    h = sp.expand(-sp.Rational(1, 4) * (v.T * hessian_G.adjugate() * v)&#91;0&#93;)
    S = (sp.hessian(h, source_vars) / 2).applyfunc(sp.expand)
    cross_v = sp.Matrix(&#91;&#91;0, -c, b&#93;, &#91;c, 0, -a&#93;, &#91;-b, a, 0&#93;&#93;)
    W = (-2 * S * cross_v).applyfunc(sp.expand)

    if homogeneous_degree(h, source_vars) != 2:
        raise AssertionError("h must be quadratic in source variables")
    if homogeneous_degree(h, target_vars) != 4:
        raise AssertionError("h must have target degree four")
    for entry in W:
        if entry != 0 and homogeneous_degree(entry, target_vars) != 5:
            raise AssertionError("W entries must have target degree five")

    assert_zero_matrix(W * v, "Wv")
    assert_zero(sp.trace(W), "trace(W)")

    # W^2 is scalar only after quotienting by the radial relation Av.
    defect_matrix = (W * W + 3 * branch * sp.eye(3)).applyfunc(sp.expand)
    assert_zero_matrix(cross_v * defect_matrix, "K_v(W^2+3BI)")

    # Recover the unique correction row r from the c-row and verify globally.
    row_entries: list&#91;sp.Expr&#93; = &#91;&#93;
    for j in range(3):
        quotient, remainder = sp.div(
            sp.Poly(defect_matrix&#91;2, j&#93;, *target_vars), sp.Poly(c, *target_vars)
        )
        assert_zero(remainder.as_expr(), f"division remainder for r_{j}")
        row_entries.append(sp.expand(quotient.as_expr()))
    r = sp.Matrix(1, 3, row_entries)
    for entry in r:
        if homogeneous_degree(entry, target_vars) != 9:
            raise AssertionError("r entries must have target degree nine")

    assert_zero_matrix(defect_matrix - v * r, "W^2+3BI-vr")
    assert_zero_matrix(r * W, "rW")
    assert_zero((r * v)&#91;0&#93; - 3 * branch, "rv-3B")

    # Exact 4x4 homogeneous matrix factorization over S=k&#91;a,b,c,rho&#93;.
    Phi = (rho * sp.eye(3) - W).row_join(v)
    Phi = Phi.col_join((-r).row_join(sp.Matrix(&#91;&#91;rho&#93;&#93;)))
    Psi = (rho * sp.eye(3) + W).row_join(-v)
    Psi = Psi.col_join(r.row_join(sp.Matrix(&#91;&#91;rho&#93;&#93;)))
    hypersurface = sp.expand(rho**2 + 3 * branch)
    assert_zero_matrix(Phi * Psi - hypersurface * sp.eye(4), "PhiPsi-fI")
    assert_zero_matrix(Psi * Phi - hypersurface * sp.eye(4), "PsiPhi-fI")

    # Exact determinant identity; it also certifies generic rank two of coker(Phi).
    determinant_phi = sp.expand(Phi.det(method="domain-ge"))
    assert_zero(determinant_phi - hypersurface**2, "det(Phi)-f^2")

    # Chart c=1: the induced endomorphism is the classical binary-Hessian matrix.
    t = sp.symbols("t")
    restricted = sp.expand(G.subs({c: 1, x: t, y: 1, z: -a * t - b}))
    coeffs = sp.Poly(restricted, t).all_coeffs()
    if len(coeffs) != 4:
        raise AssertionError("restricted fibre equation is not cubic")
    A0, B0, C0, D0 = coeffs
    H0 = sp.expand(B0**2 - 3 * A0 * C0)
    H1 = sp.expand(B0 * C0 - 9 * A0 * D0)
    H2 = sp.expand(C0**2 - 3 * B0 * D0)
    classical_W = sp.Matrix(&#91;&#91;-H1, 2 * H0&#93;, &#91;-2 * H2, H1&#93;&#93;)
    projection = sp.Matrix(&#91;&#91;1, 0, -a&#93;, &#91;0, 1, -b&#93;&#93;)
    chart_W = (projection * W.subs(c, 1)&#91;:, :2&#93;).applyfunc(sp.expand)
    assert_zero_matrix(chart_W - classical_W, "chart Hessian identity")
    assert_zero_matrix(chart_W * chart_W + 3 * branch.subs(c, 1) * sp.eye(2), "chart square")
    assert_zero(chart_W.det() - 3 * branch.subs(c, 1), "chart determinant")

    # Universal binary-cubic identity, independent of the chosen type-IV net.
    A1, B1, C1, D1 = sp.symbols("A1 B1 C1 D1")
    delta = sp.expand(
        B1**2 * C1**2
        - 4 * A1 * C1**3
        - 4 * B1**3 * D1
        - 27 * A1**2 * D1**2
        + 18 * A1 * B1 * C1 * D1
    )
    UH0 = B1**2 - 3 * A1 * C1
    UH1 = B1 * C1 - 9 * A1 * D1
    UH2 = C1**2 - 3 * B1 * D1
    universal_W = sp.Matrix(&#91;&#91;-UH1, 2 * UH0&#93;, &#91;-2 * UH2, UH1&#93;&#93;)
    assert_zero_matrix(universal_W**2 + 3 * delta * sp.eye(2), "universal Hessian square")

    # Depressed cubic and its transverse A2 matrix factorization.
    p, q = sp.symbols("p q")
    depressed_delta = -4 * p**3 - 27 * q**2
    depressed_W = sp.Matrix(&#91;&#91;9 * q, -6 * p&#93;, &#91;-2 * p**2, -9 * q&#93;&#93;)
    assert_zero_matrix(
        depressed_W**2 + 3 * depressed_delta * sp.eye(2), "depressed Hessian square"
    )
    U = rho - 9 * q
    V = rho + 9 * q
    assert_zero(U * V - 12 * p**3 - (rho**2 + 3 * depressed_delta), "A2 coordinate identity")
    local_phi = rho * sp.eye(2) - depressed_W
    local_psi = rho * sp.eye(2) + depressed_W
    local_f = rho**2 + 3 * depressed_delta
    assert_zero_matrix(local_phi * local_psi - local_f * sp.eye(2), "local phi psi")
    assert_zero_matrix(local_psi * local_phi - local_f * sp.eye(2), "local psi phi")

    # Universal ordered-root normalization and conductor.
    u, vv = sp.symbols("u vv")
    root_p = -u * vv / 3
    root_q = -(u**3 + vv**3) / 27
    root_t = (u + vv) / 3
    root_rho = (u**3 - vv**3) / 3
    assert_zero(root_t**3 + root_p * root_t + root_q, "Cardano cubic")
    assert_zero(root_rho**2 + 3 * depressed_delta.subs({p: root_p, q: root_q}), "Cardano discriminant")
    s = u + vv
    zz = u * vv
    dd = u - vv
    assert_zero(root_rho - dd * (s**2 - zz) / 3, "rho=d(s^2-z)/3")
    derivative = sp.expand(3 * root_t**2 + root_p)
    assert_zero(derivative - (s**2 - zz) / 3, "f'(t)=(s^2-z)/3")
    assert_zero((s**2 - zz) * dd - 3 * root_rho, "conductor generator times d")
    assert_zero(root_rho * dd - (s**2 - 4 * zz) * (s**2 - zz) / 3, "rho times d")

    # Exact normalization-module presentation.  With R=3*rho and ell=s^2-z,
    # C=k&#91;s,z,R&#93;/(R^2-(s^2-4z)*ell^2), and its normalization is generated by
    # 1,d with R=ell*d and d^2=s^2-4z.  Modulo the copy of C generated by 1,
    # the quotient is C/(R,ell), proving the conductor formula.
    ss, z0, RR, d0 = sp.symbols("ss z0 RR d0")
    ell = ss**2 - z0
    delta0 = ss**2 - 4 * z0
    conductor_hypersurface = RR**2 - delta0 * ell**2
    normalization_matrix = sp.Matrix(&#91;&#91;-RR, -delta0 * ell&#93;, &#91;ell, RR&#93;&#93;)
    assert_zero_matrix(
        normalization_matrix**2 - conductor_hypersurface * sp.eye(2),
        "normalization conductor matrix factorization",
    )
    relation_values = normalization_matrix.subs({RR: ell * d0, delta0: d0**2})
    assert_zero(relation_values&#91;0, 0&#93; + relation_values&#91;1, 0&#93; * d0, "normalization relation 1")
    assert_zero(relation_values&#91;0, 1&#93; + relation_values&#91;1, 1&#93; * d0, "normalization relation 2")

    # Kahler different of k&#91;u,v&#93; over k&#91;u^3,v^3,uv&#93;.
    relation_matrix = sp.Matrix(&#91;&#91;3 * u**2, 0, vv&#93;, &#91;0, 3 * vv**2, u&#93;&#93;)
    kahler_minors = &#91;
        sp.expand(relation_matrix&#91;:, &#91;0, 1&#93;&#93;.det()),
        sp.expand(relation_matrix&#91;:, &#91;0, 2&#93;&#93;.det()),
        sp.expand(relation_matrix&#91;:, &#91;1, 2&#93;&#93;.det()),
    &#93;
    expected_minors = &#91;9 * u**2 * vv**2, 3 * u**3, -3 * vv**3&#93;
    for i, (actual, expected) in enumerate(zip(kahler_minors, expected_minors)):
        assert_zero(actual - expected, f"Kahler minor {i}")

    # Fitting support of the normalization index M/WM.
    index_presentation = v.row_join(W)
    maximal_minors = &#91;&#93;
    expected_quotients = &#91;0, 3 * a, -3 * b, 3 * c&#93;
    for omitted in range(4):
        columns = &#91;j for j in range(4) if j != omitted&#93;
        minor = sp.expand(index_presentation&#91;:, columns&#93;.det())
        maximal_minors.append(minor)
        assert_zero(minor - expected_quotients&#91;omitted&#93; * branch, f"index minor {omitted}")

    payload: dict&#91;str, Any&#93; = {
        "schema_version": 2,
        "input_file": input_path.name,
        "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "base_field": "Q",
        "splitting_field": "Q(zeta_3)",
        "resolvent_coordinate": {
            "lambda": "zeta_3-zeta_3**2",
            "lambda_square": "-3",
            "rho": "lambda*w",
            "equation": str(hypersurface),
            "rho_degree": 5,
        },
        "hessian_covariant": {
            "definition": "h=-(1/4)*v^T*adj(Hess_x(aP+bQ+cR))*v; S=(1/2)*Hess_x(h); W=-2*S*K_v",
            "h": str(h),
            "W": matrix_to_strings(W),
            "correction_row_r": matrix_to_strings(r)&#91;0&#93;,
        },
        "module_presentations": {
            "M": "A(-4) --(a,b,c)^T--&gt; A(-3)^3 --&gt; M --&gt; 0",
            "L": "Qrho(-4) plus Qrho(-8)^3 --&#91;v | rho*I-W&#93;--&gt; Qrho(-3)^3 --&gt; L --&gt; 0",
            "P": "coker(Phi), with Phi: Qrho(-8)^3 plus Qrho(-4) -&gt; Qrho(-3)^3 plus Qrho(1)",
            "extension": "0 --&gt; Qrho(1) --&gt; P --&gt; L --&gt; 0",
            "normalization_index": "T/(Qrho tensor_A B) is isomorphic as an A-module to M/W*M",
        },
        "matrix_factorization": {
            "Phi_block_form": "&#91;&#91;rho*I-W, v&#93;,&#91;-r,rho&#93;&#93;",
            "Psi_block_form": "&#91;&#91;rho*I+W,-v&#93;,&#91;r,rho&#93;&#93;",
            "Phi": matrix_to_strings(Phi),
            "Psi": matrix_to_strings(Psi),
            "hypersurface": str(hypersurface),
            "determinant": str(determinant_phi),
            "determinant_identity": "det(Phi)=hypersurface**2",
        },
        "local_models": {
            "binary_hessian_matrix": "&#91;&#91;-H1,2*H0&#93;,&#91;-2*H2,H1&#93;&#93;",
            "binary_hessian_coefficients": {
                "H0": "B^2-3*A*C",
                "H1": "B*C-9*A*D",
                "H2": "C^2-3*B*D",
            },
            "depressed_cubic": "t^3+p*t+q",
            "discriminant": str(depressed_delta),
            "W_depressed": matrix_to_strings(depressed_W),
            "A2_coordinates": {"U": str(U), "V": str(V), "equation": "U*V=12*p^3"},
            "conductor_order_in_normalization": "(rho,3*t^2+p)",
            "kahler_different_T_over_Q": "(u^3,v^3,u^2*v^2)",
        },
        "index_fitting": {
            "presentation": "coker(&#91;v|W&#93;)",
            "maximal_minors": &#91;str(m) for m in maximal_minors&#93;,
            "ideal": "branch*(a,b,c)",
            "annihilator": "(branch)",
            "Q_scalar_conductor": "(rho)",
        },
        "certificates": {
            "h_source_degree": 2,
            "h_target_degree": 4,
            "W_target_degree": 5,
            "r_target_degree": 9,
            "Wv_zero": True,
            "trace_W_zero": True,
            "W_square_mod_radial": True,
            "rW_zero": True,
            "rv_equals_3_branch": True,
            "matrix_factorization_both_orders": True,
            "chart_binary_hessian_identity": True,
            "universal_binary_hessian_identity": True,
            "local_A2_class_nonfree": True,
            "universal_conductor_identity": True,
            "normalization_conductor_presentation": True,
            "kahler_different_identity": True,
            "index_fitting_identity": True,
        },
    }
    payload&#91;"canonical_sha256"&#93; = canonical_sha256(payload)
    return payload


def main() -&gt; None:
    args = parse_args()
    payload = build_certificate(args.input_json)
    rendered = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True) + "\n"

    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
        print(f"WROTE {args.write_json}")

    if args.check_json:
        expected = args.check_json.read_text(encoding="utf-8")
        if rendered != expected:
            raise AssertionError(f"reconstructed JSON differs from {args.check_json}")
        print(f"PASS byte-for-byte certificate replay: {args.check_json}")

    cert = payload&#91;"certificates"&#93;
    print("PASS Hessian covariant: Wv=0 and W^2=-3*branch on M")
    print("PASS correction row: W^2+3*branch*I=v*r, rW=0, rv=3*branch")
    print("PASS global 4x4 matrix factorization in both orders")
    print("PASS chart c=1 equals the classical binary-Hessian endomorphism")
    print("PASS transverse depressed-cubic model is A2 with a nonfree order-three class")
    print("PASS universal conductor and Kahler-different identities")
    print("PASS normalization-index Fitting ideal = branch*(a,b,c)")
    print(f"canonical_sha256={payload&#91;'canonical_sha256'&#93;}")
    if not all(cert.values()):
        raise AssertionError("one or more boolean certificates are false")


if __name__ == "__main__":
    main()
</code></pre>

[Back to Lane 1](cubic-flatness-normalization-defects.md)
