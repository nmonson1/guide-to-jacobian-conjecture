# Lane 5 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`research-notes/finite-diagnostics-20260803-v1/verify_lane5_encoded_shear_packet.py`](#source-900f6bbe0a61079a) — `553f4bed9eae63afbfbf5a60354fbd89615f27da0ef3fde11226ccfad15d8493`
- [`research-notes/lane5-degree-budgets/README.md`](#source-150c519812fd742b) — `2c8f21c6c8f232976c8c563ce75efd4f1fcb5eb1c5ecb64239486c09c6be79c9`
- [`research-notes/lane5-degree-budgets/REDUCED_WORD_SEPARATION.md`](#source-3792ba2683f7331e) — `944ca8d8144b39dbf4a4c8ea7300c23bba8d45d92fd02ae70120185c3ffdfad9`
- [`research-notes/lane5-degree-budgets/all_elementary_monomial_shears.json`](#source-d6911ca72194f23a) — `4d169769582009f33ddf58430621cc0bd61a6d65262904a26e282d891c4e809c`
- [`research-notes/lane5-degree-budgets/all_elementary_monomial_shears.py`](#source-475f7fcdbf33aece) — `fa003e761302e6a84c8988fe96d29523959a3e4418759c6482e5c014fc85794c`
- [`research-notes/lane5-degree-budgets/coefficient_transport.md`](#source-e9c67bd9a2c5c268) — `97fde970df9d4e74b29bdaf605b7019b4d9271a81825db329155dbe0a26e77f5`
- [`research-notes/lane5-degree-budgets/elementary_shear_scan.json`](#source-f1c107cd6dee57ee) — `a5a02b00fdd1bd489fb5f4e4b5c870a681c728c13f2e6724ea960f37228bf906`
- [`research-notes/lane5-degree-budgets/elementary_shear_scan.py`](#source-23231a729cc074f2) — `9c1ce67f17b0411705857e581a43cc381df2b3a6e3f2e60adce6065bb804ede8`
- [`research-notes/lane5-degree-budgets/lacunary_polynomial_shears.md`](#source-8af47f98c4f1d666) — `9d154fa986ada4d976317369050a41978d1e41ef9171e5b0945c92e273eab334`
- [`research-notes/lane5-degree-budgets/lacunary_polynomial_shears.py`](#source-2fa4afdcfe7a66d7) — `0bc025fe73e78ca1fb10b37d60ab2b7ffecccea9d5fd9e76b590f349f45f9eee`
- [`research-notes/lane5-degree-budgets/one_sided_high_weight_compositions.md`](#source-7decd4931d041216) — `43d406b08a45c66ad8fae7ea3a4fa4d42ceca361bb7213e78d831055d82581cd`
- [`research-notes/lane5-degree-budgets/one_sided_high_weight_semigroup.md`](#source-8f65f57cf63282ce) — `e8d98c34261b506290dd7dec55fddf1feda32f0fb5dce0eb6e8eb57a7dad81ae`
- [`research-notes/lane5-degree-budgets/reduced_word_separation.output.json`](#source-a1f41387252fe775) — `1c1d623ccb44b101994bc5f12b33bfed8fe7f25778f8171a462d95f1d7f35f55`
- [`research-notes/lane5-degree-budgets/resonant_weight_certificate.json`](#source-9a583e6f9c47abec) — `4a805712a1208ce0c79e595ae56effc797efd1c6507fe78be94f007b9983af48`
- [`research-notes/lane5-degree-budgets/resonant_weight_certificate.py`](#source-2763d2393fd2e4b7) — `4e5c5d517619af4804a6754370eac764eced54ce6177a6003037489eb53f1877`
- [`research-notes/lane5-degree-budgets/standard_filtration_certificate.json`](#source-5dd4e35e012d9761) — `280a87b4ffb84579c56b71aec95d09e9345becc38a66a0b1ec197b0ce9d4a8fb`
- [`research-notes/lane5-degree-budgets/standard_filtration_certificate.py`](#source-c9dee41efc8efea6) — `942e3ff34aa09032ef70b410ebf6ee87595d0a4c2669ff48fdac3f2f917fb9df`
- [`research-notes/lane5-degree-budgets/verify_baseline_counterexample.py`](#source-9ec82063f46b1a95) — `e1e56a2e73fb485bc3e9345429bc24a11bb8c72b833d849d323b3dc8303efb09`
- [`research-notes/lane5-degree-budgets/verify_reduced_word_separation.py`](#source-b547c1e19853a679) — `1c4995c43f7bb50a46381abd205192e1191c962c2a13be0c6f4d33aeb5c5b2e9`

<a id="source-900f6bbe0a61079a"></a>

## `research-notes/finite-diagnostics-20260803-v1/verify_lane5_encoded_shear_packet.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Aggregate the bounded exact Lane 5 encoded-shear diagnostics."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents&#91;2&#93;
PACKET = ROOT / "research-notes/lane5-degree-budgets"
PROGRAMS = (
    "all_elementary_monomial_shears.py",
    "verify_reduced_word_separation.py",
    "lacunary_polynomial_shears.py",
)


def run_json(name: str) -&gt; tuple&#91;dict&#91;str, object&#93;, str&#93;:
    path = PACKET / name
    run = subprocess.run(
        &#91;sys.executable, str(path)&#93;,
        cwd=PACKET,
        check=False,
        capture_output=True,
        text=True,
    )
    if run.returncode != 0:
        raise AssertionError(f"{name} failed:\n{run.stdout}{run.stderr}")
    return json.loads(run.stdout), hashlib.sha256(path.read_bytes()).hexdigest()


def main() -&gt; int:
    records = {name: run_json(name) for name in PROGRAMS}
    elementary = records&#91;PROGRAMS&#91;0&#93;&#93;&#91;0&#93;
    reduced = records&#91;PROGRAMS&#91;1&#93;&#93;&#91;0&#93;
    lacunary = records&#91;PROGRAMS&#91;2&#93;&#93;&#91;0&#93;
    if elementary.get("status") != "pass" or elementary.get("finite_case_count") != 81:
        raise AssertionError("all-elementary certificate changed")
    if elementary.get("finite_rank_82_cases") != 10:
        raise AssertionError("rank-82 elementary case count changed")
    if elementary.get("finite_rank_83_cases") != 71:
        raise AssertionError("rank-83 elementary case count changed")
    if reduced.get("status") != "pass" or reduced.get("weight_width") != 18:
        raise AssertionError("reduced-word certificate changed")
    if lacunary.get("status") != "pass" or lacunary.get("weight_width") != 18:
        raise AssertionError("lacunary-tail certificate changed")

    result = {
        "schema_version": 1,
        "name": "Lane 5 finite encoded shear enumeration",
        "status": "pass",
        "source_sha256": {name: records&#91;name&#93;&#91;1&#93; for name in PROGRAMS},
        "elementary_monomial_shears": {
            "finite_cases": 81,
            "rank_82_cases": 10,
            "rank_83_cases": 71,
            "resonant_minor_count": elementary&#91;"resonant"&#93;&#91;"minor_count"&#93;,
            "all_exponents_closed_by_weight_tails": True,
        },
        "separated_words": {
            "weight_width": reduced&#91;"weight_width"&#93;,
            "nested_example": reduced&#91;"nested_example"&#93;,
            "arbitrary_length_example": reduced&#91;"arbitrary_length_example"&#93;,
        },
        "does_not_establish": &#91;
            "the missing full semidegree-normalization group",
            "all resonant mixed-sign alternating words",
            "a statement for wild source automorphisms",
            "left--right or stable invariance of the degree-six filtration",
        &#93;,
        "failed_large_job_policy": (
            "No 8-CPU/96-GB search was rerun; this packet replays the distinct finite "
            "81-case enumeration and structural exact word certificates."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result&#91;"certificate_sha256"&#93; = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-150c519812fd742b"></a>

## `research-notes/lane5-degree-budgets/README.md`

<pre><code class="language-markdown">
# Lane 5 degree-six filtration and elementary-shear theorems

This directory studies the displayed three-variable Keller map

```text
A0 = 1 + x*y
P  = A0^3*z + y^2*A0*(4+3*x*y)
Q  = y + 3*x*A0^2*z + 3*x*y^2*(4+3*x*y)
R  = 2*x - 3*x^2*y - x^3*z
```

and the embedded algebra `S=k&#91;P,Q,R&#93;` inside `B=k&#91;x,y,z&#93;`, over a
characteristic-zero field.

The results below concern degree at most six. They do not yet cover arbitrary
mixed-sign compositions or wild source automorphisms.

## Theorem A: standard and affine source coordinates

In the displayed coordinates,

```text
S intersect B_{&lt;=6} = span_k{1,Q,R}.
```

Consequently

```text
k&#91;S intersect B_{&lt;=6}&#93; = k&#91;Q,R&#93;,
```

which has transcendence degree two.

Every affine source automorphism preserves `B_{&lt;=6}`. Therefore, for every
affine automorphism `L`,

```text
L(S) intersect B_{&lt;=6} = span_k{1,L(Q),L(R)}.
```

The standard certificate uses all 84 source monomials of degree at most six
and 81 exact rational common-fiber difference rows. The selected `81 x 81`
minor is nonzero modulo `1000003`, with determinant `214012`. The exact kernel
vectors are `1`, `Q`, and `R`.

Replay:

```bash
python3 standard_filtration_certificate.py
```

## Theorem B: every single elementary monomial source shear

Let `i` and `j` be distinct source coordinates, let `N&gt;=2`, and let `c` be any
scalar. Define

```text
sigma(x_i) = x_i + c*x_j^N
```

and fix the third coordinate. Then

```text
sigma(S) intersect B_{&lt;=6}
```

is exactly:

```text
span{1,Q,R}              if c=0;

span{1,sigma(R)}         if c!=0 and deg sigma(R)&lt;=6;

k                         if c!=0 and deg sigma(R)&gt;6.
```

In particular, for every such shear,

```text
trdeg k&#91;sigma(S) intersect B_{&lt;=6}&#93; &lt;= 2,
```

and for every nontrivial shear the transcendence degree is at most one.
Therefore no single elementary monomial source shear can expose three
algebraically independent target functions of degree at most six.

The nonconstant cases are precisely

| Shear | Exponents retaining `sigma(R)` |
| --- | --- |
| `z -&gt; z+c*x^N` | `N=2,3` |
| `y -&gt; y+c*x^N` | `N=2,3,4` |
| `z -&gt; z+c*y^N` | `N=2,3` |
| `y -&gt; y+c*z^N` | `N=2,3,4` |

The two shears changing `x` always have intersection `k` when `c!=0`.

Replay the complete theorem with

```bash
python3 all_elementary_monomial_shears.py
```

The verifier checks 81 finite exponent/direction cases, the exact resonant
coefficient family, and the structural infinite tails.

## Proof architecture for Theorem B

### 1. Finite exact range

For coefficient one, exact rational common-fiber matrices certify all
exponents below the weight-separation thresholds:

```text
z+x^N:  2 &lt;= N &lt;= 16
y+x^N:  2 &lt;= N &lt;= 17
x+y^N:  2 &lt;= N &lt;= 17
z+y^N:  2 &lt;= N &lt;= 20
y+z^N:  2 &lt;= N &lt;= 9
x+z^N:  2 &lt;= N &lt;= 8
```

There are 81 cases. Ten have rank 82 and the displayed kernel
`span{1,sigma(R)}`; the other 71 have rank 83 and only constants in the
kernel. Every modular minor is backed by exact rational rows.

### 2. Torus-weight separation for every larger exponent

The source torus has weights

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2,
```

while `P,Q,R` have weights `2,1,-1`. The space `B_{&lt;=6}` has weights in
`&#91;-6,12&#93;`, of width 18.

Write a shear as `exp(cD)`, where `D=x_j^N partial_{x_i}` is a homogeneous
locally nilpotent derivation of weight `e`. If `|e|&gt;18` and

```text
g in exp(cD)(S) intersect B_{&lt;=6},
```

then `exp(-cD)g` belongs to the graded algebra `S`. Distinct terms
`D^m(g_w)` have distinct torus weights because the input weights differ by at
most 18 while each nonzero step changes weight by more than 18. Hence every
weight component `g_w` already lies in `S`. Theorem A gives

```text
g in span{1,Q,R}.
```

If the `Q` or `R` coefficient were nonzero, the same separated-weight
argument would force `D(Q)` or `D(R)` to lie in `S`.

The three points

```text
u = (-12,  1/11,  -8/11)
v = (-10,  1/11, -14/11)
w = ( 22, -1/22, 65/484)
```

all map to

```text
(P,Q,R) = (0,1/11,-1320).
```

Their exact derivative values show, for each of the six shear directions and
every exponent, that neither `D(Q)` nor `D(R)` is constant on this fiber.
Thus neither lies in `S`. Only constants survive.

The resulting sharp structural thresholds are

```text
z+x^N: N&gt;=17      y+x^N: N&gt;=18      x+y^N: N&gt;=18
z+y^N: N&gt;=21      y+z^N: N&gt;=10      x+z^N: N&gt;=9.
```

Together with the finite certificates, these cover every `N&gt;=2`.

### 3. All nonzero coefficients

Conjugation by the source torus rescales the coefficient of every elementary
monomial shear except

```text
z -&gt; z+c*y^2.
```

Thus, after extension to an algebraic closure, every nonzero coefficient in
the nonresonant cases is conjugate to coefficient one. The intersection
statement then descends to the original characteristic-zero field.

### 4. Exact resonant family

The shear `z -&gt; z+c*y^2` preserves the source torus grading. Split
`B_{&lt;=6}` into its 19 weight spaces. Each has dimension at most eight.

The file `resonant_weight_certificate.json` supplies 33 exact rational
determinantal minors. Their gcds in `Q&#91;c&#93;` are:

```text
1  in every weight except weight 1;
c  in weight 1.
```

The weight-zero kernel is always generated by `1`; the weight-minus-one
kernel is generated by

```text
sigma_c(R) = R - c*x^3*y^2.
```

At `c=0`, weight one additionally contains `Q`, as in Theorem A. At every
`c!=0`, its rank is full. Hence

```text
sigma_c(S) intersect B_{&lt;=6}
  = span{1,sigma_c(R)}
```

for every nonzero `c`, with no exceptional coefficients.

Replay this component alone with

```bash
python3 resonant_weight_certificate.py
```

## Theorem C: arbitrary one-sided high-weight source words

Let `U_+` be the semigroup generated by exponentials of homogeneous locally
nilpotent source derivations of torus weight at least `19`, and let `U_-` be
the corresponding semigroup of weights at most `-19`. Then, for every

```text
sigma in U_+ union U_-,
```

one has

```text
sigma(S) intersect B_{&lt;=6}
  subset span{1,Q,R}.
```

Thus the generated algebra has transcendence degree at most two. Word length,
coefficients, order, and coordinate direction are unrestricted, and the
factors need not commute.

The proof is a general weight-window lemma. If a graded subalgebra `A` is
acted on by a word of homogeneous locally nilpotent derivations whose weights
all exceed the width of a finite weight window on the same side, then every
nonzero derivative word leaves that window. For
`g in sigma(A) intersect V`, the in-window components of `sigma^(-1)(g)` are
therefore exactly the components of `g`; gradedness forces them into `A`.

The theorem covers arbitrary noncommuting words in the positive generators

```text
x -&gt; x+c*y^N,   N&gt;=18;
z -&gt; z+c*y^N,   N&gt;=21;
y -&gt; y+c*z^N,   N&gt;=10;
x -&gt; x+c*z^N,   N&gt;=9,
```

or arbitrary words in the negative generators

```text
z -&gt; z+c*x^N,   N&gt;=17;
y -&gt; y+c*x^N,   N&gt;=18.
```

It also permits arbitrary interleaving with the resonant weight-zero shears
`z -&gt; z+a*y^2`. After normal-ordering those factors to the right, the exact
resonant theorem gives transcendence degree at most two when the total
resonant parameter is zero and at most one otherwise. An arbitrary affine
source post-factor preserves all conclusions.

Complete proof:

```text
one_sided_high_weight_semigroup.md
```

This strictly extends the same-direction polynomial-tail theorem in
`lacunary_polynomial_shears.md`: noncommuting coordinate directions are now
allowed.

## Certificate and proof files

```text
standard_filtration_certificate.py
standard_filtration_certificate.json

elementary_shear_scan.py
elementary_shear_scan.json

resonant_weight_certificate.py
resonant_weight_certificate.json

all_elementary_monomial_shears.py
all_elementary_monomial_shears.json

lacunary_polynomial_shears.md
one_sided_high_weight_semigroup.md
```

The first pair proves Theorem A. The older bounded shear pair remains a compact
42-case checkpoint. The resonant pair proves the complete one-parameter
weight-preserving family. The all-elementary pair combines the expanded
81-case finite certificate with the weight-separation proof. The final two
notes prove same-direction and arbitrary-direction high-weight composition
theorems.

## Filtered differential obstruction

For an embedded inclusion `iota:A=k&#91;u1,u2,u3&#93; -&gt; B`, a source automorphism
`sigma`, and a degree bound `D`, set

```text
F_D^sigma A = {a in A : deg sigma(iota(a)) &lt;= D}.
```

For a basis `f1,...,fm`, define `J_D^sigma` as the ideal of the `3 x 3`
minors of

```text
(partial fi / partial uj).
```

This ideal is basis independent. In characteristic zero:

1. `J_D^sigma=0` exactly when the generated algebra has transcendence degree
   at most two.
2. If `F_D^sigma A` contains a polynomial coordinate frame, then
   `J_D^sigma=A`.
3. Therefore properness of `J_D^sigma` obstructs a degree-`D` target frame.

The elementary-shear theorem proves the stronger condition `J_6^sigma=0` for
every single elementary monomial source shear. Theorem C proves the same
condition for every one-sided high-weight source word.

## Structural limits

No exhaustive filtration of `k&#91;x1,x2,x3&#93;` by finite-dimensional vector spaces
can be literally invariant under every polynomial automorphism. If one finite
piece contains `x1`, invariance under

```text
x1 -&gt; x1+x2^N
```

would put all powers `x2^N` in that same piece.

Likewise, every degree budget obtained from a finite family of normalized
divisorial valuations is diluted to zero by triangular source shears. A
successful full-orbit theory must use a genuinely global boundary object, an
infinite valuation system, or a non-degree-increasing canonicalization.

The remaining Lane 5 gap is confined more sharply: it consists of nonlinear
words containing low-weight factors, mixed positive/negative high-weight
factors whose derivative weights can return to the degree-six window, and the
possible wild part of `Aut(k&#91;x,y,z&#93;)`.
</code></pre>

<a id="source-3792ba2683f7331e"></a>

## `research-notes/lane5-degree-budgets/REDUCED_WORD_SEPARATION.md`

<pre><code class="language-markdown">
# Reduced-word weight separation for Lane 5

## Setup

Let

\&#91;
B=k&#91;x,y,z&#93;,\qquad S=k&#91;P,Q,R&#93;\subset B,
\&#93;

where \(k\) has characteristic zero and

\&#91;
\begin{aligned}
P&amp;=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
Q&amp;=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
R&amp;=2x-3x^2y-x^3z.
\end{aligned}
\&#93;

Use the source-torus grading

\&#91;
w(x)=-1,\qquad w(y)=1,\qquad w(z)=2.
\&#93;

Then \(S\) is graded, with

\&#91;
w(P)=2,\qquad w(Q)=1,\qquad w(R)=-1,
\&#93;

and the exact standard-filtration certificate gives

\&#91;
S\cap B_{\le6}=\operatorname{span}_k\{1,Q,R\}.
\&#93;

A derivation \(\delta\) is **homogeneous of shift** \(d\) if
\(\delta(B_n)\subseteq B_{n+d}\) for every weight space \(B_n\).
Every monomial elementary derivation

\&#91;
\delta=c m\,\partial_{x_i},\qquad
m\in k&#91;x_j,x_k&#93;,
\&#93;

is locally nilpotent and homogeneous of shift

\&#91;
d=w(m)-w(x_i).
\&#93;

## Taylor no-return theorem

Let \(V\subseteq B\) be torus-stable and supported in a weight interval
\(&#91;a,b&#93;\) of width \(W=b-a\). Let \(C\subseteq B\) be a graded subalgebra,
let \(\delta_1,\ldots,\delta_t\) be homogeneous locally nilpotent derivations
of shifts \(d_1,\ldots,d_t\), and put

\&#91;
\Phi=\exp(\delta_t)\cdots\exp(\delta_1).
\&#93;

For this ordered word and this finite-dimensional \(V\), let
\(\mathcal A_V\subset\mathbf N^t\) be the finite set of multiindices
\(\alpha\) for which

\&#91;
\delta_1^{\alpha_1}\cdots\delta_t^{\alpha_t}
\&#93;

is nonzero on some element of \(V\). If

\&#91;
|\alpha\cdot d|&gt;W
\tag{1}
\&#93;

for every nonzero \(\alpha\in\mathcal A_V\), then

\&#91;
\boxed{\Phi(C)\cap V\subseteq C\cap V.}
\tag{2}
\&#93;

### Proof

Take \(h\in\Phi(C)\cap V\) and put \(g=\Phi^{-1}h\in C\). The ordered
Taylor expansion is finite:

\&#91;
g=\sum_{\alpha\in\mathcal A_V}
  \frac{(-1)^{|\alpha|}}{\alpha_1!\cdots\alpha_t!}
  \delta_1^{\alpha_1}\cdots\delta_t^{\alpha_t}h.
\tag{3}
\&#93;

The zero-multiindex term is \(h\), supported in \(&#91;a,b&#93;\). Every nonzero
\(\alpha\)-term is supported in the translated interval
\(&#91;a,b&#93;+\alpha\cdot d\), which is disjoint from \(&#91;a,b&#93;\) by (1). Hence the
weight components of \(g\) inside \(&#91;a,b&#93;\) are exactly the components of
\(h\). Since \(g\in C\) and \(C\) is graded, those components lie in \(C\),
so \(h\in C\cap V\). \(\square\)

This strictly extends the one-sided weight-window lemma: positive and negative
shifts may be mixed, provided no nonzero ordered Taylor word returns to the
original window.

The set \(\mathcal A_V\) is finite because \(V\) is finite dimensional and
the ordered derivations are locally nilpotent.

## Exactness under full Taylor separation

Assume now

\&#91;
C\cap B_{\le D}=k\oplus kq\oplus kr,
\&#93;

where \(q,r\) are homogeneous of distinct weights. Suppose the stronger
condition

\&#91;
| (\alpha-\beta)\cdot d |&gt;3D
\tag{4}
\&#93;

holds for every distinct \(\alpha,\beta\in\mathcal A_{B_{\le D}}\). If, for
some \(j\),

\&#91;
\delta_jq\notin C,\qquad \delta_jr\notin C,
\tag{5}
\&#93;

then

\&#91;
\boxed{\Phi(C)\cap B_{\le D}=k.}
\&#93;

Indeed, (4) separates every Taylor multiindex block in (3). Gradedness of
\(C\) puts each block in \(C\), including the zero block, so
\(h=a+bq+cr\). The \(e_j\)-block gives \(\delta_jh\in C\). Its
\(q\)- and \(r\)-parts have distinct weights, and (5) forces \(b=c=0\).

## Arbitrarily long commuting compositions with mixed signs

Fix one target coordinate \(x_i\). Let

\&#91;
\delta_r=c_r m_r\partial_{x_i}\qquad(1\le r\le t)
\&#93;

with \(c_r\ne0\), where each \(m_r\) is a monomial in the other two
coordinates. These derivations commute, and

\&#91;
\exp(\delta_t)\cdots\exp(\delta_1)
 =\exp\!\left(\sum_{r=1}^t\delta_r\right)
\&#93;

sends

\&#91;
x_i\longmapsto x_i+\sum_{r=1}^t c_rm_r.
\&#93;

On \(B_{\le D}\), only multiindices with \(|\alpha|\le D\) occur. Therefore
it is enough that

\&#91;
|\gamma\cdot d|&gt;3D
\tag{6}
\&#93;

for every nonzero \(\gamma\in\mathbf Z^t\) with
\(\|\gamma\|_1\le2D\). A convenient sufficient condition, after ordering the
shifts by construction, is

\&#91;
|d_1|&gt;3D,\qquad
|d_r|&gt;2D\sum_{s&lt;r}|d_s|+3D\quad(r\ge2).
\tag{7}
\&#93;

For Lane 5, the common-fiber witnesses from the pure-monomial theorem show
that \(m_r\partial_{x_i}Q\) and \(m_r\partial_{x_i}R\) are outside \(S\) for
every nonzero monomial in the other two source coordinates. Hence (6), or the
stronger condition (7), gives

\&#91;
\boxed{
\exp\!\left(\sum c_rm_r\partial_{x_i}\right)(S)\cap B_{\le6}=k.
}
\&#93;

This is especially useful for mixed positive/negative shift support, which is
not covered by the one-sided high-weight semigroup theorem.

For example, use the target coordinate \(y\). The shifts of
\(z^M\partial_y\) and \(x^N\partial_y\) are respectively \(2M-1\) and
\(-N-1\). The alternating superincreasing shifts

\&#91;
19,-247,3211,-41743
\&#93;

are realized by

\&#91;
y\longmapsto y+c_1z^{10}+c_2x^{246}+c_3z^{1606}+c_4x^{41742}.
\&#93;

For arbitrary nonzero coefficients, its transformed image algebra has only
constants in degree at most six. The construction continues to arbitrary word
length by the recurrence (7).

## A genuinely mixed-sign noncommuting family

Let

\&#91;
\delta_1=x^N\partial_y,\qquad
\delta_2=y^M\partial_z,
\&#93;

and

\&#91;
\Psi_{N,M}=\exp(\delta_1)\exp(\delta_2).
\&#93;

The derivations do not commute and have shifts of opposite signs. On
coordinates,

\&#91;
\Psi_{N,M}(x,y,z)
 =\bigl(x,\ y+x^N,\ z+(y+x^N)^M\bigr).
\&#93;

Their shifts are

\&#91;
d_1=-N-1,\qquad d_2=M-2.
\&#93;

For \(h\in B_{\le6}\), the expansion of
\(\Psi_{N,M}^{-1}h=\exp(-\delta_2)\exp(-\delta_1)h\) uses only

\&#91;
0\le\alpha_1\le6,\qquad0\le\alpha_2\le6.
\&#93;

Indeed, \(\delta_1\) is applied first and does not increase the degree in
\(z\), after which \(\delta_2\) can act at most six times.

Assume

\&#91;
N\ge18,\qquad M\ge21,
\&#93;

and impose the finite arithmetic nonresonance condition

\&#91;
|a(N+1)-b(M-2)|&gt;18
\quad\text{for every }1\le a,b\le6.
\tag{8}
\&#93;

For distinct \(\alpha,\beta\in\{0,\ldots,6\}^2\), a shift collision can only
occur when the two coefficient differences have the same sign. Condition (8)
then gives (4); opposite signs add the two magnitudes, while a zero coefficient
leaves a multiple of \(N+1\) or \(M-2\), both greater than 18.

A simple sufficient subfamily is

\&#91;
M\ge21,\qquad N\ge6M+6,
\&#93;

because then \(N+1-6(M-2)&gt;18\). The exact common-fiber witness already used
for the one-step theorem gives

\&#91;
x^N\partial_yQ,\ x^N\partial_yR,
\ y^M\partial_zQ,\ y^M\partial_zR\notin S
\&#93;

for all \(N,M\ge2\). The reduced-word theorem therefore yields

\&#91;
\boxed{
\Psi_{N,M}(S)\cap B_{\le6}=k
\qquad\text{whenever (8) holds}.
}
\&#93;

This is an infinite theorem for genuinely noncommuting triangular words with
both positive and negative torus shifts. It lies outside both one-sided
high-weight subgroups. Arbitrary affine source transformations applied after
\(\Psi_{N,M}\) preserve the conclusion.

## Scope and next target

The theorem covers:

- arbitrary finite reduced words satisfying the Taylor no-return condition
  (1), with exactness under the stronger separation condition (4);
- arbitrarily long commuting polynomial shears with mixed-sign,
  superincreasing support;
- an explicit infinite noncommuting mixed-sign triangular family.

It does not yet control words whose ordered Taylor shifts return to or overlap
the degree-six weight window. Those resonant mixed-sign reduced words are the
next finite or geometric frontier.
</code></pre>

<a id="source-d6911ca72194f23a"></a>

## `research-notes/lane5-degree-budgets/all_elementary_monomial_shears.json`

<pre><code class="language-json">
{"coefficient_scope":"All coefficients in characteristic zero: c=0 is affine/standard; nonzero nonresonant coefficients are torus-conjugate to 1; z+c*y^2 is covered by the exact resonant weight certificate.","conclusion":"For every characteristic-zero field k, every c in k, every exponent N&gt;=2, and each of the six elementary monomial source shears xi -&gt; xi + c*xj^N (i!=j), the algebra generated by sigma_c,N(k&#91;P,Q,R&#93;) intersect k&#91;x,y,z&#93;_{&lt;=6} has transcendence degree at most one. More precisely, the intersection is span{1,Q,R} for c=0; for c!=0 it is span{1,sigma(R)} exactly when sigma(R) has degree at most six, and k otherwise.","degree_bound":6,"field":"Q","finite_case_ranges":{"x+yN":&#91;2,17&#93;,"x+zN":&#91;2,8&#93;,"y+xN":&#91;2,17&#93;,"y+zN":&#91;2,9&#93;,"z+xN":&#91;2,16&#93;,"z+yN":&#91;2,20&#93;},"finite_cases":&#91;{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0,80&#93;,"pivot_minor_determinant_mod_prime":582420,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0,83&#93;,"pivot_minor_determinant_mod_prime":546773,"rank":82},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":112751,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":736810,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":32598,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":84464,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":623215,"rank":83},{"exponent":9,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":762006,"rank":83},{"exponent":10,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":699525,"rank":83},{"exponent":11,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":877684,"rank":83},{"exponent":12,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":186225,"rank":83},{"exponent":13,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":724303,"rank":83},{"exponent":14,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":885928,"rank":83},{"exponent":15,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":430780,"rank":83},{"exponent":16,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":660803,"rank":83},{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0,74&#93;,"pivot_minor_determinant_mod_prime":228425,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0,80&#93;,"pivot_minor_determinant_mod_prime":508300,"rank":82},{"exponent":4,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0,83&#93;,"pivot_minor_determinant_mod_prime":752237,"rank":82},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":351059,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":661259,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":283954,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":327041,"rank":83},{"exponent":9,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":932898,"rank":83},{"exponent":10,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":472848,"rank":83},{"exponent":11,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":959817,"rank":83},{"exponent":12,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":900174,"rank":83},{"exponent":13,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":410594,"rank":83},{"exponent":14,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":129209,"rank":83},{"exponent":15,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":872197,"rank":83},{"exponent":16,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":747721,"rank":83},{"exponent":17,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":798150,"rank":83},{"exponent":2,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":457172,"rank":83},{"exponent":3,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":406607,"rank":83},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":553918,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":975352,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":518757,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":959917,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":285826,"rank":83},{"exponent":9,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":831057,"rank":83},{"exponent":10,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":712809,"rank":83},{"exponent":11,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":823478,"rank":83},{"exponent":12,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":621366,"rank":83},{"exponent":13,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":4384,"rank":83},{"exponent":14,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":485452,"rank":83},{"exponent":15,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":890483,"rank":83},{"exponent":16,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":684662,"rank":83},{"exponent":17,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":238733,"rank":83},{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0,71&#93;,"pivot_minor_determinant_mod_prime":640259,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0,73&#93;,"pivot_minor_determinant_mod_prime":901386,"rank":82},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":780972,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":441694,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":482854,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":865898,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":392587,"rank":83},{"exponent":9,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":250936,"rank":83},{"exponent":10,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":37462,"rank":83},{"exponent":11,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":827664,"rank":83},{"exponent":12,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":151830,"rank":83},{"exponent":13,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":43236,"rank":83},{"exponent":14,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":584270,"rank":83},{"exponent":15,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":374792,"rank":83},{"exponent":16,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":169441,"rank":83},{"exponent":17,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":766115,"rank":83},{"exponent":18,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":222976,"rank":83},{"exponent":19,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":429773,"rank":83},{"exponent":20,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":328867,"rank":83},{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0,65&#93;,"pivot_minor_determinant_mod_prime":898592,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0,65&#93;,"pivot_minor_determinant_mod_prime":971931,"rank":82},{"exponent":4,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0,65&#93;,"pivot_minor_determinant_mod_prime":342229,"rank":82},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":103900,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":813977,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":37567,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":976194,"rank":83},{"exponent":9,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":753158,"rank":83},{"exponent":2,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":194196,"rank":83},{"exponent":3,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":571221,"rank":83},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":733234,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":60686,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":915794,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":313231,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":94070,"rank":83}&#93;,"high_thresholds":{"x+yN":18,"x+zN":9,"y+xN":18,"y+zN":10,"z+xN":17,"z+yN":21},"prime":1000003,"resonant_script":{"path":"resonant_weight_certificate.py","sha256":"4e5c5d517619af4804a6754370eac764eced54ce6177a6003037489eb53f1877"},"schema_version":1,"script":{"path":"all_elementary_monomial_shears.py","sha256":"44e4892b39de80cbde6ce7034e9451623d407607f64c2d55762b13d38940f6c5"},"theorem_id":"lane5-all-elementary-monomial-source-shears-degree6"}
</code></pre>

<a id="source-475f7fcdbf33aece"></a>

## `research-notes/lane5-degree-budgets/all_elementary_monomial_shears.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the all-exponent elementary-monomial-source-shear theorem.

The finite part replays exact rational common-fiber certificates for every
exponent not covered by the torus-weight separation lemma.  The infinite tail
is certified structurally from the source torus grading and one explicit
three-point fiber.  The resonant coefficient family z -&gt; z + c*y^2 is delegated
to resonant_weight_certificate.py.

This verifies a theorem for single elementary shears.  It does not cover
arbitrary compositions of shears or wild source automorphisms.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from elementary_shear_scan import BOUND, PRIME, candidate_points, verify_case
from resonant_weight_certificate import verify as verify_resonant

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "all_elementary_monomial_shears.json"

SOURCE_WEIGHTS = {"x": -1, "y": 1, "z": 2}
WEIGHT_INTERVAL = (-6, 12)
HIGH_THRESHOLDS = {
    "z+xN": 17,
    "y+xN": 18,
    "x+yN": 18,
    "z+yN": 21,
    "y+zN": 10,
    "x+zN": 9,
}


def map_f(point: tuple&#91;Fraction, Fraction, Fraction&#93;) -&gt; tuple&#91;Fraction, Fraction, Fraction&#93;:
    x, y, z = point
    a = 1 + x * y
    p = a**3 * z + y**2 * a * (4 + 3 * x * y)
    q = y + 3 * x * a**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    r = 2 * x - 3 * x**2 * y - x**3 * z
    return p, q, r


def derivatives(point: tuple&#91;Fraction, Fraction, Fraction&#93;) -&gt; dict&#91;str, Fraction&#93;:
    x, y, z = point
    return {
        "Q_x": 3 * (3*x**2*y**2*z + 6*x*y**3 + 4*x*y*z + 4*y**2 + z),
        "Q_y": 6*x**3*y*z + 27*x**2*y**2 + 6*x**2*z + 24*x*y + 1,
        "Q_z": 3*x*(x*y + 1)**2,
        "R_x": -3*x**2*z - 6*x*y + 2,
        "R_y": -3*x**2,
        "R_z": -x**3,
    }


def verify_weight_tail() -&gt; dict&#91;str, object&#93;:
    low, high = WEIGHT_INTERVAL
    if high - low != 18:
        raise AssertionError("ordinary degree-six torus-weight width changed")

    derivation_weights = {
        "z+xN": lambda n: -n - 2,
        "y+xN": lambda n: -n - 1,
        "x+yN": lambda n: n + 1,
        "z+yN": lambda n: n - 2,
        "y+zN": lambda n: 2*n - 1,
        "x+zN": lambda n: 2*n + 1,
    }
    for kind, threshold in HIGH_THRESHOLDS.items():
        if abs(derivation_weights&#91;kind&#93;(threshold)) &lt;= 18:
            raise AssertionError(f"{kind}: threshold does not enter the separated range")
        if threshold &gt; 2 and abs(derivation_weights&#91;kind&#93;(threshold - 1)) &gt; 18:
            raise AssertionError(f"{kind}: threshold is not minimal")

    u = (Fraction(-12), Fraction(1, 11), Fraction(-8, 11))
    v = (Fraction(-10), Fraction(1, 11), Fraction(-14, 11))
    w = (Fraction(22), Fraction(-1, 22), Fraction(65, 484))
    target = (Fraction(0), Fraction(1, 11), Fraction(-1320))
    if not (map_f(u) == map_f(v) == map_f(w) == target):
        raise AssertionError("high-weight witness points are not one fiber")

    du, dv, dw = derivatives(u), derivatives(v), derivatives(w)
    expected = {
        "u": {
            "Q_x": Fraction(-684, 1331), "Q_y": Fraction(7753, 121),
            "Q_z": Fraction(-36, 121), "R_x": Fraction(3550, 11),
            "R_y": Fraction(-432), "R_z": Fraction(1728),
        },
        "v": {
            "Q_x": Fraction(750, 1331), "Q_y": Fraction(-8219, 121),
            "Q_z": Fraction(-30, 121), "R_x": Fraction(4282, 11),
            "R_y": Fraction(-300), "R_z": Fraction(1000),
        },
        "w": {
            "Q_x": Fraction(-3, 242), "Q_y": Fraction(4),
            "Q_z": Fraction(0), "R_x": Fraction(-187),
            "R_y": Fraction(-1452), "R_z": Fraction(-10648),
        },
    }
    if du != expected&#91;"u"&#93; or dv != expected&#91;"v"&#93; or dw != expected&#91;"w"&#93;:
        raise AssertionError("derivative witness table changed")

    if du&#91;"Q_z"&#93; == 0 or dw&#91;"Q_z"&#93; != 0:
        raise AssertionError("z-derivative zero witness changed")
    if abs(u&#91;0&#93;) == abs(v&#91;0&#93;):
        raise AssertionError("x-power witness lost strict magnitude")
    if not (du&#91;"Q_y"&#93; &gt; 0 &gt; dv&#91;"Q_y"&#93;):
        raise AssertionError("y+x^N Q witness lost opposite signs")
    if not (du&#91;"Q_x"&#93; &lt; 0 &lt; dv&#91;"Q_x"&#93;):
        raise AssertionError("x+y^N Q witness lost opposite signs")
    if not (u&#91;1&#93; == v&#91;1&#93; != 0):
        raise AssertionError("same-y witness changed")
    if du&#91;"Q_z"&#93; == dv&#91;"Q_z"&#93; or du&#91;"R_z"&#93; == dv&#91;"R_z"&#93;:
        raise AssertionError("same-y z-derivative witness changed")
    if not (u&#91;2&#93; &lt; 0 and v&#91;2&#93; &lt; 0 and du&#91;"Q_y"&#93; &gt; 0 &gt; dv&#91;"Q_y"&#93;):
        raise AssertionError("y+z^N Q sign witness changed")
    if not (
        Fraction(36, 25) * Fraction(4, 7) &lt; 1
        and Fraction(3550, 4282) * Fraction(4, 7) &lt; 1
    ):
        raise AssertionError("z-power strict-ratio witnesses changed")

    return {
        "status": "pass",
        "weight_interval": list(WEIGHT_INTERVAL),
        "weight_width": high - low,
        "high_thresholds": HIGH_THRESHOLDS,
        "common_fiber_target": &#91;str(value) for value in target&#93;,
        "conclusion": (
            "For every listed direction, every nonzero shear coefficient, "
            "and every exponent at or above its threshold, the degree-six "
            "intersection is k."
        ),
    }


def main() -&gt; int:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if certificate&#91;"prime"&#93; != PRIME or certificate&#91;"degree_bound"&#93; != BOUND:
        raise AssertionError("finite certificate parameters changed")
    candidates = candidate_points()
    finite_results = &#91;
        verify_case(case, candidates) for case in certificate&#91;"finite_cases"&#93;
    &#93;
    tail = verify_weight_tail()
    resonant = verify_resonant()
    result = {
        "status": "pass",
        "finite_case_count": len(finite_results),
        "finite_rank_82_cases": sum(item&#91;"rank"&#93; == 82 for item in finite_results),
        "finite_rank_83_cases": sum(item&#91;"rank"&#93; == 83 for item in finite_results),
        "tail": tail,
        "resonant": resonant,
        "conclusion": certificate&#91;"conclusion"&#93;,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-e9c67bd9a2c5c268"></a>

## `research-notes/lane5-degree-budgets/coefficient_transport.md`

<pre><code class="language-markdown">
# Coefficient transport for elementary Lane 5 shears

Let `S=k&#91;P,Q,R&#93;` be the displayed image subalgebra in `B=k&#91;x,y,z&#93;`, over a
characteristic-zero field. The source torus

```text
T_lambda(x,y,z) = (lambda^(-1)*x, lambda*y, lambda^2*z)
```

acts equivariantly:

```text
T_lambda(P,Q,R) = (lambda^2*P, lambda*Q, lambda^(-1)*R).
```

Thus `T_lambda(S)=S`, and the torus preserves every ordinary-degree piece of
`B`.

For a monomial elementary shear sending `X_i` to `X_i+c*m`, direct
conjugation gives

```text
T_lambda^(-1) E_(i,m,c) T_lambda
  = E_(i,m,c*lambda^(w(X_i)-w(m))),
```

where

```text
w(x)=-1,  w(y)=1,  w(z)=2.
```

Whenever `w(X_i)-w(m)` is nonzero, every nonzero coefficient becomes
coefficient one after extending to an algebraic closure. The exact
coefficient-one intersection theorem therefore transports to every nonzero
coefficient and descends to the original characteristic-zero field.

For the six monomial directions,

| Shear | Weight difference |
| --- | ---: |
| `z -&gt; z+c*x^N` | `N+2` |
| `y -&gt; y+c*x^N` | `N+1` |
| `x -&gt; x+c*y^N` | `-N-1` |
| `z -&gt; z+c*y^N` | `2-N` |
| `y -&gt; y+c*z^N` | `1-2N` |
| `x -&gt; x+c*z^N` | `-1-2N` |

The unique resonance with `N&gt;=2` is

```text
z -&gt; z+c*y^2.
```

## Exact resonant closure

The resonant shear preserves the torus grading. Decompose `B_{&lt;=6}` into its
19 weight spaces. Their dimensions are at most eight. The exact certificate
in

```text
resonant_weight_certificate.py
resonant_weight_certificate.json
```

supplies 33 rational determinantal minors. Their gcds in `Q&#91;c&#93;` are

```text
1  in every weight except weight 1;
c  in weight 1.
```

The permanent weight-zero kernel is generated by `1`, and the permanent
weight-minus-one kernel is generated by

```text
E_c(R)=R-c*x^3*y^2.
```

At `c=0`, weight one contributes `Q`, reproducing the standard intersection.
For every `c!=0`, weight one has full rank. Hence there are no nonzero
exceptional coefficients:

```text
E_c(S) intersect B_{&lt;=6}
  = span{1,E_c(R)}       for every c!=0.
```

Together with torus transport, this proves the coefficient statement for all
six elementary monomial shear directions, every exponent `N&gt;=2`, and every
coefficient.

## Affine source closure

The standard theorem also transports under every affine source automorphism
`L`, because `L(B_{&lt;=6})=B_{&lt;=6}`:

```text
L(S) intersect B_{&lt;=6} = span{1,L(Q),L(R)}.
```

The composition frontier is now narrower. The same-direction theorem in
`lacunary_polynomial_shears.md` closes arbitrary high-weight polynomial
tails, and `one_sided_high_weight_semigroup.md` closes arbitrary noncommuting
words whose nonzero weights all lie beyond the degree-six window on one side,
including arbitrary interleaving with this resonant family. Low-weight words,
mixed positive/negative high-weight words, and wild automorphisms remain open.
</code></pre>

<a id="source-f1c107cd6dee57ee"></a>

## `research-notes/lane5-degree-budgets/elementary_shear_scan.json`

<pre><code class="language-json">
{"candidate_pool":{"a_range":&#91;-12,0&#93;,"b_range":&#91;-12,1&#93;,"h":&#91;"1","2","3"&#93;,"pair_order":&#91;1,2&#93;,"signs":&#91;1,-1&#93;},"cases":&#91;{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0,80&#93;,"pivot_minor_determinant_mod_prime":582420,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0,83&#93;,"pivot_minor_determinant_mod_prime":546773,"rank":82},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":112751,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":736810,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":32598,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":84464,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"z+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":623215,"rank":83},{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0,74&#93;,"pivot_minor_determinant_mod_prime":228425,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0,80&#93;,"pivot_minor_determinant_mod_prime":508300,"rank":82},{"exponent":4,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0,83&#93;,"pivot_minor_determinant_mod_prime":752237,"rank":82},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":351059,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":661259,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":283954,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"y+xN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":327041,"rank":83},{"exponent":2,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":457172,"rank":83},{"exponent":3,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":406607,"rank":83},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":553918,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":975352,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":518757,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":959917,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"x+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":285826,"rank":83},{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0,71&#93;,"pivot_minor_determinant_mod_prime":640259,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0,73&#93;,"pivot_minor_determinant_mod_prime":901386,"rank":82},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":780972,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":441694,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":482854,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":865898,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"z+yN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":392587,"rank":83},{"exponent":2,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0,65&#93;,"pivot_minor_determinant_mod_prime":898592,"rank":82},{"exponent":3,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0,65&#93;,"pivot_minor_determinant_mod_prime":971931,"rank":82},{"exponent":4,"intersection_basis":&#91;"1","sigma(R)"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0,65&#93;,"pivot_minor_determinant_mod_prime":342229,"rank":82},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":103900,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":813977,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":37567,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"y+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":976194,"rank":83},{"exponent":2,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":194196,"rank":83},{"exponent":3,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":571221,"rank":83},{"exponent":4,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":733234,"rank":83},{"exponent":5,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":60686,"rank":83},{"exponent":6,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":915794,"rank":83},{"exponent":7,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":313231,"rank":83},{"exponent":8,"intersection_basis":&#91;"1"&#93;,"kind":"x+zN","nonpivot_columns":&#91;0&#93;,"pivot_minor_determinant_mod_prime":94070,"rank":83}&#93;,"conclusion":"For each listed elementary source shear sigma, sigma(k&#91;P,Q,R&#93;) intersect k&#91;x,y,z&#93;_{&lt;=6} is exactly the span of the listed intersection_basis. Hence its generated algebra has transcendence degree at most one.","degree_bound":6,"prime":1000003,"schema_version":1,"scope":"Six coefficient-one monomial shear directions, exponents 2 through 8.","theorem_id":"lane5-elementary-monomial-shear-degree6"}
</code></pre>

<a id="source-23231a729cc074f2"></a>

## `research-notes/lane5-degree-budgets/elementary_shear_scan.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify bounded elementary-source-shear Lane 5 certificates.

For each coefficient-one monomial shear in six coordinate directions and each
exponent 2 through 8, the script constructs rational common-fiber pairs for
the sheared map, finds a nonzero modular minor on B_{&lt;=6}, and checks the exact
kernel vectors that identify the filtered intersection.

The result is a finite exact family, not a classification of arbitrary source
automorphisms.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from standard_filtration_certificate import (
    dot,
    evaluate_monomials,
    fraction_mod,
    monomials_degree_at_most,
    split_target,
)

HERE = Path(__file__).resolve().parent
EXPECTED = HERE / "elementary_shear_scan.json"
PRIME = 1_000_003
BOUND = 6
MONOMIALS = monomials_degree_at_most(BOUND)
INDEX = {monomial: index for index, monomial in enumerate(MONOMIALS)}


def transform_inverse(
    kind: str,
    exponent: int,
    point: tuple&#91;Fraction, Fraction, Fraction&#93;,
) -&gt; tuple&#91;Fraction, Fraction, Fraction&#93;:
    x, y, z = point
    if kind == "z+xN":
        return x, y, z - x**exponent
    if kind == "y+xN":
        return x, y - x**exponent, z
    if kind == "x+yN":
        return x - y**exponent, y, z
    if kind == "z+yN":
        return x, y, z - y**exponent
    if kind == "y+zN":
        return x, y - z**exponent, z
    if kind == "x+zN":
        return x - z**exponent, y, z
    raise ValueError(f"unknown shear kind: {kind}")


def add_row_echelon(row: list&#91;int&#93;, basis: dict&#91;int, list&#91;int&#93;&#93;) -&gt; bool:
    work = row&#91;:&#93;
    for pivot in sorted(basis):
        factor = work&#91;pivot&#93;
        if not factor:
            continue
        basis_row = basis&#91;pivot&#93;
        for column in range(pivot, len(work)):
            work&#91;column&#93; = (
                work&#91;column&#93; - factor * basis_row&#91;column&#93;
            ) % PRIME
    pivot = next((i for i, entry in enumerate(work) if entry), None)
    if pivot is None:
        return False
    inverse = pow(work&#91;pivot&#93;, PRIME - 2, PRIME)
    for column in range(pivot, len(work)):
        work&#91;column&#93; = work&#91;column&#93; * inverse % PRIME
    basis&#91;pivot&#93; = work
    return True


def determinant_mod(matrix: list&#91;list&#91;int&#93;&#93;) -&gt; int:
    work = &#91;&#91;entry % PRIME for entry in row&#93; for row in matrix&#93;
    size = len(work)
    determinant = 1
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work&#91;row&#93;&#91;column&#93;), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work&#91;column&#93;, work&#91;pivot_row&#93; = work&#91;pivot_row&#93;, work&#91;column&#93;
            determinant = -determinant
        pivot = work&#91;column&#93;&#91;column&#93; % PRIME
        determinant = determinant * pivot % PRIME
        inverse = pow(pivot, PRIME - 2, PRIME)
        for row in range(column + 1, size):
            if not work&#91;row&#93;&#91;column&#93;:
                continue
            factor = work&#91;row&#93;&#91;column&#93; * inverse % PRIME
            for offset in range(column, size):
                work&#91;row&#93;&#91;offset&#93; = (
                    work&#91;row&#93;&#91;offset&#93; - factor * work&#91;column&#93;&#91;offset&#93;
                ) % PRIME
    return determinant % PRIME


def constant_vector() -&gt; list&#91;Fraction&#93;:
    vector = &#91;Fraction(0)&#93; * len(MONOMIALS)
    vector&#91;INDEX&#91;(0, 0, 0)&#93;&#93; = 1
    return vector


def sheared_r_vector(kind: str, exponent: int) -&gt; list&#91;Fraction&#93; | None:
    """Coefficient vector of sigma(R), when its total degree is at most six."""
    coefficients: dict&#91;tuple&#91;int, int, int&#93;, Fraction&#93; = {
        (1, 0, 0): Fraction(2),
        (2, 1, 0): Fraction(-3),
        (3, 0, 1): Fraction(-1),
    }
    if kind == "z+xN":
        monomial, coefficient = (exponent + 3, 0, 0), Fraction(-1)
    elif kind == "y+xN":
        monomial, coefficient = (exponent + 2, 0, 0), Fraction(-3)
    elif kind == "z+yN":
        monomial, coefficient = (3, exponent, 0), Fraction(-1)
    elif kind == "y+zN":
        monomial, coefficient = (2, 0, exponent), Fraction(-3)
    else:
        return None
    coefficients&#91;monomial&#93; = coefficients.get(monomial, Fraction(0)) + coefficient
    if any(
        sum(monomial) &gt; BOUND and coefficient
        for monomial, coefficient in coefficients.items()
    ):
        return None
    vector = &#91;Fraction(0)&#93; * len(MONOMIALS)
    for monomial, coefficient in coefficients.items():
        if coefficient:
            vector&#91;INDEX&#91;monomial&#93;&#93; = coefficient
    return vector


def candidate_points() -&gt; list&#91;dict&#91;str, object&#93;&#93;:
    candidates: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    for h in (Fraction(1), Fraction(2), Fraction(3)):
        for a in range(-12, 1):
            for b in range(-12, 2):
                for sign in (1, -1):
                    try:
                        _, points = split_target(
                            Fraction(a), Fraction(b), h, sign
                        )
                    except (ValueError, ZeroDivisionError):
                        continue
                    candidates.append(
                        {
                            "a": str(a),
                            "b": str(b),
                            "h": str(h),
                            "sign": sign,
                            "points": points,
                        }
                    )
    return candidates


def verify_case(
    expected: dict&#91;str, object&#93;,
    candidates: list&#91;dict&#91;str, object&#93;&#93;,
) -&gt; dict&#91;str, object&#93;:
    kind = str(expected&#91;"kind"&#93;)
    exponent = int(expected&#91;"exponent"&#93;)
    target_rank = int(expected&#91;"rank"&#93;)
    basis: dict&#91;int, list&#91;int&#93;&#93; = {}
    exact_rows: list&#91;list&#91;Fraction&#93;&#93; = &#91;&#93;

    for candidate in candidates:
        points = &#91;
            transform_inverse(kind, exponent, point)
            for point in candidate&#91;"points"&#93;  # type: ignore&#91;index&#93;
        &#93;
        first = evaluate_monomials(points&#91;0&#93;, MONOMIALS, BOUND)
        for pair in (1, 2):
            second = evaluate_monomials(points&#91;pair&#93;, MONOMIALS, BOUND)
            exact_row = &#91;left - right for left, right in zip(first, second)&#93;
            modular_row = &#91;fraction_mod(entry, PRIME) for entry in exact_row&#93;
            if not add_row_echelon(modular_row, basis):
                continue
            exact_rows.append(exact_row)
            if len(basis) == target_rank:
                break
        if len(basis) == target_rank:
            break

    if len(basis) != target_rank:
        raise AssertionError(f"{kind}, N={exponent}: target rank not reached")
    pivots = sorted(basis)
    nonpivots = &#91;
        column for column in range(len(MONOMIALS)) if column not in set(pivots)
    &#93;
    if nonpivots != &#91;int(value) for value in expected&#91;"nonpivot_columns"&#93;&#93;:
        raise AssertionError(f"{kind}, N={exponent}: pivot columns changed")

    modular_rows = &#91;
        &#91;fraction_mod(entry, PRIME) for entry in row&#93; for row in exact_rows
    &#93;
    determinant = determinant_mod(
        &#91;&#91;row&#91;column&#93; for column in pivots&#93; for row in modular_rows&#93;
    )
    if determinant != int(expected&#91;"pivot_minor_determinant_mod_prime"&#93;):
        raise AssertionError(f"{kind}, N={exponent}: determinant changed")

    vectors = {"1": constant_vector()}
    sheared_r = sheared_r_vector(kind, exponent)
    if sheared_r is not None:
        vectors&#91;"sigma(R)"&#93; = sheared_r
    expected_basis = &#91;str(value) for value in expected&#91;"intersection_basis"&#93;&#93;
    if list(vectors) != expected_basis:
        raise AssertionError(f"{kind}, N={exponent}: kernel basis changed")
    for name, vector in vectors.items():
        if any(dot(row, vector) != 0 for row in exact_rows):
            raise AssertionError(
                f"{kind}, N={exponent}: {name} is not in the exact kernel"
            )

    kernel_dimension = len(MONOMIALS) - target_rank
    if kernel_dimension != len(vectors):
        raise AssertionError(f"{kind}, N={exponent}: kernel dimension changed")

    return {
        "kind": kind,
        "exponent": exponent,
        "rank": target_rank,
        "kernel_dimension": kernel_dimension,
        "intersection_basis": expected_basis,
        "pivot_minor_determinant_mod_prime": determinant,
        "status": "pass",
    }


def main() -&gt; int:
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    if int(expected&#91;"prime"&#93;) != PRIME or int(expected&#91;"degree_bound"&#93;) != BOUND:
        raise AssertionError("global certificate parameters changed")
    candidates = candidate_points()
    results = &#91;verify_case(case, candidates) for case in expected&#91;"cases"&#93;&#93;
    summary = {
        "status": "pass",
        "case_count": len(results),
        "prime": PRIME,
        "degree_bound": BOUND,
        "rank_82_cases": sum(result&#91;"rank"&#93; == 82 for result in results),
        "rank_83_cases": sum(result&#91;"rank"&#93; == 83 for result in results),
        "conclusion": expected&#91;"conclusion"&#93;,
        "cases": results,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-8af47f98c4f1d666"></a>

## `research-notes/lane5-degree-budgets/lacunary_polynomial_shears.md`

<pre><code class="language-markdown">
# High-weight polynomial-shear composition theorem

Let

```text
S = k&#91;P,Q,R&#93; subset B = k&#91;x,y,z&#93;
```

for the displayed Keller map, over a characteristic-zero field. Give `B` the
source-torus grading

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2.
```

Then `S` is graded, with

```text
wt(P)=2,  wt(Q)=1,  wt(R)=-1,
```

while `B_{&lt;=6}` is supported on `&#91;-6,12&#93;`, a weight interval of width 18.

This note proves a composition theorem for arbitrary finite polynomial shears
supported outside that weight window. No lacunarity or separation among the
individual monomials is required.

## Theorem

Fix distinct coordinates `x_i,x_j`. Let

```text
f(x_j) = a_0+a_1*x_j + sum_{N in E} c_N*x_j^N,
```

where `E` is finite, every `N&gt;=2`, and every displayed `c_N` is nonzero. Put

```text
D_N = x_j^N partial_{x_i},
e_N = N*wt(x_j)-wt(x_i).
```

Assume the nonlinear shifts are all on one side of the degree-six window:

```text
e_N &gt;= 19 for every N in E,
```

or

```text
e_N &lt;= -19 for every N in E.
```

If `E` is nonempty and `sigma_f` is the source shear

```text
x_i -&gt; x_i+f(x_j),
```

then

```text
sigma_f(S) intersect B_{&lt;=6} = k.
```

Thus an arbitrary number of same-direction high-weight elementary shears,
with arbitrary coefficients and arbitrarily close exponents, cannot expose a
nonconstant image-algebra element of source degree at most six.

## Proof

The affine part `a_0+a_1*x_j` commutes with the nonlinear shear and preserves
`B_{&lt;=6}`. It can therefore be removed. Write

```text
D_f = sum_{N in E} c_N D_N,
sigma_f = exp(D_f).
```

Take

```text
g in sigma_f(S) intersect B_{&lt;=6}
```

and decompose `g=sum_w g_w` into torus weights, where `-6&lt;=w&lt;=12`.
Since each `D_N` lowers the exponent of the same coordinate `x_i`, the
expansion of `sigma_f^(-1)(g)` stops after total derivative order six.

### Positive shifts

Suppose every `e_N&gt;=19`. Every term involving at least one derivative has
weight at least

```text
-6+19=13,
```

whereas every zero-order term `g_w` has weight at most 12. Since
`sigma_f^(-1)(g)` lies in the graded algebra `S`, each `g_w` lies in `S`.
The standard filtration theorem gives

```text
g in S intersect B_{&lt;=6} = span{1,Q,R}.
```

Write `g=a+bQ+dR`, and let `e_0` be the smallest shift occurring in `f`.
If `d!=0`, the unique lowest-weight nonzero derivative term in
`sigma_f^(-1)(g)` is

```text
-d*c_0*D_0(R),       of weight -1+e_0.
```

Every other first-order term has larger weight, and every higher-order term
has weight at least `-1+2e_0`. Hence `D_0(R)` would belong to `S`.

If `d=0` but `b!=0`, the unique lowest derivative term is

```text
-b*c_0*D_0(Q),       of weight 1+e_0,
```

so `D_0(Q)` would belong to `S`.

### Negative shifts

Suppose every `e_N&lt;=-19`, and let `e_0` be the largest shift, meaning the one
closest to zero. Derivative terms have weight at most

```text
12-19=-7,
```

so they cannot collide with zero-order weights, which are at least -6. Again
`g` belongs to `span{1,Q,R}`.

If `b!=0`, the unique highest-weight derivative term is

```text
-b*c_0*D_0(Q),       of weight 1+e_0.
```

After `b=0`, a nonzero `d` would make

```text
-d*c_0*D_0(R),       of weight -1+e_0,
```

the unique highest derivative term. Thus a nonconstant `g` again forces one
of `D_0(Q),D_0(R)` to lie in `S`.

### Exact common-fiber obstruction

The three rational source points

```text
u = (-12,  1/11,  -8/11)
v = (-10,  1/11, -14/11)
w = ( 22, -1/22, 65/484)
```

have the common image

```text
F(u)=F(v)=F(w)=(0,1/11,-1320).
```

Their derivative values are

```text
             Q_x          Q_y          Q_z       R_x       R_y    R_z
u       -684/1331      7753/121      -36/121    3550/11    -432   1728
v        750/1331     -8219/121      -30/121    4282/11    -300   1000
w        -3/242              4             0       -187   -1452 -10648
```

For each of the six coordinate directions and every `N&gt;=2`, multiplying the
relevant derivative column by `x_j^N` gives unequal values on this common
fiber. Therefore

```text
D_N(Q) notin S,       D_N(R) notin S.
```

The contradictions above force `b=d=0`. Hence `g` is constant.

## Concrete thresholds

The theorem applies to every polynomial whose nonlinear support is contained
in the indicated tail:

```text
z -&gt; z+f(x):   every nonlinear exponent N&gt;=17
y -&gt; y+f(x):   every nonlinear exponent N&gt;=18
x -&gt; x+f(y):   every nonlinear exponent N&gt;=18
z -&gt; z+f(y):   every nonlinear exponent N&gt;=21
y -&gt; y+f(z):   every nonlinear exponent N&gt;=10
x -&gt; x+f(z):   every nonlinear exponent N&gt;=9.
```

The coefficients and the number of terms are unrestricted.

## Resonant-plus-tail corollary

The weight-zero shear

```text
z -&gt; z+a*y^2
```

preserves the torus grading and commutes with every shear `z-&gt;z+c_N*y^N`.
The exact resonant certificate gives its degree-six intersection as
`span{1,sigma_a(R)}`. Repeating the proof above with this graded intermediate
algebra shows:

```text
z -&gt; z+a_0+a_1*y+a_2*y^2 + sum_{N&gt;=21} c_N*y^N
```

has degree-six intersection `k` whenever the high tail is nonzero. If the
high tail vanishes, the exact resonant theorem applies.

## Relation to the single-shear theorem

For a one-term polynomial, the theorem recovers the infinite structural tails
of `all_elementary_monomial_shears.py`. The finite exact certificates fill the
remaining exponents. Together they prove every single monomial shear; the
present theorem additionally closes arbitrary finite compositions inside each
high-weight same-direction tail.

## Remaining scope

Closely spaced low-weight polynomial terms and noncommuting shear directions
can produce weight collisions inside the interval `&#91;-6,12&#93;`. They are not
covered here. These are now the first genuine composition cases.
</code></pre>

<a id="source-2fa4afdcfe7a66d7"></a>

## `research-notes/lane5-degree-budgets/lacunary_polynomial_shears.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Check the arithmetic and exact witness for high-weight polynomial shears."""

from __future__ import annotations

import json
from fractions import Fraction

WIDTH = 18
WEIGHTS = {"x": -1, "y": 1, "z": 2}
DIRECTIONS = (
    ("z+xN", "z", "x", 17, -1),
    ("y+xN", "y", "x", 18, -1),
    ("x+yN", "x", "y", 18, 1),
    ("z+yN", "z", "y", 21, 1),
    ("y+zN", "y", "z", 10, 1),
    ("x+zN", "x", "z", 9, 1),
)


def map_f(point: tuple&#91;Fraction, Fraction, Fraction&#93;):
    x, y, z = point
    a = 1 + x*y
    return (
        a**3*z + y**2*a*(4+3*x*y),
        y + 3*x*a**2*z + 3*x*y**2*(4+3*x*y),
        2*x - 3*x**2*y - x**3*z,
    )


def derivatives(point: tuple&#91;Fraction, Fraction, Fraction&#93;):
    x, y, z = point
    return {
        "Q_x": 3*(3*x**2*y**2*z + 6*x*y**3 + 4*x*y*z + 4*y**2 + z),
        "Q_y": 6*x**3*y*z + 27*x**2*y**2 + 6*x**2*z + 24*x*y + 1,
        "Q_z": 3*x*(x*y+1)**2,
        "R_x": -3*x**2*z - 6*x*y + 2,
        "R_y": -3*x**2,
        "R_z": -x**3,
    }


def main() -&gt; int:
    u = (Fraction(-12), Fraction(1, 11), Fraction(-8, 11))
    v = (Fraction(-10), Fraction(1, 11), Fraction(-14, 11))
    w = (Fraction(22), Fraction(-1, 22), Fraction(65, 484))
    target = (Fraction(0), Fraction(1, 11), Fraction(-1320))
    if not (map_f(u) == map_f(v) == map_f(w) == target):
        raise AssertionError("common-fiber witness changed")

    derivative_table = {
        name: derivatives(point) for name, point in (("u",u),("v",v),("w",w))
    }
    thresholds = &#91;&#93;
    for name, changed, base, threshold, sign in DIRECTIONS:
        shift = threshold*WEIGHTS&#91;base&#93;-WEIGHTS&#91;changed&#93;
        previous = (threshold-1)*WEIGHTS&#91;base&#93;-WEIGHTS&#91;changed&#93;
        if sign*shift &lt; 19:
            raise AssertionError(f"{name}: threshold misses the high-weight tail")
        if sign*previous &gt;= 19:
            raise AssertionError(f"{name}: threshold is not minimal")
        for exponent in range(threshold, threshold+25):
            current = exponent*WEIGHTS&#91;base&#93;-WEIGHTS&#91;changed&#93;
            if sign*current &lt; 19:
                raise AssertionError(f"{name}: tail changed sign or magnitude")
        thresholds.append({"direction":name,"threshold":threshold,"first_shift":shift})

    resonant_shift = 2*WEIGHTS&#91;"y"&#93;-WEIGHTS&#91;"z"&#93;
    if resonant_shift != 0:
        raise AssertionError("z+y^2 is no longer weight zero")

    result = {
        "status": "pass",
        "degree_bound": 6,
        "weight_interval": &#91;-6,12&#93;,
        "weight_width": WIDTH,
        "thresholds": thresholds,
        "resonant_shift_z_plus_y2": resonant_shift,
        "common_fiber_target": &#91;str(value) for value in target&#93;,
        "derivatives": {
            point: {key: str(value) for key, value in table.items()}
            for point, table in derivative_table.items()
        },
        "conclusion": (
            "Each listed threshold is the first exponent whose derivation "
            "weight lies strictly outside the degree-six weight window; the "
            "exact three-point fiber supplies the D(Q),D(R) obstruction used "
            "for arbitrary finite polynomial tails."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-7decd4931d041216"></a>

## `research-notes/lane5-degree-budgets/one_sided_high_weight_compositions.md`

<pre><code class="language-markdown">
# One-sided high-weight noncommuting composition theorem

Let

```text
S=k&#91;P,Q,R&#93; subset B=k&#91;x,y,z&#93;
```

for the displayed Keller map, with source-torus weights

```text
wt(x)=-1,  wt(y)=1,  wt(z)=2.
```

Then `S` is graded, `P,Q,R` have weights `2,1,-1`, and `B_{&lt;=6}` is supported
on the interval `&#91;-6,12&#93;`, of width `18`.

## Abstract window-separation lemma

Let `B=direct_sum_w B_w` be a `Z`-graded algebra, let `A subset B` be graded,
and let

```text
V subset direct_sum_{a&lt;=w&lt;=b} B_w.
```

Put `W=b-a`. Let

```text
Phi = exp(D_m) ... exp(D_1),
```

where every `D_i` is a homogeneous locally nilpotent derivation. If all their
weights are greater than `W`, or all are less than `-W`, then

```text
Phi(A) intersect V  subset  A intersect V.
```

### Proof

Take `g in Phi(A) intersect V`, write `g=sum_{a&lt;=w&lt;=b} g_w`, and expand

```text
Phi^(-1)(g)=exp(-D_1)...exp(-D_m)(g).
```

The expansion is finite. Every ordered derivative word applied to `g_w` has
weight

```text
w+n_1*wt(D_1)+...+n_m*wt(D_m),
```

with all `n_i&gt;=0`. If the weights are positive, every nonzero word has weight
greater than `a+W=b`; if they are negative, every nonzero word has weight less
than `b-W=a`. Hence the components of `Phi^(-1)(g)` in `&#91;a,b&#93;` are exactly
the `g_w`. Since `Phi^(-1)(g)` lies in the graded algebra `A`, each `g_w`
lies in `A`. Therefore `g lies in A intersect V`.  ∎

No commutativity, factorization normal form, or bound on word length is used.

## Main Lane 5 theorem

Let

```text
Phi = exp(c_m D_m) ... exp(c_1 D_1)
```

be any finite ordered composition, where every `c_i` is nonzero and every
`D_i` is a homogeneous locally nilpotent source derivation of torus weight
`e_i`. The derivations need not commute and may change different coordinates.

Assume either

```text
e_i &gt;= 19 for every i
```

or

```text
e_i &lt;= -19 for every i.
```

Then

```text
Phi(S) intersect B_{&lt;=6}
  subset S intersect B_{&lt;=6}
  = span_k{1,Q,R}.
```

Consequently

```text
trdeg k&#91;Phi(S) intersect B_{&lt;=6}&#93; &lt;= 2.
```

Thus no one-sided high-weight composition can produce a degree-at-most-six
target coordinate frame. This is a genuine noncommuting composition theorem,
not a finite scan.

## Elementary-monomial corollary

For

```text
D=x_j^N partial_{x_i},
```

one has

```text
e=N*wt(x_j)-wt(x_i).
```

Therefore any finite ordered composition of elementary monomial shears is
covered when all factors are chosen from one of the following two one-sided
sets.

### Negative side

```text
z -&gt; z+c*x^N,   N&gt;=17
y -&gt; y+c*x^N,   N&gt;=18
```

### Positive side

```text
x -&gt; x+c*y^N,   N&gt;=18
z -&gt; z+c*y^N,   N&gt;=21
y -&gt; y+c*z^N,   N&gt;=10
x -&gt; x+c*z^N,   N&gt;=9
```

Factors from the same side may be mixed in any order, may repeat weights, and
need not commute. Coefficients are arbitrary. Polynomial shears with several
same-direction high-weight monomials are included by factoring their commuting
summands.

## Infinite subgroups and restricted orbit-minimality

Let `G_+` be the subgroup generated by all positive-side shears above, and
let `G_-` be the subgroup generated by the two negative-side families. The
inverse of a generator has the same weight and merely negates its coefficient,
so every element of `G_+` or `G_-` has a one-sided factorization to which the
main theorem applies.

Therefore, for every `Phi in G_+ union G_-`,

```text
trdeg k&#91;Phi(S) intersect B_{&lt;=6}&#93; &lt;= 2.
```

If `L` is an affine source automorphism, then `L(B_{&lt;=6})=B_{&lt;=6}` and

```text
L(Phi(S)) intersect B_{&lt;=6}
  = L(Phi(S) intersect B_{&lt;=6}).
```

Hence the same conclusion holds for every source transformation in

```text
Aff_3(k) G_+   union   Aff_3(k) G_-.
```

Target automorphisms merely choose another polynomial coordinate frame of
`S`. By the orbit-degree criterion, the known map admits no left-right
equivalent presentation of degree at most six whose source transformation
lies in either of these two infinite affine-extended subgroups. Since its
displayed degree is seven, its orbit-minimal degree is exactly seven within
both restricted orbit classes.

`G_+` is nonabelian because its generators may change interacting
coordinates. The two negative families commute with one another, so `G_-` is
abelian.

## Arbitrary interleaving with the resonant shear

The weight-zero source automorphisms

```text
rho_a: z -&gt; z+a*y^2
```

commute with the torus, and their degree-six intersections are exactly

```text
rho_0(S) intersect B_{&lt;=6}=span{1,Q,R},

rho_a(S) intersect B_{&lt;=6}=span{1,rho_a(R)}  for a!=0.
```

Take any word formed from resonant factors and nonzero-weight factors whose
weights are all at least `19`, or all at most `-19`. Move every resonant factor
to the right using

```text
rho exp(D)=exp(rho D rho^(-1)) rho.
```

Conjugation by `rho` preserves local nilpotence and the weight of `D`, and the
resonant factors combine additively. Thus the word has the form

```text
Phi = U rho_a
```

with `U` still one-sided. Applying the window-separation lemma to the graded
algebra `rho_a(S)` gives

```text
Phi(S) intersect B_{&lt;=6}
  subset rho_a(S) intersect B_{&lt;=6}.
```

Consequently the generated algebra has transcendence degree at most two when
`a=0` and at most one when `a!=0`. This permits arbitrary interleaving and
noncommuting high-weight factors, not merely a resonant factor placed at one
end.

The same restricted orbit-minimality conclusion survives an arbitrary affine
source post-factor.

## Exact-intersection refinement

The main theorem gives the Lane 5 obstruction without deciding which of
`Q,R` survive. A sharper conclusion is available when the extremal
first-order layer is nondegenerate.

In the positive case let `e_0=min e_i`; in the negative case let
`e_0=max e_i`. Put

```text
D_* = sum_{e_i=e_0} c_i D_i.
```

If

```text
D_*(Q) notin S,       D_*(R) notin S,
```

then

```text
Phi(S) intersect B_{&lt;=6}=k.
```

Indeed, after the main theorem write `g=a+bQ+dR`. On the positive side a
nonzero `d` isolates `D_*(R)` at the lowest derivative weight; after `d=0`, a
nonzero `b` isolates `D_*(Q)`. On the negative side the same argument uses the
highest derivative weight in the reverse order.

For a unique extremal elementary monomial derivation, the exact three-point
common fiber proves both nonmembership conditions, so the intersection is
`k`. Repeated extremal weights reduce to a finite linear-independence problem
in the quotient by fiber-constant polynomials.

## Scope

The theorem permits arbitrary noncommuting compositions but requires all
nonzero weight shifts to lie strictly on the same side of the degree-six
window, apart from the completely controlled resonant family. Mixed
positive/negative sequences and factors with weights in `&#91;-18,18&#93;` remain the
first uncontrolled composition regimes. These are precisely the places where
ordered derivative-word weights can return to the degree-six window.
</code></pre>

<a id="source-8f65f57cf63282ce"></a>

## `research-notes/lane5-degree-budgets/one_sided_high_weight_semigroup.md`

<pre><code class="language-markdown">
# One-sided high-weight source-semigroup theorem

The canonical theorem and proof are now maintained in
&#91;`one_sided_high_weight_compositions.md`&#93;(one_sided_high_weight_compositions.md).
That note contains the abstract weight-window lemma, the noncommuting
one-sided source-group theorem, restricted orbit-minimality, resonant
interleaving, and the exact-intersection refinement.
</code></pre>

<a id="source-a1f41387252fe775"></a>

## `research-notes/lane5-degree-budgets/reduced_word_separation.output.json`

<pre><code class="language-json">
{
  "arbitrary_length_example": {
    "absolute_shifts": &#91;
      19,
      247,
      3211,
      41743
    &#93;,
    "length": 4,
    "signed_shifts": &#91;
      19,
      -247,
      3211,
      -41743
    &#93;,
    "terms_for_y_shear": &#91;
      {
        "monomial": "z^10",
        "shift": 19
      },
      {
        "monomial": "x^246",
        "shift": -247
      },
      {
        "monomial": "z^1606",
        "shift": 3211
      },
      {
        "monomial": "x^41742",
        "shift": -41743
      }
    &#93;
  },
  "conclusion": "Taylor no-return controls mixed-sign reduced words; full separation gives constant degree-six intersection, including arbitrary-length mixed-sign commuting words and a noncommuting triangular family.",
  "degree_bound": 6,
  "derivative_witnesses_distinct": &#91;
    "x^N*dQdy",
    "x^N*dRdy",
    "y^M*dQdz",
    "y^M*dRdz"
  &#93;,
  "fiber_witness_target": &#91;
    "-1/9",
    "-1/3",
    "3"
  &#93;,
  "nested_example": {
    "M": 21,
    "N": 132,
    "arithmetic_gap": 19,
    "d1": -133,
    "d2": 19,
    "minimum_shift_gap": 19
  },
  "status": "pass",
  "weight_width": 18
}
</code></pre>

<a id="source-9a583e6f9c47abec"></a>

## `research-notes/lane5-degree-budgets/resonant_weight_certificate.json`

<pre><code class="language-json">
{"conclusion":"For c=0 the degree-six intersection is span{1,Q,R}; for c!=0 it is span{1,sigma_c(R)}.","degree_bound":6,"field":"Q","minor_count":33,"parameter":"c","schema_version":1,"script":{"path":"resonant_weight_certificate.py","sha256":"4e5c5d517619af4804a6754370eac764eced54ce6177a6003037489eb53f1877"},"shear":"z -&gt; z + c*y^2","theorem_id":"lane5-resonant-z-plus-cy2-degree6","torus_weights":{"x":-1,"y":1,"z":2},"weight_interval":&#91;-6,12&#93;,"weights":&#91;{"columns":&#91;83&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"a3867eeb33c442602cefff618fd4ab96e72ed5aa9ccbc7daa926f087a027a3fe","degree":0,"pivot_local_columns":&#91;0&#93;,"rows":&#91;&#91;676,1&#93;&#93;,"selection_c":0,"selection_seed":0}&#93;,"monomials":&#91;&#91;6,0,0&#93;&#93;,"target_rank":1,"weight":-6},{"columns":&#91;80&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"f131c9ec1b0cb087f68d8b77afa647c4e488708e3c874d2bad256ca95d4afea9","degree":0,"pivot_local_columns":&#91;0&#93;,"rows":&#91;&#91;188,1&#93;&#93;,"selection_c":0,"selection_seed":0}&#93;,"monomials":&#91;&#91;5,0,0&#93;&#93;,"target_rank":1,"weight":-5},{"columns":&#91;74,82&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"451f39e1c6d1cd52199b3bbdb958bd6201ddd1cf1304436365b9f400b8fa47b3","degree":0,"pivot_local_columns":&#91;0,1&#93;,"rows":&#91;&#91;772,2&#93;,&#91;361,1&#93;&#93;,"selection_c":0,"selection_seed":0}&#93;,"monomials":&#91;&#91;4,0,0&#93;,&#91;5,1,0&#93;&#93;,"target_rank":2,"weight":-4},{"columns":&#91;64,77,81&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"ca3b300d4f2977d8384b7cde42c0c4a5074712bb068b2e808a9f9f3be471d726","degree":1,"pivot_local_columns":&#91;0,1,2&#93;,"rows":&#91;&#91;463,2&#93;,&#91;417,2&#93;,&#91;701,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"6af3fe52caa101efcbc17f8d1cf9fbdb9f30e5b8d5822bcb48dc71d9fcb81102","degree":1,"pivot_local_columns":&#91;0,1,2&#93;,"rows":&#91;&#91;479,1&#93;,&#91;145,1&#93;,&#91;723,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;3,0,0&#93;,&#91;4,1,0&#93;,&#91;5,0,1&#93;&#93;,"target_rank":3,"weight":-3},{"columns":&#91;49,68,75,79&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"5e807972e89b75b1f22f8b12bed78193aa8787b7f3e234ffe5ed135eea49c8f8","degree":0,"pivot_local_columns":&#91;0,1,2,3&#93;,"rows":&#91;&#91;37,1&#93;,&#91;454,2&#93;,&#91;712,2&#93;,&#91;698,2&#93;&#93;,"selection_c":0,"selection_seed":0}&#93;,"monomials":&#91;&#91;2,0,0&#93;,&#91;3,1,0&#93;,&#91;4,0,1&#93;,&#91;4,2,0&#93;&#93;,"target_rank":4,"weight":-2},{"columns":&#91;28,54,65,71,78&#93;,"expected_kernel":"span{sigma_c(R)}","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"0f22d09e9468b2c26265ae8bb0e66e9332cf6007e68ce09c8d8807cc144b63a8","degree":1,"pivot_local_columns":&#91;0,1,3,4&#93;,"rows":&#91;&#91;356,1&#93;,&#91;639,1&#93;,&#91;663,1&#93;,&#91;243,2&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"05b781c5ef8f38b1390c95848b692d3be9508d002ea0cc37ba2bbd6fc45e1c6a","degree":1,"pivot_local_columns":&#91;0,1,3,4&#93;,"rows":&#91;&#91;583,1&#93;,&#91;815,1&#93;,&#91;261,2&#93;,&#91;389,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;1,0,0&#93;,&#91;2,1,0&#93;,&#91;3,0,1&#93;,&#91;3,2,0&#93;,&#91;4,1,1&#93;&#93;,"target_rank":4,"weight":-1},{"columns":&#91;0,34,50,58,69,73,76&#93;,"expected_kernel":"span{1}","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"b1904dcd4eac2e6e9330f0f17b45948c04214af7b30bf90e7a1231510f08089e","degree":2,"pivot_local_columns":&#91;1,2,3,4,5,6&#93;,"rows":&#91;&#91;839,1&#93;,&#91;202,1&#93;,&#91;700,1&#93;,&#91;194,1&#93;,&#91;494,2&#93;,&#91;125,2&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"c58e23b79fa2d7c60ad0922317c3ab1ab74e1db7829e2bfd7e05278ca37f15d7","degree":2,"pivot_local_columns":&#91;1,2,3,4,5,6&#93;,"rows":&#91;&#91;603,1&#93;,&#91;403,2&#93;,&#91;671,1&#93;,&#91;19,2&#93;,&#91;107,2&#93;,&#91;793,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,0&#93;,&#91;1,1,0&#93;,&#91;2,0,1&#93;,&#91;2,2,0&#93;,&#91;3,1,1&#93;,&#91;3,3,0&#93;,&#91;4,0,2&#93;&#93;,"target_rank":6,"weight":0},{"columns":&#91;7,29,39,55,61,66,72&#93;,"expected_kernel":"span{Q} at c=0, zero for c!=0","expected_minor_gcd":"c","minors":&#91;{"c_order":1,"coefficient_sha256":"1ccd4bff23fae28b9bfe7c3ebe6904c88fefc754e90e1c9724870440052a7e8f","degree":1,"pivot_local_columns":&#91;0,1,2,3,4,5,6&#93;,"rows":&#91;&#91;105,1&#93;,&#91;24,2&#93;,&#91;809,1&#93;,&#91;536,1&#93;,&#91;573,2&#93;,&#91;372,1&#93;,&#91;468,1&#93;&#93;,"selection_c":1,"selection_seed":0}&#93;,"monomials":&#91;&#91;0,1,0&#93;,&#91;1,0,1&#93;,&#91;1,2,0&#93;,&#91;2,1,1&#93;,&#91;2,3,0&#93;,&#91;3,0,2&#93;,&#91;3,2,1&#93;&#93;,"target_rank":7,"weight":1},{"columns":&#91;1,13,35,43,51,59,63,70&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"1178a352c833afc1c8338f8dccc55061a1861e721bc3e8447fdfc81ff2688276","degree":2,"pivot_local_columns":&#91;0,1,2,3,4,5,6,7&#93;,"rows":&#91;&#91;318,2&#93;,&#91;451,2&#93;,&#91;198,1&#93;,&#91;674,2&#93;,&#91;77,1&#93;,&#91;368,2&#93;,&#91;718,2&#93;,&#91;766,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"2861522b26145ff9724422b37d25666fd3bf45fc1154b3ada298eba2454b4f46","degree":2,"pivot_local_columns":&#91;0,1,2,3,4,5,6,7&#93;,"rows":&#91;&#91;47,1&#93;,&#91;546,1&#93;,&#91;567,1&#93;,&#91;22,2&#93;,&#91;109,2&#93;,&#91;278,1&#93;,&#91;35,1&#93;,&#91;468,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,1&#93;,&#91;0,2,0&#93;,&#91;1,1,1&#93;,&#91;1,3,0&#93;,&#91;2,0,2&#93;,&#91;2,2,1&#93;,&#91;2,4,0&#93;,&#91;3,1,2&#93;&#93;,"target_rank":8,"weight":2},{"columns":&#91;8,18,30,40,46,56,62,67&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"663d0d4694bf4f98512f33dc7e56a30ca5329f3b396101a563b9b78d280b4552","degree":5,"pivot_local_columns":&#91;0,1,2,3,4,5,6,7&#93;,"rows":&#91;&#91;291,2&#93;,&#91;805,1&#93;,&#91;91,2&#93;,&#91;70,1&#93;,&#91;66,1&#93;,&#91;147,1&#93;,&#91;304,2&#93;,&#91;194,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"e6f0f9f50636203b43168702195cd3e2f29b8db01743669c8e80fcaa42512510","degree":5,"pivot_local_columns":&#91;0,1,2,3,4,5,6,7&#93;,"rows":&#91;&#91;230,2&#93;,&#91;596,1&#93;,&#91;285,1&#93;,&#91;647,2&#93;,&#91;840,2&#93;,&#91;455,1&#93;,&#91;833,1&#93;,&#91;115,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,1,1&#93;,&#91;0,3,0&#93;,&#91;1,0,2&#93;,&#91;1,2,1&#93;,&#91;1,4,0&#93;,&#91;2,1,2&#93;,&#91;2,3,1&#93;,&#91;3,0,3&#93;&#93;,"target_rank":8,"weight":3},{"columns":&#91;2,14,22,36,44,48,52,60&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"135de2c051e82ef83c96df21f2e0fe6dcffc5a9e066d6f3cca6c2ec349a212a9","degree":4,"pivot_local_columns":&#91;0,1,2,3,4,5,6,7&#93;,"rows":&#91;&#91;30,2&#93;,&#91;633,2&#93;,&#91;452,2&#93;,&#91;417,1&#93;,&#91;613,2&#93;,&#91;812,2&#93;,&#91;170,1&#93;,&#91;437,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"115dcf8e1bb5299f9467495aaa70beedcf19c124a6535f0b553beae0d106954e","degree":4,"pivot_local_columns":&#91;0,1,2,3,4,5,6,7&#93;,"rows":&#91;&#91;86,2&#93;,&#91;714,2&#93;,&#91;513,1&#93;,&#91;725,2&#93;,&#91;683,2&#93;,&#91;64,2&#93;,&#91;57,2&#93;,&#91;378,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,2&#93;,&#91;0,2,1&#93;,&#91;0,4,0&#93;,&#91;1,1,2&#93;,&#91;1,3,1&#93;,&#91;1,5,0&#93;,&#91;2,0,3&#93;,&#91;2,2,2&#93;&#93;,"target_rank":8,"weight":4},{"columns":&#91;9,19,25,31,41,47,57&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"273bfac33c60085127228bd3fd8409934d14acdd646b534f4476a07bd2b3dc18","degree":6,"pivot_local_columns":&#91;0,1,2,3,4,5,6&#93;,"rows":&#91;&#91;775,2&#93;,&#91;25,2&#93;,&#91;74,1&#93;,&#91;673,2&#93;,&#91;102,1&#93;,&#91;569,2&#93;,&#91;662,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"f781af52d3f833dace0c202f26e797fa9ae2cc56d576066cce6124dc66b44a32","degree":6,"pivot_local_columns":&#91;0,1,2,3,4,5,6&#93;,"rows":&#91;&#91;330,2&#93;,&#91;4,2&#93;,&#91;722,1&#93;,&#91;469,2&#93;,&#91;236,1&#93;,&#91;123,2&#93;,&#91;750,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,1,2&#93;,&#91;0,3,1&#93;,&#91;0,5,0&#93;,&#91;1,0,3&#93;,&#91;1,2,2&#93;,&#91;1,4,1&#93;,&#91;2,1,3&#93;&#93;,"target_rank":7,"weight":5},{"columns":&#91;3,15,23,27,37,45,53&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"31017a33cdd9cc4dfb038aa1aa8758a43451792c103ed4ccd6313ee79befbe6c","degree":8,"pivot_local_columns":&#91;0,1,2,3,4,5,6&#93;,"rows":&#91;&#91;293,2&#93;,&#91;482,2&#93;,&#91;846,2&#93;,&#91;466,2&#93;,&#91;315,1&#93;,&#91;193,2&#93;,&#91;847,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"ba5759c6561cad908893020cd84681bd9c6a5c6f544bc256576623a388484f8e","degree":8,"pivot_local_columns":&#91;0,1,2,3,4,5,6&#93;,"rows":&#91;&#91;116,1&#93;,&#91;598,2&#93;,&#91;367,2&#93;,&#91;209,1&#93;,&#91;565,2&#93;,&#91;821,2&#93;,&#91;458,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,3&#93;,&#91;0,2,2&#93;,&#91;0,4,1&#93;,&#91;0,6,0&#93;,&#91;1,1,3&#93;,&#91;1,3,2&#93;,&#91;2,0,4&#93;&#93;,"target_rank":7,"weight":6},{"columns":&#91;10,20,26,32,42&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"bdc1c8cadb1977e388396d0090dc647381da2cd1f6e575b75243493ec274574a","degree":9,"pivot_local_columns":&#91;0,1,2,3,4&#93;,"rows":&#91;&#91;341,1&#93;,&#91;250,2&#93;,&#91;804,2&#93;,&#91;358,2&#93;,&#91;734,2&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"d48aa534c144e7ead9accdbba5248f7629b4b4b342e9dfd78a7aef11a569715e","degree":9,"pivot_local_columns":&#91;0,1,2,3,4&#93;,"rows":&#91;&#91;308,1&#93;,&#91;329,2&#93;,&#91;12,1&#93;,&#91;145,2&#93;,&#91;73,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,1,3&#93;,&#91;0,3,2&#93;,&#91;0,5,1&#93;,&#91;1,0,4&#93;,&#91;1,2,3&#93;&#93;,"target_rank":5,"weight":7},{"columns":&#91;4,16,24,38&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"06d8b067d5c38d485814527c115a0f090a53489cc9c9aa39708f0bb5fa7fbfcc","degree":10,"pivot_local_columns":&#91;0,1,2,3&#93;,"rows":&#91;&#91;736,2&#93;,&#91;666,2&#93;,&#91;220,2&#93;,&#91;83,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"1bf19ad775e3cfce040f44da4243401ff044fea4454b7a222262cbc7f9681ecd","degree":10,"pivot_local_columns":&#91;0,1,2,3&#93;,"rows":&#91;&#91;170,1&#93;,&#91;628,1&#93;,&#91;484,2&#93;,&#91;575,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,4&#93;,&#91;0,2,3&#93;,&#91;0,4,2&#93;,&#91;1,1,4&#93;&#93;,"target_rank":4,"weight":8},{"columns":&#91;11,21,33&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"3f64614b5b39af6bf780f7ceb4add0d3a3c8b4da6fd00e9824478ad3a30bf44f","degree":11,"pivot_local_columns":&#91;0,1,2&#93;,"rows":&#91;&#91;97,1&#93;,&#91;763,2&#93;,&#91;696,2&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"6ce2a29af069e055a8db0a34633f15cf7bdad2324186d7a32b0ba67958c3020e","degree":11,"pivot_local_columns":&#91;0,1,2&#93;,"rows":&#91;&#91;832,1&#93;,&#91;686,1&#93;,&#91;579,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,1,4&#93;,&#91;0,3,3&#93;,&#91;1,0,5&#93;&#93;,"target_rank":3,"weight":9},{"columns":&#91;5,17&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"4706dbb6991c95a408ba5f0e6bff263720ab3e1d96ea8f9120d5b7cdab8070d2","degree":8,"pivot_local_columns":&#91;0,1&#93;,"rows":&#91;&#91;526,2&#93;,&#91;60,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"5c26020b1282df8b3a7fa21382119ecb0de3ad921daa9c98fbb83a0e4a0e33ca","degree":8,"pivot_local_columns":&#91;0,1&#93;,"rows":&#91;&#91;762,1&#93;,&#91;626,1&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,5&#93;,&#91;0,2,4&#93;&#93;,"target_rank":2,"weight":10},{"columns":&#91;12&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"340544b804dc0c837272d1eb25ab85588eb42877e34b784a87ef8755a1f5d850","degree":5,"pivot_local_columns":&#91;0&#93;,"rows":&#91;&#91;105,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"6fb57df92295853e08b9b844c18470edf43c6c050c3a22532240c2072c67e7df","degree":5,"pivot_local_columns":&#91;0&#93;,"rows":&#91;&#91;32,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,1,5&#93;&#93;,"target_rank":1,"weight":11},{"columns":&#91;6&#93;,"expected_kernel":"zero","expected_minor_gcd":"1","minors":&#91;{"c_order":0,"coefficient_sha256":"782182f0c7379fe51c59e20f760617b9c1e2e9e225cd8297fcff7045b8e56d26","degree":6,"pivot_local_columns":&#91;0&#93;,"rows":&#91;&#91;556,1&#93;&#93;,"selection_c":0,"selection_seed":0},{"c_order":0,"coefficient_sha256":"e9f87da85178b07ca64b610a6f43b92450894f354d5a74c34f9b078046345926","degree":6,"pivot_local_columns":&#91;0&#93;,"rows":&#91;&#91;620,2&#93;&#93;,"selection_c":0,"selection_seed":1}&#93;,"monomials":&#91;&#91;0,0,6&#93;&#93;,"target_rank":1,"weight":12}&#93;}
</code></pre>

<a id="source-2763d2393fd2e4b7"></a>

## `research-notes/lane5-degree-budgets/resonant_weight_certificate.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the resonant Lane 5 family z -&gt; z + c*y^2 exactly over Q&#91;c&#93;.

The source torus weights are wt(x)=-1, wt(y)=1, wt(z)=2, so this shear is
weight preserving.  The degree-at-most-six source space splits into 19 small
weight spaces.  For each weight, the certificate supplies one or two exact
rational collision minors.  Their gcd over Q&#91;c&#93; is 1, except in weight 1 where
it is c.  This proves that the only degree-six fiber-constant polynomials are

    span{1,Q,R}                  when c = 0,
    span{1, sigma_c(R)}          when c != 0.

The standard c=0 equality is separately pinned by
standard_filtration_certificate.py.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from standard_filtration_certificate import (
    monomials_degree_at_most,
    split_target,
)

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "resonant_weight_certificate.json"
BOUND = 6
MONOMIALS = monomials_degree_at_most(BOUND)


def candidate_points() -&gt; list&#91;tuple&#91;tuple&#91;Fraction, Fraction, Fraction&#93;, ...&#93;&#93;:
    candidates = &#91;&#93;
    for h in (Fraction(1), Fraction(2), Fraction(3)):
        for a in range(-12, 1):
            for b in range(-12, 2):
                for sign in (1, -1):
                    try:
                        _, points = split_target(Fraction(a), Fraction(b), h, sign)
                    except (ValueError, ZeroDivisionError):
                        continue
                    candidates.append(points)
    return candidates


def determinant(matrix: list&#91;list&#91;Fraction&#93;&#93;) -&gt; Fraction:
    work = &#91;&#91;Fraction(entry) for entry in row&#93; for row in matrix&#93;
    size = len(work)
    value = Fraction(1)
    sign = 1
    for column in range(size):
        pivot_row = next(
            (row for row in range(column, size) if work&#91;row&#93;&#91;column&#93;), None
        )
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != column:
            work&#91;column&#93;, work&#91;pivot_row&#93; = work&#91;pivot_row&#93;, work&#91;column&#93;
            sign = -sign
        pivot = work&#91;column&#93;&#91;column&#93;
        value *= pivot
        for row in range(column + 1, size):
            if not work&#91;row&#93;&#91;column&#93;:
                continue
            factor = work&#91;row&#93;&#91;column&#93; / pivot
            for offset in range(column + 1, size):
                work&#91;row&#93;&#91;offset&#93; -= factor * work&#91;column&#93;&#91;offset&#93;
            work&#91;row&#93;&#91;column&#93; = 0
    return sign * value


def evaluate_columns(
    point: tuple&#91;Fraction, Fraction, Fraction&#93;,
    columns: list&#91;int&#93;,
    parameter: int,
) -&gt; list&#91;Fraction&#93;:
    x, y, z = point
    transformed_z = z - parameter * y**2
    return &#91;
        x**i * y**j * transformed_z**k
        for i, j, k in (MONOMIALS&#91;column&#93; for column in columns)
    &#93;


def interpolate_consecutive(values: list&#91;Fraction&#93;) -&gt; list&#91;Fraction&#93;:
    """Interpolate f(0),...,f(d) in the monomial basis over Q."""
    differences = &#91;Fraction(value) for value in values&#93;
    leading_differences = &#91;&#93;
    while differences:
        leading_differences.append(differences&#91;0&#93;)
        differences = &#91;
            differences&#91;index + 1&#93; - differences&#91;index&#93;
            for index in range(len(differences) - 1)
        &#93;

    coefficients = &#91;Fraction(0)&#93; * len(values)
    falling_factorial = &#91;Fraction(1)&#93;
    factorial = 1
    for degree, difference in enumerate(leading_differences):
        if degree:
            updated = &#91;Fraction(0)&#93; * (len(falling_factorial) + 1)
            for index, coefficient in enumerate(falling_factorial):
                updated&#91;index&#93; -= (degree - 1) * coefficient
                updated&#91;index + 1&#93; += coefficient
            falling_factorial = updated
            factorial *= degree
        scale = difference / factorial
        for index, coefficient in enumerate(falling_factorial):
            coefficients&#91;index&#93; += scale * coefficient
    return trim(coefficients)


def trim(poly: list&#91;Fraction&#93;) -&gt; list&#91;Fraction&#93;:
    result = &#91;Fraction(value) for value in poly&#93;
    while len(result) &gt; 1 and result&#91;-1&#93; == 0:
        result.pop()
    return result


def monic(poly: list&#91;Fraction&#93;) -&gt; list&#91;Fraction&#93;:
    result = trim(poly)
    if result == &#91;0&#93;:
        return result
    return &#91;coefficient / result&#91;-1&#93; for coefficient in result&#93;


def divide(
    dividend: list&#91;Fraction&#93;, divisor: list&#91;Fraction&#93;
) -&gt; tuple&#91;list&#91;Fraction&#93;, list&#91;Fraction&#93;&#93;:
    remainder = trim(dividend)
    divisor = trim(divisor)
    if divisor == &#91;0&#93;:
        raise ZeroDivisionError
    quotient = &#91;Fraction(0)&#93; * max(1, len(remainder) - len(divisor) + 1)
    while remainder != &#91;0&#93; and len(remainder) &gt;= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder&#91;-1&#93; / divisor&#91;-1&#93;
        quotient&#91;shift&#93; = coefficient
        for index, value in enumerate(divisor):
            remainder&#91;index + shift&#93; -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def gcd(left: list&#91;Fraction&#93;, right: list&#91;Fraction&#93;) -&gt; list&#91;Fraction&#93;:
    left, right = trim(left), trim(right)
    while right != &#91;0&#93;:
        _, remainder = divide(left, right)
        left, right = right, remainder
    return monic(left)


def coefficient_hash(poly: list&#91;Fraction&#93;) -&gt; str:
    payload = json.dumps(
        &#91;str(value) for value in trim(poly)&#93;, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def c_order(poly: list&#91;Fraction&#93;) -&gt; int:
    return next(index for index, value in enumerate(poly) if value)


def expected_gcd(value: str) -&gt; list&#91;Fraction&#93;:
    if value == "1":
        return &#91;Fraction(1)&#93;
    if value == "c":
        return &#91;Fraction(0), Fraction(1)&#93;
    raise ValueError(f"unsupported expected gcd: {value}")


def verify() -&gt; dict&#91;str, object&#93;:
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if certificate&#91;"degree_bound"&#93; != BOUND:
        raise AssertionError("degree bound changed")
    candidates = candidate_points()
    weights = &#91;&#93;

    for entry in certificate&#91;"weights"&#93;:
        weight = int(entry&#91;"weight"&#93;)
        columns = &#91;int(value) for value in entry&#91;"columns"&#93;&#93;
        gcd_poly: list&#91;Fraction&#93; | None = None

        for minor in entry&#91;"minors"&#93;:
            local_pivots = &#91;int(value) for value in minor&#91;"pivot_local_columns"&#93;&#93;
            selected_columns = &#91;columns&#91;index&#93; for index in local_pivots&#93;
            degree_bound = sum(MONOMIALS&#91;column&#93;&#91;2&#93; for column in selected_columns)
            determinant_values = &#91;&#93;

            for parameter in range(degree_bound + 1):
                matrix = &#91;&#93;
                for candidate_index, pair in minor&#91;"rows"&#93;:
                    points = candidates&#91;int(candidate_index)&#93;
                    first = evaluate_columns(points&#91;0&#93;, selected_columns, parameter)
                    second = evaluate_columns(
                        points&#91;int(pair)&#93;, selected_columns, parameter
                    )
                    matrix.append(
                        &#91;left - right for left, right in zip(first, second)&#93;
                    )
                determinant_values.append(determinant(matrix))

            polynomial = interpolate_consecutive(determinant_values)
            if len(polynomial) - 1 != int(minor&#91;"degree"&#93;):
                raise AssertionError(f"weight {weight}: determinant degree changed")
            if c_order(polynomial) != int(minor&#91;"c_order"&#93;):
                raise AssertionError(f"weight {weight}: c-order changed")
            if coefficient_hash(polynomial) != minor&#91;"coefficient_sha256"&#93;:
                raise AssertionError(f"weight {weight}: determinant changed")
            gcd_poly = (
                monic(polynomial)
                if gcd_poly is None
                else gcd(gcd_poly, polynomial)
            )

        expected = expected_gcd(entry&#91;"expected_minor_gcd"&#93;)
        if gcd_poly != expected:
            raise AssertionError(f"weight {weight}: minor gcd changed")

        weights.append(
            {
                "weight": weight,
                "dimension": len(columns),
                "target_rank": int(entry&#91;"target_rank"&#93;),
                "minor_count": len(entry&#91;"minors"&#93;),
                "minor_gcd": entry&#91;"expected_minor_gcd"&#93;,
            }
        )

    return {
        "status": "pass",
        "weight_count": len(weights),
        "minor_count": sum(item&#91;"minor_count"&#93; for item in weights),
        "weights": weights,
        "conclusion": certificate&#91;"conclusion"&#93;,
    }


def main() -&gt; int:
    print(json.dumps(verify(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-5dd4e35e012d9761"></a>

## `research-notes/lane5-degree-budgets/standard_filtration_certificate.json`

<pre><code class="language-json">
{"characteristic_extension":"every characteristic-zero field by base change","conclusion":"Q&#91;P,Q,R&#93; intersect Q&#91;x,y,z&#93;_{&lt;=6} = span_Q{1,Q,R}; after base change the same holds over every characteristic-zero field. Therefore k&#91;F_6 A&#93;=k&#91;Q,R&#93; and has transcendence degree two.","degree_bound":6,"exact_kernel_vectors":&#91;"1","Q","R"&#93;,"field":"Q","inverse_cubic":{"C":"27*p^2*r^2 - 18*p*q*r + 16*p + q^3*r - q^2","equation":"C(p,q,r)*x^3 + (4-3*q*r)*x - 2*r = 0"},"map":{"A":"1+x*y","P":"A^3*z + y^2*A*(4+3*x*y)","Q":"y + 3*x*A^2*z + 3*x*y^2*(4+3*x*y)","R":"2*x - 3*x^2*y - x^3*z"},"monomial_order_description":&#91;"i=0..6","j=0..6-i","k=0..6-i-j","column is x^i*y^j*z^k"&#93;,"monomials":&#91;&#91;0,0,0&#93;,&#91;0,0,1&#93;,&#91;0,0,2&#93;,&#91;0,0,3&#93;,&#91;0,0,4&#93;,&#91;0,0,5&#93;,&#91;0,0,6&#93;,&#91;0,1,0&#93;,&#91;0,1,1&#93;,&#91;0,1,2&#93;,&#91;0,1,3&#93;,&#91;0,1,4&#93;,&#91;0,1,5&#93;,&#91;0,2,0&#93;,&#91;0,2,1&#93;,&#91;0,2,2&#93;,&#91;0,2,3&#93;,&#91;0,2,4&#93;,&#91;0,3,0&#93;,&#91;0,3,1&#93;,&#91;0,3,2&#93;,&#91;0,3,3&#93;,&#91;0,4,0&#93;,&#91;0,4,1&#93;,&#91;0,4,2&#93;,&#91;0,5,0&#93;,&#91;0,5,1&#93;,&#91;0,6,0&#93;,&#91;1,0,0&#93;,&#91;1,0,1&#93;,&#91;1,0,2&#93;,&#91;1,0,3&#93;,&#91;1,0,4&#93;,&#91;1,0,5&#93;,&#91;1,1,0&#93;,&#91;1,1,1&#93;,&#91;1,1,2&#93;,&#91;1,1,3&#93;,&#91;1,1,4&#93;,&#91;1,2,0&#93;,&#91;1,2,1&#93;,&#91;1,2,2&#93;,&#91;1,2,3&#93;,&#91;1,3,0&#93;,&#91;1,3,1&#93;,&#91;1,3,2&#93;,&#91;1,4,0&#93;,&#91;1,4,1&#93;,&#91;1,5,0&#93;,&#91;2,0,0&#93;,&#91;2,0,1&#93;,&#91;2,0,2&#93;,&#91;2,0,3&#93;,&#91;2,0,4&#93;,&#91;2,1,0&#93;,&#91;2,1,1&#93;,&#91;2,1,2&#93;,&#91;2,1,3&#93;,&#91;2,2,0&#93;,&#91;2,2,1&#93;,&#91;2,2,2&#93;,&#91;2,3,0&#93;,&#91;2,3,1&#93;,&#91;2,4,0&#93;,&#91;3,0,0&#93;,&#91;3,0,1&#93;,&#91;3,0,2&#93;,&#91;3,0,3&#93;,&#91;3,1,0&#93;,&#91;3,1,1&#93;,&#91;3,1,2&#93;,&#91;3,2,0&#93;,&#91;3,2,1&#93;,&#91;3,3,0&#93;,&#91;4,0,0&#93;,&#91;4,0,1&#93;,&#91;4,0,2&#93;,&#91;4,1,0&#93;,&#91;4,1,1&#93;,&#91;4,2,0&#93;,&#91;5,0,0&#93;,&#91;5,0,1&#93;,&#91;5,1,0&#93;,&#91;6,0,0&#93;&#93;,"nonpivot_columns":&#91;0,65,72&#93;,"nonpivot_monomials":&#91;&#91;0,0,0&#93;,&#91;3,0,1&#93;,&#91;3,2,1&#93;&#93;,"pivot_columns":&#91;1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,73,74,75,76,77,78,79,80,81,82,83&#93;,"pivot_minor_determinant_mod_prime":214012,"prime":1000003,"rank":81,"schema_version":1,"scope":"This is the standard source-coordinate filtration only. It is not a theorem for arbitrary polynomial source automorphisms.","script":{"path":"standard_filtration_certificate.py","sha256":"942e3ff34aa09032ef70b410ebf6ee87595d0a4c2669ff48fdac3f2f917fb9df"},"selected_rows":&#91;{"a":"-12","b":"-11","h":"1","pair":1,"sign":1},{"a":"-12","b":"-11","h":"1","pair":2,"sign":1},{"a":"-12","b":"-11","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-11","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-10","h":"1","pair":1,"sign":1},{"a":"-12","b":"-10","h":"1","pair":2,"sign":1},{"a":"-12","b":"-10","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-10","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-9","h":"1","pair":1,"sign":1},{"a":"-12","b":"-9","h":"1","pair":2,"sign":1},{"a":"-12","b":"-9","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-9","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-8","h":"1","pair":1,"sign":1},{"a":"-12","b":"-8","h":"1","pair":2,"sign":1},{"a":"-12","b":"-8","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-8","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-7","h":"1","pair":1,"sign":1},{"a":"-12","b":"-7","h":"1","pair":2,"sign":1},{"a":"-12","b":"-7","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-7","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-6","h":"1","pair":1,"sign":1},{"a":"-12","b":"-6","h":"1","pair":2,"sign":1},{"a":"-12","b":"-6","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-6","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-5","h":"1","pair":1,"sign":1},{"a":"-12","b":"-5","h":"1","pair":2,"sign":1},{"a":"-12","b":"-5","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-5","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-4","h":"1","pair":1,"sign":1},{"a":"-12","b":"-4","h":"1","pair":2,"sign":1},{"a":"-12","b":"-4","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-4","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-3","h":"1","pair":1,"sign":1},{"a":"-12","b":"-3","h":"1","pair":2,"sign":1},{"a":"-12","b":"-3","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-3","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-2","h":"1","pair":1,"sign":1},{"a":"-12","b":"-2","h":"1","pair":2,"sign":1},{"a":"-12","b":"-2","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-2","h":"1","pair":2,"sign":-1},{"a":"-12","b":"-1","h":"1","pair":1,"sign":1},{"a":"-12","b":"-1","h":"1","pair":2,"sign":1},{"a":"-12","b":"-1","h":"1","pair":1,"sign":-1},{"a":"-12","b":"-1","h":"1","pair":2,"sign":-1},{"a":"-12","b":"1","h":"1","pair":1,"sign":1},{"a":"-12","b":"1","h":"1","pair":2,"sign":1},{"a":"-12","b":"1","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-10","h":"1","pair":1,"sign":1},{"a":"-11","b":"-10","h":"1","pair":2,"sign":1},{"a":"-11","b":"-10","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-10","h":"1","pair":2,"sign":-1},{"a":"-11","b":"-9","h":"1","pair":1,"sign":1},{"a":"-11","b":"-9","h":"1","pair":2,"sign":1},{"a":"-11","b":"-9","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-9","h":"1","pair":2,"sign":-1},{"a":"-11","b":"-8","h":"1","pair":1,"sign":1},{"a":"-11","b":"-8","h":"1","pair":2,"sign":1},{"a":"-11","b":"-8","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-8","h":"1","pair":2,"sign":-1},{"a":"-11","b":"-7","h":"1","pair":1,"sign":1},{"a":"-11","b":"-7","h":"1","pair":2,"sign":1},{"a":"-11","b":"-7","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-7","h":"1","pair":2,"sign":-1},{"a":"-11","b":"-6","h":"1","pair":1,"sign":1},{"a":"-11","b":"-6","h":"1","pair":2,"sign":1},{"a":"-11","b":"-6","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-6","h":"1","pair":2,"sign":-1},{"a":"-11","b":"-5","h":"1","pair":1,"sign":1},{"a":"-11","b":"-5","h":"1","pair":2,"sign":1},{"a":"-11","b":"-5","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-5","h":"1","pair":2,"sign":-1},{"a":"-11","b":"-4","h":"1","pair":1,"sign":1},{"a":"-11","b":"-4","h":"1","pair":2,"sign":1},{"a":"-11","b":"-4","h":"1","pair":1,"sign":-1},{"a":"-11","b":"-4","h":"1","pair":2,"sign":-1},{"a":"-10","b":"-9","h":"1","pair":1,"sign":1},{"a":"-10","b":"-9","h":"1","pair":2,"sign":1},{"a":"-12","b":"-11","h":"2","pair":1,"sign":1},{"a":"-12","b":"-11","h":"2","pair":2,"sign":1},{"a":"-12","b":"-11","h":"2","pair":1,"sign":-1},{"a":"-12","b":"-10","h":"2","pair":1,"sign":1}&#93;,"theorem_id":"lane5-standard-source-filtration-degree6"}
</code></pre>

<a id="source-c9dee41efc8efea6"></a>

## `research-notes/lane5-degree-budgets/standard_filtration_certificate.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the Lane 5 standard-source degree-six fiber certificate.

The script uses only Python's standard library.  It reconstructs rational
split fibers of the displayed Keller map, forms the evaluation-difference
matrix on all source monomials of total degree at most six, checks an 81 x 81
minor modulo a prime, and verifies the exact kernel vectors 1, Q, and R.

A nonzero modular minor is also a nonzero rational minor.  Since every element
of k&#91;P,Q,R&#93; is constant on each displayed fiber pair, the certificate proves
over every characteristic-zero field k that

    k&#91;P,Q,R&#93; intersect k&#91;x,y,z&#93;_{&lt;=6} = span_k{1,Q,R}.

Consequently the algebra generated by the standard degree-six filtered piece
is k&#91;Q,R&#93; and has transcendence degree two.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "standard_filtration_certificate.json"


def q(value: object) -&gt; Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def monomials_degree_at_most(bound: int) -&gt; list&#91;tuple&#91;int, int, int&#93;&#93;:
    return &#91;
        (i, j, k)
        for i in range(bound + 1)
        for j in range(bound + 1 - i)
        for k in range(bound + 1 - i - j)
    &#93;


def map_f(point: tuple&#91;Fraction, Fraction, Fraction&#93;) -&gt; tuple&#91;Fraction, Fraction, Fraction&#93;:
    x, y, z = map(q, point)
    a = 1 + x * y
    p = a**3 * z + y**2 * a * (4 + 3 * x * y)
    qq = y + 3 * x * a**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    r = 2 * x - 3 * x**2 * y - x**3 * z
    return p, qq, r


def inverse_point(
    x: Fraction, p: Fraction, qq: Fraction, r: Fraction
) -&gt; tuple&#91;Fraction, Fraction, Fraction&#93;:
    """Recover a source point from a root x of the inverse cubic."""
    x, p, qq, r = map(q, (x, p, qq, r))
    denominator = x * (4 - 3 * qq * r) - 3 * r
    if x == 0 or denominator == 0:
        raise ZeroDivisionError("inverse chart denominator vanishes")
    t = x * ((qq - 9 * p * r) * x - 2) / denominator
    y = (t - 1) / x
    z = (2 * x - 3 * x * x * y - r) / x**3
    return x, y, z


def split_target(
    a: Fraction, b: Fraction, h: Fraction, sign: int
) -&gt; tuple&#91;
    tuple&#91;Fraction, Fraction, Fraction&#93;,
    tuple&#91;
        tuple&#91;Fraction, Fraction, Fraction&#93;,
        tuple&#91;Fraction, Fraction, Fraction&#93;,
        tuple&#91;Fraction, Fraction, Fraction&#93;,
    &#93;,
&#93;:
    """Construct a rational target whose inverse cubic has roots a,b,-a-b."""
    a, b, h = map(q, (a, b, h))
    c = -a - b
    if h == 0 or 0 in (a, b, c) or len({a, b, c}) != 3:
        raise ValueError("roots must be nonzero and distinct")
    s2 = a * b + a * c + b * c
    s3 = a * b * c
    cubic_lead = -h * h
    r = cubic_lead * s3 / 2
    if r == 0:
        raise ValueError("r vanishes")
    qq = (4 - cubic_lead * s2) / (3 * r)
    delta = (a - b) * (a - c) * (b - c)
    linear_coefficient = 16 - 18 * qq * r
    p = (-linear_coefficient + sign * h**3 * delta) / (54 * r**2)

    recovered_lead = (
        27 * p**2 * r**2 - 18 * p * qq * r + 16 * p + qq**3 * r - qq**2
    )
    if recovered_lead != cubic_lead:
        raise AssertionError("target does not have the prescribed inverse cubic")

    target = (p, qq, r)
    points = tuple(inverse_point(root, *target) for root in (a, b, c))
    if any(map_f(point) != target for point in points):
        raise AssertionError("recovered point does not map to the target")
    return target, points  # type: ignore&#91;return-value&#93;


def evaluate_monomials(
    point: tuple&#91;Fraction, Fraction, Fraction&#93;,
    monomials: list&#91;tuple&#91;int, int, int&#93;&#93;,
    bound: int,
) -&gt; list&#91;Fraction&#93;:
    x, y, z = point
    xp = &#91;Fraction(1)&#93;
    yp = &#91;Fraction(1)&#93;
    zp = &#91;Fraction(1)&#93;
    for _ in range(bound):
        xp.append(xp&#91;-1&#93; * x)
        yp.append(yp&#91;-1&#93; * y)
        zp.append(zp&#91;-1&#93; * z)
    return &#91;xp&#91;i&#93; * yp&#91;j&#93; * zp&#91;k&#93; for i, j, k in monomials&#93;


def row_from_descriptor(
    descriptor: dict&#91;str, object&#93;,
    monomials: list&#91;tuple&#91;int, int, int&#93;&#93;,
    bound: int,
) -&gt; list&#91;Fraction&#93;:
    _, points = split_target(
        Fraction(str(descriptor&#91;"a"&#93;)),
        Fraction(str(descriptor&#91;"b"&#93;)),
        Fraction(str(descriptor&#91;"h"&#93;)),
        int(descriptor&#91;"sign"&#93;),
    )
    pair = int(descriptor&#91;"pair"&#93;)
    first = evaluate_monomials(points&#91;0&#93;, monomials, bound)
    second = evaluate_monomials(points&#91;pair&#93;, monomials, bound)
    return &#91;u - v for u, v in zip(first, second)&#93;


def fraction_mod(value: Fraction, prime: int) -&gt; int:
    numerator = value.numerator % prime
    denominator = value.denominator % prime
    if denominator == 0:
        raise ZeroDivisionError("certificate denominator vanishes modulo prime")
    return numerator * pow(denominator, prime - 2, prime) % prime


def rank_and_pivots(matrix: list&#91;list&#91;int&#93;&#93;, prime: int) -&gt; tuple&#91;int, list&#91;int&#93;&#93;:
    work = &#91;&#91;entry % prime for entry in row&#93; for row in matrix&#93;
    rows = len(work)
    columns = len(work&#91;0&#93;)
    rank = 0
    pivots: list&#91;int&#93; = &#91;&#93;
    for column in range(columns):
        pivot_row = next(
            (index for index in range(rank, rows) if work&#91;index&#93;&#91;column&#93;), None
        )
        if pivot_row is None:
            continue
        work&#91;rank&#93;, work&#91;pivot_row&#93; = work&#91;pivot_row&#93;, work&#91;rank&#93;
        inverse = pow(work&#91;rank&#93;&#91;column&#93;, prime - 2, prime)
        work&#91;rank&#93; = &#91;entry * inverse % prime for entry in work&#91;rank&#93;&#93;
        for index in range(rows):
            if index == rank or not work&#91;index&#93;&#91;column&#93;:
                continue
            factor = work&#91;index&#93;&#91;column&#93;
            work&#91;index&#93; = &#91;
                (entry - factor * pivot) % prime
                for entry, pivot in zip(work&#91;index&#93;, work&#91;rank&#93;)
            &#93;
        pivots.append(column)
        rank += 1
        if rank == rows:
            break
    return rank, pivots


def determinant_mod(matrix: list&#91;list&#91;int&#93;&#93;, prime: int) -&gt; int:
    work = &#91;&#91;entry % prime for entry in row&#93; for row in matrix&#93;
    size = len(work)
    determinant = 1
    for column in range(size):
        pivot_row = next(
            (index for index in range(column, size) if work&#91;index&#93;&#91;column&#93;), None
        )
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work&#91;column&#93;, work&#91;pivot_row&#93; = work&#91;pivot_row&#93;, work&#91;column&#93;
            determinant = -determinant
        pivot = work&#91;column&#93;&#91;column&#93; % prime
        determinant = determinant * pivot % prime
        inverse = pow(pivot, prime - 2, prime)
        for index in range(column + 1, size):
            if not work&#91;index&#93;&#91;column&#93;:
                continue
            factor = work&#91;index&#93;&#91;column&#93; * inverse % prime
            for offset in range(column, size):
                work&#91;index&#93;&#91;offset&#93; = (
                    work&#91;index&#93;&#91;offset&#93; - factor * work&#91;column&#93;&#91;offset&#93;
                ) % prime
    return determinant % prime


def dot(left: Iterable&#91;Fraction&#93;, right: Iterable&#91;Fraction&#93;) -&gt; Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def kernel_vectors(
    monomials: list&#91;tuple&#91;int, int, int&#93;&#93;,
) -&gt; dict&#91;str, list&#91;Fraction&#93;&#93;:
    index = {monomial: position for position, monomial in enumerate(monomials)}
    vectors = {name: &#91;Fraction(0)&#93; * len(monomials) for name in ("1", "Q", "R")}
    vectors&#91;"1"&#93;&#91;index&#91;(0, 0, 0)&#93;&#93; = 1
    for monomial, coefficient in {
        (0, 1, 0): 1,
        (1, 0, 1): 3,
        (2, 1, 1): 6,
        (3, 2, 1): 3,
        (1, 2, 0): 12,
        (2, 3, 0): 9,
    }.items():
        vectors&#91;"Q"&#93;&#91;index&#91;monomial&#93;&#93; = coefficient
    for monomial, coefficient in {
        (1, 0, 0): 2,
        (2, 1, 0): -3,
        (3, 0, 1): -1,
    }.items():
        vectors&#91;"R"&#93;&#91;index&#91;monomial&#93;&#93; = coefficient
    return vectors


def verify(certificate: dict&#91;str, object&#93;) -&gt; dict&#91;str, object&#93;:
    bound = int(certificate&#91;"degree_bound"&#93;)
    prime = int(certificate&#91;"prime"&#93;)
    monomials = monomials_degree_at_most(bound)
    expected_monomials = &#91;list(item) for item in monomials&#93;
    if expected_monomials != certificate&#91;"monomials"&#93;:
        raise AssertionError("monomial order differs from the certificate")

    descriptors = certificate&#91;"selected_rows"&#93;
    if not isinstance(descriptors, list):
        raise TypeError("selected_rows must be a list")
    exact_rows = &#91;
        row_from_descriptor(descriptor, monomials, bound)
        for descriptor in descriptors
    &#93;
    modular_rows = &#91;
        &#91;fraction_mod(entry, prime) for entry in row&#93; for row in exact_rows
    &#93;
    rank, pivots = rank_and_pivots(modular_rows, prime)
    expected_pivots = &#91;int(value) for value in certificate&#91;"pivot_columns"&#93;&#93;
    if rank != int(certificate&#91;"rank"&#93;) or pivots != expected_pivots:
        raise AssertionError("modular rank or pivot columns changed")

    minor = &#91;&#91;row&#91;column&#93; for column in pivots&#93; for row in modular_rows&#93;
    determinant = determinant_mod(minor, prime)
    if determinant != int(certificate&#91;"pivot_minor_determinant_mod_prime"&#93;):
        raise AssertionError("pivot minor determinant changed")

    vectors = kernel_vectors(monomials)
    for name, vector in vectors.items():
        if any(dot(row, vector) != 0 for row in exact_rows):
            raise AssertionError(f"{name} is not in the exact rational kernel")

    nonpivots = &#91;
        column for column in range(len(monomials)) if column not in set(pivots)
    &#93;
    if nonpivots != &#91;int(value) for value in certificate&#91;"nonpivot_columns"&#93;&#93;:
        raise AssertionError("nonpivot columns changed")

    return {
        "status": "pass",
        "degree_bound": bound,
        "monomial_count": len(monomials),
        "row_count": len(exact_rows),
        "prime": prime,
        "rank": rank,
        "kernel_dimension": len(monomials) - rank,
        "pivot_minor_determinant_mod_prime": determinant,
        "exact_kernel_vectors_checked": list(vectors),
        "conclusion": certificate&#91;"conclusion"&#93;,
    }


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=CERTIFICATE,
        help="certificate JSON to verify",
    )
    args = parser.parse_args()
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = verify(certificate)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-9ec82063f46b1a95"></a>

## `research-notes/lane5-degree-budgets/verify_baseline_counterexample.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the determinant and rational collision of the baseline map.

This finite exact check establishes only the displayed polynomial identities.
It does not prove any filtration, automorphism, or minimum-degree statement.
"""

from __future__ import annotations

import sympy as sp


def main() -&gt; int:
    x, y, z = sp.symbols("x y z")
    frame = 1 + x * y
    p = sp.expand(frame**3 * z + y**2 * frame * (4 + 3 * x * y))
    q = sp.expand(y + 3 * x * frame**2 * z + 3 * x * y**2 * (4 + 3 * x * y))
    r = sp.expand(2 * x - 3 * x**2 * y - x**3 * z)

    determinant = sp.factor(sp.Matrix(&#91;p, q, r&#93;).jacobian(&#91;x, y, z&#93;).det())
    if determinant != -2:
        raise AssertionError(f"Jacobian determinant changed: {determinant}")

    points = (
        (sp.Integer(0), sp.Integer(0), -sp.Rational(1, 4)),
        (sp.Integer(1), -sp.Rational(3, 2), sp.Rational(13, 2)),
        (-sp.Integer(1), sp.Rational(3, 2), sp.Rational(13, 2)),
    )
    images = tuple(
        tuple(value.subs({x: px, y: py, z: pz}) for value in (p, q, r))
        for px, py, pz in points
    )
    expected = (-sp.Rational(1, 4), sp.Integer(0), sp.Integer(0))
    if any(image != expected for image in images):
        raise AssertionError(f"collision changed: {images}")
    if len(set(points)) != 3:
        raise AssertionError("the three source points are not distinct")

    print("baseline counterexample certificate: PASS")
    print("det J(P,Q,R) = -2")
    print(f"three distinct rational points map to {expected}")
    print("does not establish: filtration, orbit, or minimum-degree claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-b547c1e19853a679"></a>

## `research-notes/lane5-degree-budgets/verify_reduced_word_separation.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the numerical and fiber-witness claims in the mixed-sign theorem."""

from __future__ import annotations

import json
from fractions import Fraction

D = 6
WIDTH = 3 * D


def map_f(point: tuple&#91;Fraction, Fraction, Fraction&#93;):
    x, y, z = point
    a = 1 + x * y
    p = a**3 * z + y**2 * a * (4 + 3 * x * y)
    q = y + 3 * x * a**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    r = 2 * x - 3 * x**2 * y - x**3 * z
    return p, q, r


def derivatives(point: tuple&#91;Fraction, Fraction, Fraction&#93;):
    x, y, z = point
    qx = 3 * z + 12 * x * y * z + 9 * x**2 * y**2 * z + 12 * y**2 + 18 * x * y**3
    qy = 1 + 6 * x**2 * z + 6 * x**3 * y * z + 24 * x * y + 27 * x**2 * y**2
    qz = 3 * x * (1 + x * y) ** 2
    rx = 2 - 6 * x * y - 3 * x**2 * z
    ry = -3 * x**2
    rz = -x**3
    return qx, qy, qz, rx, ry, rz


def check_nested(N: int, M: int) -&gt; dict&#91;str, int&#93;:
    if N &lt; 18 or M &lt; 21:
        raise AssertionError("mixed-sign nested-family size hypotheses are not satisfied")
    d1 = -N - 1
    d2 = M - 2
    arithmetic_gap = min(
        abs(a * (N + 1) - b * (M - 2))
        for a in range(1, D + 1)
        for b in range(1, D + 1)
    )
    if arithmetic_gap &lt;= WIDTH:
        raise AssertionError("mixed-sign arithmetic nonresonance failed")
    minimum = None
    for a1 in range(D + 1):
        for a2 in range(D + 1):
            for b1 in range(D + 1):
                for b2 in range(D + 1):
                    if (a1, a2) == (b1, b2):
                        continue
                    value = abs((a1 - b1) * d1 + (a2 - b2) * d2)
                    minimum = value if minimum is None else min(minimum, value)
    if minimum is None or minimum &lt;= WIDTH:
        raise AssertionError("nested-family support is not separated")
    return {
        "N": N,
        "M": M,
        "d1": d1,
        "d2": d2,
        "arithmetic_gap": arithmetic_gap,
        "minimum_shift_gap": minimum,
    }


def superincreasing_shifts(length: int) -&gt; list&#91;int&#93;:
    shifts = &#91;19&#93;
    while len(shifts) &lt; length:
        shifts.append(12 * sum(shifts) + 19)
    return shifts


def check_superincreasing(length: int) -&gt; dict&#91;str, object&#93;:
    shifts = superincreasing_shifts(length)
    for index, shift in enumerate(shifts):
        if index == 0:
            if shift &lt;= WIDTH:
                raise AssertionError("first shift is too small")
        elif shift &lt;= 2 * D * sum(shifts&#91;:index&#93;) + WIDTH:
            raise AssertionError("superincreasing recurrence failed")
    signed = &#91;shift if index % 2 == 0 else -shift for index, shift in enumerate(shifts)&#93;
    terms = &#91;&#93;
    for shift in signed:
        if shift &gt; 0:
            terms.append({"monomial": f"z^{(shift + 1) // 2}", "shift": shift})
        else:
            terms.append({"monomial": f"x^{-shift - 1}", "shift": shift})
    return {
        "length": length,
        "absolute_shifts": shifts,
        "signed_shifts": signed,
        "terms_for_y_shear": terms,
    }


def main() -&gt; int:
    u = (Fraction(1), Fraction(-4, 3), Fraction(3))
    v = (Fraction(2), Fraction(1, 6), Fraction(-1, 8))
    if map_f(u) != map_f(v):
        raise AssertionError("common-fiber witness changed")
    qxu, qyu, qzu, rxu, ryu, rzu = derivatives(u)
    qxv, qyv, qzv, rxv, ryv, rzv = derivatives(v)

    M, N = 21, 132
    values = {
        "x^N*dQdy": (u&#91;0&#93; ** N * qyu, v&#91;0&#93; ** N * qyv),
        "x^N*dRdy": (u&#91;0&#93; ** N * ryu, v&#91;0&#93; ** N * ryv),
        "y^M*dQdz": (u&#91;1&#93; ** M * qzu, v&#91;1&#93; ** M * qzv),
        "y^M*dRdz": (u&#91;1&#93; ** M * rzu, v&#91;1&#93; ** M * rzv),
    }
    if any(left == right for left, right in values.values()):
        raise AssertionError("a derivative witness unexpectedly became fiber-constant")

    result = {
        "status": "pass",
        "degree_bound": D,
        "weight_width": WIDTH,
        "nested_example": check_nested(N, M),
        "arbitrary_length_example": check_superincreasing(4),
        "fiber_witness_target": &#91;str(value) for value in map_f(u)&#93;,
        "derivative_witnesses_distinct": list(values),
        "conclusion": (
            "Taylor no-return controls mixed-sign reduced words; full separation "
            "gives constant degree-six intersection, including arbitrary-length "
            "mixed-sign commuting words and a noncommuting triangular family."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

[Back to Lane 5](intrinsic-degree-valuative-budgets.md)
