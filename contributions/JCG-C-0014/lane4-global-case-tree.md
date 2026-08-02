# Rooted Lane 4 case tree with complement routing

## 1. Root and status convention

Let `k` be an algebraically closed field of characteristic zero, and let

\[
F=X+H_2+H_3+H_4:k^3\longrightarrow k^3,
\qquad F(0)=0,\quad DF(0)=I,\quad \det DF=1,
\]

with each `H_i` homogeneous of degree `i`.  This is the root object `Q4-ROOT`.
Write

\[
\rho_4=\dim_k\langle H_{4,1},H_{4,2},H_{4,3}\rangle.
\]

The tree distinguishes four statuses.

| Status | Meaning |
| --- | --- |
| `closed-import` | A conventional theorem is imported with the hypotheses listed in Section 4. |
| `closed-exact` | A finite calculation is publicly identified and its precise scope is recorded in the crosswalk. |
| `conditional` | The leaf closes only after one or more imported routing statements are independently verified. |
| `open` | A proof interface, omitted artifact, or terminal system remains unresolved. |

An `AUDIT-*` node is an unresolved proof interface.  It is not a claim that a
new geometric family exists.  `Q4-F4`, by contrast, is the surviving terminal
algebraic candidate after accepting the upstream interfaces.

## 2. Tree

### 2.1 Degree and leading target span

1. `Q4-ROOT` splits into `H_4=0` and `H_4\ne0`.
   - `H_4=0` is the degree-at-most-three branch and is closed by the recorded
     degree-three theorem.
   - `H_4\ne0` proceeds to `\rho_4=1,2,3`.  No division is used here, so these
     three rank strata are exhaustive determinantal children.
2. `\rho_4=1` is the rank-one leading branch.  Its use in a global quartic
   proof is `closed-import`, not re-proved in the Lane 4 packet.
3. `\rho_4=3` invokes the leading-image factorization
   \[
   H_4=G\,h(A,B),\qquad \gcd(A,B)=1,
   \qquad \deg G+\deg(h)\deg(A)=4,
   \]
   with `A,B` homogeneous of the same degree and `h:P^1\to P^2` a proper
   basepoint-free parametrization of the projective leading image.
   The theorem interface itself is `AUDIT-LEAD-FACT`: the public packet gives
   a candidate repair, but the global source has not yet been independently
   checked line by line.  Failure to establish any of rationality,
   basepoint-freeness, coprimeness, properness, or equality of source degrees
   routes to that named audit node; it is not silently discarded.
4. Once the factorization interface is accepted, the nondegenerate numerical
   possibilities are
   \[
   (\deg h,\deg A,\deg G)=(2,1,2),(2,2,0),(3,1,1),(4,1,0).
   \]
   The omitted value `\deg h=1` is exactly the line-image complement and
   returns to `\rho_4=2`.

### 2.2 Leading-span-three curve leaves

The four numerical children have the following ownership.

| Node | Leading image | Exact inherited hypotheses | Disposition |
| --- | --- | --- | --- |
| `S3-CONIC-FIXED` | `G` times a nondegenerate conic, `(2,1,2)` | `G` squarefree after multiplicity routing; conic parametrization proper; all stabilizer-orbit complements retained | candidate conic proofs plus exact terminal replays; conditional on orbit completeness |
| `S3-CONIC-PRIMITIVE` | quadratic Veronese source, `(2,2,0)` | coprime quadratic pair; no common basepoint; proper conic image | imported quadratic-source classification; public Lane 4 packet lacks the complete file-level crosswalk |
| `S3-CUBIC` | fixed linear factor times a proper rational cubic, `(3,1,1)` | cubic is reduced and proper; cusp/node classification; marked point or transverse factor routed | candidate proof plus exact displayed charts; conditional on orbit coverage |
| `S3-QUARTIC` | proper rational quartic, `(4,1,0)` | preceding frontier reduction leaves only tangent-syzygy types `(3,(1,2))` and `(2,(2,2))` | exact terminal calculations, but the frontier preclassification is `AUDIT-RQ-FRONTIER` |

For each curve normalization, the complement is explicit:

- conic rank degeneration routes to rank-one or span-two, not to a generic
  conic checker;
- a common factor or basepoint of the quadratic source routes to the fixed
  factor or basepoint child;
- reducible or nonproper cubic parametrizations route to their lower curve or
  fixed-factor owner;
- failure of the rational-quartic tangent-syzygy preclassification routes to
  `AUDIT-RQ-FRONTIER`.

Consequently, the often-used statement “leading target span three is
impossible” remains conditional.  It cannot be used to enter the span-two
branch without accepting `AUDIT-LEAD-FACT`, the curve-orbit interfaces, and
`AUDIT-RQ-FRONTIER`.

### 2.3 Leading-span-two reduction

After a constant target change, write

\[
H_4=(P,Q,0),\qquad R=(H_3)_3.
\]

The target change is invertible on the open set where two chosen leading
coordinates are independent.  Its vanishing determinant is exactly the
`\rho_4=1` child.

- `R=0` is `S2-R0`.  The candidate repair obtains a quadratic coordinate and
  then a plane Keller pair.  The plane theorem interface and descent are
  recorded in `proof-repairs.tex`.
- `R\ne0` enters the weighted leading relation.  Every localization in this
  reduction has a named zero child in the CSV.  The four-loci theorem is
  recorded as the interface `AUDIT-FOUR-LOCI`; until checked, no global claim
  may assume that the following owners are exhaustive.

The intended four owners are:

1. binary pencil: after a source change, `P,Q,R\in k[x,y]`;
2. genuinely nonbinary quadratic-source locus;
3. primitive coprime pencil containing a fourth power;
4. fixed-factor locus in which every genuinely nonbinary component is a
   special fiber of the rational pencil `P/Q`.

Overlaps are owned in that order: extract a fixed gcd first; send a binary
common generator to the binary tree; send rank-one source degeneration back
upstream; only then call a primitive chart.

### 2.4 Binary pencil

Let `G=gcd(P,Q)`.

#### Fixed factor

If `G\ne1`, route by `g=deg G`.

- `g=1,2,3` are the recorded binary fixed-factor bundles.  Their 38 replay
  groups are reported to pass, but the public Lane 4 packet does not expose a
  file-level command/hash row for every group.  The mathematical leaf is
  therefore conditional and the evidence interface is `AUDIT-BINARY-FIXED-XW`.
- `g=4` is rank one and returns to `\rho_4=1`.
- Any common factor hidden by a primitive normalization is the vanishing
  complement of that normalization and returns here.

#### Coprime pencil

Assume `G=1`.  Normalize a Hilbert--Burch matrix only on the chart where its
selected pivot minor is nonzero.  The zero-minor complement is `S2-ZERO-MINOR`
and is not obtained by specialization from a nonzero-minor formula.

On the all-minors-nonzero chart, let `r` be the ramification degree of the
pencil.

| Ramification | Child | Disposition |
| --- | --- | --- |
| `r=0,1,2` | `S2-RLE2` | recorded exact bundles; conditional on the public artifact crosswalk |
| `r=3`, Hilbert--Burch type `(2,5)` | `S2-R3-25` | routes to the earlier degree-two-ramification owner |
| `r=3`, type `(3,4)` | `S2-R3-34` | split by the weighted-inflection parameter and exceptional divisors |
| `r=4` | `S2-R4` | candidate projective proof plus exact standalone checker |
| `r=5` | `S2-R5` | aligned-power reduction, cubic-coordinate lemma, and plane theorem |

For `r=3`, every denominator or rank condition is bifurcated:

- `\tau+1\ne0` versus `\tau=-1`;
- generic weighted-inflection determinant nonzero versus its exceptional
  divisor;
- selected Hilbert--Burch pivot nonzero versus the alternate pivot chart;
- resultant/saturation factor nonzero versus each projective factor stratum;
- first normal amplitude nonzero versus the zero-normal plane-reduction child.

The packet supplies an exact checker for the complete displayed `\tau=-1`
branch.  The generic `(3,4)` formulas report a remaining exceptional family
`F_4`.  On that family one must solve the degree-six equations over

\[
\mathbb Q(\tau)[d]/(q_4(d,\tau))
\]

and then determine whether unrestricted lower binary terms in `H_3,H_2` can
cancel the degree-five obstruction.  No complete public checker is attached.
This is the terminal candidate `Q4-F4`.

### 2.5 Nonbinary quadratic-source, fourth-power, and fixed-component owners

- `S2-QUAD-SOURCE` uses nine recorded quadratic-source charts.  Every chart
  must state the nonzero minor used to normalize it and route the zero minor
  to the adjacent chart or rank-degenerate owner.  The mathematical source
  reports successful exact checks, but the public Lane 4 packet omits the
  per-chart hashes and commands; this is `AUDIT-QUAD-XW`.
- `S2-FOURTH-POWER` is the primitive coprime pencil containing a fourth
  power.  The aligned case and the zero-minor complement have distinct proof
  owners.
- `S2-NONBINARY-FIXED` uses the corrected valuation identity
  \[
  4\nu_\Gamma(R)=3s+c_\xi m,\qquad \sum_\xi c_\xi=3,
  \]
  without assuming `c_\xi\ge0`.  Binary common-generator components return
  to the binary tree.  The genuinely nonbinary endpoint is normalized to
  \[
  H_4=(x^4,xR,0),\qquad (H_3)_3=R,\qquad x\nmid R,
  \]
  and is closed only after the expanded homogeneous cubic centralizer lemma
  in `proof-repairs.tex`.

The valuation equation's possibilities `s=0` and `s>0`, negative `c_\xi`, a
binary component, and a component on which the pencil ratio is constant are
all explicit children in the CSV.  None is erased by a positivity argument.

## 3. Final quartic statement

This tree does not justify a theorem that every quartic Keller map is
invertible.  The strongest honest conclusion is:

> Conditional on the leading-image factorization, the exhaustive four-loci
> routing, the imported curve-orbit classifications, and the omitted
> proof-to-code interfaces, every recorded terminal quartic branch is closed
> except the exceptional primitive binary triple-ramification compatibility
> system `Q4-F4`.

`Q4-F4` is not an explicit map.  It is a finite normal-form compatibility
problem whose solution set has not been shown empty and whose points have not
been lifted back through the entire tree.  The unconditional public interval
therefore remains `4 <= D_min <= 7`.

## 4. Imported theorem-interface ledger

### 4.1 Plane degree criterion

Input:

- a plane Keller pair over an algebraically closed characteristic-zero field;
- at least one coordinate degree has at most two prime factors, counted with
  multiplicity;
- in Lane 4 the relevant degree set is `{1,2,3,4,5,6,7,9}`;
- after straightening a coordinate over `\overline{k(t)}`, the inverse must be
  descended uniquely to `k(t)` and then combined with the birational Keller
  implication.

The exact Appelgate--Onishi and Nowicki--Nakai locators and the field transfer
are in `proof-repairs.tex`.

### 4.2 Leading-image factorization

Required input and output:

- the projective leading image is a rational curve, not merely set-theoretic;
- the normalization map is represented by a coprime pair `A,B` of equal
  source degree;
- `h` is a proper basepoint-free parametrization, not a nonproper multiple
  cover;
- the fixed factor `G` is separated with multiplicity;
- line-image complement routes to `\rho_4=2`;
- the four numerical triples follow from `deg G + deg(h) deg(A)=4`.

Any unproved item above is `AUDIT-LEAD-FACT`.

### 4.3 Conic orbit leaves

A conic checker is called only after:

- conic rank and reducedness are fixed;
- the allowed source and target actions are stated;
- a stabilizer orbit representative is reached on an explicitly nonzero
  chart;
- the vanishing stabilizer invariant routes to another representative;
- arbitrary lower homogeneous coefficients allowed by the theorem are still
  present in the terminal determinant system.

The seven representatives used by the packet are owned separately.  A
terminal coefficient identity does not prove orbit completeness.

### 4.4 Rational cubic leaves

A cubic checker is called only after:

- the cubic is a proper reduced rational plane cubic;
- cusp and node are separated;
- the fixed linear factor is transverse, marked on a branch, or on the stated
  tangent/fiber orbit;
- the node branch interchange at infinity is covered;
- translation/localization determinants and their zero complements are
  routed;
- the exact checker retains the normal amplitudes permitted by the prose
  theorem.

### 4.5 Rational quartic frontier

The two exact tangent-syzygy systems are terminal only under the prior theorem
that all other proper rational-quartic orbit types have been eliminated or
routed.  That prior theorem is not replaced by the two terminal checks.
Failure of the preclassification is `AUDIT-RQ-FRONTIER`.

### 4.6 Binary ramification and Hilbert--Burch charts

For each chart record:

- `gcd(P,Q)` and primitive/coprime status;
- selected nonzero pivot minor and its zero child;
- ramification degree `r` and partition type;
- Hilbert--Burch degree type;
- resultant/saturation factors inverted;
- first and second normal amplitudes retained;
- coefficient field, including algebraic extensions such as the `F_4` field;
- whether the checker proves a displayed ideal, a saturation, or only a
  sample identity.

### 4.7 Specialization rule

No checker may be specialized by setting a denominator to zero unless the
zero locus is independently proved to be the scheme-theoretic closure of the
same chart.  In this contribution every such zero is instead routed to a
named sibling.  Likewise, a computation over a sample parameter value is not
used to prove a generic or exceptional family.

## 5. Degree-five/six fixed-factor boundary is not a quartic child

The condition

\[
V_{\mathbf P^2}(G,A,B)\ne\varnothing
\]

belongs to the degree-five/six fixed-factor conic appendix, where
`H_D=G(A^2,AB,B^2)` and `D=g+2e`.  It is not a missing quartic branch and must
not be used to block or close `Q4-F4`.

For `(g,e)=(3,1)` in degree five, the genuinely three-variable cubic factor is
already excluded; the binary overlap remains separate.  For `(g,e)=(1,2)`,
the pointed basepoint normal form in `proof-repairs.tex` reduces the surviving
locus to

\[
G=z,\qquad A=xy+z\ell_1,\qquad B=y^2+z\ell_2
\]

at a chosen basepoint `[1:0:0]`, after projective source and constant target
changes, with the stated regular-sequence and nonconstant-ratio hypotheses.
This resolves the ownership and normalization of the basepoint locus but not
the Keller equations on that quintic boundary.
