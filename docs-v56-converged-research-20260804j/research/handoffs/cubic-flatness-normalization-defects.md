---
title: "Model research brief — Flatness defects after cubic normalization"
description: "A self-contained mathematical handoff for a research model."
---

# Flatness defects after cubic normalization

<p class="claim-tag">Lane 1 · Updated 4 August 2026</p>

## Scope

Study the finite normalization of a generic-degree-three Keller map at an
omitted target value. The known theory identifies the exact finite defect and
its quadratic-resolvent and collision-cohomology carriers. The frontier is to
exclude those carriers or construct one satisfying all stated local
constraints.

Success would remove the only possible nonflat points of a cubic
normalization; it would not by itself recover the affine source opening.

The Alpöge--Fable map is a benchmark, not the unresolved case: its own finite
normalization is already proved flat by the marked-root symmetry in the
linked packet. The live problem concerns other Keller maps of **generic
degree three**, meaning degree three of the function-field extension. This is
different from the polynomial-degree-three descendant used in Lane 6.

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

At a closed value $y$, put $A=R_y$ and $\Delta_y=(\Delta_F)_y$. If
$\Delta_y\ne0$, completion has one normal rank-three local factor. That
cubic factor cannot be cyclic: its character idempotents would split the
integral closure into rank-one reflexive modules over a factorial complete
regular local ring, forcing freeness and contradicting the defect. Thus the
defect branch is non-Galois and its Galois closure has group $S_3$. In this
defect case let $T$ be the normalization in that $S_3$-Galois closure. More
precisely, if
$B_i=T^{H_i}$ are the three cubic subalgebras and $S_i$ their conjugate
polynomial source algebras, put

\[
U_i=\operatorname{Spec}T\times_{\operatorname{Spec}B_i}
\operatorname{Spec}S_i.
\]

These are affine opens of the inverse image of the attained locus. When
$y$ is omitted they do not contain a point over $y$; nevertheless their
coordinate rings are $A$-modules, and the closed-point local cohomology of
their Čech complex measures the failure to glue across the deleted fibre.
The three openings give

\[
C_y^0\xrightarrow{d_0}C_y^1\xrightarrow{d_1}C_y^2,
\qquad K_y=\ker d_1,\quad I_y=\operatorname{im}d_0.
\]

Here the terms are sums of coordinate rings of the $U_i$ and their
intersections, with the usual alternating differentials. Thus $I_y$ is a
submodule of $K_y$, not an ideal in a source-chart ring. Its
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
- For the exact marked cubic
  \(cT^3-2T^2+bT-2a\), the finite completion, discriminant, resolvent,
  conductor, different, and the preceding zero-saturation calculation are
  all available as one reproducible benchmark.
- Normal \(S_3\) monodromy and the transverse splitting pattern do not force
  flatness: the elliptic-cone model below has a non-MCM eigensheaf and a
  length-two global collision quotient even though its standard local axes
  have zero punctual quotient.
- In the smooth homogeneous one-generator case, a dense affine-three-space
  opening would force the presentation degree to be \(d=4\). This is the
  type-IV triple-plane case. A fixed explicit type-IV net, its branch decic,
  21 cusps, length-one cone defect, and resolvent matrix factorization are
  supplied below as an equation-level test object.
- These results neither prove $\Delta_F=0$ in general nor supply an actual
  omitted-value local equation for an arbitrary map.

## Examples and fixed test objects

### A transverse carrier

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

### A non-MCM global boundary model

The [elliptic-cone construction](lane-1-source-packet.md#source-ecb5fca02f9c9fd5)
is a normal \(S_3\) cubic cone with an explicit finite defect and non-MCM
resolvent eigensheaf. Its global gluing, rather than the local collision axes
alone, creates the nonzero saturation quotient. It is not a polynomial Keller
map.

### A smooth homogeneous type-IV test object

The [type-IV gate and explicit net](lane-1-source-packet.md#source-69caa73289f1610d)
give a finite flat projective triple plane from a quartic net with a reduced
length-13 base scheme. Its branch decic is irreducible over \(\mathbf Q\) and
has 21 \(A_2\) cusps. The affine cone has a length-one Ext defect and an
explicit \(4\times4\) resolvent matrix factorization. This is a fixed
equation-level test object, not a Keller map; in particular it does not
supply the three source openings needed for the Keller Čech quotient.

## Live problem

The elliptic-cone model proves that normality, \(S_3\)-symmetry, order-three
reflexive class, and the transverse local axes do **not** force the resolvent
module to be MCM. A successful general theorem must therefore use a
Keller-specific hypothesis that holds for every actual cubic Keller
normalization and excludes that model. The complementary construction
problem is equally concrete: build an actual generic-degree-three Keller
normalization with a non-MCM carrier, exhibit its omitted target value and
quadratic resolvent, and supply the three source openings and overlap maps
needed to compute its Čech defect. Producing another abstract non-MCM pair is
not a solution.

The fixed type-IV cone supplies a second, independent test: either realize a
compatible affine Keller opening, or prove that the displayed Euler-lift and
boundary geometry obstruct every such opening.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Find the Keller-specific cubic-resolvent constraint — Ready now

`TSK-L1-KELLER-RESOLVENT-CARRIER` · proof, exploration · open ended

**Goal.** Prove a Keller-specific MCM criterion excluding the known elliptic-cone model, or construct an actual cubic Keller normalization with a non-MCM carrier and its source-opening Čech defect.

**Why it matters.** This attacks the only possible nonflat carrier without mistaking an already-known abstract boundary model for progress on Keller maps.

**Public inputs.**

- [Exact quadratic-resolvent carrier of the cubic flatness defect](../working-mathematics/units/RMU-1A8D0004.md) (retained unit `RMU-1A8D0004`).
- [Elliptic-cone model realizes a non-MCM cubic resolvent carrier](../working-mathematics/units/RMU-1B8F0002.md) (retained unit `RMU-1B8F0002`).
- [Exact Ext, resolvent, source-opening, and Čech comparison theorem.](lane-1-source-packet.md#source-195de0d23627037b).

**Complete when.**

- A proved condition holds for every relevant Keller normalization and excludes the model, or an actual Keller example supplies the omitted value, resolvent module, three source openings, overlaps, and Čech quotient.

**Possible starts.**

- Identify a geometric condition forced by an etale affine source opening and test it against the elliptic-cone carrier.
- Analyze depth, divisor class, conductor, and local cohomology simultaneously rather than only transverse surface sections.

**Freedom.**

- A stronger vanishing theorem or a genuine Keller countermodel is welcome.

**Mathematical limits.**

- Another abstract non-MCM double cover is not a completion.
- Do not infer a local S3 decomposition group from global monodromy.

### Test the fixed type-IV Keller realizability gate — Ready now

`TSK-L1-TYPEIV-REALIZABILITY` · proof, exploration · sustained

**Goal.** Construct a compatible affine Keller opening of the explicit type-IV cone or prove that the Euler lift and boundary geometry exclude every such opening.

**Why it matters.** This decides the fixed smooth homogeneous one-generator test object at equation level.

**Public inputs.**

- [Explicit type-IV triple-plane test object and cone module](../working-mathematics/units/RMU-1B8F0004.md) (retained unit `RMU-1B8F0004`).
- [Fixed equations, open boundary, Euler-lift condition, and exact certificates.](lane-1-source-packet.md#source-69caa73289f1610d).

**Complete when.**

- A source opening and Keller identities are checked, or a theorem excludes every compatible opening.

**Possible starts.**

- Study affine openings compatible with the divergence-three Euler lift.
- Use the explicit branch and resolvent module to derive an obstruction.

**Freedom.**

- Separate fixed-equation arguments from statements valid for every type-IV cone.

**Mathematical limits.**

- Excluding this cone does not settle singular projectivizations or the general nonhomogeneous problem.
<!-- RETAINED_TASKS_END -->

## Limits

The problem is local at a hypothetical omitted defect value. Source splitting
already proves flatness at attained values. The marked-root benchmark and ADE
models are examples and do not identify an actual defect value.

## Direct sources

- [Complete Lane 1 proof source](lane-1-source-packet.md#source-195de0d23627037b)
- [Exact resolvent and transverse-ADE source](lane-1-source-packet.md#source-31b28e4d427212ea)
- [Recovery manifest](lane-1-source-packet.md#source-d8d50dd353502656)
- [Canonical Ext appendix](../proof-sources/01-cubic-incidence/appendices/flatness-defect-repairs.md)
- [Marked-root, elliptic-cone, and type-IV proof packet](lane-1-source-packet.md#source-aef55c7c330abe18)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-1-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
