# The projective kernel carrier for five-dimensional collisions

Lane 7 · 2026-08-03

## Why this lane matters

The fifteen original collision equations admit an exact linear splitting.
What remains is a comparatively small determinantal problem whose geometry
would decide whether the regular five-dimensional collision family is a pure
curve and whether nonunique markings occur. Purity controls whether the
known smooth germ is representative or sits beside hidden higher-dimensional
pieces; the Plücker open distinguishes genuine collisions of two marked
source points from coincident-marking artifacts.

## Setup and notation

Let

\[
A_0=\mathbf Q[a_0,\ldots,a_6].
\]

The exact source packet defines an irreducible quartic
\(d\in A_0\) and a matrix

\[
M(a)\in\operatorname{Mat}_{10\times5}(A_0).
\]

Write \(I_j(M)\) for the ideal of \(j\times j\) minors. On the regular open
\(D(d)\), the parameter carrier is

\[
\mathcal D=V(I_5(M))\cap D(d).
\]

For a nonzero column \(u=(u_0,\ldots,u_4)^t\), the projective-kernel
incidence is

\[
\mathcal I=\{(a,[u])\in D(d)\times\mathbf P^4:M(a)u=0\}.
\]

The exact component-input bundle supplies \(d\) and the matrices
\(M,A,CA,H,C,Q,R\) directly, together with a hash-pinned reconstruction and
verifier. The splitting reconstructs a second marking vector
\(v=-d^{-1}C(a)A(a)u\). Put \(w=(CA)u\) and

\[
\eta_{ij}=u_iw_j-u_jw_i.
\]

The two markings are independent exactly on the open set where at least one
\(\eta_{ij}\ne0\). This Plücker-open condition must remain visible in every
component calculation.

The five standard charts \(u_i=1\) have the ten equations \(M(a)u=0\)
together with a localization equation \(zd-1=0\). Their exact generated
inputs are supplied below.

## Reusable mathematics

### Global splitting

The original \(15\times10\) marking incidence is polynomially equivalent to
a residual system, and on \(D(d)\) it is scheme-theoretically equivalent to
\(M(a)u=0\), with the second marking reconstructed by the displayed formula.

The earlier fifteen-quintic input is the affine normalization
\(a_7=v_4=1\) of the same homogeneous marking incidence. After \(v_4\) is
restored, the split factorization gives, on \(D(d)\), the inverse
reconstruction \(v=-d^{-1}(CA)u\). Thus the five projective-kernel charts
\(u_i=1\) replace the marking variables only on \(D(d)\); the older open
\(u_3-u_4v_3\ne0\) is one of the ten independent-marking opens, not an
additional component condition.

### Boundary factorization

The supplied exact matrices satisfy

\[
CH=dI_5,\quad QH=0,\quad CR=0,\quad QR=dI_5,\quad HC+RQ=dI_{10}.
\]

Consequently the splitting degenerates precisely on \(d=0\). The compact
bundle verifier reconstructs every matrix from the maintained sources and
checks all five identities.

### Exact nonuniqueness locus

The locus with a kernel of dimension at least two is

\[
V(I_4(M))\cap D(d).
\]

Thus uniqueness of the projective marking on the regular carrier is
equivalent to \(I_4(M):d^\infty=(1)\).

### One smooth branch

At \(a=(8,7,1,7,2,9,0)\) over \(\mathbf F_{11}\), one has \(d=1\),
\(\operatorname{rank}M=4\), and rank six for the determinantal normal map.
This gives a one-dimensional characteristic-zero component through the
lifted smooth germ. It does not prove purity elsewhere.

## Live problem

Prove that \(I_5(M)\) has grade six after localization at \(d\), retaining
the Plücker open, and determine whether
\(V(I_4(M))\cap D(d)\) is empty.

If the grade is six, the Eagon--Northcott complex makes \(\mathcal D\) a pure
Cohen--Macaulay curve before component decomposition. The remaining work is
to prove the grade, identify its components, and decide which meet the
independent-marking open.

## Ready task L7-T1 — grade six from the split architecture

**Inputs.** The self-contained
[component and Plücker bundle](lane-7-source-packet.md#source-867e4fccbf4a8d1c),
its [exact machine-readable data](lane-7-source-packet.md#source-8ac5c833df312401),
and its verifier, supplying \(d,M,A,CA,H,C,Q,R\); the complete
[split-incidence theorem](lane-7-source-packet.md#source-a0e37d2743e92c4e),
and the [five projective-kernel charts](lane-7-source-packet.md#source-740f2fbd37373ad8).

**Deliverable.** Give a characteristic-zero proof that
\(I_5(M)A_0[d^{-1}]\) has grade six, or exhibit a lower-grade associated
prime. State the resulting Eagon--Northcott consequences and determine, on
each component found, whether some \(\eta_{ij}\) is nonzero. Also test or
reduce the exact corank-two target \(I_4(M):d^\infty=(1)\).

**Dependencies.** Only the pinned polynomial identities over
\(\mathbf Q[a_0,\ldots,a_6]\) and localization at \(d\).

**Limits.** Expected codimension and the one smooth point do not prove global
grade, purity, or Plücker openness.

## Optional exact-CAS route

The [projective-kernel packet](lane-7-source-packet.md#source-740f2fbd37373ad8)
contains generators for all five rational and good-prime charts, including
the exact [chart generator](lane-7-source-packet.md#source-8b6128de9797b077).
A useful computation should preserve the exact characteristic-zero output
and use finite characteristic only as a cross-check. It should report
dimension before attempting grade or decomposition, and it must keep the
Plücker-open question separate.

Connections to Lane 4 are welcome when they preserve the localization and
marking-open hypotheses.

## Exact sources

- [Complete theorem and proof](lane-7-source-packet.md#source-a0e37d2743e92c4e)
- [Self-contained component and Plücker bundle](lane-7-source-packet.md#source-867e4fccbf4a8d1c)
- [Exact machine-readable component data](lane-7-source-packet.md#source-8ac5c833df312401)
- [Exact bundle verifier](lane-7-source-packet.md#source-03ebac2c2b77f766)
- [Identity checker](lane-7-source-packet.md#source-d3702b088e5916ba)
- [Five-chart input packet](lane-7-source-packet.md#source-740f2fbd37373ad8)
- [Macaulay2 generator](lane-7-source-packet.md#source-03cf56b8bd9c6caf)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-7-source-packet.md) · [Exact collision-chart input](lane-7-collision-input.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
