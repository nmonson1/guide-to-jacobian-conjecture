# Where bounded-degree source triviality first fails

Lane 3 · 2026-08-03

## Scope

Use the completed order-five and order-six calculations and the exact formal
family to locate a genuinely intrinsic complexity obstruction. Do not repeat
the recovered finite-order row reductions.

## Setup and definitions

The local Keller germ is studied in a weighted source slice. At order $r$,
the source-flow image $I_r$ and its maximal-ideal multiple
$\mathfrak m I_{r-1}$ measure new coordinate-trivial directions. A
**primitive class** is a class in $I_r/\mathfrak m I_{r-1}$.

For the formal family

\[
A=c(1+\alpha c),\qquad
B=-2-4\alpha c+q\alpha^2c^2,
\]

let framed degree-$D$ equivalence mean equivalence by the fixed framed
polynomial source operations of degree at most $D$. The exact residual is
proportional to $\delta\alpha^{D+2}$; over $\alpha=s\bmod s^M$, the minimal
framed degree is $M-2$.

## Results to use

- The recovered direct-coordinate order-five cache is exact as a replay of
  that cache. For degrees $2,3,4,5$, the reported new primitive counts are
  $11,13,11,0$; at degree five
  $\operatorname{rank}(\mathfrak m I)=2503$ and
  $\operatorname{rank}(I)=2538$. It is not an independent reconstruction
  from the displayed germ and slice, nor a marked-root comparison.
- At order six, weights $+2,+3,+4,+5$ have rank/nullity
  $553/62,545/41,523/23,473/7$; weights $+6$ and above in the archived
  range have full column rank over two good primes.
- The unique primitive weight-three sextic class is exact: ranks $542$ and
  $545$, initial rank $341/342$, leaving one four-term primitive class.
- The formal family gives compatible Artin equivalences and the sharp framed
  law $M-2$. Distinct $q$ remain inequivalent under complete stable
  polynomial equivalence. For unrestricted complexity,
  $\liminf \kappa/\log\log M\ge 1/\log 4$; a linear unrestricted degree law
  is not known.

## Example: the sextic primitive

The four-term sextic representative is an example of a new order-six class.
It is not evidence for a second class, for a characteristic-zero orbit
classification, or for the unrestricted linear degree law.

## Live problem

Turn the escaping conductor decoration in the formal family into an intrinsic
recovery theorem: characterize which bounded-complexity equivalences must
recover $\alpha$ to order $D+2$, and determine the strongest degree lower
bound that survives removal of the framing.

## Tasks

### L3-T1 — Intrinsic recovery from the Artin tower

Inputs: the [formal-effectivity theorem](lane-3-source-packet.md),
the [Lane 3 recovery integration](lane-3-source-packet.md),
and the stable-$q$ classification in
[RMU-9075E072](../working-mathematics/units/RMU-9075E072.md).

Deliverable: an invariant defined without the chosen frame, a theorem showing
how a complexity-$D$ equivalence transports it along every Artin quotient,
and either an improved unrestricted lower bound or an explicit mechanism that
prevents improvement beyond the current logarithmic law.

Dependencies: stable inequivalence of distinct $q$ and exact compatibility
of the Artin truncations.

Limits: the finite samples do not establish an asymptotic law; the sharp
$M-2$ statement is framed and cannot simply be renamed intrinsic.

### L3-T2 — Compare direct and marked-root complexes through order six

Inputs: the recovered order-five row spaces and order-six cache linked from
the integration packet, plus the root-coordinate source-flow TeX
[here](../proof-sources/03-local-rigidity/appendices/root-coordinate-source-flow.md).

Deliverable: a chain map with explicit bases through order six that sends the
known primitive sextic to its marked-root representative, or the exact first
unmatched differential.

Dependencies: native marked-root homotopy/basis data, which are not yet in the
recovery packet.

Limits: this comparison is blocked until those native data are supplied; it
must not recompute or relabel the known order-five/order-six ranks.

Alternative connections: a realization-complexity bridge to Lane 6 is welcome
if it preserves the framed/unrestricted distinction.

## Limits

The order-five result is cache-relative, the order-six result is a finite
weighted calculation, and the formal theorem uses external stable
classification. None is a complete classification of characteristic-zero
deformation orbits.

## Direct sources

- [Order-five recovery program](lane-3-source-packet.md)
- [Formal family TeX](../proof-sources/03-local-rigidity/main.md)

---
[Portfolio](state-of-the-program.md) · [Exact source packet](lane-3-source-packet.md) · [Release metadata](release.json) · [Retained mathematics](../working-mathematics/index.md) · [Current proof sources](../proof-sources/index.md)
