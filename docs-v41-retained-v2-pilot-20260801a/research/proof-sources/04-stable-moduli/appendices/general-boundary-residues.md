---
title: "Text proof source — 04-stable-moduli/appendices/general-boundary-residues.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `5de53be9b8de879a01c753a90c8f95a5cd9cda8962493f69673cc4f38fadef9f` · 8,590 bytes

## Exact label anchors

<a id="label-app-general-boundary-residues"></a>
- `app:general-boundary-residues` — source line 2
<a id="label-prop-general-frame"></a>
- `prop:general-frame` — source line 28
<a id="label-thm-general-boundary-torelli"></a>
- `thm:general-boundary-torelli` — source line 100
<a id="label-cor-large-stable-moduli"></a>
- `cor:large-stable-moduli` — source line 209

## Complete source

~~~tex
\section{Boundary residues for general squarefree cubic frames}
\label{app:general-boundary-residues}

The one-parameter invariant is the first member of a general construction.
We record the squarefree statement here; the full standalone sequel source,
including expanded calculations and examples, is retained under
\path{supplements/}.

\begin{definition}[Admissible frame]
A pair \(A,B\in\C[c]\) is admissible if
\[
A(0)=0,\quad A'(0)=1,\qquad
B(0)=-2,\quad B'(0)=-2A''(0).
\]
Using
\[
c=2x-3x^2y-x^3z,\qquad
t=y+\frac1x,\qquad r=\frac2x,
\]
define \(G_{A,B}=(a,b,c)\) by
\[
b=r-3A(c)t^2-2B(c)t,\qquad
2a=A(c)t^3+B(c)t^2+tb.
\]
\end{definition}

\begin{proposition}[Universal cubic frame]
\label{prop:general-frame}
For every admissible pair, \(G_{A,B}\) is polynomial and
\[
\det DG_{A,B}=-2.
\]
If \(A\ne0\), its generic degree is three.
\end{proposition}

\begin{proof}
Write
\[
A=c+a_2c^2+c^3A_3(c),\qquad
B=-2-4a_2c+c^2B_2(c),
\]
which is equivalent to the four admissibility conditions.  With
\(\xi=1+xy\), \(d=2-3xy-x^2z\), \(c=xd\), and \(t=\xi/x\), the only
terms that can have poles are
\[
\frac{2+4\xi-3d\xi^2}{x}
\quad\text{and}\quad
\frac{2\xi-2d\xi^3+2\xi^2}{x^2}
+\frac{2a_2d\xi^2(2-d\xi)}{x}.
\]
The three factorizations displayed in the proof of \cref{prop:basic} show
that these are polynomial.  Every term involving \(c^3A_3\) or \(c^2B_2\)
is already polynomial after substituting \(c=xd\) and \(t=\xi/x\).

On \(x\ne0\),
the change \((x,y,z)\mapsto(t,r,c)\) has determinant \(-2x\), while
\((t,r,c)\mapsto(a,b,c)\) has determinant \(r/2\).  Since \(r=2/x\),
the product is \(-2\), and polynomiality extends it across \(x=0\).
Finite simple roots of
\[
A(c)T^3+B(c)T^2+bT-2a
\]
recover the source, giving generic degree three.
\end{proof}

Assume now that \(A\) is squarefree and \(\gcd(A,B)=1\).  Put
\[
Z_A^\circ=V(A/c)\subset\Gm.
\]
Homogenizing the inverse cubic gives
\[
A(c)U^3+B(c)U^2V+bUV^2-2aV^3=0.
\]
At a root \(s\) of \(A\), in the local coordinate \(V/U\), the transverse
derivative of the infinity section is \(B(s)\).  The root over \(c=0\) is
retained in the affine source; the roots in \(Z_A^\circ\) are deleted.
Thus the natural decorated infinity datum is
\[
\left(Z_A^\circ,\ \sigma_B=B|_{Z_A^\circ}\right).
\]

The discriminant component is normalized by
\[
\nu_{A,B}\colon\A^2_{c,t}\longrightarrow D_{A,B},
\]
\[
b=-3A(c)t^2-2B(c)t,\qquad
a=-A(c)t^3-\frac12B(c)t^2.
\]
The preimage of its singular locus is
\[
L_{A,B}=V(3A(c)t+B(c)),
\]
and the deleted infinity components lift to the vertical lines
\[
M_s=V(c-s),\qquad s\in Z_A^\circ.
\]

\begin{theorem}[Stable boundary Torelli on the squarefree locus]
\label{thm:general-boundary-torelli}
Let \((A,B)\) and \((\widetilde A,\widetilde B)\) be admissible squarefree
coprime pairs.  The following are equivalent:
\begin{enumerate}[label=(\roman*)]
\item \(G_{A,B}\) and \(G_{\widetilde A,\widetilde B}\) are stably
polynomially left--right equivalent;
\item they are ordinarily polynomially left--right equivalent;
\item there is \(u\in\C^*\) such that
\[
\widetilde A(uc)=uA(c),\qquad
\widetilde B(uc)-B(c)\in cA(c)\C[c];
\]
\item multiplication by \(u\) identifies the decorated finite schemes
\[
(Z_A^\circ,\sigma_B)
\quad\text{and}\quad
(Z_{\widetilde A}^\circ,\sigma_{\widetilde B}).
\]
\end{enumerate}
\end{theorem}

\begin{proof}
A stable equivalence preserves the reduced nonproperness divisor.  First
dispose of the cases in which the deleted scheme is empty.  Since an
admissible \(A\) has a simple zero at the origin, \(Z_A^\circ=\varnothing\)
is equivalent to \(A=c\).  If exactly one deleted scheme is empty, the two
nonproperness divisors have different numbers of irreducible components;
hence (i) is false, as are (iii) and (iv).  If both are empty, then
\(A=\widetilde A=c\), while admissibility makes
\(\widetilde B-B\) divisible by \(c^2=cA\).  Thus (iii) holds (with
\(u=1\)), and the root translation below proves (ii).  This also settles
the empty--empty instance of (iv).

Assume henceforth that both deleted schemes are nonempty.  The unique
singular nonplane component of the nonproperness divisor is the primitive
discriminant component; its other components are the planes \(c=s\),
\(s\in Z_A^\circ\).  Passing to normalizations gives an automorphism of a
cylinder over \(\A^2_{c,t}\) preserving \(L_{A,B}\) and the union of the
vertical lines.

Write \(Q_A=A/c\), and let \(C,T\) be the pullbacks of the target
normalization coordinates.  Unique factorization gives
\[
Q_{\widetilde A}(C)=\lambda Q_A(c),\qquad \lambda\in\C^*.
\]
Hence \(C\) is algebraic over \(\C(c)\).  The field \(\C(c)\) is relatively
algebraically closed in the purely transcendental cylinder function field,
so \(C\in\C(c)\).  Polynomiality of the automorphism and the same argument
for its inverse force
\[
C=uc+v,\qquad u\in\C^*.
\]

Preservation of the irreducible singular-preimage curve gives
\[
3\widetilde A(C)T+\widetilde B(C)
=\kappa(3A(c)t+B(c)),\qquad \kappa\in\C^*.
\]
Solving this identity shows that \(T\) has no stabilization-variable
dependence and has the form \(T=\mu(c)t+h(c)\).  In coordinates
\((c,t,w_1,\ldots,w_m)\), the full cylinder Jacobian factors as
\[
C'(c)\mu(c)
\det\!\left(\frac{\partial(W_1,\ldots,W_m)}
{\partial(w_1,\ldots,w_m)}\right).
\]
It is a nonzero constant, so \(\mu\in\C^*\).

Comparing \(t\)-coefficients shows that \(C\) carries the complete root set
of \(A\) to that of \(\widetilde A\).  It already carries the deleted roots
to the deleted roots, so the sole retained root is preserved and \(v=0\).
The constant coefficient at \(c=0\) gives \(\kappa=1\); differentiating the
\(t\)-coefficient at zero then gives \(u\mu=1\).  Consequently
\[
\widetilde A(uc)=uA(c).
\]
The remaining coefficient identity is
\[
\widetilde B(uc)-B(c)=-3uA(c)h(c).
\]
Its derivative at zero vanishes by admissibility and the displayed identity
for \(A\); hence \(h(0)=0\), proving (iii).

For (iii)\(\Leftrightarrow\)(iv), equality of the residue values at every
root of the squarefree \(Q_A\) is equivalent to divisibility of
\(\widetilde B(uc)-B(c)\) by \(Q_A\).  Admissibility and the scaled
\(A\)-identity make the same difference divisible by \(c^2\).  Since
\((c,Q_A)=1\), this is exactly divisibility by \(c^2Q_A=cA\).

Finally, after the diagonal change
\[
(x,y,z)\mapsto(ux,y/u,z/u^2),\qquad
(a,b,c)\mapsto(a/u^2,b/u,uc),
\]
condition (iii) reduces to
\[
\widetilde B-B=3A\phi,\qquad \phi\in c\C[c].
\]
The source root translation
\[
(x,y,z)\mapsto
\left(x,y+\phi(c),z-3\frac{\phi(c)}x\right)
\]
is polynomial, preserves \(c\), and shifts \(t\) by \(\phi(c)\).
Expanding the cubic supplies a triangular target automorphism, proving
ordinary left--right equivalence.
\end{proof}

\begin{corollary}[Arbitrarily large fixed-degree stable moduli]
\label{cor:large-stable-moduli}
If \(\deg A=N+1\), the generic squarefree orbit space is
\[
\frac{
\{(s_i,v_i)_{i=1}^N\in(\Gm\times\Gm)^N:s_i\ne s_j\}
}{\Gm\times S_N},
\]
where \(\Gm\) scales the \(s_i\) and fixes the \(v_i\).  Its generic
dimension is \(2N-1\).  Fixing a root configuration with no scaling symmetry
leaves an \(N\)-dimensional family of pairwise stably inequivalent maps.
With the canonical interpolating representative for \(B\), every map in
such a family has
\[
\begin{gathered}
\det DG=-2,\qquad \mu(G)=3,\\
(\deg G_1,\deg G_2,\deg G_3)=(4N+7,4N+6,4).
\end{gathered}
\]
Here ``dimension'' means the dimension of the indicated coarse orbit locus;
the quotient notation does not assert that the unrestricted stable
left--right moduli functor is represented by this variety.
\end{corollary}

\begin{remark}[The quadratic modulus]
For
\[
A=c+\alpha c^2,\qquad B=-2-4\alpha c+\beta c^2,
\]
the unique deleted infinity point is \(-1/\alpha\), and
\[
B(-1/\alpha)=2+\frac{\beta}{\alpha^2}=q+2.
\]
Thus \(q\) is the normalized transverse derivative at the deleted infinity
section.  Equivalently, it is the principal part of the rational
Tschirnhaus translation needed to identify the cubic frames.  At \(q=-2\)
that derivative vanishes and the deleted section becomes ramified.
\end{remark}

\paragraph{Proof boundary.}
The exact verifier checks all displayed polynomial identities, the frame
Jacobian, the marked infinity section, the root-translation gauge, and an
explicit three-parameter interpolation family.  The four load-bearing
geometric steps---identification of the affine open in the finite
completion, equality with the nonproperness locus, lifting stable
equivalences through normalization, and rigidity of the marked vertical
cylinder---still require independent specialist review.
~~~

[Back to the text-source index](../../index.md)
