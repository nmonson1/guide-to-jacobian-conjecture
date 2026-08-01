---
title: "Text proof source — 06-plane-boundary/appendices/degree-twenty-one-certificates.tex"
description: "Sanitized current source with exact TeX-label anchors."
---

# Text proof source

`manuscripts/06-plane-boundary/appendices/degree-twenty-one-certificates.tex`

This is the current sanitized source text used by the retained working graph. Comments and private locators are omitted; mathematical content and line numbering are preserved. PDFs are optional reading copies.

Published SHA-256: `a6ab7aef2666462fed4ba5968c13d6f14475bb8ef8be1113a28df3db0d95c8a5` · 20,152 bytes

## Exact label anchors

<a id="label-app-degree-twenty-one"></a>
- `app:degree-twenty-one` — source line 3
<a id="label-eq-degree21-face"></a>
- `eq:degree21-face` — source line 28
<a id="label-prop-degree21-belyi"></a>
- `prop:degree21-belyi` — source line 33
<a id="label-thm-borisov-fminusfive"></a>
- `thm:borisov-fminusfive` — source line 82
<a id="label-prop-terminal-residue-provenance"></a>
- `prop:terminal-residue-provenance` — source line 208
<a id="label-thm-terminal-unit"></a>
- `thm:terminal-unit` — source line 243
<a id="label-thm-branchwise-terminal-unit"></a>
- `thm:branchwise-terminal-unit` — source line 287
<a id="label-thm-terminal-toric-certificate"></a>
- `thm:terminal-toric-certificate` — source line 329
<a id="label-subsec-two-chart-layer-seven"></a>
- `subsec:two-chart-layer-seven` — source line 378
<a id="label-prop-k4-chart-transition"></a>
- `prop:k4-chart-transition` — source line 386
<a id="label-thm-stored-terminal-layer-seven"></a>
- `thm:stored-terminal-layer-seven` — source line 433

## Complete source

~~~tex
\section{The degree-\texorpdfstring{\(21\)}{21} divisor and terminal
  certificates}
\label{app:degree-twenty-one}

The body develops the lattice-gap quotient covers.  Here we record the
complementary calculation on the original lower face and the exact
certificates obtained after substituting its five dessins into the two
surviving Newton supports.

\subsection{The lower face}

For either surviving support in the reduction of Guccione et al.
\cite{guccioneEtAl2022degree108}, the transformed bracket is
\[
[P,Q]=X^2.
\]
For the primitive toric valuation
\[
\nu(X)=-2,\qquad \nu(Y)=1,
\]
put \(z=XY^2\).  The lower faces have the form
\[
P_{\mathrm{face}}=Xp(z),\qquad
Q_{\mathrm{face}}=X^2Yq(z),
\]
where \(\deg p=7\), \(\deg q=10\), and
\begin{equation}
\label{eq:degree21-face}
pq+2zpq'-3zp'q=1.
\end{equation}

\begin{proposition}[The degree-\(21\) Belyi map]
\label{prop:degree21-belyi}
The rational function
\[
\tau(z)=z\frac{q(z)^2}{p(z)^3}
\]
is a degree-\(21\) Belyi map with passport
\[
(2^{10}1),\qquad(3^7),\qquad(17\,1^4).
\]
There are exactly five connected dessin isomorphism classes with this
passport.  They form one arithmetic orbit over an irreducible quintic field
and have monodromy \(A_{21}\).
\end{proposition}

\begin{proof}
Equation \eqref{eq:degree21-face} implies that \(p,q\) are coprime and
nonzero at zero.  Differentiation gives
\[
\tau'(z)=\frac{q(z)}{p(z)^4}.
\]
Thus the ten roots of \(q\) give double zeros, the seven roots of \(p\)
give triple poles, and infinity has ramification index \(17\).  The total
ramification is
\[
10+14+16=40=2\cdot21-2,
\]
so there is no additional branch value.

The exact Murnaghan--Nakayama character calculation in \(S_{21}\), followed
by the class-size factor, gives \(5\cdot21!\) labeled triples.  Each is
transitive, and the deck group is trivial, so there are five isomorphism
classes.  Exact coefficient reconstruction places all five over one
quintic field.  It remains to identify the monodromy group \(G\).  All three
branch permutations are even, so \(G\subseteq A_{21}\).  Transitivity rules
out every nontrivial block size except \(3\) and \(7\).  A \(17\)-cycle acts
trivially on a set of \(7\) or \(3\) blocks, since neither \(S_7\) nor \(S_3\)
has an element of order \(17\).  It would therefore preserve every block,
but a block containing a moved point would contain the entire
\(17\)-element orbit, a contradiction.  Thus \(G\) is primitive.  Jordan's
theorem for a primitive group containing a prime cycle of length
\(17\le21-3\) gives \(A_{21}\subseteq G\), and hence \(G=A_{21}\).
The enumeration and coefficient reconstruction remain computer-assisted;
the monodromy identification no longer depends on a permutation
certificate.
\end{proof}

\subsection{Identification with Borisov's divisor}

\begin{theorem}[Valuation over \(F_{-5}\)]
\label{thm:borisov-fminusfive}
Let \(E_\nu\) be the source divisor defined by \(\nu\).  Its target center is
Borisov's divisor \(F_{-5}\).  The normal ramification index and residue
degree are
\[
(e,f)=(1,21).
\]
Consequently neither surviving Newton support can realize Borisov's
Three-dessin framework.
\end{theorem}

\begin{proof}
Set \(t=Y\), so \(x=t^2/z\) in the original source coordinates.  The source
volume form is
\[
dx\wedge dy=t^{-6}z^2\,dt\wedge dz.
\]
After adding the reduced boundary coefficient, the augmented-canonical label
is \(-5\).

The face expansions are
\[
P=t^{-2}zp(z)+\text{higher \(\nu\)-terms},\qquad
Q=t^{-3}z^2q(z)+\text{higher \(\nu\)-terms}.
\]
On the target put
\[
s=\frac P Q,\qquad \lambda=\frac{Q^2}{P^3}.
\]
Then \(s\) is a uniformizer and
\[
dP\wedge dQ=-s^{-6}\lambda^{-3}\,ds\wedge d\lambda,
\]
so the target label is also \(-5\).  Pullback gives
\[
\frac P Q
=t\left(\frac{p(z)}{zq(z)}+O(t)\right),
\]
hence \(e=1\).  The residue of \(\lambda\) is
\[
\operatorname{res}_{E_\nu}(\lambda)
=z\frac{q(z)^2}{p(z)^3}=\tau(z),
\]
so \(f=21\) by \cref{prop:degree21-belyi}.

In Borisov's target coordinates \((y_1,y_2)=(Q,P)\), the divisor
\(F_{-5}\) is characterized by valuations \((-3,-2)\) and by the
nonconstant residual parameter \(y_1^2/y_2^3\).  Those are exactly the
values above.  Later infinitely-near divisors with the same two numerical
orders have constant residue of this parameter, so they are distinguished.

For clarity, the complete dictionary at the generic points is
\[
\begin{array}{c|c|c}
 & E_\nu\text{ on the source} & F_{-5}\text{ on the target}\\ \hline
\text{normal parameter} & t=Y & s=P/Q\\
\text{residual parameter} & z=XY^2 & \lambda=Q^2/P^3\\
\text{orders of }(P,Q) & (-2,-3) & (-2,-3)\\
\text{normal map} & s=t\bigl(p/(zq)+O(t)\bigr) & e=1\\
\text{residue map} & z\longmapsto zq^2/p^3 & f=21
\end{array}
\]
Equivalently, at the completed generic points the map has the form
\[
\operatorname{Spec}k(E_\nu)[[t]]
\ \xrightarrow{\quad s=t\,u(z,t),\ \lambda=\tau(z)+O(t)\quad}\
\operatorname{Spec}k(F_{-5})[[s]],
\]
where \(u(z,0)=p(z)/(zq(z))\) is a unit and
\([k(E_\nu):k(F_{-5})]=\deg\tau=21\).

Borisov's Three-dessin framework gives residue degree \(16\) on its unique
source divisor above \(F_{-5}\) \cite{borisov2020frameworks}.  The forced
divisor has residue degree
\(21\), a contradiction.  This excludes the named framework, not the two
supports themselves.
\end{proof}

\begin{corollary}
Any plane counterexample of maximum coordinate degree below \(125\) has
generic degree at least \(21\).
\end{corollary}

\begin{proof}
The published below-\(125\) reduction leaves the two supports above, and the
generic-degree formula contains the contribution \(ef=21\) from
\cref{thm:borisov-fminusfive}.
\end{proof}

\begin{question}
Is \(E_\nu\) the only source divisor over the generic point of \(F_{-5}\)?
The calculation \(f=21\) is one residue-degree contribution; cancellation
valuations or infinitely-near divisors could contribute additional sheets.
\end{question}

\subsection{Exact support certificates}

An independent exact program starts with all lattice points of each
normalized Newton support and the deficiencies
\[
d_P(i,j)=j-2i+2,\qquad d_Q(i,j)=j-2i+3.
\]
It reconstructs the lower face over the quintic field and checks all
eighteen coefficients of \eqref{eq:degree21-face}.  For the truncated
support, seven weight-three compatibility equations and eighteen
weight-four equations span all fourteen weight-four monomials in the four
effective positive-weight parameters.  Hence these parameters lie in the
radical of the obstruction ideal, forcing the required top vertices to
vanish.  The vertex-saturated truncated system is therefore empty in
characteristic zero.  Because the computation is carried out in the
quintic coefficient field, the same conclusion holds for all five
conjugate dessins.

For the full support, the same direct layer recursion reaches a weight-four
perfect square.  On its zero set the top \(P\)- and \(Q\)-vertex
coefficients are nonzero multiples of \(t_{1,1}^2\) and \(t_{1,1}^3\);
vertex saturation therefore permits the normalization \(t_{1,1}=1\).
Exact layer elimination then reduces the problem to fifteen equations in
five variables over the same quintic field.
For the residue and five-variable terminal systems, write
\[
K_0=\mathbb Q[u]/(u^5-u^4+3u^3+3u^2+26).
\]
Six selected equations already generate the unit ideal.

\begin{proposition}[Exact residue provenance of the terminal equations]
\label{prop:terminal-residue-provenance}
For the stored lower face and normal-layer forcing terms through order
\(8\), every archived layer matrix is the matrix of
\(\mathscr D_r^{2,3}\) in the displayed monomial windows.  Every left-null
row is represented by an explicit principal part \(\lambda\) satisfying the
filtered adjoint equations, and its compatibility polynomial is exactly
\[
\operatorname{Res}_{z=0}\bigl(\lambda(-\Phi_r)\bigr).
\]
Before parameter normalization, the numbers of nonzero compatibility
polynomials at layers \(6,7,8\) are \(4,5,6\).  After the recorded
normalization and duplicate removal, the distinct equations have counts
\[
(1,3,5,6)\quad\text{at layers}\quad(5,6,7,8).
\]
The resulting fifteen equations agree coefficientwise with the archived
normalized system, and the six equations used below are the coordinate
projection with zero-based archived indices \(4,6,8,9,10,11\).
\end{proposition}

\begin{proof}[Exact computer-assisted proof]
The supplement rebuilds the lower face over
\(\mathbb Q[u]/(u^5-u^4+3u^3+3u^2+26)\), forms every matrix directly from
\(\mathscr D_r^{2,3}\), and computes exact row-reduction transforms.
For each left-null row it constructs the dual principal part and verifies
the two filtered formal-adjoint equations coefficientwise.  Pairing that
principal part with \(-\Phi_r\) reproduces the row-reduced compatibility
polynomial exactly.  The normalization map is then applied symbolically;
the resulting fifteen polynomials are compared term by term with the
archived JSON representation.  The replay writes the bases, matrices,
principal parts, normalization map, comparison, and projection matrix to
machine-readable audit files.
\end{proof}

\begin{theorem}[Conditional five-variable terminal unit-ideal certificate]
\label{thm:terminal-unit}
Suppose replay of the archived Macaulay data confirms that its \(7{,}121\)
rows are the complete ordered target monomial basis, that this basis contains
\(1\), and that the certified \(7{,}121\)-by-\(7{,}121\) minor uses every
target row.  Then, for the stored normalized full-support system, the six
selected obstruction equations generate the unit ideal over \(K_0\).
\end{theorem}

\begin{proof}[Exact computer-assisted certificate]
For the six selected polynomials \(F_i\), let \(V_i\) be the recorded
multiplier spaces and let \(W\) be the recorded target monomial space.  The
Macaulay map
\[
\mu:\bigoplus_{i=1}^6V_i\longrightarrow W,
\qquad (H_i)_i\longmapsto\sum_i H_iF_i
\]
has \(10{,}824\) columns.  The certificate must verify that its
\(7{,}121\) rows are the complete ordered basis of \(W\), that this basis
contains the constant monomial \(1\), and that the selected
\(7{,}121\)-by-\(7{,}121\) minor uses every target row.  Subject to those
three replay conditions, reduction at a good prime and at the selected
quintic embedding gives
\[
\det=859\pmod{2053}.
\]
The determinant is therefore nonzero in characteristic zero and \(\mu\) is
surjective, so \(1\in(F_1,\ldots,F_6)\).  If the recorded rows are only a
subset of a larger target basis, the minor proves only a rank statement and
does not prove the conclusion.  The certificate package regenerates all
fifteen exact equations, rebuilds the matrix, and replays the fixed pivot
minor; confirming the three target-basis conditions is an explicit audit
obligation.
\end{proof}

There is also a later, branchwise exact certificate for the same terminal
analysis.  After the ordinary branches are eliminated, two exceptional
systems remain; denote their ideals in
\(K_\eta[I,H,G,A]\) by \(I_+\) and \(I_-\), where
\(K_\eta=\mathbb Q[\eta]/(T(\eta))\) and the explicit quintic
\(T\) is recorded with the branch certificate.  We keep this field model
separate from \(K_0\); the branch certificate is checked in its displayed
primitive element and does not require an unstated identification of the two.

\begin{theorem}[Branchwise exact Nullstellensatz certificates]
\label{thm:branchwise-terminal-unit}
For each sign, the stored nine-generator ideal is the unit ideal:
\[
I_+=K_\eta[I,H,G,A],\qquad I_-=K_\eta[I,H,G,A].
\]
More precisely, the supplement gives cofactors \(C_{\epsilon,j}\) such that
\[
\sum_{j=0}^{8}C_{\epsilon,j}F_{\epsilon,j}=1,
\qquad \epsilon\in\{+,-\},
\]
and every product \(C_{\epsilon,j}F_{\epsilon,j}\) has total degree at most
five.
\end{theorem}

\begin{proof}[Exact computer-assisted certificate]
The monomials of total degree at most five in four variables span a
\(126\)-dimensional space.  Modular row reduction at \(p=31\), using a root
of the quintic field polynomial, selects \(111\) rows.  The two selected
\(111\times111\) minors have determinants \(1\) and \(17\) modulo \(31\).
Exact rational elimination then produces 80 nonzero cofactor monomials for
each sign.  A separate GMP program and an independently written
rational-arithmetic Python implementation multiply the cofactors by the
original generators, reduce in the quintic field, and recover exactly the
constant polynomial \(1\).
\end{proof}

The compact source distribution contains the branch generators and replay
programs; the companion large-data archive contains the selected matrices
and exact cofactors.  This certificate is unconditional for the two stored
ideals.  Its use in the global support analysis still depends on the prior
reduction from the five-variable terminal system to the two exceptional
branches.

Combining the truncated resultant with either terminal certificate
architecture eliminates both encoded support alternatives after the
degree-\(21\) face substitution.  This statement is exact for the stored
systems.  Turning it into a stand-alone global below-\(125\) proof requires a
line-by-line audit that the published Newton reduction, the five faces, all
saturations and normalizations, the ordinary-branch elimination, and the
layer systems exhaust every candidate.

\begin{theorem}[Compact toric terminal certificate]
\label{thm:terminal-toric-certificate}
Let
\[
\rho=F_4,\qquad(g_1,g_2,g_3,g_4,g_5)
=(F_6,F_8,F_9,F_{10},F_{11})
\]
be the six exact normalized obstruction polynomials in the supplement.
Then
\[
V(\rho,g_1,g_2,g_3,g_4,g_5)(\overline {K_0})=\varnothing
\]
over the quintic coefficient field \(K_0\).
\end{theorem}

\begin{proof}[Exact computer-assisted proof]
At \(p=2053\) and the split value \(u=216\), the five \(g_i\) have mixed
volume \(296\).  The Minkowski sum has \(344\) proper faces: \(270\) have a
monomial initial form, and exact saturated Laurent calculations show that
the other \(74\) initial ideals are unit ideals.  Hence the entire special
toric intersection is the reduced \(296\)-point scheme represented by the
archived multiplication matrices.  Multiplication by \(\rho\) has
determinant \(682\ne0\pmod{2053}\).

Let \(R\) be the unramified local DVR at \((2053,u-216)\), let
\(\mathcal T_R\) be the proper toric model, and put
\(Z=V(g_1,\ldots,g_5)\subseteq\mathcal T_R\).  The special fiber is finite
and has no toric-boundary points.  The non-quasi-finite locus of the proper
morphism \(Z\to\operatorname{Spec}R\) is closed, and its image is closed.  It
contains neither the closed point nor, by specialization in the spectrum of
a local DVR, the generic point.  Hence the morphism is quasi-finite and
proper, therefore finite.  Write \(A=\Gamma(Z,\mathcal O_Z)\).  Invertibility
of multiplication by \(\bar\rho\) on \(A/\mathfrak mA\) gives
\((A/\rho A)\otimes_R k=0\); Nakayama's lemma gives \(A/\rho A=0\).
Thus \(\rho\) is a unit on \(Z\), and the six polynomials have no common
zero over the algebraic closure of the characteristic-zero fraction field.
No finite-flat or finite-\'{e}tale lifting assertion is needed.  Repeating
the modular determinant calculation over the five split embeddings gives
determinant residues \(682,116,337,242,740\), whose product is
\(51\pmod{2053}\).
\end{proof}

This theorem is unconditional for the displayed six polynomials.  Its use
as an obstruction to the two normalized terminal \((8,28)\) support
alternatives is connected to those raw supports by the independent exact
reconstruction above.  The remaining global dependency is the published
Newton-polygon reduction asserting that every below-\(125\) Keller pair is
covered by those alternatives.

\subsection{A two-chart layer-seven certificate}
\label{subsec:two-chart-layer-seven}

The large layer-eight terminal certificate is not needed for the stored
degree-\(21\) full-support specialization.  A second exact calculation
identifies the missing layer-four operation, passes to its adjacent Newton
chart, and obtains a contradiction using only layers five through seven.

\begin{proposition}[The layer-four direction is a chart transition]
\label{prop:k4-chart-transition}
The one-dimensional residual kernel at normal layer four is not induced by
a nontrivial fixed-chart polynomial or Laurent source automorphism.
It is the infinitesimal form of the complete-chain operation
\[
Y\longmapsto Y+\lambda X^{-4},
\]
which changes the completed Newton chart.

In adjacent blowdown coordinates
\[
u=(xy)^{-1},\qquad v=y,\qquad w=v-v_*,
\]
write
\[
\widehat P=Lu+P_2+P_3+\cdots,\qquad
\widehat Q=Muw+Nu^2+Q_3+Q_4+\cdots.
\]
The Jacobian equation forces
\[
L=0,\qquad F_5=0,\qquad
2P_2\partial_wQ_3-3Q_3\partial_wP_2=0,
\]
and hence
\[
P_2=CR^2,\qquad Q_3=GR^3
\]
for a common linear form \(R\).
\end{proposition}

\begin{proof}
The fixed-chart kernel is identified with weighted-divergence-free vector
fields by the exact identity
\[
\mathscr D_r\Theta_r(f,g)=(f\Psi)'+(r-5)g\Psi,
\qquad \Psi=z^2.
\]
Exact support-window calculation gives residual dimensions
\((1,2,1,1)\) in layers one through four.  A nonlinear fixed-chart shear
calculation forces its leading parameter to vanish.  Conjugating the
\(k=4\) complete-chain operation into the adjacent chart gives the stated
translation, and the first homogeneous parts of the transformed Jacobian
identity give the three displayed equations.  Unique factorization yields
the common approximate root.
\end{proof}

\begin{theorem}[Stored terminal no-gluing theorem]
\label{thm:stored-terminal-layer-seven}
After the canonical \(k=4\) rechart and the forced adjacent-chart
condition of \cref{prop:k4-chart-transition}, the complete
layer-five-through-seven support and chart-matching equations of the stored
degree-\(21\) terminal specialization have no common zero over the
algebraic closure of
\[
K_0=\mathbb Q[u]/(u^5-u^4+3u^3+3u^2+26).
\]
\end{theorem}

\begin{proof}[Exact computer-assisted proof]
After the adjacent-chart linear equation is imposed, the layer-five
equation is affine-linear in one remaining coefficient \(d\):
\[
F_5=D(x)d+R(x,a,b).
\]
On \(D=0\), the specialized layer-five-through-seven equations have an
exact nineteen-term Nullstellensatz identity.

On \(D\ne0\), eliminating \(d\) reduces the problem to a five-generator
ideal \(J\subset K_0[x,a,b]\).  At the good prime
\((2053,u-216)\), integral points are excluded by a 201-term affine unit
certificate.  The common normal fan has \(93\) face patterns: \(61\) have a
monomial initial form, \(32\) require exact residue-torus tests, and the ten
surviving cones are covered by two explicit weighted charts.  Exact
identities in the \(x\)-dominant and \(a\)-dominant charts exclude those
cones.  Properness of the weighted compactification lifts emptiness from the
good fiber to characteristic zero.  An independent weighted-projective
implementation gives the same conclusion.
\end{proof}

\Cref{thm:stored-terminal-layer-seven} is exact for the displayed stored
terminal system and has been replayed from the recovered source package.
It does not independently prove that every plane Keller pair below degree
\(125\) reaches this system.  That global interpretation still depends on
the upstream Newton-polygon reduction and its exhaustiveness; neither the
plane Jacobian conjecture nor a new independent proof of the \(125\) bound
is asserted here.

\subsection{Credit for the \texorpdfstring{\(125\)}{125} bound}

MathOverflow user \texttt{ratto3423} publicly announced a lower bound of
\(125\) for the maximum coordinate degree of any characteristic-zero plane
counterexample.  The claim rests on a computer-assisted elimination of the
same two supports \cite{ratto3423degree125}.  We credit the public theorem
announcement to \texttt{ratto3423}.  The answer does not disclose enough
method to compare its computation with the certificates above.

Accordingly, our claim is not priority for the degree-\(125\) conclusion.
The potential contribution of this project is the explicit degree-\(21\)
boundary description and an independently auditable terminal certificate
architecture.  The current certificate is conditional only at the upstream
exhaustiveness layer described above, not at its final linear-algebra step.
~~~

[Back to the text-source index](../../index.md)
