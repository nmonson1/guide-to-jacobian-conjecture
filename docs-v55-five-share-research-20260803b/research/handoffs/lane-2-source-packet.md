# Lane 2 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`manuscripts/04-stable-moduli/appendices/additional-moduli.tex`](#source-e991564f4e348a86) — `c3ba641f86d542308063e8bc887c81625df87dd2a51e178d642050aa0e9a8b0b`
- [`manuscripts/04-stable-moduli/appendices/logarithmic-deformations.tex`](#source-64043996c15ede18) — `dff5c1179daf28397332704a27acd680a07e511ee6f307a02a2749aa9dc59b7f`
- [`manuscripts/04-stable-moduli/appendices/reciprocal-family.tex`](#source-ff8158d98bea3a4b) — `c811df707cd779ad80dbbb82090e372b7a346f4bdfbe66b04ebf6f070fc4eb1b`
- [`manuscripts/04-stable-moduli/appendices/weighted-lift-moduli.tex`](#source-2eef65010676e8cc) — `f354466688f7b2c7350fb0013c5d25e880bc56b2890ae0ccb366a6ceb91803a1`
- [`research-notes/lane2-adjacent-merge-20260803-v1/PRS_SPECIALIZATION_CONTRACT.md`](#source-1cb0e52d6cb87b72) — `d8266441fda8698cff656bbf49ba0ba682a578a3c0ff184ef6f201bb92eaea95`
- [`research-notes/lane2-adjacent-merge-20260803-v1/README.md`](#source-39a1177974f5e030) — `93012792adb504c053ddf80b21b4f157636247cfa227d04a12b20d4586001ab4`
- [`research-notes/lane2-adjacent-merge-20260803-v1/adjacent-merge-theorem.md`](#source-ef4628d8c892bc73) — `e5d65da3f31b0460ed8df6f66d5742f375a281b6ffcc913ddeae98da2aaf54b9`
- [`research-notes/lane2-adjacent-merge-20260803-v1/adjacent_merge_report.json`](#source-07f339823674727e) — `965ddc85f6552c9f7c97488ad32bbabb5760aea0b90c656648394e1c03a3f37b`
- [`research-notes/lane2-adjacent-merge-20260803-v1/verify_adjacent_merge.py`](#source-15e93255c30465a0) — `e4ff94433fc5d8097dfecc93bf0c4d062adc820504c4b3a892549bbfe02797ad`
- [`research-notes/lane2-adjacent-merge-20260803-v1/verify_adjacent_merge_independent.py`](#source-6d19b492e8373155) — `e19a606a571a90292fbe46dec688edada0c4e8a3f4dc2c06501c040ab11c5a12`
- [`research-notes/lane2-projective-normalization-20260803-v1/README.md`](#source-bde5074568c74356) — `4b85dae645b970d2a3ef1c6596ec31f48700b7e7fbbb868b36f1d2471ca6c7e4`
- [`research-notes/lane2-projective-normalization-20260803-v1/bihomogeneous-normalization.md`](#source-cf3c9ea55a4230d8) — `abff0cc31d5b9453cfafc2fabb065a0bf1704b3e260624fd6da512c0b04256ca`
- [`research-notes/lane2-projective-normalization-20260803-v1/verify_bihomogeneous_normalization.py`](#source-ee0ae7a75ef14c24) — `66645f191a16909ad0a51d246afb161786f6315de07fd124a74bf3d958ca77ae`
- [`research-notes/lane2-projective-normalization-20260803-v1/verify_conductor_module.py`](#source-05a87f7e3f84a817) — `979f776d023d9682f350c1fdf37502224f1af940056f2ccee25cde18b57ff979`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_exact_ordered_outer_resolution.md`](#source-26cddbd8db58d696) — `41760240268625d0571e61df35444be3fa8ade6d5da65524920729859c4b7569`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_exact_ordered_outer_resolution_checks.py`](#source-e5195063ad85c860) — `06abbed9b5303bdf4c778ae0546189eebdf54b6e9a19c4601cc619ffdb5c5db4`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_m5_resolution_addendum.md`](#source-5825840330291c07) — `acf78c87030623db41c4c9dc7f676f738c1b92ae3083ca0f6e8fd42416566fcf`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_universal_outer_graph_resolution.md`](#source-6795c38c845ebf0d) — `a660367ffee41fb204d80d12a937be55cb1cdc82020a7276c02ab73afaf622a1`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_hankel_rank_profile.md`](#source-7bf7ef7e0d9d74e6) — `3907694e1edbd019aeb8f86567df3fbaecf04a1fe20448c1fda514b49730ad20`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_hankel_rank_profile_checks.py`](#source-49668fb256743c46) — `b10ea931dac362a2afc8ec6651a7e0ec1e536da6240a87e6e2e4d0d668372011`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_psc_hankel_schur.md`](#source-2af31fd24c3a8d0f) — `dedfa121fed4c0b1ec10b663c2b1cc53a5b6b967cd458867e168e34fc952ce3d`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_psc_hankel_schur_checks.py`](#source-95a864d399454f98) — `b3ac19fcd1210541ac9cb07ec08b096e85bb49437b7d6ea25de24c3e07593de1`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_structural_checks.py`](#source-daf219707509ef2f) — `cf674d9e4ea2f6bb4547edb4a0bced69d08342412ec50d0b70bb4bc397e2ba0c`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_structural_lemmas.md`](#source-789ec859829a957c) — `ce2c4c6f2c3cbb55590fa7b9628321905b1ac6a08a6fc1bc7d5c70ca9aa2c3b8`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_m5_composition_grid_checks.py`](#source-209248dda0cb15da) — `e617708736ab3387640d53f4178a7742fd04510f376197970207352805542d68`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_m5_nu5_actual_flag_checks.py`](#source-46df9b7e598d9f8f) — `40fcd64554f8a9a12e7d05b3ca8d4b2dcfb15241904c9c004f969714ad89970b`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_m5_nu5_actual_prs_flag.md`](#source-a390d36f88cafaa0) — `cdfc7d0e7c234e124aca026b93f00ce3f8d69ece4e4c4aa78c44193c46509538`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_saturated_multirees_equations.md`](#source-794624f89288ba28) — `00f9feb430536990b7cb324c99ca37e4059cfa3b473962e8baadc6ac6c019bec`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_checks.py`](#source-25b301a7bd7faa22) — `e72ecf76c6f16b42c0eece8cc072b4647b0204fce474d36c48317974bde3e247`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_theorem.md`](#source-98a7063c40bcaa46) — `b24cb8f0c001cdfd0d9931faf82fbb616b2b2da25c3ddd55b0185a225b216392`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_checks.py`](#source-813098830565c0aa) — `d3c3ef91a5618ce62a07b325155f77636281bb3abea89fb04753af85d3afc571`
- [`research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_theorem.md`](#source-485c3d5f593645a2) — `874f9affa3e59f4fb4c15d3b2ebe326f6e3e45ce9932633e9e8f38806df03193`

<a id="source-e991564f4e348a86"></a>

## `manuscripts/04-stable-moduli/appendices/additional-moduli.tex`

<pre><code class="language-tex">
\section{Additional restricted moduli results}
\label{app:additional-moduli}

The results in this appendix concern narrower equivalence problems than the
stable left--right problem solved in the body.  They are retained because
they identify useful intermediate moduli spaces, but they should not be read
as classifications of all Keller maps of the stated degree.

\subsection{A grading-preserving degree-five modulus}

For the mixed grading
\&#91;
\deg(x,y,z)=(-1,1,2),
\&#93;
the equivariant Keller equation reduces to a finite coefficient system in
the quotient variables \(u=xy\) and \(v=x^2z\).  If
\&#91;
X=xf(u,v),\qquad Y=x^{-1}g(u,v),\qquad Z=x^{-2}h(u,v),
\&#93;
that system is
\&#91;
gJ(f,h)-2hJ(f,g)+fJ(g,h)=1.
\&#93;

\begin{proposition}&#91;Restricted fixed-degree moduli&#93;
\label{prop:degree-five-equivariant-moduli}
Inside the analyzed generic-degree-five equivariant family, the
grading-preserving left--right orbit space contains an affine
one-parameter family.  Its members are separated by the affine-scaling
class of the critical-root configuration of the associated one-variable
polynomial.
\end{proposition}

\begin{proof}&#91;Exact-elimination proof record&#93;
The weight restrictions leave finitely many coefficients.  Solving the
determinant equations gives a family whose remaining data include a
one-variable critical polynomial.  Every grading-preserving source and
target transformation acts on its roots through the restricted affine
scaling group.  A cross-ratio-type invariant of the critical roots varies,
which separates the displayed one-parameter subfamily.  The archived
elimination and transformation calculation is exact; the proposition makes
no assertion about equivalences that do not preserve the grading.
\end{proof}

\subsection{The low-degree cubic frame and its based parameter}
\label{sec:based-parameter}

\begin{proposition}&#91;Based low-degree normal form&#93;
\label{prop:based-kappa-normal-form}
In the reciprocal boundary stratum of ordinary degree at most seven, the
pole-cancellation and Keller equations reduce the cubic frame to a normal
form with a single residual coefficient \(\kappa\) when the boundary frame
and basepoint are fixed.  Residual scaling gives exactly two based classes,
\(\kappa=0\) and \(\kappa\ne0\).  After the frame is forgotten, a
determinant-one source--target translation moves \(\kappa\), so it is not an
invariant of ordinary left--right equivalence.
\end{proposition}

\begin{proof}
Solving the coefficient equations in the fixed reciprocal frame eliminates
every coefficient except \(\kappa\).  The residual diagonal action is
transitive on its nonzero values.  Substitution of the explicit
determinant-one translation into the cubic-frame formula changes
\(\kappa\) while preserving the unframed map class.
\end{proof}

The pole-cancellation equations in the general cubic marked-root frame admit
an exact normal form.  In ordinary degree at most seven, every member of
that frame is polynomially source--target equivalent to the base map.  Thus
the frame itself produces no additional unbased degree-seven modulus.

If the boundary frame and basepoint are fixed, a residual coefficient
traditionally denoted \(\kappa\) remains.  The exact restricted
classification has two based classes:
\&#91;
\kappa=0,\qquad \kappa\ne0.
\&#93;
The nonzero values are related by the residual scaling.  On forgetting the
frame, the literal coefficient can be moved by a determinant-one
source--target translation; it is therefore not an invariant of ordinary
left--right equivalence.

Coefficientwise formal trivializations of the nonzero based family exist by
formal \'{e}taleness, but their spatial degrees grow with the deformation
order.  The recovered calculation gives componentwise degrees
\&#91;
(36,34,36),\qquad (71,69,71)
\&#93;
for the first two recursively determined coefficients.  These values are
evidence of growth, not a lower-bound theorem for every possible
trivialization.

\begin{remark}&#91;Why these statements are separate&#93;
\Cref{prop:degree-five-equivariant-moduli} uses a grading as part of the
equivalence problem.  The \(\kappa\)-classification uses a fixed boundary
frame and basepoint.  Neither competes with the intrinsic stable invariant
\(q\) proved in the body, nor with the reciprocal-family boundary invariant
of \cref{app:reciprocal-family}.
\end{remark}
</code></pre>

<a id="source-64043996c15ede18"></a>

## `manuscripts/04-stable-moduli/appendices/logarithmic-deformations.tex`

<pre><code class="language-tex">
\section{The boundary-framed logarithmic deformation complex}
\label{app:logarithmic-deformations}

At the degenerate reciprocal member \(g=1\), consider the finite flat cubic
completion
\&#91;
X_0=
V(2pu^3-qu^2v+2uv^2-rv^3)
\subset\A^3_{p,q,r}\times\PP^1_{&#91;u:v&#93;}.
\&#93;
On \(u\ne0\), put \(t=v/u\) and
\&#91;
J=\frac{3rt^2-4t+q}{2}.
\&#93;
Then \((t,r,J)\) are coordinates on \(X_0\), with
\&#91;
q=2J+4t-3rt^2,\qquad
p=tJ+t^2-rt^3.
\&#93;
The repeated-root divisor is \(D_0=(J=0)\), and the triple-root curve is
\&#91;
C_0=(J=0,\ 2-3rt=0).
\&#93;

\begin{proposition}&#91;Exact logarithmic complex&#93;
\label{prop:logarithmic-complex}
For deformations of
\&#91;
\pi_0:(X_0,D_0)\longrightarrow\A^3
\&#93;
with target fixed and \(D_0\) marked, the nontrivial part of the logarithmic
tangent differential is
\&#91;
N=
\begin{pmatrix}
J&amp;0\\
2-3rt&amp;J
\end{pmatrix}.
\&#93;
It is injective, and
\&#91;
H^1(\mathbb T_{\pi_0}^{\log})=\operatorname{coker}N,\qquad
H^i(\mathbb T_{\pi_0}^{\log})=0\quad(i\ne1).
\&#93;
Moreover,
\&#91;
\operatorname{Fitt}_0(\operatorname{coker}N)=(J^2),\qquad
\operatorname{Fitt}_1(\operatorname{coker}N)=(J,2-3rt).
\&#93;
\end{proposition}

\begin{proof}
A basis for \(T_{X_0}(-\log D_0)\) is
\&#91;
\partial_t,\qquad\partial_r,\qquad J\partial_J.
\&#93;
The \(\partial_r\)-to-\(\partial_r\) summand splits.  In the remaining
target coordinates
\&#91;
U=\delta p-\frac t2\delta q,\qquad V=\frac12\delta q,
\&#93;
direct differentiation gives \(N\).  Since \(\det N=J^2\) in the domain
\(\C&#91;t,r,J&#93;\), \(N\) is injective.  Affineness gives the stated
hypercohomology, and the Fitting ideals are the minors of the displayed
matrix.
\end{proof}

For
\&#91;
g_\epsilon(p)=1+\epsilon p^2\eta(p),\qquad\epsilon^2=0,
\&#93;
the induced class is
\&#91;
&#91;-p^3\eta(p)&#93;e_U\in\operatorname{coker}N.
\&#93;
It is nonzero for \(\eta\ne0\): restriction to \(J=0\) sends
\&#91;
p\longmapsto t^2(1-rt)
\&#93;
and embeds \(\C&#91;p&#93;\) into \(\C&#91;t,r&#93;\).  These directions integrate to the
exact reciprocal family.

\begin{remark}&#91;Why the framing matters&#93;
If arbitrary target vector fields are restored, the target field
\(-p^3\eta(p)\partial_p\) kills the displayed infinitesimal class.  The
calculation therefore describes the fixed-target, boundary-marked
deformation problem, or any finite-type moduli problem imposing equivalent
framing.  It does not claim that the same tangent vector survives
unrestricted affine target gauge.
\end{remark}
</code></pre>

<a id="source-ff8158d98bea3a4b"></a>

## `manuscripts/04-stable-moduli/appendices/reciprocal-family.tex`

<pre><code class="language-tex">
\section{The reciprocal cubic family}
\label{app:reciprocal-family}

The family in the body gives a clean affine line of stable orbits.  A second
construction gives much larger fixed-generic-degree families and boundary
curves of arbitrary genus.  We record it separately because the algebraic
construction is exact, while the last stable-separation step still requires a
specialist audit of the birational argument.

Put
\&#91;
A=1+xy,\qquad
B=A^2z+y^2(4+3xy),\qquad
P=AB,
\&#93;
\&#91;
Q=y+3xB,\qquad
R=2x-3x^2y-x^3z.
\&#93;
Thus \((P,Q,R)\) is the unnormalized degree-seven map.  On \(A\ne0\), set
\&#91;
s=\frac{x}{A}.
\&#93;
Then \(Ps=xB\) and \(1-ys=A^{-1}\).

\subsection{Pole cancellation}

Let \(g(p)\in\C&#91;p&#93;\).  In the rational coordinates \((P,s,y)\), consider
\&#91;
q=y+3Pg(P)s,\qquad
r=2Pg(P)s^3-qs^2+2s.
\&#93;

\begin{proposition}&#91;Reciprocal pole-cancellation criterion&#93;
\label{prop:reciprocal-pole}
The prescription \((P,q,r)\) extends to a polynomial self-map of
\(\A^3\) if and only if
\&#91;
g(0)=1,\qquad g'(0)=0.
\&#93;
Equivalently, \(g(p)=1+p^2\eta(p)\) for a unique
\(\eta\in\C&#91;p&#93;\).
\end{proposition}

\begin{proof}
The second coordinate is \(q=y+3xB\,g(P)\).  Comparing the third coordinate
with \(R\) gives
\&#91;
r-R=-\frac{x^3B}{A^2}\bigl(g(P)-1\bigr).
\&#93;
Write \(g(P)-1=c_0+c_1P+P^2\eta(P)\).  Since
\(\gcd(A,x^3B)=1\) in \(\C&#91;x,y,z&#93;\), polynomiality forces
\(A^2\mid c_0+c_1AB\).  Reducing first modulo \(A\), and then after one
division by \(A\), gives \(c_0=c_1=0\).  The converse follows from
\&#91;
r-R=-x^3B^3\eta(P).
\&#93;
\end{proof}

For \(\eta\in\C&#91;p&#93;\), define
\begin{equation}
\label{eq:reciprocal-map}
\begin{aligned}
Q_\eta&amp;=Q+3xA^2B^3\eta(P),\\
R_\eta&amp;=R-x^3B^3\eta(P),\\
\mathcal G_\eta&amp;=(P,Q_\eta,R_\eta),
\end{aligned}
\end{equation}
and write \(g(p)=1+p^2\eta(p)\).

\begin{theorem}&#91;Algebraic properties of the reciprocal family&#93;
\label{thm:reciprocal-basic}
For every \(\eta\),
\&#91;
\det J\mathcal G_\eta=-2.
\&#93;
The map has generic degree three and generic Galois group \(S_3\).
\end{theorem}

\begin{proof}
In rational coordinates,
\&#91;
Q_\eta=y+3Pg(P)s,\qquad
R_\eta=2Pg(P)s^3-Q_\eta s^2+2s.
\&#93;
Direct differentiation gives
\&#91;
\det\frac{\partial(P,Q_\eta,R_\eta)}{\partial(P,s,y)}
=-\frac2A,\qquad
\det\frac{\partial(P,s,y)}{\partial(x,y,z)}=A.
\&#93;
Their product is \(-2\).

For target coordinates \((p,q,r)\), the primitive element satisfies
\begin{equation}
\label{eq:reciprocal-cubic}
\Omega_{p,q,r}(S)
=2pg(p)S^3-qS^2+2S-r=0.
\end{equation}
Moreover \(y=q-3pg(p)s\), so
\(\C(x,y,z)=\C(p,q,s)\).  Over \(\C(p,q)\), the right side defining \(r\)
is a degree-three rational function of \(s\), proving generic degree three
and irreducibility.  The discriminant is \(4\Delta_\eta\), where
\&#91;
\Delta_\eta
=q^2-16pg-q^3r+18pgqr-27p^2g^2r^2.
\&#93;
As a quadratic in \(r\), its discriminant is
\((q^2-12pg)^3\), which is not a square in the generic function field.
The irreducible cubic therefore has Galois group \(S_3\).
\end{proof}

\subsection{The image and finite completion}

Define
\&#91;
\Gamma_\eta:
\quad q^2=12pg(p),\quad 3qr=4,
\&#93;
and
\&#91;
\Lambda_\eta:
\quad g(p)=0,\quad qr=1.
\&#93;

\begin{theorem}&#91;Exact image&#93;
\label{thm:reciprocal-image}
Set-theoretically over \(\C\),
\&#91;
\A^3\setminus\mathcal G_\eta(\A^3)
=\Gamma_\eta\sqcup\Lambda_\eta.
\&#93;
\end{theorem}

\begin{proof}
A simple root \(s\) of \eqref{eq:reciprocal-cubic} reconstructs a unique
source point.  Indeed, with
\&#91;
D=\Omega'(s),\quad a=\frac2D,\quad
x=as,\quad y=q-3pg(p)s,\quad b=\frac pa,
\&#93;
put
\&#91;
z=\frac{b-y^2(4+3xy)}{a^2}.
\&#93;
Then \(1+xy=a\), \(B=b\), and substitution gives the target
\((p,q,r)\).

For \(p\ne0\), a target is therefore omitted precisely when
\(\Omega\) has no simple root.  If \(g(p)\ne0\), this happens exactly when
the cubic is a cube of a linear polynomial, which gives \(\Gamma_\eta\).
If \(g(p)=0\), the equation is quadratic and has no simple root exactly
when \(qr=1\), which gives \(\Lambda_\eta\).

The plane \(p=0\) is in the image.  If \(p=q=0\), take
\((x,y,z)=(r/2,0,0)\).  If \(p=0\) and \(q\ne0\), take
\&#91;
x=\frac2q,\qquad y=-\frac q2,\qquad
z=\frac{5q^2}{4}-\frac{\eta(0)q^6}{64}-\frac{rq^3}{8}.
\&#93;
Neither displayed omitted locus meets this plane.
\end{proof}

Let
\&#91;
\mathcal X_\eta=
V\!\left(
2pg(p)u^3-qu^2v+2uv^2-rv^3
\right)
\subset\A^3_{p,q,r}\times\PP^1_{&#91;u:v&#93;}.
\&#93;
The projection \(\mathcal X_\eta\to\A^3\) is finite flat of rank three.
The source embeds by
\&#91;
(x,y,z)\longmapsto
\bigl(\mathcal G_\eta(x,y,z),&#91;x:A&#93;\bigr).
\&#93;
If \(\mathcal R_\eta\) is the repeated-root divisor and
\(\mathcal I_\eta=V(v,g(p))\), the reconstruction above in the two
projective charts gives
\&#91;
\A^3\simeq
\mathcal X_\eta\setminus
(\mathcal R_\eta\cup\mathcal I_\eta)
\&#93;
and hence
\begin{equation}
\label{eq:reciprocal-nonproper}
S_{\mathcal G_\eta}^{\mathrm{red}}
=V\bigl(g(p)\Delta_\eta(p,q,r)\bigr).
\end{equation}
This finite completion is also the natural frame for the moduli assertions
below.

\subsection{Curves and stable separation}

The component \(\Gamma_\eta\) is a dense open of the normalization of
\&#91;
C_\eta:\qquad u^2=12p\bigl(1+p^2\eta(p)\bigr).
\&#93;
If \(\eta\ne0\) has degree \(d\) and the polynomial on the right is
squarefree, then
\&#91;
g(C_\eta)=\left\lfloor\frac{d+2}{2}\right\rfloor.
\&#93;
Each distinct root of \(g\) contributes a rational
\(\Gm\)-component to \(\Lambda_\eta\).

\begin{theorem}&#91;Stable curve invariant&#93;
\label{thm:reciprocal-stable}
Assume that \(C_\eta\) and \(C_\theta\) are smooth projective curves of
positive genus.  If \(\mathcal G_\eta\) and \(\mathcal G_\theta\) are
polynomially left--right equivalent after stabilization, then
\&#91;
C_\eta\simeq C_\theta.
\&#93;
Consequently the reciprocal family contains positive-dimensional families
of fixed generic degree.  Their boundary curves realize every positive genus.
\end{theorem}

\begin{proof}
Stable left--right equivalence identifies the reduced nonproperness loci
after taking a product with affine space.  In
\eqref{eq:reciprocal-nonproper}, the components arising from
\(\Lambda_\eta\) are rational, whereas \(\Gamma_\eta\) has projective
normalization \(C_\eta\).  Hence an isomorphism of stabilized
nonproperness loci must carry the unique nonrational component to the unique
nonrational component.  On function fields it gives
\&#91;
\C(C_\eta)(t_1,\ldots,t_m)
\simeq
\C(C_\theta)(s_1,\ldots,s_m).
\&#93;
Thus \(C_\eta\) and \(C_\theta\) are stably birational.  Smooth projective
curves of positive genus are the maximal rationally connected quotients of
their products with projective space, so stable birationality forces
\(C_\eta\) and \(C_\theta\) to be birational.  Smooth projective birational
curves are isomorphic.

For each genus, take
\&#91;
g_{\tau,m}(p)
=(1-p^2)(1-p^2/\tau^2)
\prod_{j=3}^{m}(1-p^2/\alpha_j^2).
\&#93;
Varying the symmetric branch set gives nonisomorphic curves for general
\(\tau\).  Moreover,
\(\eta=(g-1)/p^2\) is polynomial and the branch cross-ratios vary.
\end{proof}

\subsection{The collision-preserving line}
\label{sec:reciprocal-collision-line}

For
\&#91;
\eta_\lambda(p)=\frac{\lambda}{3}(4p+1),
\qquad
g_\lambda(p)=1+\frac{\lambda}{3}p^2(4p+1),
\&#93;
the projective normalization is the short Weierstrass curve with
\&#91;
j(\lambda)=\frac{1728\lambda}{\lambda+324}.
\&#93;
For \(\lambda\ne0,-324\), the omitted set has one elliptic component and
three rational components.  At \(\lambda=0\), it has one component
\(\Gm\).  At \(\lambda=-324\),
\&#91;
g_{-324}(p)=-(6p+1)^2(12p-1),
\&#93;
and the reduced omitted locus has three components: two copies of
\(\Gm\) and a rational curve whose normalization is
\(\PP^1\) minus six points.  By
\cref{thm:reciprocal-stable}, these data give a complete pairwise
separation of the \(\lambda\)-line.

\subsection{Degree and framed moduli}
\label{sec:reciprocal-degree-moduli}

If
\&#91;
g(p)=1+c_2p^2+\cdots+c_mp^m,\qquad c_m\ne0,
\&#93;
then
\&#91;
\deg\mathcal G_\eta=7m+6.
\&#93;
Thus degree \(20\) is the first nonbase member of this reciprocal normal
form, while degree \(27\) is the first positive-dimensional quotient.  These
are normal-form statements, not absolute lower bounds under arbitrary
polynomial equivalence.  The separate coarse argument presently gives only
\&#91;
4\le d_{\mathrm{positive\ genus}}\le20.
\&#93;

Fix a degree bound \(m\) for \(\eta\) and retain the finite completion,
infinity section, and target coordinates as part of the framing.  Let
\&#91;
V_m=\set{\eta\in\C&#91;p&#93;:\deg\eta\le m}.
\&#93;
The residual source scaling acts on the coefficient of \(p^i\) with weight
\(-(2i+4)\).  Exact pole cancellation and a calculation of
frame-preserving source--target transformations give the framed moduli
groupoid
\&#91;
&#91;V_m/\Gm&#93;.
\&#93;
Its tangent complex at \(\eta\) is the standard two-term complex
\&#91;
\operatorname{Lie}(\Gm)\longrightarrow T_\eta V_m.
\&#93;
With the boundary marked, differentiation of
\eqref{eq:reciprocal-cubic} gives the corresponding logarithmic
deformation complex.  This is a statement about the framed reciprocal
family; it is not a presentation of the full unframed Keller moduli stack.
</code></pre>

<a id="source-2eef65010676e8cc"></a>

## `manuscripts/04-stable-moduli/appendices/weighted-lift-moduli.tex`

<pre><code class="language-tex">
\section{Fixed-degree moduli in the weighted-lift construction}
\label{app:weighted-lift-moduli}

The cubic-frame families studied in the body have generic degree three.
There is also a fixed-degree moduli theorem for the public weighted-lift
construction.  A seed polynomial \(p\) of degree \(d\) satisfies
\&#91;
p(0)=0,\qquad p(1)=-1,\qquad
\int_0^1p(w)\,dw=0
\&#93;
and produces a counterexample of generic degree \(n=d+1\).  Put
\&#91;
q(w)=wp(w)-\int_0^wp(s)\,ds,
\qquad q'(w)=wp'(w).
\&#93;
For \(d=4\), the two-dimensional normalized seed family is already explicit:
\&#91;
\begin{split}
p_{C,D}(w)={}&amp;
\left(2+\frac C2+\frac{4D}{5}\right)w
\left(-3-\frac{3C}{2}-\frac{9D}{5}\right)w^2\\
&amp;+Cw^3+Dw^4.
\end{split}
\&#93;
Thus the first nontrivial fixed-degree case is not merely a dimension count.
For the cubic \(p'_{C,D}\), two invariants under simultaneous rescaling of
the polynomial and its variable are
\&#91;
 I(C,D)=-\frac{9C(5C+6D+10)}{2D(5C+8D+20)},\qquad
 J(C,D)=\frac{135C^3}{8D^2(5C+8D+20)}.
\&#93;
Their Jacobian is
\&#91;
 \det\frac{\partial(I,J)}{\partial(C,D)}
 =-\frac{30375C^3}{2D^4(5C+8D+20)^3},
\&#93;
so they separate a two-parameter family on a dense open set.

\begin{theorem}&#91;Intrinsic critical-root arrangement&#93;
\label{thm:weighted-critical-roots}
Assume
\&#91;
p'(0)\ne0,\qquad p'\text{ is squarefree with nonzero roots},\qquad
\gcd(p,q)=w.
\&#93;
The unique nonnormal hypersurface component \(S_p\) of the nonproperness
set has normalization
\&#91;
\nu_p:\A^2_{u,\zeta}\longrightarrow S_p,
\qquad
\nu_p(u,\zeta)=
\left(
\frac{q(\zeta u)}{\zeta^2},
\frac{p(\zeta u)}{\zeta},
\zeta
\right).
\&#93;
Its ramification divisor is
\&#91;
R_p=V(p'(\zeta u))
=\bigcup_{r\in\operatorname{Crit}(p)}V(\zeta u-r).
\&#93;
The unordered critical-root configuration of \(p\), modulo common scaling,
is invariant under arbitrary polynomial left--right equivalence of the
weighted-lift maps.
\end{theorem}

\begin{proof}
The displayed quotients are polynomials because \(p(0)=0\) and \(q\)
vanishes to order at least two.  Write \(w=\zeta u\).  If a valuation ring
contains
\&#91;
\zeta,\qquad p(w)/\zeta,\qquad q(w)/\zeta^2,
\&#93;
then it contains \(u\): negative valuation of \(w\) is incompatible with
integrality of \(p(w)/\zeta\); positive valuation and \(p'(0)\ne0\) give
\(v(w)\ge v(\zeta)\); and \(v(w)=0&lt;v(\zeta)\) would give a nonzero common
root of \(p\) and \(q\).  Thus \(\nu_p\) is finite.  It is birational on the
open reconstruction locus, and \(\A^2\) is normal, so it is the
normalization.

Differentiation gives
\&#91;
\partial_u\left(\frac{p(\zeta u)}{\zeta}\right)
=p'(\zeta u),\qquad
\partial_u\left(\frac{q(\zeta u)}{\zeta^2}\right)
=u\,p'(\zeta u),
\&#93;
which proves the ramification formula.

All other hypersurface components of the nonproperness set lie in the plane
\(\zeta=0\) and are normal.  Hence \(S_p\) is intrinsically the unique
nonnormal component, and an arbitrary left--right equivalence lifts to an
automorphism of its normalization carrying \(R_p\) to \(R_{\widetilde p}\).
Componentwise,
\&#91;
\phi^*(u'\zeta'-\widetilde r_i)
=\lambda_i(u\zeta-r_{\sigma(i)}).
\&#93;
Subtracting two identities makes all \(\lambda_i\) equal, so
\&#91;
\phi^*(u'\zeta')=\lambda u\zeta+\mu.
\&#93;
The left side factors into two coordinate polynomials.  If \(\mu\ne0\),
\(\lambda u\zeta+\mu\) is irreducible, a contradiction.  Thus
\(\mu=0\), and
\&#91;
\{\widetilde r_i\}=\lambda\{r_i\}.
\&#93;
\end{proof}

\begin{corollary}&#91;Moduli at every fixed generic degree&#93;
\label{cor:weighted-fixed-degree-moduli}
For every \(n\ge4\), the weighted-lift construction contains an
\((n-3)\)-dimensional family of pairwise inequivalent counterexamples of
generic degree \(n\), even under arbitrary polynomial left--right
equivalence.
\end{corollary}

\begin{proof}
The degree-\(d=n-1\) seed space cut out by the three displayed linear
conditions has dimension \(d-2=n-3\).  The map to critical-root
configurations modulo scaling is generically finite.  Indeed, after fixing
a representative \(\{r_i\}\), every derivative has the form
\&#91;
p'(w)=K\prod_{i=1}^{d-1}(w-\lambda r_i).
\&#93;
The integral condition becomes
\&#91;
\int_0^1(1-s)\prod_i(s-\lambda r_i)\,ds=0.
\&#93;
This is a nonzero polynomial equation in \(\lambda\); at \(\lambda=0\), its
value is \(1/(d(d+1))\).  There are therefore only finitely many
\(\lambda\), and \(p(1)=-1\) then determines \(K\).  Apply
\cref{thm:weighted-critical-roots}.
\end{proof}

\begin{remark}
The dimension statement means that the seed variety maps generically
finitely to algebraically separating invariants.  It does not assert the
existence of a separated coarse moduli scheme.
\end{remark}
</code></pre>

<a id="source-1cb0e52d6cb87b72"></a>

## `research-notes/lane2-adjacent-merge-20260803-v1/PRS_SPECIALIZATION_CONTRACT.md`

<pre><code class="language-markdown">
# PRS specialization contract for P4-L2A

The abstract adjacent-merge problem needs more than four monomial exponents.
It also needs the exact transform convention. Two operations that are both
called a “weak transform” in the literature give different answers for

\&#91;
I=(X^a,Y^b),\qquad J=(Y^c,Z^d).
\&#93;

## Convention gate

A packet must select one of:

```text
cartier_factor_weak
exceptional_saturation
```

### `cartier_factor_weak`

Remove only the largest common exceptional Cartier factor from the pulled-back
second pair. In this adjacent model one generator always has exceptional order
zero. Therefore no exceptional factor is removed, both orders retain the
simultaneous ray, and the normalized models are identical for every positive
`a,b,c,d`.

### `exceptional_saturation`

Replace the pulled-back second ideal `K` by `K:E^\infty` on the canonical
toric cover. This removes an exceptional component and produces the two
circuit triangulations. Their flip/flop type is determined by `delta` below.

The selected convention must be supported by a proof artifact for the actual
PRS graph. A name alone is insufficient.

## Fail-closed rule

A packet is admissible only if it validates against
`prs-adjacent-merge-contract.schema.json` and passes
`validate_prs_contract.py`. Missing data must produce

```text
INSUFFICIENT PRS PIVOT DATA
```

rather than a guessed convention or exponent quadruple.

## Required mathematical content

1. **Transform convention.** The selected operation and a hash-pinned proof
   showing that it is the actual PRS construction.
2. **Toroidal chart.** Primitive parameters `(X,Y,Z)`, their divisor lattice,
   all localizations, and identification of the shared divisor `Y=0`.
3. **Four pivot valuations.** After removing the declared projective common
   monomial factor from each pair, the valuation rows must be

   ```text
   I: (a,0,0), (0,b,0)
   J: (0,c,0), (0,0,d).
   ```

4. **Integral-closure certificate.** A certificate that the actual ideals have
   the same integral closures as `(X^a,Y^b)` and `(Y^c,Z^d)`. This is the
   no-extra-Newton-ray condition.
5. **Transform ledger.** In both orders: the canonical-cover exceptional
   coordinate, exceptional order of every generator, common Cartier factor,
   Cartier weak generators, full saturation, selected operation, the exact
   selected generator list, and retained closed complement. The selected list
   must equal the Cartier-weak list or the saturated list according to the
   top-level convention.
6. **Lattice and characters.** Primitive rays, stacky multiplicities, circuit
   Smith data, simultaneous-ray multiplicity, projective-coordinate
   characters, and relative-Jacobian character.
7. **Transfer data.** Exact transfer matrices in both orders, including
   monomial factors and immutable artifact hashes.

## Computation

From the certified exponents compute

```text
g1 = gcd(a,b),       g2 = gcd(c,d),
a0 = a/g1, b0=b/g1, c0=c/g2, d0=d/g2,
h  = gcd(a0,d0),
delta = a0*(c0-1) - d0*(b0-1).
```

The output is:

```text
cartier_factor_weak:
    commuting_simultaneous, for every delta

exceptional_saturation:
    delta = 0 : flop
    delta &gt; 0 : J_then_I -&gt; I_then_J flip
    delta &lt; 0 : I_then_J -&gt; J_then_I flip
```

The coarse answer does not settle stacky triple-overlap compatibility. The
character and transfer blocks remain load-bearing inputs for P4-L2B.

## Calibration fixtures

`quintic_unit_calibration.json` selects `exceptional_saturation` and records

```text
a=b=c=d=1,
u=(1,1,0), v=(0,1,1), w=(1,1,1),
u+e_z=e_x+v,
classification=flop.
```

`quintic_unit_cartier_weak_calibration.json` uses the same exponents but
selects `cartier_factor_weak`; its classification is
`commuting_simultaneous`.

Both are marked `calibration_only`. Neither substitutes for an arbitrary-rank
PRS pivot packet.
</code></pre>

<a id="source-39a1177974f5e030"></a>

## `research-notes/lane2-adjacent-merge-20260803-v1/README.md`

<pre><code class="language-markdown">
# Adjacent noncoprime merge packet

This packet resolves the abstract adjacent monomial-merge problem after
distinguishing two operations often called weak transform.

- Removing only a common Cartier factor gives the simultaneous fan in either
  order.
- Saturating by the exceptional divisor gives the two circuit triangulations.
  Their relation is governed by
  \(\Delta=a_0(c_0-1)-d_0(b_0-1)\): equality gives a flop and the sign gives
  the flip direction.

`adjacent-merge-theorem.md` contains the proof. Two independent exact programs
check the fan, saturation, circuit, index, discrepancy, and flop formulas.
`PRS_SPECIALIZATION_CONTRACT.md` lists the additional pivot and convention data
required before this abstract result can be applied to an actual all-rank PRS
packet.

No arbitrary-rank PRS specialization is claimed here.
</code></pre>

<a id="source-ef4628d8c892bc73"></a>

## `research-notes/lane2-adjacent-merge-20260803-v1/adjacent-merge-theorem.md`

<pre><code class="language-markdown">
# P4-L2A: convention-complete noncoprime adjacent-merge theorem

&gt; **Scope.** Two independent exact replay programs are supplied. The abstract
&gt; toric problem is resolved after separating two transformations that are often
&gt; both called a “weak transform.” Under common-Cartier-factor removal the two
&gt; orders commute; under full exceptional saturation they differ by the circuit
&gt; flip/flop classified below. An actual PRS specialization must declare which
&gt; operation it uses and supply its pivot valuations.
&gt;
&gt; **Ground field.** The coarse toric statements work over any field.
&gt; Characteristic zero is retained because that is the ambient hypothesis of the
&gt; PRS program.

## 1. Problem and result

Let

\&#91;
A=k&#91;x,y,z&#93;,\qquad
I=(x^a,y^b),\qquad
J=(y^c,z^d),
\qquad a,b,c,d&gt;0.
\&#93;

After the first normalized monomial blowup there are two distinct operations
on the pulled-back second center:

1. **Cartier-factor weak transform:** remove only the largest common power of
   the first exceptional divisor from all generators;
2. **exceptional-saturated transform:** replace the pulled-back ideal `K` by
   `K:E^\infty` on the canonical toric cover, i.e. take the ideal of the
   strict transform of its zero scheme.

The distinction is load-bearing here. For these adjacent ideals the first
operation removes no exceptional power, whereas the second deletes a
codimension-two exceptional component.

Put

\&#91;
 g_1=\gcd(a,b),\qquad g_2=\gcd(c,d),
\&#93;

\&#91;
 a_0=\frac a{g_1},\quad b_0=\frac b{g_1},\qquad
 c_0=\frac c{g_2},\quad d_0=\frac d{g_2}.
\&#93;

Thus

\&#91;
\gcd(a_0,b_0)=\gcd(c_0,d_0)=1.
\&#93;

The primitive normalized-blowup rays are

\&#91;
 u=(b_0,a_0,0),\qquad
 v=(0,d_0,c_0).
\&#93;

### Theorem 1.1 — convention dichotomy

**(W) Cartier-factor weak transform.** Both orders give the same normalized
model, namely the simultaneous-linearity fan `Sigma_sim` of Section 5, for
every positive quadruple `(a,b,c,d)`.

**(S) Exceptional saturation.** The two orders are distinct small toric
modifications of one four-ray contraction. Their comparison is governed by

\&#91;
\boxed{
\Delta=a_0(c_0-1)-d_0(b_0-1).
}
\&#93;

For this convention:

- the two ordered fans are never equal over the identity lattice map;
- they are isomorphic in codimension one and differ by one circuit diagonal;
- `Delta=0` exactly when the wall crossing is a toric flop;
- `Delta&gt;0` gives a `J then I` to `I then J` flip;
- `Delta&lt;0` gives the reverse flip;
- the coarse criterion depends only on the reduced exponent pairs, while the
  discarded gcds and the cross-gcd still matter for stacky and character data.

Consequently there is no convention-independent nontrivial order criterion.
The rest of the note proves both branches and isolates the exact PRS input
still missing.

## 2. Exact transform conventions

Let `sigma` be the positive octant in

\&#91;
N_\mathbb R=\mathbb R e_x\oplus\mathbb R e_y\oplus\mathbb R e_z,
\qquad N=\mathbb Z^3.
\&#93;

The normalized blowup of a monomial ideal is the toric subdivision on which
its order function is linear. For

\&#91;
I=(x^a,y^b)
\&#93;

the wall is

\&#91;
a n_x=b n_y,
\&#93;

and its primitive ray is `u`. For `J` the primitive ray is `v`.

After the first normalized blowup, work on a simplicial affine chart and pass
to the canonical finite toric cover whose lattice is generated by the
primitive rays of that cone. On this cover the first exceptional divisor has
a single monomial equation `E=0`.

### Definition 2.1 — Cartier-factor weak transform

For a pulled-back monomial ideal `K`, put

\&#91;
\nu_E(K)=\min\{\nu_E(f): f\text{ is a monomial generator of }K\}
\&#93;

and define

\&#91;
K^{\mathrm{wk}}=E^{-\nu_E(K)}K.
\&#93;

This is the operation used when a projective pair is simplified by deleting a
common Cartier factor. Multiplication by the resulting invertible exceptional
ideal does not change the projective map or its normalized blowup.

### Definition 2.2 — exceptional-saturated transform

Define instead

\&#91;
K^{\mathrm{sat}}=K:E^\infty.
\&#93;

This is the ideal of the strict transform of `V(K)` on the canonical cover.
Normalize its blowup and descend the resulting fan to `N`.

### Lemma 2.3 — the two operations differ in the adjacent model

On the only nontrivial `I`-first chart, the second center becomes

\&#91;
K=(E^{a_0c}Y^c,Z^d).
\&#93;

Since the second generator has exceptional order zero,

\&#91;
K^{\mathrm{wk}}=K.
\&#93;

But

\&#91;
K^{\mathrm{sat}}=(Y^c,Z^d).
\&#93;

The reverse order has the same dichotomy. Thus Cartier-factor removal retains
the simultaneous Rees valuation, while saturation deletes it. Sections 3 and
4 first compute the saturated branch; Section 5 proves that the Cartier-factor
branch is the simultaneous fan.

## 3. First order: `I` then `J`

The normalized blowup of `I` has fan

\&#91;
\Sigma_I^{\max}
=
\{\langle e_x,u,e_z\rangle,
  \langle u,e_y,e_z\rangle\}.
\&#93;

The calculation of the exceptional-saturated transform is exact on the two canonical covers.

### 3.1 Cone `sigma_{Ix}=&lt;e_x,u,e_z&gt;`

Use the cover lattice with basis

\&#91;
e_x,u,e_z.
\&#93;

Let its affine coordinates be `(X,E,Z)`. The original monomials pull back as

\&#91;
x=X E^{b_0},\qquad y=E^{a_0},\qquad z=Z.
\&#93;

The first ideal becomes principal:

\&#91;
I\mathcal O
=
E^{g_1a_0b_0}(X^a,1).
\&#93;

The second ideal becomes

\&#91;
J\mathcal O=(E^{a_0c},Z^d).
\&#93;

Hence

\&#91;
(E^{a_0c},Z^d):E^\infty=(1).
\&#93;

The strict transform of the second center is absent on this chart.

### 3.2 Cone `sigma_{Iy}=&lt;u,e_y,e_z&gt;`

Use the cover lattice with basis

\&#91;
u,e_y,e_z
\&#93;

and coordinates `(E,Y,Z)`. Then

\&#91;
x=E^{b_0},\qquad y=E^{a_0}Y,\qquad z=Z,
\&#93;

and

\&#91;
I\mathcal O=E^{g_1a_0b_0}(1,Y^b).
\&#93;

The pulled-back second ideal is

\&#91;
J\mathcal O=(E^{a_0c}Y^c,Z^d).
\&#93;

Exceptional saturation gives

\&#91;
\boxed{
(E^{a_0c}Y^c,Z^d):E^\infty=(Y^c,Z^d).
}
\&#93;

The normalized blowup of `(Y^c,Z^d)` inserts the primitive ray

\&#91;
d_0e_y+c_0e_z=v.
\&#93;

### Theorem 3.1 — saturated `I`-first fan

The maximal cones of the cover-saturated ordered model are

\&#91;
\boxed{
\Sigma_+^{\max}
=
\left\{
\langle e_x,u,e_z\rangle,
\langle u,e_y,v\rangle,
\langle u,v,e_z\rangle
\right\}.
}
\&#93;

Here `+` denotes `I` followed by the exceptional-saturated transform of `J`.

---

## 4. Reverse order: `J` then `I`

The normalized blowup of `J` has fan

\&#91;
\Sigma_J^{\max}
=
\{\langle e_x,e_y,v\rangle,
  \langle e_x,v,e_z\rangle\}.
\&#93;

### 4.1 Cone `tau_{Jy}=&lt;e_x,e_y,v&gt;`

On the canonical cover with basis `e_x,e_y,v`, use coordinates `(X,Y,F)`. Then

\&#91;
x=X,\qquad y=YF^{d_0},\qquad z=F^{c_0}.
\&#93;

The first blowup ideal is principal:

\&#91;
J\mathcal O=F^{g_2c_0d_0}(Y^c,1).
\&#93;

The other center pulls back to

\&#91;
I\mathcal O=(X^a,Y^bF^{b d_0}),
\&#93;

and saturation gives

\&#91;
\boxed{
(X^a,Y^bF^{bd_0}):F^\infty=(X^a,Y^b).
}
\&#93;

Its normalized blowup inserts

\&#91;
b_0e_x+a_0e_y=u.
\&#93;

### 4.2 Cone `tau_{Jz}=&lt;e_x,v,e_z&gt;`

On the cover with basis `e_x,v,e_z`, write

\&#91;
x=X,\qquad y=F^{d_0},\qquad z=F^{c_0}Z.
\&#93;

Then

\&#91;
I\mathcal O=(X^a,F^{bd_0}),
\&#93;

so

\&#91;
(X^a,F^{bd_0}):F^\infty=(1).
\&#93;

### Theorem 4.1 — saturated `J`-first fan

The maximal cones are

\&#91;
\boxed{
\Sigma_-^{\max}
=
\left\{
\langle e_x,u,v\rangle,
\langle u,e_y,v\rangle,
\langle e_x,v,e_z\rangle
\right\}.
}
\&#93;

Here `-` denotes `J` followed by the exceptional-saturated transform of `I`.

---

## 5. Cartier-factor weak transforms and the simultaneous fan

The two order functions are

\&#91;
\varphi_I(n)=\min(a_0n_x,b_0n_y),
\qquad
\varphi_J(n)=\min(c_0n_y,d_0n_z).
\&#93;

Their walls meet on the primitive ray

\&#91;
\boxed{
 w=
 \left(
 \frac{b_0d_0}{h},
 \frac{a_0d_0}{h},
 \frac{a_0c_0}{h}
 \right),
 \qquad h=\gcd(a_0,d_0).
}
\&#93;

The four domains of simultaneous linearity are obtained from the four choices of winning monomial. Their extreme rays are:

\&#91;
\begin{array}{c|c|c}
I\text{ winner}&amp;J\text{ winner}&amp;\text{cone}\\
\hline
x^a&amp;y^c&amp;\langle v,w,e_z\rangle\\
x^a&amp;z^d&amp;\langle u,e_y,v,w\rangle\\
y^b&amp;y^c&amp;\langle e_x,w,e_z\rangle\\
y^b&amp;z^d&amp;\langle e_x,u,w\rangle\\
\end{array}
\&#93;

Thus the simultaneous-linearity fan is

\&#91;
\boxed{
\Sigma_{\mathrm{sim}}^{\max}
=
\left\{
\langle e_x,u,w\rangle,
\langle e_x,w,e_z\rangle,
\langle u,e_y,v,w\rangle,
\langle w,v,e_z\rangle
\right\}.
}
\&#93;

The middle cone is generally non-simplicial.

### Theorem 5.1 — Cartier-factor weak transforms commute

Under Definition 2.1, either order produces `Sigma_sim`.

#### Proof

On each canonical chart after blowing up `I`, one pulled-back generator of `J`
has exceptional order zero: it is the transform of `z^d`. Hence
`nu_E(J O)=0`, so the Cartier-factor weak transform is the total transform.
Symmetrically, after blowing up `J`, the transform of `x^a` has exceptional
order zero. Normalizing the second blowup therefore refines the first fan by
the other order function. This is exactly the common refinement on which both
`varphi_I` and `varphi_J` are linear, and the four chambers above are
independent of order. ∎

### Consequence

Under common-Cartier-factor removal, the order-comparison criterion is

\&#91;
\boxed{\text{the two orders agree for every }a,b,c,d&gt;0.}
\&#93;

The nontrivial circuit ambiguity is introduced only by deleting the
exceptional component through full saturation. The ray `w` is retained by the
Cartier-factor/total-transform model and absent from both saturated ordered
models.

---

## 6. Common contraction and circuit

The two exceptional-saturated ordered fans share the rays

\&#91;
e_x,e_y,e_z,u,v
\&#93;

and the common cone

\&#91;
\langle u,e_y,v\rangle.
\&#93;

On the complementary support, define

\&#91;
\mathcal Q=\langle e_x,u,v,e_z\rangle.
\&#93;

The fan

\&#91;
\overline\Sigma^{\max}
=
\{\mathcal Q,\langle u,e_y,v\rangle\}
\&#93;

is a common contraction. The two orders triangulate `Q` by different diagonals:

\&#91;
\Sigma_+:\quad\langle u,e_z\rangle,
\qquad
\Sigma_-:\quad\langle e_x,v\rangle.
\&#93;

Both contractions are projective and small. For `Sigma_+`, define a
piecewise-linear function by

\&#91;
\psi_+(u)=\psi_+(e_z)=0,
\qquad
\psi_+(e_x)=\psi_+(v)=1.
\&#93;

The linear extension from `\langle e_x,u,e_z\rangle` takes the value
`-r/s` at `v`, while the extension from `\langle u,v,e_z\rangle` takes the
value `-s/r` at `e_x`. Both are strictly less than the prescribed value `1`.
Thus `\psi_+` is the maximum of the two linear pieces and is strictly convex
across `\langle u,e_z\rangle`.

For `Sigma_-`, put

\&#91;
\psi_-(e_x)=\psi_-(v)=0,
\qquad
\psi_-(u)=\psi_-(e_z)=1.
\&#93;

The two off-cone extension values are `-p/q` and `-q/p`, again strictly less
than `1`. Hence `\psi_-` is strictly convex across
`\langle e_x,v\rangle`. The subdivisions are the two coherent
triangulations of `Q`. They introduce no new ray, so the exceptional loci have
codimension two.

Every triple among `e_x,u,v,e_z` is linearly independent. Hence these four rays form a circuit.

Put

\&#91;
 p=\frac{d_0}{h},\qquad
 q=\frac{a_0c_0}{h},\qquad
 r=\frac{b_0d_0}{h},\qquad
 s=\frac{a_0}{h}.
\&#93;

They are positive integers with

\&#91;
\gcd(p,q,r,s)=1.
\&#93;

### Theorem 6.1 — primitive circuit

One has the primitive relation

\&#91;
\boxed{
pu+q e_z=r e_x+s v=w.
}
\&#93;

Equivalently, in the unreduced exponents let

\&#91;
G=\gcd(bd,ad,ac)=g_1g_2h.
\&#93;

Then

\&#91;
\boxed{
\frac{dg_1}{G}u+\frac{ac}{G}e_z
=
\frac{bd}{G}e_x+\frac{ag_2}{G}v.
}
\&#93;

### Cross-lattice quotient

The four circuit rays generate

\&#91;
L=\mathbb Ze_x+\mathbb Ze_z+h\mathbb Ze_y
\subset N.
\&#93;

Therefore

\&#91;
\boxed{N/L\cong\mathbb Z/h\mathbb Z.}
\&#93;

On the finite toric cover with lattice `L`, the circuit is a rank-one GIT wall with weights

\&#91;
(p,q,-r,-s).
\&#93;

The original circuit is its finite cyclic quotient of order `h`.

---

## 7. Common resolution

The ray `w` lies in the relative interior of both diagonals:

\&#91;
w=pu+qe_z=re_x+sv.
\&#93;

Star-subdividing either ordered fan at `w` gives the same fan

\&#91;
\boxed{
\widehat\Sigma^{\max}
=
\left\{
\begin{aligned}
&amp;\langle e_x,u,w\rangle,\\
&amp;\langle e_x,w,e_z\rangle,\\
&amp;\langle u,e_y,v\rangle,\\
&amp;\langle u,v,w\rangle,\\
&amp;\langle w,v,e_z\rangle.
\end{aligned}
\right\}
}
\&#93;

It also refines `Sigma_sim`: it triangulates the non-simplicial cone

\&#91;
\langle u,e_y,v,w\rangle
\&#93;

by the diagonal `\langle u,v\rangle`.

The resulting diagram separates the three constructions:

```text
                         X_hat
                       /   |   \
       divisorial     /    |    \     divisorial
                     /     |     \
                   X_+   X_sim   X_-
                     \             /
                      \           /
                       X_bar(Q)
```

The maps `X_hat -&gt; X_+` and `X_hat -&gt; X_-` contract the divisor of `w` to the respective diagonal curves. The map `X_hat -&gt; X_sim` is small because it only triangulates the central non-simplicial cone.

---

## 8. Cone indices and quotient singularities

The absolute determinants of the maximal cones are:

\&#91;
\begin{array}{c|c}
\Sigma_+&amp;\text{index}\\
\hline
\langle e_x,u,e_z\rangle&amp;a_0\\
\langle u,e_y,v\rangle&amp;b_0c_0\\
\langle u,v,e_z\rangle&amp;b_0d_0\\
\end{array}
\qquad
\begin{array}{c|c}
\Sigma_-&amp;\text{index}\\
\hline
\langle e_x,u,v\rangle&amp;a_0c_0\\
\langle u,e_y,v\rangle&amp;b_0c_0\\
\langle e_x,v,e_z\rangle&amp;d_0\\
\end{array}
\&#93;

These are the orders of the corresponding torus-fixed quotient groups on the coarse simplicial models. The two contracted curves have saturated ray lattices because

\&#91;
\gcd(a_0,b_0)=\gcd(c_0,d_0)=1;
\&#93;

there is no generic coarse quotient along either curve. The finite quotient `h` occurs across the full four-ray circuit.

The discarded scalars `g_1,g_2` do not affect the coarse normalized fans. In
the unreduced monomial Rees presentation, however, the natural wall vectors are

\&#91;
\widetilde u=(b,a,0)=g_1u,
\qquad
\widetilde v=(0,d,c)=g_2v,
\&#93;

and the simultaneous wall intersection is

\&#91;
\widetilde w=(bd,ad,ac)=G w,
\qquad G=g_1g_2h.
\&#93;

Thus a stacky Rees enhancement can retain `g_1`, `g_2`, and `G` as
nonprimitive ray multiplicities even though the coarse fan discards them. They
cannot be omitted from a PRS character calculation.

---

## 9. Canonical discrepancies and the order criterion

Let `E_w` be the divisor introduced by the common star subdivision.

For a simplicial toric cone, if a primitive subdivision ray is written as

\&#91;
w=\sum_i\lambda_i v_i,
\&#93;

its discrepancy is

\&#91;
\sum_i\lambda_i-1.
\&#93;

Therefore

\&#91;
 a(E_w;X_+)=p+q-1,
\&#93;

\&#91;
 a(E_w;X_-)=r+s-1.
\&#93;

Their difference is

\&#91;
\begin{aligned}
 a(E_w;X_+)-a(E_w;X_-)
 &amp;=p+q-r-s\\
 &amp;=\frac{a_0(c_0-1)-d_0(b_0-1)}{h}\\
 &amp;=\frac{\Delta}{h}.
\end{aligned}
\&#93;

### Theorem 9.1 — saturated order comparison

Under Definition 2.2, the birational map

\&#91;
X_+\dashrightarrow X_-
\&#93;

is a toric flop if and only if

\&#91;
\boxed{
\Delta=0,
\quad\text{i.e.}\quad
 a_0(c_0-1)=d_0(b_0-1).
}
\&#93;

In the unreduced exponents this is equivalent to

\&#91;
\boxed{
 d\gcd(a,b)+ac
 =
 bd+a\gcd(c,d).
}
\&#93;

If `C_+` and `C_-` are the invariant curves contracted by the two small maps to `X_bar`, the wall relations are respectively

\&#91;
r e_x+s v-pu-qe_z=0
\&#93;

across `\langle u,e_z\rangle`, and its negative across
`\langle e_x,v\rangle`. The toric wall-intersection formula therefore gives
positive rational constants `m_+,m_-&gt;0` such that

\&#91;
K_{X_+}\cdot C_+
=\frac{p+q-r-s}{m_+},
\qquad
K_{X_-}\cdot C_-
=\frac{r+s-p-q}{m_-}.
\&#93;

Consequently

\&#91;
\operatorname{sign}(K_{X_+}\cdot C_+)=\operatorname{sign}(\Delta),
\qquad
\operatorname{sign}(K_{X_-}\cdot C_-)=-\operatorname{sign}(\Delta).
\&#93;

Hence:

- `Delta&gt;0`: the `J then I` model is `K`-negative and flips to the `I then J` model;
- `Delta&lt;0`: the `I then J` model is `K`-negative and flips to the reverse model;
- `Delta=0`: both contractions are crepant and the wall crossing is a flop.

### Equivalent Q-Gorenstein criterion

The common four-ray cone `Q` is Q-Gorenstein exactly when a linear form can take value `1` on all four rays. The circuit relation shows that this is equivalent to

\&#91;
p+q=r+s.
\&#93;

Thus `X_bar` is Q-Gorenstein exactly on the flop locus.

### GIT character proof

On the circuit cover lattice `L`, the rank-one GIT weights are

\&#91;
(p,q,-r,-s).
\&#93;

The canonical character of the four-coordinate cover is

\&#91;
p+q-r-s=\Delta/h.
\&#93;

It vanishes exactly on the same locus. This gives a second proof of the crepancy criterion and identifies the character that must be transported in a stacky triple-overlap calculation.

---

## 10. Complete parametrization of the flop locus

Write

\&#91;
a_0=hA,\qquad d_0=hD,
\qquad \gcd(A,D)=1.
\&#93;

The equation `Delta=0` becomes

\&#91;
A(c_0-1)=D(b_0-1).
\&#93;

Since `A` and `D` are coprime, `A` divides `b_0-1` and `D` divides
`c_0-1`. The two quotients agree, so there is a unique integer `t&gt;=0` such
that

\&#91;
\boxed{
 b_0=1+At,
 \qquad
 c_0=1+Dt.
}
\&#93;

Conversely, these formulas imply `Delta=0`. To retain the reduced-pair hypotheses one also requires

\&#91;
\gcd(h,1+At)=\gcd(h,1+Dt)=1.
\&#93;

Thus every reduced crepant quadruple has the form

\&#91;
\boxed{
(a_0,b_0,c_0,d_0)
=
(hA,1+At,1+Dt,hD)
}
\&#93;

with

\&#91;
\gcd(A,D)=1,
\qquad
\gcd(h,(1+At)(1+Dt))=1.
\&#93;

The exponent-one quintic calibration is

\&#91;
a_0=b_0=c_0=d_0=1,
\&#93;

for which

\&#91;
u+e_z=e_x+v
\&#93;

and the wall is the Atiyah flop.

---

## 11. What the all-rank PRS theorem does and does not determine

The public all-rank Lane 2 theorem determines:

- the normal-index composition;
- each block size
  \&#91;
  d_j=n_j-n_{j-1};
  \&#93;
- the radial Smith exponent
  \&#91;
  \mu_j=\nu-m+n_{j-1}+n_j
  \&#93;
  with multiplicity `d_j`.

Those are one-parameter radial data. The adjacent-merge theorem needs a
three-divisor valuation model, four reduced exponents, and a declared transform
operation. The public record for the toroidal PRS graph states that an explicit
chart monomial ideal exists, but it supplies no public locator from which its
four local pivot valuations, transform convention, saturation factors, or
characters can be reconstructed.

The public exact quintic packet does show removal of common Cartier factors
when simplifying projective pairs. That supports Definition 2.1 locally, but
it does not constitute an all-rank definition for the abstract adjacent-merge
construction. Therefore the theorem cannot yet be specialized merely from
block sizes and scalar Smith exponents, and Definition 2.2 must not be silently
substituted for Definition 2.1.

---

## 12. Exact PRS specialization data required

A PRS adjacent merge is classified once the following packet is supplied.

### 12.1 Transform convention

The packet must select exactly one of

```text
cartier_factor_weak
exceptional_saturation
```

and cite the proof location showing that this operation is the one used by the
actual PRS graph. Under the first choice, Theorem 5.1 applies and the orders
agree. Under the second, Theorem 9.1 applies and `Delta` controls the flip or
flop.

### 12.2 Toroidal coordinate packet

A normal local or completed chart `R`, with primitive boundary parameters

\&#91;
X,Y,Z
\&#93;

and a specified lattice isomorphism

\&#91;
\operatorname{Div}_{\mathrm{tor}}(R)\cong\mathbb Z^3.
\&#93;

The packet must identify which divisor is shared by the two adjacent merges. In the model above it is `Y=0`.

### 12.3 Four pivot valuation vectors

After removing one common monomial factor from each projective pair, the two adjacent center ideals must have integral closures

\&#91;
\overline{I_{\mathrm{PRS}}}
=
\overline{(X^a,Y^b)},
\&#93;

\&#91;
\overline{J_{\mathrm{PRS}}}
=
\overline{(Y^c,Z^d)}.
\&#93;

Equivalently, the four leading pivot sections must have valuation matrix

\&#91;
\boxed{
\begin{pmatrix}
 a&amp;0&amp;0\\
 0&amp;b&amp;0\\
 0&amp;c&amp;0\\
 0&amp;0&amp;d
\end{pmatrix}
}
\&#93;

up to the two declared row-pair translations corresponding to projective common factors.

A Gröbner, Newton-polyhedron, or integral-dependence certificate must show that higher terms add no new compact Newton face. A leading-term display without this certificate is insufficient because normalized blowups depend on integral closure, not only on the first visible monomials.

### 12.4 Transform ledger

For each order, the packet must state:

- the first exceptional ray and its primitive/coarse multiplicity;
- the exceptional orders of every pulled-back generator;
- the exact common Cartier factor removed, if Definition 2.1 is selected;
- the exact saturation and resulting ideal, if Definition 2.2 is selected;
- every localization used to make units invertible;
- the retained closed complement.

The shared common-factor valuation `kappa` must be attached to an actual divisor and to the four pivot valuation rows. A scalar `kappa` without that incidence information does not determine `a,b,c,d`.

### 12.5 Lattice and stack data

The coarse criterion uses the primitive rays, but P4-L2B needs more:

- nonprimitive stacky ray multiplicities, including any retained analogues of `g_1` and `g_2`;
- the cross-circuit quotient `N/L`, whose abstract model has order
  \&#91;
  h=\gcd(a_0,d_0);
  \&#93;
- Smith normal forms or explicit character matrices for every quotient chart;
- the stacky multiplicity assigned to the simultaneous ray `w`;
- projective-coordinate and exceptional-line-bundle characters.

### 12.6 PRS transfer data

The packet must include the exact adjacent transfer matrices before and after each merge, together with:

- their monomial factors in `X,Y,Z`;
- the unit residual matrices;
- the action on every projective PRS coordinate;
- the induced character on the relative-Jacobian marking.

This is what allows the coarse circuit comparison to be upgraded to literal equality or a measured residual character on triple overlaps.

---

## 13. Fail-closed specialization rule

Given a schema-valid packet, compute

\&#91;
g_1=\gcd(a,b),\quad g_2=\gcd(c,d),
\&#93;

\&#91;
a_0=a/g_1,\quad b_0=b/g_1,
\quad c_0=c/g_2,\quad d_0=d/g_2,
\&#93;

and

\&#91;
\Delta=a_0(c_0-1)-d_0(b_0-1).
\&#93;

The report is then:

\&#91;
\begin{array}{c|c}
\texttt{cartier\_factor\_weak}
 &amp;\text{orders identical; model }\Sigma_{\mathrm{sim}}\\
\texttt{exceptional\_saturation},\ \Delta=0
 &amp;\text{coarse crepant flop}\\
\texttt{exceptional\_saturation},\ \Delta&gt;0
 &amp;J\!\to I\text{ model flips to }I\!\to J\\
\texttt{exceptional\_saturation},\ \Delta&lt;0
 &amp;I\!\to J\text{ model flips to }J\!\to I\\
\end{array}
\&#93;

If any convention, integral-closure, transform, lattice, or character field is missing, the result must be

```text
INSUFFICIENT PRS PIVOT DATA
```

rather than an inferred exponent quadruple.

---

## 14. Consequence for P4-L2B

The abstract toric part of the triple-overlap problem is now explicit but
convention-dependent. A Cartier-factor weak wall contributes one literal
simultaneous refinement and no diagonal ambiguity. An exceptional-saturated
wall contributes:

1. a primitive circuit relation;
2. a finite cyclic circuit quotient of order `h`;
3. a canonical GIT character `Delta/h`;
4. two ordered diagonal choices;
5. one simultaneous ray removed by saturation.

What remains for the actual PRS triple overlap is not the coarse fan calculation. It is the comparison of:

- the two products of PRS transfer matrices;
- the stacky quotient characters;
- the projective-coordinate linearizations;
- the relative-Jacobian marking.

A residual character on a triple overlap should be reported rather than silently identified with a fixed-chart automorphism.

---

## 15. Evidence boundary

The supplied exact programs verify:

- that Cartier-factor exceptional orders are zero in both orders and hence
  give the simultaneous fan;
- all canonical-cover monomial saturation formulas;
- the simultaneous fan by reconstructing its extreme rays from inequalities;
- the two ordered fan formulas;
- every circuit coefficient and primitive-ray formula;
- the cross-lattice index `h`;
- all cone-index formulas;
- the discrepancy difference;
- the complete parametrization of the flop locus.

The main program checks all

\&#91;
1\le a,b,c,d\le12
\&#93;

and an independent standard-library implementation checks all

\&#91;
1\le a,b,c,d\le16.
\&#93;

The programs do not replace the standard toric facts used in the proof: normalized monomial blowups are described by order-function subdivisions, simplicial canonical divisors are evaluated by their support functions, and coherent circuit triangulations give projective toric flips/flops.

No arbitrary-rank PRS specialization is claimed without a schema-valid pivot packet.
</code></pre>

<a id="source-07f339823674727e"></a>

## `research-notes/lane2-adjacent-merge-20260803-v1/adjacent_merge_report.json`

<pre><code class="language-json">
{
  "crepant_raw_quadruples": 2016,
  "grid_max": 12,
  "negative_delta_raw_quadruples": 9360,
  "positive_delta_raw_quadruples": 9360,
  "raw_quadruples_checked": 20736,
  "reduced_records": 8281,
  "reduced_records_sha256": "f06151e38cb599c63cbf7180544db170db7b0db59388276827d30f483a1aa99a",
  "schema_version": 1,
  "theorem": {
    "cartier_factor_weak_criterion": "orders always identical",
    "cartier_factor_weak_fan": "simultaneous_fan_in_both_orders",
    "exceptional_saturation_flop_criterion": "a0*(c0-1) = d0*(b0-1)",
    "saturated_minus_fan": &#91;
      "&lt;e_x,u,v&gt;",
      "&lt;u,e_y,v&gt;",
      "&lt;e_x,v,e_z&gt;"
    &#93;,
    "saturated_plus_fan": &#91;
      "&lt;e_x,u,e_z&gt;",
      "&lt;u,e_y,v&gt;",
      "&lt;u,v,e_z&gt;"
    &#93;,
    "simultaneous_fan": &#91;
      "&lt;e_x,u,w&gt;",
      "&lt;e_x,w,e_z&gt;",
      "&lt;u,e_y,v,w&gt;",
      "&lt;w,v,e_z&gt;"
    &#93;
  }
}
</code></pre>

<a id="source-15e93255c30465a0"></a>

## `research-notes/lane2-adjacent-merge-20260803-v1/verify_adjacent_merge.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact verifier for P4-L2A: noncoprime adjacent toric merges.

The verifier checks, for all 1 &lt;= a,b,c,d &lt;= GRID_MAX:

1. the primitive normalized-blowup rays u and v;
2. the canonical-cover exceptional-saturation calculation in both orders;
3. the two exceptional-saturated ordered fans and the Cartier-weak common refinement;
4. the simultaneous-linearity fan from its defining inequalities;
5. the primitive circuit, common lattice index, and common refinement ray w;
6. cone-index formulas;
7. discrepancy difference and the K-flip/flop criterion;
8. the complete parametrization of the crepant locus.

The geometric facts that normalized monomial blowups are the fan subdivisions
of their order functions, and that toric discrepancies are evaluated by the
canonical support function, are conventional proof inputs. Everything
specific to the displayed formulas is checked exactly here.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import gcd
import json
from pathlib import Path
from typing import Iterable, Sequence

import sympy as sp

GRID_MAX = 12
ROOT = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "adjacent_merge_report.json"

Vec = tuple&#91;int, int, int&#93;


def gcd_many(values: Iterable&#91;int&#93;) -&gt; int:
    g = 0
    for value in values:
        g = gcd(g, abs(int(value)))
    return g


def add(*vectors: Vec) -&gt; Vec:
    return tuple(sum(v&#91;i&#93; for v in vectors) for i in range(3))  # type: ignore&#91;return-value&#93;


def scale(k: int, v: Vec) -&gt; Vec:
    return (k * v&#91;0&#93;, k * v&#91;1&#93;, k * v&#91;2&#93;)


def dot(a: Vec, b: Vec) -&gt; int:
    return sum(a&#91;i&#93; * b&#91;i&#93; for i in range(3))


def cross(a: Vec, b: Vec) -&gt; Vec:
    return (
        a&#91;1&#93; * b&#91;2&#93; - a&#91;2&#93; * b&#91;1&#93;,
        a&#91;2&#93; * b&#91;0&#93; - a&#91;0&#93; * b&#91;2&#93;,
        a&#91;0&#93; * b&#91;1&#93; - a&#91;1&#93; * b&#91;0&#93;,
    )


def primitive(v: Vec) -&gt; Vec:
    g = gcd_many(v)
    if g == 0:
        raise ValueError("zero vector has no primitive representative")
    vv = tuple(x // g for x in v)
    for x in vv:
        if x:
            if x &lt; 0:
                vv = tuple(-y for y in vv)
            break
    return vv  # type: ignore&#91;return-value&#93;


def det3(a: Vec, b: Vec, c: Vec) -&gt; int:
    return dot(a, cross(b, c))


def cone_index(rays: Sequence&#91;Vec&#93;) -&gt; int:
    if len(rays) != 3:
        raise ValueError("full-dimensional simplicial cone requires three rays")
    return abs(det3(rays&#91;0&#93;, rays&#91;1&#93;, rays&#91;2&#93;))


def extreme_rays(inequalities: Sequence&#91;Vec&#93;) -&gt; set&#91;Vec&#93;:
    """Extreme rays of a pointed three-dimensional cone {n: row.n &gt;= 0}.

    In dimension three, every extreme ray is the intersection of two facet
    hyperplanes. The routine is exact and intentionally small.
    """
    rays: set&#91;Vec&#93; = set()
    for i, j in combinations(range(len(inequalities)), 2):
        candidate = cross(inequalities&#91;i&#93;, inequalities&#91;j&#93;)
        if candidate == (0, 0, 0):
            continue
        for oriented in (candidate, scale(-1, candidate)):
            if all(dot(row, oriented) &gt;= 0 for row in inequalities):
                rays.add(primitive(oriented))
                break
    return rays


def minimal_monomial_generators(gens: Iterable&#91;tuple&#91;int, ...&#93;&#93;) -&gt; tuple&#91;tuple&#91;int, ...&#93;, ...&#93;:
    data = sorted(set(gens), key=lambda x: (sum(x), x))
    keep: list&#91;tuple&#91;int, ...&#93;&#93; = &#91;&#93;
    for candidate in data:
        if any(all(a &lt;= b for a, b in zip(existing, candidate)) for existing in keep):
            continue
        keep = &#91;
            existing
            for existing in keep
            if not all(a &lt;= b for a, b in zip(candidate, existing))
        &#93;
        keep.append(candidate)
    return tuple(sorted(keep))


def saturate_monomial_by_variable(
    gens: Iterable&#91;tuple&#91;int, ...&#93;&#93;, variable: int
) -&gt; tuple&#91;tuple&#91;int, ...&#93;, ...&#93;:
    """Return generators of I:x_variable^infinity for a monomial ideal I."""
    stripped = &#91;&#93;
    for exponent in gens:
        row = list(exponent)
        row&#91;variable&#93; = 0
        stripped.append(tuple(row))
    return minimal_monomial_generators(stripped)


@dataclass(frozen=True)
class MergeData:
    a: int
    b: int
    c: int
    d: int
    g1: int
    g2: int
    a0: int
    b0: int
    c0: int
    d0: int
    h: int
    u: Vec
    v: Vec
    w: Vec
    p: int
    q: int
    r: int
    s: int
    delta: int


def merge_data(a: int, b: int, c: int, d: int) -&gt; MergeData:
    if min(a, b, c, d) &lt;= 0:
        raise ValueError("all exponents must be positive")
    g1 = gcd(a, b)
    g2 = gcd(c, d)
    a0, b0 = a // g1, b // g1
    c0, d0 = c // g2, d // g2
    h = gcd(a0, d0)
    u = (b0, a0, 0)
    v = (0, d0, c0)
    w = (b0 * d0 // h, a0 * d0 // h, a0 * c0 // h)
    p = d0 // h
    q = a0 * c0 // h
    r = b0 * d0 // h
    s = a0 // h
    delta = a0 * (c0 - 1) - d0 * (b0 - 1)
    return MergeData(a, b, c, d, g1, g2, a0, b0, c0, d0, h, u, v, w, p, q, r, s, delta)


def check_cover_transforms(m: MergeData) -&gt; None:
    """Check Cartier-factor and exceptional-saturated transforms.

    Exponent order in each tuple is (first chart coordinate, exceptional E,
    second chart coordinate). Only monomial saturation is used.
    """
    # Blow up I first. On cone &lt;e_x,u,e_z&gt;:
    # x = X E^b0, y = E^a0, z = Z.
    n_i = m.g1 * m.a0 * m.b0
    x_a = (m.a, m.a * m.b0, 0)
    y_b = (0, m.b * m.a0, 0)
    assert x_a&#91;1&#93; == y_b&#91;1&#93; == n_i
    j_left = ((0, m.a0 * m.c, 0), (0, 0, m.d))
    assert min(g&#91;1&#93; for g in j_left) == 0  # Cartier weak transform is total.
    assert saturate_monomial_by_variable(j_left, 1) == ((0, 0, 0),)

    # On cone &lt;u,e_y,e_z&gt;: x=E^b0, y=E^a0 Y, z=Z.
    x_a = (0, m.a * m.b0, 0)
    y_b = (m.b, m.b * m.a0, 0)
    assert x_a&#91;1&#93; == y_b&#91;1&#93; == n_i
    j_right = ((m.c, m.a0 * m.c, 0), (0, 0, m.d))
    assert min(g&#91;1&#93; for g in j_right) == 0  # Cartier weak transform is total.
    assert saturate_monomial_by_variable(j_right, 1) == minimal_monomial_generators(
        ((m.c, 0, 0), (0, 0, m.d))
    )

    # Blow up J first. On cone &lt;e_x,e_y,v&gt;:
    # x=X, y=Y F^d0, z=F^c0.
    n_j = m.g2 * m.c0 * m.d0
    y_c = (0, m.c, m.c * m.d0)
    z_d = (0, 0, m.d * m.c0)
    assert y_c&#91;2&#93; == z_d&#91;2&#93; == n_j
    i_left = ((m.a, 0, 0), (0, m.b, m.b * m.d0))
    assert min(g&#91;2&#93; for g in i_left) == 0  # Cartier weak transform is total.
    assert saturate_monomial_by_variable(i_left, 2) == minimal_monomial_generators(
        ((m.a, 0, 0), (0, m.b, 0))
    )

    # On cone &lt;e_x,v,e_z&gt;: x=X, y=F^d0, z=F^c0 Z.
    y_c = (0, m.c * m.d0, 0)
    z_d = (0, m.d * m.c0, m.d)
    assert y_c&#91;1&#93; == z_d&#91;1&#93; == n_j
    i_right = ((m.a, 0, 0), (0, m.b * m.d0, 0))
    assert min(g&#91;1&#93; for g in i_right) == 0  # Cartier weak transform is total.
    assert saturate_monomial_by_variable(i_right, 1) == ((0, 0, 0),)


def check_simultaneous_fan(m: MergeData) -&gt; None:
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    # Signs: x_win means a0*n_x &lt;= b0*n_y; y_win_J means c0*n_y &lt;= d0*n_z.
    regions = {
        (True, True): {ez, m.v, m.w},
        (True, False): {m.u, ey, m.v, m.w},
        (False, True): {ex, m.w, ez},
        (False, False): {ex, m.u, m.w},
    }
    for (x_win, y_win_j), expected in regions.items():
        rows: list&#91;Vec&#93; = &#91;ex, ey, ez&#93;
        rows.append((-m.a0, m.b0, 0) if x_win else (m.a0, -m.b0, 0))
        rows.append((0, -m.c0, m.d0) if y_win_j else (0, m.c0, -m.d0))
        found = extreme_rays(rows)
        assert found == expected, (m, (x_win, y_win_j), found, expected)


def check_circuit_and_indices(m: MergeData) -&gt; None:
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    assert primitive(m.u) == m.u
    assert primitive(m.v) == m.v
    assert primitive(m.w) == m.w
    assert add(scale(m.p, m.u), scale(m.q, ez)) == m.w
    assert add(scale(m.r, ex), scale(m.s, m.v)) == m.w
    assert gcd_many((m.p, m.q, m.r, m.s)) == 1

    # Every proper triple is independent: this is a genuine four-ray circuit.
    determinants = {
        "ex_u_ez": abs(det3(ex, m.u, ez)),
        "u_v_ez": abs(det3(m.u, m.v, ez)),
        "ex_u_v": abs(det3(ex, m.u, m.v)),
        "ex_v_ez": abs(det3(ex, m.v, ez)),
    }
    assert determinants == {
        "ex_u_ez": m.a0,
        "u_v_ez": m.b0 * m.d0,
        "ex_u_v": m.a0 * m.c0,
        "ex_v_ez": m.d0,
    }

    plus_indices = (
        cone_index((ex, m.u, ez)),
        cone_index((m.u, ey, m.v)),
        cone_index((m.u, m.v, ez)),
    )
    minus_indices = (
        cone_index((ex, m.u, m.v)),
        cone_index((m.u, ey, m.v)),
        cone_index((ex, m.v, ez)),
    )
    assert plus_indices == (m.a0, m.b0 * m.c0, m.b0 * m.d0)
    assert minus_indices == (m.a0 * m.c0, m.b0 * m.c0, m.d0)

    # The four circuit rays generate Z e_x + Z e_z + h Z e_y.
    index = gcd_many(determinants.values())
    assert index == m.h
    assert gcd(m.a0, m.d0) == m.h

    # The two circuit triangulations are strict coherent subdivisions.
    # Plus heights: H(u)=H(ez)=0, H(ex)=H(v)=1.
    assert Fraction(-m.r, m.s) &lt; 1  # linear extension from &lt;ex,u,ez&gt; at v
    assert Fraction(-m.s, m.r) &lt; 1  # linear extension from &lt;u,v,ez&gt; at ex
    # Minus heights: H(ex)=H(v)=0, H(u)=H(ez)=1.
    assert Fraction(-m.p, m.q) &lt; 1  # extension from &lt;ex,u,v&gt; at ez
    assert Fraction(-m.q, m.p) &lt; 1  # extension from &lt;ex,v,ez&gt; at u

    # Discrepancy difference on the common star subdivision.
    discrepancy_plus = m.p + m.q - 1
    discrepancy_minus = m.r + m.s - 1
    assert discrepancy_plus - discrepancy_minus == m.delta // m.h
    assert m.delta % m.h == 0

    # The four-ray contraction is Q-Gorenstein iff all four rays lie on one
    # affine height-one hyperplane. Values on ex and ez force alpha=gamma=1;
    # the u equation forces beta=(1-b0)/a0, and v then gives delta=0.
    beta = Fraction(1 - m.b0, m.a0)
    q_gorenstein = Fraction(m.d0) * beta + m.c0 == 1
    assert q_gorenstein == (m.delta == 0)

    # Raw-exponent version used by the handoff note.
    G = gcd_many((m.b * m.d, m.a * m.d, m.a * m.c))
    assert G == m.g1 * m.g2 * m.h
    assert m.p == m.d * m.g1 // G
    assert m.q == m.a * m.c // G
    assert m.r == m.b * m.d // G
    assert m.s == m.a * m.g2 // G
    assert scale(m.g1, m.u) == (m.b, m.a, 0)
    assert scale(m.g2, m.v) == (0, m.d, m.c)
    assert scale(G, m.w) == (m.b * m.d, m.a * m.d, m.a * m.c)


def check_flop_parametrization(m: MergeData) -&gt; None:
    if m.delta != 0:
        return
    A = m.a0 // m.h
    D = m.d0 // m.h
    assert gcd(A, D) == 1
    assert (m.b0 - 1) % A == 0
    assert (m.c0 - 1) % D == 0
    t1 = (m.b0 - 1) // A
    t2 = (m.c0 - 1) // D
    assert t1 == t2 and t1 &gt;= 0
    assert m.b0 == 1 + A * t1
    assert m.c0 == 1 + D * t1
    assert gcd(m.h, m.b0) == gcd(m.h, m.c0) == 1


def symbolic_checks() -&gt; None:
    a0, b0, c0, d0, h = sp.symbols("a0 b0 c0 d0 h", positive=True, integer=True)
    ex = sp.Matrix(&#91;1, 0, 0&#93;)
    ez = sp.Matrix(&#91;0, 0, 1&#93;)
    u = sp.Matrix(&#91;b0, a0, 0&#93;)
    v = sp.Matrix(&#91;0, d0, c0&#93;)
    w = sp.Matrix(&#91;b0 * d0 / h, a0 * d0 / h, a0 * c0 / h&#93;)
    p, q, r, s = d0 / h, a0 * c0 / h, b0 * d0 / h, a0 / h
    assert sp.simplify(p * u + q * ez - w) == sp.zeros(3, 1)
    assert sp.simplify(r * ex + s * v - w) == sp.zeros(3, 1)
    delta = a0 * (c0 - 1) - d0 * (b0 - 1)
    assert sp.simplify((p + q - 1) - (r + s - 1) - delta / h) == 0


def main() -&gt; None:
    symbolic_checks()
    records: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    total = 0
    crepant = 0
    positive = 0
    negative = 0

    for a, b, c, d in product(range(1, GRID_MAX + 1), repeat=4):
        m = merge_data(a, b, c, d)
        check_cover_transforms(m)
        check_simultaneous_fan(m)
        check_circuit_and_indices(m)
        check_flop_parametrization(m)
        total += 1
        if m.delta == 0:
            crepant += 1
        elif m.delta &gt; 0:
            positive += 1
        else:
            negative += 1
        # Retain one representative for each reduced quadruple.
        if m.g1 == 1 and m.g2 == 1:
            records.append(
                {
                    "a0": m.a0,
                    "b0": m.b0,
                    "c0": m.c0,
                    "d0": m.d0,
                    "h": m.h,
                    "u": m.u,
                    "v": m.v,
                    "w": m.w,
                    "circuit": &#91;m.p, m.q, -m.r, -m.s&#93;,
                    "delta": m.delta,
                    "classification": (
                        "flop" if m.delta == 0 else "J_to_I -&gt; I_to_J flip" if m.delta &gt; 0 else "I_to_J -&gt; J_to_I flip"
                    ),
                }
            )

    canonical = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    digest = sha256(canonical).hexdigest()
    report = {
        "schema_version": 1,
        "grid_max": GRID_MAX,
        "raw_quadruples_checked": total,
        "crepant_raw_quadruples": crepant,
        "positive_delta_raw_quadruples": positive,
        "negative_delta_raw_quadruples": negative,
        "reduced_records": len(records),
        "reduced_records_sha256": digest,
        "theorem": {
            "cartier_factor_weak_fan": "simultaneous_fan_in_both_orders",
            "saturated_plus_fan": &#91;"&lt;e_x,u,e_z&gt;", "&lt;u,e_y,v&gt;", "&lt;u,v,e_z&gt;"&#93;,
            "saturated_minus_fan": &#91;"&lt;e_x,u,v&gt;", "&lt;u,e_y,v&gt;", "&lt;e_x,v,e_z&gt;"&#93;,
            "simultaneous_fan": &#91;
                "&lt;e_x,u,w&gt;",
                "&lt;e_x,w,e_z&gt;",
                "&lt;u,e_y,v,w&gt;",
                "&lt;w,v,e_z&gt;",
            &#93;,
            "cartier_factor_weak_criterion": "orders always identical",
            "exceptional_saturation_flop_criterion": "a0*(c0-1) = d0*(b0-1)",
        },
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("P4-L2A exact adjacent-merge verification")
    print(f"grid: 1 &lt;= a,b,c,d &lt;= {GRID_MAX}")
    print(f"raw quadruples checked: {total}")
    print(f"crepant / delta&gt;0 / delta&lt;0: {crepant} / {positive} / {negative}")
    print(f"reduced records: {len(records)}")
    print(f"reduced-record digest: {digest}")
    print("Cartier-factor weak transforms commute: PASS")
    print("canonical-cover exceptional saturations: PASS")
    print("saturated ordered fans: PASS")
    print("simultaneous-linearity fan: PASS")
    print("primitive circuit and lattice-index formulas: PASS")
    print("cone indices, coherent triangulations, and discrepancies: PASS")
    print("Q-Gorenstein/flop criterion and crepant-locus parametrization: PASS")
    print("ALL P4-L2A ADJACENT-MERGE CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-6d19b492e8373155"></a>

## `research-notes/lane2-adjacent-merge-20260803-v1/verify_adjacent_merge_independent.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independent standard-library replay for the P4-L2A toric theorem.

This implementation intentionally does not import SymPy. It reconstructs the
four simultaneous chambers directly from inequalities, checks the two circuit
triangulations and canonical-cover monomial saturations, and audits the flop
locus through a larger finite grid.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations, product
from math import gcd
import json

GRID_MAX = 16


def gcd_all(xs):
    g = 0
    for x in xs:
        g = gcd(g, abs(x))
    return g


def dot(a, b):
    return a&#91;0&#93;*b&#91;0&#93; + a&#91;1&#93;*b&#91;1&#93; + a&#91;2&#93;*b&#91;2&#93;


def cross(a, b):
    return (
        a&#91;1&#93;*b&#91;2&#93;-a&#91;2&#93;*b&#91;1&#93;,
        a&#91;2&#93;*b&#91;0&#93;-a&#91;0&#93;*b&#91;2&#93;,
        a&#91;0&#93;*b&#91;1&#93;-a&#91;1&#93;*b&#91;0&#93;,
    )


def neg(a):
    return (-a&#91;0&#93;, -a&#91;1&#93;, -a&#91;2&#93;)


def primitive(v):
    g = gcd_all(v)
    assert g
    w = tuple(x//g for x in v)
    for x in w:
        if x:
            return neg(w) if x &lt; 0 else w
    raise AssertionError


def det(a, b, c):
    return dot(a, cross(b, c))


def extreme_rays(rows):
    ans = set()
    for i, j in combinations(range(len(rows)), 2):
        v = cross(rows&#91;i&#93;, rows&#91;j&#93;)
        if v == (0,0,0):
            continue
        for w in (v, neg(v)):
            if all(dot(r, w) &gt;= 0 for r in rows):
                ans.add(primitive(w))
                break
    return ans


def monomial_saturate(gens, idx):
    stripped = &#91;&#93;
    for g in gens:
        row = list(g)
        row&#91;idx&#93; = 0
        stripped.append(tuple(row))
    minimal = &#91;&#93;
    for q in sorted(set(stripped), key=lambda z:(sum(z), z)):
        if any(all(p&#91;i&#93; &lt;= q&#91;i&#93; for i in range(len(q))) for p in minimal):
            continue
        minimal = &#91;p for p in minimal if not all(q&#91;i&#93; &lt;= p&#91;i&#93; for i in range(len(q)))&#93;
        minimal.append(q)
    return tuple(sorted(minimal))


def audit(a,b,c,d):
    ex,ey,ez=(1,0,0),(0,1,0),(0,0,1)
    g1,g2=gcd(a,b),gcd(c,d)
    a0,b0,c0,d0=a//g1,b//g1,c//g2,d//g2
    h=gcd(a0,d0)
    u=(b0,a0,0)
    v=(0,d0,c0)
    w=(b0*d0//h,a0*d0//h,a0*c0//h)
    p,q,r,s=d0//h,a0*c0//h,b0*d0//h,a0//h
    delta=a0*(c0-1)-d0*(b0-1)

    assert tuple(p*u&#91;i&#93;+q*ez&#91;i&#93; for i in range(3)) == w
    assert tuple(r*ex&#91;i&#93;+s*v&#91;i&#93; for i in range(3)) == w
    assert gcd_all((p,q,r,s)) == 1
    assert gcd_all(w) == 1

    # Circuit determinants and the cross-lattice quotient N/L = Z/h.
    minors=(abs(det(ex,u,ez)),abs(det(u,v,ez)),abs(det(ex,u,v)),abs(det(ex,v,ez)))
    assert minors==(a0,b0*d0,a0*c0,d0)
    assert gcd_all(minors)==h

    # Ordered cone indices.
    assert (abs(det(ex,u,ez)),abs(det(u,ey,v)),abs(det(u,v,ez))) == (a0,b0*c0,b0*d0)
    assert (abs(det(ex,u,v)),abs(det(u,ey,v)),abs(det(ex,v,ez))) == (a0*c0,b0*c0,d0)

    # Four domains of simultaneous linearity.
    chambers={
      (1,1):{ez,v,w},
      (1,-1):{u,ey,v,w},
      (-1,1):{ex,w,ez},
      (-1,-1):{ex,u,w},
    }
    for (si,sj),expected in chambers.items():
        rows=&#91;ex,ey,ez&#93;
        rows.append((-a0,b0,0) if si==1 else (a0,-b0,0))
        rows.append((0,-c0,d0) if sj==1 else (0,c0,-d0))
        assert extreme_rays(rows)==expected

    # Cartier-factor weak transforms remove no exceptional power in either
    # order, because one generator has exceptional order zero on every chart.
    assert min(q&#91;1&#93; for q in ((0,a0*c,0),(0,0,d)))==0
    assert min(q&#91;1&#93; for q in ((c,a0*c,0),(0,0,d)))==0
    assert min(q&#91;2&#93; for q in ((a,0,0),(0,b,b*d0)))==0
    assert min(q&#91;1&#93; for q in ((a,0,0),(0,b*d0,0)))==0

    # Canonical-cover exceptional saturation, I then J.
    assert monomial_saturate(((0,a0*c,0),(0,0,d)),1)==((0,0,0),)
    assert monomial_saturate(((c,a0*c,0),(0,0,d)),1)==tuple(sorted(((c,0,0),(0,0,d))))
    # Reverse order.
    assert monomial_saturate(((a,0,0),(0,b,b*d0)),2)==tuple(sorted(((a,0,0),(0,b,0))))
    assert monomial_saturate(((a,0,0),(0,b*d0,0)),1)==((0,0,0),)

    # Coherent triangulations: the nonselected ray lies strictly above each
    # linear extension of the assigned 0/1 height data.
    from fractions import Fraction
    assert Fraction(-r,s)&lt;1 and Fraction(-s,r)&lt;1
    assert Fraction(-p,q)&lt;1 and Fraction(-q,p)&lt;1

    # Discrepancy difference, Q-Gorenstein criterion, and flop parametrization.
    assert (p+q-1)-(r+s-1)==delta//h
    assert delta%h==0
    beta=Fraction(1-b0,a0)
    assert ((d0*beta+c0)==1)==(delta==0)
    G=g1*g2*h
    assert tuple(g1*x for x in u)==(b,a,0)
    assert tuple(g2*x for x in v)==(0,d,c)
    assert tuple(G*x for x in w)==(b*d,a*d,a*c)
    if delta==0:
        A,D=a0//h,d0//h
        assert gcd(A,D)==1
        assert (b0-1)%A==0 and (c0-1)%D==0
        t=(b0-1)//A
        assert t==(c0-1)//D
        assert b0==1+A*t and c0==1+D*t
    return (a0,b0,c0,d0,h,p,q,r,s,delta)


def main():
    counts={"flop":0,"positive":0,"negative":0}
    reduced=set()
    for values in product(range(1,GRID_MAX+1), repeat=4):
        rec=audit(*values)
        reduced.add(rec)
        delta=rec&#91;-1&#93;
        counts&#91;"flop" if delta==0 else "positive" if delta&gt;0 else "negative"&#93; += 1
    encoded=json.dumps(sorted(reduced),separators=(",",":"),sort_keys=False).encode()
    digest=sha256(encoded).hexdigest()
    print("Independent P4-L2A replay (Python standard library)")
    print(f"grid: 1 &lt;= a,b,c,d &lt;= {GRID_MAX}")
    print(f"quadruples: {GRID_MAX**4}")
    print(f"class counts: {counts}")
    print(f"distinct reduced records: {len(reduced)}")
    print(f"record digest: {digest}")
    print("inequality reconstruction of simultaneous fan: PASS")
    print("Cartier-factor weak transforms commute: PASS")
    print("canonical-cover monomial saturations: PASS")
    print("circuit, lattice, coherence, and discrepancy formulas: PASS")
    print("Q-Gorenstein criterion and flop parametrization: PASS")
    print("INDEPENDENT P4-L2A CHECKS PASSED")

if __name__ == "__main__":
    main()
</code></pre>

<a id="source-bde5074568c74356"></a>

## `research-notes/lane2-projective-normalization-20260803-v1/README.md`

<pre><code class="language-markdown">
# Fixed quintic projective normalization packet

This packet gives one global bihomogeneous normalization algebra for the
fixed quintic outer simultaneous graph in Lane 2. It covers all four standard
charts of the two projective factors, proves finite birational normality,
computes the conductor, and records the overlap character of its generator.

The mathematical source is `bihomogeneous-normalization.md`. The two exact
programs replay complementary parts of the calculation:

- `verify_bihomogeneous_normalization.py` checks the seven bihomogeneous
  relations, four local presentations, saturated graph ideals, normality
  inputs, special fibres, and conductor gluing;
- `verify_conductor_module.py` independently computes the module-theoretic
  conductor annihilator.

This is a theorem about the displayed ordered pair of quintic ideals. It does
not establish an all-rank PRS theorem or a Torelli classification of arbitrary
marked inputs.

The corresponding immutable replay logs are under
`/path/to/versioned-artifact`.
</code></pre>

<a id="source-cf3c9ea55a4230d8"></a>

## `research-notes/lane2-projective-normalization-20260803-v1/bihomogeneous-normalization.md`

<pre><code class="language-markdown">
# Lane 2 A0: a single bihomogeneous normalization algebra

**Target:** `P4-L2A0`, projective completion of the exact quintic outer simultaneous graph.

The exact polynomial assertions are replayed by two algorithmically independent computations in this directory, both using SymPy 1.14.0. The Serre, Hilbert--Burch, and regular-element steps are written out below rather than delegated to those computations.

**Scope:** characteristic zero.  The displayed arguments only require the usual source-packet hypotheses together with invertibility of `2` where the two conductor sheets are separated.

**Source boundary:** the finite--finite normalization and the `T != 0` second-infinity normalization are imported from the public Lane 2 source packet at source commit

```text
43fe2294f74c961039a5b522f27a5982d511daa3
```

The source packet file is

```text
data/model-handoffs-v22-20260803c/lane-2-source-packet.md
```

with published SHA-256

```text
c58eed8642c332ebf2dcb5df492e9aeb0e3fda423377ceb11c3dfbe5a70ad2f4
```

The new contribution here is one global bihomogeneous algebra, a chart-complete normality proof, and an exact module-theoretic conductor computation.

---

## 1. Universal outer pair and graph

Let

\&#91;
\begin{aligned}
f_0&amp;=xz,
&amp;g_0&amp;=xt+yz,\\
f_1&amp;=(x-y^2)(x+z+ty),
&amp;g_1&amp;=xt+yz+2xy-y^3.
\end{aligned}
\&#93;

Use projective coordinates

\&#91;
&#91;U:V&#93;=&#91;f_0:g_0&#93;,
\qquad
&#91;P:Q&#93;=&#91;f_1:g_1&#93;.
\&#93;

Let

\&#91;
\Gamma
\subset
\mathbb A^4_{x,y,z,t}
\times\mathbb P^1_{&#91;U:V&#93;}
\times\mathbb P^1_{&#91;P:Q&#93;}
\&#93;

be the saturated closure of the simultaneous graph.  Thus its two incidence equations are

\&#91;
Ug_0-Vf_0=0,
\qquad
Pg_1-Qf_1=0,
\&#93;

but the scheme is understood with the base-locus torsion removed.

Put

\&#91;
h=x+z+ty,
\qquad
A=U^2-UVt+V^2z,
\qquad
X=Vx-Uy.
\tag{1.1}
\&#93;

Let

\&#91;
L=\mathcal O_{\Gamma}(1,1).
\&#93;

On the total space `Tot(L)`, denote the tautological fiber value by `Xi`.  In Cox notation, `Xi` has bidegree `(1,1)`.

---

## 2. The seven global relations

Define the following bihomogeneous sections on `Tot(L)`:

\&#91;
\begin{aligned}
R_0={}&amp;U(xt+yz)-Vxz,\\
R_1={}&amp;P(xt+yz+2xy-y^3)-Q(x-y^2)h,\\
R_2={}&amp;P(Vz+Uy)+\Xi y-UQh,\\
R_3={}&amp;\Xi z-(Vz-Ut)(Qh-Py)-UPz,\\
R_4={}&amp;\Xi(Vx-Uy)+UQ(U-Vy)h\\
&amp;\hspace{20mm}-UP\bigl(V(x+z-y^2)+Uy\bigr),\\
R_5={}&amp;U\Xi(x-y^2)-APx,\\
R_6={}&amp;\Xi^2-A\bigl(P^2-PQ(t+y)+Q^2h\bigr).
\end{aligned}
\tag{2.1}
\&#93;

Their bidegrees are respectively

\&#91;
(1,0),\ (0,1),\ (1,1),\ (1,1),\ (2,1),\ (2,1),\ (2,2).
\tag{2.2}
\&#93;

Let

\&#91;
\widetilde\Gamma=V(R_0,\ldots,R_6)\subset\operatorname{Tot}(L).
\tag{2.3}
\&#93;

The first six relations arise by bihomogenizing the complete first-projective-infinity chart.  They alone acquire an excess closure on the `V=0` boundary.  The additional relation

\&#91;
\boxed{R_5=U\Xi(x-y^2)-APx}
\tag{2.4}
\&#93;

is exactly the missing `U`-chart saturation relation.  With it included, all four standard charts are correct without any unrecorded chartwise repair.

More precisely, on the `U=P=1` chart the relation `R_5` is not contained in

\&#91;
(R_0,R_1,R_2,R_3,R_4,R_6),
\&#93;

whereas the exact saturation identity

\&#91;
(R_0,R_1,R_2,R_3,R_4,R_6):V^\infty
=(R_0,\ldots,R_6)
\tag{2.5}
\&#93;

holds after localization to this chart.  Thus `R_5` records a genuine boundary closure correction rather than a redundant presentational choice.

### Theorem 2.1 — global projective normalization

The projection

\&#91;
\nu:\widetilde\Gamma\longrightarrow\Gamma
\tag{2.6}
\&#93;

is finite, birational, and normal.  Consequently it is the normalization of the saturated projective simultaneous graph.

The morphism is projective and separated over `A^4`.

The rest of this note proves the theorem.

---

## 3. Exact recovery of all four affine charts

The tautological coordinate has local representatives

\&#91;
w=\frac{\Xi}{UP},
\qquad
\omega=\frac{\Xi}{UQ},
\qquad
\psi=\frac{\Xi}{VP},
\qquad
\chi=\frac{\Xi}{VQ}.
\tag{3.1}
\&#93;

Hence on overlaps

\&#91;
\boxed{
\omega=\frac{P}{Q}w,
\qquad
\psi=\frac{U}{V}w,
\qquad
\chi=\frac{U}{V}\omega
      =\frac{P}{Q}\psi.
}
\tag{3.2}
\&#93;

These are transition functions of `O(1,1)`.

### 3.1 `U=P=1`: finite--finite

Set

\&#91;
\lambda=V,
\qquad
\rho=Q,
\qquad
T=t-\lambda z,
\&#93;

and

\&#91;
\alpha=1-T\lambda,
\quad
u=Ty+z,
\quad
\xi=x-y^2,
\quad
v=u+\alpha x.
\&#93;

The sheaf ideal generated by (2.1) becomes exactly

\&#91;
\begin{aligned}
F_0&amp;=Tx+yz,\\
F_1&amp;=wu-\alpha z,\\
F_2&amp;=w\xi-\alpha x,\\
F_3&amp;=\rho v-\lambda z-(w+1)y,\\
F_4&amp;=w^2-\alpha(1-T\rho+\rho wy).
\end{aligned}
\tag{3.3}
\&#93;

This is the finite--finite normalization proved in the source packet.

Eliminating `w` gives exactly

\&#91;
(Tx+yz,\ g_1-\rho f_1):(f_0f_1)^\infty.
\tag{3.4}
\&#93;

### 3.2 `U=Q=1`: second-projective infinity

Set

\&#91;
\theta=P,
\qquad
\omega=\Xi,
\qquad
T=t-\lambda z.
\&#93;

The global ideal becomes exactly

\&#91;
\begin{aligned}
G_0&amp;=Tx+yz,\\
G_1&amp;=\omega(Ty+z)-(1-T\lambda)\theta z,\\
G_2&amp;=\omega(x-y^2)-(1-T\lambda)\theta x,\\
G_3&amp;=Ty+z+(1-T\lambda)x
     -\lambda\theta z-(\omega+\theta)y,\\
G_4&amp;=\omega^2-(1-T\lambda)
       (\theta^2-T\theta+\omega y).
\end{aligned}
\tag{3.5}
\&#93;

Eliminating `omega` gives exactly

\&#91;
(Tx+yz,\ f_1-\theta g_1):(f_0g_1)^\infty.
\tag{3.6}
\&#93;

### 3.3 `V=P=1`: first-projective infinity

Set

\&#91;
\eta=U,
\qquad
\rho=Q,
\qquad
\psi=\Xi,
\&#93;

and

\&#91;
A_\eta=\eta^2+z-\eta t,
\qquad
X_\eta=x-\eta y.
\&#93;

The seven global relations generate exactly the six-equation ideal

\&#91;
\begin{aligned}
K_0&amp;=\eta(xt+yz)-xz,\\
K_1&amp;=g_1-\rho f_1,\\
K_2&amp;=z+\eta y+\psi y-\eta\rho h,\\
K_3&amp;=\psi z-(z-\eta t)(\rho h-y)-\eta z,\\
K_4&amp;=\psi X_\eta+\eta\rho(\eta-y)h
      -\eta(x+z+\eta y-y^2),\\
K_5&amp;=\psi^2-A_\eta
       \bigl(1-\rho(t+y)+\rho^2h\bigr).
\end{aligned}
\tag{3.7}
\&#93;

The extra global relation `R_5` is a consequence of these six equations on this chart.

Eliminating `psi` gives exactly

\&#91;
(\eta g_0-f_0,\ g_1-\rho f_1):(g_0f_1)^\infty.
\tag{3.8}
\&#93;

Moreover

\&#91;
(K_0,\ldots,K_5):\eta^\infty=(K_0,\ldots,K_5).
\tag{3.9}
\&#93;

### 3.4 `V=Q=1`: double infinity

Set

\&#91;
\eta=U,
\qquad
\theta=P,
\qquad
\chi=\Xi.
\&#93;

The global ideal becomes exactly

\&#91;
\begin{aligned}
L_0&amp;=\eta g_0-f_0,\\
L_1&amp;=\theta g_1-f_1,\\
L_2&amp;=\theta(z+\eta y)+\chi y-\eta h,\\
L_3&amp;=\chi z-(z-\eta t)(h-\theta y)-\eta\theta z,\\
L_4&amp;=\chi X_\eta+\eta(\eta-y)h
      -\eta\theta(x+z+\eta y-y^2),\\
L_5&amp;=\chi^2-A_\eta
      \bigl(\theta^2-\theta(t+y)+h\bigr).
\end{aligned}
\tag{3.10}
\&#93;

Eliminating `chi` gives exactly

\&#91;
(\eta g_0-f_0,\ \theta g_1-f_1):(g_0g_1)^\infty.
\tag{3.11}
\&#93;

The ideal is saturated by both `eta` and `theta`.

### 3.5 Consequences

Every chart has a monic quadratic in its local normalization coordinate.  Thus `nu` is finite.  On the dense finite--finite open, `w` is the rational function already identified in the source packet, so `nu` is birational.

The four elimination identities show that the image is the saturated simultaneous graph, not the naive incidence scheme.

---

## 4. Normality

Normality is already known on the finite--finite chart.  It remains to justify the three charts meeting projective infinity.

### 4.1 Second infinity: a height-two determinantal ring

On the `U=Q=1` chart, work near

\&#91;
T=\theta=0.
\&#93;

Then

\&#91;
\alpha=1-T\lambda
\&#93;

is a unit.  Define

\&#91;
B=T(1-\lambda\theta)-\alpha y,
\qquad
r=\omega-\alpha\theta,
\qquad
q=\omega+\theta-T.
\&#93;

After using `G_3` to eliminate `x`, the remaining ideal is the maximal-minor ideal of

\&#91;
M=
\begin{pmatrix}
B&amp;Ty&amp;r\\
q&amp;z&amp;-\omega
\end{pmatrix}.
\tag{4.1}
\&#93;

The exact identities are

\&#91;
\det M_{12}=TG_3-\alpha G_0,
\qquad
\det M_{13}=-G_4,
\qquad
\det M_{23}=-G_1.
\tag{4.2}
\&#93;

Also

\&#91;
(\omega-\alpha\theta)G_3
=(1-\lambda\theta)G_1+\alpha G_2-yG_4,
\tag{4.3}
\&#93;

so `G_2` is redundant after `G_3` is used.

The two minors `G_1` and `G_4` have gcd `1`.  Therefore the maximal-minor ideal has height exactly two.  Hilbert--Burch gives Cohen--Macaulayness, hence `S_2`.  The ring has dimension four.

Exact saturation gives

\&#91;
(G_0,\ldots,G_4):\theta^\infty
=(G_0,\ldots,G_4)
\tag{4.4}
\&#93;

and likewise for saturation by `T`.  Since the `theta`-localization is the finite--finite normal domain, the whole chart injects into a domain and is itself a domain.

At `T=theta=0`, after eliminating `x`, the fiber is

\&#91;
k&#91;\lambda,y,z,\omega&#93;/
(yz,\omega z,\omega(\omega-y)).
\tag{4.5}
\&#93;

It has the exact reduced decomposition

\&#91;
(y,\omega)
\cap
(z,\omega)
\cap
(z,\omega-y).
\tag{4.6}
\&#93;

Each component has dimension two.  Thus the unresolved subset has codimension two.  Every codimension-one point lies in `D(T)` or `D(theta)`, where normality is supplied respectively by the source packet's second-infinity theorem and the finite--finite normalization.  Hence the chart is `R_1+S_2` and is normal.

### 4.2 First infinity: regular-element descent

The ideal (3.7) is `eta`-saturated, and its localization at `eta` is the finite--finite normal domain.  Hence the chart ring is a domain and `eta` is a nonzerodivisor.

At `eta=0`, its exact fiber is

\&#91;
\mathfrak p_A\cap\mathfrak p_B,
\tag{4.7}
\&#93;

where

\&#91;
\mathfrak p_A=
\bigl(
 z,\psi,
 xt+2xy-y^3-\rho(x-y^2)(x+ty)
\bigr),
\tag{4.8}
\&#93;

\&#91;
\mathfrak p_B=
\bigl(
 x,z+\psi y,
 \rho y(t-\psi)-(\psi+y)
\bigr).
\tag{4.9}
\&#93;

Both are prime.  For `p_A`, the remaining equation is primitive linear in `rho`, and

\&#91;
\gcd\bigl((x-y^2)(x+ty),\ xt+2xy-y^3\bigr)=1.
\&#93;

For `p_B`, the remaining equation is primitive linear in `rho`, and

\&#91;
\gcd\bigl(y(t-\psi),\psi+y\bigr)=1.
\&#93;

Thus the special fiber is reduced, hence `S_1`.  Since `eta` is regular and the complement `D(eta)` is normal, the regular-element depth lemma gives `S_2` for the total ring.  A height-one prime containing `eta` is minimal over `(eta)`; the reduced special fiber makes the corresponding one-dimensional local ring regular.  Hence the chart is `R_1`, and therefore normal.

### 4.3 Double infinity

The same argument applies to (3.10).  The ideal is `eta`-saturated, its `eta`-localization is the normal second-infinity chart, and the exact special fiber is

\&#91;
\mathfrak a\cap\mathfrak b,
\tag{4.10}
\&#93;

where

\&#91;
\mathfrak a=
\bigl(
z,\chi,
\theta g_1(x,y,0,t)-f_1(x,y,0,t)
\bigr),
\tag{4.11}
\&#93;

\&#91;
\mathfrak b=
\bigl(
 x,
 \chi-z-y(t-\theta),
 (t-\theta)y^2+z(\theta+y)
\bigr).
\tag{4.12}
\&#93;

Both are prime, using

\&#91;
\gcd(f_1(x,y,0,t),g_1(x,y,0,t))=1
\&#93;

and

\&#91;
\gcd(z-y^2,\ y(ty+z))=1.
\&#93;

The reduced-fiber regular-element argument gives normality.

At the corner `eta=theta=0`, the fiber is retained explicitly as the reduced union

\&#91;
\begin{aligned}
&amp;(x,y,z-\chi),\\
&amp;(\chi,x,z+ty),\\
&amp;(\chi,z,x-y^2),\\
&amp;(\chi,z,x+ty).
\end{aligned}
\tag{4.13}
\&#93;

No projective-boundary component is discarded.

This proves normality of all four charts and therefore of `tilde Gamma`.

---

## 5. Exact conductor by a module quotient

The following elementary lemma removes the ambiguity in the earlier chartwise conductor argument.

### Lemma 5.1 — annihilator formula

Let `S` be a polynomial ring, let `I` be an ideal, and suppose

\&#91;
B=
S&#91;\zeta&#93;/
\bigl(
I,
\zeta^2-c_1\zeta-c_0,
 a_i+b_i\zeta
\bigr).
\tag{5.1}
\&#93;

Assume the displayed ideal contracts to `I` in `S`, so that

\&#91;
A=S/I\subset B.
\&#93;

Then `B/A` is cyclic, generated by the class of `zeta`, and

\&#91;
\boxed{
\operatorname{Ann}_S(B/A)
=I+(b_i,\ a_i+b_ic_1).
}
\tag{5.2}
\&#93;

Consequently the conductor in `A` is the image of this ideal.

#### Proof

The monic quadratic reduces every element of `B` to `a+b zeta`, so `B/A` is generated by the class of `zeta`.  The relation

\&#91;
a_i+b_i\zeta=0
\&#93;

gives

\&#91;
b_i\bar\zeta=0
\&#93;

in `B/A`.  Multiplying by `zeta` and reducing `zeta^2=c_1zeta+c_0` gives

\&#91;
(a_i+b_ic_1)\bar\zeta=0.
\&#93;

Conversely, reduce every polynomial multiplier of every defining relation modulo the monic quadratic.  The coefficient of `zeta` in any resulting linear relation lies in the ideal on the right side of (5.2).  Hence there are no further annihilators. ∎

### 5.2 Application to the four charts

On the finite--finite chart, the coefficients of `w` in the three linear relations are

\&#91;
u,
\qquad
x-y^2,
\qquad
-y.
\&#93;

They generate

\&#91;
(x,y,z).
\&#93;

On the second-infinity chart, the coefficients of `omega` are the same three elements.

On the two first-infinity charts, the coefficients of `psi` or `chi` are

\&#91;
y,
\qquad
z,
\qquad
x-\eta y,
\&#93;

and again generate `(x,y,z)`.

The additional coefficients `a_i+b_ic_1` supplied by Lemma 5.1 lie in the same ideal.  Exact module-Groebner quotient computations independently return

\&#91;
\operatorname{Ann}_A(B/A)=(x,y,z)
\&#93;

on all four charts.

Therefore the global conductor is exactly

\&#91;
\boxed{
\mathfrak c=(x,y,z)\mathcal O_\Gamma.
}
\tag{5.3}
\&#93;

This is an equality, not only a radical or support statement.

---

## 6. Global conductor cover

Modulo `(x,y,z)`, equation `R_6` becomes

\&#91;
\boxed{
\Xi^2=U(U-tV)P(P-tQ).
}
\tag{6.1}
\&#93;

Thus the inverse image of the conductor is one double cover in the line bundle `O(1,1)`.

Its four local forms are

\&#91;
\begin{array}{c|c}
\text{chart}&amp;\text{equation}\\ \hline
U=P=1
&amp;w^2=(1-tV)(1-tQ),\\&#91;1mm&#93;
U=Q=1
&amp;\omega^2=(1-tV)P(P-t),\\&#91;1mm&#93;
V=P=1
&amp;\psi^2=U(U-t)(1-tQ),\\&#91;1mm&#93;
V=Q=1
&amp;\chi^2=U(U-t)P(P-t).
\end{array}
\tag{6.2}
\&#93;

Equivalently, in the finite notation of Section 3,

\&#91;
\begin{aligned}
w^2&amp;=(1-T\lambda)(1-T\rho),\\
\omega^2&amp;=(1-T\lambda)\theta(\theta-T),\\
\psi^2&amp;=\eta(\eta-t)(1-\rho t),\\
\chi^2&amp;=\eta(\eta-t)\theta(\theta-t).
\end{aligned}
\tag{6.3}
\&#93;

The branch divisor consists of four projective sections

\&#91;
U=0,
\qquad
U=tV,
\qquad
P=0,
\qquad
P=tQ.
\tag{6.4}
\&#93;

At `t=0`, the two sections in each projective factor collide and

\&#91;
\Xi^2=U^2P^2.
\tag{6.5}
\&#93;

This gives the global origin of the two local sheets that appear in the finite `T=0` analysis.

---

## 7. Projectivity, separatedness, and the next overlap problem

The graph `Gamma` is closed in

\&#91;
\mathbb A^4\times\mathbb P^1\times\mathbb P^1,
\&#93;

so it is projective and separated over `A^4`.  The normalization map is finite; therefore `tilde Gamma` is also projective and separated over `A^4`.

The normalization coordinate is not an untracked scalar.  It has the exact character

\&#91;
\boxed{\Xi\in\mathcal O(1,1).}
\tag{7.1}
\&#93;

This is the line-bundle datum needed in the later `P4-L2B` triple-overlap comparison.  Any triple-overlap theorem must transport this character together with the toric lattice map and the PRS transfer matrices.

---

## 8. Reproducibility and evidence boundary

Executed in this package:

1. exact bidegree verification of all seven relations;
2. exact ideal equality with all four local normalization presentations;
3. exact elimination to all four saturated graph ideals;
4. exact `eta` and `theta` saturation checks at infinity;
5. exact Hilbert--Burch minor identities and gcd check;
6. exact reduced special-fiber decompositions;
7. exact `O(1,1)` conductor gluing;
8. independent module-Groebner computation of the conductor annihilator.

Not delegated to the scripts:

1. the imported finite--finite and `T != 0` normality theorems;
2. Hilbert--Burch implies Cohen--Macaulay in height two;
3. the regular-element `S_1 -&gt; S_2` depth argument;
4. Serre's `R_1+S_2` criterion;
5. finite birational normal models are normalizations.

These are the conventional theorem inputs that require ordinary mathematical review.
</code></pre>

<a id="source-ee0ae7a75ef14c24"></a>

## `research-notes/lane2-projective-normalization-20260803-v1/verify_bihomogeneous_normalization.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact verification of the bihomogeneous Lane-2 A0 normalization.

This script checks the seven global bihomogeneous relations, their four
standard affine charts, the saturated graph images, the local normality
inputs, and the O(1,1) conductor cover.

It uses exact rational polynomial arithmetic in SymPy 1.14.0.  Serre's
criterion and the depth/Hilbert--Burch deductions are mathematical arguments
recorded in the companion note; the script verifies their polynomial inputs.
"""
from __future__ import annotations

import sympy as sp


def eliminated_saturation(gens, sat, variables):
    """Compute (gens : sat^infinity) by one-variable elimination."""
    aux = sp.Dummy("sat_aux")
    gb = sp.groebner(&#91;*gens, 1 - aux * sat&#93;, aux, *variables, order="lex")
    return &#91;sp.expand(p.as_expr()) for p in gb.polys if not p.as_expr().has(aux)&#93;


def eliminate_one(gens, variable, remaining):
    gb = sp.groebner(gens, variable, *remaining, order="lex")
    return &#91;sp.expand(p.as_expr()) for p in gb.polys if not p.as_expr().has(variable)&#93;


def ideal_equal(gens_a, gens_b, variables, label):
    ga = sp.groebner(gens_a, *variables, order="lex")
    gb = sp.groebner(gens_b, *variables, order="lex")
    assert all(ga.reduce(sp.expand(f))&#91;1&#93; == 0 for f in gens_b), f"{label}: B not in A"
    assert all(gb.reduce(sp.expand(f))&#91;1&#93; == 0 for f in gens_a), f"{label}: A not in B"


def ideal_intersection(gens_a, gens_b, variables):
    aux = sp.Dummy("mix_aux")
    gb = sp.groebner(
        &#91;*(aux * f for f in gens_a), *((1 - aux) * f for f in gens_b)&#93;,
        aux,
        *variables,
        order="lex",
    )
    return &#91;sp.expand(p.as_expr()) for p in gb.polys if not p.as_expr().has(aux)&#93;


def section(title):
    print(f"\n&#91;{title}&#93;")


# ---------------------------------------------------------------------------
# Global Cox-coordinate presentation
# ---------------------------------------------------------------------------
section("global bihomogeneous presentation")
x, y, z, t, U, V, P, Q, Xi = sp.symbols("x y z t U V P Q Xi")
f0 = x * z
g0 = x * t + y * z
h = x + z + t * y
f1 = (x - y**2) * h
g1 = x * t + y * z + 2 * x * y - y**3
A = U**2 - U * V * t + V**2 * z
X = V * x - U * y

R0 = sp.expand(U * g0 - V * f0)
R1 = sp.expand(P * g1 - Q * f1)
R2 = sp.expand(P * (V * z + U * y) + Xi * y - U * Q * h)
R3 = sp.expand(Xi * z - (V * z - U * t) * (Q * h - P * y) - U * P * z)
R4 = sp.expand(
    Xi * X
    + U * Q * (U - V * y) * h
    - U * P * (V * (x + z - y**2) + U * y)
)
R5 = sp.expand(U * Xi * (x - y**2) - A * P * x)
R6 = sp.expand(Xi**2 - A * (P**2 - P * Q * (t + y) + Q**2 * h))
GLOBAL = &#91;R0, R1, R2, R3, R4, R5, R6&#93;
EXPECTED_BIDEGREES = &#91;(1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (2, 1), (2, 2)&#93;

s, r = sp.symbols("s r")
scale = {U: s * U, V: s * V, P: r * P, Q: r * Q, Xi: s * r * Xi}
for poly, (du, dp) in zip(GLOBAL, EXPECTED_BIDEGREES):
    assert sp.expand(poly.xreplace(scale) - s**du * r**dp * poly) == 0
assert sp.Poly(R6, Xi).degree() == 2 and sp.Poly(R6, Xi).LC() == 1
print("seven relations have the declared bidegrees and a monic quadratic: PASS")


# ---------------------------------------------------------------------------
# U=P=1: finite--finite chart
# ---------------------------------------------------------------------------
section("U=P=1 finite--finite chart")
lam, rho, T, w = sp.symbols("lambda rho T w")
t_ff = T + lam * z
alpha = 1 - T * lam
u = T * y + z
xi = x - y**2
v = u + alpha * x
f0_ff = x * z
g0_ff = x * t_ff + y * z
h_ff = x + z + t_ff * y
f1_ff = (x - y**2) * h_ff
g1_ff = x * t_ff + y * z + 2 * x * y - y**3
F0 = sp.expand(T * x + y * z)
F1 = sp.expand(w * u - alpha * z)
F2 = sp.expand(w * xi - alpha * x)
F3 = sp.expand(rho * v - lam * z - (w + 1) * y)
F4 = sp.expand(w**2 - alpha * (1 - T * rho + rho * w * y))
FF = &#91;F0, F1, F2, F3, F4&#93;
GLOBAL_FF = &#91;
    sp.expand(f.subs({U: 1, P: 1, V: lam, Q: rho, Xi: w, t: t_ff}))
    for f in GLOBAL
&#93;
ideal_equal(GLOBAL_FF, FF, &#91;w, rho, lam, T, x, y, z&#93;, "finite--finite chart")

# The first six bihomogeneous relations (R0,...,R4,R6) are the closure
# obtained from the V-chart.  On the U=P=1 chart they are strictly too weak
# along V=lambda=0.  Saturating by lambda adds precisely R5.
GLOBAL_FF_WITHOUT_R5 = &#91;GLOBAL_FF&#91;i&#93; for i in (0, 1, 2, 3, 4, 6)&#93;
gb_without_r5 = sp.groebner(
    GLOBAL_FF_WITHOUT_R5, w, rho, lam, T, x, y, z, order="lex"
)
assert gb_without_r5.reduce(GLOBAL_FF&#91;5&#93;)&#91;1&#93; != 0
SAT_WITHOUT_R5 = eliminated_saturation(
    GLOBAL_FF_WITHOUT_R5,
    lam,
    &#91;w, rho, lam, T, x, y, z&#93;,
)
ideal_equal(
    SAT_WITHOUT_R5,
    GLOBAL_FF,
    &#91;w, rho, lam, T, x, y, z&#93;,
    "missing U-chart saturation relation",
)

I_FF = eliminated_saturation(
    &#91;F0, sp.expand(g1_ff - rho * f1_ff)&#93;,
    f0_ff * f1_ff,
    &#91;rho, lam, T, x, y, z&#93;,
)
E_FF = eliminate_one(FF, w, &#91;rho, lam, T, x, y, z&#93;)
ideal_equal(I_FF, E_FF, &#91;rho, lam, T, x, y, z&#93;, "finite--finite image")
print("global chart equals the known finite normalization and its saturated image: PASS")


# ---------------------------------------------------------------------------
# U=Q=1: second-projective infinity
# ---------------------------------------------------------------------------
section("U=Q=1 second-projective-infinity chart")
theta, omega = sp.symbols("theta omega")
G0 = F0
G1 = sp.expand(omega * u - alpha * theta * z)
G2 = sp.expand(omega * xi - alpha * theta * x)
G3 = sp.expand(v - lam * theta * z - (omega + theta) * y)
G4 = sp.expand(omega**2 - alpha * (theta**2 - T * theta + omega * y))
UQ = &#91;G0, G1, G2, G3, G4&#93;
GLOBAL_UQ = &#91;
    sp.expand(f.subs({U: 1, Q: 1, V: lam, P: theta, Xi: omega, t: t_ff}))
    for f in GLOBAL
&#93;
ideal_equal(GLOBAL_UQ, UQ, &#91;omega, theta, lam, T, x, y, z&#93;, "second-infinity chart")

I_UQ = eliminated_saturation(
    &#91;F0, sp.expand(f1_ff - theta * g1_ff)&#93;,
    f0_ff * g1_ff,
    &#91;theta, lam, T, x, y, z&#93;,
)
E_UQ = eliminate_one(UQ, omega, &#91;theta, lam, T, x, y, z&#93;)
ideal_equal(I_UQ, E_UQ, &#91;theta, lam, T, x, y, z&#93;, "second-infinity image")

# These contractions make the domain argument fail-closed: localization at
# theta is the finite--finite normalization, while localization at T is the
# previously established second-infinity normalization.
SAT_UQ_THETA = eliminated_saturation(
    UQ, theta, &#91;omega, theta, lam, T, x, y, z&#93;
)
ideal_equal(
    SAT_UQ_THETA,
    UQ,
    &#91;omega, theta, lam, T, x, y, z&#93;,
    "second-infinity theta saturation",
)
SAT_UQ_T = eliminated_saturation(UQ, T, &#91;omega, theta, lam, T, x, y, z&#93;)
ideal_equal(
    SAT_UQ_T,
    UQ,
    &#91;omega, theta, lam, T, x, y, z&#93;,
    "second-infinity T saturation",
)

# Hilbert--Burch model near T=theta=0.
B = T * (1 - lam * theta) - alpha * y
rr = omega - alpha * theta
qq = omega + theta - T
M = sp.Matrix(&#91;&#91;B, T * y, rr&#93;, &#91;qq, z, -omega&#93;&#93;)
minors = &#91;
    sp.expand(M&#91;:, &#91;0, 1&#93;&#93;.det()),
    sp.expand(M&#91;:, &#91;0, 2&#93;&#93;.det()),
    sp.expand(M&#91;:, &#91;1, 2&#93;&#93;.det()),
&#93;
assert sp.expand(minors&#91;0&#93; - (T * G3 - alpha * G0)) == 0
assert sp.expand(minors&#91;1&#93; + G4) == 0
assert sp.expand(minors&#91;2&#93; + G1) == 0
assert sp.expand(
    (omega - alpha * theta) * G3
    - ((1 - lam * theta) * G1 + alpha * G2 - y * G4)
) == 0
assert sp.gcd(G1, G4) == 1

# Exact central-fiber decomposition.
y0, z0, o0, l0 = sp.symbols("y0 z0 o0 l0")
central = &#91;y0 * z0, o0 * z0, o0 * (o0 - y0)&#93;
central_primes = &#91;&#91;y0, o0&#93;, &#91;z0, o0&#93;, &#91;z0, o0 - y0&#93;&#93;
inter = ideal_intersection(central_primes&#91;0&#93;, central_primes&#91;1&#93;, &#91;o0, y0, z0, l0&#93;)
inter = ideal_intersection(inter, central_primes&#91;2&#93;, &#91;o0, y0, z0, l0&#93;)
ideal_equal(inter, central, &#91;o0, y0, z0, l0&#93;, "second-infinity central fiber")
print(
    "saturated image, theta/T contractions, height-two determinantal input, "
    "and central fiber: PASS"
)


# ---------------------------------------------------------------------------
# V=P=1: first-projective infinity
# ---------------------------------------------------------------------------
section("V=P=1 first-projective-infinity chart")
eta, psi, rho2 = sp.symbols("eta psi rho2")
Aeta = eta**2 + z - eta * t
Xeta = x - eta * y
K0 = sp.expand(eta * g0 - f0)
K1 = sp.expand(g1 - rho2 * f1)
K2 = sp.expand(z + eta * y + psi * y - eta * rho2 * h)
K3 = sp.expand(psi * z - (z - eta * t) * (rho2 * h - y) - eta * z)
K4 = sp.expand(
    psi * Xeta
    + eta * rho2 * (eta - y) * h
    - eta * (x + z + eta * y - y**2)
)
K5 = sp.expand(psi**2 - Aeta * (1 - rho2 * (t + y) + rho2**2 * h))
VP = &#91;K0, K1, K2, K3, K4, K5&#93;
GLOBAL_VP = &#91;
    sp.expand(f.subs({V: 1, P: 1, U: eta, Q: rho2, Xi: psi}))
    for f in GLOBAL
&#93;
ideal_equal(GLOBAL_VP, VP, &#91;psi, rho2, t, y, x, z, eta&#93;, "first-infinity chart")

I_VP = eliminated_saturation(
    &#91;K0, K1&#93;,
    g0 * f1,
    &#91;rho2, t, y, x, z, eta&#93;,
)
E_VP = eliminate_one(VP, psi, &#91;rho2, t, y, x, z, eta&#93;)
ideal_equal(I_VP, E_VP, &#91;rho2, t, y, x, z, eta&#93;, "first-infinity image")

SAT_VP = eliminated_saturation(VP, eta, &#91;psi, rho2, t, y, x, z, eta&#93;)
ideal_equal(SAT_VP, VP, &#91;psi, rho2, t, y, x, z, eta&#93;, "first-infinity eta saturation")

EA = sp.expand((g1 - rho2 * f1).subs(z, 0))
LB = sp.expand(rho2 * y * (t - psi) - (psi + y))
PA = &#91;z, psi, EA&#93;
PB = &#91;x, z + psi * y, LB&#93;
VP0 = &#91;sp.expand(f.subs(eta, 0)) for f in VP&#93;
inter = ideal_intersection(PA, PB, &#91;psi, rho2, t, y, x, z&#93;)
ideal_equal(inter, VP0, &#91;psi, rho2, t, y, x, z&#93;, "first-infinity eta fiber")
assert sp.gcd((x - y**2) * (x + t * y), x * t + 2 * x * y - y**3) == 1
assert sp.gcd(y * (t - psi), psi + y) == 1
print("saturated image, eta contraction, and reduced two-prime fiber: PASS")


# ---------------------------------------------------------------------------
# V=Q=1: double infinity
# ---------------------------------------------------------------------------
section("V=Q=1 double-infinity chart")
chi, theta2 = sp.symbols("chi theta2")
L0 = K0
L1 = sp.expand(theta2 * g1 - f1)
L2 = sp.expand(theta2 * (z + eta * y) + chi * y - eta * h)
L3 = sp.expand(chi * z - (z - eta * t) * (h - theta2 * y) - eta * theta2 * z)
L4 = sp.expand(
    chi * Xeta
    + eta * (eta - y) * h
    - eta * theta2 * (x + z + eta * y - y**2)
)
L5 = sp.expand(chi**2 - Aeta * (theta2**2 - theta2 * (t + y) + h))
VQ = &#91;L0, L1, L2, L3, L4, L5&#93;
GLOBAL_VQ = &#91;
    sp.expand(f.subs({V: 1, Q: 1, U: eta, P: theta2, Xi: chi}))
    for f in GLOBAL
&#93;
ideal_equal(GLOBAL_VQ, VQ, &#91;chi, theta2, t, y, x, z, eta&#93;, "double-infinity chart")

I_VQ = eliminated_saturation(
    &#91;K0, L1&#93;,
    g0 * g1,
    &#91;theta2, t, y, x, z, eta&#93;,
)
E_VQ = eliminate_one(VQ, chi, &#91;theta2, t, y, x, z, eta&#93;)
ideal_equal(I_VQ, E_VQ, &#91;theta2, t, y, x, z, eta&#93;, "double-infinity image")

SAT_VQ_ETA = eliminated_saturation(VQ, eta, &#91;chi, theta2, t, y, x, z, eta&#93;)
ideal_equal(SAT_VQ_ETA, VQ, &#91;chi, theta2, t, y, x, z, eta&#93;, "double-infinity eta saturation")
SAT_VQ_THETA = eliminated_saturation(VQ, theta2, &#91;chi, theta2, t, y, x, z, eta&#93;)
ideal_equal(SAT_VQ_THETA, VQ, &#91;chi, theta2, t, y, x, z, eta&#93;, "double-infinity theta saturation")

f1z = sp.expand(f1.subs(z, 0))
g1z = sp.expand(g1.subs(z, 0))
AQ = &#91;z, chi, sp.expand(theta2 * g1z - f1z)&#93;
BQ = &#91;
    x,
    sp.expand(chi - z - y * (t - theta2)),
    sp.expand((t - theta2) * y**2 + z * (theta2 + y)),
&#93;
VQ0 = &#91;sp.expand(f.subs(eta, 0)) for f in VQ&#93;
inter = ideal_intersection(AQ, BQ, &#91;chi, theta2, t, y, x, z&#93;)
ideal_equal(inter, VQ0, &#91;chi, theta2, t, y, x, z&#93;, "double-infinity eta fiber")
assert sp.gcd(f1z, g1z) == 1
assert sp.gcd(z - y**2, y * (t * y + z)) == 1

C1 = &#91;x, y, z - chi&#93;
C2 = &#91;chi, x, z + t * y&#93;
C3 = &#91;chi, z, x - y**2&#93;
C4 = &#91;chi, z, x + t * y&#93;
inter4 = ideal_intersection(C1, C2, &#91;chi, t, y, x, z&#93;)
inter4 = ideal_intersection(inter4, C3, &#91;chi, t, y, x, z&#93;)
inter4 = ideal_intersection(inter4, C4, &#91;chi, t, y, x, z&#93;)
VQ00 = &#91;sp.expand(f.subs({eta: 0, theta2: 0})) for f in VQ&#93;
ideal_equal(inter4, VQ00, &#91;chi, t, y, x, z&#93;, "double-infinity corner fiber")
print("saturated image, two-prime eta fiber, and four-component corner: PASS")


# ---------------------------------------------------------------------------
# Global conductor cover and transition functions
# ---------------------------------------------------------------------------
section("global O(1,1) conductor cover")
GLOBAL_CONDUCTOR = sp.expand(R6.subs({x: 0, y: 0, z: 0}))
EXPECTED_GLOBAL_CONDUCTOR = sp.expand(
    Xi**2 - U * (U - t * V) * P * (P - t * Q)
)
assert GLOBAL_CONDUCTOR == EXPECTED_GLOBAL_CONDUCTOR

# Local conductor equations obtained directly from the chart quadratics.
cond_FF = sp.expand(F4.subs({x: 0, y: 0, z: 0}))
cond_UQ = sp.expand(G4.subs({x: 0, y: 0, z: 0}))
cond_VP = sp.expand(K5.subs({x: 0, y: 0, z: 0}))
cond_VQ = sp.expand(L5.subs({x: 0, y: 0, z: 0}))
assert cond_FF == sp.expand(w**2 - (1 - T * lam) * (1 - T * rho))
assert cond_UQ == sp.expand(omega**2 - (1 - T * lam) * theta * (theta - T))
assert cond_VP == sp.expand(psi**2 - eta * (eta - t) * (1 - rho2 * t))
assert cond_VQ == sp.expand(chi**2 - eta * (eta - t) * theta2 * (theta2 - t))

# Transition identities after clearing denominators.
assert sp.expand(
    rho**2 * cond_UQ.subs({theta: 1 / rho, omega: w / rho}) - cond_FF
) == 0
assert sp.expand(
    lam**2 * cond_VP.subs({eta: 1 / lam, psi: w / lam, t: T, rho2: rho})
    - cond_FF.subs(z, 0)
) == 0
assert sp.expand(
    rho2**2 * cond_VQ.subs({theta2: 1 / rho2, chi: psi / rho2}) - cond_VP
) == 0
print("Xi transforms as O(1,1) and the four conductor equations glue: PASS")

print("\nALL BIHOMOGENEOUS A0 CHECKS PASSED")
</code></pre>

<a id="source-05a87f7e3f84a817"></a>

## `research-notes/lane2-projective-normalization-20260803-v1/verify_conductor_module.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independent module-Groebner conductor audit for Lane-2 A0.

For each of the four affine charts this program computes B/A as a cyclic
module and obtains its annihilator via SymPy's AGCA module-quotient algorithm.
This is a different computation from checking that the displayed linear
relations are multiples of (x,y,z).

The general input is
    B = S&#91;zeta&#93;/(I, zeta^2-c1*zeta-c0, a_i+b_i*zeta).
After adjoining the multiplication-by-zeta transforms of the linear
relations, B/A is represented as a quotient of a free S-module of rank two.
The module quotient computes Ann_S(B/A) exactly.
"""
from __future__ import annotations

import sympy as sp
from sympy import QQ


def eliminate_one(gens, variable, remaining):
    gb = sp.groebner(gens, variable, *remaining, order="lex")
    return &#91;sp.expand(p.as_expr()) for p in gb.polys if not p.as_expr().has(variable)&#93;


def ideal_equal(gens_a, gens_b, variables, label):
    ga = sp.groebner(gens_a, *variables, order="lex")
    gb = sp.groebner(gens_b, *variables, order="lex")
    assert all(ga.reduce(sp.expand(f))&#91;1&#93; == 0 for f in gens_b), f"{label}: B not in A"
    assert all(gb.reduce(sp.expand(f))&#91;1&#93; == 0 for f in gens_a), f"{label}: A not in B"


def audit_chart(name, zeta, basevars, Bgens, linear, c0, c1, conductor_gens):
    print(f"\n&#91;{name}&#93;")
    I = eliminate_one(Bgens, zeta, basevars)

    # Confirm that the normalization ideal is generated by the eliminated
    # base ideal, the displayed linear relations, and the monic quadratic.
    displayed = &#91;*I, *(sp.expand(a + b * zeta) for a, b in linear), sp.expand(zeta**2 - c1 * zeta - c0)&#93;
    ideal_equal(Bgens, displayed, &#91;zeta, *basevars&#93;, f"{name} displayed presentation")

    R = QQ.old_poly_ring(*basevars)
    F = R.free_module(2)

    def cv(expr):
        return R.convert(sp.expand(expr))

    cc0, cc1 = cv(c0), cv(c1)

    # Relations for the S-module B with basis (1,zeta), followed by killing
    # the A-summand generated by 1.  Multiplication by zeta sends
    # (a,b) to (b*c0, a+b*c1).
    relations = &#91;&#91;1, 0&#93;&#93;
    for f in I:
        relations.append(&#91;0, cv(f)&#93;)
    for a, b in linear:
        aa, bb = cv(a), cv(b)
        relations.append(&#91;aa, bb&#93;)
        relations.append(&#91;bb * cc0, aa + bb * cc1&#93;)

    N = F.submodule(*relations, order="lex", TOP=True)
    zeta_submodule = F.submodule(&#91;0, 1&#93;)
    annihilator = N.module_quotient(zeta_submodule)
    expected = R.ideal(*&#91;cv(f) for f in I&#93;, *&#91;cv(g) for g in conductor_gens&#93;)
    bare_conductor = R.ideal(*&#91;cv(g) for g in conductor_gens&#93;)
    assert expected == bare_conductor
    assert annihilator == bare_conductor

    print(f"elimination generators: {len(I)}")
    print("module quotient annihilator: (x,y,z)")
    print("conductor audit: PASS")


# ---------------------------------------------------------------------------
# U=P=1
# ---------------------------------------------------------------------------
w, rho, lam, T, x, y, z = sp.symbols("w rho lambda T x y z")
t_ff = T + lam * z
h_ff = x + z + t_ff * y
alpha = 1 - T * lam
u = T * y + z
xi = x - y**2
v = u + alpha * x
F0 = T * x + y * z
linear_FF = &#91;
    (-alpha * z, u),
    (-alpha * x, xi),
    (rho * v - lam * z - y, -y),
&#93;
c0_FF = alpha * (1 - T * rho)
c1_FF = alpha * rho * y
B_FF = &#91;
    F0,
    *(sp.expand(a + b * w) for a, b in linear_FF),
    sp.expand(w**2 - c1_FF * w - c0_FF),
&#93;
audit_chart(
    "U=P=1 finite--finite",
    w,
    &#91;rho, lam, T, x, y, z&#93;,
    B_FF,
    linear_FF,
    c0_FF,
    c1_FF,
    &#91;x, y, z&#93;,
)


# ---------------------------------------------------------------------------
# U=Q=1
# ---------------------------------------------------------------------------
omega, theta = sp.symbols("omega theta")
linear_UQ = &#91;
    (-alpha * theta * z, u),
    (-alpha * theta * x, xi),
    (v - lam * theta * z - theta * y, -y),
&#93;
c0_UQ = alpha * theta * (theta - T)
c1_UQ = alpha * y
B_UQ = &#91;
    F0,
    *(sp.expand(a + b * omega) for a, b in linear_UQ),
    sp.expand(omega**2 - c1_UQ * omega - c0_UQ),
&#93;
audit_chart(
    "U=Q=1 second infinity",
    omega,
    &#91;theta, lam, T, x, y, z&#93;,
    B_UQ,
    linear_UQ,
    c0_UQ,
    c1_UQ,
    &#91;x, y, z&#93;,
)


# ---------------------------------------------------------------------------
# V=P=1
# ---------------------------------------------------------------------------
psi, eta, rho2, t = sp.symbols("psi eta rho2 t")
h = x + z + t * y
f0 = x * z
g0 = x * t + y * z
f1 = (x - y**2) * h
g1 = x * t + y * z + 2 * x * y - y**3
Aeta = eta**2 + z - eta * t
Xeta = x - eta * y
K0 = eta * g0 - f0
K1 = g1 - rho2 * f1
linear_VP = &#91;
    (z + eta * y - eta * rho2 * h, y),
    (-(z - eta * t) * (rho2 * h - y) - eta * z, z),
    (
        eta * rho2 * (eta - y) * h
        - eta * (x + z + eta * y - y**2),
        Xeta,
    ),
&#93;
c0_VP = Aeta * (1 - rho2 * (t + y) + rho2**2 * h)
c1_VP = sp.Integer(0)
B_VP = &#91;
    K0,
    K1,
    *(sp.expand(a + b * psi) for a, b in linear_VP),
    sp.expand(psi**2 - c0_VP),
&#93;
audit_chart(
    "V=P=1 first infinity",
    psi,
    &#91;rho2, t, y, x, z, eta&#93;,
    B_VP,
    linear_VP,
    c0_VP,
    c1_VP,
    &#91;x, y, z&#93;,
)


# ---------------------------------------------------------------------------
# V=Q=1
# ---------------------------------------------------------------------------
chi, theta2 = sp.symbols("chi theta2")
linear_VQ = &#91;
    (theta2 * (z + eta * y) - eta * h, y),
    (-(z - eta * t) * (h - theta2 * y) - eta * theta2 * z, z),
    (
        eta * (eta - y) * h
        - eta * theta2 * (x + z + eta * y - y**2),
        Xeta,
    ),
&#93;
c0_VQ = Aeta * (theta2**2 - theta2 * (t + y) + h)
c1_VQ = sp.Integer(0)
B_VQ = &#91;
    K0,
    theta2 * g1 - f1,
    *(sp.expand(a + b * chi) for a, b in linear_VQ),
    sp.expand(chi**2 - c0_VQ),
&#93;
audit_chart(
    "V=Q=1 double infinity",
    chi,
    &#91;theta2, t, y, x, z, eta&#93;,
    B_VQ,
    linear_VQ,
    c0_VQ,
    c1_VQ,
    &#91;x, y, z&#93;,
)

print("\nALL MODULE-GROEBNER CONDUCTOR CHECKS PASSED")
</code></pre>

<a id="source-26cddbd8db58d696"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_exact_ordered_outer_resolution.md`

<pre><code class="language-markdown">
# Exact ordered resolution of the quintic outer-pair graph

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact symbolic replay supplied.
&gt; **Scope:** characteristic zero, or more generally a field in which `2` and the
&gt; translation parameter below are units.  The theorem is formal/étale-local
&gt; along the deepest quintic middle-graph fiber and covers the affine chart of
&gt; the first projective outer direction.  It proves an exact higher-order
&gt; resolution theorem for the ordered graph.  It does not identify that ordered
&gt; model with the normalization of the unordered simultaneous multi-Rees graph,
&gt; and it does not address the unique degenerate first-direction chart at
&gt; projective infinity.

## 1. Universal outer pair

Let

\&#91;
R=k&#91;x,y,z,t&#93;
\&#93;

and put

\&#91;
J_0=(f_0,g_0)
=(xz,\ yz+xt).
\&#93;

Consider the locally nilpotent derivation

\&#91;
\partial
=-y^2\partial_x+y\partial_t+(x+yt)\partial_z.
\&#93;

For a unit \(s\in k^\times\), its time-\(s\) map is

\&#91;
\tau_s=\exp(s\partial),
\&#93;

\&#91;
\tau_s(x,y,z,t)
=
(x-sy^2,\ y,\ z+s(x+yt),\ t+sy).
\&#93;

Set

\&#91;
J_s=\tau_s(J_0)=(f_s,g_s).
\&#93;

A direct expansion gives

\&#91;
f_s=(x-sy^2)(z+sx+syt),
\&#93;

\&#91;
g_s=xt+yz+2sxy-s^2y^3.
\&#93;

The actual quintic pair from the middle \(\mathsf Z\)-chart is the case
\(s=1\): under

\&#91;
(x,y,z,t)=(C,D,u,v),
\&#93;

the top factor is

\&#91;
&#91;Cu:Du+Cv&#93;=&#91;f_0:g_0&#93;,
\&#93;

while the bottom factor is

\&#91;
&#91;(C-D^2)(u+C+Dv):D(u+C+Dv)+(C-D^2)(v+D)&#93;
=&#91;f_1:g_1&#93;.
\&#93;

Thus the theorem below applies verbatim to the full higher-order quintic
outer pair, not merely to its quadratic initial forms.

## 2. First graph and its finite-direction node

Let \(&#91;P_0:Q_0&#93;\) be the first projective direction.  On the affine chart
\(P_0\ne0\), put

\&#91;
\lambda=Q_0/P_0.
\&#93;

The graph of \(&#91;f_0:g_0&#93;\) is

\&#91;
g_0-\lambda f_0=0.
\&#93;

After the exact change

\&#91;
T=t-\lambda z,
\&#93;

this is

\&#91;
\boxed{xT+yz=0.}
\&#93;

Choose the small resolution obtained by blowing up the rank-one ideal
\((x,y)\).  It has two standard affine charts.

### Chart A

\&#91;
y=ax,
\qquad
T=-az.
\&#93;

Its coordinates are \((x,z,a,\lambda)\).

### Chart B

\&#91;
x=by,
\qquad
z=-bT.
\&#93;

Its coordinates are \((b,y,T,\lambda)\).

Both charts are affine four-space, so the first graph has been resolved
exactly on the finite-direction locus.

## 3. Exact monomialization on Chart A

Pull \(J_s\) to Chart A.  Substituting

\&#91;
y=ax,
\qquad
T=-az,
\qquad
 t=T+\lambda z=(\lambda-a)z
\&#93;

gives

\&#91;
f_s=xU F,
\qquad
g_s=xG,
\&#93;

where

\&#91;
U=1-a^2sx,
\&#93;

\&#91;
F=sx+z+as(\lambda-a)xz,
\&#93;

\&#91;
G=\lambda z+2asx-a^3s^2x^2.
\&#93;

The factor \(x\) is a common Cartier factor and \(U\) is a unit near the
exceptional fiber.  Hence the weak projective map is equivalent to

\&#91;
&#91;F:G&#93;.
\&#93;

Put

\&#91;
c=as(\lambda-a),
\qquad
Z=F=sx+(1+cx)z.
\&#93;

Since \(1+cx\) is a unit, \(Z\) is a regular coordinate replacing \(z\).
Define

\&#91;
H=
(2as-a^3s^2x)(1+cx)-s\lambda.
\&#93;

Then the following exact identity holds:

\&#91;
(1+cx)G-\lambda Z=xH.
\&#93;

Consequently

\&#91;
\boxed{(F,G)=(Z,xH)}
\&#93;

in the completed or étale local ring.

The coordinate change is nonsingular because

\&#91;
\frac{\partial H}{\partial\lambda}
=-s(1-a^2sx)^2=-sU^2,
\&#93;

which is a unit.  Therefore

\&#91;
(a,x,Z,H)
\&#93;

are étale coordinates.

This is the key higher-order statement: no uncomputed terms remain.  The weak
second ideal is exactly the monomial complete intersection

\&#91;
(Z,xH).
\&#93;

## 4. Exact residual conifold

Because \(Z,xH\) form a regular sequence, their Rees algebra is the symmetric
algebra.  Thus the second graph is cut out by one bilinear relation.

On the projective chart in which the relation has affine coordinate \(r\), it
is

\&#91;
\boxed{rZ=xH.}
\&#93;

The complementary projective chart is smooth because its equation can be
solved for \(Z\).  The displayed chart is the threefold ordinary double point

\&#91;
rZ-xH=0
\&#93;

times the smooth parameter \(a\).

Its reduced singular locus is

\&#91;
\Sigma_{\mathrm{node}}
=V(r,Z,x,H),
\&#93;

with \(a\) free.

There are two projective small resolutions.

### First small resolution

Blow up \((x,Z)\).  The strict-transform charts are

\&#91;
Z=x\zeta,
\qquad
H=r\zeta,
\&#93;

and

\&#91;
x=Z\xi,
\qquad
r=\xi H.
\&#93;

Both are affine four-space.

### Second small resolution

Blow up \((x,r)\).  The strict-transform charts are

\&#91;
r=x\rho,
\qquad
H=\rho Z,
\&#93;

and

\&#91;
x=r\xi,
\qquad
Z=\xi H.
\&#93;

Again both are affine four-space.  The two small resolutions are related by
the ordinary Atiyah flop, fiberwise over the parameter \(a\).  In particular,
the conifold step is crepant.

This proves that the finite-\(a\) part of the full higher-order ordered graph
is resolved by the same toric subdivision predicted by the quadratic normal
model.

## 5. The projective boundary of the first small resolution

Chart A does not contain the point \(a=\infty\) of the exceptional
\(\mathbb P^1\).  Chart B treats that point.

Substituting

\&#91;
x=by,
\qquad
z=-bT,
\qquad
t=T(1-\lambda b)
\&#93;

gives

\&#91;
f_s=yF_B,
\qquad
g_s=yG_B,
\&#93;

where

\&#91;
F_B=(-b+sy)
\bigl(Tb\lambda sy+Tb-Tsy-bsy\bigr),
\&#93;

\&#91;
G_B=-\bigl(Tb^2\lambda-2bsy+s^2y^2\bigr).
\&#93;

Again the common Cartier factor \(y\) is removed.  The remaining rational map
is \(&#91;F_B:G_B&#93;\).

The graph has a codimension-one nonnormal-looking boundary over
\(b=y=0\).  Blow up the ideal

\&#91;
(b,sy)=(b,y).
\&#93;

The calculation becomes independent of \(s\).

### The \(b\)-chart

Put

\&#91;
sy=kb.
\&#93;

After removing the common factor \(b^2\), the transformed pair is

\&#91;
F_k=(k-1)
\bigl(Tbk\lambda-Tk+T-bk\bigr),
\&#93;

\&#91;
G_k=-T\lambda-k^2+2k.
\&#93;

Write

\&#91;
q=k-1,
\qquad
\alpha=1-T\lambda.
\&#93;

Then

\&#91;
G_k=\alpha-q^2,
\&#93;

\&#91;
F_k=-Tq^2-bq(q+1)\alpha.
\&#93;

Let \(&#91;P_1:Q_1&#93;\) be the second projective direction.  The strict graph is

\&#91;
P_1G_k-Q_1F_k=0.
\&#93;

#### Finite second direction

On \(P_1\ne0\), put \(\mu=Q_1/P_1\).  The equation is

\&#91;
\boxed{
\alpha+(T\mu-1)q^2
+b\mu q(q+1)\alpha=0.
}
\&#93;

Above the exceptional divisor \(b=0\), this chart is smooth:

- if \(T\ne0\), the derivative with respect to \(\lambda\) is \(-T\);
- if \(T=0\), the equation forces \(q=\pm1\), and the derivative with respect
  to \(q\) is nonzero.

A direct Jacobian calculation in the original coordinates
\((b,k,T,\lambda,\mu)\) shows that the only singular component on this
chart is

\&#91;
k=0,\qquad T=0,\qquad \mu=\lambda,\qquad b\lambda=2.
\&#93;

This is exactly the residual conifold locus from Chart A, written on the
overlap.  In particular it does not meet \(b=0\) in the finite
\(\lambda\)-chart.

For completeness, the case reduction is short.  At a singular point,
\(\partial_\mu E=0\) and \(E=0\) give \(F_k=G_k=0\), hence
\(T\lambda=k(2-k)\).  The \(b\)-derivative becomes
\(k\mu(k-1)^3\).  The case \(k=1\) is excluded by the \(\lambda\)-derivative,
while \(k\notin\{0,1\}\) forces \(\mu=T=0\), then \(k=2\), which is excluded
by the \(k\)-derivative.  Thus \(k=0\); the remaining derivatives give exactly
\(T=0\), \(\mu=\lambda\), and \(b\lambda=2\).

#### Infinite second direction

On \(Q_1\ne0\), put \(\theta=P_1/Q_1\).  The equation is

\&#91;
E=
\theta(\alpha-q^2)
+Tq^2+bq(q+1)\alpha.
\&#93;

A direct Jacobian calculation gives two disjoint singular components.
The first is the same conifold component as above:

\&#91;
k=0,\qquad T=0,\qquad \lambda\theta=1,\qquad b=2\theta.
\&#93;

The second is the genuinely new boundary component

\&#91;
q=0,\qquad \alpha=0,\qquad \theta=0,
\&#93;

with \((b,T)\) free.  On the second component \(T\lambda=1\), so
\(T\) is a unit.  The two components are disjoint because the conifold has
\(k=0\), whereas the new component has \(k=1\).

Indeed, at a singular point \(F_k=G_k=0\), and the \(b\)-derivative is
\(k(k-1)^3\).  Thus \(k=0\) or \(k=1\).  The first case gives the displayed
conifold component.  The second gives \(T\lambda=1\), and the
\(\lambda\)-derivative then forces \(\theta=0\); all remaining derivatives
vanish.  No other cases occur.

Near the new component, set

\&#91;
\Theta=\theta+bq(q+1),
\&#93;

\&#91;
W=T-\Theta+bq(q+1).
\&#93;

Then \(W\) is a unit and

\&#91;
E=\alpha\Theta+Wq^2.
\&#93;

Replacing \(\alpha\) by

\&#91;
A=\alpha/W
\&#93;

gives the exact normal form

\&#91;
\boxed{A\Theta+q^2=0}
\&#93;

times the smooth parameters \((b,T)\).

Thus the only new boundary singularity is a family of du Val \(A_1\)
surface singularities.  Blowing up its singular locus

\&#91;
V(A,\Theta,q)
\&#93;

resolves it.  The three strict-transform charts are

\&#91;
\Theta_1+q_1^2=0,
\qquad
A_1+q_1^2=0,
\qquad
A_1\Theta_1+1=0,
\&#93;

and are all smooth.  Fiberwise, this is the crepant minimal resolution of the
\(A_1\) singularity.

### The \(y\)-chart

Put

\&#91;
b=\ell sy.
\&#93;

After removing the common factor \(s^2y^2\), one obtains

\&#91;
F_\ell
=-(\ell-1)
\bigl(T\ell\lambda sy+T\ell-T-\ell sy\bigr),
\&#93;

\&#91;
G_\ell=-T\ell^2\lambda+2\ell-1.
\&#93;

At \(\ell=0\), the second generator is \(-1\).  Hence the rational map
extends regularly and the graph is smooth there.  This completes the analysis
of the projective boundary of the first small resolution.

## 6. Main theorem

### Theorem 6.1 — Exact finite-direction ordered resolution

Let \(k\) have characteristic zero and let \(s\in k^\times\).  Start with the
pair

\&#91;
J_0=(xz,yz+xt),
\qquad
J_s=\tau_s(J_0).
\&#93;

Over the affine chart of the first projective direction, perform the following
ordered construction:

1. take the graph of \(J_0\);
2. take the small resolution obtained from the ideal \((x,y)\);
3. form the graph of the weak transform of \(J_s\);
4. blow up the boundary center \((b,y)\) on Chart B;
5. choose either small resolution of the residual conifold
   \(rZ=xH\) on Chart A;
6. blow up the residual \(A_1\)-singular locus
   \(V(A,\Theta,q)\) on the infinite second-direction chart.

The resulting space is smooth.  Every step is projective over the preceding
one, and the composite is birational to the ordered graph and hence to the
simultaneous graph on the locus where both projective maps are defined.

All local equations in the proof are exact polynomial identities after
inverting displayed units.  In particular, this is a full higher-order
resolution theorem, not a tangent-cone or associated-graded statement.

### Proof

Chart A is transformed exactly to the complete-intersection ideal
\((Z,xH)\).  Its graph is smooth except for the conifold family
\(rZ=xH\), and either displayed small resolution resolves that family.

On Chart B, blowing up \((b,y)\) gives the two explicit transformed pairs in
Section 5.  The \(\ell\)-chart is regular because \(G_\ell\) is a unit at the
missing projective point.  On the \(k\)-chart, the finite second-direction
chart is smooth over the new exceptional divisor and agrees away from it with
Chart A.  The infinite second-direction chart has exactly the displayed
\(A_1\) family, whose blowup is smooth.  The conifold center and the boundary \(A_1\) center are disjoint
(they have \(k=0\) and \(k=1\), respectively), so their resolutions are
compatible.  The formulas cover the two charts of the first small resolution
and the two charts of the second projective line. ∎

## 7. Reverse order and birational ambiguity

Applying \(\tau_{-s}\) exchanges the roles of \(J_0\) and \(J_s\).  Hence the
same theorem gives a reverse ordered resolution.

There are two independent conifold choices:

1. the choice of small resolution of the first graph node;
2. the choice of small resolution of the exact residual conifold.

Changing either choice is a family Atiyah flop.  The boundary \(A_1\)
resolution is canonical.  Thus, on the finite-direction locus, the entire
order-dependent birational ambiguity is accounted for by two ordinary flop
choices, exactly as suggested by the five-ray quadratic fan.

This conclusion is local.  Identifying a particular global ordered
multi-Rees construction with a particular pair of flop choices still requires
line-bundle and projective-coordinate bookkeeping.

## 8. Quintic corollary

### Corollary 8.1

On the \(\mathsf Z\)-chart of the actual \((m,\nu)=(5,5)\) middle PRS graph,
the ordered graph of the two outer projective subresultant factors admits the
smooth exact resolution of Theorem 6.1.

### Proof

Use

\&#91;
(x,y,z,t)=(C,D,u,v).
\&#93;

The top pair is \(J_0\), and the bottom pair is \(\tau_1(J_0)\), as verified
in Section 1. ∎

## 9. What this proves and what remains

The theorem proves that the quartic toric normal model genuinely lifts to the
full higher-order quintic **ordered** graph on the finite first-direction
locus.  The prior obstruction was therefore not a hidden higher-order term in
this chart.

The remaining local tasks are narrower:

- analyze the degenerate first projective direction, where the individual
  graph has the toric chart \(XZ=\eta^2yt\);
- compare the two ordered resolutions with the normalization and Stein
  factorization of the unordered simultaneous multi-Rees graph;
- identify the exact global fan and line-bundle characters;
- extend the relative-Jacobian ideals through the displayed centers.
</code></pre>

<a id="source-e5195063ad85c860"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_exact_ordered_outer_resolution_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact symbolic replay for the universal outer graph and ordered resolution.

All identities are over ZZ&#91;s&#93; and hence hold whenever s is a unit.  Smoothness
claims are verified by the displayed coordinate eliminations, not numerical
sampling.
"""
from __future__ import annotations

import sympy as sp

x, y, z, t = sp.symbols("x y z t")
T, lam, s = sp.symbols("T lam s")
a, b = sp.symbols("a b")
mu, theta = sp.symbols("mu theta")
k, ell, q = sp.symbols("k ell q")
alpha, Theta, Avar = sp.symbols("alpha Theta Avar")
r = sp.symbols("r")


def tau(poly: sp.Expr, time: sp.Expr) -&gt; sp.Expr:
    """Apply exp(time*delta) to a polynomial by substitution."""
    return sp.expand(
        poly.subs(
            {
                x: x - time * y**2,
                y: y,
                z: z + time * (x + y * t),
                t: t + time * y,
            },
            simultaneous=True,
        )
    )


def main() -&gt; None:
    f0 = x * z
    g0 = y * z + x * t

    # The additive-group action and the exact translated pair.
    u = sp.symbols("u")
    for coord in (x, y, z, t):
        lhs = tau(tau(coord, s), u)
        rhs = tau(coord, s + u)
        assert sp.expand(lhs - rhs) == 0

    fs = sp.factor(tau(f0, s))
    gs = sp.factor(tau(g0, s))
    assert fs == (x - s * y**2) * (z + s * x + s * y * t)
    assert sp.expand(gs - (x * t + y * z + 2 * s * x * y - s**2 * y**3)) == 0

    # First graph: finite-direction node.
    first_eq = sp.expand(g0 - lam * f0)
    node_eq = sp.expand(first_eq.subs(t, T + lam * z))
    assert node_eq == x * T + y * z

    # Unique degenerate projective direction of the individual graph.
    eta, X, Z = sp.symbols("eta X Z")
    inf_eq = sp.expand(eta * g0 - f0)
    # x = X + eta*y, z = Z + eta*t.
    inf_new = sp.expand(inf_eq.subs({x: X + eta * y, z: Z + eta * t}))
    assert inf_new == -(X * Z - eta**2 * y * t)

    # Blow up the infinity plane (X,Z,eta).
    e, Z1, X1 = sp.symbols("e Z1 X1")
    strict_X = sp.expand((X * Z - eta**2 * y * t).subs({Z: X * Z1, eta: X * e}) / X**2)
    assert strict_X == Z1 - e**2 * y * t
    strict_eta = sp.expand((X * Z - eta**2 * y * t).subs({X: eta * X1, Z: eta * Z1}) / eta**2)
    assert strict_eta == X1 * Z1 - y * t

    # Symmetric blowup of an ODP vertex is smooth in each standard chart.
    yy, zz, TT = sp.symbols("yy zz TT")
    strict_node_x = sp.expand((x * T + y * z).subs({T: x * TT, y: x * yy, z: x * zz}) / x**2)
    assert strict_node_x == TT + yy * zz

    # Chart A of the first small resolution: y=a*x, T=-a*z.
    fs_node = sp.expand(fs.subs(t, T + lam * z))
    gs_node = sp.expand(gs.subs(t, T + lam * z))
    fs_A = sp.factor(fs_node.subs({y: a * x, T: -a * z}))
    gs_A = sp.factor(gs_node.subs({y: a * x, T: -a * z}))

    U = 1 - a**2 * s * x
    c = a * s * (lam - a)
    F = s * x + z + c * x * z
    G = lam * z + 2 * a * s * x - a**3 * s**2 * x**2
    assert sp.expand(fs_A - x * U * F) == 0
    assert sp.expand(gs_A - x * G) == 0

    Zcoord = sp.symbols("Zcoord")
    H = (2 * a * s - a**3 * s**2 * x) * (1 + c * x) - s * lam
    assert sp.expand((1 + c * x) * G - lam * F - x * H) == 0
    assert sp.expand(sp.diff(H, lam) + s * U**2) == 0

    # In coordinates Z=F, the exact weak ideal is (Z,xH).
    z_of_Z = (Zcoord - s * x) / (1 + c * x)
    G_in_Z = sp.cancel(G.subs(z, z_of_Z))
    assert sp.factor((1 + c * x) * G_in_Z - lam * Zcoord - x * H) == 0

    # Exact conifold and both small resolutions.
    conifold = r * Zcoord - x * sp.symbols("Hc")
    Hc, zeta, xi, rho = sp.symbols("Hc zeta xi rho")
    conifold = r * Zcoord - x * Hc
    strict_c1 = sp.expand(conifold.subs({Zcoord: x * zeta, Hc: r * zeta}) / x)
    assert strict_c1 == 0
    # Better chart equations before imposing the solved variable.
    assert sp.expand((r * (x * zeta) - x * Hc) / x) == r * zeta - Hc
    assert sp.expand((r * Zcoord - (Zcoord * xi) * Hc) / Zcoord) == r - xi * Hc
    assert sp.expand(((x * rho) * Zcoord - x * Hc) / x) == rho * Zcoord - Hc
    assert sp.expand((r * Zcoord - (r * xi) * Hc) / r) == Zcoord - xi * Hc

    # Chart B of the first small resolution: x=b*y, z=-b*T.
    fs_B = sp.factor(fs_node.subs({x: b * y, z: -b * T}))
    gs_B = sp.factor(gs_node.subs({x: b * y, z: -b * T}))
    FB = (-b + s * y) * (T * b * lam * s * y + T * b - T * s * y - b * s * y)
    GB = -(T * b**2 * lam - 2 * b * s * y + s**2 * y**2)
    assert sp.expand(fs_B - y * FB) == 0
    assert sp.expand(gs_B - y * GB) == 0

    # Blow up (b,s*y), b-chart: s*y=k*b.
    Fk = sp.factor(sp.cancel(FB.subs(y, k * b / s) / b**2))
    Gk = sp.factor(sp.cancel(GB.subs(y, k * b / s) / b**2))
    assert Fk == (k - 1) * (T * b * k * lam - T * k + T - b * k)
    assert Gk == -T * lam - k**2 + 2 * k

    # q=k-1 and alpha=1-T*lam.
    Fq_expected = -T * q**2 - b * q * (q + 1) * alpha
    Gq_expected = alpha - q**2
    assert sp.expand(Fk.subs({k: q + 1, lam: (1 - alpha) / T}) - Fq_expected) == 0
    assert sp.expand(Gk.subs({k: q + 1, lam: (1 - alpha) / T}) - Gq_expected) == 0

    # Finite second projective direction.
    E_mu = sp.expand(Gq_expected - mu * Fq_expected)
    E_mu_expected = alpha + (T * mu - 1) * q**2 + b * mu * q * (q + 1) * alpha
    assert sp.expand(E_mu - E_mu_expected) == 0

    # Exact conifold component in the original (b,k,T,lam,mu) coordinates.
    E_mu_orig = sp.expand(Gk - mu * Fk)
    node_mu_sub = {k: 0, T: 0, mu: lam, b: 2 / lam}
    assert sp.simplify(E_mu_orig.subs(node_mu_sub)) == 0
    for var in (b, k, T, lam, mu):
        assert sp.simplify(sp.diff(E_mu_orig, var).subs(node_mu_sub)) == 0

    # Infinite second projective direction and exact A1 normal form.
    E_theta = sp.expand(theta * Gq_expected - Fq_expected)
    E_theta_expected = theta * (alpha - q**2) + T * q**2 + b * q * (q + 1) * alpha
    assert sp.expand(E_theta - E_theta_expected) == 0

    E_theta_orig = sp.expand(theta * Gk - Fk)
    node_theta_sub = {k: 0, T: 0, theta: 1 / lam, b: 2 / lam}
    assert sp.simplify(E_theta_orig.subs(node_theta_sub)) == 0
    for var in (b, k, T, lam, theta):
        assert sp.simplify(sp.diff(E_theta_orig, var).subs(node_theta_sub)) == 0
    a1_sub = {k: 1, lam: 1 / T, theta: 0}
    assert sp.simplify(E_theta_orig.subs(a1_sub)) == 0
    for var in (b, k, T, lam, theta):
        assert sp.simplify(sp.diff(E_theta_orig, var).subs(a1_sub)) == 0

    Theta_expr = theta + b * q * (q + 1)
    W = T - Theta + b * q * (q + 1)
    E_in_Theta = sp.expand(E_theta_expected.subs(theta, Theta - b * q * (q + 1)))
    assert sp.expand(E_in_Theta - (alpha * Theta + W * q**2)) == 0
    # alpha=Avar*W gives W*(Avar*Theta+q^2).
    assert sp.expand(E_in_Theta.subs(alpha, Avar * W) - W * (Avar * Theta + q**2)) == 0

    # Blowup of the A1 singular locus.
    A1, Th1, q1 = sp.symbols("A1 Th1 q1")
    a1_eq = Avar * Theta + q**2
    strict_A = sp.expand(a1_eq.subs({Theta: Avar * Th1, q: Avar * q1}) / Avar**2)
    strict_Th = sp.expand(a1_eq.subs({Avar: Theta * A1, q: Theta * q1}) / Theta**2)
    strict_q = sp.expand(a1_eq.subs({Avar: q * A1, Theta: q * Th1}) / q**2)
    assert strict_A == Th1 + q1**2
    assert strict_Th == A1 + q1**2
    assert strict_q == A1 * Th1 + 1

    # Blowup (b,s*y), y-chart: b=ell*s*y; the second generator is a unit at ell=0.
    Fell = sp.factor(sp.cancel(FB.subs(b, ell * s * y) / (s**2 * y**2)))
    Gell = sp.factor(sp.cancel(GB.subs(b, ell * s * y) / (s**2 * y**2)))
    assert sp.expand(Fell + (ell - 1) * (T * ell * lam * s * y + T * ell - T - ell * s * y)) == 0
    assert sp.expand(Gell - (-T * ell**2 * lam + 2 * ell - 1)) == 0
    assert Gell.subs(ell, 0) == -1

    # Actual quintic substitution: (x,y,z,t)=(C,D,u,v).
    C, D, uu, vv = sp.symbols("C D uu vv")
    top = (C * uu, D * uu + C * vv)
    bottom = (
        (C - D**2) * (uu + C + D * vv),
        D * (uu + C + D * vv) + (C - D**2) * (vv + D),
    )
    f1_quintic = fs.subs({x: C, y: D, z: uu, t: vv, s: 1})
    g1_quintic = gs.subs({x: C, y: D, z: uu, t: vv, s: 1})
    assert sp.expand(top&#91;0&#93; - f0.subs({x: C, y: D, z: uu, t: vv})) == 0
    assert sp.expand(top&#91;1&#93; - g0.subs({x: C, y: D, z: uu, t: vv})) == 0
    assert sp.expand(bottom&#91;0&#93; - f1_quintic) == 0
    assert sp.expand(bottom&#91;1&#93; - g1_quintic) == 0

    print("Ga translation and exact outer-pair formulas: passed")
    print("individual graph finite ODP and infinity toric chart: passed")
    print("Chart A exact weak ideal (Z,xH): passed")
    print("residual conifold and both small resolutions: passed")
    print("Chart B boundary blowup formulas: passed")
    print("exact boundary A1 normal form and resolution: passed")
    print("actual quintic substitution: passed")
    print("ALL EXACT ORDERED OUTER-RESOLUTION CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-5825840330291c07"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_m5_resolution_addendum.md`

<pre><code class="language-markdown">
# Addendum to the actual \((5,5)\) PRS flag note

&gt; **Status:** corrective addendum and theorem upgrade.
&gt; **Applies to:** `lane2_m5_nu5_actual_prs_flag.md` from the preceding packet.

## 1. Correction to the individual outer-graph statement

The earlier note correctly identified the finite affine ratio chart

\&#91;
yz+xt-\lambda xz=0
\&#93;

with an ordinary double point after replacing \(t\) by \(t-\lambda z\).
It then overextended that description to the entire projective graph.

At the missing projective direction, put \(\eta=1/\lambda\).  The exact
coordinate change

\&#91;
X=x-\eta y,
\qquad
Z=z-\eta t
\&#93;

gives

\&#91;
\boxed{XZ=\eta^2yt.}
\&#93;

Thus the full individual graph has an additional two-dimensional toric
singular stratum at \(\eta=0\).  It is normal, but its singular locus is not
only the \(\mathbb P^1\) over the deepest coefficient point.

The companion note `lane2_universal_outer_graph_resolution.md` gives a
complete two-center resolution of this graph.

## 2. Upgrade from a quadratic model to an exact ordered theorem

The earlier note proved only that the **quadratic** simultaneous outer graph
reduces to the quartic toric model.  The companion note
`lane2_exact_ordered_outer_resolution.md` proves an exact higher-order result.

On the finite first-direction chart, after one small resolution of the top
outer graph, the weak bottom ideal is exactly

\&#91;
\boxed{(Z,xH)}
\&#93;

in étale coordinates, with

\&#91;
\frac{\partial H}{\partial\lambda}
=-s(1-a^2sx)^2
\&#93;

a unit.  Hence the residual graph is the exact conifold family

\&#91;
\boxed{rZ=xH,}
\&#93;

not merely a conifold tangent cone.

The projective boundary of the first small resolution has one further exact
singularity: a family of \(A_1\) surfaces

\&#91;
\boxed{A\Theta+q^2=0.}
\&#93;

The conifold and \(A_1\) strata are disjoint and admit explicit smooth
projective resolutions.  This proves that the quartic fan prediction lifts to
the full higher-order **ordered** quintic graph on the finite first-direction
locus.

## 3. Revised local status

The corrected local conclusions are:

1. the middle twisted-cubic graph is smooth;
2. each outer graph is normal but has two projective-direction strata:
   finite ODP charts and one toric infinity chart;
3. on the finite first-direction locus, the ordered two-factor graph has an
   exact conifold stratum and an exact \(A_1\) boundary stratum;
4. both are explicitly resolved;
5. the reverse order follows by the inverse additive-group translation;
6. comparison with the normalization of the unordered simultaneous
   multi-Rees graph remains open.

The remaining obstruction is therefore no longer an unknown higher-order
term in the ordered finite-direction chart.  It is the global comparison and
descent problem: projective infinity, unordered normalization, line-bundle
characters, and the relative-Jacobian marking.
</code></pre>

<a id="source-6795c38c845ebf0d"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260801b/lane2_universal_outer_graph_resolution.md`

<pre><code class="language-markdown">
# The universal outer graph: exact singular locus and a global resolution

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact symbolic replay supplied.
&gt; **Scope:** the universal two-generator ideal
&gt; \(J=(xz,yz+xt)\) over a characteristic-zero field.  This note repairs the
&gt; earlier claim that every projective direction is an ordinary-double-point
&gt; chart.  There is one degenerate projective direction with a larger toric
&gt; singular stratum.

## 1. The graph

Let

\&#91;
f=xz,
\qquad
g=yz+xt,
\&#93;

and define

\&#91;
\Gamma_J
=\overline{\operatorname{Graph}(&#91;f:g&#93;)}
\subset
\mathbb A^4_{x,y,z,t}\times\mathbb P^1_{&#91;U:V&#93;}.
\&#93;

Since \((f,g)\) is a regular sequence, the Rees algebra is of linear type and

\&#91;
\Gamma_J=V(Ug-Vf).
\&#93;

## 2. Finite projective directions

On \(U\ne0\), put \(\lambda=V/U\).  The equation is

\&#91;
yz+xt-\lambda xz=0.
\&#93;

With

\&#91;
T=t-\lambda z,
\&#93;

it becomes

\&#91;
\boxed{xT+yz=0.}
\&#93;

Thus every finite projective direction is a threefold ordinary double point,
with the projective parameter \(\lambda\) smooth.  Its singular locus on this
chart is

\&#91;
x=y=z=T=0.
\&#93;

## 3. The unique degenerate projective direction

On \(V\ne0\), put \(\eta=U/V\).  The equation is

\&#91;
\eta(yz+xt)-xz=0.
\&#93;

Set

\&#91;
X=x-\eta y,
\qquad
Z=z-\eta t.
\&#93;

Then

\&#91;
XZ=xz-\eta(xt+yz)+\eta^2yt,
\&#93;

so the graph equation becomes the exact toric binomial

\&#91;
\boxed{XZ=\eta^2yt.}
\&#93;

The reduced singular locus is the union of

\&#91;
L=V(X,Z,y,t),
\&#93;

with \(\eta\) free, and

\&#91;
P_\infty=V(X,Z,\eta),
\&#93;

with \((y,t)\) free.  Their intersection is one point.

Geometrically, \(L\) is the closure of the ordinary-double-point line from
the finite projective chart.  The plane \(P_\infty\) is the additional
singular stratum at the pure \(f=xz\) direction.

## 4. Normality

The graph is an irreducible hypersurface and therefore Cohen--Macaulay.  Its
singular locus has codimension at least two: \(P_\infty\) has dimension two
inside the fourfold \(\Gamma_J\), while \(L\) has dimension one.  Hence
Serre's \(R_1+S_2\) criterion gives:

### Proposition 4.1

\&#91;
\boxed{\Gamma_J\text{ is normal.}}
\&#93;

Thus the special projective direction is a regularity problem, not a
normalization defect.

## 5. First blowup: the infinity plane

Blow up

\&#91;
P_\infty=V(X,Z,\eta)
\&#93;

in the toric chart \(XZ=\eta^2yt\).

### The \(X\)-chart

Put

\&#91;
Z=XZ_1,
\qquad
\eta=Xe.
\&#93;

After removing \(X^2\), the strict equation is

\&#91;
Z_1=e^2yt,
\&#93;

which is smooth.

### The \(Z\)-chart

Symmetrically, the strict equation is smooth.

### The \(\eta\)-chart

Put

\&#91;
X=\eta X_1,
\qquad
Z=\eta Z_1.
\&#93;

After removing \(\eta^2\), the strict equation is

\&#91;
\boxed{X_1Z_1=yt.}
\&#93;

This is a conifold times the smooth parameter \(\eta\).  Its singular locus
is

\&#91;
X_1=Z_1=y=t=0,
\&#93;

which is exactly the strict transform of \(L\).

The blowup is crepant: in the smooth ambient fivefold, the center has
codimension three and the hypersurface has multiplicity two along it.

## 6. Second blowup: the strict ordinary-double-point line

Blow up the strict transform \(\widetilde L\).

- On every finite projective chart, this is the blowup of the vertex in
  \(xT+yz=0\), fiberwise over \(\lambda\).
- On the \(\eta\)-chart after the first blowup, it is the blowup of the vertex
  in \(X_1Z_1-yt=0\), fiberwise over \(\eta\).

For example, on the \(x\)-chart of the first model,

\&#91;
T=xT_1,
\qquad
y=xy_1,
\qquad
z=xz_1,
\&#93;

and the strict equation is

\&#91;
T_1+y_1z_1=0,
\&#93;

which is smooth.  The other charts are identical by symmetry.  The same
calculation resolves \(X_1Z_1=yt\).

### Theorem 6.1 — Canonical two-center resolution

The sequence

\&#91;
\operatorname{Bl}_{\widetilde L}
\operatorname{Bl}_{P_\infty}\Gamma_J
\longrightarrow
\Gamma_J
\&#93;

is a smooth projective resolution.

The first blowup is crepant.  The second is the symmetric divisorial
resolution of the remaining ordinary-double-point family.  Replacing the
second blowup by either small resolution gives the usual local crepant
alternatives wherever those choices glue.

## 7. Consequence for the quintic program

The outer projective factors in the quintic middle chart are copies of this
universal graph.  Hence any global quintic compactification must distinguish:

1. the dense finite-direction ordinary-double-point locus; and
2. the unique projective infinity direction with toric equation
   \(XZ=\eta^2yt\).

A local proof carried out only in the affine ratio \(\lambda\) does not cover
that second stratum.  The ordered-resolution theorem in the companion note is
therefore deliberately scoped to the finite first-direction locus, while the
present theorem supplies the exact missing boundary model.
</code></pre>

<a id="source-7bf7ef7e0d9d74e6"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_hankel_rank_profile.md`

<pre><code class="language-markdown">
# Normal indices determine the full Hankel rank-profile permutation

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact regression supplied.
&gt; **Scope:** a field, a finite nonsingular scalar Hankel matrix, and normal
&gt; indices defined by nonzero leading principal minors.  Combined with the
&gt; companion--Hankel and principal-subresultant identifications in the adjacent
&gt; notes, this proves the previously missing all-rank block-reversal statement
&gt; in `RMU-4D2E0001`.

## 1. Statement

Let \(\Lambda:k&#91;w&#93;\to k\) be a linear functional and put

\&#91;
s_{r+1}=\Lambda(w^r).
\&#93;

For \(n\ge0\), let

\&#91;
H_n=(s_{i+j+1})_{0\le i,j&lt;n},
\qquad
D_n=\det H_n,
\qquad
D_0=1.
\&#93;

Assume \(H_m\) is nonsingular.  List the normal indices

\&#91;
0=n_0&lt;n_1&lt;\cdots&lt;n_s=m
\&#93;

for which \(D_{n_j}\ne0\), and put

\&#91;
d_j=n_j-n_{j-1}.
\&#93;

### Theorem 1.1 — Complete rank-profile theorem

The northwest rank-profile permutation of \(H_m\) is

\&#91;
\boxed{
J_{d_1}\oplus J_{d_2}\oplus\cdots\oplus J_{d_s},
}
\&#93;

where \(J_d\) is the reversal permutation of a consecutive block of size
\(d\).

Equivalently, every gap between consecutive normal indices contributes one
and only one reversal block.

## 2. Orthogonal residuals and Schur complements

Write

\&#91;
\langle f,g\rangle=\Lambda(fg).
\&#93;

Let

\&#91;
V_d=k&#91;w&#93;_{&lt;d}.
\&#93;

If \(D_d\ne0\), the form is nondegenerate on \(V_d\).  For each \(i\ge0\),
there is therefore a unique residual polynomial

\&#91;
r_i=w^{d+i}-\pi_d(w^{d+i})
\&#93;

such that

\&#91;
\pi_d(w^{d+i})\in V_d,
\qquad
r_i\perp V_d.
\&#93;

The first residual

\&#91;
p_d=r_0
\&#93;

is the unique monic degree-\(d\) polynomial orthogonal to \(V_d\).

Partition a larger leading Hankel matrix after its first \(d\) rows and
columns.  Its Schur complement has entries

\&#91;
S^{(d)}_{ij}=\langle r_i,r_j\rangle.
\&#93;

Indeed, subtracting the orthogonal projections from the tail monomials is
exactly block Gaussian elimination of the Gram matrix.

For every \(t\), Schur's determinant formula gives

\&#91;
\boxed{
\det S^{(d)}_t=\frac{D_{d+t}}{D_d}.
}
\&#93;

## 3. The gap lemma

Fix consecutive normal indices

\&#91;
d=n_{j-1},
\qquad
n_j=d+e.
\&#93;

Thus

\&#91;
D_d\ne0,
\qquad
D_{d+t}=0\quad(1\le t&lt;e),
\qquad
D_{d+e}\ne0.
\&#93;

Define the transformed moments

\&#91;
\mu_a=\langle p_d,w^ap_d\rangle.
\&#93;

### Lemma 3.1 — Orthogonality propagates through the gap

One has

\&#91;
\mu_0=\mu_1=\cdots=\mu_{e-2}=0,
\qquad
\mu_{e-1}\ne0.
\&#93;

Moreover, on the first \(e\) residuals, the Schur complement is related by a
unit lower-triangular congruence to the Hankel matrix

\&#91;
T_e=(\mu_{a+b})_{0\le a,b&lt;e}.
\&#93;

#### Proof

We prove inductively that, before step \(t\),

\&#91;
p_d\perp V_{d+t-1}
\&#93;

and

\&#91;
\mu_0=\cdots=\mu_{t-2}=0.
\&#93;

This is true for \(t=1\), because \(p_d\perp V_d\).

For \(0\le i&lt;t\), put

\&#91;
u_i=w^ip_d.
\&#93;

If \(a&lt;d\), then

\&#91;
i+a\le d+t-2,
\&#93;

so the induction hypothesis gives

\&#91;
\langle u_i,w^a\rangle=0.
\&#93;

Thus \(u_i\in V_d^\perp\).  The space

\&#91;
V_d^\perp\cap k&#91;w&#93;_{&lt;d+i+1}
\&#93;

has dimension \(i+1\), and

\&#91;
r_0,\ldots,r_i
\&#93;

form a basis of it.  Comparing leading terms gives a unit lower-triangular
relation

\&#91;
(u_0,\ldots,u_{t-1})^{\mathsf T}
=U_t(r_0,\ldots,r_{t-1})^{\mathsf T}.
\&#93;

Therefore

\&#91;
T_t=U_tS^{(d)}_tU_t^{\mathsf T}.
\&#93;

In particular,

\&#91;
\det T_t=\det S^{(d)}_t.
\&#93;

Since \(\mu_0,\ldots,\mu_{t-2}\) vanish, \(T_t\) has zeros strictly before
its anti-diagonal and constant anti-diagonal \(\mu_{t-1}\).  Hence

\&#91;
\det T_t
=(-1)^{\binom t2}\mu_{t-1}^{\,t}.
\&#93;

For \(t&lt;e\), the normal-index hypothesis and Schur's formula give

\&#91;
\det T_t=\det S^{(d)}_t=0,
\&#93;

so \(\mu_{t-1}=0\).

Write

\&#91;
w^{t-1}p_d=w^{d+t-1}+h,
\qquad
\deg h\le d+t-2.
\&#93;

The induction hypothesis gives \(\langle p_d,h\rangle=0\), and therefore

\&#91;
0=\mu_{t-1}
=\langle p_d,w^{d+t-1}\rangle.
\&#93;

This extends the orthogonality to \(V_{d+t}\), completing the induction.

At \(t=e\), the determinant is nonzero, so

\&#91;
\mu_{e-1}\ne0.
\&#93;
∎

### Corollary 3.2 — Every normal-index gap is a reversal block

The northwest rank-profile permutation of the first \(e\) rows and columns of
\(S^{(d)}\) is \(J_e\).

#### Proof

The matrix \(T_e\) satisfies

\&#91;
(T_e)_{ab}=0\quad\text{if }a+b&lt;e-1
\&#93;

and has nonzero anti-diagonal \(\mu_{e-1}\).  Consequently every northwest
\(a\times b\) prefix has rank

\&#91;
\max(0,a+b-e),
\&#93;

which is exactly the prefix-rank function of \(J_e\).

The congruence

\&#91;
T_e=U_eS^{(d)}_eU_e^{\mathsf T}
\&#93;

uses a lower-triangular matrix on the left and an upper-triangular matrix on
the right.  Such transformations preserve all northwest prefix ranks. ∎

## 4. Proof of the complete theorem

Start at \(d=n_0=0\).  Corollary 3.2 gives the first reversal block
\(J_{d_1}\).

Because the corresponding leading block is nonsingular, block Gaussian
elimination clears its right and lower rectangles using a unit lower
transformation on the left and a unit upper transformation on the right.
These transformations preserve all northwest prefix ranks.  The residual
matrix is the Schur complement after the first normal index.

Apply Corollary 3.2 with

\&#91;
d=n_1,
\qquad
e=d_2.
\&#93;

It gives the next block \(J_{d_2}\).  Continue through all consecutive normal
indices.  Schur-complement associativity shows that eliminating the blocks
successively gives the same residual as taking the Schur complement of the
full leading \(n_j\times n_j\) block directly.

Thus the complete rank-profile permutation is

\&#91;
J_{d_1}\oplus\cdots\oplus J_{d_s}.
\&#93;
∎

## 5. Consequences for the companion--PRS theorem

For the Lane 2 matrix associated with multiplication by \(w^\nu\bmod Q\):

1. the exact triangular identity
   \&#91;
   K_\nu=L_QH_\nu
   \&#93;
   identifies its northwest rank profile with the moment Hankel matrix;
2. the convention-complete identity
   \&#91;
   \operatorname{psc}_{m-k}(w^\nu,Q)
   =(-1)^{\binom k2}\det H_k
   \&#93;
   identifies the Euclidean/subresultant normal indices with the Hankel normal
   indices;
3. Theorem 1.1 gives
   \&#91;
   J_{d_1}\oplus\cdots\oplus J_{d_s};
   \&#93;
4. the filtered Bruhat--Smith lemma then gives exponent
   \&#91;
   \boxed{\nu-m+n_{j-1}+n_j}
   \&#93;
   with multiplicity \(d_j\).

Thus the rank-profile and filtered-Smith portions of `RMU-4D2E0001` now have a
self-contained proof chain.  What remains for the broader Lane 2 program is
not this local linear algebra, but the global geometry of closures of the
composition cells and the compatibility of their graph modifications.

## 6. Exact replay

The supplied checker verifies:

- all \(2^{m-1}\) ordered compositions for every \(2\le m\le5\), using 30
  explicit moment sequences;
- every northwest rectangular prefix rank against the direct sum of reversal
  blocks;
- the orthogonal-polynomial gap propagation;
- the exact triangular congruence
  \&#91;
  T_e=U_eS_eU_e^{\mathsf T};
  \&#93;
- 120 additional exact nonsingular Hankel examples in ranks \(6,7,8\).

All checks pass.
</code></pre>

<a id="source-49668fb256743c46"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_hankel_rank_profile_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for the all-rank Hankel normal-index rank-profile theorem."""
from __future__ import annotations

import random
from fractions import Fraction
import sympy as sp


REPRESENTATIVES: dict&#91;int, dict&#91;tuple&#91;int, ...&#93;, tuple&#91;int, ...&#93;&#93;&#93; = {
    2: {
        (1, 1): (-1, -1, 0),
        (2,): (0, -1, -1),
    },
    3: {
        (1, 1, 1): (-1, -1, 0, -1, -1),
        (1, 2): (-1, -1, -1, 0, -1),
        (2, 1): (0, -1, -1, -1, 0),
        (3,): (0, 0, -1, -1, -1),
    },
    4: {
        (1, 1, 1, 1): (-1, -1, 0, -1, -1, -1, -1),
        (1, 1, 2): (-1, -1, 0, -1, 1, -1, -1),
        (1, 2, 1): (-1, -1, -1, 0, -1, -1, -1),
        (1, 3): (-1, -1, -1, -1, 0, -1, -1),
        (2, 1, 1): (0, -1, -1, -1, 0, -1, -1),
        (2, 2): (0, -1, -1, -1, -1, 0, -1),
        (3, 1): (0, 0, -1, -1, -1, -1, 0),
        (4,): (0, 0, 0, -1, -1, -1, -1),
    },
    5: {
        (1, 1, 1, 1, 1): (-1, -1, 0, -1, -1, -1, -1, -1, 0),
        (1, 1, 1, 2): (-1, -1, 0, -1, -1, 0, -1, 0, -1),
        (1, 1, 2, 1): (-1, -1, 0, -1, 1, -1, -1, -1, -1),
        (1, 1, 3): (-1, -1, 0, 0, 0, 0, -1, -1, -1),
        (1, 2, 1, 1): (-1, -1, -1, 0, -1, -1, -1, -1, -1),
        (1, 2, 2): (-1, -1, -1, 0, -1, 0, 0, 0, -1),
        (1, 3, 1): (-1, -1, -1, -1, 0, -1, -1, -1, -1),
        (1, 4): (-1, -1, -1, -1, -1, 0, -1, -1, -1),
        (2, 1, 1, 1): (0, -1, -1, -1, 0, -1, -1, -1, -1),
        (2, 1, 2): (0, -1, -1, -1, 0, 0, 1, -1, -1),
        (2, 2, 1): (0, -1, -1, -1, -1, 0, -1, -1, -1),
        (2, 3): (0, -1, -1, -1, -1, -1, 0, -1, -1),
        (3, 1, 1): (0, 0, -1, -1, -1, -1, 0, -1, -1),
        (3, 2): (0, 0, -1, -1, -1, -1, -1, 0, -1),
        (4, 1): (0, 0, 0, -1, -1, -1, -1, -1, 0),
        (5,): (0, 0, 0, 0, -1, -1, -1, -1, -1),
    },
}


def hankel(seq: tuple&#91;int, ...&#93; | list&#91;sp.Expr&#93;, rows: int, cols: int | None = None, shift: int = 0) -&gt; sp.Matrix:
    if cols is None:
        cols = rows
    return sp.Matrix(&#91;&#91;seq&#91;shift + i + j&#93; for j in range(cols)&#93; for i in range(rows)&#93;)


def normal_indices(seq: tuple&#91;int, ...&#93;, m: int) -&gt; list&#91;int&#93;:
    result = &#91;0&#93;
    for k in range(1, m + 1):
        if hankel(seq, k).det() != 0:
            result.append(k)
    return result


def expected_permutation(indices: list&#91;int&#93;, m: int) -&gt; sp.Matrix:
    p = sp.zeros(m)
    for left, right in zip(indices&#91;:-1&#93;, indices&#91;1:&#93;):
        for i in range(left, right):
            p&#91;i, left + right - 1 - i&#93; = 1
    return p


def assert_prefix_ranks(matrix: sp.Matrix, permutation: sp.Matrix) -&gt; None:
    rows, cols = matrix.shape
    for a in range(1, rows + 1):
        for b in range(1, cols + 1):
            assert matrix&#91;:a, :b&#93;.rank() == permutation&#91;:a, :b&#93;.rank()


def bilinear(seq: tuple&#91;int, ...&#93;, f: list&#91;sp.Expr&#93;, g: list&#91;sp.Expr&#93;, shift: int = 0) -&gt; sp.Expr:
    value = sp.Integer(0)
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            value += fi * gj * seq&#91;shift + i + j&#93;
    return sp.expand(value)


def monic_orthogonal_polynomial(seq: tuple&#91;int, ...&#93;, d: int) -&gt; list&#91;sp.Expr&#93;:
    if d == 0:
        return &#91;sp.Integer(1)&#93;
    hd = hankel(seq, d)
    rhs = sp.Matrix(&#91;-seq&#91;d + j&#93; for j in range(d)&#93;)
    lower = list(hd.LUsolve(rhs))
    return &#91;sp.expand(x) for x in lower&#93; + &#91;sp.Integer(1)&#93;


def schur_complement(seq: tuple&#91;int, ...&#93;, m: int, d: int) -&gt; sp.Matrix:
    full = hankel(seq, m)
    if d == 0:
        return full
    a = full&#91;:d, :d&#93;
    b = full&#91;:d, d:&#93;
    c = full&#91;d:, d:&#93;
    return sp.simplify(c - b.T * a.inv() * b)


def verify_gap_model(seq: tuple&#91;int, ...&#93;, m: int, left: int, right: int) -&gt; None:
    e = right - left
    p = monic_orthogonal_polynomial(seq, left)
    mu = &#91;bilinear(seq, p, &#91;sp.Integer(0)&#93; * j + p) for j in range(2 * e - 1)&#93;
    assert all(value == 0 for value in mu&#91;: e - 1&#93;)
    assert mu&#91;e - 1&#93; != 0

    s = schur_complement(seq, m, left)&#91;:e, :e&#93;
    t = sp.Matrix(&#91;&#91;mu&#91;i + j&#93; for j in range(e)&#93; for i in range(e)&#93;)

    # Construct residual polynomials r_i=w^{d+i}-projection to degree &lt;d.
    residuals: list&#91;list&#91;sp.Expr&#93;&#93; = &#91;&#93;
    for i in range(e):
        if left == 0:
            residuals.append(&#91;sp.Integer(0)&#93; * i + &#91;sp.Integer(1)&#93;)
            continue
        hd = hankel(seq, left)
        rhs = sp.Matrix(&#91;seq&#91;left + i + j&#93; for j in range(left)&#93;)
        projection = list(hd.LUsolve(rhs))
        r = &#91;-sp.expand(x) for x in projection&#93;
        r.extend(&#91;sp.Integer(0)&#93; * i)
        r.append(sp.Integer(1))
        residuals.append(r)

    # u_i=w^i p is a unit-lower-triangular combination of r_0,...,r_i.
    u = sp.eye(e)
    for i in range(e):
        shifted = &#91;sp.Integer(0)&#93; * i + p
        for ell in range(i):
            degree = left + ell
            coefficient = shifted&#91;degree&#93; if degree &lt; len(shifted) else sp.Integer(0)
            u&#91;i, ell&#93; = coefficient
        combination = &#91;sp.Integer(0)&#93; * (left + i + 1)
        for ell in range(i + 1):
            for degree, value in enumerate(residuals&#91;ell&#93;):
                combination&#91;degree&#93; += u&#91;i, ell&#93; * value
        assert all(sp.expand(a - b) == 0 for a, b in zip(shifted, combination))

    assert sp.simplify(t - u * s * u.T) == sp.zeros(e)
    assert_prefix_ranks(s, sp.Matrix(&#91;&#91;1 if i + j == e - 1 else 0 for j in range(e)&#93; for i in range(e)&#93;))


def verify_sequence(seq: tuple&#91;int, ...&#93;, m: int) -&gt; tuple&#91;int, ...&#93;:
    indices = normal_indices(seq, m)
    assert indices&#91;-1&#93; == m
    composition = tuple(b - a for a, b in zip(indices&#91;:-1&#93;, indices&#91;1:&#93;))
    full = hankel(seq, m)
    permutation = expected_permutation(indices, m)
    assert_prefix_ranks(full, permutation)
    for left, right in zip(indices&#91;:-1&#93;, indices&#91;1:&#93;):
        verify_gap_model(seq, m, left, right)
    return composition


def main() -&gt; None:
    representative_cases = 0
    represented_compositions = 0
    for m, by_composition in REPRESENTATIVES.items():
        assert len(by_composition) == 2 ** (m - 1)
        for expected, seq in by_composition.items():
            actual = verify_sequence(seq, m)
            assert actual == expected
            representative_cases += 1
        represented_compositions += len(by_composition)

    rng = random.Random(20260802)
    random_cases = 0
    for m in (6, 7, 8):
        while random_cases &lt; (m - 5) * 40:
            seq = tuple(rng.choice((-2, -1, 0, 1, 2)) for _ in range(2 * m - 1))
            if hankel(seq, m).det() == 0:
                continue
            verify_sequence(seq, m)
            random_cases += 1

    print(f"composition representatives: {representative_cases}")
    print(f"all compositions represented through rank 5: {represented_compositions}")
    print(f"additional exact random cases in ranks 6–8: {random_cases}")
    print("ALL HANKEL RANK-PROFILE CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-2af31fd24c3a8d0f"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_psc_hankel_schur.md`

<pre><code class="language-markdown">
# Principal subresultants, Krylov minors, and rectangular Schur polynomials

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact symbolic and
&gt; integer regression supplied.
&gt; **Scope:** a field of characteristic zero, a monic polynomial with nonzero
&gt; constant term, and the explicit determinant convention below.  The proof is
&gt; algebraic and extends to any characteristic in which the displayed
&gt; identities and separability reductions are interpreted appropriately.

This note removes the convention-dependent part of `RMU-4D2E0001` that had
been attributed only to an unavailable source message.

## 1. Setup and determinant convention

Let

\&#91;
Q(w)=w^m+q_1w^{m-1}+\cdots+q_m,
\qquad q_m\ne0,
\&#93;

let \(\nu\ge m\), and put

\&#91;
R(w)=w^\nu\bmod Q(w),
\qquad \deg R&lt;m.
\&#93;

Expand at infinity

\&#91;
\frac{R(w)}{Q(w)}=\sum_{\ell\ge1}s_\ell w^{-\ell}
\&#93;

and define

\&#91;
H_k=(s_{i+j+1})_{0\le i,j&lt;k}.
\&#93;

For \(1\le k\le m\), define the displayed principal subresultant coefficient
\(\operatorname{psc}_{m-k}^{\mathrm{disp}}(Q,R)\) to be the determinant of
the \((2k-1)\times(2k-1)\) coefficient matrix whose rows, in order, are

\&#91;
w^{k-2}Q,\ldots,Q,
\quad
w^{k-1}R,\ldots,R,
\&#93;

and whose columns, in order, are the coefficients of

\&#91;
w^{m+k-2},w^{m+k-3},\ldots,w^{m-k}.
\&#93;

This is the standard principal-subresultant determinant after fixing the row
and column order explicitly.  Other common conventions differ by a fixed
sign only.

## 2. The exact determinant identity

### Theorem 2.1 — PSC equals a northwest Krylov determinant

Let \(K_k\) be the \(k\times k\) matrix whose \(j\)-th column, for
\(0\le j&lt;k\), consists of the coefficients of

\&#91;
w^jR\bmod Q
\&#93;

in degrees \(m-1,m-2,\ldots,m-k\).  Then

\&#91;
\boxed{
\operatorname{psc}_{m-k}^{\mathrm{disp}}(Q,R)
=(-1)^{\binom{k}{2}}\det K_k.
}
\&#93;

#### Proof

The first \(k-1\) rows of the displayed subresultant matrix have leading
coefficients forming the identity matrix in the columns of degrees

\&#91;
m+k-2,m+k-3,\ldots,m.
\&#93;

Use these rows to divide every lower row by the monic polynomial \(Q\).  This
is a sequence of determinant-preserving row operations.  The resulting lower
rows are

\&#91;
w^{k-1}R\bmod Q,\ldots,R,
\&#93;

and the lower-right \(k\times k\) block records their coefficients in degrees
\(m-1,\ldots,m-k\).

The rows occur in the reverse of the column order used in \(K_k\).  Reversing
\(k\) objects contributes the sign

\&#91;
(-1)^{\binom{k}{2}},
\&#93;

and transposition does not change a determinant. ∎

### Theorem 2.2 — Krylov equals Hankel

One has

\&#91;
\boxed{\det K_k=\det H_k.}
\&#93;

#### Proof

Let \(K_\nu=JC^\nu\) be the full descending-coefficient companion--Krylov
matrix, as in the structural lemma packet, and let

\&#91;
L_Q=(q_{i-j})_{0\le j\le i&lt;m},\qquad q_0=1.
\&#93;

The exact identity

\&#91;
K_\nu=L_QH_\nu
\&#93;

holds, where \(H_\nu=(s_{i+j+1})_{0\le i,j&lt;m}\).  Taking the northwest
\(k\times k\) block gives

\&#91;
(K_\nu)_k=(L_Q)_kH_k.
\&#93;

The matrix \((L_Q)_k\) is unit lower triangular, so its determinant is one.
The block \((K_\nu)_k\) is exactly \(K_k\). ∎

Combining the two theorems gives

\&#91;
\boxed{
\operatorname{psc}_{m-k}^{\mathrm{disp}}(Q,R)
=(-1)^{\binom{k}{2}}\det H_k.
}
\&#93;

Since replacing \(w^\nu\) by its remainder modulo the monic polynomial \(Q\)
is itself determinant-preserving Sylvester elimination, the same displayed
principal coefficient is obtained from the pair \((w^\nu,Q)\).

## 3. Root formula and the rectangular partition

Let \(\alpha_1,\ldots,\alpha_m\) be the roots of \(Q\) in a splitting field.
First assume they are distinct.  Since

\&#91;
R(\alpha_i)=\alpha_i^\nu,
\&#93;

partial fractions give

\&#91;
\frac{R(w)}{Q(w)}
=\sum_{i=1}^m
 \frac{\alpha_i^\nu}{Q'(\alpha_i)(w-\alpha_i)}.
\&#93;

Consequently

\&#91;
s_\ell
=\sum_{i=1}^m
 \frac{\alpha_i^{\nu+\ell-1}}{Q'(\alpha_i)}.
\&#93;

### Theorem 3.1 — Hankel determinant as a subset sum

For \(1\le k\le m\),

\&#91;
\det H_k
=(-1)^{\binom{k}{2}}
\sum_{\substack{I\subset\{1,\ldots,m\}\\|I|=k}}
\frac{\prod_{i\in I}\alpha_i^\nu}
{\prod_{i\in I,\ j\notin I}(\alpha_i-\alpha_j)}.
\&#93;

#### Proof

Write

\&#91;
H_k=V_I\,\operatorname{diag}
\left(\frac{\alpha_i^\nu}{Q'(\alpha_i)}\right)V_I^{\mathsf T}
\&#93;

at the level of the full rectangular Vandermonde factorization and apply
Cauchy--Binet.  This gives

\&#91;
\det H_k
=\sum_{|I|=k}
 \frac{\prod_{i\in I}\alpha_i^\nu\,\Delta_I^2}
 {\prod_{i\in I}Q'(\alpha_i)}.
\&#93;

For each unordered pair inside \(I\), the two derivative factors contribute
one minus sign, while the remaining derivative factors are exactly the cross
product in the denominator.  Hence

\&#91;
\frac{\Delta_I^2}{\prod_{i\in I}Q'(\alpha_i)}
=
rac{(-1)^{\binom{k}{2}}}
 {\prod_{i\in I,j\notin I}(\alpha_i-\alpha_j)}.
\&#93;
∎

Put

\&#91;
a=\nu-m+k.
\&#93;

This is nonnegative because \(\nu\ge m\).

### Theorem 3.2 — The subset sum is a rectangular Schur polynomial

Let \(\lambda=(a^k)\), the rectangle of height \(k\) and width \(a\).  Then

\&#91;
\sum_{|I|=k}
\frac{\prod_{i\in I}\alpha_i^\nu}
{\prod_{i\in I,j\notin I}(\alpha_i-\alpha_j)}
=s_{(a^k)}(\alpha_1,\ldots,\alpha_m).
\&#93;

#### Proof

Use the bialternant formula for the partition

\&#91;
(a,\ldots,a,0,\ldots,0),
\&#93;

with \(k\) copies of \(a\).  The numerator alternant has exponent rows

\&#91;
\nu+k-1,\ldots,\nu,
\quad
m-k-1,\ldots,0.
\&#93;

Laplace-expand along the first \(k\) rows.  Choosing a set \(I\) of \(k\)
columns contributes

\&#91;
\left(\prod_{i\in I}\alpha_i^\nu\right)
\Delta_I\Delta_{I^c}.
\&#93;

Dividing by the full Vandermonde leaves precisely the displayed cross
denominator; the Laplace and Vandermonde shuffle signs cancel. ∎

The distinct-root locus is Zariski dense, and both sides are symmetric
polynomials in the roots.  Therefore the identity extends to arbitrary monic
\(Q\), including nonreduced root schemes.

## 4. Final convention-complete identity

### Corollary 4.1

For every \(1\le k\le m\),

\&#91;
\boxed{
\operatorname{psc}_{m-k}^{\mathrm{disp}}(w^\nu,Q)
=s_{((\nu-m+k)^k)}(\alpha_1,\ldots,\alpha_m)
=(-1)^{\binom{k}{2}}\det H_k.
}
\&#93;

Thus:

1. the southwest/northwest Krylov determinant convention is explicit;
2. the subresultant sign is explicit;
3. the rectangular partition is
   \(((\nu-m+k)^k)\);
4. the vanishing loci and normal indices are independent of every remaining
   sign convention.

## 5. Consequences for Lane 2

The following portions of the retained rank-profile record are now proved
without relying on a private source message:

- companion--Krylov prefixes reduce triangularly to genuine Hankel prefixes;
- the relevant leading Hankel determinants are principal subresultant
  coefficients;
- those coefficients are rectangular Schur polynomials with the displayed
  partition;
- the first normal-index gap gives the first reversal block;
- once the full block-reversal profile is known, the filtered Smith exponents
  follow formally.

The remaining all-rank step is narrow: prove that successive Schur complements
of the Hankel moment matrix retain the required quasi-Hankel prefix-rank
recursion, thereby producing every later reversal block.  Existing arbitrary
rank-profile Hankel factorizations strongly support this step, but a
self-contained proof in the exact conventions of this program is still
needed.

## 6. Exact replay

The supplied script checks both identities

\&#91;
\operatorname{psc}_{m-k}^{\mathrm{disp}}
=(-1)^{\binom{k}{2}}\det H_k
\&#93;

and

\&#91;
\operatorname{psc}_{m-k}^{\mathrm{disp}}
=s_{((\nu-m+k)^k)}
\&#93;

for:

- 150 deterministic integer polynomial cases with \(2\le m\le7\);
- 675 exact determinant identities across all \(k\);
- 27 fully symbolic identities in ranks \(2,3,4\).

All checks pass.
</code></pre>

<a id="source-95a864d399454f98"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_psc_hankel_schur_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact regression checks for the all-rank PSC–Hankel–Schur identity."""
from __future__ import annotations

import itertools
import sympy as sp

w = sp.symbols("w")


def coeff_row(poly: sp.Expr, degrees: list&#91;int&#93;) -&gt; list&#91;sp.Expr&#93;:
    p = sp.Poly(poly, w)
    return &#91;p.coeff_monomial(w**d) for d in degrees&#93;


def displayed_psc(Q: sp.Expr, R: sp.Expr, m: int, k: int) -&gt; sp.Expr:
    """PSC_{m-k} in the displayed row/column convention of the note."""
    degrees = list(range(m + k - 2, m - k - 1, -1))
    rows: list&#91;list&#91;sp.Expr&#93;&#93; = &#91;&#93;
    for a in range(k - 2, -1, -1):
        rows.append(coeff_row(sp.expand(w**a * Q), degrees))
    for a in range(k - 1, -1, -1):
        rows.append(coeff_row(sp.expand(w**a * R), degrees))
    matrix = sp.Matrix(rows)
    assert matrix.shape == (2 * k - 1, 2 * k - 1)
    return sp.expand(matrix.det())


def moments_of_R_over_Q(
    q: tuple&#91;int, ...&#93;, R: sp.Expr, m: int, count: int
) -&gt; list&#91;sp.Expr&#93;:
    """Return s_1,...,s_count for R/Q=sum s_l w^{-l}."""
    rp = sp.Poly(R, w)
    numerator = &#91;sp.Integer(0)&#93; * (count + 1)
    for a in range(m):
        ell = m - a
        if ell &lt;= count:
            numerator&#91;ell&#93; = rp.coeff_monomial(w**a)

    s = &#91;sp.Integer(0)&#93; * (count + 1)
    for ell in range(1, count + 1):
        value = numerator&#91;ell&#93;
        for i in range(1, min(m, ell - 1) + 1):
            value -= q&#91;i - 1&#93; * s&#91;ell - i&#93;
        s&#91;ell&#93; = sp.expand(value)
    return s&#91;1:&#93;


def hankel_det(moments: list&#91;sp.Expr&#93;, k: int) -&gt; sp.Expr:
    return sp.expand(
        sp.Matrix(&#91;&#91;moments&#91;i + j&#93; for j in range(k)&#93; for i in range(k)&#93;).det()
    )


def complete_symmetric(q: tuple&#91;int, ...&#93;, m: int, count: int) -&gt; list&#91;sp.Expr&#93;:
    """h_0,...,h_count for roots of w^m+q_1w^{m-1}+...+q_m."""
    h = &#91;sp.Integer(1)&#93;
    for n in range(1, count + 1):
        value = sp.Integer(0)
        for i in range(1, min(m, n) + 1):
            value += q&#91;i - 1&#93; * h&#91;n - i&#93;
        h.append(sp.expand(-value))
    return h


def rectangular_schur(q: tuple&#91;int, ...&#93;, m: int, width: int, height: int) -&gt; sp.Expr:
    h = complete_symmetric(q, m, width + height - 1)

    def h_at(index: int) -&gt; sp.Expr:
        return sp.Integer(0) if index &lt; 0 else h&#91;index&#93;

    jt = sp.Matrix(
        &#91;
            &#91;h_at(width - i + j) for j in range(height)&#93;
            for i in range(height)
        &#93;
    )
    return sp.expand(jt.det())


def coefficient_samples(m: int) -&gt; list&#91;tuple&#91;int, ...&#93;&#93;:
    # Deterministic samples, always with nonzero constant coefficient.
    values = &#91;-2, -1, 0, 1, 2&#93;
    samples: list&#91;tuple&#91;int, ...&#93;&#93; = &#91;&#93;
    for index, prefix in enumerate(itertools.product(values, repeat=m - 1)):
        if index % max(1, 5 ** max(0, m - 3)) != 0:
            continue
        constant = (-1, 1, 2)&#91;len(samples) % 3&#93;
        samples.append(tuple(prefix) + (constant,))
        if len(samples) == 5:
            break
    return samples


def main() -&gt; None:
    tested_polynomials = 0
    tested_identities = 0
    symbolic_identities = 0

    for m in range(2, 8):
        for nu in range(m, m + 5):
            for q in coefficient_samples(m):
                Q = w**m + sum(q&#91;i&#93; * w ** (m - 1 - i) for i in range(m))
                R = sp.rem(w**nu, Q, w)
                moments = moments_of_R_over_Q(q, R, m, 2 * m - 1)
                for k in range(1, m + 1):
                    psc = displayed_psc(Q, R, m, k)
                    hdet = hankel_det(moments, k)
                    sign = (-1) ** (k * (k - 1) // 2)
                    schur = rectangular_schur(q, m, nu - m + k, k)
                    assert sp.expand(psc - sign * hdet) == 0
                    assert sp.expand(psc - schur) == 0
                    tested_identities += 1
                tested_polynomials += 1

    # Fully symbolic checks in the first nontrivial ranks.
    for m in (2, 3, 4):
        qsym = sp.symbols(f"q1:{m + 1}")
        Q = w**m + sum(qsym&#91;i&#93; * w ** (m - 1 - i) for i in range(m))
        for nu in range(m, m + 3):
            R = sp.rem(w**nu, Q, w)
            moments = moments_of_R_over_Q(qsym, R, m, 2 * m - 1)
            for k in range(1, m + 1):
                psc = displayed_psc(Q, R, m, k)
                hdet = hankel_det(moments, k)
                sign = (-1) ** (k * (k - 1) // 2)
                schur = rectangular_schur(qsym, m, nu - m + k, k)
                assert sp.expand(psc - sign * hdet) == 0
                assert sp.expand(psc - schur) == 0
                symbolic_identities += 1

    print(f"numeric polynomial cases: {tested_polynomials}")
    print(f"numeric determinant identities: {tested_identities}")
    print(f"fully symbolic identities: {symbolic_identities}")
    print("ALL PSC–HANKEL–SCHUR CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-daf219707509ef2f"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_structural_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact regression checks for the all-rank Lane-2 structural lemmas.

Checks:
1. the cyclotomic remainder-coordinate Jacobian formula;
2. the unit-lower-Toeplitz reduction J C^nu = L H from the companion
   Krylov matrix to a symmetric Hankel moment matrix;
3. the first-normal-block rank formula.
"""
from __future__ import annotations

from itertools import product
import sympy as sp

w, z, lam = sp.symbols("w z lam")


def companion_desc(q: list&#91;sp.Expr&#93;) -&gt; sp.Matrix:
    """Multiplication by w in ascending basis for Q=w^m+q1*w^(m-1)+...+qm."""
    m = len(q)
    C = sp.zeros(m)
    for j in range(m-1):
        C&#91;j+1, j&#93; = 1
    for i in range(m):
        C&#91;i, m-1&#93; = -q&#91;m-1-i&#93;
    return C


def reverse_matrix(m: int) -&gt; sp.Matrix:
    J = sp.zeros(m)
    for i in range(m):
        J&#91;i, m-1-i&#93; = 1
    return J


def lower_toeplitz(q: list&#91;sp.Expr&#93;) -&gt; sp.Matrix:
    m = len(q)
    qq = &#91;sp.Integer(1), *q&#93;
    return sp.Matrix(m, m, lambda i, j: qq&#91;i-j&#93; if i &gt;= j else 0)


def moments(q: list&#91;sp.Expr&#93;, nu: int, count: int) -&gt; list&#91;sp.Expr&#93;:
    m = len(q)
    Q = w**m + sum(q&#91;i&#93;*w**(m-1-i) for i in range(m))
    R = sp.rem(w**nu, Q, domain=sp.QQ)
    numerator = sp.expand(z**m * R.subs(w, 1/z))
    denominator = 1 + sum(q&#91;i&#93;*z**(i+1) for i in range(m))
    series = sp.series(numerator/denominator, z, 0, count+1).removeO().expand()
    return &#91;sp.expand(series.coeff(z, j)) for j in range(1, count+1)&#93;


def check_cyclotomic_jacobians() -&gt; int:
    checked = 0
    for m in range(2, 7):
        aa = sp.symbols(f"a0:{m}")
        Q = w**m + sum(aa&#91;i&#93;*w**i for i in range(m))
        C0 = sp.zeros(m)
        for j in range(m-1):
            C0&#91;j+1, j&#93; = 1
        C0&#91;0, m-1&#93; = lam
        point = {aa&#91;0&#93;: -lam, **{aa&#91;i&#93;: 0 for i in range(1, m)}}
        for nu in range(m, 3*m+2):
            k, r = divmod(nu, m)
            R = sp.Poly(sp.rem(w**nu, Q, w), w)
            coeff = sp.Matrix(&#91;R.coeff_monomial(w**i) for i in range(m)&#93;)
            Jac = coeff.jacobian(aa).subs(point).applyfunc(sp.expand)
            expected = (-k*lam**(k-1)) * (C0**r)
            assert (Jac-expected).applyfunc(sp.expand) == sp.zeros(m)
            determinant = sp.factor(Jac.det())
            predicted = sp.factor(
                (-k*lam**(k-1))**m * (((-1)**(m-1)*lam)**r)
            )
            assert sp.expand(determinant-predicted) == 0
            checked += 1
    return checked


def check_krylov_hankel() -&gt; int:
    checked = 0
    samples = &#91;
        (-2, -1, 1, 2),
        (-1, 0, 1, 1),
        (1, -2, 2, -1),
    &#93;
    for m in range(2, 7):
        for seed in samples:
            q = &#91;sp.Integer(seed&#91;i % len(seed)&#93;) for i in range(m)&#93;
            if q&#91;-1&#93; == 0:
                q&#91;-1&#93; = 1
            C = companion_desc(q)
            J = reverse_matrix(m)
            L = lower_toeplitz(q)
            for nu in range(m, m+4):
                ss = moments(q, nu, 2*m-1)
                H = sp.Matrix(m, m, lambda i, j: ss&#91;i+j&#93;)
                K = J*(C**nu)
                assert (K-L*H).applyfunc(sp.expand) == sp.zeros(m)
                assert H == H.T
                # L is unit lower triangular, hence every NW rank agrees.
                for a in range(1, m+1):
                    for b in range(1, m+1):
                        assert K&#91;:a, :b&#93;.rank() == H&#91;:a, :b&#93;.rank()
                checked += 1
    return checked


def check_first_normal_block() -&gt; int:
    checked = 0
    # Moment strings with first nonzero moment s_d, followed by deterministic tails.
    for n in range(2, 9):
        for d in range(1, n+1):
            seq = &#91;sp.Integer(0)&#93;*(d-1) + &#91;sp.Integer(2)&#93;
            seq += &#91;sp.Integer((j % 5)-2) for j in range(2*n-len(seq))&#93;
            H = sp.Matrix(n, n, lambda i, j: seq&#91;i+j&#93;)
            for a in range(1, d+1):
                for b in range(1, d+1):
                    expected = max(0, a+b-d)
                    assert H&#91;:a, :b&#93;.rank() == expected
            detd = sp.factor(H&#91;:d, :d&#93;.det())
            expected_det = (-1)**(d*(d-1)//2) * 2**d
            assert detd == expected_det
            checked += 1
    return checked


def main() -&gt; None:
    c1 = check_cyclotomic_jacobians()
    c2 = check_krylov_hankel()
    c3 = check_first_normal_block()
    print(f"cyclotomic Jacobian cases: {c1}")
    print(f"Krylov-to-Hankel exact cases: {c2}")
    print(f"first-normal-block cases: {c3}")
    print("ALL LANE-2 ALL-RANK STRUCTURAL CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-789ec859829a957c"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_all_rank_structural_lemmas.md`

<pre><code class="language-markdown">
# All-rank structural repairs for Lane 2

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact regression script supplied.
&gt; **Scope:** characteristic zero unless otherwise stated.  These lemmas repair
&gt; the local coordinate and filtered-Smith parts of `RMU-4D2E0001`.  The
&gt; formerly missing arbitrary-rank block recursion is now proved separately in
&gt; `lane2_all_rank_hankel_rank_profile.md`.

## 1. Cyclotomic remainder coordinates are étale

Let

\&#91;
Q(w)=w^m+q_1w^{m-1}+\cdots+q_m
\&#93;

and let

\&#91;
\mathcal R_\nu(Q)=w^\nu\bmod Q\in k&#91;w&#93;_{&lt;m}.
\&#93;

This defines a polynomial map from the monic coefficient space to the
\(m\)-dimensional remainder space.

### Theorem 1.1 — Explicit cyclotomic differential

Fix \(\lambda\ne0\), put

\&#91;
Q_0=w^m-\lambda,
\&#93;

and write

\&#91;
\nu=km+r,
\qquad
k\ge1,
\qquad
0\le r&lt;m.
\&#93;

Identify the tangent space at \(Q_0\) with \(k&#91;w&#93;_{&lt;m}\).  Then

\&#91;
d\mathcal R_\nu\big|_{Q_0}(\delta Q)
=-k\lambda^{k-1}
 \bigl(w^r\delta Q\bmod(w^m-\lambda)\bigr).
\&#93;

In particular, this differential is invertible whenever \(k\) and
\(\lambda\) are units.  Over a characteristic-zero field, the remainder map
is étale at every \(Q_0=w^m-\lambda\) and every \(\nu\ge m\).

### Proof

Work over the dual numbers and write

\&#91;
Q_\epsilon=w^m-\lambda+\epsilon\delta Q,
\qquad \epsilon^2=0.
\&#93;

In the quotient by \(Q_\epsilon\),

\&#91;
w^m=\lambda-\epsilon\delta Q.
\&#93;

Hence

\&#91;
\begin{aligned}
w^\nu
&amp;=w^r(w^m)^k\\
&amp;=w^r(\lambda-\epsilon\delta Q)^k\\
&amp;=\lambda^kw^r
 -k\lambda^{k-1}\epsilon w^r\delta Q.
\end{aligned}
\&#93;

Reducing the last product modulo \(w^m-\lambda\) gives the formula.
Multiplication by \(w^r\) is an automorphism of
\(k&#91;w&#93;/(w^m-\lambda)\), because \(w^m=\lambda\) is a unit. ∎

### Determinant

In the ascending monomial basis, multiplication by \(w\) modulo
\(w^m-\lambda\) has determinant

\&#91;
(-1)^{m-1}\lambda.
\&#93;

Therefore

\&#91;
\det d\mathcal R_\nu|_{Q_0}
=
(-k\lambda^{k-1})^m
\bigl((-1)^{m-1}\lambda\bigr)^r.
\&#93;

This is the precise replacement for the earlier unsupported sentence that a
“deepest cyclotomic cell is étale.”  When \(r=0\), the remainder is constant
and the differential is the scalar
\(-k\lambda^{k-1}\operatorname{id}\).

## 2. The companion--Krylov matrix is triangularly Hankel

Let \(C\) be multiplication by \(w\) on \(k&#91;w&#93;/(Q)\) in the ascending basis

\&#91;
1,w,\ldots,w^{m-1},
\&#93;

and let \(J\) reverse that basis.  The matrix

\&#91;
K_\nu=JC^\nu
\&#93;

has as its \(j\)-th column the coefficients of
\(w^{\nu+j}\bmod Q\), written in descending order.

Put

\&#91;
R_\nu=w^\nu\bmod Q
\&#93;

and expand at infinity

\&#91;
\frac{R_\nu(w)}{Q(w)}
=\sum_{\ell\ge1}s_\ell w^{-\ell}.
\&#93;

Define the symmetric Hankel matrix

\&#91;
H_\nu=(s_{i+j+1})_{0\le i,j&lt;m}.
\&#93;

Finally, with \(q_0=1\), let

\&#91;
L_Q=(q_{i-j})_{0\le j\le i&lt;m}
\&#93;

be the unit lower-triangular Toeplitz matrix.

### Theorem 2.1 — Exact triangular reduction

One has the identity

\&#91;
\boxed{K_\nu=L_QH_\nu.}
\&#93;

Consequently \(K_\nu\) and \(H_\nu\) have identical ranks for every
northwest rectangular prefix, and hence the same rank-profile permutation.

### Proof

The proper part of

\&#91;
w^j\frac{R_\nu}{Q}
\&#93;

is

\&#91;
\frac{w^{\nu+j}\bmod Q}{Q}.
\&#93;

Its Laurent coefficients are therefore
\(s_{j+1},s_{j+2},\ldots\).  If

\&#91;
w^{\nu+j}\bmod Q
=\sum_{a=0}^{m-1}r_{a,j}w^a,
\&#93;

then multiplying the Laurent series by

\&#91;
Q=w^m+q_1w^{m-1}+\cdots+q_m
\&#93;

gives

\&#91;
r_{m-1-i,j}
=\sum_{b=0}^i q_{i-b}s_{b+j+1}.
\&#93;

This is exactly the matrix identity.  Since every leading square block of
\(L_Q\) is invertible, left multiplication by \(L_Q\) preserves every
northwest prefix rank. ∎

This removes a convention problem in the retained theorem: the displayed
companion matrix need not itself look symmetric.  It is related by a fixed
unit lower-triangular operation to the genuine moment Hankel matrix.

## 3. The first normal block is always a reversal

Let

\&#91;
H=(s_{i+j+1})_{0\le i,j&lt;N}
\&#93;

be a scalar Hankel matrix.  Suppose its first nonsingular leading principal
minor has size \(d\):

\&#91;
\det H_k=0\quad(1\le k&lt;d),
\qquad
\det H_d\ne0.
\&#93;

### Theorem 3.1 — First-gap reversal lemma

Then

\&#91;
s_1=\cdots=s_{d-1}=0,
\qquad
s_d\ne0,
\&#93;

and, for \(1\le a,b\le d\),

\&#91;
\operatorname{rank}H_{&#91;1,a&#93;\times&#91;1,b&#93;}
=\max(0,a+b-d).
\&#93;

Thus the northwest rank-profile permutation on the first \(d\) rows and
columns is exactly the reversal matrix \(J_d\).

### Proof

Induct on \(k\).  If
\(s_1=\cdots=s_{k-1}=0\), then the leading \(k\times k\) Hankel determinant is

\&#91;
\det H_k
=(-1)^{k(k-1)/2}s_k^k.
\&#93;

The vanishing and nonvanishing assumptions therefore give the first claim.

For an \(a\times b\) northwest rectangle with \(a,b\le d\), every entry with
\(i+j&lt;d-1\) is zero.  Hence at most

\&#91;
t=\max(0,a+b-d)
\&#93;

rows can be nonzero.  The final \(t\) relevant rows and columns contain an
anti-triangular \(t\times t\) minor with anti-diagonal entry \(s_d\), so its
rank is exactly \(t\). ∎

## 4. The rank-profile recursion is now complete

The first-gap lemma in this note is the initial case of the general argument
proved in `lane2_all_rank_hankel_rank_profile.md`.  That proof uses the moment
functional and monic orthogonal residual polynomial at each normal index.  It
shows that the next Schur-complement block is unit-triangularly congruent to a
Hankel matrix whose first nonzero moment lies on its anti-diagonal.  Hence every
normal-index gap contributes exactly one reversal block, and iteration gives

\&#91;
J_{d_1}\oplus\cdots\oplus J_{d_s}.
\&#93;

No quasi-Hankel continuation hypothesis remains.

## 5. Filtered Smith exponents after the rank profile

Suppose the resulting Bruhat factorization is

\&#91;
H_\nu=LPU,
\&#93;

with \(L\) unit lower triangular, \(U\) unit upper triangular, and

\&#91;
P=J_{d_1}\oplus\cdots\oplus J_{d_s},
\qquad
d_j=n_j-n_{j-1}.
\&#93;

Under the radial deformation

\&#91;
Q_r(w)=r^mQ(w/r),
\&#93;

the regular conjugated lower and upper factors remain unimodular over
\(k&#91;&#91;r&#93;&#93;\).  A pivot in row \(i\), column \(\pi(i)\) has full exponent

\&#91;
\nu-m+1+i+\pi(i).
\&#93;

On the reversal block with indices
\(n_{j-1},\ldots,n_j-1\),

\&#91;
i+\pi(i)=n_{j-1}+n_j-1.
\&#93;

Therefore the Smith exponent on that block is

\&#91;
\boxed{\nu-m+n_{j-1}+n_j}
\&#93;

with multiplicity \(d_j\).

The determinant check telescopes:

\&#91;
\sum_jd_j(\nu-m+n_{j-1}+n_j)=m\nu.
\&#93;

Hence the filtered Smith statement is unconditional once combined with the
normal-index rank-profile theorem proved in the companion note.

## 6. Revised proof dependency for `RMU-4D2E0001`

The retained theorem can be split into five auditable pieces:

| piece | status after this note |
|---|---|
| cyclotomic remainder coordinates | proved, with explicit Jacobian |
| companion--Krylov to Hankel reduction | proved by \(K_\nu=L_QH_\nu\) |
| first normal block | proved directly |
| later block recursion | proved by orthogonal-residual Schur-complement induction |
| radial Smith exponents | proved from the block-reversal permutation |

The principal-subresultant/Hankel-determinant/rectangular-Schur identity is
proved in `lane2_all_rank_psc_hankel_schur.md`, and the full normal-index block
recursion is proved in `lane2_all_rank_hankel_rank_profile.md`.  Thus no
load-bearing general-rank linear-algebra step remains in this local theorem.

## 7. Literature bridge to audit

Two primary references provide an external literature bridge for the completed
block-factorization theorem:

- D. Pal and T. Kailath, *Fast Triangular Factorization and Inversion of Hankel
  and Related Matrices with Arbitrary Rank Profile*, SIAM J. Matrix Anal.
  Appl., DOI `10.1137/S0895479889172643`.
- A. Taik and S. Belhaj, *Block Factorization of Hankel Matrices and Euclidean
  Algorithm*, Math. Model. Nat. Phenom. 5 (2010).

The present proof is self-contained in the program's conventions; these
references now serve as independent structural context rather than as a
missing proof dependency.
</code></pre>

<a id="source-209248dda0cb15da"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_m5_composition_grid_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Deterministic exact rank-profile and Smith regression for m=5.

Grid:
    q_i in {-1,0,1}, q_5 != 0, and 5 &lt;= nu &lt;= 15.
For every case, the script computes Euclidean normal indices, the northwest
rank profile of the reversed companion Krylov matrix, and all radial Smith
exponents from determinantal valuations.
"""
from __future__ import annotations

from itertools import combinations, product
import sympy as sp

w = sp.symbols("w")


def companion(coeffs: tuple&#91;int, ...&#93;) -&gt; sp.Matrix:
    m = len(coeffs)
    matrix = sp.zeros(m)
    for j in range(m-1):
        matrix&#91;j+1, j&#93; = 1
    for i in range(m):
        matrix&#91;i, m-1&#93; = -coeffs&#91;m-1-i&#93;
    return matrix


def normal_indices(coeffs: tuple&#91;int, ...&#93;, nu: int) -&gt; list&#91;int&#93;:
    m = len(coeffs)
    polynomial = w**m + sum(sp.Integer(coeffs&#91;i&#93;)*w**(m-1-i) for i in range(m))
    left = sp.Poly(w**nu, w, domain=sp.QQ)
    right = sp.Poly(polynomial, w, domain=sp.QQ)
    indices = &#91;0&#93;
    while True:
        remainder = left.rem(right)
        if remainder.is_zero:
            raise AssertionError("unexpected non-coprime pair")
        indices.append(m-remainder.degree())
        if remainder.degree() == 0:
            return indices
        left, right = right, remainder


def block_reversal(composition: tuple&#91;int, ...&#93;) -&gt; sp.Matrix:
    m = sum(composition)
    permutation = sp.zeros(m)
    offset = 0
    for block in composition:
        for i in range(block):
            permutation&#91;offset+i, offset+block-1-i&#93; = 1
        offset += block
    return permutation


def same_northwest_ranks(left: sp.Matrix, right: sp.Matrix) -&gt; tuple&#91;bool, tuple&#91;int, int&#93; | None&#93;:
    m = left.rows
    for rows in range(1, m+1):
        for columns in range(1, m+1):
            if left&#91;:rows, :columns&#93;.rank() != right&#91;:rows, :columns&#93;.rank():
                return False, (rows, columns)
    return True, None


def smith_exponents(matrix: sp.Matrix, nu: int) -&gt; tuple&#91;int, ...&#93;:
    """Valuations after C_r^nu=r^nu D^{-1} C^nu D."""
    m = matrix.rows
    determinantal_valuations = &#91;0&#93;
    for size in range(1, m+1):
        best: int | None = None
        for rows in combinations(range(m), size):
            for columns in combinations(range(m), size):
                if matrix.extract(rows, columns).det() == 0:
                    continue
                value = size*nu + sum(columns)-sum(rows)
                best = value if best is None else min(best, value)
        if best is None:
            raise AssertionError("full companion power unexpectedly singular")
        determinantal_valuations.append(best)
    return tuple(
        determinantal_valuations&#91;i&#93;-determinantal_valuations&#91;i-1&#93;
        for i in range(1, m+1)
    )


def predicted_exponents(indices: list&#91;int&#93;, nu: int, m: int) -&gt; tuple&#91;int, ...&#93;:
    return tuple(
        exponent
        for left, right in zip(indices, indices&#91;1:&#93;)
        for exponent in &#91;nu-m+left+right&#93;*(right-left)
    )


def main() -&gt; None:
    counts: dict&#91;tuple&#91;int, ...&#93;, int&#93; = {}
    checked = 0
    reversal = sp.zeros(5)
    for i in range(5):
        reversal&#91;i, 4-i&#93; = 1

    for coeffs in product(range(-1, 2), repeat=5):
        if coeffs&#91;-1&#93; == 0:
            continue
        matrix = companion(coeffs)
        for nu in range(5, 16):
            indices = normal_indices(coeffs, nu)
            composition = tuple(right-left for left, right in zip(indices, indices&#91;1:&#93;))
            counts&#91;composition&#93; = counts.get(composition, 0)+1

            power = matrix**nu
            okay, position = same_northwest_ranks(
                reversal*power,
                block_reversal(composition),
            )
            if not okay:
                raise AssertionError(("rank-profile failure", coeffs, nu, composition, position))

            actual = smith_exponents(power, nu)
            predicted = predicted_exponents(indices, nu, 5)
            if actual != predicted:
                raise AssertionError(("Smith failure", coeffs, nu, composition, actual, predicted))
            checked += 1

    expected_compositions = {
        (1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 1, 2, 1), (1, 1, 3),
        (1, 2, 1, 1), (1, 2, 2), (1, 3, 1), (1, 4),
        (2, 1, 1, 1), (2, 1, 2), (2, 2, 1), (2, 3),
        (3, 1, 1), (3, 2), (4, 1), (5,),
    }
    assert set(counts) == expected_compositions
    assert checked == 1782

    print(f"exact cases checked: {checked}")
    print(f"ordered compositions realized: {len(counts)} of 16")
    for composition in sorted(counts):
        print(f"{composition}: {counts&#91;composition&#93;}")
    print("ALL M=5 COMPOSITION-GRID CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-46df9b7e598d9f8f"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_m5_nu5_actual_flag_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for the actual complete-PRS coefficient model at (m,nu)=(5,5).

We work on the transverse cyclotomic slice
    Q = w^5 - A w^4 - B w^3 - C w^2 - D w - 1,
so w^5 mod Q = A w^4 + B w^3 + C w^2 + D w + 1.
All identities are over ZZ and hence valid in characteristic zero.
"""
from __future__ import annotations

import sympy as sp

w = sp.symbols("w")
A, B, C, D = sp.symbols("A B C D")
u, v = sp.symbols("u v")
x, y, z, t = sp.symbols("x y z t")
lam, mu = sp.symbols("lam mu")


def main() -&gt; None:
    Q = w**5 - A*w**4 - B*w**3 - C*w**2 - D*w - 1
    chain = sp.subresultants(w**5, Q, w)
    by_degree = {sp.degree(p, w): sp.Poly(sp.expand(p), w) for p in chain}

    s3 = by_degree&#91;3&#93;
    s2 = by_degree&#91;2&#93;
    s1 = by_degree&#91;1&#93;

    X = B**2 - A*C
    Y = A*D - B*C
    Z = C**2 - B*D

    # Degree-three and degree-two subresultants.
    assert sp.expand(s3.as_expr() - (X*w**3 - Y*w**2 + (B*D-A)*w + B)) == 0
    U = X + D*Y + C*Z
    V = Y + D*Z
    assert sp.expand(s2.as_expr() + U*w**2 + V*w + Z) == 0

    P = -A + 2*B*D + C**2 - 3*C*D**2 + D**4
    T = B - 2*C*D + D**3
    assert sp.expand(s1.as_expr() - (P*w + T)) == 0

    # Exact Hilbert--Burch syzygies for the twisted-cubic center.
    assert sp.expand(D*X + C*Y + B*Z) == 0
    assert sp.expand(C*X + B*Y + A*Z) == 0

    # The degree-two coefficient ideal is exactly (X,Y,Z).
    assert sp.expand(V - (Y + D*Z)) == 0
    assert sp.expand(U - (X + D*V + (C-D**2)*Z)) == 0

    # W=Z chart of the middle graph; solve its two linear syzygies exactly.
    Amid = -C*u + D*u*v + C*v**2
    Bmid = -D*u - C*v
    assert sp.expand(D*u + C*v + Bmid) == 0
    assert sp.expand(C*u + Bmid*v + Amid) == 0
    Zpull = sp.expand(Z.subs({A: Amid, B: Bmid}))
    assert Zpull == C**2 + C*D*v + D**2*u

    # Exact top restriction and exact bottom parametrization.
    assert tuple(sp.expand(e.subs({A: 0, B: 0})) for e in (X, Y, Z)) == (0, 0, C**2)
    Abot = C**2 + C*D**2 - D**4
    Bbot = D*(2*C-D**2)
    kappa = C-D**2
    assert tuple(sp.factor(e.subs({A: Abot, B: Bbot})) for e in (X, Y, Z)) == (
        -kappa**3,
        -D*kappa**2,
        kappa**2,
    )

    # The two outer centers meet in the explicit length-six complete intersection.
    f = D*(2*C-D**2)
    g = C**2 + C*D**2 - D**4
    assert sp.factor(sp.resultant(f, g, C)) == -D**6
    assert sp.factor(sp.resultant(f, g, D)) == C**6
    gb = sp.groebner(&#91;f, g&#93;, C, D, order="lex")
    assert &#91;sp.expand(p.as_expr()) for p in gb.polys&#93; == &#91;
        2*C**2-D**4,
        2*C*D-D**3,
        D**5,
    &#93;

    # Exact universal-node form of the top factor.
    Atop = sp.expand(Amid + v*Bmid)
    assert Atop == -C*u
    assert Bmid == -(D*u+C*v)

    # Exact universal-node form of the bottom factor.
    Ppull = sp.expand(P.subs({A: Amid, B: Bmid}))
    Tpull = sp.expand(T.subs({A: Amid, B: Bmid}))
    rho = u + C + D*v
    s = v + D
    assert sp.expand(Tpull + D*rho + kappa*s) == 0
    assert sp.expand(Ppull - s*Tpull - kappa*rho) == 0

    # The coordinate change between the two node models is a polynomial automorphism.
    xp = x-y**2
    yp = y
    zp = z+x+y*t
    tp = t+y
    xback = sp.expand(xp+y**2)
    tback = sp.expand(tp-y)
    zback = sp.expand(zp-xp-y*tp)
    assert (xback, yp, zback, tback) == (x, y, z, t)

    # It is the time-one map of a locally nilpotent derivation on the generators.
    # delta(x)=-y^2, delta(y)=0, delta(t)=y, delta(z)=x+yt, and delta^2(z)=0.
    assert sp.expand((-y**2) + y*y) == 0

    # Every individual outer graph chart is an exact ODP times its projective parameter.
    node = y*z + x*t - lam*x*z
    shifted = sp.expand(node.subs(t, t+lam*z))
    assert shifted == x*t + y*z
    assert sp.factor(sp.hessian(x*t+y*z, (x, t, y, z)).det()) == 1

    # Saturated simultaneous quadratic model.
    f0 = x*z
    g0 = y*z+x*t
    f1 = x*(z+x)
    g1 = y*(z+x)+x*(t+y)
    E0 = sp.expand(g0-lam*f0)
    E1 = sp.expand(g1-mu*f1)
    K = 2*y+(lam-mu)*z-mu*x
    assert sp.expand(E1-E0-x*K) == 0
    ysol = (mu*x-(lam-mu)*z)/2
    reduced = sp.expand(2*E0.subs(y, ysol))
    assert sp.expand(reduced - (2*x*t + (mu-2*lam)*x*z - (lam-mu)*z**2)) == 0
    tau = sp.symbols("tau")
    reduced_shift = sp.expand(reduced.subs(t, tau-(mu-2*lam)*z/2))
    assert sp.expand(reduced_shift - (2*x*tau-(lam-mu)*z**2)) == 0

    # The symmetric blowup of the toric singular locus resolves the quadratic model.
    Xc, Tc, Zc, alpha = sp.symbols("Xc Tc Zc alpha")
    model = Xc*Tc+alpha*Zc**2
    # X-chart: Tc=Xc*T1, Zc=Xc*Z1.
    T1, Z1 = sp.symbols("T1 Z1")
    strict_x = sp.expand(model.subs({Tc: Xc*T1, Zc: Xc*Z1}) / Xc**2)
    assert strict_x == T1+alpha*Z1**2
    # T-chart.
    X1 = sp.symbols("X1")
    strict_t = sp.expand(model.subs({Xc: Tc*X1, Zc: Tc*Z1}) / Tc**2)
    assert strict_t == X1+alpha*Z1**2
    # Z-chart.
    strict_z = sp.expand(model.subs({Xc: Zc*X1, Tc: Zc*T1}) / Zc**2)
    assert strict_z == X1*T1+alpha

    print("actual subresultant formulas: passed")
    print("exact twisted-cubic middle center and smooth graph charts: passed")
    print("top and bottom doubled contacts: passed")
    print("outer-center intersection algebra: length 6")
    print("both outer graph factors: exact universal ODP models")
    print("simultaneous quadratic graph: quartic toric model x smooth parameter")
    print("ALL ACTUAL (m,nu)=(5,5) COMPLETE-PRS LOCAL CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-a390d36f88cafaa0"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802a/lane2_m5_nu5_actual_prs_flag.md`

<pre><code class="language-markdown">
# The actual quintic complete-PRS flag at \((m,\nu)=(5,5)\)

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact symbolic replay supplied.
&gt; **Scope:** the formal coefficient-space neighborhood of the cyclotomic point
&gt; \(Q=w^5-1\), after fixing the smooth constant-remainder parameter.  The
&gt; corresponding neighborhood along \(Q=w^5-\lambda\), \(\lambda\ne0\), is
&gt; obtained after an étale scalar normalization.  This note does not prove the
&gt; all-\(\nu\) or all-rank logarithmic theorem.

## 1. Why this is a correction

A previous exploratory note varied the second polynomial while keeping
\(Q=w^5-1\) fixed.  That is a useful universal two-polynomial slice, but it is
not the actual \(\nu=5\) coefficient-space relation.  In the coefficient
space one has

\&#91;
Q=w^5-Aw^4-Bw^3-Cw^2-Dw-1,
\&#93;

and therefore

\&#91;
w^5\bmod Q=Aw^4+Bw^3+Cw^2+Dw+1.
\&#93;

The actual subresultant flag is substantially cleaner: its middle center is
*exactly* the twisted-cubic determinantal cone.

## 2. Exact subresultants

Put

\&#91;
X=B^2-AC,\qquad
Y=AD-BC,\qquad
Z=C^2-BD.
\&#93;

With the Sylvester convention used by the exact replay,

\&#91;
\operatorname{Sres}_3(w^5,Q)
 =Xw^3-Yw^2+(BD-A)w+B.
\&#93;

The degree-two subresultant is

\&#91;
\operatorname{Sres}_2(w^5,Q)
 =-Uw^2-Vw-Z,
\&#93;

where

\&#91;
V=Y+DZ,
\qquad
U=X+DY+CZ=X+DV+(C-D^2)Z.
\&#93;

Finally,

\&#91;
\operatorname{Sres}_1(w^5,Q)=Pw+T
\&#93;

with

\&#91;
P=-A+2BD+C^2-3CD^2+D^4,
\qquad
T=B-2CD+D^3.
\&#93;

Consequently the three nontrivial projective base ideals are

\&#91;
I_3=(A,B),
\qquad
I_2=(X,Y,Z),
\qquad
I_1=(P,T).
\&#93;

The first and last centers are smooth codimension-two surfaces.  The middle
center is the affine cone over the twisted cubic.

## 3. The middle center is exactly determinantal

The generators satisfy the exact Hilbert--Burch syzygies

\&#91;
DX+CY+BZ=0,
\qquad
CX+BY+AZ=0.
\&#93;

Equivalently, \(I_2\) is the maximal-minor ideal of

\&#91;
\begin{pmatrix}
D&amp;C\\
C&amp;B\\
B&amp;A
\end{pmatrix}.
\&#93;

Thus there are no hidden tangent-cone equations: the center itself is already

\&#91;
V(B^2-AC,\ AD-BC,\ C^2-BD).
\&#93;

The projective graph is the incidence in
\(\mathbb A^4_{A,B,C,D}\times\mathbb P^2_{&#91;\mathsf X:\mathsf Y:\mathsf Z&#93;}\)
cut out by

\&#91;
D\mathsf X+C\mathsf Y+B\mathsf Z=0,
\qquad
C\mathsf X+B\mathsf Y+A\mathsf Z=0.
\&#93;

It is smooth.  Away from the center this is the ordinary graph.  On the
center away from the cone vertex it is the blowup of a smooth codimension-two
subscheme.  At the vertex, the three projective charts have independent
linear differentials; the fiber is the full \(\mathbb P^2\), since the
quadratic map \((A,B,C,D)\mapsto(X,Y,Z)\) is dominant.

### Exact \(\mathsf Z\)-chart

Write

\&#91;
u=\mathsf X/\mathsf Z,
\qquad
v=\mathsf Y/\mathsf Z.
\&#93;

The two incidence equations solve exactly as

\&#91;
B=-Du-Cv,
\qquad
A=-Cu+Duv+Cv^2.
\&#93;

Hence this graph chart is the affine four-space
\(\mathbb A^4_{C,D,u,v}\).

The pulled-back middle ideal is principal, generated by

\&#91;
Z=C^2+CDv+D^2u.
\&#93;

## 4. Smooth graph versus logarithmic boundary

Although the middle graph is smooth, its exceptional divisor is singular
along the deepest \(\mathbb P^2\)-fiber.  On the \(\mathsf Z\)-chart this
fiber is \(F=V(C,D)\).

Blow up \(F\).  On the chart \(C=D\lambda\), the strict exceptional equation
is

\&#91;
\lambda^2+v\lambda+u=0.
\&#93;

Its derivative with respect to \(u\) is a unit.  The analogous second chart is
also smooth.  Globally, the intersection of the new exceptional divisor with
the strict middle divisor is the double cover of
\(\mathbb P^2_{&#91;\mathsf X:\mathsf Y:\mathsf Z&#93;}\) branched over

\&#91;
\mathsf Y^2-4\mathsf X\mathsf Z=0.
\&#93;

Thus the graph and its first logarithmic repair are distinct even in this
smallest quintic flag.

## 5. Exact top and bottom contacts

On the top center \(I_3=(A,B)\),

\&#91;
(X,Y,Z)=(0,0,C^2).
\&#93;

Its strict lift to the \(\mathsf Z\)-chart is therefore

\&#91;
L_3':\quad u=v=0.
\&#93;

For the bottom center, solving \(P=T=0\) gives

\&#91;
B=D(2C-D^2),
\qquad
A=C^2+CD^2-D^4.
\&#93;

Put \(\kappa=C-D^2\).  Then exactly

\&#91;
(X,Y,Z)=\kappa^2(-\kappa,-D,1).
\&#93;

Its strict lift is

\&#91;
L_1':\quad u=D^2-C,\qquad v=-D.
\&#93;

Both restrictions of the middle ideal are doubled Cartier contacts:

\&#91;
I_2\mathcal O_{L_3}=(C^2),
\qquad
I_2\mathcal O_{L_1}=(\kappa^2).
\&#93;

The strict lifts \(L_3'\) and \(L_1'\) are smooth and meet transversely at the
single deepest point in the smooth middle graph.

### The original intersection algebra

Before adjoining the middle direction, the outer centers meet in

\&#91;
\frac{k&#91;&#91;C,D&#93;&#93;}
{\bigl(D(2C-D^2),\ C^2+CD^2-D^4\bigr)}.
\&#93;

A Gröbner basis is

\&#91;
2C^2-D^4,
\qquad
2CD-D^3,
\qquad
D^5,
\&#93;

so the intersection has length six, with basis

\&#91;
1,\ C,\ D,\ D^2,\ D^3,\ D^4.
\&#93;

Thus the middle graph converts an order-six contact into a transverse reduced
intersection of the strict lifts.  It does **not**, however, automatically
resolve the two pulled-back projective ideals.

## 6. Both outer graph factors have one exact universal form

### Top factor

On the middle graph,

\&#91;
A+vB=-Cu,
\qquad
B=-(Du+Cv).
\&#93;

After an invertible projective change of the two generators, the top factor is
therefore the graph of

\&#91;
&#91;Cu:Du+Cv&#93;.
\&#93;

### Bottom factor

Put

\&#91;
\kappa=C-D^2,
\qquad
\rho=u+C+Dv,
\qquad
s=v+D.
\&#93;

Then

\&#91;
T=-(D\rho+\kappa s),
\qquad
P-sT=\kappa\rho.
\&#93;

After another invertible projective change, the bottom factor is the graph of

\&#91;
&#91;\kappa\rho:D\rho+\kappa s&#93;.
\&#93;

Hence both factors are copies of the universal ideal

\&#91;
J=(xz,\ yz+xt)\subset k&#91;x,y,z,t&#93;.
\&#93;

The coordinate systems are related by the polynomial automorphism

\&#91;
\tau(x,y,z,t)
=(x-y^2,\ y,\ z+x+yt,\ t+y).
\&#93;

Its inverse is

\&#91;
(x',y,z',t')
\longmapsto
(x'+y^2,\ y,\ z'-x'-yt',\ t'-y).
\&#93;

Moreover,

\&#91;
\tau=\exp(\partial),
\&#93;

where

\&#91;
\partial
=-y^2\partial_x+y\partial_t+(x+yt)\partial_z
\&#93;

is locally nilpotent on the four coordinate generators.  This identifies the
change from the top node model to the bottom node model as an exact unipotent
translation, not merely a coincidence of quadratic jets.

## 7. Exact individual graph singularities

On an affine projective chart of the graph of \(J\), with ratio \(\lambda\),
the equation is

\&#91;
yz+xt-\lambda xz=0.
\&#93;

After replacing \(t\) by \(t-\lambda z\), this becomes

\&#91;
xt+yz=0.
\&#93;

Therefore each outer graph factor is exactly a threefold ordinary double
point times the smooth projective parameter.  Its singular locus is the
\(\mathbb P^1\) over the deepest coefficient point.  Blowing up that line is
a symmetric resolution with quadric exceptional fibers; the two small
resolutions are related by the fiberwise Atiyah flop.

This exact normal form supersedes the earlier conclusion based only on the
2-jet.

## 8. The simultaneous quadratic model recycles the quartic toric chart

The remaining issue is the simultaneous graph of \(J\) and \(\tau^*J\).  Its
full higher-order Rees algebra is not yet determined.  Its saturated quadratic
model can nevertheless be computed exactly.

The linear part of \(\tau\) is

\&#91;
\tau_1(x,y,z,t)=(x,y,z+x,t+y).
\&#93;

Thus the two leading pairs are

\&#91;
(f_0,g_0)=(xz,\ yz+xt),
\&#93;

\&#91;
(f_1,g_1)=(x(z+x),\ y(z+x)+x(t+y)).
\&#93;

On the product chart with ratios \(\lambda,\mu\), put

\&#91;
E_0=g_0-\lambda f_0,
\qquad
E_1=g_1-\mu f_1.
\&#93;

Then

\&#91;
E_1-E_0
=x\bigl(2y+(\lambda-\mu)z-\mu x\bigr).
\&#93;

After saturation by the selected first homogeneous coordinates, the closure
is cut out by \(E_0\) and

\&#91;
K=2y+(\lambda-\mu)z-\mu x.
\&#93;

Eliminating \(y\), then replacing

\&#91;
T=t+\frac{\mu-2\lambda}{2}z,
\qquad
a=\frac{\mu-\lambda}{2},
\&#93;

gives

\&#91;
xT+az^2=0.
\&#93;

The complementary combination \((\lambda+\mu)/2\) is a smooth parameter.
Consequently the simultaneous quadratic graph is exactly the quartic toric
singularity

\&#91;
XY+AZ^2=0
\&#93;

times a smooth line.

Its reduced singular locus is \(V(X,Y,Z)\).  Blowing up that locus resolves
it: the three strict-transform charts are

\&#91;
Y_1+AZ_1^2=0,
\qquad
X_1+AZ_1^2=0,
\qquad
X_1Y_1+A=0.
\&#93;

The same five-ray fan from the quartic overlap therefore resolves the leading
simultaneous quintic model, and the two ordered resolutions are related by the
same two crepant toric flops, now with one extra smooth parameter.

This proves compatibility of the **normal model**.  Lifting the fan to the
full higher-order simultaneous Rees algebra is the next exact lemma; it is not
silently assumed here.

## 9. Consequences

The actual \((5,5)\) coefficient-space flag now has the following verified
structure:

1. the middle base ideal is exactly the twisted-cubic determinantal ideal;
2. its projective graph is smooth;
3. its exceptional divisor has a canonical conic-branched logarithmic repair;
4. the two outer centers have doubled contact with the middle center and an
   explicit length-six mutual intersection;
5. after adjoining the middle direction, their strict lifts are transverse;
6. each pulled-back outer projective graph is an exact family of ordinary
   double points;
7. the two node models are related by an explicit unipotent polynomial
   automorphism;
8. their simultaneous quadratic graph is the already-solved quartic toric
   singularity times a smooth parameter.

The remaining local quintic task is now narrow: compute the saturated full
multi-Rees algebra of \(J\) and \(\tau^*J\), and prove that the symmetric or
ordered toric modifications of its normal model lift to the exact graph.
</code></pre>

<a id="source-794624f89288ba28"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_saturated_multirees_equations.md`

<pre><code class="language-markdown">
# Exact saturated equations for the finite–finite unordered chart

&gt; **Status:** exact algebraic certificate accompanying the cubic-scroll normalization theorem.
&gt; **Scope:** the universal pair `(J_0,J_1)` after normalizing the nonzero translation parameter to one.

Let

\&#91;
T=t-\lambda z,
\qquad
J_0=(xz,yz+xt),
\qquad
J_1=((x-y^2)(z+x+yt),\ xt+yz+2xy-y^3).
\&#93;

Let `rho` denote the finite ratio on the second projective factor.  The naive
two-equation incidence ideal is

\&#91;
I_{\mathrm{naive}}
=(xT+yz,\ g_1-\rho f_1).
\&#93;

It contains torsion supported on the common base locus.  The graph closure is
the saturation

\&#91;
I_{\mathrm{graph}}
=I_{\mathrm{naive}}:(xz\,f_1)^\infty.
\&#93;

Define

\&#91;
\begin{aligned}
A_1={}&amp;-T\rho y^2-\lambda yz+\rho xy-\rho y^3-\rho yz-y^2,\\
A_2={}&amp;\lambda\rho yz-\lambda z+\rho x-\rho y^2+\rho z-2y,
\end{aligned}
\&#93;

and

\&#91;
M_{\lambda,\rho}
=
\begin{pmatrix}
A_1&amp;A_2\\
x-y^2&amp;-y\\
Ty+z&amp;T
\end{pmatrix}.
\&#93;

## Proposition

The saturated graph ideal is exactly

\&#91;
\boxed{I_{\mathrm{graph}}=I_2(M_{\lambda,\rho}).}
\&#93;

The lower minor is

\&#91;
T(x-y^2)+y(Ty+z)=xT+yz.
\&#93;

The other two minors are the two Sylvester forms obtained when the second
graph equation is saturated by the two selected source generators.  The
matrix gives their Hilbert--Burch syzygies automatically.

The supplied replay proves the equality in two independent exact ways:

1. elimination of an auxiliary variable from
   \&#91;
   (I_{\mathrm{naive}},1-hxz f_1);
   \&#93;
2. mutual reduction of the elimination basis and the three maximal minors.

Thus the unordered chart is a codimension-two perfect determinantal scheme,
not the naive complete intersection of the two graph equations.

Its Jacobian singular ideal has radical

\&#91;
\sqrt{\operatorname{Jac}(I_{\mathrm{graph}})}=(x,y,z).
\&#93;

Hence the chart is singular in codimension one and is not normal.  On `T != 0`
the companion theorem transforms it exactly to

\&#91;
\alpha z^2=u^2B,
\&#93;

whose normalization is the cubic-scroll cone.
</code></pre>

<a id="source-25b301a7bd7faa22"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact replay for the unordered quintic outer-graph normalization theorem."""
from __future__ import annotations

import sympy as sp


def main() -&gt; None:
    x, y, z, t = sp.symbols("x y z t")
    T, lam, rho, theta = sp.symbols("T lam rho theta")
    u, alpha, B = sp.symbols("u alpha B")

    f0 = x*z
    g0 = y*z + x*t
    f1 = (x-y**2)*(z+x+y*t)
    g1 = x*t + y*z + 2*x*y - y**3

    # First graph and T-unit coordinates.
    first = sp.expand((g0-lam*f0).subs(t, T+lam*z))
    assert first == x*T+y*z

    x_sub = -y*z/T
    f1_first = sp.factor(f1.subs({t:T+lam*z, x:x_sub}, simultaneous=True))
    g1_first = sp.factor(g1.subs({t:T+lam*z, x:x_sub}, simultaneous=True))
    assert sp.simplify(f1_first/y + (T*y+z)*(T**2*y+T*lam*y*z+T*z-y*z)/T**2) == 0
    assert sp.simplify(g1_first/y + (T*y**2+lam*z**2+2*y*z)/T) == 0

    # u=Ty+z, alpha=1-T lambda.
    y_sub = (u-z)/T
    Fstar = u*(T**2*u-alpha*u*z+alpha*z**2)
    Gstar = T*(u**2-alpha*z**2)

    fweak_scaled = sp.factor((-T**3*f1_first/y).subs({y:y_sub, lam:(1-alpha)/T}))
    gweak_scaled = sp.factor((-T**3*g1_first/y).subs({y:y_sub, lam:(1-alpha)/T}))
    assert sp.expand(fweak_scaled-Fstar) == 0
    assert sp.expand(gweak_scaled-Gstar) == 0

    # Finite second direction and exact pinch coordinate.
    D = T+rho*u
    beta = 1-rho*T
    Bexpr = (T*beta+rho*alpha*z)/D
    Efin = sp.expand(rho*Fstar-Gstar)
    assert sp.factor(Efin-D*(alpha*z**2-u**2*Bexpr)) == 0

    rho_inv = T*(1-B)/(T**2+B*u-alpha*z)
    assert sp.factor(Bexpr.subs(rho,rho_inv)-B) == 0

    # Normalization relations and the two smooth conductor-blowup charts.
    q, p, w = sp.symbols("q p w")
    pinch = alpha*z**2-u**2*B
    strict_u = sp.expand(pinch.subs({z:q*u, B:alpha*q**2})/u**2)
    strict_z = sp.expand(pinch.subs({u:p*z, alpha:B*p**2})/z**2)
    assert strict_u == 0
    assert strict_z == 0
    assert sp.expand((alpha*q)**2-alpha*(alpha*q**2)) == 0
    assert sp.expand((B*p)**2-(B*p**2)*B) == 0
    assert sp.expand((alpha*q)*u-alpha*(q*u)) == 0
    assert sp.expand((B*p)*z-B*(p*z)) == 0

    # Infinity chart: exact discriminant normal form.
    A = T*(T-theta)-alpha*z
    Einf = sp.expand(Fstar-theta*Gstar)
    assert sp.expand(Einf-(A*u**2+alpha*z**2*u+alpha*theta*T*z**2)) == 0

    W = 2*A*u+alpha*z**2
    Binf = alpha*z**2-4*A*theta*T
    assert sp.expand(W**2-alpha*Binf*z**2-4*A*Einf) == 0

    # Jacobian of (u,theta)-&gt;(W,Binf) at the branch center.
    dW_du = sp.diff(W,u).subs({u:0,z:0,theta:0})
    dW_dth = sp.diff(W,theta).subs({u:0,z:0,theta:0})
    dB_du = sp.diff(Binf,u).subs({u:0,z:0,theta:0})
    dB_dth = sp.diff(Binf,theta).subs({u:0,z:0,theta:0})
    jac = sp.expand(dW_du*dB_dth-dW_dth*dB_du)
    assert jac == -8*T**5

    # Blowup of (W,z) equals the normalization on the z chart.
    winf = sp.symbols("winf")
    inf_eq = W**2-alpha*Binf*z**2
    # Abstract strict transform: W=winf*z.
    Wa, Za, Aa, Ba = sp.symbols("Wa Za Aa Ba")
    abstract = Wa**2-Aa*Ba*Za**2
    strict_inf_z = sp.expand(abstract.subs(Wa,winf*Za)/Za**2)
    assert strict_inf_z == winf**2-Aa*Ba

    # A1 resolution charts.
    a1eq = winf**2-Aa*Ba
    b1, a1, w1 = sp.symbols("b1 a1 w1")
    strict_A = sp.expand(a1eq.subs({Ba:Aa*b1,winf:Aa*w1})/Aa**2)
    strict_B = sp.expand(a1eq.subs({Aa:Ba*a1,winf:Ba*w1})/Ba**2)
    strict_w = sp.expand(a1eq.subs({Aa:winf*a1,Ba:winf*b1})/winf**2)
    assert strict_A == w1**2-b1
    assert strict_B == w1**2-a1
    assert strict_w == 1-a1*b1

    # Global conductor branch polynomial.
    P,Q = sp.symbols("P Q")
    branch = alpha*P*(P-T*Q)
    assert sp.expand(branch.subs({P:1,Q:rho})-alpha*(1-T*rho)) == 0
    assert sp.expand(branch.subs({P:theta,Q:1})-alpha*theta*(theta-T)) == 0
    assert sp.expand(Binf.subs({u:0,z:0})-4*T**2*theta*(theta-T)) == 0

    # Exact Hilbert--Burch presentation of the saturated finite-finite chart.
    A1 = -T*rho*y**2-lam*y*z+rho*x*y-rho*y**3-rho*y*z-y**2
    A2 = lam*rho*y*z-lam*z+rho*x-rho*y**2+rho*z-2*y
    M = sp.Matrix(&#91;
        &#91;A1,A2&#93;,
        &#91;x-y**2,-y&#93;,
        &#91;T*y+z,T&#93;,
    &#93;)
    minors = &#91;
        sp.expand(M&#91;1,0&#93;*M&#91;2,1&#93;-M&#91;1,1&#93;*M&#91;2,0&#93;),
        sp.expand(M&#91;0,0&#93;*M&#91;2,1&#93;-M&#91;0,1&#93;*M&#91;2,0&#93;),
        sp.expand(M&#91;0,0&#93;*M&#91;1,1&#93;-M&#91;0,1&#93;*M&#91;1,0&#93;),
    &#93;
    assert minors&#91;0&#93; == x*T+y*z

    # Check the saturation by elimination and equality of ideals via Groebner bases.
    h = sp.symbols("h")
    t_expr = T+lam*z
    fs = sp.expand(f1.subs(t,t_expr))
    gs = sp.expand(g1.subs(t,t_expr))
    E0 = x*T+y*z
    E1 = sp.expand(gs-rho*fs)
    sat = sp.groebner(
        &#91;E0,E1,1-h*(x*z)*fs&#93;,
        h,rho,lam,T,z,y,x,
        order="lex",
    )
    sat_no_h = &#91;p.as_expr() for p in sat.polys if not p.as_expr().has(h)&#93;
    Gsat = sp.groebner(sat_no_h,rho,lam,T,z,y,x,order="grevlex")
    Gmin = sp.groebner(minors,rho,lam,T,z,y,x,order="grevlex")
    for f in sat_no_h:
        assert Gmin.reduce(f)&#91;1&#93; == 0
    for f in minors:
        assert Gsat.reduce(f)&#91;1&#93; == 0

    # Singular radical of the saturated chart is (x,y,z).
    vars_ff = (x,y,z,T,lam,rho)
    Jac = sp.Matrix(&#91;&#91;sp.diff(f,v) for v in vars_ff&#93; for f in minors&#93;)
    jac_minors = &#91;&#93;
    for i in range(3):
        for j in range(i+1,3):
            for a in range(6):
                for b in range(a+1,6):
                    m = sp.expand(Jac&#91;i,a&#93;*Jac&#91;j,b&#93;-Jac&#91;i,b&#93;*Jac&#91;j,a&#93;)
                    if m != 0:
                        jac_minors.append(m)
    Gsing = sp.groebner(minors+jac_minors,rho,lam,T,z,y,x,order="grevlex")
    assert Gsing.reduce(x**2)&#91;1&#93; == 0
    assert Gsing.reduce(y**3)&#91;1&#93; == 0
    assert Gsing.reduce(z**3)&#91;1&#93; == 0
    for f in minors+jac_minors:
        assert sp.expand(f.subs({x:0,y:0,z:0})) == 0

    # The cubic-scroll normalization is singular only at its vertex.
    aa, bb, uu, zz, ww = sp.symbols("aa bb uu zz ww")
    scroll = &#91;ww**2-aa*bb, ww*uu-aa*zz, ww*zz-bb*uu&#93;
    Jscroll = sp.Matrix(&#91;&#91;sp.diff(f,v) for v in (aa,bb,uu,zz,ww)&#93; for f in scroll&#93;)
    scroll_jac = &#91;&#93;
    for i in range(3):
        for j in range(i+1,3):
            for a in range(5):
                for b in range(a+1,5):
                    m = sp.expand(Jscroll&#91;i,a&#93;*Jscroll&#91;j,b&#93;-Jscroll&#91;i,b&#93;*Jscroll&#91;j,a&#93;)
                    if m != 0:
                        scroll_jac.append(m)
    Gscroll = sp.groebner(scroll+scroll_jac,ww,zz,uu,bb,aa,order="grevlex")
    for v in (aa,bb,uu,zz,ww):
        assert Gscroll.reduce(v**2)&#91;1&#93; == 0
    for f in scroll+scroll_jac:
        assert sp.expand(f.subs({aa:0,bb:0,uu:0,zz:0,ww:0})) == 0

    print("first-graph reduction and exact weak pair: passed")
    print("finite second-direction double-pinch normal form: passed")
    print("cubic-scroll normalization and smooth conductor blowup charts: passed")
    print("second-projective-infinity discriminant normal form: passed")
    print("A1 normalization/resolution and global conductor branch: passed")
    print("Hilbert--Burch saturated multi-Rees chart: passed")
    print("ALL UNORDERED NORMALIZATION CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-98a7063c40bcaa46"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802c/lane2_unordered_normalization_theorem.md`

<pre><code class="language-markdown">
# Cubic-scroll normalization of the unordered quintic outer graph

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact symbolic replay supplied.
&gt; **Scope:** characteristic different from `2`; the translation parameter is a unit.  The theorem treats the finite first-projective-direction chart of the universal outer pair and gives the exact normalization over the open set `T != 0`, including both charts of the second projective line.  The remaining codimension-two locus in the nonnormal divisor lies over `T=0` and is the locus of the residual conifold found in the ordered-resolution theorem.

## 1. Universal pair and normalization of the translation parameter

Let

\&#91;
J_0=(xz,\ yz+xt)\subset k&#91;x,y,z,t&#93;
\&#93;

and let

\&#91;
J_s=\tau_s(J_0),
\qquad
\tau_s(x,y,z,t)
=(x-sy^2,\ y,\ z+s(x+yt),\ t+sy).
\&#93;

If `s` is a unit, the diagonal change

\&#91;
(x',y',z',t')=(sx,sy,z,t)
\&#93;

carries the pair `(J_0,J_s)`, up to harmless common scalar factors in each
projective pair, to `(J_0,J_1)`.  We therefore put `s=1`.

Write

\&#91;
f_0=xz,
\qquad
g_0=yz+xt,
\&#93;

\&#91;
f_1=(x-y^2)(z+x+yt),
\qquad
g_1=xt+yz+2xy-y^3.
\&#93;

Let `lambda` be the finite coordinate on the first projective factor and put

\&#91;
T=t-\lambda z.
\&#93;

The first graph is

\&#91;
X_0=V(xT+yz).
\&#93;

The theorem concerns the open set `T != 0`.  There the first graph is smooth
and

\&#91;
x=-\frac{yz}{T}.
\&#93;

Put

\&#91;
u=Ty+z,
\qquad
\alpha=1-T\lambda.
\&#93;

After substituting the first-graph equation, both generators of `J_1` have the
common Cartier factor `y`.  Removing it does not change the projective map.
Up to one common invertible scalar, the resulting pair is

\&#91;
F_*=u\bigl(T^2u-\alpha uz+\alpha z^2\bigr),
\qquad
G_*=T\bigl(u^2-\alpha z^2\bigr).
\&#93;

All formulas below are exact.

## 2. Finite second direction: an exact double-pinch equation

On the chart in which

\&#91;
\rho=G_*/F_*
\&#93;

is finite, the unordered simultaneous graph is

\&#91;
\rho F_*=G_*.
\&#93;

Set

\&#91;
D=T+\rho u,
\qquad
\beta=1-\rho T,
\&#93;

and, on the neighborhood `D != 0`, define

\&#91;
B=\frac{T\beta+\rho\alpha z}{D}.
\&#93;

Then

\&#91;
\rho F_*-G_*
=D\bigl(\alpha z^2-u^2B\bigr).
\&#93;

At the nonnormal divisor `u=z=0`, one has `D=T`, while

\&#91;
\left.\frac{\partial B}{\partial\rho}\right|_{u=z=0}=-T.
\&#93;

Thus `B` is a regular coordinate replacing `rho` on a Zariski neighborhood
of that divisor.  The inverse is explicit:

\&#91;
\rho=
\frac{T(1-B)}{T^2+Bu-\alpha z}.
\&#93;

Consequently the finite--finite chart is exactly

\&#91;
\boxed{
X_{\mathrm{fin}}
=\operatorname{Spec}
 k&#91;T^{\pm1},u,z,\alpha,B&#93;/(\alpha z^2-u^2B).
}
\&#93;

The singular locus is the divisor

\&#91;
D_{\mathrm{cond}}=V(u,z).
\&#93;

Since `X_fin` is a hypersurface, it is Cohen--Macaulay.  Its singular locus
has codimension one, so it is not normal.

## 3. Exact normalization: the cubic-scroll cone

In the function field of `X_fin`, put

\&#91;
w=\frac{\alpha z}{u}=\frac{Bu}{z}.
\&#93;

Then `w` is integral and satisfies

\&#91;
w^2=\alpha B,
\qquad
wu=\alpha z,
\qquad
wz=Bu.
\&#93;

Define

\&#91;
\widetilde X_{\mathrm{fin}}
=\operatorname{Spec}
\frac{k&#91;T^{\pm1},\alpha,B,u,z,w&#93;}
{(w^2-\alpha B,\ wu-\alpha z,\ wz-Bu)}.
\&#93;

### Theorem 3.1 — Normalization

The finite morphism

\&#91;
\widetilde X_{\mathrm{fin}}\longrightarrow X_{\mathrm{fin}}
\&#93;

is the normalization.

### Proof

Ignoring the smooth unit `T`, the displayed ring is the semigroup ring

\&#91;
k&#91;a^2,ab,b^2,ac,bc&#93;
\&#93;

under

\&#91;
\alpha=a^2,
\quad w=ab,
\quad B=b^2,
\quad u=ac,
\quad z=bc.
\&#93;

Its exponent semigroup is

\&#91;
S=\{(i,j,k)\in\mathbb Z_{\ge0}^3:
 i+j+k\equiv0\pmod2,\ k\le i+j\}.
\&#93;

This semigroup is saturated in its lattice.  Indeed, choose nonnegative
`p &lt;= i`, `q &lt;= j` with `p+q=k`; the remaining pair
`(i-p,j-q)` has even sum and is generated by `(2,0)`, `(1,1)`, `(0,2)`.
Hence the semigroup ring is normal.

The original ring is generated by the same monomials except `ab`.  Its
semigroup saturation adds exactly `ab`, so adjoining `w=ab` gives the entire
integral closure. ∎

The three equations are the maximal minors of

\&#91;
\begin{pmatrix}
\alpha&amp;w&amp;u\\
w&amp;B&amp;z
\end{pmatrix}.
\&#93;

Thus, transversely to `T`, the normalization is the affine cone over the
rational normal cubic scroll `S(1,2)`.  Its singular locus is only the vertex

\&#91;
V(\alpha,B,u,z,w).
\&#93;

The conductor in `X_fin` is

\&#91;
\mathfrak c=(u,z).
\&#93;

Its inverse image in the normalization is the double cover

\&#91;
V(u,z),
\qquad
w^2=\alpha B.
\&#93;

## 4. Canonical smooth resolution of the finite chart

Blow up the conductor ideal `(u,z)` on `X_fin`.

On the `u`-chart, put `z=qu`.  The strict equation is

\&#91;
B=\alpha q^2.
\&#93;

On the `z`-chart, put `u=pz`.  The strict equation is

\&#91;
\alpha=Bp^2.
\&#93;

Both charts are affine four-space.  They glue by

\&#91;
p=q^{-1},
\qquad
B=\alpha q^2,
\qquad
z=qu.
\&#93;

Hence

\&#91;
\boxed{\operatorname{Bl}_{(u,z)}X_{\mathrm{fin}}\text{ is smooth}.}
\&#93;

The map factors through the normalization.  On the two charts the additional
normalization coordinate is

\&#91;
w=\alpha q
\qquad\text{and}\qquad
w=Bp,
\&#93;

respectively.  The induced morphism to the cubic-scroll cone is its standard
small resolution.  It is the total space

\&#91;
\operatorname{Tot}_{\mathbb P^1}
\bigl(\mathcal O_{\mathbb P^1}(-2)
      \oplus
      \mathcal O_{\mathbb P^1}(-1)\bigr)
\&#93;

times the smooth `T`-factor.  Its exceptional fiber over the scroll vertex is
one `P^1`.

This gives an order-independent smooth resolution of the unordered graph on
the finite second-direction chart.

## 5. The missing second-projective direction

Let

\&#91;
\theta=F_*/G_*
\&#93;

be the coordinate on the other second-projective chart.  Its graph equation
is

\&#91;
F_*-\theta G_*=0.
\&#93;

Put

\&#91;
A=T(T-\theta)-\alpha z.
\&#93;

Near the pure `G_*` direction `theta=0`, the function `A` is a unit.  The
graph equation is the quadratic

\&#91;
Au^2+\alpha z^2u+\alpha\theta Tz^2=0.
\&#93;

Define

\&#91;
W=2Au+\alpha z^2,
\qquad
B_\infty=\alpha z^2-4A\theta T.
\&#93;

Then the discriminant identity gives

\&#91;
\boxed{W^2=\alpha B_\infty z^2.}
\&#93;

At the locus `u=z=theta=0`, the changes `u -&gt; W` and
`theta -&gt; B_infty` have invertible Jacobian.  Therefore this is an exact
étale-local normal form for the finite--infinite chart.

### Theorem 5.1 — Normalization at second-projective infinity

The normalization of

\&#91;
X_\infty=V(W^2-\alpha B_\infty z^2)
\&#93;

is

\&#91;
\widetilde X_\infty
=
V(w^2-\alpha B_\infty),
\qquad
W=wz.
\&#93;

Equivalently,

\&#91;
\widetilde X_\infty
=
\operatorname{Spec}
 k&#91;T^{\pm1},\alpha,B_\infty,z,w&#93;/(w^2-\alpha B_\infty).
\&#93;

The conductor in the nonnormal chart is `(W,z)`.  Blowing it up is exactly
the normalization: on the `z`-chart the new coordinate is `w=W/z`, while the
other blowup chart is its open subset `w != 0`.

The normalization has the residual singular locus

\&#91;
V(\alpha,B_\infty,w),
\&#93;

with `(T,z)` smooth.  It is a family of du Val `A_1` surface singularities.
Blowing up that singular locus gives the three smooth charts

\&#91;
B_1+w_1^2=0,
\qquad
\alpha_1+w_1^2=0,
\qquad
\alpha_1B_1+1=0.
\&#93;

This is exactly the `A_1` resolution appearing in the ordered construction,
now derived as a resolution of the normalization of the unordered graph.

## 6. Global conductor cover over the second projective line

Let `&#91;P:Q&#93;=&#91;F_*:G_*&#93;` be homogeneous coordinates on the second projective
factor.  On `P != 0`, the conductor coordinate is

\&#91;
B=1-TQ/P.
\&#93;

Hence, after setting `omega=P w`, the normalization of the conductor is

\&#91;
\omega^2=\alpha P(P-TQ).
\&#93;

On `Q != 0`, put `theta=P/Q`.  The discriminant calculation above restricts,
up to the square unit `4T^2`, to

\&#91;
\alpha\theta(\theta-T).
\&#93;

Thus the two local normalizations glue, and the conductor double cover is
canonically

\&#91;
\boxed{
\omega^2=\alpha P(P-TQ)
}
\&#93;

with `omega` a local section of `O_{P^1}(1)`.

For `alpha != 0` it is a double cover of the second projective line branched
at

\&#91;
P=0
\qquad\text{and}\qquad
P-TQ=0.
\&#93;

The two branch sections are precisely the two special second directions
visible in the exact ordered charts.

## 7. Consequence for the quintic PRS flag

Under

\&#91;
(x,y,z,t)=(C,D,u,v),
\&#93;

the actual `(m,nu)=(5,5)` outer pair is `(J_0,J_1)`.  Therefore the theorem
computes the normalization of its unordered simultaneous outer graph over

\&#91;
T=t-\lambda z\ne0.
\&#93;

The result is stronger than the preceding ordered-resolution theorem:

1. the unordered graph is explicitly nonnormal along a divisor;
2. its finite chart normalizes to the cubic-scroll cone;
3. its second-projective-infinity chart normalizes to an `A_1` family;
4. the conductor and its global double cover are explicit;
5. the canonical conductor blowups give smooth resolutions;
6. every normal ordered resolution factors uniquely through this
   normalization.

The remaining local frontier is now the codimension-two subset

\&#91;
T=0
\&#93;

inside the conductor divisor.  This is exactly where the ordered calculation
found the residual conifold.  Determining the finite normalization there and
gluing it to the cubic-scroll charts is the next theorem-facing step.
</code></pre>

<a id="source-813098830565c0aa"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_checks.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact replay for the T=0 normalization and toric normal-form theorem."""
from __future__ import annotations

import itertools
import sympy as sp


def pfaffian4(a, b, c, d, e, f):
    """Pfaffian of &#91;&#91;0,a,b,c&#93;,&#91;-a,0,d,e&#93;,&#91;-b,-d,0,f&#93;,&#91;-c,-e,-f,0&#93;&#93;."""
    return sp.expand(a*f-b*e+c*d)


def main() -&gt; None:
    x, y, z, T, lam, rho, w = sp.symbols("x y z T lam rho w")
    alpha = 1-T*lam
    beta = 1-T*rho
    u = T*y+z
    xi = x-y**2
    v = u+alpha*x

    F0 = sp.expand(T*x+y*z)
    F1 = sp.expand(w*u-alpha*z)
    F2 = sp.expand(w*xi-alpha*x)
    F3 = sp.expand(rho*v-lam*z-(w+1)*y)
    F4 = sp.expand(w**2-alpha*(beta+rho*w*y))
    finite_ideal = &#91;F0,F1,F2,F3,F4&#93;

    # Saturated Hilbert--Burch graph.
    A1 = -T*rho*y**2-lam*y*z+rho*x*y-rho*y**3-rho*y*z-y**2
    A2 = lam*rho*y*z-lam*z+rho*x-rho*y**2+rho*z-2*y
    M = sp.Matrix(&#91;&#91;A1,A2&#93;,&#91;xi,-y&#93;,&#91;u,T&#93;&#93;)
    minors = &#91;
        sp.expand(M&#91;1,0&#93;*M&#91;2,1&#93;-M&#91;1,1&#93;*M&#91;2,0&#93;),
        sp.expand(M&#91;0,0&#93;*M&#91;2,1&#93;-M&#91;0,1&#93;*M&#91;2,0&#93;),
        sp.expand(M&#91;0,0&#93;*M&#91;1,1&#93;-M&#91;0,1&#93;*M&#91;1,0&#93;),
    &#93;
    assert minors&#91;0&#93; == F0

    qsat = sp.symbols("qsat")
    Gsat = sp.groebner(
        minors+&#91;F1,1-qsat*u&#93;,
        qsat,w,rho,lam,T,z,y,x,
        order="lex",
    )
    sat_no_q = &#91;p.as_expr() for p in Gsat.polys if not p.as_expr().has(qsat)&#93;
    Gsat2 = sp.groebner(sat_no_q,w,rho,lam,T,z,y,x,order="grevlex")
    Gfin = sp.groebner(finite_ideal,w,rho,lam,T,z,y,x,order="grevlex")
    for f in sat_no_q:
        assert Gfin.reduce(f)&#91;1&#93; == 0
    for f in finite_ideal:
        assert Gsat2.reduce(f)&#91;1&#93; == 0

    # Exact syzygies used on the two sheets.
    assert sp.expand(y*F1+T*F2-(w-alpha)*F0) == 0
    assert sp.expand((w-alpha)*F3-(rho-lam)*F1-rho*alpha*F2+y*F4) == 0

    B = sp.expand(beta+rho*w*y)
    assert sp.expand(F4-(w**2-alpha*B)) == 0
    assert sp.expand(w*z-B*u-((1-rho*y)*F1+T*F3-rho*alpha*F0)) == 0

    # Negative-sheet Jacobian.
    Jminus = sp.Matrix(&#91;
        &#91;sp.diff(F1,var) for var in (z,x,w)&#93;,
        &#91;sp.diff(F2,var) for var in (z,x,w)&#93;,
        &#91;sp.diff(F4,var) for var in (z,x,w)&#93;,
    &#93;)
    det_minus = sp.factor(Jminus.det().subs({x:0,y:0,z:0,T:0,w:-1}))
    assert det_minus == -8

    # Positive-sheet variables.
    h = sp.symbols("h")
    s = 1-h
    m1 = sp.expand(h*x-y**2)
    m2 = sp.expand(T*y+h*z)
    m3 = F0
    F = sp.expand(alpha-s**2*beta-rho*alpha*s*y)
    ell1 = sp.expand(s*(rho*s-lam))
    ell2 = sp.expand(alpha+s)
    ell3 = sp.expand(rho*alpha*s)
    G0 = sp.expand(x*ell3-y*ell2+z*ell1)

    w_sub = alpha/s
    assert sp.factor((s/alpha)*F1.subs(w,w_sub)-m2) == 0
    assert sp.factor((s/alpha)*F2.subs(w,w_sub)-m1) == 0
    assert sp.factor((s**2/alpha)*F4.subs(w,w_sub)-F) == 0
    transformed_F3 = sp.expand(s*F3.subs(w,w_sub))
    assert sp.factor(transformed_F3-G0-rho*s*m2) == 0

    # Pfaffian presentation.
    Phi = sp.Matrix(&#91;
        &#91;0,0,x,y,z&#93;,
        &#91;0,0,y,h,-T&#93;,
        &#91;-x,-y,0,ell1,ell2&#93;,
        &#91;-y,-h,-ell1,0,ell3&#93;,
        &#91;-z,T,-ell2,-ell3,0&#93;,
    &#93;)
    pf = &#91;&#93;
    for omit in range(5):
        inds = &#91;i for i in range(5) if i != omit&#93;
        Q = Phi.extract(inds,inds)
        pf.append(pfaffian4(Q&#91;0,1&#93;,Q&#91;0,2&#93;,Q&#91;0,3&#93;,Q&#91;1,2&#93;,Q&#91;1,3&#93;,Q&#91;2,3&#93;))
    assert &#91;sp.expand(t) for t in pf&#93; == &#91;sp.expand(-F),G0,m2,m3,sp.expand(-m1)&#93;

    # Pfaffian syzygies and local complete intersection.
    assert sp.expand(ell2*m1-(x*F+y*G0-ell1*m3)) == 0
    assert sp.expand(ell2*m2-(z*F-T*G0+ell3*m3)) == 0

    R = sp.expand(T*ell2+z*ell3)
    Delta = ell1
    assert sp.expand(ell2*m3-(x*R+Delta*z**2-z*G0)) == 0

    # Etale coordinate change at the central positive sheet.
    old = (h,y,T,rho,x,z,lam)
    new = (F,G0,R,Delta,x,z,lam)
    Jchange = sp.Matrix(&#91;&#91;sp.diff(f,var) for var in old&#93; for f in new&#93;)
    det_change = sp.factor(Jchange.det().subs({h:0,y:0,T:0,x:0,z:0}))
    assert det_change == -8

    # Exact resolution charts of the abstract normal form x*R0+Delta0*z^2.
    a,b,c,d = sp.symbols("a b c d")
    R0, Delta0 = sp.symbols("R0 Delta0")
    normal = x*R0+Delta0*z**2
    strict_x = sp.expand(normal.subs(z,a*x)/x)
    assert strict_x == R0+Delta0*a**2*x
    strict_z = sp.expand(normal.subs(x,b*z)/z)
    assert strict_z == b*R0+Delta0*z
    conifold = b*R0+Delta0*z
    strict_b = sp.expand(conifold.subs(z,c*b)/b)
    strict_z2 = sp.expand(conifold.subs(b,d*z)/z)
    assert strict_b == R0+Delta0*c
    assert strict_z2 == d*R0+Delta0

    # Singular locus of the toric normal form.
    vars_nf = (x,R0,z,Delta0,lam)
    grad = &#91;sp.diff(normal,var) for var in vars_nf&#93;
    assert grad == &#91;R0,x,2*Delta0*z,z**2,0&#93;

    print("saturated graph-of-w presentation: passed")
    print("finite cubic-scroll gluing identities: passed")
    print("negative T=0 sheet smoothness: passed")
    print("positive-sheet Pfaffian presentation: passed")
    print("exact etale normal form x*R+Delta*z^2: passed")
    print("two-step toric/conifold resolution: passed")
    print("ALL T=0 NORMALIZATION CHECKS PASSED")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-485c3d5f593645a2"></a>

## `research-notes/lane2-prs-boundary-20260802-v1/lane2-progress-20260802d/lane2_T0_normalization_theorem.md`

<pre><code class="language-markdown">
# Finite normalization across the quintic `T=0` conifold locus

&gt; **Status:** new unrefereed proof draft; AI-assisted; exact symbolic replay supplied.
&gt; **Scope:** characteristic different from `2`; the finite-coordinate chart on each of the two projective outer factors; the translation parameter has been normalized to one.  This theorem closes the residual-conifold part of the `T=0` gap left by the cubic-scroll normalization theorem.  The projective-infinity charts at `T=0` remain separate.

## 1. The saturated unordered graph

Let

\&#91;
J_0=(xz,\ yz+xt),
\&#93;

\&#91;
J_1=((x-y^2)(z+x+yt),\ xt+yz+2xy-y^3).
\&#93;

Use finite projective coordinates `lambda` and `rho` for the two directions and put

\&#91;
T=t-\lambda z.
\&#93;

The first graph equation is

\&#91;
F_0=Tx+yz=0.
\&#93;

The saturated two-factor graph is the codimension-two Hilbert--Burch scheme
cut out by the maximal minors of

\&#91;
M_{\lambda,\rho}=
\begin{pmatrix}
A_1&amp;A_2\\
x-y^2&amp;-y\\
Ty+z&amp;T
\end{pmatrix},
\&#93;

where

\&#91;
\begin{aligned}
A_1={}&amp;-T\rho y^2-\lambda yz+\rho xy-\rho y^3-\rho yz-y^2,\\
A_2={}&amp;\lambda\rho yz-\lambda z+\rho x-\rho y^2+\rho z-2y.
\end{aligned}
\&#93;

It is the graph closure, hence irreducible.  Its singular radical is
`(x,y,z)`, so it is smooth away from the nonnormal divisor

\&#91;
D=V(x,y,z).
\&#93;

Put

\&#91;
\alpha=1-T\lambda,
\qquad
\beta=1-T\rho,
\&#93;

\&#91;
u=Ty+z,
\qquad
\xi=x-y^2,
\qquad
v=u+\alpha x.
\&#93;

In the function field define

\&#91;
w=\frac{\alpha z}{u}.
\&#93;

The first graph equation also gives

\&#91;
w=\frac{\alpha x}{\xi}
\&#93;

where the second expression is defined.

## 2. Exact finite presentation

Define

\&#91;
\begin{aligned}
F_1&amp;=wu-\alpha z,\\
F_2&amp;=w\xi-\alpha x,\\
F_3&amp;=\rho v-\lambda z-(w+1)y,\\
F_4&amp;=w^2-\alpha(\beta+\rho wy).
\end{aligned}
\&#93;

### Proposition 2.1

The closure of the graph of the rational function `w` is

\&#91;
\widetilde X^{\mathrm{ff}}
=
\operatorname{Spec}
\frac{k&#91;x,y,z,T,\lambda,\rho,w&#93;}
{(F_0,F_1,F_2,F_3,F_4)}.
\&#93;

Equivalently,

\&#91;
(I_2(M_{\lambda,\rho}),\ wu-\alpha z):u^\infty
=(F_0,F_1,F_2,F_3,F_4).
\&#93;

The forgetful morphism

\&#91;
\nu:\widetilde X^{\mathrm{ff}}\longrightarrow X^{\mathrm{ff}}
\&#93;

is finite and birational: `F_4` is monic in `w`, while `w` is the displayed
rational function on a dense open set.

The supplied replay verifies the saturation equality by mutual exact
Gröbner reduction.  The remaining proof is to show that the finite birational
source is normal.

## 3. Compatibility with the `T != 0` cubic-scroll chart

Set

\&#91;
B=\beta+\rho wy.
\&#93;

The equations imply

\&#91;
w^2=\alpha B,
\qquad
wu=\alpha z,
\qquad
wz=Bu.
\&#93;

The third identity follows from

\&#91;
wz-Bu
=(1-\rho y)F_1+TF_3-\rho\alpha F_0.
\&#93;

Thus over `T != 0` this is exactly the cubic-scroll normalization

\&#91;
I_2
\begin{pmatrix}
\alpha&amp;w&amp;u\\
w&amp;B&amp;z
\end{pmatrix}=0
\&#93;

obtained previously.  Near the conductor the coordinate change is invertible;
indeed

\&#91;
\rho=
\frac{T(1-B)}{T^2+Bu-\alpha z}.
\&#93;

Hence the new finite extension glues to the established normalization on the
punctured `T`-line.

## 4. The negative sheet is smooth

On $D\cap V(T)$, equation `F_4` reduces to

\&#91;
w^2=1.
\&#93;

Consider the sheet through `w=-1`.  There

\&#91;
w-\alpha=-2
\&#93;

is a unit.  The exact syzygies

\&#91;
yF_1+TF_2=(w-\alpha)F_0,
\&#93;

\&#91;
(w-\alpha)F_3
=(\rho-\lambda)F_1+\rho\alpha F_2-yF_4
\&#93;

show that the local ideal is generated by `F_1,F_2,F_4`.
Their Jacobian with respect to `(z,x,w)` has determinant `-8` at the sheet.
Therefore the negative sheet is smooth, with local coordinates

\&#91;
(T,\lambda,\rho,y).
\&#93;

## 5. The positive sheet as a Pfaffian model

Now work near `T=0,w=1`.  Here `w` and `alpha` are units.  Put

\&#91;
h=\frac{w-\alpha}{w},
\qquad
s=1-h=\frac{\alpha}{w}.
\&#93;

The first three equations become the maximal minors

\&#91;
m_1=hx-y^2,
\qquad
m_2=Ty+hz,
\qquad
m_3=Tx+yz
\&#93;

of

\&#91;
\begin{pmatrix}
x&amp;y&amp;z\\
y&amp;h&amp;-T
\end{pmatrix}.
\&#93;

The remaining two equations, after multiplication by units, are

\&#91;
F=\alpha-s^2\beta-\rho\alpha sy,
\&#93;

and

\&#91;
G_0=x\ell_3-y\ell_2+z\ell_1,
\&#93;

where

\&#91;
\ell_1=s(\rho s-\lambda),
\qquad
\ell_2=\alpha+s,
\qquad
\ell_3=\rho\alpha s.
\&#93;

The transformed `F_3` differs from `G_0` by the multiple
`rho*s*m_2`, so the ideals agree.

### Proposition 5.1 — Pfaffian presentation

The positive-sheet ideal is the ideal of submaximal Pfaffians of

\&#91;
\Phi=
\begin{pmatrix}
0&amp;0&amp;x&amp;y&amp;z\\
0&amp;0&amp;y&amp;h&amp;-T\\
-x&amp;-y&amp;0&amp;\ell_1&amp;\ell_2\\
-y&amp;-h&amp;-\ell_1&amp;0&amp;\ell_3\\
-z&amp;T&amp;-\ell_2&amp;-\ell_3&amp;0
\end{pmatrix}.
\&#93;

Up to the standard alternating signs, its five Pfaffians are

\&#91;
-F,\quad G_0,\quad m_2,\quad m_3,\quad -m_1.
\&#93;

Since `ell_2=2` on the central sheet, it is a unit nearby.  The Pfaffian
syzygies give

\&#91;
\ell_2m_1=xF+yG_0-\ell_1m_3,
\&#93;

\&#91;
\ell_2m_2=zF-TG_0+\ell_3m_3.
\&#93;

Consequently the local ideal is the complete intersection

\&#91;
(F,G_0,m_3).
\&#93;

## 6. Exact toric normal form

Define

\&#91;
R=T\ell_2+z\ell_3,
\qquad
\Delta=\ell_1=s(\rho s-\lambda).
\&#93;

There is an exact identity

\&#91;
\ell_2m_3=xR+\Delta z^2-zG_0.
\&#93;

Moreover, the change of ambient coordinates

\&#91;
(h,y,T,\rho,x,z,\lambda)
\longmapsto
(F,G_0,R,\Delta,x,z,\lambda)
\&#93;

has Jacobian determinant

\&#91;
-8
\&#93;

along the central sheet

\&#91;
x=y=z=T=h=0.
\&#93;

It is therefore étale there.  After setting `F=G_0=0` and dividing by the
unit `ell_2`, the positive sheet is exactly

\&#91;
\boxed{xR+\Delta z^2=0}
\&#93;

with `lambda` an additional smooth parameter.

### Theorem 6.1 — Local normal form

At every point over

\&#91;
T=0,\qquad w=1,
\&#93;

the completed or étale local ring of $\widetilde X^{\mathrm{ff}}$ is

\&#91;
\boxed{
 k&#91;&#91;x,R,z,\Delta,\lambda&#93;&#93;/(xR+\Delta z^2).
}
\&#93;

The singular locus is

\&#91;
\Sigma_+=V(x,R,z),
\&#93;

with `(Delta,lambda)` free.  It has codimension two.  The hypersurface is an
irreducible Cohen--Macaulay domain and is regular in codimension one; hence it
is normal.

For `Delta` a unit, the transverse surface is a du Val `A_1` singularity.
At `Delta=0` its fiber becomes the reducible crossing `xR=0`, but the total
space remains normal.  On the central sheet

\&#91;
\Delta=\rho-\lambda,
\&#93;

so the diagonal second-direction locus is exactly the degeneration locus of
this `A_1` family.

## 7. Normalization theorem

### Theorem 7.1 — Finite normalization across `T=0`

The finite birational morphism

\&#91;
\nu:\widetilde X^{\mathrm{ff}}\to X^{\mathrm{ff}}
\&#93;

is the normalization of the saturated unordered finite--finite graph.

### Proof

Away from `D=V(x,y,z)`, the original graph is smooth, hence normal, and a
finite birational extension is an isomorphism.  Along $D\cap V(T\ne0)$, the
extension is the already proved cubic-scroll normalization.  Along
$D\cap V(T=0)$, the two roots `w=+1` and `w=-1` give an open cover after an
étale localization because `2` is invertible.  The negative sheet is smooth
by Section 4.  The positive sheet is the normal toric hypersurface of
Theorem 6.1.  Therefore $\widetilde X^{\mathrm{ff}}$ is normal everywhere on this finite--finite chart.  A finite
birational map from a normal integral scheme is the normalization.  ∎

## 8. Resolution and the residual conifold

The normal form

\&#91;
Y=V(xR+\Delta z^2)
\&#93;

has a direct projective resolution.

First blow up the non-Cartier ideal `(x,z)`.

- On the `x`-chart, `z=ax`, and the strict transform is
  \&#91;
  R+\Delta a^2x=0,
  \&#93;
  which is smooth.

- On the `z`-chart, `x=bz`, and the strict transform is
  \&#91;
  \boxed{bR+\Delta z=0}.
  \&#93;
  This is the ordinary threefold conifold, with `lambda` a smooth parameter.

Resolve the conifold by blowing up either `(b,z)` or `(b,Delta)`.
For `(b,z)`, the two strict-transform charts are

\&#91;
R+\Delta c=0,
\qquad
 dR+\Delta=0,
\&#93;

and are smooth.  The alternative choice is the standard Atiyah flop.

Thus the residual conifold in the ordered construction is not an additional
higher-order obstruction: it is the unique node created by a toric partial
resolution of the finite normalization.  The two order choices correspond to
the two small-resolution choices after this contraction.

## 9. Quintic PRS corollary

Under

\&#91;
(x,y,z,t)=(C,D,u,v),
\&#93;

the actual `(m,nu)=(5,5)` outer subresultant pair is `(J_0,J_1)`.
Therefore Theorem 7.1 gives the exact normalization of its unordered outer
multi-graph on the two finite projective-direction charts, including the
previously unresolved `T=0` locus.

The finite--finite residual-conifold locus is therefore no longer open.  The
remaining local projective work consists of the `T=0` second-direction-infinity
collision and the first-direction-infinity chart of the individual outer
graph.  Beyond those charts, the remaining work is line-bundle and projective
gluing, plus extension of the relative-Jacobian marking.
</code></pre>

[Back to Lane 2](boundary-completeness-torelli-at-infinity.md)
