# Lane 7: Five-dimensional collision geometry

## Problem and scope

Consider cubic-homogeneous Keller maps `X-H(X)` in five variables whose
quadratic Jacobian pencil is everywhere regular of generic Jordan type `(5)`
along a collision line. Lane 7 asks for the characteristic-zero component
geometry of the exact full-kernel collision chart and for the first-normal
obstruction on each component.

Here *Keller* means `det(I-JH)=1`. An *everywhere-regular type-(5) pencil*
is one for which `JH(su+tv)` is a single nilpotent Jordan block for every
`[s:t] in P^1`. A *collision-line datum* is a pair of distinct points with
the same image together with the projective pencil on their span; after
translation and scaling the points are represented by `v` and `v+u` below.

This is separate from the 19-to-18 compression problem of Lane 6.

## Setup and notation

Choose independent vectors `u,v` with `F(v+u)=F(v)`. Polarize `H` to the
symmetric trilinear tensor `mathcal T` and put

```text
A_0=JH(u),   B_0=6*mathcal T(u,v,-),   C_0=JH(v).
```

The collision and integrability equations include
`B_0*u=2*A_0*v` and their polarized companions. For the regular nilpotent pencil
on `P^1`, the kernel filtration has quotient
degrees `(-4,-2,0,2,4)`. On the full-span chart the eight parameters form

```text
C*lambda + Sym^6(C^2),
```

where `lambda=a_7`. In the full-kernel factorization, `T_frame` is the
constant invertible `4 x 4` frame matrix. If `I_2,I_4` are the standard
degree-two and degree-four binary-sextic invariants in the source's
normalization, regularity is controlled by

```text
det(T_frame)=((lambda^2+4I_2)^2-96I_4)/256.
```

The normalized full-kernel chart is cut out by 15 primitive quintics on the
open locus

```text
det(T)*(u_3-u_4*v_3) != 0.
```

Here `+` denotes direct sum of representations. The relevant symmetry is the
natural `SL_2` action on the binary sextic factor, together with scalar
rescaling of the marked line. The [exact public collision packet](lane-7-collision-input.md)
gives the 16-variable chart, all 15 primitive quintics, both open factors, an
exact smooth `F_11` point, and a complete Macaulay2 input. Those generated
equations, rather than this prose summary, define the computational scheme.
The eight parameters describe the pencil. After the normalizations `a_7=1`
and `v_4=1`, adjoining the marked vectors `u` and `v` gives the 16 variables
listed on the packet page.
The surrounding homogeneous-map conventions are in
[`manuscripts/05-homogeneous-descendants/main.tex`](../proof-sources/05-homogeneous-descendants/main.md); the packet page is the
complete public input for the component calculation.

## Reusable mathematics

The collision and integrability equations have a smooth one-dimensional
characteristic-zero family obtained by Hensel lifting an explicit smooth
`F_11` point ([`JCG-FFBBD77B`](../working-mathematics/units/JCG-FFBBD77B.md)). The entire `Z_11` residue disk through it has
no first-normal extension: independently assembled systems have ranks
`(60,61)` and `(125,126)` ([`JCG-64E18DF3`](../working-mathematics/units/JCG-64E18DF3.md)).

Thirty rational collision points over `F_7`, `F_11`, and `F_13` have nonzero
first-normal obstruction ([`JCG-86F5C9FA`](../working-mathematics/units/JCG-86F5C9FA.md)). This sample does not describe
characteristic-zero components.

For every globally defined generically type-`(5)` quadratic nilpotent matrix,
the rank-at-most-three locus has codimension at most two. If it extends an
everywhere-regular collision line, the codimension is exactly two and the
locus misses that line ([`JCG-15D52C7B`](../working-mathematics/units/JCG-15D52C7B.md)).

Two monolithic Macaulay2 runs produced no dimension, degree, or component
data. They are failed attempts, not negative mathematical evidence.

The marking variables can now be eliminated globally. Writing the complete
homogeneous fifteen-by-ten marking matrix as `Theta=[U|V]`, an explicit
polynomial matrix `C_u` satisfies `C_u U=I_5`. Hence the full projectivized
marking incidence is covered by the five intrinsic charts `D(v_i)`, not only
the formerly normalized chart `v_4=1`. On `D(d)`, explicit ten-by-ten matrices
give a matrix factorization of `d`, and the full system is equivalent to

```text
M(a)u=0,   v=-d^-1 C(a)A(a)u,
rank(Theta)=5+rank(M),       M in Mat_(10 x 5).
```

The determinant identities are
`det[H R]=-(256/243)d^2` and `det[C;Q]=-(243/256)d^8`. Unit:
[`RMU-5C7E0010`](../working-mathematics/units/RMU-5C7E0010.md); theorem, original fifteen equations, reconstruction helper,
exact matrices and two successful checkers:
[`research-notes/lane7-split-incidence-20260802-v1/`](lane-7-source-packet.md).

## Exact live problem

On `D(d)`, prove or refute

```text
I_4(M):d^infinity=(1)
```

and determine whether `I_5(M)` has grade six. The first equality excludes
corank two in the marking incidence; the second would make the regular carrier
a pure Cohen--Macaulay curve by Eagon--Northcott. Neither follows from the
known smooth point or expected codimension. A geometric interpretation of
`M` compatible with the `C*lambda+Sym^6(C^2)` action is preferred, but an
exact characteristic-zero saturation or grade certificate is also complete.

## Tasks and deliverables

### P5-L7A — Corank-two exclusion for the residual matrix

Status: ready.

Inputs: [`RMU-5C7E0010`](../working-mathematics/units/RMU-5C7E0010.md) and the complete standalone packet in
[`research-notes/lane7-split-incidence-20260802-v1/`](lane-7-source-packet.md), especially the stored
matrix `M`, determinant `d`, reconstruction script and theorem note.

Deliverable: a proof or exact certificate for `I_4(M):d^infinity=(1)`, or an
explicit characteristic-zero point of the corank-two locus. Preserve the
coefficient field and every saturation boundary.

### P5-L7B — Staged characteristic-zero saturation

Status: local CAS task; ready from the public exact packet.

Inputs: the original Macaulay2 block plus the much smaller exact residual
matrix `M` and determinant `d` from [`RMU-5C7E0010`](../working-mathematics/units/RMU-5C7E0010.md).

Deliverable: report the Macaulay2 version and exact command, then compute the
grade and equidimensional data of `I_5(M)` on `D(d)` before primary
decomposition. Compare with the original fifteen-equation saturation and
preserve every intermediate ideal in a new versioned run.

### P5-L7C — Componentwise first-normal section

Status: blocked on component data from P5-L7A or P5-L7B.

Deliverable: generic coefficient and augmented ranks over each component
function field, including any construction locus.

## Scope cautions

- Finite-field points do not determine characteristic-zero components.
- Failed elimination is not evidence of emptiness or irreducibility.
- Vanishing of the first obstruction would identify a construction locus.
- The regular type-`(5)` stratum has not been globally excluded.
