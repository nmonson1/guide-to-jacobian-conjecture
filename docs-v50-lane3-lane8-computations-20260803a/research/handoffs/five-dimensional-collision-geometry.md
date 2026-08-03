---
title: "Model research brief — Five-dimensional collision geometry"
description: "A self-contained mathematical handoff for a research model."
---

# Lane 7: Five-dimensional collision geometry

<p class="claim-tag">Lane 7 · Updated 3 August 2026</p>

## Problem and scope

Consider cubic-homogeneous Keller maps $F=X-H(X)$ in five variables whose
quadratic Jacobian pencil is everywhere regular of generic Jordan type $(5)$
along a collision line. Lane 7 asks for the characteristic-zero component
geometry of the exact full-kernel collision chart and for the first-normal
obstruction on every genuine component.

Here Keller means $\det(I-JH)=1$. An everywhere-regular type-$(5)$ pencil has
$JH(su+tv)$ equal to one nilpotent Jordan block for every $[s:t]\in\mathbf
P^1$. A collision datum consists of distinct points $v$ and $v+u$ with
$F(v+u)=F(v)$.

This lane is separate from the 19-to-18 compression problem in Lane 6.

## Setup and notation

The Keller condition makes $u$ and $v$ automatically independent. If they
were proportional, cubic homogeneity would give a nonzero eigenvalue of
$JH(u)$, contradicting nilpotence.

Polarize $H$ to the symmetric trilinear tensor $\mathcal T$ and put

$$
A_0=JH(u),\qquad B_0=6\mathcal T(u,v,-),\qquad C_0=JH(v).
$$

The collision and integrability equations include
$B_0u=2A_0v$ and their polarized companions. On the full-span chart the
eight pencil parameters form

$$
\mathbf C\lambda\oplus\operatorname{Sym}^6(\mathbf C^2),
$$

with $\lambda=a_7$. If $I_2,I_4$ are the normalized binary-sextic invariants
and $T_{\rm frame}$ is the fixed frame matrix, regularity is controlled by

$$
\det T_{\rm frame}
=\frac{(\lambda^2+4I_2)^2-96I_4}{256}.
$$

After the normalization $a_7=1$, the original full collision chart is cut
out by fifteen primitive quintics. The complete canonical source packet,
including those equations and matrices, is
[`research-notes/lane7-split-incidence-20260802-v1/`](lane-7-source-packet.md).

## Split incidence and genuine marking

Write the homogeneous marking matrix as $\Theta=[U\mid V]$. An explicit
polynomial left inverse of $U$ eliminates five marking variables globally.
On the accepted determinant open $D(d)$, exact matrices give

$$
M(a)u=0,\qquad
v=-d^{-1}C(a)A(a)u,\qquad
\operatorname{rank}\Theta=5+\operatorname{rank}M,
$$

where $M$ is a $10\times5$ matrix. The determinant identities are

$$
\det[H\ R]=-\frac{256}{243}d^2,\qquad
\det\begin{bmatrix}C\\Q\end{bmatrix}=-\frac{243}{256}d^8.
$$

This is theorem [`RMU-5C7E0011`](../working-mathematics/units/RMU-5C7E0011.md).

The projectivized kernel incidence is

$$
\mathcal I=\{(a,[u]):M(a)u=0,\ d(a)\ne0\}.
$$

Its five affine charts $u_i=1$ cover $\mathbf P^4$. Unit [`RMU-5C7E0012`](../working-mathematics/units/RMU-5C7E0012.md) and
[`research-notes/lane7-projective-kernel-20260803-v1/`](lane-7-source-packet.md) provide exact generators
for all five chart ideals:

$$
M(a)u=0,\qquad z\,d(a)-1=0.
$$

The packet emits independent Macaulay2 and Singular inputs over prime fields
and exact Singular inputs over $\mathbf Q$. It supplies runnable ideals, not
their dimensions.

There is a further open condition for a genuine collision pair. Put
$w=C(a)A(a)u$ and

$$
\eta_{ij}=u_iw_j-u_jw_i.
$$

The genuine marking incidence is the union of the ten opens
$D(\eta_{ij})$ inside $\mathcal I$. A component of the determinantal carrier
contributes only if at least one $\eta_{ij}$ is nonzero at its generic point.

## Reusable mathematics

- The collision and integrability equations have a smooth
  one-dimensional characteristic-zero family lifted from an explicit smooth
  point over $\mathbf F_{11}$ ([`JCG-FFBBD77B`](../working-mathematics/units/JCG-FFBBD77B.md)).
- The complete $\mathbf Z_{11}$ residue disk through that point has no
  first-normal extension: independent systems have ranks $(60,61)$ and
  $(125,126)$ ([`JCG-64E18DF3`](../working-mathematics/units/JCG-64E18DF3.md)).
- Thirty sampled finite-field collision points have a nonzero first-normal
  obstruction ([`JCG-86F5C9FA`](../working-mathematics/units/JCG-86F5C9FA.md)). They do not classify characteristic-zero
  components.
- For a globally defined generically type-$(5)$ quadratic nilpotent matrix,
  the rank-at-most-three locus has codimension at most two. If it extends an
  everywhere-regular collision line, the codimension is exactly two and the
  locus misses the line ([`JCG-15D52C7B`](../working-mathematics/units/JCG-15D52C7B.md)).
- The split incidence, automatic independence, and intrinsic Pluecker-open
  marking condition are proved in [`RMU-5C7E0011`](../working-mathematics/units/RMU-5C7E0011.md).
- Two monolithic Macaulay2 attempts produced no dimension, degree, or
  component data. Failed elimination is not negative mathematical evidence.

An earlier PR 7 experiment asserted a fixed-row corank test that was false.
Its failed assertion was initially hidden by a shell pipeline. That result is
withdrawn. The current five-chart generators do not use it.

## Exact live problem

Compute the exact characteristic-zero dimensions of all five affine charts
of $\mathcal I$. Use those results to decide the corank and grade questions

$$
I_4(M):d^\infty=(1),\qquad
\operatorname{grade}(I_5(M):d^\infty)=6,
$$

and then determine on every retained component whether some $\eta_{ij}$ is
generically nonzero.

The first equality excludes corank two on the accepted open. Grade six would
make the expected determinantal carrier a pure Cohen--Macaulay curve under
the relevant determinantal hypotheses. The Pluecker test removes degenerate
marking components. None of these conclusions follows merely from the
existence of a smooth point.

## Tasks and deliverables

### P5-L7A — Exact five-chart dimension run

Status: ready.

Inputs: [`RMU-5C7E0012`](../working-mathematics/units/RMU-5C7E0012.md),
[`research-notes/lane7-projective-kernel-20260803-v1/`](lane-7-source-packet.md), and the pinned matrices
in [`research-notes/lane7-split-incidence-20260802-v1/`](lane-7-source-packet.md).

Deliverable: for each chart $u_i=1$, preserve the generated exact
$\mathbf Q$ input, Singular version and command, complete log, input hash,
dimension, codimension, and Gröbner-basis size in a new versioned run. Also
run at least one admissible prime as a discovery cross-check, clearly
separated from the characteristic-zero result.

### P5-L7B — Corank, grade, and components

Status: ready after the chart logs from P5-L7A are available.

Inputs: the five exact chart results, the original $M,d$, and the identities
in [`RMU-5C7E0011`](../working-mathematics/units/RMU-5C7E0011.md).

Deliverable: prove or refute $I_4(M):d^\infty=(1)$ and determine the grade
and equidimensional data of $I_5(M):d^\infty$. Preserve every intermediate
ideal. If a chart has unexpected dimension, give an exact generic point or
prime component rather than discarding it.

### P5-L7C — Genuine marking on each component

Status: blocked on component data from P5-L7B.

Inputs: each retained characteristic-zero component and the ten explicit
$\eta_{ij}$ from [`RMU-5C7E0011`](../working-mathematics/units/RMU-5C7E0011.md).

Deliverable: certify that at least one $\eta_{ij}$ is nonzero at the generic
point, or prove that the component is a degenerate marking component and
remove it from collision geometry.

### P5-L7D — Componentwise first-normal section

Status: blocked on P5-L7C.

Deliverable: generic coefficient and augmented ranks of the first-normal
system over each genuine component function field, including any locus on
which the first obstruction vanishes.

## Scope cautions

- The harvested programs define exact inputs but currently establish no
  chart dimension, grade, or component theorem.
- Finite-field dimensions do not by themselves determine the
  characteristic-zero answer.
- A determinantal component is not a genuine collision component until the
  Pluecker-open condition is checked.
- Vanishing of the first obstruction would identify a construction locus,
  not a failure of the computation.
- The regular type-$(5)$ stratum has not been globally excluded.

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
