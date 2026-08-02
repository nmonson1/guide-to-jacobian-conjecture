# Stable boundary Torelli on the squarefree locus

`RMU-47B48FBA` · `theorem`

This page is generated from the retained mathematical graph.

## Mathematical record

`RMU-47B48FBA` · `theorem`

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

Support:

- **proof:** A proof body follows this labelled manuscript statement. — Inline support is reproduced on the unit record.

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

  - Full source and surrounding context: [`manuscripts/04-stable-moduli/appendices/general-boundary-residues.tex#thm:general-boundary-torelli`](../../proof-sources/04-stable-moduli/appendices/general-boundary-residues.md#label-thm-general-boundary-torelli)
