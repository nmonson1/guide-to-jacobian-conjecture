---
title: "Model research brief — The projective kernel carrier for five-dimensional collisions"
description: "A self-contained mathematical handoff for a research model."
---

# The projective kernel carrier for five-dimensional collisions

<p class="claim-tag">Lane 7 · Updated 4 August 2026</p>

## Why this lane matters

This lane is an independent minimal-dimension problem, not a specialization
of the fixed nineteen-variable map. Cubic-homogeneous Keller maps in
dimensions three and four are known to be invertible, so dimension five is
the first possible dimension for a cubic-homogeneous counterexample; see
[Hubbers's low-dimensional classification](https://www.cs.ru.nl/E.Hubbers/pubs/nilpotent_jacobians_112500.pdf).
For
\(F(x)=x+T(x,x,x)\) and a collision \(F(v+u)=F(v)\), restricting the
nilpotent Jacobian pencil to \(\mathbf P(\langle u,v\rangle)\) and imposing
the symmetry/integrability identities produces the fifteen equations used
here. They are linear in the ten marking coordinates of \(u,v\).

Those fifteen collision equations admit an exact linear splitting.
What remains is a comparatively small determinantal problem whose geometry
would decide whether the regular five-dimensional collision family is a pure
curve and whether nonunique markings occur. A new lower-cost packet isolates
six maximal minors for the grade question, fifty block minors for a sufficient
corank test, and four collinearity equations in each marking chart. These can
be tried before a full primary decomposition. The Plücker open distinguishes
genuine collisions of two marked source points from proportional-marking
artifacts.

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
verifier. In the underlying split incidence, if
\(A=\mathsf U_{0:10}\), \(B=\mathsf U_{10:15}\), and the bottom five rows of
\(\mathsf V\) are \(LH\), then

\[
G=B-LA\in\operatorname{Mat}_{5\times5}(A_0).
\]

This is the \(G\) used in the fifty-minor block filter below. The splitting
reconstructs a second marking vector
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

### One exact finite-field smooth germ

At \(a=(8,7,1,7,2,9,0)\) over \(\mathbf F_{11}\), one has \(d=1\),
\(\operatorname{rank}M=4\). Six specified maximal minors vanish and their
\(6\times7\) Jacobian has rank six, so those six equations cut a smooth
one-dimensional local germ over \(\mathbf F_{11}\). This is an exact
finite-field witness and a useful choice of minors; by itself it proves no
global or characteristic-zero dimension statement.

### Lower-cost exact tests

Let \(J\) be the ideal of those six maximal minors. Since
\(J\subset I_5(M)\), an exact proof that \(J:d^\infty\) is proper of
dimension one over \(\mathbf Q\), together with properness of
\(I_5(M):d^\infty\), would force \(\operatorname{grade}I_5(M)=6\). If the
six-minor saturation is the unit ideal, the carrier may instead be empty;
that is an exact but different outcome and does not produce a pure curve.
The packet supplies the exact-Q six-minor calculation.

Using the stored block factorization of \(M\), the ideal
\(I_4(G)+I_4(QA)\) has fifty generators and contains every regular
corank-two point. If its \(d\)-saturation is the unit ideal, the corank-two
locus is empty. The converse is not asserted: nonunit output must be checked
with the missing mixed minors or the supplied ten Grassmann charts.

Finally, after a pivot reconstructs \(w=(CA)u\), proportionality of \(u\) and
\(w\) is cut out by four equations on each chart. Five exact-Q inputs, with
alternate-pivot and residual-locus fallbacks, therefore test the complement
of the genuine marking open without first decomposing the entire carrier.

## Live problem

The remaining problem has several distinct outputs and no output may be
silently substituted for another. The lower-cost tasks should normally be
tried first:

1. decide the six-minor grade witness over \(\mathbf Q\);
2. decide the fifty-minor sufficient corank filter and use its specified
   fallback if it is inconclusive;
3. measure the proportional-marking locus in all five charts with complete
   pivot coverage;
4. if needed, compute the five full projective-kernel chart dimensions; and
5. optionally obtain an exhaustive component decomposition and test the
   Plücker open on **every** component.

If grade six holds, the Eagon--Northcott complex makes \(\mathcal D\) a pure
Cohen--Macaulay curve before component decomposition. Dimensions alone do not
prove that grade statement, and a list of components without an
exhaustiveness certificate does not solve output 5. Conversely, an exact
exhaustive primary decomposition can decide output 5 without first proving
grade six; it does not by itself prove purity or Cohen--Macaulayness.

## Earlier full-chart campaign

The bounded [Lane 7 job-accounting snapshot](lane-7-source-packet.md#source-04806d2bf166b306)
records all 27 submitted chart jobs at its fixed capture time. No exact-
\(\mathbf Q\) result marker had passed the acceptance gate, so that snapshot
supplies no chart dimension. It remains useful for diagnosing resource-heavy
full-chart methods; good-prime output is only a cross-check. The smaller
witness packet is independent of those jobs.

## Current tasks

<!-- RETAINED_TASKS_START -->
### Test grade six using the explicit six-minor witness — Ready now

`TSK-L7-GRADE-SIX-V3` · computation, proof · sustained

**Goal.** Over Q, decide the saturated six-minor locus and separately certify whether the full d-localized determinantal carrier is proper and nonempty.

**Why it matters.** A proper one-dimensional witness together with a proper full carrier proves grade I_5(M)=6 and activates Eagon--Northcott; an empty carrier is a different exact outcome.

**Public inputs.**

- [Split collision incidence with intrinsic marking-open condition](../working-mathematics/units/RMU-5C7E0011.md) (retained unit `RMU-5C7E0011`).
- [Definitions, proof of sufficiency, exact F11 witness, and execution boundary.](lane-7-source-packet.md#source-a55e11979cae7b07).
- [Fail-closed exact-Q saturation and dimension input.](lane-7-source-packet.md#source-b153cd426bdc04e3).

**Complete when.**

- Either a proper one-dimensional six-minor saturation and a proper full carrier prove grade six, the full carrier is certified empty, or a checked higher-dimensional component explains why this witness is insufficient.

**Possible starts.**

- Run the exact-Q six-minor input, then test properness of I_5(M) over Q before invoking the expected-height bound.

**Freedom.**

- A structural grade or emptiness argument may replace the calculation.

**Mathematical limits.**

- The F11 point does not prove characteristic-zero nonemptiness.
- A unit six-minor ideal does not imply that a pure curve exists.

### Test corank two with the 50-minor block filter — Ready now

`TSK-L7-CORANK-TWO-V3` · computation, proof · sustained

**Goal.** Decide over Q whether the sufficient 50-minor ideal I_4(G)+I_4(QA), saturated by d, is unit; if not, decide the full I_4(M) locus by mixed minors or all ten Grassmann charts.

**Why it matters.** This can certify uniqueness of the projective marking at lower cost while retaining a complete exact fallback.

**Public inputs.**

- [Split collision incidence with intrinsic marking-open condition](../working-mathematics/units/RMU-5C7E0011.md) (retained unit `RMU-5C7E0011`).
- [Block identity, sufficiency proof, fallback contract, and exact variable conventions.](lane-7-source-packet.md#source-a55e11979cae7b07).
- [Exact-Q 50-minor saturation input.](lane-7-source-packet.md#source-916ead81bace4dac).
- [Exact M, G, Q, and A data from which mixed-minor or Grassmann fallback inputs can be generated.](lane-7-source-packet.md#source-8ac5c833df312401).

**Complete when.**

- An exact unit-filter certificate is checked, the full I_4(M) locus is proved empty after an inconclusive filter, or a concrete d-nonzero corank-two point is verified against every minor.

**Possible starts.**

- Try the sufficient filter first; on nonunit output generate the missing mixed-minor or ten-chart full-rank tests from the exact bundle.

**Freedom.**

- A theoretical block-rank argument can replace elimination.

**Mathematical limits.**

- Finite-field emptiness alone is not a characteristic-zero certificate.
- Nonunit output from the sufficient filter is not a corank-two point.

### Measure the forbidden proportional-marking charts — Ready now

`TSK-L7-MARKING-OPEN-V1` · computation · sustained

**Goal.** Compute the exact-Q dimensions of the four-equation proportional-marking locus on each of the five projective-kernel charts and certify the pivot-atlas and residual-locus coverage.

**Why it matters.** This directly tests the complement of the genuine independent-marking open without requiring exhaustive component decomposition first.

**Public inputs.**

- [Split collision incidence with intrinsic marking-open condition](../working-mathematics/units/RMU-5C7E0011.md) (retained unit `RMU-5C7E0011`).
- [Five-chart presentation of the Lane 7 projective kernel incidence](../working-mathematics/units/RMU-5C7E0012.md) (retained unit `RMU-5C7E0012`).
- [Five exact-Q collinearity-chart inputs with pivot and residual fallbacks.](lane-7-source-packet.md#source-9069e4fddcd97c1d).
- [Derivation of the four-equation chart test and exact scope.](lane-7-source-packet.md#source-a55e11979cae7b07).

**Complete when.**

- All five characteristic-zero dimensions and every coverage fallback have exact independently checked receipts.

**Possible starts.**

- Run the five primary pivot charts, then prove coverage or run every residual and alternate-pivot case named by the packet.

**Freedom.**

- A symbolic proportionality argument may replace individual chart computations.

**Mathematical limits.**

- Chart dimensions alone do not certify a complete minimal-prime list.
- Retain the d-localization and all uncovered pivot loci.

### Fallback: compute all five exact kernel-chart dimensions — Ready now

`TSK-L7-EXACT-CHART-DIMENSIONS-V2` · computation · open ended

**Goal.** If the smaller witness calculations do not settle the carrier, obtain independently verified characteristic-zero dimensions for all five full localized projective-kernel charts.

**Why it matters.** This supplies exact global size data when the lower-cost ideals are inconclusive.

**Public inputs.**

- [Five-chart presentation of the Lane 7 projective kernel incidence](../working-mathematics/units/RMU-5C7E0012.md) (retained unit `RMU-5C7E0012`).
- [Exact-Q chart generator and result-marker convention.](lane-7-source-packet.md#source-03cf56b8bd9c6caf).
- [Bounded job history and accepted-result gate.](lane-7-source-packet.md#source-04806d2bf166b306).

**Complete when.**

- Every chart has a completed exact-Q marker, matching input hash, exit-zero receipt, and independent dimension replay.

**Possible starts.**

- Use the lower-cost six-minor, block-filter, and collinearity tasks first; diagnose prior heap-section failures before selecting a new exact algorithm.

**Freedom.**

- Certified modular reconstruction or a different exact characteristic-zero CAS is allowed.

**Mathematical limits.**

- Do not infer Q-dimensions from good-prime output.
- Do not infer grade, components, or marking openness from dimensions alone.

### Optional structural project: exhaust the collision components — Ready now

`TSK-L7-COMPONENTS-PLUCKER-V3` · proof, computation, exploration · open ended

**Goal.** If a global structural description is useful, determine every minimal component of the d-localized collision carrier with an exhaustiveness certificate and decide the independent-marking Plücker open on each.

**Why it matters.** This gives a complete geometric decomposition, but is not required before attempting the smaller grade, corank, or collinearity tests.

**Public inputs.**

- [Split collision incidence with intrinsic marking-open condition](../working-mathematics/units/RMU-5C7E0011.md) (retained unit `RMU-5C7E0011`).
- [Exact component and Plücker bundle.](lane-7-source-packet.md#source-867e4fccbf4a8d1c).

**Complete when.**

- Every minimal prime is certified exhaustive and every component has an exact verdict for the ten eta_ij coordinates.

**Possible starts.**

- Seek structural irreducibility or a certified exact-Q primary decomposition after localizing at d.

**Freedom.**

- A structural irreducibility theorem can replace explicit decomposition.

**Mathematical limits.**

- Report every minimal component, not only those found by one chart or heuristic.
- Keep the d-localization and Plücker open explicit.
- Do not infer purity or Cohen--Macaulayness unless grade is separately proved.
<!-- RETAINED_TASKS_END -->

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
- [Bounded chart-job accounting and acceptance gate](lane-7-source-packet.md#source-04806d2bf166b306)
- [Six-minor, fifty-minor, and collinearity workflow packet](lane-7-source-packet.md#source-a55e11979cae7b07)
- [Independent small-witness packet verifier](lane-7-source-packet.md#source-881d49c2fd46c63c)

## Sources and release

[Retained working mathematics](../working-mathematics/index.md) · [Optional runnable source ZIP](../inputs/lane-7-source-files.zip) · [Current proof sources](../proof-sources/index.md) · [Machine-readable release metadata](release.json)

The linked source text is preferred for full proof context; PDFs are optional archival copies.

[Back to the portfolio hub](state-of-the-program.md)
