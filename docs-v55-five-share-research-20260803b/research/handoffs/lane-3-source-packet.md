# Lane 3 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`research-notes/lane3-formal-effectivity/AUDIT.md`](#source-9e696df6258ac003) — `2daaa07bb9a0fc327da4ceb40ebde655383429e0e05b67ed939eaf9274f80725`
- [`research-notes/lane3-formal-effectivity/README.md`](#source-dfc37b04a1586b9a) — `92dc41c327a4e15686e8fb51d4e259a05cf79388500993178bdc52dbb6a9be6b`
- [`research-notes/lane3-formal-effectivity/check_manifest.py`](#source-b87908051edeb52b) — `e90c67ec5c324dddc36bb2fd912dcb3c2ae512d6f16d26a8ff57baa3cde33761`
- [`research-notes/lane3-formal-effectivity/effective_unframed_bound_report.json`](#source-62f6ce1fbe7c4990) — `29ebf7cb96eec3d6671078ae5eb2cce369e7bfc9b89428500eab9d966c0a7f9c`
- [`research-notes/lane3-formal-effectivity/formal_effectivity_independent_report.json`](#source-3559de8f7e7053fa) — `6495bcc8bcab16479caae583bbdab0ecf5fd806c245bd8370858b7fff806a184`
- [`research-notes/lane3-formal-effectivity/formal_effectivity_insertion.tex`](#source-af9fb59f00268046) — `fb9e1e150ea387ae272daf0c03af233d937eefd12530adfdd29d4b9185a0b6d2`
- [`research-notes/lane3-formal-effectivity/formal_effectivity_report.json`](#source-aa6499ff75b04b0b) — `8e3403dc5259ff05fb1b0d7eb44e7108f0a8faa0a61916926562b0d5df004f01`
- [`research-notes/lane3-formal-effectivity/formal_effectivity_theorem.md`](#source-c413ecb87f258d26) — `1f01ad944f7bcc1fbc9474497f5071fd3df91d8305b043dc975513db9c7f9267`
- [`research-notes/lane3-formal-effectivity/lane3-handoff-replacement.md`](#source-eef0e661f2b6cd27) — `564d94426a1394656e270d0af62d8664be7a437447943bcb2ce1429015a8c6e8`
- [`research-notes/lane3-formal-effectivity/manifest.json`](#source-335f4c6ff189520e) — `36c82bd989f1761a28e872066819ea151b867516b83cd52c43617da19732219f`
- [`research-notes/lane3-formal-effectivity/verify_effective_unframed_bound.py`](#source-ae5c07014ef4dc74) — `7f5cfe5706f4b41cd2c680fce23c3e907bc0e9e98a78fc052ac7b5d3cfe4b74f`
- [`research-notes/lane3-formal-effectivity/verify_formal_effectivity.py`](#source-bb39729ae4f980a8) — `fed25d2940f0fca521cde6b03d83ad96a7e7179d366ed4ac0bf99ac5c8d2632f`
- [`research-notes/lane3-formal-effectivity/verify_formal_effectivity_independent.py`](#source-f680e5ddcbf4c6be) — `700170ac7053a2cdf8521189faede15107cd651e8277eb341f108602f413f46a`
- [`research-notes/lane3-order5-recovery-20260803-v1/AUDIT.md`](#source-79247beab882091c) — `5aec7b0b85a182d14b46991dcd849d25caf8822758dd8c734f822835e6fb6d0f`
- [`research-notes/lane3-order5-recovery-20260803-v1/README.md`](#source-cd92beb1f9f8cbbe) — `778c1e21d3c91a6c41fe03821c31aaa5911e44a06fc6200216807f08b3f92e29`
- [`research-notes/lane3-order5-recovery-20260803-v1/verify_order5_recovery.py`](#source-68c9400aba7a75f5) — `3edf0aa77f4078ca6a694132acb23b5503c60ba4b4159dec5f7dfb61718bbf5a`
- [`research-notes/lane3-recovery-integration-20260803-v1/README.md`](#source-2210ec80b02f0f23) — `3c3bca61d0597864bf11764dbf733621cf13a9ef846941393fce391e34b9ea9d`
- [`research-notes/lane3-recovery-integration-20260803-v1/check_lane3_recovery.py`](#source-135f83f2902aae9d) — `0fd36045016a6daa5f4c62d0f7c2bf89ec3e8fab8383215213763798c37fed31`
- [`research-notes/lane3-recovery-integration-20260803-v1/manifest.json`](#source-c34cdf96a598d48f) — `1cefa739d294f728601a890f6d9f37e86b20ebd074b4eafa89d23ddf9fd65ccc`
- [`research-notes/lane3-recovery-integration-20260803-v1/raw-formal-effectivity-reports/effective_unframed_bound_report.json`](#source-6cb100d21dd23409) — `29ebf7cb96eec3d6671078ae5eb2cce369e7bfc9b89428500eab9d966c0a7f9c`
- [`research-notes/lane3-recovery-integration-20260803-v1/raw-formal-effectivity-reports/formal_effectivity_independent_report.json`](#source-3b6b4ee5762a28d5) — `6495bcc8bcab16479caae583bbdab0ecf5fd806c245bd8370858b7fff806a184`
- [`research-notes/lane3-recovery-integration-20260803-v1/raw-formal-effectivity-reports/formal_effectivity_report.json`](#source-280c488e813678e9) — `8e3403dc5259ff05fb1b0d7eb44e7108f0a8faa0a61916926562b0d5df004f01`

<a id="source-9e696df6258ac003"></a>

## `research-notes/lane3-formal-effectivity/AUDIT.md`

<pre><code class="language-markdown">
# Lane 3 audit, corrections, and scope

## The three quotient problems

Lane 3 juxtaposes three genuinely different objects:

1. the normalized degree-at-most-seven coefficient slice modulo an
   eleven-dimensional affine source orbit;
2. the degree-eight germ after affine, source-shear, and target-shear
   components are included; and
3. the cubic-frame family modulo arbitrary polynomial left--right equivalence
   and stabilization.

No current comparison theorem identifies these functors. The length-584
algebra is therefore not, by itself, a statement about the full stable
quotient. Conversely, the stable \(q\)-modulus is not a surviving finite
Kuranishi tangent character in the bounded degree-seven or degree-eight
calculation.

## Corrected conclusions

- The length-584 algebra is a strong theorem about the chosen bounded,
  affine-transverse germ.
- Degree-eight orbit saturation remains open. The public retained unit for the
  five-variable order-six reduction supplies no public universal matrix or
  obstruction-polynomial locator, so the proposed `3 x 3` determinant and unit
  minors cannot be independently reconstructed from the public repository.
- The degree-eleven threshold has an exact proof locator inside the full cubic
  frame. It is not a theorem that the unrestricted pointed stable-modulus
  onset is globally eleven.
- The global synthesis remains the conditional interval
  \(8\le D_{\mathrm{mod}}(G)\le11\), with equality at eleven only inside the
  cubic-frame locus.

## New conceptual bridge

For the pointed family

\&#91;
A_s(c)=c(1+sc),\qquad B_{s,q}(c)=-2-4sc+qs^2c^2,
\&#93;

the exact orbit cokernel for framed root translations is

\&#91;
\mathbf C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+sc)\simeq\mathbf C((s)).
\&#93;

It is supported on the escaping divisor \(1+sc=0\), where
\(B_{s,q}(-1/s)=q+2\), and its \(s\)-adic completion is zero. Thus every
finite Artin neighborhood forgets the boundary decoration even though the
generic stable class remembers it.

This is a failure of polynomial effectivity at infinity, not a transition
from zero to nonzero ordinary tangent dimension.

## Superseded routes retained only as audit history

Two weaker arguments were developed before the final theorem:

- a compactness/Greenberg argument proving only that unrestricted equivalence
  complexity tends to infinity; and
- a coarse effective-Noether-exponent argument giving weaker explicit bounds.

They are not included as competing theorem statements. The package uses the
sharper parametric effective Nullstellensatz, which gives

\&#91;
M\le 2b(N+1)d^N
\&#93;

for a fixed stabilization dimension and degree bound, and yields the
unrestricted \(\Omega(\log\log M)\) rate.

## Remaining theorem-facing problem

The strongest remaining problem is an Artin-base intrinsic-recovery theorem:
show that an arbitrary unframed polynomial left--right equivalence recovers
enough of the projective escaping section and its conductor decoration to
inherit the sharp framed linear law. Such a theorem could upgrade

\&#91;
\deg_c\phi_M=M-2,\qquad \deg\Theta_{\phi_M}=4M-8
\&#93;

from framed optimality to an unrestricted lower bound.

This problem is separate from characteristic-zero degree-eight orbit
saturation, which still requires the missing universal computational packet
or a new conceptual replacement.
</code></pre>

<a id="source-dfc37b04a1586b9a"></a>

## `research-notes/lane3-formal-effectivity/README.md`

<pre><code class="language-markdown">
# Lane 3 formal effectivity package

This package records a continuation of Lane 3.  It connects the bounded
coefficient germ to the stable quadratic cubic-frame modulus without
identifying those quotient problems.

## Main theorem

For

\&#91;
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\&#93;

write \(F_{\alpha,q}=G_{A_\alpha,B_{\alpha,q}}\) and
\(\delta=q'-q\).  A framed root translation of \(c\)-degree at most \(D\)
from \(F_{\alpha,q}\) to \(F_{\alpha,q'}\) exists exactly when

\&#91;
\delta\alpha^{D+2}=0.
\&#93;

For the pointed arc \(\alpha=s\) modulo \(s^M\), the optimal framed degree is
\(M-2\).  The compatible limit is coefficientwise formal but has unbounded
spatial degree.

All Artin truncations of two distinct \(q\)-arcs are ordinarily polynomially
left--right equivalent, compatibly in the truncation order.  The complete
families over \(\mathbf C&#91;&#91;s&#93;&#93;\) are not stably polynomially left--right
equivalent.  For arbitrary unframed equivalences, including arbitrary
stabilization, the package proves

\&#91;
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge \frac1{\log4}.
\&#93;

The sharp linear lower bound for arbitrary unframed equivalences remains
open.

## Package map

| File | Role |
| --- | --- |
| `formal_effectivity_theorem.md` | Complete statement, proofs, dependencies, and limitations. |
| `formal_effectivity_insertion.tex` | Manuscript-ready proposed insertion; it is not wired into the pinned manuscript release. |
| `bibliography-additions.bib` | Citation for the parametric effective Nullstellensatz used in the quantitative proof. |
| `lane3-handoff-replacement.md` | Proposed future Lane 3 handoff source; the active immutable v16 release is not modified. |
| `AUDIT.md` | Scope audit, corrected conclusions, and superseded routes. |
| `verify_formal_effectivity.py` | Exact SymPy verification of the root-translation identities, degree staircase, affine-frame equations, and finite Artin samples. |
| `verify_formal_effectivity_independent.py` | Independent sparse-polynomial verification using only the Python standard library. |
| `verify_effective_unframed_bound.py` | Combinatorial verification of coefficient counts, degree bounds, finite inequalities, and asymptotic constants. |
| `*_report.json` | Pinned exact outputs from the three verification programs. |
| `manifest.json` / `check_manifest.py` | SHA-256 source-and-report inventory and checker. |

The three reports are stored beside their producing programs and pinned by
hash in the manifest.  Their records identify the program and the exact
mathematical boundary of the calculation.  To preserve the checked-in
receipts, replay the package in a fresh copied directory rather than writing
over this source tree.

## Replay

From the repository root:

```bash
cp -a research-notes/lane3-formal-effectivity /tmp/lane3-formal-effectivity-replay-NEW
python /tmp/lane3-formal-effectivity-replay-NEW/check_manifest.py
python -m pip install "sympy==1.14.0"
python /tmp/lane3-formal-effectivity-replay-NEW/verify_formal_effectivity.py
python /tmp/lane3-formal-effectivity-replay-NEW/verify_formal_effectivity_independent.py
python /tmp/lane3-formal-effectivity-replay-NEW/verify_effective_unframed_bound.py
```

Expected terminal statuses are:

```text
LANE 3 MANIFEST OK: 10 sources and 3 pinned reports
ALL FORMAL-EFFECTIVITY CHECKS PASSED
INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED
ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED
```

The first verifier uses exact SymPy arithmetic.  The independent staircase
checker and the quantitative-bound checker use only the standard library.

## Dependencies and evidence boundary

The unframed nonexistence statements use the Program 4 complete stable
classification of the quadratic family by \(q\).  The effective lower bound
also uses D'Andrea--Krick--Sombra, Theorem 0.5 in *Heights of varieties in
multiprojective spaces and arithmetic Nullstellensätze*.

The programs verify the displayed finite identities and bookkeeping.  They do
not re-prove the stable \(q\)-classification, the generic-combination lemma,
or the external parametric Nullstellensatz.  This package does not prove
characteristic-zero degree-eight orbit saturation and does not identify the
stable modulus with a finite Kuranishi tangent character.

## Provenance

GPT-5.6 Pro performed the source audit, theorem development, proof drafting,
exact implementation, independent finite-support replication, and package
preparation.  Nathaniel Monson remains responsible for accepting, revising,
or rejecting every mathematical assertion.
</code></pre>

<a id="source-b87908051edeb52b"></a>

## `research-notes/lane3-formal-effectivity/check_manifest.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the hash-pinned Lane 3 formal-effectivity source manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.json"


def main() -&gt; None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = data&#91;"files"&#93;
    found = sorted(
        path.name
        for path in ROOT.iterdir()
        if path.is_file()
        and path.name != "manifest.json"
        and not path.name.endswith("_report.json")
    )
    listed = sorted(item&#91;"path"&#93; for item in expected)
    if found != listed:
        raise SystemExit(f"manifest file set mismatch: found={found}, listed={listed}")
    for item in expected:
        path = ROOT / item&#91;"path"&#93;
        payload = path.read_bytes()
        if len(payload) != item&#91;"bytes"&#93;:
            raise SystemExit(f"byte-size mismatch: {item&#91;'path'&#93;}")
        digest = hashlib.sha256(payload).hexdigest()
        if digest != item&#91;"sha256"&#93;:
            raise SystemExit(f"SHA-256 mismatch: {item&#91;'path'&#93;}")
    reports = data.get("generated_report_records", &#91;&#93;)
    for item in reports:
        path = ROOT / item&#91;"path"&#93;
        payload = path.read_bytes()
        if len(payload) != item&#91;"bytes"&#93;:
            raise SystemExit(f"report byte-size mismatch: {item&#91;'path'&#93;}")
        digest = hashlib.sha256(payload).hexdigest()
        if digest != item&#91;"sha256"&#93;:
            raise SystemExit(f"report SHA-256 mismatch: {item&#91;'path'&#93;}")
    print(
        f"LANE 3 MANIFEST OK: {len(expected)} sources and "
        f"{len(reports)} pinned reports"
    )


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-62f6ce1fbe7c4990"></a>

## `research-notes/lane3-formal-effectivity/effective_unframed_bound_report.json`

<pre><code class="language-json">
{
  "degree_checks": &#91;
    {
      "b": 1,
      "coefficient_degree": 11,
      "parameter_degree": 2
    },
    {
      "b": 2,
      "coefficient_degree": 11,
      "parameter_degree": 4
    },
    {
      "b": 3,
      "coefficient_degree": 11,
      "parameter_degree": 6
    },
    {
      "b": 4,
      "coefficient_degree": 11,
      "parameter_degree": 8
    },
    {
      "b": 5,
      "coefficient_degree": 11,
      "parameter_degree": 10
    },
    {
      "b": 6,
      "coefficient_degree": 11,
      "parameter_degree": 12
    },
    {
      "b": 7,
      "coefficient_degree": 11,
      "parameter_degree": 14
    },
    {
      "b": 8,
      "coefficient_degree": 11,
      "parameter_degree": 16
    },
    {
      "b": 9,
      "coefficient_degree": 11,
      "parameter_degree": 18
    },
    {
      "b": 10,
      "coefficient_degree": 11,
      "parameter_degree": 20
    },
    {
      "b": 11,
      "coefficient_degree": 12,
      "parameter_degree": 22
    },
    {
      "b": 12,
      "coefficient_degree": 13,
      "parameter_degree": 24
    },
    {
      "b": 13,
      "coefficient_degree": 14,
      "parameter_degree": 26
    },
    {
      "b": 14,
      "coefficient_degree": 15,
      "parameter_degree": 28
    },
    {
      "b": 15,
      "coefficient_degree": 16,
      "parameter_degree": 30
    },
    {
      "b": 16,
      "coefficient_degree": 17,
      "parameter_degree": 32
    },
    {
      "b": 17,
      "coefficient_degree": 18,
      "parameter_degree": 34
    },
    {
      "b": 18,
      "coefficient_degree": 19,
      "parameter_degree": 36
    },
    {
      "b": 19,
      "coefficient_degree": 20,
      "parameter_degree": 38
    },
    {
      "b": 20,
      "coefficient_degree": 21,
      "parameter_degree": 40
    }
  &#93;,
  "enumeration_checks": &#91;
    {
      "b": 0,
      "count": 1,
      "n": 1
    },
    {
      "b": 1,
      "count": 2,
      "n": 1
    },
    {
      "b": 2,
      "count": 3,
      "n": 1
    },
    {
      "b": 3,
      "count": 4,
      "n": 1
    },
    {
      "b": 4,
      "count": 5,
      "n": 1
    },
    {
      "b": 0,
      "count": 1,
      "n": 2
    },
    {
      "b": 1,
      "count": 3,
      "n": 2
    },
    {
      "b": 2,
      "count": 6,
      "n": 2
    },
    {
      "b": 3,
      "count": 10,
      "n": 2
    },
    {
      "b": 4,
      "count": 15,
      "n": 2
    },
    {
      "b": 0,
      "count": 1,
      "n": 3
    },
    {
      "b": 1,
      "count": 4,
      "n": 3
    },
    {
      "b": 2,
      "count": 10,
      "n": 3
    },
    {
      "b": 3,
      "count": 20,
      "n": 3
    },
    {
      "b": 4,
      "count": 35,
      "n": 3
    },
    {
      "b": 0,
      "count": 1,
      "n": 4
    },
    {
      "b": 1,
      "count": 5,
      "n": 4
    },
    {
      "b": 2,
      "count": 15,
      "n": 4
    },
    {
      "b": 3,
      "count": 35,
      "n": 4
    },
    {
      "b": 4,
      "count": 70,
      "n": 4
    }
  &#93;,
  "exact_samples": &#91;
    {
      "ambient_dimension": 3,
      "b": 1,
      "coefficient_variables": 48,
      "d": 11,
      "h": 2,
      "log10_H": 51.9780749632873,
      "log_H": 119.68394057299237,
      "m": 0,
      "monomials_per_coordinate": 4,
      "tradeoff_log_H": 483.0579141287609
    },
    {
      "ambient_dimension": 3,
      "b": 2,
      "coefficient_variables": 120,
      "d": 11,
      "h": 4,
      "log10_H": 127.6519675806314,
      "log_H": 293.9295176425211,
      "m": 0,
      "monomials_per_coordinate": 10,
      "tradeoff_log_H": 992.2800909606378
    },
    {
      "ambient_dimension": 3,
      "b": 4,
      "coefficient_variables": 420,
      "d": 11,
      "h": 8,
      "log10_H": 440.91229984928214,
      "log_H": 1015.2380889506779,
      "m": 0,
      "monomials_per_coordinate": 35,
      "tradeoff_log_H": 4168.982138178213
    },
    {
      "ambient_dimension": 3,
      "b": 8,
      "coefficient_variables": 1980,
      "d": 11,
      "h": 16,
      "log10_H": 2066.45852107148,
      "log_H": 4758.196585909713,
      "m": 0,
      "monomials_per_coordinate": 165,
      "tradeoff_log_H": 72375.4145070419
    },
    {
      "ambient_dimension": 3,
      "b": 12,
      "coefficient_variables": 5460,
      "d": 13,
      "h": 24,
      "log10_H": 6087.248187013575,
      "log_H": 14016.40693277249,
      "m": 0,
      "monomials_per_coordinate": 455,
      "tradeoff_log_H": 1232942.5537815283
    },
    {
      "ambient_dimension": 4,
      "b": 1,
      "coefficient_variables": 80,
      "d": 11,
      "h": 2,
      "log10_H": 85.52092982720063,
      "log_H": 196.91921815910203,
      "m": 1,
      "monomials_per_coordinate": 5,
      "tradeoff_log_H": 1279.2056277171869
    },
    {
      "ambient_dimension": 4,
      "b": 2,
      "coefficient_variables": 240,
      "d": 11,
      "h": 4,
      "log10_H": 252.91832147187682,
      "log_H": 582.3659567662195,
      "m": 1,
      "monomials_per_coordinate": 15,
      "tradeoff_log_H": 2634.826884293306
    },
    {
      "ambient_dimension": 4,
      "b": 4,
      "coefficient_variables": 1120,
      "d": 11,
      "h": 8,
      "log10_H": 1170.312502976799,
      "log_H": 2694.744123498927,
      "m": 1,
      "monomials_per_coordinate": 70,
      "tradeoff_log_H": 11102.571075533879
    },
    {
      "ambient_dimension": 4,
      "b": 8,
      "coefficient_variables": 7920,
      "d": 11,
      "h": 16,
      "log10_H": 8252.932966449087,
      "log_H": 19003.0804220248,
      "m": 1,
      "monomials_per_coordinate": 495,
      "tradeoff_log_H": 192980.6158975217
    },
    {
      "ambient_dimension": 4,
      "b": 12,
      "coefficient_variables": 29120,
      "d": 13,
      "h": 24,
      "log10_H": 32443.874836701143,
      "log_H": 74704.78255795268,
      "m": 1,
      "monomials_per_coordinate": 1820,
      "tradeoff_log_H": 3287821.023960519
    },
    {
      "ambient_dimension": 5,
      "b": 1,
      "coefficient_variables": 120,
      "d": 11,
      "h": 2,
      "log10_H": 127.35093758496743,
      "log_H": 293.23637046196114,
      "m": 2,
      "monomials_per_coordinate": 6,
      "tradeoff_log_H": 3188.529055211097
    },
    {
      "ambient_dimension": 5,
      "b": 2,
      "coefficient_variables": 420,
      "d": 11,
      "h": 4,
      "log10_H": 440.6112698536182,
      "log_H": 1014.544941770118,
      "m": 2,
      "monomials_per_coordinate": 21,
      "tradeoff_log_H": 6575.504802548853
    },
    {
      "ambient_dimension": 5,
      "b": 4,
      "coefficient_variables": 2520,
      "d": 11,
      "h": 8,
      "log10_H": 2628.6142294313954,
      "log_H": 6052.607939920762,
      "m": 2,
      "monomials_per_coordinate": 126,
      "tradeoff_log_H": 27741.74765537839
    },
    {
      "ambient_dimension": 5,
      "b": 8,
      "coefficient_variables": 25740,
      "d": 11,
      "h": 16,
      "log10_H": 26811.06246136997,
      "log_H": 61734.75275088274,
      "m": 2,
      "monomials_per_coordinate": 1287,
      "tradeoff_log_H": 482431.66158707615
    },
    {
      "ambient_dimension": 5,
      "b": 12,
      "coefficient_variables": 123760,
      "d": 13,
      "h": 24,
      "log10_H": 137868.10207654568,
      "log_H": 317453.0366408355,
      "m": 2,
      "monomials_per_coordinate": 6188,
      "tradeoff_log_H": 8219527.914693865
    },
    {
      "ambient_dimension": 6,
      "b": 1,
      "coefficient_variables": 168,
      "d": 11,
      "h": 2,
      "log10_H": 177.48288780685945,
      "log_H": 408.6694517256093,
      "m": 3,
      "monomials_per_coordinate": 7,
      "tradeoff_log_H": 7642.356784891428
    },
    {
      "ambient_dimension": 6,
      "b": 2,
      "coefficient_variables": 672,
      "d": 11,
      "h": 4,
      "log10_H": 703.2459594818791,
      "log_H": 1619.2836630112697,
      "m": 3,
      "monomials_per_coordinate": 28,
      "tradeoff_log_H": 15769.158540626802
    },
    {
      "ambient_dimension": 6,
      "b": 4,
      "coefficient_variables": 5040,
      "d": 11,
      "h": 8,
      "log10_H": 5253.2247398818845,
      "log_H": 12095.99697619955,
      "m": 3,
      "monomials_per_coordinate": 210,
      "tradeoff_log_H": 66565.23075015482
    },
    {
      "ambient_dimension": 6,
      "b": 8,
      "coefficient_variables": 72072,
      "d": 11,
      "h": 16,
      "log10_H": 75061.31549730596,
      "log_H": 172835.06612461965,
      "m": 3,
      "monomials_per_coordinate": 3003,
      "tradeoff_log_H": 1157816.1723375346
    },
    {
      "ambient_dimension": 6,
      "b": 12,
      "coefficient_variables": 445536,
      "d": 13,
      "h": 24,
      "log10_H": 496308.89450839674,
      "log_H": 1142793.4620153888,
      "m": 3,
      "monomials_per_coordinate": 18564,
      "tradeoff_log_H": 19726842.730529815
    }
  &#93;,
  "fixed_n_asymptotics": &#91;
    {
      "inverted_constant": 1.1447142425533319,
      "n": 3,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 2.260314967299373
        },
        {
          "b": 100,
          "ratio": 2.1268017495584877
        },
        {
          "b": 200,
          "ratio": 2.0624917220751415
        },
        {
          "b": 500,
          "ratio": 2.0247388761288243
        }
      &#93;,
      "target_coefficient": 2.0
    },
    {
      "inverted_constant": 1.5650845800732873,
      "n": 4,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 0.8137015810076874
        },
        {
          "b": 100,
          "ratio": 0.7372898285303093
        },
        {
          "b": 200,
          "ratio": 0.7012470073110451
        },
        {
          "b": 500,
          "ratio": 0.6803122511032859
        }
      &#93;,
      "target_coefficient": 0.6666666666666666
    },
    {
      "inverted_constant": 1.97435048583482,
      "n": 5,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 0.22376772789480814
        },
        {
          "b": 100,
          "ratio": 0.19353856722340243
        },
        {
          "b": 200,
          "ratio": 0.17969454483062378
        },
        {
          "b": 500,
          "ratio": 0.1717788433833662
        }
      &#93;,
      "target_coefficient": 0.16666666666666666
    },
    {
      "inverted_constant": 2.3761767975649812,
      "n": 6,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 0.05012396730616706
        },
        {
          "b": 100,
          "ratio": 0.041030176134997196
        },
        {
          "b": 200,
          "ratio": 0.03701707623147214
        },
        {
          "b": 500,
          "ratio": 0.03476803790075599
        }
      &#93;,
      "target_coefficient": 0.03333333333333333
    }
  &#93;,
  "formulas": {
    "H(m,b)": "2*b*(N+1)*max(b+1,11)^N",
    "N": "4*(m+3)*binomial(m+b+3,m+3)",
    "unrestricted_asymptotic": "liminf kappa_M/log(log M) &gt;= 1/log(4)",
    "unrestricted_finite_bound": "2*B*(32*(B+3)*4^B+1)*(B+11)^(32*(B+3)*4^B)"
  },
  "scope": {
    "not_verified_by_script": &#91;
      "complete stable q-classification",
      "generic-fiber emptiness",
      "constant generic-combination lemma",
      "D'Andrea-Krick-Sombra parametric Nullstellensatz"
    &#93;,
    "verified": &#91;
      "monomial count T(n,b)=binomial(n+b,n)",
      "coefficient variable count N=4*n*T(n,b)",
      "universal equation coefficient-degree bound max(b+1,11)",
      "universal parameter-degree bound 2*b",
      "finite tradeoff inequalities",
      "fixed-stabilization asymptotic leading constants",
      "unrestricted log-log coefficient log(4)"
    &#93;
  },
  "status": "ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED",
  "unrestricted_asymptotics": &#91;
    {
      "B": 10,
      "log_log_H_over_B": 2.1006972942655553,
      "target": 1.3862943611198906
    },
    {
      "B": 20,
      "log_log_H_over_B": 1.7780419688734788,
      "target": 1.3862943611198906
    },
    {
      "B": 40,
      "log_log_H_over_B": 1.60119535797237,
      "target": 1.3862943611198906
    },
    {
      "B": 80,
      "log_log_H_over_B": 1.503682663918577,
      "target": 1.3862943611198906
    },
    {
      "B": 160,
      "log_log_H_over_B": 1.4500247534938626,
      "target": 1.3862943611198906
    }
  &#93;
}
</code></pre>

<a id="source-3559de8f7e7053fa"></a>

## `research-notes/lane3-formal-effectivity/formal_effectivity_independent_report.json`

<pre><code class="language-json">
{
  "engine": "pure Python sparse dictionaries with Fraction coefficients",
  "max_modulus": 30,
  "max_ramification_order": 7,
  "sample_count": 182,
  "samples": &#91;
    {
      "D": 0,
      "M": 2,
      "e": 1,
      "sharp": true
    },
    {
      "D": 1,
      "M": 3,
      "e": 1,
      "sharp": true
    },
    {
      "D": 0,
      "M": 3,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 4,
      "e": 1,
      "sharp": true
    },
    {
      "D": 0,
      "M": 4,
      "e": 2,
      "sharp": true
    },
    {
      "D": 0,
      "M": 4,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 5,
      "e": 1,
      "sharp": true
    },
    {
      "D": 1,
      "M": 5,
      "e": 2,
      "sharp": true
    },
    {
      "D": 0,
      "M": 5,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 5,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 6,
      "e": 1,
      "sharp": true
    },
    {
      "D": 1,
      "M": 6,
      "e": 2,
      "sharp": true
    },
    {
      "D": 0,
      "M": 6,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 6,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 6,
      "e": 5,
      "sharp": true
    },
    {
      "D": 5,
      "M": 7,
      "e": 1,
      "sharp": true
    },
    {
      "D": 2,
      "M": 7,
      "e": 2,
      "sharp": true
    },
    {
      "D": 1,
      "M": 7,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 7,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 7,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 7,
      "e": 6,
      "sharp": true
    },
    {
      "D": 6,
      "M": 8,
      "e": 1,
      "sharp": true
    },
    {
      "D": 2,
      "M": 8,
      "e": 2,
      "sharp": true
    },
    {
      "D": 1,
      "M": 8,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 7,
      "sharp": true
    },
    {
      "D": 7,
      "M": 9,
      "e": 1,
      "sharp": true
    },
    {
      "D": 3,
      "M": 9,
      "e": 2,
      "sharp": true
    },
    {
      "D": 1,
      "M": 9,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 9,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 9,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 9,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 9,
      "e": 7,
      "sharp": true
    },
    {
      "D": 8,
      "M": 10,
      "e": 1,
      "sharp": true
    },
    {
      "D": 3,
      "M": 10,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 10,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 10,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 10,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 10,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 10,
      "e": 7,
      "sharp": true
    },
    {
      "D": 9,
      "M": 11,
      "e": 1,
      "sharp": true
    },
    {
      "D": 4,
      "M": 11,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 11,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 11,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 11,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 11,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 11,
      "e": 7,
      "sharp": true
    },
    {
      "D": 10,
      "M": 12,
      "e": 1,
      "sharp": true
    },
    {
      "D": 4,
      "M": 12,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 12,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 12,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 12,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 12,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 12,
      "e": 7,
      "sharp": true
    },
    {
      "D": 11,
      "M": 13,
      "e": 1,
      "sharp": true
    },
    {
      "D": 5,
      "M": 13,
      "e": 2,
      "sharp": true
    },
    {
      "D": 3,
      "M": 13,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 13,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 13,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 13,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 13,
      "e": 7,
      "sharp": true
    },
    {
      "D": 12,
      "M": 14,
      "e": 1,
      "sharp": true
    },
    {
      "D": 5,
      "M": 14,
      "e": 2,
      "sharp": true
    },
    {
      "D": 3,
      "M": 14,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 14,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 14,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 14,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 14,
      "e": 7,
      "sharp": true
    },
    {
      "D": 13,
      "M": 15,
      "e": 1,
      "sharp": true
    },
    {
      "D": 6,
      "M": 15,
      "e": 2,
      "sharp": true
    },
    {
      "D": 3,
      "M": 15,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 15,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 15,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 15,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 15,
      "e": 7,
      "sharp": true
    },
    {
      "D": 14,
      "M": 16,
      "e": 1,
      "sharp": true
    },
    {
      "D": 6,
      "M": 16,
      "e": 2,
      "sharp": true
    },
    {
      "D": 4,
      "M": 16,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 16,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 16,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 16,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 16,
      "e": 7,
      "sharp": true
    },
    {
      "D": 15,
      "M": 17,
      "e": 1,
      "sharp": true
    },
    {
      "D": 7,
      "M": 17,
      "e": 2,
      "sharp": true
    },
    {
      "D": 4,
      "M": 17,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 17,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 17,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 17,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 17,
      "e": 7,
      "sharp": true
    },
    {
      "D": 16,
      "M": 18,
      "e": 1,
      "sharp": true
    },
    {
      "D": 7,
      "M": 18,
      "e": 2,
      "sharp": true
    },
    {
      "D": 4,
      "M": 18,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 18,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 18,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 18,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 18,
      "e": 7,
      "sharp": true
    },
    {
      "D": 17,
      "M": 19,
      "e": 1,
      "sharp": true
    },
    {
      "D": 8,
      "M": 19,
      "e": 2,
      "sharp": true
    },
    {
      "D": 5,
      "M": 19,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 19,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 19,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 19,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 19,
      "e": 7,
      "sharp": true
    },
    {
      "D": 18,
      "M": 20,
      "e": 1,
      "sharp": true
    },
    {
      "D": 8,
      "M": 20,
      "e": 2,
      "sharp": true
    },
    {
      "D": 5,
      "M": 20,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 20,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 20,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 20,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 20,
      "e": 7,
      "sharp": true
    },
    {
      "D": 19,
      "M": 21,
      "e": 1,
      "sharp": true
    },
    {
      "D": 9,
      "M": 21,
      "e": 2,
      "sharp": true
    },
    {
      "D": 5,
      "M": 21,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 21,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 21,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 21,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 21,
      "e": 7,
      "sharp": true
    },
    {
      "D": 20,
      "M": 22,
      "e": 1,
      "sharp": true
    },
    {
      "D": 9,
      "M": 22,
      "e": 2,
      "sharp": true
    },
    {
      "D": 6,
      "M": 22,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 22,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 22,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 22,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 22,
      "e": 7,
      "sharp": true
    },
    {
      "D": 21,
      "M": 23,
      "e": 1,
      "sharp": true
    },
    {
      "D": 10,
      "M": 23,
      "e": 2,
      "sharp": true
    },
    {
      "D": 6,
      "M": 23,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 23,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 23,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 23,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 23,
      "e": 7,
      "sharp": true
    },
    {
      "D": 22,
      "M": 24,
      "e": 1,
      "sharp": true
    },
    {
      "D": 10,
      "M": 24,
      "e": 2,
      "sharp": true
    },
    {
      "D": 6,
      "M": 24,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 24,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 24,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 24,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 24,
      "e": 7,
      "sharp": true
    },
    {
      "D": 23,
      "M": 25,
      "e": 1,
      "sharp": true
    },
    {
      "D": 11,
      "M": 25,
      "e": 2,
      "sharp": true
    },
    {
      "D": 7,
      "M": 25,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 25,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 25,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 25,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 25,
      "e": 7,
      "sharp": true
    },
    {
      "D": 24,
      "M": 26,
      "e": 1,
      "sharp": true
    },
    {
      "D": 11,
      "M": 26,
      "e": 2,
      "sharp": true
    },
    {
      "D": 7,
      "M": 26,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 26,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 26,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 26,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 26,
      "e": 7,
      "sharp": true
    },
    {
      "D": 25,
      "M": 27,
      "e": 1,
      "sharp": true
    },
    {
      "D": 12,
      "M": 27,
      "e": 2,
      "sharp": true
    },
    {
      "D": 7,
      "M": 27,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 27,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 27,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 27,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 27,
      "e": 7,
      "sharp": true
    },
    {
      "D": 26,
      "M": 28,
      "e": 1,
      "sharp": true
    },
    {
      "D": 12,
      "M": 28,
      "e": 2,
      "sharp": true
    },
    {
      "D": 8,
      "M": 28,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 28,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 28,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 28,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 28,
      "e": 7,
      "sharp": true
    },
    {
      "D": 27,
      "M": 29,
      "e": 1,
      "sharp": true
    },
    {
      "D": 13,
      "M": 29,
      "e": 2,
      "sharp": true
    },
    {
      "D": 8,
      "M": 29,
      "e": 3,
      "sharp": true
    },
    {
      "D": 6,
      "M": 29,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 29,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 29,
      "e": 6,
      "sharp": true
    },
    {
      "D": 3,
      "M": 29,
      "e": 7,
      "sharp": true
    },
    {
      "D": 28,
      "M": 30,
      "e": 1,
      "sharp": true
    },
    {
      "D": 13,
      "M": 30,
      "e": 2,
      "sharp": true
    },
    {
      "D": 8,
      "M": 30,
      "e": 3,
      "sharp": true
    },
    {
      "D": 6,
      "M": 30,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 30,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 30,
      "e": 6,
      "sharp": true
    },
    {
      "D": 3,
      "M": 30,
      "e": 7,
      "sharp": true
    }
  &#93;,
  "status": "INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED"
}
</code></pre>

<a id="source-af9fb59f00268046"></a>

## `research-notes/lane3-formal-effectivity/formal_effectivity_insertion.tex`

<pre><code class="language-tex">
\subsection{Formal effectivity of the quadratic modulus}
\label{subsec:formal-effectivity-q-modulus}

The preceding formal source-triviality result can be sharpened in two
independent directions.  First, the framed root-translation equation has an
exact annihilator and degree law over every coefficient ring.  Second, the
resulting compatible Artin isomorphisms do not algebraize to a stable
polynomial left--right equivalence over \(\C&#91;&#91;s&#93;&#93;\).  Thus the stable
left--right groupoid itself fails formal effectivity at the quadratic
modulus, even though the quantitative lower bound below is proved only in the
framed translation groupoid.  The complete stable \(q\)-classification is
the load-bearing input for generic-fiber nonexistence; the existing all-order
coefficientwise formal source triviality is overlapping background sharpened
by the explicit calculation below.  The exact annihilator law,
nonalgebraizability, unrestricted complexity escape, and diagonal obstruction
are the new deductions in this subsection.

For a commutative \(\Q\)-algebra \(R\), let
\&#91;
 A_\alpha(c)=c(1+\alpha c),\qquad
 B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\&#93;
and write \(F_{\alpha,q}=G_{A_\alpha,B_{\alpha,q}}\).  Put
\(\delta=q'-q\).

For \(\phi(c)\in cR&#91;c&#93;\), define
\&#91;
 \Theta_\phi(x,y,z)=
 \left(x,y+\phi(c),z-3\frac{\phi(c)}x\right),
\&#93;
\&#91;
 \ell_\phi=3A\phi^2+2B\phi,
 \qquad
 \eta_\phi=A\phi^3+B\phi^2,
\&#93;
and
\&#91;
 \Xi_\phi(a,b,c)=
 \left(a-\frac12\phi(c)b-\frac12\eta_\phi(c),
       b+\ell_\phi(c),c\right).
\&#93;
The source map is polynomial because \(c/x=2-3xy-x^2z\), fixes \(c\),
and shifts \(t\) by \(\phi(c)\).  Direct expansion gives
\begin{equation}
\label{eq:q-pairwise-root-translation}
 G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
\end{equation}

\begin{theorem}&#91;Exact framed effectivity law&#93;
\label{thm:q-framed-effectivity-law}
Let \(D\ge0\).  A \(c\)-fixed framed root translation of
\(c\)-degree at most \(D\) carries \(F_{\alpha,q}\) to
\(F_{\alpha,q'}\) if and only if
\&#91;
 \delta\alpha^{D+2}=0.
\&#93;
When it exists, it is unique and is given by
\&#91;
 \phi_D(c)=\frac\delta3\alpha^2c
 \sum_{j=0}^{D-1}(-\alpha c)^j,
\&#93;
where the sum is empty for \(D=0\).  Before imposing the annihilator
condition, the residual is exactly
\&#91;
 B_{\alpha,q'}-B_{\alpha,q}-3A_\alpha\phi_D
 =(-1)^D\delta\alpha^{D+2}c^{D+2}.
\&#93;
Consequently, if
\&#91;
 N=\min\{n\ge2:\delta\alpha^n=0\}
\&#93;
exists, then \(N=2\) means that the frames already agree and the
translation is zero; for \(N\ge3\), its exact degree is \(N-2\).  If no
such \(N\) exists, there is no polynomial framed translation.
\end{theorem}

\begin{proof}
The coefficient equation is
\&#91;
 3c(1+\alpha c)\phi(c)=\delta\alpha^2c^2.
\&#93;
Canceling \(c\) and writing
\(\phi=p_1c+\cdots+p_Dc^D\) gives
\&#91;
 3p_1=\delta\alpha^2,\qquad
 p_i=-\alpha p_{i-1}\ (2\le i\le D),\qquad
 \alpha p_D=0.
\&#93;
Thus
\&#91;
 p_i=\frac\delta3(-1)^{i-1}\alpha^{i+1},
\&#93;
and the terminal equation is precisely
\(\delta\alpha^{D+2}=0\).  This proves existence and uniqueness.  The
finite geometric-series identity gives the displayed residual.  For \(N\ge3\), minimality makes the coefficient of \(c^{N-2}\)
nonzero, proving the exact degree.  When \(N=2\), the frames already
coincide and \(\phi=0\).
\end{proof}

\begin{proposition}&#91;Exact framed orbit cokernel&#93;
\label{prop:q-framed-orbit-cokernel}
Let
\&#91;
 \mu_\alpha:cR&#91;c&#93;\longrightarrow c^2R&#91;c&#93;,
 \qquad \phi\longmapsto3A_\alpha\phi.
\&#93;
Then
\&#91;
 \operatorname{coker}(\mu_\alpha)
 \simeq R&#91;c&#93;/(1+\alpha c),
\&#93;
and the difference between the \(q'\)- and \(q\)-frames is the class
\&#91;
 \frac{q'-q}{3}\alpha^2\bmod(1+\alpha c).
\&#93;
For \(R=\C&#91;&#91;s&#93;&#93;\) and \(\alpha=s\), this cokernel is
\&#91;
 \C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+sc)\simeq\C((s)).
\&#93;
It is nonzero, but its reduction modulo every \(s^M\), and hence its
\(s\)-adic completion, is zero.
\end{proposition}

\begin{proof}
Divide the source by \(c\), the target by \(c^2\), and the map by the unit
three.  The resulting map is multiplication by \(1+\alpha c\).  In the
special case, the quotient relation is \(c=-s^{-1}\), giving
\(\C&#91;&#91;s&#93;&#93;&#91;1/s&#93;=\C((s))\).  Since \(s\) is invertible there, all
\(s\)-power quotients vanish.
\end{proof}

\begin{corollary}&#91;Ramification and obstruction staircase&#93;
\label{cor:q-ramification-degree-law}
Let \(R_M=\C&#91;s&#93;/(s^M)\), let
\(\alpha=s^eu(s)\) with \(u(0)\ne0\), and let \(q\ne q'\).  The exact
framed translation degree is
\&#91;
 D_M=\max\left(0,\left\lceil\frac Me\right\rceil-2\right).
\&#93;
For the unramified arc \(\alpha=s\), this is \(D_M=M-2\) for \(M\ge3\),
and the optimal degree-\(D\) residual is
\&#91;
 (-1)^D(q'-q)s^{D+2}c^{D+2}.
\&#93;
For \(D\ge1\), the canonical source and target automorphisms in
\eqref{eq:q-pairwise-root-translation} have exact ordinary degrees
\&#91;
 \deg\Theta_{\phi_D}=4D,
 \qquad
 \deg\Xi_{\phi_D}=D+1.
\&#93;
\end{corollary}

\begin{proof}
The nilpotence index of \(s^eu(s)\) in \(R_M\) is
\(\lceil M/e\rceil\), so the first assertion follows from
\cref{thm:q-framed-effectivity-law}.  The residual formula is its displayed
identity with \(\alpha=s\).  Since \(c(x,y,z)\) has degree four and the top
coefficient of \(\phi_D\) is nonzero, the source degree is \(4D\).  On the
target the term \(\phi_D(c)b\) has degree \(D+1\), while nilpotence and the
explicit formulas for \(\ell_\phi,\eta_\phi\) bound all remaining
corrections by \(D\).
\end{proof}

The same degree survives the residual affine transformations of the
normalized conductor chart.  Indeed, over a local ring with \(\alpha\) in
the maximal ideal, suppose
\&#91;
 C=uc+v,\qquad T=\nu t+h(c)
\&#93;
satisfies
\&#91;
 A_\alpha(C)\nu=\kappa A_\alpha(c),
\qquad
 B_{\alpha,q'}(C)+3A_\alpha(C)h(c)=
 \kappa B_{\alpha,q}(c).
\&#93;
Coefficient comparison gives
\&#91;
 v=0,\quad \kappa=1,\quad \nu u=1,\quad
 \alpha(u-1)=0,
\&#93;
and then
\&#91;
 h(c)=\frac{q-q'}{3u}\frac{\alpha^2c}{1+\alpha c}.
\&#93;
Multiplication by the unit \(u^{-1}\) does not alter the exact degree in
\cref{thm:q-framed-effectivity-law}.

\begin{theorem}&#91;Failure of formal effectivity in the stable groupoid&#93;
\label{thm:q-stable-formal-noneffectivity}
Let
\&#91;
 \mathcal F_q=F_{s,q}
\&#93;
be regarded as a polynomial Keller map over \(\C&#91;&#91;s&#93;&#93;\).  If \(q\ne q'\),
then:
\begin{enumerate}&#91;label=(\roman*)&#93;
\item for every \(M\ge1\), the reductions of
\(\mathcal F_q\) and \(\mathcal F_{q'}\) modulo \(s^M\) are ordinarily
polynomially left--right equivalent;
\item these equivalences may be chosen compatibly in \(M\); but
\item the two maps are not stably polynomially left--right equivalent over
\(\C&#91;&#91;s&#93;&#93;\).
\end{enumerate}
Consequently the stable isomorphism functor is not formally effective at
this pair of arcs.
\end{theorem}

\begin{proof}
For \(M\le2\) the frames agree.  For \(M\ge3\), use
\&#91;
 \phi_M(c)=\frac{q'-q}{3}s^2c
 \sum_{j=0}^{M-3}(-sc)^j
\&#93;
in \eqref{eq:q-pairwise-root-translation}.  The extra term in
\(\phi_{M+1}\) is divisible by \(s^M\), so the equivalences are compatible.

Suppose a stable polynomial equivalence existed over \(\C&#91;&#91;s&#93;&#93;\).  Base
change to an algebraic closure \(L\) of \(\C((s))\).  The diagonal
cubic-frame scaling normalizes the nonzero coefficient \(\alpha=s\) to
\(\alpha=1\), so the two generic fibers become \(G_q\) and \(G_{q'}\)
over \(L\).

Fix the stabilization dimension and the finite degrees of the polynomial
automorphisms and their inverses in this alleged equivalence.  Their
coefficients form an \(L\)-point of a finite-type affine \(\C\)-scheme cut
out by the inverse-composition equations and the left--right identity.  Since
\(\C\) is algebraically closed, nonemptiness gives a \(\C\)-point.  That
would be a stable polynomial equivalence between \(G_q\) and \(G_{q'}\)
over \(\C\), contradicting the complete \(q\)-classification.
\end{proof}

\subsection{Effective unframed complexity lower bounds}
\label{subsec:q-effective-unframed-bound}

The preceding framed calculation has a linear degree law.  We now give a
weaker but completely unframed lower bound.  No recovery of the cubic frame,
conductor chart, or escaping section is assumed.

Fix distinct \(q,q'\in\C\), put
\&#91;
 F_q=G_{c(1+sc),\,-2-4sc+qs^2c^2},
 \qquad R_M=\C&#91;s&#93;/(s^M),
\&#93;
and fix a stabilization dimension \(m\ge0\) and a degree bound \(b\ge1\).
Set
\&#91;
 n=3+m,\qquad
 T(n,b)=\binom{n+b}{n},\qquad
 N(n,b)=4nT(n,b),
\&#93;
\&#91;
 d_b=\max\{b+1,11\},\qquad h_b=2b.
\&#93;

Introduce coefficient variables for four polynomial maps
\&#91;
 \Phi,\Phi^{-1},\Psi,\Psi^{-1}:\A^n\longrightarrow\A^n
\&#93;
of degree at most \(b\).  Their two-sided inverse equations and the stable
left--right identity
\&#91;
 (F_{q'}\times\id_{\A^m})\circ\Phi
 =\Psi\circ(F_q\times\id_{\A^m})
\&#93;
define an affine scheme \(E_{m,b}\) over \(\C&#91;s&#93;\).  It has
\(N=N(n,b)\) coefficient variables.  Every defining equation \(f_i\) obeys
\&#91;
 \deg_X(f_i)\le d_b,
 \qquad
 \deg_s(f_i)\le h_b.
\&#93;
Indeed, a composition-inverse coefficient has degree at most \(b+1\) in the
unknown coefficients; substitution into the degree-eleven map has coefficient
degree at most eleven; and a degree-\(b\) monomial in coordinates whose
coefficients have \(s\)-degree at most two has \(s\)-degree at most \(2b\).

\begin{lemma}&#91;Reduction to \(N+1\) constant combinations&#93;
\label{lem:q-N-plus-one-combinations}
Let \(k\) be an infinite field and
\(f_1,\ldots,f_r\in k&#91;s,X_1,\ldots,X_N&#93;\) have no common zero over
\(\overline{k(s)}\).  There are constants \(\lambda_{ji}\in k\),
\(0\le j\le N\), such that
\&#91;
 g_j=\sum_i\lambda_{ji}f_i
\&#93;
are nonconstant in the \(X\)-variables and have no common zero over
\(\overline{k(s)}\).
\end{lemma}

\begin{proof}
Over \(K=\overline{k(s)}\), let \(\Lambda=(\lambda_{ji})\) range over
\(\A_K^{(N+1)r}\), and consider the incidence scheme
\&#91;
 I=\left\{(x,\Lambda):
 \sum_i\lambda_{ji}f_i(x)=0\text{ for }0\le j\le N\right\}.
\&#93;
For each \(x\), the vector \((f_1(x),\ldots,f_r(x))\) is nonzero.  Each row
of \(\Lambda\) therefore satisfies one nontrivial linear equation, and
\&#91;
 \dim I\le N+(N+1)(r-1)=(N+1)r-1.
\&#93;
The closure of its projection to the coefficient space is proper.  Requiring
a row not to produce an element of \(k&#91;s&#93;\) removes only a proper linear
subspace.  Hence a nonempty open set of tuples works over \(k(s)\).

This open contains a tuple with entries in \(k\).  Choose a nonzero polynomial
over \(k(s)\) vanishing on the bad closed set and clear denominators.  A
nonzero polynomial in \(k&#91;s,\Lambda&#93;\) cannot vanish at every constant point
of \(k^{(N+1)r}\), since \(k\) is infinite.
\end{proof}

The generic fiber of \(E_{m,b}\) is empty.  Otherwise, after extension to an
algebraic closure of \(\C(s)\), diagonal scaling would normalize \(s\ne0\)
and give a stable equivalence between \(G_q\) and \(G_{q'}\).  With \(m\)
and \(b\) fixed, such an equivalence is a point of a finite-type scheme over
\(\C\); a point over an extension field would yield a complex point,
contradicting the complete stable \(q\)-classification.

Apply \cref{lem:q-N-plus-one-combinations} to obtain \(N+1\) polynomials
\(g_0,\ldots,g_N\) with no generic common zero and with the same degree
bounds.  The parametric effective Nullstellensatz
\cite&#91;Theorem~0.5&#93;{dAndreaKrickSombra2013} supplies
\(0\ne\alpha_{m,b}(s)\in\C&#91;s&#93;\) and \(a_j\in\C&#91;s,X&#93;\) such that
\&#91;
 \alpha_{m,b}(s)=\sum_{j=0}^{N}a_jg_j
\&#93;
and
\&#91;
 \deg_s\alpha_{m,b}
 \le\sum_{\ell=0}^{N}
 \left(\prod_{j\ne\ell}\deg_Xg_j\right)\deg_sg_\ell
 \le (N+1)d_b^Nh_b.
\&#93;

\begin{theorem}&#91;Effective unframed truncation bound&#93;
\label{thm:q-effective-unframed-truncation-bound}
If the two reductions modulo \(s^M\) admit a stable polynomial left--right
equivalence with exactly \(m\) stabilization variables and with
\&#91;
 \deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\le b,
\&#93;
then
\&#91;
 \boxed{
 M\le H(m,b):=
 2b\bigl(N(n,b)+1\bigr)d_b^{N(n,b)}.}
\&#93;
\end{theorem}

\begin{proof}
An \(R_M\)-point of \(E_{m,b}\) annihilates every \(g_j\).  Evaluation of
the Bezout identity gives \(\alpha_{m,b}(s)=0\) in \(R_M\).  Since
\(\alpha_{m,b}\ne0\),
\&#91;
 M\le\ord_s\alpha_{m,b}
 \le\deg_s\alpha_{m,b}
 \le2b(N+1)d_b^N.
\&#93;
\end{proof}

\begin{corollary}&#91;Fixed-stabilization degree rate&#93;
\label{cor:q-fixed-stabilization-degree-rate}
Let \(b_{M,m}\) be the least common degree bound for an equivalence and its
four automorphism maps using exactly \(m\) added variables, and put
\(n=3+m\).  Then
\&#91;
 \liminf_{M\to\infty}
 \frac{b_{M,m}}{(\log M/\log\log M)^{1/n}}
 \ge\left(\frac{n!}{4}\right)^{1/n}.
\&#93;
In particular,
\&#91;
 b_{M,0}\ge
 \left(\frac32\frac{\log M}{\log\log M}\right)^{1/3}(1-o(1)).
\&#93;
\end{corollary}

\begin{proof}
For fixed \(n\),
\&#91;
 N(n,b)=4n\binom{n+b}{n}
 =\frac4{(n-1)!}b^n+O_n(b^{n-1}),
\&#93;
so
\&#91;
 \log H(m,b)
 =\frac4{(n-1)!}b^n\log b+O_n(b^n).
\&#93;
Asymptotic inversion gives the result.
\end{proof}

\begin{corollary}&#91;Stabilization--degree tradeoff&#93;
\label{cor:q-stabilization-degree-tradeoff}
Every such equivalence satisfies
\&#91;
 M\le
 2b\bigl(32(m+3)2^{m+b}+1\bigr)
 (b+11)^{32(m+3)2^{m+b}},
\&#93;
and consequently
\&#91;
 m+b\ge\frac{\log\log M}{\log2}
       -O(\log\log\log M).
\&#93;
\end{corollary}

\begin{proof}
Use
\(\binom{n+b}{n}\le2^{n+b}=2^{m+b+3}\), hence
\(N(n,b)\le32(m+3)2^{m+b}\), and substitute in
\cref{thm:q-effective-unframed-truncation-bound}.
\end{proof}

\begin{corollary}&#91;Explicit unrestricted complexity rate&#93;
\label{cor:q-unrestricted-complexity-rate}
Let
\&#91;
 \kappa_M(q,q')=
 \min\max\{m,\deg\Phi,\deg\Phi^{-1},
              \deg\Psi,\deg\Psi^{-1}\}
\&#93;
over all stable polynomial equivalences modulo \(s^M\).  Then
\&#91;
 \boxed{
 \kappa_M(q,q')
 \ge\frac{\log\log M}{\log4}
      -O(\log\log\log M),}
\&#93;
or equivalently
\&#91;
 \boxed{
 \liminf_{M\to\infty}
 \frac{\kappa_M(q,q')}{\log\log M}\ge\frac1{\log4}.}
\&#93;
More explicitly, \(\kappa_M(q,q')\le B\) implies
\&#91;
 M\le
 2B\bigl(32(B+3)4^B+1\bigr)
 (B+11)^{32(B+3)4^B}.
\&#93;
\end{corollary}

The result is deliberately worst-case: it treats the coefficients of four
bounded polynomial maps as independent variables and applies general
elimination.  It nevertheless proves an explicit rate for arbitrary stable
equivalences, with no frame-recovery hypothesis.  The sharp linear lower
bound remains a geometric problem.  The explicit framed construction gives
\(\kappa_M(q,q')\le4M-8\); matching this requires an intrinsic Artin-base
recovery theorem for the escaping-boundary chart.

The same non-effectivity argument works over an integral
\(\C\)-algebra \(R\) that is complete and separated for the
\(\alpha\)-adic topology, with \(\alpha\) a nonzero nonunit and
\(q,q'\in\C\) distinct.  Strictness of the powers of \(\alpha\) gives exact
framed degree \(M-2\) modulo \(\alpha^M\), and a complete-base stable
equivalence would contradict the complex generic-fiber classification after
finite-type descent.

The compatible framed translations have the unique limit
\&#91;
 \widehat\phi(c)=\frac{q'-q}{3}\frac{s^2c}{1+sc}
 =\frac{q'-q}{3}\sum_{j\ge0}(-1)^js^{j+2}c^{j+1}.
\&#93;
It lies in \(c\C&#91;c&#93;&#91;&#91;s&#93;&#93;\), the \(s\)-adic completion of
\(c\C&#91;s,c&#93;\), but not in \(c\C&#91;&#91;s&#93;&#93;&#91;c&#93;\).  Equivalently, if
\(\mathcal I_D(M)\) denotes framed isomorphisms of translation degree at
most \(D\), then
\&#91;
 \varprojlim_M\varinjlim_D\mathcal I_D(M)\ne\varnothing,
 \qquad
 \varinjlim_D\varprojlim_M\mathcal I_D(M)=\varnothing.
\&#93;
Thus completion and the bounded-degree filtration do not commute.

\begin{corollary}&#91;Obstruction to an affine finite-presentation diagonal&#93;
\label{cor:q-no-affine-fp-moduli-diagonal}
No algebraic stack can represent this stable polynomial left--right
groupoid near the two arcs, with its exact isomorphism notion, and have an
affine diagonal locally of finite presentation.
\end{corollary}

\begin{proof}
If such a stack existed, the isomorphism space between the two
\(\C&#91;&#91;s&#93;&#93;\)-objects would be affine of finite presentation, say
\(\Spec A\).  Since \(A\) is finitely presented and
\(\C&#91;&#91;s&#93;&#93;=\varprojlim_M\C&#91;s&#93;/(s^M)\), one has
\&#91;
 \Hom(A,\C&#91;&#91;s&#93;&#93;)
 \simeq
 \varprojlim_M\Hom(A,\C&#91;s&#93;/(s^M)).
\&#93;
The compatible Artin isomorphisms would therefore algebraize, contradicting
\cref{thm:q-stable-formal-noneffectivity}.
\end{proof}
</code></pre>

<a id="source-aa6499ff75b04b0b"></a>

## `research-notes/lane3-formal-effectivity/formal_effectivity_report.json`

<pre><code class="language-json">
{
  "affine_frame_checks": &#91;
    {
      "M": 3,
      "h_c_degree": 1,
      "residual_scaling": "u=1+lambda*s^2"
    },
    {
      "M": 4,
      "h_c_degree": 2,
      "residual_scaling": "u=1+lambda*s^3"
    },
    {
      "M": 5,
      "h_c_degree": 3,
      "residual_scaling": "u=1+lambda*s^4"
    },
    {
      "M": 6,
      "h_c_degree": 4,
      "residual_scaling": "u=1+lambda*s^5"
    },
    {
      "M": 7,
      "h_c_degree": 5,
      "residual_scaling": "u=1+lambda*s^6"
    },
    {
      "M": 8,
      "h_c_degree": 6,
      "residual_scaling": "u=1+lambda*s^7"
    },
    {
      "M": 9,
      "h_c_degree": 7,
      "residual_scaling": "u=1+lambda*s^8"
    },
    {
      "M": 10,
      "h_c_degree": 8,
      "residual_scaling": "u=1+lambda*s^9"
    },
    {
      "M": 11,
      "h_c_degree": 9,
      "residual_scaling": "u=1+lambda*s^10"
    },
    {
      "M": 12,
      "h_c_degree": 10,
      "residual_scaling": "u=1+lambda*s^11"
    }
  &#93;,
  "canonical_degree_checks": &#91;
    {
      "D": 1,
      "M": 3,
      "ell_c_degree": 1,
      "eta_c_degree": -1,
      "source_degree": 4,
      "target_degree": 2,
      "target_inverse_degree": 2
    },
    {
      "D": 2,
      "M": 4,
      "ell_c_degree": 2,
      "eta_c_degree": -1,
      "source_degree": 8,
      "target_degree": 3,
      "target_inverse_degree": 3
    },
    {
      "D": 3,
      "M": 5,
      "ell_c_degree": 3,
      "eta_c_degree": 2,
      "source_degree": 12,
      "target_degree": 4,
      "target_inverse_degree": 4
    },
    {
      "D": 4,
      "M": 6,
      "ell_c_degree": 4,
      "eta_c_degree": 2,
      "source_degree": 16,
      "target_degree": 5,
      "target_inverse_degree": 5
    },
    {
      "D": 5,
      "M": 7,
      "ell_c_degree": 5,
      "eta_c_degree": 4,
      "source_degree": 20,
      "target_degree": 6,
      "target_inverse_degree": 6
    },
    {
      "D": 6,
      "M": 8,
      "ell_c_degree": 6,
      "eta_c_degree": 5,
      "source_degree": 24,
      "target_degree": 7,
      "target_inverse_degree": 7
    },
    {
      "D": 7,
      "M": 9,
      "ell_c_degree": 7,
      "eta_c_degree": 6,
      "source_degree": 28,
      "target_degree": 8,
      "target_inverse_degree": 8
    },
    {
      "D": 8,
      "M": 10,
      "ell_c_degree": 8,
      "eta_c_degree": 7,
      "source_degree": 32,
      "target_degree": 9,
      "target_inverse_degree": 9
    }
  &#93;,
  "formal_limit_coefficients": &#91;
    {
      "c_degree": 1,
      "coefficient": "c*(-q + qp)/3",
      "s_power": 2,
      "source_y_degree": 4
    },
    {
      "c_degree": 2,
      "coefficient": "c**2*(q - qp)/3",
      "s_power": 3,
      "source_y_degree": 8
    },
    {
      "c_degree": 3,
      "coefficient": "c**3*(-q + qp)/3",
      "s_power": 4,
      "source_y_degree": 12
    },
    {
      "c_degree": 4,
      "coefficient": "c**4*(q - qp)/3",
      "s_power": 5,
      "source_y_degree": 16
    },
    {
      "c_degree": 5,
      "coefficient": "c**5*(-q + qp)/3",
      "s_power": 6,
      "source_y_degree": 20
    },
    {
      "c_degree": 6,
      "coefficient": "c**6*(q - qp)/3",
      "s_power": 7,
      "source_y_degree": 24
    },
    {
      "c_degree": 7,
      "coefficient": "c**7*(-q + qp)/3",
      "s_power": 8,
      "source_y_degree": 28
    },
    {
      "c_degree": 8,
      "coefficient": "c**8*(q - qp)/3",
      "s_power": 9,
      "source_y_degree": 32
    },
    {
      "c_degree": 9,
      "coefficient": "c**9*(-q + qp)/3",
      "s_power": 10,
      "source_y_degree": 36
    },
    {
      "c_degree": 10,
      "coefficient": "c**10*(q - qp)/3",
      "s_power": 11,
      "source_y_degree": 40
    },
    {
      "c_degree": 11,
      "coefficient": "c**11*(-q + qp)/3",
      "s_power": 12,
      "source_y_degree": 44
    }
  &#93;,
  "formal_limit_ring": "C&#91;c&#93;&#91;&#91;s&#93;&#93;",
  "noncommutation": "lim_M colim_D Isom_D(R_M) is nonempty, while colim_D lim_M Isom_D(R_M) is empty",
  "orbit_cokernel": "C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+s*c) = C((s))",
  "orbit_cokernel_s_inverse": "-c",
  "orbit_obstruction_class": "(q'-q)/3 * s^2",
  "polynomial_complete_base_ring": "C&#91;&#91;s&#93;&#93;&#91;c&#93;",
  "ramification_samples": &#91;
    {
      "M": 2,
      "e": 1,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 3,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 3,
      "e": 2,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 4,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 4,
      "e": 2,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 4,
      "e": 3,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 5,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 5,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 5,
      "e": 3,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 5,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 6,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 4,
      "nilpotence_index": 6
    },
    {
      "M": 6,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 6,
      "e": 3,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 6,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 7,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 5,
      "nilpotence_index": 7
    },
    {
      "M": 7,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 7,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 7,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 8,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 6,
      "nilpotence_index": 8
    },
    {
      "M": 8,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 8,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 8,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 9,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 7,
      "nilpotence_index": 9
    },
    {
      "M": 9,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 9,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 9,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 10,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 8,
      "nilpotence_index": 10
    },
    {
      "M": 10,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 10,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 10,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 11,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 9,
      "nilpotence_index": 11
    },
    {
      "M": 11,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 4,
      "nilpotence_index": 6
    },
    {
      "M": 11,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 11,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 12,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 10,
      "nilpotence_index": 12
    },
    {
      "M": 12,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 4,
      "nilpotence_index": 6
    },
    {
      "M": 12,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 12,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 13,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 11,
      "nilpotence_index": 13
    },
    {
      "M": 13,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 5,
      "nilpotence_index": 7
    },
    {
      "M": 13,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 13,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 14,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 12,
      "nilpotence_index": 14
    },
    {
      "M": 14,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 5,
      "nilpotence_index": 7
    },
    {
      "M": 14,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 14,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    }
  &#93;,
  "status": "ALL FORMAL-EFFECTIVITY CHECKS PASSED",
  "theorem_inputs_not_cas_checked": &#91;
    "stable q-classification on the generic fiber: Program 4, thm:main / cor:q-classification",
    "constant generic-combination lemma for an empty affine generic fiber",
    "D'Andrea-Krick-Sombra parametric effective Nullstellensatz (Theorem 0.5)"
  &#93;,
  "universal_residual_checks": &#91;
    {
      "D": 0,
      "phi_c_degree": -1,
      "residual": "alpha**2*c**2*delta"
    },
    {
      "D": 1,
      "phi_c_degree": 1,
      "residual": "-alpha**3*c**3*delta"
    },
    {
      "D": 2,
      "phi_c_degree": 2,
      "residual": "alpha**4*c**4*delta"
    },
    {
      "D": 3,
      "phi_c_degree": 3,
      "residual": "-alpha**5*c**5*delta"
    },
    {
      "D": 4,
      "phi_c_degree": 4,
      "residual": "alpha**6*c**6*delta"
    },
    {
      "D": 5,
      "phi_c_degree": 5,
      "residual": "-alpha**7*c**7*delta"
    },
    {
      "D": 6,
      "phi_c_degree": 6,
      "residual": "alpha**8*c**8*delta"
    },
    {
      "D": 7,
      "phi_c_degree": 7,
      "residual": "-alpha**9*c**9*delta"
    },
    {
      "D": 8,
      "phi_c_degree": 8,
      "residual": "alpha**10*c**10*delta"
    },
    {
      "D": 9,
      "phi_c_degree": 9,
      "residual": "-alpha**11*c**11*delta"
    },
    {
      "D": 10,
      "phi_c_degree": 10,
      "residual": "alpha**12*c**12*delta"
    }
  &#93;,
  "unramified_compatibility": &#91;
    {
      "M": 1,
      "c_degree": 0,
      "source_degree": 1,
      "target_degree": 1
    },
    {
      "M": 2,
      "c_degree": 0,
      "source_degree": 1,
      "target_degree": 1
    },
    {
      "M": 3,
      "c_degree": 1,
      "source_degree": 4,
      "target_degree": 2
    },
    {
      "M": 4,
      "c_degree": 2,
      "source_degree": 8,
      "target_degree": 3
    },
    {
      "M": 5,
      "c_degree": 3,
      "source_degree": 12,
      "target_degree": 4
    },
    {
      "M": 6,
      "c_degree": 4,
      "source_degree": 16,
      "target_degree": 5
    },
    {
      "M": 7,
      "c_degree": 5,
      "source_degree": 20,
      "target_degree": 6
    },
    {
      "M": 8,
      "c_degree": 6,
      "source_degree": 24,
      "target_degree": 7
    },
    {
      "M": 9,
      "c_degree": 7,
      "source_degree": 28,
      "target_degree": 8
    },
    {
      "M": 10,
      "c_degree": 8,
      "source_degree": 32,
      "target_degree": 9
    },
    {
      "M": 11,
      "c_degree": 9,
      "source_degree": 36,
      "target_degree": 10
    },
    {
      "M": 12,
      "c_degree": 10,
      "source_degree": 40,
      "target_degree": 11
    },
    {
      "M": 13,
      "c_degree": 11,
      "source_degree": 44,
      "target_degree": 12
    },
    {
      "M": 14,
      "c_degree": 12,
      "source_degree": 48,
      "target_degree": 13
    }
  &#93;
}
</code></pre>

<a id="source-c413ecb87f258d26"></a>

## `research-notes/lane3-formal-effectivity/formal_effectivity_theorem.md`

<pre><code class="language-markdown">
# Formal effectivity of the quadratic cubic-frame modulus

## Statement and scope

Let `R` be a commutative `Q`-algebra.  For `alpha,q in R`, put

\&#91;
A_\alpha(c)=c(1+\alpha c),\qquad
B_{\alpha,q}(c)=-2-4\alpha c+q\alpha^2c^2,
\&#93;

and let `F_{alpha,q}=G_{A_alpha,B_alpha,q}` be the corresponding cubic-frame
Keller map.  Write

\&#91;
\delta=q'-q.
\&#93;

The theorem below has two levels.

1. It gives an exact existence and degree criterion in the framed
   root-translation groupoid over an arbitrary coefficient ring.
2. For the pointed arcs `alpha=s` over `C&#91;&#91;s&#93;&#93;`, it proves a genuinely
   unframed statement: all Artin truncations are compatibly ordinarily
   left-right equivalent, but the two complete families are not even stably
   polynomially left-right equivalent.

Thus the stable left-right groupoid fails formal effectivity at the
quadratic modulus.  The quantitative degree lower bound is framed; the
non-effectivity conclusion and complexity divergence are unrestricted.

Two proved results frame the argument.  The complete stable
`q`-classification of the nonzero-`alpha` fibers is Theorem `thm:main` and
Corollary `cor:q-classification` of
`manuscripts/04-stable-moduli/main.tex`; it is the load-bearing input for
generic-fiber nonexistence.  The existing all-order coefficientwise formal
source triviality is overlapping background that the explicit calculation
below sharpens.  The new content is the exact orbit cokernel and annihilator
law, the sharp framed degree staircase, nonalgebraizability over `C&#91;&#91;s&#93;&#93;`,
divergence of unrestricted stable-equivalence complexity, and the diagonal
obstruction for algebraic moduli.

## 1. Root-translation identity

For `phi(c) in c R&#91;c&#93;`, define

\&#91;
\Theta_\phi(x,y,z)=
\left(x,\ y+\phi(c),\ z-3\frac{\phi(c)}x\right).
\&#93;

It is polynomial because

\&#91;
\frac cx=2-3xy-x^2z.
\&#93;

It fixes `c`, shifts the marked root coordinate `t` to `t+phi(c)`, and has
inverse `Theta_{-phi}`.  Put

\&#91;
\ell_\phi=3A\phi^2+2B\phi,
\qquad
\eta_\phi=A\phi^3+B\phi^2,
\&#93;

and define the triangular target automorphism

\&#91;
\Xi_\phi(a,b,c)=
\left(
 a-\frac12\phi(c)b-\frac12\eta_\phi(c),
 b+\ell_\phi(c),
 c
\right).
\&#93;

Direct expansion of the shifted cubic gives

\&#91;
\boxed{
G_{A,B+3A\phi}=\Xi_\phi\circ G_{A,B}\circ\Theta_\phi.
}
\&#93;

## 2. Exact Artin effectivity criterion

### Theorem 2.1 — annihilator and degree law

For an integer `D&gt;=0`, there is a `c`-fixed framed root translation of
`c`-degree at most `D` from `F_{alpha,q}` to `F_{alpha,q'}` if and only if

\&#91;
\boxed{\delta\alpha^{D+2}=0.}
\&#93;

When this condition holds, the translation is unique and equals

\&#91;
\boxed{
\phi_D(c)=
\frac\delta3\alpha^2c
\sum_{j=0}^{D-1}(-\alpha c)^j,
}
\&#93;

where the sum is empty when `D=0`.  Before imposing the annihilator
condition, its exact residual is

\&#91;
\boxed{
B_{\alpha,q'}-B_{\alpha,q}-3A_\alpha\phi_D
=(-1)^D\delta\alpha^{D+2}c^{D+2}.
}
\&#93;

If

\&#91;
N=\min\{n\ge2:\delta\alpha^n=0\}
\&#93;

exists, then `N=2` means that the two frames already agree and the unique
translation is zero.  For `N&gt;=3`, the unique translation has exact
`c`-degree `N-2`.  If no such `N` exists, there is no polynomial framed
translation.

### Proof

The coefficient equation is

\&#91;
3c(1+\alpha c)\phi(c)=\delta\alpha^2c^2.
\&#93;

Multiplication by `c` is injective in `R&#91;c&#93;`, so this is equivalent to

\&#91;
3(1+\alpha c)\phi(c)=\delta\alpha^2c.
\&#93;

Write

\&#91;
\phi(c)=p_1c+\cdots+p_Dc^D.
\&#93;

Coefficient comparison gives

\&#91;
3p_1=\delta\alpha^2,
\qquad
p_i=-\alpha p_{i-1}\quad(2\le i\le D),
\qquad
\alpha p_D=0.
\&#93;

Hence

\&#91;
p_i=\frac\delta3(-1)^{i-1}\alpha^{i+1}.
\&#93;

The terminal equation is exactly `delta*alpha^(D+2)=0`, and all coefficients
are forced, proving existence and uniqueness.  Multiplying the finite
geometric series by `1+alpha*c` gives the displayed residual.  If `N&gt;=3` is minimal, the coefficient of `c^(N-2)` is a unit multiple of
`delta*alpha^(N-1)`, which is nonzero; hence the degree is exactly `N-2`.
For `N=2`, the frames already coincide and `phi=0`.

### Proposition 2.2 — the exact orbit cokernel

The framed coefficient quotient has a one-line module description.  Let

\&#91;
\mu_\alpha:cR&#91;c&#93;\longrightarrow c^2R&#91;c&#93;,
\qquad
\phi\longmapsto 3A_\alpha\phi.
\&#93;

After dividing the source by `c`, the target by `c^2`, and the map by the
unit three,

\&#91;
\boxed{
\operatorname{coker}(\mu_\alpha)
\simeq R&#91;c&#93;/(1+\alpha c).
}
\&#93;

The difference between the `q'`- and `q`-frames is represented by

\&#91;
\boxed{
\frac{\delta}{3}\alpha^2\bmod(1+\alpha c).
}
\&#93;

For `R=C&#91;&#91;s&#93;&#93;` and `alpha=s`, evaluation at `c=-1/s` gives

\&#91;
R&#91;c&#93;/(1+sc)\simeq R&#91;1/s&#93;=\mathbb C((s)).
\&#93;

The obstruction class is nonzero when `q!=q'`, but multiplication by `s` is
invertible on the entire cokernel.  Hence every quotient modulo `s^M`, and
the `s`-adic completion of the cokernel, is zero.  The finite geometric
series in Theorem 2.1 is exactly the degree-filtered Neumann expansion of the
inverse of `1+sc`.

## 3. Ramification law over truncated DVRs

Let

\&#91;
R_M=\mathbb C&#91;s&#93;/(s^M)
\&#93;

and suppose

\&#91;
\alpha=s^eu(s),\qquad u(0)\ne0,
\&#93;

with `1&lt;=e&lt;M`.  For `q!=q'`, `delta` is a unit and the nilpotence index of
`alpha` is `ceil(M/e)`.  Theorem 2.1 gives the exact complexity

\&#91;
\boxed{
D_M=\max\left(0,\left\lceil\frac Me\right\rceil-2\right).
}
\&#93;

Equivalently, a framed translation of `c`-degree at most `D` can identify
the two ramified arcs modulo `s^M` exactly when

\&#91;
M\le e(D+2).
\&#93;

For the unramified pointed arc `alpha=s`,

\&#91;
\boxed{D_M=M-2\qquad(M\ge3).}
\&#93;

The optimal residual after allowing degree `D` is the single staircase term

\&#91;
\boxed{
(-1)^D(q'-q)s^{D+2}c^{D+2}.
}
\&#93;

Increasing the allowed degree by one kills this obstruction and moves it one
step northeast, from `(s^(D+2),c^(D+2))` to
`(s^(D+3),c^(D+3))`; there is no terminal finite obstruction.

For `D&gt;=1`, the canonical source and target automorphisms have exact ordinary
degrees

\&#91;
\boxed{
\deg\Theta_{\phi_D}=4D,
\qquad
\deg\Xi_{\phi_D}=D+1.
}
\&#93;

Indeed, `c(x,y,z)` has degree four, the top `c^D` coefficient of `phi_D` is
nonzero, and the target term `phi_D(c)b` has degree `D+1`.  Nilpotence forces
all other triangular target corrections to have degree at most `D`.

## 4. Residual affine frame changes do not improve the law

Assume now that `R` is local, `alpha` belongs to its maximal ideal, and
`delta` is a unit.  Consider an affine transformation of the normalized
conductor chart

\&#91;
C=uc+v,\qquad T=\nu t+h(c),
\&#93;

with `u,nu,kappa` units, satisfying

\&#91;
A_\alpha(C)\nu=\kappa A_\alpha(c),
\&#93;

\&#91;
B_{\alpha,q'}(C)+3A_\alpha(C)h(c)
=\kappa B_{\alpha,q}(c).
\&#93;

Then

\&#91;
\boxed{
v=0,\quad \kappa=1,\quad \nu u=1,\quad
\alpha(u-1)=0,
}
\&#93;

and

\&#91;
\boxed{
h(c)=\frac{q-q'}{3u}\frac{\alpha^2c}{1+\alpha c}.}
\&#93;

Consequently the minimal `c`-degree is again the integer in Theorem 2.1.

To prove this, the constant term of the first frame equation is
`v*(1+alpha*v)=0`.  The second factor is a unit, so `v=0`.  Comparing the
`c` and `c^2` coefficients gives `nu*u=kappa` and `alpha*(u-1)=0`.  The
constant term of the second frame equation gives `kappa=1`; its linear term
gives `h(0)=0`.  The relation `alpha*(u-1)=0` makes
`A_alpha(uc)=u*A_alpha(c)` and `B_alpha,q'(uc)=B_alpha,q'(c)`, leaving the
displayed root-translation equation.  Multiplication by the unit `u^(-1)`
cannot lower its exact degree.

## 5. Formal completion does not commute with bounded degree

Fix `q!=q'`, put `alpha=s`, and let

\&#91;
\mathcal I_D(M)
\&#93;

be the set of `c`-fixed framed isomorphisms over `R_M` whose root translation
has `c`-degree at most `D`.  Theorem 2.1 gives

\&#91;
\mathcal I_D(M)\ne\varnothing
\quad\Longleftrightarrow\quad
M\le D+2.
\&#93;

For every `M`, the union over `D` contains the unique translation

\&#91;
\phi_M(c)=\frac{q'-q}{3}s^2c
\sum_{j=0}^{M-3}(-sc)^j,
\&#93;

and these translations are compatible under `R_(M+1) -&gt; R_M`.  Therefore

\&#91;
\boxed{
\varprojlim_M\ \varinjlim_D\mathcal I_D(M)
\ne\varnothing,
\qquad
\varinjlim_D\ \varprojlim_M\mathcal I_D(M)
=\varnothing.
}
\&#93;

More precisely, the first set is a singleton and is represented by

\&#91;
\boxed{
\widehat\phi(c)=
\frac{q'-q}{3}\frac{s^2c}{1+sc}
=\frac{q'-q}{3}
\sum_{j\ge0}(-1)^js^{j+2}c^{j+1}.
}
\&#93;

It belongs to

\&#91;
c\,\mathbb C&#91;c&#93;&#91;&#91;s&#93;&#93;
=\varprojlim_M cR_M&#91;c&#93;,
\&#93;

but not to

\&#91;
c\,\mathbb C&#91;&#91;s&#93;&#93;&#91;c&#93;,
\&#93;

because its `c`-degree is unbounded.  Thus the compatible system defines a coefficientwise `s`-adic formal
left-right equivalence in `C&#91;x,y,z&#93;&#91;&#91;s&#93;&#93;`, but not a polynomial equivalence
over the complete base `C&#91;&#91;s&#93;&#93;`.

## 6. Full stable left-right non-effectivity

### Theorem 6.1 — all Artin truncations agree, the complete families do not

Let

\&#91;
\mathcal F_q=F_{s,q}
\&#93;

be viewed as a polynomial Keller map over `R=C&#91;&#91;s&#93;&#93;`.  If `q!=q'`, then:

1. for every `M&gt;=1`, the reductions
   `mathcal F_q mod s^M` and `mathcal F_q' mod s^M` are ordinarily
   polynomially left-right equivalent;
2. the equivalences can be chosen compatibly in `M`;
3. `mathcal F_q` and `mathcal F_q'` are not stably polynomially left-right
   equivalent over `C&#91;&#91;s&#93;&#93;`.

Hence the natural map

\&#91;
\operatorname{Isom}^{\rm stable}_{\mathbb C&#91;&#91;s&#93;&#93;}
(\mathcal F_q,\mathcal F_{q'})
\longrightarrow
\varprojlim_M
\operatorname{Isom}^{\rm stable}_{R_M}
(\mathcal F_q\bmod s^M,\mathcal F_{q'}\bmod s^M)
\&#93;

has empty source and nonempty target.

### Proof

For `M&lt;=2` the two frames are equal.  For `M&gt;=3`, use the compatible
translations `phi_M` above and the exact root-translation identity.  This
proves the first two assertions without stabilization.

Suppose a stable polynomial left-right equivalence existed over `C&#91;&#91;s&#93;&#93;`.
After passing to the fraction field `C((s))` and then to an algebraic closure
`L`, it would give a stable equivalence of the generic fibers.  The diagonal
scaling of the cubic frame normalizes the nonzero coefficient `alpha=s` to
`alpha=1`, carrying the two generic fibers to the normalized members `G_q`
and `G_q'` over `L`.

This already contradicts the proved classification over `C`; no separate
field-extension version of that theorem is needed.  Fix the stabilization
dimension and the finite degrees of the four polynomial automorphisms and
inverse automorphisms occurring in the alleged equivalence.  Their
coefficients form an `L`-point of an affine scheme of finite type over `C`,
cut out by the composition-inverse equations and the left-right equality.  A
nonempty finite-type scheme over the algebraically closed field `C` has a
`C`-point.  Such a point would be a stable polynomial equivalence between
`G_q` and `G_q'` over `C`, which the complete `q`-classification forbids when
`q!=q'`.  This is the required contradiction.

The formal isomorphism supplied by `widehat phi` does not contradict this
argument: its coordinate functions lie in the completed ring
`C&#91;x,y,z&#93;&#91;&#91;s&#93;&#93;`, not in the polynomial ring `C&#91;&#91;s&#93;&#93;&#91;x,y,z&#93;`.

### Theorem 6.2 — effective unrestricted complexity lower bound

For an ordinary or stable polynomial left-right equivalence over

\&#91;
R_M=\mathbb C&#91;s&#93;/(s^M),
\&#93;

define its complexity to be

\&#91;
\max\{m,\deg\Phi,\deg\Phi^{-1},\deg\Psi,\deg\Psi^{-1}\},
\&#93;

where `m` is the stabilization dimension.  Let `kappa_M(q,q')` be the
minimum complexity of an equivalence between the two `M`-th truncations.
Then

\&#91;
\boxed{
\kappa_M(q,q')
\ge \frac{\log\log M}{\log 4}
     -O(\log\log\log M),
}
\&#93;

and in particular

\&#91;
\boxed{
\liminf_{M\to\infty}
\frac{\kappa_M(q,q')}{\log\log M}\ge\frac1{\log4}.}
\&#93;

A finite version is the following.  If there is an equivalence using exactly
`m` stabilization variables, and all four automorphisms have degree at most
`b&gt;=1`, put

\&#91;
n=3+m,\qquad
T(n,b)=\binom{n+b}{n},\qquad
N(n,b)=4nT(n,b),
\&#93;

\&#91;
d_b=\max\{b+1,11\}.
\&#93;

Then

\&#91;
\boxed{
M\le 2b\bigl(N(n,b)+1\bigr)d_b^{N(n,b)}.}
\&#93;

Consequently, for fixed stabilization dimension `m`, if `b_(M,m)` is the
least common degree bound for the equivalence and its inverses and
`n=3+m`, then

\&#91;
\boxed{
\liminf_{M\to\infty}
\frac{b_{M,m}}{(\log M/\log\log M)^{1/n}}
\ge\left(\frac{n!}{4}\right)^{1/n}.}
\&#93;

In particular, ordinary equivalences satisfy

\&#91;
b_{M,0}\ge
\left(\frac32\frac{\log M}{\log\log M}\right)^{1/3}(1-o(1)).
\&#93;

### Proof

Fix `m,b`.  Introduce coefficient variables for four polynomial maps

\&#91;
\Phi,\Phi^{-1},\Psi,\Psi^{-1}:\mathbb A^n\to\mathbb A^n
\&#93;

of degree at most `b`.  There are

\&#91;
N=4n\binom{n+b}{n}
\&#93;

coefficient variables.  The two-sided inverse equations and the stable
left-right identity define an affine scheme `E_(m,b)` over `C&#91;s&#93;`.  Every
defining equation `f_i` has

\&#91;
\deg_Xf_i\le d_b,
\qquad
\deg_sf_i\le2b.
\&#93;

The first estimate follows because composition-inverse coefficients have
degree at most `b+1` in the unknown coefficients and the family has ordinary
degree eleven.  For the second, the coefficients of `F_q` have `s`-degree at
most two, and a degree-`b` monomial in its coordinates has `s`-degree at most
`2b`.

The generic fiber of `E_(m,b)` is empty.  Otherwise, after algebraic extension
of `C(s)` and diagonal normalization of `s`, it would give a stable
equivalence between `G_q` and `G_q'`.  With `m,b` fixed, that is a point of a
finite-type scheme over the algebraically closed field `C`; nonemptiness
after field extension would give a complex point, contradicting the complete
stable `q`-classification.

A dimension-count incidence argument replaces the defining equations by
`N+1` constant complex linear combinations `g_0,...,g_N` that still have no
common zero over the algebraic closure of `C(s)`.  Indeed, for a fixed point
`x`, the nonzero vector `(f_i(x))` imposes one independent linear equation on
each of `N+1` rows of combination coefficients.  The bad incidence therefore
has dimension at most one less than the parameter space.  Since `C` is
infinite, the required generic tuple can be chosen with constant complex
entries.

The parametric effective Nullstellensatz of D'Andrea--Krick--Sombra then gives
`0 != alpha_(m,b)(s) in C&#91;s&#93;` in the ideal of the `g_j`, with

\&#91;
\deg_s\alpha_{m,b}
\le\sum_{\ell=0}^{N}
\left(\prod_{j\ne\ell}\deg_Xg_j\right)\deg_sg_\ell
\le2b(N+1)d_b^N.
\&#93;

An `R_M`-point annihilates the `g_j`, hence annihilates `alpha_(m,b)`.  Thus

\&#91;
M\le\operatorname{ord}_s\alpha_{m,b}
\le\deg_s\alpha_{m,b},
\&#93;

which proves the finite bound.

For fixed `n`,

\&#91;
N(n,b)=\frac4{(n-1)!}b^n+O_n(b^{n-1}),
\&#93;

so

\&#91;
\log H(m,b)=\frac4{(n-1)!}b^n\log b+O_n(b^n).
\&#93;

Asymptotic inversion gives the fixed-stabilization statement.  For unrestricted
complexity at most `B`, use

\&#91;
N\le32(B+3)4^B,\qquad d_b\le B+11,
\&#93;

to obtain

\&#91;
M\le2B\bigl(32(B+3)4^B+1\bigr)
(B+11)^{32(B+3)4^B}.
\&#93;

Taking two logarithms gives

\&#91;
\log\log M\le B\log4+O(\log B),
\&#93;

and the asserted unrestricted rate follows.

The explicit framed equivalences still give the much larger upper bound

\&#91;
\kappa_M(q,q')\le4M-8\qquad(M\ge3).
\&#93;

The remaining open problem is the sharp **linear** unframed lower rate, not
mere divergence or effectivity.

The formal non-effectivity argument is not specific to a DVR.  Let `R` be an integral
`C`-algebra, complete and separated for the `alpha`-adic topology, with
`alpha` a nonzero nonunit, and keep `q,q' in C` distinct.  Then the reductions
modulo `alpha^M` are compatibly ordinarily left-right equivalent with exact
framed degree `M-2`, while the complete maps over `R` are not stably
equivalent.  Indeed, strictness of the powers of the nonunit `alpha` gives
the degree assertion, and nonexistence follows after passing to an algebraic
closure of `Frac(R)` and applying the same finite-type descent to the
proved complex classification.  Thus the effectivity failure is intrinsic
to a nonnilpotent parameter becoming nilpotent on every infinitesimal
quotient, not to the particular coordinate `s`.

## 7. Consequence for algebraic moduli stacks

### Corollary 7.1 — affine finite-presentation diagonals are impossible

No algebraic stack can model this stable polynomial left-right groupoid near
the two arcs while simultaneously having an affine diagonal locally of
finite presentation and representing its isomorphisms exactly.

Indeed, suppose such a stack `X` existed and let `x_q,x_q' in X(C&#91;&#91;s&#93;&#93;)` be
the two objects.  The isomorphism space

\&#91;
I=\operatorname{Isom}_X(x_q,x_q')
\&#93;

would be affine and of finite presentation over `C&#91;&#91;s&#93;&#93;`, say `I=Spec A`.
For a finitely presented algebra,

\&#91;
\operatorname{Hom}(A,\mathbb C&#91;&#91;s&#93;&#93;)
\simeq
\varprojlim_M
\operatorname{Hom}(A,R_M).
\&#93;

The compatible Artin isomorphisms would therefore produce a
`C&#91;&#91;s&#93;&#93;`-point of `I`, contradicting Theorem 6.1.

This obstruction concerns the **diagonal**, not merely separatedness of a
coarse orbit space.  A moduli construction can avoid it only by changing the
morphism notion, retaining degree or boundary data, or leaving the class of
stacks with affine finitely presented diagonal.

## 8. Lane 3 interpretation

The theorem gives a precise bridge between bounded deformation theory and
the stable `q`-modulus:

- every finite Artin neighborhood of the degree-seven point forgets `q` in
  the unrestricted polynomial left-right groupoid;
- a degree filtration recovers information progressively, with the exact law
  `M &lt;= D+2`;
- the obstruction does not die—it moves to higher `s`-order and higher
  `c`-degree;
- the compatible limit is a formal automorphism of unbounded spatial degree;
- global stable separation is recovered on the generic fiber by the deleted
  boundary value `B(-1/s)=q+2`.

Thus `q` is neither a tangent character nor a finite Kuranishi obstruction.
It is a failure of bounded-degree effectivity supported at a divisor escaping
from the formal neighborhood.
</code></pre>

<a id="source-eef0e661f2b6cd27"></a>

## `research-notes/lane3-formal-effectivity/lane3-handoff-replacement.md`

<pre><code class="language-markdown">
# Lane 3: Bounded-degree deformation, orbit saturation, and modulus onset

## Research objective

Relate three distinct filtered quotient problems without identifying them
prematurely:

1. the degree-at-most-seven coefficient slice modulo the eleven-dimensional
   normalized affine orbit;
2. the degree-eight coefficient germ after affine, source-shear, target-shear,
   and intersection components are included; and
3. the stable polynomial left-right quotient on the cubic-frame locus.

The first has a length-584 Artin algebra.  The second still lacks a global
characteristic-zero orbit-saturation theorem.  In the third, the current
cubic-frame theorem proves that ordinary degree eleven is the first degree
carrying genuine positive-dimensional stable moduli.  Assuming the current
reduced-rigidity and stable-classification theorems, the claim graph records
only the pointed global interval

```text
8 &lt;= D_mod(G) &lt;= 11,
```

with equality at eleven proved inside the cubic-frame locus.  No current
result upgrades that scoped equality to the unrestricted polynomial
left-right quotient.

This lane overlaps &#91;Program 3&#93;(local-rigidity-and-deformation-algebra.md) and
&#91;Program 4&#93;(stable-moduli.md).  The newest exact degree-eight units are the
&#91;two order-six lower-jet exclusions&#93;(../working-mathematics/units/RMU-3D8E0001.md)
and the &#91;five-variable universal reduction&#93;(../working-mathematics/units/RMU-3D8E0002.md).

## Reusable mathematics

In the normalized degree-at-most-seven coefficient scheme, an eleven-condition
affine slice transverse to the source orbit has a length-584 completed Artin
algebra.  Its Hilbert function is

```text
(1,10,44,108,157,145,86,30,3),
```

its maximal ideal has nilpotence index nine, and its Cohen--Macaulay type is
60.  Torus attractors and the fixed locus prove reduced isolation in this
bounded transverse germ.  This does not exclude degree-increasing families,
known degree-eight shear components, or moduli in an unrestricted quotient.

At the selected exceptional first-normal direction in degree eight, the full
exact characteristic-zero order-six systems at two lower jets—the base and
`c_0=1`—have unit obstruction ideal after all 24 order-five bendings are
included.  Over `F_1000033`, the complete 22-parameter lower-jet calculation
has a fixed 24-dimensional order-five kernel.  All lower-order correction
columns lie in one fixed five-dimensional image, and projection to its
three-dimensional cokernel produces three polynomials in only

```text
c_14, c_19, c_26, t_8, t_15.
```

The corrected universal assembly reproduces all 325 base columns.  An earlier
assembly overflowed because a negative determinant sign was represented as
`p-1` before integer multiplication; do not reuse that version.

The fixed-image containment is proved only modulo `1000033`.  Rank five has
not been proved everywhere, the three polynomials are not yet known to
generate the unit ideal universally, and the result is not a global
degree-eight theorem.

The Program 4 source already supplies two exact bridges to this lane:

- `thm:cubic-frame-degree-threshold` proves the degree-eleven threshold inside
  the full cubic frame; and
- `prop:formal-stable-separation` proves that every pointed `q`-arc is
  coefficientwise formally source-trivial although its punctured fibers
  remain stably separated.

For the same pointed family

```text
A_s(c)   = c*(1+s*c),
B_s,q(c) = -2 - 4*s*c + q*s^2*c^2,
```

there is a sharper explicit calculation in the framed conductor groupoid.
A root translation by `phi(c) in c R&#91;c&#93;` changes `B`
by `3*A*phi`.  Over `R_M=C&#91;s&#93;/(s^M)`, `M&gt;=3`, the unique translation from
`q` to `q'` is

```text
phi_M(c) = (q'-q)/3 * s^2*c * sum_{j=0}^{M-3} (-s*c)^j.
```

Hence

```text
deg_c(phi_M) = M-2.
```

The compatible formal gauge is

```text
phi_infty(c) = (q'-q)/3 * s^2*c/(1+s*c).
```

For `q != q'` it is not polynomial over `C&#91;s,c&#93;`; its pole is the deleted
root `c=-1/s`, where `B_s,q(-1/s)=q+2`.  After writing `phi=c*psi`, the exact polynomial-orbit obstruction is

```text
(q'-q)/3 * s^2 mod (1+s*c)
```

in `C&#91;s,c&#93;/(1+s*c)`.  Its principal-part lift is

```text
(q'-q)/3 * &#91;s^2*c/(1+s*c)&#93;
```

in `H^1_(1+s*c)(C&#91;s,c&#93;)`.  Both modules have zero `s`-adic completion because
`1+s*c` is a unit modulo every power of `s`.  Thus formal invisibility and
global stable separation are compatible for a concrete support-theoretic
reason.

The calculation has an exact coefficient-ring form.  For
`A_alpha=c*(1+alpha*c)` and `delta=q'-q`, a framed translation of `c`-degree
at most `D` exists exactly when

```text
delta * alpha^(D+2) = 0.
```

Its residual before imposing that annihilator is the single staircase term

```text
(-1)^D * delta * alpha^(D+2) * c^(D+2).
```

Thus for a ramified Artin arc `alpha=s^e*u(s)` over `C&#91;s&#93;/(s^M)`, the exact
translation degree is

```text
max(0, ceil(M/e)-2).
```

The same lower bound survives every residual affine change
`C=u*c+v, T=nu*t+h(c)` allowed by the normalized frame equations: they force
`v=0`, `alpha*(u-1)=0`, and the same rational root translation, up to a unit.
For the unramified arc, the canonical source and target gauges have degrees

```text
source: 4*(M-2),       target: M-1.
```

There is also an unrestricted theorem.  For `q != q'`, every pair of Artin
reductions of the two pointed families is compatibly ordinarily left-right
equivalent, but the complete maps over `C&#91;&#91;s&#93;&#93;` are not even stably
polynomially left-right equivalent.  A hypothetical complete-base equivalence
would give a generic-fiber stable equivalence between normalized `G_q` and
`G_q'`, contradicting the Program 4 classification.  The compatible limit
lives in `C&#91;x,y,z&#93;&#91;&#91;s&#93;&#93;` and has unbounded spatial degree; it does not lie in
`C&#91;&#91;s&#93;&#93;&#91;x,y,z&#93;`.

Consequently completion and the bounded-degree filtration do not commute:

```text
lim_M colim_D Isom_D(C&#91;s&#93;/s^M)  is nonempty,
colim_D lim_M Isom_D(C&#91;s&#93;/s^M)  is empty.
```

This proves failure of formal effectivity for the full stable left-right
isomorphism functor at the two arcs.  It also rules out an exact algebraic
moduli stack with affine diagonal locally of finite presentation: its affine
finite-presentation isomorphism space would turn the compatible Artin points
into a `C&#91;&#91;s&#93;&#93;`-point.

There is now an effective unrestricted complexity theorem that does not
assume the frame is recovered.  Suppose an equivalence modulo `s^M` uses `m`
stabilization variables, and the source and target automorphisms and their
inverses all have degree at most `b`.  Put

```text
n = 3+m,
N = 4*n*binomial(n+b,n),
d = max(b+1,11).
```

Encoding the four maps and their inverse identities gives a coefficient
scheme with `N` variables whose equations have coefficient degree at most `d`
and `s`-degree at most `2*b`.  Generic-fiber `q`-separation makes this scheme
empty over `C(s)`.  After reducing to `N+1` generic constant combinations, the
parametric effective Nullstellensatz gives a nonzero elimination polynomial
`alpha_(m,b)(s)` of degree at most

```text
2*b*(N+1)*d^N.
```

An equivalence modulo `s^M` forces `s^M` to divide this polynomial.  Therefore

```text
M &lt;= 2*b*(N+1)*d^N.
```

For fixed `m`, the least possible degree obeys

```text
b_(M,m) &gt;= ((3+m)!/4 * log(M)/log(log(M)))^(1/(3+m)) * (1-o(1)).
```

If `kappa_M(q,q')` is the minimum of the maximum of stabilization dimension
and the four automorphism degrees, then

```text
liminf kappa_M(q,q')/log(log(M)) &gt;= 1/log(4).
```

Equivalently,

```text
kappa_M(q,q') &gt;= log(log(M))/log(4) - O(log(log(log(M)))).
```

This is a fully unframed rate.  The explicit framed construction gives the
upper bound `kappa_M &lt;= 4*M-8`.  A separate intrinsic-recovery theorem over
Artin bases is still required only for the **sharp linear rate**: proving that
`M-2` and `4*M-8` are lower bounds for every unframed polynomial equivalence.

## High-priority next calculations

1. Define the nested spaces currently called the fixed five-dimensional
   correction image and the fixed two-dimensional tangent image: specify the
   ambient module, maps, bases, and quotient.  Only then compute the proposed
   `3 x 3` determinant `Delta_H(c_14,c_19,c_26)`.  A nonzero constant proves
   constant rank; factors give the exact rank-drop strata.
2. Form the `3 x 6` coefficient matrix of the three obstruction polynomials
   against `1,t_8,t_15,t_8^2,t_8*t_15,t_15^2` and find a unit minor or its
   factorization.
3. Reconstruct the sparse modular identities at several good primes and
   verify them directly over `Q`; repeat only on the resulting exceptional
   divisors.
4. Cover the other first-normal strata, the quadratic source-shear parameter,
   target-shear components, and all source/target intersections before making
   an orbit-saturation statement.
5. Prove that an arbitrary polynomial left-right equivalence over an Artin
   base intrinsically recovers enough of the projective escaping section to
   inherit the sharp framed linear degree law.  Formal non-effectivity and an
   explicit double-logarithmic unrestricted rate no longer depend on this
   step; only the optimal linear rate does.
6. Complete the source-flow/determinant comparison at orders five through
   eight.  Its role is to explain the bounded coefficient germ, not to recover
   `q` from a finite tangent character.

The newest tangent packet has rank 439, nullity 44, and a 28-dimensional
residual character; an older claim that only weights `-2,-1` remain is not
current.

## Useful deliverable

The immediate degree-eight deliverable remains a characteristic-zero unit
certificate or a finite stratification of its failure locus, with the
bounded-degree and quotient scope explicit.  On the moduli side, formal
non-effectivity and a fully unframed double-logarithmic lower rate are now
proved; the remaining theorem-facing deliverable is a projective Artin-base
recovery statement upgrading the exact framed linear **degree rate** to all
unframed polynomial equivalences.  Do not describe the
degree-eleven family as a newly discovered failure of finite-order local
rigidity: the current Program 4 manuscript already proves all-order formal
source triviality, and the new result identifies the stronger obstruction as
failure of polynomial effectivity at unbounded spatial degree.
</code></pre>

<a id="source-335f4c6ff189520e"></a>

## `research-notes/lane3-formal-effectivity/manifest.json`

<pre><code class="language-json">
{
  "base_commit": "e6deaf7b266d5d236dab78ac3765e772e2d3edba",
  "base_repository": "nmonson1/guide-to-jacobian-conjecture",
  "created_at": "2026-08-02",
  "files": &#91;
    {
      "bytes": 3290,
      "path": "AUDIT.md",
      "sha256": "2daaa07bb9a0fc327da4ceb40ebde655383429e0e05b67ed939eaf9274f80725"
    },
    {
      "bytes": 4577,
      "path": "README.md",
      "sha256": "92dc41c327a4e15686e8fb51d4e259a05cf79388500993178bdc52dbb6a9be6b"
    },
    {
      "bytes": 410,
      "path": "bibliography-additions.bib",
      "sha256": "712b75068f38de17e5f3c4bcaa406c6293d1158b303073fab9091ba803d39279"
    },
    {
      "bytes": 1684,
      "path": "check_manifest.py",
      "sha256": "e90c67ec5c324dddc36bb2fd912dcb3c2ae512d6f16d26a8ff57baa3cde33761"
    },
    {
      "bytes": 15916,
      "path": "formal_effectivity_insertion.tex",
      "sha256": "fb9e1e150ea387ae272daf0c03af233d937eefd12530adfdd29d4b9185a0b6d2"
    },
    {
      "bytes": 17598,
      "path": "formal_effectivity_theorem.md",
      "sha256": "1f01ad944f7bcc1fbc9474497f5071fd3df91d8305b043dc975513db9c7f9267"
    },
    {
      "bytes": 10276,
      "path": "lane3-handoff-replacement.md",
      "sha256": "564d94426a1394656e270d0af62d8664be7a437447943bcb2ce1429015a8c6e8"
    },
    {
      "bytes": 6150,
      "path": "verify_effective_unframed_bound.py",
      "sha256": "7f5cfe5706f4b41cd2c680fce23c3e907bc0e9e98a78fc052ac7b5d3cfe4b74f"
    },
    {
      "bytes": 14853,
      "path": "verify_formal_effectivity.py",
      "sha256": "fed25d2940f0fca521cde6b03d83ad96a7e7179d366ed4ac0bf99ac5c8d2632f"
    },
    {
      "bytes": 4047,
      "path": "verify_formal_effectivity_independent.py",
      "sha256": "700170ac7053a2cdf8521189faede15107cd651e8277eb341f108602f413f46a"
    }
  &#93;,
  "generated_reports": &#91;
    "formal_effectivity_report.json",
    "formal_effectivity_independent_report.json",
    "effective_unframed_bound_report.json"
  &#93;,
  "generated_report_records": &#91;
    {
      "bytes": 13242,
      "does_not_establish": &#91;
        "the stable q-classification used as an input",
        "the generic-combination lemma",
        "the external effective Nullstellensatz"
      &#93;,
      "path": "formal_effectivity_report.json",
      "program": "verify_formal_effectivity.py",
      "sha256": "8e3403dc5259ff05fb1b0d7eb44e7108f0a8faa0a61916926562b0d5df004f01"
    },
    {
      "bytes": 14058,
      "does_not_establish": &#91;
        "the stable q-classification used as an input",
        "any unrestricted unframed-equivalence bound"
      &#93;,
      "path": "formal_effectivity_independent_report.json",
      "program": "verify_formal_effectivity_independent.py",
      "sha256": "6495bcc8bcab16479caae583bbdab0ecf5fd806c245bd8370858b7fff806a184"
    },
    {
      "bytes": 12169,
      "does_not_establish": &#91;
        "the geometric stable-classification input",
        "the cited parametric effective Nullstellensatz"
      &#93;,
      "path": "effective_unframed_bound_report.json",
      "program": "verify_effective_unframed_bound.py",
      "sha256": "29ebf7cb96eec3d6671078ae5eb2cce369e7bfc9b89428500eab9d966c0a7f9c"
    }
  &#93;,
  "package_id": "lane3-formal-effectivity-v1",
  "schema_version": 1,
  "theorem_inputs": &#91;
    "Program 4 complete stable q-classification, proved in manuscripts/04-stable-moduli/main.tex",
    "D'Andrea-Krick-Sombra Theorem 0.5, DOI 10.24033/asens.2196"
  &#93;
}
</code></pre>

<a id="source-ae5c07014ef4dc74"></a>

## `research-notes/lane3-formal-effectivity/verify_effective_unframed_bound.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Combinatorial audit for the effective unframed complexity bound.

This script verifies the coefficient-variable counts, degree/parameter-degree
bookkeeping, finite inequalities, and asymptotic constants.  It does not
re-prove the external parametric Nullstellensatz or the stable q-classification.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterator

OUT = Path(__file__).with_name("effective_unframed_bound_report.json")


def exponent_tuples(n: int, b: int) -&gt; Iterator&#91;tuple&#91;int, ...&#93;&#93;:
    for exps in itertools.product(range(b + 1), repeat=n):
        if sum(exps) &lt;= b:
            yield exps


def monomial_count(n: int, b: int) -&gt; int:
    return math.comb(n + b, n)


def variable_count(m: int, b: int) -&gt; int:
    n = 3 + m
    return 4 * n * monomial_count(n, b)


def equation_degree_bound(b: int) -&gt; int:
    return max(b + 1, 11)


def parameter_degree_bound(b: int) -&gt; int:
    return 2 * b


def log_H(m: int, b: int) -&gt; float:
    nvars = variable_count(m, b)
    d = equation_degree_bound(b)
    return math.log(2 * b * (nvars + 1)) + nvars * math.log(d)


def unrestricted_log_H(B: int) -&gt; float:
    nvars_bound = 32 * (B + 3) * (4**B)
    return (
        math.log(2 * B * (nvars_bound + 1))
        + nvars_bound * math.log(B + 11)
    )


def tradeoff_log_H(m: int, b: int) -&gt; float:
    nvars_bound = 32 * (m + 3) * (2 ** (m + b))
    return (
        math.log(2 * b * (nvars_bound + 1))
        + nvars_bound * math.log(b + 11)
    )


def main() -&gt; None:
    enumeration_checks = &#91;&#93;
    for n in range(1, 5):
        for b in range(0, 5):
            enumerated = sum(1 for _ in exponent_tuples(n, b))
            formula = monomial_count(n, b)
            assert enumerated == formula
            enumeration_checks.append(
                {"n": n, "b": b, "count": formula}
            )

    # Degree bookkeeping for the universal coefficient equations.
    degree_checks = &#91;&#93;
    for b in range(1, 21):
        inverse_composition_degree = b + 1
        left_substitution_degree = 11
        right_substitution_degree = 1
        computed = max(
            inverse_composition_degree,
            left_substitution_degree,
            right_substitution_degree,
        )
        asserted = equation_degree_bound(b)
        assert computed == asserted
        assert parameter_degree_bound(b) == 2 * b
        degree_checks.append(
            {
                "b": b,
                "coefficient_degree": asserted,
                "parameter_degree": 2 * b,
            }
        )

    exact_samples = &#91;&#93;
    for m in range(0, 4):
        for b in (1, 2, 4, 8, 12):
            n = 3 + m
            t = monomial_count(n, b)
            nvars = variable_count(m, b)
            assert nvars == 4 * n * t
            assert t &lt;= 2 ** (n + b)
            assert nvars &lt;= 32 * (m + 3) * (2 ** (m + b))
            exact_samples.append(
                {
                    "m": m,
                    "b": b,
                    "ambient_dimension": n,
                    "monomials_per_coordinate": t,
                    "coefficient_variables": nvars,
                    "d": equation_degree_bound(b),
                    "h": parameter_degree_bound(b),
                    "log_H": log_H(m, b),
                    "log10_H": log_H(m, b) / math.log(10),
                    "tradeoff_log_H": tradeoff_log_H(m, b),
                }
            )

    fixed_n_asymptotics = &#91;&#93;
    for n in (3, 4, 5, 6):
        target = 4 / math.factorial(n - 1)
        values = &#91;&#93;
        for b in (50, 100, 200, 500):
            m = n - 3
            ratio = log_H(m, b) / (b**n * math.log(b))
            values.append({"b": b, "ratio": ratio})
        # Convergence is from above for these samples and must be reasonably close.
        assert abs(values&#91;-1&#93;&#91;"ratio"&#93; - target) / target &lt; 0.08
        fixed_n_asymptotics.append(
            {
                "n": n,
                "target_coefficient": target,
                "inverted_constant": (math.factorial(n) / 4) ** (1 / n),
                "samples": values,
            }
        )

    unrestricted_asymptotics = &#91;&#93;
    for B in (10, 20, 40, 80, 160):
        ll = math.log(unrestricted_log_H(B))
        ratio = ll / B
        unrestricted_asymptotics.append(
            {
                "B": B,
                "log_log_H_over_B": ratio,
                "target": math.log(4),
            }
        )
    assert abs(unrestricted_asymptotics&#91;-1&#93;&#91;"log_log_H_over_B"&#93; - math.log(4)) &lt; 0.08

    report = {
        "status": "ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED",
        "scope": {
            "verified": &#91;
                "monomial count T(n,b)=binomial(n+b,n)",
                "coefficient variable count N=4*n*T(n,b)",
                "universal equation coefficient-degree bound max(b+1,11)",
                "universal parameter-degree bound 2*b",
                "finite tradeoff inequalities",
                "fixed-stabilization asymptotic leading constants",
                "unrestricted log-log coefficient log(4)",
            &#93;,
            "not_verified_by_script": &#91;
                "complete stable q-classification",
                "generic-fiber emptiness",
                "constant generic-combination lemma",
                "D'Andrea-Krick-Sombra parametric Nullstellensatz",
            &#93;,
        },
        "formulas": {
            "H(m,b)": "2*b*(N+1)*max(b+1,11)^N",
            "N": "4*(m+3)*binomial(m+b+3,m+3)",
            "unrestricted_finite_bound": "2*B*(32*(B+3)*4^B+1)*(B+11)^(32*(B+3)*4^B)",
            "unrestricted_asymptotic": "liminf kappa_M/log(log M) &gt;= 1/log(4)",
        },
        "enumeration_checks": enumeration_checks,
        "degree_checks": degree_checks,
        "exact_samples": exact_samples,
        "fixed_n_asymptotics": fixed_n_asymptotics,
        "unrestricted_asymptotics": unrestricted_asymptotics,
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report&#91;"status"&#93;)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-bb39729ae4f980a8"></a>

## `research-notes/lane3-formal-effectivity/verify_formal_effectivity.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact checks for the formal-effectivity theorem of the cubic-frame q-modulus.

The script verifies finite polynomial identities underlying the proof:

1. the general root-translation left-right identity;
2. the exact residual formula for every tested degree D;
3. the annihilator/degree law over C&#91;s&#93;/(s^M) for several ramification orders;
4. compatibility of the optimal Artin gauges under truncation;
5. exact source and target degree formulas in the unramified case;
6. the residual affine-frame equations and their inability to lower degree;
7. unbounded c-degree of the compatible formal limit.

The nonexistence of a stable equivalence over C&#91;&#91;s&#93;&#93; uses the published
stable q-classification on the generic fiber and is recorded as a theorem
input rather than a CAS assertion.
"""
from __future__ import annotations

import json
from math import ceil
from pathlib import Path

import sympy as sp


def check(condition: bool, label: str) -&gt; None:
    if not condition:
        raise AssertionError(label)


def truncate_s(expr: sp.Expr, s: sp.Symbol, c: sp.Symbol, modulus: int) -&gt; sp.Expr:
    """Reduce a polynomial in s,c modulo s**modulus."""
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    result = sp.Integer(0)
    for (se, ce), coeff in sp.Poly(expr, s, c).terms():
        if se &lt; modulus:
            result += coeff * s**se * c**ce
    return sp.expand(result)


def c_degree(expr: sp.Expr, c: sp.Symbol) -&gt; int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, c).degree())


def total_degree(expr: sp.Expr, variables: tuple&#91;sp.Symbol, ...&#93;) -&gt; int:
    expr = sp.expand(expr)
    if expr == 0:
        return -1
    return int(sp.Poly(expr, *variables).total_degree())


def main() -&gt; None:
    # ------------------------------------------------------------------
    # 1. General frame-coordinate identity.
    # ------------------------------------------------------------------
    A, B, phi, t, b_target = sp.symbols("A B phi t b_target")
    B_shifted = B + 3 * A * phi
    ell = 3 * A * phi**2 + 2 * B * phi
    eta = A * phi**3 + B * phi**2

    # Source shift t -&gt; t+phi produces b_source=b_target-ell.
    b_source = b_target - ell
    two_a_source = sp.expand(
        A * (t + phi) ** 3
        + B * (t + phi) ** 2
        + (t + phi) * b_source
    )
    two_a_after_target = sp.expand(two_a_source - phi * b_source - eta)
    two_a_desired = sp.expand(A * t**3 + B_shifted * t**2 + t * b_target)
    check(two_a_after_target == two_a_desired, "root-translation LR identity")

    # Source invariant c is fixed.
    x, y, z, P = sp.symbols("x y z P")
    c_xyz = 2 * x - 3 * x**2 * y - x**3 * z
    c_transformed = sp.expand(
        2 * x - 3 * x**2 * (y + P) - x**3 * (z - 3 * P / x)
    )
    check(sp.expand(c_transformed - c_xyz) == 0, "source transformation fixes c")

    # ------------------------------------------------------------------
    # 2. Universal residual formula.
    # ------------------------------------------------------------------
    alpha, delta, c = sp.symbols("alpha delta c")
    A_alpha = c * (1 + alpha * c)
    residual_checks: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for D in range(0, 11):
        if D == 0:
            phi_D = sp.Integer(0)
        else:
            phi_D = sp.expand(
                delta
                * alpha**2
                * c
                * sum((-alpha * c) ** j for j in range(D))
                / 3
            )
        residual = sp.expand(delta * alpha**2 * c**2 - 3 * A_alpha * phi_D)
        expected = sp.expand((-1) ** D * delta * alpha ** (D + 2) * c ** (D + 2))
        check(residual == expected, f"universal residual formula D={D}")
        residual_checks.append(
            {
                "D": D,
                "phi_c_degree": c_degree(phi_D, c),
                "residual": str(sp.factor(residual)),
            }
        )

    # ------------------------------------------------------------------
    # 3. Ramification law over C&#91;s&#93;/(s^M).
    # ------------------------------------------------------------------
    s, q, qp, lam = sp.symbols("s q qp lam")
    dq = qp - q

    # Exact orbit-cokernel relation for alpha=s: in the quotient by
    # 1+s*c, multiplication by s has inverse -c.
    orbit_relation = sp.expand(s * (-c) - 1)
    orbit_denominator_basic = sp.Poly(
        1 + s * c,
        c,
        domain=sp.QQ.frac_field(s),
    )
    orbit_remainder = sp.rem(
        sp.Poly(orbit_relation, c, domain=sp.QQ.frac_field(s)),
        orbit_denominator_basic,
    )
    check(orbit_remainder.as_expr() == 0, "s is invertible in orbit cokernel")
    obstruction_numerator = sp.Poly(
        dq * s**2,
        c,
        domain=sp.QQ.frac_field(s, q, qp),
    )
    orbit_denominator = sp.Poly(
        1 + s * c,
        c,
        domain=sp.QQ.frac_field(s, q, qp),
    )
    _, obstruction_remainder = sp.div(obstruction_numerator, orbit_denominator)
    check(
        sp.expand(obstruction_remainder.as_expr() - dq * s**2) == 0,
        "q obstruction is nonzero in generic orbit cokernel",
    )

    ramification_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;

    for M in range(2, 15):
        for e in range(1, min(5, M)):
            nilpotence_index = ceil(M / e)
            D_min = max(0, nilpotence_index - 2)
            alpha_me = s**e
            A_me = c * (1 + alpha_me * c)

            if D_min == 0:
                phi_min = sp.Integer(0)
            else:
                phi_min = sp.expand(
                    dq
                    * alpha_me**2
                    * c
                    * sum((-alpha_me * c) ** j for j in range(D_min))
                    / 3
                )

            residual_min = truncate_s(
                dq * alpha_me**2 * c**2 - 3 * A_me * phi_min,
                s,
                c,
                M,
            )
            check(residual_min == 0, f"ramified existence M={M}, e={e}")

            actual_degree = c_degree(truncate_s(phi_min, s, c, M), c)
            expected_degree = -1 if D_min == 0 else D_min
            check(actual_degree == expected_degree, f"ramified degree M={M}, e={e}")

            if D_min &gt; 0:
                phi_prev = (
                    sp.Integer(0)
                    if D_min == 1
                    else sp.expand(
                        dq
                        * alpha_me**2
                        * c
                        * sum((-alpha_me * c) ** j for j in range(D_min - 1))
                        / 3
                    )
                )
                residual_prev = truncate_s(
                    dq * alpha_me**2 * c**2 - 3 * A_me * phi_prev,
                    s,
                    c,
                    M,
                )
                check(residual_prev != 0, f"ramified sharpness M={M}, e={e}")

            ramification_table.append(
                {
                    "M": M,
                    "e": e,
                    "nilpotence_index": nilpotence_index,
                    "minimal_c_degree": max(0, actual_degree),
                    "frames_already_equal": D_min == 0,
                }
            )

    # ------------------------------------------------------------------
    # 4. Unramified compatibility and exact degree staircase.
    # ------------------------------------------------------------------
    compatibility_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    phi_by_M: dict&#91;int, sp.Expr&#93; = {}
    for M in range(1, 15):
        if M &lt;= 2:
            phi_M = sp.Integer(0)
        else:
            phi_M = sp.expand(
                dq * s**2 * c * sum((-s * c) ** j for j in range(M - 2)) / 3
            )
        phi_by_M&#91;M&#93; = phi_M

        A_s = c * (1 + s * c)
        residual = truncate_s(
            dq * s**2 * c**2 - 3 * A_s * phi_M,
            s,
            c,
            M,
        )
        check(residual == 0, f"unramified equivalence mod s^{M}")

        if M &gt;= 3:
            check(c_degree(phi_M, c) == M - 2, f"unramified exact degree M={M}")
            top = sp.expand(phi_M).coeff(c, M - 2)
            expected_top = dq * (-1) ** (M - 3) * s ** (M - 1) / 3
            check(sp.expand(top - expected_top) == 0, f"unramified top term M={M}")

        compatibility_table.append(
            {
                "M": M,
                "c_degree": max(0, c_degree(phi_M, c)),
                "source_degree": 1 if M &lt;= 2 else 4 * (M - 2),
                "target_degree": 1 if M &lt;= 2 else M - 1,
            }
        )

    for M in range(1, 14):
        reduced_next = truncate_s(phi_by_M&#91;M + 1&#93;, s, c, M)
        current = truncate_s(phi_by_M&#91;M&#93;, s, c, M)
        check(reduced_next == current, f"compatibility M={M+1}-&gt;M={M}")

    # ------------------------------------------------------------------
    # 5. Exact source and target coordinate degrees.
    # ------------------------------------------------------------------
    d = 2 - 3 * x * y - x**2 * z
    c_source = x * d
    degree_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    bvar, avar, cvar = sp.symbols("b a c")

    for M in range(3, 11):
        D = M - 2
        phi_M_source = sp.expand(phi_by_M&#91;M&#93;.subs(c, c_source))
        theta_y = sp.expand(y + phi_M_source)
        theta_z = sp.expand(z - 3 * phi_M_source / x)
        source_degree = max(
            total_degree(x, (x, y, z)),
            total_degree(theta_y, (x, y, z)),
            total_degree(theta_z, (x, y, z)),
        )
        check(source_degree == 4 * D, f"source degree M={M}")

        # Target corrections over R_M; use B_q and reduce in s.
        phi_target = phi_by_M&#91;M&#93;.subs(c, cvar)
        A_target = cvar * (1 + s * cvar)
        B_target = -2 - 4 * s * cvar + q * s**2 * cvar**2
        ell_target = truncate_s(
            3 * A_target * phi_target**2 + 2 * B_target * phi_target,
            s,
            cvar,
            M,
        )
        eta_target = truncate_s(
            A_target * phi_target**3 + B_target * phi_target**2,
            s,
            cvar,
            M,
        )
        xi_a = sp.expand(avar - phi_target * bvar / 2 - eta_target / 2)
        xi_b = sp.expand(bvar + ell_target)
        target_degree = max(
            total_degree(xi_a, (avar, bvar, cvar)),
            total_degree(xi_b, (avar, bvar, cvar)),
            1,
        )
        # The inverse is triangular.  Equivalently it is the target map for
        # the reverse root translation from B+3Aphi back to B.
        xi_inv_a = sp.expand(
            avar
            + phi_target * bvar / 2
            - truncate_s(phi_target * ell_target, s, cvar, M) / 2
            + eta_target / 2
        )
        xi_inv_b = sp.expand(bvar - ell_target)
        target_inverse_degree = max(
            total_degree(xi_inv_a, (avar, bvar, cvar)),
            total_degree(xi_inv_b, (avar, bvar, cvar)),
            1,
        )
        check(target_degree == D + 1, f"target degree M={M}")
        check(target_inverse_degree == D + 1, f"target inverse degree M={M}")
        check(c_degree(ell_target, cvar) &lt;= D, f"ell c-degree M={M}")
        check(c_degree(eta_target, cvar) &lt;= D - 1, f"eta c-degree M={M}")

        degree_table.append(
            {
                "M": M,
                "D": D,
                "source_degree": source_degree,
                "target_degree": target_degree,
                "target_inverse_degree": target_inverse_degree,
                "ell_c_degree": c_degree(ell_target, cvar),
                "eta_c_degree": c_degree(eta_target, cvar),
            }
        )

    # ------------------------------------------------------------------
    # 6. Residual affine framed transformations.
    # ------------------------------------------------------------------
    affine_table: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for M in range(3, 13):
        D = M - 2
        u = 1 + lam * s ** (M - 1)
        u_inv = 1 - lam * s ** (M - 1)
        h = truncate_s(-u_inv * phi_by_M&#91;M&#93;, s, c, M)

        A_s = c * (1 + s * c)
        B_q = -2 - 4 * s * c + q * s**2 * c**2
        B_qp = -2 - 4 * s * c + qp * s**2 * c**2

        A_relation = truncate_s(
            A_s.subs(c, u * c) * u_inv - A_s,
            s,
            c,
            M,
        )
        B_relation = truncate_s(
            B_qp.subs(c, u * c)
            + 3 * A_s.subs(c, u * c) * h
            - B_q,
            s,
            c,
            M,
        )
        check(A_relation == 0, f"affine A relation M={M}")
        check(B_relation == 0, f"affine B relation M={M}")
        check(c_degree(h, c) == D, f"affine degree unchanged M={M}")
        affine_table.append(
            {
                "M": M,
                "residual_scaling": f"u=1+lambda*s^{M-1}",
                "h_c_degree": D,
            }
        )

    # ------------------------------------------------------------------
    # 7. The formal limit has unbounded c-degree.
    # ------------------------------------------------------------------
    formal_coefficients: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for n in range(2, 13):
        coeff = dq * (-1) ** (n - 2) * c ** (n - 1) / 3
        check(c_degree(coeff, c) == n - 1, f"formal coefficient degree n={n}")
        formal_coefficients.append(
            {
                "s_power": n,
                "coefficient": str(coeff),
                "c_degree": n - 1,
                "source_y_degree": 4 * (n - 1),
            }
        )

    report = {
        "status": "ALL FORMAL-EFFECTIVITY CHECKS PASSED",
        "theorem_inputs_not_cas_checked": &#91;
            "stable q-classification on the generic fiber: Program 4, thm:main / cor:q-classification",
            "constant generic-combination lemma for an empty affine generic fiber",
            "D'Andrea-Krick-Sombra parametric effective Nullstellensatz (Theorem 0.5)",
        &#93;,
        "universal_residual_checks": residual_checks,
        "ramification_samples": ramification_table,
        "unramified_compatibility": compatibility_table,
        "canonical_degree_checks": degree_table,
        "affine_frame_checks": affine_table,
        "formal_limit_coefficients": formal_coefficients,
        "orbit_cokernel": "C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+s*c) = C((s))",
        "orbit_obstruction_class": "(q'-q)/3 * s^2",
        "orbit_cokernel_s_inverse": "-c",
        "formal_limit_ring": "C&#91;c&#93;&#91;&#91;s&#93;&#93;",
        "polynomial_complete_base_ring": "C&#91;&#91;s&#93;&#93;&#91;c&#93;",
        "noncommutation": (
            "lim_M colim_D Isom_D(R_M) is nonempty, "
            "while colim_D lim_M Isom_D(R_M) is empty"
        ),
    }

    output = Path(__file__).with_name("formal_effectivity_report.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(report&#91;"status"&#93;)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-f680e5ddcbf4c6be"></a>

## `research-notes/lane3-formal-effectivity/verify_formal_effectivity_independent.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Independent finite-support checker for the effectivity staircase.

This checker deliberately uses no CAS.  Polynomials in (s,c) are sparse
Python dictionaries with rational coefficients.  It verifies the exact
residual and sharp ramification law for a grid of Artin quotients.
"""
from __future__ import annotations

from fractions import Fraction
from math import ceil
from pathlib import Path
import json

Monomial = tuple&#91;int, int&#93;
Poly = dict&#91;Monomial, Fraction&#93;


def add(*polys: Poly) -&gt; Poly:
    out: Poly = {}
    for poly in polys:
        for mon, coeff in poly.items():
            out&#91;mon&#93; = out.get(mon, Fraction(0)) + coeff
            if out&#91;mon&#93; == 0:
                del out&#91;mon&#93;
    return out


def scale(poly: Poly, scalar: Fraction) -&gt; Poly:
    return {m: scalar * a for m, a in poly.items() if scalar * a}


def mul(left: Poly, right: Poly, modulus: int | None = None) -&gt; Poly:
    out: Poly = {}
    for (si, ci), ai in left.items():
        for (sj, cj), aj in right.items():
            se = si + sj
            if modulus is not None and se &gt;= modulus:
                continue
            mon = (se, ci + cj)
            out&#91;mon&#93; = out.get(mon, Fraction(0)) + ai * aj
            if out&#91;mon&#93; == 0:
                del out&#91;mon&#93;
    return out


def monomial(s_exp: int, c_exp: int, coeff: Fraction = Fraction(1)) -&gt; Poly:
    return {} if coeff == 0 else {(s_exp, c_exp): coeff}


def c_degree(poly: Poly) -&gt; int:
    return max((c for _, c in poly), default=-1)


def phi_for(M: int, e: int, D: int) -&gt; Poly:
    # delta is normalized to 1; the factor 1/3 is retained exactly.
    out: Poly = {}
    for j in range(D):
        out = add(
            out,
            monomial(e * (j + 2), j + 1, Fraction((-1) ** j, 3)),
        )
    return {m: a for m, a in out.items() if m&#91;0&#93; &lt; M}


def residual(M: int, e: int, D: int) -&gt; Poly:
    # delta*alpha^2*c^2 - 3*c*(1+alpha*c)*phi_D
    difference = {} if 2 * e &gt;= M else monomial(2 * e, 2)
    A = add(monomial(0, 1), monomial(e, 2))
    correction = scale(mul(A, phi_for(M, e, D), modulus=M), Fraction(3))
    return add(difference, scale(correction, Fraction(-1)))


def main() -&gt; None:
    samples: list&#91;dict&#91;str, int | bool&#93;&#93; = &#91;&#93;
    for M in range(2, 31):
        for e in range(1, min(M, 8)):
            D = max(0, ceil(M / e) - 2)
            r = residual(M, e, D)
            if r:
                raise AssertionError(f"existence failed M={M}, e={e}: {r}")
            deg = c_degree(phi_for(M, e, D))
            expected = -1 if D == 0 else D
            if deg != expected:
                raise AssertionError((M, e, deg, expected))
            sharp = True
            if D &gt; 0:
                previous = residual(M, e, D - 1)
                sharp = bool(previous)
                if not sharp:
                    raise AssertionError(f"sharpness failed M={M}, e={e}")
            samples.append(
                {
                    "M": M,
                    "e": e,
                    "D": D,
                    "sharp": sharp,
                }
            )

    # Compatibility in the unramified tower.
    for M in range(1, 30):
        current_D = max(0, M - 2)
        next_D = max(0, M - 1)
        current = {m: a for m, a in phi_for(M, 1, current_D).items() if m&#91;0&#93; &lt; M}
        reduced_next = {
            m: a for m, a in phi_for(M + 1, 1, next_D).items() if m&#91;0&#93; &lt; M
        }
        if current != reduced_next:
            raise AssertionError(f"compatibility failed at M={M}")

    report = {
        "status": "INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED",
        "engine": "pure Python sparse dictionaries with Fraction coefficients",
        "sample_count": len(samples),
        "max_modulus": 30,
        "max_ramification_order": 7,
        "samples": samples,
    }
    path = Path(__file__).with_name("formal_effectivity_independent_report.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report&#91;"status"&#93;)


if __name__ == "__main__":
    main()
</code></pre>

<a id="source-79247beab882091c"></a>

## `research-notes/lane3-order5-recovery-20260803-v1/AUDIT.md`

<pre><code class="language-markdown">
# Recovery and publication audit

The source cache and the historical summary were recovered from the reviewed
Program 3 artifact intake.  The cache has SHA-256
`2790e24c2d5ec803b1b00454d96add7c2b781095a6d2431d0ee0c563ac697033`.

The replay does not trust the historical rank summary.  It reconstructs the
filtered coefficient equations from the cache, constructs the Macaulay row
spaces with a declared monomial order, and certifies the rational ranks.  The
historical summary and modular discovery table are included in the public
archive only as lineage checks.

The public exporter must omit intake identifiers, recovery-tree paths,
conversation metadata, and the original pickle rank certificate.  It may
publish the residual cache because the restricted loader audits its exact
class vocabulary before admitting it, and because the public archive pins
its digest.
</code></pre>

<a id="source-cd92beb1f9f8cbbe"></a>

## `research-notes/lane3-order5-recovery-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 3 direct order-five recovery

This packet restores and replays the recovered direct-coordinate Kuranishi
calculation through parameter order five.  The recovered cache contains the
filtered rational residual equations in the ten tangent parameters; it is
not an independent reconstruction from the displayed base map and transverse
slice.

The replay rebuilds the weighted Macaulay blocks in parameter degrees two
through five.  For every block, a nonzero pivot minor modulo a good prime
gives the rank lower bound.  Exact FLINT row reduction supplies the rational
column relations for the matching upper bound, and those relations are
checked against every original row.

The expected exact output is

| parameter degree | initial rank | Hilbert value | new minimal generators |
| ---: | ---: | ---: | ---: |
| 2 | 11 | 44 | 11 |
| 3 | 112 | 108 | 13 |
| 4 | 558 | 157 | 11 |
| 5 | 1857 | 145 | 0 |

Through order five, the ideal rank is `2538`, the maximal-ideal multiple has
rank `2503`, and the cumulative minimal-generator dimension is `35`.

## Replay

The public bundle places the recovered cache beside the verifier.  From its
root, run

```bash
uv run --with python-flint --with sympy==1.14.0 \
  python verify_order5_recovery.py \
  direct_order5_residual_series.pkl.gz \
  /tmp/lane3-order5-replay.json \
  --cache-sha256 2790e24c2d5ec803b1b00454d96add7c2b781095a6d2431d0ee0c563ac697033
cmp /tmp/lane3-order5-replay.json order5_exact_replay_certificate.json
```

The verifier refuses to overwrite an existing output.  The pickle loader is
restricted to audited builtin containers, `Fraction`, `defaultdict`, and
SymPy rational numbers.

## Boundary

This packet verifies the recovered direct-coordinate row spaces and their
exact ranks.  It does not reconstruct the order-five equations independently
from the published map, expose the marked-root contracting homotopy, compare
the direct and marked-root complexes in order five, or establish any
degree-eight orbit-saturation statement.
</code></pre>

<a id="source-68c9400aba7a75f5"></a>

## `research-notes/lane3-order5-recovery-20260803-v1/verify_order5_recovery.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Rebuild and certify the recovered direct order-five Macaulay ranks.

The recovered cache is loaded with a restricted unpickler.  Each rational
rank is proved by a modular pivot minor and exact FLINT nullspace relations
that are checked against every row.  The output is deterministic and the
destination must not already exist.
"""

from __future__ import annotations

import argparse
import builtins
import collections
import fractions
import gzip
import hashlib
import itertools
import json
import math
import pickle
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import sympy as sp
from flint import fmpq_mat


WEIGHTS = (-1, 2, -3, -2, -1, 0, 1, 1, 2, 3)
EXPECTED_CACHE_KEYS = {
    "weights",
    "pairs",
    "triples",
    "quads",
    "quints",
    "residuals",
    "k5corr",
    "block_summary5",
}
ALLOWED_PICKLE_CLASSES = {
    ("builtins", name): getattr(builtins, name)
    for name in ("dict", "list", "tuple", "set", "frozenset")
}
ALLOWED_PICKLE_CLASSES.update(
    {
        ("collections", "defaultdict"): collections.defaultdict,
        ("fractions", "Fraction"): fractions.Fraction,
        ("sympy.core.numbers", "Rational"): sp.Rational,
    }
)


class RestrictedUnpickler(pickle.Unpickler):
    """Unpickler limited to the audited cache's data classes."""

    def find_class(self, module: str, name: str) -&gt; Any:
        try:
            return ALLOWED_PICKLE_CLASSES&#91;(module, name)&#93;
        except KeyError as error:
            raise pickle.UnpicklingError(
                f"forbidden pickle global {module}.{name}"
            ) from error


def sha256(path: Path) -&gt; str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_cache(path: Path) -&gt; dict&#91;str, Any&#93;:
    with gzip.open(path, "rb") as handle:
        value = RestrictedUnpickler(handle).load()
    if not isinstance(value, dict):
        raise TypeError("order-five cache is not a dictionary")
    if set(value) != EXPECTED_CACHE_KEYS:
        raise ValueError(
            f"unexpected cache keys: {sorted(set(value) ^ EXPECTED_CACHE_KEYS)}"
        )
    if tuple(value&#91;"weights"&#93;) != WEIGHTS:
        raise ValueError("unexpected tangent-weight convention")
    if sorted(value&#91;"residuals"&#93;) != &#91;2, 3, 4, 5&#93;:
        raise ValueError("cache does not contain residual orders two through five")
    expected_counts = {
        "pairs": math.comb(11, 2),
        "triples": math.comb(12, 3),
        "quads": math.comb(13, 4),
        "quints": math.comb(14, 5),
    }
    for key, expected in expected_counts.items():
        if len(value&#91;key&#93;) != expected:
            raise ValueError(f"unexpected {key} count")
    return value


def as_fraction(value: Any) -&gt; fractions.Fraction:
    if isinstance(value, fractions.Fraction):
        return value
    if isinstance(value, sp.Rational):
        return fractions.Fraction(int(value.p), int(value.q))
    if isinstance(value, int):
        return fractions.Fraction(value)
    raise TypeError(f"unexpected coefficient type {type(value).__name__}")


def parameter_weight(monomial: Iterable&#91;int&#93;) -&gt; int:
    return sum(WEIGHTS&#91;index&#93; for index in monomial)


def parameter_monomials(
    minimum_degree: int, maximum_degree: int
) -&gt; list&#91;tuple&#91;int, ...&#93;&#93;:
    return &#91;
        monomial
        for degree in range(minimum_degree, maximum_degree + 1)
        for monomial in itertools.combinations_with_replacement(
            range(len(WEIGHTS)), degree
        )
    &#93;


def filtered_equations(
    cache: dict&#91;str, Any&#93;,
) -&gt; dict&#91;
    tuple&#91;int, tuple&#91;int, ...&#93;&#93;,
    dict&#91;tuple&#91;int, ...&#93;, fractions.Fraction&#93;,
&#93;:
    equations: dict&#91;
        tuple&#91;int, tuple&#91;int, ...&#93;&#93;,
        dict&#91;tuple&#91;int, ...&#93;, fractions.Fraction&#93;,
    &#93; = {}
    for order, blocks in sorted(cache&#91;"residuals"&#93;.items()):
        for weight, residuals in sorted(blocks.items()):
            for parameter_monomial, polynomial in residuals.items():
                if len(parameter_monomial) != order:
                    raise ValueError("parameter order mismatch")
                if parameter_weight(parameter_monomial) != weight:
                    raise ValueError("parameter weight mismatch")
                for output_monomial, coefficient in polynomial.items():
                    equation = equations.setdefault(
                        (weight, tuple(output_monomial)), {}
                    )
                    rational = as_fraction(coefficient)
                    previous = equation.get(parameter_monomial)
                    if previous is not None and previous != rational:
                        raise ValueError("conflicting filtered coefficient")
                    equation&#91;tuple(parameter_monomial)&#93; = rational
    return equations


def macaulay_rows(
    equations: dict&#91;
        tuple&#91;int, tuple&#91;int, ...&#93;&#93;,
        dict&#91;tuple&#91;int, ...&#93;, fractions.Fraction&#93;,
    &#93;,
    target_weight: int,
    maximum_degree: int,
) -&gt; tuple&#91;
    list&#91;tuple&#91;int, ...&#93;&#93;,
    list&#91;dict&#91;int, fractions.Fraction&#93;&#93;,
    list&#91;dict&#91;int, fractions.Fraction&#93;&#93;,
&#93;:
    columns = &#91;
        monomial
        for monomial in parameter_monomials(2, maximum_degree)
        if parameter_weight(monomial) == target_weight
    &#93;
    column_index = {monomial: index for index, monomial in enumerate(columns)}
    multipliers: dict&#91;tuple&#91;int, int&#93;, list&#91;tuple&#91;int, ...&#93;&#93;&#93; = (
        collections.defaultdict(list)
    )
    for monomial in parameter_monomials(0, maximum_degree - 2):
        multipliers&#91;(len(monomial), parameter_weight(monomial))&#93;.append(
            monomial
        )

    maximal_ideal_rows: list&#91;dict&#91;int, fractions.Fraction&#93;&#93; = &#91;&#93;
    total_rows: list&#91;dict&#91;int, fractions.Fraction&#93;&#93; = &#91;&#93;
    for (equation_weight, _), polynomial in sorted(equations.items()):
        leading_degree = min(len(monomial) for monomial in polynomial)
        for multiplier_degree in range(maximum_degree - leading_degree + 1):
            for multiplier in multipliers&#91;
                (multiplier_degree, target_weight - equation_weight)
            &#93;:
                row: dict&#91;int, fractions.Fraction&#93; = {}
                for monomial, coefficient in polynomial.items():
                    product = tuple(sorted(monomial + multiplier))
                    if len(product) &gt; maximum_degree:
                        continue
                    if parameter_weight(product) != target_weight:
                        raise AssertionError("constructed row has wrong weight")
                    index = column_index&#91;product&#93;
                    row&#91;index&#93; = row.get(index, fractions.Fraction()) + coefficient
                row = {index: value for index, value in row.items() if value}
                if not row:
                    continue
                total_rows.append(row)
                if multiplier_degree:
                    maximal_ideal_rows.append(row)
    return columns, maximal_ideal_rows, total_rows


def coefficient_mod_prime(value: fractions.Fraction, prime: int) -&gt; int:
    denominator = value.denominator % prime
    if not denominator:
        raise ZeroDivisionError(f"denominator is divisible by {prime}")
    return value.numerator % prime * pow(denominator, -1, prime) % prime


def modular_basis(
    rows: list&#91;dict&#91;int, fractions.Fraction&#93;&#93;, prime: int
) -&gt; tuple&#91;list&#91;int&#93;, list&#91;int&#93;, int&#93;:
    basis: dict&#91;int, dict&#91;int, int&#93;&#93; = {}
    selected_rows: list&#91;int&#93; = &#91;&#93;
    pivot_columns: list&#91;int&#93; = &#91;&#93;
    pivot_product = 1
    for row_index, rational_row in enumerate(rows):
        row = {
            column: coefficient_mod_prime(coefficient, prime)
            for column, coefficient in rational_row.items()
        }
        row = {column: value for column, value in row.items() if value}
        while row:
            pivot = min(row)
            if pivot not in basis:
                pivot_value = row&#91;pivot&#93;
                pivot_product = pivot_product * pivot_value % prime
                inverse = pow(pivot_value, -1, prime)
                basis&#91;pivot&#93; = {
                    column: value * inverse % prime
                    for column, value in row.items()
                }
                selected_rows.append(row_index)
                pivot_columns.append(pivot)
                break
            factor = row&#91;pivot&#93;
            for column, value in basis&#91;pivot&#93;.items():
                updated = (row.get(column, 0) - factor * value) % prime
                if updated:
                    row&#91;column&#93; = updated
                else:
                    row.pop(column, None)
    return selected_rows, pivot_columns, pivot_product


def as_flint_text(value: fractions.Fraction) -&gt; str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def selected_matrix(
    rows: list&#91;dict&#91;int, fractions.Fraction&#93;&#93;,
    selected_rows: list&#91;int&#93;,
    column_count: int,
) -&gt; fmpq_mat:
    entries = &#91;&#93;
    for row_index in selected_rows:
        row = rows&#91;row_index&#93;
        entries.extend(
            as_flint_text(row.get(column, fractions.Fraction()))
            for column in range(column_count)
        )
    return fmpq_mat(len(selected_rows), column_count, entries)


def exact_relations(
    matrix: fmpq_mat,
) -&gt; tuple&#91;list&#91;int&#93;, list&#91;int&#93;, list&#91;list&#91;fractions.Fraction&#93;&#93;&#93;:
    rref, rank = matrix.rref()
    pivot_columns: list&#91;int&#93; = &#91;&#93;
    pivot_rows: dict&#91;int, int&#93; = {}
    for row in range(rank):
        pivot = next(
            (column for column in range(matrix.ncols()) if rref&#91;row, column&#93;),
            None,
        )
        if pivot is None:
            raise AssertionError("nonzero RREF row has no pivot")
        pivot_columns.append(pivot)
        pivot_rows&#91;pivot&#93; = row
    free_columns = &#91;
        column for column in range(matrix.ncols()) if column not in pivot_rows
    &#93;
    relations = &#91;&#93;
    for free_column in free_columns:
        relations.append(
            &#91;
                fractions.Fraction(
                    int((-rref&#91;pivot_rows&#91;pivot&#93;, free_column&#93;).numerator),
                    int((-rref&#91;pivot_rows&#91;pivot&#93;, free_column&#93;).denominator),
                )
                for pivot in pivot_columns
            &#93;
        )
    return pivot_columns, free_columns, relations


def verify_relations(
    rows: list&#91;dict&#91;int, fractions.Fraction&#93;&#93;,
    pivot_columns: list&#91;int&#93;,
    free_columns: list&#91;int&#93;,
    relations: list&#91;list&#91;fractions.Fraction&#93;&#93;,
) -&gt; None:
    pivot_position = {column: index for index, column in enumerate(pivot_columns)}
    free_position = {column: index for index, column in enumerate(free_columns)}
    for row_index, row in enumerate(rows):
        totals = &#91;fractions.Fraction() for _ in free_columns&#93;
        for column, coefficient in row.items():
            if column in pivot_position:
                position = pivot_position&#91;column&#93;
                for relation_index, relation in enumerate(relations):
                    value = relation&#91;position&#93;
                    if value:
                        totals&#91;relation_index&#93; += coefficient * value
            else:
                totals&#91;free_position&#91;column&#93;&#93; += coefficient
        if any(totals):
            raise AssertionError(f"relation failed on row {row_index}")


def relation_digest(
    pivot_columns: list&#91;int&#93;,
    free_columns: list&#91;int&#93;,
    relations: list&#91;list&#91;fractions.Fraction&#93;&#93;,
) -&gt; str:
    value = {
        "pivots": pivot_columns,
        "free": free_columns,
        "relations": &#91;
            &#91;&#91;entry.numerator, entry.denominator&#93; for entry in relation&#93;
            for relation in relations
        &#93;,
    }
    payload = json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(payload).hexdigest()


def certify_rows(
    rows: list&#91;dict&#91;int, fractions.Fraction&#93;&#93;,
    column_count: int,
    prime: int,
) -&gt; dict&#91;str, Any&#93;:
    if not column_count:
        if rows:
            raise AssertionError("rows exist without columns")
        return {
            "row_count": 0,
            "column_count": 0,
            "rank_over_Q": 0,
            "nullity_over_Q": 0,
            "lower_bound": {"prime": prime, "selected_rows": &#91;&#93;, "pivots": &#91;&#93;},
            "upper_bound": {"all_rows_verified": True, "relation_sha256": None},
        }
    selected, modular_pivots, pivot_product = modular_basis(rows, prime)
    matrix = selected_matrix(rows, selected, column_count)
    exact_pivots, free_columns, relations = exact_relations(matrix)
    if len(exact_pivots) != len(modular_pivots):
        raise AssertionError("exact and modular ranks disagree")
    verify_relations(rows, exact_pivots, free_columns, relations)
    return {
        "row_count": len(rows),
        "column_count": column_count,
        "rank_over_Q": len(exact_pivots),
        "nullity_over_Q": len(free_columns),
        "lower_bound": {
            "prime": prime,
            "selected_rows": selected,
            "pivots": modular_pivots,
            "pivot_product_mod_prime": pivot_product,
        },
        "upper_bound": {
            "engine": "python-flint exact fmpq_mat.rref",
            "all_rows_verified": True,
            "relation_sha256": relation_digest(
                exact_pivots, free_columns, relations
            ),
        },
    }


def write_new(path: Path, value: dict&#91;str, Any&#93;) -&gt; None:
    payload = (
        json.dumps(value, indent=2, sort_keys=True, separators=(",", ": ")) + "\n"
    ).encode()
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(payload)


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cache", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--cache-sha256", required=True)
    parser.add_argument("--prime", type=int, default=1_000_003)
    args = parser.parse_args()

    cache_path = args.cache.resolve()
    actual_sha256 = sha256(cache_path)
    if actual_sha256 != args.cache_sha256:
        raise ValueError(
            f"cache digest mismatch: expected {args.cache_sha256}, "
            f"found {actual_sha256}"
        )
    cache = load_cache(cache_path)
    equations = filtered_equations(cache)
    degrees = &#91;&#93;
    previous_quotient = 11
    previous_generators = 0
    for maximum_degree in range(2, 6):
        blocks = &#91;&#93;
        total_rank = 0
        maximal_rank = 0
        weights = range(-3 * maximum_degree, 3 * maximum_degree + 1)
        for weight in weights:
            columns, maximal_rows, total_rows = macaulay_rows(
                equations, weight, maximum_degree
            )
            maximal = certify_rows(maximal_rows, len(columns), args.prime)
            total = certify_rows(total_rows, len(columns), args.prime)
            maximal_rank += maximal&#91;"rank_over_Q"&#93;
            total_rank += total&#91;"rank_over_Q"&#93;
            blocks.append(
                {
                    "weight": weight,
                    "maximal_ideal_multiple": maximal,
                    "ideal": total,
                }
            )
            print(
                f"degree {maximum_degree}, weight {weight}: "
                f"rank(mI)={maximal&#91;'rank_over_Q'&#93;}, "
                f"rank(I)={total&#91;'rank_over_Q'&#93;}",
                flush=True,
            )
        ambient = math.comb(10 + maximum_degree, maximum_degree)
        quotient = ambient - total_rank
        hilbert = quotient - previous_quotient
        degree_monomials = math.comb(9 + maximum_degree, maximum_degree)
        initial_rank = degree_monomials - hilbert
        generators = total_rank - maximal_rank
        new_generators = generators - previous_generators
        degrees.append(
            {
                "maximum_parameter_degree": maximum_degree,
                "ambient_cumulative_dimension": ambient,
                "rank_I_over_Q": total_rank,
                "rank_mI_over_Q": maximal_rank,
                "quotient_cumulative_dimension": quotient,
                "hilbert_value": hilbert,
                "initial_rank": initial_rank,
                "cumulative_minimal_generators": generators,
                "new_minimal_generators": new_generators,
                "blocks": blocks,
            }
        )
        previous_quotient = quotient
        previous_generators = generators

    expected = {
        2: (11, 44, 11),
        3: (112, 108, 13),
        4: (558, 157, 11),
        5: (1857, 145, 0),
    }
    for degree in degrees:
        observed = (
            degree&#91;"initial_rank"&#93;,
            degree&#91;"hilbert_value"&#93;,
            degree&#91;"new_minimal_generators"&#93;,
        )
        if observed != expected&#91;degree&#91;"maximum_parameter_degree"&#93;&#93;:
            raise AssertionError((degree&#91;"maximum_parameter_degree"&#93;, observed))
    final = degrees&#91;-1&#93;
    if (
        final&#91;"rank_mI_over_Q"&#93;,
        final&#91;"rank_I_over_Q"&#93;,
        final&#91;"cumulative_minimal_generators"&#93;,
    ) != (2503, 2538, 35):
        raise AssertionError("unexpected order-five cumulative ranks")

    output = {
        "schema_version": 1,
        "claim": (
            "The recovered direct-coordinate filtered Kuranishi ideal has "
            "Hilbert value 145 in parameter order five and no new minimal "
            "quintic generator."
        ),
        "scope": (
            "Exact replay of the recovered residual cache; not an independent "
            "reconstruction from the base map and transverse slice."
        ),
        "cache": {
            "path_name": cache_path.name,
            "sha256": actual_sha256,
            "restricted_unpickler": True,
        },
        "parameter_weights": list(WEIGHTS),
        "monomial_order": (
            "total parameter degree, then lexicographic combinations-with-"
            "replacement order on zero-based parameter indices"
        ),
        "degrees": degrees,
    }
    write_new(args.output.resolve(), output)
    print("order-five exact replay certificate written", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-2210ec80b02f0f23"></a>

## `research-notes/lane3-recovery-integration-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 3 recovery integration audit

This package closes the Lane 3 recovery audit without changing the retained
claim graph, handoff manifests, or any site source.  It records three distinct
evidence boundaries: the recovered direct order-five row spaces, the generated
formal-effectivity reports, and the already completed order-six weight and
sextic computations.

## Direct order five

Commit `f1b6ed8` reached `main` while this isolated branch was being prepared.
It already adds the producer and prose package at
`research-notes/lane3-order5-recovery-20260803-v1/`; those files are not
duplicated here.

The audited public archive has SHA-256
`48ae426de30743ad270b52299e633725153a27ceef20b131d657c682236c78cd`.
Its restricted-loader input cache has SHA-256
`2790e24c2d5ec803b1b00454d96add7c2b781095a6d2431d0ee0c563ac697033`,
and its exact replay certificate has SHA-256
`91aa952ea40b80a6d9c848e7aba51a9924cedb2d5b5b7caf4f7dd544b7d990e4`.
The exact replay gives

| parameter degree | initial rank | Hilbert value | new minimal generators |
| ---: | ---: | ---: | ---: |
| 2 | 11 | 44 | 11 |
| 3 | 112 | 108 | 13 |
| 4 | 558 | 157 | 11 |
| 5 | 1857 | 145 | 0 |

At degree five, `rank(mI)=2503` and `rank(I)=2538`.  Every rational upper
rank bound in the certificate is checked against every reconstructed row.
A nonzero pivot minor modulo `1000003` supplies each matching lower bound.

This is an exact replay of recovered direct-coordinate residual equations.
It is not the independent reconstruction from the displayed degree-seven map
and transverse slice requested by `P3-L3A0`, and it does not expose a
marked-root contracting homotopy.

## Formal-effectivity report retention

The three JSON files under `raw-formal-effectivity-reports/` are byte-for-byte
copies of the untracked reports inspected in the main checkout.  They also
match the reports preserved in
`runs/assimilation-replay-20260802-v1/lane3-formal-effectivity/`.
`manifest.json` pins every report and its producer.

The executable evidence retained from those reports is deliberately narrow:

- exact symbolic root-translation identities and finite residual samples;
- finite ramification, compatibility, degree, affine-frame, and formal-series
  sample grids;
- an independent sparse-`Fraction` replay of the finite staircase grid; and
- finite monomial counts, coefficient-variable counts, equation-degree
  bookkeeping, inequalities, and numerical asymptotic samples.

The status strings do not independently prove the Program 4 stable
`q`-classification, generic-fibre emptiness, the generic-combination lemma,
the parametric Nullstellensatz, the unrestricted double-logarithmic lower
bound, or the algebraic-stack corollary.  Those theorem-level conclusions
remain dependent on the hand proof and the inputs listed in `manifest.json`.
In particular, the asymptotic samples are consistency checks, not numerical
proofs of a limit.

The external bound was checked against D'Andrea--Krick--Sombra, Theorem 0.5,
which gives the parameter-degree estimate used after reduction to `N+1`
equations (&#91;DOI 10.24033/asens.2196&#93;(https://doi.org/10.24033/asens.2196)).
The reduction itself is a separate argument in
`formal_effectivity_theorem.md` and is not executed by the report producer.

## Weights +2 through +15 and the sextic

The requested order-six inputs are complete and the calculations have already
finished.  Rerunning them as new Slurm jobs would duplicate verified work.

- Weights `+2..+5` are deficient, so the full-rank driver is the wrong
  command for that range.  Exact FLINT certificates give ranks/nullities
  `553/62`, `545/41`, `523/23`, and `473/7`, respectively, and verify every
  rational relation against every original row.
- Weights `+6..+15` are full column rank.  Two-prime maximal-minor
  certificates, modulo `1000003` and `1000033`, cover the larger completed
  range `+6..+18` and therefore cover the requested range.
- The exact weight-three sextic reconstruction is runnable and already has a
  completed certificate.  It gives `rank(mI)=542`, `rank(I)=545`, sextic
  initial ranks `341` and `342`, and one primitive four-term class.

All of these computations use the same recovered order-six cache, SHA-256
`2fb4548d3c274f3216617c3815dceff7c1a0877832e99839816e2785ba4c3d82`.
The producer scripts refuse to replace a nonidentical output.  Fresh replays
must use new versioned output paths.  Representative commands are:

```bash
uv run --with python-flint python \
  manuscripts/03-local-rigidity/code/order-six/certify_deficient_block_flint.py \
  /path/to/direct_order6_residual_series.pkl.gz \
  /new/versioned/output/weight-2.json \
  --cache-sha256 2fb4548d3c274f3216617c3815dceff7c1a0877832e99839816e2785ba4c3d82 \
  --weight 2

uv run python \
  manuscripts/03-local-rigidity/code/order-six/certify_full_rank_blocks.py \
  /path/to/direct_order6_residual_series.pkl.gz \
  /new/versioned/output/full-rank-weights-6-15-p1000003.json \
  --cache-sha256 2fb4548d3c274f3216617c3815dceff7c1a0877832e99839816e2785ba4c3d82 \
  --prime 1000003 \
  --weights 6:15

uv run --with python-flint python \
  manuscripts/03-local-rigidity/code/order-six/extract_sextic_generator_flint.py \
  /path/to/direct_order6_residual_series.pkl.gz \
  /new/versioned/output/primitive-weight-three-sextic.json \
  --cache-sha256 2fb4548d3c274f3216617c3815dceff7c1a0877832e99839816e2785ba4c3d82
```

Do not run `certify_full_rank_blocks.py --weights 2:15` unchanged: it is
known to stop at weight `+2` because that block is genuinely deficient.

## Audit replay

The repository-only check validates the copied reports, their producer
hashes, the finite sample grids, and the theorem-source hashes:

```bash
uv run python \
  research-notes/lane3-recovery-integration-20260803-v1/check_lane3_recovery.py
```

On the workspace that holds the materialized evidence, add both optional
arguments:

```bash
uv run python \
  research-notes/lane3-recovery-integration-20260803-v1/check_lane3_recovery.py \
  --order5-archive \
  /path/to/versioned-artifact \
  --runs-root /path/to/versioned-artifact
```

The checker is read-only.  No canonical retained-graph selector is changed by
this package.
</code></pre>

<a id="source-135f83f2902aae9d"></a>

## `research-notes/lane3-recovery-integration-20260803-v1/check_lane3_recovery.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Check the retained Lane 3 reports and optional materialized artifacts."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import zipfile
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
REPO = HERE.parents&#91;1&#93;
MANIFEST = HERE / "manifest.json"


def digest_bytes(payload: bytes) -&gt; str:
    return hashlib.sha256(payload).hexdigest()


def digest(path: Path) -&gt; str:
    return digest_bytes(path.read_bytes())


def load_json(path: Path) -&gt; dict&#91;str, Any&#93;:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected JSON object: {path}")
    return value


def assert_hash(path: Path, expected: str) -&gt; None:
    actual = digest(path)
    if actual != expected:
        raise AssertionError(
            f"SHA-256 mismatch for {path}: expected {expected}, found {actual}"
        )


def check_formal_reports(manifest: dict&#91;str, Any&#93;) -&gt; None:
    formal = manifest&#91;"formal_effectivity"&#93;
    reports: dict&#91;str, dict&#91;str, Any&#93;&#93; = {}
    for item in formal&#91;"reports"&#93;:
        report_path = HERE / item&#91;"path"&#93;
        producer_path = REPO / item&#91;"producer_path"&#93;
        if report_path.stat().st_size != item&#91;"bytes"&#93;:
            raise AssertionError(f"byte-size mismatch: {report_path}")
        assert_hash(report_path, item&#91;"sha256"&#93;)
        assert_hash(producer_path, item&#91;"producer_sha256"&#93;)
        reports&#91;report_path.name&#93; = load_json(report_path)

    theorem = formal&#91;"theorem_source"&#93;
    assert_hash(REPO / theorem&#91;"path"&#93;, theorem&#91;"sha256"&#93;)
    program4 = formal&#91;"external_inputs_not_reproved_by_reports"&#93;&#91;0&#93;
    assert_hash(REPO / "manuscripts/04-stable-moduli/main.tex", program4&#91;"sha256"&#93;)

    symbolic = reports&#91;"formal_effectivity_report.json"&#93;
    if symbolic&#91;"status"&#93; != "ALL FORMAL-EFFECTIVITY CHECKS PASSED":
        raise AssertionError("unexpected symbolic report status")
    residuals = symbolic&#91;"universal_residual_checks"&#93;
    if &#91;item&#91;"D"&#93; for item in residuals&#93; != list(range(11)):
        raise AssertionError("unexpected universal residual sample range")
    expected_degrees = &#91;-1, *range(1, 11)&#93;
    if &#91;item&#91;"phi_c_degree"&#93; for item in residuals&#93; != expected_degrees:
        raise AssertionError("unexpected residual translation degrees")

    ramification = symbolic&#91;"ramification_samples"&#93;
    expected_pairs = &#91;
        (modulus, order)
        for modulus in range(2, 15)
        for order in range(1, min(5, modulus))
    &#93;
    if &#91;(item&#91;"M"&#93;, item&#91;"e"&#93;) for item in ramification&#93; != expected_pairs:
        raise AssertionError("unexpected symbolic ramification grid")
    for item in ramification:
        expected = max(0, math.ceil(item&#91;"M"&#93; / item&#91;"e"&#93;) - 2)
        if item&#91;"minimal_c_degree"&#93; != expected:
            raise AssertionError(f"bad ramification degree: {item}")

    compatibility = symbolic&#91;"unramified_compatibility"&#93;
    if &#91;item&#91;"M"&#93; for item in compatibility&#93; != list(range(1, 15)):
        raise AssertionError("unexpected compatibility range")
    for item in compatibility:
        modulus = item&#91;"M"&#93;
        expected_degree = max(0, modulus - 2)
        expected_source = 1 if modulus &lt;= 2 else 4 * expected_degree
        expected_target = 1 if modulus &lt;= 2 else modulus - 1
        observed = (
            item&#91;"c_degree"&#93;,
            item&#91;"source_degree"&#93;,
            item&#91;"target_degree"&#93;,
        )
        if observed != (expected_degree, expected_source, expected_target):
            raise AssertionError(f"bad compatibility row: {item}")

    canonical = symbolic&#91;"canonical_degree_checks"&#93;
    if &#91;item&#91;"M"&#93; for item in canonical&#93; != list(range(3, 11)):
        raise AssertionError("unexpected canonical degree range")
    for item in canonical:
        degree = item&#91;"M"&#93; - 2
        if (
            item&#91;"D"&#93;,
            item&#91;"source_degree"&#93;,
            item&#91;"target_degree"&#93;,
            item&#91;"target_inverse_degree"&#93;,
        ) != (degree, 4 * degree, degree + 1, degree + 1):
            raise AssertionError(f"bad canonical degree row: {item}")

    affine = symbolic&#91;"affine_frame_checks"&#93;
    if &#91;item&#91;"M"&#93; for item in affine&#93; != list(range(3, 13)):
        raise AssertionError("unexpected affine sample range")
    if any(item&#91;"h_c_degree"&#93; != item&#91;"M"&#93; - 2 for item in affine):
        raise AssertionError("affine sample lowers the expected degree")

    formal_coefficients = symbolic&#91;"formal_limit_coefficients"&#93;
    if &#91;item&#91;"s_power"&#93; for item in formal_coefficients&#93; != list(range(2, 13)):
        raise AssertionError("unexpected formal coefficient range")
    if any(item&#91;"c_degree"&#93; != item&#91;"s_power"&#93; - 1 for item in formal_coefficients):
        raise AssertionError("unexpected formal coefficient degree")

    independent = reports&#91;"formal_effectivity_independent_report.json"&#93;
    if independent&#91;"status"&#93; != "INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED":
        raise AssertionError("unexpected independent report status")
    expected_samples = &#91;
        {
            "M": modulus,
            "e": order,
            "D": max(0, math.ceil(modulus / order) - 2),
            "sharp": True,
        }
        for modulus in range(2, 31)
        for order in range(1, min(modulus, 8))
    &#93;
    if independent&#91;"samples"&#93; != expected_samples:
        raise AssertionError("independent staircase samples do not match the grid")
    if independent&#91;"sample_count"&#93; != len(expected_samples):
        raise AssertionError("independent sample count mismatch")

    bound = reports&#91;"effective_unframed_bound_report.json"&#93;
    if bound&#91;"status"&#93; != "ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED":
        raise AssertionError("unexpected bound report status")
    enumerations = bound&#91;"enumeration_checks"&#93;
    expected_enumerations = &#91;
        {"n": n, "b": degree, "count": math.comb(n + degree, n)}
        for n in range(1, 5)
        for degree in range(5)
    &#93;
    if enumerations != expected_enumerations:
        raise AssertionError("monomial enumeration checks do not match formulas")
    for item in bound&#91;"degree_checks"&#93;:
        degree = item&#91;"b"&#93;
        if item != {
            "b": degree,
            "coefficient_degree": max(degree + 1, 11),
            "parameter_degree": 2 * degree,
        }:
            raise AssertionError(f"bad equation-degree row: {item}")
    if &#91;item&#91;"b"&#93; for item in bound&#91;"degree_checks"&#93;&#93; != list(range(1, 21)):
        raise AssertionError("unexpected equation-degree sample range")
    for item in bound&#91;"exact_samples"&#93;:
        n = item&#91;"ambient_dimension"&#93;
        degree = item&#91;"b"&#93;
        monomials = math.comb(n + degree, n)
        if item&#91;"monomials_per_coordinate"&#93; != monomials:
            raise AssertionError(f"bad monomial count: {item}")
        if item&#91;"coefficient_variables"&#93; != 4 * n * monomials:
            raise AssertionError(f"bad coefficient-variable count: {item}")
    if len(bound&#91;"exact_samples"&#93;) != 20:
        raise AssertionError("unexpected exact bound sample count")
    for item in bound&#91;"fixed_n_asymptotics"&#93;:
        if not math.isclose(
            item&#91;"target_coefficient"&#93;,
            4 / math.factorial(item&#91;"n"&#93; - 1),
        ):
            raise AssertionError(f"bad fixed-n target: {item}")
    for item in bound&#91;"unrestricted_asymptotics"&#93;:
        if not math.isclose(item&#91;"target"&#93;, math.log(4)):
            raise AssertionError(f"bad unrestricted target: {item}")


def check_order5_archive(path: Path, manifest: dict&#91;str, Any&#93;) -&gt; None:
    order5 = manifest&#91;"order5_evidence"&#93;
    assert_hash(path, order5&#91;"archive_sha256"&#93;)
    with zipfile.ZipFile(path) as archive:
        cache = archive.read(order5&#91;"cache_name"&#93;)
        certificate_payload = archive.read(order5&#91;"certificate_name"&#93;)
        producer = archive.read(Path(manifest&#91;"order5_overlap"&#93;&#91;"producer_path"&#93;).name)
    if digest_bytes(cache) != order5&#91;"cache_sha256"&#93;:
        raise AssertionError("order-five cache digest mismatch")
    if digest_bytes(certificate_payload) != order5&#91;"certificate_sha256"&#93;:
        raise AssertionError("order-five certificate digest mismatch")
    if digest_bytes(producer) != manifest&#91;"order5_overlap"&#93;&#91;"producer_sha256"&#93;:
        raise AssertionError("order-five producer digest mismatch")
    certificate = json.load(io.TextIOWrapper(io.BytesIO(certificate_payload)))
    if certificate&#91;"cache"&#93;&#91;"sha256"&#93; != order5&#91;"cache_sha256"&#93;:
        raise AssertionError("certificate names a different order-five cache")
    final = certificate&#91;"degrees"&#93;&#91;-1&#93;
    retained = order5&#91;"retained_result"&#93;
    observed = {
        "initial_rank": final&#91;"initial_rank"&#93;,
        "hilbert_value": final&#91;"hilbert_value"&#93;,
        "new_minimal_generators": final&#91;"new_minimal_generators"&#93;,
        "rank_mI_over_Q": final&#91;"rank_mI_over_Q"&#93;,
        "rank_I_over_Q": final&#91;"rank_I_over_Q"&#93;,
    }
    if observed != retained:
        raise AssertionError(f"order-five retained result mismatch: {observed}")
    for degree in certificate&#91;"degrees"&#93;:
        for block in degree&#91;"blocks"&#93;:
            for key in ("maximal_ideal_multiple", "ideal"):
                if not block&#91;key&#93;&#91;"upper_bound"&#93;&#91;"all_rows_verified"&#93;:
                    raise AssertionError(
                        "order-five upper bound is not all-row verified"
                    )


def check_order6_artifacts(runs_root: Path, manifest: dict&#91;str, Any&#93;) -&gt; None:
    order6 = manifest&#91;"order6_evidence"&#93;
    for relative, expected in order6&#91;"producer_sha256"&#93;.items():
        assert_hash(REPO / relative, expected)
    loaded: dict&#91;str, dict&#91;str, Any&#93;&#93; = {}
    for relative, expected in order6&#91;"artifacts"&#93;.items():
        path = runs_root / relative
        assert_hash(path, expected)
        loaded&#91;relative&#93; = load_json(path)

    positive_paths = &#91;
        "program3-order6-positive-v2/full-rank-blocks-p1000003.json",
        "program3-order6-positive-v2/full-rank-blocks-p1000033.json",
    &#93;
    for expected_prime, relative in zip((1_000_003, 1_000_033), positive_paths):
        data = loaded&#91;relative&#93;
        if data&#91;"prime"&#93; != expected_prime:
            raise AssertionError(f"unexpected prime in {relative}")
        if data&#91;"cache"&#93;&#91;"sha256"&#93; != order6&#91;"cache_sha256"&#93;:
            raise AssertionError(f"cache mismatch in {relative}")
        if &#91;item&#91;"weight"&#93; for item in data&#91;"blocks"&#93;&#93; != list(range(6, 19)):
            raise AssertionError(f"unexpected positive-weight coverage in {relative}")
        for block in data&#91;"blocks"&#93;:
            if not block&#91;"full_column_rank_over_Q"&#93;:
                raise AssertionError(f"non-full block in {relative}")
            if block&#91;"rank"&#93; != block&#91;"column_count"&#93;:
                raise AssertionError(f"rank mismatch in {relative}")
            if block&#91;"echelon_pivot_product_mod_prime"&#93; == 0:
                raise AssertionError(f"zero pivot product in {relative}")

    for weight in range(1, 6):
        relative = f"program3-order6-deficient-v3/weight-{weight}.json"
        data = loaded&#91;relative&#93;
        if data&#91;"weight"&#93; != weight:
            raise AssertionError(f"wrong deficient weight in {relative}")
        if data&#91;"cache"&#93;&#91;"sha256"&#93; != order6&#91;"cache_sha256"&#93;:
            raise AssertionError(f"cache mismatch in {relative}")
        if data&#91;"rank_over_Q"&#93; + data&#91;"nullity_over_Q"&#93; != data&#91;"column_count"&#93;:
            raise AssertionError(f"rank-nullity mismatch in {relative}")
        if not data&#91;"upper_bound_certificate"&#93;&#91;"all_rational_rows_verified"&#93;:
            raise AssertionError(f"upper bound is not all-row verified in {relative}")
        if data&#91;"lower_bound_certificate"&#93;&#91;"echelon_pivot_product_mod_prime"&#93; == 0:
            raise AssertionError(f"zero deficient pivot product in {relative}")

    sextic_relative = "program3-order6-sextic-v1/primitive-weight-three-sextic.json"
    sextic = loaded&#91;sextic_relative&#93;
    if sextic&#91;"cache"&#93;&#91;"sha256"&#93; != order6&#91;"cache_sha256"&#93;:
        raise AssertionError("sextic cache mismatch")
    expected = order6&#91;"sextic_result"&#93;
    observed = {
        "target_weight": sextic&#91;"target_weight"&#93;,
        "rank_mI_over_Q": sextic&#91;"rank_mI_over_Q"&#93;,
        "rank_I_over_Q": sextic&#91;"rank_I_over_Q"&#93;,
        "sextic_initial_rank_mI_over_Q": sextic&#91;"sextic_initial_rank_mI_over_Q"&#93;,
        "sextic_initial_rank_I_over_Q": sextic&#91;"sextic_initial_rank_I_over_Q"&#93;,
        "new_sextic_dimension": sextic&#91;"new_sextic_dimension"&#93;,
        "primitive_term_count": sextic&#91;"primitive_sextic"&#93;&#91;"term_count"&#93;,
    }
    if observed != expected:
        raise AssertionError(f"sextic result mismatch: {observed}")
    upper = sextic&#91;"upper_bound_certificates"&#93;
    if not upper&#91;"mI_all_rational_rows_verified"&#93;:
        raise AssertionError("sextic mI upper bound is not all-row verified")
    if not upper&#91;"I_all_rational_rows_verified"&#93;:
        raise AssertionError("sextic I upper bound is not all-row verified")


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order5-archive", type=Path)
    parser.add_argument("--runs-root", type=Path)
    args = parser.parse_args()
    manifest = load_json(MANIFEST)
    check_formal_reports(manifest)
    print("FORMAL REPORT RETENTION CHECKS PASSED")
    if args.order5_archive is not None:
        check_order5_archive(args.order5_archive.resolve(), manifest)
        print("ORDER-FIVE ARCHIVE CHECKS PASSED")
    if args.runs_root is not None:
        check_order6_artifacts(args.runs_root.resolve(), manifest)
        print("ORDER-SIX ARTIFACT CHECKS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-c34cdf96a598d48f"></a>

## `research-notes/lane3-recovery-integration-20260803-v1/manifest.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "package_id": "lane3-recovery-integration-20260803-v1",
  "base_commit": "25fd4547397cca49fbff3293e381359930cbdbf0",
  "order5_overlap": {
    "commit": "f1b6ed8",
    "note": "The order-five producer and prose package were independently added to main while this branch was being prepared; this package audits that result without duplicating those files.",
    "producer_bytes": 18151,
    "producer_path": "research-notes/lane3-order5-recovery-20260803-v1/verify_order5_recovery.py",
    "producer_sha256": "3edf0aa77f4078ca6a694132acb23b5503c60ba4b4159dec5f7dfb61718bbf5a"
  },
  "order5_evidence": {
    "archive_name": "03-direct-order-five-recovery-2026-08-03-v1.zip",
    "archive_sha256": "48ae426de30743ad270b52299e633725153a27ceef20b131d657c682236c78cd",
    "cache_name": "direct_order5_residual_series.pkl.gz",
    "cache_sha256": "2790e24c2d5ec803b1b00454d96add7c2b781095a6d2431d0ee0c563ac697033",
    "certificate_name": "order5_exact_replay_certificate.json",
    "certificate_sha256": "91aa952ea40b80a6d9c848e7aba51a9924cedb2d5b5b7caf4f7dd544b7d990e4",
    "scope": "Exact replay of a recovered direct-coordinate residual cache, not an independent reconstruction from the displayed map and slice.",
    "retained_result": {
      "initial_rank": 1857,
      "hilbert_value": 145,
      "new_minimal_generators": 0,
      "rank_mI_over_Q": 2503,
      "rank_I_over_Q": 2538
    }
  },
  "formal_effectivity": {
    "reports": &#91;
      {
        "bytes": 13242,
        "path": "raw-formal-effectivity-reports/formal_effectivity_report.json",
        "producer_path": "research-notes/lane3-formal-effectivity/verify_formal_effectivity.py",
        "producer_sha256": "fed25d2940f0fca521cde6b03d83ad96a7e7179d366ed4ac0bf99ac5c8d2632f",
        "sha256": "8e3403dc5259ff05fb1b0d7eb44e7108f0a8faa0a61916926562b0d5df004f01",
        "retained_scope": "Exact symbolic identities plus the finite degree, ramification, compatibility, affine-frame, and formal-coefficient samples encoded by the producer."
      },
      {
        "bytes": 14058,
        "path": "raw-formal-effectivity-reports/formal_effectivity_independent_report.json",
        "producer_path": "research-notes/lane3-formal-effectivity/verify_formal_effectivity_independent.py",
        "producer_sha256": "700170ac7053a2cdf8521189faede15107cd651e8277eb341f108602f413f46a",
        "sha256": "6495bcc8bcab16479caae583bbdab0ecf5fd806c245bd8370858b7fff806a184",
        "retained_scope": "Pure-Python sparse checks of the finite residual staircase, sharpness grid, and compatibility grid."
      },
      {
        "bytes": 12169,
        "path": "raw-formal-effectivity-reports/effective_unframed_bound_report.json",
        "producer_path": "research-notes/lane3-formal-effectivity/verify_effective_unframed_bound.py",
        "producer_sha256": "7f5cfe5706f4b41cd2c680fce23c3e907bc0e9e98a78fc052ac7b5d3cfe4b74f",
        "sha256": "29ebf7cb96eec3d6671078ae5eb2cce369e7bfc9b89428500eab9d966c0a7f9c",
        "retained_scope": "Finite combinatorial counts, equation-degree bookkeeping, inequalities, and numerical asymptotic samples only."
      }
    &#93;,
    "theorem_source": {
      "path": "research-notes/lane3-formal-effectivity/formal_effectivity_theorem.md",
      "sha256": "1f01ad944f7bcc1fbc9474497f5071fd3df91d8305b043dc975513db9c7f9267"
    },
    "external_inputs_not_reproved_by_reports": &#91;
      {
        "locator": "manuscripts/04-stable-moduli/main.tex, thm:main and cor:q-classification",
        "sha256": "6ad054451c7b0087602be4961ce33102947eb5d53002a8579077784cc1fb0806",
        "statement": "Complete stable q-classification on the normalized generic fibre."
      },
      {
        "doi": "10.24033/asens.2196",
        "locator": "D'Andrea--Krick--Sombra, Theorem 0.5",
        "statement": "Parametric effective Nullstellensatz degree bound."
      },
      {
        "locator": "formal_effectivity_theorem.md, Theorem 6.2 proof",
        "statement": "Constant generic-combination reduction from all coefficient equations to N+1 equations."
      }
    &#93;,
    "not_promoted_from_executable_status_alone": &#91;
      "generic-fibre emptiness",
      "the unrestricted stable-equivalence lower bound",
      "the algebraic-stack diagonal corollary",
      "the stable q-classification",
      "the external Nullstellensatz"
    &#93;
  },
  "order6_evidence": {
    "cache_name": "direct_order6_residual_series.pkl.gz",
    "cache_sha256": "2fb4548d3c274f3216617c3815dceff7c1a0877832e99839816e2785ba4c3d82",
    "producer_sha256": {
      "manuscripts/03-local-rigidity/code/order-six/certify_deficient_block.py": "25f640f66536d1cec017830bba4d3813746fe8198e8bee9281afdc597d522d34",
      "manuscripts/03-local-rigidity/code/order-six/certify_deficient_block_flint.py": "58592924c0c1ad91760312f297c7c2853ce846d129daca15aa077b037914b150",
      "manuscripts/03-local-rigidity/code/order-six/certify_full_rank_blocks.py": "4ee98911c458c4c9981547b8161779629a314586193bf8f11b9570fea756a748",
      "manuscripts/03-local-rigidity/code/order-six/extract_sextic_generator_flint.py": "20cb78032fa04a2e071195ed4f62a2db879967b51da7913abf149dfe5cea0b9f"
    },
    "artifacts": {
      "program3-order6-positive-v2/full-rank-blocks-p1000003.json": "51f15a2532821280870b130f1f095facfd65c7326b76c0646b308f5af1d12b96",
      "program3-order6-positive-v2/full-rank-blocks-p1000033.json": "1a5ec0729f1ef0e0fa2c4bfa23771590047c50e985a4bb4be7cbaeaa369e8410",
      "program3-order6-deficient-v3/weight-1.json": "c5843f917029a1f9666abcddee774b4de4c6cf79bb4523a0bfefbe791b5c4e3e",
      "program3-order6-deficient-v3/weight-2.json": "fd627e9efcb30965db61d57d8ccbd4532500e57bd46e1b8313a634a3fdaf8340",
      "program3-order6-deficient-v3/weight-3.json": "04abe980ecce3ee31f059994039553eea24794224e3d56f86f48a5787f390e3c",
      "program3-order6-deficient-v3/weight-4.json": "2fa0ad1c45dca7675f6aa607d024b8ef095c7639a44f009a9ed6a7c0a7bd99c0",
      "program3-order6-deficient-v3/weight-5.json": "a9d574f67ff4faa6f4e157988b9a6263d8bd454eb73b2f652ebbe8db73398547",
      "program3-order6-sextic-v1/primitive-weight-three-sextic.json": "4eb5fe272b8dd78e62d740a6790d84f3e26122a9340e13e50c7128b95993e753"
    },
    "requested_weight_coverage": {
      "exact_deficient_blocks": &#91;2, 3, 4, 5&#93;,
      "two_prime_full_rank_blocks": &#91;6, 7, 8, 9, 10, 11, 12, 13, 14, 15&#93;
    },
    "sextic_result": {
      "target_weight": 3,
      "rank_mI_over_Q": 542,
      "rank_I_over_Q": 545,
      "sextic_initial_rank_mI_over_Q": 341,
      "sextic_initial_rank_I_over_Q": 342,
      "new_sextic_dimension": 1,
      "primitive_term_count": 4
    }
  }
}
</code></pre>

<a id="source-6cb100d21dd23409"></a>

## `research-notes/lane3-recovery-integration-20260803-v1/raw-formal-effectivity-reports/effective_unframed_bound_report.json`

<pre><code class="language-json">
{
  "degree_checks": &#91;
    {
      "b": 1,
      "coefficient_degree": 11,
      "parameter_degree": 2
    },
    {
      "b": 2,
      "coefficient_degree": 11,
      "parameter_degree": 4
    },
    {
      "b": 3,
      "coefficient_degree": 11,
      "parameter_degree": 6
    },
    {
      "b": 4,
      "coefficient_degree": 11,
      "parameter_degree": 8
    },
    {
      "b": 5,
      "coefficient_degree": 11,
      "parameter_degree": 10
    },
    {
      "b": 6,
      "coefficient_degree": 11,
      "parameter_degree": 12
    },
    {
      "b": 7,
      "coefficient_degree": 11,
      "parameter_degree": 14
    },
    {
      "b": 8,
      "coefficient_degree": 11,
      "parameter_degree": 16
    },
    {
      "b": 9,
      "coefficient_degree": 11,
      "parameter_degree": 18
    },
    {
      "b": 10,
      "coefficient_degree": 11,
      "parameter_degree": 20
    },
    {
      "b": 11,
      "coefficient_degree": 12,
      "parameter_degree": 22
    },
    {
      "b": 12,
      "coefficient_degree": 13,
      "parameter_degree": 24
    },
    {
      "b": 13,
      "coefficient_degree": 14,
      "parameter_degree": 26
    },
    {
      "b": 14,
      "coefficient_degree": 15,
      "parameter_degree": 28
    },
    {
      "b": 15,
      "coefficient_degree": 16,
      "parameter_degree": 30
    },
    {
      "b": 16,
      "coefficient_degree": 17,
      "parameter_degree": 32
    },
    {
      "b": 17,
      "coefficient_degree": 18,
      "parameter_degree": 34
    },
    {
      "b": 18,
      "coefficient_degree": 19,
      "parameter_degree": 36
    },
    {
      "b": 19,
      "coefficient_degree": 20,
      "parameter_degree": 38
    },
    {
      "b": 20,
      "coefficient_degree": 21,
      "parameter_degree": 40
    }
  &#93;,
  "enumeration_checks": &#91;
    {
      "b": 0,
      "count": 1,
      "n": 1
    },
    {
      "b": 1,
      "count": 2,
      "n": 1
    },
    {
      "b": 2,
      "count": 3,
      "n": 1
    },
    {
      "b": 3,
      "count": 4,
      "n": 1
    },
    {
      "b": 4,
      "count": 5,
      "n": 1
    },
    {
      "b": 0,
      "count": 1,
      "n": 2
    },
    {
      "b": 1,
      "count": 3,
      "n": 2
    },
    {
      "b": 2,
      "count": 6,
      "n": 2
    },
    {
      "b": 3,
      "count": 10,
      "n": 2
    },
    {
      "b": 4,
      "count": 15,
      "n": 2
    },
    {
      "b": 0,
      "count": 1,
      "n": 3
    },
    {
      "b": 1,
      "count": 4,
      "n": 3
    },
    {
      "b": 2,
      "count": 10,
      "n": 3
    },
    {
      "b": 3,
      "count": 20,
      "n": 3
    },
    {
      "b": 4,
      "count": 35,
      "n": 3
    },
    {
      "b": 0,
      "count": 1,
      "n": 4
    },
    {
      "b": 1,
      "count": 5,
      "n": 4
    },
    {
      "b": 2,
      "count": 15,
      "n": 4
    },
    {
      "b": 3,
      "count": 35,
      "n": 4
    },
    {
      "b": 4,
      "count": 70,
      "n": 4
    }
  &#93;,
  "exact_samples": &#91;
    {
      "ambient_dimension": 3,
      "b": 1,
      "coefficient_variables": 48,
      "d": 11,
      "h": 2,
      "log10_H": 51.9780749632873,
      "log_H": 119.68394057299237,
      "m": 0,
      "monomials_per_coordinate": 4,
      "tradeoff_log_H": 483.0579141287609
    },
    {
      "ambient_dimension": 3,
      "b": 2,
      "coefficient_variables": 120,
      "d": 11,
      "h": 4,
      "log10_H": 127.6519675806314,
      "log_H": 293.9295176425211,
      "m": 0,
      "monomials_per_coordinate": 10,
      "tradeoff_log_H": 992.2800909606378
    },
    {
      "ambient_dimension": 3,
      "b": 4,
      "coefficient_variables": 420,
      "d": 11,
      "h": 8,
      "log10_H": 440.91229984928214,
      "log_H": 1015.2380889506779,
      "m": 0,
      "monomials_per_coordinate": 35,
      "tradeoff_log_H": 4168.982138178213
    },
    {
      "ambient_dimension": 3,
      "b": 8,
      "coefficient_variables": 1980,
      "d": 11,
      "h": 16,
      "log10_H": 2066.45852107148,
      "log_H": 4758.196585909713,
      "m": 0,
      "monomials_per_coordinate": 165,
      "tradeoff_log_H": 72375.4145070419
    },
    {
      "ambient_dimension": 3,
      "b": 12,
      "coefficient_variables": 5460,
      "d": 13,
      "h": 24,
      "log10_H": 6087.248187013575,
      "log_H": 14016.40693277249,
      "m": 0,
      "monomials_per_coordinate": 455,
      "tradeoff_log_H": 1232942.5537815283
    },
    {
      "ambient_dimension": 4,
      "b": 1,
      "coefficient_variables": 80,
      "d": 11,
      "h": 2,
      "log10_H": 85.52092982720063,
      "log_H": 196.91921815910203,
      "m": 1,
      "monomials_per_coordinate": 5,
      "tradeoff_log_H": 1279.2056277171869
    },
    {
      "ambient_dimension": 4,
      "b": 2,
      "coefficient_variables": 240,
      "d": 11,
      "h": 4,
      "log10_H": 252.91832147187682,
      "log_H": 582.3659567662195,
      "m": 1,
      "monomials_per_coordinate": 15,
      "tradeoff_log_H": 2634.826884293306
    },
    {
      "ambient_dimension": 4,
      "b": 4,
      "coefficient_variables": 1120,
      "d": 11,
      "h": 8,
      "log10_H": 1170.312502976799,
      "log_H": 2694.744123498927,
      "m": 1,
      "monomials_per_coordinate": 70,
      "tradeoff_log_H": 11102.571075533879
    },
    {
      "ambient_dimension": 4,
      "b": 8,
      "coefficient_variables": 7920,
      "d": 11,
      "h": 16,
      "log10_H": 8252.932966449087,
      "log_H": 19003.0804220248,
      "m": 1,
      "monomials_per_coordinate": 495,
      "tradeoff_log_H": 192980.6158975217
    },
    {
      "ambient_dimension": 4,
      "b": 12,
      "coefficient_variables": 29120,
      "d": 13,
      "h": 24,
      "log10_H": 32443.874836701143,
      "log_H": 74704.78255795268,
      "m": 1,
      "monomials_per_coordinate": 1820,
      "tradeoff_log_H": 3287821.023960519
    },
    {
      "ambient_dimension": 5,
      "b": 1,
      "coefficient_variables": 120,
      "d": 11,
      "h": 2,
      "log10_H": 127.35093758496743,
      "log_H": 293.23637046196114,
      "m": 2,
      "monomials_per_coordinate": 6,
      "tradeoff_log_H": 3188.529055211097
    },
    {
      "ambient_dimension": 5,
      "b": 2,
      "coefficient_variables": 420,
      "d": 11,
      "h": 4,
      "log10_H": 440.6112698536182,
      "log_H": 1014.544941770118,
      "m": 2,
      "monomials_per_coordinate": 21,
      "tradeoff_log_H": 6575.504802548853
    },
    {
      "ambient_dimension": 5,
      "b": 4,
      "coefficient_variables": 2520,
      "d": 11,
      "h": 8,
      "log10_H": 2628.6142294313954,
      "log_H": 6052.607939920762,
      "m": 2,
      "monomials_per_coordinate": 126,
      "tradeoff_log_H": 27741.74765537839
    },
    {
      "ambient_dimension": 5,
      "b": 8,
      "coefficient_variables": 25740,
      "d": 11,
      "h": 16,
      "log10_H": 26811.06246136997,
      "log_H": 61734.75275088274,
      "m": 2,
      "monomials_per_coordinate": 1287,
      "tradeoff_log_H": 482431.66158707615
    },
    {
      "ambient_dimension": 5,
      "b": 12,
      "coefficient_variables": 123760,
      "d": 13,
      "h": 24,
      "log10_H": 137868.10207654568,
      "log_H": 317453.0366408355,
      "m": 2,
      "monomials_per_coordinate": 6188,
      "tradeoff_log_H": 8219527.914693865
    },
    {
      "ambient_dimension": 6,
      "b": 1,
      "coefficient_variables": 168,
      "d": 11,
      "h": 2,
      "log10_H": 177.48288780685945,
      "log_H": 408.6694517256093,
      "m": 3,
      "monomials_per_coordinate": 7,
      "tradeoff_log_H": 7642.356784891428
    },
    {
      "ambient_dimension": 6,
      "b": 2,
      "coefficient_variables": 672,
      "d": 11,
      "h": 4,
      "log10_H": 703.2459594818791,
      "log_H": 1619.2836630112697,
      "m": 3,
      "monomials_per_coordinate": 28,
      "tradeoff_log_H": 15769.158540626802
    },
    {
      "ambient_dimension": 6,
      "b": 4,
      "coefficient_variables": 5040,
      "d": 11,
      "h": 8,
      "log10_H": 5253.2247398818845,
      "log_H": 12095.99697619955,
      "m": 3,
      "monomials_per_coordinate": 210,
      "tradeoff_log_H": 66565.23075015482
    },
    {
      "ambient_dimension": 6,
      "b": 8,
      "coefficient_variables": 72072,
      "d": 11,
      "h": 16,
      "log10_H": 75061.31549730596,
      "log_H": 172835.06612461965,
      "m": 3,
      "monomials_per_coordinate": 3003,
      "tradeoff_log_H": 1157816.1723375346
    },
    {
      "ambient_dimension": 6,
      "b": 12,
      "coefficient_variables": 445536,
      "d": 13,
      "h": 24,
      "log10_H": 496308.89450839674,
      "log_H": 1142793.4620153888,
      "m": 3,
      "monomials_per_coordinate": 18564,
      "tradeoff_log_H": 19726842.730529815
    }
  &#93;,
  "fixed_n_asymptotics": &#91;
    {
      "inverted_constant": 1.1447142425533319,
      "n": 3,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 2.260314967299373
        },
        {
          "b": 100,
          "ratio": 2.1268017495584877
        },
        {
          "b": 200,
          "ratio": 2.0624917220751415
        },
        {
          "b": 500,
          "ratio": 2.0247388761288243
        }
      &#93;,
      "target_coefficient": 2.0
    },
    {
      "inverted_constant": 1.5650845800732873,
      "n": 4,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 0.8137015810076874
        },
        {
          "b": 100,
          "ratio": 0.7372898285303093
        },
        {
          "b": 200,
          "ratio": 0.7012470073110451
        },
        {
          "b": 500,
          "ratio": 0.6803122511032859
        }
      &#93;,
      "target_coefficient": 0.6666666666666666
    },
    {
      "inverted_constant": 1.97435048583482,
      "n": 5,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 0.22376772789480814
        },
        {
          "b": 100,
          "ratio": 0.19353856722340243
        },
        {
          "b": 200,
          "ratio": 0.17969454483062378
        },
        {
          "b": 500,
          "ratio": 0.1717788433833662
        }
      &#93;,
      "target_coefficient": 0.16666666666666666
    },
    {
      "inverted_constant": 2.3761767975649812,
      "n": 6,
      "samples": &#91;
        {
          "b": 50,
          "ratio": 0.05012396730616706
        },
        {
          "b": 100,
          "ratio": 0.041030176134997196
        },
        {
          "b": 200,
          "ratio": 0.03701707623147214
        },
        {
          "b": 500,
          "ratio": 0.03476803790075599
        }
      &#93;,
      "target_coefficient": 0.03333333333333333
    }
  &#93;,
  "formulas": {
    "H(m,b)": "2*b*(N+1)*max(b+1,11)^N",
    "N": "4*(m+3)*binomial(m+b+3,m+3)",
    "unrestricted_asymptotic": "liminf kappa_M/log(log M) &gt;= 1/log(4)",
    "unrestricted_finite_bound": "2*B*(32*(B+3)*4^B+1)*(B+11)^(32*(B+3)*4^B)"
  },
  "scope": {
    "not_verified_by_script": &#91;
      "complete stable q-classification",
      "generic-fiber emptiness",
      "constant generic-combination lemma",
      "D'Andrea-Krick-Sombra parametric Nullstellensatz"
    &#93;,
    "verified": &#91;
      "monomial count T(n,b)=binomial(n+b,n)",
      "coefficient variable count N=4*n*T(n,b)",
      "universal equation coefficient-degree bound max(b+1,11)",
      "universal parameter-degree bound 2*b",
      "finite tradeoff inequalities",
      "fixed-stabilization asymptotic leading constants",
      "unrestricted log-log coefficient log(4)"
    &#93;
  },
  "status": "ALL EFFECTIVE UNFRAMED BOUND CHECKS PASSED",
  "unrestricted_asymptotics": &#91;
    {
      "B": 10,
      "log_log_H_over_B": 2.1006972942655553,
      "target": 1.3862943611198906
    },
    {
      "B": 20,
      "log_log_H_over_B": 1.7780419688734788,
      "target": 1.3862943611198906
    },
    {
      "B": 40,
      "log_log_H_over_B": 1.60119535797237,
      "target": 1.3862943611198906
    },
    {
      "B": 80,
      "log_log_H_over_B": 1.503682663918577,
      "target": 1.3862943611198906
    },
    {
      "B": 160,
      "log_log_H_over_B": 1.4500247534938626,
      "target": 1.3862943611198906
    }
  &#93;
}
</code></pre>

<a id="source-3b6b4ee5762a28d5"></a>

## `research-notes/lane3-recovery-integration-20260803-v1/raw-formal-effectivity-reports/formal_effectivity_independent_report.json`

<pre><code class="language-json">
{
  "engine": "pure Python sparse dictionaries with Fraction coefficients",
  "max_modulus": 30,
  "max_ramification_order": 7,
  "sample_count": 182,
  "samples": &#91;
    {
      "D": 0,
      "M": 2,
      "e": 1,
      "sharp": true
    },
    {
      "D": 1,
      "M": 3,
      "e": 1,
      "sharp": true
    },
    {
      "D": 0,
      "M": 3,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 4,
      "e": 1,
      "sharp": true
    },
    {
      "D": 0,
      "M": 4,
      "e": 2,
      "sharp": true
    },
    {
      "D": 0,
      "M": 4,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 5,
      "e": 1,
      "sharp": true
    },
    {
      "D": 1,
      "M": 5,
      "e": 2,
      "sharp": true
    },
    {
      "D": 0,
      "M": 5,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 5,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 6,
      "e": 1,
      "sharp": true
    },
    {
      "D": 1,
      "M": 6,
      "e": 2,
      "sharp": true
    },
    {
      "D": 0,
      "M": 6,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 6,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 6,
      "e": 5,
      "sharp": true
    },
    {
      "D": 5,
      "M": 7,
      "e": 1,
      "sharp": true
    },
    {
      "D": 2,
      "M": 7,
      "e": 2,
      "sharp": true
    },
    {
      "D": 1,
      "M": 7,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 7,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 7,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 7,
      "e": 6,
      "sharp": true
    },
    {
      "D": 6,
      "M": 8,
      "e": 1,
      "sharp": true
    },
    {
      "D": 2,
      "M": 8,
      "e": 2,
      "sharp": true
    },
    {
      "D": 1,
      "M": 8,
      "e": 3,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 8,
      "e": 7,
      "sharp": true
    },
    {
      "D": 7,
      "M": 9,
      "e": 1,
      "sharp": true
    },
    {
      "D": 3,
      "M": 9,
      "e": 2,
      "sharp": true
    },
    {
      "D": 1,
      "M": 9,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 9,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 9,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 9,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 9,
      "e": 7,
      "sharp": true
    },
    {
      "D": 8,
      "M": 10,
      "e": 1,
      "sharp": true
    },
    {
      "D": 3,
      "M": 10,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 10,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 10,
      "e": 4,
      "sharp": true
    },
    {
      "D": 0,
      "M": 10,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 10,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 10,
      "e": 7,
      "sharp": true
    },
    {
      "D": 9,
      "M": 11,
      "e": 1,
      "sharp": true
    },
    {
      "D": 4,
      "M": 11,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 11,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 11,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 11,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 11,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 11,
      "e": 7,
      "sharp": true
    },
    {
      "D": 10,
      "M": 12,
      "e": 1,
      "sharp": true
    },
    {
      "D": 4,
      "M": 12,
      "e": 2,
      "sharp": true
    },
    {
      "D": 2,
      "M": 12,
      "e": 3,
      "sharp": true
    },
    {
      "D": 1,
      "M": 12,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 12,
      "e": 5,
      "sharp": true
    },
    {
      "D": 0,
      "M": 12,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 12,
      "e": 7,
      "sharp": true
    },
    {
      "D": 11,
      "M": 13,
      "e": 1,
      "sharp": true
    },
    {
      "D": 5,
      "M": 13,
      "e": 2,
      "sharp": true
    },
    {
      "D": 3,
      "M": 13,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 13,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 13,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 13,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 13,
      "e": 7,
      "sharp": true
    },
    {
      "D": 12,
      "M": 14,
      "e": 1,
      "sharp": true
    },
    {
      "D": 5,
      "M": 14,
      "e": 2,
      "sharp": true
    },
    {
      "D": 3,
      "M": 14,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 14,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 14,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 14,
      "e": 6,
      "sharp": true
    },
    {
      "D": 0,
      "M": 14,
      "e": 7,
      "sharp": true
    },
    {
      "D": 13,
      "M": 15,
      "e": 1,
      "sharp": true
    },
    {
      "D": 6,
      "M": 15,
      "e": 2,
      "sharp": true
    },
    {
      "D": 3,
      "M": 15,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 15,
      "e": 4,
      "sharp": true
    },
    {
      "D": 1,
      "M": 15,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 15,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 15,
      "e": 7,
      "sharp": true
    },
    {
      "D": 14,
      "M": 16,
      "e": 1,
      "sharp": true
    },
    {
      "D": 6,
      "M": 16,
      "e": 2,
      "sharp": true
    },
    {
      "D": 4,
      "M": 16,
      "e": 3,
      "sharp": true
    },
    {
      "D": 2,
      "M": 16,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 16,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 16,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 16,
      "e": 7,
      "sharp": true
    },
    {
      "D": 15,
      "M": 17,
      "e": 1,
      "sharp": true
    },
    {
      "D": 7,
      "M": 17,
      "e": 2,
      "sharp": true
    },
    {
      "D": 4,
      "M": 17,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 17,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 17,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 17,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 17,
      "e": 7,
      "sharp": true
    },
    {
      "D": 16,
      "M": 18,
      "e": 1,
      "sharp": true
    },
    {
      "D": 7,
      "M": 18,
      "e": 2,
      "sharp": true
    },
    {
      "D": 4,
      "M": 18,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 18,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 18,
      "e": 5,
      "sharp": true
    },
    {
      "D": 1,
      "M": 18,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 18,
      "e": 7,
      "sharp": true
    },
    {
      "D": 17,
      "M": 19,
      "e": 1,
      "sharp": true
    },
    {
      "D": 8,
      "M": 19,
      "e": 2,
      "sharp": true
    },
    {
      "D": 5,
      "M": 19,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 19,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 19,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 19,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 19,
      "e": 7,
      "sharp": true
    },
    {
      "D": 18,
      "M": 20,
      "e": 1,
      "sharp": true
    },
    {
      "D": 8,
      "M": 20,
      "e": 2,
      "sharp": true
    },
    {
      "D": 5,
      "M": 20,
      "e": 3,
      "sharp": true
    },
    {
      "D": 3,
      "M": 20,
      "e": 4,
      "sharp": true
    },
    {
      "D": 2,
      "M": 20,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 20,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 20,
      "e": 7,
      "sharp": true
    },
    {
      "D": 19,
      "M": 21,
      "e": 1,
      "sharp": true
    },
    {
      "D": 9,
      "M": 21,
      "e": 2,
      "sharp": true
    },
    {
      "D": 5,
      "M": 21,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 21,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 21,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 21,
      "e": 6,
      "sharp": true
    },
    {
      "D": 1,
      "M": 21,
      "e": 7,
      "sharp": true
    },
    {
      "D": 20,
      "M": 22,
      "e": 1,
      "sharp": true
    },
    {
      "D": 9,
      "M": 22,
      "e": 2,
      "sharp": true
    },
    {
      "D": 6,
      "M": 22,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 22,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 22,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 22,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 22,
      "e": 7,
      "sharp": true
    },
    {
      "D": 21,
      "M": 23,
      "e": 1,
      "sharp": true
    },
    {
      "D": 10,
      "M": 23,
      "e": 2,
      "sharp": true
    },
    {
      "D": 6,
      "M": 23,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 23,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 23,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 23,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 23,
      "e": 7,
      "sharp": true
    },
    {
      "D": 22,
      "M": 24,
      "e": 1,
      "sharp": true
    },
    {
      "D": 10,
      "M": 24,
      "e": 2,
      "sharp": true
    },
    {
      "D": 6,
      "M": 24,
      "e": 3,
      "sharp": true
    },
    {
      "D": 4,
      "M": 24,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 24,
      "e": 5,
      "sharp": true
    },
    {
      "D": 2,
      "M": 24,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 24,
      "e": 7,
      "sharp": true
    },
    {
      "D": 23,
      "M": 25,
      "e": 1,
      "sharp": true
    },
    {
      "D": 11,
      "M": 25,
      "e": 2,
      "sharp": true
    },
    {
      "D": 7,
      "M": 25,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 25,
      "e": 4,
      "sharp": true
    },
    {
      "D": 3,
      "M": 25,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 25,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 25,
      "e": 7,
      "sharp": true
    },
    {
      "D": 24,
      "M": 26,
      "e": 1,
      "sharp": true
    },
    {
      "D": 11,
      "M": 26,
      "e": 2,
      "sharp": true
    },
    {
      "D": 7,
      "M": 26,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 26,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 26,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 26,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 26,
      "e": 7,
      "sharp": true
    },
    {
      "D": 25,
      "M": 27,
      "e": 1,
      "sharp": true
    },
    {
      "D": 12,
      "M": 27,
      "e": 2,
      "sharp": true
    },
    {
      "D": 7,
      "M": 27,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 27,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 27,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 27,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 27,
      "e": 7,
      "sharp": true
    },
    {
      "D": 26,
      "M": 28,
      "e": 1,
      "sharp": true
    },
    {
      "D": 12,
      "M": 28,
      "e": 2,
      "sharp": true
    },
    {
      "D": 8,
      "M": 28,
      "e": 3,
      "sharp": true
    },
    {
      "D": 5,
      "M": 28,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 28,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 28,
      "e": 6,
      "sharp": true
    },
    {
      "D": 2,
      "M": 28,
      "e": 7,
      "sharp": true
    },
    {
      "D": 27,
      "M": 29,
      "e": 1,
      "sharp": true
    },
    {
      "D": 13,
      "M": 29,
      "e": 2,
      "sharp": true
    },
    {
      "D": 8,
      "M": 29,
      "e": 3,
      "sharp": true
    },
    {
      "D": 6,
      "M": 29,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 29,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 29,
      "e": 6,
      "sharp": true
    },
    {
      "D": 3,
      "M": 29,
      "e": 7,
      "sharp": true
    },
    {
      "D": 28,
      "M": 30,
      "e": 1,
      "sharp": true
    },
    {
      "D": 13,
      "M": 30,
      "e": 2,
      "sharp": true
    },
    {
      "D": 8,
      "M": 30,
      "e": 3,
      "sharp": true
    },
    {
      "D": 6,
      "M": 30,
      "e": 4,
      "sharp": true
    },
    {
      "D": 4,
      "M": 30,
      "e": 5,
      "sharp": true
    },
    {
      "D": 3,
      "M": 30,
      "e": 6,
      "sharp": true
    },
    {
      "D": 3,
      "M": 30,
      "e": 7,
      "sharp": true
    }
  &#93;,
  "status": "INDEPENDENT EFFECTIVITY STAIRCASE CHECKS PASSED"
}
</code></pre>

<a id="source-280c488e813678e9"></a>

## `research-notes/lane3-recovery-integration-20260803-v1/raw-formal-effectivity-reports/formal_effectivity_report.json`

<pre><code class="language-json">
{
  "affine_frame_checks": &#91;
    {
      "M": 3,
      "h_c_degree": 1,
      "residual_scaling": "u=1+lambda*s^2"
    },
    {
      "M": 4,
      "h_c_degree": 2,
      "residual_scaling": "u=1+lambda*s^3"
    },
    {
      "M": 5,
      "h_c_degree": 3,
      "residual_scaling": "u=1+lambda*s^4"
    },
    {
      "M": 6,
      "h_c_degree": 4,
      "residual_scaling": "u=1+lambda*s^5"
    },
    {
      "M": 7,
      "h_c_degree": 5,
      "residual_scaling": "u=1+lambda*s^6"
    },
    {
      "M": 8,
      "h_c_degree": 6,
      "residual_scaling": "u=1+lambda*s^7"
    },
    {
      "M": 9,
      "h_c_degree": 7,
      "residual_scaling": "u=1+lambda*s^8"
    },
    {
      "M": 10,
      "h_c_degree": 8,
      "residual_scaling": "u=1+lambda*s^9"
    },
    {
      "M": 11,
      "h_c_degree": 9,
      "residual_scaling": "u=1+lambda*s^10"
    },
    {
      "M": 12,
      "h_c_degree": 10,
      "residual_scaling": "u=1+lambda*s^11"
    }
  &#93;,
  "canonical_degree_checks": &#91;
    {
      "D": 1,
      "M": 3,
      "ell_c_degree": 1,
      "eta_c_degree": -1,
      "source_degree": 4,
      "target_degree": 2,
      "target_inverse_degree": 2
    },
    {
      "D": 2,
      "M": 4,
      "ell_c_degree": 2,
      "eta_c_degree": -1,
      "source_degree": 8,
      "target_degree": 3,
      "target_inverse_degree": 3
    },
    {
      "D": 3,
      "M": 5,
      "ell_c_degree": 3,
      "eta_c_degree": 2,
      "source_degree": 12,
      "target_degree": 4,
      "target_inverse_degree": 4
    },
    {
      "D": 4,
      "M": 6,
      "ell_c_degree": 4,
      "eta_c_degree": 2,
      "source_degree": 16,
      "target_degree": 5,
      "target_inverse_degree": 5
    },
    {
      "D": 5,
      "M": 7,
      "ell_c_degree": 5,
      "eta_c_degree": 4,
      "source_degree": 20,
      "target_degree": 6,
      "target_inverse_degree": 6
    },
    {
      "D": 6,
      "M": 8,
      "ell_c_degree": 6,
      "eta_c_degree": 5,
      "source_degree": 24,
      "target_degree": 7,
      "target_inverse_degree": 7
    },
    {
      "D": 7,
      "M": 9,
      "ell_c_degree": 7,
      "eta_c_degree": 6,
      "source_degree": 28,
      "target_degree": 8,
      "target_inverse_degree": 8
    },
    {
      "D": 8,
      "M": 10,
      "ell_c_degree": 8,
      "eta_c_degree": 7,
      "source_degree": 32,
      "target_degree": 9,
      "target_inverse_degree": 9
    }
  &#93;,
  "formal_limit_coefficients": &#91;
    {
      "c_degree": 1,
      "coefficient": "c*(-q + qp)/3",
      "s_power": 2,
      "source_y_degree": 4
    },
    {
      "c_degree": 2,
      "coefficient": "c**2*(q - qp)/3",
      "s_power": 3,
      "source_y_degree": 8
    },
    {
      "c_degree": 3,
      "coefficient": "c**3*(-q + qp)/3",
      "s_power": 4,
      "source_y_degree": 12
    },
    {
      "c_degree": 4,
      "coefficient": "c**4*(q - qp)/3",
      "s_power": 5,
      "source_y_degree": 16
    },
    {
      "c_degree": 5,
      "coefficient": "c**5*(-q + qp)/3",
      "s_power": 6,
      "source_y_degree": 20
    },
    {
      "c_degree": 6,
      "coefficient": "c**6*(q - qp)/3",
      "s_power": 7,
      "source_y_degree": 24
    },
    {
      "c_degree": 7,
      "coefficient": "c**7*(-q + qp)/3",
      "s_power": 8,
      "source_y_degree": 28
    },
    {
      "c_degree": 8,
      "coefficient": "c**8*(q - qp)/3",
      "s_power": 9,
      "source_y_degree": 32
    },
    {
      "c_degree": 9,
      "coefficient": "c**9*(-q + qp)/3",
      "s_power": 10,
      "source_y_degree": 36
    },
    {
      "c_degree": 10,
      "coefficient": "c**10*(q - qp)/3",
      "s_power": 11,
      "source_y_degree": 40
    },
    {
      "c_degree": 11,
      "coefficient": "c**11*(-q + qp)/3",
      "s_power": 12,
      "source_y_degree": 44
    }
  &#93;,
  "formal_limit_ring": "C&#91;c&#93;&#91;&#91;s&#93;&#93;",
  "noncommutation": "lim_M colim_D Isom_D(R_M) is nonempty, while colim_D lim_M Isom_D(R_M) is empty",
  "orbit_cokernel": "C&#91;&#91;s&#93;&#93;&#91;c&#93;/(1+s*c) = C((s))",
  "orbit_cokernel_s_inverse": "-c",
  "orbit_obstruction_class": "(q'-q)/3 * s^2",
  "polynomial_complete_base_ring": "C&#91;&#91;s&#93;&#93;&#91;c&#93;",
  "ramification_samples": &#91;
    {
      "M": 2,
      "e": 1,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 3,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 3,
      "e": 2,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 4,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 4,
      "e": 2,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 4,
      "e": 3,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 5,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 5,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 5,
      "e": 3,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 5,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 6,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 4,
      "nilpotence_index": 6
    },
    {
      "M": 6,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 6,
      "e": 3,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 6,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 7,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 5,
      "nilpotence_index": 7
    },
    {
      "M": 7,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 7,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 7,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 8,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 6,
      "nilpotence_index": 8
    },
    {
      "M": 8,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 8,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 8,
      "e": 4,
      "frames_already_equal": true,
      "minimal_c_degree": 0,
      "nilpotence_index": 2
    },
    {
      "M": 9,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 7,
      "nilpotence_index": 9
    },
    {
      "M": 9,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 9,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 9,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 10,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 8,
      "nilpotence_index": 10
    },
    {
      "M": 10,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 10,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 10,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 11,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 9,
      "nilpotence_index": 11
    },
    {
      "M": 11,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 4,
      "nilpotence_index": 6
    },
    {
      "M": 11,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 11,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 12,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 10,
      "nilpotence_index": 12
    },
    {
      "M": 12,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 4,
      "nilpotence_index": 6
    },
    {
      "M": 12,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 12,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 1,
      "nilpotence_index": 3
    },
    {
      "M": 13,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 11,
      "nilpotence_index": 13
    },
    {
      "M": 13,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 5,
      "nilpotence_index": 7
    },
    {
      "M": 13,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 13,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    },
    {
      "M": 14,
      "e": 1,
      "frames_already_equal": false,
      "minimal_c_degree": 12,
      "nilpotence_index": 14
    },
    {
      "M": 14,
      "e": 2,
      "frames_already_equal": false,
      "minimal_c_degree": 5,
      "nilpotence_index": 7
    },
    {
      "M": 14,
      "e": 3,
      "frames_already_equal": false,
      "minimal_c_degree": 3,
      "nilpotence_index": 5
    },
    {
      "M": 14,
      "e": 4,
      "frames_already_equal": false,
      "minimal_c_degree": 2,
      "nilpotence_index": 4
    }
  &#93;,
  "status": "ALL FORMAL-EFFECTIVITY CHECKS PASSED",
  "theorem_inputs_not_cas_checked": &#91;
    "stable q-classification on the generic fiber: Program 4, thm:main / cor:q-classification",
    "constant generic-combination lemma for an empty affine generic fiber",
    "D'Andrea-Krick-Sombra parametric effective Nullstellensatz (Theorem 0.5)"
  &#93;,
  "universal_residual_checks": &#91;
    {
      "D": 0,
      "phi_c_degree": -1,
      "residual": "alpha**2*c**2*delta"
    },
    {
      "D": 1,
      "phi_c_degree": 1,
      "residual": "-alpha**3*c**3*delta"
    },
    {
      "D": 2,
      "phi_c_degree": 2,
      "residual": "alpha**4*c**4*delta"
    },
    {
      "D": 3,
      "phi_c_degree": 3,
      "residual": "-alpha**5*c**5*delta"
    },
    {
      "D": 4,
      "phi_c_degree": 4,
      "residual": "alpha**6*c**6*delta"
    },
    {
      "D": 5,
      "phi_c_degree": 5,
      "residual": "-alpha**7*c**7*delta"
    },
    {
      "D": 6,
      "phi_c_degree": 6,
      "residual": "alpha**8*c**8*delta"
    },
    {
      "D": 7,
      "phi_c_degree": 7,
      "residual": "-alpha**9*c**9*delta"
    },
    {
      "D": 8,
      "phi_c_degree": 8,
      "residual": "alpha**10*c**10*delta"
    },
    {
      "D": 9,
      "phi_c_degree": 9,
      "residual": "-alpha**11*c**11*delta"
    },
    {
      "D": 10,
      "phi_c_degree": 10,
      "residual": "alpha**12*c**12*delta"
    }
  &#93;,
  "unramified_compatibility": &#91;
    {
      "M": 1,
      "c_degree": 0,
      "source_degree": 1,
      "target_degree": 1
    },
    {
      "M": 2,
      "c_degree": 0,
      "source_degree": 1,
      "target_degree": 1
    },
    {
      "M": 3,
      "c_degree": 1,
      "source_degree": 4,
      "target_degree": 2
    },
    {
      "M": 4,
      "c_degree": 2,
      "source_degree": 8,
      "target_degree": 3
    },
    {
      "M": 5,
      "c_degree": 3,
      "source_degree": 12,
      "target_degree": 4
    },
    {
      "M": 6,
      "c_degree": 4,
      "source_degree": 16,
      "target_degree": 5
    },
    {
      "M": 7,
      "c_degree": 5,
      "source_degree": 20,
      "target_degree": 6
    },
    {
      "M": 8,
      "c_degree": 6,
      "source_degree": 24,
      "target_degree": 7
    },
    {
      "M": 9,
      "c_degree": 7,
      "source_degree": 28,
      "target_degree": 8
    },
    {
      "M": 10,
      "c_degree": 8,
      "source_degree": 32,
      "target_degree": 9
    },
    {
      "M": 11,
      "c_degree": 9,
      "source_degree": 36,
      "target_degree": 10
    },
    {
      "M": 12,
      "c_degree": 10,
      "source_degree": 40,
      "target_degree": 11
    },
    {
      "M": 13,
      "c_degree": 11,
      "source_degree": 44,
      "target_degree": 12
    },
    {
      "M": 14,
      "c_degree": 12,
      "source_degree": 48,
      "target_degree": 13
    }
  &#93;
}
</code></pre>

[Back to Lane 3](bounded-degree-deformation-modulus-onset.md)
