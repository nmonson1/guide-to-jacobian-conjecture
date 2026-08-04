---
title: "Model research brief — From local normal recurrences to three-chart attachment"
description: "A self-contained mathematical handoff for a research model."
---

# From local normal recurrences to three-chart attachment

<p class="claim-tag">Lane 9 · Updated 4 August 2026</p>

## Why this lane matters

A nonzero condition in one chosen coefficient slice is not a geometric
obstruction. It becomes intrinsic only after every fresh parameter, overlap
correction, presentation relation, and adjacent-chart transport has been
included. This lane develops the exact interface needed to make that passage.

## Ambient coefficient windows for Lane 8's \(F_2\) family

Here \(F_2\) is [Lane 8's complete-corner-chain family](plane-newton-queue-terminal-certificates.md),
not a single polynomial map. The sets below are maximal independent-coefficient
windows for one terminal chart; the actual root-divisible and nonlinear
support conditions form a smaller locus supplied, in stages, by Lane 8.

After the denominator-five shear, write a monomial as \(x^{a/5}y^J\), where
\(a,J\in\mathbf Z\) and \(J\ge0\), put \(w=a-J\), and let
\(\langle w\rangle_5\in\{0,1,2,3,4\}\) be its residue. More explicitly,
a source monomial \(x^iy^j\) contributes, for \(0\le J\le j\), at

\[
(a,J)=(5i-j+J,J),\qquad w=a-J=5i-j.
\]

The maximal Newton-bounded support windows are

\[
S_P=\{(a,J):-60\le w\le15,\ 0\le J\le60-\langle w\rangle_5,\
5a-17J\le3\},
\]

\[
S_Q=\{(a,J):-100\le w\le25,\ 0\le J\le100-\langle w\rangle_5,\
5a-17J\le5\}.
\]

In the terminal chart

\[
x=t^{-25},\qquad y=t^{17}z,\qquad u=z^5,
\]

write

\[
P=t^{-3}\sum_rt^rA_r(z),\qquad
Q=t^{-5}\sum_rt^rB_r(z),
\]

where

\[
A_r=z^{(1-2r)\bmod5}\bar A_r(u),\qquad
B_r=z^{(-2r)\bmod5}\bar B_r(u).
\]

These maximal windows contain \(4433\) \(P\)-coefficients in \(981\)
nonempty layers and \(12340\) \(Q\)-coefficients in \(1663\) layers. They are
an independent-coefficient outer model. Lane 8 has now recovered the complete
linear descent selecting the actual root-divisible subspace: its 202 blocks
have \(533+1440=1973\) free coordinates and \(3900+10900=14800\) inherited
linear relations, with an exact triangular inverse. The nonlinear
common-power, determinant, open, and support-stratum conditions have not yet
been imposed.

## Parameter-complete finite-order system

Fix a characteristic-zero coefficient field \(K\). At normal order \(r\), let
\(V_r^{\mathrm{corr}}\) be the finite-dimensional space of endpoint and
overlap corrections, \(V_r^{\mathrm{fresh}}\) the space of every fresh
parameter, and

\[
W_r
\]

the finite-dimensional equation space with one coordinate for every
determinant, overlap, support, presentation, and cyclic-descent equation at
that order. This \(W_r\) is an equation space, not the scalar series \(W(T)\)
of the exact-normal-linearization coordinates. Put
\(X_r=(x_r,p_r)\in V_r^{\mathrm{corr}}\oplus
V_r^{\mathrm{fresh}}\). After lower orders are fixed, the complete affine
system is

\[
M_rX_r=b_r,\qquad
M_r=[C_r\mid P_r]:
V_r^{\mathrm{corr}}\oplus V_r^{\mathrm{fresh}}\longrightarrow W_r,
\qquad b_r\in W_r.
\]

Here \(C_r\) contains endpoint and overlap correction columns, while \(P_r\)
contains all fresh-parameter columns. The intrinsic obstruction quotient and
forcing class are

\[
\operatorname{Ob}_r=\operatorname{coker}M_r
=W_r/(\operatorname{im}C_r+\operatorname{im}P_r),
\qquad [b_r]\in\operatorname{Ob}_r.
\]

The full system is solvable exactly when \([b_r]=0\), equivalently

\[
b_r\in\operatorname{im}C_r+\operatorname{im}P_r.
\]

Its dual space of obstruction functionals is

\[
\operatorname{Ob}_r^\vee\simeq\ker M_r^t
=\ker C_r^t\cap\ker P_r^t.
\]

Thus a left-null functional \(\lambda^tC_r=0\) from the
fresh-parameter-zero slice is intrinsic only if \(\lambda^tP_r=0\).

For the \(C_5\)-character decomposition, assume that \(K\) contains a chosen
primitive fifth root of unity and that every displayed space, map, and forcing vector is
\(C_5\)-equivariant. Otherwise make the character decomposition after the
separable extension \(K(\zeta_5)\); finite-system feasibility is unchanged by
that extension. Feasibility must hold in every character block.

## Reusable mathematics

In the retained weighted slice, define the nonlinear order-\(r\) forcing

\[
\Phi_r(z)=\sum_{\substack{i+j=r\\i,j>0}}
\bigl((3-i)A_iB'_j+(j-5)A'_iB_j\bigr).
\]

After the earlier linear equations have been solved through order \(r-10\),
\(\omega_r=[z^0]\Phi_r\). Thus \(\omega_r\) is one constant output
coordinate in that slice; it is not an intrinsic obstruction unless it
descends to the displayed cokernel \(\operatorname{Ob}_r\).

1. The first target coordinate outside the linear image in the maximal-window
   model is the constant coefficient at order \(510\).
2. One exact rational weighted slice uses parameters at orders \(10\), \(260\),
   and \(270\) to cancel \(\omega_{510}\) and \(\omega_{520}\).
3. The formerly nonzero value of \(\omega_{530}\) was obtained after setting
   all new coordinates to zero. Reopening five order-\(280\) coordinates gives a four-dimensional
   \(\omega_{510}\)-kernel, a three-dimensional joint
   \(\omega_{510},\omega_{520}\)-kernel, and a direction cancelling
   \(\omega_{530}\). The determinant vanishes through order \(530\).
4. This order-\(530\) result is still a slice: it reopens only order \(280\)
   and does not impose the now-explicit inherited root-divisibility relations
   or the nonlinear actual-chain conditions.
5. In lower-face coordinates \(t=Y,z=XY^2\), the **bare \(k=4\) wall** is
   the Laurent shear \(X'=X\), \(Y'=Y+\lambda X^{-4}\). Equivalently,
   \(t'=t(1+h)\), \(z'=z(1+h)^2\), with
   \(h=\lambda t^7z^{-4}\). “Bare” distinguishes this operation from the
   corrected Rees/Kummer candidate. The ambient wall groupoid has \(73\)
   exact replay tests for coefficient, equation, overlap, dual, and quotient
   transport. The bare wall starts at normal order seven and is the identity
   through order six. These ambient transports are not yet the actual
   adjacent \(F_2\) chart.

For the ambient wall model used below, \(E_0\) is the full degree-21
coefficient window through layer 15 and \(T_E(\lambda)\) is the exact wall
transport on that window. Put \(E_\lambda=T_E(\lambda)E_0\); thus
\(E_1\) and \(E_{-1}\) are the transported windows at parameters \(1\) and
\(-1\). Their sum is the minimal three-chart ambient saturation, while
their common intersection is the all-parameter stable core. These are
ambient Laurent-jet charts, not the missing actual adjacent \(F_2\) charts.

The sufficiency of the three parameters is an exact finite-order statement,
not a sampling heuristic. Through the stated cutoff the transport is
\(T_E(\lambda)=I+\lambda N+\lambda^2N^2/2\) with \(N^3=0\). Hence every
coordinate outside \(E_0\) is a polynomial of degree at most two in
\(\lambda\); vanishing at \(0,1,-1\) is equivalent to vanishing for every
parameter. The verified first- and second-order wall images likewise show
that \(E_0+E_1+E_{-1}\) contains the entire minimal orbit saturation.

## Live problem

Lane 9 is the attachment companion to Lane 8.  Lane 8 is responsible for the
actual nonlinear \(F_2\) locus, exhaustive support strata, and exported normal
windows.  Lane 9 is responsible for adjoining the actual adjacent-chart
correction and fresh-parameter spaces, transporting them through overlaps,
and deciding the resulting parameter-complete obstruction classes.

The ready shared task is first to prove the finite obstruction-groupoid
theorem used in Lane 6, with the \(C_5\)-grading, filtered
correction/fresh/equation spaces, dual transport, and relation homotopies made
explicit in a fail-closed schema and checker.  Specializing that checker to
the supplied ambient \(E_0,E_1,E_{-1}\) wall charts is a separate bounded
certificate task, blocked only until the interface exists.  The ambient task
does not require actual \(F_2\) matrices and does not manufacture them.

The abstract cohomological criterion is standard; the useful output is the
certificate infrastructure that makes the finite move list, overlap maps,
and claimed exhaustiveness explicit and independently checkable.

The geometric \(F_2\) application is separate and blocked. The linear
inherited-relation packet is available, but it still requires Lane 8's
nonlinear actual normal windows and support strata, together with an
adjacent-chart presentation. Only then can one export matched blocks
\(M_r=[C_r\mid P_r]\), continue the parameter-complete system beyond order
\(530\), and transport it through an actual overlap. The current
zero-new-coordinate and order-280 slices cannot be promoted to those
claims.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Prove and implement the fail-closed obstruction-groupoid interface — Ready now

`TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3` · proof, reusable interface theorem, computation · bounded

**Goal.** State and prove the finite generator-and-relations transport and contractible-stabilization theorem, define a certificate schema containing every required complex, map, homotopy, forcing coboundary, quotient, and dual field, and implement a checker that rejects any omitted or inconsistent field.

**Why it matters.** This supplies one reusable theorem and machine-checkable interface for both homogeneous-presentation transport and plane-chart attachment.

**Public inputs.**

- [Parameter-complete obstruction criterion for an F2 attachment block](../working-mathematics/units/RMU-6C9E0011.md) (retained unit `RMU-6C9E0011`).
- [Existing finite transition, quotient, dual, forcing, relation, and stabilization contract.](lane-9-source-packet.md#source-6b8deae43ed5055d).
- [Current exact checker schema to extend fail-closed.](lane-9-source-packet.md#source-32f266f643e1100f).

**Complete when.**

- The theorem is proved, every proof hypothesis is a required certificate field, valid examples replay, and mutation tests show that omission or corruption of each field fails.

**Possible starts.**

- Prove functoriality on generators and relation words, then encode exactly the identities used by the proof as mandatory schema fields and negative tests.

**Freedom.**

- An equivalent derived formulation is allowed if it exports the same finite certificate and verdict.

**Mathematical limits.**

- The interface does not discover or prove exhaustive any program-specific geometric operation groupoid.
- Passing the schema does not identify ambient wall charts with actual adjacent F2 charts.

### Certify the characteristic-zero ambient three-wall atlas — Blocked

`TSK-L6-L9-AMBIENT-WALL-CERTIFICATE-V1` · computation, proof · bounded

**Goal.** Encode the supplied characteristic-zero E_0,E_1,E_{-1} wall atlas in the certified schema and prove by one hash-pinned replay that its transitions, relations, forcing transport, quotients, duals, and triple overlaps pass.

**Why it matters.** This gives the shared interface one concrete cross-lane benchmark without confusing the ambient atlas with either program's missing geometric groupoid.

**Public inputs.**

- [Exact k=4 wall transport, grading correction and finite overlap groupoid](../working-mathematics/units/RMU-6C9E0010.md) (retained unit `RMU-6C9E0010`).
- [Exact ambient wall maps and finite-order overlap identities.](lane-9-source-packet.md#source-d6c38a4c865ab7c9).
- [Dual transport and triple-overlap theorem for the ambient atlas.](lane-9-source-packet.md#source-bcb444020cf39f50).

**Task dependencies.**

- `TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3`

**Blocked on.**

- The fail-closed shared certificate schema and checker have not yet been completed.

**Complete when.**

- The complete ambient certificate and source hashes pass the shared checker and independently reproduce all 73 declared identities.

**Possible starts.**

- Use the nilpotent quadratic wall transport to certify that parameters 0, 1, and -1 generate the stated finite-order ambient saturation in characteristic zero.

**Freedom.**

- An equivalent three-parameter certificate is allowed if its equivalence to the supplied atlas is proved.

**Mathematical limits.**

- The certificate does not prove either geometric operation list exhaustive.
- The ambient wall charts are not the absent actual adjacent F2 charts.

### Attach Lane 8's actual F2 blocks across three charts — Blocked

`TSK-L9-ACTUAL-F2-ATTACHMENT-V5` · computation, proof · open ended

**Goal.** Receive Lane 8's matched nonlinear F2 blocks and support strata, encode the adjacent-chart maps in the shared interface, and continue the parameter-complete obstruction system beyond order 530.

**Why it matters.** This is the attachment companion to Lane 8: it turns local actual-family data into an intrinsic three-chart obstruction or realization statement.

**Public inputs.**

- [Exact root-divisibility coordinates for the degree-125 F2 linear descent](../working-mathematics/units/JCG-66D861AF.md) (retained unit `JCG-66D861AF`).
- [Exact k=4 wall transport, grading correction and finite overlap groupoid](../working-mathematics/units/RMU-6C9E0010.md) (retained unit `RMU-6C9E0010`).
- [Parameter-complete obstruction criterion for an F2 attachment block](../working-mathematics/units/RMU-6C9E0011.md) (retained unit `RMU-6C9E0011`).
- [Exact F2 weighted-slice continuation through order 530](../working-mathematics/units/RMU-6D8E0015.md) (retained unit `RMU-6D8E0015`).
- [Parameter-complete block and obstruction contract.](lane-9-source-packet.md#source-89e4eda45b4d5d16).

**Task dependencies.**

- `TSK-L6-L9-OBSTRUCTION-GROUPOID-SCHEMA-V3`
- `TSK-L8-F2-ACTUAL-LOCUS-V2`

**Blocked on.**

- Lane 8 has not yet supplied the nonlinear actual locus, support strata, and exported normal windows.
- The actual adjacent-chart coefficient, equation, fresh-parameter, dual, and overlap matrices are absent.

**Complete when.**

- Lane 8's actual matched blocks pass relation, quotient, dual, forcing, and cocycle checks and yield a parameter-complete verdict through a stated order beyond 530.

**Possible starts.**

- Use the shared schema to specify every required pairwise and triple-overlap map before testing forcing classes.

**Freedom.**

- A stronger constructible-locus attachment theorem may replace order-by-order continuation.

**Mathematical limits.**

- The zero-new-coordinate and order-280 slices are not actual-chain obstructions.
- Ambient wall maps are a benchmark, not the missing adjacent F2 chart.
- Do not redo Lane 8's completed 202-block linear parametrization.
<!-- RETAINED_TASKS_END -->

## Exact sources

- [Lane 8/9 recovery audit](lane-9-source-packet.md#source-38ab8bd19d25aff4)
- [Fresh-order-\(280\) exact program](lane-9-source-packet.md#source-151645a0e17f5aa6)
- [Machine-readable evidence](lane-9-source-packet.md#source-ab81932dfb3d4762)
- [Normal-linearization source](../proof-sources/06-plane-boundary/appendices/exact-normal-linearization.md)
- [Ambient wall-overlap theorem](lane-9-source-packet.md#source-d6c38a4c865ab7c9)
- [Dual and triple-overlap theorem](lane-9-source-packet.md#source-bcb444020cf39f50)
- [Cyclic wall-parameter descent](lane-9-source-packet.md#source-fa8ccec644530dcc)
- [Exact 202-block linear root-divisibility coordinates](lane-9-source-packet.md#source-e1384a8451d58dd7)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-9-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
