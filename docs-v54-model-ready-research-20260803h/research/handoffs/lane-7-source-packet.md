# Lane 7 exact research source packet

This page exposes the proof notes, computation contracts, programs,
and finite inputs used by the focused lane brief. Each section names
its canonical repository path and source hash. No private checkout or
download is required.

## Included files

- [`research-notes/lane7-component-inputs-20260803-v1/README.md`](#source-867e4fccbf4a8d1c) — `8241282f6528aec7a6f79a9ba5cba3044f2c351e1b57dacff433c26dfa7e596f`
- [`research-notes/lane7-component-inputs-20260803-v1/build_component_bundle.py`](#source-0d5c024071f214a5) — `5c76818fa360d3f0bbf9ebf723f5091e301a051bcad2ea5777dabd74acc8339a`
- [`research-notes/lane7-component-inputs-20260803-v1/lane7_exact_component_bundle.json`](#source-8ac5c833df312401) — `6699a296a95d68d64653b1c39dd52866cef36361c50df13f258ef068b277907e`
- [`research-notes/lane7-component-inputs-20260803-v1/manifest.json`](#source-6dc9eb2635a2bed8) — `f1050edafa1802679db27e1ac8f036758fe5be297dc0a345e15ac822b569d96d`
- [`research-notes/lane7-component-inputs-20260803-v1/verify_component_bundle.py`](#source-03ebac2c2b77f766) — `9b7ef6d11825e537a35c7a89857690f8f305ec9c9c764c4fc5551acd1d077fc8`
- [`research-notes/lane7-projective-kernel-20260803-v1/README.md`](#source-740f2fbd37373ad8) — `d6675732ee52f61e4fb113d3c45521f5d8be557b4c2359a87fb2d93fa35970bd`
- [`research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_input.py`](#source-b555e0f9d637888f) — `3a5c8dd3c3aa5d57f2cbb139dad970f96c7c0eaf247b7978fef4d6c3db28dc87`
- [`research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_macaulay2.py`](#source-03cf56b8bd9c6caf) — `28778c1c2f0240ef6b8fbc3075eb8840361a491534ce4f5059197834563ff0e1`
- [`research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_singular.py`](#source-8b6128de9797b077) — `290697bd851eecc2509b09cf440966874cf51fc9c011dc1bd9fcc7fa69af5de7`
- [`research-notes/lane7-projective-kernel-20260803-v1/generate_macaulay2_input.py`](#source-279fc259f53bdbf9) — `5e417707876d39efc5f780ba95cff9f33c9f209b8b14b76a9484e70c12eaef01`
- [`research-notes/lane7-projective-kernel-20260803-v1/prepare_five_chart_runs.py`](#source-efcfe78f40b44e90) — `5f207a222cc03379033f778981471f9e0e7211b62913c3c009eef7c20ca3bf1c`
- [`research-notes/lane7-projective-kernel-20260803-v1/test_kernel_chart_macaulay2.py`](#source-ac8b7aff9c24d854) — `7d9c338cadaae22811ad4e40128b89c78a407d305dd3a8a9c25d6fcf8714bb3a`
- [`research-notes/lane7-projective-kernel-20260803-v1/test_plucker_transport.py`](#source-e0ebcaa6e425b78d) — `22ca784d94dee019eee780909e1e615b6311b4e668e140847a2f8d37f6d39e30`
- [`research-notes/lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json`](#source-1ebb898687fd03df) — `a251278a145ab0cfcf249809267edb2d6529738684b5136ec5faef62c7aa3dfb`
- [`research-notes/lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json`](#source-fd22317d1e90a478) — `4e1a014a6616a990ac50d255fb7426a9f8ae1d06cbf5066ba52c8415da63cbda`
- [`research-notes/lane7-split-incidence-20260802-v1/lane7-split-incidence-theorem.md`](#source-a0e37d2743e92c4e) — `3d365808d7fc3426bbe6db5aafc981e014c654b4aea623a6c13f9ccd9d8923de`
- [`research-notes/lane7-split-incidence-20260802-v1/reconstruct_matrices.py`](#source-ac804ad823e1e515) — `b6bbbbec46eeffc89f1f535cfb859d3bcb1f10b1debe39217af49b7e76fd824f`
- [`research-notes/lane7-split-incidence-20260802-v1/verify_split_determinants.py`](#source-04ef47ee7aa0d345) — `ca1c168da85e42dc27a19bbf40c93b5e4185f19b3ecadb2899d5f1375ebc0319`
- [`research-notes/lane7-split-incidence-20260802-v1/verify_split_determinants_report.json`](#source-386d4aff08adc8e8) — `e5b108357cbb96c0b0e979f0242dd8f6c308cd521eb7f01827a8cd8dc6ca9421`
- [`research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_report.json`](#source-a49c880a704d2b7f) — `f0a78dce8f1f7f65a92f0d22267dfe143cc1828fbe6f2f435644276b8f505264`
- [`research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_theorem.py`](#source-d3702b088e5916ba) — `dadd947874d8b1967a39e55e39c64b4c549574d32523d0440c4cb6ef09369495`

<a id="source-867e4fccbf4a8d1c"></a>

## `research-notes/lane7-component-inputs-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 7 self-contained component and Plücker inputs

This packet closes a source-access gap in the Lane 7 research handoff. The
older split-incidence directory contains every exact dependency used by its
checker, but its factorization JSON refers to `Q` and `R` by filename and it
does not store either `A` or the product `CA` directly. A reader given only a
selective rendering of that directory therefore cannot reconstruct the second
marking or test the Plücker open without first recovering the large upstream
certificate chain.

`lane7_exact_component_bundle.json` is the compact research interface. Over

\&#91;
A_0=\mathbf Q&#91;a_0,\ldots,a_6&#93;
\&#93;

it stores, as expanded exact polynomial strings:

- the quartic `d`;
- the residual matrix `M` of shape \(10\times5\);
- the matrices `H,C,Q,R` in the determinant-boundary factorization;
- the top source block `A` of shape \(10\times5\);
- the directly usable product `CA` of shape \(5\times5\).

Thus a component calculation needs only the bundle. For
\(u=(u_0,\ldots,u_4)^t\), put

\&#91;
w=(CA)u,\qquad
\eta_{ij}=u_iw_j-u_jw_i.
\&#93;

On \(D(d)\), the second marking is \(v=-d^{-1}w\). A component of
\(V(I_5(M))\cap D(d)\) meets the independent-marking locus exactly when not
all ten \(\eta_{ij}\) vanish identically on its projective-kernel incidence.

## Reproduction and verification

The bundle was deterministically regenerated from the maintained exact
split-incidence sources:

```text
uv run python -B \
  research-notes/lane7-component-inputs-20260803-v1/build_component_bundle.py \
  research-notes/lane7-component-inputs-20260803-v1/lane7_exact_component_bundle.json
```

The builder refuses to overwrite an existing output. The verifier checks the
manifest hashes, reconstructs `A`, `H`, and `C` from the original certificate,
checks the five matrix-factorization identities, checks `CA=C*A`, checks the
stored residual matrix, and checks the sign convention in the Plücker
transport:

```text
uv run python -B \
  research-notes/lane7-component-inputs-20260803-v1/verify_component_bundle.py
```

`manifest.json` pins both the compact bundle and every source file required to
reconstruct it. The successful verification report is retained in the
immutable run directory
`/path/to/versioned-artifact`.

## Exact scope

This packet supplies the inputs needed to study grade, corank, components,
and the componentwise Plücker open. It proves no grade-six, purity,
decomposition, corank-two exclusion, or componentwise nonvanishing result by
itself.
</code></pre>

<a id="source-0d5c024071f214a5"></a>

## `research-notes/lane7-component-inputs-20260803-v1/build_component_bundle.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Build the self-contained exact input bundle for Lane 7 component work."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "lane7-split-incidence-20260802-v1"
sys.path.insert(0, str(SOURCE))

from reconstruct_matrices import a, decode_coeff_matrix, transformed  # noqa: E402


def parse_entries(path: Path) -&gt; sp.Matrix:
    data = json.loads(path.read_text(encoding="utf-8"))
    local_symbols = {str(variable): variable for variable in a}
    return sp.Matrix(
        &#91;
            &#91;sp.sympify(entry, locals=local_symbols) for entry in row&#93;
            for row in data&#91;"entries"&#93;
        &#93;
    )


def matrix_strings(matrix: sp.Matrix) -&gt; list&#91;list&#91;str&#93;&#93;:
    return &#91;&#91;str(sp.expand(entry)) for entry in row&#93; for row in matrix.tolist()&#93;


def theorem_matrices() -&gt; tuple&#91;
    sp.Expr, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix
&#93;:
    _, _, determinant, _, matrix_u, _, matrix_v = transformed()
    matrix_a = matrix_u&#91;:10, :&#93;
    matrix_h = matrix_v&#91;:10, :&#93;

    left_inverse_v = decode_coeff_matrix(SOURCE / "Hv_left_inverse.json")
    extension = sp.zeros(15, 10)
    for index in range(10):
        extension&#91;index, index&#93; = 1
    for index, sign in enumerate((1, 1, -1, 1, 1)):
        extension&#91;10 + index, index&#93; = sp.Rational(3, 2) * sign
    matrix_c = (left_inverse_v * extension).applyfunc(sp.expand)

    matrix_q = parse_entries(SOURCE / "Hv10_syzygies_exact.json")
    matrix_r = parse_entries(SOURCE / "Hv10_right_inverse_exact.json")
    return determinant, matrix_a, matrix_h, matrix_c, matrix_q, matrix_r


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(f"refusing to overwrite existing output: {args.output}")

    determinant, matrix_a, matrix_h, matrix_c, matrix_q, matrix_r = theorem_matrices()
    matrix_ca = (matrix_c * matrix_a).applyfunc(sp.expand)
    stored_residual = parse_entries(SOURCE / "collision_residual_matrix_M.json")
    stored_factorization = json.loads(
        (SOURCE / "Hv10_split_matrix_factorization.json").read_text(encoding="utf-8")
    )
    local_symbols = {str(variable): variable for variable in a}
    stored_determinant = sp.sympify(stored_factorization&#91;"d"&#93;, locals=local_symbols)
    stored_h = sp.Matrix(
        &#91;
            &#91;sp.sympify(entry, locals=local_symbols) for entry in row&#93;
            for row in stored_factorization&#91;"H"&#93;
        &#93;
    )
    stored_c = sp.Matrix(
        &#91;
            &#91;sp.sympify(entry, locals=local_symbols) for entry in row&#93;
            for row in stored_factorization&#91;"C"&#93;
        &#93;
    )
    assert sp.expand(determinant - stored_determinant) == 0
    assert matrix_h == stored_h
    assert matrix_c == stored_c

    bundle = {
        "schema_version": 1,
        "ring": "Q&#91;a0,...,a6&#93;",
        "parameters": &#91;str(variable) for variable in a&#93;,
        "kernel_coordinates": &#91;f"u{index}" for index in range(5)&#93;,
        "definitions": {
            "carrier": "V(I_5(M)) intersect D(d)",
            "second_marking": "v = -d^(-1) * CA * u",
            "plucker_numerator": "eta_ij = u_i*(CA*u)_j - u_j*(CA*u)_i",
            "independent_marking_open": "some eta_ij != 0",
            "corank_two_locus": "V(I_4(M)) intersect D(d)",
        },
        "d": str(sp.expand(determinant)),
        "matrices": {
            "M": {"shape": &#91;10, 5&#93;, "entries": matrix_strings(stored_residual)},
            "A": {"shape": &#91;10, 5&#93;, "entries": matrix_strings(matrix_a)},
            "CA": {"shape": &#91;5, 5&#93;, "entries": matrix_strings(matrix_ca)},
            "H": {"shape": &#91;10, 5&#93;, "entries": matrix_strings(matrix_h)},
            "C": {"shape": &#91;5, 10&#93;, "entries": matrix_strings(matrix_c)},
            "Q": {"shape": &#91;5, 10&#93;, "entries": matrix_strings(matrix_q)},
            "R": {"shape": &#91;10, 5&#93;, "entries": matrix_strings(matrix_r)},
        },
        "factorization_identities": &#91;
            "C*H = d*I_5",
            "Q*H = 0",
            "C*R = 0",
            "Q*R = d*I_5",
            "H*C + R*Q = d*I_10",
        &#93;,
        "does_not_establish": &#91;
            "grade six or Cohen--Macaulayness of I_5(M) on D(d)",
            "I_4(M):d^infinity = (1)",
            "component decomposition or purity",
            "generic Plucker nonvanishing on any component",
            "a first-normal obstruction",
        &#93;,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(bundle, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-8ac5c833df312401"></a>

## `research-notes/lane7-component-inputs-20260803-v1/lane7_exact_component_bundle.json`

<pre><code class="language-json">
{
  "d": "36*a0*a2*a3*a5 - 12*a0*a2*a4**2 + 108*a0*a3*a6**2 - 54*a0*a3*a6 + 6*a0*a3 - 24*a0*a4*a5*a6 + 6*a0*a4*a5 + 4*a0*a5**3 - 36*a1**2*a3*a5 + 12*a1**2*a4**2 - 216*a1*a2*a3*a6 + 54*a1*a2*a3 + 24*a1*a2*a4*a5 - 72*a1*a4*a6**2 + 36*a1*a4*a6 - 6*a1*a4 + 24*a1*a5**2*a6 - 6*a1*a5**2 + 108*a2**3*a3 + 72*a2**2*a4*a6 - 18*a2**2*a4 + 12*a2**2*a5**2 + 108*a2*a5*a6**2 - 54*a2*a5*a6 + 3*a2*a5 + 108*a6**4 - 108*a6**3 + 33*a6**2 - 3*a6",
  "definitions": {
    "carrier": "V(I_5(M)) intersect D(d)",
    "corank_two_locus": "V(I_4(M)) intersect D(d)",
    "independent_marking_open": "some eta_ij != 0",
    "plucker_numerator": "eta_ij = u_i*(CA*u)_j - u_j*(CA*u)_i",
    "second_marking": "v = -d^(-1) * CA * u"
  },
  "does_not_establish": &#91;
    "grade six or Cohen--Macaulayness of I_5(M) on D(d)",
    "I_4(M):d^infinity = (1)",
    "component decomposition or purity",
    "generic Plucker nonvanishing on any component",
    "a first-normal obstruction"
  &#93;,
  "factorization_identities": &#91;
    "C*H = d*I_5",
    "Q*H = 0",
    "C*R = 0",
    "Q*R = d*I_5",
    "H*C + R*Q = d*I_10"
  &#93;,
  "kernel_coordinates": &#91;
    "u0",
    "u1",
    "u2",
    "u3",
    "u4"
  &#93;,
  "matrices": {
    "A": {
      "entries": &#91;
        &#91;
          "-2*a0*a3/27 - 2*a0*a4/27 + 2*a2*a5/81 + 2*a2*a6/9 - 1/81",
          "-a0*a3/3 + a2*a5/9 - 1/18",
          "4*a0*a3/81 + 4*a0*a4/81 + 2*a0*a5/27 + 2*a1/27 + 2*a2**2/9 - 4*a2*a5/243 - 4*a2*a6/27 + 2/243",
          "-8*a0*a3/243 - 8*a0*a4/243 - 4*a0*a5/81 - 2*a0*a6/9 + a0/9 + 2*a1*a2/9 - 4*a1/81 - 4*a2**2/27 + 8*a2*a5/729 + 8*a2*a6/81 - 4/729",
          "16*a0*a3/729 + 16*a0*a4/729 + 8*a0*a5/243 + 4*a0*a6/27 - 2*a0/27 - 4*a1*a2/27 + 8*a1/243 + 8*a2**2/81 - 16*a2*a5/2187 - 16*a2*a6/243 + 8/2187"
        &#93;,
        &#91;
          "-2*a1*a3/27 - 2*a1*a4/27 + 2*a5*a6/81 + 2*a6**2/9 - 1/54",
          "-a1*a3/3 + a5*a6/9",
          "4*a1*a3/81 + 4*a1*a4/81 + 2*a1*a5/27 + 2*a2*a6/9 + 2*a2/27 - 4*a5*a6/243 - 4*a6**2/27 + 1/81",
          "-8*a1*a3/243 - 8*a1*a4/243 - 4*a1*a5/81 + a1/9 - 4*a2*a6/27 - 4*a2/81 + 8*a5*a6/729 + 8*a6**2/81 - 2/243",
          "2*a0*a6/9 - 2*a1*a2/9 + 16*a1*a3/729 + 16*a1*a4/729 + 8*a1*a5/243 - 2*a1/27 + 8*a2*a6/81 + 8*a2/243 - 16*a5*a6/2187 - 16*a6**2/243 + 4/729"
        &#93;,
        &#91;
          "2*a2*a3/9 + 2*a2*a4/9 + 2*a4/81 + 2*a5**2/81 + 2*a5*a6/9 + 2*a5/27",
          "a2*a3 + a4/9 + a5**2/9",
          "-4*a2*a3/27 - 4*a2*a4/27 - 4*a4/243 - 4*a5**2/243 - 4*a5*a6/27 - 4*a5/81 - 4*a6/9 + 1/9",
          "2*a1*a5/9 + 8*a2*a3/81 + 8*a2*a4/81 + 2*a2*a6/3 - 5*a2/9 + 8*a4/729 + 8*a5**2/729 + 8*a5*a6/81 + 8*a5/243 + 8*a6/27 - 2/27",
          "2*a0*a5/9 - 4*a1*a5/27 - 2*a1/9 + 2*a2**2/3 - 16*a2*a3/243 - 16*a2*a4/243 - 4*a2*a6/9 + 10*a2/27 - 16*a4/2187 - 16*a5**2/2187 - 16*a5*a6/243 - 16*a5/729 - 16*a6/81 + 4/81"
        &#93;,
        &#91;
          "-2*a3*a6/9 + a3/9 + 2*a4*a5/81 + a4/9",
          "-a3*a6 + a3/2 + a4*a5/9",
          "2*a2*a4/9 + 4*a3*a6/27 - 2*a3/27 - 4*a4*a5/243 - 2*a4/27 + 2*a5*a6/9 - 5*a5/27",
          "2*a1*a4/9 - 4*a2*a4/27 - 8*a3*a6/81 + 4*a3/81 + 8*a4*a5/729 + 4*a4/81 - 4*a5*a6/27 + 10*a5/81 - 2*a6**2/3 + 2*a6/3 - 1/9",
          "2*a0*a4/9 - 4*a1*a4/27 + 8*a2*a4/81 - 2*a2*a6/3 + a2/3 + 16*a3*a6/243 - 8*a3/243 - 16*a4*a5/2187 - 8*a4/243 + 8*a5*a6/81 - 20*a5/243 + 4*a6**2/9 - 4*a6/9 + 2/27"
        &#93;,
        &#91;
          "2*a3*a6/3 - 2*a4*a5/27",
          "0",
          "2*a2*a3/3 - 4*a3*a6/9 + 4*a4*a5/81 - 2*a4/27 + 2*a5**2/27",
          "2*a1*a3/3 - 4*a2*a3/9 + 8*a3*a6/27 - 8*a4*a5/243 + 4*a4/81 - 4*a5**2/81 - 2*a5*a6/9 + a5/9",
          "2*a0*a3/3 - 4*a1*a3/9 + 8*a2*a3/27 - 2*a2*a5/9 - 16*a3*a6/81 + 16*a4*a5/729 - 8*a4/243 + 8*a5**2/243 + 4*a5*a6/27 - 2*a5/27 + 1/9"
        &#93;,
        &#91;
          "4*a0*a4/81 + 4*a0*a5/27 + 4*a1*a5/81 + 4*a1*a6/9 - 2*a1/9 + 2*a2/27",
          "2*a0*a4/9 + 2*a1*a5/9 + a2/3",
          "-8*a0*a4/243 - 8*a0*a5/81 - 4*a0*a6/9 + 2*a0/27 + 4*a1*a2/9 - 8*a1*a5/243 - 8*a1*a6/27 + 4*a1/27 - 4*a2/81",
          "-4*a0*a2/9 + 16*a0*a4/729 + 16*a0*a5/243 + 8*a0*a6/27 - 4*a0/81 + 4*a1**2/9 - 8*a1*a2/27 + 16*a1*a5/729 + 16*a1*a6/81 - 8*a1/81 + 8*a2/243",
          "8*a0*a2/27 - 32*a0*a4/2187 - 32*a0*a5/729 - 16*a0*a6/81 + 8*a0/243 - 8*a1**2/27 + 16*a1*a2/81 - 32*a1*a5/2187 - 32*a1*a6/243 + 16*a1/243 - 16*a2/729"
        &#93;,
        &#91;
          "4*a1*a4/81 + 4*a1*a5/27 + 4*a2*a5/81 + 4*a2*a6/9 - 2*a2/9 + 2*a6/27 - 1/81",
          "2*a1*a4/9 + 2*a2*a5/9 + a6/3 - 1/18",
          "-8*a1*a4/243 - 8*a1*a5/81 - 4*a1*a6/9 + 2*a1/27 + 4*a2**2/9 - 8*a2*a5/243 - 8*a2*a6/27 + 4*a2/27 - 4*a6/81 + 2/243",
          "16*a1*a4/729 + 16*a1*a5/243 + 8*a1*a6/27 - 4*a1/81 - 8*a2**2/27 + 16*a2*a5/729 + 16*a2*a6/81 - 8*a2/81 + 8*a6/243 - 4/729",
          "4*a0*a2/9 - 4*a1**2/9 - 32*a1*a4/2187 - 32*a1*a5/729 - 16*a1*a6/81 + 8*a1/243 + 16*a2**2/81 - 32*a2*a5/2187 - 32*a2*a6/243 + 16*a2/243 - 16*a6/729 + 8/2187"
        &#93;,
        &#91;
          "4*a2*a4/27 + 4*a2*a5/9 + 4*a5*a6/27 - 10*a5/81 + 4*a6**2/3 - 10*a6/9 + 2/9",
          "2*a2*a4/3 + 2*a5*a6/3 - 5*a5/9",
          "-8*a2*a4/81 - 8*a2*a5/27 - 2*a2/9 - 8*a5*a6/81 + 20*a5/243 - 8*a6**2/9 + 20*a6/27 - 4/27",
          "4*a1*a6/3 - 4*a1/9 - 4*a2**2/3 + 16*a2*a4/243 + 16*a2*a5/81 + 4*a2/27 + 16*a5*a6/243 - 40*a5/729 + 16*a6**2/27 - 40*a6/81 + 8/81",
          "4*a0*a6/3 - 4*a0/9 - 4*a1*a2/3 - 8*a1*a6/9 + 8*a1/27 + 8*a2**2/9 - 32*a2*a4/729 - 32*a2*a5/243 - 8*a2/81 - 32*a5*a6/729 + 80*a5/2187 - 32*a6**2/81 + 80*a6/243 - 16/243"
        &#93;,
        &#91;
          "4*a4*a6/27 + 2*a4/27 - 4*a5**2/81 + 2*a5/9",
          "2*a4*a6/3 + a4/3 - 2*a5**2/9",
          "-4*a2*a5/9 - 8*a4*a6/81 - 4*a4/81 + 8*a5**2/243 - 4*a5/27 - 4*a6**2/3 + 2*a6/9",
          "-4*a1*a5/9 + 8*a2*a5/27 - 4*a2*a6/3 + 16*a4*a6/243 + 8*a4/243 - 16*a5**2/729 + 8*a5/81 + 8*a6**2/9 - 4*a6/27",
          "-4*a0*a5/9 + 8*a1*a5/27 - 4*a1*a6/3 - 16*a2*a5/81 + 8*a2*a6/9 - 32*a4*a6/729 - 16*a4/729 + 32*a5**2/2187 - 16*a5/243 - 16*a6**2/27 + 8*a6/81"
        &#93;,
        &#91;
          "4*a3/9 - 4*a4*a6/9 + 4*a4/9 + 4*a5**2/27",
          "2*a3",
          "-4*a2*a4/9 - 8*a3/27 + 8*a4*a6/27 - 8*a4/27 - 8*a5**2/81 - 4*a5*a6/9 - 4*a5/27",
          "-4*a1*a4/9 + 8*a2*a4/27 - 4*a2*a5/9 + 16*a3/81 - 16*a4*a6/81 + 16*a4/81 + 16*a5**2/243 + 8*a5*a6/27 + 8*a5/81 + 2*a6/3 - 2/9",
          "-4*a0*a4/9 + 8*a1*a4/27 - 4*a1*a5/9 - 16*a2*a4/81 + 8*a2*a5/27 + 2*a2/3 - 32*a3/243 + 32*a4*a6/243 - 32*a4/243 - 32*a5**2/729 - 16*a5*a6/81 - 16*a5/243 - 4*a6/9 + 4/27"
        &#93;
      &#93;,
      "shape": &#91;
        10,
        5
      &#93;
    },
    "C": {
      "entries": &#91;
        &#91;
          "-324*a0*a1*a3*a5 + 108*a0*a1*a4**2 - 972*a0*a2*a3*a6 + 162*a0*a2*a3 + 108*a0*a2*a4*a5 - 324*a0*a4*a6**2 + 54*a0*a4*a6 + 108*a0*a5**2*a6 - 972*a1**2*a3*a6 + 324*a1**2*a3 + 108*a1**2*a4*a5 + 972*a1*a2**2*a3 + 108*a1*a2*a4 + 216*a1*a2*a5**2 + 324*a1*a5*a6**2 - 108*a1*a5*a6 + 324*a2**3*a4 + 648*a2**2*a5*a6 - 54*a2**2*a5 + 972*a2*a6**3 - 486*a2*a6**2 + 54*a2*a6",
          "324*a0**2*a3*a5 - 108*a0**2*a4**2 + 1944*a0*a1*a3*a6 - 648*a0*a1*a3 - 216*a0*a1*a4*a5 + 648*a0*a2*a4*a6 - 270*a0*a2*a4 - 216*a0*a2*a5**2 - 54*a0*a5*a6 - 972*a1**2*a2*a3 - 108*a1**2*a4 - 108*a1**2*a5**2 - 648*a1*a2**2*a4 - 648*a1*a2*a5*a6 - 108*a1*a2*a5 - 324*a1*a6**2 + 108*a1*a6 - 324*a2**3*a5 - 972*a2**2*a6**2 + 324*a2**2*a6",
          "-54*a0**2*a3 + 324*a0*a1*a2*a3 + 108*a0*a1*a4*a6 - 90*a0*a1*a4 + 108*a0*a2**2*a4 + 108*a0*a2*a5*a6 - 72*a0*a2*a5 - 54*a0*a6**2 + 27*a0*a6 - 324*a1**3*a3 - 216*a1**2*a2*a4 + 108*a1**2*a5*a6 - 54*a1**2*a5 - 216*a1*a2**2*a5 + 324*a1*a2*a6**2 - 108*a1*a2*a6 - 324*a2**3*a6",
          "324*a0**2*a2*a3 + 108*a0**2*a4*a6 - 18*a0**2*a4 - 324*a0*a1**2*a3 - 108*a0*a1*a2*a4 + 108*a0*a1*a5*a6 + 18*a0*a1*a5 - 216*a0*a2**2*a5 - 324*a0*a2*a6**2 + 216*a0*a2*a6 - 45*a0*a2 + 108*a1**2*a2*a5 + 216*a1**2*a6 - 54*a1**2 + 648*a1*a2**2*a6 - 324*a1*a2**2 - 324*a2**4",
          "-108*a0**2*a2*a4 - 108*a0**2*a5*a6 + 36*a0**2*a5 + 108*a0*a1**2*a4 - 648*a0*a1*a6**2 + 432*a0*a1*a6 - 72*a0*a1 + 324*a0*a2**2*a6 - 162*a0*a2**2 + 108*a1**3*a5 + 648*a1**2*a2*a6 - 162*a1**2*a2 - 324*a1*a2**3",
          "-648*a0*a2*a3*a5 + 216*a0*a2*a4**2 - 1944*a0*a3*a6**2 + 972*a0*a3*a6 - 108*a0*a3 + 432*a0*a4*a5*a6 - 108*a0*a4*a5 - 72*a0*a5**3 + 648*a1**2*a3*a5 - 216*a1**2*a4**2 + 3888*a1*a2*a3*a6 - 972*a1*a2*a3 - 432*a1*a2*a4*a5 + 1296*a1*a4*a6**2 - 648*a1*a4*a6 + 108*a1*a4 - 432*a1*a5**2*a6 + 108*a1*a5**2 - 1944*a2**3*a3 - 1296*a2**2*a4*a6 + 324*a2**2*a4 - 216*a2**2*a5**2 - 1944*a2*a5*a6**2 + 972*a2*a5*a6 - 54*a2*a5 - 1944*a6**4 + 1944*a6**3 - 594*a6**2 + 54*a6",
          "-648*a0*a1*a3*a5 + 216*a0*a1*a4**2 - 1944*a0*a2*a3*a6 + 324*a0*a2*a3 + 216*a0*a2*a4*a5 - 648*a0*a4*a6**2 + 108*a0*a4*a6 + 216*a0*a5**2*a6 - 1944*a1**2*a3*a6 + 648*a1**2*a3 + 216*a1**2*a4*a5 + 1944*a1*a2**2*a3 + 216*a1*a2*a4 + 432*a1*a2*a5**2 + 648*a1*a5*a6**2 - 216*a1*a5*a6 + 648*a2**3*a4 + 1296*a2**2*a5*a6 - 108*a2**2*a5 + 1944*a2*a6**3 - 972*a2*a6**2 + 108*a2*a6",
          "216*a0**2*a3*a5 - 72*a0**2*a4**2 + 648*a0*a1*a3*a6 - 216*a0*a1*a3 - 72*a0*a1*a4*a5 + 648*a0*a2**2*a3 + 648*a0*a2*a4*a6 - 180*a0*a2*a4 - 72*a0*a2*a5**2 + 216*a0*a5*a6**2 - 108*a0*a5*a6 - 648*a1**2*a2*a3 - 216*a1**2*a4*a6 - 216*a1*a2**2*a4 - 108*a1*a2*a5 + 648*a1*a6**3 - 540*a1*a6**2 + 108*a1*a6 - 216*a2**3*a5 - 648*a2**2*a6**2 + 216*a2**2*a6",
          "648*a0**2*a3*a6 - 108*a0**2*a3 - 72*a0**2*a4*a5 - 1296*a0*a1*a2*a3 - 216*a0*a1*a4*a6 + 108*a0*a1*a4 - 72*a0*a1*a5**2 - 216*a0*a2**2*a4 + 36*a0*a2*a5 + 648*a0*a6**3 - 432*a0*a6**2 + 54*a0*a6 + 648*a1**3*a3 + 216*a1**2*a2*a4 - 432*a1**2*a5*a6 + 108*a1**2*a5 + 216*a1*a2**2*a5 - 1296*a1*a2*a6**2 + 432*a1*a2*a6 + 648*a2**3*a6",
          "-216*a0**2*a4*a6 + 36*a0**2*a4 + 72*a0**2*a5**2 + 432*a0*a1*a2*a4 + 432*a0*a1*a5*a6 - 180*a0*a1*a5 + 432*a0*a2**2*a5 + 1296*a0*a2*a6**2 - 756*a0*a2*a6 + 90*a0*a2 - 216*a1**3*a4 - 432*a1**2*a2*a5 + 648*a1**2*a6**2 - 540*a1**2*a6 + 108*a1**2 - 1944*a1*a2**2*a6 + 648*a1*a2**2 + 648*a2**4"
        &#93;,
        &#91;
          "-1458*a1*a3*a6 + 486*a1*a3 + 162*a1*a4*a5 + 1458*a2**2*a3 + 486*a2*a4*a6 + 162*a2*a5**2 + 486*a5*a6**2 - 162*a5*a6",
          "1458*a0*a3*a6 - 486*a0*a3 - 162*a0*a4*a5 - 1458*a1*a2*a3 - 162*a1*a4 - 162*a1*a5**2 - 486*a2**2*a4 - 486*a2*a5*a6 - 162*a2*a5 - 486*a6**2 + 162*a6",
          "486*a0*a2*a3 + 162*a0*a4*a6 - 54*a0*a4 - 486*a1**2*a3 - 162*a1*a2*a4 + 162*a1*a5*a6 - 81*a1*a5 - 162*a2**2*a5 - 81*a2*a6",
          "27*a0*a5 + 324*a1*a6 - 81*a1 - 243*a2**2",
          "-162*a0*a2*a5 - 486*a0*a6**2 + 243*a0*a6 - 27*a0 + 162*a1**2*a5 + 972*a1*a2*a6 - 243*a1*a2 - 486*a2**3",
          "0",
          "-2916*a1*a3*a6 + 972*a1*a3 + 324*a1*a4*a5 + 2916*a2**2*a3 + 972*a2*a4*a6 + 324*a2*a5**2 + 972*a5*a6**2 - 324*a5*a6",
          "972*a0*a3*a6 - 324*a0*a3 - 108*a0*a4*a5 - 972*a1*a2*a3 - 324*a1*a4*a6 + 324*a2*a5*a6 - 162*a2*a5 + 972*a6**3 - 810*a6**2 + 162*a6",
          "-972*a0*a2*a3 - 108*a0*a5**2 + 972*a1**2*a3 - 648*a1*a5*a6 + 162*a1*a5 - 972*a2*a6**2 + 486*a2*a6",
          "324*a0*a2*a4 + 324*a0*a5*a6 - 108*a0*a5 - 324*a1**2*a4 - 324*a1*a2*a5 + 972*a1*a6**2 - 810*a1*a6 + 162*a1 - 972*a2**2*a6 + 486*a2**2"
        &#93;,
        &#91;
          "-648*a0*a2*a3*a5 + 216*a0*a2*a4**2 - 1944*a0*a3*a6**2 + 972*a0*a3*a6 - 108*a0*a3 + 432*a0*a4*a5*a6 - 108*a0*a4*a5 - 72*a0*a5**3 + 648*a1**2*a3*a5 - 216*a1**2*a4**2 + 3888*a1*a2*a3*a6 - 972*a1*a2*a3 - 432*a1*a2*a4*a5 + 1296*a1*a4*a6**2 - 324*a1*a4*a6 - 432*a1*a5**2*a6 - 1944*a2**3*a3 - 1296*a2**2*a4*a6 - 216*a2**2*a5**2 - 1944*a2*a5*a6**2 + 324*a2*a5*a6 - 1944*a6**4 + 972*a6**3 - 108*a6**2",
          "-648*a0*a1*a3*a5 + 216*a0*a1*a4**2 - 1944*a0*a2*a3*a6 + 324*a0*a2*a3 + 216*a0*a2*a4*a5 - 648*a0*a4*a6**2 - 216*a0*a4*a6 + 108*a0*a4 + 216*a0*a5**2*a6 + 108*a0*a5**2 - 1944*a1**2*a3*a6 + 648*a1**2*a3 + 216*a1**2*a4*a5 + 1944*a1*a2**2*a3 + 540*a1*a2*a4 + 432*a1*a2*a5**2 + 648*a1*a5*a6**2 + 108*a1*a5*a6 + 648*a2**3*a4 + 1296*a2**2*a5*a6 + 216*a2**2*a5 + 1944*a2*a6**3 - 216*a2*a6",
          "-216*a0**2*a3*a5 + 72*a0**2*a4**2 - 648*a0*a1*a3*a6 + 216*a0*a1*a3 + 72*a0*a1*a4*a5 - 648*a0*a2**2*a3 - 648*a0*a2*a4*a6 + 72*a0*a2*a4 + 72*a0*a2*a5**2 - 216*a0*a5*a6**2 + 18*a0*a5 + 648*a1**2*a2*a3 + 216*a1**2*a4*a6 + 108*a1**2*a4 + 216*a1*a2**2*a4 + 216*a1*a2*a5 - 648*a1*a6**3 + 216*a1*a6**2 - 54*a1*a6 + 216*a2**3*a5 + 648*a2**2*a6**2 + 108*a2**2*a6",
          "648*a0**2*a3*a6 - 108*a0**2*a3 - 72*a0**2*a4*a5 - 1296*a0*a1*a2*a3 - 216*a0*a1*a4*a6 + 108*a0*a1*a4 - 72*a0*a1*a5**2 - 216*a0*a2**2*a4 + 144*a0*a2*a5 + 648*a0*a6**3 - 108*a0*a6**2 - 108*a0*a6 + 18*a0 + 648*a1**3*a3 + 216*a1**2*a2*a4 - 432*a1**2*a5*a6 + 216*a1*a2**2*a5 - 1296*a1*a2*a6**2 - 216*a1*a2*a6 + 162*a1*a2 + 648*a2**3*a6 + 324*a2**3",
          "-216*a0**2*a4*a6 + 36*a0**2*a4 + 72*a0**2*a5**2 + 432*a0*a1*a2*a4 + 432*a0*a1*a5*a6 - 180*a0*a1*a5 + 432*a0*a2**2*a5 + 1296*a0*a2*a6**2 - 756*a0*a2*a6 + 90*a0*a2 - 216*a1**3*a4 - 432*a1**2*a2*a5 + 648*a1**2*a6**2 - 540*a1**2*a6 + 108*a1**2 - 1944*a1*a2**2*a6 + 648*a1*a2**2 + 648*a2**4",
          "0",
          "648*a1*a4*a6 - 216*a1*a4 - 216*a1*a5**2 - 648*a2**2*a4 - 1296*a2*a5*a6 + 108*a2*a5 - 1944*a6**3 + 972*a6**2 - 108*a6",
          "-216*a0*a4*a6 + 72*a0*a4 + 72*a0*a5**2 + 216*a1*a2*a4 + 216*a1*a5*a6 + 216*a2**2*a5 + 648*a2*a6**2 - 216*a2*a6",
          "216*a0*a2*a4 + 216*a0*a5*a6 - 36*a0*a5 - 216*a1**2*a4 - 216*a1*a2*a5 + 648*a1*a6**2 - 108*a1*a6 - 648*a2**2*a6",
          "-216*a0*a2*a5 - 648*a0*a6**2 + 324*a0*a6 - 36*a0 + 216*a1**2*a5 + 1296*a1*a2*a6 - 324*a1*a2 - 648*a2**3"
        &#93;,
        &#91;
          "-324*a1*a3*a5 + 108*a1*a4**2 - 972*a2*a3*a6 + 162*a2*a3 + 108*a2*a4*a5 - 324*a4*a6**2 + 54*a4*a6 + 108*a5**2*a6",
          "324*a0*a3*a5 - 108*a0*a4**2 + 1944*a1*a3*a6 - 648*a1*a3 - 216*a1*a4*a5 - 972*a2**2*a3 - 162*a2*a4 - 216*a2*a5**2 - 324*a5*a6**2 + 54*a5*a6",
          "324*a0*a3*a6 - 162*a0*a3 - 36*a0*a4*a5 - 324*a1*a2*a3 - 108*a1*a4*a6 - 54*a1*a4 + 108*a2*a5*a6 - 108*a2*a5 + 324*a6**3 - 324*a6**2 + 81*a6",
          "648*a0*a2*a3 + 108*a0*a4*a6 - 18*a0*a4 + 36*a0*a5**2 - 648*a1**2*a3 - 108*a1*a2*a4 + 324*a1*a5*a6 - 54*a1*a5 - 108*a2**2*a5 + 324*a2*a6**2 - 108*a2*a6 - 27*a2",
          "-216*a0*a2*a4 - 216*a0*a5*a6 + 72*a0*a5 + 216*a1**2*a4 + 216*a1*a2*a5 - 648*a1*a6**2 + 540*a1*a6 - 108*a1 + 648*a2**2*a6 - 324*a2**2",
          "0",
          "-648*a1*a3*a5 + 216*a1*a4**2 - 1944*a2*a3*a6 + 324*a2*a3 + 216*a2*a4*a5 - 648*a4*a6**2 + 108*a4*a6 + 216*a5**2*a6",
          "216*a0*a3*a5 - 72*a0*a4**2 + 648*a2**2*a3 + 432*a2*a4*a6 - 108*a2*a4 + 216*a5*a6**2 - 108*a5*a6",
          "648*a0*a3*a6 - 108*a0*a3 - 72*a0*a4*a5 - 648*a1*a2*a3 - 216*a1*a4*a6 + 108*a1*a4 + 216*a2*a5*a6 + 648*a6**3 - 432*a6**2 + 54*a6",
          "-216*a0*a4*a6 + 36*a0*a4 + 72*a0*a5**2 + 216*a1*a2*a4 + 216*a1*a5*a6 - 108*a1*a5 + 216*a2**2*a5 + 648*a2*a6**2 - 432*a2*a6 + 54*a2"
        &#93;,
        &#91;
          "0",
          "324*a1*a3*a5 - 108*a1*a4**2 + 972*a2*a3*a6 - 162*a2*a3 - 108*a2*a4*a5 + 324*a4*a6**2 - 54*a4*a6 - 108*a5**2*a6",
          "108*a0*a3*a5 - 36*a0*a4**2 + 324*a2**2*a3 + 216*a2*a4*a6 - 54*a2*a4 + 108*a5*a6**2 - 54*a5*a6",
          "-324*a0*a3*a6 + 54*a0*a3 + 36*a0*a4*a5 + 324*a1*a2*a3 + 108*a1*a4*a6 - 54*a1*a4 - 108*a2*a5*a6 - 324*a6**3 + 216*a6**2 - 27*a6",
          "108*a0*a4*a6 - 18*a0*a4 - 36*a0*a5**2 - 108*a1*a2*a4 - 108*a1*a5*a6 + 54*a1*a5 - 108*a2**2*a5 - 324*a2*a6**2 + 216*a2*a6 - 27*a2",
          "0",
          "0",
          "0",
          "0",
          "0"
        &#93;
      &#93;,
      "shape": &#91;
        5,
        10
      &#93;
    },
    "CA": {
      "entries": &#91;
        &#91;
          "12*a0**2*a2*a3**2 + 12*a0**2*a2*a3*a4 - 4*a0**2*a3*a4*a6 - 2*a0**2*a3*a4/3 + 28*a0**2*a3*a5**2/3 + 60*a0**2*a3*a5*a6 - 2*a0**2*a3*a5 - 20*a0**2*a4**2*a5/9 - 24*a0**2*a4**2*a6 + 8*a0**2*a4*a5**2/3 - 12*a0*a1**2*a3**2 - 12*a0*a1**2*a3*a4 + 20*a0*a1*a2*a3*a4 - 168*a0*a1*a2*a3*a5 + 76*a0*a1*a2*a4**2 + 84*a0*a1*a3*a5*a6 - 134*a0*a1*a3*a5/3 + 36*a0*a1*a3*a6 - 12*a0*a1*a3 - 8*a0*a1*a4**2*a6 + 64*a0*a1*a4**2/9 - 32*a0*a1*a4*a5**2/9 + 60*a0*a1*a4*a5*a6 - 82*a0*a1*a4*a5/3 - 32*a0*a1*a5**3/3 + 48*a0*a2**2*a3*a5 - 216*a0*a2**2*a3*a6 + 72*a0*a2**2*a3 - 8*a0*a2**2*a4**2 + 48*a0*a2**2*a4*a5 + 228*a0*a2*a3*a6**2 - 168*a0*a2*a3*a6 + 21*a0*a2*a3 - 40*a0*a2*a4*a5*a6/3 + 22*a0*a2*a4*a5/3 + 84*a0*a2*a4*a6**2 - 42*a0*a2*a4*a6 + 8*a0*a2*a5**2*a6 - 4*a0*a2*a5**2 + 32*a0*a4*a6**3 - 104*a0*a4*a6**2/3 + 16*a0*a4*a6/3 - 8*a0*a5**2*a6**2 + 22*a0*a5**2*a6/3 + 24*a0*a5*a6**3 - 14*a0*a5*a6**2 - a0*a5*a6 - 16*a1**3*a3*a4 + 72*a1**3*a3*a5 - 40*a1**3*a4**2 - 64*a1**2*a2*a3*a5 + 108*a1**2*a2*a3*a6 - 54*a1**2*a2*a3 + 16*a1**2*a2*a4**2/3 - 60*a1**2*a2*a4*a5 + 120*a1**2*a3*a6**2 - 128*a1**2*a3*a6 + 30*a1**2*a3 - 32*a1**2*a4*a5*a6/3 + 20*a1**2*a4*a5/3 + 192*a1**2*a4*a6**2 - 128*a1**2*a4*a6 + 20*a1**2*a4 - 4*a1**2*a5**3/3 - 68*a1**2*a5**2*a6 + 14*a1**2*a5**2 - 336*a1*a2**2*a3*a6 + 144*a1*a2**2*a3 + 16*a1*a2**2*a4*a5/3 - 336*a1*a2**2*a4*a6 + 96*a1*a2**2*a4 + 16*a1*a2**2*a5**2 - 56*a1*a2*a4*a6**2 + 56*a1*a2*a4*a6/3 + 4*a1*a2*a4 - 8*a1*a2*a5**2*a6 + 32*a1*a2*a5**2/3 - 240*a1*a2*a5*a6**2 + 92*a1*a2*a5*a6 - 10*a1*a2*a5 - 24*a1*a5*a6**3 + 28*a1*a5*a6**2 - 20*a1*a5*a6/3 - 216*a1*a6**4 + 216*a1*a6**3 - 78*a1*a6**2 + 10*a1*a6 + 108*a2**4*a3 + 108*a2**4*a4 + 24*a2**3*a4*a6 + 12*a2**3*a4 + 4*a2**3*a5**2 + 108*a2**3*a5*a6 - 18*a2**3*a5 + 12*a2**2*a5*a6**2 + 20*a2**2*a5*a6 - 2*a2**2*a5 + 108*a2**2*a6**3 - 90*a2**2*a6**2 + 18*a2**2*a6 + 36*a2*a6**3 - 18*a2*a6**2 + 2*a2*a6",
          "54*a0**2*a2*a3**2 - 18*a0**2*a3*a4*a6 - 3*a0**2*a3*a4 + 42*a0**2*a3*a5**2 - 10*a0**2*a4**2*a5 - 54*a0*a1**2*a3**2 + 90*a0*a1*a2*a3*a4 + 378*a0*a1*a3*a5*a6 - 201*a0*a1*a3*a5 - 36*a0*a1*a4**2*a6 + 32*a0*a1*a4**2 - 16*a0*a1*a4*a5**2 + 216*a0*a2**2*a3*a5 - 36*a0*a2**2*a4**2 + 1026*a0*a2*a3*a6**2 - 756*a0*a2*a3*a6 + 189*a0*a2*a3/2 - 60*a0*a2*a4*a5*a6 + 33*a0*a2*a4*a5 + 144*a0*a4*a6**3 - 156*a0*a4*a6**2 + 24*a0*a4*a6 - 36*a0*a5**2*a6**2 + 33*a0*a5**2*a6 - 72*a1**3*a3*a4 - 288*a1**2*a2*a3*a5 + 24*a1**2*a2*a4**2 + 540*a1**2*a3*a6**2 - 576*a1**2*a3*a6 + 135*a1**2*a3 - 48*a1**2*a4*a5*a6 + 30*a1**2*a4*a5 - 6*a1**2*a5**3 - 1512*a1*a2**2*a3*a6 + 648*a1*a2**2*a3 + 24*a1*a2**2*a4*a5 - 252*a1*a2*a4*a6**2 + 84*a1*a2*a4*a6 + 18*a1*a2*a4 - 36*a1*a2*a5**2*a6 + 48*a1*a2*a5**2 - 108*a1*a5*a6**3 + 126*a1*a5*a6**2 - 30*a1*a5*a6 + 486*a2**4*a3 + 108*a2**3*a4*a6 + 54*a2**3*a4 + 18*a2**3*a5**2 + 54*a2**2*a5*a6**2 + 90*a2**2*a5*a6 - 9*a2**2*a5 + 162*a2*a6**3 - 81*a2*a6**2 + 9*a2*a6",
          "-8*a0**2*a2*a3**2 - 8*a0**2*a2*a3*a4 - 48*a0**2*a2*a3*a5 + 12*a0**2*a2*a4**2 + 8*a0**2*a3*a4*a6/3 + 4*a0**2*a3*a4/9 - 56*a0**2*a3*a5**2/9 - 40*a0**2*a3*a5*a6 + 4*a0**2*a3*a5/3 - 288*a0**2*a3*a6**2 + 120*a0**2*a3*a6 - 14*a0**2*a3 + 40*a0**2*a4**2*a5/27 + 16*a0**2*a4**2*a6 - 16*a0**2*a4*a5**2/9 + 68*a0**2*a4*a5*a6 - 38*a0**2*a4*a5/3 - 40*a0**2*a5**3/3 + 8*a0*a1**2*a3**2 + 8*a0*a1**2*a3*a4 + 12*a0*a1**2*a3*a5 - 40*a0*a1*a2*a3*a4/3 + 112*a0*a1*a2*a3*a5 + 504*a0*a1*a2*a3*a6 - 96*a0*a1*a2*a3 - 152*a0*a1*a2*a4**2/3 - 76*a0*a1*a2*a4*a5 - 56*a0*a1*a3*a5*a6 + 268*a0*a1*a3*a5/9 - 24*a0*a1*a3*a6 + 8*a0*a1*a3 + 16*a0*a1*a4**2*a6/3 - 128*a0*a1*a4**2/27 + 64*a0*a1*a4*a5**2/27 - 40*a0*a1*a4*a5*a6 + 164*a0*a1*a4*a5/9 + 72*a0*a1*a4*a6**2 - 40*a0*a1*a4*a6 + 10*a0*a1*a4/3 + 64*a0*a1*a5**3/9 - 52*a0*a1*a5**2*a6 + 26*a0*a1*a5**2 - 216*a0*a2**3*a3 - 32*a0*a2**2*a3*a5 + 144*a0*a2**2*a3*a6 - 48*a0*a2**2*a3 + 16*a0*a2**2*a4**2/3 - 32*a0*a2**2*a4*a5 - 72*a0*a2**2*a4*a6 + 18*a0*a2**2*a4 - 72*a0*a2**2*a5**2 - 152*a0*a2*a3*a6**2 + 112*a0*a2*a3*a6 - 14*a0*a2*a3 + 80*a0*a2*a4*a5*a6/9 - 44*a0*a2*a4*a5/9 - 56*a0*a2*a4*a6**2 + 28*a0*a2*a4*a6 - 16*a0*a2*a5**2*a6/3 + 8*a0*a2*a5**2/3 - 324*a0*a2*a5*a6**2 + 170*a0*a2*a5*a6 - 17*a0*a2*a5 - 64*a0*a4*a6**3/3 + 208*a0*a4*a6**2/9 - 32*a0*a4*a6/9 + 16*a0*a5**2*a6**2/3 - 44*a0*a5**2*a6/9 - 16*a0*a5*a6**3 + 28*a0*a5*a6**2/3 + 2*a0*a5*a6/3 - 288*a0*a6**4 + 264*a0*a6**3 - 74*a0*a6**2 + 7*a0*a6 + 32*a1**3*a3*a4/3 - 48*a1**3*a3*a5 - 216*a1**3*a3*a6 + 36*a1**3*a3 + 80*a1**3*a4**2/3 + 40*a1**3*a4*a5 + 108*a1**2*a2**2*a3 + 128*a1**2*a2*a3*a5/3 - 72*a1**2*a2*a3*a6 + 36*a1**2*a2*a3 - 32*a1**2*a2*a4**2/9 + 40*a1**2*a2*a4*a5 + 24*a1**2*a2*a4*a6 - 8*a1**2*a2*a4 + 64*a1**2*a2*a5**2 - 80*a1**2*a3*a6**2 + 256*a1**2*a3*a6/3 - 20*a1**2*a3 + 64*a1**2*a4*a5*a6/9 - 40*a1**2*a4*a5/9 - 128*a1**2*a4*a6**2 + 256*a1**2*a4*a6/3 - 40*a1**2*a4/3 + 8*a1**2*a5**3/9 + 136*a1**2*a5**2*a6/3 - 28*a1**2*a5**2/3 + 48*a1**2*a5*a6**2 + 24*a1**2*a5*a6 - 12*a1**2*a5 + 224*a1*a2**2*a3*a6 - 96*a1*a2**2*a3 - 32*a1*a2**2*a4*a5/9 + 224*a1*a2**2*a4*a6 - 64*a1*a2**2*a4 - 32*a1*a2**2*a5**2/3 + 216*a1*a2**2*a5*a6 - 80*a1*a2**2*a5 + 112*a1*a2*a4*a6**2/3 - 112*a1*a2*a4*a6/9 - 8*a1*a2*a4/3 + 16*a1*a2*a5**2*a6/3 - 64*a1*a2*a5**2/9 + 160*a1*a2*a5*a6**2 - 184*a1*a2*a5*a6/3 + 20*a1*a2*a5/3 + 288*a1*a2*a6**3 - 120*a1*a2*a6**2 + 8*a1*a2*a6 + 16*a1*a5*a6**3 - 56*a1*a5*a6**2/3 + 40*a1*a5*a6/9 + 144*a1*a6**4 - 144*a1*a6**3 + 52*a1*a6**2 - 20*a1*a6/3 - 72*a2**4*a3 - 72*a2**4*a4 - 72*a2**4*a5 - 16*a2**3*a4*a6 - 8*a2**3*a4 - 8*a2**3*a5**2/3 - 72*a2**3*a5*a6 + 12*a2**3*a5 - 108*a2**3*a6**2 - 8*a2**2*a5*a6**2 - 40*a2**2*a5*a6/3 + 4*a2**2*a5/3 - 72*a2**2*a6**3 + 60*a2**2*a6**2 - 12*a2**2*a6 - 24*a2*a6**3 + 12*a2*a6**2 - 4*a2*a6/3",
          "-36*a0**2*a1*a3*a5 + 12*a0**2*a1*a4**2 + 16*a0**2*a2*a3**2/3 + 16*a0**2*a2*a3*a4/3 + 32*a0**2*a2*a3*a5 - 252*a0**2*a2*a3*a6 + 60*a0**2*a2*a3 - 8*a0**2*a2*a4**2 + 32*a0**2*a2*a4*a5 - 16*a0**2*a3*a4*a6/9 - 8*a0**2*a3*a4/27 + 112*a0**2*a3*a5**2/27 + 80*a0**2*a3*a5*a6/3 - 8*a0**2*a3*a5/9 + 192*a0**2*a3*a6**2 - 80*a0**2*a3*a6 + 28*a0**2*a3/3 - 80*a0**2*a4**2*a5/81 - 32*a0**2*a4**2*a6/3 + 32*a0**2*a4*a5**2/27 - 136*a0**2*a4*a5*a6/3 + 76*a0**2*a4*a5/9 - 108*a0**2*a4*a6**2 + 54*a0**2*a4*a6 - 6*a0**2*a4 + 80*a0**2*a5**3/9 + 40*a0**2*a5**2*a6 - 12*a0**2*a5**2 - 16*a0*a1**2*a3**2/3 - 16*a0*a1**2*a3*a4/3 - 8*a0*a1**2*a3*a5 - 36*a0*a1**2*a3*a6 + 288*a0*a1*a2**2*a3 + 80*a0*a1*a2*a3*a4/9 - 224*a0*a1*a2*a3*a5/3 - 336*a0*a1*a2*a3*a6 + 64*a0*a1*a2*a3 + 304*a0*a1*a2*a4**2/9 + 152*a0*a1*a2*a4*a5/3 + 156*a0*a1*a2*a4*a6 - 70*a0*a1*a2*a4 + 32*a0*a1*a2*a5**2 + 112*a0*a1*a3*a5*a6/3 - 536*a0*a1*a3*a5/27 + 16*a0*a1*a3*a6 - 16*a0*a1*a3/3 - 32*a0*a1*a4**2*a6/9 + 256*a0*a1*a4**2/81 - 128*a0*a1*a4*a5**2/81 + 80*a0*a1*a4*a5*a6/3 - 328*a0*a1*a4*a5/27 - 48*a0*a1*a4*a6**2 + 80*a0*a1*a4*a6/3 - 20*a0*a1*a4/9 - 128*a0*a1*a5**3/27 + 104*a0*a1*a5**2*a6/3 - 52*a0*a1*a5**2/3 + 180*a0*a1*a5*a6**2 - 140*a0*a1*a5*a6 + 30*a0*a1*a5 + 144*a0*a2**3*a3 + 72*a0*a2**3*a4 + 64*a0*a2**2*a3*a5/3 - 96*a0*a2**2*a3*a6 + 32*a0*a2**2*a3 - 32*a0*a2**2*a4**2/9 + 64*a0*a2**2*a4*a5/3 + 48*a0*a2**2*a4*a6 - 12*a0*a2**2*a4 + 48*a0*a2**2*a5**2 + 192*a0*a2**2*a5*a6 - 72*a0*a2**2*a5 + 304*a0*a2*a3*a6**2/3 - 224*a0*a2*a3*a6/3 + 28*a0*a2*a3/3 - 160*a0*a2*a4*a5*a6/27 + 88*a0*a2*a4*a5/27 + 112*a0*a2*a4*a6**2/3 - 56*a0*a2*a4*a6/3 + 32*a0*a2*a5**2*a6/9 - 16*a0*a2*a5**2/9 + 216*a0*a2*a5*a6**2 - 340*a0*a2*a5*a6/3 + 34*a0*a2*a5/3 + 396*a0*a2*a6**3 - 408*a0*a2*a6**2 + 141*a0*a2*a6 - 15*a0*a2 + 128*a0*a4*a6**3/9 - 416*a0*a4*a6**2/27 + 64*a0*a4*a6/27 - 32*a0*a5**2*a6**2/9 + 88*a0*a5**2*a6/27 + 32*a0*a5*a6**3/3 - 56*a0*a5*a6**2/9 - 4*a0*a5*a6/9 + 192*a0*a6**4 - 176*a0*a6**3 + 148*a0*a6**2/3 - 14*a0*a6/3 - 108*a1**3*a2*a3 - 64*a1**3*a3*a4/9 + 32*a1**3*a3*a5 + 144*a1**3*a3*a6 - 24*a1**3*a3 - 160*a1**3*a4**2/9 - 80*a1**3*a4*a5/3 - 48*a1**3*a4*a6 + 24*a1**3*a4 - 12*a1**3*a5**2 - 72*a1**2*a2**2*a3 - 48*a1**2*a2**2*a4 - 256*a1**2*a2*a3*a5/9 + 48*a1**2*a2*a3*a6 - 24*a1**2*a2*a3 + 64*a1**2*a2*a4**2/27 - 80*a1**2*a2*a4*a5/3 - 16*a1**2*a2*a4*a6 + 16*a1**2*a2*a4/3 - 128*a1**2*a2*a5**2/3 - 132*a1**2*a2*a5*a6 + 60*a1**2*a2*a5 + 160*a1**2*a3*a6**2/3 - 512*a1**2*a3*a6/9 + 40*a1**2*a3/3 - 128*a1**2*a4*a5*a6/27 + 80*a1**2*a4*a5/27 + 256*a1**2*a4*a6**2/3 - 512*a1**2*a4*a6/9 + 80*a1**2*a4/9 - 16*a1**2*a5**3/27 - 272*a1**2*a5**2*a6/9 + 56*a1**2*a5**2/9 - 32*a1**2*a5*a6**2 - 16*a1**2*a5*a6 + 8*a1**2*a5 + 144*a1**2*a6**3 - 240*a1**2*a6**2 + 120*a1**2*a6 - 18*a1**2 - 12*a1*a2**3*a5 - 448*a1*a2**2*a3*a6/3 + 64*a1*a2**2*a3 + 64*a1*a2**2*a4*a5/27 - 448*a1*a2**2*a4*a6/3 + 128*a1*a2**2*a4/3 + 64*a1*a2**2*a5**2/9 - 144*a1*a2**2*a5*a6 + 160*a1*a2**2*a5/3 - 396*a1*a2**2*a6**2 + 444*a1*a2**2*a6 - 108*a1*a2**2 - 224*a1*a2*a4*a6**2/9 + 224*a1*a2*a4*a6/27 + 16*a1*a2*a4/9 - 32*a1*a2*a5**2*a6/9 + 128*a1*a2*a5**2/27 - 320*a1*a2*a5*a6**2/3 + 368*a1*a2*a5*a6/9 - 40*a1*a2*a5/9 - 192*a1*a2*a6**3 + 80*a1*a2*a6**2 - 16*a1*a2*a6/3 - 32*a1*a5*a6**3/3 + 112*a1*a5*a6**2/9 - 80*a1*a5*a6/27 - 96*a1*a6**4 + 96*a1*a6**3 - 104*a1*a6**2/3 + 40*a1*a6/9 + 48*a2**4*a3 + 48*a2**4*a4 + 48*a2**4*a5 + 108*a2**4*a6 - 108*a2**4 + 32*a2**3*a4*a6/3 + 16*a2**3*a4/3 + 16*a2**3*a5**2/9 + 48*a2**3*a5*a6 - 8*a2**3*a5 + 72*a2**3*a6**2 + 16*a2**2*a5*a6**2/3 + 80*a2**2*a5*a6/9 - 8*a2**2*a5/9 + 48*a2**2*a6**3 - 40*a2**2*a6**2 + 8*a2**2*a6 + 16*a2*a6**3 - 8*a2*a6**2 + 8*a2*a6/9",
          "-36*a0**3*a3*a5 + 12*a0**3*a4**2 + 24*a0**2*a1*a3*a5 - 288*a0**2*a1*a3*a6 + 60*a0**2*a1*a3 - 8*a0**2*a1*a4**2 + 32*a0**2*a1*a4*a5 - 180*a0**2*a2**2*a3 - 32*a0**2*a2*a3**2/9 - 32*a0**2*a2*a3*a4/9 - 64*a0**2*a2*a3*a5/3 + 168*a0**2*a2*a3*a6 - 40*a0**2*a2*a3 + 16*a0**2*a2*a4**2/3 - 64*a0**2*a2*a4*a5/3 - 252*a0**2*a2*a4*a6 + 36*a0**2*a2*a4 + 40*a0**2*a2*a5**2 + 32*a0**2*a3*a4*a6/27 + 16*a0**2*a3*a4/81 - 224*a0**2*a3*a5**2/81 - 160*a0**2*a3*a5*a6/9 + 16*a0**2*a3*a5/27 - 128*a0**2*a3*a6**2 + 160*a0**2*a3*a6/3 - 56*a0**2*a3/9 + 160*a0**2*a4**2*a5/243 + 64*a0**2*a4**2*a6/9 - 64*a0**2*a4*a5**2/81 + 272*a0**2*a4*a5*a6/9 - 152*a0**2*a4*a5/27 + 72*a0**2*a4*a6**2 - 36*a0**2*a4*a6 + 4*a0**2*a4 - 160*a0**2*a5**3/27 - 80*a0**2*a5**2*a6/3 + 8*a0**2*a5**2 - 72*a0**2*a5*a6**2 + 18*a0**2*a5*a6 + 4*a0**2*a5 + 576*a0*a1**2*a2*a3 + 32*a0*a1**2*a3**2/9 + 32*a0*a1**2*a3*a4/9 + 16*a0*a1**2*a3*a5/3 + 24*a0*a1**2*a3*a6 + 144*a0*a1**2*a4*a6 - 28*a0*a1**2*a4 + 20*a0*a1**2*a5**2 - 192*a0*a1*a2**2*a3 + 300*a0*a1*a2**2*a4 - 160*a0*a1*a2*a3*a4/27 + 448*a0*a1*a2*a3*a5/9 + 224*a0*a1*a2*a3*a6 - 128*a0*a1*a2*a3/3 - 608*a0*a1*a2*a4**2/27 - 304*a0*a1*a2*a4*a5/9 - 104*a0*a1*a2*a4*a6 + 140*a0*a1*a2*a4/3 - 64*a0*a1*a2*a5**2/3 + 156*a0*a1*a2*a5*a6 - 74*a0*a1*a2*a5 - 224*a0*a1*a3*a5*a6/9 + 1072*a0*a1*a3*a5/81 - 32*a0*a1*a3*a6/3 + 32*a0*a1*a3/9 + 64*a0*a1*a4**2*a6/27 - 512*a0*a1*a4**2/243 + 256*a0*a1*a4*a5**2/243 - 160*a0*a1*a4*a5*a6/9 + 656*a0*a1*a4*a5/81 + 32*a0*a1*a4*a6**2 - 160*a0*a1*a4*a6/9 + 40*a0*a1*a4/27 + 256*a0*a1*a5**3/81 - 208*a0*a1*a5**2*a6/9 + 104*a0*a1*a5**2/9 - 120*a0*a1*a5*a6**2 + 280*a0*a1*a5*a6/3 - 20*a0*a1*a5 - 504*a0*a1*a6**3 + 276*a0*a1*a6**2 - 6*a0*a1*a6 - 8*a0*a1 - 96*a0*a2**3*a3 - 48*a0*a2**3*a4 + 252*a0*a2**3*a5 - 128*a0*a2**2*a3*a5/9 + 64*a0*a2**2*a3*a6 - 64*a0*a2**2*a3/3 + 64*a0*a2**2*a4**2/27 - 128*a0*a2**2*a4*a5/9 - 32*a0*a2**2*a4*a6 + 8*a0*a2**2*a4 - 32*a0*a2**2*a5**2 - 128*a0*a2**2*a5*a6 + 48*a0*a2**2*a5 + 792*a0*a2**2*a6**2 - 396*a0*a2**2*a6 + 27*a0*a2**2 - 608*a0*a2*a3*a6**2/9 + 448*a0*a2*a3*a6/9 - 56*a0*a2*a3/9 + 320*a0*a2*a4*a5*a6/81 - 176*a0*a2*a4*a5/81 - 224*a0*a2*a4*a6**2/9 + 112*a0*a2*a4*a6/9 - 64*a0*a2*a5**2*a6/27 + 32*a0*a2*a5**2/27 - 144*a0*a2*a5*a6**2 + 680*a0*a2*a5*a6/9 - 68*a0*a2*a5/9 - 264*a0*a2*a6**3 + 272*a0*a2*a6**2 - 94*a0*a2*a6 + 10*a0*a2 - 256*a0*a4*a6**3/27 + 832*a0*a4*a6**2/81 - 128*a0*a4*a6/81 + 64*a0*a5**2*a6**2/27 - 176*a0*a5**2*a6/81 - 64*a0*a5*a6**3/9 + 112*a0*a5*a6**2/27 + 8*a0*a5*a6/27 - 128*a0*a6**4 + 352*a0*a6**3/3 - 296*a0*a6**2/9 + 28*a0*a6/9 - 216*a1**4*a3 + 72*a1**3*a2*a3 - 168*a1**3*a2*a4 + 128*a1**3*a3*a4/27 - 64*a1**3*a3*a5/3 - 96*a1**3*a3*a6 + 16*a1**3*a3 + 320*a1**3*a4**2/27 + 160*a1**3*a4*a5/9 + 32*a1**3*a4*a6 - 16*a1**3*a4 + 8*a1**3*a5**2 + 168*a1**3*a5*a6 - 24*a1**3*a5 + 48*a1**2*a2**2*a3 + 32*a1**2*a2**2*a4 - 276*a1**2*a2**2*a5 + 512*a1**2*a2*a3*a5/27 - 32*a1**2*a2*a3*a6 + 16*a1**2*a2*a3 - 128*a1**2*a2*a4**2/81 + 160*a1**2*a2*a4*a5/9 + 32*a1**2*a2*a4*a6/3 - 32*a1**2*a2*a4/9 + 256*a1**2*a2*a5**2/9 + 88*a1**2*a2*a5*a6 - 40*a1**2*a2*a5 + 864*a1**2*a2*a6**2 - 372*a1**2*a2*a6 + 36*a1**2*a2 - 320*a1**2*a3*a6**2/9 + 1024*a1**2*a3*a6/27 - 80*a1**2*a3/9 + 256*a1**2*a4*a5*a6/81 - 160*a1**2*a4*a5/81 - 512*a1**2*a4*a6**2/9 + 1024*a1**2*a4*a6/27 - 160*a1**2*a4/27 + 32*a1**2*a5**3/81 + 544*a1**2*a5**2*a6/27 - 112*a1**2*a5**2/27 + 64*a1**2*a5*a6**2/3 + 32*a1**2*a5*a6/3 - 16*a1**2*a5/3 - 96*a1**2*a6**3 + 160*a1**2*a6**2 - 80*a1**2*a6 + 12*a1**2 + 8*a1*a2**3*a5 - 1224*a1*a2**3*a6 + 288*a1*a2**3 + 896*a1*a2**2*a3*a6/9 - 128*a1*a2**2*a3/3 - 128*a1*a2**2*a4*a5/81 + 896*a1*a2**2*a4*a6/9 - 256*a1*a2**2*a4/9 - 128*a1*a2**2*a5**2/27 + 96*a1*a2**2*a5*a6 - 320*a1*a2**2*a5/9 + 264*a1*a2**2*a6**2 - 296*a1*a2**2*a6 + 72*a1*a2**2 + 448*a1*a2*a4*a6**2/27 - 448*a1*a2*a4*a6/81 - 32*a1*a2*a4/27 + 64*a1*a2*a5**2*a6/27 - 256*a1*a2*a5**2/81 + 640*a1*a2*a5*a6**2/9 - 736*a1*a2*a5*a6/27 + 80*a1*a2*a5/27 + 128*a1*a2*a6**3 - 160*a1*a2*a6**2/3 + 32*a1*a2*a6/9 + 64*a1*a5*a6**3/9 - 224*a1*a5*a6**2/27 + 160*a1*a5*a6/81 + 64*a1*a6**4 - 64*a1*a6**3 + 208*a1*a6**2/9 - 80*a1*a6/27 + 324*a2**5 - 32*a2**4*a3 - 32*a2**4*a4 - 32*a2**4*a5 - 72*a2**4*a6 + 72*a2**4 - 64*a2**3*a4*a6/9 - 32*a2**3*a4/9 - 32*a2**3*a5**2/27 - 32*a2**3*a5*a6 + 16*a2**3*a5/3 - 48*a2**3*a6**2 - 32*a2**2*a5*a6**2/9 - 160*a2**2*a5*a6/27 + 16*a2**2*a5/27 - 32*a2**2*a6**3 + 80*a2**2*a6**2/3 - 16*a2**2*a6/3 - 32*a2*a6**3/3 + 16*a2*a6**2/3 - 16*a2*a6/27"
        &#93;,
        &#91;
          "24*a0*a2*a3*a4 + 48*a0*a2*a3*a5**2 + 432*a0*a2*a3*a5*a6 - 324*a0*a2*a3*a5 - 16*a0*a2*a4**2*a5 - 144*a0*a2*a4**2*a6 + 132*a0*a2*a4**2 + 144*a0*a3*a5*a6**2 - 30*a0*a3*a5*a6 - 5*a0*a3*a5 + 1296*a0*a3*a6**3 - 1458*a0*a3*a6**2 + 531*a0*a3*a6 - 63*a0*a3 + 4*a0*a4**2*a6 - 4*a0*a4**2/3 - 32*a0*a4*a5**2*a6 + 14*a0*a4*a5**2/3 - 288*a0*a4*a5*a6**2 + 306*a0*a4*a5*a6 - 68*a0*a4*a5 + 16*a0*a5**4/3 + 48*a0*a5**3*a6 - 40*a0*a5**3 - 24*a1**2*a3*a4 - 48*a1**2*a3*a5**2 - 432*a1**2*a3*a5*a6 + 324*a1**2*a3*a5 + 16*a1**2*a4**2*a5 + 144*a1**2*a4**2*a6 - 132*a1**2*a4**2 - 288*a1*a2*a3*a5*a6 + 30*a1*a2*a3*a5 - 2592*a1*a2*a3*a6**2 + 2106*a1*a2*a3*a6 - 405*a1*a2*a3 - 4*a1*a2*a4**2 + 32*a1*a2*a4*a5**2 + 288*a1*a2*a4*a5*a6 - 216*a1*a2*a4*a5 + 180*a1*a3*a6**2 - 192*a1*a3*a6 + 45*a1*a3 - 96*a1*a4*a5*a6**2 + 32*a1*a4*a5*a6 + 2*a1*a4*a5 - 864*a1*a4*a6**3 + 1152*a1*a4*a6**2 - 480*a1*a4*a6 + 66*a1*a4 + 32*a1*a5**3*a6 - 10*a1*a5**3 + 288*a1*a5**2*a6**2 - 318*a1*a5**2*a6 + 57*a1*a5**2 + 144*a2**3*a3*a5 + 1296*a2**3*a3*a6 - 648*a2**3*a3 - 180*a2**2*a3*a6 + 135*a2**2*a3 + 96*a2**2*a4*a5*a6 - 34*a2**2*a4*a5 + 864*a2**2*a4*a6**2 - 882*a2**2*a4*a6 + 198*a2**2*a4 + 16*a2**2*a5**3 + 144*a2**2*a5**2*a6 - 84*a2**2*a5**2 - 48*a2*a4*a6**2 + 40*a2*a4*a6 + 144*a2*a5**2*a6**2 - 90*a2*a5**2*a6 + 14*a2*a5**2 + 1296*a2*a5*a6**3 - 1602*a2*a5*a6**2 + 507*a2*a5*a6 - 33*a2*a5 + 144*a5*a6**4 - 180*a5*a6**3 + 86*a5*a6**2 - 14*a5*a6 + 1296*a6**5 - 2268*a6**4 + 1368*a6**3 - 351*a6**2 + 33*a6",
          "108*a0*a2*a3*a4 + 216*a0*a2*a3*a5**2 - 72*a0*a2*a4**2*a5 + 648*a0*a3*a5*a6**2 - 135*a0*a3*a5*a6 - 45*a0*a3*a5/2 + 18*a0*a4**2*a6 - 6*a0*a4**2 - 144*a0*a4*a5**2*a6 + 21*a0*a4*a5**2 + 24*a0*a5**4 - 108*a1**2*a3*a4 - 216*a1**2*a3*a5**2 + 72*a1**2*a4**2*a5 - 1296*a1*a2*a3*a5*a6 + 135*a1*a2*a3*a5 - 18*a1*a2*a4**2 + 144*a1*a2*a4*a5**2 + 810*a1*a3*a6**2 - 864*a1*a3*a6 + 405*a1*a3/2 - 432*a1*a4*a5*a6**2 + 144*a1*a4*a5*a6 + 9*a1*a4*a5 + 144*a1*a5**3*a6 - 45*a1*a5**3 + 648*a2**3*a3*a5 - 810*a2**2*a3*a6 + 1215*a2**2*a3/2 + 432*a2**2*a4*a5*a6 - 153*a2**2*a4*a5 + 72*a2**2*a5**3 - 216*a2*a4*a6**2 + 180*a2*a4*a6 + 648*a2*a5**2*a6**2 - 405*a2*a5**2*a6 + 63*a2*a5**2 + 648*a5*a6**4 - 810*a5*a6**3 + 387*a5*a6**2 - 63*a5*a6",
          "432*a0*a2**2*a3*a5 - 144*a0*a2**2*a4**2 - 16*a0*a2*a3*a4 - 32*a0*a2*a3*a5**2 - 288*a0*a2*a3*a5*a6 + 216*a0*a2*a3*a5 + 1296*a0*a2*a3*a6**2 - 486*a0*a2*a3*a6 + 72*a0*a2*a3 + 32*a0*a2*a4**2*a5/3 + 96*a0*a2*a4**2*a6 - 88*a0*a2*a4**2 - 288*a0*a2*a4*a5*a6 + 30*a0*a2*a4*a5 + 48*a0*a2*a5**3 - 96*a0*a3*a5*a6**2 + 20*a0*a3*a5*a6 + 10*a0*a3*a5/3 - 864*a0*a3*a6**3 + 972*a0*a3*a6**2 - 354*a0*a3*a6 + 42*a0*a3 - 8*a0*a4**2*a6/3 + 8*a0*a4**2/9 + 64*a0*a4*a5**2*a6/3 - 28*a0*a4*a5**2/9 + 192*a0*a4*a5*a6**2 - 204*a0*a4*a5*a6 + 136*a0*a4*a5/3 - 36*a0*a4*a6**2 + 24*a0*a4*a6 - 4*a0*a4 - 32*a0*a5**4/9 - 32*a0*a5**3*a6 + 80*a0*a5**3/3 - 12*a0*a5**2*a6 + 9*a0*a5**2 - 432*a1**2*a2*a3*a5 + 144*a1**2*a2*a4**2 + 16*a1**2*a3*a4 + 32*a1**2*a3*a5**2 + 288*a1**2*a3*a5*a6 - 216*a1**2*a3*a5 - 324*a1**2*a3*a6 + 54*a1**2*a3 - 32*a1**2*a4**2*a5/3 - 96*a1**2*a4**2*a6 + 88*a1**2*a4**2 + 60*a1**2*a4*a5 - 2592*a1*a2**2*a3*a6 + 810*a1*a2**2*a3 + 288*a1*a2**2*a4*a5 + 192*a1*a2*a3*a5*a6 - 20*a1*a2*a3*a5 + 1728*a1*a2*a3*a6**2 - 1404*a1*a2*a3*a6 + 270*a1*a2*a3 + 8*a1*a2*a4**2/3 - 64*a1*a2*a4*a5**2/3 - 192*a1*a2*a4*a5*a6 + 144*a1*a2*a4*a5 - 864*a1*a2*a4*a6**2 + 576*a1*a2*a4*a6 - 102*a1*a2*a4 + 288*a1*a2*a5**2*a6 - 30*a1*a2*a5**2 - 120*a1*a3*a6**2 + 128*a1*a3*a6 - 30*a1*a3 + 64*a1*a4*a5*a6**2 - 64*a1*a4*a5*a6/3 - 4*a1*a4*a5/3 + 576*a1*a4*a6**3 - 768*a1*a4*a6**2 + 320*a1*a4*a6 - 44*a1*a4 - 64*a1*a5**3*a6/3 + 20*a1*a5**3/3 - 192*a1*a5**2*a6**2 + 212*a1*a5**2*a6 - 38*a1*a5**2 + 72*a1*a5*a6**2 + 36*a1*a5*a6 - 18*a1*a5 + 1296*a2**4*a3 - 96*a2**3*a3*a5 - 864*a2**3*a3*a6 + 432*a2**3*a3 + 864*a2**3*a4*a6 - 270*a2**3*a4 + 144*a2**3*a5**2 + 120*a2**2*a3*a6 - 90*a2**2*a3 - 64*a2**2*a4*a5*a6 + 68*a2**2*a4*a5/3 - 576*a2**2*a4*a6**2 + 588*a2**2*a4*a6 - 132*a2**2*a4 - 32*a2**2*a5**3/3 - 96*a2**2*a5**2*a6 + 56*a2**2*a5**2 + 1296*a2**2*a5*a6**2 - 594*a2**2*a5*a6 - 21*a2**2*a5 + 32*a2*a4*a6**2 - 80*a2*a4*a6/3 - 96*a2*a5**2*a6**2 + 60*a2*a5**2*a6 - 28*a2*a5**2/3 - 864*a2*a5*a6**3 + 1068*a2*a5*a6**2 - 338*a2*a5*a6 + 22*a2*a5 + 1296*a2*a6**4 - 1188*a2*a6**3 + 324*a2*a6**2 - 33*a2*a6 - 96*a5*a6**4 + 120*a5*a6**3 - 172*a5*a6**2/3 + 28*a5*a6/3 - 864*a6**5 + 1512*a6**4 - 912*a6**3 + 234*a6**2 - 22*a6",
          "432*a0*a1*a2*a3*a5 - 144*a0*a1*a2*a4**2 + 1296*a0*a1*a3*a6**2 - 810*a0*a1*a3*a6 + 126*a0*a1*a3 - 288*a0*a1*a4*a5*a6 + 90*a0*a1*a4*a5 + 48*a0*a1*a5**3 - 288*a0*a2**2*a3*a5 + 324*a0*a2**2*a3 + 96*a0*a2**2*a4**2 + 32*a0*a2*a3*a4/3 + 64*a0*a2*a3*a5**2/3 + 192*a0*a2*a3*a5*a6 - 144*a0*a2*a3*a5 - 864*a0*a2*a3*a6**2 + 324*a0*a2*a3*a6 - 48*a0*a2*a3 - 64*a0*a2*a4**2*a5/9 - 64*a0*a2*a4**2*a6 + 176*a0*a2*a4**2/3 + 192*a0*a2*a4*a5*a6 - 20*a0*a2*a4*a5 + 144*a0*a2*a4*a6 - 42*a0*a2*a4 - 32*a0*a2*a5**3 + 48*a0*a2*a5**2 + 64*a0*a3*a5*a6**2 - 40*a0*a3*a5*a6/3 - 20*a0*a3*a5/9 + 576*a0*a3*a6**3 - 648*a0*a3*a6**2 + 236*a0*a3*a6 - 28*a0*a3 + 16*a0*a4**2*a6/9 - 16*a0*a4**2/27 - 128*a0*a4*a5**2*a6/9 + 56*a0*a4*a5**2/27 - 128*a0*a4*a5*a6**2 + 136*a0*a4*a5*a6 - 272*a0*a4*a5/9 + 24*a0*a4*a6**2 - 16*a0*a4*a6 + 8*a0*a4/3 + 64*a0*a5**4/27 + 64*a0*a5**3*a6/3 - 160*a0*a5**3/9 + 8*a0*a5**2*a6 - 6*a0*a5**2 + 180*a0*a5*a6**2 - 111*a0*a5*a6 + 18*a0*a5 - 432*a1**3*a3*a5 + 144*a1**3*a4**2 + 288*a1**2*a2*a3*a5 - 2592*a1**2*a2*a3*a6 + 486*a1**2*a2*a3 - 96*a1**2*a2*a4**2 + 288*a1**2*a2*a4*a5 - 32*a1**2*a3*a4/3 - 64*a1**2*a3*a5**2/3 - 192*a1**2*a3*a5*a6 + 144*a1**2*a3*a5 + 216*a1**2*a3*a6 - 36*a1**2*a3 + 64*a1**2*a4**2*a5/9 + 64*a1**2*a4**2*a6 - 176*a1**2*a4**2/3 - 40*a1**2*a4*a5 - 864*a1**2*a4*a6**2 + 360*a1**2*a4*a6 - 36*a1**2*a4 + 288*a1**2*a5**2*a6 - 90*a1**2*a5**2 + 1296*a1*a2**3*a3 + 1728*a1*a2**2*a3*a6 - 540*a1*a2**2*a3 - 192*a1*a2**2*a4*a5 + 864*a1*a2**2*a4*a6 - 234*a1*a2**2*a4 + 144*a1*a2**2*a5**2 - 128*a1*a2*a3*a5*a6 + 40*a1*a2*a3*a5/3 - 1152*a1*a2*a3*a6**2 + 936*a1*a2*a3*a6 - 180*a1*a2*a3 - 16*a1*a2*a4**2/9 + 128*a1*a2*a4*a5**2/9 + 128*a1*a2*a4*a5*a6 - 96*a1*a2*a4*a5 + 576*a1*a2*a4*a6**2 - 384*a1*a2*a4*a6 + 68*a1*a2*a4 - 192*a1*a2*a5**2*a6 + 20*a1*a2*a5**2 + 1296*a1*a2*a5*a6**2 - 738*a1*a2*a5*a6 + 72*a1*a2*a5 + 80*a1*a3*a6**2 - 256*a1*a3*a6/3 + 20*a1*a3 - 128*a1*a4*a5*a6**2/3 + 128*a1*a4*a5*a6/9 + 8*a1*a4*a5/9 - 384*a1*a4*a6**3 + 512*a1*a4*a6**2 - 640*a1*a4*a6/3 + 88*a1*a4/3 + 128*a1*a5**3*a6/9 - 40*a1*a5**3/9 + 128*a1*a5**2*a6**2 - 424*a1*a5**2*a6/3 + 76*a1*a5**2/3 - 48*a1*a5*a6**2 - 24*a1*a5*a6 + 12*a1*a5 + 1296*a1*a6**4 - 1080*a1*a6**3 + 36*a1*a6**2 + 144*a1*a6 - 27*a1 - 864*a2**4*a3 + 64*a2**3*a3*a5 + 576*a2**3*a3*a6 - 288*a2**3*a3 - 576*a2**3*a4*a6 + 180*a2**3*a4 - 96*a2**3*a5**2 + 36*a2**3*a5 - 80*a2**2*a3*a6 + 60*a2**2*a3 + 128*a2**2*a4*a5*a6/3 - 136*a2**2*a4*a5/9 + 384*a2**2*a4*a6**2 - 392*a2**2*a4*a6 + 88*a2**2*a4 + 64*a2**2*a5**3/9 + 64*a2**2*a5**2*a6 - 112*a2**2*a5**2/3 - 864*a2**2*a5*a6**2 + 396*a2**2*a5*a6 + 14*a2**2*a5 - 108*a2**2*a6**2 + 207*a2**2*a6 - 81*a2**2 - 64*a2*a4*a6**2/3 + 160*a2*a4*a6/9 + 64*a2*a5**2*a6**2 - 40*a2*a5**2*a6 + 56*a2*a5**2/9 + 576*a2*a5*a6**3 - 712*a2*a5*a6**2 + 676*a2*a5*a6/3 - 44*a2*a5/3 - 864*a2*a6**4 + 792*a2*a6**3 - 216*a2*a6**2 + 22*a2*a6 + 64*a5*a6**4 - 80*a5*a6**3 + 344*a5*a6**2/9 - 56*a5*a6/9 + 576*a6**5 - 1008*a6**4 + 608*a6**3 - 156*a6**2 + 44*a6/3",
          "432*a0**2*a2*a3*a5 - 144*a0**2*a2*a4**2 + 1296*a0**2*a3*a6**2 - 810*a0**2*a3*a6 + 126*a0**2*a3 - 288*a0**2*a4*a5*a6 + 90*a0**2*a4*a5 + 48*a0**2*a5**3 - 432*a0*a1**2*a3*a5 + 144*a0*a1**2*a4**2 - 288*a0*a1*a2*a3*a5 - 2592*a0*a1*a2*a3*a6 + 1134*a0*a1*a2*a3 + 96*a0*a1*a2*a4**2 + 288*a0*a1*a2*a4*a5 - 864*a0*a1*a3*a6**2 + 540*a0*a1*a3*a6 - 84*a0*a1*a3 + 192*a0*a1*a4*a5*a6 - 60*a0*a1*a4*a5 - 864*a0*a1*a4*a6**2 + 504*a0*a1*a4*a6 - 78*a0*a1*a4 - 32*a0*a1*a5**3 + 288*a0*a1*a5**2*a6 - 42*a0*a1*a5**2 + 1296*a0*a2**3*a3 + 192*a0*a2**2*a3*a5 - 216*a0*a2**2*a3 - 64*a0*a2**2*a4**2 + 864*a0*a2**2*a4*a6 - 90*a0*a2**2*a4 + 144*a0*a2**2*a5**2 - 64*a0*a2*a3*a4/9 - 128*a0*a2*a3*a5**2/9 - 128*a0*a2*a3*a5*a6 + 96*a0*a2*a3*a5 + 576*a0*a2*a3*a6**2 - 216*a0*a2*a3*a6 + 32*a0*a2*a3 + 128*a0*a2*a4**2*a5/27 + 128*a0*a2*a4**2*a6/3 - 352*a0*a2*a4**2/9 - 128*a0*a2*a4*a5*a6 + 40*a0*a2*a4*a5/3 - 96*a0*a2*a4*a6 + 28*a0*a2*a4 + 64*a0*a2*a5**3/3 - 32*a0*a2*a5**2 + 1296*a0*a2*a5*a6**2 - 630*a0*a2*a5*a6 - 3*a0*a2*a5 - 128*a0*a3*a5*a6**2/3 + 80*a0*a3*a5*a6/9 + 40*a0*a3*a5/27 - 384*a0*a3*a6**3 + 432*a0*a3*a6**2 - 472*a0*a3*a6/3 + 56*a0*a3/3 - 32*a0*a4**2*a6/27 + 32*a0*a4**2/81 + 256*a0*a4*a5**2*a6/27 - 112*a0*a4*a5**2/81 + 256*a0*a4*a5*a6**2/3 - 272*a0*a4*a5*a6/3 + 544*a0*a4*a5/27 - 16*a0*a4*a6**2 + 32*a0*a4*a6/3 - 16*a0*a4/9 - 128*a0*a5**4/81 - 128*a0*a5**3*a6/9 + 320*a0*a5**3/27 - 16*a0*a5**2*a6/3 + 4*a0*a5**2 - 120*a0*a5*a6**2 + 74*a0*a5*a6 - 12*a0*a5 + 1296*a0*a6**4 - 1620*a0*a6**3 + 558*a0*a6**2 - 45*a0*a6 - 3*a0 + 288*a1**3*a3*a5 - 324*a1**3*a3 - 96*a1**3*a4**2 - 192*a1**2*a2*a3*a5 + 1728*a1**2*a2*a3*a6 - 324*a1**2*a2*a3 + 64*a1**2*a2*a4**2 - 192*a1**2*a2*a4*a5 - 144*a1**2*a2*a4 + 64*a1**2*a3*a4/9 + 128*a1**2*a3*a5**2/9 + 128*a1**2*a3*a5*a6 - 96*a1**2*a3*a5 - 144*a1**2*a3*a6 + 24*a1**2*a3 - 128*a1**2*a4**2*a5/27 - 128*a1**2*a4**2*a6/3 + 352*a1**2*a4**2/9 + 80*a1**2*a4*a5/3 + 576*a1**2*a4*a6**2 - 240*a1**2*a4*a6 + 24*a1**2*a4 - 192*a1**2*a5**2*a6 + 60*a1**2*a5**2 + 252*a1**2*a5*a6 - 36*a1**2*a5 - 864*a1*a2**3*a3 - 1152*a1*a2**2*a3*a6 + 360*a1*a2**2*a3 + 128*a1*a2**2*a4*a5 - 576*a1*a2**2*a4*a6 + 156*a1*a2**2*a4 - 96*a1*a2**2*a5**2 - 144*a1*a2**2*a5 + 256*a1*a2*a3*a5*a6/3 - 80*a1*a2*a3*a5/9 + 768*a1*a2*a3*a6**2 - 624*a1*a2*a3*a6 + 120*a1*a2*a3 + 32*a1*a2*a4**2/27 - 256*a1*a2*a4*a5**2/27 - 256*a1*a2*a4*a5*a6/3 + 64*a1*a2*a4*a5 - 384*a1*a2*a4*a6**2 + 256*a1*a2*a4*a6 - 136*a1*a2*a4/3 + 128*a1*a2*a5**2*a6 - 40*a1*a2*a5**2/3 - 864*a1*a2*a5*a6**2 + 492*a1*a2*a5*a6 - 48*a1*a2*a5 + 972*a1*a2*a6**2 - 504*a1*a2*a6 + 54*a1*a2 - 160*a1*a3*a6**2/3 + 512*a1*a3*a6/9 - 40*a1*a3/3 + 256*a1*a4*a5*a6**2/9 - 256*a1*a4*a5*a6/27 - 16*a1*a4*a5/27 + 256*a1*a4*a6**3 - 1024*a1*a4*a6**2/3 + 1280*a1*a4*a6/9 - 176*a1*a4/9 - 256*a1*a5**3*a6/27 + 80*a1*a5**3/27 - 256*a1*a5**2*a6**2/3 + 848*a1*a5**2*a6/9 - 152*a1*a5**2/9 + 32*a1*a5*a6**2 + 16*a1*a5*a6 - 8*a1*a5 - 864*a1*a6**4 + 720*a1*a6**3 - 24*a1*a6**2 - 96*a1*a6 + 18*a1 + 576*a2**4*a3 - 128*a2**3*a3*a5/3 - 384*a2**3*a3*a6 + 192*a2**3*a3 + 384*a2**3*a4*a6 - 120*a2**3*a4 + 64*a2**3*a5**2 - 24*a2**3*a5 - 540*a2**3*a6 + 189*a2**3 + 160*a2**2*a3*a6/3 - 40*a2**2*a3 - 256*a2**2*a4*a5*a6/9 + 272*a2**2*a4*a5/27 - 256*a2**2*a4*a6**2 + 784*a2**2*a4*a6/3 - 176*a2**2*a4/3 - 128*a2**2*a5**3/27 - 128*a2**2*a5**2*a6/3 + 224*a2**2*a5**2/9 + 576*a2**2*a5*a6**2 - 264*a2**2*a5*a6 - 28*a2**2*a5/3 + 72*a2**2*a6**2 - 138*a2**2*a6 + 54*a2**2 + 128*a2*a4*a6**2/9 - 320*a2*a4*a6/27 - 128*a2*a5**2*a6**2/3 + 80*a2*a5**2*a6/3 - 112*a2*a5**2/27 - 384*a2*a5*a6**3 + 1424*a2*a5*a6**2/3 - 1352*a2*a5*a6/9 + 88*a2*a5/9 + 576*a2*a6**4 - 528*a2*a6**3 + 144*a2*a6**2 - 44*a2*a6/3 - 128*a5*a6**4/3 + 160*a5*a6**3/3 - 688*a5*a6**2/27 + 112*a5*a6/27 - 384*a6**5 + 672*a6**4 - 1216*a6**3/3 + 104*a6**2 - 88*a6/9"
        &#93;,
        &#91;
          "24*a0**2*a3**2*a6 - 4*a0**2*a3**2 - 8*a0**2*a3*a4*a5 + 24*a0**2*a3*a4*a6 - 4*a0**2*a3*a4 - 16*a0**2*a3*a5**2 + 16*a0**2*a4**3/9 + 8*a0**2*a4**2*a5/3 - 48*a0*a1*a2*a3**2 - 48*a0*a1*a2*a3*a4 - 24*a0*a1*a3*a4*a6 + 28*a0*a1*a3*a4/3 - 32*a0*a1*a3*a5**2/3 - 120*a0*a1*a3*a5*a6 + 28*a0*a1*a3*a5 + 40*a0*a1*a4**2*a5/9 + 16*a0*a1*a4**2*a6 + 8*a0*a1*a4*a5**2/3 - 24*a0*a2**2*a3*a4 - 48*a0*a2**2*a3*a5 - 8*a0*a2**2*a4**2 - 24*a0*a2*a3*a5*a6 - 212*a0*a2*a3*a5/3 - 216*a0*a2*a3*a6**2 + 72*a0*a2*a3*a6 - 6*a0*a2*a3 - 16*a0*a2*a4**2*a6 + 232*a0*a2*a4**2/9 + 40*a0*a2*a4*a5**2/9 - 24*a0*a2*a4*a5*a6 - 4*a0*a2*a4*a5/3 + 16*a0*a2*a5**3/3 + 24*a0*a3*a6**3 - 244*a0*a3*a6**2 + 116*a0*a3*a6 - 38*a0*a3/3 - 40*a0*a4*a5*a6**2/3 + 128*a0*a4*a5*a6/3 - 28*a0*a4*a5/3 - 48*a0*a4*a6**3 - 64*a0*a4*a6**2 + 24*a0*a4*a6 + 8*a0*a5**3*a6/3 - 52*a0*a5**3/9 + 8*a0*a5**2*a6**2 + 16*a0*a5**2*a6 + 2*a0*a5**2 + 24*a1**3*a3**2 + 24*a1**3*a3*a4 + 24*a1**2*a2*a3*a4 + 48*a1**2*a2*a3*a5 + 8*a1**2*a2*a4**2 - 40*a1**2*a3*a5*a6 + 88*a1**2*a3*a5 - 216*a1**2*a3*a6**2 + 108*a1**2*a3*a6 - 12*a1**2*a3 + 16*a1**2*a4**2*a6/3 - 64*a1**2*a4**2/3 + 8*a1**2*a4*a5**2/3 + 24*a1**2*a4*a5*a6 + 12*a1**2*a4*a5 + 32*a1*a2**2*a3*a5 + 216*a1*a2**2*a3*a6 - 36*a1*a2**2*a3 + 16*a1*a2**2*a4**2/3 + 24*a1*a2**2*a4*a5 - 48*a1*a2*a3*a6**2 + 472*a1*a2*a3*a6 - 114*a1*a2*a3 - 100*a1*a2*a4*a5/3 - 48*a1*a2*a4*a6**2 + 220*a1*a2*a4*a6 - 40*a1*a2*a4 + 16*a1*a2*a5**3/3 + 48*a1*a2*a5**2*a6 - 24*a1*a2*a5**2 - 16*a1*a4*a6**3 + 352*a1*a4*a6**2/3 - 104*a1*a4*a6/3 + 8*a1*a4/3 + 8*a1*a5**2*a6**2 - 100*a1*a5**2*a6/3 + 8*a1*a5**2/3 + 24*a1*a5*a6**3 + 40*a1*a5*a6**2 + 2*a1*a5*a6 + 24*a2**3*a3*a6 - 228*a2**3*a3 + 40*a2**3*a4*a5/3 + 96*a2**3*a4*a6 - 120*a2**3*a4 + 16*a2**3*a5**2 + 16*a2**2*a4*a6**2 - 328*a2**2*a4*a6/3 + 8*a2**2*a4 + 16*a2**2*a5**2*a6 - 56*a2**2*a5**2/3 + 192*a2**2*a5*a6**2 - 160*a2**2*a5*a6 + 20*a2**2*a5 + 24*a2*a5*a6**3 - 144*a2*a5*a6**2 + 124*a2*a5*a6/3 - 4*a2*a5/3 + 216*a2*a6**4 - 252*a2*a6**3 + 120*a2*a6**2 - 20*a2*a6 - 120*a6**4 + 84*a6**3 - 56*a6**2/3 + 4*a6/3",
          "108*a0**2*a3**2*a6 - 18*a0**2*a3**2 - 36*a0**2*a3*a4*a5 + 8*a0**2*a4**3 - 216*a0*a1*a2*a3**2 - 108*a0*a1*a3*a4*a6 + 42*a0*a1*a3*a4 - 48*a0*a1*a3*a5**2 + 20*a0*a1*a4**2*a5 - 108*a0*a2**2*a3*a4 - 108*a0*a2*a3*a5*a6 - 318*a0*a2*a3*a5 - 72*a0*a2*a4**2*a6 + 116*a0*a2*a4**2 + 20*a0*a2*a4*a5**2 + 108*a0*a3*a6**3 - 1098*a0*a3*a6**2 + 522*a0*a3*a6 - 57*a0*a3 - 60*a0*a4*a5*a6**2 + 192*a0*a4*a5*a6 - 42*a0*a4*a5 + 12*a0*a5**3*a6 - 26*a0*a5**3 + 108*a1**3*a3**2 + 108*a1**2*a2*a3*a4 - 180*a1**2*a3*a5*a6 + 396*a1**2*a3*a5 + 24*a1**2*a4**2*a6 - 96*a1**2*a4**2 + 12*a1**2*a4*a5**2 + 144*a1*a2**2*a3*a5 + 24*a1*a2**2*a4**2 - 216*a1*a2*a3*a6**2 + 2124*a1*a2*a3*a6 - 513*a1*a2*a3 - 150*a1*a2*a4*a5 + 24*a1*a2*a5**3 - 72*a1*a4*a6**3 + 528*a1*a4*a6**2 - 156*a1*a4*a6 + 12*a1*a4 + 36*a1*a5**2*a6**2 - 150*a1*a5**2*a6 + 12*a1*a5**2 + 108*a2**3*a3*a6 - 1026*a2**3*a3 + 60*a2**3*a4*a5 + 72*a2**2*a4*a6**2 - 492*a2**2*a4*a6 + 36*a2**2*a4 + 72*a2**2*a5**2*a6 - 84*a2**2*a5**2 + 108*a2*a5*a6**3 - 648*a2*a5*a6**2 + 186*a2*a5*a6 - 6*a2*a5 - 540*a6**4 + 378*a6**3 - 84*a6**2 + 6*a6",
          "-16*a0**2*a3**2*a6 + 8*a0**2*a3**2/3 + 16*a0**2*a3*a4*a5/3 - 16*a0**2*a3*a4*a6 + 8*a0**2*a3*a4/3 + 32*a0**2*a3*a5**2/3 + 24*a0**2*a3*a5*a6 - 12*a0**2*a3*a5 - 32*a0**2*a4**3/27 - 16*a0**2*a4**2*a5/9 - 16*a0**2*a4**2*a6 + 16*a0**2*a4**2/3 + 8*a0**2*a4*a5**2/3 + 32*a0*a1*a2*a3**2 + 32*a0*a1*a2*a3*a4 - 24*a0*a1*a2*a3*a5 + 24*a0*a1*a2*a4**2 + 16*a0*a1*a3*a4*a6 - 56*a0*a1*a3*a4/9 + 64*a0*a1*a3*a5**2/9 + 80*a0*a1*a3*a5*a6 - 56*a0*a1*a3*a5/3 + 144*a0*a1*a3*a6**2 - 96*a0*a1*a3*a6 + 16*a0*a1*a3 - 80*a0*a1*a4**2*a5/27 - 32*a0*a1*a4**2*a6/3 - 16*a0*a1*a4*a5**2/9 - 8*a0*a1*a4*a5*a6 + 4*a0*a1*a4*a5/3 + 8*a0*a1*a5**3/3 + 16*a0*a2**2*a3*a4 + 32*a0*a2**2*a3*a5 - 72*a0*a2**2*a3*a6 - 12*a0*a2**2*a3 + 16*a0*a2**2*a4**2/3 + 32*a0*a2**2*a4*a5 + 16*a0*a2*a3*a5*a6 + 424*a0*a2*a3*a5/9 + 144*a0*a2*a3*a6**2 - 48*a0*a2*a3*a6 + 4*a0*a2*a3 + 32*a0*a2*a4**2*a6/3 - 464*a0*a2*a4**2/27 - 80*a0*a2*a4*a5**2/27 + 16*a0*a2*a4*a5*a6 + 8*a0*a2*a4*a5/9 + 72*a0*a2*a4*a6**2 - 112*a0*a2*a4*a6 + 40*a0*a2*a4/3 - 32*a0*a2*a5**3/9 + 8*a0*a2*a5**2*a6 + 28*a0*a2*a5**2 - 16*a0*a3*a6**3 + 488*a0*a3*a6**2/3 - 232*a0*a3*a6/3 + 76*a0*a3/9 + 80*a0*a4*a5*a6**2/9 - 256*a0*a4*a5*a6/9 + 56*a0*a4*a5/9 + 32*a0*a4*a6**3 + 128*a0*a4*a6**2/3 - 16*a0*a4*a6 - 16*a0*a5**3*a6/9 + 104*a0*a5**3/27 - 16*a0*a5**2*a6**2/3 - 32*a0*a5**2*a6/3 - 4*a0*a5**2/3 + 24*a0*a5*a6**3 + 12*a0*a5*a6**2 - 24*a0*a5*a6 + 4*a0*a5 - 16*a1**3*a3**2 - 16*a1**3*a3*a4 - 24*a1**3*a3*a5 - 16*a1**2*a2*a3*a4 - 32*a1**2*a2*a3*a5 - 360*a1**2*a2*a3*a6 + 120*a1**2*a2*a3 - 16*a1**2*a2*a4**2/3 + 16*a1**2*a2*a4*a5 + 80*a1**2*a3*a5*a6/3 - 176*a1**2*a3*a5/3 + 144*a1**2*a3*a6**2 - 72*a1**2*a3*a6 + 8*a1**2*a3 - 32*a1**2*a4**2*a6/9 + 128*a1**2*a4**2/9 - 16*a1**2*a4*a5**2/9 - 16*a1**2*a4*a5*a6 - 8*a1**2*a4*a5 - 48*a1**2*a4*a6**2 + 88*a1**2*a4*a6 - 12*a1**2*a4 + 16*a1**2*a5**2*a6 - 40*a1**2*a5**2 + 216*a1*a2**3*a3 - 64*a1*a2**2*a3*a5/3 - 144*a1*a2**2*a3*a6 + 24*a1*a2**2*a3 - 32*a1*a2**2*a4**2/9 - 16*a1*a2**2*a4*a5 - 48*a1*a2**2*a4*a6 + 4*a1*a2**2*a4 + 40*a1*a2**2*a5**2 + 32*a1*a2*a3*a6**2 - 944*a1*a2*a3*a6/3 + 76*a1*a2*a3 + 200*a1*a2*a4*a5/9 + 32*a1*a2*a4*a6**2 - 440*a1*a2*a4*a6/3 + 80*a1*a2*a4/3 - 32*a1*a2*a5**3/9 - 32*a1*a2*a5**2*a6 + 16*a1*a2*a5**2 + 120*a1*a2*a5*a6**2 - 244*a1*a2*a5*a6 + 50*a1*a2*a5 + 32*a1*a4*a6**3/3 - 704*a1*a4*a6**2/9 + 208*a1*a4*a6/9 - 16*a1*a4/9 - 16*a1*a5**2*a6**2/3 + 200*a1*a5**2*a6/9 - 16*a1*a5**2/9 - 16*a1*a5*a6**3 - 80*a1*a5*a6**2/3 - 4*a1*a5*a6/3 + 144*a1*a6**4 - 384*a1*a6**3 + 136*a1*a6**2 - 14*a1*a6 + 72*a2**4*a4 - 16*a2**3*a3*a6 + 152*a2**3*a3 - 80*a2**3*a4*a5/9 - 64*a2**3*a4*a6 + 80*a2**3*a4 - 32*a2**3*a5**2/3 + 72*a2**3*a5*a6 + 76*a2**3*a5 - 32*a2**2*a4*a6**2/3 + 656*a2**2*a4*a6/9 - 16*a2**2*a4/3 - 32*a2**2*a5**2*a6/3 + 112*a2**2*a5**2/9 - 128*a2**2*a5*a6**2 + 320*a2**2*a5*a6/3 - 40*a2**2*a5/3 + 72*a2**2*a6**3 + 96*a2**2*a6**2 - 4*a2**2*a6 - 16*a2*a5*a6**3 + 96*a2*a5*a6**2 - 248*a2*a5*a6/9 + 8*a2*a5/9 - 144*a2*a6**4 + 168*a2*a6**3 - 80*a2*a6**2 + 40*a2*a6/3 + 80*a6**4 - 56*a6**3 + 112*a6**2/9 - 8*a6/9",
          "48*a0**2*a2*a3*a5 - 16*a0**2*a2*a4**2 + 32*a0**2*a3**2*a6/3 - 16*a0**2*a3**2/9 - 32*a0**2*a3*a4*a5/9 + 32*a0**2*a3*a4*a6/3 - 16*a0**2*a3*a4/9 - 64*a0**2*a3*a5**2/9 - 16*a0**2*a3*a5*a6 + 8*a0**2*a3*a5 + 72*a0**2*a3*a6**2 - 12*a0**2*a3*a6 + 64*a0**2*a4**3/81 + 32*a0**2*a4**2*a5/27 + 32*a0**2*a4**2*a6/3 - 32*a0**2*a4**2/9 - 16*a0**2*a4*a5**2/9 - 8*a0**2*a4*a5*a6 - 72*a0*a1**2*a3*a5 + 24*a0*a1**2*a4**2 - 64*a0*a1*a2*a3**2/3 - 64*a0*a1*a2*a3*a4/3 + 16*a0*a1*a2*a3*a5 - 216*a0*a1*a2*a3*a6 - 12*a0*a1*a2*a3 - 16*a0*a1*a2*a4**2 + 8*a0*a1*a2*a4*a5 - 32*a0*a1*a3*a4*a6/3 + 112*a0*a1*a3*a4/27 - 128*a0*a1*a3*a5**2/27 - 160*a0*a1*a3*a5*a6/3 + 112*a0*a1*a3*a5/9 - 96*a0*a1*a3*a6**2 + 64*a0*a1*a3*a6 - 32*a0*a1*a3/3 + 160*a0*a1*a4**2*a5/81 + 64*a0*a1*a4**2*a6/9 + 32*a0*a1*a4*a5**2/27 + 16*a0*a1*a4*a5*a6/3 - 8*a0*a1*a4*a5/9 - 96*a0*a1*a4*a6**2 + 60*a0*a1*a4*a6 - 12*a0*a1*a4 - 16*a0*a1*a5**3/9 + 16*a0*a1*a5**2*a6 - 12*a0*a1*a5**2 + 144*a0*a2**3*a3 - 32*a0*a2**2*a3*a4/3 - 64*a0*a2**2*a3*a5/3 + 48*a0*a2**2*a3*a6 + 8*a0*a2**2*a3 - 32*a0*a2**2*a4**2/9 - 64*a0*a2**2*a4*a5/3 + 120*a0*a2**2*a4*a6 - 112*a0*a2**2*a4 - 16*a0*a2**2*a5**2 - 32*a0*a2*a3*a5*a6/3 - 848*a0*a2*a3*a5/27 - 96*a0*a2*a3*a6**2 + 32*a0*a2*a3*a6 - 8*a0*a2*a3/3 - 64*a0*a2*a4**2*a6/9 + 928*a0*a2*a4**2/81 + 160*a0*a2*a4*a5**2/81 - 32*a0*a2*a4*a5*a6/3 - 16*a0*a2*a4*a5/27 - 48*a0*a2*a4*a6**2 + 224*a0*a2*a4*a6/3 - 80*a0*a2*a4/9 + 64*a0*a2*a5**3/27 - 16*a0*a2*a5**2*a6/3 - 56*a0*a2*a5**2/3 + 48*a0*a2*a5*a6**2 - 200*a0*a2*a5*a6 + 48*a0*a2*a5 + 32*a0*a3*a6**3/3 - 976*a0*a3*a6**2/9 + 464*a0*a3*a6/9 - 152*a0*a3/27 - 160*a0*a4*a5*a6**2/27 + 512*a0*a4*a5*a6/27 - 112*a0*a4*a5/27 - 64*a0*a4*a6**3/3 - 256*a0*a4*a6**2/9 + 32*a0*a4*a6/3 + 32*a0*a5**3*a6/27 - 208*a0*a5**3/81 + 32*a0*a5**2*a6**2/9 + 64*a0*a5**2*a6/9 + 8*a0*a5**2/9 - 16*a0*a5*a6**3 - 8*a0*a5*a6**2 + 16*a0*a5*a6 - 8*a0*a5/3 + 72*a0*a6**4 - 372*a0*a6**3 + 276*a0*a6**2 - 72*a0*a6 + 6*a0 + 32*a1**3*a3**2/3 + 32*a1**3*a3*a4/3 + 16*a1**3*a3*a5 - 144*a1**3*a3*a6 + 72*a1**3*a3 + 24*a1**3*a4*a5 + 72*a1**2*a2**2*a3 + 32*a1**2*a2*a3*a4/3 + 64*a1**2*a2*a3*a5/3 + 240*a1**2*a2*a3*a6 - 80*a1**2*a2*a3 + 32*a1**2*a2*a4**2/9 - 32*a1**2*a2*a4*a5/3 - 24*a1**2*a2*a4*a6 + 60*a1**2*a2*a4 + 48*a1**2*a2*a5**2 - 160*a1**2*a3*a5*a6/9 + 352*a1**2*a3*a5/9 - 96*a1**2*a3*a6**2 + 48*a1**2*a3*a6 - 16*a1**2*a3/3 + 64*a1**2*a4**2*a6/27 - 256*a1**2*a4**2/27 + 32*a1**2*a4*a5**2/27 + 32*a1**2*a4*a5*a6/3 + 16*a1**2*a4*a5/3 + 32*a1**2*a4*a6**2 - 176*a1**2*a4*a6/3 + 8*a1**2*a4 - 32*a1**2*a5**2*a6/3 + 80*a1**2*a5**2/3 + 24*a1**2*a5*a6**2 + 60*a1**2*a5*a6 - 36*a1**2*a5 - 144*a1*a2**3*a3 + 24*a1*a2**3*a4 + 128*a1*a2**2*a3*a5/9 + 96*a1*a2**2*a3*a6 - 16*a1*a2**2*a3 + 64*a1*a2**2*a4**2/27 + 32*a1*a2**2*a4*a5/3 + 32*a1*a2**2*a4*a6 - 8*a1*a2**2*a4/3 - 80*a1*a2**2*a5**2/3 + 168*a1*a2**2*a5*a6 - 64*a1*a2*a3*a6**2/3 + 1888*a1*a2*a3*a6/9 - 152*a1*a2*a3/3 - 400*a1*a2*a4*a5/27 - 64*a1*a2*a4*a6**2/3 + 880*a1*a2*a4*a6/9 - 160*a1*a2*a4/9 + 64*a1*a2*a5**3/27 + 64*a1*a2*a5**2*a6/3 - 32*a1*a2*a5**2/3 - 80*a1*a2*a5*a6**2 + 488*a1*a2*a5*a6/3 - 100*a1*a2*a5/3 + 216*a1*a2*a6**3 + 144*a1*a2*a6**2 - 270*a1*a2*a6 + 54*a1*a2 - 64*a1*a4*a6**3/9 + 1408*a1*a4*a6**2/27 - 416*a1*a4*a6/27 + 32*a1*a4/27 + 32*a1*a5**2*a6**2/9 - 400*a1*a5**2*a6/27 + 32*a1*a5**2/27 + 32*a1*a5*a6**3/3 + 160*a1*a5*a6**2/9 + 8*a1*a5*a6/9 - 96*a1*a6**4 + 256*a1*a6**3 - 272*a1*a6**2/3 + 28*a1*a6/3 - 48*a2**4*a4 - 48*a2**4*a5 + 32*a2**3*a3*a6/3 - 304*a2**3*a3/3 + 160*a2**3*a4*a5/27 + 128*a2**3*a4*a6/3 - 160*a2**3*a4/3 + 64*a2**3*a5**2/9 - 48*a2**3*a5*a6 - 152*a2**3*a5/3 - 72*a2**3*a6**2 - 60*a2**3*a6 + 108*a2**3 + 64*a2**2*a4*a6**2/9 - 1312*a2**2*a4*a6/27 + 32*a2**2*a4/9 + 64*a2**2*a5**2*a6/9 - 224*a2**2*a5**2/27 + 256*a2**2*a5*a6**2/3 - 640*a2**2*a5*a6/9 + 80*a2**2*a5/9 - 48*a2**2*a6**3 - 64*a2**2*a6**2 + 8*a2**2*a6/3 + 32*a2*a5*a6**3/3 - 64*a2*a5*a6**2 + 496*a2*a5*a6/27 - 16*a2*a5/27 + 96*a2*a6**4 - 112*a2*a6**3 + 160*a2*a6**2/3 - 80*a2*a6/9 - 160*a6**4/3 + 112*a6**3/3 - 224*a6**2/27 + 16*a6/27",
          "-24*a0**2*a1*a3*a5 + 8*a0**2*a1*a4**2 - 32*a0**2*a2*a3*a5 - 144*a0**2*a2*a3*a6 + 24*a0**2*a2*a3 + 32*a0**2*a2*a4**2/3 + 16*a0**2*a2*a4*a5 - 64*a0**2*a3**2*a6/9 + 32*a0**2*a3**2/27 + 64*a0**2*a3*a4*a5/27 - 64*a0**2*a3*a4*a6/9 + 32*a0**2*a3*a4/27 + 128*a0**2*a3*a5**2/27 + 32*a0**2*a3*a5*a6/3 - 16*a0**2*a3*a5/3 - 48*a0**2*a3*a6**2 + 8*a0**2*a3*a6 - 128*a0**2*a4**3/243 - 64*a0**2*a4**2*a5/81 - 64*a0**2*a4**2*a6/9 + 64*a0**2*a4**2/27 + 32*a0**2*a4*a5**2/27 + 16*a0**2*a4*a5*a6/3 - 72*a0**2*a4*a6**2 + 24*a0**2*a4*a6 - 8*a0**2*a4 + 24*a0**2*a5**2*a6 - 4*a0**2*a5**2 + 48*a0*a1**2*a3*a5 - 72*a0*a1**2*a3*a6 + 24*a0*a1**2*a3 - 16*a0*a1**2*a4**2 + 8*a0*a1**2*a4*a5 + 216*a0*a1*a2**2*a3 + 128*a0*a1*a2*a3**2/9 + 128*a0*a1*a2*a3*a4/9 - 32*a0*a1*a2*a3*a5/3 + 144*a0*a1*a2*a3*a6 + 8*a0*a1*a2*a3 + 32*a0*a1*a2*a4**2/3 - 16*a0*a1*a2*a4*a5/3 + 120*a0*a1*a2*a4*a6 - 64*a0*a1*a2*a4 + 24*a0*a1*a2*a5**2 + 64*a0*a1*a3*a4*a6/9 - 224*a0*a1*a3*a4/81 + 256*a0*a1*a3*a5**2/81 + 320*a0*a1*a3*a5*a6/9 - 224*a0*a1*a3*a5/27 + 64*a0*a1*a3*a6**2 - 128*a0*a1*a3*a6/3 + 64*a0*a1*a3/9 - 320*a0*a1*a4**2*a5/243 - 128*a0*a1*a4**2*a6/27 - 64*a0*a1*a4*a5**2/81 - 32*a0*a1*a4*a5*a6/9 + 16*a0*a1*a4*a5/27 + 64*a0*a1*a4*a6**2 - 40*a0*a1*a4*a6 + 8*a0*a1*a4 + 32*a0*a1*a5**3/27 - 32*a0*a1*a5**2*a6/3 + 8*a0*a1*a5**2 + 120*a0*a1*a5*a6**2 - 108*a0*a1*a5*a6 - 8*a0*a1*a5 - 96*a0*a2**3*a3 + 48*a0*a2**3*a4 + 64*a0*a2**2*a3*a4/9 + 128*a0*a2**2*a3*a5/9 - 32*a0*a2**2*a3*a6 - 16*a0*a2**2*a3/3 + 64*a0*a2**2*a4**2/27 + 128*a0*a2**2*a4*a5/9 - 80*a0*a2**2*a4*a6 + 224*a0*a2**2*a4/3 + 32*a0*a2**2*a5**2/3 + 144*a0*a2**2*a5*a6 - 104*a0*a2**2*a5 + 64*a0*a2*a3*a5*a6/9 + 1696*a0*a2*a3*a5/81 + 64*a0*a2*a3*a6**2 - 64*a0*a2*a3*a6/3 + 16*a0*a2*a3/9 + 128*a0*a2*a4**2*a6/27 - 1856*a0*a2*a4**2/243 - 320*a0*a2*a4*a5**2/243 + 64*a0*a2*a4*a5*a6/9 + 32*a0*a2*a4*a5/81 + 32*a0*a2*a4*a6**2 - 448*a0*a2*a4*a6/9 + 160*a0*a2*a4/27 - 128*a0*a2*a5**3/81 + 32*a0*a2*a5**2*a6/9 + 112*a0*a2*a5**2/9 - 32*a0*a2*a5*a6**2 + 400*a0*a2*a5*a6/3 - 32*a0*a2*a5 + 288*a0*a2*a6**3 - 444*a0*a2*a6**2 + 132*a0*a2*a6 - 8*a0*a2 - 64*a0*a3*a6**3/9 + 1952*a0*a3*a6**2/27 - 928*a0*a3*a6/27 + 304*a0*a3/81 + 320*a0*a4*a5*a6**2/81 - 1024*a0*a4*a5*a6/81 + 224*a0*a4*a5/81 + 128*a0*a4*a6**3/9 + 512*a0*a4*a6**2/27 - 64*a0*a4*a6/9 - 64*a0*a5**3*a6/81 + 416*a0*a5**3/243 - 64*a0*a5**2*a6**2/27 - 128*a0*a5**2*a6/27 - 16*a0*a5**2/27 + 32*a0*a5*a6**3/3 + 16*a0*a5*a6**2/3 - 32*a0*a5*a6/3 + 16*a0*a5/9 - 48*a0*a6**4 + 248*a0*a6**3 - 184*a0*a6**2 + 48*a0*a6 - 4*a0 - 72*a1**3*a2*a3 - 64*a1**3*a3**2/9 - 64*a1**3*a3*a4/9 - 32*a1**3*a3*a5/3 + 96*a1**3*a3*a6 - 48*a1**3*a3 - 16*a1**3*a4*a5 - 48*a1**3*a4*a6 + 48*a1**3*a4 - 48*a1**2*a2**2*a3 - 24*a1**2*a2**2*a4 - 64*a1**2*a2*a3*a4/9 - 128*a1**2*a2*a3*a5/9 - 160*a1**2*a2*a3*a6 + 160*a1**2*a2*a3/3 - 64*a1**2*a2*a4**2/27 + 64*a1**2*a2*a4*a5/9 + 16*a1**2*a2*a4*a6 - 40*a1**2*a2*a4 - 32*a1**2*a2*a5**2 - 48*a1**2*a2*a5*a6 + 120*a1**2*a2*a5 + 320*a1**2*a3*a5*a6/27 - 704*a1**2*a3*a5/27 + 64*a1**2*a3*a6**2 - 32*a1**2*a3*a6 + 32*a1**2*a3/9 - 128*a1**2*a4**2*a6/81 + 512*a1**2*a4**2/81 - 64*a1**2*a4*a5**2/81 - 64*a1**2*a4*a5*a6/9 - 32*a1**2*a4*a5/9 - 64*a1**2*a4*a6**2/3 + 352*a1**2*a4*a6/9 - 16*a1**2*a4/3 + 64*a1**2*a5**2*a6/9 - 160*a1**2*a5**2/9 - 16*a1**2*a5*a6**2 - 40*a1**2*a5*a6 + 24*a1**2*a5 + 144*a1**2*a6**3 - 264*a1**2*a6**2 + 12*a1**2 + 96*a1*a2**3*a3 - 16*a1*a2**3*a4 - 24*a1*a2**3*a5 - 256*a1*a2**2*a3*a5/27 - 64*a1*a2**2*a3*a6 + 32*a1*a2**2*a3/3 - 128*a1*a2**2*a4**2/81 - 64*a1*a2**2*a4*a5/9 - 64*a1*a2**2*a4*a6/3 + 16*a1*a2**2*a4/9 + 160*a1*a2**2*a5**2/9 - 112*a1*a2**2*a5*a6 - 288*a1*a2**2*a6**2 + 744*a1*a2**2*a6 - 90*a1*a2**2 + 128*a1*a2*a3*a6**2/9 - 3776*a1*a2*a3*a6/27 + 304*a1*a2*a3/9 + 800*a1*a2*a4*a5/81 + 128*a1*a2*a4*a6**2/9 - 1760*a1*a2*a4*a6/27 + 320*a1*a2*a4/27 - 128*a1*a2*a5**3/81 - 128*a1*a2*a5**2*a6/9 + 64*a1*a2*a5**2/9 + 160*a1*a2*a5*a6**2/3 - 976*a1*a2*a5*a6/9 + 200*a1*a2*a5/9 - 144*a1*a2*a6**3 - 96*a1*a2*a6**2 + 180*a1*a2*a6 - 36*a1*a2 + 128*a1*a4*a6**3/27 - 2816*a1*a4*a6**2/81 + 832*a1*a4*a6/81 - 64*a1*a4/81 - 64*a1*a5**2*a6**2/27 + 800*a1*a5**2*a6/81 - 64*a1*a5**2/81 - 64*a1*a5*a6**3/9 - 320*a1*a5*a6**2/27 - 16*a1*a5*a6/27 + 64*a1*a6**4 - 512*a1*a6**3/3 + 544*a1*a6**2/9 - 56*a1*a6/9 + 32*a2**4*a4 + 32*a2**4*a5 + 72*a2**4*a6 - 252*a2**4 - 64*a2**3*a3*a6/9 + 608*a2**3*a3/9 - 320*a2**3*a4*a5/81 - 256*a2**3*a4*a6/9 + 320*a2**3*a4/9 - 128*a2**3*a5**2/27 + 32*a2**3*a5*a6 + 304*a2**3*a5/9 + 48*a2**3*a6**2 + 40*a2**3*a6 - 72*a2**3 - 128*a2**2*a4*a6**2/27 + 2624*a2**2*a4*a6/81 - 64*a2**2*a4/27 - 128*a2**2*a5**2*a6/27 + 448*a2**2*a5**2/81 - 512*a2**2*a5*a6**2/9 + 1280*a2**2*a5*a6/27 - 160*a2**2*a5/27 + 32*a2**2*a6**3 + 128*a2**2*a6**2/3 - 16*a2**2*a6/9 - 64*a2*a5*a6**3/9 + 128*a2*a5*a6**2/3 - 992*a2*a5*a6/81 + 32*a2*a5/81 - 64*a2*a6**4 + 224*a2*a6**3/3 - 320*a2*a6**2/9 + 160*a2*a6/27 + 320*a6**4/9 - 224*a6**3/9 + 448*a6**2/81 - 32*a6/81"
        &#93;,
        &#91;
          "24*a0*a2*a3**2 + 32*a0*a2*a3*a4*a5 + 24*a0*a2*a3*a4 + 96*a0*a2*a3*a5**2 - 32*a0*a2*a4**3/3 - 32*a0*a2*a4**2*a5 + 96*a0*a3*a4*a6**2 - 44*a0*a3*a4*a6 + 2*a0*a3*a4 + 32*a0*a3*a5**2/3 + 288*a0*a3*a5*a6**2 - 60*a0*a3*a5*a6 + 6*a0*a3*a5 - 64*a0*a4**2*a5*a6/3 + 20*a0*a4**2*a5/9 - 24*a0*a4**2*a6 + 32*a0*a4*a5**3/9 - 64*a0*a4*a5**2*a6 + 52*a0*a4*a5**2/3 + 32*a0*a5**4/3 - 24*a1**2*a3**2 - 32*a1**2*a3*a4*a5 - 24*a1**2*a3*a4 - 96*a1**2*a3*a5**2 + 32*a1**2*a4**3/3 + 32*a1**2*a4**2*a5 - 192*a1*a2*a3*a4*a6 + 44*a1*a2*a3*a4 - 576*a1*a2*a3*a5*a6 + 24*a1*a2*a3*a5 + 64*a1*a2*a4**2*a5/3 + 36*a1*a2*a4**2 + 64*a1*a2*a4*a5**2 + 76*a1*a3*a5*a6 - 42*a1*a3*a5 + 216*a1*a3*a6**2 - 108*a1*a3*a6 + 12*a1*a3 - 64*a1*a4**2*a6**2 + 56*a1*a4**2*a6/3 + 8*a1*a4**2/3 + 64*a1*a4*a5**2*a6/3 - 8*a1*a4*a5**2 - 192*a1*a4*a5*a6**2 + 84*a1*a4*a5*a6 - 22*a1*a4*a5 + 64*a1*a5**3*a6 - 16*a1*a5**3 + 96*a2**3*a3*a4 + 288*a2**3*a3*a5 - 324*a2**2*a3*a6 + 90*a2**2*a3 + 64*a2**2*a4**2*a6 - 16*a2**2*a4**2 + 32*a2**2*a4*a5**2/3 + 192*a2**2*a4*a5*a6 - 12*a2**2*a4*a5 + 32*a2**2*a5**3 + 132*a2*a3*a6**2 - 120*a2*a3*a6 + 15*a2*a3 + 96*a2*a4*a5*a6**2 - 152*a2*a4*a5*a6/3 + 6*a2*a4*a5 - 12*a2*a4*a6**2 - 18*a2*a4*a6 - 8*a2*a5**3/3 + 288*a2*a5**2*a6**2 - 128*a2*a5**2*a6 + 4*a2*a5**2 + 96*a4*a6**4 - 56*a4*a6**3 - 12*a4*a6**2 + 4*a4*a6 - 12*a5**2*a6**2 + 26*a5**2*a6/3 + 288*a5*a6**4 - 276*a5*a6**3 + 72*a5*a6**2 - 7*a5*a6",
          "108*a0*a2*a3**2 + 144*a0*a2*a3*a4*a5 - 48*a0*a2*a4**3 + 432*a0*a3*a4*a6**2 - 198*a0*a3*a4*a6 + 9*a0*a3*a4 + 48*a0*a3*a5**2 - 96*a0*a4**2*a5*a6 + 10*a0*a4**2*a5 + 16*a0*a4*a5**3 - 108*a1**2*a3**2 - 144*a1**2*a3*a4*a5 + 48*a1**2*a4**3 - 864*a1*a2*a3*a4*a6 + 198*a1*a2*a3*a4 + 96*a1*a2*a4**2*a5 + 342*a1*a3*a5*a6 - 189*a1*a3*a5 - 288*a1*a4**2*a6**2 + 84*a1*a4**2*a6 + 12*a1*a4**2 + 96*a1*a4*a5**2*a6 - 36*a1*a4*a5**2 + 432*a2**3*a3*a4 + 288*a2**2*a4**2*a6 - 72*a2**2*a4**2 + 48*a2**2*a4*a5**2 + 594*a2*a3*a6**2 - 540*a2*a3*a6 + 135*a2*a3/2 + 432*a2*a4*a5*a6**2 - 228*a2*a4*a5*a6 + 27*a2*a4*a5 - 12*a2*a5**3 + 432*a4*a6**4 - 252*a4*a6**3 - 54*a4*a6**2 + 18*a4*a6 - 54*a5**2*a6**2 + 39*a5**2*a6",
          "-16*a0*a2*a3**2 - 64*a0*a2*a3*a4*a5/3 - 16*a0*a2*a3*a4 - 64*a0*a2*a3*a5**2 - 288*a0*a2*a3*a5*a6 - 36*a0*a2*a3*a5 + 64*a0*a2*a4**3/9 + 64*a0*a2*a4**2*a5/3 + 96*a0*a2*a4**2*a6 + 4*a0*a2*a4**2 - 64*a0*a3*a4*a6**2 + 88*a0*a3*a4*a6/3 - 4*a0*a3*a4/3 - 64*a0*a3*a5**2/9 - 192*a0*a3*a5*a6**2 + 40*a0*a3*a5*a6 - 4*a0*a3*a5 - 864*a0*a3*a6**3 + 144*a0*a3*a6**2 + 84*a0*a3*a6 - 18*a0*a3 + 128*a0*a4**2*a5*a6/9 - 40*a0*a4**2*a5/27 + 16*a0*a4**2*a6 - 64*a0*a4*a5**3/27 + 128*a0*a4*a5**2*a6/3 - 104*a0*a4*a5**2/9 + 192*a0*a4*a5*a6**2 + 12*a0*a4*a5*a6 - 34*a0*a4*a5/3 - 64*a0*a5**4/9 - 32*a0*a5**3*a6 - 12*a0*a5**3 + 16*a1**2*a3**2 + 64*a1**2*a3*a4*a5/3 + 16*a1**2*a3*a4 + 64*a1**2*a3*a5**2 + 288*a1**2*a3*a5*a6 - 64*a1**2*a4**3/9 - 64*a1**2*a4**2*a5/3 - 96*a1**2*a4**2*a6 + 8*a1**2*a4**2 + 128*a1*a2*a3*a4*a6 - 88*a1*a2*a3*a4/3 + 384*a1*a2*a3*a5*a6 - 16*a1*a2*a3*a5 + 1728*a1*a2*a3*a6**2 - 120*a1*a2*a3 - 128*a1*a2*a4**2*a5/9 - 24*a1*a2*a4**2 - 128*a1*a2*a4*a5**2/3 - 192*a1*a2*a4*a5*a6 - 44*a1*a2*a4*a5 - 152*a1*a3*a5*a6/3 + 28*a1*a3*a5 - 144*a1*a3*a6**2 + 72*a1*a3*a6 - 8*a1*a3 + 128*a1*a4**2*a6**2/3 - 112*a1*a4**2*a6/9 - 16*a1*a4**2/9 - 128*a1*a4*a5**2*a6/9 + 16*a1*a4*a5**2/3 + 128*a1*a4*a5*a6**2 - 56*a1*a4*a5*a6 + 44*a1*a4*a5/3 + 576*a1*a4*a6**3 - 216*a1*a4*a6**2 + 8*a1*a4*a6 + 2*a1*a4 - 128*a1*a5**3*a6/3 + 32*a1*a5**3/3 - 192*a1*a5**2*a6**2 + 12*a1*a5**2*a6 + 18*a1*a5**2 - 64*a2**3*a3*a4 - 192*a2**3*a3*a5 - 864*a2**3*a3*a6 - 252*a2**3*a3 + 216*a2**2*a3*a6 - 60*a2**2*a3 - 128*a2**2*a4**2*a6/3 + 32*a2**2*a4**2/3 - 64*a2**2*a4*a5**2/9 - 128*a2**2*a4*a5*a6 + 8*a2**2*a4*a5 - 576*a2**2*a4*a6**2 + 48*a2**2*a4*a6 + 6*a2**2*a4 - 64*a2**2*a5**3/3 - 96*a2**2*a5**2*a6 - 52*a2**2*a5**2 - 88*a2*a3*a6**2 + 80*a2*a3*a6 - 10*a2*a3 - 64*a2*a4*a5*a6**2 + 304*a2*a4*a5*a6/9 - 4*a2*a4*a5 + 8*a2*a4*a6**2 + 12*a2*a4*a6 + 16*a2*a5**3/9 - 192*a2*a5**2*a6**2 + 256*a2*a5**2*a6/3 - 8*a2*a5**2/3 - 864*a2*a5*a6**3 + 144*a2*a5*a6**2 + 118*a2*a5*a6 - 15*a2*a5 - 64*a4*a6**4 + 112*a4*a6**3/3 + 8*a4*a6**2 - 8*a4*a6/3 + 8*a5**2*a6**2 - 52*a5**2*a6/9 - 192*a5*a6**4 + 184*a5*a6**3 - 48*a5*a6**2 + 14*a5*a6/3 - 864*a6**5 + 576*a6**4 + 12*a6**3 - 60*a6**2 + 9*a6",
          "-36*a0*a1*a3*a5 + 12*a0*a1*a4**2 - 288*a0*a2**2*a3*a5 + 96*a0*a2**2*a4**2 + 32*a0*a2*a3**2/3 + 128*a0*a2*a3*a4*a5/9 + 32*a0*a2*a3*a4/3 + 128*a0*a2*a3*a5**2/3 + 192*a0*a2*a3*a5*a6 + 24*a0*a2*a3*a5 - 864*a0*a2*a3*a6**2 + 144*a0*a2*a3*a6 + 36*a0*a2*a3 - 128*a0*a2*a4**3/27 - 128*a0*a2*a4**2*a5/9 - 64*a0*a2*a4**2*a6 - 8*a0*a2*a4**2/3 + 192*a0*a2*a4*a5*a6 - 8*a0*a2*a4*a5 - 32*a0*a2*a5**3 + 128*a0*a3*a4*a6**2/3 - 176*a0*a3*a4*a6/9 + 8*a0*a3*a4/9 + 128*a0*a3*a5**2/27 + 128*a0*a3*a5*a6**2 - 80*a0*a3*a5*a6/3 + 8*a0*a3*a5/3 + 576*a0*a3*a6**3 - 96*a0*a3*a6**2 - 56*a0*a3*a6 + 12*a0*a3 - 256*a0*a4**2*a5*a6/27 + 80*a0*a4**2*a5/81 - 32*a0*a4**2*a6/3 + 128*a0*a4*a5**3/81 - 256*a0*a4*a5**2*a6/9 + 208*a0*a4*a5**2/27 - 128*a0*a4*a5*a6**2 - 8*a0*a4*a5*a6 + 68*a0*a4*a5/9 - 108*a0*a4*a6**2 + 54*a0*a4*a6 - 6*a0*a4 + 128*a0*a5**4/27 + 64*a0*a5**3*a6/3 + 8*a0*a5**3 + 44*a0*a5**2*a6 - 12*a0*a5**2 + 288*a1**2*a2*a3*a5 - 96*a1**2*a2*a4**2 - 32*a1**2*a3**2/3 - 128*a1**2*a3*a4*a5/9 - 32*a1**2*a3*a4/3 - 128*a1**2*a3*a5**2/3 - 192*a1**2*a3*a5*a6 + 144*a1**2*a3*a6 - 72*a1**2*a3 + 128*a1**2*a4**3/27 + 128*a1**2*a4**2*a5/9 + 64*a1**2*a4**2*a6 - 16*a1**2*a4**2/3 - 24*a1**2*a4*a5 + 1728*a1*a2**2*a3*a6 - 396*a1*a2**2*a3 - 192*a1*a2**2*a4*a5 - 256*a1*a2*a3*a4*a6/3 + 176*a1*a2*a3*a4/9 - 256*a1*a2*a3*a5*a6 + 32*a1*a2*a3*a5/3 - 1152*a1*a2*a3*a6**2 + 80*a1*a2*a3 + 256*a1*a2*a4**2*a5/27 + 16*a1*a2*a4**2 + 256*a1*a2*a4*a5**2/9 + 128*a1*a2*a4*a5*a6 + 88*a1*a2*a4*a5/3 + 576*a1*a2*a4*a6**2 - 204*a1*a2*a4*a6 - 6*a1*a2*a4 - 192*a1*a2*a5**2*a6 + 24*a1*a2*a5**2 + 304*a1*a3*a5*a6/9 - 56*a1*a3*a5/3 + 96*a1*a3*a6**2 - 48*a1*a3*a6 + 16*a1*a3/3 - 256*a1*a4**2*a6**2/9 + 224*a1*a4**2*a6/27 + 32*a1*a4**2/27 + 256*a1*a4*a5**2*a6/27 - 32*a1*a4*a5**2/9 - 256*a1*a4*a5*a6**2/3 + 112*a1*a4*a5*a6/3 - 88*a1*a4*a5/9 - 384*a1*a4*a6**3 + 144*a1*a4*a6**2 - 16*a1*a4*a6/3 - 4*a1*a4/3 + 256*a1*a5**3*a6/9 - 64*a1*a5**3/9 + 128*a1*a5**2*a6**2 - 8*a1*a5**2*a6 - 12*a1*a5**2 + 48*a1*a5*a6**2 - 60*a1*a5*a6 + 18*a1*a5 - 864*a2**4*a3 + 128*a2**3*a3*a4/3 + 128*a2**3*a3*a5 + 576*a2**3*a3*a6 + 168*a2**3*a3 - 576*a2**3*a4*a6 + 144*a2**3*a4 - 96*a2**3*a5**2 - 144*a2**2*a3*a6 + 40*a2**2*a3 + 256*a2**2*a4**2*a6/9 - 64*a2**2*a4**2/9 + 128*a2**2*a4*a5**2/27 + 256*a2**2*a4*a5*a6/3 - 16*a2**2*a4*a5/3 + 384*a2**2*a4*a6**2 - 32*a2**2*a4*a6 - 4*a2**2*a4 + 128*a2**2*a5**3/9 + 64*a2**2*a5**2*a6 + 104*a2**2*a5**2/3 - 864*a2**2*a5*a6**2 + 420*a2**2*a5*a6 - 36*a2**2*a5 + 176*a2*a3*a6**2/3 - 160*a2*a3*a6/3 + 20*a2*a3/3 + 128*a2*a4*a5*a6**2/3 - 608*a2*a4*a5*a6/27 + 8*a2*a4*a5/3 - 16*a2*a4*a6**2/3 - 8*a2*a4*a6 - 32*a2*a5**3/27 + 128*a2*a5**2*a6**2 - 512*a2*a5**2*a6/9 + 16*a2*a5**2/9 + 576*a2*a5*a6**3 - 96*a2*a5*a6**2 - 236*a2*a5*a6/3 + 10*a2*a5 - 864*a2*a6**4 + 900*a2*a6**3 - 360*a2*a6**2 + 81*a2*a6 - 9*a2 + 128*a4*a6**4/3 - 224*a4*a6**3/9 - 16*a4*a6**2/3 + 16*a4*a6/9 - 16*a5**2*a6**2/3 + 104*a5**2*a6/27 + 128*a5*a6**4 - 368*a5*a6**3/3 + 32*a5*a6**2 - 28*a5*a6/9 + 576*a6**5 - 384*a6**4 - 8*a6**3 + 40*a6**2 - 6*a6",
          "-36*a0**2*a3*a5 + 12*a0**2*a4**2 - 288*a0*a1*a2*a3*a5 + 96*a0*a1*a2*a4**2 + 24*a0*a1*a3*a5 - 864*a0*a1*a3*a6**2 + 288*a0*a1*a3*a6 - 36*a0*a1*a3 - 8*a0*a1*a4**2 + 192*a0*a1*a4*a5*a6 - 32*a0*a1*a4*a5 - 32*a0*a1*a5**3 + 192*a0*a2**2*a3*a5 - 252*a0*a2**2*a3 - 64*a0*a2**2*a4**2 - 64*a0*a2*a3**2/9 - 256*a0*a2*a3*a4*a5/27 - 64*a0*a2*a3*a4/9 - 256*a0*a2*a3*a5**2/9 - 128*a0*a2*a3*a5*a6 - 16*a0*a2*a3*a5 + 576*a0*a2*a3*a6**2 - 96*a0*a2*a3*a6 - 24*a0*a2*a3 + 256*a0*a2*a4**3/81 + 256*a0*a2*a4**2*a5/27 + 128*a0*a2*a4**2*a6/3 + 16*a0*a2*a4**2/9 - 128*a0*a2*a4*a5*a6 + 16*a0*a2*a4*a5/3 - 252*a0*a2*a4*a6 + 12*a0*a2*a4 + 64*a0*a2*a5**3/3 + 20*a0*a2*a5**2 - 256*a0*a3*a4*a6**2/9 + 352*a0*a3*a4*a6/27 - 16*a0*a3*a4/27 - 256*a0*a3*a5**2/81 - 256*a0*a3*a5*a6**2/3 + 160*a0*a3*a5*a6/9 - 16*a0*a3*a5/9 - 384*a0*a3*a6**3 + 64*a0*a3*a6**2 + 112*a0*a3*a6/3 - 8*a0*a3 + 512*a0*a4**2*a5*a6/81 - 160*a0*a4**2*a5/243 + 64*a0*a4**2*a6/9 - 256*a0*a4*a5**3/243 + 512*a0*a4*a5**2*a6/27 - 416*a0*a4*a5**2/81 + 256*a0*a4*a5*a6**2/3 + 16*a0*a4*a5*a6/3 - 136*a0*a4*a5/27 + 72*a0*a4*a6**2 - 36*a0*a4*a6 + 4*a0*a4 - 256*a0*a5**4/81 - 128*a0*a5**3*a6/9 - 16*a0*a5**3/3 - 88*a0*a5**2*a6/3 + 8*a0*a5**2 - 108*a0*a5*a6**2 + 18*a0*a5*a6 + 8*a0*a5 + 288*a1**3*a3*a5 - 96*a1**3*a4**2 - 192*a1**2*a2*a3*a5 + 1728*a1**2*a2*a3*a6 - 144*a1**2*a2*a3 + 64*a1**2*a2*a4**2 - 192*a1**2*a2*a4*a5 + 64*a1**2*a3**2/9 + 256*a1**2*a3*a4*a5/27 + 64*a1**2*a3*a4/9 + 256*a1**2*a3*a5**2/9 + 128*a1**2*a3*a5*a6 - 96*a1**2*a3*a6 + 48*a1**2*a3 - 256*a1**2*a4**3/81 - 256*a1**2*a4**2*a5/27 - 128*a1**2*a4**2*a6/3 + 32*a1**2*a4**2/9 + 16*a1**2*a4*a5 + 576*a1**2*a4*a6**2 - 168*a1**2*a4*a6 + 36*a1**2*a4 - 192*a1**2*a5**2*a6 + 48*a1**2*a5**2 - 864*a1*a2**3*a3 - 1152*a1*a2**2*a3*a6 + 264*a1*a2**2*a3 + 128*a1*a2**2*a4*a5 - 576*a1*a2**2*a4*a6 + 252*a1*a2**2*a4 - 96*a1*a2**2*a5**2 + 512*a1*a2*a3*a4*a6/9 - 352*a1*a2*a3*a4/27 + 512*a1*a2*a3*a5*a6/3 - 64*a1*a2*a3*a5/9 + 768*a1*a2*a3*a6**2 - 160*a1*a2*a3/3 - 512*a1*a2*a4**2*a5/81 - 32*a1*a2*a4**2/3 - 512*a1*a2*a4*a5**2/27 - 256*a1*a2*a4*a5*a6/3 - 176*a1*a2*a4*a5/9 - 384*a1*a2*a4*a6**2 + 136*a1*a2*a4*a6 + 4*a1*a2*a4 + 128*a1*a2*a5**2*a6 - 16*a1*a2*a5**2 - 864*a1*a2*a5*a6**2 + 468*a1*a2*a5*a6 - 42*a1*a2*a5 - 608*a1*a3*a5*a6/27 + 112*a1*a3*a5/9 - 64*a1*a3*a6**2 + 32*a1*a3*a6 - 32*a1*a3/9 + 512*a1*a4**2*a6**2/27 - 448*a1*a4**2*a6/81 - 64*a1*a4**2/81 - 512*a1*a4*a5**2*a6/81 + 64*a1*a4*a5**2/27 + 512*a1*a4*a5*a6**2/9 - 224*a1*a4*a5*a6/9 + 176*a1*a4*a5/27 + 256*a1*a4*a6**3 - 96*a1*a4*a6**2 + 32*a1*a4*a6/9 + 8*a1*a4/9 - 512*a1*a5**3*a6/27 + 128*a1*a5**3/27 - 256*a1*a5**2*a6**2/3 + 16*a1*a5**2*a6/3 + 8*a1*a5**2 - 32*a1*a5*a6**2 + 40*a1*a5*a6 - 12*a1*a5 - 864*a1*a6**4 + 504*a1*a6**3 - 72*a1*a6**2 + 42*a1*a6 - 12*a1 + 576*a2**4*a3 - 256*a2**3*a3*a4/9 - 256*a2**3*a3*a5/3 - 384*a2**3*a3*a6 - 112*a2**3*a3 + 384*a2**3*a4*a6 - 96*a2**3*a4 + 64*a2**3*a5**2 + 108*a2**3*a5 + 96*a2**2*a3*a6 - 80*a2**2*a3/3 - 512*a2**2*a4**2*a6/27 + 128*a2**2*a4**2/27 - 256*a2**2*a4*a5**2/81 - 512*a2**2*a4*a5*a6/9 + 32*a2**2*a4*a5/9 - 256*a2**2*a4*a6**2 + 64*a2**2*a4*a6/3 + 8*a2**2*a4/3 - 256*a2**2*a5**3/27 - 128*a2**2*a5**2*a6/3 - 208*a2**2*a5**2/9 + 576*a2**2*a5*a6**2 - 280*a2**2*a5*a6 + 24*a2**2*a5 + 396*a2**2*a6**2 - 180*a2**2*a6 - 9*a2**2 - 352*a2*a3*a6**2/9 + 320*a2*a3*a6/9 - 40*a2*a3/9 - 256*a2*a4*a5*a6**2/9 + 1216*a2*a4*a5*a6/81 - 16*a2*a4*a5/9 + 32*a2*a4*a6**2/9 + 16*a2*a4*a6/3 + 64*a2*a5**3/81 - 256*a2*a5**2*a6**2/3 + 1024*a2*a5**2*a6/27 - 32*a2*a5**2/27 - 384*a2*a5*a6**3 + 64*a2*a5*a6**2 + 472*a2*a5*a6/9 - 20*a2*a5/3 + 576*a2*a6**4 - 600*a2*a6**3 + 240*a2*a6**2 - 54*a2*a6 + 6*a2 - 256*a4*a6**4/9 + 448*a4*a6**3/27 + 32*a4*a6**2/9 - 32*a4*a6/27 + 32*a5**2*a6**2/9 - 208*a5**2*a6/81 - 256*a5*a6**4/3 + 736*a5*a6**3/9 - 64*a5*a6**2/3 + 56*a5*a6/27 - 384*a6**5 + 256*a6**4 + 16*a6**3/3 - 80*a6**2/3 + 4*a6"
        &#93;,
        &#91;
          "24*a0*a2*a3**2*a5 - 8*a0*a2*a3*a4**2 + 24*a0*a2*a3*a4*a5 - 8*a0*a2*a4**3 + 72*a0*a3**2*a6**2 - 48*a0*a3**2*a6 + 6*a0*a3**2 - 16*a0*a3*a4*a5*a6 + 8*a0*a3*a4*a5 + 72*a0*a3*a4*a6**2 - 48*a0*a3*a4*a6 + 6*a0*a3*a4 + 8*a0*a3*a5**3/3 + 8*a0*a3*a5**2 - 8*a0*a4**3/9 - 16*a0*a4**2*a5*a6 + 8*a0*a4**2*a5/3 + 8*a0*a4*a5**3/3 - 24*a1**2*a3**2*a5 + 8*a1**2*a3*a4**2 - 24*a1**2*a3*a4*a5 + 8*a1**2*a4**3 - 144*a1*a2*a3**2*a6 + 48*a1*a2*a3**2 + 16*a1*a2*a3*a4*a5 - 144*a1*a2*a3*a4*a6 + 48*a1*a2*a3*a4 + 16*a1*a2*a4**2*a5 - 48*a1*a3*a4*a6**2 + 28*a1*a3*a4*a6 - 6*a1*a3*a4 + 16*a1*a3*a5**2*a6 + 36*a1*a3*a5*a6 - 6*a1*a3*a5 - 4*a1*a4**2*a5/3 - 48*a1*a4**2*a6**2 + 16*a1*a4**2*a6 - 4*a1*a4**2 + 16*a1*a4*a5**2*a6 - 4*a1*a4*a5**2 + 72*a2**3*a3**2 + 72*a2**3*a3*a4 + 48*a2**2*a3*a4*a6 - 4*a2**2*a3*a4 + 8*a2**2*a3*a5**2 + 24*a2**2*a3*a5 + 48*a2**2*a4**2*a6 - 12*a2**2*a4**2 + 8*a2**2*a4*a5**2 + 72*a2*a3*a5*a6**2 - 28*a2*a3*a5*a6 + 108*a2*a3*a6**2 - 36*a2*a3*a6 + 3*a2*a3 + 16*a2*a4**2*a6/3 - 4*a2*a4**2/3 - 4*a2*a4*a5**2/3 + 72*a2*a4*a5*a6**2 - 36*a2*a4*a5*a6 + 72*a3*a6**4 - 84*a3*a6**3 + 30*a3*a6**2 - 3*a3*a6 + 20*a4*a5*a6**2/3 - 2*a4*a5*a6 + 72*a4*a6**4 - 48*a4*a6**3 + 18*a4*a6**2 - 2*a4*a6 - 4*a5**3*a6/3 - 4*a5**2*a6**2 - 2*a5**2*a6",
          "108*a0*a2*a3**2*a5 - 36*a0*a2*a3*a4**2 + 324*a0*a3**2*a6**2 - 216*a0*a3**2*a6 + 27*a0*a3**2 - 72*a0*a3*a4*a5*a6 + 36*a0*a3*a4*a5 + 12*a0*a3*a5**3 - 4*a0*a4**3 - 108*a1**2*a3**2*a5 + 36*a1**2*a3*a4**2 - 648*a1*a2*a3**2*a6 + 216*a1*a2*a3**2 + 72*a1*a2*a3*a4*a5 - 216*a1*a3*a4*a6**2 + 126*a1*a3*a4*a6 - 27*a1*a3*a4 + 72*a1*a3*a5**2*a6 - 6*a1*a4**2*a5 + 324*a2**3*a3**2 + 216*a2**2*a3*a4*a6 - 18*a2**2*a3*a4 + 36*a2**2*a3*a5**2 + 324*a2*a3*a5*a6**2 - 126*a2*a3*a5*a6 + 24*a2*a4**2*a6 - 6*a2*a4**2 - 6*a2*a4*a5**2 + 324*a3*a6**4 - 378*a3*a6**3 + 135*a3*a6**2 - 27*a3*a6/2 + 30*a4*a5*a6**2 - 9*a4*a5*a6 - 6*a5**3*a6",
          "-16*a0*a2*a3**2*a5 + 16*a0*a2*a3*a4**2/3 - 16*a0*a2*a3*a4*a5 - 24*a0*a2*a3*a5**2 + 16*a0*a2*a4**3/3 + 8*a0*a2*a4**2*a5 - 48*a0*a3**2*a6**2 + 32*a0*a3**2*a6 - 4*a0*a3**2 + 32*a0*a3*a4*a5*a6/3 - 16*a0*a3*a4*a5/3 - 48*a0*a3*a4*a6**2 + 32*a0*a3*a4*a6 - 4*a0*a3*a4 - 16*a0*a3*a5**3/9 - 16*a0*a3*a5**2/3 - 72*a0*a3*a5*a6**2 + 24*a0*a3*a5*a6 + 2*a0*a3*a5 + 16*a0*a4**3/27 + 32*a0*a4**2*a5*a6/3 - 16*a0*a4**2*a5/9 + 8*a0*a4**2*a6 - 8*a0*a4**2/3 - 16*a0*a4*a5**3/9 + 16*a0*a4*a5**2*a6 - 16*a0*a4*a5**2/3 - 8*a0*a5**4/3 + 16*a1**2*a3**2*a5 - 16*a1**2*a3*a4**2/3 + 16*a1**2*a3*a4*a5 + 24*a1**2*a3*a5**2 - 16*a1**2*a4**3/3 - 8*a1**2*a4**2*a5 + 96*a1*a2*a3**2*a6 - 32*a1*a2*a3**2 - 32*a1*a2*a3*a4*a5/3 + 96*a1*a2*a3*a4*a6 - 32*a1*a2*a3*a4 + 144*a1*a2*a3*a5*a6 - 12*a1*a2*a3*a5 - 32*a1*a2*a4**2*a5/3 - 12*a1*a2*a4**2 - 16*a1*a2*a4*a5**2 + 32*a1*a3*a4*a6**2 - 56*a1*a3*a4*a6/3 + 4*a1*a3*a4 - 32*a1*a3*a5**2*a6/3 - 24*a1*a3*a5*a6 + 4*a1*a3*a5 + 8*a1*a4**2*a5/9 + 32*a1*a4**2*a6**2 - 32*a1*a4**2*a6/3 + 8*a1*a4**2/3 - 32*a1*a4*a5**2*a6/3 + 8*a1*a4*a5**2/3 + 48*a1*a4*a5*a6**2 - 28*a1*a4*a5*a6 + 6*a1*a4*a5 - 16*a1*a5**3*a6 + 4*a1*a5**3 - 48*a2**3*a3**2 - 48*a2**3*a3*a4 - 72*a2**3*a3*a5 - 32*a2**2*a3*a4*a6 + 8*a2**2*a3*a4/3 - 16*a2**2*a3*a5**2/3 - 16*a2**2*a3*a5 + 36*a2**2*a3*a6 + 6*a2**2*a3 - 32*a2**2*a4**2*a6 + 8*a2**2*a4**2 - 16*a2**2*a4*a5**2/3 - 48*a2**2*a4*a5*a6 - 8*a2**2*a5**3 - 48*a2*a3*a5*a6**2 + 56*a2*a3*a5*a6/3 - 72*a2*a3*a6**2 + 24*a2*a3*a6 - 2*a2*a3 - 32*a2*a4**2*a6/9 + 8*a2*a4**2/9 + 8*a2*a4*a5**2/9 - 48*a2*a4*a5*a6**2 + 24*a2*a4*a5*a6 - 12*a2*a4*a6**2 + 22*a2*a4*a6 - 4*a2*a4 - 72*a2*a5**2*a6**2 + 28*a2*a5**2*a6 - 2*a2*a5**2 - 48*a3*a6**4 + 56*a3*a6**3 - 20*a3*a6**2 + 2*a3*a6 - 40*a4*a5*a6**2/9 + 4*a4*a5*a6/3 - 48*a4*a6**4 + 32*a4*a6**3 - 12*a4*a6**2 + 4*a4*a6/3 + 8*a5**3*a6/9 + 8*a5**2*a6**2/3 + 4*a5**2*a6/3 - 72*a5*a6**4 + 60*a5*a6**3 - 10*a5*a6**2 - a5*a6",
          "32*a0*a2*a3**2*a5/3 - 32*a0*a2*a3*a4**2/9 + 32*a0*a2*a3*a4*a5/3 + 16*a0*a2*a3*a5**2 + 72*a0*a2*a3*a5*a6 - 60*a0*a2*a3*a5 - 32*a0*a2*a4**3/9 - 16*a0*a2*a4**2*a5/3 - 24*a0*a2*a4**2*a6 + 20*a0*a2*a4**2 + 32*a0*a3**2*a6**2 - 64*a0*a3**2*a6/3 + 8*a0*a3**2/3 - 64*a0*a3*a4*a5*a6/9 + 32*a0*a3*a4*a5/9 + 32*a0*a3*a4*a6**2 - 64*a0*a3*a4*a6/3 + 8*a0*a3*a4/3 + 32*a0*a3*a5**3/27 + 32*a0*a3*a5**2/9 + 48*a0*a3*a5*a6**2 - 16*a0*a3*a5*a6 - 4*a0*a3*a5/3 + 216*a0*a3*a6**3 - 252*a0*a3*a6**2 + 72*a0*a3*a6 - 6*a0*a3 - 32*a0*a4**3/81 - 64*a0*a4**2*a5*a6/9 + 32*a0*a4**2*a5/27 - 16*a0*a4**2*a6/3 + 16*a0*a4**2/9 + 32*a0*a4*a5**3/27 - 32*a0*a4*a5**2*a6/3 + 32*a0*a4*a5**2/9 - 48*a0*a4*a5*a6**2 + 40*a0*a4*a5*a6 - 6*a0*a4*a5 + 16*a0*a5**4/9 + 8*a0*a5**3*a6 - 4*a0*a5**3 - 32*a1**2*a3**2*a5/3 + 32*a1**2*a3*a4**2/9 - 32*a1**2*a3*a4*a5/3 - 16*a1**2*a3*a5**2 - 72*a1**2*a3*a5*a6 + 72*a1**2*a3*a5 + 32*a1**2*a4**3/9 + 16*a1**2*a4**2*a5/3 + 24*a1**2*a4**2*a6 - 24*a1**2*a4**2 - 64*a1*a2*a3**2*a6 + 64*a1*a2*a3**2/3 + 64*a1*a2*a3*a4*a5/9 - 64*a1*a2*a3*a4*a6 + 64*a1*a2*a3*a4/3 - 96*a1*a2*a3*a5*a6 + 8*a1*a2*a3*a5 - 432*a1*a2*a3*a6**2 + 468*a1*a2*a3*a6 - 72*a1*a2*a3 + 64*a1*a2*a4**2*a5/9 + 8*a1*a2*a4**2 + 32*a1*a2*a4*a5**2/3 + 48*a1*a2*a4*a5*a6 - 36*a1*a2*a4*a5 - 64*a1*a3*a4*a6**2/3 + 112*a1*a3*a4*a6/9 - 8*a1*a3*a4/3 + 64*a1*a3*a5**2*a6/9 + 16*a1*a3*a5*a6 - 8*a1*a3*a5/3 - 16*a1*a4**2*a5/27 - 64*a1*a4**2*a6**2/3 + 64*a1*a4**2*a6/9 - 16*a1*a4**2/9 + 64*a1*a4*a5**2*a6/9 - 16*a1*a4*a5**2/9 - 32*a1*a4*a5*a6**2 + 56*a1*a4*a5*a6/3 - 4*a1*a4*a5 - 144*a1*a4*a6**3 + 192*a1*a4*a6**2 - 60*a1*a4*a6 + 6*a1*a4 + 32*a1*a5**3*a6/3 - 8*a1*a5**3/3 + 48*a1*a5**2*a6**2 - 48*a1*a5**2*a6 + 6*a1*a5**2 + 32*a2**3*a3**2 + 32*a2**3*a3*a4 + 48*a2**3*a3*a5 + 216*a2**3*a3*a6 - 180*a2**3*a3 + 64*a2**2*a3*a4*a6/3 - 16*a2**2*a3*a4/9 + 32*a2**2*a3*a5**2/9 + 32*a2**2*a3*a5/3 - 24*a2**2*a3*a6 - 4*a2**2*a3 + 64*a2**2*a4**2*a6/3 - 16*a2**2*a4**2/3 + 32*a2**2*a4*a5**2/9 + 32*a2**2*a4*a5*a6 + 144*a2**2*a4*a6**2 - 156*a2**2*a4*a6 + 30*a2**2*a4 + 16*a2**2*a5**3/3 + 24*a2**2*a5**2*a6 - 12*a2**2*a5**2 + 32*a2*a3*a5*a6**2 - 112*a2*a3*a5*a6/9 + 48*a2*a3*a6**2 - 16*a2*a3*a6 + 4*a2*a3/3 + 64*a2*a4**2*a6/27 - 16*a2*a4**2/27 - 16*a2*a4*a5**2/27 + 32*a2*a4*a5*a6**2 - 16*a2*a4*a5*a6 + 8*a2*a4*a6**2 - 44*a2*a4*a6/3 + 8*a2*a4/3 + 48*a2*a5**2*a6**2 - 56*a2*a5**2*a6/3 + 4*a2*a5**2/3 + 216*a2*a5*a6**3 - 252*a2*a5*a6**2 + 72*a2*a5*a6 - 3*a2*a5 + 32*a3*a6**4 - 112*a3*a6**3/3 + 40*a3*a6**2/3 - 4*a3*a6/3 + 80*a4*a5*a6**2/27 - 8*a4*a5*a6/9 + 32*a4*a6**4 - 64*a4*a6**3/3 + 8*a4*a6**2 - 8*a4*a6/9 - 16*a5**3*a6/27 - 16*a5**2*a6**2/9 - 8*a5**2*a6/9 + 48*a5*a6**4 - 40*a5*a6**3 + 20*a5*a6**2/3 + 2*a5*a6/3 + 216*a6**5 - 360*a6**4 + 198*a6**3 - 42*a6**2 + 3*a6",
          "12*a0*a1*a3*a5 - 4*a0*a1*a4**2 + 72*a0*a2**2*a3*a5 - 24*a0*a2**2*a4**2 - 64*a0*a2*a3**2*a5/9 + 64*a0*a2*a3*a4**2/27 - 64*a0*a2*a3*a4*a5/9 - 32*a0*a2*a3*a5**2/3 - 48*a0*a2*a3*a5*a6 + 40*a0*a2*a3*a5 + 216*a0*a2*a3*a6**2 - 36*a0*a2*a3*a6 + 64*a0*a2*a4**3/27 + 32*a0*a2*a4**2*a5/9 + 16*a0*a2*a4**2*a6 - 40*a0*a2*a4**2/3 - 48*a0*a2*a4*a5*a6 + 4*a0*a2*a4*a5 + 8*a0*a2*a5**3 - 64*a0*a3**2*a6**2/3 + 128*a0*a3**2*a6/9 - 16*a0*a3**2/9 + 128*a0*a3*a4*a5*a6/27 - 64*a0*a3*a4*a5/27 - 64*a0*a3*a4*a6**2/3 + 128*a0*a3*a4*a6/9 - 16*a0*a3*a4/9 - 64*a0*a3*a5**3/81 - 64*a0*a3*a5**2/27 - 32*a0*a3*a5*a6**2 + 32*a0*a3*a5*a6/3 + 8*a0*a3*a5/9 - 144*a0*a3*a6**3 + 168*a0*a3*a6**2 - 48*a0*a3*a6 + 4*a0*a3 + 64*a0*a4**3/243 + 128*a0*a4**2*a5*a6/27 - 64*a0*a4**2*a5/81 + 32*a0*a4**2*a6/9 - 32*a0*a4**2/27 - 64*a0*a4*a5**3/81 + 64*a0*a4*a5**2*a6/9 - 64*a0*a4*a5**2/27 + 32*a0*a4*a5*a6**2 - 80*a0*a4*a5*a6/3 + 4*a0*a4*a5 + 36*a0*a4*a6**2 + 6*a0*a4*a6 - 2*a0*a4 - 32*a0*a5**4/27 - 16*a0*a5**3*a6/3 + 8*a0*a5**3/3 - 12*a0*a5**2*a6 - 4*a0*a5**2 - 72*a1**2*a2*a3*a5 + 24*a1**2*a2*a4**2 + 64*a1**2*a3**2*a5/9 - 64*a1**2*a3*a4**2/27 + 64*a1**2*a3*a4*a5/9 + 32*a1**2*a3*a5**2/3 + 48*a1**2*a3*a5*a6 - 48*a1**2*a3*a5 - 64*a1**2*a4**3/27 - 32*a1**2*a4**2*a5/9 - 16*a1**2*a4**2*a6 + 16*a1**2*a4**2 - 432*a1*a2**2*a3*a6 + 72*a1*a2**2*a3 + 48*a1*a2**2*a4*a5 + 128*a1*a2*a3**2*a6/3 - 128*a1*a2*a3**2/9 - 128*a1*a2*a3*a4*a5/27 + 128*a1*a2*a3*a4*a6/3 - 128*a1*a2*a3*a4/9 + 64*a1*a2*a3*a5*a6 - 16*a1*a2*a3*a5/3 + 288*a1*a2*a3*a6**2 - 312*a1*a2*a3*a6 + 48*a1*a2*a3 - 128*a1*a2*a4**2*a5/27 - 16*a1*a2*a4**2/3 - 64*a1*a2*a4*a5**2/9 - 32*a1*a2*a4*a5*a6 + 24*a1*a2*a4*a5 - 144*a1*a2*a4*a6**2 + 36*a1*a2*a4*a6 - 18*a1*a2*a4 + 48*a1*a2*a5**2*a6 - 12*a1*a2*a5**2 + 128*a1*a3*a4*a6**2/9 - 224*a1*a3*a4*a6/27 + 16*a1*a3*a4/9 - 128*a1*a3*a5**2*a6/27 - 32*a1*a3*a5*a6/3 + 16*a1*a3*a5/9 + 32*a1*a4**2*a5/81 + 128*a1*a4**2*a6**2/9 - 128*a1*a4**2*a6/27 + 32*a1*a4**2/27 - 128*a1*a4*a5**2*a6/27 + 32*a1*a4*a5**2/27 + 64*a1*a4*a5*a6**2/3 - 112*a1*a4*a5*a6/9 + 8*a1*a4*a5/3 + 96*a1*a4*a6**3 - 128*a1*a4*a6**2 + 40*a1*a4*a6 - 4*a1*a4 - 64*a1*a5**3*a6/9 + 16*a1*a5**3/9 - 32*a1*a5**2*a6**2 + 32*a1*a5**2*a6 - 4*a1*a5**2 - 24*a1*a5*a6**2 + 6*a1*a5 + 216*a2**4*a3 - 64*a2**3*a3**2/3 - 64*a2**3*a3*a4/3 - 32*a2**3*a3*a5 - 144*a2**3*a3*a6 + 120*a2**3*a3 + 144*a2**3*a4*a6 - 36*a2**3*a4 + 24*a2**3*a5**2 - 128*a2**2*a3*a4*a6/9 + 32*a2**2*a3*a4/27 - 64*a2**2*a3*a5**2/27 - 64*a2**2*a3*a5/9 + 16*a2**2*a3*a6 + 8*a2**2*a3/3 - 128*a2**2*a4**2*a6/9 + 32*a2**2*a4**2/9 - 64*a2**2*a4*a5**2/27 - 64*a2**2*a4*a5*a6/3 - 96*a2**2*a4*a6**2 + 104*a2**2*a4*a6 - 20*a2**2*a4 - 32*a2**2*a5**3/9 - 16*a2**2*a5**2*a6 + 8*a2**2*a5**2 + 216*a2**2*a5*a6**2 - 120*a2**2*a5*a6 - 6*a2**2*a5 - 64*a2*a3*a5*a6**2/3 + 224*a2*a3*a5*a6/27 - 32*a2*a3*a6**2 + 32*a2*a3*a6/3 - 8*a2*a3/9 - 128*a2*a4**2*a6/81 + 32*a2*a4**2/81 + 32*a2*a4*a5**2/81 - 64*a2*a4*a5*a6**2/3 + 32*a2*a4*a5*a6/3 - 16*a2*a4*a6**2/3 + 88*a2*a4*a6/9 - 16*a2*a4/9 - 32*a2*a5**2*a6**2 + 112*a2*a5**2*a6/9 - 8*a2*a5**2/9 - 144*a2*a5*a6**3 + 168*a2*a5*a6**2 - 48*a2*a5*a6 + 2*a2*a5 + 216*a2*a6**4 - 252*a2*a6**3 + 54*a2*a6**2 + 15*a2*a6 - 3*a2 - 64*a3*a6**4/3 + 224*a3*a6**3/9 - 80*a3*a6**2/9 + 8*a3*a6/9 - 160*a4*a5*a6**2/81 + 16*a4*a5*a6/27 - 64*a4*a6**4/3 + 128*a4*a6**3/9 - 16*a4*a6**2/3 + 16*a4*a6/27 + 32*a5**3*a6/81 + 32*a5**2*a6**2/27 + 16*a5**2*a6/27 - 32*a5*a6**4 + 80*a5*a6**3/3 - 40*a5*a6**2/9 - 4*a5*a6/9 - 144*a6**5 + 240*a6**4 - 132*a6**3 + 28*a6**2 - 2*a6"
        &#93;
      &#93;,
      "shape": &#91;
        5,
        5
      &#93;
    },
    "H": {
      "entries": &#91;
        &#91;
          "-2*a1*a3/3 - 2*a2*a4/9 - a5/9",
          "2*a1*a5/27 + 2*a2*a6/9 - 5*a2/27",
          "2*a1*a4/9 + 2*a2*a5/9 + a6/3 - 1/18",
          "-2*a1*a6/9 - a1/9 + 2*a2**2/9",
          "-2*a0/9"
        &#93;,
        &#91;
          "-2*a2*a3/3 - 2*a4*a6/9 + a4/9",
          "2*a2*a5/27 + 2*a6**2/9 - 5*a6/27 + 1/27",
          "2*a2*a4/9 + 2*a5*a6/9 - a5/9",
          "-a2/9",
          "2*a1*a6/9 - 2*a1/9 - 2*a2**2/9"
        &#93;,
        &#91;
          "2*a3*a6 - a3/3 - 2*a4*a5/9",
          "-a5/27",
          "-2*a4*a6/3 + a4/9 + 2*a5**2/9",
          "2*a2*a5/9 + 2*a6**2/3 - a6/9",
          "2*a1*a5/9 + 2*a2*a6/3 + 2*a2/9"
        &#93;,
        &#91;
          "2*a3*a5/3 - 2*a4**2/9",
          "2*a4*a6/9 - 2*a4/27 - 2*a5**2/27",
          "0",
          "2*a2*a4/9 + 2*a5*a6/9",
          "2*a1*a4/9 + 2*a2*a5/9 - a6/3 + 1/9"
        &#93;,
        &#91;
          "0",
          "2*a3*a6/3 - 2*a3/9 - 2*a4*a5/27",
          "2*a3*a5/3 - 2*a4**2/9",
          "2*a2*a3/3 + 2*a4*a6/9",
          "2*a1*a3/3 + 2*a2*a4/9 - a5/9"
        &#93;,
        &#91;
          "-a0*a3/3 + a2*a5/9 - 1/18",
          "a0*a5/27 + a1/27 + a2**2/9",
          "a0*a4/9 - a2*a6/3",
          "-a0*a6/9 + a0/18 + a1*a2/9",
          "0"
        &#93;,
        &#91;
          "-a1*a3/3 + a5*a6/9",
          "a1*a5/27 + a2*a6/9 + a2/27",
          "a1*a4/9 - a6**2/3 + 1/36",
          "a1/18",
          "a0*a6/9 - a1*a2/9"
        &#93;,
        &#91;
          "-a2*a3 - a4/9 - a5**2/9",
          "2*a6/9 - 1/18",
          "a2*a4/3 + a5*a6/3 + a5/9",
          "-a1*a5/9 - a2*a6/3 + 5*a2/18",
          "-a0*a5/9 + a1/9 - a2**2/3"
        &#93;,
        &#91;
          "-a3*a6 + a3/2 + a4*a5/9",
          "a2*a4/9 + a5*a6/9 - 5*a5/54",
          "-a4/6",
          "a1*a4/9 - a6**2/3 + a6/3 - 1/18",
          "a0*a4/9 - a2*a6/3 + a2/6"
        &#93;,
        &#91;
          "0",
          "a2*a3/3 - a4/27 + a5**2/27",
          "-a3*a6 + a4*a5/9",
          "a1*a3/3 - a5*a6/9 + a5/18",
          "a0*a3/3 - a2*a5/9 + 1/18"
        &#93;
      &#93;,
      "shape": &#91;
        10,
        5
      &#93;
    },
    "M": {
      "entries": &#91;
        &#91;
          "2*a0*a3/9 + 8*a0*a4/27 + 2*a0*a5/9 - 2*a1*a3/27 + 8*a1*a5/27 + 2*a1*a6/3 - a1/3 - 2*a2*a4/81 - 2*a2*a5/27 - a2/18 - a5/81 - 2*a6/27 + 1/54",
          "a0*a3 + a0*a4/3 - a1*a3/3 + a1*a4/3 + a1*a5/3 - a2*a4/9 + a2/2 - a5/18 + a6/6",
          "-4*a0*a3/27 - 16*a0*a4/81 - 10*a0*a5/27 - 2*a0*a6/3 + a0/9 + 2*a1*a2/3 + 4*a1*a3/81 - 10*a1*a5/81 - 10*a1*a6/9 + 2*a1/9 + 4*a2*a4/243 + 4*a2*a5/81 + 2*a2*a6/9 - 4*a2/27 + 2*a5/243 + 4*a6/81 - 1/81",
          "-2*a0*a2/3 + 8*a0*a3/81 + 32*a0*a4/243 + 20*a0*a5/81 + 10*a0*a6/9 - 19*a0/54 + 2*a1**2/3 - 10*a1*a2/9 - 8*a1*a3/243 + 20*a1*a5/243 + 14*a1*a6/27 - 7*a1/27 + 2*a2**2/9 - 8*a2*a4/729 - 8*a2*a5/243 - 4*a2*a6/27 + 8*a2/81 - 4*a5/729 - 8*a6/243 + 2/243",
          "10*a0*a2/9 - 16*a0*a3/243 - 64*a0*a4/729 - 40*a0*a5/243 - 20*a0*a6/27 + a0/81 - 10*a1**2/9 + 20*a1*a2/27 + 16*a1*a3/729 - 40*a1*a5/729 - 28*a1*a6/81 + 14*a1/81 - 4*a2**2/27 + 16*a2*a4/2187 + 16*a2*a5/729 + 8*a2*a6/81 - 16*a2/243 + 8*a5/2187 + 16*a6/729 - 4/729"
        &#93;,
        &#91;
          "2*a1*a3/9 + 8*a1*a4/27 + 2*a1*a5/9 - 2*a2*a3/27 + 8*a2*a5/27 + 2*a2*a6/3 - a2/3 - 2*a4*a6/81 + a4/81 - 2*a5*a6/27 + a5/54 - a6/9 + 1/27",
          "a1*a3 + a1*a4/3 - a2*a3/3 + a2*a4/3 + a2*a5/3 - a4*a6/9 + a4/18 - a5/12 + a6/2 - 1/12",
          "-4*a1*a3/27 - 16*a1*a4/81 - 10*a1*a5/27 - 2*a1*a6/3 + a1/9 + 2*a2**2/3 + 4*a2*a3/81 - 10*a2*a5/81 - 10*a2*a6/9 + a2/6 + 4*a4*a6/243 - 2*a4/243 + 4*a5*a6/81 - a5/81 + 2*a6**2/9 - a6/9 + 1/81",
          "8*a1*a3/81 + 32*a1*a4/243 + 20*a1*a5/81 + 10*a1*a6/9 - 11*a1/27 - 10*a2**2/9 - 8*a2*a3/243 + 20*a2*a5/243 + 20*a2*a6/27 - 2*a2/9 - 8*a4*a6/729 + 4*a4/729 - 8*a5*a6/243 + 2*a5/243 - 4*a6**2/27 + 2*a6/27 - 2/243",
          "2*a0*a2/3 - a0/18 - 2*a1**2/3 - 16*a1*a3/243 - 64*a1*a4/729 - 40*a1*a5/243 - 14*a1*a6/27 + 4*a1/81 + 14*a2**2/27 + 16*a2*a3/729 - 40*a2*a5/729 - 40*a2*a6/81 + 4*a2/27 + 16*a4*a6/2187 - 8*a4/2187 + 16*a5*a6/729 - 4*a5/729 + 8*a6**2/81 - 4*a6/81 + 4/729"
        &#93;,
        &#91;
          "2*a2*a3/3 + 8*a2*a4/9 + 2*a2*a5/3 - 2*a3*a6/9 + a3/27 + 2*a4*a5/81 + a4/27 + 2*a5**2/27 + 8*a5*a6/9 - 7*a5/54 + 2*a6**2 - 5*a6/3 + 1/3",
          "3*a2*a3 + a2*a4 - a3*a6 + a3/6 + a4*a5/9 + a4*a6 + a5*a6 - 5*a5/6",
          "-4*a2*a3/9 - 16*a2*a4/27 - 10*a2*a5/9 - a2/3 + 4*a3*a6/27 - 2*a3/81 - 4*a4*a5/243 - 2*a4/81 - 4*a5**2/81 - 16*a5*a6/27 + 10*a5/81 - 10*a6**2/3 + 13*a6/9 - 1/6",
          "2*a1*a6 - 2*a1/3 - 2*a2**2 + 8*a2*a3/27 + 32*a2*a4/81 + 14*a2*a5/27 - 5*a2/18 - 8*a3*a6/81 + 4*a3/243 + 8*a4*a5/729 + 4*a4/243 + 8*a5**2/243 + 32*a5*a6/81 - 20*a5/243 + 14*a6**2/9 - 23*a6/27 + 1/9",
          "2*a0*a6 - 2*a0/3 - 2*a1*a2 - 2*a1*a5/9 - 10*a1*a6/3 + 7*a1/9 + 10*a2**2/3 - 16*a2*a3/81 - 64*a2*a4/243 - 28*a2*a5/81 - 2*a2*a6/3 - a2/27 + 16*a3*a6/243 - 8*a3/729 - 16*a4*a5/2187 - 8*a4/729 - 16*a5**2/729 - 64*a5*a6/243 + 40*a5/729 - 28*a6**2/27 + 46*a6/81 - 2/27"
        &#93;,
        &#91;
          "2*a3*a5/27 + 2*a3*a6/3 - 5*a3/18 - 2*a4**2/81 - 2*a4*a5/27 + 8*a4*a6/9 - 2*a4/9 - 8*a5**2/27 + a5/3",
          "a3*a5/3 + 3*a3*a6 - 5*a3/4 - a4**2/9 - a4*a5/3 + a4*a6 + a4/2 - a5**2/3",
          "-2*a2*a5/3 - 4*a3*a5/81 - 4*a3*a6/9 + 5*a3/27 + 4*a4**2/243 + 4*a4*a5/81 - 10*a4*a6/27 + 2*a4/27 + 10*a5**2/81 - a5/18 - 2*a6**2 + a6/3",
          "-2*a1*a5/3 + 2*a2*a4/9 + 10*a2*a5/9 - 2*a2*a6 + 8*a3*a5/243 + 8*a3*a6/27 - 10*a3/81 - 8*a4**2/729 - 8*a4*a5/243 + 20*a4*a6/81 - 4*a4/81 - 20*a5**2/243 + 2*a5*a6/9 + a5/27 + 10*a6**2/3 - 14*a6/9 + 1/6",
          "-2*a0*a5/3 + 2*a1*a4/9 + 10*a1*a5/9 - 2*a1*a6 - 4*a2*a4/27 - 14*a2*a5/27 + 10*a2*a6/3 - a2/2 - 16*a3*a5/729 - 16*a3*a6/81 + 20*a3/243 + 16*a4**2/2187 + 16*a4*a5/729 - 40*a4*a6/243 + 8*a4/243 + 40*a5**2/729 - 4*a5*a6/27 - 2*a5/81 - 20*a6**2/9 + 19*a6/27"
        &#93;,
        &#91;
          "a3/2 - 2*a4*a6/3 + 2*a4/3 + 2*a5**2/9",
          "a3*a5 + 3*a3 - a4**2/3",
          "-2*a2*a4/3 + 2*a3*a6/3 - 5*a3/9 - 2*a4*a5/27 + 10*a4*a6/9 - 5*a4/9 - 10*a5**2/27 - 2*a5*a6/3 - 2*a5/9",
          "-2*a1*a4/3 + 2*a2*a3/3 + 10*a2*a4/9 - 2*a2*a5/3 - 4*a3*a6/9 + 10*a3/27 + 4*a4*a5/81 - 14*a4*a6/27 + 10*a4/27 + 20*a5**2/81 + 10*a5*a6/9 - a5/54 + a6 - 1/3",
          "-2*a0*a4/3 + 2*a1*a3/3 + 10*a1*a4/9 - 2*a1*a5/3 - 4*a2*a3/9 - 14*a2*a4/27 + 10*a2*a5/9 + a2 + 8*a3*a6/27 - 20*a3/81 - 8*a4*a5/243 + 28*a4*a6/81 - 20*a4/81 - 40*a5**2/243 - 20*a5*a6/27 - 8*a5/81 - a6 + 1/18"
        &#93;,
        &#91;
          "-a1*a3**2*a6/9 + a1*a3**2/54 + a1*a3*a4*a5/27 - a1*a3*a4*a6/9 + a1*a3*a4/54 + 2*a1*a3*a5**2/27 - 2*a1*a4**3/243 - a1*a4**2*a5/81 + a2**2*a3**2/9 + a2**2*a3*a4/9 + a2*a3*a4*a6/9 - 7*a2*a3*a4/162 + 4*a2*a3*a5**2/81 + 5*a2*a3*a5*a6/9 - 7*a2*a3*a5/54 - 5*a2*a4**2*a5/243 - 2*a2*a4**2*a6/27 - a2*a4*a5**2/81 + 4*a3*a5*a6**2/27 - 13*a3*a5*a6/162 + a3*a5/108 + a3*a6**3 - 2*a3*a6**2/3 + 5*a3*a6/36 - a3/108 + 2*a4**2*a6**2/81 - 5*a4**2*a6/243 + a4**2/243 - 8*a4*a5**2*a6/243 + 5*a4*a5**2/486 - a4*a5*a6**2/9 + a4*a5*a6/162 + a4*a5/162 + a5**4/243 + a5**3*a6/81 + a5**3/162",
          "-a1*a3**2*a6/2 + a1*a3**2/12 + a1*a3*a4*a5/6 - a1*a4**3/27 + a2**2*a3**2/2 + a2*a3*a4*a6/2 - 7*a2*a3*a4/36 + 2*a2*a3*a5**2/9 - 5*a2*a4**2*a5/54 + 2*a3*a5*a6**2/3 - 13*a3*a5*a6/36 + a3*a5/24 + a4**2*a6**2/9 - 5*a4**2*a6/54 + a4**2/54 - 4*a4*a5**2*a6/27 + 5*a4*a5**2/108 + a5**4/54",
          "2*a1*a3**2*a6/27 - a1*a3**2/81 - 2*a1*a3*a4*a5/81 + 2*a1*a3*a4*a6/27 - a1*a3*a4/81 - 4*a1*a3*a5**2/81 - a1*a3*a5*a6/9 + a1*a3*a5/18 + 4*a1*a4**3/729 + 2*a1*a4**2*a5/243 + 2*a1*a4**2*a6/27 - 2*a1*a4**2/81 - a1*a4*a5**2/81 - 2*a2**2*a3**2/27 - 2*a2**2*a3*a4/27 + 2*a2**2*a3*a5/9 - a2**2*a4**2/9 - 2*a2*a3*a4*a6/27 + 7*a2*a3*a4/243 - 8*a2*a3*a5**2/243 - 10*a2*a3*a5*a6/27 + 7*a2*a3*a5/81 + a2*a3*a6**2/3 - a2*a3*a6/18 - a2*a3/54 + 10*a2*a4**2*a5/729 + 4*a2*a4**2*a6/81 + 2*a2*a4*a5**2/243 - 5*a2*a4*a5*a6/27 + 4*a2*a4*a5/81 + 2*a2*a5**3/81 - 8*a3*a5*a6**2/81 + 13*a3*a5*a6/243 - a3*a5/162 - 2*a3*a6**3/3 + 4*a3*a6**2/9 - 5*a3*a6/54 + a3/162 - 4*a4**2*a6**2/243 + 10*a4**2*a6/729 - 2*a4**2/729 + 16*a4*a5**2*a6/729 - 5*a4*a5**2/729 + 2*a4*a5*a6**2/27 - a4*a5*a6/243 - a4*a5/243 - 2*a4*a6**3/9 + 7*a4*a6**2/27 - 8*a4*a6/81 + a4/81 - 2*a5**4/729 - 2*a5**3*a6/243 - a5**3/243 + a5**2*a6**2/27 - a5**2*a6/27 + a5**2/108",
          "a1*a2*a3*a5/9 - a1*a2*a4**2/27 - 4*a1*a3**2*a6/81 + 2*a1*a3**2/243 + 4*a1*a3*a4*a5/243 - 4*a1*a3*a4*a6/81 + 2*a1*a3*a4/243 + 8*a1*a3*a5**2/243 + 2*a1*a3*a5*a6/27 - a1*a3*a5/27 + 2*a1*a3*a6**2/3 - 4*a1*a3*a6/9 + a1*a3/18 - 8*a1*a4**3/2187 - 4*a1*a4**2*a5/729 - 4*a1*a4**2*a6/81 + 4*a1*a4**2/243 + 2*a1*a4*a5**2/243 - 5*a1*a4*a5*a6/27 + a1*a4*a5/18 + a1*a5**3/27 + 4*a2**2*a3**2/81 + 4*a2**2*a3*a4/81 - 4*a2**2*a3*a5/27 - a2**2*a3*a6/3 + 2*a2**2*a3/9 + 2*a2**2*a4**2/27 + 2*a2**2*a4*a5/27 + 4*a2*a3*a4*a6/81 - 14*a2*a3*a4/729 + 16*a2*a3*a5**2/729 + 20*a2*a3*a5*a6/81 - 14*a2*a3*a5/243 - 2*a2*a3*a6**2/9 + a2*a3*a6/27 + a2*a3/81 - 20*a2*a4**2*a5/2187 - 8*a2*a4**2*a6/243 - 4*a2*a4*a5**2/729 + 10*a2*a4*a5*a6/81 - 8*a2*a4*a5/243 - a2*a4*a6**2/9 + 7*a2*a4*a6/54 - a2*a4/27 - 4*a2*a5**3/243 + a2*a5**2*a6/9 - a2*a5**2/27 + 16*a3*a5*a6**2/243 - 26*a3*a5*a6/729 + a3*a5/243 + 4*a3*a6**3/9 - 8*a3*a6**2/27 + 5*a3*a6/81 - a3/243 + 8*a4**2*a6**2/729 - 20*a4**2*a6/2187 + 4*a4**2/2187 - 32*a4*a5**2*a6/2187 + 10*a4*a5**2/2187 - 4*a4*a5*a6**2/81 + 2*a4*a5*a6/729 + 2*a4*a5/729 + 4*a4*a6**3/27 - 14*a4*a6**2/81 + 16*a4*a6/243 - 2*a4/243 + 4*a5**4/2187 + 4*a5**3*a6/729 + 2*a5**3/729 - 2*a5**2*a6**2/81 + 2*a5**2*a6/81 - a5**2/162 + a5*a6**3/9 - 2*a5*a6**2/27 + a5*a6/108",
          "a0*a2*a3*a5/3 - a0*a2*a4**2/9 + a0*a3*a6**2 - a0*a3*a6/2 + a0*a3/18 - 2*a0*a4*a5*a6/9 + a0*a4*a5/18 + a0*a5**3/27 - 2*a1**2*a3*a5/9 + 2*a1**2*a4**2/27 - 2*a1*a2*a3*a5/27 - a1*a2*a3*a6 + 5*a1*a2*a3/18 + 2*a1*a2*a4**2/81 + a1*a2*a4*a5/9 + 8*a1*a3**2*a6/243 - 4*a1*a3**2/729 - 8*a1*a3*a4*a5/729 + 8*a1*a3*a4*a6/243 - 4*a1*a3*a4/729 - 16*a1*a3*a5**2/729 - 4*a1*a3*a5*a6/81 + 2*a1*a3*a5/81 - 4*a1*a3*a6**2/9 + 8*a1*a3*a6/27 - a1*a3/27 + 16*a1*a4**3/6561 + 8*a1*a4**2*a5/2187 + 8*a1*a4**2*a6/243 - 8*a1*a4**2/729 - 4*a1*a4*a5**2/729 + 10*a1*a4*a5*a6/81 - a1*a4*a5/27 - 2*a1*a4*a6**2/9 + 8*a1*a4*a6/27 - a1*a4/18 - 2*a1*a5**3/81 + 2*a1*a5**2*a6/27 - 2*a1*a5**2/27 + a2**3*a3/3 - 8*a2**2*a3**2/243 - 8*a2**2*a3*a4/243 + 8*a2**2*a3*a5/81 + 2*a2**2*a3*a6/9 - 4*a2**2*a3/27 - 4*a2**2*a4**2/81 - 4*a2**2*a4*a5/81 + a2**2*a4*a6/9 - a2**2*a4/6 + a2**2*a5**2/27 - 8*a2*a3*a4*a6/243 + 28*a2*a3*a4/2187 - 32*a2*a3*a5**2/2187 - 40*a2*a3*a5*a6/243 + 28*a2*a3*a5/729 + 4*a2*a3*a6**2/27 - 2*a2*a3*a6/81 - 2*a2*a3/243 + 40*a2*a4**2*a5/6561 + 16*a2*a4**2*a6/729 + 8*a2*a4*a5**2/2187 - 20*a2*a4*a5*a6/243 + 16*a2*a4*a5/729 + 2*a2*a4*a6**2/27 - 7*a2*a4*a6/81 + 2*a2*a4/81 + 8*a2*a5**3/729 - 2*a2*a5**2*a6/27 + 2*a2*a5**2/81 + a2*a5*a6**2/9 - 8*a2*a5*a6/27 + 11*a2*a5/108 - 32*a3*a5*a6**2/729 + 52*a3*a5*a6/2187 - 2*a3*a5/729 - 8*a3*a6**3/27 + 16*a3*a6**2/81 - 10*a3*a6/243 + 2*a3/729 - 16*a4**2*a6**2/2187 + 40*a4**2*a6/6561 - 8*a4**2/6561 + 64*a4*a5**2*a6/6561 - 20*a4*a5**2/6561 + 8*a4*a5*a6**2/243 - 4*a4*a5*a6/2187 - 4*a4*a5/2187 - 8*a4*a6**3/81 + 28*a4*a6**2/243 - 32*a4*a6/729 + 4*a4/729 - 8*a5**4/6561 - 8*a5**3*a6/2187 - 4*a5**3/2187 + 4*a5**2*a6**2/243 - 4*a5**2*a6/243 + a5**2/243 - 2*a5*a6**3/27 + 4*a5*a6**2/81 - a5*a6/162 - a6**3/3 + a6**2/3 - 11*a6/108 + 1/108"
        &#93;,
        &#91;
          "-a0*a3**2*a6/18 + a0*a3**2/108 + a0*a3*a4*a5/54 - a0*a3*a4*a6/18 + a0*a3*a4/108 + a0*a3*a5**2/27 - a0*a4**3/243 - a0*a4**2*a5/162 + a1*a2*a3**2/18 + a1*a2*a3*a4/18 + 2*a1*a3*a4*a6/27 - a1*a3*a4/54 - a1*a3*a5**2/54 - a1*a3*a5/18 + 2*a1*a4**2*a6/27 - a1*a4*a5**2/54 - a2**2*a3*a4/54 + 4*a2**2*a3*a5/9 - a2**2*a4**2/6 - 13*a2*a3*a5*a6/54 + a2*a3*a5/6 + a2*a3*a6**2 - 7*a2*a3*a6/12 + 7*a2*a3/72 + 5*a2*a4**2*a6/81 - 7*a2*a4**2/162 - 5*a2*a4*a5*a6/18 + 11*a2*a4*a5/108 + a2*a5**3/27 - 5*a3*a6**3/9 + 19*a3*a6**2/27 - 13*a3*a6/54 + 5*a3/216 + 7*a4*a5*a6**2/81 - 7*a4*a5*a6/81 + 5*a4*a5/324 - 2*a4*a6**3/9 + 7*a4*a6**2/27 - a4*a6/18 - a5**3*a6/81 + a5**3/108 + a5**2*a6**2/27 - a5**2*a6/36 - a5**2/216",
          "-a0*a3**2*a6/4 + a0*a3**2/24 + a0*a3*a4*a5/12 - a0*a4**3/54 + a1*a2*a3**2/4 + a1*a3*a4*a6/3 - a1*a3*a4/12 - a1*a3*a5**2/12 - a2**2*a3*a4/12 - 13*a2*a3*a5*a6/12 + 3*a2*a3*a5/4 + 5*a2*a4**2*a6/18 - 7*a2*a4**2/36 - 5*a3*a6**3/2 + 19*a3*a6**2/6 - 13*a3*a6/12 + 5*a3/48 + 7*a4*a5*a6**2/18 - 7*a4*a5*a6/18 + 5*a4*a5/72 - a5**3*a6/18 + a5**3/24",
          "a0*a3**2*a6/27 - a0*a3**2/162 - a0*a3*a4*a5/81 + a0*a3*a4*a6/27 - a0*a3*a4/162 - 2*a0*a3*a5**2/81 - a0*a3*a5*a6/18 + a0*a3*a5/36 + 2*a0*a4**3/729 + a0*a4**2*a5/243 + a0*a4**2*a6/27 - a0*a4**2/81 - a0*a4*a5**2/162 - a1*a2*a3**2/27 - a1*a2*a3*a4/27 + 5*a1*a2*a3*a5/18 - a1*a2*a4**2/9 - 4*a1*a3*a4*a6/81 + a1*a3*a4/81 + a1*a3*a5**2/81 + a1*a3*a5/27 + a1*a3*a6**2 - a1*a3*a6/3 + a1*a3/36 - 4*a1*a4**2*a6/81 + a1*a4*a5**2/81 - 8*a1*a4*a5*a6/27 + a1*a4*a5/18 + a1*a5**3/18 + a2**2*a3*a4/81 - 8*a2**2*a3*a5/27 - a2**2*a3*a6/3 + a2**2*a3/36 + a2**2*a4**2/9 + a2**2*a4*a5/18 + 13*a2*a3*a5*a6/81 - a2*a3*a5/9 - 2*a2*a3*a6**2/3 + 7*a2*a3*a6/18 - 7*a2*a3/108 - 10*a2*a4**2*a6/243 + 7*a2*a4**2/243 + 5*a2*a4*a5*a6/27 - 11*a2*a4*a5/162 - 2*a2*a4*a6**2/9 + 5*a2*a4*a6/27 - a2*a4/54 - 2*a2*a5**3/81 + 7*a2*a5**2*a6/54 - 5*a2*a5**2/54 + 10*a3*a6**3/27 - 38*a3*a6**2/81 + 13*a3*a6/81 - 5*a3/324 - 14*a4*a5*a6**2/243 + 14*a4*a5*a6/243 - 5*a4*a5/486 + 4*a4*a6**3/27 - 14*a4*a6**2/81 + a4*a6/27 + 2*a5**3*a6/243 - a5**3/162 - 2*a5**2*a6**2/81 + a5**2*a6/54 + a5**2/324 + a5*a6**3/9 - a5*a6**2/6 + 2*a5*a6/27 - a5/108",
          "-a0*a2*a3*a5/9 + a0*a2*a4**2/27 - 2*a0*a3**2*a6/81 + a0*a3**2/243 + 2*a0*a3*a4*a5/243 - 2*a0*a3*a4*a6/81 + a0*a3*a4/243 + 4*a0*a3*a5**2/243 + a0*a3*a5*a6/27 - a0*a3*a5/54 - a0*a3*a6**2/6 + a0*a3*a6/36 - 4*a0*a4**3/2187 - 2*a0*a4**2*a5/729 - 2*a0*a4**2*a6/81 + 2*a0*a4**2/243 + a0*a4*a5**2/243 + a0*a4*a5*a6/54 + a1**2*a3*a5/3 - a1**2*a4**2/9 + 2*a1*a2*a3**2/81 + 2*a1*a2*a3*a4/81 - 5*a1*a2*a3*a5/27 + 13*a1*a2*a3*a6/6 - 5*a1*a2*a3/12 + 2*a1*a2*a4**2/27 - 2*a1*a2*a4*a5/9 + 8*a1*a3*a4*a6/243 - 2*a1*a3*a4/243 - 2*a1*a3*a5**2/243 - 2*a1*a3*a5/81 - 2*a1*a3*a6**2/3 + 2*a1*a3*a6/9 - a1*a3/54 + 8*a1*a4**2*a6/243 - 2*a1*a4*a5**2/243 + 16*a1*a4*a5*a6/81 - a1*a4*a5/27 + 8*a1*a4*a6**2/9 - 4*a1*a4*a6/9 + a1*a4/18 - a1*a5**3/27 - 5*a1*a5**2*a6/18 + a1*a5**2/12 - 4*a2**3*a3/3 - 2*a2**2*a3*a4/243 + 16*a2**2*a3*a5/81 + 2*a2**2*a3*a6/9 - a2**2*a3/54 - 2*a2**2*a4**2/27 - a2**2*a4*a5/27 - 19*a2**2*a4*a6/18 + 7*a2**2*a4/18 - a2**2*a5**2/9 - 26*a2*a3*a5*a6/243 + 2*a2*a3*a5/27 + 4*a2*a3*a6**2/9 - 7*a2*a3*a6/27 + 7*a2*a3/162 + 20*a2*a4**2*a6/729 - 14*a2*a4**2/729 - 10*a2*a4*a5*a6/81 + 11*a2*a4*a5/243 + 4*a2*a4*a6**2/27 - 10*a2*a4*a6/81 + a2*a4/81 + 4*a2*a5**3/243 - 7*a2*a5**2*a6/81 + 5*a2*a5**2/81 - 3*a2*a5*a6**2/2 + 37*a2*a5*a6/36 - a2*a5/6 - 20*a3*a6**3/81 + 76*a3*a6**2/243 - 26*a3*a6/243 + 5*a3/486 + 28*a4*a5*a6**2/729 - 28*a4*a5*a6/729 + 5*a4*a5/729 - 8*a4*a6**3/81 + 28*a4*a6**2/243 - 2*a4*a6/81 - 4*a5**3*a6/729 + a5**3/243 + 4*a5**2*a6**2/243 - a5**2*a6/81 - a5**2/486 - 2*a5*a6**3/27 + a5*a6**2/9 - 4*a5*a6/81 + a5/162 - 5*a6**4/3 + 19*a6**3/9 - 35*a6**2/36 + 7*a6/36 - 1/72",
          "2*a0*a1*a3*a5/9 - 2*a0*a1*a4**2/27 + 2*a0*a2*a3*a5/27 + 5*a0*a2*a3*a6/6 - 2*a0*a2*a3/9 - 2*a0*a2*a4**2/81 - 5*a0*a2*a4*a5/54 + 4*a0*a3**2*a6/243 - 2*a0*a3**2/729 - 4*a0*a3*a4*a5/729 + 4*a0*a3*a4*a6/243 - 2*a0*a3*a4/729 - 8*a0*a3*a5**2/729 - 2*a0*a3*a5*a6/81 + a0*a3*a5/81 + a0*a3*a6**2/9 - a0*a3*a6/54 + 8*a0*a4**3/6561 + 4*a0*a4**2*a5/2187 + 4*a0*a4**2*a6/243 - 4*a0*a4**2/729 - 2*a0*a4*a5**2/729 - a0*a4*a5*a6/81 + a0*a4*a6**2/3 - a0*a4*a6/9 + a0*a4/54 - a0*a5**2*a6/9 + a0*a5**2/108 - 2*a1**2*a3*a5/9 + a1**2*a3*a6 - a1**2*a3/6 + 2*a1**2*a4**2/27 - a1**2*a4*a5/9 - 7*a1*a2**2*a3/6 - 4*a1*a2*a3**2/243 - 4*a1*a2*a3*a4/243 + 10*a1*a2*a3*a5/81 - 13*a1*a2*a3*a6/9 + 5*a1*a2*a3/18 - 4*a1*a2*a4**2/81 + 4*a1*a2*a4*a5/27 + a1*a2*a4/18 - 5*a1*a2*a5**2/18 - 16*a1*a3*a4*a6/729 + 4*a1*a3*a4/729 + 4*a1*a3*a5**2/729 + 4*a1*a3*a5/243 + 4*a1*a3*a6**2/9 - 4*a1*a3*a6/27 + a1*a3/81 - 16*a1*a4**2*a6/729 + 4*a1*a4*a5**2/729 - 32*a1*a4*a5*a6/243 + 2*a1*a4*a5/81 - 16*a1*a4*a6**2/27 + 8*a1*a4*a6/27 - a1*a4/27 + 2*a1*a5**3/81 + 5*a1*a5**2*a6/27 - a1*a5**2/18 - 4*a1*a5*a6**2/9 + 2*a1*a5*a6/9 + 8*a2**3*a3/9 - a2**3*a4/2 + 4*a2**2*a3*a4/729 - 32*a2**2*a3*a5/243 - 4*a2**2*a3*a6/27 + a2**2*a3/81 + 4*a2**2*a4**2/81 + 2*a2**2*a4*a5/81 + 19*a2**2*a4*a6/27 - 7*a2**2*a4/27 + 2*a2**2*a5**2/27 - 19*a2**2*a5*a6/18 + 13*a2**2*a5/36 + 52*a2*a3*a5*a6/729 - 4*a2*a3*a5/81 - 8*a2*a3*a6**2/27 + 14*a2*a3*a6/81 - 7*a2*a3/243 - 40*a2*a4**2*a6/2187 + 28*a2*a4**2/2187 + 20*a2*a4*a5*a6/243 - 22*a2*a4*a5/729 - 8*a2*a4*a6**2/81 + 20*a2*a4*a6/243 - 2*a2*a4/243 - 8*a2*a5**3/729 + 14*a2*a5**2*a6/243 - 10*a2*a5**2/243 + a2*a5*a6**2 - 37*a2*a5*a6/54 + a2*a5/9 - 5*a2*a6**3/3 + 13*a2*a6**2/9 - 13*a2*a6/36 + a2/36 + 40*a3*a6**3/243 - 152*a3*a6**2/729 + 52*a3*a6/729 - 5*a3/729 - 56*a4*a5*a6**2/2187 + 56*a4*a5*a6/2187 - 10*a4*a5/2187 + 16*a4*a6**3/243 - 56*a4*a6**2/729 + 4*a4*a6/243 + 8*a5**3*a6/2187 - 2*a5**3/729 - 8*a5**2*a6**2/729 + 2*a5**2*a6/243 + a5**2/729 + 4*a5*a6**3/81 - 2*a5*a6**2/27 + 8*a5*a6/243 - a5/243 + 10*a6**4/9 - 38*a6**3/27 + 35*a6**2/54 - 7*a6/54 + 1/108"
        &#93;,
        &#91;
          "-a0**2*a2*a3**2*a5/6 + a0**2*a2*a3*a4**2/27 - a0**2*a2*a3*a4*a5/6 + a0**2*a2*a4**3/27 + 2*a0**2*a3**2*a6/9 - a0**2*a3**2/27 - a0**2*a3*a4*a5*a6/54 - 17*a0**2*a3*a4*a5/324 + 2*a0**2*a3*a4*a6/9 - a0**2*a3*a4/27 - a0**2*a3*a5**3/18 - a0**2*a3*a5**2*a6/2 - 7*a0**2*a3*a5**2/108 + 2*a0**2*a4**3*a6/81 + 2*a0**2*a4**3/243 + 5*a0**2*a4**2*a5**2/486 + 2*a0**2*a4**2*a5*a6/9 - a0**2*a4**2*a5/162 - 2*a0**2*a4*a5**3/81 + a0*a1**2*a3**2*a5/6 - a0*a1**2*a3*a4**2/27 + a0*a1**2*a3*a4*a5/6 - a0*a1**2*a4**3/27 + 2*a0*a1*a2*a3**2*a6/3 - a0*a1*a2*a3**2/2 - 29*a0*a1*a2*a3*a4*a5/54 + 2*a0*a1*a2*a3*a4*a6/3 - a0*a1*a2*a3*a4/2 - a0*a1*a2*a3*a5**2/9 + 8*a0*a1*a2*a4**3/81 - 11*a0*a1*a2*a4**2*a5/54 - 5*a0*a1*a3*a4*a6**2/9 + 7*a0*a1*a3*a4*a6/54 + a0*a1*a3*a4/27 - 11*a0*a1*a3*a5**2*a6/18 + 19*a0*a1*a3*a5**2/108 - 3*a0*a1*a3*a5*a6**2 + a0*a1*a3*a5*a6/3 + a0*a1*a3*a5/9 + 16*a0*a1*a4**2*a5*a6/81 - a0*a1*a4**2*a5/27 + 4*a0*a1*a4**2*a6**2/9 - a0*a1*a4**2*a6/27 + a0*a1*a4**2/54 - a0*a1*a4*a5**2*a6/54 + a0*a1*a4*a5**2/12 - a0*a2**3*a3**2 - a0*a2**3*a3*a4 - 11*a0*a2**2*a3*a4*a6/9 + 5*a0*a2**2*a3*a4/27 - 7*a0*a2**2*a3*a5**2/9 - 5*a0*a2**2*a3*a5*a6 + 25*a0*a2**2*a3*a5/18 + 19*a0*a2**2*a4**2*a5/81 + 7*a0*a2**2*a4**2*a6/9 - 7*a0*a2**2*a4**2/18 - 5*a0*a2**2*a4*a5**2/27 - 59*a0*a2*a3*a5*a6**2/18 + 85*a0*a2*a3*a5*a6/108 - 11*a0*a2*a3*a5/108 - 15*a0*a2*a3*a6**3 + 41*a0*a2*a3*a6**2/4 - 21*a0*a2*a3*a6/8 + 17*a0*a2*a3/72 - 10*a0*a2*a4**2*a6**2/27 + 61*a0*a2*a4**2*a6/162 - 2*a0*a2*a4**2/81 + 38*a0*a2*a4*a5**2*a6/81 - a0*a2*a4*a5**2/9 + 17*a0*a2*a4*a5*a6**2/18 - 5*a0*a2*a4*a5*a6/6 + 11*a0*a2*a4*a5/54 - 4*a0*a2*a5**4/81 - 7*a0*a2*a5**3*a6/27 + 7*a0*a2*a5**3/54 - 22*a0*a3*a6**3/9 + 73*a0*a3*a6**2/54 - 23*a0*a3*a6/108 + a0*a3/108 - a0*a4*a5*a6**3/3 + 103*a0*a4*a5*a6**2/162 - 13*a0*a4*a5*a6/81 + a0*a4*a5/108 - a0*a4*a6**4 - 4*a0*a4*a6**3/9 + 17*a0*a4*a6**2/108 + a0*a4*a6/108 + 2*a0*a5**3*a6**2/27 - 31*a0*a5**3*a6/324 + a0*a5**3/162 + 29*a0*a5**2*a6**2/108 + a0*a5**2*a6/24 + a1**3*a3**2/6 + a1**3*a3*a4*a5/3 + a1**3*a3*a4/6 + a1**3*a3*a5**2/3 - 2*a1**3*a4**3/27 + a1**2*a2**2*a3**2/3 + a1**2*a2**2*a3*a4/3 + 14*a1**2*a2*a3*a4*a6/9 - 2*a1**2*a2*a3*a4/9 + 2*a1**2*a2*a3*a5**2/3 + 13*a1**2*a2*a3*a5*a6/2 - 7*a1**2*a2*a3*a5/4 - 7*a1**2*a2*a4**2*a5/27 - 7*a1**2*a2*a4**2*a6/9 + 4*a1**2*a2*a4**2/9 - a1**2*a2*a4*a5**2/18 - 2*a1**2*a3*a5*a6**2/3 + 11*a1**2*a3*a5*a6/9 - a1**2*a3*a5/9 - 3*a1**2*a3*a6**2/2 + 3*a1**2*a3*a6/4 - a1**2*a3/12 + 4*a1**2*a4**2*a6**2/9 - 4*a1**2*a4**2*a6/9 + a1**2*a4**2/18 - a1**2*a4*a5**2*a6/9 + a1**2*a4*a5**2/27 + 7*a1**2*a4*a5*a6/18 + a1**2*a5**4/54 + a1**2*a5**3*a6/18 + a1**2*a5**3/36 - 4*a1*a2**3*a3*a4/9 - 4*a1*a2**3*a3*a5/3 + 10*a1*a2**2*a3*a5*a6/3 - 29*a1*a2**2*a3*a5/36 + 15*a1*a2**2*a3*a6**2 - 35*a1*a2**2*a3*a6/4 + 35*a1*a2**2*a3/24 - 2*a1*a2**2*a4**2*a6/9 + 5*a1*a2**2*a4**2/54 - 2*a1*a2**2*a4*a5**2/9 - a1*a2**2*a4*a5*a6/3 + 11*a1*a2**2*a4*a5/18 - 2*a1*a2**2*a5**3/9 - 2*a1*a2*a3*a6**3/3 + 46*a1*a2*a3*a6**2/9 - 47*a1*a2*a3*a6/36 + a1*a2*a3/72 + 7*a1*a2*a4*a5*a6**2/27 - 25*a1*a2*a4*a5*a6/54 + 5*a1*a2*a4*a5/108 + 10*a1*a2*a4*a6**3/3 - 20*a1*a2*a4*a6**2/9 + 4*a1*a2*a4*a6/3 - 2*a1*a2*a4/9 - a1*a2*a5**3*a6/27 + a1*a2*a5**3/108 - 8*a1*a2*a5**2*a6**2/9 + 47*a1*a2*a5**2*a6/36 - 13*a1*a2*a5**2/72 - 2*a1*a4*a6**4/3 + 17*a1*a4*a6**3/9 - 19*a1*a4*a6**2/27 + a1*a4*a6/9 - a1*a4/108 + 2*a1*a5**2*a6**3/9 - 29*a1*a5**2*a6**2/54 + a1*a5**2*a6/9 - a1*a5**2/108 + 5*a1*a5*a6**3/6 - a1*a5*a6**2/36 - a1*a5*a6/36 - 7*a2**4*a3*a5/6 - 6*a2**4*a3*a6 + 3*a2**4*a3 - a2**4*a4*a5/2 + a2**3*a3*a6**2/3 - 7*a2**3*a3*a6/3 - a2**3*a3/24 - 10*a2**3*a4*a5*a6/27 + 11*a2**3*a4*a5/108 - 8*a2**3*a4*a6**2/3 + 29*a2**3*a4*a6/12 - 2*a2**3*a4/3 - 5*a2**3*a5**3/54 - 17*a2**3*a5**2*a6/18 + 17*a2**3*a5**2/36 + 2*a2**2*a4*a6**3/9 - 35*a2**2*a4*a6**2/27 + 11*a2**2*a4*a6/54 - a2**2*a4/36 - a2**2*a5**2*a6**2/2 + 7*a2**2*a5**2*a6/108 - a2**2*a5**2/108 - 23*a2**2*a5*a6**3/6 + 101*a2**2*a5*a6**2/18 - 137*a2**2*a5*a6/72 + a2**2*a5/9 - a2*a5*a6**4/3 - 4*a2*a5*a6**3/3 + 67*a2*a5*a6**2/108 - a2*a5*a6/12 + a2*a5/216 - 3*a2*a6**5 + 7*a2*a6**4 - 53*a2*a6**3/12 + 41*a2*a6**2/36 - a2*a6/9 - 5*a6**5/3 + 3*a6**4/2 - 55*a6**3/108 + 17*a6**2/216 - a6/216",
          "-3*a0**2*a2*a3**2*a5/4 + a0**2*a2*a3*a4**2/6 + a0**2*a3**2*a6 - a0**2*a3**2/6 - a0**2*a3*a4*a5*a6/12 - 17*a0**2*a3*a4*a5/72 - a0**2*a3*a5**3/4 + a0**2*a4**3*a6/9 + a0**2*a4**3/27 + 5*a0**2*a4**2*a5**2/108 + 3*a0*a1**2*a3**2*a5/4 - a0*a1**2*a3*a4**2/6 + 3*a0*a1*a2*a3**2*a6 - 9*a0*a1*a2*a3**2/4 - 29*a0*a1*a2*a3*a4*a5/12 + 4*a0*a1*a2*a4**3/9 - 5*a0*a1*a3*a4*a6**2/2 + 7*a0*a1*a3*a4*a6/12 + a0*a1*a3*a4/6 - 11*a0*a1*a3*a5**2*a6/4 + 19*a0*a1*a3*a5**2/24 + 8*a0*a1*a4**2*a5*a6/9 - a0*a1*a4**2*a5/6 - 9*a0*a2**3*a3**2/2 - 11*a0*a2**2*a3*a4*a6/2 + 5*a0*a2**2*a3*a4/6 - 7*a0*a2**2*a3*a5**2/2 + 19*a0*a2**2*a4**2*a5/18 - 59*a0*a2*a3*a5*a6**2/4 + 85*a0*a2*a3*a5*a6/24 - 11*a0*a2*a3*a5/24 - 5*a0*a2*a4**2*a6**2/3 + 61*a0*a2*a4**2*a6/36 - a0*a2*a4**2/9 + 19*a0*a2*a4*a5**2*a6/9 - a0*a2*a4*a5**2/2 - 2*a0*a2*a5**4/9 - 11*a0*a3*a6**3 + 73*a0*a3*a6**2/12 - 23*a0*a3*a6/24 + a0*a3/24 - 3*a0*a4*a5*a6**3/2 + 103*a0*a4*a5*a6**2/36 - 13*a0*a4*a5*a6/18 + a0*a4*a5/24 + a0*a5**3*a6**2/3 - 31*a0*a5**3*a6/72 + a0*a5**3/36 + 3*a1**3*a3**2/4 + 3*a1**3*a3*a4*a5/2 - a1**3*a4**3/3 + 3*a1**2*a2**2*a3**2/2 + 7*a1**2*a2*a3*a4*a6 - a1**2*a2*a3*a4 + 3*a1**2*a2*a3*a5**2 - 7*a1**2*a2*a4**2*a5/6 - 3*a1**2*a3*a5*a6**2 + 11*a1**2*a3*a5*a6/2 - a1**2*a3*a5/2 + 2*a1**2*a4**2*a6**2 - 2*a1**2*a4**2*a6 + a1**2*a4**2/4 - a1**2*a4*a5**2*a6/2 + a1**2*a4*a5**2/6 + a1**2*a5**4/12 - 2*a1*a2**3*a3*a4 + 15*a1*a2**2*a3*a5*a6 - 29*a1*a2**2*a3*a5/8 - a1*a2**2*a4**2*a6 + 5*a1*a2**2*a4**2/12 - a1*a2**2*a4*a5**2 - 3*a1*a2*a3*a6**3 + 23*a1*a2*a3*a6**2 - 47*a1*a2*a3*a6/8 + a1*a2*a3/16 + 7*a1*a2*a4*a5*a6**2/6 - 25*a1*a2*a4*a5*a6/12 + 5*a1*a2*a4*a5/24 - a1*a2*a5**3*a6/6 + a1*a2*a5**3/24 - 3*a1*a4*a6**4 + 17*a1*a4*a6**3/2 - 19*a1*a4*a6**2/6 + a1*a4*a6/2 - a1*a4/24 + a1*a5**2*a6**3 - 29*a1*a5**2*a6**2/12 + a1*a5**2*a6/2 - a1*a5**2/24 - 21*a2**4*a3*a5/4 + 3*a2**3*a3*a6**2/2 - 21*a2**3*a3*a6/2 - 3*a2**3*a3/16 - 5*a2**3*a4*a5*a6/3 + 11*a2**3*a4*a5/24 - 5*a2**3*a5**3/12 + a2**2*a4*a6**3 - 35*a2**2*a4*a6**2/6 + 11*a2**2*a4*a6/12 - a2**2*a4/8 - 9*a2**2*a5**2*a6**2/4 + 7*a2**2*a5**2*a6/24 - a2**2*a5**2/24 - 3*a2*a5*a6**4/2 - 6*a2*a5*a6**3 + 67*a2*a5*a6**2/24 - 3*a2*a5*a6/8 + a2*a5/48 - 15*a6**5/2 + 27*a6**4/4 - 55*a6**3/24 + 17*a6**2/48 - a6/48",
          "a0**2*a2*a3**2*a5/9 - 2*a0**2*a2*a3*a4**2/81 + a0**2*a2*a3*a4*a5/9 + a0**2*a2*a3*a5**2/3 - 2*a0**2*a2*a4**3/81 - 5*a0**2*a2*a4**2*a5/54 - 4*a0**2*a3**2*a6/27 + 2*a0**2*a3**2/81 + a0**2*a3*a4*a5*a6/81 + 17*a0**2*a3*a4*a5/486 - 4*a0**2*a3*a4*a6/27 + 2*a0**2*a3*a4/81 + a0**2*a3*a5**3/27 + a0**2*a3*a5**2*a6/3 + 7*a0**2*a3*a5**2/162 + 2*a0**2*a3*a5*a6**2 - 7*a0**2*a3*a5*a6/9 + a0**2*a3*a5/36 - 4*a0**2*a4**3*a6/243 - 4*a0**2*a4**3/729 - 5*a0**2*a4**2*a5**2/729 - 4*a0**2*a4**2*a5*a6/27 + a0**2*a4**2*a5/243 - 2*a0**2*a4**2*a6**2/9 + 2*a0**2*a4**2/81 + 4*a0**2*a4*a5**3/243 - 19*a0**2*a4*a5**2*a6/54 + 29*a0**2*a4*a5**2/324 + 2*a0**2*a5**4/27 - a0*a1**2*a3**2*a5/9 + 2*a0*a1**2*a3*a4**2/81 - a0*a1**2*a3*a4*a5/9 - a0*a1**2*a3*a5**2/6 + 2*a0*a1**2*a4**3/81 + a0*a1**2*a4**2*a5/27 - 4*a0*a1*a2*a3**2*a6/9 + a0*a1*a2*a3**2/3 + 29*a0*a1*a2*a3*a4*a5/81 - 4*a0*a1*a2*a3*a4*a6/9 + a0*a1*a2*a3*a4/3 + 2*a0*a1*a2*a3*a5**2/27 - 4*a0*a1*a2*a3*a5*a6/3 + a0*a1*a2*a3*a5/18 - 16*a0*a1*a2*a4**3/243 + 11*a0*a1*a2*a4**2*a5/81 - 5*a0*a1*a2*a4**2*a6/9 + 8*a0*a1*a2*a4**2/27 + a0*a1*a2*a4*a5**2/2 + 10*a0*a1*a3*a4*a6**2/27 - 7*a0*a1*a3*a4*a6/81 - 2*a0*a1*a3*a4/81 + 11*a0*a1*a3*a5**2*a6/27 - 19*a0*a1*a3*a5**2/162 + 2*a0*a1*a3*a5*a6**2 - 2*a0*a1*a3*a5*a6/9 - 2*a0*a1*a3*a5/27 + 6*a0*a1*a3*a6**3 - 3*a0*a1*a3*a6**2 + a0*a1*a3*a6/6 + a0*a1*a3/18 - 32*a0*a1*a4**2*a5*a6/243 + 2*a0*a1*a4**2*a5/81 - 8*a0*a1*a4**2*a6**2/27 + 2*a0*a1*a4**2*a6/81 - a0*a1*a4**2/81 + a0*a1*a4*a5**2*a6/81 - a0*a1*a4*a5**2/18 - 14*a0*a1*a4*a5*a6**2/9 + 31*a0*a1*a4*a5*a6/54 - 5*a0*a1*a4*a5/108 + a0*a1*a5**3*a6/2 - 5*a0*a1*a5**3/36 + 2*a0*a2**3*a3**2/3 + 2*a0*a2**3*a3*a4/3 - 2*a0*a2**3*a3*a5 + 4*a0*a2**3*a4**2/3 + 22*a0*a2**2*a3*a4*a6/27 - 10*a0*a2**2*a3*a4/81 + 14*a0*a2**2*a3*a5**2/27 + 10*a0*a2**2*a3*a5*a6/3 - 25*a0*a2**2*a3*a5/27 - 9*a0*a2**2*a3*a6**2 + 31*a0*a2**2*a3*a6/12 - 5*a0*a2**2*a3/18 - 38*a0*a2**2*a4**2*a5/243 - 14*a0*a2**2*a4**2*a6/27 + 7*a0*a2**2*a4**2/27 + 10*a0*a2**2*a4*a5**2/81 + 31*a0*a2**2*a4*a5*a6/9 - 31*a0*a2**2*a4*a5/54 + 59*a0*a2*a3*a5*a6**2/27 - 85*a0*a2*a3*a5*a6/162 + 11*a0*a2*a3*a5/162 + 10*a0*a2*a3*a6**3 - 41*a0*a2*a3*a6**2/6 + 7*a0*a2*a3*a6/4 - 17*a0*a2*a3/108 + 20*a0*a2*a4**2*a6**2/81 - 61*a0*a2*a4**2*a6/243 + 4*a0*a2*a4**2/243 - 76*a0*a2*a4*a5**2*a6/243 + 2*a0*a2*a4*a5**2/27 - 17*a0*a2*a4*a5*a6**2/27 + 5*a0*a2*a4*a5*a6/9 - 11*a0*a2*a4*a5/81 + 7*a0*a2*a4*a6**3/3 - 8*a0*a2*a4*a6**2/3 + 25*a0*a2*a4*a6/54 - a0*a2*a4/54 + 8*a0*a2*a5**4/243 + 14*a0*a2*a5**3*a6/81 - 7*a0*a2*a5**3/81 + 31*a0*a2*a5**2*a6**2/18 - 41*a0*a2*a5**2*a6/108 + a0*a2*a5**2/36 + 44*a0*a3*a6**3/27 - 73*a0*a3*a6**2/81 + 23*a0*a3*a6/162 - a0*a3/162 + 2*a0*a4*a5*a6**3/9 - 103*a0*a4*a5*a6**2/243 + 26*a0*a4*a5*a6/243 - a0*a4*a5/162 + 2*a0*a4*a6**4/3 + 8*a0*a4*a6**3/27 - 17*a0*a4*a6**2/162 - a0*a4*a6/162 - 4*a0*a5**3*a6**2/81 + 31*a0*a5**3*a6/486 - a0*a5**3/243 - 29*a0*a5**2*a6**2/162 - a0*a5**2*a6/36 + 2*a0*a5*a6**4 - 13*a0*a5*a6**3/9 + 5*a0*a5*a6**2/36 + 5*a0*a5*a6/216 - a1**3*a3**2/9 - 2*a1**3*a3*a4*a5/9 - a1**3*a3*a4/9 - 2*a1**3*a3*a5**2/9 - a1**3*a3*a5*a6 + 4*a1**3*a4**3/81 + 2*a1**3*a4**2*a6/3 - a1**3*a4**2/9 - 2*a1**3*a4*a5**2/9 - 2*a1**2*a2**2*a3**2/9 - 2*a1**2*a2**2*a3*a4/9 + 13*a1**2*a2**2*a3*a5/6 - a1**2*a2**2*a4**2 - 28*a1**2*a2*a3*a4*a6/27 + 4*a1**2*a2*a3*a4/27 - 4*a1**2*a2*a3*a5**2/9 - 13*a1**2*a2*a3*a5*a6/3 + 7*a1**2*a2*a3*a5/6 - 12*a1**2*a2*a3*a6**2 + 3*a1**2*a2*a3*a6 + a1**2*a2*a3/4 + 14*a1**2*a2*a4**2*a5/81 + 14*a1**2*a2*a4**2*a6/27 - 8*a1**2*a2*a4**2/27 + a1**2*a2*a4*a5**2/27 + 4*a1**2*a2*a4*a5*a6/9 + a1**2*a2*a4*a5/9 - 2*a1**2*a2*a5**3/9 + 4*a1**2*a3*a5*a6**2/9 - 22*a1**2*a3*a5*a6/27 + 2*a1**2*a3*a5/27 + a1**2*a3*a6**2 - a1**2*a3*a6/2 + a1**2*a3/18 - 8*a1**2*a4**2*a6**2/27 + 8*a1**2*a4**2*a6/27 - a1**2*a4**2/27 + 2*a1**2*a4*a5**2*a6/27 - 2*a1**2*a4*a5**2/81 - 7*a1**2*a4*a5*a6/27 - 4*a1**2*a4*a6**3 + 3*a1**2*a4*a6**2 - 2*a1**2*a4*a6/3 + a1**2*a4/18 - a1**2*a5**4/81 - a1**2*a5**3*a6/27 - a1**2*a5**3/54 + a1**2*a5**2*a6**2 - 5*a1**2*a5**2*a6/6 + a1**2*a5**2/12 + 8*a1*a2**3*a3*a4/27 + 8*a1*a2**3*a3*a5/9 + 19*a1*a2**3*a3*a6 - 31*a1*a2**3*a3/12 - 4*a1*a2**3*a4*a5/3 - 20*a1*a2**2*a3*a5*a6/9 + 29*a1*a2**2*a3*a5/54 - 10*a1*a2**2*a3*a6**2 + 35*a1*a2**2*a3*a6/6 - 35*a1*a2**2*a3/36 + 4*a1*a2**2*a4**2*a6/27 - 5*a1*a2**2*a4**2/81 + 4*a1*a2**2*a4*a5**2/27 + 2*a1*a2**2*a4*a5*a6/9 - 11*a1*a2**2*a4*a5/27 + 6*a1*a2**2*a4*a6**2 - 17*a1*a2**2*a4*a6/6 + 19*a1*a2**2*a4/36 + 4*a1*a2**2*a5**3/27 - 4*a1*a2**2*a5**2*a6/3 + 3*a1*a2**2*a5**2/4 + 4*a1*a2*a3*a6**3/9 - 92*a1*a2*a3*a6**2/27 + 47*a1*a2*a3*a6/54 - a1*a2*a3/108 - 14*a1*a2*a4*a5*a6**2/81 + 25*a1*a2*a4*a5*a6/81 - 5*a1*a2*a4*a5/162 - 20*a1*a2*a4*a6**3/9 + 40*a1*a2*a4*a6**2/27 - 8*a1*a2*a4*a6/9 + 4*a1*a2*a4/27 + 2*a1*a2*a5**3*a6/81 - a1*a2*a5**3/162 + 16*a1*a2*a5**2*a6**2/27 - 47*a1*a2*a5**2*a6/54 + 13*a1*a2*a5**2/108 + 13*a1*a2*a5*a6**3/3 - 23*a1*a2*a5*a6**2/6 + 13*a1*a2*a5*a6/36 + a1*a2*a5/18 + 4*a1*a4*a6**4/9 - 34*a1*a4*a6**3/27 + 38*a1*a4*a6**2/81 - 2*a1*a4*a6/27 + a1*a4/162 - 4*a1*a5**2*a6**3/27 + 29*a1*a5**2*a6**2/81 - 2*a1*a5**2*a6/27 + a1*a5**2/162 - 5*a1*a5*a6**3/9 + a1*a5*a6**2/54 + a1*a5*a6/54 + 6*a1*a6**5 - 8*a1*a6**4 + 7*a1*a6**3/3 - a1*a6**2/12 - a1*a6/36 - 6*a2**5*a3 + 7*a2**4*a3*a5/9 + 4*a2**4*a3*a6 - 2*a2**4*a3 + a2**4*a4*a5/3 - 3*a2**4*a4*a6 + 5*a2**4*a4/4 - a2**4*a5**2/3 - 2*a2**3*a3*a6**2/9 + 14*a2**3*a3*a6/9 + a2**3*a3/36 + 20*a2**3*a4*a5*a6/81 - 11*a2**3*a4*a5/162 + 16*a2**3*a4*a6**2/9 - 29*a2**3*a4*a6/18 + 4*a2**3*a4/9 + 5*a2**3*a5**3/81 + 17*a2**3*a5**2*a6/27 - 17*a2**3*a5**2/54 - 9*a2**3*a5*a6**2/2 + 137*a2**3*a5*a6/36 - 5*a2**3*a5/72 - 4*a2**2*a4*a6**3/27 + 70*a2**2*a4*a6**2/81 - 11*a2**2*a4*a6/81 + a2**2*a4/54 + a2**2*a5**2*a6**2/3 - 7*a2**2*a5**2*a6/162 + a2**2*a5**2/162 + 23*a2**2*a5*a6**3/9 - 101*a2**2*a5*a6**2/27 + 137*a2**2*a5*a6/108 - 2*a2**2*a5/27 - 5*a2**2*a6**4 + 41*a2**2*a6**3/6 - 65*a2**2*a6**2/36 + 11*a2**2*a6/72 + 2*a2*a5*a6**4/9 + 8*a2*a5*a6**3/9 - 67*a2*a5*a6**2/162 + a2*a5*a6/18 - a2*a5/324 + 2*a2*a6**5 - 14*a2*a6**4/3 + 53*a2*a6**3/18 - 41*a2*a6**2/54 + 2*a2*a6/27 + 10*a6**5/9 - a6**4 + 55*a6**3/162 - 17*a6**2/324 + a6/324",
          "a0**2*a1*a3*a5**2/6 - a0**2*a1*a4**2*a5/18 - 2*a0**2*a2*a3**2*a5/27 + 4*a0**2*a2*a3*a4**2/243 - 2*a0**2*a2*a3*a4*a5/27 - 2*a0**2*a2*a3*a5**2/9 + 3*a0**2*a2*a3*a5*a6/2 + a0**2*a2*a3*a5/9 + 4*a0**2*a2*a4**3/243 + 5*a0**2*a2*a4**2*a5/81 - a0**2*a2*a4**2*a6/9 - 7*a0**2*a2*a4**2/54 - 4*a0**2*a2*a4*a5**2/27 + 8*a0**2*a3**2*a6/81 - 4*a0**2*a3**2/243 - 2*a0**2*a3*a4*a5*a6/243 - 17*a0**2*a3*a4*a5/729 + 8*a0**2*a3*a4*a6/81 - 4*a0**2*a3*a4/243 - 2*a0**2*a3*a5**3/81 - 2*a0**2*a3*a5**2*a6/9 - 7*a0**2*a3*a5**2/243 - 4*a0**2*a3*a5*a6**2/3 + 14*a0**2*a3*a5*a6/27 - a0**2*a3*a5/54 + 7*a0**2*a3*a6**2/6 - 13*a0**2*a3*a6/36 + a0**2*a3/36 + 8*a0**2*a4**3*a6/729 + 8*a0**2*a4**3/2187 + 10*a0**2*a4**2*a5**2/2187 + 8*a0**2*a4**2*a5*a6/81 - 2*a0**2*a4**2*a5/729 + 4*a0**2*a4**2*a6**2/27 - 4*a0**2*a4**2/243 - 8*a0**2*a4*a5**3/729 + 19*a0**2*a4*a5**2*a6/81 - 29*a0**2*a4*a5**2/486 + 11*a0**2*a4*a5*a6**2/18 - 49*a0**2*a4*a5*a6/108 + a0**2*a4*a5/18 - 4*a0**2*a5**4/81 - 2*a0**2*a5**3*a6/9 + 2*a0**2*a5**3/27 + 2*a0*a1**2*a3**2*a5/27 - 4*a0*a1**2*a3*a4**2/243 + 2*a0*a1**2*a3*a4*a5/27 + a0*a1**2*a3*a5**2/9 - a0*a1**2*a3*a5*a6/2 - a0*a1**2*a3*a5/2 - 4*a0*a1**2*a4**3/243 - 2*a0*a1**2*a4**2*a5/81 + 2*a0*a1**2*a4**2*a6/9 + a0*a1**2*a4**2/6 - 8*a0*a1*a2**2*a3*a5/3 + 4*a0*a1*a2**2*a4**2/9 + 8*a0*a1*a2*a3**2*a6/27 - 2*a0*a1*a2*a3**2/9 - 58*a0*a1*a2*a3*a4*a5/243 + 8*a0*a1*a2*a3*a4*a6/27 - 2*a0*a1*a2*a3*a4/9 - 4*a0*a1*a2*a3*a5**2/81 + 8*a0*a1*a2*a3*a5*a6/9 - a0*a1*a2*a3*a5/27 - 7*a0*a1*a2*a3*a6**2 + 5*a0*a1*a2*a3*a6/4 - a0*a1*a2*a3/3 + 32*a0*a1*a2*a4**3/729 - 22*a0*a1*a2*a4**2*a5/243 + 10*a0*a1*a2*a4**2*a6/27 - 16*a0*a1*a2*a4**2/81 - a0*a1*a2*a4*a5**2/3 + 13*a0*a1*a2*a4*a5*a6/18 - 4*a0*a1*a2*a5**3/9 - 20*a0*a1*a3*a4*a6**2/81 + 14*a0*a1*a3*a4*a6/243 + 4*a0*a1*a3*a4/243 - 22*a0*a1*a3*a5**2*a6/81 + 19*a0*a1*a3*a5**2/243 - 4*a0*a1*a3*a5*a6**2/3 + 4*a0*a1*a3*a5*a6/27 + 4*a0*a1*a3*a5/81 - 4*a0*a1*a3*a6**3 + 2*a0*a1*a3*a6**2 - a0*a1*a3*a6/9 - a0*a1*a3/27 + 64*a0*a1*a4**2*a5*a6/729 - 4*a0*a1*a4**2*a5/243 + 16*a0*a1*a4**2*a6**2/81 - 4*a0*a1*a4**2*a6/243 + 2*a0*a1*a4**2/243 - 2*a0*a1*a4*a5**2*a6/243 + a0*a1*a4*a5**2/27 + 28*a0*a1*a4*a5*a6**2/27 - 31*a0*a1*a4*a5*a6/81 + 5*a0*a1*a4*a5/162 - 2*a0*a1*a4*a6**3/3 - 4*a0*a1*a4*a6**2/9 + 2*a0*a1*a4*a6/9 - a0*a1*a4/36 - a0*a1*a5**3*a6/3 + 5*a0*a1*a5**3/54 - 5*a0*a1*a5**2*a6**2/6 + 7*a0*a1*a5**2*a6/9 - a0*a1*a5**2/6 - 4*a0*a2**3*a3**2/9 - 4*a0*a2**3*a3*a4/9 + 4*a0*a2**3*a3*a5/3 + 3*a0*a2**3*a3*a6 - 2*a0*a2**3*a3/3 - 8*a0*a2**3*a4**2/9 - 7*a0*a2**3*a4*a5/9 - 44*a0*a2**2*a3*a4*a6/81 + 20*a0*a2**2*a3*a4/243 - 28*a0*a2**2*a3*a5**2/81 - 20*a0*a2**2*a3*a5*a6/9 + 50*a0*a2**2*a3*a5/81 + 6*a0*a2**2*a3*a6**2 - 31*a0*a2**2*a3*a6/18 + 5*a0*a2**2*a3/27 + 76*a0*a2**2*a4**2*a5/729 + 28*a0*a2**2*a4**2*a6/81 - 14*a0*a2**2*a4**2/81 - 20*a0*a2**2*a4*a5**2/243 - 62*a0*a2**2*a4*a5*a6/27 + 31*a0*a2**2*a4*a5/81 + 5*a0*a2**2*a4*a6**2/3 - 11*a0*a2**2*a4*a6/9 + a0*a2**2*a4/18 - 17*a0*a2**2*a5**2*a6/9 + a0*a2**2*a5**2/2 - 118*a0*a2*a3*a5*a6**2/81 + 85*a0*a2*a3*a5*a6/243 - 11*a0*a2*a3*a5/243 - 20*a0*a2*a3*a6**3/3 + 41*a0*a2*a3*a6**2/9 - 7*a0*a2*a3*a6/6 + 17*a0*a2*a3/162 - 40*a0*a2*a4**2*a6**2/243 + 122*a0*a2*a4**2*a6/729 - 8*a0*a2*a4**2/729 + 152*a0*a2*a4*a5**2*a6/729 - 4*a0*a2*a4*a5**2/81 + 34*a0*a2*a4*a5*a6**2/81 - 10*a0*a2*a4*a5*a6/27 + 22*a0*a2*a4*a5/243 - 14*a0*a2*a4*a6**3/9 + 16*a0*a2*a4*a6**2/9 - 25*a0*a2*a4*a6/81 + a0*a2*a4/81 - 16*a0*a2*a5**4/729 - 28*a0*a2*a5**3*a6/243 + 14*a0*a2*a5**3/243 - 31*a0*a2*a5**2*a6**2/27 + 41*a0*a2*a5**2*a6/162 - a0*a2*a5**2/54 - 17*a0*a2*a5*a6**3/6 + 25*a0*a2*a5*a6**2/18 - 17*a0*a2*a5*a6/36 + a0*a2*a5/18 - 88*a0*a3*a6**3/81 + 146*a0*a3*a6**2/243 - 23*a0*a3*a6/243 + a0*a3/243 - 4*a0*a4*a5*a6**3/27 + 206*a0*a4*a5*a6**2/729 - 52*a0*a4*a5*a6/729 + a0*a4*a5/243 - 4*a0*a4*a6**4/9 - 16*a0*a4*a6**3/81 + 17*a0*a4*a6**2/243 + a0*a4*a6/243 + 8*a0*a5**3*a6**2/243 - 31*a0*a5**3*a6/729 + 2*a0*a5**3/729 + 29*a0*a5**2*a6**2/243 + a0*a5**2*a6/54 - 4*a0*a5*a6**4/3 + 26*a0*a5*a6**3/27 - 5*a0*a5*a6**2/54 - 5*a0*a5*a6/324 - 11*a0*a6**4/6 + 14*a0*a6**3/9 - 11*a0*a6**2/24 + a0*a6/24 + 3*a1**3*a2*a3*a5/2 - a1**3*a2*a4**2/3 + 2*a1**3*a3**2/27 + 4*a1**3*a3*a4*a5/27 + 2*a1**3*a3*a4/27 + 4*a1**3*a3*a5**2/27 + 2*a1**3*a3*a5*a6/3 - a1**3*a3*a6 + a1**3*a3/2 - 8*a1**3*a4**3/243 - 4*a1**3*a4**2*a6/9 + 2*a1**3*a4**2/27 + 4*a1**3*a4*a5**2/27 + a1**3*a4*a5/6 + a1**3*a5**3/6 + 4*a1**2*a2**2*a3**2/27 + 4*a1**2*a2**2*a3*a4/27 - 13*a1**2*a2**2*a3*a5/9 + 4*a1**2*a2**2*a3*a6 + a1**2*a2**2*a3/4 + 2*a1**2*a2**2*a4**2/3 + 56*a1**2*a2*a3*a4*a6/81 - 8*a1**2*a2*a3*a4/81 + 8*a1**2*a2*a3*a5**2/27 + 26*a1**2*a2*a3*a5*a6/9 - 7*a1**2*a2*a3*a5/9 + 8*a1**2*a2*a3*a6**2 - 2*a1**2*a2*a3*a6 - a1**2*a2*a3/6 - 28*a1**2*a2*a4**2*a5/243 - 28*a1**2*a2*a4**2*a6/81 + 16*a1**2*a2*a4**2/81 - 2*a1**2*a2*a4*a5**2/81 - 8*a1**2*a2*a4*a5*a6/27 - 2*a1**2*a2*a4*a5/27 + 2*a1**2*a2*a4*a6**2/3 + a1**2*a2*a4*a6/2 + 4*a1**2*a2*a5**3/27 + 7*a1**2*a2*a5**2*a6/6 - a1**2*a2*a5**2/12 - 8*a1**2*a3*a5*a6**2/27 + 44*a1**2*a3*a5*a6/81 - 4*a1**2*a3*a5/81 - 2*a1**2*a3*a6**2/3 + a1**2*a3*a6/3 - a1**2*a3/27 + 16*a1**2*a4**2*a6**2/81 - 16*a1**2*a4**2*a6/81 + 2*a1**2*a4**2/81 - 4*a1**2*a4*a5**2*a6/81 + 4*a1**2*a4*a5**2/243 + 14*a1**2*a4*a5*a6/81 + 8*a1**2*a4*a6**3/3 - 2*a1**2*a4*a6**2 + 4*a1**2*a4*a6/9 - a1**2*a4/27 + 2*a1**2*a5**4/243 + 2*a1**2*a5**3*a6/81 + a1**2*a5**3/81 - 2*a1**2*a5**2*a6**2/3 + 5*a1**2*a5**2*a6/9 - a1**2*a5**2/18 + 3*a1**2*a5*a6**2/2 - 11*a1**2*a5*a6/12 + a1**2*a5/12 - 2*a1*a2**4*a3 - 16*a1*a2**3*a3*a4/81 - 16*a1*a2**3*a3*a5/27 - 38*a1*a2**3*a3*a6/3 + 31*a1*a2**3*a3/18 + 8*a1*a2**3*a4*a5/9 - a1*a2**3*a4*a6 + 5*a1*a2**3*a4/12 - a1*a2**3*a5**2/6 + 40*a1*a2**2*a3*a5*a6/27 - 29*a1*a2**2*a3*a5/81 + 20*a1*a2**2*a3*a6**2/3 - 35*a1*a2**2*a3*a6/9 + 35*a1*a2**2*a3/54 - 8*a1*a2**2*a4**2*a6/81 + 10*a1*a2**2*a4**2/243 - 8*a1*a2**2*a4*a5**2/81 - 4*a1*a2**2*a4*a5*a6/27 + 22*a1*a2**2*a4*a5/81 - 4*a1*a2**2*a4*a6**2 + 17*a1*a2**2*a4*a6/9 - 19*a1*a2**2*a4/54 - 8*a1*a2**2*a5**3/81 + 8*a1*a2**2*a5**2*a6/9 - a1*a2**2*a5**2/2 + 13*a1*a2**2*a5*a6**2/6 - 7*a1*a2**2*a5*a6/12 + a1*a2**2*a5/4 - 8*a1*a2*a3*a6**3/27 + 184*a1*a2*a3*a6**2/81 - 47*a1*a2*a3*a6/81 + a1*a2*a3/162 + 28*a1*a2*a4*a5*a6**2/243 - 50*a1*a2*a4*a5*a6/243 + 5*a1*a2*a4*a5/243 + 40*a1*a2*a4*a6**3/27 - 80*a1*a2*a4*a6**2/81 + 16*a1*a2*a4*a6/27 - 8*a1*a2*a4/81 - 4*a1*a2*a5**3*a6/243 + a1*a2*a5**3/243 - 32*a1*a2*a5**2*a6**2/81 + 47*a1*a2*a5**2*a6/81 - 13*a1*a2*a5**2/162 - 26*a1*a2*a5*a6**3/9 + 23*a1*a2*a5*a6**2/9 - 13*a1*a2*a5*a6/54 - a1*a2*a5/27 + a1*a2*a6**4 + 17*a1*a2*a6**3/6 - 3*a1*a2*a6**2 + 5*a1*a2*a6/12 + a1*a2/24 - 8*a1*a4*a6**4/27 + 68*a1*a4*a6**3/81 - 76*a1*a4*a6**2/243 + 4*a1*a4*a6/81 - a1*a4/243 + 8*a1*a5**2*a6**3/81 - 58*a1*a5**2*a6**2/243 + 4*a1*a5**2*a6/81 - a1*a5**2/243 + 10*a1*a5*a6**3/27 - a1*a5*a6**2/81 - a1*a5*a6/81 - 4*a1*a6**5 + 16*a1*a6**4/3 - 14*a1*a6**3/9 + a1*a6**2/18 + a1*a6/54 + 4*a2**5*a3 - 14*a2**4*a3*a5/27 - 8*a2**4*a3*a6/3 + 4*a2**4*a3/3 - 2*a2**4*a4*a5/9 + 2*a2**4*a4*a6 - 5*a2**4*a4/6 + 2*a2**4*a5**2/9 - 7*a2**4*a5*a6/6 + a2**4*a5/3 + 4*a2**3*a3*a6**2/27 - 28*a2**3*a3*a6/27 - a2**3*a3/54 - 40*a2**3*a4*a5*a6/243 + 11*a2**3*a4*a5/243 - 32*a2**3*a4*a6**2/27 + 29*a2**3*a4*a6/27 - 8*a2**3*a4/27 - 10*a2**3*a5**3/243 - 34*a2**3*a5**2*a6/81 + 17*a2**3*a5**2/81 + 3*a2**3*a5*a6**2 - 137*a2**3*a5*a6/54 + 5*a2**3*a5/108 - a2**3*a6**3 - a2**3*a6**2/3 + 19*a2**3*a6/24 + a2**3/8 + 8*a2**2*a4*a6**3/81 - 140*a2**2*a4*a6**2/243 + 22*a2**2*a4*a6/243 - a2**2*a4/81 - 2*a2**2*a5**2*a6**2/9 + 7*a2**2*a5**2*a6/243 - a2**2*a5**2/243 - 46*a2**2*a5*a6**3/27 + 202*a2**2*a5*a6**2/81 - 137*a2**2*a5*a6/162 + 4*a2**2*a5/81 + 10*a2**2*a6**4/3 - 41*a2**2*a6**3/9 + 65*a2**2*a6**2/54 - 11*a2**2*a6/108 - 4*a2*a5*a6**4/27 - 16*a2*a5*a6**3/27 + 67*a2*a5*a6**2/243 - a2*a5*a6/27 + a2*a5/486 - 4*a2*a6**5/3 + 28*a2*a6**4/9 - 53*a2*a6**3/27 + 41*a2*a6**2/81 - 4*a2*a6/81 - 20*a6**5/27 + 2*a6**4/3 - 55*a6**3/243 + 17*a6**2/486 - a6/486",
          "a0**3*a3*a5**2/6 - a0**3*a4**2*a5/18 - a0**2*a1*a3*a5**2/9 + a0**2*a1*a3*a5*a6 - 7*a0**2*a1*a3*a5/18 + a0**2*a1*a4**2*a5/27 + a0**2*a1*a4**2*a6/9 + a0**2*a1*a4**2/27 - 4*a0**2*a1*a4*a5**2/27 - 7*a0**2*a2**2*a3*a5/2 + 13*a0**2*a2**2*a4**2/9 + 4*a0**2*a2*a3**2*a5/81 - 8*a0**2*a2*a3*a4**2/729 + 4*a0**2*a2*a3*a4*a5/81 + 4*a0**2*a2*a3*a5**2/27 - a0**2*a2*a3*a5*a6 - 2*a0**2*a2*a3*a5/27 - 15*a0**2*a2*a3*a6**2 + 77*a0**2*a2*a3*a6/12 - 25*a0**2*a2*a3/36 - 8*a0**2*a2*a4**3/729 - 10*a0**2*a2*a4**2*a5/243 + 2*a0**2*a2*a4**2*a6/27 + 7*a0**2*a2*a4**2/81 + 8*a0**2*a2*a4*a5**2/81 + 77*a0**2*a2*a4*a5*a6/18 - 91*a0**2*a2*a4*a5/108 - 2*a0**2*a2*a5**3/3 - 16*a0**2*a3**2*a6/243 + 8*a0**2*a3**2/729 + 4*a0**2*a3*a4*a5*a6/729 + 34*a0**2*a3*a4*a5/2187 - 16*a0**2*a3*a4*a6/243 + 8*a0**2*a3*a4/729 + 4*a0**2*a3*a5**3/243 + 4*a0**2*a3*a5**2*a6/27 + 14*a0**2*a3*a5**2/729 + 8*a0**2*a3*a5*a6**2/9 - 28*a0**2*a3*a5*a6/81 + a0**2*a3*a5/81 - 7*a0**2*a3*a6**2/9 + 13*a0**2*a3*a6/54 - a0**2*a3/54 - 16*a0**2*a4**3*a6/2187 - 16*a0**2*a4**3/6561 - 20*a0**2*a4**2*a5**2/6561 - 16*a0**2*a4**2*a5*a6/243 + 4*a0**2*a4**2*a5/2187 - 8*a0**2*a4**2*a6**2/81 + 8*a0**2*a4**2/729 + 16*a0**2*a4*a5**3/2187 - 38*a0**2*a4*a5**2*a6/243 + 29*a0**2*a4*a5**2/729 - 11*a0**2*a4*a5*a6**2/27 + 49*a0**2*a4*a5*a6/162 - a0**2*a4*a5/27 - a0**2*a4*a6**3 - a0**2*a4*a6**2/6 - a0**2*a4*a6/9 + a0**2*a4/54 + 8*a0**2*a5**4/243 + 4*a0**2*a5**3*a6/27 - 4*a0**2*a5**3/81 + 2*a0**2*a5**2*a6**2/3 + a0**2*a5**2*a6/36 + a0**2*a5**2/54 + 10*a0*a1**2*a2*a3*a5/3 - 2*a0*a1**2*a2*a4**2 - 4*a0*a1**2*a3**2*a5/81 + 8*a0*a1**2*a3*a4**2/729 - 4*a0*a1**2*a3*a4*a5/81 - 2*a0*a1**2*a3*a5**2/27 + a0*a1**2*a3*a5*a6/3 + a0*a1**2*a3*a5/3 + 6*a0*a1**2*a3*a6**2 - 7*a0*a1**2*a3*a6/2 + a0*a1**2*a3/2 + 8*a0*a1**2*a4**3/729 + 4*a0*a1**2*a4**2*a5/243 - 4*a0*a1**2*a4**2*a6/27 - a0*a1**2*a4**2/9 - 19*a0*a1**2*a4*a5*a6/9 + 5*a0*a1**2*a4*a5/9 + a0*a1**2*a5**3/6 + 16*a0*a1*a2**2*a3*a5/9 + 23*a0*a1*a2**2*a3*a6 - 59*a0*a1*a2**2*a3/12 - 8*a0*a1*a2**2*a4**2/27 - 65*a0*a1*a2**2*a4*a5/18 - 16*a0*a1*a2*a3**2*a6/81 + 4*a0*a1*a2*a3**2/27 + 116*a0*a1*a2*a3*a4*a5/729 - 16*a0*a1*a2*a3*a4*a6/81 + 4*a0*a1*a2*a3*a4/27 + 8*a0*a1*a2*a3*a5**2/243 - 16*a0*a1*a2*a3*a5*a6/27 + 2*a0*a1*a2*a3*a5/81 + 14*a0*a1*a2*a3*a6**2/3 - 5*a0*a1*a2*a3*a6/6 + 2*a0*a1*a2*a3/9 - 64*a0*a1*a2*a4**3/2187 + 44*a0*a1*a2*a4**2*a5/729 - 20*a0*a1*a2*a4**2*a6/81 + 32*a0*a1*a2*a4**2/243 + 2*a0*a1*a2*a4*a5**2/9 - 13*a0*a1*a2*a4*a5*a6/27 + 23*a0*a1*a2*a4*a6**2/3 - 4*a0*a1*a2*a4*a6 + 11*a0*a1*a2*a4/12 + 8*a0*a1*a2*a5**3/27 - 43*a0*a1*a2*a5**2*a6/18 + 11*a0*a1*a2*a5**2/9 + 40*a0*a1*a3*a4*a6**2/243 - 28*a0*a1*a3*a4*a6/729 - 8*a0*a1*a3*a4/729 + 44*a0*a1*a3*a5**2*a6/243 - 38*a0*a1*a3*a5**2/729 + 8*a0*a1*a3*a5*a6**2/9 - 8*a0*a1*a3*a5*a6/81 - 8*a0*a1*a3*a5/243 + 8*a0*a1*a3*a6**3/3 - 4*a0*a1*a3*a6**2/3 + 2*a0*a1*a3*a6/27 + 2*a0*a1*a3/81 - 128*a0*a1*a4**2*a5*a6/2187 + 8*a0*a1*a4**2*a5/729 - 32*a0*a1*a4**2*a6**2/243 + 8*a0*a1*a4**2*a6/729 - 4*a0*a1*a4**2/729 + 4*a0*a1*a4*a5**2*a6/729 - 2*a0*a1*a4*a5**2/81 - 56*a0*a1*a4*a5*a6**2/81 + 62*a0*a1*a4*a5*a6/243 - 5*a0*a1*a4*a5/243 + 4*a0*a1*a4*a6**3/9 + 8*a0*a1*a4*a6**2/27 - 4*a0*a1*a4*a6/27 + a0*a1*a4/54 + 2*a0*a1*a5**3*a6/9 - 5*a0*a1*a5**3/81 + 5*a0*a1*a5**2*a6**2/9 - 14*a0*a1*a5**2*a6/27 + a0*a1*a5**2/9 + 4*a0*a1*a5*a6**3 - 31*a0*a1*a5*a6**2/18 - 5*a0*a1*a5*a6/36 - a0*a1*a5/18 - 9*a0*a2**4*a3 + 8*a0*a2**3*a3**2/27 + 8*a0*a2**3*a3*a4/27 - 8*a0*a2**3*a3*a5/9 - 2*a0*a2**3*a3*a6 + 4*a0*a2**3*a3/9 + 16*a0*a2**3*a4**2/27 + 14*a0*a2**3*a4*a5/27 - 14*a0*a2**3*a4*a6/3 + 25*a0*a2**3*a4/12 - 13*a0*a2**3*a5**2/6 + 88*a0*a2**2*a3*a4*a6/243 - 40*a0*a2**2*a3*a4/729 + 56*a0*a2**2*a3*a5**2/243 + 40*a0*a2**2*a3*a5*a6/27 - 100*a0*a2**2*a3*a5/243 - 4*a0*a2**2*a3*a6**2 + 31*a0*a2**2*a3*a6/27 - 10*a0*a2**2*a3/81 - 152*a0*a2**2*a4**2*a5/2187 - 56*a0*a2**2*a4**2*a6/243 + 28*a0*a2**2*a4**2/243 + 40*a0*a2**2*a4*a5**2/729 + 124*a0*a2**2*a4*a5*a6/81 - 62*a0*a2**2*a4*a5/243 - 10*a0*a2**2*a4*a6**2/9 + 22*a0*a2**2*a4*a6/27 - a0*a2**2*a4/27 + 34*a0*a2**2*a5**2*a6/27 - a0*a2**2*a5**2/3 - 28*a0*a2**2*a5*a6**2/3 + 241*a0*a2**2*a5*a6/36 - 13*a0*a2**2*a5/18 + 236*a0*a2*a3*a5*a6**2/243 - 170*a0*a2*a3*a5*a6/729 + 22*a0*a2*a3*a5/729 + 40*a0*a2*a3*a6**3/9 - 82*a0*a2*a3*a6**2/27 + 7*a0*a2*a3*a6/9 - 17*a0*a2*a3/243 + 80*a0*a2*a4**2*a6**2/729 - 244*a0*a2*a4**2*a6/2187 + 16*a0*a2*a4**2/2187 - 304*a0*a2*a4*a5**2*a6/2187 + 8*a0*a2*a4*a5**2/243 - 68*a0*a2*a4*a5*a6**2/243 + 20*a0*a2*a4*a5*a6/81 - 44*a0*a2*a4*a5/729 + 28*a0*a2*a4*a6**3/27 - 32*a0*a2*a4*a6**2/27 + 50*a0*a2*a4*a6/243 - 2*a0*a2*a4/243 + 32*a0*a2*a5**4/2187 + 56*a0*a2*a5**3*a6/729 - 28*a0*a2*a5**3/729 + 62*a0*a2*a5**2*a6**2/81 - 41*a0*a2*a5**2*a6/243 + a0*a2*a5**2/81 + 17*a0*a2*a5*a6**3/9 - 25*a0*a2*a5*a6**2/27 + 17*a0*a2*a5*a6/54 - a0*a2*a5/27 - 3*a0*a2*a6**4 + 37*a0*a2*a6**3/6 - 31*a0*a2*a6**2/9 + 13*a0*a2*a6/24 - a0*a2/72 + 176*a0*a3*a6**3/243 - 292*a0*a3*a6**2/729 + 46*a0*a3*a6/729 - 2*a0*a3/729 + 8*a0*a4*a5*a6**3/81 - 412*a0*a4*a5*a6**2/2187 + 104*a0*a4*a5*a6/2187 - 2*a0*a4*a5/729 + 8*a0*a4*a6**4/27 + 32*a0*a4*a6**3/243 - 34*a0*a4*a6**2/729 - 2*a0*a4*a6/729 - 16*a0*a5**3*a6**2/729 + 62*a0*a5**3*a6/2187 - 4*a0*a5**3/2187 - 58*a0*a5**2*a6**2/729 - a0*a5**2*a6/81 + 8*a0*a5*a6**4/9 - 52*a0*a5*a6**3/81 + 5*a0*a5*a6**2/81 + 5*a0*a5*a6/486 + 11*a0*a6**4/9 - 28*a0*a6**3/27 + 11*a0*a6**2/36 - a0*a6/36 - a1**4*a3*a5 + 2*a1**4*a4**2/3 - a1**3*a2*a3*a5 - 12*a1**3*a2*a3*a6 + 3*a1**3*a2*a3 + 2*a1**3*a2*a4**2/9 + 2*a1**3*a2*a4*a5 - 4*a1**3*a3**2/81 - 8*a1**3*a3*a4*a5/81 - 4*a1**3*a3*a4/81 - 8*a1**3*a3*a5**2/81 - 4*a1**3*a3*a5*a6/9 + 2*a1**3*a3*a6/3 - a1**3*a3/3 + 16*a1**3*a4**3/729 + 8*a1**3*a4**2*a6/27 - 4*a1**3*a4**2/81 - 8*a1**3*a4*a5**2/81 - a1**3*a4*a5/9 - 4*a1**3*a4*a6**2 + 7*a1**3*a4*a6/3 - a1**3*a4/2 - a1**3*a5**3/9 + a1**3*a5**2*a6/3 - a1**3*a5**2/3 + 5*a1**2*a2**3*a3 - 8*a1**2*a2**2*a3**2/81 - 8*a1**2*a2**2*a3*a4/81 + 26*a1**2*a2**2*a3*a5/27 - 8*a1**2*a2**2*a3*a6/3 - a1**2*a2**2*a3/6 - 4*a1**2*a2**2*a4**2/9 + 8*a1**2*a2**2*a4*a6/3 - a1**2*a2**2*a4 + 11*a1**2*a2**2*a5**2/6 - 112*a1**2*a2*a3*a4*a6/243 + 16*a1**2*a2*a3*a4/243 - 16*a1**2*a2*a3*a5**2/81 - 52*a1**2*a2*a3*a5*a6/27 + 14*a1**2*a2*a3*a5/27 - 16*a1**2*a2*a3*a6**2/3 + 4*a1**2*a2*a3*a6/3 + a1**2*a2*a3/9 + 56*a1**2*a2*a4**2*a5/729 + 56*a1**2*a2*a4**2*a6/243 - 32*a1**2*a2*a4**2/243 + 4*a1**2*a2*a4*a5**2/243 + 16*a1**2*a2*a4*a5*a6/81 + 4*a1**2*a2*a4*a5/81 - 4*a1**2*a2*a4*a6**2/9 - a1**2*a2*a4*a6/3 - 8*a1**2*a2*a5**3/81 - 7*a1**2*a2*a5**2*a6/9 + a1**2*a2*a5**2/18 - a1**2*a2*a5*a6**2/3 - 5*a1**2*a2*a5*a6/6 + a1**2*a2*a5/12 + 16*a1**2*a3*a5*a6**2/81 - 88*a1**2*a3*a5*a6/243 + 8*a1**2*a3*a5/243 + 4*a1**2*a3*a6**2/9 - 2*a1**2*a3*a6/9 + 2*a1**2*a3/81 - 32*a1**2*a4**2*a6**2/243 + 32*a1**2*a4**2*a6/243 - 4*a1**2*a4**2/243 + 8*a1**2*a4*a5**2*a6/243 - 8*a1**2*a4*a5**2/729 - 28*a1**2*a4*a5*a6/243 - 16*a1**2*a4*a6**3/9 + 4*a1**2*a4*a6**2/3 - 8*a1**2*a4*a6/27 + 2*a1**2*a4/81 - 4*a1**2*a5**4/729 - 4*a1**2*a5**3*a6/243 - 2*a1**2*a5**3/243 + 4*a1**2*a5**2*a6**2/9 - 10*a1**2*a5**2*a6/27 + a1**2*a5**2/27 - a1**2*a5*a6**2 + 11*a1**2*a5*a6/18 - a1**2*a5/18 + 6*a1**2*a6**4 - 7*a1**2*a6**3 + 11*a1**2*a6**2/6 - 5*a1**2*a6/12 + a1**2/12 + 4*a1*a2**4*a3/3 + 32*a1*a2**3*a3*a4/243 + 32*a1*a2**3*a3*a5/81 + 76*a1*a2**3*a3*a6/9 - 31*a1*a2**3*a3/27 - 16*a1*a2**3*a4*a5/27 + 2*a1*a2**3*a4*a6/3 - 5*a1*a2**3*a4/18 + a1*a2**3*a5**2/9 + 16*a1*a2**3*a5*a6/3 - 7*a1*a2**3*a5/6 - 80*a1*a2**2*a3*a5*a6/81 + 58*a1*a2**2*a3*a5/243 - 40*a1*a2**2*a3*a6**2/9 + 70*a1*a2**2*a3*a6/27 - 35*a1*a2**2*a3/81 + 16*a1*a2**2*a4**2*a6/243 - 20*a1*a2**2*a4**2/729 + 16*a1*a2**2*a4*a5**2/243 + 8*a1*a2**2*a4*a5*a6/81 - 44*a1*a2**2*a4*a5/243 + 8*a1*a2**2*a4*a6**2/3 - 34*a1*a2**2*a4*a6/27 + 19*a1*a2**2*a4/81 + 16*a1*a2**2*a5**3/243 - 16*a1*a2**2*a5**2*a6/27 + a1*a2**2*a5**2/3 - 13*a1*a2**2*a5*a6**2/9 + 7*a1*a2**2*a5*a6/18 - a1*a2**2*a5/6 - 4*a1*a2**2*a6**3 + 4*a1*a2**2*a6**2 - a1*a2**2*a6/12 + a1*a2**2/6 + 16*a1*a2*a3*a6**3/81 - 368*a1*a2*a3*a6**2/243 + 94*a1*a2*a3*a6/243 - a1*a2*a3/243 - 56*a1*a2*a4*a5*a6**2/729 + 100*a1*a2*a4*a5*a6/729 - 10*a1*a2*a4*a5/729 - 80*a1*a2*a4*a6**3/81 + 160*a1*a2*a4*a6**2/243 - 32*a1*a2*a4*a6/81 + 16*a1*a2*a4/243 + 8*a1*a2*a5**3*a6/729 - 2*a1*a2*a5**3/729 + 64*a1*a2*a5**2*a6**2/243 - 94*a1*a2*a5**2*a6/243 + 13*a1*a2*a5**2/243 + 52*a1*a2*a5*a6**3/27 - 46*a1*a2*a5*a6**2/27 + 13*a1*a2*a5*a6/81 + 2*a1*a2*a5/81 - 2*a1*a2*a6**4/3 - 17*a1*a2*a6**3/9 + 2*a1*a2*a6**2 - 5*a1*a2*a6/18 - a1*a2/36 + 16*a1*a4*a6**4/81 - 136*a1*a4*a6**3/243 + 152*a1*a4*a6**2/729 - 8*a1*a4*a6/243 + 2*a1*a4/729 - 16*a1*a5**2*a6**3/243 + 116*a1*a5**2*a6**2/729 - 8*a1*a5**2*a6/243 + 2*a1*a5**2/729 - 20*a1*a5*a6**3/81 + 2*a1*a5*a6**2/243 + 2*a1*a5*a6/243 + 8*a1*a6**5/3 - 32*a1*a6**4/9 + 28*a1*a6**3/27 - a1*a6**2/27 - a1*a6/81 - 8*a2**5*a3/3 - 3*a2**5*a5/2 + 28*a2**4*a3*a5/81 + 16*a2**4*a3*a6/9 - 8*a2**4*a3/9 + 4*a2**4*a4*a5/27 - 4*a2**4*a4*a6/3 + 5*a2**4*a4/9 - 4*a2**4*a5**2/27 + 7*a2**4*a5*a6/9 - 2*a2**4*a5/9 + a2**4*a6**2 - a2**4*a6 - a2**4/8 - 8*a2**3*a3*a6**2/81 + 56*a2**3*a3*a6/81 + a2**3*a3/81 + 80*a2**3*a4*a5*a6/729 - 22*a2**3*a4*a5/729 + 64*a2**3*a4*a6**2/81 - 58*a2**3*a4*a6/81 + 16*a2**3*a4/81 + 20*a2**3*a5**3/729 + 68*a2**3*a5**2*a6/243 - 34*a2**3*a5**2/243 - 2*a2**3*a5*a6**2 + 137*a2**3*a5*a6/81 - 5*a2**3*a5/162 + 2*a2**3*a6**3/3 + 2*a2**3*a6**2/9 - 19*a2**3*a6/36 - a2**3/12 - 16*a2**2*a4*a6**3/243 + 280*a2**2*a4*a6**2/729 - 44*a2**2*a4*a6/729 + 2*a2**2*a4/243 + 4*a2**2*a5**2*a6**2/27 - 14*a2**2*a5**2*a6/729 + 2*a2**2*a5**2/729 + 92*a2**2*a5*a6**3/81 - 404*a2**2*a5*a6**2/243 + 137*a2**2*a5*a6/243 - 8*a2**2*a5/243 - 20*a2**2*a6**4/9 + 82*a2**2*a6**3/27 - 65*a2**2*a6**2/81 + 11*a2**2*a6/162 + 8*a2*a5*a6**4/81 + 32*a2*a5*a6**3/81 - 134*a2*a5*a6**2/729 + 2*a2*a5*a6/81 - a2*a5/729 + 8*a2*a6**5/9 - 56*a2*a6**4/27 + 106*a2*a6**3/81 - 82*a2*a6**2/243 + 8*a2*a6/243 + 40*a6**5/81 - 4*a6**4/9 + 110*a6**3/729 - 17*a6**2/729 + a6/729"
        &#93;,
        &#91;
          "-a0**2*a2*a3**2*a4/18 - a0**2*a2*a3*a4**2/18 + a0**2*a3*a4**2*a6/54 + a0**2*a3*a4**2/324 - 7*a0**2*a3*a4*a5**2/162 - 5*a0**2*a3*a4*a5*a6/18 + a0**2*a3*a4*a5/108 + 5*a0**2*a4**3*a5/486 + a0**2*a4**3*a6/9 - a0**2*a4**2*a5**2/81 + a0*a1**2*a3**2*a4/18 + a0*a1**2*a3*a4**2/18 - 7*a0*a1*a2*a3*a4**2/54 + 7*a0*a1*a2*a3*a4*a5/9 - 7*a0*a1*a2*a4**3/18 + 2*a0*a1*a3**2*a6**2/3 - 7*a0*a1*a3**2*a6/18 + 5*a0*a1*a3**2/108 - 29*a0*a1*a3*a4*a5*a6/54 + 31*a0*a1*a3*a4*a5/108 + 2*a0*a1*a3*a4*a6**2/3 - 5*a0*a1*a3*a4*a6/9 + 11*a0*a1*a3*a4/108 - 2*a0*a1*a3*a5**3/27 - 7*a0*a1*a3*a5**2*a6/9 + 7*a0*a1*a3*a5**2/54 + 5*a0*a1*a4**3*a6/81 - 11*a0*a1*a4**3/243 + a0*a1*a4**2*a5**2/27 - 5*a0*a1*a4**2*a5*a6/54 + 41*a0*a1*a4**2*a5/324 + a0*a1*a4*a5**3/27 - a0*a2**2*a3**2*a6/6 + 7*a0*a2**2*a3**2/36 - a0*a2**2*a3*a4*a5/3 + 5*a0*a2**2*a3*a4*a6/6 - 5*a0*a2**2*a3*a4/36 + 8*a0*a2**2*a3*a5**2/9 + a0*a2**2*a4**3/81 - 19*a0*a2**2*a4**2*a5/27 - 10*a0*a2*a3*a4*a6**2/9 + 55*a0*a2*a3*a4*a6/54 - 55*a0*a2*a3*a4/324 - 16*a0*a2*a3*a5**2*a6/27 + 2*a0*a2*a3*a5**2/81 + 11*a0*a2*a3*a5*a6**2/6 - 13*a0*a2*a3*a5*a6/6 + 115*a0*a2*a3*a5/216 + 5*a0*a2*a4**2*a5*a6/162 + 7*a0*a2*a4**2*a5/486 - 13*a0*a2*a4**2*a6**2/18 + 95*a0*a2*a4**2*a6/108 - 7*a0*a2*a4**2/36 + a0*a2*a4*a5**3/27 - 17*a0*a2*a4*a5**2*a6/18 + 91*a0*a2*a4*a5**2/324 + 4*a0*a2*a5**4/27 - a0*a3*a5*a6**3 + 11*a0*a3*a5*a6**2/27 - 17*a0*a3*a5*a6/648 + a0*a3*a5/432 + 3*a0*a3*a6**4/2 - 5*a0*a3*a6**3 + 7*a0*a3*a6**2/2 - 133*a0*a3*a6/144 + 37*a0*a3/432 - 7*a0*a4**2*a6**3/27 + 49*a0*a4**2*a6**2/162 - 73*a0*a4**2*a6/972 + 5*a0*a4**2/972 + 4*a0*a4*a5**2*a6**2/27 - 13*a0*a4*a5**2*a6/972 - 23*a0*a4*a5**2/1944 - 29*a0*a4*a5*a6**3/18 + 113*a0*a4*a5*a6**2/54 - 65*a0*a4*a5*a6/81 + 17*a0*a4*a5/162 - a0*a5**4*a6/162 - 13*a0*a5**4/972 + 5*a0*a5**3*a6**2/18 - 22*a0*a5**3*a6/81 + 41*a0*a5**3/648 + a1**3*a3*a4**2/9 - a1**3*a3*a4*a5/3 + 2*a1**3*a4**3/9 - a1**2*a2*a3**2*a6 + a1**2*a2*a3**2/6 + a1**2*a2*a3*a4*a5/2 - 3*a1**2*a2*a3*a4*a6/2 + 5*a1**2*a2*a3*a4/12 + a1**2*a2*a3*a5**2/9 - a1**2*a2*a4**3/81 + 13*a1**2*a2*a4**2*a5/27 - 5*a1**2*a3*a4*a6**2/9 + 14*a1**2*a3*a4*a6/27 - 7*a1**2*a3*a4/54 - 7*a1**2*a3*a5**2*a6/18 + 55*a1**2*a3*a5**2/108 - 3*a1**2*a3*a5*a6**2 + 17*a1**2*a3*a5*a6/6 - 5*a1**2*a3*a5/9 + 4*a1**2*a4**2*a5*a6/27 - a1**2*a4**2*a5/6 - 2*a1**2*a4**2*a6**2/9 - 7*a1**2*a4**2*a6/27 + a1**2*a4**2/12 + a1**2*a4*a5**3/54 + 4*a1**2*a4*a5**2*a6/9 - a1**2*a4*a5**2/54 + a1*a2**3*a3**2/2 + a1*a2**3*a3*a4/2 + 8*a1*a2**2*a3*a4*a6/9 - 5*a1*a2**2*a3*a4/9 + 14*a1*a2**2*a3*a5**2/27 + 13*a1*a2**2*a3*a5*a6/6 - 5*a1*a2**2*a3*a5/12 + a1*a2**2*a4**2*a5/162 + a1*a2**2*a4**2*a6/2 - a1*a2**2*a4**2/4 + 23*a1*a2**2*a4*a5**2/54 - 23*a1*a2*a3*a5*a6**2/18 + 121*a1*a2*a3*a5*a6/36 - 61*a1*a2*a3*a5/72 - 9*a1*a2*a3*a6**3/2 + 11*a1*a2*a3*a6**2 - 29*a1*a2*a3*a6/6 + 29*a1*a2*a3/48 + 7*a1*a2*a4**2*a6**2/27 - 20*a1*a2*a4**2*a6/81 + a1*a2*a4**2/36 + 11*a1*a2*a4*a5**2*a6/81 - 85*a1*a2*a4*a5**2/324 + a1*a2*a4*a5*a6**2/3 - 29*a1*a2*a4*a5*a6/108 + a1*a2*a4*a5/24 + 7*a1*a2*a5**4/162 + 37*a1*a2*a5**3*a6/54 - 19*a1*a2*a5**3/108 - 4*a1*a3*a6**4/3 + 17*a1*a3*a6**3/6 - 56*a1*a3*a6**2/27 + 73*a1*a3*a6/108 - 35*a1*a3/432 - 4*a1*a4*a5*a6**3/27 + 77*a1*a4*a5*a6**2/162 - 17*a1*a4*a5*a6/162 + a1*a4*a5/648 - 10*a1*a4*a6**4/3 + 20*a1*a4*a6**3/3 - 211*a1*a4*a6**2/54 + a1*a4*a6 - 7*a1*a4/72 + 4*a1*a5**3*a6**2/27 - 19*a1*a5**3*a6/81 + 5*a1*a5**3/216 + 14*a1*a5**2*a6**3/9 - 53*a1*a5**2*a6**2/27 + 53*a1*a5**2*a6/72 - 35*a1*a5**2/432 + a2**4*a3*a4/18 - 4*a2**4*a3*a5/3 + a2**4*a4**2/2 + 20*a2**3*a3*a5*a6/9 - 7*a2**3*a3*a5/3 - 7*a2**3*a3*a6/2 + 5*a2**3*a3/6 - 5*a2**3*a4**2*a6/27 + 7*a2**3*a4**2/54 + 5*a2**3*a4*a5**2/54 + 5*a2**3*a4*a5*a6/2 - 41*a2**3*a4*a5/36 + 10*a2**2*a3*a6**3/3 - 40*a2**2*a3*a6**2/9 + 127*a2**2*a3*a6/72 - 5*a2**2*a3/18 + 7*a2**2*a4*a5*a6**2/18 - 71*a2**2*a4*a5*a6/108 + a2**2*a4*a5/36 + 29*a2**2*a4*a6**3/6 - 125*a2**2*a4*a6**2/18 + 29*a2**2*a4*a6/12 - 7*a2**2*a4/24 + 2*a2**2*a5**3*a6/9 - 5*a2**2*a5**3/27 + 8*a2**2*a5**2*a6**2/3 - 11*a2**2*a5**2*a6/6 + a2**2*a5**2/4 + 4*a2*a4*a6**4/9 - 35*a2*a4*a6**3/54 + 29*a2*a4*a6**2/108 - 5*a2*a4*a6/108 + 7*a2*a5**2*a6**3/9 - 17*a2*a5**2*a6**2/12 + 4*a2*a5**2*a6/9 - a2*a5**2/36 + 25*a2*a5*a6**4/3 - 445*a2*a5*a6**3/36 + 413*a2*a5*a6**2/72 - 73*a2*a5*a6/72 + 7*a2*a5/144 + 2*a5*a6**5/3 - 5*a5*a6**4/3 + 59*a5*a6**3/54 - 31*a5*a6**2/108 + a5*a6/36 + 6*a6**6 - 13*a6**5 + 121*a6**4/12 - 67*a6**3/18 + 97*a6**2/144 - 7*a6/144",
          "-a0**2*a2*a3**2*a4/4 + a0**2*a3*a4**2*a6/12 + a0**2*a3*a4**2/72 - 7*a0**2*a3*a4*a5**2/36 + 5*a0**2*a4**3*a5/108 + a0*a1**2*a3**2*a4/4 - 7*a0*a1*a2*a3*a4**2/12 + 3*a0*a1*a3**2*a6**2 - 7*a0*a1*a3**2*a6/4 + 5*a0*a1*a3**2/24 - 29*a0*a1*a3*a4*a5*a6/12 + 31*a0*a1*a3*a4*a5/24 - a0*a1*a3*a5**3/3 + 5*a0*a1*a4**3*a6/18 - 11*a0*a1*a4**3/54 + a0*a1*a4**2*a5**2/6 - 3*a0*a2**2*a3**2*a6/4 + 7*a0*a2**2*a3**2/8 - 3*a0*a2**2*a3*a4*a5/2 + a0*a2**2*a4**3/18 - 5*a0*a2*a3*a4*a6**2 + 55*a0*a2*a3*a4*a6/12 - 55*a0*a2*a3*a4/72 - 8*a0*a2*a3*a5**2*a6/3 + a0*a2*a3*a5**2/9 + 5*a0*a2*a4**2*a5*a6/36 + 7*a0*a2*a4**2*a5/108 + a0*a2*a4*a5**3/6 - 9*a0*a3*a5*a6**3/2 + 11*a0*a3*a5*a6**2/6 - 17*a0*a3*a5*a6/144 + a0*a3*a5/96 - 7*a0*a4**2*a6**3/6 + 49*a0*a4**2*a6**2/36 - 73*a0*a4**2*a6/216 + 5*a0*a4**2/216 + 2*a0*a4*a5**2*a6**2/3 - 13*a0*a4*a5**2*a6/216 - 23*a0*a4*a5**2/432 - a0*a5**4*a6/36 - 13*a0*a5**4/216 + a1**3*a3*a4**2/2 - 9*a1**2*a2*a3**2*a6/2 + 3*a1**2*a2*a3**2/4 + 9*a1**2*a2*a3*a4*a5/4 - a1**2*a2*a4**3/18 - 5*a1**2*a3*a4*a6**2/2 + 7*a1**2*a3*a4*a6/3 - 7*a1**2*a3*a4/12 - 7*a1**2*a3*a5**2*a6/4 + 55*a1**2*a3*a5**2/24 + 2*a1**2*a4**2*a5*a6/3 - 3*a1**2*a4**2*a5/4 + a1**2*a4*a5**3/12 + 9*a1*a2**3*a3**2/4 + 4*a1*a2**2*a3*a4*a6 - 5*a1*a2**2*a3*a4/2 + 7*a1*a2**2*a3*a5**2/3 + a1*a2**2*a4**2*a5/36 - 23*a1*a2*a3*a5*a6**2/4 + 121*a1*a2*a3*a5*a6/8 - 61*a1*a2*a3*a5/16 + 7*a1*a2*a4**2*a6**2/6 - 10*a1*a2*a4**2*a6/9 + a1*a2*a4**2/8 + 11*a1*a2*a4*a5**2*a6/18 - 85*a1*a2*a4*a5**2/72 + 7*a1*a2*a5**4/36 - 6*a1*a3*a6**4 + 51*a1*a3*a6**3/4 - 28*a1*a3*a6**2/3 + 73*a1*a3*a6/24 - 35*a1*a3/96 - 2*a1*a4*a5*a6**3/3 + 77*a1*a4*a5*a6**2/36 - 17*a1*a4*a5*a6/36 + a1*a4*a5/144 + 2*a1*a5**3*a6**2/3 - 19*a1*a5**3*a6/18 + 5*a1*a5**3/48 + a2**4*a3*a4/4 + 10*a2**3*a3*a5*a6 - 21*a2**3*a3*a5/2 - 5*a2**3*a4**2*a6/6 + 7*a2**3*a4**2/12 + 5*a2**3*a4*a5**2/12 + 15*a2**2*a3*a6**3 - 20*a2**2*a3*a6**2 + 127*a2**2*a3*a6/16 - 5*a2**2*a3/4 + 7*a2**2*a4*a5*a6**2/4 - 71*a2**2*a4*a5*a6/24 + a2**2*a4*a5/8 + a2**2*a5**3*a6 - 5*a2**2*a5**3/6 + 2*a2*a4*a6**4 - 35*a2*a4*a6**3/12 + 29*a2*a4*a6**2/24 - 5*a2*a4*a6/24 + 7*a2*a5**2*a6**3/2 - 51*a2*a5**2*a6**2/8 + 2*a2*a5**2*a6 - a2*a5**2/8 + 3*a5*a6**5 - 15*a5*a6**4/2 + 59*a5*a6**3/12 - 31*a5*a6**2/24 + a5*a6/8",
          "a0**2*a2*a3**2*a4/27 + a0**2*a2*a3*a4**2/27 + 2*a0**2*a2*a3*a4*a5/9 - a0**2*a2*a4**3/18 - a0**2*a3*a4**2*a6/81 - a0**2*a3*a4**2/486 + 7*a0**2*a3*a4*a5**2/243 + 5*a0**2*a3*a4*a5*a6/27 - a0**2*a3*a4*a5/162 + 4*a0**2*a3*a4*a6**2/3 - 5*a0**2*a3*a4*a6/9 + 7*a0**2*a3*a4/108 - 5*a0**2*a4**3*a5/729 - 2*a0**2*a4**3*a6/27 + 2*a0**2*a4**2*a5**2/243 - 17*a0**2*a4**2*a5*a6/54 + 19*a0**2*a4**2*a5/324 + 5*a0**2*a4*a5**3/81 - a0*a1**2*a3**2*a4/27 - a0*a1**2*a3*a4**2/27 - a0*a1**2*a3*a4*a5/18 + 7*a0*a1*a2*a3*a4**2/81 - 14*a0*a1*a2*a3*a4*a5/27 - 7*a0*a1*a2*a3*a4*a6/3 + 4*a0*a1*a2*a3*a4/9 + a0*a1*a2*a3*a5**2/3 + 7*a0*a1*a2*a4**3/27 + 5*a0*a1*a2*a4**2*a5/18 - 4*a0*a1*a3**2*a6**2/9 + 7*a0*a1*a3**2*a6/27 - 5*a0*a1*a3**2/162 + 29*a0*a1*a3*a4*a5*a6/81 - 31*a0*a1*a3*a4*a5/162 - 4*a0*a1*a3*a4*a6**2/9 + 10*a0*a1*a3*a4*a6/27 - 11*a0*a1*a3*a4/162 + 4*a0*a1*a3*a5**3/81 + 14*a0*a1*a3*a5**2*a6/27 - 7*a0*a1*a3*a5**2/81 + 8*a0*a1*a3*a5*a6**2/3 - 23*a0*a1*a3*a5*a6/18 + 7*a0*a1*a3*a5/36 - 10*a0*a1*a4**3*a6/243 + 22*a0*a1*a4**3/729 - 2*a0*a1*a4**2*a5**2/81 + 5*a0*a1*a4**2*a5*a6/81 - 41*a0*a1*a4**2*a5/486 - 5*a0*a1*a4**2*a6**2/9 + 10*a0*a1*a4**2*a6/27 - 17*a0*a1*a4**2/324 - 2*a0*a1*a4*a5**3/81 - 5*a0*a1*a4*a5**2*a6/18 - 13*a0*a1*a4*a5**2/324 + a0*a1*a5**4/9 + a0*a2**3*a3*a4 + a0*a2**2*a3**2*a6/9 - 7*a0*a2**2*a3**2/54 + 2*a0*a2**2*a3*a4*a5/9 - 5*a0*a2**2*a3*a4*a6/9 + 5*a0*a2**2*a3*a4/54 - 16*a0*a2**2*a3*a5**2/27 - a0*a2**2*a3*a5*a6 - 8*a0*a2**2*a3*a5/9 - 2*a0*a2**2*a4**3/243 + 38*a0*a2**2*a4**2*a5/81 + 7*a0*a2**2*a4**2*a6/18 + 4*a0*a2**2*a4**2/27 + 17*a0*a2**2*a4*a5**2/27 + 20*a0*a2*a3*a4*a6**2/27 - 55*a0*a2*a3*a4*a6/81 + 55*a0*a2*a3*a4/486 + 32*a0*a2*a3*a5**2*a6/81 - 4*a0*a2*a3*a5**2/243 - 11*a0*a2*a3*a5*a6**2/9 + 13*a0*a2*a3*a5*a6/9 - 115*a0*a2*a3*a5/324 + a0*a2*a3*a6**3/2 - 41*a0*a2*a3*a6**2/12 + 125*a0*a2*a3*a6/72 - 53*a0*a2*a3/216 - 5*a0*a2*a4**2*a5*a6/243 - 7*a0*a2*a4**2*a5/729 + 13*a0*a2*a4**2*a6**2/27 - 95*a0*a2*a4**2*a6/162 + 7*a0*a2*a4**2/54 - 2*a0*a2*a4*a5**3/81 + 17*a0*a2*a4*a5**2*a6/27 - 91*a0*a2*a4*a5**2/486 + 16*a0*a2*a4*a5*a6**2/9 - 23*a0*a2*a4*a5*a6/36 + 19*a0*a2*a4*a5/648 - 8*a0*a2*a5**4/81 + 7*a0*a2*a5**3*a6/27 - 14*a0*a2*a5**3/81 + 2*a0*a3*a5*a6**3/3 - 22*a0*a3*a5*a6**2/81 + 17*a0*a3*a5*a6/972 - a0*a3*a5/648 - a0*a3*a6**4 + 10*a0*a3*a6**3/3 - 7*a0*a3*a6**2/3 + 133*a0*a3*a6/216 - 37*a0*a3/648 + 14*a0*a4**2*a6**3/81 - 49*a0*a4**2*a6**2/243 + 73*a0*a4**2*a6/1458 - 5*a0*a4**2/1458 - 8*a0*a4*a5**2*a6**2/81 + 13*a0*a4*a5**2*a6/1458 + 23*a0*a4*a5**2/2916 + 29*a0*a4*a5*a6**3/27 - 113*a0*a4*a5*a6**2/81 + 130*a0*a4*a5*a6/243 - 17*a0*a4*a5/243 + 7*a0*a4*a6**4/3 - 17*a0*a4*a6**3/6 + 11*a0*a4*a6**2/9 - 149*a0*a4*a6/648 + 5*a0*a4/324 + a0*a5**4*a6/243 + 13*a0*a5**4/1458 - 5*a0*a5**3*a6**2/27 + 44*a0*a5**3*a6/243 - 41*a0*a5**3/972 + a0*a5**2*a6**3/6 - 13*a0*a5**2*a6**2/108 + a0*a5**2*a6/54 - a0*a5**2/144 - 2*a1**3*a3*a4**2/27 + 2*a1**3*a3*a4*a5/9 + a1**3*a3*a4*a6 - a1**3*a3*a4/6 - 4*a1**3*a4**3/27 - 2*a1**3*a4**2*a5/9 - a1**2*a2**2*a3*a4/2 + 2*a1**2*a2*a3**2*a6/3 - a1**2*a2*a3**2/9 - a1**2*a2*a3*a4*a5/3 + a1**2*a2*a3*a4*a6 - 5*a1**2*a2*a3*a4/18 - 2*a1**2*a2*a3*a5**2/27 - 4*a1**2*a2*a3*a5*a6/3 + 13*a1**2*a2*a3*a5/9 + 2*a1**2*a2*a4**3/243 - 26*a1**2*a2*a4**2*a5/81 + a1**2*a2*a4**2*a6/9 - 17*a1**2*a2*a4**2/54 - 19*a1**2*a2*a4*a5**2/54 + 10*a1**2*a3*a4*a6**2/27 - 28*a1**2*a3*a4*a6/81 + 7*a1**2*a3*a4/81 + 7*a1**2*a3*a5**2*a6/27 - 55*a1**2*a3*a5**2/162 + 2*a1**2*a3*a5*a6**2 - 17*a1**2*a3*a5*a6/9 + 10*a1**2*a3*a5/27 + 3*a1**2*a3*a6**3 - 3*a1**2*a3*a6**2 + a1**2*a3*a6 - 7*a1**2*a3/72 - 8*a1**2*a4**2*a5*a6/81 + a1**2*a4**2*a5/9 + 4*a1**2*a4**2*a6**2/27 + 14*a1**2*a4**2*a6/81 - a1**2*a4**2/18 - a1**2*a4*a5**3/81 - 8*a1**2*a4*a5**2*a6/27 + a1**2*a4*a5**2/81 - 10*a1**2*a4*a5*a6**2/9 + 41*a1**2*a4*a5*a6/54 - a1**2*a4*a5/12 + a1**2*a5**3*a6/6 - 7*a1**2*a5**3/36 - a1*a2**3*a3**2/3 - a1*a2**3*a3*a4/3 + a1*a2**3*a4**2/6 - 16*a1*a2**2*a3*a4*a6/27 + 10*a1*a2**2*a3*a4/27 - 28*a1*a2**2*a3*a5**2/81 - 13*a1*a2**2*a3*a5*a6/9 + 5*a1*a2**2*a3*a5/18 - 19*a1*a2**2*a3*a6**2/2 + 131*a1*a2**2*a3*a6/12 - 55*a1*a2**2*a3/24 - a1*a2**2*a4**2*a5/243 - a1*a2**2*a4**2*a6/3 + a1*a2**2*a4**2/6 - 23*a1*a2**2*a4*a5**2/81 + a1*a2**2*a4*a5*a6/9 - 55*a1*a2**2*a4*a5/108 - 2*a1*a2**2*a5**3/27 + 23*a1*a2*a3*a5*a6**2/27 - 121*a1*a2*a3*a5*a6/54 + 61*a1*a2*a3*a5/108 + 3*a1*a2*a3*a6**3 - 22*a1*a2*a3*a6**2/3 + 29*a1*a2*a3*a6/9 - 29*a1*a2*a3/72 - 14*a1*a2*a4**2*a6**2/81 + 40*a1*a2*a4**2*a6/243 - a1*a2*a4**2/54 - 22*a1*a2*a4*a5**2*a6/243 + 85*a1*a2*a4*a5**2/486 - 2*a1*a2*a4*a5*a6**2/9 + 29*a1*a2*a4*a5*a6/162 - a1*a2*a4*a5/36 - 13*a1*a2*a4*a6**3/3 + 17*a1*a2*a4*a6**2/3 - 203*a1*a2*a4*a6/108 + 7*a1*a2*a4/36 - 7*a1*a2*a5**4/243 - 37*a1*a2*a5**3*a6/81 + 19*a1*a2*a5**3/162 + 11*a1*a2*a5**2*a6**2/9 - 58*a1*a2*a5**2*a6/27 + 97*a1*a2*a5**2/216 + 8*a1*a3*a6**4/9 - 17*a1*a3*a6**3/9 + 112*a1*a3*a6**2/81 - 73*a1*a3*a6/162 + 35*a1*a3/648 + 8*a1*a4*a5*a6**3/81 - 77*a1*a4*a5*a6**2/243 + 17*a1*a4*a5*a6/243 - a1*a4*a5/972 + 20*a1*a4*a6**4/9 - 40*a1*a4*a6**3/9 + 211*a1*a4*a6**2/81 - 2*a1*a4*a6/3 + 7*a1*a4/108 - 8*a1*a5**3*a6**2/81 + 38*a1*a5**3*a6/243 - 5*a1*a5**3/324 - 28*a1*a5**2*a6**3/27 + 106*a1*a5**2*a6**2/81 - 53*a1*a5**2*a6/108 + 35*a1*a5**2/648 + 2*a1*a5*a6**4/3 - 31*a1*a5*a6**3/18 + 35*a1*a5*a6**2/36 - 31*a1*a5*a6/108 + 7*a1*a5/216 - a2**4*a3*a4/27 + 8*a2**4*a3*a5/9 + 4*a2**4*a3*a6 - 23*a2**4*a3/6 - a2**4*a4**2/3 + a2**4*a4*a5/3 - 40*a2**3*a3*a5*a6/27 + 14*a2**3*a3*a5/9 + 7*a2**3*a3*a6/3 - 5*a2**3*a3/9 + 10*a2**3*a4**2*a6/81 - 7*a2**3*a4**2/81 - 5*a2**3*a4*a5**2/81 - 5*a2**3*a4*a5*a6/3 + 41*a2**3*a4*a5/54 + 19*a2**3*a4*a6**2/6 - 137*a2**3*a4*a6/36 + 5*a2**3*a4/9 - 2*a2**3*a5**2*a6/9 + 7*a2**3*a5**2/18 - 20*a2**2*a3*a6**3/9 + 80*a2**2*a3*a6**2/27 - 127*a2**2*a3*a6/108 + 5*a2**2*a3/27 - 7*a2**2*a4*a5*a6**2/27 + 71*a2**2*a4*a5*a6/162 - a2**2*a4*a5/54 - 29*a2**2*a4*a6**3/9 + 125*a2**2*a4*a6**2/27 - 29*a2**2*a4*a6/18 + 7*a2**2*a4/36 - 4*a2**2*a5**3*a6/27 + 10*a2**2*a5**3/81 - 16*a2**2*a5**2*a6**2/9 + 11*a2**2*a5**2*a6/9 - a2**2*a5**2/6 + 5*a2**2*a5*a6**3/3 - 113*a2**2*a5*a6**2/36 + 77*a2**2*a5*a6/72 - 8*a2*a4*a6**4/27 + 35*a2*a4*a6**3/81 - 29*a2*a4*a6**2/162 + 5*a2*a4*a6/162 - 14*a2*a5**2*a6**3/27 + 17*a2*a5**2*a6**2/18 - 8*a2*a5**2*a6/27 + a2*a5**2/54 - 50*a2*a5*a6**4/9 + 445*a2*a5*a6**3/54 - 413*a2*a5*a6**2/108 + 73*a2*a5*a6/108 - 7*a2*a5/216 + 2*a2*a6**5 - 16*a2*a6**4/3 + 137*a2*a6**3/36 - 77*a2*a6**2/72 + a2*a6/9 - 4*a5*a6**5/9 + 10*a5*a6**4/9 - 59*a5*a6**3/81 + 31*a5*a6**2/162 - a5*a6/54 - 4*a6**6 + 26*a6**5/3 - 121*a6**4/18 + 67*a6**3/27 - 97*a6**2/216 + 7*a6/216",
          "a0**2*a1*a3*a4*a5/6 - a0**2*a1*a4**3/18 - 2*a0**2*a2*a3**2*a4/81 - 2*a0**2*a2*a3*a4**2/81 - 4*a0**2*a2*a3*a4*a5/27 + 7*a0**2*a2*a3*a4*a6/6 - 5*a0**2*a2*a3*a4/18 + a0**2*a2*a4**3/27 - 4*a0**2*a2*a4**2*a5/27 + 2*a0**2*a3*a4**2*a6/243 + a0**2*a3*a4**2/729 - 14*a0**2*a3*a4*a5**2/729 - 10*a0**2*a3*a4*a5*a6/81 + a0**2*a3*a4*a5/243 - 8*a0**2*a3*a4*a6**2/9 + 10*a0**2*a3*a4*a6/27 - 7*a0**2*a3*a4/162 + 10*a0**2*a4**3*a5/2187 + 4*a0**2*a4**3*a6/81 - 4*a0**2*a4**2*a5**2/729 + 17*a0**2*a4**2*a5*a6/81 - 19*a0**2*a4**2*a5/486 + a0**2*a4**2*a6**2/2 - a0**2*a4**2*a6/4 + a0**2*a4**2/36 - 10*a0**2*a4*a5**3/243 - 5*a0**2*a4*a5**2*a6/27 + a0**2*a4*a5**2/18 + 2*a0*a1**2*a3**2*a4/81 + 2*a0*a1**2*a3*a4**2/81 + a0*a1**2*a3*a4*a5/27 + a0*a1**2*a3*a4*a6/6 + a0*a1**2*a3*a5**2/3 - a0*a1**2*a4**2*a5/9 - 4*a0*a1*a2**2*a3*a4/3 - 14*a0*a1*a2*a3*a4**2/243 + 28*a0*a1*a2*a3*a4*a5/81 + 14*a0*a1*a2*a3*a4*a6/9 - 8*a0*a1*a2*a3*a4/27 - 2*a0*a1*a2*a3*a5**2/9 + 29*a0*a1*a2*a3*a5*a6/6 - 71*a0*a1*a2*a3*a5/36 - 14*a0*a1*a2*a4**3/81 - 5*a0*a1*a2*a4**2*a5/27 - 11*a0*a1*a2*a4**2*a6/9 + 37*a0*a1*a2*a4**2/54 - 5*a0*a1*a2*a4*a5**2/9 + 8*a0*a1*a3**2*a6**2/27 - 14*a0*a1*a3**2*a6/81 + 5*a0*a1*a3**2/243 - 58*a0*a1*a3*a4*a5*a6/243 + 31*a0*a1*a3*a4*a5/243 + 8*a0*a1*a3*a4*a6**2/27 - 20*a0*a1*a3*a4*a6/81 + 11*a0*a1*a3*a4/243 - 8*a0*a1*a3*a5**3/243 - 28*a0*a1*a3*a5**2*a6/81 + 14*a0*a1*a3*a5**2/243 - 16*a0*a1*a3*a5*a6**2/9 + 23*a0*a1*a3*a5*a6/27 - 7*a0*a1*a3*a5/54 + 7*a0*a1*a3*a6**3/2 - 53*a0*a1*a3*a6**2/12 + 115*a0*a1*a3*a6/72 - 13*a0*a1*a3/72 + 20*a0*a1*a4**3*a6/729 - 44*a0*a1*a4**3/2187 + 4*a0*a1*a4**2*a5**2/243 - 10*a0*a1*a4**2*a5*a6/243 + 41*a0*a1*a4**2*a5/729 + 10*a0*a1*a4**2*a6**2/27 - 20*a0*a1*a4**2*a6/81 + 17*a0*a1*a4**2/486 + 4*a0*a1*a4*a5**3/243 + 5*a0*a1*a4*a5**2*a6/27 + 13*a0*a1*a4*a5**2/486 - a0*a1*a4*a5*a6**2/6 + 19*a0*a1*a4*a5*a6/27 - 5*a0*a1*a4*a5/24 - 2*a0*a1*a5**4/27 - 7*a0*a1*a5**3*a6/18 + 5*a0*a1*a5**3/108 - 2*a0*a2**3*a3*a4/3 - 8*a0*a2**3*a3*a5/3 - a0*a2**3*a4**2/9 - 2*a0*a2**2*a3**2*a6/27 + 7*a0*a2**2*a3**2/81 - 4*a0*a2**2*a3*a4*a5/27 + 10*a0*a2**2*a3*a4*a6/27 - 5*a0*a2**2*a3*a4/81 + 32*a0*a2**2*a3*a5**2/81 + 2*a0*a2**2*a3*a5*a6/3 + 16*a0*a2**2*a3*a5/27 - 3*a0*a2**2*a3*a6**2/2 + 7*a0*a2**2*a3*a6/12 - a0*a2**2*a3/18 + 4*a0*a2**2*a4**3/729 - 76*a0*a2**2*a4**2*a5/243 - 7*a0*a2**2*a4**2*a6/27 - 8*a0*a2**2*a4**2/81 - 34*a0*a2**2*a4*a5**2/81 - 2*a0*a2**2*a4*a5*a6 + 35*a0*a2**2*a4*a5/54 - 4*a0*a2**2*a5**3/9 - 40*a0*a2*a3*a4*a6**2/81 + 110*a0*a2*a3*a4*a6/243 - 55*a0*a2*a3*a4/729 - 64*a0*a2*a3*a5**2*a6/243 + 8*a0*a2*a3*a5**2/729 + 22*a0*a2*a3*a5*a6**2/27 - 26*a0*a2*a3*a5*a6/27 + 115*a0*a2*a3*a5/486 - a0*a2*a3*a6**3/3 + 41*a0*a2*a3*a6**2/18 - 125*a0*a2*a3*a6/108 + 53*a0*a2*a3/324 + 10*a0*a2*a4**2*a5*a6/729 + 14*a0*a2*a4**2*a5/2187 - 26*a0*a2*a4**2*a6**2/81 + 95*a0*a2*a4**2*a6/243 - 7*a0*a2*a4**2/81 + 4*a0*a2*a4*a5**3/243 - 34*a0*a2*a4*a5**2*a6/81 + 91*a0*a2*a4*a5**2/729 - 32*a0*a2*a4*a5*a6**2/27 + 23*a0*a2*a4*a5*a6/54 - 19*a0*a2*a4*a5/972 - 4*a0*a2*a4*a6**3/3 + 4*a0*a2*a4*a6**2/3 - 14*a0*a2*a4*a6/27 + 17*a0*a2*a4/216 + 16*a0*a2*a5**4/243 - 14*a0*a2*a5**3*a6/81 + 28*a0*a2*a5**3/243 - 59*a0*a2*a5**2*a6**2/18 + 67*a0*a2*a5**2*a6/36 - 29*a0*a2*a5**2/108 - 4*a0*a3*a5*a6**3/9 + 44*a0*a3*a5*a6**2/243 - 17*a0*a3*a5*a6/1458 + a0*a3*a5/972 + 2*a0*a3*a6**4/3 - 20*a0*a3*a6**3/9 + 14*a0*a3*a6**2/9 - 133*a0*a3*a6/324 + 37*a0*a3/972 - 28*a0*a4**2*a6**3/243 + 98*a0*a4**2*a6**2/729 - 73*a0*a4**2*a6/2187 + 5*a0*a4**2/2187 + 16*a0*a4*a5**2*a6**2/243 - 13*a0*a4*a5**2*a6/2187 - 23*a0*a4*a5**2/4374 - 58*a0*a4*a5*a6**3/81 + 226*a0*a4*a5*a6**2/243 - 260*a0*a4*a5*a6/729 + 34*a0*a4*a5/729 - 14*a0*a4*a6**4/9 + 17*a0*a4*a6**3/9 - 22*a0*a4*a6**2/27 + 149*a0*a4*a6/972 - 5*a0*a4/486 - 2*a0*a5**4*a6/729 - 13*a0*a5**4/2187 + 10*a0*a5**3*a6**2/81 - 88*a0*a5**3*a6/729 + 41*a0*a5**3/1458 - a0*a5**2*a6**3/9 + 13*a0*a5**2*a6**2/162 - a0*a5**2*a6/81 + a0*a5**2/216 - 7*a0*a5*a6**4/2 + 137*a0*a5*a6**3/36 - 169*a0*a5*a6**2/108 + 137*a0*a5*a6/432 - a0*a5/36 + a1**3*a2*a3*a4/2 + 4*a1**3*a3*a4**2/81 - 4*a1**3*a3*a4*a5/27 - 2*a1**3*a3*a4*a6/3 + a1**3*a3*a4/9 - 2*a1**3*a3*a5*a6 + 4*a1**3*a3*a5/3 + 8*a1**3*a4**3/81 + 4*a1**3*a4**2*a5/27 + 2*a1**3*a4**2*a6/3 - 4*a1**3*a4**2/9 + a1**3*a4*a5**2/6 + a1**2*a2**2*a3*a4/3 + a1**2*a2**2*a3*a5/6 + 5*a1**2*a2**2*a4**2/18 - 4*a1**2*a2*a3**2*a6/9 + 2*a1**2*a2*a3**2/27 + 2*a1**2*a2*a3*a4*a5/9 - 2*a1**2*a2*a3*a4*a6/3 + 5*a1**2*a2*a3*a4/27 + 4*a1**2*a2*a3*a5**2/81 + 8*a1**2*a2*a3*a5*a6/9 - 26*a1**2*a2*a3*a5/27 - 9*a1**2*a2*a3*a6**2/2 + 23*a1**2*a2*a3*a6/4 - 29*a1**2*a2*a3/24 - 4*a1**2*a2*a4**3/729 + 52*a1**2*a2*a4**2*a5/243 - 2*a1**2*a2*a4**2*a6/27 + 17*a1**2*a2*a4**2/81 + 19*a1**2*a2*a4*a5**2/81 + 5*a1**2*a2*a4*a5*a6/9 - 17*a1**2*a2*a4*a5/36 + 7*a1**2*a2*a5**3/18 - 20*a1**2*a3*a4*a6**2/81 + 56*a1**2*a3*a4*a6/243 - 14*a1**2*a3*a4/243 - 14*a1**2*a3*a5**2*a6/81 + 55*a1**2*a3*a5**2/243 - 4*a1**2*a3*a5*a6**2/3 + 34*a1**2*a3*a5*a6/27 - 20*a1**2*a3*a5/81 - 2*a1**2*a3*a6**3 + 2*a1**2*a3*a6**2 - 2*a1**2*a3*a6/3 + 7*a1**2*a3/108 + 16*a1**2*a4**2*a5*a6/243 - 2*a1**2*a4**2*a5/27 - 8*a1**2*a4**2*a6**2/81 - 28*a1**2*a4**2*a6/243 + a1**2*a4**2/27 + 2*a1**2*a4*a5**3/243 + 16*a1**2*a4*a5**2*a6/81 - 2*a1**2*a4*a5**2/243 + 20*a1**2*a4*a5*a6**2/27 - 41*a1**2*a4*a5*a6/81 + a1**2*a4*a5/18 - 8*a1**2*a4*a6**3/3 + 32*a1**2*a4*a6**2/9 - 23*a1**2*a4*a6/18 + 5*a1**2*a4/36 - a1**2*a5**3*a6/9 + 7*a1**2*a5**3/54 + 5*a1**2*a5**2*a6**2/6 - 19*a1**2*a5**2*a6/36 - a1**2*a5**2/24 + 2*a1*a2**3*a3**2/9 + 2*a1*a2**3*a3*a4/9 - 7*a1*a2**3*a3*a6/2 - a1*a2**3*a3 - a1*a2**3*a4**2/9 + 17*a1*a2**3*a4*a5/18 + 32*a1*a2**2*a3*a4*a6/81 - 20*a1*a2**2*a3*a4/81 + 56*a1*a2**2*a3*a5**2/243 + 26*a1*a2**2*a3*a5*a6/27 - 5*a1*a2**2*a3*a5/27 + 19*a1*a2**2*a3*a6**2/3 - 131*a1*a2**2*a3*a6/18 + 55*a1*a2**2*a3/36 + 2*a1*a2**2*a4**2*a5/729 + 2*a1*a2**2*a4**2*a6/9 - a1*a2**2*a4**2/9 + 46*a1*a2**2*a4*a5**2/243 - 2*a1*a2**2*a4*a5*a6/27 + 55*a1*a2**2*a4*a5/162 + a1*a2**2*a4*a6**2/6 - 55*a1*a2**2*a4*a6/36 + a1*a2**2*a4/3 + 4*a1*a2**2*a5**3/81 + 5*a1*a2**2*a5**2*a6/2 - 5*a1*a2**2*a5**2/6 - 46*a1*a2*a3*a5*a6**2/81 + 121*a1*a2*a3*a5*a6/81 - 61*a1*a2*a3*a5/162 - 2*a1*a2*a3*a6**3 + 44*a1*a2*a3*a6**2/9 - 58*a1*a2*a3*a6/27 + 29*a1*a2*a3/108 + 28*a1*a2*a4**2*a6**2/243 - 80*a1*a2*a4**2*a6/729 + a1*a2*a4**2/81 + 44*a1*a2*a4*a5**2*a6/729 - 85*a1*a2*a4*a5**2/729 + 4*a1*a2*a4*a5*a6**2/27 - 29*a1*a2*a4*a5*a6/243 + a1*a2*a4*a5/54 + 26*a1*a2*a4*a6**3/9 - 34*a1*a2*a4*a6**2/9 + 203*a1*a2*a4*a6/162 - 7*a1*a2*a4/54 + 14*a1*a2*a5**4/729 + 74*a1*a2*a5**3*a6/243 - 19*a1*a2*a5**3/243 - 22*a1*a2*a5**2*a6**2/27 + 116*a1*a2*a5**2*a6/81 - 97*a1*a2*a5**2/324 + 4*a1*a2*a5*a6**3 - 97*a1*a2*a5*a6**2/36 - 7*a1*a2*a5*a6/12 + 7*a1*a2*a5/24 - 16*a1*a3*a6**4/27 + 34*a1*a3*a6**3/27 - 224*a1*a3*a6**2/243 + 73*a1*a3*a6/243 - 35*a1*a3/972 - 16*a1*a4*a5*a6**3/243 + 154*a1*a4*a5*a6**2/729 - 34*a1*a4*a5*a6/729 + a1*a4*a5/1458 - 40*a1*a4*a6**4/27 + 80*a1*a4*a6**3/27 - 422*a1*a4*a6**2/243 + 4*a1*a4*a6/9 - 7*a1*a4/162 + 16*a1*a5**3*a6**2/243 - 76*a1*a5**3*a6/729 + 5*a1*a5**3/486 + 56*a1*a5**2*a6**3/81 - 212*a1*a5**2*a6**2/243 + 53*a1*a5**2*a6/162 - 35*a1*a5**2/972 - 4*a1*a5*a6**4/9 + 31*a1*a5*a6**3/27 - 35*a1*a5*a6**2/54 + 31*a1*a5*a6/162 - 7*a1*a5/324 + 2*a1*a6**5 - 2*a1*a6**4 - 8*a1*a6**3/9 + 13*a1*a6**2/9 - 17*a1*a6/36 + 7*a1/144 + 4*a2**5*a3 + 2*a2**4*a3*a4/81 - 16*a2**4*a3*a5/27 - 8*a2**4*a3*a6/3 + 23*a2**4*a3/9 + 2*a2**4*a4**2/9 - 2*a2**4*a4*a5/9 + 19*a2**4*a4*a6/6 - 7*a2**4*a4/6 + 80*a2**3*a3*a5*a6/81 - 28*a2**3*a3*a5/27 - 14*a2**3*a3*a6/9 + 10*a2**3*a3/27 - 20*a2**3*a4**2*a6/243 + 14*a2**3*a4**2/243 + 10*a2**3*a4*a5**2/243 + 10*a2**3*a4*a5*a6/9 - 41*a2**3*a4*a5/81 - 19*a2**3*a4*a6**2/9 + 137*a2**3*a4*a6/54 - 10*a2**3*a4/27 + 4*a2**3*a5**2*a6/27 - 7*a2**3*a5**2/27 + 14*a2**3*a5*a6**2/3 - 13*a2**3*a5*a6/3 + 4*a2**3*a5/3 + 40*a2**2*a3*a6**3/27 - 160*a2**2*a3*a6**2/81 + 127*a2**2*a3*a6/162 - 10*a2**2*a3/81 + 14*a2**2*a4*a5*a6**2/81 - 71*a2**2*a4*a5*a6/243 + a2**2*a4*a5/81 + 58*a2**2*a4*a6**3/27 - 250*a2**2*a4*a6**2/81 + 29*a2**2*a4*a6/27 - 7*a2**2*a4/54 + 8*a2**2*a5**3*a6/81 - 20*a2**2*a5**3/243 + 32*a2**2*a5**2*a6**2/27 - 22*a2**2*a5**2*a6/27 + a2**2*a5**2/9 - 10*a2**2*a5*a6**3/9 + 113*a2**2*a5*a6**2/54 - 77*a2**2*a5*a6/108 + 6*a2**2*a6**4 - 9*a2**2*a6**3 + 43*a2**2*a6**2/8 - 37*a2**2*a6/24 + a2**2/6 + 16*a2*a4*a6**4/81 - 70*a2*a4*a6**3/243 + 29*a2*a4*a6**2/243 - 5*a2*a4*a6/243 + 28*a2*a5**2*a6**3/81 - 17*a2*a5**2*a6**2/27 + 16*a2*a5**2*a6/81 - a2*a5**2/81 + 100*a2*a5*a6**4/27 - 445*a2*a5*a6**3/81 + 413*a2*a5*a6**2/162 - 73*a2*a5*a6/162 + 7*a2*a5/324 - 4*a2*a6**5/3 + 32*a2*a6**4/9 - 137*a2*a6**3/54 + 77*a2*a6**2/108 - 2*a2*a6/27 + 8*a5*a6**5/27 - 20*a5*a6**4/27 + 118*a5*a6**3/243 - 31*a5*a6**2/243 + a5*a6/81 + 8*a6**6/3 - 52*a6**5/9 + 121*a6**4/27 - 134*a6**3/81 + 97*a6**2/324 - 7*a6/324",
          "a0**3*a3*a4*a5/6 - a0**3*a4**3/18 - a0**2*a1*a3*a4*a5/9 + 4*a0**2*a1*a3*a4*a6/3 - 5*a0**2*a1*a3*a4/18 + a0**2*a1*a3*a5**2/3 + a0**2*a1*a4**3/27 - 7*a0**2*a1*a4**2*a5/27 + 5*a0**2*a2**2*a3*a4/6 + 4*a0**2*a2*a3**2*a4/243 + 4*a0**2*a2*a3*a4**2/243 + 8*a0**2*a2*a3*a4*a5/81 - 7*a0**2*a2*a3*a4*a6/9 + 5*a0**2*a2*a3*a4/27 + 3*a0**2*a2*a3*a5*a6/2 - 11*a0**2*a2*a3*a5/12 - 2*a0**2*a2*a4**3/81 + 8*a0**2*a2*a4**2*a5/81 + a0**2*a2*a4**2*a6 + a0**2*a2*a4**2/36 - 8*a0**2*a2*a4*a5**2/27 - 4*a0**2*a3*a4**2*a6/729 - 2*a0**2*a3*a4**2/2187 + 28*a0**2*a3*a4*a5**2/2187 + 20*a0**2*a3*a4*a5*a6/243 - 2*a0**2*a3*a4*a5/729 + 16*a0**2*a3*a4*a6**2/27 - 20*a0**2*a3*a4*a6/81 + 7*a0**2*a3*a4/243 + 3*a0**2*a3*a6**3/2 - 11*a0**2*a3*a6**2/4 + 29*a0**2*a3*a6/24 - 11*a0**2*a3/72 - 20*a0**2*a4**3*a5/6561 - 8*a0**2*a4**3*a6/243 + 8*a0**2*a4**2*a5**2/2187 - 34*a0**2*a4**2*a5*a6/243 + 19*a0**2*a4**2*a5/729 - a0**2*a4**2*a6**2/3 + a0**2*a4**2*a6/6 - a0**2*a4**2/54 + 20*a0**2*a4*a5**3/729 + 10*a0**2*a4*a5**2*a6/81 - a0**2*a4*a5**2/27 + a0**2*a4*a5*a6**2/3 + a0**2*a4*a5*a6/4 - 25*a0**2*a4*a5/216 - a0**2*a5**3*a6/18 - 5*a0**2*a5**3/108 - 8*a0*a1**2*a2*a3*a4/3 - 4*a0*a1**2*a3**2*a4/243 - 4*a0*a1**2*a3*a4**2/243 - 2*a0*a1**2*a3*a4*a5/81 - a0*a1**2*a3*a4*a6/9 - 2*a0*a1**2*a3*a5**2/9 + 4*a0*a1**2*a3*a5*a6/3 + 5*a0*a1**2*a3*a5/18 + 2*a0*a1**2*a4**2*a5/27 - 5*a0*a1**2*a4**2*a6/9 - a0*a1**2*a4**2/27 - 5*a0*a1**2*a4*a5**2/18 + 8*a0*a1*a2**2*a3*a4/9 - 13*a0*a1*a2**2*a3*a5/6 - 10*a0*a1*a2**2*a4**2/9 + 28*a0*a1*a2*a3*a4**2/729 - 56*a0*a1*a2*a3*a4*a5/243 - 28*a0*a1*a2*a3*a4*a6/27 + 16*a0*a1*a2*a3*a4/81 + 4*a0*a1*a2*a3*a5**2/27 - 29*a0*a1*a2*a3*a5*a6/9 + 71*a0*a1*a2*a3*a5/54 - 7*a0*a1*a2*a3*a6**2/2 + 67*a0*a1*a2*a3*a6/12 - 35*a0*a1*a2*a3/24 + 28*a0*a1*a2*a4**3/243 + 10*a0*a1*a2*a4**2*a5/81 + 22*a0*a1*a2*a4**2*a6/27 - 37*a0*a1*a2*a4**2/81 + 10*a0*a1*a2*a4*a5**2/27 + a0*a1*a2*a4*a5*a6/18 - 5*a0*a1*a2*a4*a5/54 - 7*a0*a1*a2*a5**3/18 - 16*a0*a1*a3**2*a6**2/81 + 28*a0*a1*a3**2*a6/243 - 10*a0*a1*a3**2/729 + 116*a0*a1*a3*a4*a5*a6/729 - 62*a0*a1*a3*a4*a5/729 - 16*a0*a1*a3*a4*a6**2/81 + 40*a0*a1*a3*a4*a6/243 - 22*a0*a1*a3*a4/729 + 16*a0*a1*a3*a5**3/729 + 56*a0*a1*a3*a5**2*a6/243 - 28*a0*a1*a3*a5**2/729 + 32*a0*a1*a3*a5*a6**2/27 - 46*a0*a1*a3*a5*a6/81 + 7*a0*a1*a3*a5/81 - 7*a0*a1*a3*a6**3/3 + 53*a0*a1*a3*a6**2/18 - 115*a0*a1*a3*a6/108 + 13*a0*a1*a3/108 - 40*a0*a1*a4**3*a6/2187 + 88*a0*a1*a4**3/6561 - 8*a0*a1*a4**2*a5**2/729 + 20*a0*a1*a4**2*a5*a6/729 - 82*a0*a1*a4**2*a5/2187 - 20*a0*a1*a4**2*a6**2/81 + 40*a0*a1*a4**2*a6/243 - 17*a0*a1*a4**2/729 - 8*a0*a1*a4*a5**3/729 - 10*a0*a1*a4*a5**2*a6/81 - 13*a0*a1*a4*a5**2/729 + a0*a1*a4*a5*a6**2/9 - 38*a0*a1*a4*a5*a6/81 + 5*a0*a1*a4*a5/36 + a0*a1*a4*a6**3/3 + 7*a0*a1*a4*a6**2/9 - 53*a0*a1*a4*a6/108 + 19*a0*a1*a4/216 + 4*a0*a1*a5**4/81 + 7*a0*a1*a5**3*a6/27 - 5*a0*a1*a5**3/162 + a0*a1*a5**2*a6**2/3 - 19*a0*a1*a5**2*a6/54 - 5*a0*a1*a5**2/72 + 4*a0*a2**3*a3*a4/9 + 16*a0*a2**3*a3*a5/9 - a0*a2**3*a3*a6/2 - 23*a0*a2**3*a3/12 + 2*a0*a2**3*a4**2/27 - 25*a0*a2**3*a4*a5/18 + 4*a0*a2**2*a3**2*a6/81 - 14*a0*a2**2*a3**2/243 + 8*a0*a2**2*a3*a4*a5/81 - 20*a0*a2**2*a3*a4*a6/81 + 10*a0*a2**2*a3*a4/243 - 64*a0*a2**2*a3*a5**2/243 - 4*a0*a2**2*a3*a5*a6/9 - 32*a0*a2**2*a3*a5/81 + a0*a2**2*a3*a6**2 - 7*a0*a2**2*a3*a6/18 + a0*a2**2*a3/27 - 8*a0*a2**2*a4**3/2187 + 152*a0*a2**2*a4**2*a5/729 + 14*a0*a2**2*a4**2*a6/81 + 16*a0*a2**2*a4**2/243 + 68*a0*a2**2*a4*a5**2/243 + 4*a0*a2**2*a4*a5*a6/3 - 35*a0*a2**2*a4*a5/81 - 13*a0*a2**2*a4*a6**2/6 + 5*a0*a2**2*a4*a6/36 - 2*a0*a2**2*a4/9 + 8*a0*a2**2*a5**3/27 - 5*a0*a2**2*a5**2*a6/18 + 5*a0*a2**2*a5**2/108 + 80*a0*a2*a3*a4*a6**2/243 - 220*a0*a2*a3*a4*a6/729 + 110*a0*a2*a3*a4/2187 + 128*a0*a2*a3*a5**2*a6/729 - 16*a0*a2*a3*a5**2/2187 - 44*a0*a2*a3*a5*a6**2/81 + 52*a0*a2*a3*a5*a6/81 - 115*a0*a2*a3*a5/729 + 2*a0*a2*a3*a6**3/9 - 41*a0*a2*a3*a6**2/27 + 125*a0*a2*a3*a6/162 - 53*a0*a2*a3/486 - 20*a0*a2*a4**2*a5*a6/2187 - 28*a0*a2*a4**2*a5/6561 + 52*a0*a2*a4**2*a6**2/243 - 190*a0*a2*a4**2*a6/729 + 14*a0*a2*a4**2/243 - 8*a0*a2*a4*a5**3/729 + 68*a0*a2*a4*a5**2*a6/243 - 182*a0*a2*a4*a5**2/2187 + 64*a0*a2*a4*a5*a6**2/81 - 23*a0*a2*a4*a5*a6/81 + 19*a0*a2*a4*a5/1458 + 8*a0*a2*a4*a6**3/9 - 8*a0*a2*a4*a6**2/9 + 28*a0*a2*a4*a6/81 - 17*a0*a2*a4/324 - 32*a0*a2*a5**4/729 + 28*a0*a2*a5**3*a6/243 - 56*a0*a2*a5**3/729 + 59*a0*a2*a5**2*a6**2/27 - 67*a0*a2*a5**2*a6/54 + 29*a0*a2*a5**2/162 + 7*a0*a2*a5*a6**3/2 - 65*a0*a2*a5*a6**2/18 + 23*a0*a2*a5*a6/108 + 67*a0*a2*a5/432 + 8*a0*a3*a5*a6**3/27 - 88*a0*a3*a5*a6**2/729 + 17*a0*a3*a5*a6/2187 - a0*a3*a5/1458 - 4*a0*a3*a6**4/9 + 40*a0*a3*a6**3/27 - 28*a0*a3*a6**2/27 + 133*a0*a3*a6/486 - 37*a0*a3/1458 + 56*a0*a4**2*a6**3/729 - 196*a0*a4**2*a6**2/2187 + 146*a0*a4**2*a6/6561 - 10*a0*a4**2/6561 - 32*a0*a4*a5**2*a6**2/729 + 26*a0*a4*a5**2*a6/6561 + 23*a0*a4*a5**2/6561 + 116*a0*a4*a5*a6**3/243 - 452*a0*a4*a5*a6**2/729 + 520*a0*a4*a5*a6/2187 - 68*a0*a4*a5/2187 + 28*a0*a4*a6**4/27 - 34*a0*a4*a6**3/27 + 44*a0*a4*a6**2/81 - 149*a0*a4*a6/1458 + 5*a0*a4/729 + 4*a0*a5**4*a6/2187 + 26*a0*a5**4/6561 - 20*a0*a5**3*a6**2/243 + 176*a0*a5**3*a6/2187 - 41*a0*a5**3/2187 + 2*a0*a5**2*a6**3/27 - 13*a0*a5**2*a6**2/243 + 2*a0*a5**2*a6/243 - a0*a5**2/324 + 7*a0*a5*a6**4/3 - 137*a0*a5*a6**3/54 + 169*a0*a5*a6**2/162 - 137*a0*a5*a6/648 + a0*a5/54 + 6*a0*a6**5 - 17*a0*a6**4/2 + 41*a0*a6**3/12 - 11*a0*a6**2/36 - 31*a0*a6/432 + 5*a0/432 + a1**4*a3*a4 - a1**3*a2*a3*a4/3 - a1**3*a2*a3*a5/3 + 7*a1**3*a2*a4**2/9 - 8*a1**3*a3*a4**2/243 + 8*a1**3*a3*a4*a5/81 + 4*a1**3*a3*a4*a6/9 - 2*a1**3*a3*a4/27 + 4*a1**3*a3*a5*a6/3 - 8*a1**3*a3*a5/9 + 3*a1**3*a3*a6**2 - 5*a1**3*a3*a6/2 + 7*a1**3*a3/12 - 16*a1**3*a4**3/243 - 8*a1**3*a4**2*a5/81 - 4*a1**3*a4**2*a6/9 + 8*a1**3*a4**2/27 - a1**3*a4*a5**2/9 - 4*a1**3*a4*a5*a6/3 + 7*a1**3*a4*a5/18 - 2*a1**2*a2**2*a3*a4/9 - a1**2*a2**2*a3*a5/9 - 8*a1**2*a2**2*a3*a6 + 5*a1**2*a2**2*a3/2 - 5*a1**2*a2**2*a4**2/27 + 5*a1**2*a2**2*a4*a5/3 + 8*a1**2*a2*a3**2*a6/27 - 4*a1**2*a2*a3**2/81 - 4*a1**2*a2*a3*a4*a5/27 + 4*a1**2*a2*a3*a4*a6/9 - 10*a1**2*a2*a3*a4/81 - 8*a1**2*a2*a3*a5**2/243 - 16*a1**2*a2*a3*a5*a6/27 + 52*a1**2*a2*a3*a5/81 + 3*a1**2*a2*a3*a6**2 - 23*a1**2*a2*a3*a6/6 + 29*a1**2*a2*a3/36 + 8*a1**2*a2*a4**3/2187 - 104*a1**2*a2*a4**2*a5/729 + 4*a1**2*a2*a4**2*a6/81 - 34*a1**2*a2*a4**2/243 - 38*a1**2*a2*a4*a5**2/243 - 10*a1**2*a2*a4*a5*a6/27 + 17*a1**2*a2*a4*a5/54 - 3*a1**2*a2*a4*a6**2 + 35*a1**2*a2*a4*a6/18 - a1**2*a2*a4/9 - 7*a1**2*a2*a5**3/27 - 25*a1**2*a2*a5**2*a6/18 + 19*a1**2*a2*a5**2/36 + 40*a1**2*a3*a4*a6**2/243 - 112*a1**2*a3*a4*a6/729 + 28*a1**2*a3*a4/729 + 28*a1**2*a3*a5**2*a6/243 - 110*a1**2*a3*a5**2/729 + 8*a1**2*a3*a5*a6**2/9 - 68*a1**2*a3*a5*a6/81 + 40*a1**2*a3*a5/243 + 4*a1**2*a3*a6**3/3 - 4*a1**2*a3*a6**2/3 + 4*a1**2*a3*a6/9 - 7*a1**2*a3/162 - 32*a1**2*a4**2*a5*a6/729 + 4*a1**2*a4**2*a5/81 + 16*a1**2*a4**2*a6**2/243 + 56*a1**2*a4**2*a6/729 - 2*a1**2*a4**2/81 - 4*a1**2*a4*a5**3/729 - 32*a1**2*a4*a5**2*a6/243 + 4*a1**2*a4*a5**2/729 - 40*a1**2*a4*a5*a6**2/81 + 82*a1**2*a4*a5*a6/243 - a1**2*a4*a5/27 + 16*a1**2*a4*a6**3/9 - 64*a1**2*a4*a6**2/27 + 23*a1**2*a4*a6/27 - 5*a1**2*a4/54 + 2*a1**2*a5**3*a6/27 - 7*a1**2*a5**3/81 - 5*a1**2*a5**2*a6**2/9 + 19*a1**2*a5**2*a6/54 + a1**2*a5**2/36 - 2*a1**2*a5*a6**3/3 + 13*a1**2*a5*a6**2/18 - 11*a1**2*a5*a6/18 + a1**2*a5/6 + 11*a1*a2**4*a3/2 - 4*a1*a2**3*a3**2/27 - 4*a1*a2**3*a3*a4/27 + 7*a1*a2**3*a3*a6/3 + 2*a1*a2**3*a3/3 + 2*a1*a2**3*a4**2/27 - 17*a1*a2**3*a4*a5/27 + 8*a1*a2**3*a4*a6/3 - 7*a1*a2**3*a4/6 + 25*a1*a2**3*a5**2/18 - 64*a1*a2**2*a3*a4*a6/243 + 40*a1*a2**2*a3*a4/243 - 112*a1*a2**2*a3*a5**2/729 - 52*a1*a2**2*a3*a5*a6/81 + 10*a1*a2**2*a3*a5/81 - 38*a1*a2**2*a3*a6**2/9 + 131*a1*a2**2*a3*a6/27 - 55*a1*a2**2*a3/54 - 4*a1*a2**2*a4**2*a5/2187 - 4*a1*a2**2*a4**2*a6/27 + 2*a1*a2**2*a4**2/27 - 92*a1*a2**2*a4*a5**2/729 + 4*a1*a2**2*a4*a5*a6/81 - 55*a1*a2**2*a4*a5/243 - a1*a2**2*a4*a6**2/9 + 55*a1*a2**2*a4*a6/54 - 2*a1*a2**2*a4/9 - 8*a1*a2**2*a5**3/243 - 5*a1*a2**2*a5**2*a6/3 + 5*a1*a2**2*a5**2/9 - 13*a1*a2**2*a5*a6**2/3 + 10*a1*a2**2*a5*a6/3 - a1*a2**2*a5/9 + 92*a1*a2*a3*a5*a6**2/243 - 242*a1*a2*a3*a5*a6/243 + 61*a1*a2*a3*a5/243 + 4*a1*a2*a3*a6**3/3 - 88*a1*a2*a3*a6**2/27 + 116*a1*a2*a3*a6/81 - 29*a1*a2*a3/162 - 56*a1*a2*a4**2*a6**2/729 + 160*a1*a2*a4**2*a6/2187 - 2*a1*a2*a4**2/243 - 88*a1*a2*a4*a5**2*a6/2187 + 170*a1*a2*a4*a5**2/2187 - 8*a1*a2*a4*a5*a6**2/81 + 58*a1*a2*a4*a5*a6/729 - a1*a2*a4*a5/81 - 52*a1*a2*a4*a6**3/27 + 68*a1*a2*a4*a6**2/27 - 203*a1*a2*a4*a6/243 + 7*a1*a2*a4/81 - 28*a1*a2*a5**4/2187 - 148*a1*a2*a5**3*a6/729 + 38*a1*a2*a5**3/729 + 44*a1*a2*a5**2*a6**2/81 - 232*a1*a2*a5**2*a6/243 + 97*a1*a2*a5**2/486 - 8*a1*a2*a5*a6**3/3 + 97*a1*a2*a5*a6**2/54 + 7*a1*a2*a5*a6/18 - 7*a1*a2*a5/36 - 8*a1*a2*a6**4 + 28*a1*a2*a6**3/3 - 143*a1*a2*a6**2/36 + 43*a1*a2*a6/36 - a1*a2/6 + 32*a1*a3*a6**4/81 - 68*a1*a3*a6**3/81 + 448*a1*a3*a6**2/729 - 146*a1*a3*a6/729 + 35*a1*a3/1458 + 32*a1*a4*a5*a6**3/729 - 308*a1*a4*a5*a6**2/2187 + 68*a1*a4*a5*a6/2187 - a1*a4*a5/2187 + 80*a1*a4*a6**4/81 - 160*a1*a4*a6**3/81 + 844*a1*a4*a6**2/729 - 8*a1*a4*a6/27 + 7*a1*a4/243 - 32*a1*a5**3*a6**2/729 + 152*a1*a5**3*a6/2187 - 5*a1*a5**3/729 - 112*a1*a5**2*a6**3/243 + 424*a1*a5**2*a6**2/729 - 53*a1*a5**2*a6/243 + 35*a1*a5**2/1458 + 8*a1*a5*a6**4/27 - 62*a1*a5*a6**3/81 + 35*a1*a5*a6**2/81 - 31*a1*a5*a6/243 + 7*a1*a5/486 - 4*a1*a6**5/3 + 4*a1*a6**4/3 + 16*a1*a6**3/27 - 26*a1*a6**2/27 + 17*a1*a6/54 - 7*a1/216 - 8*a2**5*a3/3 + 3*a2**5*a4/2 - 4*a2**4*a3*a4/243 + 32*a2**4*a3*a5/81 + 16*a2**4*a3*a6/9 - 46*a2**4*a3/27 - 4*a2**4*a4**2/27 + 4*a2**4*a4*a5/27 - 19*a2**4*a4*a6/9 + 7*a2**4*a4/9 + 20*a2**4*a5*a6/3 - 17*a2**4*a5/6 - 160*a2**3*a3*a5*a6/243 + 56*a2**3*a3*a5/81 + 28*a2**3*a3*a6/27 - 20*a2**3*a3/81 + 40*a2**3*a4**2*a6/729 - 28*a2**3*a4**2/729 - 20*a2**3*a4*a5**2/729 - 20*a2**3*a4*a5*a6/27 + 82*a2**3*a4*a5/243 + 38*a2**3*a4*a6**2/27 - 137*a2**3*a4*a6/81 + 20*a2**3*a4/81 - 8*a2**3*a5**2*a6/81 + 14*a2**3*a5**2/81 - 28*a2**3*a5*a6**2/9 + 26*a2**3*a5*a6/9 - 8*a2**3*a5/9 + 10*a2**3*a6**3 - 28*a2**3*a6**2/3 + 71*a2**3*a6/24 - 7*a2**3/12 - 80*a2**2*a3*a6**3/81 + 320*a2**2*a3*a6**2/243 - 127*a2**2*a3*a6/243 + 20*a2**2*a3/243 - 28*a2**2*a4*a5*a6**2/243 + 142*a2**2*a4*a5*a6/729 - 2*a2**2*a4*a5/243 - 116*a2**2*a4*a6**3/81 + 500*a2**2*a4*a6**2/243 - 58*a2**2*a4*a6/81 + 7*a2**2*a4/81 - 16*a2**2*a5**3*a6/243 + 40*a2**2*a5**3/729 - 64*a2**2*a5**2*a6**2/81 + 44*a2**2*a5**2*a6/81 - 2*a2**2*a5**2/27 + 20*a2**2*a5*a6**3/27 - 113*a2**2*a5*a6**2/81 + 77*a2**2*a5*a6/162 - 4*a2**2*a6**4 + 6*a2**2*a6**3 - 43*a2**2*a6**2/12 + 37*a2**2*a6/36 - a2**2/9 - 32*a2*a4*a6**4/243 + 140*a2*a4*a6**3/729 - 58*a2*a4*a6**2/729 + 10*a2*a4*a6/729 - 56*a2*a5**2*a6**3/243 + 34*a2*a5**2*a6**2/81 - 32*a2*a5**2*a6/243 + 2*a2*a5**2/243 - 200*a2*a5*a6**4/81 + 890*a2*a5*a6**3/243 - 413*a2*a5*a6**2/243 + 73*a2*a5*a6/243 - 7*a2*a5/486 + 8*a2*a6**5/9 - 64*a2*a6**4/27 + 137*a2*a6**3/81 - 77*a2*a6**2/162 + 4*a2*a6/81 - 16*a5*a6**5/81 + 40*a5*a6**4/81 - 236*a5*a6**3/729 + 62*a5*a6**2/729 - 2*a5*a6/243 - 16*a6**6/9 + 104*a6**5/27 - 242*a6**4/81 + 268*a6**3/243 - 97*a6**2/486 + 7*a6/486"
        &#93;,
        &#91;
          "-a0**2*a2*a3**3/18 - a0**2*a2*a3**2*a4/18 + a0**2*a3**2*a4*a6/18 - a0**2*a3**2*a4/324 - 7*a0**2*a3**2*a5**2/162 - 5*a0**2*a3**2*a5*a6/18 + a0**2*a3**2*a5/108 - a0**2*a3*a4**2*a5/486 + 4*a0**2*a3*a4**2*a6/27 - a0**2*a3*a4**2/162 - a0**2*a3*a4*a5**2/27 + 2*a0**2*a4**4/729 + a0**2*a4**3*a5/243 + a0*a1**2*a3**3/18 + a0*a1**2*a3**2*a4/18 - a0*a1*a2*a3**2*a4/6 + 7*a0*a1*a2*a3**2*a5/9 - 23*a0*a1*a2*a3*a4**2/54 - 17*a0*a1*a3**2*a5*a6/54 + 7*a0*a1*a3**2*a5/36 - a0*a1*a3**2*a6/6 + a0*a1*a3**2/18 - a0*a1*a3*a4**2/54 - 2*a0*a1*a3*a4*a5**2/81 - 7*a0*a1*a3*a4*a5*a6/18 + 17*a0*a1*a3*a4*a5/108 + a0*a1*a4**3*a5/81 + 2*a0*a1*a4**3*a6/81 + a0*a1*a4**2*a5**2/81 - a0*a2**2*a3**2*a5/3 + a0*a2**2*a3**2*a6 - a0*a2**2*a3**2/3 + a0*a2**2*a3*a4**2/81 - 11*a0*a2**2*a3*a4*a5/27 - 7*a0*a2*a3**2*a6**2/6 + 49*a0*a2*a3**2*a6/54 - 73*a0*a2*a3**2/648 - 2*a0*a2*a3*a4*a5*a6/27 - 47*a0*a2*a3*a4*a5/324 - 5*a0*a2*a3*a4*a6**2/6 + 47*a0*a2*a3*a4*a6/108 - 2*a0*a2*a3*a4/81 - a0*a2*a3*a5**3/81 - a0*a2*a3*a5**2*a6/3 - 11*a0*a2*a3*a5**2/81 - 2*a0*a2*a4**3*a6/243 + 35*a0*a2*a4**3/729 + a0*a2*a4**2*a5**2/81 + a0*a2*a4**2*a5*a6/81 + 35*a0*a2*a4**2*a5/486 + a0*a2*a4*a5**3/81 - 7*a0*a3*a4*a6**3/27 - 4*a0*a3*a4*a6**2/27 + 17*a0*a3*a4*a6/108 - 7*a0*a3*a4/324 + a0*a3*a5**2*a6**2/81 - a0*a3*a5**2*a6/81 - 5*a0*a3*a5**2/648 - 5*a0*a3*a5*a6**3/9 - 4*a0*a3*a5*a6**2/27 + 7*a0*a3*a5*a6/36 - 7*a0*a3*a5/216 - a0*a4**2*a5*a6**2/243 + 19*a0*a4**2*a5*a6/243 - a0*a4**2*a5/54 - 2*a0*a4**2*a6**3/27 - 5*a0*a4**2*a6**2/81 + a0*a4**2*a6/27 + a0*a4*a5**3*a6/243 - 13*a0*a4*a5**3/972 + a0*a4*a5**2*a6**2/27 + 49*a0*a4*a5**2*a6/324 - a0*a4*a5**2/27 - 2*a0*a5**4/81 + a1**3*a3**2*a4/9 - a1**3*a3**2*a5/3 + 2*a1**3*a3*a4**2/9 + a1**2*a2*a3**2*a5/3 - a1**2*a2*a3**2*a6/2 + a1**2*a2*a3**2/4 + 7*a1**2*a2*a3*a4*a5/18 - 4*a1**2*a3**2*a6**2/9 + a1**2*a3**2*a6/2 - 7*a1**2*a3**2/54 + 7*a1**2*a3*a4*a5/54 - 10*a1**2*a3*a4*a6**2/9 + 2*a1**2*a3*a4*a6/3 - 11*a1**2*a3*a4/108 - a1**2*a3*a5**3/54 + a1**2*a3*a5**2*a6/6 + 19*a1**2*a3*a5**2/108 - 10*a1**2*a4**3/243 + a1**2*a4**2*a5**2/81 + 2*a1**2*a4**2*a5*a6/27 - 5*a1**2*a4**2*a5/81 + 13*a1*a2**2*a3**2*a6/9 - 37*a1*a2**2*a3**2/54 + 2*a1*a2**2*a3*a4*a5/27 + 16*a1*a2**2*a3*a4*a6/9 - 14*a1*a2**2*a3*a4/27 + 2*a1*a2**2*a3*a5**2/27 - 2*a1*a2**2*a4**3/243 - a1*a2**2*a4**2*a5/81 + 4*a1*a2*a3*a4*a6**2/9 + 91*a1*a2*a3*a4*a6/162 - 11*a1*a2*a3*a4/54 - 5*a1*a2*a3*a5**2*a6/27 + 5*a1*a2*a3*a5**2/108 + a1*a2*a3*a5*a6**2/9 + 5*a1*a2*a3*a5*a6/4 - 5*a1*a2*a3*a5/24 - a1*a2*a4**2*a5*a6/81 - 35*a1*a2*a4**2*a5/486 + 2*a1*a2*a4**2*a6**2/27 + 5*a1*a2*a4**2*a6/81 - a1*a2*a4**2/18 + 2*a1*a2*a4*a5**3/81 + a1*a2*a4*a5**2*a6/9 - 10*a1*a2*a4*a5**2/81 - a1*a3*a5*a6**3/27 + 2*a1*a3*a5*a6**2/27 - 25*a1*a3*a5*a6/324 + a1*a3*a5/36 + a1*a3*a6**3/3 - 7*a1*a3*a6**2/36 + a1*a3*a6/24 - a1*a3/216 + 4*a1*a4**2*a6**3/81 + 16*a1*a4**2*a6**2/81 - 41*a1*a4**2*a6/486 + 2*a1*a4**2/243 - a1*a4*a5**2*a6**2/27 - 16*a1*a4*a5**2*a6/243 + 7*a1*a4*a5**2/486 + 11*a1*a4*a5*a6**2/27 - 71*a1*a4*a5*a6/324 + 13*a1*a4*a5/324 + a1*a5**4*a6/81 - a1*a5**4/972 + a1*a5**3*a6**2/27 - 43*a1*a5**3*a6/324 + 23*a1*a5**3/648 - 7*a2**4*a3**2/18 - 7*a2**4*a3*a4/18 - 2*a2**3*a3*a4*a6/27 - 37*a2**3*a3*a4/81 + 23*a2**3*a3*a5**2/162 + 5*a2**3*a3*a5*a6/6 - 139*a2**3*a3*a5/108 - 5*a2**3*a4**2*a5/243 - 2*a2**3*a4**2*a6/27 + a2**3*a4**2/9 - a2**3*a4*a5**2/81 + 7*a2**2*a3*a5*a6**2/54 + 8*a2**2*a3*a5*a6/81 - 41*a2**2*a3*a5/216 + 3*a2**2*a3*a6**3/2 - 9*a2**2*a3*a6**2/4 + a2**2*a3*a6 - 37*a2**2*a3/216 - 2*a2**2*a4**2*a6**2/81 - 8*a2**2*a4**2*a6/27 + 23*a2**2*a4**2/243 - 2*a2**2*a4*a5**2*a6/243 - 23*a2**2*a4*a5**2/972 + a2**2*a4*a5*a6**2/9 - 49*a2**2*a4*a5*a6/324 - 2*a2**2*a4*a5/81 + 4*a2**2*a5**4/243 + 4*a2**2*a5**3*a6/81 - 5*a2**2*a5**3/54 - a2*a3*a6**4/9 + 37*a2*a3*a6**3/54 - 305*a2*a3*a6**2/324 + 239*a2*a3*a6/648 - 25*a2*a3/648 - a2*a4*a5*a6**3/9 - 157*a2*a4*a5*a6**2/486 + 215*a2*a4*a5*a6/972 - 7*a2*a4*a5/243 + 2*a2*a4*a6**4/9 + 2*a2*a4*a6**3/27 - 43*a2*a4*a6**2/162 + 7*a2*a4*a6/108 + 2*a2*a5**3*a6**2/27 - 19*a2*a5**3*a6/972 - a2*a5**3/108 + 2*a2*a5**2*a6**3/9 - 221*a2*a5**2*a6**2/324 + 65*a2*a5**2*a6/216 - 7*a2*a5**2/648 - 4*a4*a6**5/27 - 8*a4*a6**4/81 + 25*a4*a6**3/162 - 13*a4*a6**2/324 + a4*a6/324 + 2*a5**2*a6**4/27 - 2*a5**2*a6**3/27 + a5**2*a6**2/36 - a5**2*a6/162 + 2*a5*a6**5/9 - 20*a5*a6**4/27 + 7*a5*a6**3/12 - 37*a5*a6**2/216 + a5*a6/54",
          "-a0**2*a2*a3**3/4 + a0**2*a3**2*a4*a6/4 - a0**2*a3**2*a4/72 - 7*a0**2*a3**2*a5**2/36 - a0**2*a3*a4**2*a5/108 + a0**2*a4**4/81 + a0*a1**2*a3**3/4 - 3*a0*a1*a2*a3**2*a4/4 - 17*a0*a1*a3**2*a5*a6/12 + 7*a0*a1*a3**2*a5/8 - a0*a1*a3*a4**2/12 - a0*a1*a3*a4*a5**2/9 + a0*a1*a4**3*a5/18 - 3*a0*a2**2*a3**2*a5/2 + a0*a2**2*a3*a4**2/18 - 21*a0*a2*a3**2*a6**2/4 + 49*a0*a2*a3**2*a6/12 - 73*a0*a2*a3**2/144 - a0*a2*a3*a4*a5*a6/3 - 47*a0*a2*a3*a4*a5/72 - a0*a2*a3*a5**3/18 - a0*a2*a4**3*a6/27 + 35*a0*a2*a4**3/162 + a0*a2*a4**2*a5**2/18 - 7*a0*a3*a4*a6**3/6 - 2*a0*a3*a4*a6**2/3 + 17*a0*a3*a4*a6/24 - 7*a0*a3*a4/72 + a0*a3*a5**2*a6**2/18 - a0*a3*a5**2*a6/18 - 5*a0*a3*a5**2/144 - a0*a4**2*a5*a6**2/54 + 19*a0*a4**2*a5*a6/54 - a0*a4**2*a5/12 + a0*a4*a5**3*a6/54 - 13*a0*a4*a5**3/216 + a1**3*a3**2*a4/2 + 3*a1**2*a2*a3**2*a5/2 - 2*a1**2*a3**2*a6**2 + 9*a1**2*a3**2*a6/4 - 7*a1**2*a3**2/12 + 7*a1**2*a3*a4*a5/12 - a1**2*a3*a5**3/12 - 5*a1**2*a4**3/27 + a1**2*a4**2*a5**2/18 + 13*a1*a2**2*a3**2*a6/2 - 37*a1*a2**2*a3**2/12 + a1*a2**2*a3*a4*a5/3 - a1*a2**2*a4**3/27 + 2*a1*a2*a3*a4*a6**2 + 91*a1*a2*a3*a4*a6/36 - 11*a1*a2*a3*a4/12 - 5*a1*a2*a3*a5**2*a6/6 + 5*a1*a2*a3*a5**2/24 - a1*a2*a4**2*a5*a6/18 - 35*a1*a2*a4**2*a5/108 + a1*a2*a4*a5**3/9 - a1*a3*a5*a6**3/6 + a1*a3*a5*a6**2/3 - 25*a1*a3*a5*a6/72 + a1*a3*a5/8 + 2*a1*a4**2*a6**3/9 + 8*a1*a4**2*a6**2/9 - 41*a1*a4**2*a6/108 + a1*a4**2/27 - a1*a4*a5**2*a6**2/6 - 8*a1*a4*a5**2*a6/27 + 7*a1*a4*a5**2/108 + a1*a5**4*a6/18 - a1*a5**4/216 - 7*a2**4*a3**2/4 - a2**3*a3*a4*a6/3 - 37*a2**3*a3*a4/18 + 23*a2**3*a3*a5**2/36 - 5*a2**3*a4**2*a5/54 + 7*a2**2*a3*a5*a6**2/12 + 4*a2**2*a3*a5*a6/9 - 41*a2**2*a3*a5/48 - a2**2*a4**2*a6**2/9 - 4*a2**2*a4**2*a6/3 + 23*a2**2*a4**2/54 - a2**2*a4*a5**2*a6/27 - 23*a2**2*a4*a5**2/216 + 2*a2**2*a5**4/27 - a2*a3*a6**4/2 + 37*a2*a3*a6**3/12 - 305*a2*a3*a6**2/72 + 239*a2*a3*a6/144 - 25*a2*a3/144 - a2*a4*a5*a6**3/2 - 157*a2*a4*a5*a6**2/108 + 215*a2*a4*a5*a6/216 - 7*a2*a4*a5/54 + a2*a5**3*a6**2/3 - 19*a2*a5**3*a6/216 - a2*a5**3/24 - 2*a4*a6**5/3 - 4*a4*a6**4/9 + 25*a4*a6**3/36 - 13*a4*a6**2/72 + a4*a6/72 + a5**2*a6**4/3 - a5**2*a6**3/3 + a5**2*a6**2/8 - a5**2*a6/36",
          "a0**2*a2*a3**3/27 + a0**2*a2*a3**2*a4/27 + 2*a0**2*a2*a3**2*a5/9 - a0**2*a2*a3*a4**2/18 - a0**2*a3**2*a4*a6/27 + a0**2*a3**2*a4/486 + 7*a0**2*a3**2*a5**2/243 + 5*a0**2*a3**2*a5*a6/27 - a0**2*a3**2*a5/162 + 4*a0**2*a3**2*a6**2/3 - 5*a0**2*a3**2*a6/9 + 7*a0**2*a3**2/108 + a0**2*a3*a4**2*a5/729 - 8*a0**2*a3*a4**2*a6/81 + a0**2*a3*a4**2/243 + 2*a0**2*a3*a4*a5**2/81 - 5*a0**2*a3*a4*a5*a6/18 + 13*a0**2*a3*a4*a5/324 + 5*a0**2*a3*a5**3/81 - 4*a0**2*a4**4/2187 - 2*a0**2*a4**3*a5/729 - 2*a0**2*a4**3*a6/81 + 2*a0**2*a4**3/243 + a0**2*a4**2*a5**2/243 - a0*a1**2*a3**3/27 - a0*a1**2*a3**2*a4/27 - a0*a1**2*a3**2*a5/18 + a0*a1*a2*a3**2*a4/9 - 14*a0*a1*a2*a3**2*a5/27 - 7*a0*a1*a2*a3**2*a6/3 + 4*a0*a1*a2*a3**2/9 + 23*a0*a1*a2*a3*a4**2/81 + 17*a0*a1*a2*a3*a4*a5/54 + a0*a1*a2*a4**3/27 + 17*a0*a1*a3**2*a5*a6/81 - 7*a0*a1*a3**2*a5/54 + a0*a1*a3**2*a6/9 - a0*a1*a3**2/27 + a0*a1*a3*a4**2/81 + 4*a0*a1*a3*a4*a5**2/243 + 7*a0*a1*a3*a4*a5*a6/27 - 17*a0*a1*a3*a4*a5/162 - a0*a1*a3*a4*a6**2/9 + a0*a1*a3*a4*a6/27 + a0*a1*a3*a4/108 + 17*a0*a1*a3*a5**2*a6/54 - 17*a0*a1*a3*a5**2/108 - 2*a0*a1*a4**3*a5/243 - 4*a0*a1*a4**3*a6/243 - 2*a0*a1*a4**2*a5**2/243 - 5*a0*a1*a4**2*a5*a6/81 + a0*a1*a4**2*a5/54 + a0*a1*a4*a5**3/81 + a0*a2**3*a3**2 + 2*a0*a2**2*a3**2*a5/9 - 2*a0*a2**2*a3**2*a6/3 + 2*a0*a2**2*a3**2/9 - 2*a0*a2**2*a3*a4**2/243 + 22*a0*a2**2*a3*a4*a5/81 + 2*a0*a2**2*a3*a4*a6/9 - 11*a0*a2**2*a3*a4/108 + 4*a0*a2**2*a3*a5**2/9 + a0*a2**2*a4**2*a5/27 + 7*a0*a2*a3**2*a6**2/9 - 49*a0*a2*a3**2*a6/81 + 73*a0*a2*a3**2/972 + 4*a0*a2*a3*a4*a5*a6/81 + 47*a0*a2*a3*a4*a5/486 + 5*a0*a2*a3*a4*a6**2/9 - 47*a0*a2*a3*a4*a6/162 + 4*a0*a2*a3*a4/243 + 2*a0*a2*a3*a5**3/243 + 2*a0*a2*a3*a5**2*a6/9 + 22*a0*a2*a3*a5**2/243 + 5*a0*a2*a3*a5*a6**2/2 - 8*a0*a2*a3*a5*a6/9 + 11*a0*a2*a3*a5/216 + 4*a0*a2*a4**3*a6/729 - 70*a0*a2*a4**3/2187 - 2*a0*a2*a4**2*a5**2/243 - 2*a0*a2*a4**2*a5*a6/243 - 35*a0*a2*a4**2*a5/729 - a0*a2*a4**2*a6**2/27 - 41*a0*a2*a4**2*a6/162 + 25*a0*a2*a4**2/486 - 2*a0*a2*a4*a5**3/243 - a0*a2*a4*a5**2*a6/27 + 43*a0*a2*a4*a5**2/972 + a0*a2*a5**4/81 + 14*a0*a3*a4*a6**3/81 + 8*a0*a3*a4*a6**2/81 - 17*a0*a3*a4*a6/162 + 7*a0*a3*a4/486 - 2*a0*a3*a5**2*a6**2/243 + 2*a0*a3*a5**2*a6/243 + 5*a0*a3*a5**2/972 + 10*a0*a3*a5*a6**3/27 + 8*a0*a3*a5*a6**2/81 - 7*a0*a3*a5*a6/54 + 7*a0*a3*a5/324 + 8*a0*a3*a6**4/3 - 13*a0*a3*a6**3/9 + 11*a0*a3*a6**2/108 + 13*a0*a3*a6/216 - a0*a3/108 + 2*a0*a4**2*a5*a6**2/729 - 38*a0*a4**2*a5*a6/729 + a0*a4**2*a5/81 + 4*a0*a4**2*a6**3/81 + 10*a0*a4**2*a6**2/243 - 2*a0*a4**2*a6/81 - 2*a0*a4*a5**3*a6/729 + 13*a0*a4*a5**3/1458 - 2*a0*a4*a5**2*a6**2/81 - 49*a0*a4*a5**2*a6/486 + 2*a0*a4*a5**2/81 - a0*a4*a5*a6**3/9 - 31*a0*a4*a5*a6**2/162 + 25*a0*a4*a5*a6/324 - a0*a4*a5/108 + 4*a0*a5**4/243 + 2*a0*a5**3*a6**2/81 + a0*a5**3*a6/27 - a0*a5**3/216 - 2*a1**3*a3**2*a4/27 + 2*a1**3*a3**2*a5/9 + a1**3*a3**2*a6 - a1**3*a3**2/6 - 4*a1**3*a3*a4**2/27 - 2*a1**3*a3*a4*a5/9 - a1**2*a2**2*a3**2/2 - 2*a1**2*a2*a3**2*a5/9 + a1**2*a2*a3**2*a6/3 - a1**2*a2*a3**2/6 - 7*a1**2*a2*a3*a4*a5/27 - 2*a1**2*a2*a3*a4*a6/3 + 2*a1**2*a2*a3*a4/9 - 5*a1**2*a2*a3*a5**2/9 + a1**2*a2*a4**2*a5/9 + 8*a1**2*a3**2*a6**2/27 - a1**2*a3**2*a6/3 + 7*a1**2*a3**2/81 - 7*a1**2*a3*a4*a5/81 + 20*a1**2*a3*a4*a6**2/27 - 4*a1**2*a3*a4*a6/9 + 11*a1**2*a3*a4/162 + a1**2*a3*a5**3/81 - a1**2*a3*a5**2*a6/9 - 19*a1**2*a3*a5**2/162 - 5*a1**2*a3*a5*a6**2/9 - 4*a1**2*a3*a5*a6/9 + a1**2*a3*a5/6 + 20*a1**2*a4**3/729 - 2*a1**2*a4**2*a5**2/243 - 4*a1**2*a4**2*a5*a6/81 + 10*a1**2*a4**2*a5/243 + 2*a1**2*a4**2*a6/9 - 4*a1**2*a4**2/81 + a1**2*a4*a5**2*a6/27 - 7*a1**2*a4*a5**2/162 + a1*a2**3*a3*a4/3 - 26*a1*a2**2*a3**2*a6/27 + 37*a1*a2**2*a3**2/81 - 4*a1*a2**2*a3*a4*a5/81 - 32*a1*a2**2*a3*a4*a6/27 + 28*a1*a2**2*a3*a4/81 - 4*a1*a2**2*a3*a5**2/81 - 3*a1*a2**2*a3*a5*a6 + 73*a1*a2**2*a3*a5/108 + 4*a1*a2**2*a4**3/729 + 2*a1*a2**2*a4**2*a5/243 + 5*a1*a2**2*a4**2*a6/27 + 4*a1*a2**2*a4**2/81 + 17*a1*a2**2*a4*a5**2/81 - 8*a1*a2*a3*a4*a6**2/27 - 91*a1*a2*a3*a4*a6/243 + 11*a1*a2*a3*a4/81 + 10*a1*a2*a3*a5**2*a6/81 - 5*a1*a2*a3*a5**2/162 - 2*a1*a2*a3*a5*a6**2/27 - 5*a1*a2*a3*a5*a6/6 + 5*a1*a2*a3*a5/36 - 13*a1*a2*a3*a6**3/3 - 13*a1*a2*a3*a6**2/18 + 11*a1*a2*a3*a6/12 - 5*a1*a2*a3/36 + 2*a1*a2*a4**2*a5*a6/243 + 35*a1*a2*a4**2*a5/729 - 4*a1*a2*a4**2*a6**2/81 - 10*a1*a2*a4**2*a6/243 + a1*a2*a4**2/27 - 4*a1*a2*a4*a5**3/243 - 2*a1*a2*a4*a5**2*a6/27 + 20*a1*a2*a4*a5**2/243 + 4*a1*a2*a4*a5*a6**2/27 + 47*a1*a2*a4*a5*a6/162 - 4*a1*a2*a4*a5/81 + 4*a1*a2*a5**3*a6/27 - 29*a1*a2*a5**3/324 + 2*a1*a3*a5*a6**3/81 - 4*a1*a3*a5*a6**2/81 + 25*a1*a3*a5*a6/486 - a1*a3*a5/54 - 2*a1*a3*a6**3/9 + 7*a1*a3*a6**2/54 - a1*a3*a6/36 + a1*a3/324 - 8*a1*a4**2*a6**3/243 - 32*a1*a4**2*a6**2/243 + 41*a1*a4**2*a6/729 - 4*a1*a4**2/729 + 2*a1*a4*a5**2*a6**2/81 + 32*a1*a4*a5**2*a6/729 - 7*a1*a4*a5**2/729 - 22*a1*a4*a5*a6**2/81 + 71*a1*a4*a5*a6/486 - 13*a1*a4*a5/486 - 4*a1*a4*a6**4/9 - 20*a1*a4*a6**3/27 + 11*a1*a4*a6**2/18 - 13*a1*a4*a6/81 + 5*a1*a4/324 - 2*a1*a5**4*a6/243 + a1*a5**4/1458 - 2*a1*a5**3*a6**2/81 + 43*a1*a5**3*a6/486 - 23*a1*a5**3/972 + 7*a1*a5**2*a6**3/27 + 5*a1*a5**2*a6**2/54 - 2*a1*a5**2*a6/27 + a1*a5**2/216 + 7*a2**4*a3**2/27 + 7*a2**4*a3*a4/27 + 14*a2**4*a3*a5/9 - a2**4*a4**2/9 + 4*a2**3*a3*a4*a6/81 + 74*a2**3*a3*a4/243 - 23*a2**3*a3*a5**2/243 - 5*a2**3*a3*a5*a6/9 + 139*a2**3*a3*a5/162 + 5*a2**3*a3*a6**2/2 + 7*a2**3*a3*a6/9 - 25*a2**3*a3/108 + 10*a2**3*a4**2*a5/729 + 4*a2**3*a4**2*a6/81 - 2*a2**3*a4**2/27 + 2*a2**3*a4*a5**2/243 + 7*a2**3*a4*a5*a6/27 - 5*a2**3*a4*a5/324 + 11*a2**3*a5**3/81 - 7*a2**2*a3*a5*a6**2/81 - 16*a2**2*a3*a5*a6/243 + 41*a2**2*a3*a5/324 - a2**2*a3*a6**3 + 3*a2**2*a3*a6**2/2 - 2*a2**2*a3*a6/3 + 37*a2**2*a3/324 + 4*a2**2*a4**2*a6**2/243 + 16*a2**2*a4**2*a6/81 - 46*a2**2*a4**2/729 + 4*a2**2*a4*a5**2*a6/729 + 23*a2**2*a4*a5**2/1458 - 2*a2**2*a4*a5*a6**2/27 + 49*a2**2*a4*a5*a6/486 + 4*a2**2*a4*a5/243 + 5*a2**2*a4*a6**3/9 + 53*a2**2*a4*a6**2/54 - 67*a2**2*a4*a6/108 + 23*a2**2*a4/324 - 8*a2**2*a5**4/729 - 8*a2**2*a5**3*a6/243 + 5*a2**2*a5**3/81 + a2**2*a5**2*a6**2 - 181*a2**2*a5**2*a6/324 + 97*a2**2*a5**2/648 + 2*a2*a3*a6**4/27 - 37*a2*a3*a6**3/81 + 305*a2*a3*a6**2/486 - 239*a2*a3*a6/972 + 25*a2*a3/972 + 2*a2*a4*a5*a6**3/27 + 157*a2*a4*a5*a6**2/729 - 215*a2*a4*a5*a6/1458 + 14*a2*a4*a5/729 - 4*a2*a4*a6**4/27 - 4*a2*a4*a6**3/81 + 43*a2*a4*a6**2/243 - 7*a2*a4*a6/162 - 4*a2*a5**3*a6**2/81 + 19*a2*a5**3*a6/1458 + a2*a5**3/162 - 4*a2*a5**2*a6**3/27 + 221*a2*a5**2*a6**2/486 - 65*a2*a5**2*a6/324 + 7*a2*a5**2/972 + 19*a2*a5*a6**4/9 - 10*a2*a5*a6**3/9 + a2*a5*a6**2/6 - 19*a2*a5*a6/324 + 7*a2*a5/648 + 8*a4*a6**5/81 + 16*a4*a6**4/243 - 25*a4*a6**3/243 + 13*a4*a6**2/486 - a4*a6/486 - 4*a5**2*a6**4/81 + 4*a5**2*a6**3/81 - a5**2*a6**2/54 + a5**2*a6/243 - 4*a5*a6**5/27 + 40*a5*a6**4/81 - 7*a5*a6**3/18 + 37*a5*a6**2/324 - a5*a6/81 + 4*a6**6/3 - 8*a6**5/9 - 7*a6**4/54 + 23*a6**3/108 - a6**2/18 + a6/216",
          "a0**2*a1*a3**2*a5/6 - a0**2*a1*a3*a4**2/18 - 2*a0**2*a2*a3**3/81 - 2*a0**2*a2*a3**2*a4/81 - 4*a0**2*a2*a3**2*a5/27 + 7*a0**2*a2*a3**2*a6/6 - 5*a0**2*a2*a3**2/18 + a0**2*a2*a3*a4**2/27 - 2*a0**2*a2*a3*a4*a5/27 - 2*a0**2*a2*a4**3/81 + 2*a0**2*a3**2*a4*a6/81 - a0**2*a3**2*a4/729 - 14*a0**2*a3**2*a5**2/729 - 10*a0**2*a3**2*a5*a6/81 + a0**2*a3**2*a5/243 - 8*a0**2*a3**2*a6**2/9 + 10*a0**2*a3**2*a6/27 - 7*a0**2*a3**2/162 - 2*a0**2*a3*a4**2*a5/2187 + 16*a0**2*a3*a4**2*a6/243 - 2*a0**2*a3*a4**2/729 - 4*a0**2*a3*a4*a5**2/243 + 5*a0**2*a3*a4*a5*a6/27 - 13*a0**2*a3*a4*a5/486 + 11*a0**2*a3*a4*a6**2/18 - 29*a0**2*a3*a4*a6/108 + a0**2*a3*a4/36 - 10*a0**2*a3*a5**3/243 - 5*a0**2*a3*a5**2*a6/27 + a0**2*a3*a5**2/18 + 8*a0**2*a4**4/6561 + 4*a0**2*a4**3*a5/2187 + 4*a0**2*a4**3*a6/243 - 4*a0**2*a4**3/729 - 2*a0**2*a4**2*a5**2/729 - a0**2*a4**2*a5*a6/81 + 2*a0*a1**2*a3**3/81 + 2*a0*a1**2*a3**2*a4/81 + a0*a1**2*a3**2*a5/27 + a0*a1**2*a3**2*a6/6 - a0*a1**2*a3*a4*a5/9 + a0*a1**2*a4**3/27 - 4*a0*a1*a2**2*a3**2/3 - 2*a0*a1*a2*a3**2*a4/27 + 28*a0*a1*a2*a3**2*a5/81 + 14*a0*a1*a2*a3**2*a6/9 - 8*a0*a1*a2*a3**2/27 - 46*a0*a1*a2*a3*a4**2/243 - 17*a0*a1*a2*a3*a4*a5/81 - 19*a0*a1*a2*a3*a4*a6/18 + 11*a0*a1*a2*a3*a4/36 - 2*a0*a1*a2*a4**3/81 - a0*a1*a2*a4**2*a5/27 - 34*a0*a1*a3**2*a5*a6/243 + 7*a0*a1*a3**2*a5/81 - 2*a0*a1*a3**2*a6/27 + 2*a0*a1*a3**2/81 - 2*a0*a1*a3*a4**2/243 - 8*a0*a1*a3*a4*a5**2/729 - 14*a0*a1*a3*a4*a5*a6/81 + 17*a0*a1*a3*a4*a5/243 + 2*a0*a1*a3*a4*a6**2/27 - 2*a0*a1*a3*a4*a6/81 - a0*a1*a3*a4/162 - 17*a0*a1*a3*a5**2*a6/81 + 17*a0*a1*a3*a5**2/162 - 11*a0*a1*a3*a5*a6**2/18 + 7*a0*a1*a3*a5*a6/12 - a0*a1*a3*a5/9 + 4*a0*a1*a4**3*a5/729 + 8*a0*a1*a4**3*a6/729 + 4*a0*a1*a4**2*a5**2/729 + 10*a0*a1*a4**2*a5*a6/243 - a0*a1*a4**2*a5/81 - 4*a0*a1*a4**2*a6**2/27 + 2*a0*a1*a4**2*a6/27 - a0*a1*a4**2/54 - 2*a0*a1*a4*a5**3/243 - a0*a1*a4*a5**2/108 - 2*a0*a2**3*a3**2/3 - a0*a2**3*a3*a4/9 - 4*a0*a2**2*a3**2*a5/27 + 4*a0*a2**2*a3**2*a6/9 - 4*a0*a2**2*a3**2/27 + 4*a0*a2**2*a3*a4**2/729 - 44*a0*a2**2*a3*a4*a5/243 - 4*a0*a2**2*a3*a4*a6/27 + 11*a0*a2**2*a3*a4/162 - 8*a0*a2**2*a3*a5**2/27 - a0*a2**2*a3*a5*a6/3 + 17*a0*a2**2*a3*a5/27 - 2*a0*a2**2*a4**2*a5/81 + 2*a0*a2**2*a4**2*a6/27 - 43*a0*a2**2*a4**2/162 - 2*a0*a2**2*a4*a5**2/27 - 14*a0*a2*a3**2*a6**2/27 + 98*a0*a2*a3**2*a6/243 - 73*a0*a2*a3**2/1458 - 8*a0*a2*a3*a4*a5*a6/243 - 47*a0*a2*a3*a4*a5/729 - 10*a0*a2*a3*a4*a6**2/27 + 47*a0*a2*a3*a4*a6/243 - 8*a0*a2*a3*a4/729 - 4*a0*a2*a3*a5**3/729 - 4*a0*a2*a3*a5**2*a6/27 - 44*a0*a2*a3*a5**2/729 - 5*a0*a2*a3*a5*a6**2/3 + 16*a0*a2*a3*a5*a6/27 - 11*a0*a2*a3*a5/324 - 5*a0*a2*a3*a6**3/6 + 7*a0*a2*a3*a6**2/3 - 193*a0*a2*a3*a6/216 + 7*a0*a2*a3/72 - 8*a0*a2*a4**3*a6/2187 + 140*a0*a2*a4**3/6561 + 4*a0*a2*a4**2*a5**2/729 + 4*a0*a2*a4**2*a5*a6/729 + 70*a0*a2*a4**2*a5/2187 + 2*a0*a2*a4**2*a6**2/81 + 41*a0*a2*a4**2*a6/243 - 25*a0*a2*a4**2/729 + 4*a0*a2*a4*a5**3/729 + 2*a0*a2*a4*a5**2*a6/81 - 43*a0*a2*a4*a5**2/1458 - 2*a0*a2*a4*a5*a6**2/27 - 65*a0*a2*a4*a5*a6/162 + 5*a0*a2*a4*a5/54 - 2*a0*a2*a5**4/243 - a0*a2*a5**3*a6/27 + a0*a2*a5**3/18 - 28*a0*a3*a4*a6**3/243 - 16*a0*a3*a4*a6**2/243 + 17*a0*a3*a4*a6/243 - 7*a0*a3*a4/729 + 4*a0*a3*a5**2*a6**2/729 - 4*a0*a3*a5**2*a6/729 - 5*a0*a3*a5**2/1458 - 20*a0*a3*a5*a6**3/81 - 16*a0*a3*a5*a6**2/243 + 7*a0*a3*a5*a6/81 - 7*a0*a3*a5/486 - 16*a0*a3*a6**4/9 + 26*a0*a3*a6**3/27 - 11*a0*a3*a6**2/162 - 13*a0*a3*a6/324 + a0*a3/162 - 4*a0*a4**2*a5*a6**2/2187 + 76*a0*a4**2*a5*a6/2187 - 2*a0*a4**2*a5/243 - 8*a0*a4**2*a6**3/243 - 20*a0*a4**2*a6**2/729 + 4*a0*a4**2*a6/243 + 4*a0*a4*a5**3*a6/2187 - 13*a0*a4*a5**3/2187 + 4*a0*a4*a5**2*a6**2/243 + 49*a0*a4*a5**2*a6/729 - 4*a0*a4*a5**2/243 + 2*a0*a4*a5*a6**3/27 + 31*a0*a4*a5*a6**2/243 - 25*a0*a4*a5*a6/486 + a0*a4*a5/162 + a0*a4*a6**4/9 - 11*a0*a4*a6**3/27 + 37*a0*a4*a6**2/108 - 11*a0*a4*a6/108 + a0*a4/108 - 8*a0*a5**4/729 - 4*a0*a5**3*a6**2/243 - 2*a0*a5**3*a6/81 + a0*a5**3/324 - 2*a0*a5**2*a6**3/27 + 2*a0*a5**2*a6**2/27 - a0*a5**2*a6/24 + a0*a5**2/108 + a1**3*a2*a3**2/2 + 4*a1**3*a3**2*a4/81 - 4*a1**3*a3**2*a5/27 - 2*a1**3*a3**2*a6/3 + a1**3*a3**2/9 + 8*a1**3*a3*a4**2/81 + 4*a1**3*a3*a4*a5/27 - a1**3*a3*a5**2/6 + a1**3*a4**2*a5/9 + a1**2*a2**2*a3**2/3 + a1**2*a2**2*a3*a4/3 + 4*a1**2*a2*a3**2*a5/27 - 2*a1**2*a2*a3**2*a6/9 + a1**2*a2*a3**2/9 + 14*a1**2*a2*a3*a4*a5/81 + 4*a1**2*a2*a3*a4*a6/9 - 4*a1**2*a2*a3*a4/27 + 10*a1**2*a2*a3*a5**2/27 - 7*a1**2*a2*a3*a5*a6/6 - 7*a1**2*a2*a3*a5/12 - 2*a1**2*a2*a4**2*a5/27 + a1**2*a2*a4**2*a6/9 + 5*a1**2*a2*a4**2/18 + 2*a1**2*a2*a4*a5**2/9 - 16*a1**2*a3**2*a6**2/81 + 2*a1**2*a3**2*a6/9 - 14*a1**2*a3**2/243 + 14*a1**2*a3*a4*a5/243 - 40*a1**2*a3*a4*a6**2/81 + 8*a1**2*a3*a4*a6/27 - 11*a1**2*a3*a4/243 - 2*a1**2*a3*a5**3/243 + 2*a1**2*a3*a5**2*a6/27 + 19*a1**2*a3*a5**2/243 + 10*a1**2*a3*a5*a6**2/27 + 8*a1**2*a3*a5*a6/27 - a1**2*a3*a5/9 - 4*a1**2*a3*a6**3/3 + 2*a1**2*a3*a6**2 - 8*a1**2*a3*a6/9 + a1**2*a3/9 - 40*a1**2*a4**3/2187 + 4*a1**2*a4**2*a5**2/729 + 8*a1**2*a4**2*a5*a6/243 - 20*a1**2*a4**2*a5/729 - 4*a1**2*a4**2*a6/27 + 8*a1**2*a4**2/243 - 2*a1**2*a4*a5**2*a6/81 + 7*a1**2*a4*a5**2/243 - 2*a1**2*a4*a5*a6**2/9 + 2*a1**2*a4*a5*a6/27 - a1**2*a4*a5/36 + a1**2*a5**3*a6/9 - a1**2*a5**3/108 - 2*a1*a2**3*a3*a4/9 + 17*a1*a2**3*a3*a5/18 - a1*a2**3*a4**2/27 + 52*a1*a2**2*a3**2*a6/81 - 74*a1*a2**2*a3**2/243 + 8*a1*a2**2*a3*a4*a5/243 + 64*a1*a2**2*a3*a4*a6/81 - 56*a1*a2**2*a3*a4/243 + 8*a1*a2**2*a3*a5**2/243 + 2*a1*a2**2*a3*a5*a6 - 73*a1*a2**2*a3*a5/162 + 3*a1*a2**2*a3*a6**2/2 - 65*a1*a2**2*a3*a6/9 + 29*a1*a2**2*a3/18 - 8*a1*a2**2*a4**3/2187 - 4*a1*a2**2*a4**2*a5/729 - 10*a1*a2**2*a4**2*a6/81 - 8*a1*a2**2*a4**2/243 - 34*a1*a2**2*a4*a5**2/243 + 13*a1*a2**2*a4*a5*a6/27 + 53*a1*a2**2*a4*a5/108 + 4*a1*a2**2*a5**3/27 + 16*a1*a2*a3*a4*a6**2/81 + 182*a1*a2*a3*a4*a6/729 - 22*a1*a2*a3*a4/243 - 20*a1*a2*a3*a5**2*a6/243 + 5*a1*a2*a3*a5**2/243 + 4*a1*a2*a3*a5*a6**2/81 + 5*a1*a2*a3*a5*a6/9 - 5*a1*a2*a3*a5/54 + 26*a1*a2*a3*a6**3/9 + 13*a1*a2*a3*a6**2/27 - 11*a1*a2*a3*a6/18 + 5*a1*a2*a3/54 - 4*a1*a2*a4**2*a5*a6/729 - 70*a1*a2*a4**2*a5/2187 + 8*a1*a2*a4**2*a6**2/243 + 20*a1*a2*a4**2*a6/729 - 2*a1*a2*a4**2/81 + 8*a1*a2*a4*a5**3/729 + 4*a1*a2*a4*a5**2*a6/81 - 40*a1*a2*a4*a5**2/729 - 8*a1*a2*a4*a5*a6**2/81 - 47*a1*a2*a4*a5*a6/243 + 8*a1*a2*a4*a5/243 - 2*a1*a2*a4*a6**3/9 - 40*a1*a2*a4*a6**2/27 + 7*a1*a2*a4*a6/12 - a1*a2*a4/18 - 8*a1*a2*a5**3*a6/81 + 29*a1*a2*a5**3/486 + 7*a1*a2*a5**2*a6**2/9 + 29*a1*a2*a5**2*a6/108 - 17*a1*a2*a5**2/108 - 4*a1*a3*a5*a6**3/243 + 8*a1*a3*a5*a6**2/243 - 25*a1*a3*a5*a6/729 + a1*a3*a5/81 + 4*a1*a3*a6**3/27 - 7*a1*a3*a6**2/81 + a1*a3*a6/54 - a1*a3/486 + 16*a1*a4**2*a6**3/729 + 64*a1*a4**2*a6**2/729 - 82*a1*a4**2*a6/2187 + 8*a1*a4**2/2187 - 4*a1*a4*a5**2*a6**2/243 - 64*a1*a4*a5**2*a6/2187 + 14*a1*a4*a5**2/2187 + 44*a1*a4*a5*a6**2/243 - 71*a1*a4*a5*a6/729 + 13*a1*a4*a5/729 + 8*a1*a4*a6**4/27 + 40*a1*a4*a6**3/81 - 11*a1*a4*a6**2/27 + 26*a1*a4*a6/243 - 5*a1*a4/486 + 4*a1*a5**4*a6/729 - a1*a5**4/2187 + 4*a1*a5**3*a6**2/243 - 43*a1*a5**3*a6/729 + 23*a1*a5**3/1458 - 14*a1*a5**2*a6**3/81 - 5*a1*a5**2*a6**2/81 + 4*a1*a5**2*a6/81 - a1*a5**2/324 + 5*a1*a5*a6**4/9 - 4*a1*a5*a6**3/9 + a1*a5*a6**2/54 + 13*a1*a5*a6/216 - a1*a5/72 - 14*a2**4*a3**2/81 - 14*a2**4*a3*a4/81 - 28*a2**4*a3*a5/27 - a2**4*a3*a6/6 + 31*a2**4*a3/9 + 2*a2**4*a4**2/27 + 2*a2**4*a4*a5/27 - 8*a2**3*a3*a4*a6/243 - 148*a2**3*a3*a4/729 + 46*a2**3*a3*a5**2/729 + 10*a2**3*a3*a5*a6/27 - 139*a2**3*a3*a5/243 - 5*a2**3*a3*a6**2/3 - 14*a2**3*a3*a6/27 + 25*a2**3*a3/162 - 20*a2**3*a4**2*a5/2187 - 8*a2**3*a4**2*a6/243 + 4*a2**3*a4**2/81 - 4*a2**3*a4*a5**2/729 - 14*a2**3*a4*a5*a6/81 + 5*a2**3*a4*a5/486 + a2**3*a4*a6**2/3 + 35*a2**3*a4*a6/18 - 65*a2**3*a4/108 - 22*a2**3*a5**3/243 + a2**3*a5**2*a6/3 + 4*a2**3*a5**2/27 + 14*a2**2*a3*a5*a6**2/243 + 32*a2**2*a3*a5*a6/729 - 41*a2**2*a3*a5/486 + 2*a2**2*a3*a6**3/3 - a2**2*a3*a6**2 + 4*a2**2*a3*a6/9 - 37*a2**2*a3/486 - 8*a2**2*a4**2*a6**2/729 - 32*a2**2*a4**2*a6/243 + 92*a2**2*a4**2/2187 - 8*a2**2*a4*a5**2*a6/2187 - 23*a2**2*a4*a5**2/2187 + 4*a2**2*a4*a5*a6**2/81 - 49*a2**2*a4*a5*a6/729 - 8*a2**2*a4*a5/729 - 10*a2**2*a4*a6**3/27 - 53*a2**2*a4*a6**2/81 + 67*a2**2*a4*a6/162 - 23*a2**2*a4/486 + 16*a2**2*a5**4/2187 + 16*a2**2*a5**3*a6/729 - 10*a2**2*a5**3/243 - 2*a2**2*a5**2*a6**2/3 + 181*a2**2*a5**2*a6/486 - 97*a2**2*a5**2/972 + 11*a2**2*a5*a6**3/9 + 55*a2**2*a5*a6**2/27 - 359*a2**2*a5*a6/216 + a2**2*a5/4 - 4*a2*a3*a6**4/81 + 74*a2*a3*a6**3/243 - 305*a2*a3*a6**2/729 + 239*a2*a3*a6/1458 - 25*a2*a3/1458 - 4*a2*a4*a5*a6**3/81 - 314*a2*a4*a5*a6**2/2187 + 215*a2*a4*a5*a6/2187 - 28*a2*a4*a5/2187 + 8*a2*a4*a6**4/81 + 8*a2*a4*a6**3/243 - 86*a2*a4*a6**2/729 + 7*a2*a4*a6/243 + 8*a2*a5**3*a6**2/243 - 19*a2*a5**3*a6/2187 - a2*a5**3/243 + 8*a2*a5**2*a6**3/81 - 221*a2*a5**2*a6**2/729 + 65*a2*a5**2*a6/486 - 7*a2*a5**2/1458 - 38*a2*a5*a6**4/27 + 20*a2*a5*a6**3/27 - a2*a5*a6**2/9 + 19*a2*a5*a6/486 - 7*a2*a5/972 + a2*a6**5 + 35*a2*a6**4/18 - 89*a2*a6**3/27 + 43*a2*a6**2/27 - 35*a2*a6/108 + 5*a2/216 - 16*a4*a6**5/243 - 32*a4*a6**4/729 + 50*a4*a6**3/729 - 13*a4*a6**2/729 + a4*a6/729 + 8*a5**2*a6**4/243 - 8*a5**2*a6**3/243 + a5**2*a6**2/81 - 2*a5**2*a6/729 + 8*a5*a6**5/81 - 80*a5*a6**4/243 + 7*a5*a6**3/27 - 37*a5*a6**2/486 + 2*a5*a6/243 - 8*a6**6/9 + 16*a6**5/27 + 7*a6**4/81 - 23*a6**3/162 + a6**2/27 - a6/324",
          "a0**3*a3**2*a5/6 - a0**3*a3*a4**2/18 - a0**2*a1*a3**2*a5/9 + 4*a0**2*a1*a3**2*a6/3 - 5*a0**2*a1*a3**2/18 + a0**2*a1*a3*a4**2/27 - 5*a0**2*a1*a3*a4*a5/27 + a0**2*a1*a4**3/81 + 5*a0**2*a2**2*a3**2/6 + 4*a0**2*a2*a3**3/243 + 4*a0**2*a2*a3**2*a4/243 + 8*a0**2*a2*a3**2*a5/81 - 7*a0**2*a2*a3**2*a6/9 + 5*a0**2*a2*a3**2/27 - 2*a0**2*a2*a3*a4**2/81 + 4*a0**2*a2*a3*a4*a5/81 + 17*a0**2*a2*a3*a4*a6/18 - 7*a0**2*a2*a3*a4/54 - 5*a0**2*a2*a3*a5**2/27 + 4*a0**2*a2*a4**3/243 + 2*a0**2*a2*a4**2*a5/81 - 4*a0**2*a3**2*a4*a6/243 + 2*a0**2*a3**2*a4/2187 + 28*a0**2*a3**2*a5**2/2187 + 20*a0**2*a3**2*a5*a6/243 - 2*a0**2*a3**2*a5/729 + 16*a0**2*a3**2*a6**2/27 - 20*a0**2*a3**2*a6/81 + 7*a0**2*a3**2/243 + 4*a0**2*a3*a4**2*a5/6561 - 32*a0**2*a3*a4**2*a6/729 + 4*a0**2*a3*a4**2/2187 + 8*a0**2*a3*a4*a5**2/729 - 10*a0**2*a3*a4*a5*a6/81 + 13*a0**2*a3*a4*a5/729 - 11*a0**2*a3*a4*a6**2/27 + 29*a0**2*a3*a4*a6/162 - a0**2*a3*a4/54 + 20*a0**2*a3*a5**3/729 + 10*a0**2*a3*a5**2*a6/81 - a0**2*a3*a5**2/27 + a0**2*a3*a5*a6**2/3 - a0**2*a3*a5*a6/9 + a0**2*a3*a5/108 - 16*a0**2*a4**4/19683 - 8*a0**2*a4**3*a5/6561 - 8*a0**2*a4**3*a6/729 + 8*a0**2*a4**3/2187 + 4*a0**2*a4**2*a5**2/2187 + 2*a0**2*a4**2*a5*a6/243 - a0**2*a4**2*a6**2/9 + a0**2*a4**2*a6/54 - a0**2*a4**2/81 + a0**2*a4*a5**2*a6/27 + a0**2*a4*a5**2/324 - 8*a0*a1**2*a2*a3**2/3 - 4*a0*a1**2*a3**3/243 - 4*a0*a1**2*a3**2*a4/243 - 2*a0*a1**2*a3**2*a5/81 - a0*a1**2*a3**2*a6/9 + 2*a0*a1**2*a3*a4*a5/27 - 7*a0*a1**2*a3*a4*a6/9 + a0*a1**2*a3*a4/6 - a0*a1**2*a3*a5**2/6 - 2*a0*a1**2*a4**3/81 + a0*a1**2*a4**2*a5/27 + 8*a0*a1*a2**2*a3**2/9 - 19*a0*a1*a2**2*a3*a4/18 + 4*a0*a1*a2*a3**2*a4/81 - 56*a0*a1*a2*a3**2*a5/243 - 28*a0*a1*a2*a3**2*a6/27 + 16*a0*a1*a2*a3**2/81 + 92*a0*a1*a2*a3*a4**2/729 + 34*a0*a1*a2*a3*a4*a5/243 + 19*a0*a1*a2*a3*a4*a6/27 - 11*a0*a1*a2*a3*a4/54 - 23*a0*a1*a2*a3*a5*a6/18 + 37*a0*a1*a2*a3*a5/54 + 4*a0*a1*a2*a4**3/243 + 2*a0*a1*a2*a4**2*a5/81 + 4*a0*a1*a2*a4**2*a6/27 - 13*a0*a1*a2*a4**2/162 + a0*a1*a2*a4*a5**2/9 + 68*a0*a1*a3**2*a5*a6/729 - 14*a0*a1*a3**2*a5/243 + 4*a0*a1*a3**2*a6/81 - 4*a0*a1*a3**2/243 + 4*a0*a1*a3*a4**2/729 + 16*a0*a1*a3*a4*a5**2/2187 + 28*a0*a1*a3*a4*a5*a6/243 - 34*a0*a1*a3*a4*a5/729 - 4*a0*a1*a3*a4*a6**2/81 + 4*a0*a1*a3*a4*a6/243 + a0*a1*a3*a4/243 + 34*a0*a1*a3*a5**2*a6/243 - 17*a0*a1*a3*a5**2/243 + 11*a0*a1*a3*a5*a6**2/27 - 7*a0*a1*a3*a5*a6/18 + 2*a0*a1*a3*a5/27 + 8*a0*a1*a3*a6**3/3 - 2*a0*a1*a3*a6**2/9 - 4*a0*a1*a3*a6/9 + a0*a1*a3/12 - 8*a0*a1*a4**3*a5/2187 - 16*a0*a1*a4**3*a6/2187 - 8*a0*a1*a4**2*a5**2/2187 - 20*a0*a1*a4**2*a5*a6/729 + 2*a0*a1*a4**2*a5/243 + 8*a0*a1*a4**2*a6**2/81 - 4*a0*a1*a4**2*a6/81 + a0*a1*a4**2/81 + 4*a0*a1*a4*a5**3/729 + a0*a1*a4*a5**2/162 - 5*a0*a1*a4*a5*a6**2/27 - a0*a1*a4*a5*a6/3 + a0*a1*a4*a5/27 + a0*a1*a5**3*a6/9 + 7*a0*a1*a5**3/108 + 4*a0*a2**3*a3**2/9 + 2*a0*a2**3*a3*a4/27 - a0*a2**3*a3*a5/6 - a0*a2**3*a4**2/9 + 8*a0*a2**2*a3**2*a5/81 - 8*a0*a2**2*a3**2*a6/27 + 8*a0*a2**2*a3**2/81 - 8*a0*a2**2*a3*a4**2/2187 + 88*a0*a2**2*a3*a4*a5/729 + 8*a0*a2**2*a3*a4*a6/81 - 11*a0*a2**2*a3*a4/243 + 16*a0*a2**2*a3*a5**2/81 + 2*a0*a2**2*a3*a5*a6/9 - 34*a0*a2**2*a3*a5/81 - 2*a0*a2**2*a3*a6**2 - a0*a2**2*a3*a6/9 + 65*a0*a2**2*a3/216 + 4*a0*a2**2*a4**2*a5/243 - 4*a0*a2**2*a4**2*a6/81 + 43*a0*a2**2*a4**2/243 + 4*a0*a2**2*a4*a5**2/81 + 2*a0*a2**2*a4*a5*a6/9 + 53*a0*a2**2*a4*a5/324 + a0*a2**2*a5**3/9 + 28*a0*a2*a3**2*a6**2/81 - 196*a0*a2*a3**2*a6/729 + 73*a0*a2*a3**2/2187 + 16*a0*a2*a3*a4*a5*a6/729 + 94*a0*a2*a3*a4*a5/2187 + 20*a0*a2*a3*a4*a6**2/81 - 94*a0*a2*a3*a4*a6/729 + 16*a0*a2*a3*a4/2187 + 8*a0*a2*a3*a5**3/2187 + 8*a0*a2*a3*a5**2*a6/81 + 88*a0*a2*a3*a5**2/2187 + 10*a0*a2*a3*a5*a6**2/9 - 32*a0*a2*a3*a5*a6/81 + 11*a0*a2*a3*a5/486 + 5*a0*a2*a3*a6**3/9 - 14*a0*a2*a3*a6**2/9 + 193*a0*a2*a3*a6/324 - 7*a0*a2*a3/108 + 16*a0*a2*a4**3*a6/6561 - 280*a0*a2*a4**3/19683 - 8*a0*a2*a4**2*a5**2/2187 - 8*a0*a2*a4**2*a5*a6/2187 - 140*a0*a2*a4**2*a5/6561 - 4*a0*a2*a4**2*a6**2/243 - 82*a0*a2*a4**2*a6/729 + 50*a0*a2*a4**2/2187 - 8*a0*a2*a4*a5**3/2187 - 4*a0*a2*a4*a5**2*a6/243 + 43*a0*a2*a4*a5**2/2187 + 4*a0*a2*a4*a5*a6**2/81 + 65*a0*a2*a4*a5*a6/243 - 5*a0*a2*a4*a5/81 + 4*a0*a2*a4*a6**3/9 - 49*a0*a2*a4*a6**2/54 + a0*a2*a4*a6/3 - 4*a0*a2*a4/81 + 4*a0*a2*a5**4/729 + 2*a0*a2*a5**3*a6/81 - a0*a2*a5**3/27 + 16*a0*a2*a5**2*a6**2/27 + 5*a0*a2*a5**2*a6/108 - 55*a0*a2*a5**2/648 + 56*a0*a3*a4*a6**3/729 + 32*a0*a3*a4*a6**2/729 - 34*a0*a3*a4*a6/729 + 14*a0*a3*a4/2187 - 8*a0*a3*a5**2*a6**2/2187 + 8*a0*a3*a5**2*a6/2187 + 5*a0*a3*a5**2/2187 + 40*a0*a3*a5*a6**3/243 + 32*a0*a3*a5*a6**2/729 - 14*a0*a3*a5*a6/243 + 7*a0*a3*a5/729 + 32*a0*a3*a6**4/27 - 52*a0*a3*a6**3/81 + 11*a0*a3*a6**2/243 + 13*a0*a3*a6/486 - a0*a3/243 + 8*a0*a4**2*a5*a6**2/6561 - 152*a0*a4**2*a5*a6/6561 + 4*a0*a4**2*a5/729 + 16*a0*a4**2*a6**3/729 + 40*a0*a4**2*a6**2/2187 - 8*a0*a4**2*a6/729 - 8*a0*a4*a5**3*a6/6561 + 26*a0*a4*a5**3/6561 - 8*a0*a4*a5**2*a6**2/729 - 98*a0*a4*a5**2*a6/2187 + 8*a0*a4*a5**2/729 - 4*a0*a4*a5*a6**3/81 - 62*a0*a4*a5*a6**2/729 + 25*a0*a4*a5*a6/729 - a0*a4*a5/243 - 2*a0*a4*a6**4/27 + 22*a0*a4*a6**3/81 - 37*a0*a4*a6**2/162 + 11*a0*a4*a6/162 - a0*a4/162 + 16*a0*a5**4/2187 + 8*a0*a5**3*a6**2/729 + 4*a0*a5**3*a6/243 - a0*a5**3/486 + 4*a0*a5**2*a6**3/81 - 4*a0*a5**2*a6**2/81 + a0*a5**2*a6/36 - a0*a5**2/162 + 2*a0*a5*a6**4/3 - 4*a0*a5*a6**3/9 + a0*a5*a6**2/108 + 7*a0*a5*a6/216 - a0*a5/216 + a1**4*a3**2 - a1**3*a2*a3**2/3 + 2*a1**3*a2*a3*a4/3 - 8*a1**3*a3**2*a4/243 + 8*a1**3*a3**2*a5/81 + 4*a1**3*a3**2*a6/9 - 2*a1**3*a3**2/27 - 16*a1**3*a3*a4**2/243 - 8*a1**3*a3*a4*a5/81 + a1**3*a3*a5**2/9 - a1**3*a3*a5*a6 - 5*a1**3*a3*a5/18 - 2*a1**3*a4**2*a5/27 + 4*a1**3*a4**2/27 - 2*a1**2*a2**2*a3**2/9 - 2*a1**2*a2**2*a3*a4/9 + 17*a1**2*a2**2*a3*a5/18 + 2*a1**2*a2**2*a4**2/27 - 8*a1**2*a2*a3**2*a5/81 + 4*a1**2*a2*a3**2*a6/27 - 2*a1**2*a2*a3**2/27 - 28*a1**2*a2*a3*a4*a5/243 - 8*a1**2*a2*a3*a4*a6/27 + 8*a1**2*a2*a3*a4/81 - 20*a1**2*a2*a3*a5**2/81 + 7*a1**2*a2*a3*a5*a6/9 + 7*a1**2*a2*a3*a5/18 - 17*a1**2*a2*a3*a6**2/3 - a1**2*a2*a3*a6 + 5*a1**2*a2*a3/12 + 4*a1**2*a2*a4**2*a5/81 - 2*a1**2*a2*a4**2*a6/27 - 5*a1**2*a2*a4**2/27 - 4*a1**2*a2*a4*a5**2/27 + a1**2*a2*a4*a5*a6/9 + 11*a1**2*a2*a4*a5/27 + 32*a1**2*a3**2*a6**2/243 - 4*a1**2*a3**2*a6/27 + 28*a1**2*a3**2/729 - 28*a1**2*a3*a4*a5/729 + 80*a1**2*a3*a4*a6**2/243 - 16*a1**2*a3*a4*a6/81 + 22*a1**2*a3*a4/729 + 4*a1**2*a3*a5**3/729 - 4*a1**2*a3*a5**2*a6/81 - 38*a1**2*a3*a5**2/729 - 20*a1**2*a3*a5*a6**2/81 - 16*a1**2*a3*a5*a6/81 + 2*a1**2*a3*a5/27 + 8*a1**2*a3*a6**3/9 - 4*a1**2*a3*a6**2/3 + 16*a1**2*a3*a6/27 - 2*a1**2*a3/27 + 80*a1**2*a4**3/6561 - 8*a1**2*a4**2*a5**2/2187 - 16*a1**2*a4**2*a5*a6/729 + 40*a1**2*a4**2*a5/2187 + 8*a1**2*a4**2*a6/81 - 16*a1**2*a4**2/729 + 4*a1**2*a4*a5**2*a6/243 - 14*a1**2*a4*a5**2/729 + 4*a1**2*a4*a5*a6**2/27 - 4*a1**2*a4*a5*a6/81 + a1**2*a4*a5/54 - 4*a1**2*a4*a6**3/9 - 2*a1**2*a4*a6**2/3 + 17*a1**2*a4*a6/54 - a1**2*a4/36 - 2*a1**2*a5**3*a6/27 + a1**2*a5**3/162 + 2*a1**2*a5**2*a6**2/9 + 11*a1**2*a5**2*a6/54 - 5*a1**2*a5**2/54 + 4*a1*a2**3*a3*a4/27 - 17*a1*a2**3*a3*a5/27 + 16*a1*a2**3*a3*a6/3 + 25*a1*a2**3*a3/18 + 2*a1*a2**3*a4**2/81 + a1*a2**3*a4*a5/9 - 104*a1*a2**2*a3**2*a6/243 + 148*a1*a2**2*a3**2/729 - 16*a1*a2**2*a3*a4*a5/729 - 128*a1*a2**2*a3*a4*a6/243 + 112*a1*a2**2*a3*a4/729 - 16*a1*a2**2*a3*a5**2/729 - 4*a1*a2**2*a3*a5*a6/3 + 73*a1*a2**2*a3*a5/243 - a1*a2**2*a3*a6**2 + 130*a1*a2**2*a3*a6/27 - 29*a1*a2**2*a3/27 + 16*a1*a2**2*a4**3/6561 + 8*a1*a2**2*a4**2*a5/2187 + 20*a1*a2**2*a4**2*a6/243 + 16*a1*a2**2*a4**2/729 + 68*a1*a2**2*a4*a5**2/729 - 26*a1*a2**2*a4*a5*a6/81 - 53*a1*a2**2*a4*a5/162 + a1*a2**2*a4*a6**2/9 + 85*a1*a2**2*a4*a6/54 - 13*a1*a2**2*a4/27 - 8*a1*a2**2*a5**3/81 + 5*a1*a2**2*a5**2*a6/27 + 8*a1*a2**2*a5**2/27 - 32*a1*a2*a3*a4*a6**2/243 - 364*a1*a2*a3*a4*a6/2187 + 44*a1*a2*a3*a4/729 + 40*a1*a2*a3*a5**2*a6/729 - 10*a1*a2*a3*a5**2/729 - 8*a1*a2*a3*a5*a6**2/243 - 10*a1*a2*a3*a5*a6/27 + 5*a1*a2*a3*a5/81 - 52*a1*a2*a3*a6**3/27 - 26*a1*a2*a3*a6**2/81 + 11*a1*a2*a3*a6/27 - 5*a1*a2*a3/81 + 8*a1*a2*a4**2*a5*a6/2187 + 140*a1*a2*a4**2*a5/6561 - 16*a1*a2*a4**2*a6**2/729 - 40*a1*a2*a4**2*a6/2187 + 4*a1*a2*a4**2/243 - 16*a1*a2*a4*a5**3/2187 - 8*a1*a2*a4*a5**2*a6/243 + 80*a1*a2*a4*a5**2/2187 + 16*a1*a2*a4*a5*a6**2/243 + 94*a1*a2*a4*a5*a6/729 - 16*a1*a2*a4*a5/729 + 4*a1*a2*a4*a6**3/27 + 80*a1*a2*a4*a6**2/81 - 7*a1*a2*a4*a6/18 + a1*a2*a4/27 + 16*a1*a2*a5**3*a6/243 - 29*a1*a2*a5**3/729 - 14*a1*a2*a5**2*a6**2/27 - 29*a1*a2*a5**2*a6/162 + 17*a1*a2*a5**2/162 + 11*a1*a2*a5*a6**3/9 + 26*a1*a2*a5*a6**2/27 - 26*a1*a2*a5*a6/27 + 29*a1*a2*a5/216 + 8*a1*a3*a5*a6**3/729 - 16*a1*a3*a5*a6**2/729 + 50*a1*a3*a5*a6/2187 - 2*a1*a3*a5/243 - 8*a1*a3*a6**3/81 + 14*a1*a3*a6**2/243 - a1*a3*a6/81 + a1*a3/729 - 32*a1*a4**2*a6**3/2187 - 128*a1*a4**2*a6**2/2187 + 164*a1*a4**2*a6/6561 - 16*a1*a4**2/6561 + 8*a1*a4*a5**2*a6**2/729 + 128*a1*a4*a5**2*a6/6561 - 28*a1*a4*a5**2/6561 - 88*a1*a4*a5*a6**2/729 + 142*a1*a4*a5*a6/2187 - 26*a1*a4*a5/2187 - 16*a1*a4*a6**4/81 - 80*a1*a4*a6**3/243 + 22*a1*a4*a6**2/81 - 52*a1*a4*a6/729 + 5*a1*a4/729 - 8*a1*a5**4*a6/2187 + 2*a1*a5**4/6561 - 8*a1*a5**3*a6**2/729 + 86*a1*a5**3*a6/2187 - 23*a1*a5**3/2187 + 28*a1*a5**2*a6**3/243 + 10*a1*a5**2*a6**2/243 - 8*a1*a5**2*a6/243 + a1*a5**2/486 - 10*a1*a5*a6**4/27 + 8*a1*a5*a6**3/27 - a1*a5*a6**2/81 - 13*a1*a5*a6/324 + a1*a5/108 + 4*a1*a6**5/3 - 4*a1*a6**4/9 - 11*a1*a6**3/18 + 7*a1*a6**2/18 - 17*a1*a6/216 + a1/216 - 7*a2**5*a3/6 + 28*a2**4*a3**2/243 + 28*a2**4*a3*a4/243 + 56*a2**4*a3*a5/81 + a2**4*a3*a6/9 - 62*a2**4*a3/27 - 4*a2**4*a4**2/81 - 4*a2**4*a4*a5/81 + a2**4*a4*a6/9 + a2**4*a4/6 + a2**4*a5**2/27 + 16*a2**3*a3*a4*a6/729 + 296*a2**3*a3*a4/2187 - 92*a2**3*a3*a5**2/2187 - 20*a2**3*a3*a5*a6/81 + 278*a2**3*a3*a5/729 + 10*a2**3*a3*a6**2/9 + 28*a2**3*a3*a6/81 - 25*a2**3*a3/243 + 40*a2**3*a4**2*a5/6561 + 16*a2**3*a4**2*a6/729 - 8*a2**3*a4**2/243 + 8*a2**3*a4*a5**2/2187 + 28*a2**3*a4*a5*a6/243 - 5*a2**3*a4*a5/729 - 2*a2**3*a4*a6**2/9 - 35*a2**3*a4*a6/27 + 65*a2**3*a4/162 + 44*a2**3*a5**3/729 - 2*a2**3*a5**2*a6/9 - 8*a2**3*a5**2/81 - a2**3*a5*a6**2/9 + 49*a2**3*a5*a6/54 - 7*a2**3*a5/24 - 28*a2**2*a3*a5*a6**2/729 - 64*a2**2*a3*a5*a6/2187 + 41*a2**2*a3*a5/729 - 4*a2**2*a3*a6**3/9 + 2*a2**2*a3*a6**2/3 - 8*a2**2*a3*a6/27 + 37*a2**2*a3/729 + 16*a2**2*a4**2*a6**2/2187 + 64*a2**2*a4**2*a6/729 - 184*a2**2*a4**2/6561 + 16*a2**2*a4*a5**2*a6/6561 + 46*a2**2*a4*a5**2/6561 - 8*a2**2*a4*a5*a6**2/243 + 98*a2**2*a4*a5*a6/2187 + 16*a2**2*a4*a5/2187 + 20*a2**2*a4*a6**3/81 + 106*a2**2*a4*a6**2/243 - 67*a2**2*a4*a6/243 + 23*a2**2*a4/729 - 32*a2**2*a5**4/6561 - 32*a2**2*a5**3*a6/2187 + 20*a2**2*a5**3/729 + 4*a2**2*a5**2*a6**2/9 - 181*a2**2*a5**2*a6/729 + 97*a2**2*a5**2/1458 - 22*a2**2*a5*a6**3/27 - 110*a2**2*a5*a6**2/81 + 359*a2**2*a5*a6/324 - a2**2*a5/6 - a2**2*a6**4/3 + 17*a2**2*a6**3/9 - 41*a2**2*a6**2/27 + 29*a2**2*a6/72 - a2**2/27 + 8*a2*a3*a6**4/243 - 148*a2*a3*a6**3/729 + 610*a2*a3*a6**2/2187 - 239*a2*a3*a6/2187 + 25*a2*a3/2187 + 8*a2*a4*a5*a6**3/243 + 628*a2*a4*a5*a6**2/6561 - 430*a2*a4*a5*a6/6561 + 56*a2*a4*a5/6561 - 16*a2*a4*a6**4/243 - 16*a2*a4*a6**3/729 + 172*a2*a4*a6**2/2187 - 14*a2*a4*a6/729 - 16*a2*a5**3*a6**2/729 + 38*a2*a5**3*a6/6561 + 2*a2*a5**3/729 - 16*a2*a5**2*a6**3/243 + 442*a2*a5**2*a6**2/2187 - 65*a2*a5**2*a6/729 + 7*a2*a5**2/2187 + 76*a2*a5*a6**4/81 - 40*a2*a5*a6**3/81 + 2*a2*a5*a6**2/27 - 19*a2*a5*a6/729 + 7*a2*a5/1458 - 2*a2*a6**5/3 - 35*a2*a6**4/27 + 178*a2*a6**3/81 - 86*a2*a6**2/81 + 35*a2*a6/162 - 5*a2/324 + 32*a4*a6**5/729 + 64*a4*a6**4/2187 - 100*a4*a6**3/2187 + 26*a4*a6**2/2187 - 2*a4*a6/2187 - 16*a5**2*a6**4/729 + 16*a5**2*a6**3/729 - 2*a5**2*a6**2/243 + 4*a5**2*a6/2187 - 16*a5*a6**5/243 + 160*a5*a6**4/729 - 14*a5*a6**3/81 + 37*a5*a6**2/729 - 4*a5*a6/729 + 16*a6**6/27 - 32*a6**5/81 - 14*a6**4/243 + 23*a6**3/243 - 2*a6**2/81 + a6/486"
        &#93;
      &#93;,
      "shape": &#91;
        10,
        5
      &#93;
    },
    "Q": {
      "entries": &#91;
        &#91;
          "0",
          "3*a2*a3*a5 - a2*a4**2 + 9*a3*a6**2 - 9*a3*a6/2 + a3/2 - 2*a4*a5*a6 + a4*a5/2 + a5**3/3",
          "a1*a3*a5 - a1*a4**2/3 + 3*a2*a3*a6 - a2*a3 - a2*a4*a5/3 + a4*a6**2 - 5*a4*a6/6 + a4/6 - a5**2*a6/3 + a5**2/6",
          "-3*a1*a3*a6 + a1*a3/2 + a1*a4*a5/3 + 3*a2**2*a3 + a2*a4*a6 - a2*a4/2 + a2*a5**2/3 + a5*a6**2 - 2*a5*a6/3 + a5/12",
          "a1*a4*a6 - a1*a4/6 - a1*a5**2/3 - a2**2*a4 - 2*a2*a5*a6 + 5*a2*a5/6 - 3*a6**3 + 3*a6**2 - 11*a6/12 + 1/12",
          "0",
          "0",
          "0",
          "0",
          "0"
        &#93;,
        &#91;
          "3*a2*a3*a5/2 - a2*a4**2/2 + 9*a3*a6**2/2 - 9*a3*a6/4 + a3/4 - a4*a5*a6 + a4*a5/4 + a5**3/6",
          "3*a2*a3/4 + a4*a6 - a4/4 - a5**2/4",
          "a0*a3*a5/2 - a0*a4**2/6 + 3*a1*a3*a6/2 - a1*a3/4 - a1*a4*a5/6 + a2*a4*a6/2 - a2*a5**2/6 + a5*a6/12 - a5/24",
          "-3*a0*a3*a6/2 + a0*a3/4 + a0*a4*a5/6 + 3*a1*a2*a3/2 - a1*a4/6 + a1*a5**2/6 + a2**2*a4/2 + a2*a5*a6/2 - 5*a2*a5/12 - a6**2/2 + a6/3 - 1/24",
          "a0*a4*a6/2 - a0*a4/12 - a0*a5**2/6 - a1*a2*a4/2 - a1*a5*a6/2 + a1*a5/4 - a2**2*a5/2 - 3*a2*a6**2/2 + a2*a6 - a2/8",
          "0",
          "3*a2*a3*a5 - a2*a4**2 + 9*a3*a6**2 - 9*a3*a6/2 + a3/2 - 2*a4*a5*a6 + a4*a5/2 + a5**3/3",
          "-a1*a3*a5 + a1*a4**2/3 - 3*a2*a3*a6 + a2*a3 + a2*a4*a5/3 - a4*a6**2 + 5*a4*a6/6 - a4/6 + a5**2*a6/3 - a5**2/6",
          "-3*a1*a3*a6 + a1*a3/2 + a1*a4*a5/3 + 3*a2**2*a3 + a2*a4*a6 - a2*a4/2 + a2*a5**2/3 + a5*a6**2 - 2*a5*a6/3 + a5/12",
          "a1*a4*a6 - a1*a4/6 - a1*a5**2/3 - a2**2*a4 - 2*a2*a5*a6 + 5*a2*a5/6 - 3*a6**3 + 3*a6**2 - 11*a6/12 + 1/12"
        &#93;,
        &#91;
          "3*a0*a1*a3*a5**2/2 - a0*a1*a4**2*a5/2 - 9*a0*a2*a3*a5*a6/2 - 9*a0*a2*a3*a5/4 + 3*a0*a2*a4**2*a6 + a0*a2*a4**2/2 - a0*a2*a4*a5**2/2 - 27*a0*a3*a6**3 + 9*a0*a3*a6**2 + 3*a0*a3*a6/4 - a0*a3/4 + 15*a0*a4*a5*a6**2/2 - 3*a0*a4*a5*a6/4 - a0*a4*a5/4 - 3*a0*a5**3*a6/2 - a0*a5**3/6 + 27*a1**2*a3*a5*a6/2 - 3*a1**2*a4**2*a6 - a1**2*a4**2/2 - a1**2*a4*a5**2/2 - 9*a1*a2**2*a3*a5/2 + 54*a1*a2*a3*a6**2 - 9*a1*a2*a3*a6/4 - 3*a1*a2*a3 - 6*a1*a2*a4*a5*a6 - 7*a1*a2*a4*a5/4 - a1*a2*a5**3 + 18*a1*a4*a6**3 - 3*a1*a4*a6**2 - a1*a4*a6 + a1*a4/4 - 15*a1*a5**2*a6**2/2 + a1*a5**2/4 - 27*a2**3*a3*a6 - 27*a2**3*a3/4 - 3*a2**3*a4*a5/2 - 18*a2**2*a4*a6**2 - 9*a2**2*a4*a6/4 + 3*a2**2*a4/4 - 6*a2**2*a5**2*a6 - a2**2*a5**2/2 - 63*a2*a5*a6**3/2 + 9*a2*a5*a6**2/2 + 2*a2*a5*a6 - a2*a5/8 - 27*a6**5 + 27*a6**4/2 + 3*a6**3/4 - 9*a6**2/8 + a6/8",
          "-3*a0**2*a3*a5**2/2 + a0**2*a4**2*a5/2 - 18*a0*a1*a3*a5*a6 + 3*a0*a1*a4**2*a6 + a0*a1*a4**2 + a0*a1*a4*a5**2 - 18*a0*a2**2*a3*a5 + 6*a0*a2**2*a4**2 - 81*a0*a2*a3*a6**2 + 81*a0*a2*a3*a6/4 - 3*a0*a2*a3/4 + 12*a0*a2*a4*a5*a6 - a0*a2*a4*a5/2 - a0*a2*a5**3 - 9*a0*a4*a6**3 - 9*a0*a4*a6**2/2 + 3*a0*a4*a6/2 + 3*a0*a5**2*a6**2 + 9*a0*a5**2*a6/4 + 27*a1**2*a2*a3*a5/2 - 3*a1**2*a2*a4**2 - 27*a1**2*a3*a6/2 + 9*a1**2*a3/2 - 3*a1**2*a4*a5*a6 + 3*a1**2*a4*a5 + 3*a1**2*a5**3/2 + 27*a1*a2**2*a3*a6 + 45*a1*a2**2*a3/4 + 3*a1*a2**2*a4*a5 + 15*a1*a2*a4*a6/2 + 3*a1*a2*a4/4 + 9*a1*a2*a5**2*a6 + 9*a1*a2*a5**2/4 + 9*a1*a5*a6**3 + 9*a1*a5*a6**2/2 - 3*a1*a5*a6/2 + 9*a2**3*a4*a6 + 9*a2**3*a4/4 + 3*a2**3*a5**2/2 + 45*a2**2*a5*a6**2/2 + 15*a2**2*a5*a6/4 + 27*a2*a6**4 - 3*a2*a6**2",
          "-3*a0**2*a3*a5*a6 - 3*a0**2*a3*a5/4 + a0**2*a4**2*a6 + a0**2*a4**2/3 - 15*a0*a1*a2*a3*a5/2 + 2*a0*a1*a2*a4**2 - 9*a0*a1*a3*a6**2 + a0*a1*a3 + a0*a1*a4*a5*a6/2 + 3*a0*a1*a4*a5/4 - 27*a0*a2**2*a3*a6 + 9*a0*a2**2*a3/4 + 3*a0*a2**2*a4*a5/2 - 15*a0*a2*a4*a6**2 + 15*a0*a2*a4*a6/4 - a0*a2*a4/4 + 5*a0*a2*a5**2*a6/2 - a0*a2*a5**2/2 - 3*a0*a5*a6**3 - a0*a5*a6**2/4 + 13*a0*a5*a6/24 + 9*a1**3*a3*a5/2 - a1**3*a4**2 + 18*a1**2*a2*a3*a6 + 3*a1**2*a2*a3/4 + 6*a1**2*a4*a6**2 - a1**2*a4*a6/2 + a1**2*a4/2 - 3*a1**2*a5**2*a6/2 + 3*a1**2*a5**2/4 + 3*a1*a2**2*a4*a6 + 3*a1*a2**2*a4/4 + a1*a2**2*a5**2 - 3*a1*a2*a5*a6**2/2 + 9*a1*a2*a5*a6/4 + 5*a1*a2*a5/8 - 9*a1*a6**4 + 3*a1*a6**3/2 + 3*a1*a6**2/2 - a1*a6/2 + 9*a2**3*a5*a6/2 + 3*a2**3*a5/4 + 9*a2**2*a6**3 + 3*a2**2*a6**2/2 - 3*a2**2*a6/8",
          "-3*a0**2*a2*a3*a5/2 + 9*a0**2*a3*a6**2 + 3*a0**2*a3*a6/2 - a0**2*a3/2 - 3*a0**2*a4*a5*a6/2 - a0**2*a4*a5/4 + 3*a0*a1**2*a3*a5/2 - 9*a0*a1*a2*a3 - 3*a0*a1*a2*a4*a5/2 - 3*a0*a1*a4*a6**2 + a0*a1*a4*a6/2 + a0*a1*a4/2 - 3*a0*a1*a5**2*a6/2 - 5*a0*a1*a5**2/12 - 18*a0*a2**3*a3 - 9*a0*a2**2*a4*a6 + 5*a0*a2**2*a4/2 - a0*a2**2*a5**2 - 9*a0*a2*a5*a6**2/2 + 5*a0*a2*a5*a6 - a0*a2*a5/4 + 9*a0*a6**4 - 11*a0*a6**2/4 + 5*a0*a6/12 + 9*a1**3*a3/2 + a1**3*a4*a5 + 9*a1**2*a2**2*a3 + 6*a1**2*a2*a4*a6 - a1**2*a2*a4 + a1**2*a2*a5**2/2 - 3*a1**2*a5*a6**2 - 9*a1**2*a5*a6/2 + a1**2*a5 + 2*a1*a2**2*a5 - 18*a1*a2*a6**3 - 9*a1*a2*a6**2/2 + 11*a1*a2*a6/4 + a1*a2/8 + 3*a2**4*a5/2 + 9*a2**3*a6**2 + 9*a2**3*a6/2 + 3*a2**3/8",
          "a0**2*a2*a4*a5/2 - 3*a0**2*a4*a6**2 - a0**2*a4*a6/2 + a0**2*a4/6 + 3*a0**2*a5**2*a6/2 + a0**2*a5**2/6 - a0*a1**2*a4*a5/2 + 3*a0*a1*a2*a4 + 2*a0*a1*a2*a5**2 + 9*a0*a1*a5*a6**2 - 5*a0*a1*a5*a6/2 - a0*a1*a5/2 + 6*a0*a2**3*a4 + 33*a0*a2**2*a5*a6/2 - 5*a0*a2**2*a5/2 + 36*a0*a2*a6**3 - 93*a0*a2*a6**2/4 + 29*a0*a2*a6/8 - a0*a2/8 - 3*a1**3*a4/2 - 3*a1**3*a5**2/2 - 3*a1**2*a2**2*a4 - 15*a1**2*a2*a5*a6 + 3*a1**2*a2*a5/2 + 9*a1**2*a6**2/2 - 15*a1**2*a6/4 + 3*a1**2/4 + 3*a1*a2**3*a5/2 - 27*a1*a2**2*a6**2 + 3*a1*a2**2*a6/2 + 21*a1*a2**2/8 + 9*a2**4*a6 + 9*a2**4/4",
          "3*a0*a2*a3*a5**2 - a0*a2*a4**2*a5 + 9*a0*a3*a5*a6**2 - 9*a0*a3*a5*a6/2 + a0*a3*a5/2 - 2*a0*a4*a5**2*a6 + a0*a4*a5**2/2 + a0*a5**4/3 - 3*a1**2*a3*a5**2 + a1**2*a4**2*a5 - 18*a1*a2*a3*a5*a6 + 9*a1*a2*a3*a5/2 + 2*a1*a2*a4*a5**2 - 6*a1*a4*a5*a6**2 + 3*a1*a4*a5*a6 - a1*a4*a5/2 + 2*a1*a5**3*a6 - a1*a5**3/2 + 9*a2**3*a3*a5 + 6*a2**2*a4*a5*a6 - 3*a2**2*a4*a5/2 + a2**2*a5**3 + 9*a2*a5**2*a6**2 - 9*a2*a5**2*a6/2 + a2*a5**2/4 + 9*a5*a6**4 - 9*a5*a6**3 + 11*a5*a6**2/4 - a5*a6/4",
          "3*a0*a1*a3*a5**2 - a0*a1*a4**2*a5 + 9*a0*a2*a3*a5*a6 - 9*a0*a2*a3*a5/2 + a0*a2*a4**2 - a0*a2*a4*a5**2 - 9*a0*a3*a6**2 + 9*a0*a3*a6/2 - a0*a3/2 + 3*a0*a4*a5*a6**2 + 3*a0*a4*a5*a6/2 - a0*a4*a5/2 - a0*a5**3*a6 - a0*a5**3/3 + 9*a1**2*a3*a5*a6 - a1**2*a4**2 - a1**2*a4*a5**2 - 9*a1*a2**2*a3*a5 + 45*a1*a2*a3*a6/2 - 6*a1*a2*a3 - 7*a1*a2*a4*a5/2 - 2*a1*a2*a5**3 + 12*a1*a4*a6**2 - 5*a1*a4*a6 + a1*a4/2 - 3*a1*a5**2*a6**2 - 3*a1*a5**2*a6 + a1*a5**2/2 - 27*a2**3*a3/2 - 3*a2**3*a4*a5 - 27*a2**2*a4*a6/2 + 3*a2**2*a4/2 - 6*a2**2*a5**2*a6 - a2**2*a5**2 - 9*a2*a5*a6**3 - 18*a2*a5*a6**2 + 11*a2*a5*a6/2 - a2*a5/4 - 27*a6**4 + 18*a6**3 - 15*a6**2/4 + a6/4",
          "-a0**2*a3*a5**2 + a0**2*a4**2*a5/3 - 3*a0*a1*a3*a5*a6 + a0*a1*a3*a5 + a0*a1*a4*a5**2/3 - 3*a0*a2**2*a3*a5 - 3*a0*a2*a3*a6/2 + a0*a2*a3/2 - 3*a0*a2*a4*a5*a6 + a0*a2*a4*a5 + a0*a2*a5**3/3 - 2*a0*a4*a6**2 + 2*a0*a4*a6/3 - a0*a5**2*a6**2 + 7*a0*a5**2*a6/6 + 3*a1**2*a2*a3*a5 + a1**2*a4*a5*a6 + 3*a1*a2**2*a3/2 + a1*a2**2*a4*a5 + 5*a1*a2*a4*a6/2 + a1*a2*a5**2/2 - 3*a1*a5*a6**3 + 9*a1*a5*a6**2/2 - a1*a5*a6/2 + a2**3*a5**2 + 3*a2**2*a5*a6**2 + a2**2*a5*a6/2 + a2**2*a5/4 + 9*a2*a6**3/2 - 3*a2*a6**2/4 - a2*a6/4",
          "-3*a0**2*a3*a5*a6 + a0**2*a3*a5/2 + a0**2*a4*a5**2/3 + 6*a0*a1*a2*a3*a5 + a0*a1*a4*a5*a6 - a0*a1*a4*a5/2 + a0*a1*a5**3/3 + 3*a0*a2**2*a3/2 + a0*a2**2*a4*a5 + 2*a0*a2*a4*a6 - 3*a0*a5*a6**3 + 4*a0*a5*a6**2 - 7*a0*a5*a6/12 - 3*a1**3*a3*a5 - 3*a1**2*a2*a3/2 - a1**2*a2*a4*a5 - 2*a1**2*a4*a6 + 2*a1**2*a5**2*a6 - a1**2*a5**2/2 - a1*a2**2*a5**2 + 6*a1*a2*a5*a6**2 - 3*a1*a2*a5*a6 - a1*a2*a5/4 + 6*a1*a6**3 - a1*a6**2 - 3*a2**3*a5*a6 - 9*a2**2*a6**2/2 - 3*a2**2*a6/4",
          "a0**2*a4*a5*a6 - a0**2*a4*a5/6 - a0**2*a5**3/3 - 2*a0*a1*a2*a4*a5 - 2*a0*a1*a5**2*a6 + 5*a0*a1*a5**2/6 - a0*a2**2*a4/2 - 2*a0*a2**2*a5**2 - 6*a0*a2*a5*a6**2 + a0*a2*a5*a6 - a0*a2*a5/4 - 6*a0*a6**3 + 3*a0*a6**2 - a0*a6/3 + a1**3*a4*a5 + a1**2*a2*a4/2 + 2*a1**2*a2*a5**2 - 3*a1**2*a5*a6**2 + 9*a1**2*a5*a6/2 - a1**2*a5/2 + 9*a1*a2**2*a5*a6 - 5*a1*a2**2*a5/2 + 21*a1*a2*a6**2/2 - 7*a1*a2*a6/4 - a1*a2/4 - 3*a2**4*a5 - 9*a2**3*a6/2 - 3*a2**3/4"
        &#93;,
        &#91;
          "3*a0*a1*a3*a4*a5/2 - a0*a1*a4**3/2 + 9*a0*a2*a3*a4*a6/2 - 3*a0*a2*a3*a4/4 - a0*a2*a4**2*a5/2 + 3*a0*a4**2*a6**2/2 - a0*a4**2*a6/4 - a0*a4*a5**2*a6/2 + 9*a1**2*a3*a4*a6/2 - 3*a1**2*a3*a4/2 + 3*a1**2*a3*a5**2 - 3*a1**2*a4**2*a5/2 - 9*a1*a2**2*a3*a4/2 + 45*a1*a2*a3*a5*a6/2 - 27*a1*a2*a3*a5/4 - 3*a1*a2*a4**2*a6/2 + a1*a2*a4**2/4 - 3*a1*a2*a4*a5**2 + 27*a1*a3*a6**3/2 - 63*a1*a3*a6**2/4 + 51*a1*a3*a6/8 - 7*a1*a3/8 + 3*a1*a4*a5*a6**2/2 + a1*a4*a5*a6 - 3*a1*a4*a5/8 - 3*a1*a5**3*a6/2 - a1*a5**3/12 - 18*a2**3*a3*a5 + 3*a2**3*a4**2/2 - 27*a2**2*a3*a6**2 + 63*a2**2*a3*a6/4 - 3*a2**2*a3 - 3*a2**2*a4*a5*a6 - 3*a2**2*a4*a5/4 - 2*a2**2*a5**3 - 9*a2*a4*a6**3/2 + 3*a2*a4*a6**2 - 3*a2*a4*a6/4 - 9*a2*a5**2*a6**2 + 11*a2*a5**2*a6/4 - a2*a5**2/4 - 9*a5*a6**4 + 27*a5*a6**3/4 - 2*a5*a6**2 + a5*a6/4",
          "-3*a0**2*a3*a4*a5/2 + a0**2*a4**3/2 - 9*a0*a1*a3*a4*a6 + 3*a0*a1*a3*a4 - 3*a0*a1*a3*a5**2 + 2*a0*a1*a4**2*a5 - 45*a0*a2*a3*a5*a6/2 + 33*a0*a2*a3*a5/4 + 3*a0*a2*a4**2*a6/2 - a0*a2*a4**2/2 + 2*a0*a2*a4*a5**2 - 81*a0*a3*a6**3/2 + 153*a0*a3*a6**2/4 - 99*a0*a3*a6/8 + 11*a0*a3/8 + 6*a0*a4*a5*a6**2 - 17*a0*a4*a5*a6/4 + 7*a0*a4*a5/8 - a0*a5**3*a6/2 + 5*a0*a5**3/12 + 9*a1**2*a2*a3*a4/2 - 9*a1**2*a3*a5*a6 + 9*a1**2*a3*a5/2 + 3*a1**2*a4*a5**2/2 + 45*a1*a2**2*a3*a5/2 - 3*a1*a2**2*a4**2/2 + 81*a1*a2*a3*a6**2/2 - 45*a1*a2*a3*a6/4 + 3*a1*a2*a3/8 - 6*a1*a2*a4*a5*a6 + 15*a1*a2*a4*a5/4 + 7*a1*a2*a5**3/2 + 6*a1*a4*a6**2 - 2*a1*a4*a6 + a1*a4/8 + 3*a1*a5**2*a6**2 - 3*a1*a5**2*a6/2 + a1*a5**2/8 - 9*a2**3*a3 + 9*a2**3*a4*a5/2 + 9*a2**2*a4*a6**2/2 - 39*a2**2*a4*a6/4 + 3*a2**2*a4/4 + 6*a2**2*a5**2*a6 + 3*a2**2*a5**2/2 + 9*a2*a5*a6**3 - 15*a2*a5*a6**2/4 - 9*a2*a5*a6/4 + 3*a2*a5/8 - 9*a6**3/2 + 21*a6**2/8 - 3*a6/8",
          "a0**2*a3*a4/4 - 3*a0*a1*a2*a3*a4/2 - 3*a0*a1*a3*a5*a6 + 2*a0*a1*a3*a5 + a0*a1*a4**2*a6/2 - a0*a1*a4**2/12 - 6*a0*a2**2*a3*a5 + a0*a2**2*a4**2/2 - 27*a0*a2*a3*a6**2/2 + 12*a0*a2*a3*a6 - 11*a0*a2*a3/4 - a0*a2*a4*a5*a6 + a0*a2*a4*a5/12 - 9*a0*a4*a6**3/2 + 6*a0*a4*a6**2 - 13*a0*a4*a6/6 + 5*a0*a4/24 + a0*a5**2*a6**2/2 - a0*a5**2*a6 + a0*a5**2/8 + 3*a1**3*a3*a4/2 + 15*a1**2*a2*a3*a5/2 - a1**2*a2*a4**2/2 + 9*a1**2*a3*a6**2/2 - 15*a1**2*a3*a6/4 + 7*a1**2*a3/8 + 5*a1**2*a4*a5/6 + 9*a1*a2**2*a3*a6/2 - 3*a1*a2**2*a3 + 3*a1*a2**2*a4*a5/2 + 9*a1*a2*a4*a6**2/2 - 15*a1*a2*a4*a6/4 + a1*a2*a4/4 - 2*a1*a2*a5**2*a6 + 11*a1*a2*a5**2/6 - 3*a1*a5*a6**3 + 5*a1*a5*a6**2/2 - 37*a1*a5*a6/24 + 7*a1*a5/48 - 3*a2**3*a4*a6/2 + 2*a2**3*a5**2 + 3*a2**2*a5*a6**2 - a2**2*a5*a6/4 - a2**2*a5/4 + 3*a2*a6**3/2 - 21*a2*a6**2/8 + 3*a2*a6/4",
          "-3*a0**2*a2*a3*a4/2 - a0**2*a4**2*a6/2 + a0**2*a4**2/12 + 3*a0*a1**2*a3*a4/2 - 3*a0*a1*a2*a3*a5 + a0*a1*a2*a4**2/2 + 9*a0*a1*a3*a6**2 - 6*a0*a1*a3*a6 + 3*a0*a1*a3/4 - 5*a0*a1*a4*a5*a6/2 + 7*a0*a1*a4*a5/12 - 9*a0*a2**2*a3*a6/2 + 21*a0*a2**2*a3/4 - 3*a0*a2*a4*a6**2 + 3*a0*a2*a4*a6 - a0*a2*a4/4 - a0*a2*a5**2*a6/2 + 5*a0*a2*a5**2/12 - 3*a0*a5*a6**3/2 + 11*a0*a5*a6**2/4 - 2*a0*a5*a6/3 + a0*a5/48 + 3*a1**3*a3*a5 - 9*a1**2*a2*a3*a6 + 2*a1**2*a2*a4*a5 - a1**2*a4*a6 - a1**2*a4/6 - 3*a1**2*a5**2*a6/2 - a1**2*a5**2/12 + 9*a1*a2**3*a3/2 + 3*a1*a2**2*a4*a6 - a1*a2**2*a4/2 + 3*a1*a2**2*a5**2/2 - 9*a1*a2*a5*a6/2 + 5*a1*a2*a5/6 - 3*a1*a6**3 + 9*a1*a6**2/2 - 17*a1*a6/12 + 7*a1/48 - 3*a2**4*a4/2 + 7*a2**3*a5/2 + 9*a2**2*a6**2/2 - 35*a2**2*a6/8 + a2**2/2",
          "a0**2*a2*a4**2/2 + a0**2*a4*a5*a6/2 - a0**2*a4*a5/6 - a0*a1**2*a4**2/2 + a0*a1*a2*a4*a5 + a0*a1*a4/12 + 2*a0*a1*a5**2*a6 - 5*a0*a1*a5**2/6 - a0*a2**2*a4 + 2*a0*a2**2*a5**2 + 12*a0*a2*a5*a6**2 - 19*a0*a2*a5*a6/2 + 37*a0*a2*a5/24 + 27*a0*a6**4/2 - 39*a0*a6**3/2 + 9*a0*a6**2 - 79*a0*a6/48 + 5*a0/48 - 3*a1**3*a4*a5/2 + 3*a1**2*a2*a4/4 - 7*a1**2*a2*a5**2/2 + 3*a1**2*a5*a6**2/2 - 5*a1**2*a5*a6/4 + 5*a1**2*a5/8 - 33*a1*a2**2*a5*a6/2 + 6*a1*a2**2*a5 - 18*a1*a2*a6**3 + 69*a1*a2*a6**2/4 - 21*a1*a2*a6/8 - 3*a1*a2/16 + 6*a2**4*a5 + 9*a2**3*a6**2 - 21*a2**3*a6/4 - 3*a2**3/4",
          "3*a0*a2*a3*a4*a5 - a0*a2*a4**3 + 9*a0*a3*a4*a6**2 - 9*a0*a3*a4*a6/2 + a0*a3*a4/2 - 2*a0*a4**2*a5*a6 + a0*a4**2*a5/2 + a0*a4*a5**3/3 - 3*a1**2*a3*a4*a5 + a1**2*a4**3 - 18*a1*a2*a3*a4*a6 + 9*a1*a2*a3*a4/2 + 2*a1*a2*a4**2*a5 - 6*a1*a4**2*a6**2 + 3*a1*a4**2*a6 - a1*a4**2/2 + 2*a1*a4*a5**2*a6 - a1*a4*a5**2/2 + 9*a2**3*a3*a4 + 6*a2**2*a4**2*a6 - 3*a2**2*a4**2/2 + a2**2*a4*a5**2 + 9*a2*a4*a5*a6**2 - 9*a2*a4*a5*a6/2 + a2*a4*a5/4 + 9*a4*a6**4 - 9*a4*a6**3 + 11*a4*a6**2/4 - a4*a6/4",
          "3*a0*a1*a3*a4*a5 - a0*a1*a4**3 + 9*a0*a2*a3*a4*a6 - 3*a0*a2*a3*a4/2 + 6*a0*a2*a3*a5**2 - 3*a0*a2*a4**2*a5 + 18*a0*a3*a5*a6**2 - 9*a0*a3*a5*a6 + a0*a3*a5 + 3*a0*a4**2*a6**2 - a0*a4**2*a6/2 - 5*a0*a4*a5**2*a6 + a0*a4*a5**2 + 2*a0*a5**4/3 + 9*a1**2*a3*a4*a6 - 3*a1**2*a3*a4 - a1**2*a4**2*a5 - 9*a1*a2**2*a3*a4 + 9*a1*a2*a3*a5*a6 - 9*a1*a2*a3*a5/2 - 3*a1*a2*a4**2*a6 + a1*a2*a4**2/2 - 2*a1*a2*a4*a5**2 + 27*a1*a3*a6**3 - 63*a1*a3*a6**2/2 + 51*a1*a3*a6/4 - 7*a1*a3/4 - 9*a1*a4*a5*a6**2 + 8*a1*a4*a5*a6 - 7*a1*a4*a5/4 + a1*a5**3*a6 - 7*a1*a5**3/6 - 18*a2**3*a3*a5 + 3*a2**3*a4**2 - 54*a2**2*a3*a6**2 + 63*a2**2*a3*a6/2 - 6*a2**2*a3 + 6*a2**2*a4*a5*a6 - 9*a2**2*a4*a5/2 - 2*a2**2*a5**3 - 9*a2*a4*a6**3 + 6*a2*a4*a6**2 - 3*a2*a4*a6/2 - 7*a2*a5**2*a6/2 - 9*a5*a6**3/2 + 3*a5*a6**2/2",
          "-a0**2*a3*a4*a5 + a0**2*a4**3/3 - 3*a0*a1*a3*a4*a6 + a0*a1*a3*a4 - 2*a0*a1*a3*a5**2 + a0*a1*a4**2*a5 - 3*a0*a2**2*a3*a4 - 6*a0*a2*a3*a5*a6 + 3*a0*a2*a3*a5 - 3*a0*a2*a4**2*a6 + a0*a2*a4**2/2 + a0*a2*a4*a5**2 + 9*a0*a3*a6**2/2 - 3*a0*a3*a6 + a0*a3/2 - 3*a0*a4*a5*a6**2 + 2*a0*a4*a5*a6/3 + a0*a4*a5/6 + 2*a0*a5**3*a6/3 + 3*a1**2*a2*a3*a4 - 3*a1**2*a3*a5*a6 + a1**2*a3*a5/2 + 2*a1**2*a4**2*a6 - a1**2*a4**2/6 + 6*a1*a2**2*a3*a5 - a1*a2**2*a4**2 - 9*a1*a2*a3*a6**2 + a1*a2*a3 + a1*a2*a4*a5*a6 + 4*a1*a2*a4*a5/3 - 6*a1*a4*a6**3 + 4*a1*a4*a6**2 - 11*a1*a4*a6/12 + a1*a4/12 + a1*a5**2*a6**2 + a1*a5**2*a6/3 + a1*a5**2/12 + 18*a2**3*a3*a6 - 3*a2**3*a3 - a2**3*a4*a5 + 9*a2**2*a4*a6**2 - 4*a2**2*a4*a6 + a2**2*a4/2 - 2*a2**2*a5**2*a6 + 2*a2**2*a5**2 + 11*a2*a5*a6**2/2 - 11*a2*a5*a6/4 + a2*a5/4 + 9*a6**4/2 - 21*a6**3/4 + 2*a6**2 - a6/4",
          "-3*a0**2*a3*a4*a6 + a0**2*a3*a4/2 + a0**2*a4**2*a5/3 + 6*a0*a1*a2*a3*a4 - 6*a0*a1*a3*a5*a6 + a0*a1*a3*a5 + a0*a1*a4**2*a6 - a0*a1*a4**2/2 + a0*a1*a4*a5**2 + 6*a0*a2**2*a3*a5 + a0*a2**2*a4**2 - 3*a0*a2*a3*a6/2 + a0*a2*a3 + 2*a0*a2*a4*a5*a6 - a0*a2*a4*a5/2 + 2*a0*a2*a5**3/3 - 3*a0*a4*a6**3 + 2*a0*a4*a6**2 - a0*a4*a6/4 + 2*a0*a5**2*a6**2 - 5*a0*a5**2*a6/6 + a0*a5**2/6 - 3*a1**3*a3*a4 - a1**2*a2*a4**2 - 9*a1**2*a3*a6**2 + 15*a1**2*a3*a6/2 - 7*a1**2*a3/4 + 3*a1**2*a4*a5*a6 - 5*a1**2*a4*a5/3 + 27*a1*a2**2*a3*a6 - 15*a1*a2**2*a3/2 - 3*a1*a2**2*a4*a5 + 9*a1*a2*a4*a6**2 - 5*a1*a2*a4*a6 + 3*a1*a2*a4/4 + a1*a2*a5**2*a6 - 7*a1*a2*a5**2/6 + 3*a1*a5*a6**3 - 5*a1*a5*a6**2/2 + 11*a1*a5*a6/6 - 7*a1*a5/24 - 18*a2**4*a3 - 9*a2**3*a4*a6 + 3*a2**3*a4 - 2*a2**3*a5**2 - 6*a2**2*a5*a6**2 + 2*a2**2*a5*a6 - a2**2*a5/2 - 3*a2*a6**3/2 + 7*a2*a6**2/4 - a2*a6/2",
          "a0**2*a4**2*a6 - a0**2*a4**2/6 - a0**2*a4*a5**2/3 - 2*a0*a1*a2*a4**2 + a0*a1*a4*a5/2 - 2*a0*a1*a5**3/3 - 4*a0*a2**2*a4*a5 - 6*a0*a2*a4*a6**2 + 4*a0*a2*a4*a6 - 3*a0*a2*a4/4 - 4*a0*a2*a5**2*a6 + a0*a2*a5**2 - 6*a0*a5*a6**3 + 9*a0*a5*a6**2/2 - 4*a0*a5*a6/3 + a0*a5/6 + a1**3*a4**2 + 2*a1**2*a2*a4*a5 + a1**2*a4/12 - a1**2*a5**2*a6 + 7*a1**2*a5**2/6 - a1*a2**2*a4/2 + 2*a1*a2**2*a5**2 - 6*a1*a2*a5*a6**2 + 9*a1*a2*a5*a6 - 23*a1*a2*a5/12 - 9*a1*a6**4 + 15*a1*a6**3 - 19*a1*a6**2/2 + 65*a1*a6/24 - 7*a1/24 + 3*a2**4*a4 + 12*a2**3*a5*a6 - 7*a2**3*a5 + 18*a2**2*a6**3 - 39*a2**2*a6**2/2 + 29*a2**2*a6/4 - a2**2"
        &#93;,
        &#91;
          "3*a0*a1*a3**2*a5/2 - a0*a1*a3*a4**2/2 + 9*a0*a2*a3**2*a6/2 - 3*a0*a2*a3**2/4 - 3*a0*a2*a3*a4*a5/2 + a0*a2*a4**3/3 - 3*a0*a3*a4*a6**2/2 + 5*a0*a3*a4*a6/4 - a0*a3*a4/6 - a0*a3*a5**2*a6/2 + 2*a0*a4**2*a5*a6/3 - a0*a4**2*a5/6 - a0*a4*a5**3/9 + 9*a1**2*a3**2*a6/2 - 3*a1**2*a3**2/2 + a1**2*a3*a4*a5/2 - a1**2*a4**3/3 - 9*a1*a2**2*a3**2/2 + 6*a1*a2*a3*a4*a6 - 2*a1*a2*a3*a4 - a1*a2*a3*a5**2 - 2*a1*a2*a4**2*a5/3 - 3*a1*a3*a5*a6**2/2 + a1*a3*a5*a6/4 + a1*a3*a5/4 + 2*a1*a4**2*a6**2 - 2*a1*a4**2*a6/3 - 2*a1*a4*a5**2*a6/3 + a1*a4*a5**2/12 - 9*a2**3*a3*a4/2 - 3*a2**2*a3*a5*a6 - 3*a2**2*a3*a5/2 - 2*a2**2*a4**2*a6 + 5*a2**2*a4**2/6 - a2**2*a4*a5**2/3 - 9*a2*a3*a6**3/2 - 15*a2*a3*a6**2/4 + 13*a2*a3*a6/4 - 5*a2*a3/12 - 3*a2*a4*a5*a6**2 + 9*a2*a4*a5*a6/4 - 5*a2*a4*a5/12 - 7*a2*a5**3/36 - 3*a4*a6**4 + 2*a4*a6**3 - a4*a6**2/4 + a5**2*a6**2/12 - a5**2*a6/12",
          "-3*a0**2*a3**2*a5/2 + a0**2*a3*a4**2/2 - 9*a0*a1*a3**2*a6 + 3*a0*a1*a3**2 + a0*a1*a4**3/3 - 6*a0*a2*a3*a4*a6 + 7*a0*a2*a3*a4/4 - a0*a2*a3*a5**2 + a0*a2*a4**2*a5 - 6*a0*a3*a5*a6**2 + 7*a0*a3*a5*a6/2 - 7*a0*a3*a5/12 - a0*a4**2*a6**2 - a0*a4**2*a6/6 + a0*a4**2/6 + 5*a0*a4*a5**2*a6/3 - a0*a4*a5**2/4 - 2*a0*a5**4/9 + 9*a1**2*a2*a3**2/2 - 3*a1**2*a3*a4*a6 + 3*a1**2*a3*a4/2 + a1**2*a3*a5**2/2 + a1**2*a4**2*a5/3 + 6*a1*a2**2*a3*a4 + 9*a1*a2*a3*a5/4 + a1*a2*a4**2*a6 + 2*a1*a2*a4*a5**2/3 - 9*a1*a3*a6**3 + 12*a1*a3*a6**2 - 15*a1*a3*a6/4 + a1*a3/4 + 3*a1*a4*a5*a6**2 - 2*a1*a4*a5*a6 + a1*a4*a5/3 - a1*a5**3*a6/3 + a1*a5**3/4 + 15*a2**3*a3*a5/2 - a2**3*a4**2 + 45*a2**2*a3*a6**2/2 - 21*a2**2*a3*a6/2 - 3*a2**2*a3/4 - 2*a2**2*a4*a5*a6 + 5*a2**2*a4*a5/4 + 2*a2**2*a5**3/3 + 3*a2*a4*a6**3 - a2*a4*a6**2/2 - 23*a2*a4*a6/12 + 5*a2*a4/12 + a2*a5**2*a6/4 + a2*a5**2/4 + a5*a6**3/2 - 7*a5*a6**2/12 + a5*a6/6",
          "a0**2*a3**2/4 - a0**2*a3*a4*a5/3 + a0**2*a4**3/9 - 3*a0*a1*a2*a3**2/2 - 3*a0*a1*a3*a4*a6/2 + 3*a0*a1*a3*a4/4 - 2*a0*a1*a3*a5**2/3 + a0*a1*a4**2*a5/3 - 3*a0*a2**2*a3*a4/2 - 5*a0*a2*a3*a5*a6/2 + a0*a2*a3*a5/4 - a0*a2*a4**2*a6 + 4*a0*a2*a4**2/9 + a0*a2*a4*a5**2/3 - a0*a3*a6**2/4 + 3*a0*a3*a6/8 - a0*a3/12 - a0*a4*a5*a6**2 + 25*a0*a4*a5*a6/36 - 5*a0*a4*a5/36 + 2*a0*a5**3*a6/9 - a0*a5**3/9 + 3*a1**3*a3**2/2 + 2*a1**2*a2*a3*a4 - 3*a1**2*a3*a5*a6/2 + a1**2*a3*a5 + 2*a1**2*a4**2*a6/3 - a1**2*a4**2/6 + 3*a1*a2**2*a3*a5 - a1*a2**2*a4**2/3 - 9*a1*a2*a3*a6**2/2 + 5*a1*a2*a3*a6/2 - 5*a1*a2*a3/6 + a1*a2*a4*a5*a6/3 + 7*a1*a2*a4*a5/36 - 2*a1*a4*a6**3 + 7*a1*a4*a6**2/3 - 13*a1*a4*a6/12 + a1*a4/6 + a1*a5**2*a6**2/3 - 5*a1*a5**2*a6/12 + a1*a5**2/8 + 15*a2**3*a3*a6/2 - 5*a2**3*a3/2 - a2**3*a4*a5/3 + 3*a2**2*a4*a6**2 - 8*a2**2*a4*a6/3 + 5*a2**2*a4/12 - 2*a2**2*a5**2*a6/3 + 19*a2**2*a5**2/36 - a2*a5*a6**2/3 + 11*a2*a5*a6/72 + a2*a5/36 - a6**4/2 + 3*a6**3/4 - a6**2/3 + a6/24",
          "-3*a0**2*a2*a3**2/2 + a0**2*a3*a4*a6/2 - a0**2*a3*a4/12 - a0**2*a4**2*a5/9 + 3*a0*a1**2*a3**2/2 - 3*a0*a1*a2*a3*a4/2 + 3*a0*a1*a3*a5*a6/2 - 5*a0*a1*a3*a5/12 - a0*a1*a4**2*a6/3 + a0*a1*a4**2/6 - a0*a1*a4*a5**2/3 - a0*a2**2*a3*a5 - a0*a2**2*a4**2/3 + 3*a0*a2*a3*a6**2/2 + a0*a2*a3*a6 - a0*a2*a3/24 - 2*a0*a2*a4*a5*a6/3 + 2*a0*a2*a4*a5/9 - 2*a0*a2*a5**3/9 + a0*a4*a6**3 - a0*a4*a6**2/3 - 5*a0*a4*a6/36 + a0*a4/36 - 2*a0*a5**2*a6**2/3 + 7*a0*a5**2*a6/18 - a0*a5**2/72 + a1**3*a3*a4 - a1**2*a2*a3*a5/2 + a1**2*a2*a4**2/3 + 3*a1**2*a3*a6**2 - 7*a1**2*a3*a6/2 + a1**2*a3/2 - a1**2*a4*a5*a6 + a1**2*a4*a5/3 - 12*a1*a2**2*a3*a6 + 5*a1*a2**2*a3/2 + a1*a2**2*a4*a5 - 3*a1*a2*a4*a6**2 + 7*a1*a2*a4*a6/6 + a1*a2*a4/9 - a1*a2*a5**2*a6/3 + a1*a2*a5**2/18 - a1*a5*a6**3 + 7*a1*a5*a6**2/6 - a1*a5*a6/3 + 15*a2**4*a3/2 + 3*a2**3*a4*a6 - 4*a2**3*a4/3 + 2*a2**3*a5**2/3 + 2*a2**2*a5*a6**2 - 11*a2**2*a5*a6/6 + 53*a2**2*a5/72 + 11*a2*a6**2/12 - 43*a2*a6/72 + 5*a2/72",
          "a0**2*a2*a3*a4/2 + a0**2*a3*a5*a6/2 - a0**2*a3*a5/6 - a0**2*a4**2*a6/3 + a0**2*a4**2/18 + a0**2*a4*a5**2/9 - a0*a1**2*a3*a4/2 + 2*a0*a1*a2*a4**2/3 + 3*a0*a1*a3*a6**2 - 2*a0*a1*a3*a6 + a0*a1*a3/3 - a0*a1*a4*a5/6 + 2*a0*a1*a5**3/9 - 3*a0*a2**2*a3*a6/2 + 3*a0*a2**2*a3/4 + 4*a0*a2**2*a4*a5/3 + 2*a0*a2*a4*a6**2 - 11*a0*a2*a4*a6/6 + 2*a0*a2*a4/9 + 4*a0*a2*a5**2*a6/3 - 11*a0*a2*a5**2/36 + 2*a0*a5*a6**3 - 23*a0*a5*a6**2/12 + 13*a0*a5*a6/24 - a0*a5/24 - a1**3*a3*a5/2 - a1**3*a4**2/3 - 3*a1**2*a2*a3*a6 + 3*a1**2*a2*a3/4 - 2*a1**2*a2*a4*a5/3 + a1**2*a4/12 + a1**2*a5**2*a6/3 - a1**2*a5**2/4 + 3*a1*a2**3*a3/2 + 2*a1*a2**2*a4/3 - 2*a1*a2**2*a5**2/3 + 2*a1*a2*a5*a6**2 - 5*a1*a2*a5*a6/3 + 7*a1*a2*a5/24 + 3*a1*a6**4 - 5*a1*a6**3 + 17*a1*a6**2/6 - 5*a1*a6/8 + a1/24 - a2**4*a4 - 4*a2**3*a5*a6 + 29*a2**3*a5/12 - 6*a2**2*a6**3 + 8*a2**2*a6**2 - 37*a2**2*a6/12 + 7*a2**2/24",
          "3*a0*a2*a3**2*a5 - a0*a2*a3*a4**2 + 9*a0*a3**2*a6**2 - 9*a0*a3**2*a6/2 + a0*a3**2/2 - 2*a0*a3*a4*a5*a6 + a0*a3*a4*a5/2 + a0*a3*a5**3/3 - 3*a1**2*a3**2*a5 + a1**2*a3*a4**2 - 18*a1*a2*a3**2*a6 + 9*a1*a2*a3**2/2 + 2*a1*a2*a3*a4*a5 - 6*a1*a3*a4*a6**2 + 3*a1*a3*a4*a6 - a1*a3*a4/2 + 2*a1*a3*a5**2*a6 - a1*a3*a5**2/2 + 9*a2**3*a3**2 + 6*a2**2*a3*a4*a6 - 3*a2**2*a3*a4/2 + a2**2*a3*a5**2 + 9*a2*a3*a5*a6**2 - 9*a2*a3*a5*a6/2 + a2*a3*a5/4 + 9*a3*a6**4 - 9*a3*a6**3 + 11*a3*a6**2/4 - a3*a6/4",
          "3*a0*a1*a3**2*a5 - a0*a1*a3*a4**2 + 9*a0*a2*a3**2*a6 - 3*a0*a2*a3**2/2 - a0*a2*a3*a4*a5 + 3*a0*a3*a4*a6**2 - a0*a3*a4*a6/2 - a0*a3*a5**2*a6 + 9*a1**2*a3**2*a6 - 3*a1**2*a3**2 - a1**2*a3*a4*a5 - 9*a1*a2**2*a3**2 - a1*a2*a3*a4 - 2*a1*a2*a3*a5**2 - 3*a1*a3*a5*a6**2 + a1*a3*a5*a6/2 + a1*a3*a5/2 + 2*a1*a4**2*a6/3 - a1*a4**2/3 - a1*a4*a5**2/6 - 3*a2**3*a3*a4 - 6*a2**2*a3*a5*a6 - 3*a2**2*a3*a5 + 2*a2**2*a4**2/3 - 9*a2*a3*a6**3 - 15*a2*a3*a6**2/2 + 13*a2*a3*a6/2 - 5*a2*a3/6 + 3*a2*a4*a5*a6/2 - 2*a2*a4*a5/3 - 7*a2*a5**3/18 - 2*a4*a6**3 + 4*a4*a6**2/3 - a4*a6/6 + a5**2*a6**2/6 - a5**2*a6/6",
          "-a0**2*a3**2*a5 + a0**2*a3*a4**2/3 - 3*a0*a1*a3**2*a6 + a0*a1*a3**2 + a0*a1*a3*a4*a5/3 - 3*a0*a2**2*a3**2 - 3*a0*a2*a3*a4*a6 + 5*a0*a2*a3*a4/6 + a0*a2*a3*a5**2/3 - a0*a3*a5*a6**2 + 2*a0*a3*a5*a6/3 - a0*a3*a5/6 - 2*a0*a4**2*a6/9 + a0*a4**2/9 + a0*a4*a5**2/18 + 3*a1**2*a2*a3**2 + a1**2*a3*a4*a6 + a1*a2**2*a3*a4 + 5*a1*a2*a3*a5/3 - 2*a1*a2*a4**2/9 - 3*a1*a3*a6**3 + 5*a1*a3*a6**2/2 - a1*a3*a6/2 + a1*a4*a5*a6/6 + a2**3*a3*a5 + 3*a2**2*a3*a6**2 + 3*a2**2*a3*a6 - 5*a2**2*a3/3 - 2*a2**2*a4*a5/9 + 2*a2*a4*a6**2 - 14*a2*a4*a6/9 + 5*a2*a4/18 - 7*a2*a5**2*a6/18 + 7*a2*a5**2/36 + a5*a6**3/6 - a5*a6**2/4 + a5*a6/12",
          "-3*a0**2*a3**2*a6 + a0**2*a3**2/2 + a0**2*a3*a4*a5/3 + 6*a0*a1*a2*a3**2 + a0*a1*a3*a4*a6 - a0*a1*a3*a4/2 + a0*a1*a3*a5**2/3 + a0*a2**2*a3*a4 - 2*a0*a2*a3*a5/3 + a0*a2*a4**2/3 - 3*a0*a3*a6**3 + a0*a3*a6**2 - a0*a3*a6/12 + 4*a0*a4*a5*a6/9 - a0*a4*a5/18 - a0*a5**3/18 - 3*a1**3*a3**2 - a1**2*a2*a3*a4 + 2*a1**2*a3*a5*a6 - a1**2*a4**2/3 - a1*a2**2*a3*a5 + 6*a1*a2*a3*a6**2 + 4*a1*a2*a3*a6 - 5*a1*a2*a3/6 - 8*a1*a2*a4*a5/9 + 4*a1*a4*a6**2/3 - a1*a4*a6/3 - a1*a5**2*a6/3 + a1*a5**2/12 - 3*a2**3*a3*a6 - 5*a2**3*a3 - 8*a2**2*a4*a6/3 + 5*a2**2*a4/6 - 5*a2**2*a5**2/9 - 5*a2*a5*a6**2/2 + 49*a2*a5*a6/36 - 5*a2*a5/36 - a6**4 + 2*a6**3/3 - a6**2/12",
          "a0**2*a3*a4*a6 - a0**2*a3*a4/6 - a0**2*a3*a5**2/3 - 2*a0*a1*a2*a3*a4 - 2*a0*a1*a3*a5*a6 + 5*a0*a1*a3*a5/6 - 2*a0*a2**2*a3*a5 - 6*a0*a2*a3*a6**2 + 7*a0*a2*a3*a6/2 - 5*a0*a2*a3/12 - a0*a2*a4*a5/6 - 2*a0*a4*a6**2/3 + 4*a0*a4*a6/9 - a0*a4/18 + a0*a5**2*a6/18 - a0*a5**2/18 + a1**3*a3*a4 + 2*a1**2*a2*a3*a5 - 3*a1**2*a3*a6**2 + 5*a1**2*a3*a6/2 - a1**2*a3/2 + a1**2*a4*a5/6 + 9*a1*a2**2*a3*a6 - 3*a1*a2**2*a3 - 2*a1*a2*a4/9 + 7*a1*a2*a5**2/18 + a1*a5*a6**2/6 - a1*a5*a6/4 + a1*a5/12 - 3*a2**4*a3 + 2*a2**3*a4/3 + 5*a2**2*a5*a6/2 - 41*a2**2*a5/36 + 4*a2*a6**3 - 13*a2*a6**2/3 + 13*a2*a6/9 - 5*a2/36"
        &#93;
      &#93;,
      "shape": &#91;
        5,
        10
      &#93;
    },
    "R": {
      "entries": &#91;
        &#91;
          "-96*a0*a1*a5 - 216*a0*a2*a6 - 84*a0*a2 - 144*a1**2*a6 + 216*a1**2 + 504*a1*a2**2",
          "96*a0*a2*a5 - 24*a0 + 144*a1*a2*a6 - 264*a1*a2 - 288*a2**3",
          "-24",
          "-48*a2",
          "-144*a1"
        &#93;,
        &#91;
          "-96*a0*a2*a5 - 216*a0*a6**2 + 168*a0*a6 - 18*a0 + 72*a1*a2*a6 + 36*a1*a2 + 288*a2**3",
          "96*a0*a5*a6 - 48*a0*a5 + 144*a1*a6**2 - 96*a1*a6 + 12*a1 - 288*a2**2*a6 - 96*a2**2",
          "0",
          "24 - 48*a6",
          "-144*a2"
        &#93;,
        &#91;
          "72*a0*a5*a6 + 12*a0*a5 + 216*a1*a2*a5 + 432*a1*a6**2 - 504*a1*a6 + 36*a1 - 864*a2**2*a6 + 144*a2**2",
          "96*a0*a5**2 + 144*a1*a5*a6 - 24*a1*a5 - 288*a2**2*a5 + 720*a2*a6 - 120*a2",
          "0",
          "-48*a5",
          "432*a6 - 72"
        &#93;,
        &#91;
          "-216*a0*a4*a6 + 60*a0*a4 + 96*a0*a5**2 + 216*a1*a2*a4 + 144*a1*a5*a6 - 144*a1*a5 - 288*a2**2*a5 + 36*a2",
          "96*a0*a4*a5 + 144*a1*a4*a6 - 24*a1*a4 - 288*a2**2*a4 + 240*a2*a5",
          "0",
          "-48*a4",
          "144*a5"
        &#93;,
        &#91;
          "-648*a0*a3*a6 + 180*a0*a3 + 96*a0*a4*a5 + 648*a1*a2*a3 + 144*a1*a4*a6 - 144*a1*a4 - 288*a2**2*a4 - 36*a6",
          "288*a0*a3*a5 + 432*a1*a3*a6 - 72*a1*a3 - 864*a2**2*a3 + 240*a2*a4",
          "0",
          "-144*a3",
          "144*a4"
        &#93;,
        &#91;
          "-48*a0**2*a5 - 72*a0*a1*a6 + 72*a0*a1 + 288*a0*a2**2 - 72*a1**2*a2",
          "-96*a0*a2",
          "24*a2",
          "0",
          "-72*a0"
        &#93;,
        &#91;
          "-48*a0*a1*a5 + 144*a0*a2*a6 - 144*a1**2*a6 + 72*a1**2 + 144*a1*a2**2",
          "24*a0*a6 + 12*a0 - 120*a1*a2",
          "24*a6",
          "0",
          "-72*a1"
        &#93;,
        &#91;
          "-288*a0*a2*a5 - 108*a0*a6 + 12*a0 + 72*a1**2*a5 - 216*a1*a2*a6 + 324*a1*a2 + 432*a2**3",
          "24*a0*a5 + 72*a1*a6 + 24*a1 - 504*a2**2",
          "-24*a5",
          "-24",
          "-216*a2"
        &#93;,
        &#91;
          "144*a0*a2*a4 - 144*a0*a5*a6 + 72*a0*a5 - 72*a1**2*a4 - 216*a1*a6**2 + 324*a1*a6 - 126*a1 + 432*a2**2*a6 - 216*a2**2",
          "24*a0*a4 - 360*a2*a6 + 216*a2",
          "24*a4",
          "0",
          "108 - 216*a6"
        &#93;,
        &#91;
          "432*a0*a2*a3 - 48*a0*a5**2 - 216*a1**2*a3 - 72*a1*a5*a6 + 72*a1*a5 + 144*a2**2*a5 + 18*a2",
          "72*a0*a3 - 120*a2*a5 - 36*a6",
          "72*a3",
          "0",
          "-72*a5"
        &#93;
      &#93;,
      "shape": &#91;
        10,
        5
      &#93;
    }
  },
  "parameters": &#91;
    "a0",
    "a1",
    "a2",
    "a3",
    "a4",
    "a5",
    "a6"
  &#93;,
  "ring": "Q&#91;a0,...,a6&#93;",
  "schema_version": 1
}
</code></pre>

<a id="source-6dc9eb2635a2bed8"></a>

## `research-notes/lane7-component-inputs-20260803-v1/manifest.json`

<pre><code class="language-json">
{
  "schema_version": 1,
  "packet_id": "lane7-component-inputs-20260803-v1",
  "status": "exact_reconstruction_passed",
  "ring": "Q&#91;a0,...,a6&#93;",
  "research_interface": "research-notes/lane7-component-inputs-20260803-v1/lane7_exact_component_bundle.json",
  "files": &#91;
    {
      "path": "research-notes/lane7-component-inputs-20260803-v1/README.md",
      "role": "mathematical interface and scope",
      "sha256": "8241282f6528aec7a6f79a9ba5cba3044f2c351e1b57dacff433c26dfa7e596f"
    },
    {
      "path": "research-notes/lane7-component-inputs-20260803-v1/build_component_bundle.py",
      "role": "deterministic builder",
      "sha256": "5c76818fa360d3f0bbf9ebf723f5091e301a051bcad2ea5777dabd74acc8339a"
    },
    {
      "path": "research-notes/lane7-component-inputs-20260803-v1/verify_component_bundle.py",
      "role": "exact verifier",
      "sha256": "9b7ef6d11825e537a35c7a89857690f8f305ec9c9c764c4fc5551acd1d077fc8"
    },
    {
      "path": "research-notes/lane7-component-inputs-20260803-v1/lane7_exact_component_bundle.json",
      "role": "self-contained research input",
      "sha256": "6699a296a95d68d64653b1c39dd52866cef36361c50df13f258ef068b277907e"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/reconstruct_matrices.py",
      "role": "source reconstruction helper",
      "sha256": "b6bbbbec46eeffc89f1f535cfb859d3bcb1f10b1debe39217af49b7e76fd824f"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/collision-system.json",
      "role": "original collision equations",
      "sha256": "23c607c2efc6115437fcc2979f5caff583fd1d7fa9c02f382bf10686d3e07167"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/quadratic_syzygies.json",
      "role": "source-block reconstruction",
      "sha256": "3dbbf36b46c6ba5dc80745cbdc46c97da934e4c35e05961c9b123bd54a3d1a37"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/V_quadratic_syzygies.json",
      "role": "target-block reconstruction",
      "sha256": "4a384970a04f7a68d35c6d3870deddb082ed27c4d4922fa829f3d21050159b77"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/Hv_left_inverse.json",
      "role": "left inverse used to reconstruct C",
      "sha256": "243fbaa5dcbc7022a9b23a7b5facb95bf0ad9a9ebcd1eb3f0133a0bcd1a081b4"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json",
      "role": "stored d, H, and C",
      "sha256": "a251278a145ab0cfcf249809267edb2d6529738684b5136ec5faef62c7aa3dfb"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/Hv10_syzygies_exact.json",
      "role": "stored Q",
      "sha256": "fe9dfce8d92db150ed6e9f6d02f4ad7668a2671b3b13ee04f5777d78d851a9aa"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/Hv10_right_inverse_exact.json",
      "role": "stored R",
      "sha256": "120de1d892ca7199d86e2948a438ce9ca3147966a315236e95f00113faa1a674"
    },
    {
      "path": "research-notes/lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json",
      "role": "stored residual matrix M",
      "sha256": "4e1a014a6616a990ac50d255fb7426a9f8ae1d06cbf5066ba52c8415da63cbda"
    }
  &#93;,
  "does_not_establish": &#91;
    "grade six or Cohen--Macaulayness of I_5(M) on D(d)",
    "I_4(M):d^infinity = (1)",
    "component decomposition or purity",
    "generic Plucker nonvanishing on any component",
    "a first-normal obstruction"
  &#93;
}
</code></pre>

<a id="source-03ebac2c2b77f766"></a>

## `research-notes/lane7-component-inputs-20260803-v1/verify_component_bundle.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Verify the Lane 7 compact component bundle against its exact sources."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parent
REPOSITORY = ROOT.parents&#91;1&#93;
SOURCE = ROOT.parent / "lane7-split-incidence-20260802-v1"
sys.path.insert(0, str(ROOT))

from build_component_bundle import parse_entries, theorem_matrices  # noqa: E402


def sha256(path: Path) -&gt; str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_bundle_matrix(
    data: dict, name: str, symbols: tuple&#91;sp.Symbol, ...&#93;
) -&gt; sp.Matrix:
    item = data&#91;"matrices"&#93;&#91;name&#93;
    rows, columns = item&#91;"shape"&#93;
    entries = item&#91;"entries"&#93;
    assert len(entries) == rows
    assert all(len(row) == columns for row in entries)
    local_symbols = {str(variable): variable for variable in symbols}
    return sp.Matrix(
        &#91;&#91;sp.sympify(entry, locals=local_symbols) for entry in row&#93; for row in entries&#93;
    )


def zero(matrix: sp.Matrix) -&gt; bool:
    return all(sp.expand(entry) == 0 for entry in matrix)


def main() -&gt; int:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    hash_checks: dict&#91;str, bool&#93; = {}
    for entry in manifest&#91;"files"&#93;:
        path = REPOSITORY / entry&#91;"path"&#93;
        hash_checks&#91;entry&#91;"path"&#93;&#93; = path.is_file() and sha256(path) == entry&#91;"sha256"&#93;
    if not all(hash_checks.values()):
        raise SystemExit(f"manifest hash failure: {hash_checks}")

    bundle = json.loads(
        (ROOT / "lane7_exact_component_bundle.json").read_text(encoding="utf-8")
    )
    parameters = sp.symbols("a0:7")
    local_symbols = {str(variable): variable for variable in parameters}
    determinant = sp.sympify(bundle&#91;"d"&#93;, locals=local_symbols)
    matrix_m = parse_bundle_matrix(bundle, "M", parameters)
    matrix_a = parse_bundle_matrix(bundle, "A", parameters)
    matrix_ca = parse_bundle_matrix(bundle, "CA", parameters)
    matrix_h = parse_bundle_matrix(bundle, "H", parameters)
    matrix_c = parse_bundle_matrix(bundle, "C", parameters)
    matrix_q = parse_bundle_matrix(bundle, "Q", parameters)
    matrix_r = parse_bundle_matrix(bundle, "R", parameters)

    source_d, source_a, source_h, source_c, source_q, source_r = theorem_matrices()
    source_m = parse_entries(SOURCE / "collision_residual_matrix_M.json")
    checks = {
        "bundle_d_matches_source": sp.expand(determinant - source_d) == 0,
        "bundle_M_matches_source": matrix_m == source_m,
        "bundle_A_matches_reconstruction": matrix_a == source_a,
        "bundle_H_matches_reconstruction": matrix_h == source_h,
        "bundle_C_matches_reconstruction": matrix_c == source_c,
        "bundle_Q_matches_source": matrix_q == source_q,
        "bundle_R_matches_source": matrix_r == source_r,
        "bundle_CA_is_C_times_A": zero(matrix_ca - matrix_c * matrix_a),
        "C_H_is_dI5": zero(matrix_c * matrix_h - determinant * sp.eye(5)),
        "Q_H_is_zero": zero(matrix_q * matrix_h),
        "C_R_is_zero": zero(matrix_c * matrix_r),
        "Q_R_is_dI5": zero(matrix_q * matrix_r - determinant * sp.eye(5)),
        "H_C_plus_R_Q_is_dI10": zero(
            matrix_h * matrix_c + matrix_r * matrix_q - determinant * sp.eye(10)
        ),
    }

    kernel = sp.Matrix(sp.symbols("u0:5"))
    second_numerator = matrix_ca * kernel
    plucker_checks = {}
    for i in range(5):
        for j in range(i + 1, 5):
            eta = sp.expand(
                kernel&#91;i&#93; * second_numerator&#91;j&#93; - kernel&#91;j&#93; * second_numerator&#91;i&#93;
            )
            reconstructed_minor = sp.cancel(
                kernel&#91;i&#93; * (-second_numerator&#91;j&#93; / determinant)
                - kernel&#91;j&#93; * (-second_numerator&#91;i&#93; / determinant)
            )
            plucker_checks&#91;f"eta_{i}{j}"&#93; = (
                sp.cancel(determinant * reconstructed_minor + eta) == 0
            )
    checks&#91;"all_ten_plucker_transport_signs"&#93; = all(plucker_checks.values())
    if not all(checks.values()):
        raise SystemExit(f"exact check failure: {checks}")

    report = {
        "schema_version": 1,
        "status": "pass",
        "checks": checks,
        "manifest_hashes_checked": len(hash_checks),
        "matrix_shapes": {
            name: bundle&#91;"matrices"&#93;&#91;name&#93;&#91;"shape"&#93;
            for name in ("M", "A", "CA", "H", "C", "Q", "R")
        },
        "does_not_establish": bundle&#91;"does_not_establish"&#93;,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-740f2fbd37373ad8"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/README.md`

<pre><code class="language-markdown">
# Lane 7 exact projective-kernel chart packet

This packet preserves the useful new machinery from public site PR 7 at
exact head 4c488f26a510271aa73cf1cd8a5fc2cf3446ad69. It is an extension of the
canonical split-incidence packet in
../lane7-split-incidence-20260802-v1/, not a replacement for it.

## Mathematical interface

Let M(a) be the stored 10 by 5 residual matrix, let d(a) be the determinant
used to define the accepted open set D(d), and let &#91;u&#93; lie in P^4. The
projective kernel incidence is

    I = {(a,&#91;u&#93;) : M(a)u=0 and d(a) is nonzero}.

The five affine charts u_i=1 cover P^4. On each chart the packet writes the
ten exact equations M(a)u=0 together with z*d(a)-1. Therefore exact
dimensions of all five localized chart ideals determine the dimension of I.
The generators do not themselves compute those dimensions.

The already-retained Pluecker transport theorem explains how the marked
two-plane data are reconstructed from this kernel incidence. Its proof and
source matrices remain in ../lane7-split-incidence-20260802-v1/.

## Harvested programs

- generate_macaulay2_input.py reconstructs the pinned residual matrix and
  optional localization over Q or a prime field.
- generate_kernel_chart_input.py emits any affine chart for Macaulay2 over a
  prime field.
- generate_kernel_chart_singular.py independently emits the same charts for
  Singular, over a prime field or exactly over Q by modular reconstruction.
- generate_kernel_chart_macaulay2.py emits the same five charts over either
  Q or a good prime.  It is the exact-Q route for the pinned project
  Macaulay2 1.26.06 Apptainer toolchain when no Singular executable is
  available.
- test_plucker_transport.py checks the five Pluecker relations, all ten
  normalized two-plane charts, and the transport identity.
- test_kernel_chart_macaulay2.py checks all ten Q/F_1009 renderings and rejects
  characteristics that kill a denominator-clearing row unit.
- prepare_five_chart_runs.py creates a new run root with ten immutable chart
  directories, the requested separate exact-Q/good-prime Slurm profiles,
  hash-pinned inputs and scripts, a source/toolchain manifest, and explicit
  does-not-establish boundaries.  It refuses an existing run root and does
  not submit jobs.  Each script sets its persistent chart directory as the
  Slurm working directory, so execution does not depend on a submit-side
  worktree being mounted on the compute node.  The manifest pins the package
  versions, package hashes, and complete toolchain hash manifest in addition
  to the launcher and SIF.

The four copied source files have SHA-256 digests:

    5e417707876d39efc5f780ba95cff9f33c9f209b8b14b76a9484e70c12eaef01  generate_macaulay2_input.py
    3a5c8dd3c3aa5d57f2cbb139dad970f96c7c0eaf247b7978fef4d6c3db28dc87  generate_kernel_chart_input.py
    290697bd851eecc2509b09cf440966874cf51fc9c011dc1bd9fcc7fa69af5de7  generate_kernel_chart_singular.py
    22ca784d94dee019eee780909e1e615b6311b4e668e140847a2f8d37f6d39e30  test_plucker_transport.py

## Honest result boundary

At harvest time the PR 7 packet/interface job, finite-field chart job, exact
Q chart job, and disposable Singular-rootfs job were still pending in GitHub
Actions. No chart dimension, codimension, carrier grade, or corank conclusion
is promoted here.

An earlier fixed-row corank assertion in PR 7 was false. A shell pipeline had
also allowed the failed CAS assertion to be masked by tee. Later commits made
pipeline failures propagate and removed the false test. Neither the
withdrawn assertion nor output from that workflow is evidence.

## Local replay

The generators can be replayed against the canonical source packet:

    uv run --with sympy==1.14.0 python \
      research-notes/lane7-projective-kernel-20260803-v1/test_plucker_transport.py

    uv run --with sympy==1.14.0 python \
      research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_singular.py \
      research-notes/lane7-split-incidence-20260802-v1 \
      /tmp/lane7-kernel-chart-0.sing --chart 0 --characteristic 0

Neither Singular nor Macaulay2 is installed on the current host, so local
validation stops after exact source reconstruction and generated-input
inspection. CAS output becomes reusable mathematics only when its logs and
artifacts are preserved and independently checked.

The project also has a hash-pinned rootless Macaulay2 toolchain outside this
repository.  A run using it must record the launcher, SIF and package-manifest
hashes, generated input hash, exact command, scheduler resources, and complete
log.  The exact-Q and good-prime results remain separate evidence: a prime
result is a discovery cross-check, not a characteristic-zero certificate.
</code></pre>

<a id="source-b555e0f9d637888f"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_input.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Generate one localized projective-kernel chart for the Lane 7 matrix.

For a chosen chart ``u_chart = 1``, this writes the ten equations ``M(a)u=0``
in the seven parameter variables, four remaining kernel coordinates, and the
localizer ``z*d-1``.  Coefficients are expanded and reduced in the requested
prime field before they reach the CAS.  This removes rational-expression
parsing and preserves the chart because the packet-specific row multipliers
are units at every accepted prime.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp

from generate_macaulay2_input import ROW_DENOMINATOR_LCMS


def render_polynomial(poly: sp.Poly, characteristic: int) -&gt; str:
    """Render a polynomial with small signed representatives modulo p."""
    rendered: list&#91;str&#93; = &#91;&#93;
    variables = poly.gens
    for exponents, coefficient in poly.terms():
        value = int(coefficient) % characteristic
        if value == 0:
            continue
        if value &gt; characteristic // 2:
            value -= characteristic

        factors: list&#91;str&#93; = &#91;&#93;
        for variable, exponent in zip(variables, exponents):
            if exponent == 1:
                factors.append(str(variable))
            elif exponent &gt; 1:
                factors.append(f"{variable}^{exponent}")
        monomial = "*".join(factors)

        if not monomial:
            term = str(value)
        elif value == 1:
            term = monomial
        elif value == -1:
            term = f"-{monomial}"
        else:
            term = f"{value}*{monomial}"
        rendered.append(term)

    if not rendered:
        return "0"
    return " + ".join(rendered).replace("+ -", "- ")


def parse_integral_polynomial(
    expression: str,
    scale: int,
    parameters: tuple&#91;sp.Symbol, ...&#93;,
    local_symbols: dict&#91;str, sp.Symbol&#93;,
) -&gt; sp.Poly:
    polynomial = sp.Poly(
        scale * sp.sympify(expression, locals=local_symbols),
        *parameters,
        domain=sp.QQ,
    )
    if any(coefficient.q != 1 for coefficient in polynomial.coeffs()):
        raise ValueError("row multiplier failed to clear a coefficient denominator")
    return polynomial


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--chart", type=int, required=True, choices=range(5))
    parser.add_argument("--characteristic", type=int, required=True)
    args = parser.parse_args()

    characteristic = args.characteristic
    if not sp.isprime(characteristic):
        raise ValueError("kernel-chart certificates require a prime characteristic")
    if any(scale % characteristic == 0 for scale in ROW_DENOMINATOR_LCMS):
        raise ValueError("chosen characteristic kills a denominator-clearing row unit")

    residual = json.loads(
        (args.source_directory / "collision_residual_matrix_M.json").read_text(
            encoding="utf-8"
        )
    )
    factorization = json.loads(
        (args.source_directory / "Hv10_split_matrix_factorization.json").read_text(
            encoding="utf-8"
        )
    )
    entries = residual.get("entries")
    determinant = factorization.get("d")
    if not isinstance(entries, list) or len(entries) != 10:
        raise ValueError("expected a 10 by 5 residual matrix")
    if any(not isinstance(row, list) or len(row) != 5 for row in entries):
        raise ValueError("expected a 10 by 5 residual matrix")
    if not isinstance(determinant, str):
        raise ValueError("factorization artifact does not contain determinant d")

    parameters = sp.symbols("a0:7")
    kernel_variables = sp.symbols("x0:4")
    z = sp.Symbol("z")
    local_symbols = {str(variable): variable for variable in parameters}
    free_coordinates = iter(kernel_variables)
    kernel_coordinates: list&#91;sp.Expr&#93; = &#91;
        sp.Integer(1) if index == args.chart else next(free_coordinates)
        for index in range(5)
    &#93;
    all_chart_variables = (*parameters, *kernel_variables)

    parsed_rows: list&#91;list&#91;sp.Poly&#93;&#93; = &#91;&#93;
    for scale, row in zip(ROW_DENOMINATOR_LCMS, entries):
        parsed_rows.append(
            &#91;
                parse_integral_polynomial(entry, scale, parameters, local_symbols)
                for entry in row
            &#93;
        )

    equations: list&#91;str&#93; = &#91;&#93;
    for row in parsed_rows:
        expression = sum(
            polynomial.as_expr() * coordinate
            for polynomial, coordinate in zip(row, kernel_coordinates)
        )
        reduced = sp.Poly(expression, *all_chart_variables, modulus=characteristic)
        equations.append(render_polynomial(reduced, characteristic))

    determinant_poly = sp.Poly(
        sp.sympify(determinant, locals=local_symbols),
        *parameters,
        modulus=characteristic,
    )
    determinant_text = render_polynomial(determinant_poly, characteristic)

    variables = &#91;str(variable) for variable in (*all_chart_variables, z)&#93;
    tag = f"KERNEL_CHART_{args.chart}_CHAR_{characteristic}"
    equation_block = ",\n  ".join(equations)

    lines = &#91;
        "-- Generated from the hash-checked public Lane 7 source packet.",
        "-- This is an affine chart of the projective kernel incidence.",
        "-- Rational coefficients were cleared by row units and reduced mod p.",
        f"R = ZZ/{characteristic}&#91;{','.join(variables)}, MonomialOrder =&gt; GRevLex&#93;;",
        f"d = {determinant_text};",
        "kernelEquations = {\n  " + equation_block + "\n};",
        "assert(#kernelEquations == 10);",
        "localizerEquation = z*d - 1;",
        "I = ideal kernelEquations + ideal(localizerEquation);",
        f'print "{tag}_BEGIN";',
        "G = gb I;",
        "unitI = (I == 1);",
        f'print("{tag}_UNIT=" | toString unitI);',
        "if unitI then (",
        f'  print "{tag}_DIM=EMPTY";',
        ") else (",
        "  dimI = dim I;",
        "  codimI = codim I;",
        f'  print("{tag}_DIM=" | toString dimI);',
        f'  print("{tag}_CODIM=" | toString codimI);',
        "  assert(dimI &lt;= 1);",
        "  assert(codimI &gt;= 11);",
        ");",
        f'print "{tag}_END";',
    &#93;
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"wrote chart {args.chart} over F_{characteristic} to {args.output}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, sp.SympifyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
</code></pre>

<a id="source-03cf56b8bd9c6caf"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_macaulay2.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Generate one exact or prime-field Lane 7 kernel chart for Macaulay2.

The retained packet already has an exact-Q Singular generator, but the pinned
project toolchain contains Macaulay2 rather than the Singular command-line
driver.  This independent renderer uses the same hash-pinned matrix and row
units while emitting a self-contained Macaulay2 dimension calculation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp

from generate_kernel_chart_input import parse_integral_polynomial, render_polynomial
from generate_kernel_chart_singular import render_integer_polynomial
from generate_macaulay2_input import ROW_DENOMINATOR_LCMS


def render_chart(
    entries: list&#91;list&#91;str&#93;&#93;,
    determinant: str,
    chart: int,
    characteristic: int,
) -&gt; str:
    """Return a complete Macaulay2 program for one affine kernel chart."""
    if chart not in range(5):
        raise ValueError("chart must be between zero and four")
    if characteristic &lt; 0 or (
        characteristic != 0 and not sp.isprime(characteristic)
    ):
        raise ValueError("characteristic must be zero or prime")
    if characteristic and any(
        scale % characteristic == 0 for scale in ROW_DENOMINATOR_LCMS
    ):
        raise ValueError("chosen characteristic kills a denominator-clearing row unit")
    if len(entries) != 10 or any(len(row) != 5 for row in entries):
        raise ValueError("expected a 10 by 5 residual matrix")

    parameters = sp.symbols("a0:7")
    kernel_variables = sp.symbols("x0:4")
    z = sp.Symbol("z")
    local_symbols = {str(variable): variable for variable in parameters}
    free_coordinates = iter(kernel_variables)
    kernel_coordinates: list&#91;sp.Expr&#93; = &#91;
        sp.Integer(1) if index == chart else next(free_coordinates)
        for index in range(5)
    &#93;
    all_chart_variables = (*parameters, *kernel_variables)

    equations: list&#91;str&#93; = &#91;&#93;
    for scale, row in zip(ROW_DENOMINATOR_LCMS, entries):
        parsed = &#91;
            parse_integral_polynomial(entry, scale, parameters, local_symbols)
            for entry in row
        &#93;
        expression = sum(
            polynomial.as_expr() * coordinate
            for polynomial, coordinate in zip(parsed, kernel_coordinates)
        )
        if characteristic:
            polynomial = sp.Poly(
                expression, *all_chart_variables, modulus=characteristic
            )
            equations.append(render_polynomial(polynomial, characteristic))
        else:
            polynomial = sp.Poly(expression, *all_chart_variables, domain=sp.ZZ)
            equations.append(render_integer_polynomial(polynomial))

    determinant_expression = sp.sympify(determinant, locals=local_symbols)
    if characteristic:
        determinant_poly = sp.Poly(
            determinant_expression, *parameters, modulus=characteristic
        )
        determinant_text = render_polynomial(determinant_poly, characteristic)
        coefficient_ring = f"ZZ/{characteristic}"
        field_tag = f"CHAR_{characteristic}"
    else:
        determinant_poly = sp.Poly(
            determinant_expression, *parameters, domain=sp.QQ
        )
        if any(coefficient.q != 1 for coefficient in determinant_poly.coeffs()):
            raise ValueError("determinant has an uncleared rational coefficient")
        determinant_text = render_integer_polynomial(
            sp.Poly(determinant_poly.as_expr(), *parameters, domain=sp.ZZ)
        )
        coefficient_ring = "QQ"
        field_tag = "QQ"

    variables = &#91;str(variable) for variable in (*all_chart_variables, z)&#93;
    tag = f"KERNEL_CHART_{chart}_{field_tag}_MACAULAY2"
    equation_block = ",\n  ".join(&#91;*equations, "z*d-1"&#93;)
    lines = &#91;
        "-- Generated from the hash-pinned Lane 7 source packet.",
        "-- The ten matrix rows were multiplied by nonzero integer row units.",
        f"R = {coefficient_ring}&#91;{','.join(variables)}, MonomialOrder =&gt; GRevLex&#93;;",
        f"d = {determinant_text};",
        "I = ideal(\n  " + equation_block + "\n);",
        "assert(numgens I == 11);",
        f'print "{tag}_BEGIN";',
        "G = gb I;",
        "unitI = (I == 1);",
        f'print("{tag}_UNIT=" | toString unitI);',
        "if unitI then (",
        f'  print "{tag}_DIM=EMPTY";',
        f'  print "{tag}_CODIM=EMPTY";',
        ") else (",
        "  dimI = dim I;",
        "  codimI = codim I;",
        f'  print("{tag}_DIM=" | toString dimI);',
        f'  print("{tag}_CODIM=" | toString codimI);',
        ");",
        "GB = gens G;",
        "gbSize = numgens source GB;",
        f'print("{tag}_GB_SIZE=" | toString gbSize);',
        f'print "{tag}_END";',
    &#93;
    return "\n\n".join(lines) + "\n"


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--chart", type=int, required=True, choices=range(5))
    parser.add_argument(
        "--characteristic",
        type=int,
        required=True,
        help="0 for QQ; otherwise a good prime",
    )
    args = parser.parse_args()

    residual = json.loads(
        (args.source_directory / "collision_residual_matrix_M.json").read_text(
            encoding="utf-8"
        )
    )
    factorization = json.loads(
        (args.source_directory / "Hv10_split_matrix_factorization.json").read_text(
            encoding="utf-8"
        )
    )
    entries = residual.get("entries")
    determinant = factorization.get("d")
    if not isinstance(entries, list):
        raise ValueError("residual artifact has no entries array")
    if not isinstance(determinant, str):
        raise ValueError("factorization artifact does not contain determinant d")

    program = render_chart(entries, determinant, args.chart, args.characteristic)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(program, encoding="utf-8")
    field_name = "QQ" if args.characteristic == 0 else f"F_{args.characteristic}"
    print(f"wrote Macaulay2 chart {args.chart} over {field_name} to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, sp.SympifyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
</code></pre>

<a id="source-8b6128de9797b077"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/generate_kernel_chart_singular.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Generate one Singular computation for a Lane 7 projective-kernel chart."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import sympy as sp

from generate_kernel_chart_input import parse_integral_polynomial, render_polynomial
from generate_macaulay2_input import ROW_DENOMINATOR_LCMS


def render_integer_polynomial(poly: sp.Poly) -&gt; str:
    """Render an integral polynomial without rational-expression overhead."""
    rendered: list&#91;str&#93; = &#91;&#93;
    variables = poly.gens
    for exponents, coefficient in poly.terms():
        value = int(coefficient)
        if value == 0:
            continue
        factors: list&#91;str&#93; = &#91;&#93;
        for variable, exponent in zip(variables, exponents):
            if exponent == 1:
                factors.append(str(variable))
            elif exponent &gt; 1:
                factors.append(f"{variable}^{exponent}")
        monomial = "*".join(factors)
        if not monomial:
            term = str(value)
        elif value == 1:
            term = monomial
        elif value == -1:
            term = f"-{monomial}"
        else:
            term = f"{value}*{monomial}"
        rendered.append(term)
    if not rendered:
        return "0"
    return " + ".join(rendered).replace("+ -", "- ")


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--chart", type=int, required=True, choices=range(5))
    parser.add_argument(
        "--characteristic",
        type=int,
        required=True,
        help="0 for QQ; otherwise a prime not killing a row multiplier",
    )
    args = parser.parse_args()

    characteristic = args.characteristic
    if characteristic &lt; 0 or (characteristic != 0 and not sp.isprime(characteristic)):
        raise ValueError("characteristic must be zero or prime")
    if characteristic and any(
        scale % characteristic == 0 for scale in ROW_DENOMINATOR_LCMS
    ):
        raise ValueError("chosen characteristic kills a denominator-clearing row unit")

    residual = json.loads(
        (args.source_directory / "collision_residual_matrix_M.json").read_text(
            encoding="utf-8"
        )
    )
    factorization = json.loads(
        (args.source_directory / "Hv10_split_matrix_factorization.json").read_text(
            encoding="utf-8"
        )
    )
    entries = residual.get("entries")
    determinant = factorization.get("d")
    if not isinstance(entries, list) or len(entries) != 10:
        raise ValueError("expected a 10 by 5 residual matrix")
    if any(not isinstance(row, list) or len(row) != 5 for row in entries):
        raise ValueError("expected a 10 by 5 residual matrix")
    if not isinstance(determinant, str):
        raise ValueError("factorization artifact does not contain determinant d")

    parameters = sp.symbols("a0:7")
    kernel_variables = sp.symbols("x0:4")
    z = sp.Symbol("z")
    local_symbols = {str(variable): variable for variable in parameters}
    free_coordinates = iter(kernel_variables)
    kernel_coordinates: list&#91;sp.Expr&#93; = &#91;
        sp.Integer(1) if index == args.chart else next(free_coordinates)
        for index in range(5)
    &#93;
    all_chart_variables = (*parameters, *kernel_variables)

    equations: list&#91;str&#93; = &#91;&#93;
    for scale, row in zip(ROW_DENOMINATOR_LCMS, entries):
        parsed = &#91;
            parse_integral_polynomial(entry, scale, parameters, local_symbols)
            for entry in row
        &#93;
        expression = sum(
            polynomial.as_expr() * coordinate
            for polynomial, coordinate in zip(parsed, kernel_coordinates)
        )
        if characteristic:
            polynomial = sp.Poly(
                expression, *all_chart_variables, modulus=characteristic
            )
            equations.append(render_polynomial(polynomial, characteristic))
        else:
            polynomial = sp.Poly(expression, *all_chart_variables, domain=sp.ZZ)
            equations.append(render_integer_polynomial(polynomial))

    determinant_expression = sp.sympify(determinant, locals=local_symbols)
    if characteristic:
        determinant_poly = sp.Poly(
            determinant_expression, *parameters, modulus=characteristic
        )
        determinant_text = render_polynomial(determinant_poly, characteristic)
        field_tag = f"CHAR_{characteristic}"
    else:
        determinant_poly = sp.Poly(
            determinant_expression, *parameters, domain=sp.QQ
        )
        if any(coefficient.q != 1 for coefficient in determinant_poly.coeffs()):
            raise ValueError("determinant has an uncleared rational coefficient")
        determinant_poly = sp.Poly(
            determinant_poly.as_expr(), *parameters, domain=sp.ZZ
        )
        determinant_text = render_integer_polynomial(determinant_poly)
        field_tag = "QQ"

    variables = &#91;str(variable) for variable in (*all_chart_variables, z)&#93;
    tag = f"KERNEL_CHART_{args.chart}_{field_tag}_SINGULAR"
    ring_characteristic = characteristic if characteristic else 0

    lines = &#91;
        f"ring R = {ring_characteristic},({','.join(variables)}),dp;",
        f"poly d = {determinant_text};",
        "ideal I =\n  " + ",\n  ".join(&#91;*equations, "z*d-1"&#93;) + ";",
        f'print("{tag}_BEGIN");',
    &#93;
    if characteristic:
        lines.append("ideal J = slimgb(I);")
    else:
        lines.extend(
            &#91;
                'LIB "modstd.lib";',
                "// modStd uses modular images, rational reconstruction, and an exact final test.",
                "ideal J = modStd(I);",
            &#93;
        )
    lines.extend(
        &#91;
            "int dimI = dim(J);",
            "int codimI = nvars(basering)-dimI;",
            f'print("{tag}_DIM="+string(dimI));',
            f'print("{tag}_CODIM="+string(codimI));',
            f'print("{tag}_GB_SIZE="+string(size(J)));',
            f'print("{tag}_END");',
            "exit;",
        &#93;
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    field_name = "QQ" if characteristic == 0 else f"F_{characteristic}"
    print(f"wrote Singular chart {args.chart} over {field_name} to {args.output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError, sp.SympifyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
</code></pre>

<a id="source-279fc259f53bdbf9"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/generate_macaulay2_input.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Generate a standalone Macaulay2 input from the extracted Lane 7 JSON.

The generator translates Python's ``**`` exponent notation to Macaulay2's
``^`` notation.  By default it preserves the rational entries verbatim.  The
optional row scaling multiplies by nonzero rational constants, hence preserves
all determinantal rank loci while producing integral matrix entries that are
usually much faster for exact Groebner-basis calculations.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

_ALLOWED_EXPRESSION = re.compile(r"&#91;A-Za-z0-9_+\-*/^(). &#93;+\Z")

# Least common multiples of all coefficient denominators in the ten rows of
# collision_residual_matrix_M.json from the hash-pinned v19 Lane 7 packet.
# Multiplying rows by these nonzero integers changes every minor only by a unit.
ROW_DENOMINATOR_LCMS = &#91;
    4374,
    8748,
    4374,
    8748,
    486,
    52488,
    104976,
    104976,
    209952,
    314928,
&#93;


def m2_expression(expression: str) -&gt; str:
    converted = expression.replace("**", "^")
    if _ALLOWED_EXPRESSION.fullmatch(converted) is None:
        raise ValueError(f"unsupported character in polynomial expression: {expression!r}")
    return converted


def m2_matrix(rows: list&#91;list&#91;str&#93;&#93;) -&gt; str:
    if not rows or not rows&#91;0&#93;:
        raise ValueError("matrix must be nonempty")
    width = len(rows&#91;0&#93;)
    if any(len(row) != width for row in rows):
        raise ValueError("matrix is ragged")
    rendered_rows = &#91;
        "{" + ", ".join(m2_expression(entry) for entry in row) + "}"
        for row in rows
    &#93;
    return "matrix {\n  " + ",\n  ".join(rendered_rows) + "\n}"


def scaled_rows(entries: list&#91;list&#91;str&#93;&#93;, clear_denominators: bool) -&gt; list&#91;list&#91;str&#93;&#93;:
    if not clear_denominators:
        return entries
    if len(entries) != len(ROW_DENOMINATOR_LCMS):
        raise ValueError("row-denominator table does not match the residual matrix")
    return &#91;
        &#91;f"{scale}*({entry})" for entry in row&#93;
        for scale, row in zip(ROW_DENOMINATOR_LCMS, entries)
    &#93;


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source_directory",
        type=Path,
        help="directory containing the extracted Lane 7 JSON files",
    )
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--characteristic",
        type=int,
        default=0,
        help="0 for QQ; otherwise use ZZ/p",
    )
    parser.add_argument(
        "--with-localizer",
        action="store_true",
        help="adjoin z and define localizerEquation=z*d-1",
    )
    parser.add_argument(
        "--clear-row-denominators",
        action="store_true",
        help="multiply rows by packet-specific denominator LCMs",
    )
    args = parser.parse_args()

    if args.characteristic &lt; 0:
        raise ValueError("characteristic must be nonnegative")

    residual_path = args.source_directory / "collision_residual_matrix_M.json"
    factorization_path = args.source_directory / "Hv10_split_matrix_factorization.json"
    residual = json.loads(residual_path.read_text(encoding="utf-8"))
    factorization = json.loads(factorization_path.read_text(encoding="utf-8"))

    entries = residual.get("entries")
    if not isinstance(entries, list) or len(entries) != 10:
        raise ValueError("expected residual entries to have ten rows")
    if any(not isinstance(row, list) or len(row) != 5 for row in entries):
        raise ValueError("expected residual entries to be a 10 by 5 matrix")

    determinant = factorization.get("d")
    if not isinstance(determinant, str):
        raise ValueError("factorization artifact does not contain determinant d")

    coefficient_ring = "QQ" if args.characteristic == 0 else f"ZZ/{args.characteristic}"
    variables = &#91;f"a{i}" for i in range(7)&#93;
    if args.with_localizer:
        variables.append("z")

    matrix_entries = scaled_rows(entries, args.clear_row_denominators)
    lines = &#91;
        "-- Generated from the hash-checked public Lane 7 source packet.",
        "-- Do not edit this file by hand; edit the generator instead.",
        f"R = {coefficient_ring}&#91;{','.join(variables)}, MonomialOrder =&gt; GRevLex&#93;;",
        f"d = {m2_expression(determinant)};",
        f"M = {m2_matrix(matrix_entries)};",
        "assert(numrows M == 10 and numcols M == 5);",
    &#93;
    if args.clear_row_denominators:
        lines.append("-- M has been row-scaled by nonzero constants; rank loci are unchanged.")
    if args.with_localizer:
        lines.append("localizerEquation = z*d - 1;")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    print(
        f"wrote {args.output} over {coefficient_ring} "
        f"({'with' if args.with_localizer else 'without'} localizer; "
        f"{'cleared' if args.clear_row_denominators else 'verbatim'} rows)"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
</code></pre>

<a id="source-efcfe78f40b44e90"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/prepare_five_chart_runs.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Prepare immutable exact-Q and good-prime Lane 7 Slurm run directories."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import stat

from generate_kernel_chart_macaulay2 import render_chart


ROOT = Path(__file__).resolve().parent


def sha256(path: Path) -&gt; str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_new(path: Path, content: str, executable: bool = False) -&gt; None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        handle.write(content)
    if executable:
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP)


def slurm_program(
    *,
    chart: int,
    field_name: str,
    chart_directory: Path,
    toolchain_launcher: Path,
    cpus: int,
    memory: str,
    walltime: str,
) -&gt; str:
    input_path = chart_directory / "input.m2"
    return f"""#!/usr/bin/env bash
#SBATCH --job-name=l7-{field_name}-c{chart}
#SBATCH --partition=research
#SBATCH --cpus-per-task={cpus}
#SBATCH --mem={memory}
#SBATCH --time={walltime}
#SBATCH --chdir={chart_directory}
#SBATCH --output={chart_directory}/slurm-%j.stdout.txt
#SBATCH --error={chart_directory}/slurm-%j.stderr.txt

set -euo pipefail
cd {chart_directory}
date --utc --iso-8601=seconds
sha256sum {input_path}
{toolchain_launcher} --version
/usr/bin/time -v -o resource-usage.txt {toolchain_launcher} --script {input_path}
date --utc --iso-8601=seconds
"""


def main() -&gt; int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("run_root", type=Path)
    parser.add_argument("toolchain_launcher", type=Path)
    parser.add_argument("toolchain_image", type=Path)
    parser.add_argument("--prime", type=int, default=1009)
    parser.add_argument("--repository-commit", required=True)
    args = parser.parse_args()

    if args.run_root.exists():
        raise FileExistsError(f"refusing to overwrite existing run root: {args.run_root}")
    for path in (
        args.source_directory,
        args.toolchain_launcher,
        args.toolchain_image,
    ):
        if not path.exists():
            raise FileNotFoundError(path)
    if len(args.repository_commit) != 40:
        raise ValueError("repository commit must be a full 40-hex identifier")

    residual_path = args.source_directory / "collision_residual_matrix_M.json"
    factorization_path = (
        args.source_directory / "Hv10_split_matrix_factorization.json"
    )
    toolchain_root = args.toolchain_launcher.parent.parent
    dependency_paths = &#91;
        toolchain_root / name
        for name in (
            "PACKAGE_SHA256SUMS",
            "PACKAGE_VERSIONS.tsv",
            "TOOLCHAIN_SHA256SUMS",
        )
    &#93;
    for path in dependency_paths:
        if not path.is_file():
            raise FileNotFoundError(path)
    residual = json.loads(residual_path.read_text(encoding="utf-8"))
    factorization = json.loads(factorization_path.read_text(encoding="utf-8"))
    entries = residual&#91;"entries"&#93;
    determinant = factorization&#91;"d"&#93;

    args.run_root.mkdir(parents=True, exist_ok=False)
    jobs: list&#91;dict&#91;str, object&#93;&#93; = &#91;&#93;
    profiles = (
        ("exact-q", 0, 4, "48G", "12:00:00"),
        (f"prime-{args.prime}", args.prime, 1, "12G", "02:00:00"),
    )
    for field_name, characteristic, cpus, memory, walltime in profiles:
        for chart in range(5):
            chart_directory = args.run_root / field_name / f"chart-{chart}"
            chart_directory.mkdir(parents=True, exist_ok=False)
            input_path = chart_directory / "input.m2"
            sbatch_path = chart_directory / "run.sbatch"
            write_new(
                input_path,
                render_chart(entries, determinant, chart, characteristic),
            )
            write_new(
                sbatch_path,
                slurm_program(
                    chart=chart,
                    field_name=field_name,
                    chart_directory=chart_directory,
                    toolchain_launcher=args.toolchain_launcher,
                    cpus=cpus,
                    memory=memory,
                    walltime=walltime,
                ),
                executable=True,
            )
            jobs.append(
                {
                    "field": "Q" if characteristic == 0 else f"F_{characteristic}",
                    "chart": chart,
                    "characteristic": characteristic,
                    "resources": {
                        "partition": "research",
                        "cpus": cpus,
                        "memory": memory,
                        "walltime": walltime,
                    },
                    "input": str(input_path),
                    "input_sha256": sha256(input_path),
                    "sbatch": str(sbatch_path),
                    "sbatch_sha256": sha256(sbatch_path),
                    "submit_command": f"sbatch {sbatch_path}",
                    "does_not_establish": (
                        "A finite-field result is a discovery cross-check only."
                        if characteristic
                        else "A chart dimension does not prove global component purity, "
                        "the Pluecker-open condition, or a first-normal obstruction."
                    ),
                }
            )

    manifest = {
        "schema_version": 1,
        "repository_commit": args.repository_commit,
        "generator": str(ROOT / "generate_kernel_chart_macaulay2.py"),
        "generator_sha256": sha256(ROOT / "generate_kernel_chart_macaulay2.py"),
        "source_files": &#91;
            {"path": str(residual_path), "sha256": sha256(residual_path)},
            {"path": str(factorization_path), "sha256": sha256(factorization_path)},
        &#93;,
        "toolchain": {
            "launcher": str(args.toolchain_launcher),
            "launcher_sha256": sha256(args.toolchain_launcher),
            "image": str(args.toolchain_image),
            "image_sha256": sha256(args.toolchain_image),
            "dependency_manifests": &#91;
                {"path": str(path), "sha256": sha256(path)}
                for path in dependency_paths
            &#93;,
        },
        "prime": args.prime,
        "jobs": jobs,
        "global_does_not_establish": &#91;
            "I_4(M):d^infinity=(1)",
            "grade or purity of I_5(M):d^infinity",
            "characteristic-zero component decomposition",
            "generic nonvanishing of a Pluecker coordinate on each component",
            "componentwise first-normal obstruction",
        &#93;,
    }
    manifest_path = args.run_root / "manifest.json"
    write_new(manifest_path, json.dumps(manifest, indent=2) + "\n")
    write_new(
        args.run_root / "SUBMIT_COMMANDS.txt",
        "\n".join(str(job&#91;"submit_command"&#93;) for job in jobs) + "\n",
    )
    print(f"prepared {len(jobs)} immutable job directories at {args.run_root}")
    print(f"manifest_sha256={sha256(manifest_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-ac8b7aff9c24d854"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/test_kernel_chart_macaulay2.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Regression tests for the exact/prime Macaulay2 chart renderer."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

from generate_kernel_chart_macaulay2 import render_chart
from generate_macaulay2_input import ROW_DENOMINATOR_LCMS


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "lane7-split-incidence-20260802-v1"


def main() -&gt; int:
    residual = json.loads(
        (SOURCE / "collision_residual_matrix_M.json").read_text(encoding="utf-8")
    )
    factorization = json.loads(
        (SOURCE / "Hv10_split_matrix_factorization.json").read_text(encoding="utf-8")
    )
    entries = residual&#91;"entries"&#93;
    determinant = factorization&#91;"d"&#93;

    assert sp.isprime(1009)
    assert all(scale % 1009 for scale in ROW_DENOMINATOR_LCMS)
    for chart in range(5):
        exact = render_chart(entries, determinant, chart, 0)
        prime = render_chart(entries, determinant, chart, 1009)
        assert f"KERNEL_CHART_{chart}_QQ_MACAULAY2_BEGIN" in exact
        assert f"KERNEL_CHART_{chart}_CHAR_1009_MACAULAY2_BEGIN" in prime
        assert "R = QQ&#91;" in exact
        assert "R = ZZ/1009&#91;" in prime
        assert exact.count("z*d-1") == 1
        assert prime.count("z*d-1") == 1
        assert "assert(numgens I == 11);" in exact
        assert "assert(numgens I == 11);" in prime
        assert "_GB_SIZE=" in exact
        assert "_GB_SIZE=" in prime

    for bad_characteristic in (2, 3, 6):
        try:
            render_chart(entries, determinant, 0, bad_characteristic)
        except ValueError:
            pass
        else:
            raise AssertionError(f"accepted bad characteristic {bad_characteristic}")

    print("verified five exact-Q and five F_1009 Macaulay2 chart renderings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-e0ebcaa6e425b78d"></a>

## `research-notes/lane7-projective-kernel-20260803-v1/test_plucker_transport.py`

<pre><code class="language-python">
#!/usr/bin/env python3
"""Exact symbolic checks for the Lane 7 Pluecker marking transport."""

from __future__ import annotations

import itertools

import sympy as sp

u = sp.symbols("u0:5")
v = sp.symbols("v0:5")
d = sp.symbols("d", nonzero=True)
b = sp.symbols("b0:25")
B = sp.Matrix(5, 5, b)


def eta(i: int, j: int, second: tuple&#91;sp.Expr, ...&#93; | list&#91;sp.Expr&#93; = v) -&gt; sp.Expr:
    return sp.expand(u&#91;i&#93; * second&#91;j&#93; - u&#91;j&#93; * second&#91;i&#93;)


def main() -&gt; int:
    # The five quadratic equations for Gr(2,5).
    for i, j, k, ell in itertools.combinations(range(5), 4):
        relation = (
            eta(i, j) * eta(k, ell)
            - eta(i, k) * eta(j, ell)
            + eta(i, ell) * eta(j, k)
        )
        assert sp.expand(relation) == 0

    # Every independent pair lies in one of these ten normalized charts.
    for i, j in itertools.combinations(range(5), 2):
        denominator = eta(i, j)
        p = &#91;sp.cancel(eta(r, j) / denominator) for r in range(5)&#93;
        q = &#91;sp.cancel(eta(i, r) / denominator) for r in range(5)&#93;
        assert sp.cancel(p&#91;i&#93; - 1) == 0
        assert sp.cancel(p&#91;j&#93;) == 0
        assert sp.cancel(q&#91;i&#93;) == 0
        assert sp.cancel(q&#91;j&#93; - 1) == 0

        expected_p = &#91;
            sp.cancel((v&#91;j&#93; * u&#91;r&#93; - u&#91;j&#93; * v&#91;r&#93;) / denominator)
            for r in range(5)
        &#93;
        expected_q = &#91;
            sp.cancel((-v&#91;i&#93; * u&#91;r&#93; + u&#91;i&#93; * v&#91;r&#93;) / denominator)
            for r in range(5)
        &#93;
        assert all(sp.cancel(x - y) == 0 for x, y in zip(p, expected_p))
        assert all(sp.cancel(x - y) == 0 for x, y in zip(q, expected_q))

    # On D(d), Theorem C reconstructs v=-d^{-1}Bu. Thus
    # d*eta_ij=-(u_i(Bu)_j-u_j(Bu)_i) for every Pluecker coordinate.
    Bu = B * sp.Matrix(u)
    reconstructed_v = tuple(sp.cancel(-entry / d) for entry in Bu)
    for i, j in itertools.combinations(range(5), 2):
        phi = sp.expand(u&#91;i&#93; * Bu&#91;j&#93; - u&#91;j&#93; * Bu&#91;i&#93;)
        transported = sp.cancel(d * eta(i, j, reconstructed_v) + phi)
        assert transported == 0

    # The formerly normalized affine open is precisely eta_34 on v4=1.
    assert sp.expand(eta(3, 4).subs(v&#91;4&#93;, 1) - (u&#91;3&#93; - u&#91;4&#93; * v&#91;3&#93;)) == 0

    print(
        "verified 5 Pluecker relations, all 10 normalized charts, "
        "and d*eta_ij=-Phi_ij for the projective-kernel reconstruction"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
</code></pre>

<a id="source-1ebb898687fd03df"></a>

## `research-notes/lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json`

<pre><code class="language-json">
{
  "ring": "Q&#91;a0,...,a6&#93;",
  "d": "36*a0*a2*a3*a5 - 12*a0*a2*a4**2 + 108*a0*a3*a6**2 - 54*a0*a3*a6 + 6*a0*a3 - 24*a0*a4*a5*a6 + 6*a0*a4*a5 + 4*a0*a5**3 - 36*a1**2*a3*a5 + 12*a1**2*a4**2 - 216*a1*a2*a3*a6 + 54*a1*a2*a3 + 24*a1*a2*a4*a5 - 72*a1*a4*a6**2 + 36*a1*a4*a6 - 6*a1*a4 + 24*a1*a5**2*a6 - 6*a1*a5**2 + 108*a2**3*a3 + 72*a2**2*a4*a6 - 18*a2**2*a4 + 12*a2**2*a5**2 + 108*a2*a5*a6**2 - 54*a2*a5*a6 + 3*a2*a5 + 108*a6**4 - 108*a6**3 + 33*a6**2 - 3*a6",
  "H_shape": &#91;
    10,
    5
  &#93;,
  "C_shape": &#91;
    5,
    10
  &#93;,
  "Q_shape": &#91;
    5,
    10
  &#93;,
  "R_shape": &#91;
    10,
    5
  &#93;,
  "H": &#91;
    &#91;
      "-2*a1*a3/3 - 2*a2*a4/9 - a5/9",
      "2*a1*a5/27 + 2*a2*a6/9 - 5*a2/27",
      "2*a1*a4/9 + 2*a2*a5/9 + a6/3 - 1/18",
      "-2*a1*a6/9 - a1/9 + 2*a2**2/9",
      "-2*a0/9"
    &#93;,
    &#91;
      "-2*a2*a3/3 - 2*a4*a6/9 + a4/9",
      "2*a2*a5/27 + 2*a6**2/9 - 5*a6/27 + 1/27",
      "2*a2*a4/9 + 2*a5*a6/9 - a5/9",
      "-a2/9",
      "2*a1*a6/9 - 2*a1/9 - 2*a2**2/9"
    &#93;,
    &#91;
      "2*a3*a6 - a3/3 - 2*a4*a5/9",
      "-a5/27",
      "-2*a4*a6/3 + a4/9 + 2*a5**2/9",
      "2*a2*a5/9 + 2*a6**2/3 - a6/9",
      "2*a1*a5/9 + 2*a2*a6/3 + 2*a2/9"
    &#93;,
    &#91;
      "2*a3*a5/3 - 2*a4**2/9",
      "2*a4*a6/9 - 2*a4/27 - 2*a5**2/27",
      "0",
      "2*a2*a4/9 + 2*a5*a6/9",
      "2*a1*a4/9 + 2*a2*a5/9 - a6/3 + 1/9"
    &#93;,
    &#91;
      "0",
      "2*a3*a6/3 - 2*a3/9 - 2*a4*a5/27",
      "2*a3*a5/3 - 2*a4**2/9",
      "2*a2*a3/3 + 2*a4*a6/9",
      "2*a1*a3/3 + 2*a2*a4/9 - a5/9"
    &#93;,
    &#91;
      "-a0*a3/3 + a2*a5/9 - 1/18",
      "a0*a5/27 + a1/27 + a2**2/9",
      "a0*a4/9 - a2*a6/3",
      "-a0*a6/9 + a0/18 + a1*a2/9",
      "0"
    &#93;,
    &#91;
      "-a1*a3/3 + a5*a6/9",
      "a1*a5/27 + a2*a6/9 + a2/27",
      "a1*a4/9 - a6**2/3 + 1/36",
      "a1/18",
      "a0*a6/9 - a1*a2/9"
    &#93;,
    &#91;
      "-a2*a3 - a4/9 - a5**2/9",
      "2*a6/9 - 1/18",
      "a2*a4/3 + a5*a6/3 + a5/9",
      "-a1*a5/9 - a2*a6/3 + 5*a2/18",
      "-a0*a5/9 + a1/9 - a2**2/3"
    &#93;,
    &#91;
      "-a3*a6 + a3/2 + a4*a5/9",
      "a2*a4/9 + a5*a6/9 - 5*a5/54",
      "-a4/6",
      "a1*a4/9 - a6**2/3 + a6/3 - 1/18",
      "a0*a4/9 - a2*a6/3 + a2/6"
    &#93;,
    &#91;
      "0",
      "a2*a3/3 - a4/27 + a5**2/27",
      "-a3*a6 + a4*a5/9",
      "a1*a3/3 - a5*a6/9 + a5/18",
      "a0*a3/3 - a2*a5/9 + 1/18"
    &#93;
  &#93;,
  "C": &#91;
    &#91;
      "-324*a0*a1*a3*a5 + 108*a0*a1*a4**2 - 972*a0*a2*a3*a6 + 162*a0*a2*a3 + 108*a0*a2*a4*a5 - 324*a0*a4*a6**2 + 54*a0*a4*a6 + 108*a0*a5**2*a6 - 972*a1**2*a3*a6 + 324*a1**2*a3 + 108*a1**2*a4*a5 + 972*a1*a2**2*a3 + 108*a1*a2*a4 + 216*a1*a2*a5**2 + 324*a1*a5*a6**2 - 108*a1*a5*a6 + 324*a2**3*a4 + 648*a2**2*a5*a6 - 54*a2**2*a5 + 972*a2*a6**3 - 486*a2*a6**2 + 54*a2*a6",
      "324*a0**2*a3*a5 - 108*a0**2*a4**2 + 1944*a0*a1*a3*a6 - 648*a0*a1*a3 - 216*a0*a1*a4*a5 + 648*a0*a2*a4*a6 - 270*a0*a2*a4 - 216*a0*a2*a5**2 - 54*a0*a5*a6 - 972*a1**2*a2*a3 - 108*a1**2*a4 - 108*a1**2*a5**2 - 648*a1*a2**2*a4 - 648*a1*a2*a5*a6 - 108*a1*a2*a5 - 324*a1*a6**2 + 108*a1*a6 - 324*a2**3*a5 - 972*a2**2*a6**2 + 324*a2**2*a6",
      "-54*a0**2*a3 + 324*a0*a1*a2*a3 + 108*a0*a1*a4*a6 - 90*a0*a1*a4 + 108*a0*a2**2*a4 + 108*a0*a2*a5*a6 - 72*a0*a2*a5 - 54*a0*a6**2 + 27*a0*a6 - 324*a1**3*a3 - 216*a1**2*a2*a4 + 108*a1**2*a5*a6 - 54*a1**2*a5 - 216*a1*a2**2*a5 + 324*a1*a2*a6**2 - 108*a1*a2*a6 - 324*a2**3*a6",
      "324*a0**2*a2*a3 + 108*a0**2*a4*a6 - 18*a0**2*a4 - 324*a0*a1**2*a3 - 108*a0*a1*a2*a4 + 108*a0*a1*a5*a6 + 18*a0*a1*a5 - 216*a0*a2**2*a5 - 324*a0*a2*a6**2 + 216*a0*a2*a6 - 45*a0*a2 + 108*a1**2*a2*a5 + 216*a1**2*a6 - 54*a1**2 + 648*a1*a2**2*a6 - 324*a1*a2**2 - 324*a2**4",
      "-108*a0**2*a2*a4 - 108*a0**2*a5*a6 + 36*a0**2*a5 + 108*a0*a1**2*a4 - 648*a0*a1*a6**2 + 432*a0*a1*a6 - 72*a0*a1 + 324*a0*a2**2*a6 - 162*a0*a2**2 + 108*a1**3*a5 + 648*a1**2*a2*a6 - 162*a1**2*a2 - 324*a1*a2**3",
      "-648*a0*a2*a3*a5 + 216*a0*a2*a4**2 - 1944*a0*a3*a6**2 + 972*a0*a3*a6 - 108*a0*a3 + 432*a0*a4*a5*a6 - 108*a0*a4*a5 - 72*a0*a5**3 + 648*a1**2*a3*a5 - 216*a1**2*a4**2 + 3888*a1*a2*a3*a6 - 972*a1*a2*a3 - 432*a1*a2*a4*a5 + 1296*a1*a4*a6**2 - 648*a1*a4*a6 + 108*a1*a4 - 432*a1*a5**2*a6 + 108*a1*a5**2 - 1944*a2**3*a3 - 1296*a2**2*a4*a6 + 324*a2**2*a4 - 216*a2**2*a5**2 - 1944*a2*a5*a6**2 + 972*a2*a5*a6 - 54*a2*a5 - 1944*a6**4 + 1944*a6**3 - 594*a6**2 + 54*a6",
      "-648*a0*a1*a3*a5 + 216*a0*a1*a4**2 - 1944*a0*a2*a3*a6 + 324*a0*a2*a3 + 216*a0*a2*a4*a5 - 648*a0*a4*a6**2 + 108*a0*a4*a6 + 216*a0*a5**2*a6 - 1944*a1**2*a3*a6 + 648*a1**2*a3 + 216*a1**2*a4*a5 + 1944*a1*a2**2*a3 + 216*a1*a2*a4 + 432*a1*a2*a5**2 + 648*a1*a5*a6**2 - 216*a1*a5*a6 + 648*a2**3*a4 + 1296*a2**2*a5*a6 - 108*a2**2*a5 + 1944*a2*a6**3 - 972*a2*a6**2 + 108*a2*a6",
      "216*a0**2*a3*a5 - 72*a0**2*a4**2 + 648*a0*a1*a3*a6 - 216*a0*a1*a3 - 72*a0*a1*a4*a5 + 648*a0*a2**2*a3 + 648*a0*a2*a4*a6 - 180*a0*a2*a4 - 72*a0*a2*a5**2 + 216*a0*a5*a6**2 - 108*a0*a5*a6 - 648*a1**2*a2*a3 - 216*a1**2*a4*a6 - 216*a1*a2**2*a4 - 108*a1*a2*a5 + 648*a1*a6**3 - 540*a1*a6**2 + 108*a1*a6 - 216*a2**3*a5 - 648*a2**2*a6**2 + 216*a2**2*a6",
      "648*a0**2*a3*a6 - 108*a0**2*a3 - 72*a0**2*a4*a5 - 1296*a0*a1*a2*a3 - 216*a0*a1*a4*a6 + 108*a0*a1*a4 - 72*a0*a1*a5**2 - 216*a0*a2**2*a4 + 36*a0*a2*a5 + 648*a0*a6**3 - 432*a0*a6**2 + 54*a0*a6 + 648*a1**3*a3 + 216*a1**2*a2*a4 - 432*a1**2*a5*a6 + 108*a1**2*a5 + 216*a1*a2**2*a5 - 1296*a1*a2*a6**2 + 432*a1*a2*a6 + 648*a2**3*a6",
      "-216*a0**2*a4*a6 + 36*a0**2*a4 + 72*a0**2*a5**2 + 432*a0*a1*a2*a4 + 432*a0*a1*a5*a6 - 180*a0*a1*a5 + 432*a0*a2**2*a5 + 1296*a0*a2*a6**2 - 756*a0*a2*a6 + 90*a0*a2 - 216*a1**3*a4 - 432*a1**2*a2*a5 + 648*a1**2*a6**2 - 540*a1**2*a6 + 108*a1**2 - 1944*a1*a2**2*a6 + 648*a1*a2**2 + 648*a2**4"
    &#93;,
    &#91;
      "-1458*a1*a3*a6 + 486*a1*a3 + 162*a1*a4*a5 + 1458*a2**2*a3 + 486*a2*a4*a6 + 162*a2*a5**2 + 486*a5*a6**2 - 162*a5*a6",
      "1458*a0*a3*a6 - 486*a0*a3 - 162*a0*a4*a5 - 1458*a1*a2*a3 - 162*a1*a4 - 162*a1*a5**2 - 486*a2**2*a4 - 486*a2*a5*a6 - 162*a2*a5 - 486*a6**2 + 162*a6",
      "486*a0*a2*a3 + 162*a0*a4*a6 - 54*a0*a4 - 486*a1**2*a3 - 162*a1*a2*a4 + 162*a1*a5*a6 - 81*a1*a5 - 162*a2**2*a5 - 81*a2*a6",
      "27*a0*a5 + 324*a1*a6 - 81*a1 - 243*a2**2",
      "-162*a0*a2*a5 - 486*a0*a6**2 + 243*a0*a6 - 27*a0 + 162*a1**2*a5 + 972*a1*a2*a6 - 243*a1*a2 - 486*a2**3",
      "0",
      "-2916*a1*a3*a6 + 972*a1*a3 + 324*a1*a4*a5 + 2916*a2**2*a3 + 972*a2*a4*a6 + 324*a2*a5**2 + 972*a5*a6**2 - 324*a5*a6",
      "972*a0*a3*a6 - 324*a0*a3 - 108*a0*a4*a5 - 972*a1*a2*a3 - 324*a1*a4*a6 + 324*a2*a5*a6 - 162*a2*a5 + 972*a6**3 - 810*a6**2 + 162*a6",
      "-972*a0*a2*a3 - 108*a0*a5**2 + 972*a1**2*a3 - 648*a1*a5*a6 + 162*a1*a5 - 972*a2*a6**2 + 486*a2*a6",
      "324*a0*a2*a4 + 324*a0*a5*a6 - 108*a0*a5 - 324*a1**2*a4 - 324*a1*a2*a5 + 972*a1*a6**2 - 810*a1*a6 + 162*a1 - 972*a2**2*a6 + 486*a2**2"
    &#93;,
    &#91;
      "-648*a0*a2*a3*a5 + 216*a0*a2*a4**2 - 1944*a0*a3*a6**2 + 972*a0*a3*a6 - 108*a0*a3 + 432*a0*a4*a5*a6 - 108*a0*a4*a5 - 72*a0*a5**3 + 648*a1**2*a3*a5 - 216*a1**2*a4**2 + 3888*a1*a2*a3*a6 - 972*a1*a2*a3 - 432*a1*a2*a4*a5 + 1296*a1*a4*a6**2 - 324*a1*a4*a6 - 432*a1*a5**2*a6 - 1944*a2**3*a3 - 1296*a2**2*a4*a6 - 216*a2**2*a5**2 - 1944*a2*a5*a6**2 + 324*a2*a5*a6 - 1944*a6**4 + 972*a6**3 - 108*a6**2",
      "-648*a0*a1*a3*a5 + 216*a0*a1*a4**2 - 1944*a0*a2*a3*a6 + 324*a0*a2*a3 + 216*a0*a2*a4*a5 - 648*a0*a4*a6**2 - 216*a0*a4*a6 + 108*a0*a4 + 216*a0*a5**2*a6 + 108*a0*a5**2 - 1944*a1**2*a3*a6 + 648*a1**2*a3 + 216*a1**2*a4*a5 + 1944*a1*a2**2*a3 + 540*a1*a2*a4 + 432*a1*a2*a5**2 + 648*a1*a5*a6**2 + 108*a1*a5*a6 + 648*a2**3*a4 + 1296*a2**2*a5*a6 + 216*a2**2*a5 + 1944*a2*a6**3 - 216*a2*a6",
      "-216*a0**2*a3*a5 + 72*a0**2*a4**2 - 648*a0*a1*a3*a6 + 216*a0*a1*a3 + 72*a0*a1*a4*a5 - 648*a0*a2**2*a3 - 648*a0*a2*a4*a6 + 72*a0*a2*a4 + 72*a0*a2*a5**2 - 216*a0*a5*a6**2 + 18*a0*a5 + 648*a1**2*a2*a3 + 216*a1**2*a4*a6 + 108*a1**2*a4 + 216*a1*a2**2*a4 + 216*a1*a2*a5 - 648*a1*a6**3 + 216*a1*a6**2 - 54*a1*a6 + 216*a2**3*a5 + 648*a2**2*a6**2 + 108*a2**2*a6",
      "648*a0**2*a3*a6 - 108*a0**2*a3 - 72*a0**2*a4*a5 - 1296*a0*a1*a2*a3 - 216*a0*a1*a4*a6 + 108*a0*a1*a4 - 72*a0*a1*a5**2 - 216*a0*a2**2*a4 + 144*a0*a2*a5 + 648*a0*a6**3 - 108*a0*a6**2 - 108*a0*a6 + 18*a0 + 648*a1**3*a3 + 216*a1**2*a2*a4 - 432*a1**2*a5*a6 + 216*a1*a2**2*a5 - 1296*a1*a2*a6**2 - 216*a1*a2*a6 + 162*a1*a2 + 648*a2**3*a6 + 324*a2**3",
      "-216*a0**2*a4*a6 + 36*a0**2*a4 + 72*a0**2*a5**2 + 432*a0*a1*a2*a4 + 432*a0*a1*a5*a6 - 180*a0*a1*a5 + 432*a0*a2**2*a5 + 1296*a0*a2*a6**2 - 756*a0*a2*a6 + 90*a0*a2 - 216*a1**3*a4 - 432*a1**2*a2*a5 + 648*a1**2*a6**2 - 540*a1**2*a6 + 108*a1**2 - 1944*a1*a2**2*a6 + 648*a1*a2**2 + 648*a2**4",
      "0",
      "648*a1*a4*a6 - 216*a1*a4 - 216*a1*a5**2 - 648*a2**2*a4 - 1296*a2*a5*a6 + 108*a2*a5 - 1944*a6**3 + 972*a6**2 - 108*a6",
      "-216*a0*a4*a6 + 72*a0*a4 + 72*a0*a5**2 + 216*a1*a2*a4 + 216*a1*a5*a6 + 216*a2**2*a5 + 648*a2*a6**2 - 216*a2*a6",
      "216*a0*a2*a4 + 216*a0*a5*a6 - 36*a0*a5 - 216*a1**2*a4 - 216*a1*a2*a5 + 648*a1*a6**2 - 108*a1*a6 - 648*a2**2*a6",
      "-216*a0*a2*a5 - 648*a0*a6**2 + 324*a0*a6 - 36*a0 + 216*a1**2*a5 + 1296*a1*a2*a6 - 324*a1*a2 - 648*a2**3"
    &#93;,
    &#91;
      "-324*a1*a3*a5 + 108*a1*a4**2 - 972*a2*a3*a6 + 162*a2*a3 + 108*a2*a4*a5 - 324*a4*a6**2 + 54*a4*a6 + 108*a5**2*a6",
      "324*a0*a3*a5 - 108*a0*a4**2 + 1944*a1*a3*a6 - 648*a1*a3 - 216*a1*a4*a5 - 972*a2**2*a3 - 162*a2*a4 - 216*a2*a5**2 - 324*a5*a6**2 + 54*a5*a6",
      "324*a0*a3*a6 - 162*a0*a3 - 36*a0*a4*a5 - 324*a1*a2*a3 - 108*a1*a4*a6 - 54*a1*a4 + 108*a2*a5*a6 - 108*a2*a5 + 324*a6**3 - 324*a6**2 + 81*a6",
      "648*a0*a2*a3 + 108*a0*a4*a6 - 18*a0*a4 + 36*a0*a5**2 - 648*a1**2*a3 - 108*a1*a2*a4 + 324*a1*a5*a6 - 54*a1*a5 - 108*a2**2*a5 + 324*a2*a6**2 - 108*a2*a6 - 27*a2",
      "-216*a0*a2*a4 - 216*a0*a5*a6 + 72*a0*a5 + 216*a1**2*a4 + 216*a1*a2*a5 - 648*a1*a6**2 + 540*a1*a6 - 108*a1 + 648*a2**2*a6 - 324*a2**2",
      "0",
      "-648*a1*a3*a5 + 216*a1*a4**2 - 1944*a2*a3*a6 + 324*a2*a3 + 216*a2*a4*a5 - 648*a4*a6**2 + 108*a4*a6 + 216*a5**2*a6",
      "216*a0*a3*a5 - 72*a0*a4**2 + 648*a2**2*a3 + 432*a2*a4*a6 - 108*a2*a4 + 216*a5*a6**2 - 108*a5*a6",
      "648*a0*a3*a6 - 108*a0*a3 - 72*a0*a4*a5 - 648*a1*a2*a3 - 216*a1*a4*a6 + 108*a1*a4 + 216*a2*a5*a6 + 648*a6**3 - 432*a6**2 + 54*a6",
      "-216*a0*a4*a6 + 36*a0*a4 + 72*a0*a5**2 + 216*a1*a2*a4 + 216*a1*a5*a6 - 108*a1*a5 + 216*a2**2*a5 + 648*a2*a6**2 - 432*a2*a6 + 54*a2"
    &#93;,
    &#91;
      "0",
      "324*a1*a3*a5 - 108*a1*a4**2 + 972*a2*a3*a6 - 162*a2*a3 - 108*a2*a4*a5 + 324*a4*a6**2 - 54*a4*a6 - 108*a5**2*a6",
      "108*a0*a3*a5 - 36*a0*a4**2 + 324*a2**2*a3 + 216*a2*a4*a6 - 54*a2*a4 + 108*a5*a6**2 - 54*a5*a6",
      "-324*a0*a3*a6 + 54*a0*a3 + 36*a0*a4*a5 + 324*a1*a2*a3 + 108*a1*a4*a6 - 54*a1*a4 - 108*a2*a5*a6 - 324*a6**3 + 216*a6**2 - 27*a6",
      "108*a0*a4*a6 - 18*a0*a4 - 36*a0*a5**2 - 108*a1*a2*a4 - 108*a1*a5*a6 + 54*a1*a5 - 108*a2**2*a5 - 324*a2*a6**2 + 216*a2*a6 - 27*a2",
      "0",
      "0",
      "0",
      "0",
      "0"
    &#93;
  &#93;,
  "Q_file": "Hv10_syzygies_exact.json",
  "R_file": "Hv10_right_inverse_exact.json",
  "identities": &#91;
    "C H = d I_5",
    "Q H = 0",
    "C R = 0",
    "Q R = d I_5",
    "H C + R Q = d I_10"
  &#93;
}
</code></pre>

<a id="source-fd22317d1e90a478"></a>

## `research-notes/lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json`

<pre><code class="language-json">
{
  "ring": "Q&#91;a0,...,a6&#93;",
  "shape": &#91;
    10,
    5
  &#93;,
  "definition": "M = vertical_stack(G, Q*A), A=top ten rows of H_u, G=bottom H_u - L*A",
  "G": &#91;
    &#91;
      "2*a0*a3/9 + 8*a0*a4/27 + 2*a0*a5/9 - 2*a1*a3/27 + 8*a1*a5/27 + 2*a1*a6/3 - a1/3 - 2*a2*a4/81 - 2*a2*a5/27 - a2/18 - a5/81 - 2*a6/27 + 1/54",
      "a0*a3 + a0*a4/3 - a1*a3/3 + a1*a4/3 + a1*a5/3 - a2*a4/9 + a2/2 - a5/18 + a6/6",
      "-4*a0*a3/27 - 16*a0*a4/81 - 10*a0*a5/27 - 2*a0*a6/3 + a0/9 + 2*a1*a2/3 + 4*a1*a3/81 - 10*a1*a5/81 - 10*a1*a6/9 + 2*a1/9 + 4*a2*a4/243 + 4*a2*a5/81 + 2*a2*a6/9 - 4*a2/27 + 2*a5/243 + 4*a6/81 - 1/81",
      "-2*a0*a2/3 + 8*a0*a3/81 + 32*a0*a4/243 + 20*a0*a5/81 + 10*a0*a6/9 - 19*a0/54 + 2*a1**2/3 - 10*a1*a2/9 - 8*a1*a3/243 + 20*a1*a5/243 + 14*a1*a6/27 - 7*a1/27 + 2*a2**2/9 - 8*a2*a4/729 - 8*a2*a5/243 - 4*a2*a6/27 + 8*a2/81 - 4*a5/729 - 8*a6/243 + 2/243",
      "10*a0*a2/9 - 16*a0*a3/243 - 64*a0*a4/729 - 40*a0*a5/243 - 20*a0*a6/27 + a0/81 - 10*a1**2/9 + 20*a1*a2/27 + 16*a1*a3/729 - 40*a1*a5/729 - 28*a1*a6/81 + 14*a1/81 - 4*a2**2/27 + 16*a2*a4/2187 + 16*a2*a5/729 + 8*a2*a6/81 - 16*a2/243 + 8*a5/2187 + 16*a6/729 - 4/729"
    &#93;,
    &#91;
      "2*a1*a3/9 + 8*a1*a4/27 + 2*a1*a5/9 - 2*a2*a3/27 + 8*a2*a5/27 + 2*a2*a6/3 - a2/3 - 2*a4*a6/81 + a4/81 - 2*a5*a6/27 + a5/54 - a6/9 + 1/27",
      "a1*a3 + a1*a4/3 - a2*a3/3 + a2*a4/3 + a2*a5/3 - a4*a6/9 + a4/18 - a5/12 + a6/2 - 1/12",
      "-4*a1*a3/27 - 16*a1*a4/81 - 10*a1*a5/27 - 2*a1*a6/3 + a1/9 + 2*a2**2/3 + 4*a2*a3/81 - 10*a2*a5/81 - 10*a2*a6/9 + a2/6 + 4*a4*a6/243 - 2*a4/243 + 4*a5*a6/81 - a5/81 + 2*a6**2/9 - a6/9 + 1/81",
      "8*a1*a3/81 + 32*a1*a4/243 + 20*a1*a5/81 + 10*a1*a6/9 - 11*a1/27 - 10*a2**2/9 - 8*a2*a3/243 + 20*a2*a5/243 + 20*a2*a6/27 - 2*a2/9 - 8*a4*a6/729 + 4*a4/729 - 8*a5*a6/243 + 2*a5/243 - 4*a6**2/27 + 2*a6/27 - 2/243",
      "2*a0*a2/3 - a0/18 - 2*a1**2/3 - 16*a1*a3/243 - 64*a1*a4/729 - 40*a1*a5/243 - 14*a1*a6/27 + 4*a1/81 + 14*a2**2/27 + 16*a2*a3/729 - 40*a2*a5/729 - 40*a2*a6/81 + 4*a2/27 + 16*a4*a6/2187 - 8*a4/2187 + 16*a5*a6/729 - 4*a5/729 + 8*a6**2/81 - 4*a6/81 + 4/729"
    &#93;,
    &#91;
      "2*a2*a3/3 + 8*a2*a4/9 + 2*a2*a5/3 - 2*a3*a6/9 + a3/27 + 2*a4*a5/81 + a4/27 + 2*a5**2/27 + 8*a5*a6/9 - 7*a5/54 + 2*a6**2 - 5*a6/3 + 1/3",
      "3*a2*a3 + a2*a4 - a3*a6 + a3/6 + a4*a5/9 + a4*a6 + a5*a6 - 5*a5/6",
      "-4*a2*a3/9 - 16*a2*a4/27 - 10*a2*a5/9 - a2/3 + 4*a3*a6/27 - 2*a3/81 - 4*a4*a5/243 - 2*a4/81 - 4*a5**2/81 - 16*a5*a6/27 + 10*a5/81 - 10*a6**2/3 + 13*a6/9 - 1/6",
      "2*a1*a6 - 2*a1/3 - 2*a2**2 + 8*a2*a3/27 + 32*a2*a4/81 + 14*a2*a5/27 - 5*a2/18 - 8*a3*a6/81 + 4*a3/243 + 8*a4*a5/729 + 4*a4/243 + 8*a5**2/243 + 32*a5*a6/81 - 20*a5/243 + 14*a6**2/9 - 23*a6/27 + 1/9",
      "2*a0*a6 - 2*a0/3 - 2*a1*a2 - 2*a1*a5/9 - 10*a1*a6/3 + 7*a1/9 + 10*a2**2/3 - 16*a2*a3/81 - 64*a2*a4/243 - 28*a2*a5/81 - 2*a2*a6/3 - a2/27 + 16*a3*a6/243 - 8*a3/729 - 16*a4*a5/2187 - 8*a4/729 - 16*a5**2/729 - 64*a5*a6/243 + 40*a5/729 - 28*a6**2/27 + 46*a6/81 - 2/27"
    &#93;,
    &#91;
      "2*a3*a5/27 + 2*a3*a6/3 - 5*a3/18 - 2*a4**2/81 - 2*a4*a5/27 + 8*a4*a6/9 - 2*a4/9 - 8*a5**2/27 + a5/3",
      "a3*a5/3 + 3*a3*a6 - 5*a3/4 - a4**2/9 - a4*a5/3 + a4*a6 + a4/2 - a5**2/3",
      "-2*a2*a5/3 - 4*a3*a5/81 - 4*a3*a6/9 + 5*a3/27 + 4*a4**2/243 + 4*a4*a5/81 - 10*a4*a6/27 + 2*a4/27 + 10*a5**2/81 - a5/18 - 2*a6**2 + a6/3",
      "-2*a1*a5/3 + 2*a2*a4/9 + 10*a2*a5/9 - 2*a2*a6 + 8*a3*a5/243 + 8*a3*a6/27 - 10*a3/81 - 8*a4**2/729 - 8*a4*a5/243 + 20*a4*a6/81 - 4*a4/81 - 20*a5**2/243 + 2*a5*a6/9 + a5/27 + 10*a6**2/3 - 14*a6/9 + 1/6",
      "-2*a0*a5/3 + 2*a1*a4/9 + 10*a1*a5/9 - 2*a1*a6 - 4*a2*a4/27 - 14*a2*a5/27 + 10*a2*a6/3 - a2/2 - 16*a3*a5/729 - 16*a3*a6/81 + 20*a3/243 + 16*a4**2/2187 + 16*a4*a5/729 - 40*a4*a6/243 + 8*a4/243 + 40*a5**2/729 - 4*a5*a6/27 - 2*a5/81 - 20*a6**2/9 + 19*a6/27"
    &#93;,
    &#91;
      "a3/2 - 2*a4*a6/3 + 2*a4/3 + 2*a5**2/9",
      "a3*a5 + 3*a3 - a4**2/3",
      "-2*a2*a4/3 + 2*a3*a6/3 - 5*a3/9 - 2*a4*a5/27 + 10*a4*a6/9 - 5*a4/9 - 10*a5**2/27 - 2*a5*a6/3 - 2*a5/9",
      "-2*a1*a4/3 + 2*a2*a3/3 + 10*a2*a4/9 - 2*a2*a5/3 - 4*a3*a6/9 + 10*a3/27 + 4*a4*a5/81 - 14*a4*a6/27 + 10*a4/27 + 20*a5**2/81 + 10*a5*a6/9 - a5/54 + a6 - 1/3",
      "-2*a0*a4/3 + 2*a1*a3/3 + 10*a1*a4/9 - 2*a1*a5/3 - 4*a2*a3/9 - 14*a2*a4/27 + 10*a2*a5/9 + a2 + 8*a3*a6/27 - 20*a3/81 - 8*a4*a5/243 + 28*a4*a6/81 - 20*a4/81 - 40*a5**2/243 - 20*a5*a6/27 - 8*a5/81 - a6 + 1/18"
    &#93;
  &#93;,
  "QA": &#91;
    &#91;
      "-a1*a3**2*a6/9 + a1*a3**2/54 + a1*a3*a4*a5/27 - a1*a3*a4*a6/9 + a1*a3*a4/54 + 2*a1*a3*a5**2/27 - 2*a1*a4**3/243 - a1*a4**2*a5/81 + a2**2*a3**2/9 + a2**2*a3*a4/9 + a2*a3*a4*a6/9 - 7*a2*a3*a4/162 + 4*a2*a3*a5**2/81 + 5*a2*a3*a5*a6/9 - 7*a2*a3*a5/54 - 5*a2*a4**2*a5/243 - 2*a2*a4**2*a6/27 - a2*a4*a5**2/81 + 4*a3*a5*a6**2/27 - 13*a3*a5*a6/162 + a3*a5/108 + a3*a6**3 - 2*a3*a6**2/3 + 5*a3*a6/36 - a3/108 + 2*a4**2*a6**2/81 - 5*a4**2*a6/243 + a4**2/243 - 8*a4*a5**2*a6/243 + 5*a4*a5**2/486 - a4*a5*a6**2/9 + a4*a5*a6/162 + a4*a5/162 + a5**4/243 + a5**3*a6/81 + a5**3/162",
      "-a1*a3**2*a6/2 + a1*a3**2/12 + a1*a3*a4*a5/6 - a1*a4**3/27 + a2**2*a3**2/2 + a2*a3*a4*a6/2 - 7*a2*a3*a4/36 + 2*a2*a3*a5**2/9 - 5*a2*a4**2*a5/54 + 2*a3*a5*a6**2/3 - 13*a3*a5*a6/36 + a3*a5/24 + a4**2*a6**2/9 - 5*a4**2*a6/54 + a4**2/54 - 4*a4*a5**2*a6/27 + 5*a4*a5**2/108 + a5**4/54",
      "2*a1*a3**2*a6/27 - a1*a3**2/81 - 2*a1*a3*a4*a5/81 + 2*a1*a3*a4*a6/27 - a1*a3*a4/81 - 4*a1*a3*a5**2/81 - a1*a3*a5*a6/9 + a1*a3*a5/18 + 4*a1*a4**3/729 + 2*a1*a4**2*a5/243 + 2*a1*a4**2*a6/27 - 2*a1*a4**2/81 - a1*a4*a5**2/81 - 2*a2**2*a3**2/27 - 2*a2**2*a3*a4/27 + 2*a2**2*a3*a5/9 - a2**2*a4**2/9 - 2*a2*a3*a4*a6/27 + 7*a2*a3*a4/243 - 8*a2*a3*a5**2/243 - 10*a2*a3*a5*a6/27 + 7*a2*a3*a5/81 + a2*a3*a6**2/3 - a2*a3*a6/18 - a2*a3/54 + 10*a2*a4**2*a5/729 + 4*a2*a4**2*a6/81 + 2*a2*a4*a5**2/243 - 5*a2*a4*a5*a6/27 + 4*a2*a4*a5/81 + 2*a2*a5**3/81 - 8*a3*a5*a6**2/81 + 13*a3*a5*a6/243 - a3*a5/162 - 2*a3*a6**3/3 + 4*a3*a6**2/9 - 5*a3*a6/54 + a3/162 - 4*a4**2*a6**2/243 + 10*a4**2*a6/729 - 2*a4**2/729 + 16*a4*a5**2*a6/729 - 5*a4*a5**2/729 + 2*a4*a5*a6**2/27 - a4*a5*a6/243 - a4*a5/243 - 2*a4*a6**3/9 + 7*a4*a6**2/27 - 8*a4*a6/81 + a4/81 - 2*a5**4/729 - 2*a5**3*a6/243 - a5**3/243 + a5**2*a6**2/27 - a5**2*a6/27 + a5**2/108",
      "a1*a2*a3*a5/9 - a1*a2*a4**2/27 - 4*a1*a3**2*a6/81 + 2*a1*a3**2/243 + 4*a1*a3*a4*a5/243 - 4*a1*a3*a4*a6/81 + 2*a1*a3*a4/243 + 8*a1*a3*a5**2/243 + 2*a1*a3*a5*a6/27 - a1*a3*a5/27 + 2*a1*a3*a6**2/3 - 4*a1*a3*a6/9 + a1*a3/18 - 8*a1*a4**3/2187 - 4*a1*a4**2*a5/729 - 4*a1*a4**2*a6/81 + 4*a1*a4**2/243 + 2*a1*a4*a5**2/243 - 5*a1*a4*a5*a6/27 + a1*a4*a5/18 + a1*a5**3/27 + 4*a2**2*a3**2/81 + 4*a2**2*a3*a4/81 - 4*a2**2*a3*a5/27 - a2**2*a3*a6/3 + 2*a2**2*a3/9 + 2*a2**2*a4**2/27 + 2*a2**2*a4*a5/27 + 4*a2*a3*a4*a6/81 - 14*a2*a3*a4/729 + 16*a2*a3*a5**2/729 + 20*a2*a3*a5*a6/81 - 14*a2*a3*a5/243 - 2*a2*a3*a6**2/9 + a2*a3*a6/27 + a2*a3/81 - 20*a2*a4**2*a5/2187 - 8*a2*a4**2*a6/243 - 4*a2*a4*a5**2/729 + 10*a2*a4*a5*a6/81 - 8*a2*a4*a5/243 - a2*a4*a6**2/9 + 7*a2*a4*a6/54 - a2*a4/27 - 4*a2*a5**3/243 + a2*a5**2*a6/9 - a2*a5**2/27 + 16*a3*a5*a6**2/243 - 26*a3*a5*a6/729 + a3*a5/243 + 4*a3*a6**3/9 - 8*a3*a6**2/27 + 5*a3*a6/81 - a3/243 + 8*a4**2*a6**2/729 - 20*a4**2*a6/2187 + 4*a4**2/2187 - 32*a4*a5**2*a6/2187 + 10*a4*a5**2/2187 - 4*a4*a5*a6**2/81 + 2*a4*a5*a6/729 + 2*a4*a5/729 + 4*a4*a6**3/27 - 14*a4*a6**2/81 + 16*a4*a6/243 - 2*a4/243 + 4*a5**4/2187 + 4*a5**3*a6/729 + 2*a5**3/729 - 2*a5**2*a6**2/81 + 2*a5**2*a6/81 - a5**2/162 + a5*a6**3/9 - 2*a5*a6**2/27 + a5*a6/108",
      "a0*a2*a3*a5/3 - a0*a2*a4**2/9 + a0*a3*a6**2 - a0*a3*a6/2 + a0*a3/18 - 2*a0*a4*a5*a6/9 + a0*a4*a5/18 + a0*a5**3/27 - 2*a1**2*a3*a5/9 + 2*a1**2*a4**2/27 - 2*a1*a2*a3*a5/27 - a1*a2*a3*a6 + 5*a1*a2*a3/18 + 2*a1*a2*a4**2/81 + a1*a2*a4*a5/9 + 8*a1*a3**2*a6/243 - 4*a1*a3**2/729 - 8*a1*a3*a4*a5/729 + 8*a1*a3*a4*a6/243 - 4*a1*a3*a4/729 - 16*a1*a3*a5**2/729 - 4*a1*a3*a5*a6/81 + 2*a1*a3*a5/81 - 4*a1*a3*a6**2/9 + 8*a1*a3*a6/27 - a1*a3/27 + 16*a1*a4**3/6561 + 8*a1*a4**2*a5/2187 + 8*a1*a4**2*a6/243 - 8*a1*a4**2/729 - 4*a1*a4*a5**2/729 + 10*a1*a4*a5*a6/81 - a1*a4*a5/27 - 2*a1*a4*a6**2/9 + 8*a1*a4*a6/27 - a1*a4/18 - 2*a1*a5**3/81 + 2*a1*a5**2*a6/27 - 2*a1*a5**2/27 + a2**3*a3/3 - 8*a2**2*a3**2/243 - 8*a2**2*a3*a4/243 + 8*a2**2*a3*a5/81 + 2*a2**2*a3*a6/9 - 4*a2**2*a3/27 - 4*a2**2*a4**2/81 - 4*a2**2*a4*a5/81 + a2**2*a4*a6/9 - a2**2*a4/6 + a2**2*a5**2/27 - 8*a2*a3*a4*a6/243 + 28*a2*a3*a4/2187 - 32*a2*a3*a5**2/2187 - 40*a2*a3*a5*a6/243 + 28*a2*a3*a5/729 + 4*a2*a3*a6**2/27 - 2*a2*a3*a6/81 - 2*a2*a3/243 + 40*a2*a4**2*a5/6561 + 16*a2*a4**2*a6/729 + 8*a2*a4*a5**2/2187 - 20*a2*a4*a5*a6/243 + 16*a2*a4*a5/729 + 2*a2*a4*a6**2/27 - 7*a2*a4*a6/81 + 2*a2*a4/81 + 8*a2*a5**3/729 - 2*a2*a5**2*a6/27 + 2*a2*a5**2/81 + a2*a5*a6**2/9 - 8*a2*a5*a6/27 + 11*a2*a5/108 - 32*a3*a5*a6**2/729 + 52*a3*a5*a6/2187 - 2*a3*a5/729 - 8*a3*a6**3/27 + 16*a3*a6**2/81 - 10*a3*a6/243 + 2*a3/729 - 16*a4**2*a6**2/2187 + 40*a4**2*a6/6561 - 8*a4**2/6561 + 64*a4*a5**2*a6/6561 - 20*a4*a5**2/6561 + 8*a4*a5*a6**2/243 - 4*a4*a5*a6/2187 - 4*a4*a5/2187 - 8*a4*a6**3/81 + 28*a4*a6**2/243 - 32*a4*a6/729 + 4*a4/729 - 8*a5**4/6561 - 8*a5**3*a6/2187 - 4*a5**3/2187 + 4*a5**2*a6**2/243 - 4*a5**2*a6/243 + a5**2/243 - 2*a5*a6**3/27 + 4*a5*a6**2/81 - a5*a6/162 - a6**3/3 + a6**2/3 - 11*a6/108 + 1/108"
    &#93;,
    &#91;
      "-a0*a3**2*a6/18 + a0*a3**2/108 + a0*a3*a4*a5/54 - a0*a3*a4*a6/18 + a0*a3*a4/108 + a0*a3*a5**2/27 - a0*a4**3/243 - a0*a4**2*a5/162 + a1*a2*a3**2/18 + a1*a2*a3*a4/18 + 2*a1*a3*a4*a6/27 - a1*a3*a4/54 - a1*a3*a5**2/54 - a1*a3*a5/18 + 2*a1*a4**2*a6/27 - a1*a4*a5**2/54 - a2**2*a3*a4/54 + 4*a2**2*a3*a5/9 - a2**2*a4**2/6 - 13*a2*a3*a5*a6/54 + a2*a3*a5/6 + a2*a3*a6**2 - 7*a2*a3*a6/12 + 7*a2*a3/72 + 5*a2*a4**2*a6/81 - 7*a2*a4**2/162 - 5*a2*a4*a5*a6/18 + 11*a2*a4*a5/108 + a2*a5**3/27 - 5*a3*a6**3/9 + 19*a3*a6**2/27 - 13*a3*a6/54 + 5*a3/216 + 7*a4*a5*a6**2/81 - 7*a4*a5*a6/81 + 5*a4*a5/324 - 2*a4*a6**3/9 + 7*a4*a6**2/27 - a4*a6/18 - a5**3*a6/81 + a5**3/108 + a5**2*a6**2/27 - a5**2*a6/36 - a5**2/216",
      "-a0*a3**2*a6/4 + a0*a3**2/24 + a0*a3*a4*a5/12 - a0*a4**3/54 + a1*a2*a3**2/4 + a1*a3*a4*a6/3 - a1*a3*a4/12 - a1*a3*a5**2/12 - a2**2*a3*a4/12 - 13*a2*a3*a5*a6/12 + 3*a2*a3*a5/4 + 5*a2*a4**2*a6/18 - 7*a2*a4**2/36 - 5*a3*a6**3/2 + 19*a3*a6**2/6 - 13*a3*a6/12 + 5*a3/48 + 7*a4*a5*a6**2/18 - 7*a4*a5*a6/18 + 5*a4*a5/72 - a5**3*a6/18 + a5**3/24",
      "a0*a3**2*a6/27 - a0*a3**2/162 - a0*a3*a4*a5/81 + a0*a3*a4*a6/27 - a0*a3*a4/162 - 2*a0*a3*a5**2/81 - a0*a3*a5*a6/18 + a0*a3*a5/36 + 2*a0*a4**3/729 + a0*a4**2*a5/243 + a0*a4**2*a6/27 - a0*a4**2/81 - a0*a4*a5**2/162 - a1*a2*a3**2/27 - a1*a2*a3*a4/27 + 5*a1*a2*a3*a5/18 - a1*a2*a4**2/9 - 4*a1*a3*a4*a6/81 + a1*a3*a4/81 + a1*a3*a5**2/81 + a1*a3*a5/27 + a1*a3*a6**2 - a1*a3*a6/3 + a1*a3/36 - 4*a1*a4**2*a6/81 + a1*a4*a5**2/81 - 8*a1*a4*a5*a6/27 + a1*a4*a5/18 + a1*a5**3/18 + a2**2*a3*a4/81 - 8*a2**2*a3*a5/27 - a2**2*a3*a6/3 + a2**2*a3/36 + a2**2*a4**2/9 + a2**2*a4*a5/18 + 13*a2*a3*a5*a6/81 - a2*a3*a5/9 - 2*a2*a3*a6**2/3 + 7*a2*a3*a6/18 - 7*a2*a3/108 - 10*a2*a4**2*a6/243 + 7*a2*a4**2/243 + 5*a2*a4*a5*a6/27 - 11*a2*a4*a5/162 - 2*a2*a4*a6**2/9 + 5*a2*a4*a6/27 - a2*a4/54 - 2*a2*a5**3/81 + 7*a2*a5**2*a6/54 - 5*a2*a5**2/54 + 10*a3*a6**3/27 - 38*a3*a6**2/81 + 13*a3*a6/81 - 5*a3/324 - 14*a4*a5*a6**2/243 + 14*a4*a5*a6/243 - 5*a4*a5/486 + 4*a4*a6**3/27 - 14*a4*a6**2/81 + a4*a6/27 + 2*a5**3*a6/243 - a5**3/162 - 2*a5**2*a6**2/81 + a5**2*a6/54 + a5**2/324 + a5*a6**3/9 - a5*a6**2/6 + 2*a5*a6/27 - a5/108",
      "-a0*a2*a3*a5/9 + a0*a2*a4**2/27 - 2*a0*a3**2*a6/81 + a0*a3**2/243 + 2*a0*a3*a4*a5/243 - 2*a0*a3*a4*a6/81 + a0*a3*a4/243 + 4*a0*a3*a5**2/243 + a0*a3*a5*a6/27 - a0*a3*a5/54 - a0*a3*a6**2/6 + a0*a3*a6/36 - 4*a0*a4**3/2187 - 2*a0*a4**2*a5/729 - 2*a0*a4**2*a6/81 + 2*a0*a4**2/243 + a0*a4*a5**2/243 + a0*a4*a5*a6/54 + a1**2*a3*a5/3 - a1**2*a4**2/9 + 2*a1*a2*a3**2/81 + 2*a1*a2*a3*a4/81 - 5*a1*a2*a3*a5/27 + 13*a1*a2*a3*a6/6 - 5*a1*a2*a3/12 + 2*a1*a2*a4**2/27 - 2*a1*a2*a4*a5/9 + 8*a1*a3*a4*a6/243 - 2*a1*a3*a4/243 - 2*a1*a3*a5**2/243 - 2*a1*a3*a5/81 - 2*a1*a3*a6**2/3 + 2*a1*a3*a6/9 - a1*a3/54 + 8*a1*a4**2*a6/243 - 2*a1*a4*a5**2/243 + 16*a1*a4*a5*a6/81 - a1*a4*a5/27 + 8*a1*a4*a6**2/9 - 4*a1*a4*a6/9 + a1*a4/18 - a1*a5**3/27 - 5*a1*a5**2*a6/18 + a1*a5**2/12 - 4*a2**3*a3/3 - 2*a2**2*a3*a4/243 + 16*a2**2*a3*a5/81 + 2*a2**2*a3*a6/9 - a2**2*a3/54 - 2*a2**2*a4**2/27 - a2**2*a4*a5/27 - 19*a2**2*a4*a6/18 + 7*a2**2*a4/18 - a2**2*a5**2/9 - 26*a2*a3*a5*a6/243 + 2*a2*a3*a5/27 + 4*a2*a3*a6**2/9 - 7*a2*a3*a6/27 + 7*a2*a3/162 + 20*a2*a4**2*a6/729 - 14*a2*a4**2/729 - 10*a2*a4*a5*a6/81 + 11*a2*a4*a5/243 + 4*a2*a4*a6**2/27 - 10*a2*a4*a6/81 + a2*a4/81 + 4*a2*a5**3/243 - 7*a2*a5**2*a6/81 + 5*a2*a5**2/81 - 3*a2*a5*a6**2/2 + 37*a2*a5*a6/36 - a2*a5/6 - 20*a3*a6**3/81 + 76*a3*a6**2/243 - 26*a3*a6/243 + 5*a3/486 + 28*a4*a5*a6**2/729 - 28*a4*a5*a6/729 + 5*a4*a5/729 - 8*a4*a6**3/81 + 28*a4*a6**2/243 - 2*a4*a6/81 - 4*a5**3*a6/729 + a5**3/243 + 4*a5**2*a6**2/243 - a5**2*a6/81 - a5**2/486 - 2*a5*a6**3/27 + a5*a6**2/9 - 4*a5*a6/81 + a5/162 - 5*a6**4/3 + 19*a6**3/9 - 35*a6**2/36 + 7*a6/36 - 1/72",
      "2*a0*a1*a3*a5/9 - 2*a0*a1*a4**2/27 + 2*a0*a2*a3*a5/27 + 5*a0*a2*a3*a6/6 - 2*a0*a2*a3/9 - 2*a0*a2*a4**2/81 - 5*a0*a2*a4*a5/54 + 4*a0*a3**2*a6/243 - 2*a0*a3**2/729 - 4*a0*a3*a4*a5/729 + 4*a0*a3*a4*a6/243 - 2*a0*a3*a4/729 - 8*a0*a3*a5**2/729 - 2*a0*a3*a5*a6/81 + a0*a3*a5/81 + a0*a3*a6**2/9 - a0*a3*a6/54 + 8*a0*a4**3/6561 + 4*a0*a4**2*a5/2187 + 4*a0*a4**2*a6/243 - 4*a0*a4**2/729 - 2*a0*a4*a5**2/729 - a0*a4*a5*a6/81 + a0*a4*a6**2/3 - a0*a4*a6/9 + a0*a4/54 - a0*a5**2*a6/9 + a0*a5**2/108 - 2*a1**2*a3*a5/9 + a1**2*a3*a6 - a1**2*a3/6 + 2*a1**2*a4**2/27 - a1**2*a4*a5/9 - 7*a1*a2**2*a3/6 - 4*a1*a2*a3**2/243 - 4*a1*a2*a3*a4/243 + 10*a1*a2*a3*a5/81 - 13*a1*a2*a3*a6/9 + 5*a1*a2*a3/18 - 4*a1*a2*a4**2/81 + 4*a1*a2*a4*a5/27 + a1*a2*a4/18 - 5*a1*a2*a5**2/18 - 16*a1*a3*a4*a6/729 + 4*a1*a3*a4/729 + 4*a1*a3*a5**2/729 + 4*a1*a3*a5/243 + 4*a1*a3*a6**2/9 - 4*a1*a3*a6/27 + a1*a3/81 - 16*a1*a4**2*a6/729 + 4*a1*a4*a5**2/729 - 32*a1*a4*a5*a6/243 + 2*a1*a4*a5/81 - 16*a1*a4*a6**2/27 + 8*a1*a4*a6/27 - a1*a4/27 + 2*a1*a5**3/81 + 5*a1*a5**2*a6/27 - a1*a5**2/18 - 4*a1*a5*a6**2/9 + 2*a1*a5*a6/9 + 8*a2**3*a3/9 - a2**3*a4/2 + 4*a2**2*a3*a4/729 - 32*a2**2*a3*a5/243 - 4*a2**2*a3*a6/27 + a2**2*a3/81 + 4*a2**2*a4**2/81 + 2*a2**2*a4*a5/81 + 19*a2**2*a4*a6/27 - 7*a2**2*a4/27 + 2*a2**2*a5**2/27 - 19*a2**2*a5*a6/18 + 13*a2**2*a5/36 + 52*a2*a3*a5*a6/729 - 4*a2*a3*a5/81 - 8*a2*a3*a6**2/27 + 14*a2*a3*a6/81 - 7*a2*a3/243 - 40*a2*a4**2*a6/2187 + 28*a2*a4**2/2187 + 20*a2*a4*a5*a6/243 - 22*a2*a4*a5/729 - 8*a2*a4*a6**2/81 + 20*a2*a4*a6/243 - 2*a2*a4/243 - 8*a2*a5**3/729 + 14*a2*a5**2*a6/243 - 10*a2*a5**2/243 + a2*a5*a6**2 - 37*a2*a5*a6/54 + a2*a5/9 - 5*a2*a6**3/3 + 13*a2*a6**2/9 - 13*a2*a6/36 + a2/36 + 40*a3*a6**3/243 - 152*a3*a6**2/729 + 52*a3*a6/729 - 5*a3/729 - 56*a4*a5*a6**2/2187 + 56*a4*a5*a6/2187 - 10*a4*a5/2187 + 16*a4*a6**3/243 - 56*a4*a6**2/729 + 4*a4*a6/243 + 8*a5**3*a6/2187 - 2*a5**3/729 - 8*a5**2*a6**2/729 + 2*a5**2*a6/243 + a5**2/729 + 4*a5*a6**3/81 - 2*a5*a6**2/27 + 8*a5*a6/243 - a5/243 + 10*a6**4/9 - 38*a6**3/27 + 35*a6**2/54 - 7*a6/54 + 1/108"
    &#93;,
    &#91;
      "-a0**2*a2*a3**2*a5/6 + a0**2*a2*a3*a4**2/27 - a0**2*a2*a3*a4*a5/6 + a0**2*a2*a4**3/27 + 2*a0**2*a3**2*a6/9 - a0**2*a3**2/27 - a0**2*a3*a4*a5*a6/54 - 17*a0**2*a3*a4*a5/324 + 2*a0**2*a3*a4*a6/9 - a0**2*a3*a4/27 - a0**2*a3*a5**3/18 - a0**2*a3*a5**2*a6/2 - 7*a0**2*a3*a5**2/108 + 2*a0**2*a4**3*a6/81 + 2*a0**2*a4**3/243 + 5*a0**2*a4**2*a5**2/486 + 2*a0**2*a4**2*a5*a6/9 - a0**2*a4**2*a5/162 - 2*a0**2*a4*a5**3/81 + a0*a1**2*a3**2*a5/6 - a0*a1**2*a3*a4**2/27 + a0*a1**2*a3*a4*a5/6 - a0*a1**2*a4**3/27 + 2*a0*a1*a2*a3**2*a6/3 - a0*a1*a2*a3**2/2 - 29*a0*a1*a2*a3*a4*a5/54 + 2*a0*a1*a2*a3*a4*a6/3 - a0*a1*a2*a3*a4/2 - a0*a1*a2*a3*a5**2/9 + 8*a0*a1*a2*a4**3/81 - 11*a0*a1*a2*a4**2*a5/54 - 5*a0*a1*a3*a4*a6**2/9 + 7*a0*a1*a3*a4*a6/54 + a0*a1*a3*a4/27 - 11*a0*a1*a3*a5**2*a6/18 + 19*a0*a1*a3*a5**2/108 - 3*a0*a1*a3*a5*a6**2 + a0*a1*a3*a5*a6/3 + a0*a1*a3*a5/9 + 16*a0*a1*a4**2*a5*a6/81 - a0*a1*a4**2*a5/27 + 4*a0*a1*a4**2*a6**2/9 - a0*a1*a4**2*a6/27 + a0*a1*a4**2/54 - a0*a1*a4*a5**2*a6/54 + a0*a1*a4*a5**2/12 - a0*a2**3*a3**2 - a0*a2**3*a3*a4 - 11*a0*a2**2*a3*a4*a6/9 + 5*a0*a2**2*a3*a4/27 - 7*a0*a2**2*a3*a5**2/9 - 5*a0*a2**2*a3*a5*a6 + 25*a0*a2**2*a3*a5/18 + 19*a0*a2**2*a4**2*a5/81 + 7*a0*a2**2*a4**2*a6/9 - 7*a0*a2**2*a4**2/18 - 5*a0*a2**2*a4*a5**2/27 - 59*a0*a2*a3*a5*a6**2/18 + 85*a0*a2*a3*a5*a6/108 - 11*a0*a2*a3*a5/108 - 15*a0*a2*a3*a6**3 + 41*a0*a2*a3*a6**2/4 - 21*a0*a2*a3*a6/8 + 17*a0*a2*a3/72 - 10*a0*a2*a4**2*a6**2/27 + 61*a0*a2*a4**2*a6/162 - 2*a0*a2*a4**2/81 + 38*a0*a2*a4*a5**2*a6/81 - a0*a2*a4*a5**2/9 + 17*a0*a2*a4*a5*a6**2/18 - 5*a0*a2*a4*a5*a6/6 + 11*a0*a2*a4*a5/54 - 4*a0*a2*a5**4/81 - 7*a0*a2*a5**3*a6/27 + 7*a0*a2*a5**3/54 - 22*a0*a3*a6**3/9 + 73*a0*a3*a6**2/54 - 23*a0*a3*a6/108 + a0*a3/108 - a0*a4*a5*a6**3/3 + 103*a0*a4*a5*a6**2/162 - 13*a0*a4*a5*a6/81 + a0*a4*a5/108 - a0*a4*a6**4 - 4*a0*a4*a6**3/9 + 17*a0*a4*a6**2/108 + a0*a4*a6/108 + 2*a0*a5**3*a6**2/27 - 31*a0*a5**3*a6/324 + a0*a5**3/162 + 29*a0*a5**2*a6**2/108 + a0*a5**2*a6/24 + a1**3*a3**2/6 + a1**3*a3*a4*a5/3 + a1**3*a3*a4/6 + a1**3*a3*a5**2/3 - 2*a1**3*a4**3/27 + a1**2*a2**2*a3**2/3 + a1**2*a2**2*a3*a4/3 + 14*a1**2*a2*a3*a4*a6/9 - 2*a1**2*a2*a3*a4/9 + 2*a1**2*a2*a3*a5**2/3 + 13*a1**2*a2*a3*a5*a6/2 - 7*a1**2*a2*a3*a5/4 - 7*a1**2*a2*a4**2*a5/27 - 7*a1**2*a2*a4**2*a6/9 + 4*a1**2*a2*a4**2/9 - a1**2*a2*a4*a5**2/18 - 2*a1**2*a3*a5*a6**2/3 + 11*a1**2*a3*a5*a6/9 - a1**2*a3*a5/9 - 3*a1**2*a3*a6**2/2 + 3*a1**2*a3*a6/4 - a1**2*a3/12 + 4*a1**2*a4**2*a6**2/9 - 4*a1**2*a4**2*a6/9 + a1**2*a4**2/18 - a1**2*a4*a5**2*a6/9 + a1**2*a4*a5**2/27 + 7*a1**2*a4*a5*a6/18 + a1**2*a5**4/54 + a1**2*a5**3*a6/18 + a1**2*a5**3/36 - 4*a1*a2**3*a3*a4/9 - 4*a1*a2**3*a3*a5/3 + 10*a1*a2**2*a3*a5*a6/3 - 29*a1*a2**2*a3*a5/36 + 15*a1*a2**2*a3*a6**2 - 35*a1*a2**2*a3*a6/4 + 35*a1*a2**2*a3/24 - 2*a1*a2**2*a4**2*a6/9 + 5*a1*a2**2*a4**2/54 - 2*a1*a2**2*a4*a5**2/9 - a1*a2**2*a4*a5*a6/3 + 11*a1*a2**2*a4*a5/18 - 2*a1*a2**2*a5**3/9 - 2*a1*a2*a3*a6**3/3 + 46*a1*a2*a3*a6**2/9 - 47*a1*a2*a3*a6/36 + a1*a2*a3/72 + 7*a1*a2*a4*a5*a6**2/27 - 25*a1*a2*a4*a5*a6/54 + 5*a1*a2*a4*a5/108 + 10*a1*a2*a4*a6**3/3 - 20*a1*a2*a4*a6**2/9 + 4*a1*a2*a4*a6/3 - 2*a1*a2*a4/9 - a1*a2*a5**3*a6/27 + a1*a2*a5**3/108 - 8*a1*a2*a5**2*a6**2/9 + 47*a1*a2*a5**2*a6/36 - 13*a1*a2*a5**2/72 - 2*a1*a4*a6**4/3 + 17*a1*a4*a6**3/9 - 19*a1*a4*a6**2/27 + a1*a4*a6/9 - a1*a4/108 + 2*a1*a5**2*a6**3/9 - 29*a1*a5**2*a6**2/54 + a1*a5**2*a6/9 - a1*a5**2/108 + 5*a1*a5*a6**3/6 - a1*a5*a6**2/36 - a1*a5*a6/36 - 7*a2**4*a3*a5/6 - 6*a2**4*a3*a6 + 3*a2**4*a3 - a2**4*a4*a5/2 + a2**3*a3*a6**2/3 - 7*a2**3*a3*a6/3 - a2**3*a3/24 - 10*a2**3*a4*a5*a6/27 + 11*a2**3*a4*a5/108 - 8*a2**3*a4*a6**2/3 + 29*a2**3*a4*a6/12 - 2*a2**3*a4/3 - 5*a2**3*a5**3/54 - 17*a2**3*a5**2*a6/18 + 17*a2**3*a5**2/36 + 2*a2**2*a4*a6**3/9 - 35*a2**2*a4*a6**2/27 + 11*a2**2*a4*a6/54 - a2**2*a4/36 - a2**2*a5**2*a6**2/2 + 7*a2**2*a5**2*a6/108 - a2**2*a5**2/108 - 23*a2**2*a5*a6**3/6 + 101*a2**2*a5*a6**2/18 - 137*a2**2*a5*a6/72 + a2**2*a5/9 - a2*a5*a6**4/3 - 4*a2*a5*a6**3/3 + 67*a2*a5*a6**2/108 - a2*a5*a6/12 + a2*a5/216 - 3*a2*a6**5 + 7*a2*a6**4 - 53*a2*a6**3/12 + 41*a2*a6**2/36 - a2*a6/9 - 5*a6**5/3 + 3*a6**4/2 - 55*a6**3/108 + 17*a6**2/216 - a6/216",
      "-3*a0**2*a2*a3**2*a5/4 + a0**2*a2*a3*a4**2/6 + a0**2*a3**2*a6 - a0**2*a3**2/6 - a0**2*a3*a4*a5*a6/12 - 17*a0**2*a3*a4*a5/72 - a0**2*a3*a5**3/4 + a0**2*a4**3*a6/9 + a0**2*a4**3/27 + 5*a0**2*a4**2*a5**2/108 + 3*a0*a1**2*a3**2*a5/4 - a0*a1**2*a3*a4**2/6 + 3*a0*a1*a2*a3**2*a6 - 9*a0*a1*a2*a3**2/4 - 29*a0*a1*a2*a3*a4*a5/12 + 4*a0*a1*a2*a4**3/9 - 5*a0*a1*a3*a4*a6**2/2 + 7*a0*a1*a3*a4*a6/12 + a0*a1*a3*a4/6 - 11*a0*a1*a3*a5**2*a6/4 + 19*a0*a1*a3*a5**2/24 + 8*a0*a1*a4**2*a5*a6/9 - a0*a1*a4**2*a5/6 - 9*a0*a2**3*a3**2/2 - 11*a0*a2**2*a3*a4*a6/2 + 5*a0*a2**2*a3*a4/6 - 7*a0*a2**2*a3*a5**2/2 + 19*a0*a2**2*a4**2*a5/18 - 59*a0*a2*a3*a5*a6**2/4 + 85*a0*a2*a3*a5*a6/24 - 11*a0*a2*a3*a5/24 - 5*a0*a2*a4**2*a6**2/3 + 61*a0*a2*a4**2*a6/36 - a0*a2*a4**2/9 + 19*a0*a2*a4*a5**2*a6/9 - a0*a2*a4*a5**2/2 - 2*a0*a2*a5**4/9 - 11*a0*a3*a6**3 + 73*a0*a3*a6**2/12 - 23*a0*a3*a6/24 + a0*a3/24 - 3*a0*a4*a5*a6**3/2 + 103*a0*a4*a5*a6**2/36 - 13*a0*a4*a5*a6/18 + a0*a4*a5/24 + a0*a5**3*a6**2/3 - 31*a0*a5**3*a6/72 + a0*a5**3/36 + 3*a1**3*a3**2/4 + 3*a1**3*a3*a4*a5/2 - a1**3*a4**3/3 + 3*a1**2*a2**2*a3**2/2 + 7*a1**2*a2*a3*a4*a6 - a1**2*a2*a3*a4 + 3*a1**2*a2*a3*a5**2 - 7*a1**2*a2*a4**2*a5/6 - 3*a1**2*a3*a5*a6**2 + 11*a1**2*a3*a5*a6/2 - a1**2*a3*a5/2 + 2*a1**2*a4**2*a6**2 - 2*a1**2*a4**2*a6 + a1**2*a4**2/4 - a1**2*a4*a5**2*a6/2 + a1**2*a4*a5**2/6 + a1**2*a5**4/12 - 2*a1*a2**3*a3*a4 + 15*a1*a2**2*a3*a5*a6 - 29*a1*a2**2*a3*a5/8 - a1*a2**2*a4**2*a6 + 5*a1*a2**2*a4**2/12 - a1*a2**2*a4*a5**2 - 3*a1*a2*a3*a6**3 + 23*a1*a2*a3*a6**2 - 47*a1*a2*a3*a6/8 + a1*a2*a3/16 + 7*a1*a2*a4*a5*a6**2/6 - 25*a1*a2*a4*a5*a6/12 + 5*a1*a2*a4*a5/24 - a1*a2*a5**3*a6/6 + a1*a2*a5**3/24 - 3*a1*a4*a6**4 + 17*a1*a4*a6**3/2 - 19*a1*a4*a6**2/6 + a1*a4*a6/2 - a1*a4/24 + a1*a5**2*a6**3 - 29*a1*a5**2*a6**2/12 + a1*a5**2*a6/2 - a1*a5**2/24 - 21*a2**4*a3*a5/4 + 3*a2**3*a3*a6**2/2 - 21*a2**3*a3*a6/2 - 3*a2**3*a3/16 - 5*a2**3*a4*a5*a6/3 + 11*a2**3*a4*a5/24 - 5*a2**3*a5**3/12 + a2**2*a4*a6**3 - 35*a2**2*a4*a6**2/6 + 11*a2**2*a4*a6/12 - a2**2*a4/8 - 9*a2**2*a5**2*a6**2/4 + 7*a2**2*a5**2*a6/24 - a2**2*a5**2/24 - 3*a2*a5*a6**4/2 - 6*a2*a5*a6**3 + 67*a2*a5*a6**2/24 - 3*a2*a5*a6/8 + a2*a5/48 - 15*a6**5/2 + 27*a6**4/4 - 55*a6**3/24 + 17*a6**2/48 - a6/48",
      "a0**2*a2*a3**2*a5/9 - 2*a0**2*a2*a3*a4**2/81 + a0**2*a2*a3*a4*a5/9 + a0**2*a2*a3*a5**2/3 - 2*a0**2*a2*a4**3/81 - 5*a0**2*a2*a4**2*a5/54 - 4*a0**2*a3**2*a6/27 + 2*a0**2*a3**2/81 + a0**2*a3*a4*a5*a6/81 + 17*a0**2*a3*a4*a5/486 - 4*a0**2*a3*a4*a6/27 + 2*a0**2*a3*a4/81 + a0**2*a3*a5**3/27 + a0**2*a3*a5**2*a6/3 + 7*a0**2*a3*a5**2/162 + 2*a0**2*a3*a5*a6**2 - 7*a0**2*a3*a5*a6/9 + a0**2*a3*a5/36 - 4*a0**2*a4**3*a6/243 - 4*a0**2*a4**3/729 - 5*a0**2*a4**2*a5**2/729 - 4*a0**2*a4**2*a5*a6/27 + a0**2*a4**2*a5/243 - 2*a0**2*a4**2*a6**2/9 + 2*a0**2*a4**2/81 + 4*a0**2*a4*a5**3/243 - 19*a0**2*a4*a5**2*a6/54 + 29*a0**2*a4*a5**2/324 + 2*a0**2*a5**4/27 - a0*a1**2*a3**2*a5/9 + 2*a0*a1**2*a3*a4**2/81 - a0*a1**2*a3*a4*a5/9 - a0*a1**2*a3*a5**2/6 + 2*a0*a1**2*a4**3/81 + a0*a1**2*a4**2*a5/27 - 4*a0*a1*a2*a3**2*a6/9 + a0*a1*a2*a3**2/3 + 29*a0*a1*a2*a3*a4*a5/81 - 4*a0*a1*a2*a3*a4*a6/9 + a0*a1*a2*a3*a4/3 + 2*a0*a1*a2*a3*a5**2/27 - 4*a0*a1*a2*a3*a5*a6/3 + a0*a1*a2*a3*a5/18 - 16*a0*a1*a2*a4**3/243 + 11*a0*a1*a2*a4**2*a5/81 - 5*a0*a1*a2*a4**2*a6/9 + 8*a0*a1*a2*a4**2/27 + a0*a1*a2*a4*a5**2/2 + 10*a0*a1*a3*a4*a6**2/27 - 7*a0*a1*a3*a4*a6/81 - 2*a0*a1*a3*a4/81 + 11*a0*a1*a3*a5**2*a6/27 - 19*a0*a1*a3*a5**2/162 + 2*a0*a1*a3*a5*a6**2 - 2*a0*a1*a3*a5*a6/9 - 2*a0*a1*a3*a5/27 + 6*a0*a1*a3*a6**3 - 3*a0*a1*a3*a6**2 + a0*a1*a3*a6/6 + a0*a1*a3/18 - 32*a0*a1*a4**2*a5*a6/243 + 2*a0*a1*a4**2*a5/81 - 8*a0*a1*a4**2*a6**2/27 + 2*a0*a1*a4**2*a6/81 - a0*a1*a4**2/81 + a0*a1*a4*a5**2*a6/81 - a0*a1*a4*a5**2/18 - 14*a0*a1*a4*a5*a6**2/9 + 31*a0*a1*a4*a5*a6/54 - 5*a0*a1*a4*a5/108 + a0*a1*a5**3*a6/2 - 5*a0*a1*a5**3/36 + 2*a0*a2**3*a3**2/3 + 2*a0*a2**3*a3*a4/3 - 2*a0*a2**3*a3*a5 + 4*a0*a2**3*a4**2/3 + 22*a0*a2**2*a3*a4*a6/27 - 10*a0*a2**2*a3*a4/81 + 14*a0*a2**2*a3*a5**2/27 + 10*a0*a2**2*a3*a5*a6/3 - 25*a0*a2**2*a3*a5/27 - 9*a0*a2**2*a3*a6**2 + 31*a0*a2**2*a3*a6/12 - 5*a0*a2**2*a3/18 - 38*a0*a2**2*a4**2*a5/243 - 14*a0*a2**2*a4**2*a6/27 + 7*a0*a2**2*a4**2/27 + 10*a0*a2**2*a4*a5**2/81 + 31*a0*a2**2*a4*a5*a6/9 - 31*a0*a2**2*a4*a5/54 + 59*a0*a2*a3*a5*a6**2/27 - 85*a0*a2*a3*a5*a6/162 + 11*a0*a2*a3*a5/162 + 10*a0*a2*a3*a6**3 - 41*a0*a2*a3*a6**2/6 + 7*a0*a2*a3*a6/4 - 17*a0*a2*a3/108 + 20*a0*a2*a4**2*a6**2/81 - 61*a0*a2*a4**2*a6/243 + 4*a0*a2*a4**2/243 - 76*a0*a2*a4*a5**2*a6/243 + 2*a0*a2*a4*a5**2/27 - 17*a0*a2*a4*a5*a6**2/27 + 5*a0*a2*a4*a5*a6/9 - 11*a0*a2*a4*a5/81 + 7*a0*a2*a4*a6**3/3 - 8*a0*a2*a4*a6**2/3 + 25*a0*a2*a4*a6/54 - a0*a2*a4/54 + 8*a0*a2*a5**4/243 + 14*a0*a2*a5**3*a6/81 - 7*a0*a2*a5**3/81 + 31*a0*a2*a5**2*a6**2/18 - 41*a0*a2*a5**2*a6/108 + a0*a2*a5**2/36 + 44*a0*a3*a6**3/27 - 73*a0*a3*a6**2/81 + 23*a0*a3*a6/162 - a0*a3/162 + 2*a0*a4*a5*a6**3/9 - 103*a0*a4*a5*a6**2/243 + 26*a0*a4*a5*a6/243 - a0*a4*a5/162 + 2*a0*a4*a6**4/3 + 8*a0*a4*a6**3/27 - 17*a0*a4*a6**2/162 - a0*a4*a6/162 - 4*a0*a5**3*a6**2/81 + 31*a0*a5**3*a6/486 - a0*a5**3/243 - 29*a0*a5**2*a6**2/162 - a0*a5**2*a6/36 + 2*a0*a5*a6**4 - 13*a0*a5*a6**3/9 + 5*a0*a5*a6**2/36 + 5*a0*a5*a6/216 - a1**3*a3**2/9 - 2*a1**3*a3*a4*a5/9 - a1**3*a3*a4/9 - 2*a1**3*a3*a5**2/9 - a1**3*a3*a5*a6 + 4*a1**3*a4**3/81 + 2*a1**3*a4**2*a6/3 - a1**3*a4**2/9 - 2*a1**3*a4*a5**2/9 - 2*a1**2*a2**2*a3**2/9 - 2*a1**2*a2**2*a3*a4/9 + 13*a1**2*a2**2*a3*a5/6 - a1**2*a2**2*a4**2 - 28*a1**2*a2*a3*a4*a6/27 + 4*a1**2*a2*a3*a4/27 - 4*a1**2*a2*a3*a5**2/9 - 13*a1**2*a2*a3*a5*a6/3 + 7*a1**2*a2*a3*a5/6 - 12*a1**2*a2*a3*a6**2 + 3*a1**2*a2*a3*a6 + a1**2*a2*a3/4 + 14*a1**2*a2*a4**2*a5/81 + 14*a1**2*a2*a4**2*a6/27 - 8*a1**2*a2*a4**2/27 + a1**2*a2*a4*a5**2/27 + 4*a1**2*a2*a4*a5*a6/9 + a1**2*a2*a4*a5/9 - 2*a1**2*a2*a5**3/9 + 4*a1**2*a3*a5*a6**2/9 - 22*a1**2*a3*a5*a6/27 + 2*a1**2*a3*a5/27 + a1**2*a3*a6**2 - a1**2*a3*a6/2 + a1**2*a3/18 - 8*a1**2*a4**2*a6**2/27 + 8*a1**2*a4**2*a6/27 - a1**2*a4**2/27 + 2*a1**2*a4*a5**2*a6/27 - 2*a1**2*a4*a5**2/81 - 7*a1**2*a4*a5*a6/27 - 4*a1**2*a4*a6**3 + 3*a1**2*a4*a6**2 - 2*a1**2*a4*a6/3 + a1**2*a4/18 - a1**2*a5**4/81 - a1**2*a5**3*a6/27 - a1**2*a5**3/54 + a1**2*a5**2*a6**2 - 5*a1**2*a5**2*a6/6 + a1**2*a5**2/12 + 8*a1*a2**3*a3*a4/27 + 8*a1*a2**3*a3*a5/9 + 19*a1*a2**3*a3*a6 - 31*a1*a2**3*a3/12 - 4*a1*a2**3*a4*a5/3 - 20*a1*a2**2*a3*a5*a6/9 + 29*a1*a2**2*a3*a5/54 - 10*a1*a2**2*a3*a6**2 + 35*a1*a2**2*a3*a6/6 - 35*a1*a2**2*a3/36 + 4*a1*a2**2*a4**2*a6/27 - 5*a1*a2**2*a4**2/81 + 4*a1*a2**2*a4*a5**2/27 + 2*a1*a2**2*a4*a5*a6/9 - 11*a1*a2**2*a4*a5/27 + 6*a1*a2**2*a4*a6**2 - 17*a1*a2**2*a4*a6/6 + 19*a1*a2**2*a4/36 + 4*a1*a2**2*a5**3/27 - 4*a1*a2**2*a5**2*a6/3 + 3*a1*a2**2*a5**2/4 + 4*a1*a2*a3*a6**3/9 - 92*a1*a2*a3*a6**2/27 + 47*a1*a2*a3*a6/54 - a1*a2*a3/108 - 14*a1*a2*a4*a5*a6**2/81 + 25*a1*a2*a4*a5*a6/81 - 5*a1*a2*a4*a5/162 - 20*a1*a2*a4*a6**3/9 + 40*a1*a2*a4*a6**2/27 - 8*a1*a2*a4*a6/9 + 4*a1*a2*a4/27 + 2*a1*a2*a5**3*a6/81 - a1*a2*a5**3/162 + 16*a1*a2*a5**2*a6**2/27 - 47*a1*a2*a5**2*a6/54 + 13*a1*a2*a5**2/108 + 13*a1*a2*a5*a6**3/3 - 23*a1*a2*a5*a6**2/6 + 13*a1*a2*a5*a6/36 + a1*a2*a5/18 + 4*a1*a4*a6**4/9 - 34*a1*a4*a6**3/27 + 38*a1*a4*a6**2/81 - 2*a1*a4*a6/27 + a1*a4/162 - 4*a1*a5**2*a6**3/27 + 29*a1*a5**2*a6**2/81 - 2*a1*a5**2*a6/27 + a1*a5**2/162 - 5*a1*a5*a6**3/9 + a1*a5*a6**2/54 + a1*a5*a6/54 + 6*a1*a6**5 - 8*a1*a6**4 + 7*a1*a6**3/3 - a1*a6**2/12 - a1*a6/36 - 6*a2**5*a3 + 7*a2**4*a3*a5/9 + 4*a2**4*a3*a6 - 2*a2**4*a3 + a2**4*a4*a5/3 - 3*a2**4*a4*a6 + 5*a2**4*a4/4 - a2**4*a5**2/3 - 2*a2**3*a3*a6**2/9 + 14*a2**3*a3*a6/9 + a2**3*a3/36 + 20*a2**3*a4*a5*a6/81 - 11*a2**3*a4*a5/162 + 16*a2**3*a4*a6**2/9 - 29*a2**3*a4*a6/18 + 4*a2**3*a4/9 + 5*a2**3*a5**3/81 + 17*a2**3*a5**2*a6/27 - 17*a2**3*a5**2/54 - 9*a2**3*a5*a6**2/2 + 137*a2**3*a5*a6/36 - 5*a2**3*a5/72 - 4*a2**2*a4*a6**3/27 + 70*a2**2*a4*a6**2/81 - 11*a2**2*a4*a6/81 + a2**2*a4/54 + a2**2*a5**2*a6**2/3 - 7*a2**2*a5**2*a6/162 + a2**2*a5**2/162 + 23*a2**2*a5*a6**3/9 - 101*a2**2*a5*a6**2/27 + 137*a2**2*a5*a6/108 - 2*a2**2*a5/27 - 5*a2**2*a6**4 + 41*a2**2*a6**3/6 - 65*a2**2*a6**2/36 + 11*a2**2*a6/72 + 2*a2*a5*a6**4/9 + 8*a2*a5*a6**3/9 - 67*a2*a5*a6**2/162 + a2*a5*a6/18 - a2*a5/324 + 2*a2*a6**5 - 14*a2*a6**4/3 + 53*a2*a6**3/18 - 41*a2*a6**2/54 + 2*a2*a6/27 + 10*a6**5/9 - a6**4 + 55*a6**3/162 - 17*a6**2/324 + a6/324",
      "a0**2*a1*a3*a5**2/6 - a0**2*a1*a4**2*a5/18 - 2*a0**2*a2*a3**2*a5/27 + 4*a0**2*a2*a3*a4**2/243 - 2*a0**2*a2*a3*a4*a5/27 - 2*a0**2*a2*a3*a5**2/9 + 3*a0**2*a2*a3*a5*a6/2 + a0**2*a2*a3*a5/9 + 4*a0**2*a2*a4**3/243 + 5*a0**2*a2*a4**2*a5/81 - a0**2*a2*a4**2*a6/9 - 7*a0**2*a2*a4**2/54 - 4*a0**2*a2*a4*a5**2/27 + 8*a0**2*a3**2*a6/81 - 4*a0**2*a3**2/243 - 2*a0**2*a3*a4*a5*a6/243 - 17*a0**2*a3*a4*a5/729 + 8*a0**2*a3*a4*a6/81 - 4*a0**2*a3*a4/243 - 2*a0**2*a3*a5**3/81 - 2*a0**2*a3*a5**2*a6/9 - 7*a0**2*a3*a5**2/243 - 4*a0**2*a3*a5*a6**2/3 + 14*a0**2*a3*a5*a6/27 - a0**2*a3*a5/54 + 7*a0**2*a3*a6**2/6 - 13*a0**2*a3*a6/36 + a0**2*a3/36 + 8*a0**2*a4**3*a6/729 + 8*a0**2*a4**3/2187 + 10*a0**2*a4**2*a5**2/2187 + 8*a0**2*a4**2*a5*a6/81 - 2*a0**2*a4**2*a5/729 + 4*a0**2*a4**2*a6**2/27 - 4*a0**2*a4**2/243 - 8*a0**2*a4*a5**3/729 + 19*a0**2*a4*a5**2*a6/81 - 29*a0**2*a4*a5**2/486 + 11*a0**2*a4*a5*a6**2/18 - 49*a0**2*a4*a5*a6/108 + a0**2*a4*a5/18 - 4*a0**2*a5**4/81 - 2*a0**2*a5**3*a6/9 + 2*a0**2*a5**3/27 + 2*a0*a1**2*a3**2*a5/27 - 4*a0*a1**2*a3*a4**2/243 + 2*a0*a1**2*a3*a4*a5/27 + a0*a1**2*a3*a5**2/9 - a0*a1**2*a3*a5*a6/2 - a0*a1**2*a3*a5/2 - 4*a0*a1**2*a4**3/243 - 2*a0*a1**2*a4**2*a5/81 + 2*a0*a1**2*a4**2*a6/9 + a0*a1**2*a4**2/6 - 8*a0*a1*a2**2*a3*a5/3 + 4*a0*a1*a2**2*a4**2/9 + 8*a0*a1*a2*a3**2*a6/27 - 2*a0*a1*a2*a3**2/9 - 58*a0*a1*a2*a3*a4*a5/243 + 8*a0*a1*a2*a3*a4*a6/27 - 2*a0*a1*a2*a3*a4/9 - 4*a0*a1*a2*a3*a5**2/81 + 8*a0*a1*a2*a3*a5*a6/9 - a0*a1*a2*a3*a5/27 - 7*a0*a1*a2*a3*a6**2 + 5*a0*a1*a2*a3*a6/4 - a0*a1*a2*a3/3 + 32*a0*a1*a2*a4**3/729 - 22*a0*a1*a2*a4**2*a5/243 + 10*a0*a1*a2*a4**2*a6/27 - 16*a0*a1*a2*a4**2/81 - a0*a1*a2*a4*a5**2/3 + 13*a0*a1*a2*a4*a5*a6/18 - 4*a0*a1*a2*a5**3/9 - 20*a0*a1*a3*a4*a6**2/81 + 14*a0*a1*a3*a4*a6/243 + 4*a0*a1*a3*a4/243 - 22*a0*a1*a3*a5**2*a6/81 + 19*a0*a1*a3*a5**2/243 - 4*a0*a1*a3*a5*a6**2/3 + 4*a0*a1*a3*a5*a6/27 + 4*a0*a1*a3*a5/81 - 4*a0*a1*a3*a6**3 + 2*a0*a1*a3*a6**2 - a0*a1*a3*a6/9 - a0*a1*a3/27 + 64*a0*a1*a4**2*a5*a6/729 - 4*a0*a1*a4**2*a5/243 + 16*a0*a1*a4**2*a6**2/81 - 4*a0*a1*a4**2*a6/243 + 2*a0*a1*a4**2/243 - 2*a0*a1*a4*a5**2*a6/243 + a0*a1*a4*a5**2/27 + 28*a0*a1*a4*a5*a6**2/27 - 31*a0*a1*a4*a5*a6/81 + 5*a0*a1*a4*a5/162 - 2*a0*a1*a4*a6**3/3 - 4*a0*a1*a4*a6**2/9 + 2*a0*a1*a4*a6/9 - a0*a1*a4/36 - a0*a1*a5**3*a6/3 + 5*a0*a1*a5**3/54 - 5*a0*a1*a5**2*a6**2/6 + 7*a0*a1*a5**2*a6/9 - a0*a1*a5**2/6 - 4*a0*a2**3*a3**2/9 - 4*a0*a2**3*a3*a4/9 + 4*a0*a2**3*a3*a5/3 + 3*a0*a2**3*a3*a6 - 2*a0*a2**3*a3/3 - 8*a0*a2**3*a4**2/9 - 7*a0*a2**3*a4*a5/9 - 44*a0*a2**2*a3*a4*a6/81 + 20*a0*a2**2*a3*a4/243 - 28*a0*a2**2*a3*a5**2/81 - 20*a0*a2**2*a3*a5*a6/9 + 50*a0*a2**2*a3*a5/81 + 6*a0*a2**2*a3*a6**2 - 31*a0*a2**2*a3*a6/18 + 5*a0*a2**2*a3/27 + 76*a0*a2**2*a4**2*a5/729 + 28*a0*a2**2*a4**2*a6/81 - 14*a0*a2**2*a4**2/81 - 20*a0*a2**2*a4*a5**2/243 - 62*a0*a2**2*a4*a5*a6/27 + 31*a0*a2**2*a4*a5/81 + 5*a0*a2**2*a4*a6**2/3 - 11*a0*a2**2*a4*a6/9 + a0*a2**2*a4/18 - 17*a0*a2**2*a5**2*a6/9 + a0*a2**2*a5**2/2 - 118*a0*a2*a3*a5*a6**2/81 + 85*a0*a2*a3*a5*a6/243 - 11*a0*a2*a3*a5/243 - 20*a0*a2*a3*a6**3/3 + 41*a0*a2*a3*a6**2/9 - 7*a0*a2*a3*a6/6 + 17*a0*a2*a3/162 - 40*a0*a2*a4**2*a6**2/243 + 122*a0*a2*a4**2*a6/729 - 8*a0*a2*a4**2/729 + 152*a0*a2*a4*a5**2*a6/729 - 4*a0*a2*a4*a5**2/81 + 34*a0*a2*a4*a5*a6**2/81 - 10*a0*a2*a4*a5*a6/27 + 22*a0*a2*a4*a5/243 - 14*a0*a2*a4*a6**3/9 + 16*a0*a2*a4*a6**2/9 - 25*a0*a2*a4*a6/81 + a0*a2*a4/81 - 16*a0*a2*a5**4/729 - 28*a0*a2*a5**3*a6/243 + 14*a0*a2*a5**3/243 - 31*a0*a2*a5**2*a6**2/27 + 41*a0*a2*a5**2*a6/162 - a0*a2*a5**2/54 - 17*a0*a2*a5*a6**3/6 + 25*a0*a2*a5*a6**2/18 - 17*a0*a2*a5*a6/36 + a0*a2*a5/18 - 88*a0*a3*a6**3/81 + 146*a0*a3*a6**2/243 - 23*a0*a3*a6/243 + a0*a3/243 - 4*a0*a4*a5*a6**3/27 + 206*a0*a4*a5*a6**2/729 - 52*a0*a4*a5*a6/729 + a0*a4*a5/243 - 4*a0*a4*a6**4/9 - 16*a0*a4*a6**3/81 + 17*a0*a4*a6**2/243 + a0*a4*a6/243 + 8*a0*a5**3*a6**2/243 - 31*a0*a5**3*a6/729 + 2*a0*a5**3/729 + 29*a0*a5**2*a6**2/243 + a0*a5**2*a6/54 - 4*a0*a5*a6**4/3 + 26*a0*a5*a6**3/27 - 5*a0*a5*a6**2/54 - 5*a0*a5*a6/324 - 11*a0*a6**4/6 + 14*a0*a6**3/9 - 11*a0*a6**2/24 + a0*a6/24 + 3*a1**3*a2*a3*a5/2 - a1**3*a2*a4**2/3 + 2*a1**3*a3**2/27 + 4*a1**3*a3*a4*a5/27 + 2*a1**3*a3*a4/27 + 4*a1**3*a3*a5**2/27 + 2*a1**3*a3*a5*a6/3 - a1**3*a3*a6 + a1**3*a3/2 - 8*a1**3*a4**3/243 - 4*a1**3*a4**2*a6/9 + 2*a1**3*a4**2/27 + 4*a1**3*a4*a5**2/27 + a1**3*a4*a5/6 + a1**3*a5**3/6 + 4*a1**2*a2**2*a3**2/27 + 4*a1**2*a2**2*a3*a4/27 - 13*a1**2*a2**2*a3*a5/9 + 4*a1**2*a2**2*a3*a6 + a1**2*a2**2*a3/4 + 2*a1**2*a2**2*a4**2/3 + 56*a1**2*a2*a3*a4*a6/81 - 8*a1**2*a2*a3*a4/81 + 8*a1**2*a2*a3*a5**2/27 + 26*a1**2*a2*a3*a5*a6/9 - 7*a1**2*a2*a3*a5/9 + 8*a1**2*a2*a3*a6**2 - 2*a1**2*a2*a3*a6 - a1**2*a2*a3/6 - 28*a1**2*a2*a4**2*a5/243 - 28*a1**2*a2*a4**2*a6/81 + 16*a1**2*a2*a4**2/81 - 2*a1**2*a2*a4*a5**2/81 - 8*a1**2*a2*a4*a5*a6/27 - 2*a1**2*a2*a4*a5/27 + 2*a1**2*a2*a4*a6**2/3 + a1**2*a2*a4*a6/2 + 4*a1**2*a2*a5**3/27 + 7*a1**2*a2*a5**2*a6/6 - a1**2*a2*a5**2/12 - 8*a1**2*a3*a5*a6**2/27 + 44*a1**2*a3*a5*a6/81 - 4*a1**2*a3*a5/81 - 2*a1**2*a3*a6**2/3 + a1**2*a3*a6/3 - a1**2*a3/27 + 16*a1**2*a4**2*a6**2/81 - 16*a1**2*a4**2*a6/81 + 2*a1**2*a4**2/81 - 4*a1**2*a4*a5**2*a6/81 + 4*a1**2*a4*a5**2/243 + 14*a1**2*a4*a5*a6/81 + 8*a1**2*a4*a6**3/3 - 2*a1**2*a4*a6**2 + 4*a1**2*a4*a6/9 - a1**2*a4/27 + 2*a1**2*a5**4/243 + 2*a1**2*a5**3*a6/81 + a1**2*a5**3/81 - 2*a1**2*a5**2*a6**2/3 + 5*a1**2*a5**2*a6/9 - a1**2*a5**2/18 + 3*a1**2*a5*a6**2/2 - 11*a1**2*a5*a6/12 + a1**2*a5/12 - 2*a1*a2**4*a3 - 16*a1*a2**3*a3*a4/81 - 16*a1*a2**3*a3*a5/27 - 38*a1*a2**3*a3*a6/3 + 31*a1*a2**3*a3/18 + 8*a1*a2**3*a4*a5/9 - a1*a2**3*a4*a6 + 5*a1*a2**3*a4/12 - a1*a2**3*a5**2/6 + 40*a1*a2**2*a3*a5*a6/27 - 29*a1*a2**2*a3*a5/81 + 20*a1*a2**2*a3*a6**2/3 - 35*a1*a2**2*a3*a6/9 + 35*a1*a2**2*a3/54 - 8*a1*a2**2*a4**2*a6/81 + 10*a1*a2**2*a4**2/243 - 8*a1*a2**2*a4*a5**2/81 - 4*a1*a2**2*a4*a5*a6/27 + 22*a1*a2**2*a4*a5/81 - 4*a1*a2**2*a4*a6**2 + 17*a1*a2**2*a4*a6/9 - 19*a1*a2**2*a4/54 - 8*a1*a2**2*a5**3/81 + 8*a1*a2**2*a5**2*a6/9 - a1*a2**2*a5**2/2 + 13*a1*a2**2*a5*a6**2/6 - 7*a1*a2**2*a5*a6/12 + a1*a2**2*a5/4 - 8*a1*a2*a3*a6**3/27 + 184*a1*a2*a3*a6**2/81 - 47*a1*a2*a3*a6/81 + a1*a2*a3/162 + 28*a1*a2*a4*a5*a6**2/243 - 50*a1*a2*a4*a5*a6/243 + 5*a1*a2*a4*a5/243 + 40*a1*a2*a4*a6**3/27 - 80*a1*a2*a4*a6**2/81 + 16*a1*a2*a4*a6/27 - 8*a1*a2*a4/81 - 4*a1*a2*a5**3*a6/243 + a1*a2*a5**3/243 - 32*a1*a2*a5**2*a6**2/81 + 47*a1*a2*a5**2*a6/81 - 13*a1*a2*a5**2/162 - 26*a1*a2*a5*a6**3/9 + 23*a1*a2*a5*a6**2/9 - 13*a1*a2*a5*a6/54 - a1*a2*a5/27 + a1*a2*a6**4 + 17*a1*a2*a6**3/6 - 3*a1*a2*a6**2 + 5*a1*a2*a6/12 + a1*a2/24 - 8*a1*a4*a6**4/27 + 68*a1*a4*a6**3/81 - 76*a1*a4*a6**2/243 + 4*a1*a4*a6/81 - a1*a4/243 + 8*a1*a5**2*a6**3/81 - 58*a1*a5**2*a6**2/243 + 4*a1*a5**2*a6/81 - a1*a5**2/243 + 10*a1*a5*a6**3/27 - a1*a5*a6**2/81 - a1*a5*a6/81 - 4*a1*a6**5 + 16*a1*a6**4/3 - 14*a1*a6**3/9 + a1*a6**2/18 + a1*a6/54 + 4*a2**5*a3 - 14*a2**4*a3*a5/27 - 8*a2**4*a3*a6/3 + 4*a2**4*a3/3 - 2*a2**4*a4*a5/9 + 2*a2**4*a4*a6 - 5*a2**4*a4/6 + 2*a2**4*a5**2/9 - 7*a2**4*a5*a6/6 + a2**4*a5/3 + 4*a2**3*a3*a6**2/27 - 28*a2**3*a3*a6/27 - a2**3*a3/54 - 40*a2**3*a4*a5*a6/243 + 11*a2**3*a4*a5/243 - 32*a2**3*a4*a6**2/27 + 29*a2**3*a4*a6/27 - 8*a2**3*a4/27 - 10*a2**3*a5**3/243 - 34*a2**3*a5**2*a6/81 + 17*a2**3*a5**2/81 + 3*a2**3*a5*a6**2 - 137*a2**3*a5*a6/54 + 5*a2**3*a5/108 - a2**3*a6**3 - a2**3*a6**2/3 + 19*a2**3*a6/24 + a2**3/8 + 8*a2**2*a4*a6**3/81 - 140*a2**2*a4*a6**2/243 + 22*a2**2*a4*a6/243 - a2**2*a4/81 - 2*a2**2*a5**2*a6**2/9 + 7*a2**2*a5**2*a6/243 - a2**2*a5**2/243 - 46*a2**2*a5*a6**3/27 + 202*a2**2*a5*a6**2/81 - 137*a2**2*a5*a6/162 + 4*a2**2*a5/81 + 10*a2**2*a6**4/3 - 41*a2**2*a6**3/9 + 65*a2**2*a6**2/54 - 11*a2**2*a6/108 - 4*a2*a5*a6**4/27 - 16*a2*a5*a6**3/27 + 67*a2*a5*a6**2/243 - a2*a5*a6/27 + a2*a5/486 - 4*a2*a6**5/3 + 28*a2*a6**4/9 - 53*a2*a6**3/27 + 41*a2*a6**2/81 - 4*a2*a6/81 - 20*a6**5/27 + 2*a6**4/3 - 55*a6**3/243 + 17*a6**2/486 - a6/486",
      "a0**3*a3*a5**2/6 - a0**3*a4**2*a5/18 - a0**2*a1*a3*a5**2/9 + a0**2*a1*a3*a5*a6 - 7*a0**2*a1*a3*a5/18 + a0**2*a1*a4**2*a5/27 + a0**2*a1*a4**2*a6/9 + a0**2*a1*a4**2/27 - 4*a0**2*a1*a4*a5**2/27 - 7*a0**2*a2**2*a3*a5/2 + 13*a0**2*a2**2*a4**2/9 + 4*a0**2*a2*a3**2*a5/81 - 8*a0**2*a2*a3*a4**2/729 + 4*a0**2*a2*a3*a4*a5/81 + 4*a0**2*a2*a3*a5**2/27 - a0**2*a2*a3*a5*a6 - 2*a0**2*a2*a3*a5/27 - 15*a0**2*a2*a3*a6**2 + 77*a0**2*a2*a3*a6/12 - 25*a0**2*a2*a3/36 - 8*a0**2*a2*a4**3/729 - 10*a0**2*a2*a4**2*a5/243 + 2*a0**2*a2*a4**2*a6/27 + 7*a0**2*a2*a4**2/81 + 8*a0**2*a2*a4*a5**2/81 + 77*a0**2*a2*a4*a5*a6/18 - 91*a0**2*a2*a4*a5/108 - 2*a0**2*a2*a5**3/3 - 16*a0**2*a3**2*a6/243 + 8*a0**2*a3**2/729 + 4*a0**2*a3*a4*a5*a6/729 + 34*a0**2*a3*a4*a5/2187 - 16*a0**2*a3*a4*a6/243 + 8*a0**2*a3*a4/729 + 4*a0**2*a3*a5**3/243 + 4*a0**2*a3*a5**2*a6/27 + 14*a0**2*a3*a5**2/729 + 8*a0**2*a3*a5*a6**2/9 - 28*a0**2*a3*a5*a6/81 + a0**2*a3*a5/81 - 7*a0**2*a3*a6**2/9 + 13*a0**2*a3*a6/54 - a0**2*a3/54 - 16*a0**2*a4**3*a6/2187 - 16*a0**2*a4**3/6561 - 20*a0**2*a4**2*a5**2/6561 - 16*a0**2*a4**2*a5*a6/243 + 4*a0**2*a4**2*a5/2187 - 8*a0**2*a4**2*a6**2/81 + 8*a0**2*a4**2/729 + 16*a0**2*a4*a5**3/2187 - 38*a0**2*a4*a5**2*a6/243 + 29*a0**2*a4*a5**2/729 - 11*a0**2*a4*a5*a6**2/27 + 49*a0**2*a4*a5*a6/162 - a0**2*a4*a5/27 - a0**2*a4*a6**3 - a0**2*a4*a6**2/6 - a0**2*a4*a6/9 + a0**2*a4/54 + 8*a0**2*a5**4/243 + 4*a0**2*a5**3*a6/27 - 4*a0**2*a5**3/81 + 2*a0**2*a5**2*a6**2/3 + a0**2*a5**2*a6/36 + a0**2*a5**2/54 + 10*a0*a1**2*a2*a3*a5/3 - 2*a0*a1**2*a2*a4**2 - 4*a0*a1**2*a3**2*a5/81 + 8*a0*a1**2*a3*a4**2/729 - 4*a0*a1**2*a3*a4*a5/81 - 2*a0*a1**2*a3*a5**2/27 + a0*a1**2*a3*a5*a6/3 + a0*a1**2*a3*a5/3 + 6*a0*a1**2*a3*a6**2 - 7*a0*a1**2*a3*a6/2 + a0*a1**2*a3/2 + 8*a0*a1**2*a4**3/729 + 4*a0*a1**2*a4**2*a5/243 - 4*a0*a1**2*a4**2*a6/27 - a0*a1**2*a4**2/9 - 19*a0*a1**2*a4*a5*a6/9 + 5*a0*a1**2*a4*a5/9 + a0*a1**2*a5**3/6 + 16*a0*a1*a2**2*a3*a5/9 + 23*a0*a1*a2**2*a3*a6 - 59*a0*a1*a2**2*a3/12 - 8*a0*a1*a2**2*a4**2/27 - 65*a0*a1*a2**2*a4*a5/18 - 16*a0*a1*a2*a3**2*a6/81 + 4*a0*a1*a2*a3**2/27 + 116*a0*a1*a2*a3*a4*a5/729 - 16*a0*a1*a2*a3*a4*a6/81 + 4*a0*a1*a2*a3*a4/27 + 8*a0*a1*a2*a3*a5**2/243 - 16*a0*a1*a2*a3*a5*a6/27 + 2*a0*a1*a2*a3*a5/81 + 14*a0*a1*a2*a3*a6**2/3 - 5*a0*a1*a2*a3*a6/6 + 2*a0*a1*a2*a3/9 - 64*a0*a1*a2*a4**3/2187 + 44*a0*a1*a2*a4**2*a5/729 - 20*a0*a1*a2*a4**2*a6/81 + 32*a0*a1*a2*a4**2/243 + 2*a0*a1*a2*a4*a5**2/9 - 13*a0*a1*a2*a4*a5*a6/27 + 23*a0*a1*a2*a4*a6**2/3 - 4*a0*a1*a2*a4*a6 + 11*a0*a1*a2*a4/12 + 8*a0*a1*a2*a5**3/27 - 43*a0*a1*a2*a5**2*a6/18 + 11*a0*a1*a2*a5**2/9 + 40*a0*a1*a3*a4*a6**2/243 - 28*a0*a1*a3*a4*a6/729 - 8*a0*a1*a3*a4/729 + 44*a0*a1*a3*a5**2*a6/243 - 38*a0*a1*a3*a5**2/729 + 8*a0*a1*a3*a5*a6**2/9 - 8*a0*a1*a3*a5*a6/81 - 8*a0*a1*a3*a5/243 + 8*a0*a1*a3*a6**3/3 - 4*a0*a1*a3*a6**2/3 + 2*a0*a1*a3*a6/27 + 2*a0*a1*a3/81 - 128*a0*a1*a4**2*a5*a6/2187 + 8*a0*a1*a4**2*a5/729 - 32*a0*a1*a4**2*a6**2/243 + 8*a0*a1*a4**2*a6/729 - 4*a0*a1*a4**2/729 + 4*a0*a1*a4*a5**2*a6/729 - 2*a0*a1*a4*a5**2/81 - 56*a0*a1*a4*a5*a6**2/81 + 62*a0*a1*a4*a5*a6/243 - 5*a0*a1*a4*a5/243 + 4*a0*a1*a4*a6**3/9 + 8*a0*a1*a4*a6**2/27 - 4*a0*a1*a4*a6/27 + a0*a1*a4/54 + 2*a0*a1*a5**3*a6/9 - 5*a0*a1*a5**3/81 + 5*a0*a1*a5**2*a6**2/9 - 14*a0*a1*a5**2*a6/27 + a0*a1*a5**2/9 + 4*a0*a1*a5*a6**3 - 31*a0*a1*a5*a6**2/18 - 5*a0*a1*a5*a6/36 - a0*a1*a5/18 - 9*a0*a2**4*a3 + 8*a0*a2**3*a3**2/27 + 8*a0*a2**3*a3*a4/27 - 8*a0*a2**3*a3*a5/9 - 2*a0*a2**3*a3*a6 + 4*a0*a2**3*a3/9 + 16*a0*a2**3*a4**2/27 + 14*a0*a2**3*a4*a5/27 - 14*a0*a2**3*a4*a6/3 + 25*a0*a2**3*a4/12 - 13*a0*a2**3*a5**2/6 + 88*a0*a2**2*a3*a4*a6/243 - 40*a0*a2**2*a3*a4/729 + 56*a0*a2**2*a3*a5**2/243 + 40*a0*a2**2*a3*a5*a6/27 - 100*a0*a2**2*a3*a5/243 - 4*a0*a2**2*a3*a6**2 + 31*a0*a2**2*a3*a6/27 - 10*a0*a2**2*a3/81 - 152*a0*a2**2*a4**2*a5/2187 - 56*a0*a2**2*a4**2*a6/243 + 28*a0*a2**2*a4**2/243 + 40*a0*a2**2*a4*a5**2/729 + 124*a0*a2**2*a4*a5*a6/81 - 62*a0*a2**2*a4*a5/243 - 10*a0*a2**2*a4*a6**2/9 + 22*a0*a2**2*a4*a6/27 - a0*a2**2*a4/27 + 34*a0*a2**2*a5**2*a6/27 - a0*a2**2*a5**2/3 - 28*a0*a2**2*a5*a6**2/3 + 241*a0*a2**2*a5*a6/36 - 13*a0*a2**2*a5/18 + 236*a0*a2*a3*a5*a6**2/243 - 170*a0*a2*a3*a5*a6/729 + 22*a0*a2*a3*a5/729 + 40*a0*a2*a3*a6**3/9 - 82*a0*a2*a3*a6**2/27 + 7*a0*a2*a3*a6/9 - 17*a0*a2*a3/243 + 80*a0*a2*a4**2*a6**2/729 - 244*a0*a2*a4**2*a6/2187 + 16*a0*a2*a4**2/2187 - 304*a0*a2*a4*a5**2*a6/2187 + 8*a0*a2*a4*a5**2/243 - 68*a0*a2*a4*a5*a6**2/243 + 20*a0*a2*a4*a5*a6/81 - 44*a0*a2*a4*a5/729 + 28*a0*a2*a4*a6**3/27 - 32*a0*a2*a4*a6**2/27 + 50*a0*a2*a4*a6/243 - 2*a0*a2*a4/243 + 32*a0*a2*a5**4/2187 + 56*a0*a2*a5**3*a6/729 - 28*a0*a2*a5**3/729 + 62*a0*a2*a5**2*a6**2/81 - 41*a0*a2*a5**2*a6/243 + a0*a2*a5**2/81 + 17*a0*a2*a5*a6**3/9 - 25*a0*a2*a5*a6**2/27 + 17*a0*a2*a5*a6/54 - a0*a2*a5/27 - 3*a0*a2*a6**4 + 37*a0*a2*a6**3/6 - 31*a0*a2*a6**2/9 + 13*a0*a2*a6/24 - a0*a2/72 + 176*a0*a3*a6**3/243 - 292*a0*a3*a6**2/729 + 46*a0*a3*a6/729 - 2*a0*a3/729 + 8*a0*a4*a5*a6**3/81 - 412*a0*a4*a5*a6**2/2187 + 104*a0*a4*a5*a6/2187 - 2*a0*a4*a5/729 + 8*a0*a4*a6**4/27 + 32*a0*a4*a6**3/243 - 34*a0*a4*a6**2/729 - 2*a0*a4*a6/729 - 16*a0*a5**3*a6**2/729 + 62*a0*a5**3*a6/2187 - 4*a0*a5**3/2187 - 58*a0*a5**2*a6**2/729 - a0*a5**2*a6/81 + 8*a0*a5*a6**4/9 - 52*a0*a5*a6**3/81 + 5*a0*a5*a6**2/81 + 5*a0*a5*a6/486 + 11*a0*a6**4/9 - 28*a0*a6**3/27 + 11*a0*a6**2/36 - a0*a6/36 - a1**4*a3*a5 + 2*a1**4*a4**2/3 - a1**3*a2*a3*a5 - 12*a1**3*a2*a3*a6 + 3*a1**3*a2*a3 + 2*a1**3*a2*a4**2/9 + 2*a1**3*a2*a4*a5 - 4*a1**3*a3**2/81 - 8*a1**3*a3*a4*a5/81 - 4*a1**3*a3*a4/81 - 8*a1**3*a3*a5**2/81 - 4*a1**3*a3*a5*a6/9 + 2*a1**3*a3*a6/3 - a1**3*a3/3 + 16*a1**3*a4**3/729 + 8*a1**3*a4**2*a6/27 - 4*a1**3*a4**2/81 - 8*a1**3*a4*a5**2/81 - a1**3*a4*a5/9 - 4*a1**3*a4*a6**2 + 7*a1**3*a4*a6/3 - a1**3*a4/2 - a1**3*a5**3/9 + a1**3*a5**2*a6/3 - a1**3*a5**2/3 + 5*a1**2*a2**3*a3 - 8*a1**2*a2**2*a3**2/81 - 8*a1**2*a2**2*a3*a4/81 + 26*a1**2*a2**2*a3*a5/27 - 8*a1**2*a2**2*a3*a6/3 - a1**2*a2**2*a3/6 - 4*a1**2*a2**2*a4**2/9 + 8*a1**2*a2**2*a4*a6/3 - a1**2*a2**2*a4 + 11*a1**2*a2**2*a5**2/6 - 112*a1**2*a2*a3*a4*a6/243 + 16*a1**2*a2*a3*a4/243 - 16*a1**2*a2*a3*a5**2/81 - 52*a1**2*a2*a3*a5*a6/27 + 14*a1**2*a2*a3*a5/27 - 16*a1**2*a2*a3*a6**2/3 + 4*a1**2*a2*a3*a6/3 + a1**2*a2*a3/9 + 56*a1**2*a2*a4**2*a5/729 + 56*a1**2*a2*a4**2*a6/243 - 32*a1**2*a2*a4**2/243 + 4*a1**2*a2*a4*a5**2/243 + 16*a1**2*a2*a4*a5*a6/81 + 4*a1**2*a2*a4*a5/81 - 4*a1**2*a2*a4*a6**2/9 - a1**2*a2*a4*a6/3 - 8*a1**2*a2*a5**3/81 - 7*a1**2*a2*a5**2*a6/9 + a1**2*a2*a5**2/18 - a1**2*a2*a5*a6**2/3 - 5*a1**2*a2*a5*a6/6 + a1**2*a2*a5/12 + 16*a1**2*a3*a5*a6**2/81 - 88*a1**2*a3*a5*a6/243 + 8*a1**2*a3*a5/243 + 4*a1**2*a3*a6**2/9 - 2*a1**2*a3*a6/9 + 2*a1**2*a3/81 - 32*a1**2*a4**2*a6**2/243 + 32*a1**2*a4**2*a6/243 - 4*a1**2*a4**2/243 + 8*a1**2*a4*a5**2*a6/243 - 8*a1**2*a4*a5**2/729 - 28*a1**2*a4*a5*a6/243 - 16*a1**2*a4*a6**3/9 + 4*a1**2*a4*a6**2/3 - 8*a1**2*a4*a6/27 + 2*a1**2*a4/81 - 4*a1**2*a5**4/729 - 4*a1**2*a5**3*a6/243 - 2*a1**2*a5**3/243 + 4*a1**2*a5**2*a6**2/9 - 10*a1**2*a5**2*a6/27 + a1**2*a5**2/27 - a1**2*a5*a6**2 + 11*a1**2*a5*a6/18 - a1**2*a5/18 + 6*a1**2*a6**4 - 7*a1**2*a6**3 + 11*a1**2*a6**2/6 - 5*a1**2*a6/12 + a1**2/12 + 4*a1*a2**4*a3/3 + 32*a1*a2**3*a3*a4/243 + 32*a1*a2**3*a3*a5/81 + 76*a1*a2**3*a3*a6/9 - 31*a1*a2**3*a3/27 - 16*a1*a2**3*a4*a5/27 + 2*a1*a2**3*a4*a6/3 - 5*a1*a2**3*a4/18 + a1*a2**3*a5**2/9 + 16*a1*a2**3*a5*a6/3 - 7*a1*a2**3*a5/6 - 80*a1*a2**2*a3*a5*a6/81 + 58*a1*a2**2*a3*a5/243 - 40*a1*a2**2*a3*a6**2/9 + 70*a1*a2**2*a3*a6/27 - 35*a1*a2**2*a3/81 + 16*a1*a2**2*a4**2*a6/243 - 20*a1*a2**2*a4**2/729 + 16*a1*a2**2*a4*a5**2/243 + 8*a1*a2**2*a4*a5*a6/81 - 44*a1*a2**2*a4*a5/243 + 8*a1*a2**2*a4*a6**2/3 - 34*a1*a2**2*a4*a6/27 + 19*a1*a2**2*a4/81 + 16*a1*a2**2*a5**3/243 - 16*a1*a2**2*a5**2*a6/27 + a1*a2**2*a5**2/3 - 13*a1*a2**2*a5*a6**2/9 + 7*a1*a2**2*a5*a6/18 - a1*a2**2*a5/6 - 4*a1*a2**2*a6**3 + 4*a1*a2**2*a6**2 - a1*a2**2*a6/12 + a1*a2**2/6 + 16*a1*a2*a3*a6**3/81 - 368*a1*a2*a3*a6**2/243 + 94*a1*a2*a3*a6/243 - a1*a2*a3/243 - 56*a1*a2*a4*a5*a6**2/729 + 100*a1*a2*a4*a5*a6/729 - 10*a1*a2*a4*a5/729 - 80*a1*a2*a4*a6**3/81 + 160*a1*a2*a4*a6**2/243 - 32*a1*a2*a4*a6/81 + 16*a1*a2*a4/243 + 8*a1*a2*a5**3*a6/729 - 2*a1*a2*a5**3/729 + 64*a1*a2*a5**2*a6**2/243 - 94*a1*a2*a5**2*a6/243 + 13*a1*a2*a5**2/243 + 52*a1*a2*a5*a6**3/27 - 46*a1*a2*a5*a6**2/27 + 13*a1*a2*a5*a6/81 + 2*a1*a2*a5/81 - 2*a1*a2*a6**4/3 - 17*a1*a2*a6**3/9 + 2*a1*a2*a6**2 - 5*a1*a2*a6/18 - a1*a2/36 + 16*a1*a4*a6**4/81 - 136*a1*a4*a6**3/243 + 152*a1*a4*a6**2/729 - 8*a1*a4*a6/243 + 2*a1*a4/729 - 16*a1*a5**2*a6**3/243 + 116*a1*a5**2*a6**2/729 - 8*a1*a5**2*a6/243 + 2*a1*a5**2/729 - 20*a1*a5*a6**3/81 + 2*a1*a5*a6**2/243 + 2*a1*a5*a6/243 + 8*a1*a6**5/3 - 32*a1*a6**4/9 + 28*a1*a6**3/27 - a1*a6**2/27 - a1*a6/81 - 8*a2**5*a3/3 - 3*a2**5*a5/2 + 28*a2**4*a3*a5/81 + 16*a2**4*a3*a6/9 - 8*a2**4*a3/9 + 4*a2**4*a4*a5/27 - 4*a2**4*a4*a6/3 + 5*a2**4*a4/9 - 4*a2**4*a5**2/27 + 7*a2**4*a5*a6/9 - 2*a2**4*a5/9 + a2**4*a6**2 - a2**4*a6 - a2**4/8 - 8*a2**3*a3*a6**2/81 + 56*a2**3*a3*a6/81 + a2**3*a3/81 + 80*a2**3*a4*a5*a6/729 - 22*a2**3*a4*a5/729 + 64*a2**3*a4*a6**2/81 - 58*a2**3*a4*a6/81 + 16*a2**3*a4/81 + 20*a2**3*a5**3/729 + 68*a2**3*a5**2*a6/243 - 34*a2**3*a5**2/243 - 2*a2**3*a5*a6**2 + 137*a2**3*a5*a6/81 - 5*a2**3*a5/162 + 2*a2**3*a6**3/3 + 2*a2**3*a6**2/9 - 19*a2**3*a6/36 - a2**3/12 - 16*a2**2*a4*a6**3/243 + 280*a2**2*a4*a6**2/729 - 44*a2**2*a4*a6/729 + 2*a2**2*a4/243 + 4*a2**2*a5**2*a6**2/27 - 14*a2**2*a5**2*a6/729 + 2*a2**2*a5**2/729 + 92*a2**2*a5*a6**3/81 - 404*a2**2*a5*a6**2/243 + 137*a2**2*a5*a6/243 - 8*a2**2*a5/243 - 20*a2**2*a6**4/9 + 82*a2**2*a6**3/27 - 65*a2**2*a6**2/81 + 11*a2**2*a6/162 + 8*a2*a5*a6**4/81 + 32*a2*a5*a6**3/81 - 134*a2*a5*a6**2/729 + 2*a2*a5*a6/81 - a2*a5/729 + 8*a2*a6**5/9 - 56*a2*a6**4/27 + 106*a2*a6**3/81 - 82*a2*a6**2/243 + 8*a2*a6/243 + 40*a6**5/81 - 4*a6**4/9 + 110*a6**3/729 - 17*a6**2/729 + a6/729"
    &#93;,
    &#91;
      "-a0**2*a2*a3**2*a4/18 - a0**2*a2*a3*a4**2/18 + a0**2*a3*a4**2*a6/54 + a0**2*a3*a4**2/324 - 7*a0**2*a3*a4*a5**2/162 - 5*a0**2*a3*a4*a5*a6/18 + a0**2*a3*a4*a5/108 + 5*a0**2*a4**3*a5/486 + a0**2*a4**3*a6/9 - a0**2*a4**2*a5**2/81 + a0*a1**2*a3**2*a4/18 + a0*a1**2*a3*a4**2/18 - 7*a0*a1*a2*a3*a4**2/54 + 7*a0*a1*a2*a3*a4*a5/9 - 7*a0*a1*a2*a4**3/18 + 2*a0*a1*a3**2*a6**2/3 - 7*a0*a1*a3**2*a6/18 + 5*a0*a1*a3**2/108 - 29*a0*a1*a3*a4*a5*a6/54 + 31*a0*a1*a3*a4*a5/108 + 2*a0*a1*a3*a4*a6**2/3 - 5*a0*a1*a3*a4*a6/9 + 11*a0*a1*a3*a4/108 - 2*a0*a1*a3*a5**3/27 - 7*a0*a1*a3*a5**2*a6/9 + 7*a0*a1*a3*a5**2/54 + 5*a0*a1*a4**3*a6/81 - 11*a0*a1*a4**3/243 + a0*a1*a4**2*a5**2/27 - 5*a0*a1*a4**2*a5*a6/54 + 41*a0*a1*a4**2*a5/324 + a0*a1*a4*a5**3/27 - a0*a2**2*a3**2*a6/6 + 7*a0*a2**2*a3**2/36 - a0*a2**2*a3*a4*a5/3 + 5*a0*a2**2*a3*a4*a6/6 - 5*a0*a2**2*a3*a4/36 + 8*a0*a2**2*a3*a5**2/9 + a0*a2**2*a4**3/81 - 19*a0*a2**2*a4**2*a5/27 - 10*a0*a2*a3*a4*a6**2/9 + 55*a0*a2*a3*a4*a6/54 - 55*a0*a2*a3*a4/324 - 16*a0*a2*a3*a5**2*a6/27 + 2*a0*a2*a3*a5**2/81 + 11*a0*a2*a3*a5*a6**2/6 - 13*a0*a2*a3*a5*a6/6 + 115*a0*a2*a3*a5/216 + 5*a0*a2*a4**2*a5*a6/162 + 7*a0*a2*a4**2*a5/486 - 13*a0*a2*a4**2*a6**2/18 + 95*a0*a2*a4**2*a6/108 - 7*a0*a2*a4**2/36 + a0*a2*a4*a5**3/27 - 17*a0*a2*a4*a5**2*a6/18 + 91*a0*a2*a4*a5**2/324 + 4*a0*a2*a5**4/27 - a0*a3*a5*a6**3 + 11*a0*a3*a5*a6**2/27 - 17*a0*a3*a5*a6/648 + a0*a3*a5/432 + 3*a0*a3*a6**4/2 - 5*a0*a3*a6**3 + 7*a0*a3*a6**2/2 - 133*a0*a3*a6/144 + 37*a0*a3/432 - 7*a0*a4**2*a6**3/27 + 49*a0*a4**2*a6**2/162 - 73*a0*a4**2*a6/972 + 5*a0*a4**2/972 + 4*a0*a4*a5**2*a6**2/27 - 13*a0*a4*a5**2*a6/972 - 23*a0*a4*a5**2/1944 - 29*a0*a4*a5*a6**3/18 + 113*a0*a4*a5*a6**2/54 - 65*a0*a4*a5*a6/81 + 17*a0*a4*a5/162 - a0*a5**4*a6/162 - 13*a0*a5**4/972 + 5*a0*a5**3*a6**2/18 - 22*a0*a5**3*a6/81 + 41*a0*a5**3/648 + a1**3*a3*a4**2/9 - a1**3*a3*a4*a5/3 + 2*a1**3*a4**3/9 - a1**2*a2*a3**2*a6 + a1**2*a2*a3**2/6 + a1**2*a2*a3*a4*a5/2 - 3*a1**2*a2*a3*a4*a6/2 + 5*a1**2*a2*a3*a4/12 + a1**2*a2*a3*a5**2/9 - a1**2*a2*a4**3/81 + 13*a1**2*a2*a4**2*a5/27 - 5*a1**2*a3*a4*a6**2/9 + 14*a1**2*a3*a4*a6/27 - 7*a1**2*a3*a4/54 - 7*a1**2*a3*a5**2*a6/18 + 55*a1**2*a3*a5**2/108 - 3*a1**2*a3*a5*a6**2 + 17*a1**2*a3*a5*a6/6 - 5*a1**2*a3*a5/9 + 4*a1**2*a4**2*a5*a6/27 - a1**2*a4**2*a5/6 - 2*a1**2*a4**2*a6**2/9 - 7*a1**2*a4**2*a6/27 + a1**2*a4**2/12 + a1**2*a4*a5**3/54 + 4*a1**2*a4*a5**2*a6/9 - a1**2*a4*a5**2/54 + a1*a2**3*a3**2/2 + a1*a2**3*a3*a4/2 + 8*a1*a2**2*a3*a4*a6/9 - 5*a1*a2**2*a3*a4/9 + 14*a1*a2**2*a3*a5**2/27 + 13*a1*a2**2*a3*a5*a6/6 - 5*a1*a2**2*a3*a5/12 + a1*a2**2*a4**2*a5/162 + a1*a2**2*a4**2*a6/2 - a1*a2**2*a4**2/4 + 23*a1*a2**2*a4*a5**2/54 - 23*a1*a2*a3*a5*a6**2/18 + 121*a1*a2*a3*a5*a6/36 - 61*a1*a2*a3*a5/72 - 9*a1*a2*a3*a6**3/2 + 11*a1*a2*a3*a6**2 - 29*a1*a2*a3*a6/6 + 29*a1*a2*a3/48 + 7*a1*a2*a4**2*a6**2/27 - 20*a1*a2*a4**2*a6/81 + a1*a2*a4**2/36 + 11*a1*a2*a4*a5**2*a6/81 - 85*a1*a2*a4*a5**2/324 + a1*a2*a4*a5*a6**2/3 - 29*a1*a2*a4*a5*a6/108 + a1*a2*a4*a5/24 + 7*a1*a2*a5**4/162 + 37*a1*a2*a5**3*a6/54 - 19*a1*a2*a5**3/108 - 4*a1*a3*a6**4/3 + 17*a1*a3*a6**3/6 - 56*a1*a3*a6**2/27 + 73*a1*a3*a6/108 - 35*a1*a3/432 - 4*a1*a4*a5*a6**3/27 + 77*a1*a4*a5*a6**2/162 - 17*a1*a4*a5*a6/162 + a1*a4*a5/648 - 10*a1*a4*a6**4/3 + 20*a1*a4*a6**3/3 - 211*a1*a4*a6**2/54 + a1*a4*a6 - 7*a1*a4/72 + 4*a1*a5**3*a6**2/27 - 19*a1*a5**3*a6/81 + 5*a1*a5**3/216 + 14*a1*a5**2*a6**3/9 - 53*a1*a5**2*a6**2/27 + 53*a1*a5**2*a6/72 - 35*a1*a5**2/432 + a2**4*a3*a4/18 - 4*a2**4*a3*a5/3 + a2**4*a4**2/2 + 20*a2**3*a3*a5*a6/9 - 7*a2**3*a3*a5/3 - 7*a2**3*a3*a6/2 + 5*a2**3*a3/6 - 5*a2**3*a4**2*a6/27 + 7*a2**3*a4**2/54 + 5*a2**3*a4*a5**2/54 + 5*a2**3*a4*a5*a6/2 - 41*a2**3*a4*a5/36 + 10*a2**2*a3*a6**3/3 - 40*a2**2*a3*a6**2/9 + 127*a2**2*a3*a6/72 - 5*a2**2*a3/18 + 7*a2**2*a4*a5*a6**2/18 - 71*a2**2*a4*a5*a6/108 + a2**2*a4*a5/36 + 29*a2**2*a4*a6**3/6 - 125*a2**2*a4*a6**2/18 + 29*a2**2*a4*a6/12 - 7*a2**2*a4/24 + 2*a2**2*a5**3*a6/9 - 5*a2**2*a5**3/27 + 8*a2**2*a5**2*a6**2/3 - 11*a2**2*a5**2*a6/6 + a2**2*a5**2/4 + 4*a2*a4*a6**4/9 - 35*a2*a4*a6**3/54 + 29*a2*a4*a6**2/108 - 5*a2*a4*a6/108 + 7*a2*a5**2*a6**3/9 - 17*a2*a5**2*a6**2/12 + 4*a2*a5**2*a6/9 - a2*a5**2/36 + 25*a2*a5*a6**4/3 - 445*a2*a5*a6**3/36 + 413*a2*a5*a6**2/72 - 73*a2*a5*a6/72 + 7*a2*a5/144 + 2*a5*a6**5/3 - 5*a5*a6**4/3 + 59*a5*a6**3/54 - 31*a5*a6**2/108 + a5*a6/36 + 6*a6**6 - 13*a6**5 + 121*a6**4/12 - 67*a6**3/18 + 97*a6**2/144 - 7*a6/144",
      "-a0**2*a2*a3**2*a4/4 + a0**2*a3*a4**2*a6/12 + a0**2*a3*a4**2/72 - 7*a0**2*a3*a4*a5**2/36 + 5*a0**2*a4**3*a5/108 + a0*a1**2*a3**2*a4/4 - 7*a0*a1*a2*a3*a4**2/12 + 3*a0*a1*a3**2*a6**2 - 7*a0*a1*a3**2*a6/4 + 5*a0*a1*a3**2/24 - 29*a0*a1*a3*a4*a5*a6/12 + 31*a0*a1*a3*a4*a5/24 - a0*a1*a3*a5**3/3 + 5*a0*a1*a4**3*a6/18 - 11*a0*a1*a4**3/54 + a0*a1*a4**2*a5**2/6 - 3*a0*a2**2*a3**2*a6/4 + 7*a0*a2**2*a3**2/8 - 3*a0*a2**2*a3*a4*a5/2 + a0*a2**2*a4**3/18 - 5*a0*a2*a3*a4*a6**2 + 55*a0*a2*a3*a4*a6/12 - 55*a0*a2*a3*a4/72 - 8*a0*a2*a3*a5**2*a6/3 + a0*a2*a3*a5**2/9 + 5*a0*a2*a4**2*a5*a6/36 + 7*a0*a2*a4**2*a5/108 + a0*a2*a4*a5**3/6 - 9*a0*a3*a5*a6**3/2 + 11*a0*a3*a5*a6**2/6 - 17*a0*a3*a5*a6/144 + a0*a3*a5/96 - 7*a0*a4**2*a6**3/6 + 49*a0*a4**2*a6**2/36 - 73*a0*a4**2*a6/216 + 5*a0*a4**2/216 + 2*a0*a4*a5**2*a6**2/3 - 13*a0*a4*a5**2*a6/216 - 23*a0*a4*a5**2/432 - a0*a5**4*a6/36 - 13*a0*a5**4/216 + a1**3*a3*a4**2/2 - 9*a1**2*a2*a3**2*a6/2 + 3*a1**2*a2*a3**2/4 + 9*a1**2*a2*a3*a4*a5/4 - a1**2*a2*a4**3/18 - 5*a1**2*a3*a4*a6**2/2 + 7*a1**2*a3*a4*a6/3 - 7*a1**2*a3*a4/12 - 7*a1**2*a3*a5**2*a6/4 + 55*a1**2*a3*a5**2/24 + 2*a1**2*a4**2*a5*a6/3 - 3*a1**2*a4**2*a5/4 + a1**2*a4*a5**3/12 + 9*a1*a2**3*a3**2/4 + 4*a1*a2**2*a3*a4*a6 - 5*a1*a2**2*a3*a4/2 + 7*a1*a2**2*a3*a5**2/3 + a1*a2**2*a4**2*a5/36 - 23*a1*a2*a3*a5*a6**2/4 + 121*a1*a2*a3*a5*a6/8 - 61*a1*a2*a3*a5/16 + 7*a1*a2*a4**2*a6**2/6 - 10*a1*a2*a4**2*a6/9 + a1*a2*a4**2/8 + 11*a1*a2*a4*a5**2*a6/18 - 85*a1*a2*a4*a5**2/72 + 7*a1*a2*a5**4/36 - 6*a1*a3*a6**4 + 51*a1*a3*a6**3/4 - 28*a1*a3*a6**2/3 + 73*a1*a3*a6/24 - 35*a1*a3/96 - 2*a1*a4*a5*a6**3/3 + 77*a1*a4*a5*a6**2/36 - 17*a1*a4*a5*a6/36 + a1*a4*a5/144 + 2*a1*a5**3*a6**2/3 - 19*a1*a5**3*a6/18 + 5*a1*a5**3/48 + a2**4*a3*a4/4 + 10*a2**3*a3*a5*a6 - 21*a2**3*a3*a5/2 - 5*a2**3*a4**2*a6/6 + 7*a2**3*a4**2/12 + 5*a2**3*a4*a5**2/12 + 15*a2**2*a3*a6**3 - 20*a2**2*a3*a6**2 + 127*a2**2*a3*a6/16 - 5*a2**2*a3/4 + 7*a2**2*a4*a5*a6**2/4 - 71*a2**2*a4*a5*a6/24 + a2**2*a4*a5/8 + a2**2*a5**3*a6 - 5*a2**2*a5**3/6 + 2*a2*a4*a6**4 - 35*a2*a4*a6**3/12 + 29*a2*a4*a6**2/24 - 5*a2*a4*a6/24 + 7*a2*a5**2*a6**3/2 - 51*a2*a5**2*a6**2/8 + 2*a2*a5**2*a6 - a2*a5**2/8 + 3*a5*a6**5 - 15*a5*a6**4/2 + 59*a5*a6**3/12 - 31*a5*a6**2/24 + a5*a6/8",
      "a0**2*a2*a3**2*a4/27 + a0**2*a2*a3*a4**2/27 + 2*a0**2*a2*a3*a4*a5/9 - a0**2*a2*a4**3/18 - a0**2*a3*a4**2*a6/81 - a0**2*a3*a4**2/486 + 7*a0**2*a3*a4*a5**2/243 + 5*a0**2*a3*a4*a5*a6/27 - a0**2*a3*a4*a5/162 + 4*a0**2*a3*a4*a6**2/3 - 5*a0**2*a3*a4*a6/9 + 7*a0**2*a3*a4/108 - 5*a0**2*a4**3*a5/729 - 2*a0**2*a4**3*a6/27 + 2*a0**2*a4**2*a5**2/243 - 17*a0**2*a4**2*a5*a6/54 + 19*a0**2*a4**2*a5/324 + 5*a0**2*a4*a5**3/81 - a0*a1**2*a3**2*a4/27 - a0*a1**2*a3*a4**2/27 - a0*a1**2*a3*a4*a5/18 + 7*a0*a1*a2*a3*a4**2/81 - 14*a0*a1*a2*a3*a4*a5/27 - 7*a0*a1*a2*a3*a4*a6/3 + 4*a0*a1*a2*a3*a4/9 + a0*a1*a2*a3*a5**2/3 + 7*a0*a1*a2*a4**3/27 + 5*a0*a1*a2*a4**2*a5/18 - 4*a0*a1*a3**2*a6**2/9 + 7*a0*a1*a3**2*a6/27 - 5*a0*a1*a3**2/162 + 29*a0*a1*a3*a4*a5*a6/81 - 31*a0*a1*a3*a4*a5/162 - 4*a0*a1*a3*a4*a6**2/9 + 10*a0*a1*a3*a4*a6/27 - 11*a0*a1*a3*a4/162 + 4*a0*a1*a3*a5**3/81 + 14*a0*a1*a3*a5**2*a6/27 - 7*a0*a1*a3*a5**2/81 + 8*a0*a1*a3*a5*a6**2/3 - 23*a0*a1*a3*a5*a6/18 + 7*a0*a1*a3*a5/36 - 10*a0*a1*a4**3*a6/243 + 22*a0*a1*a4**3/729 - 2*a0*a1*a4**2*a5**2/81 + 5*a0*a1*a4**2*a5*a6/81 - 41*a0*a1*a4**2*a5/486 - 5*a0*a1*a4**2*a6**2/9 + 10*a0*a1*a4**2*a6/27 - 17*a0*a1*a4**2/324 - 2*a0*a1*a4*a5**3/81 - 5*a0*a1*a4*a5**2*a6/18 - 13*a0*a1*a4*a5**2/324 + a0*a1*a5**4/9 + a0*a2**3*a3*a4 + a0*a2**2*a3**2*a6/9 - 7*a0*a2**2*a3**2/54 + 2*a0*a2**2*a3*a4*a5/9 - 5*a0*a2**2*a3*a4*a6/9 + 5*a0*a2**2*a3*a4/54 - 16*a0*a2**2*a3*a5**2/27 - a0*a2**2*a3*a5*a6 - 8*a0*a2**2*a3*a5/9 - 2*a0*a2**2*a4**3/243 + 38*a0*a2**2*a4**2*a5/81 + 7*a0*a2**2*a4**2*a6/18 + 4*a0*a2**2*a4**2/27 + 17*a0*a2**2*a4*a5**2/27 + 20*a0*a2*a3*a4*a6**2/27 - 55*a0*a2*a3*a4*a6/81 + 55*a0*a2*a3*a4/486 + 32*a0*a2*a3*a5**2*a6/81 - 4*a0*a2*a3*a5**2/243 - 11*a0*a2*a3*a5*a6**2/9 + 13*a0*a2*a3*a5*a6/9 - 115*a0*a2*a3*a5/324 + a0*a2*a3*a6**3/2 - 41*a0*a2*a3*a6**2/12 + 125*a0*a2*a3*a6/72 - 53*a0*a2*a3/216 - 5*a0*a2*a4**2*a5*a6/243 - 7*a0*a2*a4**2*a5/729 + 13*a0*a2*a4**2*a6**2/27 - 95*a0*a2*a4**2*a6/162 + 7*a0*a2*a4**2/54 - 2*a0*a2*a4*a5**3/81 + 17*a0*a2*a4*a5**2*a6/27 - 91*a0*a2*a4*a5**2/486 + 16*a0*a2*a4*a5*a6**2/9 - 23*a0*a2*a4*a5*a6/36 + 19*a0*a2*a4*a5/648 - 8*a0*a2*a5**4/81 + 7*a0*a2*a5**3*a6/27 - 14*a0*a2*a5**3/81 + 2*a0*a3*a5*a6**3/3 - 22*a0*a3*a5*a6**2/81 + 17*a0*a3*a5*a6/972 - a0*a3*a5/648 - a0*a3*a6**4 + 10*a0*a3*a6**3/3 - 7*a0*a3*a6**2/3 + 133*a0*a3*a6/216 - 37*a0*a3/648 + 14*a0*a4**2*a6**3/81 - 49*a0*a4**2*a6**2/243 + 73*a0*a4**2*a6/1458 - 5*a0*a4**2/1458 - 8*a0*a4*a5**2*a6**2/81 + 13*a0*a4*a5**2*a6/1458 + 23*a0*a4*a5**2/2916 + 29*a0*a4*a5*a6**3/27 - 113*a0*a4*a5*a6**2/81 + 130*a0*a4*a5*a6/243 - 17*a0*a4*a5/243 + 7*a0*a4*a6**4/3 - 17*a0*a4*a6**3/6 + 11*a0*a4*a6**2/9 - 149*a0*a4*a6/648 + 5*a0*a4/324 + a0*a5**4*a6/243 + 13*a0*a5**4/1458 - 5*a0*a5**3*a6**2/27 + 44*a0*a5**3*a6/243 - 41*a0*a5**3/972 + a0*a5**2*a6**3/6 - 13*a0*a5**2*a6**2/108 + a0*a5**2*a6/54 - a0*a5**2/144 - 2*a1**3*a3*a4**2/27 + 2*a1**3*a3*a4*a5/9 + a1**3*a3*a4*a6 - a1**3*a3*a4/6 - 4*a1**3*a4**3/27 - 2*a1**3*a4**2*a5/9 - a1**2*a2**2*a3*a4/2 + 2*a1**2*a2*a3**2*a6/3 - a1**2*a2*a3**2/9 - a1**2*a2*a3*a4*a5/3 + a1**2*a2*a3*a4*a6 - 5*a1**2*a2*a3*a4/18 - 2*a1**2*a2*a3*a5**2/27 - 4*a1**2*a2*a3*a5*a6/3 + 13*a1**2*a2*a3*a5/9 + 2*a1**2*a2*a4**3/243 - 26*a1**2*a2*a4**2*a5/81 + a1**2*a2*a4**2*a6/9 - 17*a1**2*a2*a4**2/54 - 19*a1**2*a2*a4*a5**2/54 + 10*a1**2*a3*a4*a6**2/27 - 28*a1**2*a3*a4*a6/81 + 7*a1**2*a3*a4/81 + 7*a1**2*a3*a5**2*a6/27 - 55*a1**2*a3*a5**2/162 + 2*a1**2*a3*a5*a6**2 - 17*a1**2*a3*a5*a6/9 + 10*a1**2*a3*a5/27 + 3*a1**2*a3*a6**3 - 3*a1**2*a3*a6**2 + a1**2*a3*a6 - 7*a1**2*a3/72 - 8*a1**2*a4**2*a5*a6/81 + a1**2*a4**2*a5/9 + 4*a1**2*a4**2*a6**2/27 + 14*a1**2*a4**2*a6/81 - a1**2*a4**2/18 - a1**2*a4*a5**3/81 - 8*a1**2*a4*a5**2*a6/27 + a1**2*a4*a5**2/81 - 10*a1**2*a4*a5*a6**2/9 + 41*a1**2*a4*a5*a6/54 - a1**2*a4*a5/12 + a1**2*a5**3*a6/6 - 7*a1**2*a5**3/36 - a1*a2**3*a3**2/3 - a1*a2**3*a3*a4/3 + a1*a2**3*a4**2/6 - 16*a1*a2**2*a3*a4*a6/27 + 10*a1*a2**2*a3*a4/27 - 28*a1*a2**2*a3*a5**2/81 - 13*a1*a2**2*a3*a5*a6/9 + 5*a1*a2**2*a3*a5/18 - 19*a1*a2**2*a3*a6**2/2 + 131*a1*a2**2*a3*a6/12 - 55*a1*a2**2*a3/24 - a1*a2**2*a4**2*a5/243 - a1*a2**2*a4**2*a6/3 + a1*a2**2*a4**2/6 - 23*a1*a2**2*a4*a5**2/81 + a1*a2**2*a4*a5*a6/9 - 55*a1*a2**2*a4*a5/108 - 2*a1*a2**2*a5**3/27 + 23*a1*a2*a3*a5*a6**2/27 - 121*a1*a2*a3*a5*a6/54 + 61*a1*a2*a3*a5/108 + 3*a1*a2*a3*a6**3 - 22*a1*a2*a3*a6**2/3 + 29*a1*a2*a3*a6/9 - 29*a1*a2*a3/72 - 14*a1*a2*a4**2*a6**2/81 + 40*a1*a2*a4**2*a6/243 - a1*a2*a4**2/54 - 22*a1*a2*a4*a5**2*a6/243 + 85*a1*a2*a4*a5**2/486 - 2*a1*a2*a4*a5*a6**2/9 + 29*a1*a2*a4*a5*a6/162 - a1*a2*a4*a5/36 - 13*a1*a2*a4*a6**3/3 + 17*a1*a2*a4*a6**2/3 - 203*a1*a2*a4*a6/108 + 7*a1*a2*a4/36 - 7*a1*a2*a5**4/243 - 37*a1*a2*a5**3*a6/81 + 19*a1*a2*a5**3/162 + 11*a1*a2*a5**2*a6**2/9 - 58*a1*a2*a5**2*a6/27 + 97*a1*a2*a5**2/216 + 8*a1*a3*a6**4/9 - 17*a1*a3*a6**3/9 + 112*a1*a3*a6**2/81 - 73*a1*a3*a6/162 + 35*a1*a3/648 + 8*a1*a4*a5*a6**3/81 - 77*a1*a4*a5*a6**2/243 + 17*a1*a4*a5*a6/243 - a1*a4*a5/972 + 20*a1*a4*a6**4/9 - 40*a1*a4*a6**3/9 + 211*a1*a4*a6**2/81 - 2*a1*a4*a6/3 + 7*a1*a4/108 - 8*a1*a5**3*a6**2/81 + 38*a1*a5**3*a6/243 - 5*a1*a5**3/324 - 28*a1*a5**2*a6**3/27 + 106*a1*a5**2*a6**2/81 - 53*a1*a5**2*a6/108 + 35*a1*a5**2/648 + 2*a1*a5*a6**4/3 - 31*a1*a5*a6**3/18 + 35*a1*a5*a6**2/36 - 31*a1*a5*a6/108 + 7*a1*a5/216 - a2**4*a3*a4/27 + 8*a2**4*a3*a5/9 + 4*a2**4*a3*a6 - 23*a2**4*a3/6 - a2**4*a4**2/3 + a2**4*a4*a5/3 - 40*a2**3*a3*a5*a6/27 + 14*a2**3*a3*a5/9 + 7*a2**3*a3*a6/3 - 5*a2**3*a3/9 + 10*a2**3*a4**2*a6/81 - 7*a2**3*a4**2/81 - 5*a2**3*a4*a5**2/81 - 5*a2**3*a4*a5*a6/3 + 41*a2**3*a4*a5/54 + 19*a2**3*a4*a6**2/6 - 137*a2**3*a4*a6/36 + 5*a2**3*a4/9 - 2*a2**3*a5**2*a6/9 + 7*a2**3*a5**2/18 - 20*a2**2*a3*a6**3/9 + 80*a2**2*a3*a6**2/27 - 127*a2**2*a3*a6/108 + 5*a2**2*a3/27 - 7*a2**2*a4*a5*a6**2/27 + 71*a2**2*a4*a5*a6/162 - a2**2*a4*a5/54 - 29*a2**2*a4*a6**3/9 + 125*a2**2*a4*a6**2/27 - 29*a2**2*a4*a6/18 + 7*a2**2*a4/36 - 4*a2**2*a5**3*a6/27 + 10*a2**2*a5**3/81 - 16*a2**2*a5**2*a6**2/9 + 11*a2**2*a5**2*a6/9 - a2**2*a5**2/6 + 5*a2**2*a5*a6**3/3 - 113*a2**2*a5*a6**2/36 + 77*a2**2*a5*a6/72 - 8*a2*a4*a6**4/27 + 35*a2*a4*a6**3/81 - 29*a2*a4*a6**2/162 + 5*a2*a4*a6/162 - 14*a2*a5**2*a6**3/27 + 17*a2*a5**2*a6**2/18 - 8*a2*a5**2*a6/27 + a2*a5**2/54 - 50*a2*a5*a6**4/9 + 445*a2*a5*a6**3/54 - 413*a2*a5*a6**2/108 + 73*a2*a5*a6/108 - 7*a2*a5/216 + 2*a2*a6**5 - 16*a2*a6**4/3 + 137*a2*a6**3/36 - 77*a2*a6**2/72 + a2*a6/9 - 4*a5*a6**5/9 + 10*a5*a6**4/9 - 59*a5*a6**3/81 + 31*a5*a6**2/162 - a5*a6/54 - 4*a6**6 + 26*a6**5/3 - 121*a6**4/18 + 67*a6**3/27 - 97*a6**2/216 + 7*a6/216",
      "a0**2*a1*a3*a4*a5/6 - a0**2*a1*a4**3/18 - 2*a0**2*a2*a3**2*a4/81 - 2*a0**2*a2*a3*a4**2/81 - 4*a0**2*a2*a3*a4*a5/27 + 7*a0**2*a2*a3*a4*a6/6 - 5*a0**2*a2*a3*a4/18 + a0**2*a2*a4**3/27 - 4*a0**2*a2*a4**2*a5/27 + 2*a0**2*a3*a4**2*a6/243 + a0**2*a3*a4**2/729 - 14*a0**2*a3*a4*a5**2/729 - 10*a0**2*a3*a4*a5*a6/81 + a0**2*a3*a4*a5/243 - 8*a0**2*a3*a4*a6**2/9 + 10*a0**2*a3*a4*a6/27 - 7*a0**2*a3*a4/162 + 10*a0**2*a4**3*a5/2187 + 4*a0**2*a4**3*a6/81 - 4*a0**2*a4**2*a5**2/729 + 17*a0**2*a4**2*a5*a6/81 - 19*a0**2*a4**2*a5/486 + a0**2*a4**2*a6**2/2 - a0**2*a4**2*a6/4 + a0**2*a4**2/36 - 10*a0**2*a4*a5**3/243 - 5*a0**2*a4*a5**2*a6/27 + a0**2*a4*a5**2/18 + 2*a0*a1**2*a3**2*a4/81 + 2*a0*a1**2*a3*a4**2/81 + a0*a1**2*a3*a4*a5/27 + a0*a1**2*a3*a4*a6/6 + a0*a1**2*a3*a5**2/3 - a0*a1**2*a4**2*a5/9 - 4*a0*a1*a2**2*a3*a4/3 - 14*a0*a1*a2*a3*a4**2/243 + 28*a0*a1*a2*a3*a4*a5/81 + 14*a0*a1*a2*a3*a4*a6/9 - 8*a0*a1*a2*a3*a4/27 - 2*a0*a1*a2*a3*a5**2/9 + 29*a0*a1*a2*a3*a5*a6/6 - 71*a0*a1*a2*a3*a5/36 - 14*a0*a1*a2*a4**3/81 - 5*a0*a1*a2*a4**2*a5/27 - 11*a0*a1*a2*a4**2*a6/9 + 37*a0*a1*a2*a4**2/54 - 5*a0*a1*a2*a4*a5**2/9 + 8*a0*a1*a3**2*a6**2/27 - 14*a0*a1*a3**2*a6/81 + 5*a0*a1*a3**2/243 - 58*a0*a1*a3*a4*a5*a6/243 + 31*a0*a1*a3*a4*a5/243 + 8*a0*a1*a3*a4*a6**2/27 - 20*a0*a1*a3*a4*a6/81 + 11*a0*a1*a3*a4/243 - 8*a0*a1*a3*a5**3/243 - 28*a0*a1*a3*a5**2*a6/81 + 14*a0*a1*a3*a5**2/243 - 16*a0*a1*a3*a5*a6**2/9 + 23*a0*a1*a3*a5*a6/27 - 7*a0*a1*a3*a5/54 + 7*a0*a1*a3*a6**3/2 - 53*a0*a1*a3*a6**2/12 + 115*a0*a1*a3*a6/72 - 13*a0*a1*a3/72 + 20*a0*a1*a4**3*a6/729 - 44*a0*a1*a4**3/2187 + 4*a0*a1*a4**2*a5**2/243 - 10*a0*a1*a4**2*a5*a6/243 + 41*a0*a1*a4**2*a5/729 + 10*a0*a1*a4**2*a6**2/27 - 20*a0*a1*a4**2*a6/81 + 17*a0*a1*a4**2/486 + 4*a0*a1*a4*a5**3/243 + 5*a0*a1*a4*a5**2*a6/27 + 13*a0*a1*a4*a5**2/486 - a0*a1*a4*a5*a6**2/6 + 19*a0*a1*a4*a5*a6/27 - 5*a0*a1*a4*a5/24 - 2*a0*a1*a5**4/27 - 7*a0*a1*a5**3*a6/18 + 5*a0*a1*a5**3/108 - 2*a0*a2**3*a3*a4/3 - 8*a0*a2**3*a3*a5/3 - a0*a2**3*a4**2/9 - 2*a0*a2**2*a3**2*a6/27 + 7*a0*a2**2*a3**2/81 - 4*a0*a2**2*a3*a4*a5/27 + 10*a0*a2**2*a3*a4*a6/27 - 5*a0*a2**2*a3*a4/81 + 32*a0*a2**2*a3*a5**2/81 + 2*a0*a2**2*a3*a5*a6/3 + 16*a0*a2**2*a3*a5/27 - 3*a0*a2**2*a3*a6**2/2 + 7*a0*a2**2*a3*a6/12 - a0*a2**2*a3/18 + 4*a0*a2**2*a4**3/729 - 76*a0*a2**2*a4**2*a5/243 - 7*a0*a2**2*a4**2*a6/27 - 8*a0*a2**2*a4**2/81 - 34*a0*a2**2*a4*a5**2/81 - 2*a0*a2**2*a4*a5*a6 + 35*a0*a2**2*a4*a5/54 - 4*a0*a2**2*a5**3/9 - 40*a0*a2*a3*a4*a6**2/81 + 110*a0*a2*a3*a4*a6/243 - 55*a0*a2*a3*a4/729 - 64*a0*a2*a3*a5**2*a6/243 + 8*a0*a2*a3*a5**2/729 + 22*a0*a2*a3*a5*a6**2/27 - 26*a0*a2*a3*a5*a6/27 + 115*a0*a2*a3*a5/486 - a0*a2*a3*a6**3/3 + 41*a0*a2*a3*a6**2/18 - 125*a0*a2*a3*a6/108 + 53*a0*a2*a3/324 + 10*a0*a2*a4**2*a5*a6/729 + 14*a0*a2*a4**2*a5/2187 - 26*a0*a2*a4**2*a6**2/81 + 95*a0*a2*a4**2*a6/243 - 7*a0*a2*a4**2/81 + 4*a0*a2*a4*a5**3/243 - 34*a0*a2*a4*a5**2*a6/81 + 91*a0*a2*a4*a5**2/729 - 32*a0*a2*a4*a5*a6**2/27 + 23*a0*a2*a4*a5*a6/54 - 19*a0*a2*a4*a5/972 - 4*a0*a2*a4*a6**3/3 + 4*a0*a2*a4*a6**2/3 - 14*a0*a2*a4*a6/27 + 17*a0*a2*a4/216 + 16*a0*a2*a5**4/243 - 14*a0*a2*a5**3*a6/81 + 28*a0*a2*a5**3/243 - 59*a0*a2*a5**2*a6**2/18 + 67*a0*a2*a5**2*a6/36 - 29*a0*a2*a5**2/108 - 4*a0*a3*a5*a6**3/9 + 44*a0*a3*a5*a6**2/243 - 17*a0*a3*a5*a6/1458 + a0*a3*a5/972 + 2*a0*a3*a6**4/3 - 20*a0*a3*a6**3/9 + 14*a0*a3*a6**2/9 - 133*a0*a3*a6/324 + 37*a0*a3/972 - 28*a0*a4**2*a6**3/243 + 98*a0*a4**2*a6**2/729 - 73*a0*a4**2*a6/2187 + 5*a0*a4**2/2187 + 16*a0*a4*a5**2*a6**2/243 - 13*a0*a4*a5**2*a6/2187 - 23*a0*a4*a5**2/4374 - 58*a0*a4*a5*a6**3/81 + 226*a0*a4*a5*a6**2/243 - 260*a0*a4*a5*a6/729 + 34*a0*a4*a5/729 - 14*a0*a4*a6**4/9 + 17*a0*a4*a6**3/9 - 22*a0*a4*a6**2/27 + 149*a0*a4*a6/972 - 5*a0*a4/486 - 2*a0*a5**4*a6/729 - 13*a0*a5**4/2187 + 10*a0*a5**3*a6**2/81 - 88*a0*a5**3*a6/729 + 41*a0*a5**3/1458 - a0*a5**2*a6**3/9 + 13*a0*a5**2*a6**2/162 - a0*a5**2*a6/81 + a0*a5**2/216 - 7*a0*a5*a6**4/2 + 137*a0*a5*a6**3/36 - 169*a0*a5*a6**2/108 + 137*a0*a5*a6/432 - a0*a5/36 + a1**3*a2*a3*a4/2 + 4*a1**3*a3*a4**2/81 - 4*a1**3*a3*a4*a5/27 - 2*a1**3*a3*a4*a6/3 + a1**3*a3*a4/9 - 2*a1**3*a3*a5*a6 + 4*a1**3*a3*a5/3 + 8*a1**3*a4**3/81 + 4*a1**3*a4**2*a5/27 + 2*a1**3*a4**2*a6/3 - 4*a1**3*a4**2/9 + a1**3*a4*a5**2/6 + a1**2*a2**2*a3*a4/3 + a1**2*a2**2*a3*a5/6 + 5*a1**2*a2**2*a4**2/18 - 4*a1**2*a2*a3**2*a6/9 + 2*a1**2*a2*a3**2/27 + 2*a1**2*a2*a3*a4*a5/9 - 2*a1**2*a2*a3*a4*a6/3 + 5*a1**2*a2*a3*a4/27 + 4*a1**2*a2*a3*a5**2/81 + 8*a1**2*a2*a3*a5*a6/9 - 26*a1**2*a2*a3*a5/27 - 9*a1**2*a2*a3*a6**2/2 + 23*a1**2*a2*a3*a6/4 - 29*a1**2*a2*a3/24 - 4*a1**2*a2*a4**3/729 + 52*a1**2*a2*a4**2*a5/243 - 2*a1**2*a2*a4**2*a6/27 + 17*a1**2*a2*a4**2/81 + 19*a1**2*a2*a4*a5**2/81 + 5*a1**2*a2*a4*a5*a6/9 - 17*a1**2*a2*a4*a5/36 + 7*a1**2*a2*a5**3/18 - 20*a1**2*a3*a4*a6**2/81 + 56*a1**2*a3*a4*a6/243 - 14*a1**2*a3*a4/243 - 14*a1**2*a3*a5**2*a6/81 + 55*a1**2*a3*a5**2/243 - 4*a1**2*a3*a5*a6**2/3 + 34*a1**2*a3*a5*a6/27 - 20*a1**2*a3*a5/81 - 2*a1**2*a3*a6**3 + 2*a1**2*a3*a6**2 - 2*a1**2*a3*a6/3 + 7*a1**2*a3/108 + 16*a1**2*a4**2*a5*a6/243 - 2*a1**2*a4**2*a5/27 - 8*a1**2*a4**2*a6**2/81 - 28*a1**2*a4**2*a6/243 + a1**2*a4**2/27 + 2*a1**2*a4*a5**3/243 + 16*a1**2*a4*a5**2*a6/81 - 2*a1**2*a4*a5**2/243 + 20*a1**2*a4*a5*a6**2/27 - 41*a1**2*a4*a5*a6/81 + a1**2*a4*a5/18 - 8*a1**2*a4*a6**3/3 + 32*a1**2*a4*a6**2/9 - 23*a1**2*a4*a6/18 + 5*a1**2*a4/36 - a1**2*a5**3*a6/9 + 7*a1**2*a5**3/54 + 5*a1**2*a5**2*a6**2/6 - 19*a1**2*a5**2*a6/36 - a1**2*a5**2/24 + 2*a1*a2**3*a3**2/9 + 2*a1*a2**3*a3*a4/9 - 7*a1*a2**3*a3*a6/2 - a1*a2**3*a3 - a1*a2**3*a4**2/9 + 17*a1*a2**3*a4*a5/18 + 32*a1*a2**2*a3*a4*a6/81 - 20*a1*a2**2*a3*a4/81 + 56*a1*a2**2*a3*a5**2/243 + 26*a1*a2**2*a3*a5*a6/27 - 5*a1*a2**2*a3*a5/27 + 19*a1*a2**2*a3*a6**2/3 - 131*a1*a2**2*a3*a6/18 + 55*a1*a2**2*a3/36 + 2*a1*a2**2*a4**2*a5/729 + 2*a1*a2**2*a4**2*a6/9 - a1*a2**2*a4**2/9 + 46*a1*a2**2*a4*a5**2/243 - 2*a1*a2**2*a4*a5*a6/27 + 55*a1*a2**2*a4*a5/162 + a1*a2**2*a4*a6**2/6 - 55*a1*a2**2*a4*a6/36 + a1*a2**2*a4/3 + 4*a1*a2**2*a5**3/81 + 5*a1*a2**2*a5**2*a6/2 - 5*a1*a2**2*a5**2/6 - 46*a1*a2*a3*a5*a6**2/81 + 121*a1*a2*a3*a5*a6/81 - 61*a1*a2*a3*a5/162 - 2*a1*a2*a3*a6**3 + 44*a1*a2*a3*a6**2/9 - 58*a1*a2*a3*a6/27 + 29*a1*a2*a3/108 + 28*a1*a2*a4**2*a6**2/243 - 80*a1*a2*a4**2*a6/729 + a1*a2*a4**2/81 + 44*a1*a2*a4*a5**2*a6/729 - 85*a1*a2*a4*a5**2/729 + 4*a1*a2*a4*a5*a6**2/27 - 29*a1*a2*a4*a5*a6/243 + a1*a2*a4*a5/54 + 26*a1*a2*a4*a6**3/9 - 34*a1*a2*a4*a6**2/9 + 203*a1*a2*a4*a6/162 - 7*a1*a2*a4/54 + 14*a1*a2*a5**4/729 + 74*a1*a2*a5**3*a6/243 - 19*a1*a2*a5**3/243 - 22*a1*a2*a5**2*a6**2/27 + 116*a1*a2*a5**2*a6/81 - 97*a1*a2*a5**2/324 + 4*a1*a2*a5*a6**3 - 97*a1*a2*a5*a6**2/36 - 7*a1*a2*a5*a6/12 + 7*a1*a2*a5/24 - 16*a1*a3*a6**4/27 + 34*a1*a3*a6**3/27 - 224*a1*a3*a6**2/243 + 73*a1*a3*a6/243 - 35*a1*a3/972 - 16*a1*a4*a5*a6**3/243 + 154*a1*a4*a5*a6**2/729 - 34*a1*a4*a5*a6/729 + a1*a4*a5/1458 - 40*a1*a4*a6**4/27 + 80*a1*a4*a6**3/27 - 422*a1*a4*a6**2/243 + 4*a1*a4*a6/9 - 7*a1*a4/162 + 16*a1*a5**3*a6**2/243 - 76*a1*a5**3*a6/729 + 5*a1*a5**3/486 + 56*a1*a5**2*a6**3/81 - 212*a1*a5**2*a6**2/243 + 53*a1*a5**2*a6/162 - 35*a1*a5**2/972 - 4*a1*a5*a6**4/9 + 31*a1*a5*a6**3/27 - 35*a1*a5*a6**2/54 + 31*a1*a5*a6/162 - 7*a1*a5/324 + 2*a1*a6**5 - 2*a1*a6**4 - 8*a1*a6**3/9 + 13*a1*a6**2/9 - 17*a1*a6/36 + 7*a1/144 + 4*a2**5*a3 + 2*a2**4*a3*a4/81 - 16*a2**4*a3*a5/27 - 8*a2**4*a3*a6/3 + 23*a2**4*a3/9 + 2*a2**4*a4**2/9 - 2*a2**4*a4*a5/9 + 19*a2**4*a4*a6/6 - 7*a2**4*a4/6 + 80*a2**3*a3*a5*a6/81 - 28*a2**3*a3*a5/27 - 14*a2**3*a3*a6/9 + 10*a2**3*a3/27 - 20*a2**3*a4**2*a6/243 + 14*a2**3*a4**2/243 + 10*a2**3*a4*a5**2/243 + 10*a2**3*a4*a5*a6/9 - 41*a2**3*a4*a5/81 - 19*a2**3*a4*a6**2/9 + 137*a2**3*a4*a6/54 - 10*a2**3*a4/27 + 4*a2**3*a5**2*a6/27 - 7*a2**3*a5**2/27 + 14*a2**3*a5*a6**2/3 - 13*a2**3*a5*a6/3 + 4*a2**3*a5/3 + 40*a2**2*a3*a6**3/27 - 160*a2**2*a3*a6**2/81 + 127*a2**2*a3*a6/162 - 10*a2**2*a3/81 + 14*a2**2*a4*a5*a6**2/81 - 71*a2**2*a4*a5*a6/243 + a2**2*a4*a5/81 + 58*a2**2*a4*a6**3/27 - 250*a2**2*a4*a6**2/81 + 29*a2**2*a4*a6/27 - 7*a2**2*a4/54 + 8*a2**2*a5**3*a6/81 - 20*a2**2*a5**3/243 + 32*a2**2*a5**2*a6**2/27 - 22*a2**2*a5**2*a6/27 + a2**2*a5**2/9 - 10*a2**2*a5*a6**3/9 + 113*a2**2*a5*a6**2/54 - 77*a2**2*a5*a6/108 + 6*a2**2*a6**4 - 9*a2**2*a6**3 + 43*a2**2*a6**2/8 - 37*a2**2*a6/24 + a2**2/6 + 16*a2*a4*a6**4/81 - 70*a2*a4*a6**3/243 + 29*a2*a4*a6**2/243 - 5*a2*a4*a6/243 + 28*a2*a5**2*a6**3/81 - 17*a2*a5**2*a6**2/27 + 16*a2*a5**2*a6/81 - a2*a5**2/81 + 100*a2*a5*a6**4/27 - 445*a2*a5*a6**3/81 + 413*a2*a5*a6**2/162 - 73*a2*a5*a6/162 + 7*a2*a5/324 - 4*a2*a6**5/3 + 32*a2*a6**4/9 - 137*a2*a6**3/54 + 77*a2*a6**2/108 - 2*a2*a6/27 + 8*a5*a6**5/27 - 20*a5*a6**4/27 + 118*a5*a6**3/243 - 31*a5*a6**2/243 + a5*a6/81 + 8*a6**6/3 - 52*a6**5/9 + 121*a6**4/27 - 134*a6**3/81 + 97*a6**2/324 - 7*a6/324",
      "a0**3*a3*a4*a5/6 - a0**3*a4**3/18 - a0**2*a1*a3*a4*a5/9 + 4*a0**2*a1*a3*a4*a6/3 - 5*a0**2*a1*a3*a4/18 + a0**2*a1*a3*a5**2/3 + a0**2*a1*a4**3/27 - 7*a0**2*a1*a4**2*a5/27 + 5*a0**2*a2**2*a3*a4/6 + 4*a0**2*a2*a3**2*a4/243 + 4*a0**2*a2*a3*a4**2/243 + 8*a0**2*a2*a3*a4*a5/81 - 7*a0**2*a2*a3*a4*a6/9 + 5*a0**2*a2*a3*a4/27 + 3*a0**2*a2*a3*a5*a6/2 - 11*a0**2*a2*a3*a5/12 - 2*a0**2*a2*a4**3/81 + 8*a0**2*a2*a4**2*a5/81 + a0**2*a2*a4**2*a6 + a0**2*a2*a4**2/36 - 8*a0**2*a2*a4*a5**2/27 - 4*a0**2*a3*a4**2*a6/729 - 2*a0**2*a3*a4**2/2187 + 28*a0**2*a3*a4*a5**2/2187 + 20*a0**2*a3*a4*a5*a6/243 - 2*a0**2*a3*a4*a5/729 + 16*a0**2*a3*a4*a6**2/27 - 20*a0**2*a3*a4*a6/81 + 7*a0**2*a3*a4/243 + 3*a0**2*a3*a6**3/2 - 11*a0**2*a3*a6**2/4 + 29*a0**2*a3*a6/24 - 11*a0**2*a3/72 - 20*a0**2*a4**3*a5/6561 - 8*a0**2*a4**3*a6/243 + 8*a0**2*a4**2*a5**2/2187 - 34*a0**2*a4**2*a5*a6/243 + 19*a0**2*a4**2*a5/729 - a0**2*a4**2*a6**2/3 + a0**2*a4**2*a6/6 - a0**2*a4**2/54 + 20*a0**2*a4*a5**3/729 + 10*a0**2*a4*a5**2*a6/81 - a0**2*a4*a5**2/27 + a0**2*a4*a5*a6**2/3 + a0**2*a4*a5*a6/4 - 25*a0**2*a4*a5/216 - a0**2*a5**3*a6/18 - 5*a0**2*a5**3/108 - 8*a0*a1**2*a2*a3*a4/3 - 4*a0*a1**2*a3**2*a4/243 - 4*a0*a1**2*a3*a4**2/243 - 2*a0*a1**2*a3*a4*a5/81 - a0*a1**2*a3*a4*a6/9 - 2*a0*a1**2*a3*a5**2/9 + 4*a0*a1**2*a3*a5*a6/3 + 5*a0*a1**2*a3*a5/18 + 2*a0*a1**2*a4**2*a5/27 - 5*a0*a1**2*a4**2*a6/9 - a0*a1**2*a4**2/27 - 5*a0*a1**2*a4*a5**2/18 + 8*a0*a1*a2**2*a3*a4/9 - 13*a0*a1*a2**2*a3*a5/6 - 10*a0*a1*a2**2*a4**2/9 + 28*a0*a1*a2*a3*a4**2/729 - 56*a0*a1*a2*a3*a4*a5/243 - 28*a0*a1*a2*a3*a4*a6/27 + 16*a0*a1*a2*a3*a4/81 + 4*a0*a1*a2*a3*a5**2/27 - 29*a0*a1*a2*a3*a5*a6/9 + 71*a0*a1*a2*a3*a5/54 - 7*a0*a1*a2*a3*a6**2/2 + 67*a0*a1*a2*a3*a6/12 - 35*a0*a1*a2*a3/24 + 28*a0*a1*a2*a4**3/243 + 10*a0*a1*a2*a4**2*a5/81 + 22*a0*a1*a2*a4**2*a6/27 - 37*a0*a1*a2*a4**2/81 + 10*a0*a1*a2*a4*a5**2/27 + a0*a1*a2*a4*a5*a6/18 - 5*a0*a1*a2*a4*a5/54 - 7*a0*a1*a2*a5**3/18 - 16*a0*a1*a3**2*a6**2/81 + 28*a0*a1*a3**2*a6/243 - 10*a0*a1*a3**2/729 + 116*a0*a1*a3*a4*a5*a6/729 - 62*a0*a1*a3*a4*a5/729 - 16*a0*a1*a3*a4*a6**2/81 + 40*a0*a1*a3*a4*a6/243 - 22*a0*a1*a3*a4/729 + 16*a0*a1*a3*a5**3/729 + 56*a0*a1*a3*a5**2*a6/243 - 28*a0*a1*a3*a5**2/729 + 32*a0*a1*a3*a5*a6**2/27 - 46*a0*a1*a3*a5*a6/81 + 7*a0*a1*a3*a5/81 - 7*a0*a1*a3*a6**3/3 + 53*a0*a1*a3*a6**2/18 - 115*a0*a1*a3*a6/108 + 13*a0*a1*a3/108 - 40*a0*a1*a4**3*a6/2187 + 88*a0*a1*a4**3/6561 - 8*a0*a1*a4**2*a5**2/729 + 20*a0*a1*a4**2*a5*a6/729 - 82*a0*a1*a4**2*a5/2187 - 20*a0*a1*a4**2*a6**2/81 + 40*a0*a1*a4**2*a6/243 - 17*a0*a1*a4**2/729 - 8*a0*a1*a4*a5**3/729 - 10*a0*a1*a4*a5**2*a6/81 - 13*a0*a1*a4*a5**2/729 + a0*a1*a4*a5*a6**2/9 - 38*a0*a1*a4*a5*a6/81 + 5*a0*a1*a4*a5/36 + a0*a1*a4*a6**3/3 + 7*a0*a1*a4*a6**2/9 - 53*a0*a1*a4*a6/108 + 19*a0*a1*a4/216 + 4*a0*a1*a5**4/81 + 7*a0*a1*a5**3*a6/27 - 5*a0*a1*a5**3/162 + a0*a1*a5**2*a6**2/3 - 19*a0*a1*a5**2*a6/54 - 5*a0*a1*a5**2/72 + 4*a0*a2**3*a3*a4/9 + 16*a0*a2**3*a3*a5/9 - a0*a2**3*a3*a6/2 - 23*a0*a2**3*a3/12 + 2*a0*a2**3*a4**2/27 - 25*a0*a2**3*a4*a5/18 + 4*a0*a2**2*a3**2*a6/81 - 14*a0*a2**2*a3**2/243 + 8*a0*a2**2*a3*a4*a5/81 - 20*a0*a2**2*a3*a4*a6/81 + 10*a0*a2**2*a3*a4/243 - 64*a0*a2**2*a3*a5**2/243 - 4*a0*a2**2*a3*a5*a6/9 - 32*a0*a2**2*a3*a5/81 + a0*a2**2*a3*a6**2 - 7*a0*a2**2*a3*a6/18 + a0*a2**2*a3/27 - 8*a0*a2**2*a4**3/2187 + 152*a0*a2**2*a4**2*a5/729 + 14*a0*a2**2*a4**2*a6/81 + 16*a0*a2**2*a4**2/243 + 68*a0*a2**2*a4*a5**2/243 + 4*a0*a2**2*a4*a5*a6/3 - 35*a0*a2**2*a4*a5/81 - 13*a0*a2**2*a4*a6**2/6 + 5*a0*a2**2*a4*a6/36 - 2*a0*a2**2*a4/9 + 8*a0*a2**2*a5**3/27 - 5*a0*a2**2*a5**2*a6/18 + 5*a0*a2**2*a5**2/108 + 80*a0*a2*a3*a4*a6**2/243 - 220*a0*a2*a3*a4*a6/729 + 110*a0*a2*a3*a4/2187 + 128*a0*a2*a3*a5**2*a6/729 - 16*a0*a2*a3*a5**2/2187 - 44*a0*a2*a3*a5*a6**2/81 + 52*a0*a2*a3*a5*a6/81 - 115*a0*a2*a3*a5/729 + 2*a0*a2*a3*a6**3/9 - 41*a0*a2*a3*a6**2/27 + 125*a0*a2*a3*a6/162 - 53*a0*a2*a3/486 - 20*a0*a2*a4**2*a5*a6/2187 - 28*a0*a2*a4**2*a5/6561 + 52*a0*a2*a4**2*a6**2/243 - 190*a0*a2*a4**2*a6/729 + 14*a0*a2*a4**2/243 - 8*a0*a2*a4*a5**3/729 + 68*a0*a2*a4*a5**2*a6/243 - 182*a0*a2*a4*a5**2/2187 + 64*a0*a2*a4*a5*a6**2/81 - 23*a0*a2*a4*a5*a6/81 + 19*a0*a2*a4*a5/1458 + 8*a0*a2*a4*a6**3/9 - 8*a0*a2*a4*a6**2/9 + 28*a0*a2*a4*a6/81 - 17*a0*a2*a4/324 - 32*a0*a2*a5**4/729 + 28*a0*a2*a5**3*a6/243 - 56*a0*a2*a5**3/729 + 59*a0*a2*a5**2*a6**2/27 - 67*a0*a2*a5**2*a6/54 + 29*a0*a2*a5**2/162 + 7*a0*a2*a5*a6**3/2 - 65*a0*a2*a5*a6**2/18 + 23*a0*a2*a5*a6/108 + 67*a0*a2*a5/432 + 8*a0*a3*a5*a6**3/27 - 88*a0*a3*a5*a6**2/729 + 17*a0*a3*a5*a6/2187 - a0*a3*a5/1458 - 4*a0*a3*a6**4/9 + 40*a0*a3*a6**3/27 - 28*a0*a3*a6**2/27 + 133*a0*a3*a6/486 - 37*a0*a3/1458 + 56*a0*a4**2*a6**3/729 - 196*a0*a4**2*a6**2/2187 + 146*a0*a4**2*a6/6561 - 10*a0*a4**2/6561 - 32*a0*a4*a5**2*a6**2/729 + 26*a0*a4*a5**2*a6/6561 + 23*a0*a4*a5**2/6561 + 116*a0*a4*a5*a6**3/243 - 452*a0*a4*a5*a6**2/729 + 520*a0*a4*a5*a6/2187 - 68*a0*a4*a5/2187 + 28*a0*a4*a6**4/27 - 34*a0*a4*a6**3/27 + 44*a0*a4*a6**2/81 - 149*a0*a4*a6/1458 + 5*a0*a4/729 + 4*a0*a5**4*a6/2187 + 26*a0*a5**4/6561 - 20*a0*a5**3*a6**2/243 + 176*a0*a5**3*a6/2187 - 41*a0*a5**3/2187 + 2*a0*a5**2*a6**3/27 - 13*a0*a5**2*a6**2/243 + 2*a0*a5**2*a6/243 - a0*a5**2/324 + 7*a0*a5*a6**4/3 - 137*a0*a5*a6**3/54 + 169*a0*a5*a6**2/162 - 137*a0*a5*a6/648 + a0*a5/54 + 6*a0*a6**5 - 17*a0*a6**4/2 + 41*a0*a6**3/12 - 11*a0*a6**2/36 - 31*a0*a6/432 + 5*a0/432 + a1**4*a3*a4 - a1**3*a2*a3*a4/3 - a1**3*a2*a3*a5/3 + 7*a1**3*a2*a4**2/9 - 8*a1**3*a3*a4**2/243 + 8*a1**3*a3*a4*a5/81 + 4*a1**3*a3*a4*a6/9 - 2*a1**3*a3*a4/27 + 4*a1**3*a3*a5*a6/3 - 8*a1**3*a3*a5/9 + 3*a1**3*a3*a6**2 - 5*a1**3*a3*a6/2 + 7*a1**3*a3/12 - 16*a1**3*a4**3/243 - 8*a1**3*a4**2*a5/81 - 4*a1**3*a4**2*a6/9 + 8*a1**3*a4**2/27 - a1**3*a4*a5**2/9 - 4*a1**3*a4*a5*a6/3 + 7*a1**3*a4*a5/18 - 2*a1**2*a2**2*a3*a4/9 - a1**2*a2**2*a3*a5/9 - 8*a1**2*a2**2*a3*a6 + 5*a1**2*a2**2*a3/2 - 5*a1**2*a2**2*a4**2/27 + 5*a1**2*a2**2*a4*a5/3 + 8*a1**2*a2*a3**2*a6/27 - 4*a1**2*a2*a3**2/81 - 4*a1**2*a2*a3*a4*a5/27 + 4*a1**2*a2*a3*a4*a6/9 - 10*a1**2*a2*a3*a4/81 - 8*a1**2*a2*a3*a5**2/243 - 16*a1**2*a2*a3*a5*a6/27 + 52*a1**2*a2*a3*a5/81 + 3*a1**2*a2*a3*a6**2 - 23*a1**2*a2*a3*a6/6 + 29*a1**2*a2*a3/36 + 8*a1**2*a2*a4**3/2187 - 104*a1**2*a2*a4**2*a5/729 + 4*a1**2*a2*a4**2*a6/81 - 34*a1**2*a2*a4**2/243 - 38*a1**2*a2*a4*a5**2/243 - 10*a1**2*a2*a4*a5*a6/27 + 17*a1**2*a2*a4*a5/54 - 3*a1**2*a2*a4*a6**2 + 35*a1**2*a2*a4*a6/18 - a1**2*a2*a4/9 - 7*a1**2*a2*a5**3/27 - 25*a1**2*a2*a5**2*a6/18 + 19*a1**2*a2*a5**2/36 + 40*a1**2*a3*a4*a6**2/243 - 112*a1**2*a3*a4*a6/729 + 28*a1**2*a3*a4/729 + 28*a1**2*a3*a5**2*a6/243 - 110*a1**2*a3*a5**2/729 + 8*a1**2*a3*a5*a6**2/9 - 68*a1**2*a3*a5*a6/81 + 40*a1**2*a3*a5/243 + 4*a1**2*a3*a6**3/3 - 4*a1**2*a3*a6**2/3 + 4*a1**2*a3*a6/9 - 7*a1**2*a3/162 - 32*a1**2*a4**2*a5*a6/729 + 4*a1**2*a4**2*a5/81 + 16*a1**2*a4**2*a6**2/243 + 56*a1**2*a4**2*a6/729 - 2*a1**2*a4**2/81 - 4*a1**2*a4*a5**3/729 - 32*a1**2*a4*a5**2*a6/243 + 4*a1**2*a4*a5**2/729 - 40*a1**2*a4*a5*a6**2/81 + 82*a1**2*a4*a5*a6/243 - a1**2*a4*a5/27 + 16*a1**2*a4*a6**3/9 - 64*a1**2*a4*a6**2/27 + 23*a1**2*a4*a6/27 - 5*a1**2*a4/54 + 2*a1**2*a5**3*a6/27 - 7*a1**2*a5**3/81 - 5*a1**2*a5**2*a6**2/9 + 19*a1**2*a5**2*a6/54 + a1**2*a5**2/36 - 2*a1**2*a5*a6**3/3 + 13*a1**2*a5*a6**2/18 - 11*a1**2*a5*a6/18 + a1**2*a5/6 + 11*a1*a2**4*a3/2 - 4*a1*a2**3*a3**2/27 - 4*a1*a2**3*a3*a4/27 + 7*a1*a2**3*a3*a6/3 + 2*a1*a2**3*a3/3 + 2*a1*a2**3*a4**2/27 - 17*a1*a2**3*a4*a5/27 + 8*a1*a2**3*a4*a6/3 - 7*a1*a2**3*a4/6 + 25*a1*a2**3*a5**2/18 - 64*a1*a2**2*a3*a4*a6/243 + 40*a1*a2**2*a3*a4/243 - 112*a1*a2**2*a3*a5**2/729 - 52*a1*a2**2*a3*a5*a6/81 + 10*a1*a2**2*a3*a5/81 - 38*a1*a2**2*a3*a6**2/9 + 131*a1*a2**2*a3*a6/27 - 55*a1*a2**2*a3/54 - 4*a1*a2**2*a4**2*a5/2187 - 4*a1*a2**2*a4**2*a6/27 + 2*a1*a2**2*a4**2/27 - 92*a1*a2**2*a4*a5**2/729 + 4*a1*a2**2*a4*a5*a6/81 - 55*a1*a2**2*a4*a5/243 - a1*a2**2*a4*a6**2/9 + 55*a1*a2**2*a4*a6/54 - 2*a1*a2**2*a4/9 - 8*a1*a2**2*a5**3/243 - 5*a1*a2**2*a5**2*a6/3 + 5*a1*a2**2*a5**2/9 - 13*a1*a2**2*a5*a6**2/3 + 10*a1*a2**2*a5*a6/3 - a1*a2**2*a5/9 + 92*a1*a2*a3*a5*a6**2/243 - 242*a1*a2*a3*a5*a6/243 + 61*a1*a2*a3*a5/243 + 4*a1*a2*a3*a6**3/3 - 88*a1*a2*a3*a6**2/27 + 116*a1*a2*a3*a6/81 - 29*a1*a2*a3/162 - 56*a1*a2*a4**2*a6**2/729 + 160*a1*a2*a4**2*a6/2187 - 2*a1*a2*a4**2/243 - 88*a1*a2*a4*a5**2*a6/2187 + 170*a1*a2*a4*a5**2/2187 - 8*a1*a2*a4*a5*a6**2/81 + 58*a1*a2*a4*a5*a6/729 - a1*a2*a4*a5/81 - 52*a1*a2*a4*a6**3/27 + 68*a1*a2*a4*a6**2/27 - 203*a1*a2*a4*a6/243 + 7*a1*a2*a4/81 - 28*a1*a2*a5**4/2187 - 148*a1*a2*a5**3*a6/729 + 38*a1*a2*a5**3/729 + 44*a1*a2*a5**2*a6**2/81 - 232*a1*a2*a5**2*a6/243 + 97*a1*a2*a5**2/486 - 8*a1*a2*a5*a6**3/3 + 97*a1*a2*a5*a6**2/54 + 7*a1*a2*a5*a6/18 - 7*a1*a2*a5/36 - 8*a1*a2*a6**4 + 28*a1*a2*a6**3/3 - 143*a1*a2*a6**2/36 + 43*a1*a2*a6/36 - a1*a2/6 + 32*a1*a3*a6**4/81 - 68*a1*a3*a6**3/81 + 448*a1*a3*a6**2/729 - 146*a1*a3*a6/729 + 35*a1*a3/1458 + 32*a1*a4*a5*a6**3/729 - 308*a1*a4*a5*a6**2/2187 + 68*a1*a4*a5*a6/2187 - a1*a4*a5/2187 + 80*a1*a4*a6**4/81 - 160*a1*a4*a6**3/81 + 844*a1*a4*a6**2/729 - 8*a1*a4*a6/27 + 7*a1*a4/243 - 32*a1*a5**3*a6**2/729 + 152*a1*a5**3*a6/2187 - 5*a1*a5**3/729 - 112*a1*a5**2*a6**3/243 + 424*a1*a5**2*a6**2/729 - 53*a1*a5**2*a6/243 + 35*a1*a5**2/1458 + 8*a1*a5*a6**4/27 - 62*a1*a5*a6**3/81 + 35*a1*a5*a6**2/81 - 31*a1*a5*a6/243 + 7*a1*a5/486 - 4*a1*a6**5/3 + 4*a1*a6**4/3 + 16*a1*a6**3/27 - 26*a1*a6**2/27 + 17*a1*a6/54 - 7*a1/216 - 8*a2**5*a3/3 + 3*a2**5*a4/2 - 4*a2**4*a3*a4/243 + 32*a2**4*a3*a5/81 + 16*a2**4*a3*a6/9 - 46*a2**4*a3/27 - 4*a2**4*a4**2/27 + 4*a2**4*a4*a5/27 - 19*a2**4*a4*a6/9 + 7*a2**4*a4/9 + 20*a2**4*a5*a6/3 - 17*a2**4*a5/6 - 160*a2**3*a3*a5*a6/243 + 56*a2**3*a3*a5/81 + 28*a2**3*a3*a6/27 - 20*a2**3*a3/81 + 40*a2**3*a4**2*a6/729 - 28*a2**3*a4**2/729 - 20*a2**3*a4*a5**2/729 - 20*a2**3*a4*a5*a6/27 + 82*a2**3*a4*a5/243 + 38*a2**3*a4*a6**2/27 - 137*a2**3*a4*a6/81 + 20*a2**3*a4/81 - 8*a2**3*a5**2*a6/81 + 14*a2**3*a5**2/81 - 28*a2**3*a5*a6**2/9 + 26*a2**3*a5*a6/9 - 8*a2**3*a5/9 + 10*a2**3*a6**3 - 28*a2**3*a6**2/3 + 71*a2**3*a6/24 - 7*a2**3/12 - 80*a2**2*a3*a6**3/81 + 320*a2**2*a3*a6**2/243 - 127*a2**2*a3*a6/243 + 20*a2**2*a3/243 - 28*a2**2*a4*a5*a6**2/243 + 142*a2**2*a4*a5*a6/729 - 2*a2**2*a4*a5/243 - 116*a2**2*a4*a6**3/81 + 500*a2**2*a4*a6**2/243 - 58*a2**2*a4*a6/81 + 7*a2**2*a4/81 - 16*a2**2*a5**3*a6/243 + 40*a2**2*a5**3/729 - 64*a2**2*a5**2*a6**2/81 + 44*a2**2*a5**2*a6/81 - 2*a2**2*a5**2/27 + 20*a2**2*a5*a6**3/27 - 113*a2**2*a5*a6**2/81 + 77*a2**2*a5*a6/162 - 4*a2**2*a6**4 + 6*a2**2*a6**3 - 43*a2**2*a6**2/12 + 37*a2**2*a6/36 - a2**2/9 - 32*a2*a4*a6**4/243 + 140*a2*a4*a6**3/729 - 58*a2*a4*a6**2/729 + 10*a2*a4*a6/729 - 56*a2*a5**2*a6**3/243 + 34*a2*a5**2*a6**2/81 - 32*a2*a5**2*a6/243 + 2*a2*a5**2/243 - 200*a2*a5*a6**4/81 + 890*a2*a5*a6**3/243 - 413*a2*a5*a6**2/243 + 73*a2*a5*a6/243 - 7*a2*a5/486 + 8*a2*a6**5/9 - 64*a2*a6**4/27 + 137*a2*a6**3/81 - 77*a2*a6**2/162 + 4*a2*a6/81 - 16*a5*a6**5/81 + 40*a5*a6**4/81 - 236*a5*a6**3/729 + 62*a5*a6**2/729 - 2*a5*a6/243 - 16*a6**6/9 + 104*a6**5/27 - 242*a6**4/81 + 268*a6**3/243 - 97*a6**2/486 + 7*a6/486"
    &#93;,
    &#91;
      "-a0**2*a2*a3**3/18 - a0**2*a2*a3**2*a4/18 + a0**2*a3**2*a4*a6/18 - a0**2*a3**2*a4/324 - 7*a0**2*a3**2*a5**2/162 - 5*a0**2*a3**2*a5*a6/18 + a0**2*a3**2*a5/108 - a0**2*a3*a4**2*a5/486 + 4*a0**2*a3*a4**2*a6/27 - a0**2*a3*a4**2/162 - a0**2*a3*a4*a5**2/27 + 2*a0**2*a4**4/729 + a0**2*a4**3*a5/243 + a0*a1**2*a3**3/18 + a0*a1**2*a3**2*a4/18 - a0*a1*a2*a3**2*a4/6 + 7*a0*a1*a2*a3**2*a5/9 - 23*a0*a1*a2*a3*a4**2/54 - 17*a0*a1*a3**2*a5*a6/54 + 7*a0*a1*a3**2*a5/36 - a0*a1*a3**2*a6/6 + a0*a1*a3**2/18 - a0*a1*a3*a4**2/54 - 2*a0*a1*a3*a4*a5**2/81 - 7*a0*a1*a3*a4*a5*a6/18 + 17*a0*a1*a3*a4*a5/108 + a0*a1*a4**3*a5/81 + 2*a0*a1*a4**3*a6/81 + a0*a1*a4**2*a5**2/81 - a0*a2**2*a3**2*a5/3 + a0*a2**2*a3**2*a6 - a0*a2**2*a3**2/3 + a0*a2**2*a3*a4**2/81 - 11*a0*a2**2*a3*a4*a5/27 - 7*a0*a2*a3**2*a6**2/6 + 49*a0*a2*a3**2*a6/54 - 73*a0*a2*a3**2/648 - 2*a0*a2*a3*a4*a5*a6/27 - 47*a0*a2*a3*a4*a5/324 - 5*a0*a2*a3*a4*a6**2/6 + 47*a0*a2*a3*a4*a6/108 - 2*a0*a2*a3*a4/81 - a0*a2*a3*a5**3/81 - a0*a2*a3*a5**2*a6/3 - 11*a0*a2*a3*a5**2/81 - 2*a0*a2*a4**3*a6/243 + 35*a0*a2*a4**3/729 + a0*a2*a4**2*a5**2/81 + a0*a2*a4**2*a5*a6/81 + 35*a0*a2*a4**2*a5/486 + a0*a2*a4*a5**3/81 - 7*a0*a3*a4*a6**3/27 - 4*a0*a3*a4*a6**2/27 + 17*a0*a3*a4*a6/108 - 7*a0*a3*a4/324 + a0*a3*a5**2*a6**2/81 - a0*a3*a5**2*a6/81 - 5*a0*a3*a5**2/648 - 5*a0*a3*a5*a6**3/9 - 4*a0*a3*a5*a6**2/27 + 7*a0*a3*a5*a6/36 - 7*a0*a3*a5/216 - a0*a4**2*a5*a6**2/243 + 19*a0*a4**2*a5*a6/243 - a0*a4**2*a5/54 - 2*a0*a4**2*a6**3/27 - 5*a0*a4**2*a6**2/81 + a0*a4**2*a6/27 + a0*a4*a5**3*a6/243 - 13*a0*a4*a5**3/972 + a0*a4*a5**2*a6**2/27 + 49*a0*a4*a5**2*a6/324 - a0*a4*a5**2/27 - 2*a0*a5**4/81 + a1**3*a3**2*a4/9 - a1**3*a3**2*a5/3 + 2*a1**3*a3*a4**2/9 + a1**2*a2*a3**2*a5/3 - a1**2*a2*a3**2*a6/2 + a1**2*a2*a3**2/4 + 7*a1**2*a2*a3*a4*a5/18 - 4*a1**2*a3**2*a6**2/9 + a1**2*a3**2*a6/2 - 7*a1**2*a3**2/54 + 7*a1**2*a3*a4*a5/54 - 10*a1**2*a3*a4*a6**2/9 + 2*a1**2*a3*a4*a6/3 - 11*a1**2*a3*a4/108 - a1**2*a3*a5**3/54 + a1**2*a3*a5**2*a6/6 + 19*a1**2*a3*a5**2/108 - 10*a1**2*a4**3/243 + a1**2*a4**2*a5**2/81 + 2*a1**2*a4**2*a5*a6/27 - 5*a1**2*a4**2*a5/81 + 13*a1*a2**2*a3**2*a6/9 - 37*a1*a2**2*a3**2/54 + 2*a1*a2**2*a3*a4*a5/27 + 16*a1*a2**2*a3*a4*a6/9 - 14*a1*a2**2*a3*a4/27 + 2*a1*a2**2*a3*a5**2/27 - 2*a1*a2**2*a4**3/243 - a1*a2**2*a4**2*a5/81 + 4*a1*a2*a3*a4*a6**2/9 + 91*a1*a2*a3*a4*a6/162 - 11*a1*a2*a3*a4/54 - 5*a1*a2*a3*a5**2*a6/27 + 5*a1*a2*a3*a5**2/108 + a1*a2*a3*a5*a6**2/9 + 5*a1*a2*a3*a5*a6/4 - 5*a1*a2*a3*a5/24 - a1*a2*a4**2*a5*a6/81 - 35*a1*a2*a4**2*a5/486 + 2*a1*a2*a4**2*a6**2/27 + 5*a1*a2*a4**2*a6/81 - a1*a2*a4**2/18 + 2*a1*a2*a4*a5**3/81 + a1*a2*a4*a5**2*a6/9 - 10*a1*a2*a4*a5**2/81 - a1*a3*a5*a6**3/27 + 2*a1*a3*a5*a6**2/27 - 25*a1*a3*a5*a6/324 + a1*a3*a5/36 + a1*a3*a6**3/3 - 7*a1*a3*a6**2/36 + a1*a3*a6/24 - a1*a3/216 + 4*a1*a4**2*a6**3/81 + 16*a1*a4**2*a6**2/81 - 41*a1*a4**2*a6/486 + 2*a1*a4**2/243 - a1*a4*a5**2*a6**2/27 - 16*a1*a4*a5**2*a6/243 + 7*a1*a4*a5**2/486 + 11*a1*a4*a5*a6**2/27 - 71*a1*a4*a5*a6/324 + 13*a1*a4*a5/324 + a1*a5**4*a6/81 - a1*a5**4/972 + a1*a5**3*a6**2/27 - 43*a1*a5**3*a6/324 + 23*a1*a5**3/648 - 7*a2**4*a3**2/18 - 7*a2**4*a3*a4/18 - 2*a2**3*a3*a4*a6/27 - 37*a2**3*a3*a4/81 + 23*a2**3*a3*a5**2/162 + 5*a2**3*a3*a5*a6/6 - 139*a2**3*a3*a5/108 - 5*a2**3*a4**2*a5/243 - 2*a2**3*a4**2*a6/27 + a2**3*a4**2/9 - a2**3*a4*a5**2/81 + 7*a2**2*a3*a5*a6**2/54 + 8*a2**2*a3*a5*a6/81 - 41*a2**2*a3*a5/216 + 3*a2**2*a3*a6**3/2 - 9*a2**2*a3*a6**2/4 + a2**2*a3*a6 - 37*a2**2*a3/216 - 2*a2**2*a4**2*a6**2/81 - 8*a2**2*a4**2*a6/27 + 23*a2**2*a4**2/243 - 2*a2**2*a4*a5**2*a6/243 - 23*a2**2*a4*a5**2/972 + a2**2*a4*a5*a6**2/9 - 49*a2**2*a4*a5*a6/324 - 2*a2**2*a4*a5/81 + 4*a2**2*a5**4/243 + 4*a2**2*a5**3*a6/81 - 5*a2**2*a5**3/54 - a2*a3*a6**4/9 + 37*a2*a3*a6**3/54 - 305*a2*a3*a6**2/324 + 239*a2*a3*a6/648 - 25*a2*a3/648 - a2*a4*a5*a6**3/9 - 157*a2*a4*a5*a6**2/486 + 215*a2*a4*a5*a6/972 - 7*a2*a4*a5/243 + 2*a2*a4*a6**4/9 + 2*a2*a4*a6**3/27 - 43*a2*a4*a6**2/162 + 7*a2*a4*a6/108 + 2*a2*a5**3*a6**2/27 - 19*a2*a5**3*a6/972 - a2*a5**3/108 + 2*a2*a5**2*a6**3/9 - 221*a2*a5**2*a6**2/324 + 65*a2*a5**2*a6/216 - 7*a2*a5**2/648 - 4*a4*a6**5/27 - 8*a4*a6**4/81 + 25*a4*a6**3/162 - 13*a4*a6**2/324 + a4*a6/324 + 2*a5**2*a6**4/27 - 2*a5**2*a6**3/27 + a5**2*a6**2/36 - a5**2*a6/162 + 2*a5*a6**5/9 - 20*a5*a6**4/27 + 7*a5*a6**3/12 - 37*a5*a6**2/216 + a5*a6/54",
      "-a0**2*a2*a3**3/4 + a0**2*a3**2*a4*a6/4 - a0**2*a3**2*a4/72 - 7*a0**2*a3**2*a5**2/36 - a0**2*a3*a4**2*a5/108 + a0**2*a4**4/81 + a0*a1**2*a3**3/4 - 3*a0*a1*a2*a3**2*a4/4 - 17*a0*a1*a3**2*a5*a6/12 + 7*a0*a1*a3**2*a5/8 - a0*a1*a3*a4**2/12 - a0*a1*a3*a4*a5**2/9 + a0*a1*a4**3*a5/18 - 3*a0*a2**2*a3**2*a5/2 + a0*a2**2*a3*a4**2/18 - 21*a0*a2*a3**2*a6**2/4 + 49*a0*a2*a3**2*a6/12 - 73*a0*a2*a3**2/144 - a0*a2*a3*a4*a5*a6/3 - 47*a0*a2*a3*a4*a5/72 - a0*a2*a3*a5**3/18 - a0*a2*a4**3*a6/27 + 35*a0*a2*a4**3/162 + a0*a2*a4**2*a5**2/18 - 7*a0*a3*a4*a6**3/6 - 2*a0*a3*a4*a6**2/3 + 17*a0*a3*a4*a6/24 - 7*a0*a3*a4/72 + a0*a3*a5**2*a6**2/18 - a0*a3*a5**2*a6/18 - 5*a0*a3*a5**2/144 - a0*a4**2*a5*a6**2/54 + 19*a0*a4**2*a5*a6/54 - a0*a4**2*a5/12 + a0*a4*a5**3*a6/54 - 13*a0*a4*a5**3/216 + a1**3*a3**2*a4/2 + 3*a1**2*a2*a3**2*a5/2 - 2*a1**2*a3**2*a6**2 + 9*a1**2*a3**2*a6/4 - 7*a1**2*a3**2/12 + 7*a1**2*a3*a4*a5/12 - a1**2*a3*a5**3/12 - 5*a1**2*a4**3/27 + a1**2*a4**2*a5**2/18 + 13*a1*a2**2*a3**2*a6/2 - 37*a1*a2**2*a3**2/12 + a1*a2**2*a3*a4*a5/3 - a1*a2**2*a4**3/27 + 2*a1*a2*a3*a4*a6**2 + 91*a1*a2*a3*a4*a6/36 - 11*a1*a2*a3*a4/12 - 5*a1*a2*a3*a5**2*a6/6 + 5*a1*a2*a3*a5**2/24 - a1*a2*a4**2*a5*a6/18 - 35*a1*a2*a4**2*a5/108 + a1*a2*a4*a5**3/9 - a1*a3*a5*a6**3/6 + a1*a3*a5*a6**2/3 - 25*a1*a3*a5*a6/72 + a1*a3*a5/8 + 2*a1*a4**2*a6**3/9 + 8*a1*a4**2*a6**2/9 - 41*a1*a4**2*a6/108 + a1*a4**2/27 - a1*a4*a5**2*a6**2/6 - 8*a1*a4*a5**2*a6/27 + 7*a1*a4*a5**2/108 + a1*a5**4*a6/18 - a1*a5**4/216 - 7*a2**4*a3**2/4 - a2**3*a3*a4*a6/3 - 37*a2**3*a3*a4/18 + 23*a2**3*a3*a5**2/36 - 5*a2**3*a4**2*a5/54 + 7*a2**2*a3*a5*a6**2/12 + 4*a2**2*a3*a5*a6/9 - 41*a2**2*a3*a5/48 - a2**2*a4**2*a6**2/9 - 4*a2**2*a4**2*a6/3 + 23*a2**2*a4**2/54 - a2**2*a4*a5**2*a6/27 - 23*a2**2*a4*a5**2/216 + 2*a2**2*a5**4/27 - a2*a3*a6**4/2 + 37*a2*a3*a6**3/12 - 305*a2*a3*a6**2/72 + 239*a2*a3*a6/144 - 25*a2*a3/144 - a2*a4*a5*a6**3/2 - 157*a2*a4*a5*a6**2/108 + 215*a2*a4*a5*a6/216 - 7*a2*a4*a5/54 + a2*a5**3*a6**2/3 - 19*a2*a5**3*a6/216 - a2*a5**3/24 - 2*a4*a6**5/3 - 4*a4*a6**4/9 + 25*a4*a6**3/36 - 13*a4*a6**2/72 + a4*a6/72 + a5**2*a6**4/3 - a5**2*a6**3/3 + a5**2*a6**2/8 - a5**2*a6/36",
      "a0**2*a2*a3**3/27 + a0**2*a2*a3**2*a4/27 + 2*a0**2*a2*a3**2*a5/9 - a0**2*a2*a3*a4**2/18 - a0**2*a3**2*a4*a6/27 + a0**2*a3**2*a4/486 + 7*a0**2*a3**2*a5**2/243 + 5*a0**2*a3**2*a5*a6/27 - a0**2*a3**2*a5/162 + 4*a0**2*a3**2*a6**2/3 - 5*a0**2*a3**2*a6/9 + 7*a0**2*a3**2/108 + a0**2*a3*a4**2*a5/729 - 8*a0**2*a3*a4**2*a6/81 + a0**2*a3*a4**2/243 + 2*a0**2*a3*a4*a5**2/81 - 5*a0**2*a3*a4*a5*a6/18 + 13*a0**2*a3*a4*a5/324 + 5*a0**2*a3*a5**3/81 - 4*a0**2*a4**4/2187 - 2*a0**2*a4**3*a5/729 - 2*a0**2*a4**3*a6/81 + 2*a0**2*a4**3/243 + a0**2*a4**2*a5**2/243 - a0*a1**2*a3**3/27 - a0*a1**2*a3**2*a4/27 - a0*a1**2*a3**2*a5/18 + a0*a1*a2*a3**2*a4/9 - 14*a0*a1*a2*a3**2*a5/27 - 7*a0*a1*a2*a3**2*a6/3 + 4*a0*a1*a2*a3**2/9 + 23*a0*a1*a2*a3*a4**2/81 + 17*a0*a1*a2*a3*a4*a5/54 + a0*a1*a2*a4**3/27 + 17*a0*a1*a3**2*a5*a6/81 - 7*a0*a1*a3**2*a5/54 + a0*a1*a3**2*a6/9 - a0*a1*a3**2/27 + a0*a1*a3*a4**2/81 + 4*a0*a1*a3*a4*a5**2/243 + 7*a0*a1*a3*a4*a5*a6/27 - 17*a0*a1*a3*a4*a5/162 - a0*a1*a3*a4*a6**2/9 + a0*a1*a3*a4*a6/27 + a0*a1*a3*a4/108 + 17*a0*a1*a3*a5**2*a6/54 - 17*a0*a1*a3*a5**2/108 - 2*a0*a1*a4**3*a5/243 - 4*a0*a1*a4**3*a6/243 - 2*a0*a1*a4**2*a5**2/243 - 5*a0*a1*a4**2*a5*a6/81 + a0*a1*a4**2*a5/54 + a0*a1*a4*a5**3/81 + a0*a2**3*a3**2 + 2*a0*a2**2*a3**2*a5/9 - 2*a0*a2**2*a3**2*a6/3 + 2*a0*a2**2*a3**2/9 - 2*a0*a2**2*a3*a4**2/243 + 22*a0*a2**2*a3*a4*a5/81 + 2*a0*a2**2*a3*a4*a6/9 - 11*a0*a2**2*a3*a4/108 + 4*a0*a2**2*a3*a5**2/9 + a0*a2**2*a4**2*a5/27 + 7*a0*a2*a3**2*a6**2/9 - 49*a0*a2*a3**2*a6/81 + 73*a0*a2*a3**2/972 + 4*a0*a2*a3*a4*a5*a6/81 + 47*a0*a2*a3*a4*a5/486 + 5*a0*a2*a3*a4*a6**2/9 - 47*a0*a2*a3*a4*a6/162 + 4*a0*a2*a3*a4/243 + 2*a0*a2*a3*a5**3/243 + 2*a0*a2*a3*a5**2*a6/9 + 22*a0*a2*a3*a5**2/243 + 5*a0*a2*a3*a5*a6**2/2 - 8*a0*a2*a3*a5*a6/9 + 11*a0*a2*a3*a5/216 + 4*a0*a2*a4**3*a6/729 - 70*a0*a2*a4**3/2187 - 2*a0*a2*a4**2*a5**2/243 - 2*a0*a2*a4**2*a5*a6/243 - 35*a0*a2*a4**2*a5/729 - a0*a2*a4**2*a6**2/27 - 41*a0*a2*a4**2*a6/162 + 25*a0*a2*a4**2/486 - 2*a0*a2*a4*a5**3/243 - a0*a2*a4*a5**2*a6/27 + 43*a0*a2*a4*a5**2/972 + a0*a2*a5**4/81 + 14*a0*a3*a4*a6**3/81 + 8*a0*a3*a4*a6**2/81 - 17*a0*a3*a4*a6/162 + 7*a0*a3*a4/486 - 2*a0*a3*a5**2*a6**2/243 + 2*a0*a3*a5**2*a6/243 + 5*a0*a3*a5**2/972 + 10*a0*a3*a5*a6**3/27 + 8*a0*a3*a5*a6**2/81 - 7*a0*a3*a5*a6/54 + 7*a0*a3*a5/324 + 8*a0*a3*a6**4/3 - 13*a0*a3*a6**3/9 + 11*a0*a3*a6**2/108 + 13*a0*a3*a6/216 - a0*a3/108 + 2*a0*a4**2*a5*a6**2/729 - 38*a0*a4**2*a5*a6/729 + a0*a4**2*a5/81 + 4*a0*a4**2*a6**3/81 + 10*a0*a4**2*a6**2/243 - 2*a0*a4**2*a6/81 - 2*a0*a4*a5**3*a6/729 + 13*a0*a4*a5**3/1458 - 2*a0*a4*a5**2*a6**2/81 - 49*a0*a4*a5**2*a6/486 + 2*a0*a4*a5**2/81 - a0*a4*a5*a6**3/9 - 31*a0*a4*a5*a6**2/162 + 25*a0*a4*a5*a6/324 - a0*a4*a5/108 + 4*a0*a5**4/243 + 2*a0*a5**3*a6**2/81 + a0*a5**3*a6/27 - a0*a5**3/216 - 2*a1**3*a3**2*a4/27 + 2*a1**3*a3**2*a5/9 + a1**3*a3**2*a6 - a1**3*a3**2/6 - 4*a1**3*a3*a4**2/27 - 2*a1**3*a3*a4*a5/9 - a1**2*a2**2*a3**2/2 - 2*a1**2*a2*a3**2*a5/9 + a1**2*a2*a3**2*a6/3 - a1**2*a2*a3**2/6 - 7*a1**2*a2*a3*a4*a5/27 - 2*a1**2*a2*a3*a4*a6/3 + 2*a1**2*a2*a3*a4/9 - 5*a1**2*a2*a3*a5**2/9 + a1**2*a2*a4**2*a5/9 + 8*a1**2*a3**2*a6**2/27 - a1**2*a3**2*a6/3 + 7*a1**2*a3**2/81 - 7*a1**2*a3*a4*a5/81 + 20*a1**2*a3*a4*a6**2/27 - 4*a1**2*a3*a4*a6/9 + 11*a1**2*a3*a4/162 + a1**2*a3*a5**3/81 - a1**2*a3*a5**2*a6/9 - 19*a1**2*a3*a5**2/162 - 5*a1**2*a3*a5*a6**2/9 - 4*a1**2*a3*a5*a6/9 + a1**2*a3*a5/6 + 20*a1**2*a4**3/729 - 2*a1**2*a4**2*a5**2/243 - 4*a1**2*a4**2*a5*a6/81 + 10*a1**2*a4**2*a5/243 + 2*a1**2*a4**2*a6/9 - 4*a1**2*a4**2/81 + a1**2*a4*a5**2*a6/27 - 7*a1**2*a4*a5**2/162 + a1*a2**3*a3*a4/3 - 26*a1*a2**2*a3**2*a6/27 + 37*a1*a2**2*a3**2/81 - 4*a1*a2**2*a3*a4*a5/81 - 32*a1*a2**2*a3*a4*a6/27 + 28*a1*a2**2*a3*a4/81 - 4*a1*a2**2*a3*a5**2/81 - 3*a1*a2**2*a3*a5*a6 + 73*a1*a2**2*a3*a5/108 + 4*a1*a2**2*a4**3/729 + 2*a1*a2**2*a4**2*a5/243 + 5*a1*a2**2*a4**2*a6/27 + 4*a1*a2**2*a4**2/81 + 17*a1*a2**2*a4*a5**2/81 - 8*a1*a2*a3*a4*a6**2/27 - 91*a1*a2*a3*a4*a6/243 + 11*a1*a2*a3*a4/81 + 10*a1*a2*a3*a5**2*a6/81 - 5*a1*a2*a3*a5**2/162 - 2*a1*a2*a3*a5*a6**2/27 - 5*a1*a2*a3*a5*a6/6 + 5*a1*a2*a3*a5/36 - 13*a1*a2*a3*a6**3/3 - 13*a1*a2*a3*a6**2/18 + 11*a1*a2*a3*a6/12 - 5*a1*a2*a3/36 + 2*a1*a2*a4**2*a5*a6/243 + 35*a1*a2*a4**2*a5/729 - 4*a1*a2*a4**2*a6**2/81 - 10*a1*a2*a4**2*a6/243 + a1*a2*a4**2/27 - 4*a1*a2*a4*a5**3/243 - 2*a1*a2*a4*a5**2*a6/27 + 20*a1*a2*a4*a5**2/243 + 4*a1*a2*a4*a5*a6**2/27 + 47*a1*a2*a4*a5*a6/162 - 4*a1*a2*a4*a5/81 + 4*a1*a2*a5**3*a6/27 - 29*a1*a2*a5**3/324 + 2*a1*a3*a5*a6**3/81 - 4*a1*a3*a5*a6**2/81 + 25*a1*a3*a5*a6/486 - a1*a3*a5/54 - 2*a1*a3*a6**3/9 + 7*a1*a3*a6**2/54 - a1*a3*a6/36 + a1*a3/324 - 8*a1*a4**2*a6**3/243 - 32*a1*a4**2*a6**2/243 + 41*a1*a4**2*a6/729 - 4*a1*a4**2/729 + 2*a1*a4*a5**2*a6**2/81 + 32*a1*a4*a5**2*a6/729 - 7*a1*a4*a5**2/729 - 22*a1*a4*a5*a6**2/81 + 71*a1*a4*a5*a6/486 - 13*a1*a4*a5/486 - 4*a1*a4*a6**4/9 - 20*a1*a4*a6**3/27 + 11*a1*a4*a6**2/18 - 13*a1*a4*a6/81 + 5*a1*a4/324 - 2*a1*a5**4*a6/243 + a1*a5**4/1458 - 2*a1*a5**3*a6**2/81 + 43*a1*a5**3*a6/486 - 23*a1*a5**3/972 + 7*a1*a5**2*a6**3/27 + 5*a1*a5**2*a6**2/54 - 2*a1*a5**2*a6/27 + a1*a5**2/216 + 7*a2**4*a3**2/27 + 7*a2**4*a3*a4/27 + 14*a2**4*a3*a5/9 - a2**4*a4**2/9 + 4*a2**3*a3*a4*a6/81 + 74*a2**3*a3*a4/243 - 23*a2**3*a3*a5**2/243 - 5*a2**3*a3*a5*a6/9 + 139*a2**3*a3*a5/162 + 5*a2**3*a3*a6**2/2 + 7*a2**3*a3*a6/9 - 25*a2**3*a3/108 + 10*a2**3*a4**2*a5/729 + 4*a2**3*a4**2*a6/81 - 2*a2**3*a4**2/27 + 2*a2**3*a4*a5**2/243 + 7*a2**3*a4*a5*a6/27 - 5*a2**3*a4*a5/324 + 11*a2**3*a5**3/81 - 7*a2**2*a3*a5*a6**2/81 - 16*a2**2*a3*a5*a6/243 + 41*a2**2*a3*a5/324 - a2**2*a3*a6**3 + 3*a2**2*a3*a6**2/2 - 2*a2**2*a3*a6/3 + 37*a2**2*a3/324 + 4*a2**2*a4**2*a6**2/243 + 16*a2**2*a4**2*a6/81 - 46*a2**2*a4**2/729 + 4*a2**2*a4*a5**2*a6/729 + 23*a2**2*a4*a5**2/1458 - 2*a2**2*a4*a5*a6**2/27 + 49*a2**2*a4*a5*a6/486 + 4*a2**2*a4*a5/243 + 5*a2**2*a4*a6**3/9 + 53*a2**2*a4*a6**2/54 - 67*a2**2*a4*a6/108 + 23*a2**2*a4/324 - 8*a2**2*a5**4/729 - 8*a2**2*a5**3*a6/243 + 5*a2**2*a5**3/81 + a2**2*a5**2*a6**2 - 181*a2**2*a5**2*a6/324 + 97*a2**2*a5**2/648 + 2*a2*a3*a6**4/27 - 37*a2*a3*a6**3/81 + 305*a2*a3*a6**2/486 - 239*a2*a3*a6/972 + 25*a2*a3/972 + 2*a2*a4*a5*a6**3/27 + 157*a2*a4*a5*a6**2/729 - 215*a2*a4*a5*a6/1458 + 14*a2*a4*a5/729 - 4*a2*a4*a6**4/27 - 4*a2*a4*a6**3/81 + 43*a2*a4*a6**2/243 - 7*a2*a4*a6/162 - 4*a2*a5**3*a6**2/81 + 19*a2*a5**3*a6/1458 + a2*a5**3/162 - 4*a2*a5**2*a6**3/27 + 221*a2*a5**2*a6**2/486 - 65*a2*a5**2*a6/324 + 7*a2*a5**2/972 + 19*a2*a5*a6**4/9 - 10*a2*a5*a6**3/9 + a2*a5*a6**2/6 - 19*a2*a5*a6/324 + 7*a2*a5/648 + 8*a4*a6**5/81 + 16*a4*a6**4/243 - 25*a4*a6**3/243 + 13*a4*a6**2/486 - a4*a6/486 - 4*a5**2*a6**4/81 + 4*a5**2*a6**3/81 - a5**2*a6**2/54 + a5**2*a6/243 - 4*a5*a6**5/27 + 40*a5*a6**4/81 - 7*a5*a6**3/18 + 37*a5*a6**2/324 - a5*a6/81 + 4*a6**6/3 - 8*a6**5/9 - 7*a6**4/54 + 23*a6**3/108 - a6**2/18 + a6/216",
      "a0**2*a1*a3**2*a5/6 - a0**2*a1*a3*a4**2/18 - 2*a0**2*a2*a3**3/81 - 2*a0**2*a2*a3**2*a4/81 - 4*a0**2*a2*a3**2*a5/27 + 7*a0**2*a2*a3**2*a6/6 - 5*a0**2*a2*a3**2/18 + a0**2*a2*a3*a4**2/27 - 2*a0**2*a2*a3*a4*a5/27 - 2*a0**2*a2*a4**3/81 + 2*a0**2*a3**2*a4*a6/81 - a0**2*a3**2*a4/729 - 14*a0**2*a3**2*a5**2/729 - 10*a0**2*a3**2*a5*a6/81 + a0**2*a3**2*a5/243 - 8*a0**2*a3**2*a6**2/9 + 10*a0**2*a3**2*a6/27 - 7*a0**2*a3**2/162 - 2*a0**2*a3*a4**2*a5/2187 + 16*a0**2*a3*a4**2*a6/243 - 2*a0**2*a3*a4**2/729 - 4*a0**2*a3*a4*a5**2/243 + 5*a0**2*a3*a4*a5*a6/27 - 13*a0**2*a3*a4*a5/486 + 11*a0**2*a3*a4*a6**2/18 - 29*a0**2*a3*a4*a6/108 + a0**2*a3*a4/36 - 10*a0**2*a3*a5**3/243 - 5*a0**2*a3*a5**2*a6/27 + a0**2*a3*a5**2/18 + 8*a0**2*a4**4/6561 + 4*a0**2*a4**3*a5/2187 + 4*a0**2*a4**3*a6/243 - 4*a0**2*a4**3/729 - 2*a0**2*a4**2*a5**2/729 - a0**2*a4**2*a5*a6/81 + 2*a0*a1**2*a3**3/81 + 2*a0*a1**2*a3**2*a4/81 + a0*a1**2*a3**2*a5/27 + a0*a1**2*a3**2*a6/6 - a0*a1**2*a3*a4*a5/9 + a0*a1**2*a4**3/27 - 4*a0*a1*a2**2*a3**2/3 - 2*a0*a1*a2*a3**2*a4/27 + 28*a0*a1*a2*a3**2*a5/81 + 14*a0*a1*a2*a3**2*a6/9 - 8*a0*a1*a2*a3**2/27 - 46*a0*a1*a2*a3*a4**2/243 - 17*a0*a1*a2*a3*a4*a5/81 - 19*a0*a1*a2*a3*a4*a6/18 + 11*a0*a1*a2*a3*a4/36 - 2*a0*a1*a2*a4**3/81 - a0*a1*a2*a4**2*a5/27 - 34*a0*a1*a3**2*a5*a6/243 + 7*a0*a1*a3**2*a5/81 - 2*a0*a1*a3**2*a6/27 + 2*a0*a1*a3**2/81 - 2*a0*a1*a3*a4**2/243 - 8*a0*a1*a3*a4*a5**2/729 - 14*a0*a1*a3*a4*a5*a6/81 + 17*a0*a1*a3*a4*a5/243 + 2*a0*a1*a3*a4*a6**2/27 - 2*a0*a1*a3*a4*a6/81 - a0*a1*a3*a4/162 - 17*a0*a1*a3*a5**2*a6/81 + 17*a0*a1*a3*a5**2/162 - 11*a0*a1*a3*a5*a6**2/18 + 7*a0*a1*a3*a5*a6/12 - a0*a1*a3*a5/9 + 4*a0*a1*a4**3*a5/729 + 8*a0*a1*a4**3*a6/729 + 4*a0*a1*a4**2*a5**2/729 + 10*a0*a1*a4**2*a5*a6/243 - a0*a1*a4**2*a5/81 - 4*a0*a1*a4**2*a6**2/27 + 2*a0*a1*a4**2*a6/27 - a0*a1*a4**2/54 - 2*a0*a1*a4*a5**3/243 - a0*a1*a4*a5**2/108 - 2*a0*a2**3*a3**2/3 - a0*a2**3*a3*a4/9 - 4*a0*a2**2*a3**2*a5/27 + 4*a0*a2**2*a3**2*a6/9 - 4*a0*a2**2*a3**2/27 + 4*a0*a2**2*a3*a4**2/729 - 44*a0*a2**2*a3*a4*a5/243 - 4*a0*a2**2*a3*a4*a6/27 + 11*a0*a2**2*a3*a4/162 - 8*a0*a2**2*a3*a5**2/27 - a0*a2**2*a3*a5*a6/3 + 17*a0*a2**2*a3*a5/27 - 2*a0*a2**2*a4**2*a5/81 + 2*a0*a2**2*a4**2*a6/27 - 43*a0*a2**2*a4**2/162 - 2*a0*a2**2*a4*a5**2/27 - 14*a0*a2*a3**2*a6**2/27 + 98*a0*a2*a3**2*a6/243 - 73*a0*a2*a3**2/1458 - 8*a0*a2*a3*a4*a5*a6/243 - 47*a0*a2*a3*a4*a5/729 - 10*a0*a2*a3*a4*a6**2/27 + 47*a0*a2*a3*a4*a6/243 - 8*a0*a2*a3*a4/729 - 4*a0*a2*a3*a5**3/729 - 4*a0*a2*a3*a5**2*a6/27 - 44*a0*a2*a3*a5**2/729 - 5*a0*a2*a3*a5*a6**2/3 + 16*a0*a2*a3*a5*a6/27 - 11*a0*a2*a3*a5/324 - 5*a0*a2*a3*a6**3/6 + 7*a0*a2*a3*a6**2/3 - 193*a0*a2*a3*a6/216 + 7*a0*a2*a3/72 - 8*a0*a2*a4**3*a6/2187 + 140*a0*a2*a4**3/6561 + 4*a0*a2*a4**2*a5**2/729 + 4*a0*a2*a4**2*a5*a6/729 + 70*a0*a2*a4**2*a5/2187 + 2*a0*a2*a4**2*a6**2/81 + 41*a0*a2*a4**2*a6/243 - 25*a0*a2*a4**2/729 + 4*a0*a2*a4*a5**3/729 + 2*a0*a2*a4*a5**2*a6/81 - 43*a0*a2*a4*a5**2/1458 - 2*a0*a2*a4*a5*a6**2/27 - 65*a0*a2*a4*a5*a6/162 + 5*a0*a2*a4*a5/54 - 2*a0*a2*a5**4/243 - a0*a2*a5**3*a6/27 + a0*a2*a5**3/18 - 28*a0*a3*a4*a6**3/243 - 16*a0*a3*a4*a6**2/243 + 17*a0*a3*a4*a6/243 - 7*a0*a3*a4/729 + 4*a0*a3*a5**2*a6**2/729 - 4*a0*a3*a5**2*a6/729 - 5*a0*a3*a5**2/1458 - 20*a0*a3*a5*a6**3/81 - 16*a0*a3*a5*a6**2/243 + 7*a0*a3*a5*a6/81 - 7*a0*a3*a5/486 - 16*a0*a3*a6**4/9 + 26*a0*a3*a6**3/27 - 11*a0*a3*a6**2/162 - 13*a0*a3*a6/324 + a0*a3/162 - 4*a0*a4**2*a5*a6**2/2187 + 76*a0*a4**2*a5*a6/2187 - 2*a0*a4**2*a5/243 - 8*a0*a4**2*a6**3/243 - 20*a0*a4**2*a6**2/729 + 4*a0*a4**2*a6/243 + 4*a0*a4*a5**3*a6/2187 - 13*a0*a4*a5**3/2187 + 4*a0*a4*a5**2*a6**2/243 + 49*a0*a4*a5**2*a6/729 - 4*a0*a4*a5**2/243 + 2*a0*a4*a5*a6**3/27 + 31*a0*a4*a5*a6**2/243 - 25*a0*a4*a5*a6/486 + a0*a4*a5/162 + a0*a4*a6**4/9 - 11*a0*a4*a6**3/27 + 37*a0*a4*a6**2/108 - 11*a0*a4*a6/108 + a0*a4/108 - 8*a0*a5**4/729 - 4*a0*a5**3*a6**2/243 - 2*a0*a5**3*a6/81 + a0*a5**3/324 - 2*a0*a5**2*a6**3/27 + 2*a0*a5**2*a6**2/27 - a0*a5**2*a6/24 + a0*a5**2/108 + a1**3*a2*a3**2/2 + 4*a1**3*a3**2*a4/81 - 4*a1**3*a3**2*a5/27 - 2*a1**3*a3**2*a6/3 + a1**3*a3**2/9 + 8*a1**3*a3*a4**2/81 + 4*a1**3*a3*a4*a5/27 - a1**3*a3*a5**2/6 + a1**3*a4**2*a5/9 + a1**2*a2**2*a3**2/3 + a1**2*a2**2*a3*a4/3 + 4*a1**2*a2*a3**2*a5/27 - 2*a1**2*a2*a3**2*a6/9 + a1**2*a2*a3**2/9 + 14*a1**2*a2*a3*a4*a5/81 + 4*a1**2*a2*a3*a4*a6/9 - 4*a1**2*a2*a3*a4/27 + 10*a1**2*a2*a3*a5**2/27 - 7*a1**2*a2*a3*a5*a6/6 - 7*a1**2*a2*a3*a5/12 - 2*a1**2*a2*a4**2*a5/27 + a1**2*a2*a4**2*a6/9 + 5*a1**2*a2*a4**2/18 + 2*a1**2*a2*a4*a5**2/9 - 16*a1**2*a3**2*a6**2/81 + 2*a1**2*a3**2*a6/9 - 14*a1**2*a3**2/243 + 14*a1**2*a3*a4*a5/243 - 40*a1**2*a3*a4*a6**2/81 + 8*a1**2*a3*a4*a6/27 - 11*a1**2*a3*a4/243 - 2*a1**2*a3*a5**3/243 + 2*a1**2*a3*a5**2*a6/27 + 19*a1**2*a3*a5**2/243 + 10*a1**2*a3*a5*a6**2/27 + 8*a1**2*a3*a5*a6/27 - a1**2*a3*a5/9 - 4*a1**2*a3*a6**3/3 + 2*a1**2*a3*a6**2 - 8*a1**2*a3*a6/9 + a1**2*a3/9 - 40*a1**2*a4**3/2187 + 4*a1**2*a4**2*a5**2/729 + 8*a1**2*a4**2*a5*a6/243 - 20*a1**2*a4**2*a5/729 - 4*a1**2*a4**2*a6/27 + 8*a1**2*a4**2/243 - 2*a1**2*a4*a5**2*a6/81 + 7*a1**2*a4*a5**2/243 - 2*a1**2*a4*a5*a6**2/9 + 2*a1**2*a4*a5*a6/27 - a1**2*a4*a5/36 + a1**2*a5**3*a6/9 - a1**2*a5**3/108 - 2*a1*a2**3*a3*a4/9 + 17*a1*a2**3*a3*a5/18 - a1*a2**3*a4**2/27 + 52*a1*a2**2*a3**2*a6/81 - 74*a1*a2**2*a3**2/243 + 8*a1*a2**2*a3*a4*a5/243 + 64*a1*a2**2*a3*a4*a6/81 - 56*a1*a2**2*a3*a4/243 + 8*a1*a2**2*a3*a5**2/243 + 2*a1*a2**2*a3*a5*a6 - 73*a1*a2**2*a3*a5/162 + 3*a1*a2**2*a3*a6**2/2 - 65*a1*a2**2*a3*a6/9 + 29*a1*a2**2*a3/18 - 8*a1*a2**2*a4**3/2187 - 4*a1*a2**2*a4**2*a5/729 - 10*a1*a2**2*a4**2*a6/81 - 8*a1*a2**2*a4**2/243 - 34*a1*a2**2*a4*a5**2/243 + 13*a1*a2**2*a4*a5*a6/27 + 53*a1*a2**2*a4*a5/108 + 4*a1*a2**2*a5**3/27 + 16*a1*a2*a3*a4*a6**2/81 + 182*a1*a2*a3*a4*a6/729 - 22*a1*a2*a3*a4/243 - 20*a1*a2*a3*a5**2*a6/243 + 5*a1*a2*a3*a5**2/243 + 4*a1*a2*a3*a5*a6**2/81 + 5*a1*a2*a3*a5*a6/9 - 5*a1*a2*a3*a5/54 + 26*a1*a2*a3*a6**3/9 + 13*a1*a2*a3*a6**2/27 - 11*a1*a2*a3*a6/18 + 5*a1*a2*a3/54 - 4*a1*a2*a4**2*a5*a6/729 - 70*a1*a2*a4**2*a5/2187 + 8*a1*a2*a4**2*a6**2/243 + 20*a1*a2*a4**2*a6/729 - 2*a1*a2*a4**2/81 + 8*a1*a2*a4*a5**3/729 + 4*a1*a2*a4*a5**2*a6/81 - 40*a1*a2*a4*a5**2/729 - 8*a1*a2*a4*a5*a6**2/81 - 47*a1*a2*a4*a5*a6/243 + 8*a1*a2*a4*a5/243 - 2*a1*a2*a4*a6**3/9 - 40*a1*a2*a4*a6**2/27 + 7*a1*a2*a4*a6/12 - a1*a2*a4/18 - 8*a1*a2*a5**3*a6/81 + 29*a1*a2*a5**3/486 + 7*a1*a2*a5**2*a6**2/9 + 29*a1*a2*a5**2*a6/108 - 17*a1*a2*a5**2/108 - 4*a1*a3*a5*a6**3/243 + 8*a1*a3*a5*a6**2/243 - 25*a1*a3*a5*a6/729 + a1*a3*a5/81 + 4*a1*a3*a6**3/27 - 7*a1*a3*a6**2/81 + a1*a3*a6/54 - a1*a3/486 + 16*a1*a4**2*a6**3/729 + 64*a1*a4**2*a6**2/729 - 82*a1*a4**2*a6/2187 + 8*a1*a4**2/2187 - 4*a1*a4*a5**2*a6**2/243 - 64*a1*a4*a5**2*a6/2187 + 14*a1*a4*a5**2/2187 + 44*a1*a4*a5*a6**2/243 - 71*a1*a4*a5*a6/729 + 13*a1*a4*a5/729 + 8*a1*a4*a6**4/27 + 40*a1*a4*a6**3/81 - 11*a1*a4*a6**2/27 + 26*a1*a4*a6/243 - 5*a1*a4/486 + 4*a1*a5**4*a6/729 - a1*a5**4/2187 + 4*a1*a5**3*a6**2/243 - 43*a1*a5**3*a6/729 + 23*a1*a5**3/1458 - 14*a1*a5**2*a6**3/81 - 5*a1*a5**2*a6**2/81 + 4*a1*a5**2*a6/81 - a1*a5**2/324 + 5*a1*a5*a6**4/9 - 4*a1*a5*a6**3/9 + a1*a5*a6**2/54 + 13*a1*a5*a6/216 - a1*a5/72 - 14*a2**4*a3**2/81 - 14*a2**4*a3*a4/81 - 28*a2**4*a3*a5/27 - a2**4*a3*a6/6 + 31*a2**4*a3/9 + 2*a2**4*a4**2/27 + 2*a2**4*a4*a5/27 - 8*a2**3*a3*a4*a6/243 - 148*a2**3*a3*a4/729 + 46*a2**3*a3*a5**2/729 + 10*a2**3*a3*a5*a6/27 - 139*a2**3*a3*a5/243 - 5*a2**3*a3*a6**2/3 - 14*a2**3*a3*a6/27 + 25*a2**3*a3/162 - 20*a2**3*a4**2*a5/2187 - 8*a2**3*a4**2*a6/243 + 4*a2**3*a4**2/81 - 4*a2**3*a4*a5**2/729 - 14*a2**3*a4*a5*a6/81 + 5*a2**3*a4*a5/486 + a2**3*a4*a6**2/3 + 35*a2**3*a4*a6/18 - 65*a2**3*a4/108 - 22*a2**3*a5**3/243 + a2**3*a5**2*a6/3 + 4*a2**3*a5**2/27 + 14*a2**2*a3*a5*a6**2/243 + 32*a2**2*a3*a5*a6/729 - 41*a2**2*a3*a5/486 + 2*a2**2*a3*a6**3/3 - a2**2*a3*a6**2 + 4*a2**2*a3*a6/9 - 37*a2**2*a3/486 - 8*a2**2*a4**2*a6**2/729 - 32*a2**2*a4**2*a6/243 + 92*a2**2*a4**2/2187 - 8*a2**2*a4*a5**2*a6/2187 - 23*a2**2*a4*a5**2/2187 + 4*a2**2*a4*a5*a6**2/81 - 49*a2**2*a4*a5*a6/729 - 8*a2**2*a4*a5/729 - 10*a2**2*a4*a6**3/27 - 53*a2**2*a4*a6**2/81 + 67*a2**2*a4*a6/162 - 23*a2**2*a4/486 + 16*a2**2*a5**4/2187 + 16*a2**2*a5**3*a6/729 - 10*a2**2*a5**3/243 - 2*a2**2*a5**2*a6**2/3 + 181*a2**2*a5**2*a6/486 - 97*a2**2*a5**2/972 + 11*a2**2*a5*a6**3/9 + 55*a2**2*a5*a6**2/27 - 359*a2**2*a5*a6/216 + a2**2*a5/4 - 4*a2*a3*a6**4/81 + 74*a2*a3*a6**3/243 - 305*a2*a3*a6**2/729 + 239*a2*a3*a6/1458 - 25*a2*a3/1458 - 4*a2*a4*a5*a6**3/81 - 314*a2*a4*a5*a6**2/2187 + 215*a2*a4*a5*a6/2187 - 28*a2*a4*a5/2187 + 8*a2*a4*a6**4/81 + 8*a2*a4*a6**3/243 - 86*a2*a4*a6**2/729 + 7*a2*a4*a6/243 + 8*a2*a5**3*a6**2/243 - 19*a2*a5**3*a6/2187 - a2*a5**3/243 + 8*a2*a5**2*a6**3/81 - 221*a2*a5**2*a6**2/729 + 65*a2*a5**2*a6/486 - 7*a2*a5**2/1458 - 38*a2*a5*a6**4/27 + 20*a2*a5*a6**3/27 - a2*a5*a6**2/9 + 19*a2*a5*a6/486 - 7*a2*a5/972 + a2*a6**5 + 35*a2*a6**4/18 - 89*a2*a6**3/27 + 43*a2*a6**2/27 - 35*a2*a6/108 + 5*a2/216 - 16*a4*a6**5/243 - 32*a4*a6**4/729 + 50*a4*a6**3/729 - 13*a4*a6**2/729 + a4*a6/729 + 8*a5**2*a6**4/243 - 8*a5**2*a6**3/243 + a5**2*a6**2/81 - 2*a5**2*a6/729 + 8*a5*a6**5/81 - 80*a5*a6**4/243 + 7*a5*a6**3/27 - 37*a5*a6**2/486 + 2*a5*a6/243 - 8*a6**6/9 + 16*a6**5/27 + 7*a6**4/81 - 23*a6**3/162 + a6**2/27 - a6/324",
      "a0**3*a3**2*a5/6 - a0**3*a3*a4**2/18 - a0**2*a1*a3**2*a5/9 + 4*a0**2*a1*a3**2*a6/3 - 5*a0**2*a1*a3**2/18 + a0**2*a1*a3*a4**2/27 - 5*a0**2*a1*a3*a4*a5/27 + a0**2*a1*a4**3/81 + 5*a0**2*a2**2*a3**2/6 + 4*a0**2*a2*a3**3/243 + 4*a0**2*a2*a3**2*a4/243 + 8*a0**2*a2*a3**2*a5/81 - 7*a0**2*a2*a3**2*a6/9 + 5*a0**2*a2*a3**2/27 - 2*a0**2*a2*a3*a4**2/81 + 4*a0**2*a2*a3*a4*a5/81 + 17*a0**2*a2*a3*a4*a6/18 - 7*a0**2*a2*a3*a4/54 - 5*a0**2*a2*a3*a5**2/27 + 4*a0**2*a2*a4**3/243 + 2*a0**2*a2*a4**2*a5/81 - 4*a0**2*a3**2*a4*a6/243 + 2*a0**2*a3**2*a4/2187 + 28*a0**2*a3**2*a5**2/2187 + 20*a0**2*a3**2*a5*a6/243 - 2*a0**2*a3**2*a5/729 + 16*a0**2*a3**2*a6**2/27 - 20*a0**2*a3**2*a6/81 + 7*a0**2*a3**2/243 + 4*a0**2*a3*a4**2*a5/6561 - 32*a0**2*a3*a4**2*a6/729 + 4*a0**2*a3*a4**2/2187 + 8*a0**2*a3*a4*a5**2/729 - 10*a0**2*a3*a4*a5*a6/81 + 13*a0**2*a3*a4*a5/729 - 11*a0**2*a3*a4*a6**2/27 + 29*a0**2*a3*a4*a6/162 - a0**2*a3*a4/54 + 20*a0**2*a3*a5**3/729 + 10*a0**2*a3*a5**2*a6/81 - a0**2*a3*a5**2/27 + a0**2*a3*a5*a6**2/3 - a0**2*a3*a5*a6/9 + a0**2*a3*a5/108 - 16*a0**2*a4**4/19683 - 8*a0**2*a4**3*a5/6561 - 8*a0**2*a4**3*a6/729 + 8*a0**2*a4**3/2187 + 4*a0**2*a4**2*a5**2/2187 + 2*a0**2*a4**2*a5*a6/243 - a0**2*a4**2*a6**2/9 + a0**2*a4**2*a6/54 - a0**2*a4**2/81 + a0**2*a4*a5**2*a6/27 + a0**2*a4*a5**2/324 - 8*a0*a1**2*a2*a3**2/3 - 4*a0*a1**2*a3**3/243 - 4*a0*a1**2*a3**2*a4/243 - 2*a0*a1**2*a3**2*a5/81 - a0*a1**2*a3**2*a6/9 + 2*a0*a1**2*a3*a4*a5/27 - 7*a0*a1**2*a3*a4*a6/9 + a0*a1**2*a3*a4/6 - a0*a1**2*a3*a5**2/6 - 2*a0*a1**2*a4**3/81 + a0*a1**2*a4**2*a5/27 + 8*a0*a1*a2**2*a3**2/9 - 19*a0*a1*a2**2*a3*a4/18 + 4*a0*a1*a2*a3**2*a4/81 - 56*a0*a1*a2*a3**2*a5/243 - 28*a0*a1*a2*a3**2*a6/27 + 16*a0*a1*a2*a3**2/81 + 92*a0*a1*a2*a3*a4**2/729 + 34*a0*a1*a2*a3*a4*a5/243 + 19*a0*a1*a2*a3*a4*a6/27 - 11*a0*a1*a2*a3*a4/54 - 23*a0*a1*a2*a3*a5*a6/18 + 37*a0*a1*a2*a3*a5/54 + 4*a0*a1*a2*a4**3/243 + 2*a0*a1*a2*a4**2*a5/81 + 4*a0*a1*a2*a4**2*a6/27 - 13*a0*a1*a2*a4**2/162 + a0*a1*a2*a4*a5**2/9 + 68*a0*a1*a3**2*a5*a6/729 - 14*a0*a1*a3**2*a5/243 + 4*a0*a1*a3**2*a6/81 - 4*a0*a1*a3**2/243 + 4*a0*a1*a3*a4**2/729 + 16*a0*a1*a3*a4*a5**2/2187 + 28*a0*a1*a3*a4*a5*a6/243 - 34*a0*a1*a3*a4*a5/729 - 4*a0*a1*a3*a4*a6**2/81 + 4*a0*a1*a3*a4*a6/243 + a0*a1*a3*a4/243 + 34*a0*a1*a3*a5**2*a6/243 - 17*a0*a1*a3*a5**2/243 + 11*a0*a1*a3*a5*a6**2/27 - 7*a0*a1*a3*a5*a6/18 + 2*a0*a1*a3*a5/27 + 8*a0*a1*a3*a6**3/3 - 2*a0*a1*a3*a6**2/9 - 4*a0*a1*a3*a6/9 + a0*a1*a3/12 - 8*a0*a1*a4**3*a5/2187 - 16*a0*a1*a4**3*a6/2187 - 8*a0*a1*a4**2*a5**2/2187 - 20*a0*a1*a4**2*a5*a6/729 + 2*a0*a1*a4**2*a5/243 + 8*a0*a1*a4**2*a6**2/81 - 4*a0*a1*a4**2*a6/81 + a0*a1*a4**2/81 + 4*a0*a1*a4*a5**3/729 + a0*a1*a4*a5**2/162 - 5*a0*a1*a4*a5*a6**2/27 - a0*a1*a4*a5*a6/3 + a0*a1*a4*a5/27 + a0*a1*a5**3*a6/9 + 7*a0*a1*a5**3/108 + 4*a0*a2**3*a3**2/9 + 2*a0*a2**3*a3*a4/27 - a0*a2**3*a3*a5/6 - a0*a2**3*a4**2/9 + 8*a0*a2**2*a3**2*a5/81 - 8*a0*a2**2*a3**2*a6/27 + 8*a0*a2**2*a3**2/81 - 8*a0*a2**2*a3*a4**2/2187 + 88*a0*a2**2*a3*a4*a5/729 + 8*a0*a2**2*a3*a4*a6/81 - 11*a0*a2**2*a3*a4/243 + 16*a0*a2**2*a3*a5**2/81 + 2*a0*a2**2*a3*a5*a6/9 - 34*a0*a2**2*a3*a5/81 - 2*a0*a2**2*a3*a6**2 - a0*a2**2*a3*a6/9 + 65*a0*a2**2*a3/216 + 4*a0*a2**2*a4**2*a5/243 - 4*a0*a2**2*a4**2*a6/81 + 43*a0*a2**2*a4**2/243 + 4*a0*a2**2*a4*a5**2/81 + 2*a0*a2**2*a4*a5*a6/9 + 53*a0*a2**2*a4*a5/324 + a0*a2**2*a5**3/9 + 28*a0*a2*a3**2*a6**2/81 - 196*a0*a2*a3**2*a6/729 + 73*a0*a2*a3**2/2187 + 16*a0*a2*a3*a4*a5*a6/729 + 94*a0*a2*a3*a4*a5/2187 + 20*a0*a2*a3*a4*a6**2/81 - 94*a0*a2*a3*a4*a6/729 + 16*a0*a2*a3*a4/2187 + 8*a0*a2*a3*a5**3/2187 + 8*a0*a2*a3*a5**2*a6/81 + 88*a0*a2*a3*a5**2/2187 + 10*a0*a2*a3*a5*a6**2/9 - 32*a0*a2*a3*a5*a6/81 + 11*a0*a2*a3*a5/486 + 5*a0*a2*a3*a6**3/9 - 14*a0*a2*a3*a6**2/9 + 193*a0*a2*a3*a6/324 - 7*a0*a2*a3/108 + 16*a0*a2*a4**3*a6/6561 - 280*a0*a2*a4**3/19683 - 8*a0*a2*a4**2*a5**2/2187 - 8*a0*a2*a4**2*a5*a6/2187 - 140*a0*a2*a4**2*a5/6561 - 4*a0*a2*a4**2*a6**2/243 - 82*a0*a2*a4**2*a6/729 + 50*a0*a2*a4**2/2187 - 8*a0*a2*a4*a5**3/2187 - 4*a0*a2*a4*a5**2*a6/243 + 43*a0*a2*a4*a5**2/2187 + 4*a0*a2*a4*a5*a6**2/81 + 65*a0*a2*a4*a5*a6/243 - 5*a0*a2*a4*a5/81 + 4*a0*a2*a4*a6**3/9 - 49*a0*a2*a4*a6**2/54 + a0*a2*a4*a6/3 - 4*a0*a2*a4/81 + 4*a0*a2*a5**4/729 + 2*a0*a2*a5**3*a6/81 - a0*a2*a5**3/27 + 16*a0*a2*a5**2*a6**2/27 + 5*a0*a2*a5**2*a6/108 - 55*a0*a2*a5**2/648 + 56*a0*a3*a4*a6**3/729 + 32*a0*a3*a4*a6**2/729 - 34*a0*a3*a4*a6/729 + 14*a0*a3*a4/2187 - 8*a0*a3*a5**2*a6**2/2187 + 8*a0*a3*a5**2*a6/2187 + 5*a0*a3*a5**2/2187 + 40*a0*a3*a5*a6**3/243 + 32*a0*a3*a5*a6**2/729 - 14*a0*a3*a5*a6/243 + 7*a0*a3*a5/729 + 32*a0*a3*a6**4/27 - 52*a0*a3*a6**3/81 + 11*a0*a3*a6**2/243 + 13*a0*a3*a6/486 - a0*a3/243 + 8*a0*a4**2*a5*a6**2/6561 - 152*a0*a4**2*a5*a6/6561 + 4*a0*a4**2*a5/729 + 16*a0*a4**2*a6**3/729 + 40*a0*a4**2*a6**2/2187 - 8*a0*a4**2*a6/729 - 8*a0*a4*a5**3*a6/6561 + 26*a0*a4*a5**3/6561 - 8*a0*a4*a5**2*a6**2/729 - 98*a0*a4*a5**2*a6/2187 + 8*a0*a4*a5**2/729 - 4*a0*a4*a5*a6**3/81 - 62*a0*a4*a5*a6**2/729 + 25*a0*a4*a5*a6/729 - a0*a4*a5/243 - 2*a0*a4*a6**4/27 + 22*a0*a4*a6**3/81 - 37*a0*a4*a6**2/162 + 11*a0*a4*a6/162 - a0*a4/162 + 16*a0*a5**4/2187 + 8*a0*a5**3*a6**2/729 + 4*a0*a5**3*a6/243 - a0*a5**3/486 + 4*a0*a5**2*a6**3/81 - 4*a0*a5**2*a6**2/81 + a0*a5**2*a6/36 - a0*a5**2/162 + 2*a0*a5*a6**4/3 - 4*a0*a5*a6**3/9 + a0*a5*a6**2/108 + 7*a0*a5*a6/216 - a0*a5/216 + a1**4*a3**2 - a1**3*a2*a3**2/3 + 2*a1**3*a2*a3*a4/3 - 8*a1**3*a3**2*a4/243 + 8*a1**3*a3**2*a5/81 + 4*a1**3*a3**2*a6/9 - 2*a1**3*a3**2/27 - 16*a1**3*a3*a4**2/243 - 8*a1**3*a3*a4*a5/81 + a1**3*a3*a5**2/9 - a1**3*a3*a5*a6 - 5*a1**3*a3*a5/18 - 2*a1**3*a4**2*a5/27 + 4*a1**3*a4**2/27 - 2*a1**2*a2**2*a3**2/9 - 2*a1**2*a2**2*a3*a4/9 + 17*a1**2*a2**2*a3*a5/18 + 2*a1**2*a2**2*a4**2/27 - 8*a1**2*a2*a3**2*a5/81 + 4*a1**2*a2*a3**2*a6/27 - 2*a1**2*a2*a3**2/27 - 28*a1**2*a2*a3*a4*a5/243 - 8*a1**2*a2*a3*a4*a6/27 + 8*a1**2*a2*a3*a4/81 - 20*a1**2*a2*a3*a5**2/81 + 7*a1**2*a2*a3*a5*a6/9 + 7*a1**2*a2*a3*a5/18 - 17*a1**2*a2*a3*a6**2/3 - a1**2*a2*a3*a6 + 5*a1**2*a2*a3/12 + 4*a1**2*a2*a4**2*a5/81 - 2*a1**2*a2*a4**2*a6/27 - 5*a1**2*a2*a4**2/27 - 4*a1**2*a2*a4*a5**2/27 + a1**2*a2*a4*a5*a6/9 + 11*a1**2*a2*a4*a5/27 + 32*a1**2*a3**2*a6**2/243 - 4*a1**2*a3**2*a6/27 + 28*a1**2*a3**2/729 - 28*a1**2*a3*a4*a5/729 + 80*a1**2*a3*a4*a6**2/243 - 16*a1**2*a3*a4*a6/81 + 22*a1**2*a3*a4/729 + 4*a1**2*a3*a5**3/729 - 4*a1**2*a3*a5**2*a6/81 - 38*a1**2*a3*a5**2/729 - 20*a1**2*a3*a5*a6**2/81 - 16*a1**2*a3*a5*a6/81 + 2*a1**2*a3*a5/27 + 8*a1**2*a3*a6**3/9 - 4*a1**2*a3*a6**2/3 + 16*a1**2*a3*a6/27 - 2*a1**2*a3/27 + 80*a1**2*a4**3/6561 - 8*a1**2*a4**2*a5**2/2187 - 16*a1**2*a4**2*a5*a6/729 + 40*a1**2*a4**2*a5/2187 + 8*a1**2*a4**2*a6/81 - 16*a1**2*a4**2/729 + 4*a1**2*a4*a5**2*a6/243 - 14*a1**2*a4*a5**2/729 + 4*a1**2*a4*a5*a6**2/27 - 4*a1**2*a4*a5*a6/81 + a1**2*a4*a5/54 - 4*a1**2*a4*a6**3/9 - 2*a1**2*a4*a6**2/3 + 17*a1**2*a4*a6/54 - a1**2*a4/36 - 2*a1**2*a5**3*a6/27 + a1**2*a5**3/162 + 2*a1**2*a5**2*a6**2/9 + 11*a1**2*a5**2*a6/54 - 5*a1**2*a5**2/54 + 4*a1*a2**3*a3*a4/27 - 17*a1*a2**3*a3*a5/27 + 16*a1*a2**3*a3*a6/3 + 25*a1*a2**3*a3/18 + 2*a1*a2**3*a4**2/81 + a1*a2**3*a4*a5/9 - 104*a1*a2**2*a3**2*a6/243 + 148*a1*a2**2*a3**2/729 - 16*a1*a2**2*a3*a4*a5/729 - 128*a1*a2**2*a3*a4*a6/243 + 112*a1*a2**2*a3*a4/729 - 16*a1*a2**2*a3*a5**2/729 - 4*a1*a2**2*a3*a5*a6/3 + 73*a1*a2**2*a3*a5/243 - a1*a2**2*a3*a6**2 + 130*a1*a2**2*a3*a6/27 - 29*a1*a2**2*a3/27 + 16*a1*a2**2*a4**3/6561 + 8*a1*a2**2*a4**2*a5/2187 + 20*a1*a2**2*a4**2*a6/243 + 16*a1*a2**2*a4**2/729 + 68*a1*a2**2*a4*a5**2/729 - 26*a1*a2**2*a4*a5*a6/81 - 53*a1*a2**2*a4*a5/162 + a1*a2**2*a4*a6**2/9 + 85*a1*a2**2*a4*a6/54 - 13*a1*a2**2*a4/27 - 8*a1*a2**2*a5**3/81 + 5*a1*a2**2*a5**2*a6/27 + 8*a1*a2**2*a5**2/27 - 32*a1*a2*a3*a4*a6**2/243 - 364*a1*a2*a3*a4*a6/2187 + 44*a1*a2*a3*a4/729 + 40*a1*a2*a3*a5**2*a6/729 - 10*a1*a2*a3*a5**2/729 - 8*a1*a2*a3*a5*a6**2/243 - 10*a1*a2*a3*a5*a6/27 + 5*a1*a2*a3*a5/81 - 52*a1*a2*a3*a6**3/27 - 26*a1*a2*a3*a6**2/81 + 11*a1*a2*a3*a6/27 - 5*a1*a2*a3/81 + 8*a1*a2*a4**2*a5*a6/2187 + 140*a1*a2*a4**2*a5/6561 - 16*a1*a2*a4**2*a6**2/729 - 40*a1*a2*a4**2*a6/2187 + 4*a1*a2*a4**2/243 - 16*a1*a2*a4*a5**3/2187 - 8*a1*a2*a4*a5**2*a6/243 + 80*a1*a2*a4*a5**2/2187 + 16*a1*a2*a4*a5*a6**2/243 + 94*a1*a2*a4*a5*a6/729 - 16*a1*a2*a4*a5/729 + 4*a1*a2*a4*a6**3/27 + 80*a1*a2*a4*a6**2/81 - 7*a1*a2*a4*a6/18 + a1*a2*a4/27 + 16*a1*a2*a5**3*a6/243 - 29*a1*a2*a5**3/729 - 14*a1*a2*a5**2*a6**2/27 - 29*a1*a2*a5**2*a6/162 + 17*a1*a2*a5**2/162 + 11*a1*a2*a5*a6**3/9 + 26*a1*a2*a5*a6**2/27 - 26*a1*a2*a5*a6/27 + 29*a1*a2*a5/216 + 8*a1*a3*a5*a6**3/729 - 16*a1*a3*a5*a6**2/729 + 50*a1*a3*a5*a6/2187 - 2*a1*a3*a5/243 - 8*a1*a3*a6**3/81 + 14*a1*a3*a6**2/243 - a1*a3*a6/81 + a1*a3/729 - 32*a1*a4**2*a6**3/2187 - 128*a1*a4**2*a6**2/2187 + 164*a1*a4**2*a6/6561 - 16*a1*a4**2/6561 + 8*a1*a4*a5**2*a6**2/729 + 128*a1*a4*a5**2*a6/6561 - 28*a1*a4*a5**2/6561 - 88*a1*a4*a5*a6**2/729 + 142*a1*a4*a5*a6/2187 - 26*a1*a4*a5/2187 - 16*a1*a4*a6**4/81 - 80*a1*a4*a6**3/243 + 22*a1*a4*a6**2/81 - 52*a1*a4*a6/729 + 5*a1*a4/729 - 8*a1*a5**4*a6/2187 + 2*a1*a5**4/6561 - 8*a1*a5**3*a6**2/729 + 86*a1*a5**3*a6/2187 - 23*a1*a5**3/2187 + 28*a1*a5**2*a6**3/243 + 10*a1*a5**2*a6**2/243 - 8*a1*a5**2*a6/243 + a1*a5**2/486 - 10*a1*a5*a6**4/27 + 8*a1*a5*a6**3/27 - a1*a5*a6**2/81 - 13*a1*a5*a6/324 + a1*a5/108 + 4*a1*a6**5/3 - 4*a1*a6**4/9 - 11*a1*a6**3/18 + 7*a1*a6**2/18 - 17*a1*a6/216 + a1/216 - 7*a2**5*a3/6 + 28*a2**4*a3**2/243 + 28*a2**4*a3*a4/243 + 56*a2**4*a3*a5/81 + a2**4*a3*a6/9 - 62*a2**4*a3/27 - 4*a2**4*a4**2/81 - 4*a2**4*a4*a5/81 + a2**4*a4*a6/9 + a2**4*a4/6 + a2**4*a5**2/27 + 16*a2**3*a3*a4*a6/729 + 296*a2**3*a3*a4/2187 - 92*a2**3*a3*a5**2/2187 - 20*a2**3*a3*a5*a6/81 + 278*a2**3*a3*a5/729 + 10*a2**3*a3*a6**2/9 + 28*a2**3*a3*a6/81 - 25*a2**3*a3/243 + 40*a2**3*a4**2*a5/6561 + 16*a2**3*a4**2*a6/729 - 8*a2**3*a4**2/243 + 8*a2**3*a4*a5**2/2187 + 28*a2**3*a4*a5*a6/243 - 5*a2**3*a4*a5/729 - 2*a2**3*a4*a6**2/9 - 35*a2**3*a4*a6/27 + 65*a2**3*a4/162 + 44*a2**3*a5**3/729 - 2*a2**3*a5**2*a6/9 - 8*a2**3*a5**2/81 - a2**3*a5*a6**2/9 + 49*a2**3*a5*a6/54 - 7*a2**3*a5/24 - 28*a2**2*a3*a5*a6**2/729 - 64*a2**2*a3*a5*a6/2187 + 41*a2**2*a3*a5/729 - 4*a2**2*a3*a6**3/9 + 2*a2**2*a3*a6**2/3 - 8*a2**2*a3*a6/27 + 37*a2**2*a3/729 + 16*a2**2*a4**2*a6**2/2187 + 64*a2**2*a4**2*a6/729 - 184*a2**2*a4**2/6561 + 16*a2**2*a4*a5**2*a6/6561 + 46*a2**2*a4*a5**2/6561 - 8*a2**2*a4*a5*a6**2/243 + 98*a2**2*a4*a5*a6/2187 + 16*a2**2*a4*a5/2187 + 20*a2**2*a4*a6**3/81 + 106*a2**2*a4*a6**2/243 - 67*a2**2*a4*a6/243 + 23*a2**2*a4/729 - 32*a2**2*a5**4/6561 - 32*a2**2*a5**3*a6/2187 + 20*a2**2*a5**3/729 + 4*a2**2*a5**2*a6**2/9 - 181*a2**2*a5**2*a6/729 + 97*a2**2*a5**2/1458 - 22*a2**2*a5*a6**3/27 - 110*a2**2*a5*a6**2/81 + 359*a2**2*a5*a6/324 - a2**2*a5/6 - a2**2*a6**4/3 + 17*a2**2*a6**3/9 - 41*a2**2*a6**2/27 + 29*a2**2*a6/72 - a2**2/27 + 8*a2*a3*a6**4/243 - 148*a2*a3*a6**3/729 + 610*a2*a3*a6**2/2187 - 239*a2*a3*a6/2187 + 25*a2*a3/2187 + 8*a2*a4*a5*a6**3/243 + 628*a2*a4*a5*a6**2/6561 - 430*a2*a4*a5*a6/6561 + 56*a2*a4*a5/6561 - 16*a2*a4*a6**4/243 - 16*a2*a4*a6**3/729 + 172*a2*a4*a6**2/2187 - 14*a2*a4*a6/729 - 16*a2*a5**3*a6**2/729 + 38*a2*a5**3*a6/6561 + 2*a2*a5**3/729 - 16*a2*a5**2*a6**3/243 + 442*a2*a5**2*a6**2/2187 - 65*a2*a5**2*a6/729 + 7*a2*a5**2/2187 + 76*a2*a5*a6**4/81 - 40*a2*a5*a6**3/81 + 2*a2*a5*a6**2/27 - 19*a2*a5*a6/729 + 7*a2*a5/1458 - 2*a2*a6**5/3 - 35*a2*a6**4/27 + 178*a2*a6**3/81 - 86*a2*a6**2/81 + 35*a2*a6/162 - 5*a2/324 + 32*a4*a6**5/729 + 64*a4*a6**4/2187 - 100*a4*a6**3/2187 + 26*a4*a6**2/2187 - 2*a4*a6/2187 - 16*a5**2*a6**4/729 + 16*a5**2*a6**3/729 - 2*a5**2*a6**2/243 + 4*a5**2*a6/2187 - 16*a5*a6**5/243 + 160*a5*a6**4/729 - 14*a5*a6**3/81 + 37*a5*a6**2/729 - 4*a5*a6/729 + 16*a6**6/27 - 32*a6**5/81 - 14*a6**4/243 + 23*a6**3/243 - 2*a6**2/81 + a6/486"
    &#93;
  &#93;,
  "entries": &#91;
    &#91;
      "2*a0*a3/9 + 8*a0*a4/27 + 2*a0*a5/9 - 2*a1*a3/27 + 8*a1*a5/27 + 2*a1*a6/3 - a1/3 - 2*a2*a4/81 - 2*a2*a5/27 - a2/18 - a5/81 - 2*a6/27 + 1/54",
      "a0*a3 + a0*a4/3 - a1*a3/3 + a1*a4/3 + a1*a5/3 - a2*a4/9 + a2/2 - a5/18 + a6/6",
      "-4*a0*a3/27 - 16*a0*a4/81 - 10*a0*a5/27 - 2*a0*a6/3 + a0/9 + 2*a1*a2/3 + 4*a1*a3/81 - 10*a1*a5/81 - 10*a1*a6/9 + 2*a1/9 + 4*a2*a4/243 + 4*a2*a5/81 + 2*a2*a6/9 - 4*a2/27 + 2*a5/243 + 4*a6/81 - 1/81",
      "-2*a0*a2/3 + 8*a0*a3/81 + 32*a0*a4/243 + 20*a0*a5/81 + 10*a0*a6/9 - 19*a0/54 + 2*a1**2/3 - 10*a1*a2/9 - 8*a1*a3/243 + 20*a1*a5/243 + 14*a1*a6/27 - 7*a1/27 + 2*a2**2/9 - 8*a2*a4/729 - 8*a2*a5/243 - 4*a2*a6/27 + 8*a2/81 - 4*a5/729 - 8*a6/243 + 2/243",
      "10*a0*a2/9 - 16*a0*a3/243 - 64*a0*a4/729 - 40*a0*a5/243 - 20*a0*a6/27 + a0/81 - 10*a1**2/9 + 20*a1*a2/27 + 16*a1*a3/729 - 40*a1*a5/729 - 28*a1*a6/81 + 14*a1/81 - 4*a2**2/27 + 16*a2*a4/2187 + 16*a2*a5/729 + 8*a2*a6/81 - 16*a2/243 + 8*a5/2187 + 16*a6/729 - 4/729"
    &#93;,
    &#91;
      "2*a1*a3/9 + 8*a1*a4/27 + 2*a1*a5/9 - 2*a2*a3/27 + 8*a2*a5/27 + 2*a2*a6/3 - a2/3 - 2*a4*a6/81 + a4/81 - 2*a5*a6/27 + a5/54 - a6/9 + 1/27",
      "a1*a3 + a1*a4/3 - a2*a3/3 + a2*a4/3 + a2*a5/3 - a4*a6/9 + a4/18 - a5/12 + a6/2 - 1/12",
      "-4*a1*a3/27 - 16*a1*a4/81 - 10*a1*a5/27 - 2*a1*a6/3 + a1/9 + 2*a2**2/3 + 4*a2*a3/81 - 10*a2*a5/81 - 10*a2*a6/9 + a2/6 + 4*a4*a6/243 - 2*a4/243 + 4*a5*a6/81 - a5/81 + 2*a6**2/9 - a6/9 + 1/81",
      "8*a1*a3/81 + 32*a1*a4/243 + 20*a1*a5/81 + 10*a1*a6/9 - 11*a1/27 - 10*a2**2/9 - 8*a2*a3/243 + 20*a2*a5/243 + 20*a2*a6/27 - 2*a2/9 - 8*a4*a6/729 + 4*a4/729 - 8*a5*a6/243 + 2*a5/243 - 4*a6**2/27 + 2*a6/27 - 2/243",
      "2*a0*a2/3 - a0/18 - 2*a1**2/3 - 16*a1*a3/243 - 64*a1*a4/729 - 40*a1*a5/243 - 14*a1*a6/27 + 4*a1/81 + 14*a2**2/27 + 16*a2*a3/729 - 40*a2*a5/729 - 40*a2*a6/81 + 4*a2/27 + 16*a4*a6/2187 - 8*a4/2187 + 16*a5*a6/729 - 4*a5/729 + 8*a6**2/81 - 4*a6/81 + 4/729"
    &#93;,
    &#91;
      "2*a2*a3/3 + 8*a2*a4/9 + 2*a2*a5/3 - 2*a3*a6/9 + a3/27 + 2*a4*a5/81 + a4/27 + 2*a5**2/27 + 8*a5*a6/9 - 7*a5/54 + 2*a6**2 - 5*a6/3 + 1/3",
      "3*a2*a3 + a2*a4 - a3*a6 + a3/6 + a4*a5/9 + a4*a6 + a5*a6 - 5*a5/6",
      "-4*a2*a3/9 - 16*a2*a4/27 - 10*a2*a5/9 - a2/3 + 4*a3*a6/27 - 2*a3/81 - 4*a4*a5/243 - 2*a4/81 - 4*a5**2/81 - 16*a5*a6/27 + 10*a5/81 - 10*a6**2/3 + 13*a6/9 - 1/6",
      "2*a1*a6 - 2*a1/3 - 2*a2**2 + 8*a2*a3/27 + 32*a2*a4/81 + 14*a2*a5/27 - 5*a2/18 - 8*a3*a6/81 + 4*a3/243 + 8*a4*a5/729 + 4*a4/243 + 8*a5**2/243 + 32*a5*a6/81 - 20*a5/243 + 14*a6**2/9 - 23*a6/27 + 1/9",
      "2*a0*a6 - 2*a0/3 - 2*a1*a2 - 2*a1*a5/9 - 10*a1*a6/3 + 7*a1/9 + 10*a2**2/3 - 16*a2*a3/81 - 64*a2*a4/243 - 28*a2*a5/81 - 2*a2*a6/3 - a2/27 + 16*a3*a6/243 - 8*a3/729 - 16*a4*a5/2187 - 8*a4/729 - 16*a5**2/729 - 64*a5*a6/243 + 40*a5/729 - 28*a6**2/27 + 46*a6/81 - 2/27"
    &#93;,
    &#91;
      "2*a3*a5/27 + 2*a3*a6/3 - 5*a3/18 - 2*a4**2/81 - 2*a4*a5/27 + 8*a4*a6/9 - 2*a4/9 - 8*a5**2/27 + a5/3",
      "a3*a5/3 + 3*a3*a6 - 5*a3/4 - a4**2/9 - a4*a5/3 + a4*a6 + a4/2 - a5**2/3",
      "-2*a2*a5/3 - 4*a3*a5/81 - 4*a3*a6/9 + 5*a3/27 + 4*a4**2/243 + 4*a4*a5/81 - 10*a4*a6/27 + 2*a4/27 + 10*a5**2/81 - a5/18 - 2*a6**2 + a6/3",
      "-2*a1*a5/3 + 2*a2*a4/9 + 10*a2*a5/9 - 2*a2*a6 + 8*a3*a5/243 + 8*a3*a6/27 - 10*a3/81 - 8*a4**2/729 - 8*a4*a5/243 + 20*a4*a6/81 - 4*a4/81 - 20*a5**2/243 + 2*a5*a6/9 + a5/27 + 10*a6**2/3 - 14*a6/9 + 1/6",
      "-2*a0*a5/3 + 2*a1*a4/9 + 10*a1*a5/9 - 2*a1*a6 - 4*a2*a4/27 - 14*a2*a5/27 + 10*a2*a6/3 - a2/2 - 16*a3*a5/729 - 16*a3*a6/81 + 20*a3/243 + 16*a4**2/2187 + 16*a4*a5/729 - 40*a4*a6/243 + 8*a4/243 + 40*a5**2/729 - 4*a5*a6/27 - 2*a5/81 - 20*a6**2/9 + 19*a6/27"
    &#93;,
    &#91;
      "a3/2 - 2*a4*a6/3 + 2*a4/3 + 2*a5**2/9",
      "a3*a5 + 3*a3 - a4**2/3",
      "-2*a2*a4/3 + 2*a3*a6/3 - 5*a3/9 - 2*a4*a5/27 + 10*a4*a6/9 - 5*a4/9 - 10*a5**2/27 - 2*a5*a6/3 - 2*a5/9",
      "-2*a1*a4/3 + 2*a2*a3/3 + 10*a2*a4/9 - 2*a2*a5/3 - 4*a3*a6/9 + 10*a3/27 + 4*a4*a5/81 - 14*a4*a6/27 + 10*a4/27 + 20*a5**2/81 + 10*a5*a6/9 - a5/54 + a6 - 1/3",
      "-2*a0*a4/3 + 2*a1*a3/3 + 10*a1*a4/9 - 2*a1*a5/3 - 4*a2*a3/9 - 14*a2*a4/27 + 10*a2*a5/9 + a2 + 8*a3*a6/27 - 20*a3/81 - 8*a4*a5/243 + 28*a4*a6/81 - 20*a4/81 - 40*a5**2/243 - 20*a5*a6/27 - 8*a5/81 - a6 + 1/18"
    &#93;,
    &#91;
      "-a1*a3**2*a6/9 + a1*a3**2/54 + a1*a3*a4*a5/27 - a1*a3*a4*a6/9 + a1*a3*a4/54 + 2*a1*a3*a5**2/27 - 2*a1*a4**3/243 - a1*a4**2*a5/81 + a2**2*a3**2/9 + a2**2*a3*a4/9 + a2*a3*a4*a6/9 - 7*a2*a3*a4/162 + 4*a2*a3*a5**2/81 + 5*a2*a3*a5*a6/9 - 7*a2*a3*a5/54 - 5*a2*a4**2*a5/243 - 2*a2*a4**2*a6/27 - a2*a4*a5**2/81 + 4*a3*a5*a6**2/27 - 13*a3*a5*a6/162 + a3*a5/108 + a3*a6**3 - 2*a3*a6**2/3 + 5*a3*a6/36 - a3/108 + 2*a4**2*a6**2/81 - 5*a4**2*a6/243 + a4**2/243 - 8*a4*a5**2*a6/243 + 5*a4*a5**2/486 - a4*a5*a6**2/9 + a4*a5*a6/162 + a4*a5/162 + a5**4/243 + a5**3*a6/81 + a5**3/162",
      "-a1*a3**2*a6/2 + a1*a3**2/12 + a1*a3*a4*a5/6 - a1*a4**3/27 + a2**2*a3**2/2 + a2*a3*a4*a6/2 - 7*a2*a3*a4/36 + 2*a2*a3*a5**2/9 - 5*a2*a4**2*a5/54 + 2*a3*a5*a6**2/3 - 13*a3*a5*a6/36 + a3*a5/24 + a4**2*a6**2/9 - 5*a4**2*a6/54 + a4**2/54 - 4*a4*a5**2*a6/27 + 5*a4*a5**2/108 + a5**4/54",
      "2*a1*a3**2*a6/27 - a1*a3**2/81 - 2*a1*a3*a4*a5/81 + 2*a1*a3*a4*a6/27 - a1*a3*a4/81 - 4*a1*a3*a5**2/81 - a1*a3*a5*a6/9 + a1*a3*a5/18 + 4*a1*a4**3/729 + 2*a1*a4**2*a5/243 + 2*a1*a4**2*a6/27 - 2*a1*a4**2/81 - a1*a4*a5**2/81 - 2*a2**2*a3**2/27 - 2*a2**2*a3*a4/27 + 2*a2**2*a3*a5/9 - a2**2*a4**2/9 - 2*a2*a3*a4*a6/27 + 7*a2*a3*a4/243 - 8*a2*a3*a5**2/243 - 10*a2*a3*a5*a6/27 + 7*a2*a3*a5/81 + a2*a3*a6**2/3 - a2*a3*a6/18 - a2*a3/54 + 10*a2*a4**2*a5/729 + 4*a2*a4**2*a6/81 + 2*a2*a4*a5**2/243 - 5*a2*a4*a5*a6/27 + 4*a2*a4*a5/81 + 2*a2*a5**3/81 - 8*a3*a5*a6**2/81 + 13*a3*a5*a6/243 - a3*a5/162 - 2*a3*a6**3/3 + 4*a3*a6**2/9 - 5*a3*a6/54 + a3/162 - 4*a4**2*a6**2/243 + 10*a4**2*a6/729 - 2*a4**2/729 + 16*a4*a5**2*a6/729 - 5*a4*a5**2/729 + 2*a4*a5*a6**2/27 - a4*a5*a6/243 - a4*a5/243 - 2*a4*a6**3/9 + 7*a4*a6**2/27 - 8*a4*a6/81 + a4/81 - 2*a5**4/729 - 2*a5**3*a6/243 - a5**3/243 + a5**2*a6**2/27 - a5**2*a6/27 + a5**2/108",
      "a1*a2*a3*a5/9 - a1*a2*a4**2/27 - 4*a1*a3**2*a6/81 + 2*a1*a3**2/243 + 4*a1*a3*a4*a5/243 - 4*a1*a3*a4*a6/81 + 2*a1*a3*a4/243 + 8*a1*a3*a5**2/243 + 2*a1*a3*a5*a6/27 - a1*a3*a5/27 + 2*a1*a3*a6**2/3 - 4*a1*a3*a6/9 + a1*a3/18 - 8*a1*a4**3/2187 - 4*a1*a4**2*a5/729 - 4*a1*a4**2*a6/81 + 4*a1*a4**2/243 + 2*a1*a4*a5**2/243 - 5*a1*a4*a5*a6/27 + a1*a4*a5/18 + a1*a5**3/27 + 4*a2**2*a3**2/81 + 4*a2**2*a3*a4/81 - 4*a2**2*a3*a5/27 - a2**2*a3*a6/3 + 2*a2**2*a3/9 + 2*a2**2*a4**2/27 + 2*a2**2*a4*a5/27 + 4*a2*a3*a4*a6/81 - 14*a2*a3*a4/729 + 16*a2*a3*a5**2/729 + 20*a2*a3*a5*a6/81 - 14*a2*a3*a5/243 - 2*a2*a3*a6**2/9 + a2*a3*a6/27 + a2*a3/81 - 20*a2*a4**2*a5/2187 - 8*a2*a4**2*a6/243 - 4*a2*a4*a5**2/729 + 10*a2*a4*a5*a6/81 - 8*a2*a4*a5/243 - a2*a4*a6**2/9 + 7*a2*a4*a6/54 - a2*a4/27 - 4*a2*a5**3/243 + a2*a5**2*a6/9 - a2*a5**2/27 + 16*a3*a5*a6**2/243 - 26*a3*a5*a6/729 + a3*a5/243 + 4*a3*a6**3/9 - 8*a3*a6**2/27 + 5*a3*a6/81 - a3/243 + 8*a4**2*a6**2/729 - 20*a4**2*a6/2187 + 4*a4**2/2187 - 32*a4*a5**2*a6/2187 + 10*a4*a5**2/2187 - 4*a4*a5*a6**2/81 + 2*a4*a5*a6/729 + 2*a4*a5/729 + 4*a4*a6**3/27 - 14*a4*a6**2/81 + 16*a4*a6/243 - 2*a4/243 + 4*a5**4/2187 + 4*a5**3*a6/729 + 2*a5**3/729 - 2*a5**2*a6**2/81 + 2*a5**2*a6/81 - a5**2/162 + a5*a6**3/9 - 2*a5*a6**2/27 + a5*a6/108",
      "a0*a2*a3*a5/3 - a0*a2*a4**2/9 + a0*a3*a6**2 - a0*a3*a6/2 + a0*a3/18 - 2*a0*a4*a5*a6/9 + a0*a4*a5/18 + a0*a5**3/27 - 2*a1**2*a3*a5/9 + 2*a1**2*a4**2/27 - 2*a1*a2*a3*a5/27 - a1*a2*a3*a6 + 5*a1*a2*a3/18 + 2*a1*a2*a4**2/81 + a1*a2*a4*a5/9 + 8*a1*a3**2*a6/243 - 4*a1*a3**2/729 - 8*a1*a3*a4*a5/729 + 8*a1*a3*a4*a6/243 - 4*a1*a3*a4/729 - 16*a1*a3*a5**2/729 - 4*a1*a3*a5*a6/81 + 2*a1*a3*a5/81 - 4*a1*a3*a6**2/9 + 8*a1*a3*a6/27 - a1*a3/27 + 16*a1*a4**3/6561 + 8*a1*a4**2*a5/2187 + 8*a1*a4**2*a6/243 - 8*a1*a4**2/729 - 4*a1*a4*a5**2/729 + 10*a1*a4*a5*a6/81 - a1*a4*a5/27 - 2*a1*a4*a6**2/9 + 8*a1*a4*a6/27 - a1*a4/18 - 2*a1*a5**3/81 + 2*a1*a5**2*a6/27 - 2*a1*a5**2/27 + a2**3*a3/3 - 8*a2**2*a3**2/243 - 8*a2**2*a3*a4/243 + 8*a2**2*a3*a5/81 + 2*a2**2*a3*a6/9 - 4*a2**2*a3/27 - 4*a2**2*a4**2/81 - 4*a2**2*a4*a5/81 + a2**2*a4*a6/9 - a2**2*a4/6 + a2**2*a5**2/27 - 8*a2*a3*a4*a6/243 + 28*a2*a3*a4/2187 - 32*a2*a3*a5**2/2187 - 40*a2*a3*a5*a6/243 + 28*a2*a3*a5/729 + 4*a2*a3*a6**2/27 - 2*a2*a3*a6/81 - 2*a2*a3/243 + 40*a2*a4**2*a5/6561 + 16*a2*a4**2*a6/729 + 8*a2*a4*a5**2/2187 - 20*a2*a4*a5*a6/243 + 16*a2*a4*a5/729 + 2*a2*a4*a6**2/27 - 7*a2*a4*a6/81 + 2*a2*a4/81 + 8*a2*a5**3/729 - 2*a2*a5**2*a6/27 + 2*a2*a5**2/81 + a2*a5*a6**2/9 - 8*a2*a5*a6/27 + 11*a2*a5/108 - 32*a3*a5*a6**2/729 + 52*a3*a5*a6/2187 - 2*a3*a5/729 - 8*a3*a6**3/27 + 16*a3*a6**2/81 - 10*a3*a6/243 + 2*a3/729 - 16*a4**2*a6**2/2187 + 40*a4**2*a6/6561 - 8*a4**2/6561 + 64*a4*a5**2*a6/6561 - 20*a4*a5**2/6561 + 8*a4*a5*a6**2/243 - 4*a4*a5*a6/2187 - 4*a4*a5/2187 - 8*a4*a6**3/81 + 28*a4*a6**2/243 - 32*a4*a6/729 + 4*a4/729 - 8*a5**4/6561 - 8*a5**3*a6/2187 - 4*a5**3/2187 + 4*a5**2*a6**2/243 - 4*a5**2*a6/243 + a5**2/243 - 2*a5*a6**3/27 + 4*a5*a6**2/81 - a5*a6/162 - a6**3/3 + a6**2/3 - 11*a6/108 + 1/108"
    &#93;,
    &#91;
      "-a0*a3**2*a6/18 + a0*a3**2/108 + a0*a3*a4*a5/54 - a0*a3*a4*a6/18 + a0*a3*a4/108 + a0*a3*a5**2/27 - a0*a4**3/243 - a0*a4**2*a5/162 + a1*a2*a3**2/18 + a1*a2*a3*a4/18 + 2*a1*a3*a4*a6/27 - a1*a3*a4/54 - a1*a3*a5**2/54 - a1*a3*a5/18 + 2*a1*a4**2*a6/27 - a1*a4*a5**2/54 - a2**2*a3*a4/54 + 4*a2**2*a3*a5/9 - a2**2*a4**2/6 - 13*a2*a3*a5*a6/54 + a2*a3*a5/6 + a2*a3*a6**2 - 7*a2*a3*a6/12 + 7*a2*a3/72 + 5*a2*a4**2*a6/81 - 7*a2*a4**2/162 - 5*a2*a4*a5*a6/18 + 11*a2*a4*a5/108 + a2*a5**3/27 - 5*a3*a6**3/9 + 19*a3*a6**2/27 - 13*a3*a6/54 + 5*a3/216 + 7*a4*a5*a6**2/81 - 7*a4*a5*a6/81 + 5*a4*a5/324 - 2*a4*a6**3/9 + 7*a4*a6**2/27 - a4*a6/18 - a5**3*a6/81 + a5**3/108 + a5**2*a6**2/27 - a5**2*a6/36 - a5**2/216",
      "-a0*a3**2*a6/4 + a0*a3**2/24 + a0*a3*a4*a5/12 - a0*a4**3/54 + a1*a2*a3**2/4 + a1*a3*a4*a6/3 - a1*a3*a4/12 - a1*a3*a5**2/12 - a2**2*a3*a4/12 - 13*a2*a3*a5*a6/12 + 3*a2*a3*a5/4 + 5*a2*a4**2*a6/18 - 7*a2*a4**2/36 - 5*a3*a6**3/2 + 19*a3*a6**2/6 - 13*a3*a6/12 + 5*a3/48 + 7*a4*a5*a6**2/18 - 7*a4*a5*a6/18 + 5*a4*a5/72 - a5**3*a6/18 + a5**3/24",
      "a0*a3**2*a6/27 - a0*a3**2/162 - a0*a3*a4*a5/81 + a0*a3*a4*a6/27 - a0*a3*a4/162 - 2*a0*a3*a5**2/81 - a0*a3*a5*a6/18 + a0*a3*a5/36 + 2*a0*a4**3/729 + a0*a4**2*a5/243 + a0*a4**2*a6/27 - a0*a4**2/81 - a0*a4*a5**2/162 - a1*a2*a3**2/27 - a1*a2*a3*a4/27 + 5*a1*a2*a3*a5/18 - a1*a2*a4**2/9 - 4*a1*a3*a4*a6/81 + a1*a3*a4/81 + a1*a3*a5**2/81 + a1*a3*a5/27 + a1*a3*a6**2 - a1*a3*a6/3 + a1*a3/36 - 4*a1*a4**2*a6/81 + a1*a4*a5**2/81 - 8*a1*a4*a5*a6/27 + a1*a4*a5/18 + a1*a5**3/18 + a2**2*a3*a4/81 - 8*a2**2*a3*a5/27 - a2**2*a3*a6/3 + a2**2*a3/36 + a2**2*a4**2/9 + a2**2*a4*a5/18 + 13*a2*a3*a5*a6/81 - a2*a3*a5/9 - 2*a2*a3*a6**2/3 + 7*a2*a3*a6/18 - 7*a2*a3/108 - 10*a2*a4**2*a6/243 + 7*a2*a4**2/243 + 5*a2*a4*a5*a6/27 - 11*a2*a4*a5/162 - 2*a2*a4*a6**2/9 + 5*a2*a4*a6/27 - a2*a4/54 - 2*a2*a5**3/81 + 7*a2*a5**2*a6/54 - 5*a2*a5**2/54 + 10*a3*a6**3/27 - 38*a3*a6**2/81 + 13*a3*a6/81 - 5*a3/324 - 14*a4*a5*a6**2/243 + 14*a4*a5*a6/243 - 5*a4*a5/486 + 4*a4*a6**3/27 - 14*a4*a6**2/81 + a4*a6/27 + 2*a5**3*a6/243 - a5**3/162 - 2*a5**2*a6**2/81 + a5**2*a6/54 + a5**2/324 + a5*a6**3/9 - a5*a6**2/6 + 2*a5*a6/27 - a5/108",
      "-a0*a2*a3*a5/9 + a0*a2*a4**2/27 - 2*a0*a3**2*a6/81 + a0*a3**2/243 + 2*a0*a3*a4*a5/243 - 2*a0*a3*a4*a6/81 + a0*a3*a4/243 + 4*a0*a3*a5**2/243 + a0*a3*a5*a6/27 - a0*a3*a5/54 - a0*a3*a6**2/6 + a0*a3*a6/36 - 4*a0*a4**3/2187 - 2*a0*a4**2*a5/729 - 2*a0*a4**2*a6/81 + 2*a0*a4**2/243 + a0*a4*a5**2/243 + a0*a4*a5*a6/54 + a1**2*a3*a5/3 - a1**2*a4**2/9 + 2*a1*a2*a3**2/81 + 2*a1*a2*a3*a4/81 - 5*a1*a2*a3*a5/27 + 13*a1*a2*a3*a6/6 - 5*a1*a2*a3/12 + 2*a1*a2*a4**2/27 - 2*a1*a2*a4*a5/9 + 8*a1*a3*a4*a6/243 - 2*a1*a3*a4/243 - 2*a1*a3*a5**2/243 - 2*a1*a3*a5/81 - 2*a1*a3*a6**2/3 + 2*a1*a3*a6/9 - a1*a3/54 + 8*a1*a4**2*a6/243 - 2*a1*a4*a5**2/243 + 16*a1*a4*a5*a6/81 - a1*a4*a5/27 + 8*a1*a4*a6**2/9 - 4*a1*a4*a6/9 + a1*a4/18 - a1*a5**3/27 - 5*a1*a5**2*a6/18 + a1*a5**2/12 - 4*a2**3*a3/3 - 2*a2**2*a3*a4/243 + 16*a2**2*a3*a5/81 + 2*a2**2*a3*a6/9 - a2**2*a3/54 - 2*a2**2*a4**2/27 - a2**2*a4*a5/27 - 19*a2**2*a4*a6/18 + 7*a2**2*a4/18 - a2**2*a5**2/9 - 26*a2*a3*a5*a6/243 + 2*a2*a3*a5/27 + 4*a2*a3*a6**2/9 - 7*a2*a3*a6/27 + 7*a2*a3/162 + 20*a2*a4**2*a6/729 - 14*a2*a4**2/729 - 10*a2*a4*a5*a6/81 + 11*a2*a4*a5/243 + 4*a2*a4*a6**2/27 - 10*a2*a4*a6/81 + a2*a4/81 + 4*a2*a5**3/243 - 7*a2*a5**2*a6/81 + 5*a2*a5**2/81 - 3*a2*a5*a6**2/2 + 37*a2*a5*a6/36 - a2*a5/6 - 20*a3*a6**3/81 + 76*a3*a6**2/243 - 26*a3*a6/243 + 5*a3/486 + 28*a4*a5*a6**2/729 - 28*a4*a5*a6/729 + 5*a4*a5/729 - 8*a4*a6**3/81 + 28*a4*a6**2/243 - 2*a4*a6/81 - 4*a5**3*a6/729 + a5**3/243 + 4*a5**2*a6**2/243 - a5**2*a6/81 - a5**2/486 - 2*a5*a6**3/27 + a5*a6**2/9 - 4*a5*a6/81 + a5/162 - 5*a6**4/3 + 19*a6**3/9 - 35*a6**2/36 + 7*a6/36 - 1/72",
      "2*a0*a1*a3*a5/9 - 2*a0*a1*a4**2/27 + 2*a0*a2*a3*a5/27 + 5*a0*a2*a3*a6/6 - 2*a0*a2*a3/9 - 2*a0*a2*a4**2/81 - 5*a0*a2*a4*a5/54 + 4*a0*a3**2*a6/243 - 2*a0*a3**2/729 - 4*a0*a3*a4*a5/729 + 4*a0*a3*a4*a6/243 - 2*a0*a3*a4/729 - 8*a0*a3*a5**2/729 - 2*a0*a3*a5*a6/81 + a0*a3*a5/81 + a0*a3*a6**2/9 - a0*a3*a6/54 + 8*a0*a4**3/6561 + 4*a0*a4**2*a5/2187 + 4*a0*a4**2*a6/243 - 4*a0*a4**2/729 - 2*a0*a4*a5**2/729 - a0*a4*a5*a6/81 + a0*a4*a6**2/3 - a0*a4*a6/9 + a0*a4/54 - a0*a5**2*a6/9 + a0*a5**2/108 - 2*a1**2*a3*a5/9 + a1**2*a3*a6 - a1**2*a3/6 + 2*a1**2*a4**2/27 - a1**2*a4*a5/9 - 7*a1*a2**2*a3/6 - 4*a1*a2*a3**2/243 - 4*a1*a2*a3*a4/243 + 10*a1*a2*a3*a5/81 - 13*a1*a2*a3*a6/9 + 5*a1*a2*a3/18 - 4*a1*a2*a4**2/81 + 4*a1*a2*a4*a5/27 + a1*a2*a4/18 - 5*a1*a2*a5**2/18 - 16*a1*a3*a4*a6/729 + 4*a1*a3*a4/729 + 4*a1*a3*a5**2/729 + 4*a1*a3*a5/243 + 4*a1*a3*a6**2/9 - 4*a1*a3*a6/27 + a1*a3/81 - 16*a1*a4**2*a6/729 + 4*a1*a4*a5**2/729 - 32*a1*a4*a5*a6/243 + 2*a1*a4*a5/81 - 16*a1*a4*a6**2/27 + 8*a1*a4*a6/27 - a1*a4/27 + 2*a1*a5**3/81 + 5*a1*a5**2*a6/27 - a1*a5**2/18 - 4*a1*a5*a6**2/9 + 2*a1*a5*a6/9 + 8*a2**3*a3/9 - a2**3*a4/2 + 4*a2**2*a3*a4/729 - 32*a2**2*a3*a5/243 - 4*a2**2*a3*a6/27 + a2**2*a3/81 + 4*a2**2*a4**2/81 + 2*a2**2*a4*a5/81 + 19*a2**2*a4*a6/27 - 7*a2**2*a4/27 + 2*a2**2*a5**2/27 - 19*a2**2*a5*a6/18 + 13*a2**2*a5/36 + 52*a2*a3*a5*a6/729 - 4*a2*a3*a5/81 - 8*a2*a3*a6**2/27 + 14*a2*a3*a6/81 - 7*a2*a3/243 - 40*a2*a4**2*a6/2187 + 28*a2*a4**2/2187 + 20*a2*a4*a5*a6/243 - 22*a2*a4*a5/729 - 8*a2*a4*a6**2/81 + 20*a2*a4*a6/243 - 2*a2*a4/243 - 8*a2*a5**3/729 + 14*a2*a5**2*a6/243 - 10*a2*a5**2/243 + a2*a5*a6**2 - 37*a2*a5*a6/54 + a2*a5/9 - 5*a2*a6**3/3 + 13*a2*a6**2/9 - 13*a2*a6/36 + a2/36 + 40*a3*a6**3/243 - 152*a3*a6**2/729 + 52*a3*a6/729 - 5*a3/729 - 56*a4*a5*a6**2/2187 + 56*a4*a5*a6/2187 - 10*a4*a5/2187 + 16*a4*a6**3/243 - 56*a4*a6**2/729 + 4*a4*a6/243 + 8*a5**3*a6/2187 - 2*a5**3/729 - 8*a5**2*a6**2/729 + 2*a5**2*a6/243 + a5**2/729 + 4*a5*a6**3/81 - 2*a5*a6**2/27 + 8*a5*a6/243 - a5/243 + 10*a6**4/9 - 38*a6**3/27 + 35*a6**2/54 - 7*a6/54 + 1/108"
    &#93;,
    &#91;
      "-a0**2*a2*a3**2*a5/6 + a0**2*a2*a3*a4**2/27 - a0**2*a2*a3*a4*a5/6 + a0**2*a2*a4**3/27 + 2*a0**2*a3**2*a6/9 - a0**2*a3**2/27 - a0**2*a3*a4*a5*a6/54 - 17*a0**2*a3*a4*a5/324 + 2*a0**2*a3*a4*a6/9 - a0**2*a3*a4/27 - a0**2*a3*a5**3/18 - a0**2*a3*a5**2*a6/2 - 7*a0**2*a3*a5**2/108 + 2*a0**2*a4**3*a6/81 + 2*a0**2*a4**3/243 + 5*a0**2*a4**2*a5**2/486 + 2*a0**2*a4**2*a5*a6/9 - a0**2*a4**2*a5/162 - 2*a0**2*a4*a5**3/81 + a0*a1**2*a3**2*a5/6 - a0*a1**2*a3*a4**2/27 + a0*a1**2*a3*a4*a5/6 - a0*a1**2*a4**3/27 + 2*a0*a1*a2*a3**2*a6/3 - a0*a1*a2*a3**2/2 - 29*a0*a1*a2*a3*a4*a5/54 + 2*a0*a1*a2*a3*a4*a6/3 - a0*a1*a2*a3*a4/2 - a0*a1*a2*a3*a5**2/9 + 8*a0*a1*a2*a4**3/81 - 11*a0*a1*a2*a4**2*a5/54 - 5*a0*a1*a3*a4*a6**2/9 + 7*a0*a1*a3*a4*a6/54 + a0*a1*a3*a4/27 - 11*a0*a1*a3*a5**2*a6/18 + 19*a0*a1*a3*a5**2/108 - 3*a0*a1*a3*a5*a6**2 + a0*a1*a3*a5*a6/3 + a0*a1*a3*a5/9 + 16*a0*a1*a4**2*a5*a6/81 - a0*a1*a4**2*a5/27 + 4*a0*a1*a4**2*a6**2/9 - a0*a1*a4**2*a6/27 + a0*a1*a4**2/54 - a0*a1*a4*a5**2*a6/54 + a0*a1*a4*a5**2/12 - a0*a2**3*a3**2 - a0*a2**3*a3*a4 - 11*a0*a2**2*a3*a4*a6/9 + 5*a0*a2**2*a3*a4/27 - 7*a0*a2**2*a3*a5**2/9 - 5*a0*a2**2*a3*a5*a6 + 25*a0*a2**2*a3*a5/18 + 19*a0*a2**2*a4**2*a5/81 + 7*a0*a2**2*a4**2*a6/9 - 7*a0*a2**2*a4**2/18 - 5*a0*a2**2*a4*a5**2/27 - 59*a0*a2*a3*a5*a6**2/18 + 85*a0*a2*a3*a5*a6/108 - 11*a0*a2*a3*a5/108 - 15*a0*a2*a3*a6**3 + 41*a0*a2*a3*a6**2/4 - 21*a0*a2*a3*a6/8 + 17*a0*a2*a3/72 - 10*a0*a2*a4**2*a6**2/27 + 61*a0*a2*a4**2*a6/162 - 2*a0*a2*a4**2/81 + 38*a0*a2*a4*a5**2*a6/81 - a0*a2*a4*a5**2/9 + 17*a0*a2*a4*a5*a6**2/18 - 5*a0*a2*a4*a5*a6/6 + 11*a0*a2*a4*a5/54 - 4*a0*a2*a5**4/81 - 7*a0*a2*a5**3*a6/27 + 7*a0*a2*a5**3/54 - 22*a0*a3*a6**3/9 + 73*a0*a3*a6**2/54 - 23*a0*a3*a6/108 + a0*a3/108 - a0*a4*a5*a6**3/3 + 103*a0*a4*a5*a6**2/162 - 13*a0*a4*a5*a6/81 + a0*a4*a5/108 - a0*a4*a6**4 - 4*a0*a4*a6**3/9 + 17*a0*a4*a6**2/108 + a0*a4*a6/108 + 2*a0*a5**3*a6**2/27 - 31*a0*a5**3*a6/324 + a0*a5**3/162 + 29*a0*a5**2*a6**2/108 + a0*a5**2*a6/24 + a1**3*a3**2/6 + a1**3*a3*a4*a5/3 + a1**3*a3*a4/6 + a1**3*a3*a5**2/3 - 2*a1**3*a4**3/27 + a1**2*a2**2*a3**2/3 + a1**2*a2**2*a3*a4/3 + 14*a1**2*a2*a3*a4*a6/9 - 2*a1**2*a2*a3*a4/9 + 2*a1**2*a2*a3*a5**2/3 + 13*a1**2*a2*a3*a5*a6/2 - 7*a1**2*a2*a3*a5/4 - 7*a1**2*a2*a4**2*a5/27 - 7*a1**2*a2*a4**2*a6/9 + 4*a1**2*a2*a4**2/9 - a1**2*a2*a4*a5**2/18 - 2*a1**2*a3*a5*a6**2/3 + 11*a1**2*a3*a5*a6/9 - a1**2*a3*a5/9 - 3*a1**2*a3*a6**2/2 + 3*a1**2*a3*a6/4 - a1**2*a3/12 + 4*a1**2*a4**2*a6**2/9 - 4*a1**2*a4**2*a6/9 + a1**2*a4**2/18 - a1**2*a4*a5**2*a6/9 + a1**2*a4*a5**2/27 + 7*a1**2*a4*a5*a6/18 + a1**2*a5**4/54 + a1**2*a5**3*a6/18 + a1**2*a5**3/36 - 4*a1*a2**3*a3*a4/9 - 4*a1*a2**3*a3*a5/3 + 10*a1*a2**2*a3*a5*a6/3 - 29*a1*a2**2*a3*a5/36 + 15*a1*a2**2*a3*a6**2 - 35*a1*a2**2*a3*a6/4 + 35*a1*a2**2*a3/24 - 2*a1*a2**2*a4**2*a6/9 + 5*a1*a2**2*a4**2/54 - 2*a1*a2**2*a4*a5**2/9 - a1*a2**2*a4*a5*a6/3 + 11*a1*a2**2*a4*a5/18 - 2*a1*a2**2*a5**3/9 - 2*a1*a2*a3*a6**3/3 + 46*a1*a2*a3*a6**2/9 - 47*a1*a2*a3*a6/36 + a1*a2*a3/72 + 7*a1*a2*a4*a5*a6**2/27 - 25*a1*a2*a4*a5*a6/54 + 5*a1*a2*a4*a5/108 + 10*a1*a2*a4*a6**3/3 - 20*a1*a2*a4*a6**2/9 + 4*a1*a2*a4*a6/3 - 2*a1*a2*a4/9 - a1*a2*a5**3*a6/27 + a1*a2*a5**3/108 - 8*a1*a2*a5**2*a6**2/9 + 47*a1*a2*a5**2*a6/36 - 13*a1*a2*a5**2/72 - 2*a1*a4*a6**4/3 + 17*a1*a4*a6**3/9 - 19*a1*a4*a6**2/27 + a1*a4*a6/9 - a1*a4/108 + 2*a1*a5**2*a6**3/9 - 29*a1*a5**2*a6**2/54 + a1*a5**2*a6/9 - a1*a5**2/108 + 5*a1*a5*a6**3/6 - a1*a5*a6**2/36 - a1*a5*a6/36 - 7*a2**4*a3*a5/6 - 6*a2**4*a3*a6 + 3*a2**4*a3 - a2**4*a4*a5/2 + a2**3*a3*a6**2/3 - 7*a2**3*a3*a6/3 - a2**3*a3/24 - 10*a2**3*a4*a5*a6/27 + 11*a2**3*a4*a5/108 - 8*a2**3*a4*a6**2/3 + 29*a2**3*a4*a6/12 - 2*a2**3*a4/3 - 5*a2**3*a5**3/54 - 17*a2**3*a5**2*a6/18 + 17*a2**3*a5**2/36 + 2*a2**2*a4*a6**3/9 - 35*a2**2*a4*a6**2/27 + 11*a2**2*a4*a6/54 - a2**2*a4/36 - a2**2*a5**2*a6**2/2 + 7*a2**2*a5**2*a6/108 - a2**2*a5**2/108 - 23*a2**2*a5*a6**3/6 + 101*a2**2*a5*a6**2/18 - 137*a2**2*a5*a6/72 + a2**2*a5/9 - a2*a5*a6**4/3 - 4*a2*a5*a6**3/3 + 67*a2*a5*a6**2/108 - a2*a5*a6/12 + a2*a5/216 - 3*a2*a6**5 + 7*a2*a6**4 - 53*a2*a6**3/12 + 41*a2*a6**2/36 - a2*a6/9 - 5*a6**5/3 + 3*a6**4/2 - 55*a6**3/108 + 17*a6**2/216 - a6/216",
      "-3*a0**2*a2*a3**2*a5/4 + a0**2*a2*a3*a4**2/6 + a0**2*a3**2*a6 - a0**2*a3**2/6 - a0**2*a3*a4*a5*a6/12 - 17*a0**2*a3*a4*a5/72 - a0**2*a3*a5**3/4 + a0**2*a4**3*a6/9 + a0**2*a4**3/27 + 5*a0**2*a4**2*a5**2/108 + 3*a0*a1**2*a3**2*a5/4 - a0*a1**2*a3*a4**2/6 + 3*a0*a1*a2*a3**2*a6 - 9*a0*a1*a2*a3**2/4 - 29*a0*a1*a2*a3*a4*a5/12 + 4*a0*a1*a2*a4**3/9 - 5*a0*a1*a3*a4*a6**2/2 + 7*a0*a1*a3*a4*a6/12 + a0*a1*a3*a4/6 - 11*a0*a1*a3*a5**2*a6/4 + 19*a0*a1*a3*a5**2/24 + 8*a0*a1*a4**2*a5*a6/9 - a0*a1*a4**2*a5/6 - 9*a0*a2**3*a3**2/2 - 11*a0*a2**2*a3*a4*a6/2 + 5*a0*a2**2*a3*a4/6 - 7*a0*a2**2*a3*a5**2/2 + 19*a0*a2**2*a4**2*a5/18 - 59*a0*a2*a3*a5*a6**2/4 + 85*a0*a2*a3*a5*a6/24 - 11*a0*a2*a3*a5/24 - 5*a0*a2*a4**2*a6**2/3 + 61*a0*a2*a4**2*a6/36 - a0*a2*a4**2/9 + 19*a0*a2*a4*a5**2*a6/9 - a0*a2*a4*a5**2/2 - 2*a0*a2*a5**4/9 - 11*a0*a3*a6**3 + 73*a0*a3*a6**2/12 - 23*a0*a3*a6/24 + a0*a3/24 - 3*a0*a4*a5*a6**3/2 + 103*a0*a4*a5*a6**2/36 - 13*a0*a4*a5*a6/18 + a0*a4*a5/24 + a0*a5**3*a6**2/3 - 31*a0*a5**3*a6/72 + a0*a5**3/36 + 3*a1**3*a3**2/4 + 3*a1**3*a3*a4*a5/2 - a1**3*a4**3/3 + 3*a1**2*a2**2*a3**2/2 + 7*a1**2*a2*a3*a4*a6 - a1**2*a2*a3*a4 + 3*a1**2*a2*a3*a5**2 - 7*a1**2*a2*a4**2*a5/6 - 3*a1**2*a3*a5*a6**2 + 11*a1**2*a3*a5*a6/2 - a1**2*a3*a5/2 + 2*a1**2*a4**2*a6**2 - 2*a1**2*a4**2*a6 + a1**2*a4**2/4 - a1**2*a4*a5**2*a6/2 + a1**2*a4*a5**2/6 + a1**2*a5**4/12 - 2*a1*a2**3*a3*a4 + 15*a1*a2**2*a3*a5*a6 - 29*a1*a2**2*a3*a5/8 - a1*a2**2*a4**2*a6 + 5*a1*a2**2*a4**2/12 - a1*a2**2*a4*a5**2 - 3*a1*a2*a3*a6**3 + 23*a1*a2*a3*a6**2 - 47*a1*a2*a3*a6/8 + a1*a2*a3/16 + 7*a1*a2*a4*a5*a6**2/6 - 25*a1*a2*a4*a5*a6/12 + 5*a1*a2*a4*a5/24 - a1*a2*a5**3*a6/6 + a1*a2*a5**3/24 - 3*a1*a4*a6**4 + 17*a1*a4*a6**3/2 - 19*a1*a4*a6**2/6 + a1*a4*a6/2 - a1*a4/24 + a1*a5**2*a6**3 - 29*a1*a5**2*a6**2/12 + a1*a5**2*a6/2 - a1*a5**2/24 - 21*a2**4*a3*a5/4 + 3*a2**3*a3*a6**2/2 - 21*a2**3*a3*a6/2 - 3*a2**3*a3/16 - 5*a2**3*a4*a5*a6/3 + 11*a2**3*a4*a5/24 - 5*a2**3*a5**3/12 + a2**2*a4*a6**3 - 35*a2**2*a4*a6**2/6 + 11*a2**2*a4*a6/12 - a2**2*a4/8 - 9*a2**2*a5**2*a6**2/4 + 7*a2**2*a5**2*a6/24 - a2**2*a5**2/24 - 3*a2*a5*a6**4/2 - 6*a2*a5*a6**3 + 67*a2*a5*a6**2/24 - 3*a2*a5*a6/8 + a2*a5/48 - 15*a6**5/2 + 27*a6**4/4 - 55*a6**3/24 + 17*a6**2/48 - a6/48",
      "a0**2*a2*a3**2*a5/9 - 2*a0**2*a2*a3*a4**2/81 + a0**2*a2*a3*a4*a5/9 + a0**2*a2*a3*a5**2/3 - 2*a0**2*a2*a4**3/81 - 5*a0**2*a2*a4**2*a5/54 - 4*a0**2*a3**2*a6/27 + 2*a0**2*a3**2/81 + a0**2*a3*a4*a5*a6/81 + 17*a0**2*a3*a4*a5/486 - 4*a0**2*a3*a4*a6/27 + 2*a0**2*a3*a4/81 + a0**2*a3*a5**3/27 + a0**2*a3*a5**2*a6/3 + 7*a0**2*a3*a5**2/162 + 2*a0**2*a3*a5*a6**2 - 7*a0**2*a3*a5*a6/9 + a0**2*a3*a5/36 - 4*a0**2*a4**3*a6/243 - 4*a0**2*a4**3/729 - 5*a0**2*a4**2*a5**2/729 - 4*a0**2*a4**2*a5*a6/27 + a0**2*a4**2*a5/243 - 2*a0**2*a4**2*a6**2/9 + 2*a0**2*a4**2/81 + 4*a0**2*a4*a5**3/243 - 19*a0**2*a4*a5**2*a6/54 + 29*a0**2*a4*a5**2/324 + 2*a0**2*a5**4/27 - a0*a1**2*a3**2*a5/9 + 2*a0*a1**2*a3*a4**2/81 - a0*a1**2*a3*a4*a5/9 - a0*a1**2*a3*a5**2/6 + 2*a0*a1**2*a4**3/81 + a0*a1**2*a4**2*a5/27 - 4*a0*a1*a2*a3**2*a6/9 + a0*a1*a2*a3**2/3 + 29*a0*a1*a2*a3*a4*a5/81 - 4*a0*a1*a2*a3*a4*a6/9 + a0*a1*a2*a3*a4/3 + 2*a0*a1*a2*a3*a5**2/27 - 4*a0*a1*a2*a3*a5*a6/3 + a0*a1*a2*a3*a5/18 - 16*a0*a1*a2*a4**3/243 + 11*a0*a1*a2*a4**2*a5/81 - 5*a0*a1*a2*a4**2*a6/9 + 8*a0*a1*a2*a4**2/27 + a0*a1*a2*a4*a5**2/2 + 10*a0*a1*a3*a4*a6**2/27 - 7*a0*a1*a3*a4*a6/81 - 2*a0*a1*a3*a4/81 + 11*a0*a1*a3*a5**2*a6/27 - 19*a0*a1*a3*a5**2/162 + 2*a0*a1*a3*a5*a6**2 - 2*a0*a1*a3*a5*a6/9 - 2*a0*a1*a3*a5/27 + 6*a0*a1*a3*a6**3 - 3*a0*a1*a3*a6**2 + a0*a1*a3*a6/6 + a0*a1*a3/18 - 32*a0*a1*a4**2*a5*a6/243 + 2*a0*a1*a4**2*a5/81 - 8*a0*a1*a4**2*a6**2/27 + 2*a0*a1*a4**2*a6/81 - a0*a1*a4**2/81 + a0*a1*a4*a5**2*a6/81 - a0*a1*a4*a5**2/18 - 14*a0*a1*a4*a5*a6**2/9 + 31*a0*a1*a4*a5*a6/54 - 5*a0*a1*a4*a5/108 + a0*a1*a5**3*a6/2 - 5*a0*a1*a5**3/36 + 2*a0*a2**3*a3**2/3 + 2*a0*a2**3*a3*a4/3 - 2*a0*a2**3*a3*a5 + 4*a0*a2**3*a4**2/3 + 22*a0*a2**2*a3*a4*a6/27 - 10*a0*a2**2*a3*a4/81 + 14*a0*a2**2*a3*a5**2/27 + 10*a0*a2**2*a3*a5*a6/3 - 25*a0*a2**2*a3*a5/27 - 9*a0*a2**2*a3*a6**2 + 31*a0*a2**2*a3*a6/12 - 5*a0*a2**2*a3/18 - 38*a0*a2**2*a4**2*a5/243 - 14*a0*a2**2*a4**2*a6/27 + 7*a0*a2**2*a4**2/27 + 10*a0*a2**2*a4*a5**2/81 + 31*a0*a2**2*a4*a5*a6/9 - 31*a0*a2**2*a4*a5/54 + 59*a0*a2*a3*a5*a6**2/27 - 85*a0*a2*a3*a5*a6/162 + 11*a0*a2*a3*a5/162 + 10*a0*a2*a3*a6**3 - 41*a0*a2*a3*a6**2/6 + 7*a0*a2*a3*a6/4 - 17*a0*a2*a3/108 + 20*a0*a2*a4**2*a6**2/81 - 61*a0*a2*a4**2*a6/243 + 4*a0*a2*a4**2/243 - 76*a0*a2*a4*a5**2*a6/243 + 2*a0*a2*a4*a5**2/27 - 17*a0*a2*a4*a5*a6**2/27 + 5*a0*a2*a4*a5*a6/9 - 11*a0*a2*a4*a5/81 + 7*a0*a2*a4*a6**3/3 - 8*a0*a2*a4*a6**2/3 + 25*a0*a2*a4*a6/54 - a0*a2*a4/54 + 8*a0*a2*a5**4/243 + 14*a0*a2*a5**3*a6/81 - 7*a0*a2*a5**3/81 + 31*a0*a2*a5**2*a6**2/18 - 41*a0*a2*a5**2*a6/108 + a0*a2*a5**2/36 + 44*a0*a3*a6**3/27 - 73*a0*a3*a6**2/81 + 23*a0*a3*a6/162 - a0*a3/162 + 2*a0*a4*a5*a6**3/9 - 103*a0*a4*a5*a6**2/243 + 26*a0*a4*a5*a6/243 - a0*a4*a5/162 + 2*a0*a4*a6**4/3 + 8*a0*a4*a6**3/27 - 17*a0*a4*a6**2/162 - a0*a4*a6/162 - 4*a0*a5**3*a6**2/81 + 31*a0*a5**3*a6/486 - a0*a5**3/243 - 29*a0*a5**2*a6**2/162 - a0*a5**2*a6/36 + 2*a0*a5*a6**4 - 13*a0*a5*a6**3/9 + 5*a0*a5*a6**2/36 + 5*a0*a5*a6/216 - a1**3*a3**2/9 - 2*a1**3*a3*a4*a5/9 - a1**3*a3*a4/9 - 2*a1**3*a3*a5**2/9 - a1**3*a3*a5*a6 + 4*a1**3*a4**3/81 + 2*a1**3*a4**2*a6/3 - a1**3*a4**2/9 - 2*a1**3*a4*a5**2/9 - 2*a1**2*a2**2*a3**2/9 - 2*a1**2*a2**2*a3*a4/9 + 13*a1**2*a2**2*a3*a5/6 - a1**2*a2**2*a4**2 - 28*a1**2*a2*a3*a4*a6/27 + 4*a1**2*a2*a3*a4/27 - 4*a1**2*a2*a3*a5**2/9 - 13*a1**2*a2*a3*a5*a6/3 + 7*a1**2*a2*a3*a5/6 - 12*a1**2*a2*a3*a6**2 + 3*a1**2*a2*a3*a6 + a1**2*a2*a3/4 + 14*a1**2*a2*a4**2*a5/81 + 14*a1**2*a2*a4**2*a6/27 - 8*a1**2*a2*a4**2/27 + a1**2*a2*a4*a5**2/27 + 4*a1**2*a2*a4*a5*a6/9 + a1**2*a2*a4*a5/9 - 2*a1**2*a2*a5**3/9 + 4*a1**2*a3*a5*a6**2/9 - 22*a1**2*a3*a5*a6/27 + 2*a1**2*a3*a5/27 + a1**2*a3*a6**2 - a1**2*a3*a6/2 + a1**2*a3/18 - 8*a1**2*a4**2*a6**2/27 + 8*a1**2*a4**2*a6/27 - a1**2*a4**2/27 + 2*a1**2*a4*a5**2*a6/27 - 2*a1**2*a4*a5**2/81 - 7*a1**2*a4*a5*a6/27 - 4*a1**2*a4*a6**3 + 3*a1**2*a4*a6**2 - 2*a1**2*a4*a6/3 + a1**2*a4/18 - a1**2*a5**4/81 - a1**2*a5**3*a6/27 - a1**2*a5**3/54 + a1**2*a5**2*a6**2 - 5*a1**2*a5**2*a6/6 + a1**2*a5**2/12 + 8*a1*a2**3*a3*a4/27 + 8*a1*a2**3*a3*a5/9 + 19*a1*a2**3*a3*a6 - 31*a1*a2**3*a3/12 - 4*a1*a2**3*a4*a5/3 - 20*a1*a2**2*a3*a5*a6/9 + 29*a1*a2**2*a3*a5/54 - 10*a1*a2**2*a3*a6**2 + 35*a1*a2**2*a3*a6/6 - 35*a1*a2**2*a3/36 + 4*a1*a2**2*a4**2*a6/27 - 5*a1*a2**2*a4**2/81 + 4*a1*a2**2*a4*a5**2/27 + 2*a1*a2**2*a4*a5*a6/9 - 11*a1*a2**2*a4*a5/27 + 6*a1*a2**2*a4*a6**2 - 17*a1*a2**2*a4*a6/6 + 19*a1*a2**2*a4/36 + 4*a1*a2**2*a5**3/27 - 4*a1*a2**2*a5**2*a6/3 + 3*a1*a2**2*a5**2/4 + 4*a1*a2*a3*a6**3/9 - 92*a1*a2*a3*a6**2/27 + 47*a1*a2*a3*a6/54 - a1*a2*a3/108 - 14*a1*a2*a4*a5*a6**2/81 + 25*a1*a2*a4*a5*a6/81 - 5*a1*a2*a4*a5/162 - 20*a1*a2*a4*a6**3/9 + 40*a1*a2*a4*a6**2/27 - 8*a1*a2*a4*a6/9 + 4*a1*a2*a4/27 + 2*a1*a2*a5**3*a6/81 - a1*a2*a5**3/162 + 16*a1*a2*a5**2*a6**2/27 - 47*a1*a2*a5**2*a6/54 + 13*a1*a2*a5**2/108 + 13*a1*a2*a5*a6**3/3 - 23*a1*a2*a5*a6**2/6 + 13*a1*a2*a5*a6/36 + a1*a2*a5/18 + 4*a1*a4*a6**4/9 - 34*a1*a4*a6**3/27 + 38*a1*a4*a6**2/81 - 2*a1*a4*a6/27 + a1*a4/162 - 4*a1*a5**2*a6**3/27 + 29*a1*a5**2*a6**2/81 - 2*a1*a5**2*a6/27 + a1*a5**2/162 - 5*a1*a5*a6**3/9 + a1*a5*a6**2/54 + a1*a5*a6/54 + 6*a1*a6**5 - 8*a1*a6**4 + 7*a1*a6**3/3 - a1*a6**2/12 - a1*a6/36 - 6*a2**5*a3 + 7*a2**4*a3*a5/9 + 4*a2**4*a3*a6 - 2*a2**4*a3 + a2**4*a4*a5/3 - 3*a2**4*a4*a6 + 5*a2**4*a4/4 - a2**4*a5**2/3 - 2*a2**3*a3*a6**2/9 + 14*a2**3*a3*a6/9 + a2**3*a3/36 + 20*a2**3*a4*a5*a6/81 - 11*a2**3*a4*a5/162 + 16*a2**3*a4*a6**2/9 - 29*a2**3*a4*a6/18 + 4*a2**3*a4/9 + 5*a2**3*a5**3/81 + 17*a2**3*a5**2*a6/27 - 17*a2**3*a5**2/54 - 9*a2**3*a5*a6**2/2 + 137*a2**3*a5*a6/36 - 5*a2**3*a5/72 - 4*a2**2*a4*a6**3/27 + 70*a2**2*a4*a6**2/81 - 11*a2**2*a4*a6/81 + a2**2*a4/54 + a2**2*a5**2*a6**2/3 - 7*a2**2*a5**2*a6/162 + a2**2*a5**2/162 + 23*a2**2*a5*a6**3/9 - 101*a2**2*a5*a6**2/27 + 137*a2**2*a5*a6/108 - 2*a2**2*a5/27 - 5*a2**2*a6**4 + 41*a2**2*a6**3/6 - 65*a2**2*a6**2/36 + 11*a2**2*a6/72 + 2*a2*a5*a6**4/9 + 8*a2*a5*a6**3/9 - 67*a2*a5*a6**2/162 + a2*a5*a6/18 - a2*a5/324 + 2*a2*a6**5 - 14*a2*a6**4/3 + 53*a2*a6**3/18 - 41*a2*a6**2/54 + 2*a2*a6/27 + 10*a6**5/9 - a6**4 + 55*a6**3/162 - 17*a6**2/324 + a6/324",
      "a0**2*a1*a3*a5**2/6 - a0**2*a1*a4**2*a5/18 - 2*a0**2*a2*a3**2*a5/27 + 4*a0**2*a2*a3*a4**2/243 - 2*a0**2*a2*a3*a4*a5/27 - 2*a0**2*a2*a3*a5**2/9 + 3*a0**2*a2*a3*a5*a6/2 + a0**2*a2*a3*a5/9 + 4*a0**2*a2*a4**3/243 + 5*a0**2*a2*a4**2*a5/81 - a0**2*a2*a4**2*a6/9 - 7*a0**2*a2*a4**2/54 - 4*a0**2*a2*a4*a5**2/27 + 8*a0**2*a3**2*a6/81 - 4*a0**2*a3**2/243 - 2*a0**2*a3*a4*a5*a6/243 - 17*a0**2*a3*a4*a5/729 + 8*a0**2*a3*a4*a6/81 - 4*a0**2*a3*a4/243 - 2*a0**2*a3*a5**3/81 - 2*a0**2*a3*a5**2*a6/9 - 7*a0**2*a3*a5**2/243 - 4*a0**2*a3*a5*a6**2/3 + 14*a0**2*a3*a5*a6/27 - a0**2*a3*a5/54 + 7*a0**2*a3*a6**2/6 - 13*a0**2*a3*a6/36 + a0**2*a3/36 + 8*a0**2*a4**3*a6/729 + 8*a0**2*a4**3/2187 + 10*a0**2*a4**2*a5**2/2187 + 8*a0**2*a4**2*a5*a6/81 - 2*a0**2*a4**2*a5/729 + 4*a0**2*a4**2*a6**2/27 - 4*a0**2*a4**2/243 - 8*a0**2*a4*a5**3/729 + 19*a0**2*a4*a5**2*a6/81 - 29*a0**2*a4*a5**2/486 + 11*a0**2*a4*a5*a6**2/18 - 49*a0**2*a4*a5*a6/108 + a0**2*a4*a5/18 - 4*a0**2*a5**4/81 - 2*a0**2*a5**3*a6/9 + 2*a0**2*a5**3/27 + 2*a0*a1**2*a3**2*a5/27 - 4*a0*a1**2*a3*a4**2/243 + 2*a0*a1**2*a3*a4*a5/27 + a0*a1**2*a3*a5**2/9 - a0*a1**2*a3*a5*a6/2 - a0*a1**2*a3*a5/2 - 4*a0*a1**2*a4**3/243 - 2*a0*a1**2*a4**2*a5/81 + 2*a0*a1**2*a4**2*a6/9 + a0*a1**2*a4**2/6 - 8*a0*a1*a2**2*a3*a5/3 + 4*a0*a1*a2**2*a4**2/9 + 8*a0*a1*a2*a3**2*a6/27 - 2*a0*a1*a2*a3**2/9 - 58*a0*a1*a2*a3*a4*a5/243 + 8*a0*a1*a2*a3*a4*a6/27 - 2*a0*a1*a2*a3*a4/9 - 4*a0*a1*a2*a3*a5**2/81 + 8*a0*a1*a2*a3*a5*a6/9 - a0*a1*a2*a3*a5/27 - 7*a0*a1*a2*a3*a6**2 + 5*a0*a1*a2*a3*a6/4 - a0*a1*a2*a3/3 + 32*a0*a1*a2*a4**3/729 - 22*a0*a1*a2*a4**2*a5/243 + 10*a0*a1*a2*a4**2*a6/27 - 16*a0*a1*a2*a4**2/81 - a0*a1*a2*a4*a5**2/3 + 13*a0*a1*a2*a4*a5*a6/18 - 4*a0*a1*a2*a5**3/9 - 20*a0*a1*a3*a4*a6**2/81 + 14*a0*a1*a3*a4*a6/243 + 4*a0*a1*a3*a4/243 - 22*a0*a1*a3*a5**2*a6/81 + 19*a0*a1*a3*a5**2/243 - 4*a0*a1*a3*a5*a6**2/3 + 4*a0*a1*a3*a5*a6/27 + 4*a0*a1*a3*a5/81 - 4*a0*a1*a3*a6**3 + 2*a0*a1*a3*a6**2 - a0*a1*a3*a6/9 - a0*a1*a3/27 + 64*a0*a1*a4**2*a5*a6/729 - 4*a0*a1*a4**2*a5/243 + 16*a0*a1*a4**2*a6**2/81 - 4*a0*a1*a4**2*a6/243 + 2*a0*a1*a4**2/243 - 2*a0*a1*a4*a5**2*a6/243 + a0*a1*a4*a5**2/27 + 28*a0*a1*a4*a5*a6**2/27 - 31*a0*a1*a4*a5*a6/81 + 5*a0*a1*a4*a5/162 - 2*a0*a1*a4*a6**3/3 - 4*a0*a1*a4*a6**2/9 + 2*a0*a1*a4*a6/9 - a0*a1*a4/36 - a0*a1*a5**3*a6/3 + 5*a0*a1*a5**3/54 - 5*a0*a1*a5**2*a6**2/6 + 7*a0*a1*a5**2*a6/9 - a0*a1*a5**2/6 - 4*a0*a2**3*a3**2/9 - 4*a0*a2**3*a3*a4/9 + 4*a0*a2**3*a3*a5/3 + 3*a0*a2**3*a3*a6 - 2*a0*a2**3*a3/3 - 8*a0*a2**3*a4**2/9 - 7*a0*a2**3*a4*a5/9 - 44*a0*a2**2*a3*a4*a6/81 + 20*a0*a2**2*a3*a4/243 - 28*a0*a2**2*a3*a5**2/81 - 20*a0*a2**2*a3*a5*a6/9 + 50*a0*a2**2*a3*a5/81 + 6*a0*a2**2*a3*a6**2 - 31*a0*a2**2*a3*a6/18 + 5*a0*a2**2*a3/27 + 76*a0*a2**2*a4**2*a5/729 + 28*a0*a2**2*a4**2*a6/81 - 14*a0*a2**2*a4**2/81 - 20*a0*a2**2*a4*a5**2/243 - 62*a0*a2**2*a4*a5*a6/27 + 31*a0*a2**2*a4*a5/81 + 5*a0*a2**2*a4*a6**2/3 - 11*a0*a2**2*a4*a6/9 + a0*a2**2*a4/18 - 17*a0*a2**2*a5**2*a6/9 + a0*a2**2*a5**2/2 - 118*a0*a2*a3*a5*a6**2/81 + 85*a0*a2*a3*a5*a6/243 - 11*a0*a2*a3*a5/243 - 20*a0*a2*a3*a6**3/3 + 41*a0*a2*a3*a6**2/9 - 7*a0*a2*a3*a6/6 + 17*a0*a2*a3/162 - 40*a0*a2*a4**2*a6**2/243 + 122*a0*a2*a4**2*a6/729 - 8*a0*a2*a4**2/729 + 152*a0*a2*a4*a5**2*a6/729 - 4*a0*a2*a4*a5**2/81 + 34*a0*a2*a4*a5*a6**2/81 - 10*a0*a2*a4*a5*a6/27 + 22*a0*a2*a4*a5/243 - 14*a0*a2*a4*a6**3/9 + 16*a0*a2*a4*a6**2/9 - 25*a0*a2*a4*a6/81 + a0*a2*a4/81 - 16*a0*a2*a5**4/729 - 28*a0*a2*a5**3*a6/243 + 14*a0*a2*a5**3/243 - 31*a0*a2*a5**2*a6**2/27 + 41*a0*a2*a5**2*a6/162 - a0*a2*a5**2/54 - 17*a0*a2*a5*a6**3/6 + 25*a0*a2*a5*a6**2/18 - 17*a0*a2*a5*a6/36 + a0*a2*a5/18 - 88*a0*a3*a6**3/81 + 146*a0*a3*a6**2/243 - 23*a0*a3*a6/243 + a0*a3/243 - 4*a0*a4*a5*a6**3/27 + 206*a0*a4*a5*a6**2/729 - 52*a0*a4*a5*a6/729 + a0*a4*a5/243 - 4*a0*a4*a6**4/9 - 16*a0*a4*a6**3/81 + 17*a0*a4*a6**2/243 + a0*a4*a6/243 + 8*a0*a5**3*a6**2/243 - 31*a0*a5**3*a6/729 + 2*a0*a5**3/729 + 29*a0*a5**2*a6**2/243 + a0*a5**2*a6/54 - 4*a0*a5*a6**4/3 + 26*a0*a5*a6**3/27 - 5*a0*a5*a6**2/54 - 5*a0*a5*a6/324 - 11*a0*a6**4/6 + 14*a0*a6**3/9 - 11*a0*a6**2/24 + a0*a6/24 + 3*a1**3*a2*a3*a5/2 - a1**3*a2*a4**2/3 + 2*a1**3*a3**2/27 + 4*a1**3*a3*a4*a5/27 + 2*a1**3*a3*a4/27 + 4*a1**3*a3*a5**2/27 + 2*a1**3*a3*a5*a6/3 - a1**3*a3*a6 + a1**3*a3/2 - 8*a1**3*a4**3/243 - 4*a1**3*a4**2*a6/9 + 2*a1**3*a4**2/27 + 4*a1**3*a4*a5**2/27 + a1**3*a4*a5/6 + a1**3*a5**3/6 + 4*a1**2*a2**2*a3**2/27 + 4*a1**2*a2**2*a3*a4/27 - 13*a1**2*a2**2*a3*a5/9 + 4*a1**2*a2**2*a3*a6 + a1**2*a2**2*a3/4 + 2*a1**2*a2**2*a4**2/3 + 56*a1**2*a2*a3*a4*a6/81 - 8*a1**2*a2*a3*a4/81 + 8*a1**2*a2*a3*a5**2/27 + 26*a1**2*a2*a3*a5*a6/9 - 7*a1**2*a2*a3*a5/9 + 8*a1**2*a2*a3*a6**2 - 2*a1**2*a2*a3*a6 - a1**2*a2*a3/6 - 28*a1**2*a2*a4**2*a5/243 - 28*a1**2*a2*a4**2*a6/81 + 16*a1**2*a2*a4**2/81 - 2*a1**2*a2*a4*a5**2/81 - 8*a1**2*a2*a4*a5*a6/27 - 2*a1**2*a2*a4*a5/27 + 2*a1**2*a2*a4*a6**2/3 + a1**2*a2*a4*a6/2 + 4*a1**2*a2*a5**3/27 + 7*a1**2*a2*a5**2*a6/6 - a1**2*a2*a5**2/12 - 8*a1**2*a3*a5*a6**2/27 + 44*a1**2*a3*a5*a6/81 - 4*a1**2*a3*a5/81 - 2*a1**2*a3*a6**2/3 + a1**2*a3*a6/3 - a1**2*a3/27 + 16*a1**2*a4**2*a6**2/81 - 16*a1**2*a4**2*a6/81 + 2*a1**2*a4**2/81 - 4*a1**2*a4*a5**2*a6/81 + 4*a1**2*a4*a5**2/243 + 14*a1**2*a4*a5*a6/81 + 8*a1**2*a4*a6**3/3 - 2*a1**2*a4*a6**2 + 4*a1**2*a4*a6/9 - a1**2*a4/27 + 2*a1**2*a5**4/243 + 2*a1**2*a5**3*a6/81 + a1**2*a5**3/81 - 2*a1**2*a5**2*a6**2/3 + 5*a1**2*a5**2*a6/9 - a1**2*a5**2/18 + 3*a1**2*a5*a6**2/2 - 11*a1**2*a5*a6/12 + a1**2*a5/12 - 2*a1*a2**4*a3 - 16*a1*a2**3*a3*a4/81 - 16*a1*a2**3*a3*a5/27 - 38*a1*a2**3*a3*a6/3 + 31*a1*a2**3*a3/18 + 8*a1*a2**3*a4*a5/9 - a1*a2**3*a4*a6 + 5*a1*a2**3*a4/12 - a1*a2**3*a5**2/6 + 40*a1*a2**2*a3*a5*a6/27 - 29*a1*a2**2*a3*a5/81 + 20*a1*a2**2*a3*a6**2/3 - 35*a1*a2**2*a3*a6/9 + 35*a1*a2**2*a3/54 - 8*a1*a2**2*a4**2*a6/81 + 10*a1*a2**2*a4**2/243 - 8*a1*a2**2*a4*a5**2/81 - 4*a1*a2**2*a4*a5*a6/27 + 22*a1*a2**2*a4*a5/81 - 4*a1*a2**2*a4*a6**2 + 17*a1*a2**2*a4*a6/9 - 19*a1*a2**2*a4/54 - 8*a1*a2**2*a5**3/81 + 8*a1*a2**2*a5**2*a6/9 - a1*a2**2*a5**2/2 + 13*a1*a2**2*a5*a6**2/6 - 7*a1*a2**2*a5*a6/12 + a1*a2**2*a5/4 - 8*a1*a2*a3*a6**3/27 + 184*a1*a2*a3*a6**2/81 - 47*a1*a2*a3*a6/81 + a1*a2*a3/162 + 28*a1*a2*a4*a5*a6**2/243 - 50*a1*a2*a4*a5*a6/243 + 5*a1*a2*a4*a5/243 + 40*a1*a2*a4*a6**3/27 - 80*a1*a2*a4*a6**2/81 + 16*a1*a2*a4*a6/27 - 8*a1*a2*a4/81 - 4*a1*a2*a5**3*a6/243 + a1*a2*a5**3/243 - 32*a1*a2*a5**2*a6**2/81 + 47*a1*a2*a5**2*a6/81 - 13*a1*a2*a5**2/162 - 26*a1*a2*a5*a6**3/9 + 23*a1*a2*a5*a6**2/9 - 13*a1*a2*a5*a6/54 - a1*a2*a5/27 + a1*a2*a6**4 + 17*a1*a2*a6**3/6 - 3*a1*a2*a6**2 + 5*a1*a2*a6/12 + a1*a2/24 - 8*a1*a4*a6**4/27 + 68*a1*a4*a6**3/81 - 76*a1*a4*a6**2/243 + 4*a1*a4*a6/81 - a1*a4/243 + 8*a1*a5**2*a6**3/81 - 58*a1*a5**2*a6**2/243 + 4*a1*a5**2*a6/81 - a1*a5**2/243 + 10*a1*a5*a6**3/27 - a1*a5*a6**2/81 - a1*a5*a6/81 - 4*a1*a6**5 + 16*a1*a6**4/3 - 14*a1*a6**3/9 + a1*a6**2/18 + a1*a6/54 + 4*a2**5*a3 - 14*a2**4*a3*a5/27 - 8*a2**4*a3*a6/3 + 4*a2**4*a3/3 - 2*a2**4*a4*a5/9 + 2*a2**4*a4*a6 - 5*a2**4*a4/6 + 2*a2**4*a5**2/9 - 7*a2**4*a5*a6/6 + a2**4*a5/3 + 4*a2**3*a3*a6**2/27 - 28*a2**3*a3*a6/27 - a2**3*a3/54 - 40*a2**3*a4*a5*a6/243 + 11*a2**3*a4*a5/243 - 32*a2**3*a4*a6**2/27 + 29*a2**3*a4*a6/27 - 8*a2**3*a4/27 - 10*a2**3*a5**3/243 - 34*a2**3*a5**2*a6/81 + 17*a2**3*a5**2/81 + 3*a2**3*a5*a6**2 - 137*a2**3*a5*a6/54 + 5*a2**3*a5/108 - a2**3*a6**3 - a2**3*a6**2/3 + 19*a2**3*a6/24 + a2**3/8 + 8*a2**2*a4*a6**3/81 - 140*a2**2*a4*a6**2/243 + 22*a2**2*a4*a6/243 - a2**2*a4/81 - 2*a2**2*a5**2*a6**2/9 + 7*a2**2*a5**2*a6/243 - a2**2*a5**2/243 - 46*a2**2*a5*a6**3/27 + 202*a2**2*a5*a6**2/81 - 137*a2**2*a5*a6/162 + 4*a2**2*a5/81 + 10*a2**2*a6**4/3 - 41*a2**2*a6**3/9 + 65*a2**2*a6**2/54 - 11*a2**2*a6/108 - 4*a2*a5*a6**4/27 - 16*a2*a5*a6**3/27 + 67*a2*a5*a6**2/243 - a2*a5*a6/27 + a2*a5/486 - 4*a2*a6**5/3 + 28*a2*a6**4/9 - 53*a2*a6**3/27 + 41*a2*a6**2/81 - 4*a2*a6/81 - 20*a6**5/27 + 2*a6**4/3 - 55*a6**3/243 + 17*a6**2/486 - a6/486",
      "a0**3*a3*a5**2/6 - a0**3*a4**2*a5/18 - a0**2*a1*a3*a5**2/9 + a0**2*a1*a3*a5*a6 - 7*a0**2*a1*a3*a5/18 + a0**2*a1*a4**2*a5/27 + a0**2*a1*a4**2*a6/9 + a0**2*a1*a4**2/27 - 4*a0**2*a1*a4*a5**2/27 - 7*a0**2*a2**2*a3*a5/2 + 13*a0**2*a2**2*a4**2/9 + 4*a0**2*a2*a3**2*a5/81 - 8*a0**2*a2*a3*a4**2/729 + 4*a0**2*a2*a3*a4*a5/81 + 4*a0**2*a2*a3*a5**2/27 - a0**2*a2*a3*a5*a6 - 2*a0**2*a2*a3*a5/27 - 15*a0**2*a2*a3*a6**2 + 77*a0**2*a2*a3*a6/12 - 25*a0**2*a2*a3/36 - 8*a0**2*a2*a4**3/729 - 10*a0**2*a2*a4**2*a5/243 + 2*a0**2*a2*a4**2*a6/27 + 7*a0**2*a2*a4**2/81 + 8*a0**2*a2*a4*a5**2/81 + 77*a0**2*a2*a4*a5*a6/18 - 91*a0**2*a2*a4*a5/108 - 2*a0**2*a2*a5**3/3 - 16*a0**2*a3**2*a6/243 + 8*a0**2*a3**2/729 + 4*a0**2*a3*a4*a5*a6/729 + 34*a0**2*a3*a4*a5/2187 - 16*a0**2*a3*a4*a6/243 + 8*a0**2*a3*a4/729 + 4*a0**2*a3*a5**3/243 + 4*a0**2*a3*a5**2*a6/27 + 14*a0**2*a3*a5**2/729 + 8*a0**2*a3*a5*a6**2/9 - 28*a0**2*a3*a5*a6/81 + a0**2*a3*a5/81 - 7*a0**2*a3*a6**2/9 + 13*a0**2*a3*a6/54 - a0**2*a3/54 - 16*a0**2*a4**3*a6/2187 - 16*a0**2*a4**3/6561 - 20*a0**2*a4**2*a5**2/6561 - 16*a0**2*a4**2*a5*a6/243 + 4*a0**2*a4**2*a5/2187 - 8*a0**2*a4**2*a6**2/81 + 8*a0**2*a4**2/729 + 16*a0**2*a4*a5**3/2187 - 38*a0**2*a4*a5**2*a6/243 + 29*a0**2*a4*a5**2/729 - 11*a0**2*a4*a5*a6**2/27 + 49*a0**2*a4*a5*a6/162 - a0**2*a4*a5/27 - a0**2*a4*a6**3 - a0**2*a4*a6**2/6 - a0**2*a4*a6/9 + a0**2*a4/54 + 8*a0**2*a5**4/243 + 4*a0**2*a5**3*a6/27 - 4*a0**2*a5**3/81 + 2*a0**2*a5**2*a6**2/3 + a0**2*a5**2*a6/36 + a0**2*a5**2/54 + 10*a0*a1**2*a2*a3*a5/3 - 2*a0*a1**2*a2*a4**2 - 4*a0*a1**2*a3**2*a5/81 + 8*a0*a1**2*a3*a4**2/729 - 4*a0*a1**2*a3*a4*a5/81 - 2*a0*a1**2*a3*a5**2/27 + a0*a1**2*a3*a5*a6/3 + a0*a1**2*a3*a5/3 + 6*a0*a1**2*a3*a6**2 - 7*a0*a1**2*a3*a6/2 + a0*a1**2*a3/2 + 8*a0*a1**2*a4**3/729 + 4*a0*a1**2*a4**2*a5/243 - 4*a0*a1**2*a4**2*a6/27 - a0*a1**2*a4**2/9 - 19*a0*a1**2*a4*a5*a6/9 + 5*a0*a1**2*a4*a5/9 + a0*a1**2*a5**3/6 + 16*a0*a1*a2**2*a3*a5/9 + 23*a0*a1*a2**2*a3*a6 - 59*a0*a1*a2**2*a3/12 - 8*a0*a1*a2**2*a4**2/27 - 65*a0*a1*a2**2*a4*a5/18 - 16*a0*a1*a2*a3**2*a6/81 + 4*a0*a1*a2*a3**2/27 + 116*a0*a1*a2*a3*a4*a5/729 - 16*a0*a1*a2*a3*a4*a6/81 + 4*a0*a1*a2*a3*a4/27 + 8*a0*a1*a2*a3*a5**2/243 - 16*a0*a1*a2*a3*a5*a6/27 + 2*a0*a1*a2*a3*a5/81 + 14*a0*a1*a2*a3*a6**2/3 - 5*a0*a1*a2*a3*a6/6 + 2*a0*a1*a2*a3/9 - 64*a0*a1*a2*a4**3/2187 + 44*a0*a1*a2*a4**2*a5/729 - 20*a0*a1*a2*a4**2*a6/81 + 32*a0*a1*a2*a4**2/243 + 2*a0*a1*a2*a4*a5**2/9 - 13*a0*a1*a2*a4*a5*a6/27 + 23*a0*a1*a2*a4*a6**2/3 - 4*a0*a1*a2*a4*a6 + 11*a0*a1*a2*a4/12 + 8*a0*a1*a2*a5**3/27 - 43*a0*a1*a2*a5**2*a6/18 + 11*a0*a1*a2*a5**2/9 + 40*a0*a1*a3*a4*a6**2/243 - 28*a0*a1*a3*a4*a6/729 - 8*a0*a1*a3*a4/729 + 44*a0*a1*a3*a5**2*a6/243 - 38*a0*a1*a3*a5**2/729 + 8*a0*a1*a3*a5*a6**2/9 - 8*a0*a1*a3*a5*a6/81 - 8*a0*a1*a3*a5/243 + 8*a0*a1*a3*a6**3/3 - 4*a0*a1*a3*a6**2/3 + 2*a0*a1*a3*a6/27 + 2*a0*a1*a3/81 - 128*a0*a1*a4**2*a5*a6/2187 + 8*a0*a1*a4**2*a5/729 - 32*a0*a1*a4**2*a6**2/243 + 8*a0*a1*a4**2*a6/729 - 4*a0*a1*a4**2/729 + 4*a0*a1*a4*a5**2*a6/729 - 2*a0*a1*a4*a5**2/81 - 56*a0*a1*a4*a5*a6**2/81 + 62*a0*a1*a4*a5*a6/243 - 5*a0*a1*a4*a5/243 + 4*a0*a1*a4*a6**3/9 + 8*a0*a1*a4*a6**2/27 - 4*a0*a1*a4*a6/27 + a0*a1*a4/54 + 2*a0*a1*a5**3*a6/9 - 5*a0*a1*a5**3/81 + 5*a0*a1*a5**2*a6**2/9 - 14*a0*a1*a5**2*a6/27 + a0*a1*a5**2/9 + 4*a0*a1*a5*a6**3 - 31*a0*a1*a5*a6**2/18 - 5*a0*a1*a5*a6/36 - a0*a1*a5/18 - 9*a0*a2**4*a3 + 8*a0*a2**3*a3**2/27 + 8*a0*a2**3*a3*a4/27 - 8*a0*a2**3*a3*a5/9 - 2*a0*a2**3*a3*a6 + 4*a0*a2**3*a3/9 + 16*a0*a2**3*a4**2/27 + 14*a0*a2**3*a4*a5/27 - 14*a0*a2**3*a4*a6/3 + 25*a0*a2**3*a4/12 - 13*a0*a2**3*a5**2/6 + 88*a0*a2**2*a3*a4*a6/243 - 40*a0*a2**2*a3*a4/729 + 56*a0*a2**2*a3*a5**2/243 + 40*a0*a2**2*a3*a5*a6/27 - 100*a0*a2**2*a3*a5/243 - 4*a0*a2**2*a3*a6**2 + 31*a0*a2**2*a3*a6/27 - 10*a0*a2**2*a3/81 - 152*a0*a2**2*a4**2*a5/2187 - 56*a0*a2**2*a4**2*a6/243 + 28*a0*a2**2*a4**2/243 + 40*a0*a2**2*a4*a5**2/729 + 124*a0*a2**2*a4*a5*a6/81 - 62*a0*a2**2*a4*a5/243 - 10*a0*a2**2*a4*a6**2/9 + 22*a0*a2**2*a4*a6/27 - a0*a2**2*a4/27 + 34*a0*a2**2*a5**2*a6/27 - a0*a2**2*a5**2/3 - 28*a0*a2**2*a5*a6**2/3 + 241*a0*a2**2*a5*a6/36 - 13*a0*a2**2*a5/18 + 236*a0*a2*a3*a5*a6**2/243 - 170*a0*a2*a3*a5*a6/729 + 22*a0*a2*a3*a5/729 + 40*a0*a2*a3*a6**3/9 - 82*a0*a2*a3*a6**2/27 + 7*a0*a2*a3*a6/9 - 17*a0*a2*a3/243 + 80*a0*a2*a4**2*a6**2/729 - 244*a0*a2*a4**2*a6/2187 + 16*a0*a2*a4**2/2187 - 304*a0*a2*a4*a5**2*a6/2187 + 8*a0*a2*a4*a5**2/243 - 68*a0*a2*a4*a5*a6**2/243 + 20*a0*a2*a4*a5*a6/81 - 44*a0*a2*a4*a5/729 + 28*a0*a2*a4*a6**3/27 - 32*a0*a2*a4*a6**2/27 + 50*a0*a2*a4*a6/243 - 2*a0*a2*a4/243 + 32*a0*a2*a5**4/2187 + 56*a0*a2*a5**3*a6/729 - 28*a0*a2*a5**3/729 + 62*a0*a2*a5**2*a6**2/81 - 41*a0*a2*a5**2*a6/243 + a0*a2*a5**2/81 + 17*a0*a2*a5*a6**3/9 - 25*a0*a2*a5*a6**2/27 + 17*a0*a2*a5*a6/54 - a0*a2*a5/27 - 3*a0*a2*a6**4 + 37*a0*a2*a6**3/6 - 31*a0*a2*a6**2/9 + 13*a0*a2*a6/24 - a0*a2/72 + 176*a0*a3*a6**3/243 - 292*a0*a3*a6**2/729 + 46*a0*a3*a6/729 - 2*a0*a3/729 + 8*a0*a4*a5*a6**3/81 - 412*a0*a4*a5*a6**2/2187 + 104*a0*a4*a5*a6/2187 - 2*a0*a4*a5/729 + 8*a0*a4*a6**4/27 + 32*a0*a4*a6**3/243 - 34*a0*a4*a6**2/729 - 2*a0*a4*a6/729 - 16*a0*a5**3*a6**2/729 + 62*a0*a5**3*a6/2187 - 4*a0*a5**3/2187 - 58*a0*a5**2*a6**2/729 - a0*a5**2*a6/81 + 8*a0*a5*a6**4/9 - 52*a0*a5*a6**3/81 + 5*a0*a5*a6**2/81 + 5*a0*a5*a6/486 + 11*a0*a6**4/9 - 28*a0*a6**3/27 + 11*a0*a6**2/36 - a0*a6/36 - a1**4*a3*a5 + 2*a1**4*a4**2/3 - a1**3*a2*a3*a5 - 12*a1**3*a2*a3*a6 + 3*a1**3*a2*a3 + 2*a1**3*a2*a4**2/9 + 2*a1**3*a2*a4*a5 - 4*a1**3*a3**2/81 - 8*a1**3*a3*a4*a5/81 - 4*a1**3*a3*a4/81 - 8*a1**3*a3*a5**2/81 - 4*a1**3*a3*a5*a6/9 + 2*a1**3*a3*a6/3 - a1**3*a3/3 + 16*a1**3*a4**3/729 + 8*a1**3*a4**2*a6/27 - 4*a1**3*a4**2/81 - 8*a1**3*a4*a5**2/81 - a1**3*a4*a5/9 - 4*a1**3*a4*a6**2 + 7*a1**3*a4*a6/3 - a1**3*a4/2 - a1**3*a5**3/9 + a1**3*a5**2*a6/3 - a1**3*a5**2/3 + 5*a1**2*a2**3*a3 - 8*a1**2*a2**2*a3**2/81 - 8*a1**2*a2**2*a3*a4/81 + 26*a1**2*a2**2*a3*a5/27 - 8*a1**2*a2**2*a3*a6/3 - a1**2*a2**2*a3/6 - 4*a1**2*a2**2*a4**2/9 + 8*a1**2*a2**2*a4*a6/3 - a1**2*a2**2*a4 + 11*a1**2*a2**2*a5**2/6 - 112*a1**2*a2*a3*a4*a6/243 + 16*a1**2*a2*a3*a4/243 - 16*a1**2*a2*a3*a5**2/81 - 52*a1**2*a2*a3*a5*a6/27 + 14*a1**2*a2*a3*a5/27 - 16*a1**2*a2*a3*a6**2/3 + 4*a1**2*a2*a3*a6/3 + a1**2*a2*a3/9 + 56*a1**2*a2*a4**2*a5/729 + 56*a1**2*a2*a4**2*a6/243 - 32*a1**2*a2*a4**2/243 + 4*a1**2*a2*a4*a5**2/243 + 16*a1**2*a2*a4*a5*a6/81 + 4*a1**2*a2*a4*a5/81 - 4*a1**2*a2*a4*a6**2/9 - a1**2*a2*a4*a6/3 - 8*a1**2*a2*a5**3/81 - 7*a1**2*a2*a5**2*a6/9 + a1**2*a2*a5**2/18 - a1**2*a2*a5*a6**2/3 - 5*a1**2*a2*a5*a6/6 + a1**2*a2*a5/12 + 16*a1**2*a3*a5*a6**2/81 - 88*a1**2*a3*a5*a6/243 + 8*a1**2*a3*a5/243 + 4*a1**2*a3*a6**2/9 - 2*a1**2*a3*a6/9 + 2*a1**2*a3/81 - 32*a1**2*a4**2*a6**2/243 + 32*a1**2*a4**2*a6/243 - 4*a1**2*a4**2/243 + 8*a1**2*a4*a5**2*a6/243 - 8*a1**2*a4*a5**2/729 - 28*a1**2*a4*a5*a6/243 - 16*a1**2*a4*a6**3/9 + 4*a1**2*a4*a6**2/3 - 8*a1**2*a4*a6/27 + 2*a1**2*a4/81 - 4*a1**2*a5**4/729 - 4*a1**2*a5**3*a6/243 - 2*a1**2*a5**3/243 + 4*a1**2*a5**2*a6**2/9 - 10*a1**2*a5**2*a6/27 + a1**2*a5**2/27 - a1**2*a5*a6**2 + 11*a1**2*a5*a6/18 - a1**2*a5/18 + 6*a1**2*a6**4 - 7*a1**2*a6**3 + 11*a1**2*a6**2/6 - 5*a1**2*a6/12 + a1**2/12 + 4*a1*a2**4*a3/3 + 32*a1*a2**3*a3*a4/243 + 32*a1*a2**3*a3*a5/81 + 76*a1*a2**3*a3*a6/9 - 31*a1*a2**3*a3/27 - 16*a1*a2**3*a4*a5/27 + 2*a1*a2**3*a4*a6/3 - 5*a1*a2**3*a4/18 + a1*a2**3*a5**2/9 + 16*a1*a2**3*a5*a6/3 - 7*a1*a2**3*a5/6 - 80*a1*a2**2*a3*a5*a6/81 + 58*a1*a2**2*a3*a5/243 - 40*a1*a2**2*a3*a6**2/9 + 70*a1*a2**2*a3*a6/27 - 35*a1*a2**2*a3/81 + 16*a1*a2**2*a4**2*a6/243 - 20*a1*a2**2*a4**2/729 + 16*a1*a2**2*a4*a5**2/243 + 8*a1*a2**2*a4*a5*a6/81 - 44*a1*a2**2*a4*a5/243 + 8*a1*a2**2*a4*a6**2/3 - 34*a1*a2**2*a4*a6/27 + 19*a1*a2**2*a4/81 + 16*a1*a2**2*a5**3/243 - 16*a1*a2**2*a5**2*a6/27 + a1*a2**2*a5**2/3 - 13*a1*a2**2*a5*a6**2/9 + 7*a1*a2**2*a5*a6/18 - a1*a2**2*a5/6 - 4*a1*a2**2*a6**3 + 4*a1*a2**2*a6**2 - a1*a2**2*a6/12 + a1*a2**2/6 + 16*a1*a2*a3*a6**3/81 - 368*a1*a2*a3*a6**2/243 + 94*a1*a2*a3*a6/243 - a1*a2*a3/243 - 56*a1*a2*a4*a5*a6**2/729 + 100*a1*a2*a4*a5*a6/729 - 10*a1*a2*a4*a5/729 - 80*a1*a2*a4*a6**3/81 + 160*a1*a2*a4*a6**2/243 - 32*a1*a2*a4*a6/81 + 16*a1*a2*a4/243 + 8*a1*a2*a5**3*a6/729 - 2*a1*a2*a5**3/729 + 64*a1*a2*a5**2*a6**2/243 - 94*a1*a2*a5**2*a6/243 + 13*a1*a2*a5**2/243 + 52*a1*a2*a5*a6**3/27 - 46*a1*a2*a5*a6**2/27 + 13*a1*a2*a5*a6/81 + 2*a1*a2*a5/81 - 2*a1*a2*a6**4/3 - 17*a1*a2*a6**3/9 + 2*a1*a2*a6**2 - 5*a1*a2*a6/18 - a1*a2/36 + 16*a1*a4*a6**4/81 - 136*a1*a4*a6**3/243 + 152*a1*a4*a6**2/729 - 8*a1*a4*a6/243 + 2*a1*a4/729 - 16*a1*a5**2*a6**3/243 + 116*a1*a5**2*a6**2/729 - 8*a1*a5**2*a6/243 + 2*a1*a5**2/729 - 20*a1*a5*a6**3/81 + 2*a1*a5*a6**2/243 + 2*a1*a5*a6/243 + 8*a1*a6**5/3 - 32*a1*a6**4/9 + 28*a1*a6**3/27 - a1*a6**2/27 - a1*a6/81 - 8*a2**5*a3/3 - 3*a2**5*a5/2 + 28*a2**4*a3*a5/81 + 16*a2**4*a3*a6/9 - 8*a2**4*a3/9 + 4*a2**4*a4*a5/27 - 4*a2**4*a4*a6/3 + 5*a2**4*a4/9 - 4*a2**4*a5**2/27 + 7*a2**4*a5*a6/9 - 2*a2**4*a5/9 + a2**4*a6**2 - a2**4*a6 - a2**4/8 - 8*a2**3*a3*a6**2/81 + 56*a2**3*a3*a6/81 + a2**3*a3/81 + 80*a2**3*a4*a5*a6/729 - 22*a2**3*a4*a5/729 + 64*a2**3*a4*a6**2/81 - 58*a2**3*a4*a6/81 + 16*a2**3*a4/81 + 20*a2**3*a5**3/729 + 68*a2**3*a5**2*a6/243 - 34*a2**3*a5**2/243 - 2*a2**3*a5*a6**2 + 137*a2**3*a5*a6/81 - 5*a2**3*a5/162 + 2*a2**3*a6**3/3 + 2*a2**3*a6**2/9 - 19*a2**3*a6/36 - a2**3/12 - 16*a2**2*a4*a6**3/243 + 280*a2**2*a4*a6**2/729 - 44*a2**2*a4*a6/729 + 2*a2**2*a4/243 + 4*a2**2*a5**2*a6**2/27 - 14*a2**2*a5**2*a6/729 + 2*a2**2*a5**2/729 + 92*a2**2*a5*a6**3/81 - 404*a2**2*a5*a6**2/243 + 137*a2**2*a5*a6/243 - 8*a2**2*a5/243 - 20*a2**2*a6**4/9 + 82*a2**2*a6**3/27 - 65*a2**2*a6**2/81 + 11*a2**2*a6/162 + 8*a2*a5*a6**4/81 + 32*a2*a5*a6**3/81 - 134*a2*a5*a6**2/729 + 2*a2*a5*a6/81 - a2*a5/729 + 8*a2*a6**5/9 - 56*a2*a6**4/27 + 106*a2*a6**3/81 - 82*a2*a6**2/243 + 8*a2*a6/243 + 40*a6**5/81 - 4*a6**4/9 + 110*a6**3/729 - 17*a6**2/729 + a6/729"
    &#93;,
    &#91;
      "-a0**2*a2*a3**2*a4/18 - a0**2*a2*a3*a4**2/18 + a0**2*a3*a4**2*a6/54 + a0**2*a3*a4**2/324 - 7*a0**2*a3*a4*a5**2/162 - 5*a0**2*a3*a4*a5*a6/18 + a0**2*a3*a4*a5/108 + 5*a0**2*a4**3*a5/486 + a0**2*a4**3*a6/9 - a0**2*a4**2*a5**2/81 + a0*a1**2*a3**2*a4/18 + a0*a1**2*a3*a4**2/18 - 7*a0*a1*a2*a3*a4**2/54 + 7*a0*a1*a2*a3*a4*a5/9 - 7*a0*a1*a2*a4**3/18 + 2*a0*a1*a3**2*a6**2/3 - 7*a0*a1*a3**2*a6/18 + 5*a0*a1*a3**2/108 - 29*a0*a1*a3*a4*a5*a6/54 + 31*a0*a1*a3*a4*a5/108 + 2*a0*a1*a3*a4*a6**2/3 - 5*a0*a1*a3*a4*a6/9 + 11*a0*a1*a3*a4/108 - 2*a0*a1*a3*a5**3/27 - 7*a0*a1*a3*a5**2*a6/9 + 7*a0*a1*a3*a5**2/54 + 5*a0*a1*a4**3*a6/81 - 11*a0*a1*a4**3/243 + a0*a1*a4**2*a5**2/27 - 5*a0*a1*a4**2*a5*a6/54 + 41*a0*a1*a4**2*a5/324 + a0*a1*a4*a5**3/27 - a0*a2**2*a3**2*a6/6 + 7*a0*a2**2*a3**2/36 - a0*a2**2*a3*a4*a5/3 + 5*a0*a2**2*a3*a4*a6/6 - 5*a0*a2**2*a3*a4/36 + 8*a0*a2**2*a3*a5**2/9 + a0*a2**2*a4**3/81 - 19*a0*a2**2*a4**2*a5/27 - 10*a0*a2*a3*a4*a6**2/9 + 55*a0*a2*a3*a4*a6/54 - 55*a0*a2*a3*a4/324 - 16*a0*a2*a3*a5**2*a6/27 + 2*a0*a2*a3*a5**2/81 + 11*a0*a2*a3*a5*a6**2/6 - 13*a0*a2*a3*a5*a6/6 + 115*a0*a2*a3*a5/216 + 5*a0*a2*a4**2*a5*a6/162 + 7*a0*a2*a4**2*a5/486 - 13*a0*a2*a4**2*a6**2/18 + 95*a0*a2*a4**2*a6/108 - 7*a0*a2*a4**2/36 + a0*a2*a4*a5**3/27 - 17*a0*a2*a4*a5**2*a6/18 + 91*a0*a2*a4*a5**2/324 + 4*a0*a2*a5**4/27 - a0*a3*a5*a6**3 + 11*a0*a3*a5*a6**2/27 - 17*a0*a3*a5*a6/648 + a0*a3*a5/432 + 3*a0*a3*a6**4/2 - 5*a0*a3*a6**3 + 7*a0*a3*a6**2/2 - 133*a0*a3*a6/144 + 37*a0*a3/432 - 7*a0*a4**2*a6**3/27 + 49*a0*a4**2*a6**2/162 - 73*a0*a4**2*a6/972 + 5*a0*a4**2/972 + 4*a0*a4*a5**2*a6**2/27 - 13*a0*a4*a5**2*a6/972 - 23*a0*a4*a5**2/1944 - 29*a0*a4*a5*a6**3/18 + 113*a0*a4*a5*a6**2/54 - 65*a0*a4*a5*a6/81 + 17*a0*a4*a5/162 - a0*a5**4*a6/162 - 13*a0*a5**4/972 + 5*a0*a5**3*a6**2/18 - 22*a0*a5**3*a6/81 + 41*a0*a5**3/648 + a1**3*a3*a4**2/9 - a1**3*a3*a4*a5/3 + 2*a1**3*a4**3/9 - a1**2*a2*a3**2*a6 + a1**2*a2*a3**2/6 + a1**2*a2*a3*a4*a5/2 - 3*a1**2*a2*a3*a4*a6/2 + 5*a1**2*a2*a3*a4/12 + a1**2*a2*a3*a5**2/9 - a1**2*a2*a4**3/81 + 13*a1**2*a2*a4**2*a5/27 - 5*a1**2*a3*a4*a6**2/9 + 14*a1**2*a3*a4*a6/27 - 7*a1**2*a3*a4/54 - 7*a1**2*a3*a5**2*a6/18 + 55*a1**2*a3*a5**2/108 - 3*a1**2*a3*a5*a6**2 + 17*a1**2*a3*a5*a6/6 - 5*a1**2*a3*a5/9 + 4*a1**2*a4**2*a5*a6/27 - a1**2*a4**2*a5/6 - 2*a1**2*a4**2*a6**2/9 - 7*a1**2*a4**2*a6/27 + a1**2*a4**2/12 + a1**2*a4*a5**3/54 + 4*a1**2*a4*a5**2*a6/9 - a1**2*a4*a5**2/54 + a1*a2**3*a3**2/2 + a1*a2**3*a3*a4/2 + 8*a1*a2**2*a3*a4*a6/9 - 5*a1*a2**2*a3*a4/9 + 14*a1*a2**2*a3*a5**2/27 + 13*a1*a2**2*a3*a5*a6/6 - 5*a1*a2**2*a3*a5/12 + a1*a2**2*a4**2*a5/162 + a1*a2**2*a4**2*a6/2 - a1*a2**2*a4**2/4 + 23*a1*a2**2*a4*a5**2/54 - 23*a1*a2*a3*a5*a6**2/18 + 121*a1*a2*a3*a5*a6/36 - 61*a1*a2*a3*a5/72 - 9*a1*a2*a3*a6**3/2 + 11*a1*a2*a3*a6**2 - 29*a1*a2*a3*a6/6 + 29*a1*a2*a3/48 + 7*a1*a2*a4**2*a6**2/27 - 20*a1*a2*a4**2*a6/81 + a1*a2*a4**2/36 + 11*a1*a2*a4*a5**2*a6/81 - 85*a1*a2*a4*a5**2/324 + a1*a2*a4*a5*a6**2/3 - 29*a1*a2*a4*a5*a6/108 + a1*a2*a4*a5/24 + 7*a1*a2*a5**4/162 + 37*a1*a2*a5**3*a6/54 - 19*a1*a2*a5**3/108 - 4*a1*a3*a6**4/3 + 17*a1*a3*a6**3/6 - 56*a1*a3*a6**2/27 + 73*a1*a3*a6/108 - 35*a1*a3/432 - 4*a1*a4*a5*a6**3/27 + 77*a1*a4*a5*a6**2/162 - 17*a1*a4*a5*a6/162 + a1*a4*a5/648 - 10*a1*a4*a6**4/3 + 20*a1*a4*a6**3/3 - 211*a1*a4*a6**2/54 + a1*a4*a6 - 7*a1*a4/72 + 4*a1*a5**3*a6**2/27 - 19*a1*a5**3*a6/81 + 5*a1*a5**3/216 + 14*a1*a5**2*a6**3/9 - 53*a1*a5**2*a6**2/27 + 53*a1*a5**2*a6/72 - 35*a1*a5**2/432 + a2**4*a3*a4/18 - 4*a2**4*a3*a5/3 + a2**4*a4**2/2 + 20*a2**3*a3*a5*a6/9 - 7*a2**3*a3*a5/3 - 7*a2**3*a3*a6/2 + 5*a2**3*a3/6 - 5*a2**3*a4**2*a6/27 + 7*a2**3*a4**2/54 + 5*a2**3*a4*a5**2/54 + 5*a2**3*a4*a5*a6/2 - 41*a2**3*a4*a5/36 + 10*a2**2*a3*a6**3/3 - 40*a2**2*a3*a6**2/9 + 127*a2**2*a3*a6/72 - 5*a2**2*a3/18 + 7*a2**2*a4*a5*a6**2/18 - 71*a2**2*a4*a5*a6/108 + a2**2*a4*a5/36 + 29*a2**2*a4*a6**3/6 - 125*a2**2*a4*a6**2/18 + 29*a2**2*a4*a6/12 - 7*a2**2*a4/24 + 2*a2**2*a5**3*a6/9 - 5*a2**2*a5**3/27 + 8*a2**2*a5**2*a6**2/3 - 11*a2**2*a5**2*a6/6 + a2**2*a5**2/4 + 4*a2*a4*a6**4/9 - 35*a2*a4*a6**3/54 + 29*a2*a4*a6**2/108 - 5*a2*a4*a6/108 + 7*a2*a5**2*a6**3/9 - 17*a2*a5**2*a6**2/12 + 4*a2*a5**2*a6/9 - a2*a5**2/36 + 25*a2*a5*a6**4/3 - 445*a2*a5*a6**3/36 + 413*a2*a5*a6**2/72 - 73*a2*a5*a6/72 + 7*a2*a5/144 + 2*a5*a6**5/3 - 5*a5*a6**4/3 + 59*a5*a6**3/54 - 31*a5*a6**2/108 + a5*a6/36 + 6*a6**6 - 13*a6**5 + 121*a6**4/12 - 67*a6**3/18 + 97*a6**2/144 - 7*a6/144",
      "-a0**2*a2*a3**2*a4/4 + a0**2*a3*a4**2*a6/12 + a0**2*a3*a4**2/72 - 7*a0**2*a3*a4*a5**2/36 + 5*a0**2*a4**3*a5/108 + a0*a1**2*a3**2*a4/4 - 7*a0*a1*a2*a3*a4**2/12 + 3*a0*a1*a3**2*a6**2 - 7*a0*a1*a3**2*a6/4 + 5*a0*a1*a3**2/24 - 29*a0*a1*a3*a4*a5*a6/12 + 31*a0*a1*a3*a4*a5/24 - a0*a1*a3*a5**3/3 + 5*a0*a1*a4**3*a6/18 - 11*a0*a1*a4**3/54 + a0*a1*a4**2*a5**2/6 - 3*a0*a2**2*a3**2*a6/4 + 7*a0*a2**2*a3**2/8 - 3*a0*a2**2*a3*a4*a5/2 + a0*a2**2*a4**3/18 - 5*a0*a2*a3*a4*a6**2 + 55*a0*a2*a3*a4*a6/12 - 55*a0*a2*a3*a4/72 - 8*a0*a2*a3*a5**2*a6/3 + a0*a2*a3*a5**2/9 + 5*a0*a2*a4**2*a5*a6/36 + 7*a0*a2*a4**2*a5/108 + a0*a2*a4*a5**3/6 - 9*a0*a3*a5*a6**3/2 + 11*a0*a3*a5*a6**2/6 - 17*a0*a3*a5*a6/144 + a0*a3*a5/96 - 7*a0*a4**2*a6**3/6 + 49*a0*a4**2*a6**2/36 - 73*a0*a4**2*a6/216 + 5*a0*a4**2/216 + 2*a0*a4*a5**2*a6**2/3 - 13*a0*a4*a5**2*a6/216 - 23*a0*a4*a5**2/432 - a0*a5**4*a6/36 - 13*a0*a5**4/216 + a1**3*a3*a4**2/2 - 9*a1**2*a2*a3**2*a6/2 + 3*a1**2*a2*a3**2/4 + 9*a1**2*a2*a3*a4*a5/4 - a1**2*a2*a4**3/18 - 5*a1**2*a3*a4*a6**2/2 + 7*a1**2*a3*a4*a6/3 - 7*a1**2*a3*a4/12 - 7*a1**2*a3*a5**2*a6/4 + 55*a1**2*a3*a5**2/24 + 2*a1**2*a4**2*a5*a6/3 - 3*a1**2*a4**2*a5/4 + a1**2*a4*a5**3/12 + 9*a1*a2**3*a3**2/4 + 4*a1*a2**2*a3*a4*a6 - 5*a1*a2**2*a3*a4/2 + 7*a1*a2**2*a3*a5**2/3 + a1*a2**2*a4**2*a5/36 - 23*a1*a2*a3*a5*a6**2/4 + 121*a1*a2*a3*a5*a6/8 - 61*a1*a2*a3*a5/16 + 7*a1*a2*a4**2*a6**2/6 - 10*a1*a2*a4**2*a6/9 + a1*a2*a4**2/8 + 11*a1*a2*a4*a5**2*a6/18 - 85*a1*a2*a4*a5**2/72 + 7*a1*a2*a5**4/36 - 6*a1*a3*a6**4 + 51*a1*a3*a6**3/4 - 28*a1*a3*a6**2/3 + 73*a1*a3*a6/24 - 35*a1*a3/96 - 2*a1*a4*a5*a6**3/3 + 77*a1*a4*a5*a6**2/36 - 17*a1*a4*a5*a6/36 + a1*a4*a5/144 + 2*a1*a5**3*a6**2/3 - 19*a1*a5**3*a6/18 + 5*a1*a5**3/48 + a2**4*a3*a4/4 + 10*a2**3*a3*a5*a6 - 21*a2**3*a3*a5/2 - 5*a2**3*a4**2*a6/6 + 7*a2**3*a4**2/12 + 5*a2**3*a4*a5**2/12 + 15*a2**2*a3*a6**3 - 20*a2**2*a3*a6**2 + 127*a2**2*a3*a6/16 - 5*a2**2*a3/4 + 7*a2**2*a4*a5*a6**2/4 - 71*a2**2*a4*a5*a6/24 + a2**2*a4*a5/8 + a2**2*a5**3*a6 - 5*a2**2*a5**3/6 + 2*a2*a4*a6**4 - 35*a2*a4*a6**3/12 + 29*a2*a4*a6**2/24 - 5*a2*a4*a6/24 + 7*a2*a5**2*a6**3/2 - 51*a2*a5**2*a6**2/8 + 2*a2*a5**2*a6 - a2*a5**2/8 + 3*a5*a6**5 - 15*a5*a6**4/2 + 59*a5*a6**3/12 - 31*a5*a6**2/24 + a5*a6/8",
      "a0**2*a2*a3**2*a4/27 + a0**2*a2*a3*a4**2/27 + 2*a0**2*a2*a3*a4*a5/9 - a0**2*a2*a4**3/18 - a0**2*a3*a4**2*a6/81 - a0**2*a3*a4**2/486 + 7*a0**2*a3*a4*a5**2/243 + 5*a0**2*a3*a4*a5*a6/27 - a0**2*a3*a4*a5/162 + 4*a0**2*a3*a4*a6**2/3 - 5*a0**2*a3*a4*a6/9 + 7*a0**2*a3*a4/108 - 5*a0**2*a4**3*a5/729 - 2*a0**2*a4**3*a6/27 + 2*a0**2*a4**2*a5**2/243 - 17*a0**2*a4**2*a5*a6/54 + 19*a0**2*a4**2*a5/324 + 5*a0**2*a4*a5**3/81 - a0*a1**2*a3**2*a4/27 - a0*a1**2*a3*a4**2/27 - a0*a1**2*a3*a4*a5/18 + 7*a0*a1*a2*a3*a4**2/81 - 14*a0*a1*a2*a3*a4*a5/27 - 7*a0*a1*a2*a3*a4*a6/3 + 4*a0*a1*a2*a3*a4/9 + a0*a1*a2*a3*a5**2/3 + 7*a0*a1*a2*a4**3/27 + 5*a0*a1*a2*a4**2*a5/18 - 4*a0*a1*a3**2*a6**2/9 + 7*a0*a1*a3**2*a6/27 - 5*a0*a1*a3**2/162 + 29*a0*a1*a3*a4*a5*a6/81 - 31*a0*a1*a3*a4*a5/162 - 4*a0*a1*a3*a4*a6**2/9 + 10*a0*a1*a3*a4*a6/27 - 11*a0*a1*a3*a4/162 + 4*a0*a1*a3*a5**3/81 + 14*a0*a1*a3*a5**2*a6/27 - 7*a0*a1*a3*a5**2/81 + 8*a0*a1*a3*a5*a6**2/3 - 23*a0*a1*a3*a5*a6/18 + 7*a0*a1*a3*a5/36 - 10*a0*a1*a4**3*a6/243 + 22*a0*a1*a4**3/729 - 2*a0*a1*a4**2*a5**2/81 + 5*a0*a1*a4**2*a5*a6/81 - 41*a0*a1*a4**2*a5/486 - 5*a0*a1*a4**2*a6**2/9 + 10*a0*a1*a4**2*a6/27 - 17*a0*a1*a4**2/324 - 2*a0*a1*a4*a5**3/81 - 5*a0*a1*a4*a5**2*a6/18 - 13*a0*a1*a4*a5**2/324 + a0*a1*a5**4/9 + a0*a2**3*a3*a4 + a0*a2**2*a3**2*a6/9 - 7*a0*a2**2*a3**2/54 + 2*a0*a2**2*a3*a4*a5/9 - 5*a0*a2**2*a3*a4*a6/9 + 5*a0*a2**2*a3*a4/54 - 16*a0*a2**2*a3*a5**2/27 - a0*a2**2*a3*a5*a6 - 8*a0*a2**2*a3*a5/9 - 2*a0*a2**2*a4**3/243 + 38*a0*a2**2*a4**2*a5/81 + 7*a0*a2**2*a4**2*a6/18 + 4*a0*a2**2*a4**2/27 + 17*a0*a2**2*a4*a5**2/27 + 20*a0*a2*a3*a4*a6**2/27 - 55*a0*a2*a3*a4*a6/81 + 55*a0*a2*a3*a4/486 + 32*a0*a2*a3*a5**2*a6/81 - 4*a0*a2*a3*a5**2/243 - 11*a0*a2*a3*a5*a6**2/9 + 13*a0*a2*a3*a5*a6/9 - 115*a0*a2*a3*a5/324 + a0*a2*a3*a6**3/2 - 41*a0*a2*a3*a6**2/12 + 125*a0*a2*a3*a6/72 - 53*a0*a2*a3/216 - 5*a0*a2*a4**2*a5*a6/243 - 7*a0*a2*a4**2*a5/729 + 13*a0*a2*a4**2*a6**2/27 - 95*a0*a2*a4**2*a6/162 + 7*a0*a2*a4**2/54 - 2*a0*a2*a4*a5**3/81 + 17*a0*a2*a4*a5**2*a6/27 - 91*a0*a2*a4*a5**2/486 + 16*a0*a2*a4*a5*a6**2/9 - 23*a0*a2*a4*a5*a6/36 + 19*a0*a2*a4*a5/648 - 8*a0*a2*a5**4/81 + 7*a0*a2*a5**3*a6/27 - 14*a0*a2*a5**3/81 + 2*a0*a3*a5*a6**3/3 - 22*a0*a3*a5*a6**2/81 + 17*a0*a3*a5*a6/972 - a0*a3*a5/648 - a0*a3*a6**4 + 10*a0*a3*a6**3/3 - 7*a0*a3*a6**2/3 + 133*a0*a3*a6/216 - 37*a0*a3/648 + 14*a0*a4**2*a6**3/81 - 49*a0*a4**2*a6**2/243 + 73*a0*a4**2*a6/1458 - 5*a0*a4**2/1458 - 8*a0*a4*a5**2*a6**2/81 + 13*a0*a4*a5**2*a6/1458 + 23*a0*a4*a5**2/2916 + 29*a0*a4*a5*a6**3/27 - 113*a0*a4*a5*a6**2/81 + 130*a0*a4*a5*a6/243 - 17*a0*a4*a5/243 + 7*a0*a4*a6**4/3 - 17*a0*a4*a6**3/6 + 11*a0*a4*a6**2/9 - 149*a0*a4*a6/648 + 5*a0*a4/324 + a0*a5**4*a6/243 + 13*a0*a5**4/1458 - 5*a0*a5**3*a6**2/27 + 44*a0*a5**3*a6/243 - 41*a0*a5**3/972 + a0*a5**2*a6**3/6 - 13*a0*a5**2*a6**2/108 + a0*a5**2*a6/54 - a0*a5**2/144 - 2*a1**3*a3*a4**2/27 + 2*a1**3*a3*a4*a5/9 + a1**3*a3*a4*a6 - a1**3*a3*a4/6 - 4*a1**3*a4**3/27 - 2*a1**3*a4**2*a5/9 - a1**2*a2**2*a3*a4/2 + 2*a1**2*a2*a3**2*a6/3 - a1**2*a2*a3**2/9 - a1**2*a2*a3*a4*a5/3 + a1**2*a2*a3*a4*a6 - 5*a1**2*a2*a3*a4/18 - 2*a1**2*a2*a3*a5**2/27 - 4*a1**2*a2*a3*a5*a6/3 + 13*a1**2*a2*a3*a5/9 + 2*a1**2*a2*a4**3/243 - 26*a1**2*a2*a4**2*a5/81 + a1**2*a2*a4**2*a6/9 - 17*a1**2*a2*a4**2/54 - 19*a1**2*a2*a4*a5**2/54 + 10*a1**2*a3*a4*a6**2/27 - 28*a1**2*a3*a4*a6/81 + 7*a1**2*a3*a4/81 + 7*a1**2*a3*a5**2*a6/27 - 55*a1**2*a3*a5**2/162 + 2*a1**2*a3*a5*a6**2 - 17*a1**2*a3*a5*a6/9 + 10*a1**2*a3*a5/27 + 3*a1**2*a3*a6**3 - 3*a1**2*a3*a6**2 + a1**2*a3*a6 - 7*a1**2*a3/72 - 8*a1**2*a4**2*a5*a6/81 + a1**2*a4**2*a5/9 + 4*a1**2*a4**2*a6**2/27 + 14*a1**2*a4**2*a6/81 - a1**2*a4**2/18 - a1**2*a4*a5**3/81 - 8*a1**2*a4*a5**2*a6/27 + a1**2*a4*a5**2/81 - 10*a1**2*a4*a5*a6**2/9 + 41*a1**2*a4*a5*a6/54 - a1**2*a4*a5/12 + a1**2*a5**3*a6/6 - 7*a1**2*a5**3/36 - a1*a2**3*a3**2/3 - a1*a2**3*a3*a4/3 + a1*a2**3*a4**2/6 - 16*a1*a2**2*a3*a4*a6/27 + 10*a1*a2**2*a3*a4/27 - 28*a1*a2**2*a3*a5**2/81 - 13*a1*a2**2*a3*a5*a6/9 + 5*a1*a2**2*a3*a5/18 - 19*a1*a2**2*a3*a6**2/2 + 131*a1*a2**2*a3*a6/12 - 55*a1*a2**2*a3/24 - a1*a2**2*a4**2*a5/243 - a1*a2**2*a4**2*a6/3 + a1*a2**2*a4**2/6 - 23*a1*a2**2*a4*a5**2/81 + a1*a2**2*a4*a5*a6/9 - 55*a1*a2**2*a4*a5/108 - 2*a1*a2**2*a5**3/27 + 23*a1*a2*a3*a5*a6**2/27 - 121*a1*a2*a3*a5*a6/54 + 61*a1*a2*a3*a5/108 + 3*a1*a2*a3*a6**3 - 22*a1*a2*a3*a6**2/3 + 29*a1*a2*a3*a6/9 - 29*a1*a2*a3/72 - 14*a1*a2*a4**2*a6**2/81 + 40*a1*a2*a4**2*a6/243 - a1*a2*a4**2/54 - 22*a1*a2*a4*a5**2*a6/243 + 85*a1*a2*a4*a5**2/486 - 2*a1*a2*a4*a5*a6**2/9 + 29*a1*a2*a4*a5*a6/162 - a1*a2*a4*a5/36 - 13*a1*a2*a4*a6**3/3 + 17*a1*a2*a4*a6**2/3 - 203*a1*a2*a4*a6/108 + 7*a1*a2*a4/36 - 7*a1*a2*a5**4/243 - 37*a1*a2*a5**3*a6/81 + 19*a1*a2*a5**3/162 + 11*a1*a2*a5**2*a6**2/9 - 58*a1*a2*a5**2*a6/27 + 97*a1*a2*a5**2/216 + 8*a1*a3*a6**4/9 - 17*a1*a3*a6**3/9 + 112*a1*a3*a6**2/81 - 73*a1*a3*a6/162 + 35*a1*a3/648 + 8*a1*a4*a5*a6**3/81 - 77*a1*a4*a5*a6**2/243 + 17*a1*a4*a5*a6/243 - a1*a4*a5/972 + 20*a1*a4*a6**4/9 - 40*a1*a4*a6**3/9 + 211*a1*a4*a6**2/81 - 2*a1*a4*a6/3 + 7*a1*a4/108 - 8*a1*a5**3*a6**2/81 + 38*a1*a5**3*a6/243 - 5*a1*a5**3/324 - 28*a1*a5**2*a6**3/27 + 106*a1*a5**2*a6**2/81 - 53*a1*a5**2*a6/108 + 35*a1*a5**2/648 + 2*a1*a5*a6**4/3 - 31*a1*a5*a6**3/18 + 35*a1*a5*a6**2/36 - 31*a1*a5*a6/108 + 7*a1*a5/216 - a2**4*a3*a4/27 + 8*a2**4*a3*a5/9 + 4*a2**4*a3*a6 - 23*a2**4*a3/6 - a2**4*a4**2/3 + a2**4*a4*a5/3 - 40*a2**3*a3*a5*a6/27 + 14*a2**3*a3*a5/9 + 7*a2**3*a3*a6/3 - 5*a2**3*a3/9 + 10*a2**3*a4**2*a6/81 - 7*a2**3*a4**2/81 - 5*a2**3*a4*a5**2/81 - 5*a2**3*a4*a5*a6/3 + 41*a2**3*a4*a5/54 + 19*a2**3*a4*a6**2/6 - 137*a2**3*a4*a6/36 + 5*a2**3*a4/9 - 2*a2**3*a5**2*a6/9 + 7*a2**3*a5**2/18 - 20*a2**2*a3*a6**3/9 + 80*a2**2*a3*a6**2/27 - 127*a2**2*a3*a6/108 + 5*a2**2*a3/27 - 7*a2**2*a4*a5*a6**2/27 + 71*a2**2*a4*a5*a6/162 - a2**2*a4*a5/54 - 29*a2**2*a4*a6**3/9 + 125*a2**2*a4*a6**2/27 - 29*a2**2*a4*a6/18 + 7*a2**2*a4/36 - 4*a2**2*a5**3*a6/27 + 10*a2**2*a5**3/81 - 16*a2**2*a5**2*a6**2/9 + 11*a2**2*a5**2*a6/9 - a2**2*a5**2/6 + 5*a2**2*a5*a6**3/3 - 113*a2**2*a5*a6**2/36 + 77*a2**2*a5*a6/72 - 8*a2*a4*a6**4/27 + 35*a2*a4*a6**3/81 - 29*a2*a4*a6**2/162 + 5*a2*a4*a6/162 - 14*a2*a5**2*a6**3/27 + 17*a2*a5**2*a6**2/18 - 8*a2*a5**2*a6/27 + a2*a5**2/54 - 50*a2*a5*a6**4/9 + 445*a2*a5*a6**3/54 - 413*a2*a5*a6**2/108 + 73*a2*a5*a6/108 - 7*a2*a5/216 + 2*a2*a6**5 - 16*a2*a6**4/3 + 137*a2*a6**3/36 - 77*a2*a6**2/72 + a2*a6/9 - 4*a5*a6**5/9 + 10*a5*a6**4/9 - 59*a5*a6**3/81 + 31*a5*a6**2/162 - a5*a6/54 - 4*a6**6 + 26*a6**5/3 - 121*a6**4/18 + 67*a6**3/27 - 97*a6**2/216 + 7*a6/216",
      "a0**2*a1*a3*a4*a5/6 - a0**2*a1*a4**3/18 - 2*a0**2*a2*a3**2*a4/81 - 2*a0**2*a2*a3*a4**2/81 - 4*a0**2*a2*a3*a4*a5/27 + 7*a0**2*a2*a3*a4*a6/6 - 5*a0**2*a2*a3*a4/18 + a0**2*a2*a4**3/27 - 4*a0**2*a2*a4**2*a5/27 + 2*a0**2*a3*a4**2*a6/243 + a0**2*a3*a4**2/729 - 14*a0**2*a3*a4*a5**2/729 - 10*a0**2*a3*a4*a5*a6/81 + a0**2*a3*a4*a5/243 - 8*a0**2*a3*a4*a6**2/9 + 10*a0**2*a3*a4*a6/27 - 7*a0**2*a3*a4/162 + 10*a0**2*a4**3*a5/2187 + 4*a0**2*a4**3*a6/81 - 4*a0**2*a4**2*a5**2/729 + 17*a0**2*a4**2*a5*a6/81 - 19*a0**2*a4**2*a5/486 + a0**2*a4**2*a6**2/2 - a0**2*a4**2*a6/4 + a0**2*a4**2/36 - 10*a0**2*a4*a5**3/243 - 5*a0**2*a4*a5**2*a6/27 + a0**2*a4*a5**2/18 + 2*a0*a1**2*a3**2*a4/81 + 2*a0*a1**2*a3*a4**2/81 + a0*a1**2*a3*a4*a5/27 + a0*a1**2*a3*a4*a6/6 + a0*a1**2*a3*a5**2/3 - a0*a1**2*a4**2*a5/9 - 4*a0*a1*a2**2*a3*a4/3 - 14*a0*a1*a2*a3*a4**2/243 + 28*a0*a1*a2*a3*a4*a5/81 + 14*a0*a1*a2*a3*a4*a6/9 - 8*a0*a1*a2*a3*a4/27 - 2*a0*a1*a2*a3*a5**2/9 + 29*a0*a1*a2*a3*a5*a6/6 - 71*a0*a1*a2*a3*a5/36 - 14*a0*a1*a2*a4**3/81 - 5*a0*a1*a2*a4**2*a5/27 - 11*a0*a1*a2*a4**2*a6/9 + 37*a0*a1*a2*a4**2/54 - 5*a0*a1*a2*a4*a5**2/9 + 8*a0*a1*a3**2*a6**2/27 - 14*a0*a1*a3**2*a6/81 + 5*a0*a1*a3**2/243 - 58*a0*a1*a3*a4*a5*a6/243 + 31*a0*a1*a3*a4*a5/243 + 8*a0*a1*a3*a4*a6**2/27 - 20*a0*a1*a3*a4*a6/81 + 11*a0*a1*a3*a4/243 - 8*a0*a1*a3*a5**3/243 - 28*a0*a1*a3*a5**2*a6/81 + 14*a0*a1*a3*a5**2/243 - 16*a0*a1*a3*a5*a6**2/9 + 23*a0*a1*a3*a5*a6/27 - 7*a0*a1*a3*a5/54 + 7*a0*a1*a3*a6**3/2 - 53*a0*a1*a3*a6**2/12 + 115*a0*a1*a3*a6/72 - 13*a0*a1*a3/72 + 20*a0*a1*a4**3*a6/729 - 44*a0*a1*a4**3/2187 + 4*a0*a1*a4**2*a5**2/243 - 10*a0*a1*a4**2*a5*a6/243 + 41*a0*a1*a4**2*a5/729 + 10*a0*a1*a4**2*a6**2/27 - 20*a0*a1*a4**2*a6/81 + 17*a0*a1*a4**2/486 + 4*a0*a1*a4*a5**3/243 + 5*a0*a1*a4*a5**2*a6/27 + 13*a0*a1*a4*a5**2/486 - a0*a1*a4*a5*a6**2/6 + 19*a0*a1*a4*a5*a6/27 - 5*a0*a1*a4*a5/24 - 2*a0*a1*a5**4/27 - 7*a0*a1*a5**3*a6/18 + 5*a0*a1*a5**3/108 - 2*a0*a2**3*a3*a4/3 - 8*a0*a2**3*a3*a5/3 - a0*a2**3*a4**2/9 - 2*a0*a2**2*a3**2*a6/27 + 7*a0*a2**2*a3**2/81 - 4*a0*a2**2*a3*a4*a5/27 + 10*a0*a2**2*a3*a4*a6/27 - 5*a0*a2**2*a3*a4/81 + 32*a0*a2**2*a3*a5**2/81 + 2*a0*a2**2*a3*a5*a6/3 + 16*a0*a2**2*a3*a5/27 - 3*a0*a2**2*a3*a6**2/2 + 7*a0*a2**2*a3*a6/12 - a0*a2**2*a3/18 + 4*a0*a2**2*a4**3/729 - 76*a0*a2**2*a4**2*a5/243 - 7*a0*a2**2*a4**2*a6/27 - 8*a0*a2**2*a4**2/81 - 34*a0*a2**2*a4*a5**2/81 - 2*a0*a2**2*a4*a5*a6 + 35*a0*a2**2*a4*a5/54 - 4*a0*a2**2*a5**3/9 - 40*a0*a2*a3*a4*a6**2/81 + 110*a0*a2*a3*a4*a6/243 - 55*a0*a2*a3*a4/729 - 64*a0*a2*a3*a5**2*a6/243 + 8*a0*a2*a3*a5**2/729 + 22*a0*a2*a3*a5*a6**2/27 - 26*a0*a2*a3*a5*a6/27 + 115*a0*a2*a3*a5/486 - a0*a2*a3*a6**3/3 + 41*a0*a2*a3*a6**2/18 - 125*a0*a2*a3*a6/108 + 53*a0*a2*a3/324 + 10*a0*a2*a4**2*a5*a6/729 + 14*a0*a2*a4**2*a5/2187 - 26*a0*a2*a4**2*a6**2/81 + 95*a0*a2*a4**2*a6/243 - 7*a0*a2*a4**2/81 + 4*a0*a2*a4*a5**3/243 - 34*a0*a2*a4*a5**2*a6/81 + 91*a0*a2*a4*a5**2/729 - 32*a0*a2*a4*a5*a6**2/27 + 23*a0*a2*a4*a5*a6/54 - 19*a0*a2*a4*a5/972 - 4*a0*a2*a4*a6**3/3 + 4*a0*a2*a4*a6**2/3 - 14*a0*a2*a4*a6/27 + 17*a0*a2*a4/216 + 16*a0*a2*a5**4/243 - 14*a0*a2*a5**3*a6/81 + 28*a0*a2*a5**3/243 - 59*a0*a2*a5**2*a6**2/18 + 67*a0*a2*a5**2*a6/36 - 29*a0*a2*a5**2/108 - 4*a0*a3*a5*a6**3/9 + 44*a0*a3*a5*a6**2/243 - 17*a0*a3*a5*a6/1458 + a0*a3*a5/972 + 2*a0*a3*a6**4/3 - 20*a0*a3*a6**3/9 + 14*a0*a3*a6**2/9 - 133*a0*a3*a6/324 + 37*a0*a3/972 - 28*a0*a4**2*a6**3/243 + 98*a0*a4**2*a6**2/729 - 73*a0*a4**2*a6/2187 + 5*a0*a4**2/2187 + 16*a0*a4*a5**2*a6**2/243 - 13*a0*a4*a5**2*a6/2187 - 23*a0*a4*a5**2/4374 - 58*a0*a4*a5*a6**3/81 + 226*a0*a4*a5*a6**2/243 - 260*a0*a4*a5*a6/729 + 34*a0*a4*a5/729 - 14*a0*a4*a6**4/9 + 17*a0*a4*a6**3/9 - 22*a0*a4*a6**2/27 + 149*a0*a4*a6/972 - 5*a0*a4/486 - 2*a0*a5**4*a6/729 - 13*a0*a5**4/2187 + 10*a0*a5**3*a6**2/81 - 88*a0*a5**3*a6/729 + 41*a0*a5**3/1458 - a0*a5**2*a6**3/9 + 13*a0*a5**2*a6**2/162 - a0*a5**2*a6/81 + a0*a5**2/216 - 7*a0*a5*a6**4/2 + 137*a0*a5*a6**3/36 - 169*a0*a5*a6**2/108 + 137*a0*a5*a6/432 - a0*a5/36 + a1**3*a2*a3*a4/2 + 4*a1**3*a3*a4**2/81 - 4*a1**3*a3*a4*a5/27 - 2*a1**3*a3*a4*a6/3 + a1**3*a3*a4/9 - 2*a1**3*a3*a5*a6 + 4*a1**3*a3*a5/3 + 8*a1**3*a4**3/81 + 4*a1**3*a4**2*a5/27 + 2*a1**3*a4**2*a6/3 - 4*a1**3*a4**2/9 + a1**3*a4*a5**2/6 + a1**2*a2**2*a3*a4/3 + a1**2*a2**2*a3*a5/6 + 5*a1**2*a2**2*a4**2/18 - 4*a1**2*a2*a3**2*a6/9 + 2*a1**2*a2*a3**2/27 + 2*a1**2*a2*a3*a4*a5/9 - 2*a1**2*a2*a3*a4*a6/3 + 5*a1**2*a2*a3*a4/27 + 4*a1**2*a2*a3*a5**2/81 + 8*a1**2*a2*a3*a5*a6/9 - 26*a1**2*a2*a3*a5/27 - 9*a1**2*a2*a3*a6**2/2 + 23*a1**2*a2*a3*a6/4 - 29*a1**2*a2*a3/24 - 4*a1**2*a2*a4**3/729 + 52*a1**2*a2*a4**2*a5/243 - 2*a1**2*a2*a4**2*a6/27 + 17*a1**2*a2*a4**2/81 + 19*a1**2*a2*a4*a5**2/81 + 5*a1**2*a2*a4*a5*a6/9 - 17*a1**2*a2*a4*a5/36 + 7*a1**2*a2*a5**3/18 - 20*a1**2*a3*a4*a6**2/81 + 56*a1**2*a3*a4*a6/243 - 14*a1**2*a3*a4/243 - 14*a1**2*a3*a5**2*a6/81 + 55*a1**2*a3*a5**2/243 - 4*a1**2*a3*a5*a6**2/3 + 34*a1**2*a3*a5*a6/27 - 20*a1**2*a3*a5/81 - 2*a1**2*a3*a6**3 + 2*a1**2*a3*a6**2 - 2*a1**2*a3*a6/3 + 7*a1**2*a3/108 + 16*a1**2*a4**2*a5*a6/243 - 2*a1**2*a4**2*a5/27 - 8*a1**2*a4**2*a6**2/81 - 28*a1**2*a4**2*a6/243 + a1**2*a4**2/27 + 2*a1**2*a4*a5**3/243 + 16*a1**2*a4*a5**2*a6/81 - 2*a1**2*a4*a5**2/243 + 20*a1**2*a4*a5*a6**2/27 - 41*a1**2*a4*a5*a6/81 + a1**2*a4*a5/18 - 8*a1**2*a4*a6**3/3 + 32*a1**2*a4*a6**2/9 - 23*a1**2*a4*a6/18 + 5*a1**2*a4/36 - a1**2*a5**3*a6/9 + 7*a1**2*a5**3/54 + 5*a1**2*a5**2*a6**2/6 - 19*a1**2*a5**2*a6/36 - a1**2*a5**2/24 + 2*a1*a2**3*a3**2/9 + 2*a1*a2**3*a3*a4/9 - 7*a1*a2**3*a3*a6/2 - a1*a2**3*a3 - a1*a2**3*a4**2/9 + 17*a1*a2**3*a4*a5/18 + 32*a1*a2**2*a3*a4*a6/81 - 20*a1*a2**2*a3*a4/81 + 56*a1*a2**2*a3*a5**2/243 + 26*a1*a2**2*a3*a5*a6/27 - 5*a1*a2**2*a3*a5/27 + 19*a1*a2**2*a3*a6**2/3 - 131*a1*a2**2*a3*a6/18 + 55*a1*a2**2*a3/36 + 2*a1*a2**2*a4**2*a5/729 + 2*a1*a2**2*a4**2*a6/9 - a1*a2**2*a4**2/9 + 46*a1*a2**2*a4*a5**2/243 - 2*a1*a2**2*a4*a5*a6/27 + 55*a1*a2**2*a4*a5/162 + a1*a2**2*a4*a6**2/6 - 55*a1*a2**2*a4*a6/36 + a1*a2**2*a4/3 + 4*a1*a2**2*a5**3/81 + 5*a1*a2**2*a5**2*a6/2 - 5*a1*a2**2*a5**2/6 - 46*a1*a2*a3*a5*a6**2/81 + 121*a1*a2*a3*a5*a6/81 - 61*a1*a2*a3*a5/162 - 2*a1*a2*a3*a6**3 + 44*a1*a2*a3*a6**2/9 - 58*a1*a2*a3*a6/27 + 29*a1*a2*a3/108 + 28*a1*a2*a4**2*a6**2/243 - 80*a1*a2*a4**2*a6/729 + a1*a2*a4**2/81 + 44*a1*a2*a4*a5**2*a6/729 - 85*a1*a2*a4*a5**2/729 + 4*a1*a2*a4*a5*a6**2/27 - 29*a1*a2*a4*a5*a6/243 + a1*a2*a4*a5/54 + 26*a1*a2*a4*a6**3/9 - 34*a1*a2*a4*a6**2/9 + 203*a1*a2*a4*a6/162 - 7*a1*a2*a4/54 + 14*a1*a2*a5**4/729 + 74*a1*a2*a5**3*a6/243 - 19*a1*a2*a5**3/243 - 22*a1*a2*a5**2*a6**2/27 + 116*a1*a2*a5**2*a6/81 - 97*a1*a2*a5**2/324 + 4*a1*a2*a5*a6**3 - 97*a1*a2*a5*a6**2/36 - 7*a1*a2*a5*a6/12 + 7*a1*a2*a5/24 - 16*a1*a3*a6**4/27 + 34*a1*a3*a6**3/27 - 224*a1*a3*a6**2/243 + 73*a1*a3*a6/243 - 35*a1*a3/972 - 16*a1*a4*a5*a6**3/243 + 154*a1*a4*a5*a6**2/729 - 34*a1*a4*a5*a6/729 + a1*a4*a5/1458 - 40*a1*a4*a6**4/27 + 80*a1*a4*a6**3/27 - 422*a1*a4*a6**2/243 + 4*a1*a4*a6/9 - 7*a1*a4/162 + 16*a1*a5**3*a6**2/243 - 76*a1*a5**3*a6/729 + 5*a1*a5**3/486 + 56*a1*a5**2*a6**3/81 - 212*a1*a5**2*a6**2/243 + 53*a1*a5**2*a6/162 - 35*a1*a5**2/972 - 4*a1*a5*a6**4/9 + 31*a1*a5*a6**3/27 - 35*a1*a5*a6**2/54 + 31*a1*a5*a6/162 - 7*a1*a5/324 + 2*a1*a6**5 - 2*a1*a6**4 - 8*a1*a6**3/9 + 13*a1*a6**2/9 - 17*a1*a6/36 + 7*a1/144 + 4*a2**5*a3 + 2*a2**4*a3*a4/81 - 16*a2**4*a3*a5/27 - 8*a2**4*a3*a6/3 + 23*a2**4*a3/9 + 2*a2**4*a4**2/9 - 2*a2**4*a4*a5/9 + 19*a2**4*a4*a6/6 - 7*a2**4*a4/6 + 80*a2**3*a3*a5*a6/81 - 28*a2**3*a3*a5/27 - 14*a2**3*a3*a6/9 + 10*a2**3*a3/27 - 20*a2**3*a4**2*a6/243 + 14*a2**3*a4**2/243 + 10*a2**3*a4*a5**2/243 + 10*a2**3*a4*a5*a6/9 - 41*a2**3*a4*a5/81 - 19*a2**3*a4*a6**2/9 + 137*a2**3*a4*a6/54 - 10*a2**3*a4/27 + 4*a2**3*a5**2*a6/27 - 7*a2**3*a5**2/27 + 14*a2**3*a5*a6**2/3 - 13*a2**3*a5*a6/3 + 4*a2**3*a5/3 + 40*a2**2*a3*a6**3/27 - 160*a2**2*a3*a6**2/81 + 127*a2**2*a3*a6/162 - 10*a2**2*a3/81 + 14*a2**2*a4*a5*a6**2/81 - 71*a2**2*a4*a5*a6/243 + a2**2*a4*a5/81 + 58*a2**2*a4*a6**3/27 - 250*a2**2*a4*a6**2/81 + 29*a2**2*a4*a6/27 - 7*a2**2*a4/54 + 8*a2**2*a5**3*a6/81 - 20*a2**2*a5**3/243 + 32*a2**2*a5**2*a6**2/27 - 22*a2**2*a5**2*a6/27 + a2**2*a5**2/9 - 10*a2**2*a5*a6**3/9 + 113*a2**2*a5*a6**2/54 - 77*a2**2*a5*a6/108 + 6*a2**2*a6**4 - 9*a2**2*a6**3 + 43*a2**2*a6**2/8 - 37*a2**2*a6/24 + a2**2/6 + 16*a2*a4*a6**4/81 - 70*a2*a4*a6**3/243 + 29*a2*a4*a6**2/243 - 5*a2*a4*a6/243 + 28*a2*a5**2*a6**3/81 - 17*a2*a5**2*a6**2/27 + 16*a2*a5**2*a6/81 - a2*a5**2/81 + 100*a2*a5*a6**4/27 - 445*a2*a5*a6**3/81 + 413*a2*a5*a6**2/162 - 73*a2*a5*a6/162 + 7*a2*a5/324 - 4*a2*a6**5/3 + 32*a2*a6**4/9 - 137*a2*a6**3/54 + 77*a2*a6**2/108 - 2*a2*a6/27 + 8*a5*a6**5/27 - 20*a5*a6**4/27 + 118*a5*a6**3/243 - 31*a5*a6**2/243 + a5*a6/81 + 8*a6**6/3 - 52*a6**5/9 + 121*a6**4/27 - 134*a6**3/81 + 97*a6**2/324 - 7*a6/324",
      "a0**3*a3*a4*a5/6 - a0**3*a4**3/18 - a0**2*a1*a3*a4*a5/9 + 4*a0**2*a1*a3*a4*a6/3 - 5*a0**2*a1*a3*a4/18 + a0**2*a1*a3*a5**2/3 + a0**2*a1*a4**3/27 - 7*a0**2*a1*a4**2*a5/27 + 5*a0**2*a2**2*a3*a4/6 + 4*a0**2*a2*a3**2*a4/243 + 4*a0**2*a2*a3*a4**2/243 + 8*a0**2*a2*a3*a4*a5/81 - 7*a0**2*a2*a3*a4*a6/9 + 5*a0**2*a2*a3*a4/27 + 3*a0**2*a2*a3*a5*a6/2 - 11*a0**2*a2*a3*a5/12 - 2*a0**2*a2*a4**3/81 + 8*a0**2*a2*a4**2*a5/81 + a0**2*a2*a4**2*a6 + a0**2*a2*a4**2/36 - 8*a0**2*a2*a4*a5**2/27 - 4*a0**2*a3*a4**2*a6/729 - 2*a0**2*a3*a4**2/2187 + 28*a0**2*a3*a4*a5**2/2187 + 20*a0**2*a3*a4*a5*a6/243 - 2*a0**2*a3*a4*a5/729 + 16*a0**2*a3*a4*a6**2/27 - 20*a0**2*a3*a4*a6/81 + 7*a0**2*a3*a4/243 + 3*a0**2*a3*a6**3/2 - 11*a0**2*a3*a6**2/4 + 29*a0**2*a3*a6/24 - 11*a0**2*a3/72 - 20*a0**2*a4**3*a5/6561 - 8*a0**2*a4**3*a6/243 + 8*a0**2*a4**2*a5**2/2187 - 34*a0**2*a4**2*a5*a6/243 + 19*a0**2*a4**2*a5/729 - a0**2*a4**2*a6**2/3 + a0**2*a4**2*a6/6 - a0**2*a4**2/54 + 20*a0**2*a4*a5**3/729 + 10*a0**2*a4*a5**2*a6/81 - a0**2*a4*a5**2/27 + a0**2*a4*a5*a6**2/3 + a0**2*a4*a5*a6/4 - 25*a0**2*a4*a5/216 - a0**2*a5**3*a6/18 - 5*a0**2*a5**3/108 - 8*a0*a1**2*a2*a3*a4/3 - 4*a0*a1**2*a3**2*a4/243 - 4*a0*a1**2*a3*a4**2/243 - 2*a0*a1**2*a3*a4*a5/81 - a0*a1**2*a3*a4*a6/9 - 2*a0*a1**2*a3*a5**2/9 + 4*a0*a1**2*a3*a5*a6/3 + 5*a0*a1**2*a3*a5/18 + 2*a0*a1**2*a4**2*a5/27 - 5*a0*a1**2*a4**2*a6/9 - a0*a1**2*a4**2/27 - 5*a0*a1**2*a4*a5**2/18 + 8*a0*a1*a2**2*a3*a4/9 - 13*a0*a1*a2**2*a3*a5/6 - 10*a0*a1*a2**2*a4**2/9 + 28*a0*a1*a2*a3*a4**2/729 - 56*a0*a1*a2*a3*a4*a5/243 - 28*a0*a1*a2*a3*a4*a6/27 + 16*a0*a1*a2*a3*a4/81 + 4*a0*a1*a2*a3*a5**2/27 - 29*a0*a1*a2*a3*a5*a6/9 + 71*a0*a1*a2*a3*a5/54 - 7*a0*a1*a2*a3*a6**2/2 + 67*a0*a1*a2*a3*a6/12 - 35*a0*a1*a2*a3/24 + 28*a0*a1*a2*a4**3/243 + 10*a0*a1*a2*a4**2*a5/81 + 22*a0*a1*a2*a4**2*a6/27 - 37*a0*a1*a2*a4**2/81 + 10*a0*a1*a2*a4*a5**2/27 + a0*a1*a2*a4*a5*a6/18 - 5*a0*a1*a2*a4*a5/54 - 7*a0*a1*a2*a5**3/18 - 16*a0*a1*a3**2*a6**2/81 + 28*a0*a1*a3**2*a6/243 - 10*a0*a1*a3**2/729 + 116*a0*a1*a3*a4*a5*a6/729 - 62*a0*a1*a3*a4*a5/729 - 16*a0*a1*a3*a4*a6**2/81 + 40*a0*a1*a3*a4*a6/243 - 22*a0*a1*a3*a4/729 + 16*a0*a1*a3*a5**3/729 + 56*a0*a1*a3*a5**2*a6/243 - 28*a0*a1*a3*a5**2/729 + 32*a0*a1*a3*a5*a6**2/27 - 46*a0*a1*a3*a5*a6/81 + 7*a0*a1*a3*a5/81 - 7*a0*a1*a3*a6**3/3 + 53*a0*a1*a3*a6**2/18 - 115*a0*a1*a3*a6/108 + 13*a0*a1*a3/108 - 40*a0*a1*a4**3*a6/2187 + 88*a0*a1*a4**3/6561 - 8*a0*a1*a4**2*a5**2/729 + 20*a0*a1*a4**2*a5*a6/729 - 82*a0*a1*a4**2*a5/2187 - 20*a0*a1*a4**2*a6**2/81 + 40*a0*a1*a4**2*a6/243 - 17*a0*a1*a4**2/729 - 8*a0*a1*a4*a5**3/729 - 10*a0*a1*a4*a5**2*a6/81 - 13*a0*a1*a4*a5**2/729 + a0*a1*a4*a5*a6**2/9 - 38*a0*a1*a4*a5*a6/81 + 5*a0*a1*a4*a5/36 + a0*a1*a4*a6**3/3 + 7*a0*a1*a4*a6**2/9 - 53*a0*a1*a4*a6/108 + 19*a0*a1*a4/216 + 4*a0*a1*a5**4/81 + 7*a0*a1*a5**3*a6/27 - 5*a0*a1*a5**3/162 + a0*a1*a5**2*a6**2/3 - 19*a0*a1*a5**2*a6/54 - 5*a0*a1*a5**2/72 + 4*a0*a2**3*a3*a4/9 + 16*a0*a2**3*a3*a5/9 - a0*a2**3*a3*a6/2 - 23*a0*a2**3*a3/12 + 2*a0*a2**3*a4**2/27 - 25*a0*a2**3*a4*a5/18 + 4*a0*a2**2*a3**2*a6/81 - 14*a0*a2**2*a3**2/243 + 8*a0*a2**2*a3*a4*a5/81 - 20*a0*a2**2*a3*a4*a6/81 + 10*a0*a2**2*a3*a4/243 - 64*a0*a2**2*a3*a5**2/243 - 4*a0*a2**2*a3*a5*a6/9 - 32*a0*a2**2*a3*a5/81 + a0*a2**2*a3*a6**2 - 7*a0*a2**2*a3*a6/18 + a0*a2**2*a3/27 - 8*a0*a2**2*a4**3/2187 + 152*a0*a2**2*a4**2*a5/729 + 14*a0*a2**2*a4**2*a6/81 + 16*a0*a2**2*a4**2/243 + 68*a0*a2**2*a4*a5**2/243 + 4*a0*a2**2*a4*a5*a6/3 - 35*a0*a2**2*a4*a5/81 - 13*a0*a2**2*a4*a6**2/6 + 5*a0*a2**2*a4*a6/36 - 2*a0*a2**2*a4/9 + 8*a0*a2**2*a5**3/27 - 5*a0*a2**2*a5**2*a6/18 + 5*a0*a2**2*a5**2/108 + 80*a0*a2*a3*a4*a6**2/243 - 220*a0*a2*a3*a4*a6/729 + 110*a0*a2*a3*a4/2187 + 128*a0*a2*a3*a5**2*a6/729 - 16*a0*a2*a3*a5**2/2187 - 44*a0*a2*a3*a5*a6**2/81 + 52*a0*a2*a3*a5*a6/81 - 115*a0*a2*a3*a5/729 + 2*a0*a2*a3*a6**3/9 - 41*a0*a2*a3*a6**2/27 + 125*a0*a2*a3*a6/162 - 53*a0*a2*a3/486 - 20*a0*a2*a4**2*a5*a6/2187 - 28*a0*a2*a4**2*a5/6561 + 52*a0*a2*a4**2*a6**2/243 - 190*a0*a2*a4**2*a6/729 + 14*a0*a2*a4**2/243 - 8*a0*a2*a4*a5**3/729 + 68*a0*a2*a4*a5**2*a6/243 - 182*a0*a2*a4*a5**2/2187 + 64*a0*a2*a4*a5*a6**2/81 - 23*a0*a2*a4*a5*a6/81 + 19*a0*a2*a4*a5/1458 + 8*a0*a2*a4*a6**3/9 - 8*a0*a2*a4*a6**2/9 + 28*a0*a2*a4*a6/81 - 17*a0*a2*a4/324 - 32*a0*a2*a5**4/729 + 28*a0*a2*a5**3*a6/243 - 56*a0*a2*a5**3/729 + 59*a0*a2*a5**2*a6**2/27 - 67*a0*a2*a5**2*a6/54 + 29*a0*a2*a5**2/162 + 7*a0*a2*a5*a6**3/2 - 65*a0*a2*a5*a6**2/18 + 23*a0*a2*a5*a6/108 + 67*a0*a2*a5/432 + 8*a0*a3*a5*a6**3/27 - 88*a0*a3*a5*a6**2/729 + 17*a0*a3*a5*a6/2187 - a0*a3*a5/1458 - 4*a0*a3*a6**4/9 + 40*a0*a3*a6**3/27 - 28*a0*a3*a6**2/27 + 133*a0*a3*a6/486 - 37*a0*a3/1458 + 56*a0*a4**2*a6**3/729 - 196*a0*a4**2*a6**2/2187 + 146*a0*a4**2*a6/6561 - 10*a0*a4**2/6561 - 32*a0*a4*a5**2*a6**2/729 + 26*a0*a4*a5**2*a6/6561 + 23*a0*a4*a5**2/6561 + 116*a0*a4*a5*a6**3/243 - 452*a0*a4*a5*a6**2/729 + 520*a0*a4*a5*a6/2187 - 68*a0*a4*a5/2187 + 28*a0*a4*a6**4/27 - 34*a0*a4*a6**3/27 + 44*a0*a4*a6**2/81 - 149*a0*a4*a6/1458 + 5*a0*a4/729 + 4*a0*a5**4*a6/2187 + 26*a0*a5**4/6561 - 20*a0*a5**3*a6**2/243 + 176*a0*a5**3*a6/2187 - 41*a0*a5**3/2187 + 2*a0*a5**2*a6**3/27 - 13*a0*a5**2*a6**2/243 + 2*a0*a5**2*a6/243 - a0*a5**2/324 + 7*a0*a5*a6**4/3 - 137*a0*a5*a6**3/54 + 169*a0*a5*a6**2/162 - 137*a0*a5*a6/648 + a0*a5/54 + 6*a0*a6**5 - 17*a0*a6**4/2 + 41*a0*a6**3/12 - 11*a0*a6**2/36 - 31*a0*a6/432 + 5*a0/432 + a1**4*a3*a4 - a1**3*a2*a3*a4/3 - a1**3*a2*a3*a5/3 + 7*a1**3*a2*a4**2/9 - 8*a1**3*a3*a4**2/243 + 8*a1**3*a3*a4*a5/81 + 4*a1**3*a3*a4*a6/9 - 2*a1**3*a3*a4/27 + 4*a1**3*a3*a5*a6/3 - 8*a1**3*a3*a5/9 + 3*a1**3*a3*a6**2 - 5*a1**3*a3*a6/2 + 7*a1**3*a3/12 - 16*a1**3*a4**3/243 - 8*a1**3*a4**2*a5/81 - 4*a1**3*a4**2*a6/9 + 8*a1**3*a4**2/27 - a1**3*a4*a5**2/9 - 4*a1**3*a4*a5*a6/3 + 7*a1**3*a4*a5/18 - 2*a1**2*a2**2*a3*a4/9 - a1**2*a2**2*a3*a5/9 - 8*a1**2*a2**2*a3*a6 + 5*a1**2*a2**2*a3/2 - 5*a1**2*a2**2*a4**2/27 + 5*a1**2*a2**2*a4*a5/3 + 8*a1**2*a2*a3**2*a6/27 - 4*a1**2*a2*a3**2/81 - 4*a1**2*a2*a3*a4*a5/27 + 4*a1**2*a2*a3*a4*a6/9 - 10*a1**2*a2*a3*a4/81 - 8*a1**2*a2*a3*a5**2/243 - 16*a1**2*a2*a3*a5*a6/27 + 52*a1**2*a2*a3*a5/81 + 3*a1**2*a2*a3*a6**2 - 23*a1**2*a2*a3*a6/6 + 29*a1**2*a2*a3/36 + 8*a1**2*a2*a4**3/2187 - 104*a1**2*a2*a4**2*a5/729 + 4*a1**2*a2*a4**2*a6/81 - 34*a1**2*a2*a4**2/243 - 38*a1**2*a2*a4*a5**2/243 - 10*a1**2*a2*a4*a5*a6/27 + 17*a1**2*a2*a4*a5/54 - 3*a1**2*a2*a4*a6**2 + 35*a1**2*a2*a4*a6/18 - a1**2*a2*a4/9 - 7*a1**2*a2*a5**3/27 - 25*a1**2*a2*a5**2*a6/18 + 19*a1**2*a2*a5**2/36 + 40*a1**2*a3*a4*a6**2/243 - 112*a1**2*a3*a4*a6/729 + 28*a1**2*a3*a4/729 + 28*a1**2*a3*a5**2*a6/243 - 110*a1**2*a3*a5**2/729 + 8*a1**2*a3*a5*a6**2/9 - 68*a1**2*a3*a5*a6/81 + 40*a1**2*a3*a5/243 + 4*a1**2*a3*a6**3/3 - 4*a1**2*a3*a6**2/3 + 4*a1**2*a3*a6/9 - 7*a1**2*a3/162 - 32*a1**2*a4**2*a5*a6/729 + 4*a1**2*a4**2*a5/81 + 16*a1**2*a4**2*a6**2/243 + 56*a1**2*a4**2*a6/729 - 2*a1**2*a4**2/81 - 4*a1**2*a4*a5**3/729 - 32*a1**2*a4*a5**2*a6/243 + 4*a1**2*a4*a5**2/729 - 40*a1**2*a4*a5*a6**2/81 + 82*a1**2*a4*a5*a6/243 - a1**2*a4*a5/27 + 16*a1**2*a4*a6**3/9 - 64*a1**2*a4*a6**2/27 + 23*a1**2*a4*a6/27 - 5*a1**2*a4/54 + 2*a1**2*a5**3*a6/27 - 7*a1**2*a5**3/81 - 5*a1**2*a5**2*a6**2/9 + 19*a1**2*a5**2*a6/54 + a1**2*a5**2/36 - 2*a1**2*a5*a6**3/3 + 13*a1**2*a5*a6**2/18 - 11*a1**2*a5*a6/18 + a1**2*a5/6 + 11*a1*a2**4*a3/2 - 4*a1*a2**3*a3**2/27 - 4*a1*a2**3*a3*a4/27 + 7*a1*a2**3*a3*a6/3 + 2*a1*a2**3*a3/3 + 2*a1*a2**3*a4**2/27 - 17*a1*a2**3*a4*a5/27 + 8*a1*a2**3*a4*a6/3 - 7*a1*a2**3*a4/6 + 25*a1*a2**3*a5**2/18 - 64*a1*a2**2*a3*a4*a6/243 + 40*a1*a2**2*a3*a4/243 - 112*a1*a2**2*a3*a5**2/729 - 52*a1*a2**2*a3*a5*a6/81 + 10*a1*a2**2*a3*a5/81 - 38*a1*a2**2*a3*a6**2/9 + 131*a1*a2**2*a3*a6/27 - 55*a1*a2**2*a3/54 - 4*a1*a2**2*a4**2*a5/2187 - 4*a1*a2**2*a4**2*a6/27 + 2*a1*a2**2*a4**2/27 - 92*a1*a2**2*a4*a5**2/729 + 4*a1*a2**2*a4*a5*a6/81 - 55*a1*a2**2*a4*a5/243 - a1*a2**2*a4*a6**2/9 + 55*a1*a2**2*a4*a6/54 - 2*a1*a2**2*a4/9 - 8*a1*a2**2*a5**3/243 - 5*a1*a2**2*a5**2*a6/3 + 5*a1*a2**2*a5**2/9 - 13*a1*a2**2*a5*a6**2/3 + 10*a1*a2**2*a5*a6/3 - a1*a2**2*a5/9 + 92*a1*a2*a3*a5*a6**2/243 - 242*a1*a2*a3*a5*a6/243 + 61*a1*a2*a3*a5/243 + 4*a1*a2*a3*a6**3/3 - 88*a1*a2*a3*a6**2/27 + 116*a1*a2*a3*a6/81 - 29*a1*a2*a3/162 - 56*a1*a2*a4**2*a6**2/729 + 160*a1*a2*a4**2*a6/2187 - 2*a1*a2*a4**2/243 - 88*a1*a2*a4*a5**2*a6/2187 + 170*a1*a2*a4*a5**2/2187 - 8*a1*a2*a4*a5*a6**2/81 + 58*a1*a2*a4*a5*a6/729 - a1*a2*a4*a5/81 - 52*a1*a2*a4*a6**3/27 + 68*a1*a2*a4*a6**2/27 - 203*a1*a2*a4*a6/243 + 7*a1*a2*a4/81 - 28*a1*a2*a5**4/2187 - 148*a1*a2*a5**3*a6/729 + 38*a1*a2*a5**3/729 + 44*a1*a2*a5**2*a6**2/81 - 232*a1*a2*a5**2*a6/243 + 97*a1*a2*a5**2/486 - 8*a1*a2*a5*a6**3/3 + 97*a1*a2*a5*a6**2/54 + 7*a1*a2*a5*a6/18 - 7*a1*a2*a5/36 - 8*a1*a2*a6**4 + 28*a1*a2*a6**3/3 - 143*a1*a2*a6**2/36 + 43*a1*a2*a6/36 - a1*a2/6 + 32*a1*a3*a6**4/81 - 68*a1*a3*a6**3/81 + 448*a1*a3*a6**2/729 - 146*a1*a3*a6/729 + 35*a1*a3/1458 + 32*a1*a4*a5*a6**3/729 - 308*a1*a4*a5*a6**2/2187 + 68*a1*a4*a5*a6/2187 - a1*a4*a5/2187 + 80*a1*a4*a6**4/81 - 160*a1*a4*a6**3/81 + 844*a1*a4*a6**2/729 - 8*a1*a4*a6/27 + 7*a1*a4/243 - 32*a1*a5**3*a6**2/729 + 152*a1*a5**3*a6/2187 - 5*a1*a5**3/729 - 112*a1*a5**2*a6**3/243 + 424*a1*a5**2*a6**2/729 - 53*a1*a5**2*a6/243 + 35*a1*a5**2/1458 + 8*a1*a5*a6**4/27 - 62*a1*a5*a6**3/81 + 35*a1*a5*a6**2/81 - 31*a1*a5*a6/243 + 7*a1*a5/486 - 4*a1*a6**5/3 + 4*a1*a6**4/3 + 16*a1*a6**3/27 - 26*a1*a6**2/27 + 17*a1*a6/54 - 7*a1/216 - 8*a2**5*a3/3 + 3*a2**5*a4/2 - 4*a2**4*a3*a4/243 + 32*a2**4*a3*a5/81 + 16*a2**4*a3*a6/9 - 46*a2**4*a3/27 - 4*a2**4*a4**2/27 + 4*a2**4*a4*a5/27 - 19*a2**4*a4*a6/9 + 7*a2**4*a4/9 + 20*a2**4*a5*a6/3 - 17*a2**4*a5/6 - 160*a2**3*a3*a5*a6/243 + 56*a2**3*a3*a5/81 + 28*a2**3*a3*a6/27 - 20*a2**3*a3/81 + 40*a2**3*a4**2*a6/729 - 28*a2**3*a4**2/729 - 20*a2**3*a4*a5**2/729 - 20*a2**3*a4*a5*a6/27 + 82*a2**3*a4*a5/243 + 38*a2**3*a4*a6**2/27 - 137*a2**3*a4*a6/81 + 20*a2**3*a4/81 - 8*a2**3*a5**2*a6/81 + 14*a2**3*a5**2/81 - 28*a2**3*a5*a6**2/9 + 26*a2**3*a5*a6/9 - 8*a2**3*a5/9 + 10*a2**3*a6**3 - 28*a2**3*a6**2/3 + 71*a2**3*a6/24 - 7*a2**3/12 - 80*a2**2*a3*a6**3/81 + 320*a2**2*a3*a6**2/243 - 127*a2**2*a3*a6/243 + 20*a2**2*a3/243 - 28*a2**2*a4*a5*a6**2/243 + 142*a2**2*a4*a5*a6/729 - 2*a2**2*a4*a5/243 - 116*a2**2*a4*a6**3/81 + 500*a2**2*a4*a6**2/243 - 58*a2**2*a4*a6/81 + 7*a2**2*a4/81 - 16*a2**2*a5**3*a6/243 + 40*a2**2*a5**3/729 - 64*a2**2*a5**2*a6**2/81 + 44*a2**2*a5**2*a6/81 - 2*a2**2*a5**2/27 + 20*a2**2*a5*a6**3/27 - 113*a2**2*a5*a6**2/81 + 77*a2**2*a5*a6/162 - 4*a2**2*a6**4 + 6*a2**2*a6**3 - 43*a2**2*a6**2/12 + 37*a2**2*a6/36 - a2**2/9 - 32*a2*a4*a6**4/243 + 140*a2*a4*a6**3/729 - 58*a2*a4*a6**2/729 + 10*a2*a4*a6/729 - 56*a2*a5**2*a6**3/243 + 34*a2*a5**2*a6**2/81 - 32*a2*a5**2*a6/243 + 2*a2*a5**2/243 - 200*a2*a5*a6**4/81 + 890*a2*a5*a6**3/243 - 413*a2*a5*a6**2/243 + 73*a2*a5*a6/243 - 7*a2*a5/486 + 8*a2*a6**5/9 - 64*a2*a6**4/27 + 137*a2*a6**3/81 - 77*a2*a6**2/162 + 4*a2*a6/81 - 16*a5*a6**5/81 + 40*a5*a6**4/81 - 236*a5*a6**3/729 + 62*a5*a6**2/729 - 2*a5*a6/243 - 16*a6**6/9 + 104*a6**5/27 - 242*a6**4/81 + 268*a6**3/243 - 97*a6**2/486 + 7*a6/486"
    &#93;,
    &#91;
      "-a0**2*a2*a3**3/18 - a0**2*a2*a3**2*a4/18 + a0**2*a3**2*a4*a6/18 - a0**2*a3**2*a4/324 - 7*a0**2*a3**2*a5**2/162 - 5*a0**2*a3**2*a5*a6/18 + a0**2*a3**2*a5/108 - a0**2*a3*a4**2*a5/486 + 4*a0**2*a3*a4**2*a6/27 - a0**2*a3*a4**2/162 - a0**2*a3*a4*a5**2/27 + 2*a0**2*a4**4/729 + a0**2*a4**3*a5/243 + a0*a1**2*a3**3/18 + a0*a1**2*a3**2*a4/18 - a0*a1*a2*a3**2*a4/6 + 7*a0*a1*a2*a3**2*a5/9 - 23*a0*a1*a2*a3*a4**2/54 - 17*a0*a1*a3**2*a5*a6/54 + 7*a0*a1*a3**2*a5/36 - a0*a1*a3**2*a6/6 + a0*a1*a3**2/18 - a0*a1*a3*a4**2/54 - 2*a0*a1*a3*a4*a5**2/81 - 7*a0*a1*a3*a4*a5*a6/18 + 17*a0*a1*a3*a4*a5/108 + a0*a1*a4**3*a5/81 + 2*a0*a1*a4**3*a6/81 + a0*a1*a4**2*a5**2/81 - a0*a2**2*a3**2*a5/3 + a0*a2**2*a3**2*a6 - a0*a2**2*a3**2/3 + a0*a2**2*a3*a4**2/81 - 11*a0*a2**2*a3*a4*a5/27 - 7*a0*a2*a3**2*a6**2/6 + 49*a0*a2*a3**2*a6/54 - 73*a0*a2*a3**2/648 - 2*a0*a2*a3*a4*a5*a6/27 - 47*a0*a2*a3*a4*a5/324 - 5*a0*a2*a3*a4*a6**2/6 + 47*a0*a2*a3*a4*a6/108 - 2*a0*a2*a3*a4/81 - a0*a2*a3*a5**3/81 - a0*a2*a3*a5**2*a6/3 - 11*a0*a2*a3*a5**2/81 - 2*a0*a2*a4**3*a6/243 + 35*a0*a2*a4**3/729 + a0*a2*a4**2*a5**2/81 + a0*a2*a4**2*a5*a6/81 + 35*a0*a2*a4**2*a5/486 + a0*a2*a4*a5**3/81 - 7*a0*a3*a4*a6**3/27 - 4*a0*a3*a4*a6**2/27 + 17*a0*a3*a4*a6/108 - 7*a0*a3*a4/324 + a0*a3*a5**2*a6**2/81 - a0*a3*a5**2*a6/81 - 5*a0*a3*a5**2/648 - 5*a0*a3*a5*a6**3/9 - 4*a0*a3*a5*a6**2/27 + 7*a0*a3*a5*a6/36 - 7*a0*a3*a5/216 - a0*a4**2*a5*a6**2/243 + 19*a0*a4**2*a5*a6/243 - a0*a4**2*a5/54 - 2*a0*a4**2*a6**3/27 - 5*a0*a4**2*a6**2/81 + a0*a4**2*a6/27 + a0*a4*a5**3*a6/243 - 13*a0*a4*a5**3/972 + a0*a4*a5**2*a6**2/27 + 49*a0*a4*a5**2*a6/324 - a0*a4*a5**2/27 - 2*a0*a5**4/81 + a1**3*a3**2*a4/9 - a1**3*a3**2*a5/3 + 2*a1**3*a3*a4**2/9 + a1**2*a2*a3**2*a5/3 - a1**2*a2*a3**2*a6/2 + a1**2*a2*a3**2/4 + 7*a1**2*a2*a3*a4*a5/18 - 4*a1**2*a3**2*a6**2/9 + a1**2*a3**2*a6/2 - 7*a1**2*a3**2/54 + 7*a1**2*a3*a4*a5/54 - 10*a1**2*a3*a4*a6**2/9 + 2*a1**2*a3*a4*a6/3 - 11*a1**2*a3*a4/108 - a1**2*a3*a5**3/54 + a1**2*a3*a5**2*a6/6 + 19*a1**2*a3*a5**2/108 - 10*a1**2*a4**3/243 + a1**2*a4**2*a5**2/81 + 2*a1**2*a4**2*a5*a6/27 - 5*a1**2*a4**2*a5/81 + 13*a1*a2**2*a3**2*a6/9 - 37*a1*a2**2*a3**2/54 + 2*a1*a2**2*a3*a4*a5/27 + 16*a1*a2**2*a3*a4*a6/9 - 14*a1*a2**2*a3*a4/27 + 2*a1*a2**2*a3*a5**2/27 - 2*a1*a2**2*a4**3/243 - a1*a2**2*a4**2*a5/81 + 4*a1*a2*a3*a4*a6**2/9 + 91*a1*a2*a3*a4*a6/162 - 11*a1*a2*a3*a4/54 - 5*a1*a2*a3*a5**2*a6/27 + 5*a1*a2*a3*a5**2/108 + a1*a2*a3*a5*a6**2/9 + 5*a1*a2*a3*a5*a6/4 - 5*a1*a2*a3*a5/24 - a1*a2*a4**2*a5*a6/81 - 35*a1*a2*a4**2*a5/486 + 2*a1*a2*a4**2*a6**2/27 + 5*a1*a2*a4**2*a6/81 - a1*a2*a4**2/18 + 2*a1*a2*a4*a5**3/81 + a1*a2*a4*a5**2*a6/9 - 10*a1*a2*a4*a5**2/81 - a1*a3*a5*a6**3/27 + 2*a1*a3*a5*a6**2/27 - 25*a1*a3*a5*a6/324 + a1*a3*a5/36 + a1*a3*a6**3/3 - 7*a1*a3*a6**2/36 + a1*a3*a6/24 - a1*a3/216 + 4*a1*a4**2*a6**3/81 + 16*a1*a4**2*a6**2/81 - 41*a1*a4**2*a6/486 + 2*a1*a4**2/243 - a1*a4*a5**2*a6**2/27 - 16*a1*a4*a5**2*a6/243 + 7*a1*a4*a5**2/486 + 11*a1*a4*a5*a6**2/27 - 71*a1*a4*a5*a6/324 + 13*a1*a4*a5/324 + a1*a5**4*a6/81 - a1*a5**4/972 + a1*a5**3*a6**2/27 - 43*a1*a5**3*a6/324 + 23*a1*a5**3/648 - 7*a2**4*a3**2/18 - 7*a2**4*a3*a4/18 - 2*a2**3*a3*a4*a6/27 - 37*a2**3*a3*a4/81 + 23*a2**3*a3*a5**2/162 + 5*a2**3*a3*a5*a6/6 - 139*a2**3*a3*a5/108 - 5*a2**3*a4**2*a5/243 - 2*a2**3*a4**2*a6/27 + a2**3*a4**2/9 - a2**3*a4*a5**2/81 + 7*a2**2*a3*a5*a6**2/54 + 8*a2**2*a3*a5*a6/81 - 41*a2**2*a3*a5/216 + 3*a2**2*a3*a6**3/2 - 9*a2**2*a3*a6**2/4 + a2**2*a3*a6 - 37*a2**2*a3/216 - 2*a2**2*a4**2*a6**2/81 - 8*a2**2*a4**2*a6/27 + 23*a2**2*a4**2/243 - 2*a2**2*a4*a5**2*a6/243 - 23*a2**2*a4*a5**2/972 + a2**2*a4*a5*a6**2/9 - 49*a2**2*a4*a5*a6/324 - 2*a2**2*a4*a5/81 + 4*a2**2*a5**4/243 + 4*a2**2*a5**3*a6/81 - 5*a2**2*a5**3/54 - a2*a3*a6**4/9 + 37*a2*a3*a6**3/54 - 305*a2*a3*a6**2/324 + 239*a2*a3*a6/648 - 25*a2*a3/648 - a2*a4*a5*a6**3/9 - 157*a2*a4*a5*a6**2/486 + 215*a2*a4*a5*a6/972 - 7*a2*a4*a5/243 + 2*a2*a4*a6**4/9 + 2*a2*a4*a6**3/27 - 43*a2*a4*a6**2/162 + 7*a2*a4*a6/108 + 2*a2*a5**3*a6**2/27 - 19*a2*a5**3*a6/972 - a2*a5**3/108 + 2*a2*a5**2*a6**3/9 - 221*a2*a5**2*a6**2/324 + 65*a2*a5**2*a6/216 - 7*a2*a5**2/648 - 4*a4*a6**5/27 - 8*a4*a6**4/81 + 25*a4*a6**3/162 - 13*a4*a6**2/324 + a4*a6/324 + 2*a5**2*a6**4/27 - 2*a5**2*a6**3/27 + a5**2*a6**2/36 - a5**2*a6/162 + 2*a5*a6**5/9 - 20*a5*a6**4/27 + 7*a5*a6**3/12 - 37*a5*a6**2/216 + a5*a6/54",
      "-a0**2*a2*a3**3/4 + a0**2*a3**2*a4*a6/4 - a0**2*a3**2*a4/72 - 7*a0**2*a3**2*a5**2/36 - a0**2*a3*a4**2*a5/108 + a0**2*a4**4/81 + a0*a1**2*a3**3/4 - 3*a0*a1*a2*a3**2*a4/4 - 17*a0*a1*a3**2*a5*a6/12 + 7*a0*a1*a3**2*a5/8 - a0*a1*a3*a4**2/12 - a0*a1*a3*a4*a5**2/9 + a0*a1*a4**3*a5/18 - 3*a0*a2**2*a3**2*a5/2 + a0*a2**2*a3*a4**2/18 - 21*a0*a2*a3**2*a6**2/4 + 49*a0*a2*a3**2*a6/12 - 73*a0*a2*a3**2/144 - a0*a2*a3*a4*a5*a6/3 - 47*a0*a2*a3*a4*a5/72 - a0*a2*a3*a5**3/18 - a0*a2*a4**3*a6/27 + 35*a0*a2*a4**3/162 + a0*a2*a4**2*a5**2/18 - 7*a0*a3*a4*a6**3/6 - 2*a0*a3*a4*a6**2/3 + 17*a0*a3*a4*a6/24 - 7*a0*a3*a4/72 + a0*a3*a5**2*a6**2/18 - a0*a3*a5**2*a6/18 - 5*a0*a3*a5**2/144 - a0*a4**2*a5*a6**2/54 + 19*a0*a4**2*a5*a6/54 - a0*a4**2*a5/12 + a0*a4*a5**3*a6/54 - 13*a0*a4*a5**3/216 + a1**3*a3**2*a4/2 + 3*a1**2*a2*a3**2*a5/2 - 2*a1**2*a3**2*a6**2 + 9*a1**2*a3**2*a6/4 - 7*a1**2*a3**2/12 + 7*a1**2*a3*a4*a5/12 - a1**2*a3*a5**3/12 - 5*a1**2*a4**3/27 + a1**2*a4**2*a5**2/18 + 13*a1*a2**2*a3**2*a6/2 - 37*a1*a2**2*a3**2/12 + a1*a2**2*a3*a4*a5/3 - a1*a2**2*a4**3/27 + 2*a1*a2*a3*a4*a6**2 + 91*a1*a2*a3*a4*a6/36 - 11*a1*a2*a3*a4/12 - 5*a1*a2*a3*a5**2*a6/6 + 5*a1*a2*a3*a5**2/24 - a1*a2*a4**2*a5*a6/18 - 35*a1*a2*a4**2*a5/108 + a1*a2*a4*a5**3/9 - a1*a3*a5*a6**3/6 + a1*a3*a5*a6**2/3 - 25*a1*a3*a5*a6/72 + a1*a3*a5/8 + 2*a1*a4**2*a6**3/9 + 8*a1*a4**2*a6**2/9 - 41*a1*a4**2*a6/108 + a1*a4**2/27 - a1*a4*a5**2*a6**2/6 - 8*a1*a4*a5**2*a6/27 + 7*a1*a4*a5**2/108 + a1*a5**4*a6/18 - a1*a5**4/216 - 7*a2**4*a3**2/4 - a2**3*a3*a4*a6/3 - 37*a2**3*a3*a4/18 + 23*a2**3*a3*a5**2/36 - 5*a2**3*a4**2*a5/54 + 7*a2**2*a3*a5*a6**2/12 + 4*a2**2*a3*a5*a6/9 - 41*a2**2*a3*a5/48 - a2**2*a4**2*a6**2/9 - 4*a2**2*a4**2*a6/3 + 23*a2**2*a4**2/54 - a2**2*a4*a5**2*a6/27 - 23*a2**2*a4*a5**2/216 + 2*a2**2*a5**4/27 - a2*a3*a6**4/2 + 37*a2*a3*a6**3/12 - 305*a2*a3*a6**2/72 + 239*a2*a3*a6/144 - 25*a2*a3/144 - a2*a4*a5*a6**3/2 - 157*a2*a4*a5*a6**2/108 + 215*a2*a4*a5*a6/216 - 7*a2*a4*a5/54 + a2*a5**3*a6**2/3 - 19*a2*a5**3*a6/216 - a2*a5**3/24 - 2*a4*a6**5/3 - 4*a4*a6**4/9 + 25*a4*a6**3/36 - 13*a4*a6**2/72 + a4*a6/72 + a5**2*a6**4/3 - a5**2*a6**3/3 + a5**2*a6**2/8 - a5**2*a6/36",
      "a0**2*a2*a3**3/27 + a0**2*a2*a3**2*a4/27 + 2*a0**2*a2*a3**2*a5/9 - a0**2*a2*a3*a4**2/18 - a0**2*a3**2*a4*a6/27 + a0**2*a3**2*a4/486 + 7*a0**2*a3**2*a5**2/243 + 5*a0**2*a3**2*a5*a6/27 - a0**2*a3**2*a5/162 + 4*a0**2*a3**2*a6**2/3 - 5*a0**2*a3**2*a6/9 + 7*a0**2*a3**2/108 + a0**2*a3*a4**2*a5/729 - 8*a0**2*a3*a4**2*a6/81 + a0**2*a3*a4**2/243 + 2*a0**2*a3*a4*a5**2/81 - 5*a0**2*a3*a4*a5*a6/18 + 13*a0**2*a3*a4*a5/324 + 5*a0**2*a3*a5**3/81 - 4*a0**2*a4**4/2187 - 2*a0**2*a4**3*a5/729 - 2*a0**2*a4**3*a6/81 + 2*a0**2*a4**3/243 + a0**2*a4**2*a5**2/243 - a0*a1**2*a3**3/27 - a0*a1**2*a3**2*a4/27 - a0*a1**2*a3**2*a5/18 + a0*a1*a2*a3**2*a4/9 - 14*a0*a1*a2*a3**2*a5/27 - 7*a0*a1*a2*a3**2*a6/3 + 4*a0*a1*a2*a3**2/9 + 23*a0*a1*a2*a3*a4**2/81 + 17*a0*a1*a2*a3*a4*a5/54 + a0*a1*a2*a4**3/27 + 17*a0*a1*a3**2*a5*a6/81 - 7*a0*a1*a3**2*a5/54 + a0*a1*a3**2*a6/9 - a0*a1*a3**2/27 + a0*a1*a3*a4**2/81 + 4*a0*a1*a3*a4*a5**2/243 + 7*a0*a1*a3*a4*a5*a6/27 - 17*a0*a1*a3*a4*a5/162 - a0*a1*a3*a4*a6**2/9 + a0*a1*a3*a4*a6/27 + a0*a1*a3*a4/108 + 17*a0*a1*a3*a5**2*a6/54 - 17*a0*a1*a3*a5**2/108 - 2*a0*a1*a4**3*a5/243 - 4*a0*a1*a4**3*a6/243 - 2*a0*a1*a4**2*a5**2/243 - 5*a0*a1*a4**2*a5*a6/81 + a0*a1*a4**2*a5/54 + a0*a1*a4*a5**3/81 + a0*a2**3*a3**2 + 2*a0*a2**2*a3**2*a5/9 - 2*a0*a2**2*a3**2*a6/3 + 2*a0*a2**2*a3**2/9 - 2*a0*a2**2*a3*a4**2/243 + 22*a0*a2**2*a3*a4*a5/81 + 2*a0*a2**2*a3*a4*a6/9 - 11*a0*a2**2*a3*a4/108 + 4*a0*a2**2*a3*a5**2/9 + a0*a2**2*a4**2*a5/27 + 7*a0*a2*a3**2*a6**2/9 - 49*a0*a2*a3**2*a6/81 + 73*a0*a2*a3**2/972 + 4*a0*a2*a3*a4*a5*a6/81 + 47*a0*a2*a3*a4*a5/486 + 5*a0*a2*a3*a4*a6**2/9 - 47*a0*a2*a3*a4*a6/162 + 4*a0*a2*a3*a4/243 + 2*a0*a2*a3*a5**3/243 + 2*a0*a2*a3*a5**2*a6/9 + 22*a0*a2*a3*a5**2/243 + 5*a0*a2*a3*a5*a6**2/2 - 8*a0*a2*a3*a5*a6/9 + 11*a0*a2*a3*a5/216 + 4*a0*a2*a4**3*a6/729 - 70*a0*a2*a4**3/2187 - 2*a0*a2*a4**2*a5**2/243 - 2*a0*a2*a4**2*a5*a6/243 - 35*a0*a2*a4**2*a5/729 - a0*a2*a4**2*a6**2/27 - 41*a0*a2*a4**2*a6/162 + 25*a0*a2*a4**2/486 - 2*a0*a2*a4*a5**3/243 - a0*a2*a4*a5**2*a6/27 + 43*a0*a2*a4*a5**2/972 + a0*a2*a5**4/81 + 14*a0*a3*a4*a6**3/81 + 8*a0*a3*a4*a6**2/81 - 17*a0*a3*a4*a6/162 + 7*a0*a3*a4/486 - 2*a0*a3*a5**2*a6**2/243 + 2*a0*a3*a5**2*a6/243 + 5*a0*a3*a5**2/972 + 10*a0*a3*a5*a6**3/27 + 8*a0*a3*a5*a6**2/81 - 7*a0*a3*a5*a6/54 + 7*a0*a3*a5/324 + 8*a0*a3*a6**4/3 - 13*a0*a3*a6**3/9 + 11*a0*a3*a6**2/108 + 13*a0*a3*a6/216 - a0*a3/108 + 2*a0*a4**2*a5*a6**2/729 - 38*a0*a4**2*a5*a6/729 + a0*a4**2*a5/81 + 4*a0*a4**2*a6**3/81 + 10*a0*a4**2*a6**2/243 - 2*a0*a4**2*a6/81 - 2*a0*a4*a5**3*a6/729 + 13*a0*a4*a5**3/1458 - 2*a0*a4*a5**2*a6**2/81 - 49*a0*a4*a5**2*a6/486 + 2*a0*a4*a5**2/81 - a0*a4*a5*a6**3/9 - 31*a0*a4*a5*a6**2/162 + 25*a0*a4*a5*a6/324 - a0*a4*a5/108 + 4*a0*a5**4/243 + 2*a0*a5**3*a6**2/81 + a0*a5**3*a6/27 - a0*a5**3/216 - 2*a1**3*a3**2*a4/27 + 2*a1**3*a3**2*a5/9 + a1**3*a3**2*a6 - a1**3*a3**2/6 - 4*a1**3*a3*a4**2/27 - 2*a1**3*a3*a4*a5/9 - a1**2*a2**2*a3**2/2 - 2*a1**2*a2*a3**2*a5/9 + a1**2*a2*a3**2*a6/3 - a1**2*a2*a3**2/6 - 7*a1**2*a2*a3*a4*a5/27 - 2*a1**2*a2*a3*a4*a6/3 + 2*a1**2*a2*a3*a4/9 - 5*a1**2*a2*a3*a5**2/9 + a1**2*a2*a4**2*a5/9 + 8*a1**2*a3**2*a6**2/27 - a1**2*a3**2*a6/3 + 7*a1**2*a3**2/81 - 7*a1**2*a3*a4*a5/81 + 20*a1**2*a3*a4*a6**2/27 - 4*a1**2*a3*a4*a6/9 + 11*a1**2*a3*a4/162 + a1**2*a3*a5**3/81 - a1**2*a3*a5**2*a6/9 - 19*a1**2*a3*a5**2/162 - 5*a1**2*a3*a5*a6**2/9 - 4*a1**2*a3*a5*a6/9 + a1**2*a3*a5/6 + 20*a1**2*a4**3/729 - 2*a1**2*a4**2*a5**2/243 - 4*a1**2*a4**2*a5*a6/81 + 10*a1**2*a4**2*a5/243 + 2*a1**2*a4**2*a6/9 - 4*a1**2*a4**2/81 + a1**2*a4*a5**2*a6/27 - 7*a1**2*a4*a5**2/162 + a1*a2**3*a3*a4/3 - 26*a1*a2**2*a3**2*a6/27 + 37*a1*a2**2*a3**2/81 - 4*a1*a2**2*a3*a4*a5/81 - 32*a1*a2**2*a3*a4*a6/27 + 28*a1*a2**2*a3*a4/81 - 4*a1*a2**2*a3*a5**2/81 - 3*a1*a2**2*a3*a5*a6 + 73*a1*a2**2*a3*a5/108 + 4*a1*a2**2*a4**3/729 + 2*a1*a2**2*a4**2*a5/243 + 5*a1*a2**2*a4**2*a6/27 + 4*a1*a2**2*a4**2/81 + 17*a1*a2**2*a4*a5**2/81 - 8*a1*a2*a3*a4*a6**2/27 - 91*a1*a2*a3*a4*a6/243 + 11*a1*a2*a3*a4/81 + 10*a1*a2*a3*a5**2*a6/81 - 5*a1*a2*a3*a5**2/162 - 2*a1*a2*a3*a5*a6**2/27 - 5*a1*a2*a3*a5*a6/6 + 5*a1*a2*a3*a5/36 - 13*a1*a2*a3*a6**3/3 - 13*a1*a2*a3*a6**2/18 + 11*a1*a2*a3*a6/12 - 5*a1*a2*a3/36 + 2*a1*a2*a4**2*a5*a6/243 + 35*a1*a2*a4**2*a5/729 - 4*a1*a2*a4**2*a6**2/81 - 10*a1*a2*a4**2*a6/243 + a1*a2*a4**2/27 - 4*a1*a2*a4*a5**3/243 - 2*a1*a2*a4*a5**2*a6/27 + 20*a1*a2*a4*a5**2/243 + 4*a1*a2*a4*a5*a6**2/27 + 47*a1*a2*a4*a5*a6/162 - 4*a1*a2*a4*a5/81 + 4*a1*a2*a5**3*a6/27 - 29*a1*a2*a5**3/324 + 2*a1*a3*a5*a6**3/81 - 4*a1*a3*a5*a6**2/81 + 25*a1*a3*a5*a6/486 - a1*a3*a5/54 - 2*a1*a3*a6**3/9 + 7*a1*a3*a6**2/54 - a1*a3*a6/36 + a1*a3/324 - 8*a1*a4**2*a6**3/243 - 32*a1*a4**2*a6**2/243 + 41*a1*a4**2*a6/729 - 4*a1*a4**2/729 + 2*a1*a4*a5**2*a6**2/81 + 32*a1*a4*a5**2*a6/729 - 7*a1*a4*a5**2/729 - 22*a1*a4*a5*a6**2/81 + 71*a1*a4*a5*a6/486 - 13*a1*a4*a5/486 - 4*a1*a4*a6**4/9 - 20*a1*a4*a6**3/27 + 11*a1*a4*a6**2/18 - 13*a1*a4*a6/81 + 5*a1*a4/324 - 2*a1*a5**4*a6/243 + a1*a5**4/1458 - 2*a1*a5**3*a6**2/81 + 43*a1*a5**3*a6/486 - 23*a1*a5**3/972 + 7*a1*a5**2*a6**3/27 + 5*a1*a5**2*a6**2/54 - 2*a1*a5**2*a6/27 + a1*a5**2/216 + 7*a2**4*a3**2/27 + 7*a2**4*a3*a4/27 + 14*a2**4*a3*a5/9 - a2**4*a4**2/9 + 4*a2**3*a3*a4*a6/81 + 74*a2**3*a3*a4/243 - 23*a2**3*a3*a5**2/243 - 5*a2**3*a3*a5*a6/9 + 139*a2**3*a3*a5/162 + 5*a2**3*a3*a6**2/2 + 7*a2**3*a3*a6/9 - 25*a2**3*a3/108 + 10*a2**3*a4**2*a5/729 + 4*a2**3*a4**2*a6/81 - 2*a2**3*a4**2/27 + 2*a2**3*a4*a5**2/243 + 7*a2**3*a4*a5*a6/27 - 5*a2**3*a4*a5/324 + 11*a2**3*a5**3/81 - 7*a2**2*a3*a5*a6**2/81 - 16*a2**2*a3*a5*a6/243 + 41*a2**2*a3*a5/324 - a2**2*a3*a6**3 + 3*a2**2*a3*a6**2/2 - 2*a2**2*a3*a6/3 + 37*a2**2*a3/324 + 4*a2**2*a4**2*a6**2/243 + 16*a2**2*a4**2*a6/81 - 46*a2**2*a4**2/729 + 4*a2**2*a4*a5**2*a6/729 + 23*a2**2*a4*a5**2/1458 - 2*a2**2*a4*a5*a6**2/27 + 49*a2**2*a4*a5*a6/486 + 4*a2**2*a4*a5/243 + 5*a2**2*a4*a6**3/9 + 53*a2**2*a4*a6**2/54 - 67*a2**2*a4*a6/108 + 23*a2**2*a4/324 - 8*a2**2*a5**4/729 - 8*a2**2*a5**3*a6/243 + 5*a2**2*a5**3/81 + a2**2*a5**2*a6**2 - 181*a2**2*a5**2*a6/324 + 97*a2**2*a5**2/648 + 2*a2*a3*a6**4/27 - 37*a2*a3*a6**3/81 + 305*a2*a3*a6**2/486 - 239*a2*a3*a6/972 + 25*a2*a3/972 + 2*a2*a4*a5*a6**3/27 + 157*a2*a4*a5*a6**2/729 - 215*a2*a4*a5*a6/1458 + 14*a2*a4*a5/729 - 4*a2*a4*a6**4/27 - 4*a2*a4*a6**3/81 + 43*a2*a4*a6**2/243 - 7*a2*a4*a6/162 - 4*a2*a5**3*a6**2/81 + 19*a2*a5**3*a6/1458 + a2*a5**3/162 - 4*a2*a5**2*a6**3/27 + 221*a2*a5**2*a6**2/486 - 65*a2*a5**2*a6/324 + 7*a2*a5**2/972 + 19*a2*a5*a6**4/9 - 10*a2*a5*a6**3/9 + a2*a5*a6**2/6 - 19*a2*a5*a6/324 + 7*a2*a5/648 + 8*a4*a6**5/81 + 16*a4*a6**4/243 - 25*a4*a6**3/243 + 13*a4*a6**2/486 - a4*a6/486 - 4*a5**2*a6**4/81 + 4*a5**2*a6**3/81 - a5**2*a6**2/54 + a5**2*a6/243 - 4*a5*a6**5/27 + 40*a5*a6**4/81 - 7*a5*a6**3/18 + 37*a5*a6**2/324 - a5*a6/81 + 4*a6**6/3 - 8*a6**5/9 - 7*a6**4/54 + 23*a6**3/108 - a6**2/18 + a6/216",
      "a0**2*a1*a3**2*a5/6 - a0**2*a1*a3*a4**2/18 - 2*a0**2*a2*a3**3/81 - 2*a0**2*a2*a3**2*a4/81 - 4*a0**2*a2*a3**2*a5/27 + 7*a0**2*a2*a3**2*a6/6 - 5*a0**2*a2*a3**2/18 + a0**2*a2*a3*a4**2/27 - 2*a0**2*a2*a3*a4*a5/27 - 2*a0**2*a2*a4**3/81 + 2*a0**2*a3**2*a4*a6/81 - a0**2*a3**2*a4/729 - 14*a0**2*a3**2*a5**2/729 - 10*a0**2*a3**2*a5*a6/81 + a0**2*a3**2*a5/243 - 8*a0**2*a3**2*a6**2/9 + 10*a0**2*a3**2*a6/27 - 7*a0**2*a3**2/162 - 2*a0**2*a3*a4**2*a5/2187 + 16*a0**2*a3*a4**2*a6/243 - 2*a0**2*a3*a4**2/729 - 4*a0**2*a3*a4*a5**2/243 + 5*a0**2*a3*a4*a5*a6/27 - 13*a0**2*a3*a4*a5/486 + 11*a0**2*a3*a4*a6**2/18 - 29*a0**2*a3*a4*a6/108 + a0**2*a3*a4/36 - 10*a0**2*a3*a5**3/243 - 5*a0**2*a3*a5**2*a6/27 + a0**2*a3*a5**2/18 + 8*a0**2*a4**4/6561 + 4*a0**2*a4**3*a5/2187 + 4*a0**2*a4**3*a6/243 - 4*a0**2*a4**3/729 - 2*a0**2*a4**2*a5**2/729 - a0**2*a4**2*a5*a6/81 + 2*a0*a1**2*a3**3/81 + 2*a0*a1**2*a3**2*a4/81 + a0*a1**2*a3**2*a5/27 + a0*a1**2*a3**2*a6/6 - a0*a1**2*a3*a4*a5/9 + a0*a1**2*a4**3/27 - 4*a0*a1*a2**2*a3**2/3 - 2*a0*a1*a2*a3**2*a4/27 + 28*a0*a1*a2*a3**2*a5/81 + 14*a0*a1*a2*a3**2*a6/9 - 8*a0*a1*a2*a3**2/27 - 46*a0*a1*a2*a3*a4**2/243 - 17*a0*a1*a2*a3*a4*a5/81 - 19*a0*a1*a2*a3*a4*a6/18 + 11*a0*a1*a2*a3*a4/36 - 2*a0*a1*a2*a4**3/81 - a0*a1*a2*a4**2*a5/27 - 34*a0*a1*a3**2*a5*a6/243 + 7*a0*a1*a3**2*a5/81 - 2*a0*a1*a3**2*a6/27 + 2*a0*a1*a3**2/81 - 2*a0*a1*a3*a4**2/243 - 8*a0*a1*a3*a4*a5**2/729 - 14*a0*a1*a3*a4*a5*a6/81 + 17*a0*a1*a3*a4*a5/243 + 2*a0*a1*a3*a4*a6**2/27 - 2*a0*a1*a3*a4*a6/81 - a0*a1*a3*a4/162 - 17*a0*a1*a3*a5**2*a6/81 + 17*a0*a1*a3*a5**2/162 - 11*a0*a1*a3*a5*a6**2/18 + 7*a0*a1*a3*a5*a6/12 - a0*a1*a3*a5/9 + 4*a0*a1*a4**3*a5/729 + 8*a0*a1*a4**3*a6/729 + 4*a0*a1*a4**2*a5**2/729 + 10*a0*a1*a4**2*a5*a6/243 - a0*a1*a4**2*a5/81 - 4*a0*a1*a4**2*a6**2/27 + 2*a0*a1*a4**2*a6/27 - a0*a1*a4**2/54 - 2*a0*a1*a4*a5**3/243 - a0*a1*a4*a5**2/108 - 2*a0*a2**3*a3**2/3 - a0*a2**3*a3*a4/9 - 4*a0*a2**2*a3**2*a5/27 + 4*a0*a2**2*a3**2*a6/9 - 4*a0*a2**2*a3**2/27 + 4*a0*a2**2*a3*a4**2/729 - 44*a0*a2**2*a3*a4*a5/243 - 4*a0*a2**2*a3*a4*a6/27 + 11*a0*a2**2*a3*a4/162 - 8*a0*a2**2*a3*a5**2/27 - a0*a2**2*a3*a5*a6/3 + 17*a0*a2**2*a3*a5/27 - 2*a0*a2**2*a4**2*a5/81 + 2*a0*a2**2*a4**2*a6/27 - 43*a0*a2**2*a4**2/162 - 2*a0*a2**2*a4*a5**2/27 - 14*a0*a2*a3**2*a6**2/27 + 98*a0*a2*a3**2*a6/243 - 73*a0*a2*a3**2/1458 - 8*a0*a2*a3*a4*a5*a6/243 - 47*a0*a2*a3*a4*a5/729 - 10*a0*a2*a3*a4*a6**2/27 + 47*a0*a2*a3*a4*a6/243 - 8*a0*a2*a3*a4/729 - 4*a0*a2*a3*a5**3/729 - 4*a0*a2*a3*a5**2*a6/27 - 44*a0*a2*a3*a5**2/729 - 5*a0*a2*a3*a5*a6**2/3 + 16*a0*a2*a3*a5*a6/27 - 11*a0*a2*a3*a5/324 - 5*a0*a2*a3*a6**3/6 + 7*a0*a2*a3*a6**2/3 - 193*a0*a2*a3*a6/216 + 7*a0*a2*a3/72 - 8*a0*a2*a4**3*a6/2187 + 140*a0*a2*a4**3/6561 + 4*a0*a2*a4**2*a5**2/729 + 4*a0*a2*a4**2*a5*a6/729 + 70*a0*a2*a4**2*a5/2187 + 2*a0*a2*a4**2*a6**2/81 + 41*a0*a2*a4**2*a6/243 - 25*a0*a2*a4**2/729 + 4*a0*a2*a4*a5**3/729 + 2*a0*a2*a4*a5**2*a6/81 - 43*a0*a2*a4*a5**2/1458 - 2*a0*a2*a4*a5*a6**2/27 - 65*a0*a2*a4*a5*a6/162 + 5*a0*a2*a4*a5/54 - 2*a0*a2*a5**4/243 - a0*a2*a5**3*a6/27 + a0*a2*a5**3/18 - 28*a0*a3*a4*a6**3/243 - 16*a0*a3*a4*a6**2/243 + 17*a0*a3*a4*a6/243 - 7*a0*a3*a4/729 + 4*a0*a3*a5**2*a6**2/729 - 4*a0*a3*a5**2*a6/729 - 5*a0*a3*a5**2/1458 - 20*a0*a3*a5*a6**3/81 - 16*a0*a3*a5*a6**2/243 + 7*a0*a3*a5*a6/81 - 7*a0*a3*a5/486 - 16*a0*a3*a6**4/9 + 26*a0*a3*a6**3/27 - 11*a0*a3*a6**2/162 - 13*a0*a3*a6/324 + a0*a3/162 - 4*a0*a4**2*a5*a6**2/2187 + 76*a0*a4**2*a5*a6/2187 - 2*a0*a4**2*a5/243 - 8*a0*a4**2*a6**3/243 - 20*a0*a4**2*a6**2/729 + 4*a0*a4**2*a6/243 + 4*a0*a4*a5**3*a6/2187 - 13*a0*a4*a5**3/2187 + 4*a0*a4*a5**2*a6**2/243 + 49*a0*a4*a5**2*a6/729 - 4*a0*a4*a5**2/243 + 2*a0*a4*a5*a6**3/27 + 31*a0*a4*a5*a6**2/243 - 25*a0*a4*a5*a6/486 + a0*a4*a5/162 + a0*a4*a6**4/9 - 11*a0*a4*a6**3/27 + 37*a0*a4*a6**2/108 - 11*a0*a4*a6/108 + a0*a4/108 - 8*a0*a5**4/729 - 4*a0*a5**3*a6**2/243 - 2*a0*a5**3*a6/81 + a0*a5**3/324 - 2*a0*a5**2*a6**3/27 + 2*a0*a5**2*a6**2/27 - a0*a5**2*a6/24 + a0*a5**2/108 + a1**3*a2*a3**2/2 + 4*a1**3*a3**2*a4/81 - 4*a1**3*a3**2*a5/27 - 2*a1**3*a3**2*a6/3 + a1**3*a3**2/9 + 8*a1**3*a3*a4**2/81 + 4*a1**3*a3*a4*a5/27 - a1**3*a3*a5**2/6 + a1**3*a4**2*a5/9 + a1**2*a2**2*a3**2/3 + a1**2*a2**2*a3*a4/3 + 4*a1**2*a2*a3**2*a5/27 - 2*a1**2*a2*a3**2*a6/9 + a1**2*a2*a3**2/9 + 14*a1**2*a2*a3*a4*a5/81 + 4*a1**2*a2*a3*a4*a6/9 - 4*a1**2*a2*a3*a4/27 + 10*a1**2*a2*a3*a5**2/27 - 7*a1**2*a2*a3*a5*a6/6 - 7*a1**2*a2*a3*a5/12 - 2*a1**2*a2*a4**2*a5/27 + a1**2*a2*a4**2*a6/9 + 5*a1**2*a2*a4**2/18 + 2*a1**2*a2*a4*a5**2/9 - 16*a1**2*a3**2*a6**2/81 + 2*a1**2*a3**2*a6/9 - 14*a1**2*a3**2/243 + 14*a1**2*a3*a4*a5/243 - 40*a1**2*a3*a4*a6**2/81 + 8*a1**2*a3*a4*a6/27 - 11*a1**2*a3*a4/243 - 2*a1**2*a3*a5**3/243 + 2*a1**2*a3*a5**2*a6/27 + 19*a1**2*a3*a5**2/243 + 10*a1**2*a3*a5*a6**2/27 + 8*a1**2*a3*a5*a6/27 - a1**2*a3*a5/9 - 4*a1**2*a3*a6**3/3 + 2*a1**2*a3*a6**2 - 8*a1**2*a3*a6/9 + a1**2*a3/9 - 40*a1**2*a4**3/2187 + 4*a1**2*a4**2*a5**2/729 + 8*a1**2*a4**2*a5*a6/243 - 20*a1**2*a4**2*a5/729 - 4*a1**2*a4**2*a6/27 + 8*a1**2*a4**2/243 - 2*a1**2*a4*a5**2*a6/81 + 7*a1**2*a4*a5**2/243 - 2*a1**2*a4*a5*a6**2/9 + 2*a1**2*a4*a5*a6/27 - a1**2*a4*a5/36 + a1**2*a5**3*a6/9 - a1**2*a5**3/108 - 2*a1*a2**3*a3*a4/9 + 17*a1*a2**3*a3*a5/18 - a1*a2**3*a4**2/27 + 52*a1*a2**2*a3**2*a6/81 - 74*a1*a2**2*a3**2/243 + 8*a1*a2**2*a3*a4*a5/243 + 64*a1*a2**2*a3*a4*a6/81 - 56*a1*a2**2*a3*a4/243 + 8*a1*a2**2*a3*a5**2/243 + 2*a1*a2**2*a3*a5*a6 - 73*a1*a2**2*a3*a5/162 + 3*a1*a2**2*a3*a6**2/2 - 65*a1*a2**2*a3*a6/9 + 29*a1*a2**2*a3/18 - 8*a1*a2**2*a4**3/2187 - 4*a1*a2**2*a4**2*a5/729 - 10*a1*a2**2*a4**2*a6/81 - 8*a1*a2**2*a4**2/243 - 34*a1*a2**2*a4*a5**2/243 + 13*a1*a2**2*a4*a5*a6/27 + 53*a1*a2**2*a4*a5/108 + 4*a1*a2**2*a5**3/27 + 16*a1*a2*a3*a4*a6**2/81 + 182*a1*a2*a3*a4*a6/729 - 22*a1*a2*a3*a4/243 - 20*a1*a2*a3*a5**2*a6/243 + 5*a1*a2*a3*a5**2/243 + 4*a1*a2*a3*a5*a6**2/81 + 5*a1*a2*a3*a5*a6/9 - 5*a1*a2*a3*a5/54 + 26*a1*a2*a3*a6**3/9 + 13*a1*a2*a3*a6**2/27 - 11*a1*a2*a3*a6/18 + 5*a1*a2*a3/54 - 4*a1*a2*a4**2*a5*a6/729 - 70*a1*a2*a4**2*a5/2187 + 8*a1*a2*a4**2*a6**2/243 + 20*a1*a2*a4**2*a6/729 - 2*a1*a2*a4**2/81 + 8*a1*a2*a4*a5**3/729 + 4*a1*a2*a4*a5**2*a6/81 - 40*a1*a2*a4*a5**2/729 - 8*a1*a2*a4*a5*a6**2/81 - 47*a1*a2*a4*a5*a6/243 + 8*a1*a2*a4*a5/243 - 2*a1*a2*a4*a6**3/9 - 40*a1*a2*a4*a6**2/27 + 7*a1*a2*a4*a6/12 - a1*a2*a4/18 - 8*a1*a2*a5**3*a6/81 + 29*a1*a2*a5**3/486 + 7*a1*a2*a5**2*a6**2/9 + 29*a1*a2*a5**2*a6/108 - 17*a1*a2*a5**2/108 - 4*a1*a3*a5*a6**3/243 + 8*a1*a3*a5*a6**2/243 - 25*a1*a3*a5*a6/729 + a1*a3*a5/81 + 4*a1*a3*a6**3/27 - 7*a1*a3*a6**2/81 + a1*a3*a6/54 - a1*a3/486 + 16*a1*a4**2*a6**3/729 + 64*a1*a4**2*a6**2/729 - 82*a1*a4**2*a6/2187 + 8*a1*a4**2/2187 - 4*a1*a4*a5**2*a6**2/243 - 64*a1*a4*a5**2*a6/2187 + 14*a1*a4*a5**2/2187 + 44*a1*a4*a5*a6**2/243 - 71*a1*a4*a5*a6/729 + 13*a1*a4*a5/729 + 8*a1*a4*a6**4/27 + 40*a1*a4*a6**3/81 - 11*a1*a4*a6**2/27 + 26*a1*a4*a6/243 - 5*a1*a4/486 + 4*a1*a5**4*a6/729 - a1*a5**4/2187 + 4*a1*a5**3*a6**2/243 - 43*a1*a5**3*a6/729 + 23*a1*a5**3/1458 - 14*a1*a5**2*a6**3/81 - 5*a1*a5**2*a6**2/81 + 4*a1*a5**2*a6/81 - a1*a5**2/324 + 5*a1*a5*a6**4/9 - 4*a1*a5*a6**3/9 + a1*a5*a6**2/54 + 13*a1*a5*a6/216 - a1*a5/72 - 14*a2**4*a3**2/81 - 14*a2**4*a3*a4/81 - 28*a2**4*a3*a5/27 - a2**4*a3*a6/6 + 31*a2**4*a3/9 + 2*a2**4*a4**2/27 + 2*a2**4*a4*a5/27 - 8*a2**3*a3*a4*a6/243 - 148*a2**3*a3*a4/729 + 46*a2**3*a3*a5**2/729 + 10*a2**3*a3*a5*a6/27 - 139*a2**3*a3*a5/243 - 5*a2**3*a3*a6**2/3 - 14*a2**3*a3*a6/27 + 25*a2**3*a3/162 - 20*a2**3*a4**2*a5/2187 - 8*a2**3*a4**2*a6/243 + 4*a2**3*a4**2/81 - 4*a2**3*a4*a5**2/729 - 14*a2**3*a4*a5*a6/81 + 5*a2**3*a4*a5/486 + a2**3*a4*a6**2/3 + 35*a2**3*a4*a6/18 - 65*a2**3*a4/108 - 22*a2**3*a5**3/243 + a2**3*a5**2*a6/3 + 4*a2**3*a5**2/27 + 14*a2**2*a3*a5*a6**2/243 + 32*a2**2*a3*a5*a6/729 - 41*a2**2*a3*a5/486 + 2*a2**2*a3*a6**3/3 - a2**2*a3*a6**2 + 4*a2**2*a3*a6/9 - 37*a2**2*a3/486 - 8*a2**2*a4**2*a6**2/729 - 32*a2**2*a4**2*a6/243 + 92*a2**2*a4**2/2187 - 8*a2**2*a4*a5**2*a6/2187 - 23*a2**2*a4*a5**2/2187 + 4*a2**2*a4*a5*a6**2/81 - 49*a2**2*a4*a5*a6/729 - 8*a2**2*a4*a5/729 - 10*a2**2*a4*a6**3/27 - 53*a2**2*a4*a6**2/81 + 67*a2**2*a4*a6/162 - 23*a2**2*a4/486 + 16*a2**2*a5**4/2187 + 16*a2**2*a5**3*a6/729 - 10*a2**2*a5**3/243 - 2*a2**2*a5**2*a6**2/3 + 181*a2**2*a5**2*a6/486 - 97*a2**2*a5**2/972 + 11*a2**2*a5*a6**3/9 + 55*a2**2*a5*a6**2/27 - 359*a2**2*a5*a6/216 + a2**2*a5/4 - 4*a2*a3*a6**4/81 + 74*a2*a3*a6**3/243 - 305*a2*a3*a6**2/729 + 239*a2*a3*a6/1458 - 25*a2*a3/1458 - 4*a2*a4*a5*a6**3/81 - 314*a2*a4*a5*a6**2/2187 + 215*a2*a4*a5*a6/2187 - 28*a2*a4*a5/2187 + 8*a2*a4*a6**4/81 + 8*a2*a4*a6**3/243 - 86*a2*a4*a6**2/729 + 7*a2*a4*a6/243 + 8*a2*a5**3*a6**2/243 - 19*a2*a5**3*a6/2187 - a2*a5**3/243 + 8*a2*a5**2*a6**3/81 - 221*a2*a5**2*a6**2/729 + 65*a2*a5**2*a6/486 - 7*a2*a5**2/1458 - 38*a2*a5*a6**4/27 + 20*a2*a5*a6**3/27 - a2*a5*a6**2/9 + 19*a2*a5*a6/486 - 7*a2*a5/972 + a2*a6**5 + 35*a2*a6**4/18 - 89*a2*a6**3/27 + 43*a2*a6**2/27 - 35*a2*a6/108 + 5*a2/216 - 16*a4*a6**5/243 - 32*a4*a6**4/729 + 50*a4*a6**3/729 - 13*a4*a6**2/729 + a4*a6/729 + 8*a5**2*a6**4/243 - 8*a5**2*a6**3/243 + a5**2*a6**2/81 - 2*a5**2*a6/729 + 8*a5*a6**5/81 - 80*a5*a6**4/243 + 7*a5*a6**3/27 - 37*a5*a6**2/486 + 2*a5*a6/243 - 8*a6**6/9 + 16*a6**5/27 + 7*a6**4/81 - 23*a6**3/162 + a6**2/27 - a6/324",
      "a0**3*a3**2*a5/6 - a0**3*a3*a4**2/18 - a0**2*a1*a3**2*a5/9 + 4*a0**2*a1*a3**2*a6/3 - 5*a0**2*a1*a3**2/18 + a0**2*a1*a3*a4**2/27 - 5*a0**2*a1*a3*a4*a5/27 + a0**2*a1*a4**3/81 + 5*a0**2*a2**2*a3**2/6 + 4*a0**2*a2*a3**3/243 + 4*a0**2*a2*a3**2*a4/243 + 8*a0**2*a2*a3**2*a5/81 - 7*a0**2*a2*a3**2*a6/9 + 5*a0**2*a2*a3**2/27 - 2*a0**2*a2*a3*a4**2/81 + 4*a0**2*a2*a3*a4*a5/81 + 17*a0**2*a2*a3*a4*a6/18 - 7*a0**2*a2*a3*a4/54 - 5*a0**2*a2*a3*a5**2/27 + 4*a0**2*a2*a4**3/243 + 2*a0**2*a2*a4**2*a5/81 - 4*a0**2*a3**2*a4*a6/243 + 2*a0**2*a3**2*a4/2187 + 28*a0**2*a3**2*a5**2/2187 + 20*a0**2*a3**2*a5*a6/243 - 2*a0**2*a3**2*a5/729 + 16*a0**2*a3**2*a6**2/27 - 20*a0**2*a3**2*a6/81 + 7*a0**2*a3**2/243 + 4*a0**2*a3*a4**2*a5/6561 - 32*a0**2*a3*a4**2*a6/729 + 4*a0**2*a3*a4**2/2187 + 8*a0**2*a3*a4*a5**2/729 - 10*a0**2*a3*a4*a5*a6/81 + 13*a0**2*a3*a4*a5/729 - 11*a0**2*a3*a4*a6**2/27 + 29*a0**2*a3*a4*a6/162 - a0**2*a3*a4/54 + 20*a0**2*a3*a5**3/729 + 10*a0**2*a3*a5**2*a6/81 - a0**2*a3*a5**2/27 + a0**2*a3*a5*a6**2/3 - a0**2*a3*a5*a6/9 + a0**2*a3*a5/108 - 16*a0**2*a4**4/19683 - 8*a0**2*a4**3*a5/6561 - 8*a0**2*a4**3*a6/729 + 8*a0**2*a4**3/2187 + 4*a0**2*a4**2*a5**2/2187 + 2*a0**2*a4**2*a5*a6/243 - a0**2*a4**2*a6**2/9 + a0**2*a4**2*a6/54 - a0**2*a4**2/81 + a0**2*a4*a5**2*a6/27 + a0**2*a4*a5**2/324 - 8*a0*a1**2*a2*a3**2/3 - 4*a0*a1**2*a3**3/243 - 4*a0*a1**2*a3**2*a4/243 - 2*a0*a1**2*a3**2*a5/81 - a0*a1**2*a3**2*a6/9 + 2*a0*a1**2*a3*a4*a5/27 - 7*a0*a1**2*a3*a4*a6/9 + a0*a1**2*a3*a4/6 - a0*a1**2*a3*a5**2/6 - 2*a0*a1**2*a4**3/81 + a0*a1**2*a4**2*a5/27 + 8*a0*a1*a2**2*a3**2/9 - 19*a0*a1*a2**2*a3*a4/18 + 4*a0*a1*a2*a3**2*a4/81 - 56*a0*a1*a2*a3**2*a5/243 - 28*a0*a1*a2*a3**2*a6/27 + 16*a0*a1*a2*a3**2/81 + 92*a0*a1*a2*a3*a4**2/729 + 34*a0*a1*a2*a3*a4*a5/243 + 19*a0*a1*a2*a3*a4*a6/27 - 11*a0*a1*a2*a3*a4/54 - 23*a0*a1*a2*a3*a5*a6/18 + 37*a0*a1*a2*a3*a5/54 + 4*a0*a1*a2*a4**3/243 + 2*a0*a1*a2*a4**2*a5/81 + 4*a0*a1*a2*a4**2*a6/27 - 13*a0*a1*a2*a4**2/162 + a0*a1*a2*a4*a5**2/9 + 68*a0*a1*a3**2*a5*a6/729 - 14*a0*a1*a3**2*a5/243 + 4*a0*a1*a3**2*a6/81 - 4*a0*a1*a3**2/243 + 4*a0*a1*a3*a4**2/729 + 16*a0*a1*a3*a4*a5**2/2187 + 28*a0*a1*a3*a4*a5*a6/243 - 34*a0*a1*a3*a4*a5/729 - 4*a0*a1*a3*a4*a6**2/81 + 4*a0*a1*a3*a4*a6/243 + a0*a1*a3*a4/243 + 34*a0*a1*a3*a5**2*a6/243 - 17*a0*a1*a3*a5**2/243 + 11*a0*a1*a3*a5*a6**2/27 - 7*a0*a1*a3*a5*a6/18 + 2*a0*a1*a3*a5/27 + 8*a0*a1*a3*a6**3/3 - 2*a0*a1*a3*a6**2/9 - 4*a0*a1*a3*a6/9 + a0*a1*a3/12 - 8*a0*a1*a4**3*a5/2187 - 16*a0*a1*a4**3*a6/2187 - 8*a0*a1*a4**2*a5**2/2187 - 20*a0*a1*a4**2*a5*a6/729 + 2*a0*a1*a4**2*a5/243 + 8*a0*a1*a4**2*a6**2/81 - 4*a0*a1*a4**2*a6/81 + a0*a1*a4**2/81 + 4*a0*a1*a4*a5**3/729 + a0*a1*a4*a5**2/162 - 5*a0*a1*a4*a5*a6**2/27 - a0*a1*a4*a5*a6/3 + a0*a1*a4*a5/27 + a0*a1*a5**3*a6/9 + 7*a0*a1*a5**3/108 + 4*a0*a2**3*a3**2/9 + 2*a0*a2**3*a3*a4/27 - a0*a2**3*a3*a5/6 - a0*a2**3*a4**2/9 + 8*a0*a2**2*a3**2*a5/81 - 8*a0*a2**2*a3**2*a6/27 + 8*a0*a2**2*a3**2/81 - 8*a0*a2**2*a3*a4**2/2187 + 88*a0*a2**2*a3*a4*a5/729 + 8*a0*a2**2*a3*a4*a6/81 - 11*a0*a2**2*a3*a4/243 + 16*a0*a2**2*a3*a5**2/81 + 2*a0*a2**2*a3*a5*a6/9 - 34*a0*a2**2*a3*a5/81 - 2*a0*a2**2*a3*a6**2 - a0*a2**2*a3*a6/9 + 65*a0*a2**2*a3/216 + 4*a0*a2**2*a4**2*a5/243 - 4*a0*a2**2*a4**2*a6/81 + 43*a0*a2**2*a4**2/243 + 4*a0*a2**2*a4*a5**2/81 + 2*a0*a2**2*a4*a5*a6/9 + 53*a0*a2**2*a4*a5/324 + a0*a2**2*a5**3/9 + 28*a0*a2*a3**2*a6**2/81 - 196*a0*a2*a3**2*a6/729 + 73*a0*a2*a3**2/2187 + 16*a0*a2*a3*a4*a5*a6/729 + 94*a0*a2*a3*a4*a5/2187 + 20*a0*a2*a3*a4*a6**2/81 - 94*a0*a2*a3*a4*a6/729 + 16*a0*a2*a3*a4/2187 + 8*a0*a2*a3*a5**3/2187 + 8*a0*a2*a3*a5**2*a6/81 + 88*a0*a2*a3*a5**2/2187 + 10*a0*a2*a3*a5*a6**2/9 - 32*a0*a2*a3*a5*a6/81 + 11*a0*a2*a3*a5/486 + 5*a0*a2*a3*a6**3/9 - 14*a0*a2*a3*a6**2/9 + 193*a0*a2*a3*a6/324 - 7*a0*a2*a3/108 + 16*a0*a2*a4**3*a6/6561 - 280*a0*a2*a4**3/19683 - 8*a0*a2*a4**2*a5**2/2187 - 8*a0*a2*a4**2*a5*a6/2187 - 140*a0*a2*a4**2*a5/6561 - 4*a0*a2*a4**2*a6**2/243 - 82*a0*a2*a4**2*a6/729 + 50*a0*a2*a4**2/2187 - 8*a0*a2*a4*a5**3/2187 - 4*a0*a2*a4*a5**2*a6/243 + 43*a0*a2*a4*a5**2/2187 + 4*a0*a2*a4*a5*a6**2/81 + 65*a0*a2*a4*a5*a6/243 - 5*a0*a2*a4*a5/81 + 4*a0*a2*a4*a6**3/9 - 49*a0*a2*a4*a6**2/54 + a0*a2*a4*a6/3 - 4*a0*a2*a4/81 + 4*a0*a2*a5**4/729 + 2*a0*a2*a5**3*a6/81 - a0*a2*a5**3/27 + 16*a0*a2*a5**2*a6**2/27 + 5*a0*a2*a5**2*a6/108 - 55*a0*a2*a5**2/648 + 56*a0*a3*a4*a6**3/729 + 32*a0*a3*a4*a6**2/729 - 34*a0*a3*a4*a6/729 + 14*a0*a3*a4/2187 - 8*a0*a3*a5**2*a6**2/2187 + 8*a0*a3*a5**2*a6/2187 + 5*a0*a3*a5**2/2187 + 40*a0*a3*a5*a6**3/243 + 32*a0*a3*a5*a6**2/729 - 14*a0*a3*a5*a6/243 + 7*a0*a3*a5/729 + 32*a0*a3*a6**4/27 - 52*a0*a3*a6**3/81 + 11*a0*a3*a6**2/243 + 13*a0*a3*a6/486 - a0*a3/243 + 8*a0*a4**2*a5*a6**2/6561 - 152*a0*a4**2*a5*a6/6561 + 4*a0*a4**2*a5/729 + 16*a0*a4**2*a6**3/729 + 40*a0*a4**2*a6**2/2187 - 8*a0*a4**2*a6/729 - 8*a0*a4*a5**3*a6/6561 + 26*a0*a4*a5**3/6561 - 8*a0*a4*a5**2*a6**2/729 - 98*a0*a4*a5**2*a6/2187 + 8*a0*a4*a5**2/729 - 4*a0*a4*a5*a6**3/81 - 62*a0*a4*a5*a6**2/729 + 25*a0*a4*a5*a6/729 - a0*a4*a5/243 - 2*a0*a4*a6**4/27 + 22*a0*a4*a6**3/81 - 37*a0*a4*a6**2/162 + 11*a0*a4*a6/162 - a0*a4/162 + 16*a0*a5**4/2187 + 8*a0*a5**3*a6**2/729 + 4*a0*a5**3*a6/243 - a0*a5**3/486 + 4*a0*a5**2*a6**3/81 - 4*a0*a5**2*a6**2/81 + a0*a5**2*a6/36 - a0*a5**2/162 + 2*a0*a5*a6**4/3 - 4*a0*a5*a6**3/9 + a0*a5*a6**2/108 + 7*a0*a5*a6/216 - a0*a5/216 + a1**4*a3**2 - a1**3*a2*a3**2/3 + 2*a1**3*a2*a3*a4/3 - 8*a1**3*a3**2*a4/243 + 8*a1**3*a3**2*a5/81 + 4*a1**3*a3**2*a6/9 - 2*a1**3*a3**2/27 - 16*a1**3*a3*a4**2/243 - 8*a1**3*a3*a4*a5/81 + a1**3*a3*a5**2/9 - a1**3*a3*a5*a6 - 5*a1**3*a3*a5/18 - 2*a1**3*a4**2*a5/27 + 4*a1**3*a4**2/27 - 2*a1**2*a2**2*a3**2/9 - 2*a1**2*a2**2*a3*a4/9 + 17*a1**2*a2**2*a3*a5/18 + 2*a1**2*a2**2*a4**2/27 - 8*a1**2*a2*a3**2*a5/81 + 4*a1**2*a2*a3**2*a6/27 - 2*a1**2*a2*a3**2/27 - 28*a1**2*a2*a3*a4*a5/243 - 8*a1**2*a2*a3*a4*a6/27 + 8*a1**2*a2*a3*a4/81 - 20*a1**2*a2*a3*a5**2/81 + 7*a1**2*a2*a3*a5*a6/9 + 7*a1**2*a2*a3*a5/18 - 17*a1**2*a2*a3*a6**2/3 - a1**2*a2*a3*a6 + 5*a1**2*a2*a3/12 + 4*a1**2*a2*a4**2*a5/81 - 2*a1**2*a2*a4**2*a6/27 - 5*a1**2*a2*a4**2/27 - 4*a1**2*a2*a4*a5**2/27 + a1**2*a2*a4*a5*a6/9 + 11*a1**2*a2*a4*a5/27 + 32*a1**2*a3**2*a6**2/243 - 4*a1**2*a3**2*a6/27 + 28*a1**2*a3**2/729 - 28*a1**2*a3*a4*a5/729 + 80*a1**2*a3*a4*a6**2/243 - 16*a1**2*a3*a4*a6/81 + 22*a1**2*a3*a4/729 + 4*a1**2*a3*a5**3/729 - 4*a1**2*a3*a5**2*a6/81 - 38*a1**2*a3*a5**2/729 - 20*a1**2*a3*a5*a6**2/81 - 16*a1**2*a3*a5*a6/81 + 2*a1**2*a3*a5/27 + 8*a1**2*a3*a6**3/9 - 4*a1**2*a3*a6**2/3 + 16*a1**2*a3*a6/27 - 2*a1**2*a3/27 + 80*a1**2*a4**3/6561 - 8*a1**2*a4**2*a5**2/2187 - 16*a1**2*a4**2*a5*a6/729 + 40*a1**2*a4**2*a5/2187 + 8*a1**2*a4**2*a6/81 - 16*a1**2*a4**2/729 + 4*a1**2*a4*a5**2*a6/243 - 14*a1**2*a4*a5**2/729 + 4*a1**2*a4*a5*a6**2/27 - 4*a1**2*a4*a5*a6/81 + a1**2*a4*a5/54 - 4*a1**2*a4*a6**3/9 - 2*a1**2*a4*a6**2/3 + 17*a1**2*a4*a6/54 - a1**2*a4/36 - 2*a1**2*a5**3*a6/27 + a1**2*a5**3/162 + 2*a1**2*a5**2*a6**2/9 + 11*a1**2*a5**2*a6/54 - 5*a1**2*a5**2/54 + 4*a1*a2**3*a3*a4/27 - 17*a1*a2**3*a3*a5/27 + 16*a1*a2**3*a3*a6/3 + 25*a1*a2**3*a3/18 + 2*a1*a2**3*a4**2/81 + a1*a2**3*a4*a5/9 - 104*a1*a2**2*a3**2*a6/243 + 148*a1*a2**2*a3**2/729 - 16*a1*a2**2*a3*a4*a5/729 - 128*a1*a2**2*a3*a4*a6/243 + 112*a1*a2**2*a3*a4/729 - 16*a1*a2**2*a3*a5**2/729 - 4*a1*a2**2*a3*a5*a6/3 + 73*a1*a2**2*a3*a5/243 - a1*a2**2*a3*a6**2 + 130*a1*a2**2*a3*a6/27 - 29*a1*a2**2*a3/27 + 16*a1*a2**2*a4**3/6561 + 8*a1*a2**2*a4**2*a5/2187 + 20*a1*a2**2*a4**2*a6/243 + 16*a1*a2**2*a4**2/729 + 68*a1*a2**2*a4*a5**2/729 - 26*a1*a2**2*a4*a5*a6/81 - 53*a1*a2**2*a4*a5/162 + a1*a2**2*a4*a6**2/9 + 85*a1*a2**2*a4*a6/54 - 13*a1*a2**2*a4/27 - 8*a1*a2**2*a5**3/81 + 5*a1*a2**2*a5**2*a6/27 + 8*a1*a2**2*a5**2/27 - 32*a1*a2*a3*a4*a6**2/243 - 364*a1*a2*a3*a4*a6/2187 + 44*a1*a2*a3*a4/729 + 40*a1*a2*a3*a5**2*a6/729 - 10*a1*a2*a3*a5**2/729 - 8*a1*a2*a3*a5*a6**2/243 - 10*a1*a2*a3*a5*a6/27 + 5*a1*a2*a3*a5/81 - 52*a1*a2*a3*a6**3/27 - 26*a1*a2*a3*a6**2/81 + 11*a1*a2*a3*a6/27 - 5*a1*a2*a3/81 + 8*a1*a2*a4**2*a5*a6/2187 + 140*a1*a2*a4**2*a5/6561 - 16*a1*a2*a4**2*a6**2/729 - 40*a1*a2*a4**2*a6/2187 + 4*a1*a2*a4**2/243 - 16*a1*a2*a4*a5**3/2187 - 8*a1*a2*a4*a5**2*a6/243 + 80*a1*a2*a4*a5**2/2187 + 16*a1*a2*a4*a5*a6**2/243 + 94*a1*a2*a4*a5*a6/729 - 16*a1*a2*a4*a5/729 + 4*a1*a2*a4*a6**3/27 + 80*a1*a2*a4*a6**2/81 - 7*a1*a2*a4*a6/18 + a1*a2*a4/27 + 16*a1*a2*a5**3*a6/243 - 29*a1*a2*a5**3/729 - 14*a1*a2*a5**2*a6**2/27 - 29*a1*a2*a5**2*a6/162 + 17*a1*a2*a5**2/162 + 11*a1*a2*a5*a6**3/9 + 26*a1*a2*a5*a6**2/27 - 26*a1*a2*a5*a6/27 + 29*a1*a2*a5/216 + 8*a1*a3*a5*a6**3/729 - 16*a1*a3*a5*a6**2/729 + 50*a1*a3*a5*a6/2187 - 2*a1*a3*a5/243 - 8*a1*a3*a6**3/81 + 14*a1*a3*a6**2/243 - a1*a3*a6/81 + a1*a3/729 - 32*a1*a4**2*a6**3/2187 - 128*a1*a4**2*a6**2/2187 + 164*a1*a4**2*a6/6561 - 16*a1*a4**2/6561 + 8*a1*a4*a5**2*a6**2/729 + 128*a1*a4*a5**2*a6/6561 - 28*a1*a4*a5**2/6561 - 88*a1*a4*a5*a6**2/729 + 142*a1*a4*a5*a6/2187 - 26*a1*a4*a5/2187 - 16*a1*a4*a6**4/81 - 80*a1*a4*a6**3/243 + 22*a1*a4*a6**2/81 - 52*a1*a4*a6/729 + 5*a1*a4/729 - 8*a1*a5**4*a6/2187 + 2*a1*a5**4/6561 - 8*a1*a5**3*a6**2/729 + 86*a1*a5**3*a6/2187 - 23*a1*a5**3/2187 + 28*a1*a5**2*a6**3/243 + 10*a1*a5**2*a6**2/243 - 8*a1*a5**2*a6/243 + a1*a5**2/486 - 10*a1*a5*a6**4/27 + 8*a1*a5*a6**3/27 - a1*a5*a6**2/81 - 13*a1*a5*a6/324 + a1*a5/108 + 4*a1*a6**5/3 - 4*a1*a6**4/9 - 11*a1*a6**3/18 + 7*a1*a6**2/18 - 17*a1*a6/216 + a1/216 - 7*a2**5*a3/6 + 28*a2**4*a3**2/243 + 28*a2**4*a3*a4/243 + 56*a2**4*a3*a5/81 + a2**4*a3*a6/9 - 62*a2**4*a3/27 - 4*a2**4*a4**2/81 - 4*a2**4*a4*a5/81 + a2**4*a4*a6/9 + a2**4*a4/6 + a2**4*a5**2/27 + 16*a2**3*a3*a4*a6/729 + 296*a2**3*a3*a4/2187 - 92*a2**3*a3*a5**2/2187 - 20*a2**3*a3*a5*a6/81 + 278*a2**3*a3*a5/729 + 10*a2**3*a3*a6**2/9 + 28*a2**3*a3*a6/81 - 25*a2**3*a3/243 + 40*a2**3*a4**2*a5/6561 + 16*a2**3*a4**2*a6/729 - 8*a2**3*a4**2/243 + 8*a2**3*a4*a5**2/2187 + 28*a2**3*a4*a5*a6/243 - 5*a2**3*a4*a5/729 - 2*a2**3*a4*a6**2/9 - 35*a2**3*a4*a6/27 + 65*a2**3*a4/162 + 44*a2**3*a5**3/729 - 2*a2**3*a5**2*a6/9 - 8*a2**3*a5**2/81 - a2**3*a5*a6**2/9 + 49*a2**3*a5*a6/54 - 7*a2**3*a5/24 - 28*a2**2*a3*a5*a6**2/729 - 64*a2**2*a3*a5*a6/2187 + 41*a2**2*a3*a5/729 - 4*a2**2*a3*a6**3/9 + 2*a2**2*a3*a6**2/3 - 8*a2**2*a3*a6/27 + 37*a2**2*a3/729 + 16*a2**2*a4**2*a6**2/2187 + 64*a2**2*a4**2*a6/729 - 184*a2**2*a4**2/6561 + 16*a2**2*a4*a5**2*a6/6561 + 46*a2**2*a4*a5**2/6561 - 8*a2**2*a4*a5*a6**2/243 + 98*a2**2*a4*a5*a6/2187 + 16*a2**2*a4*a5/2187 + 20*a2**2*a4*a6**3/81 + 106*a2**2*a4*a6**2/243 - 67*a2**2*a4*a6/243 + 23*a2**2*a4/729 - 32*a2**2*a5**4/6561 - 32*a2**2*a5**3*a6/2187 + 20*a2**2*a5**3/729 + 4*a2**2*a5**2*a6**2/9 - 181*a2**2*a5**2*a6/729 + 97*a2**2*a5**2/1458 - 22*a2**2*a5*a6**3/27 - 110*a2**2*a5*a6**2/81 + 359*a2**2*a5*a6/324 - a2**2*a5/6 - a2**2*a6**4/3 + 17*a2**2*a6**3/9 - 41*a2**2*a6**2/27 + 29*a2**2*a6/72 - a2**2/27 + 8*a2*a3*a6**4/243 - 148*a2*a3*a6**3/729 + 610*a2*a3*a6**2/2187 - 239*a2*a3*a6/2187 + 25*a2*a3/2187 + 8*a2*a4*a5*a6**3/243 + 628*a2*a4*a5*a6**2/6561 - 430*a2*a4*a5*a6/6561 + 56*a2*a4*a5/6561 - 16*a2*a4*a6**4/243 - 16*a2*a4*a6**3/729 + 172*a2*a4*a6**2/2187 - 14*a2*a4*a6/729 - 16*a2*a5**3*a6**2/729 + 38*a2*a5**3*a6/6561 + 2*a2*a5**3/729 - 16*a2*a5**2*a6**3/243 + 442*a2*a5**2*a6**2/2187 - 65*a2*a5**2*a6/729 + 7*a2*a5**2/2187 + 76*a2*a5*a6**4/81 - 40*a2*a5*a6**3/81 + 2*a2*a5*a6**2/27 - 19*a2*a5*a6/729 + 7*a2*a5/1458 - 2*a2*a6**5/3 - 35*a2*a6**4/27 + 178*a2*a6**3/81 - 86*a2*a6**2/81 + 35*a2*a6/162 - 5*a2/324 + 32*a4*a6**5/729 + 64*a4*a6**4/2187 - 100*a4*a6**3/2187 + 26*a4*a6**2/2187 - 2*a4*a6/2187 - 16*a5**2*a6**4/729 + 16*a5**2*a6**3/729 - 2*a5**2*a6**2/243 + 4*a5**2*a6/2187 - 16*a5*a6**5/243 + 160*a5*a6**4/729 - 14*a5*a6**3/81 + 37*a5*a6**2/729 - 4*a5*a6/729 + 16*a6**6/27 - 32*a6**5/81 - 14*a6**4/243 + 23*a6**3/243 - 2*a6**2/81 + a6/486"
    &#93;
  &#93;,
  "rank_identity_on_D(d)": "rank(&#91;H_u|H_v&#93;) = 5 + rank(M)",
  "kernel_reconstruction_on_D(d)": "v = -d^{-1} C A u"
}
</code></pre>

<a id="source-a0e37d2743e92c4e"></a>

## `research-notes/lane7-split-incidence-20260802-v1/lane7-split-incidence-theorem.md`

<pre><code class="language-markdown">
# Lane 7 progress: split incidence and a determinant-boundary matrix factorization

**Status:** exact characteristic-zero theorem, computer-assisted by explicit
polynomial identities over \(\mathbf Q&#91;a_0,\ldots,a_6&#93;\).  This note does not
claim the remaining corank-two exclusion, global component decomposition, or
global first-normal obstruction.

## Setup

Let
\&#91;
A_0=\mathbf Q&#91;a_0,\ldots,a_6&#93;,
\qquad d=\det T.
\&#93;
After the published normalization \(a_7=1\) and after restoring the homogeneous
marking coordinate \(v_4\), the fifteen quintics are linear in the ten marking
coordinates:
\&#91;
\Theta(a)\binom uv=0,
\qquad
u=(u_0,\ldots,u_4)^t,\quad v=(v_0,\ldots,v_4)^t.
\&#93;
The previously verified quadratic reduction writes
\&#91;
\Theta=&#91;\,\mathsf U\mid\mathsf V\,&#93;,
\qquad
\mathsf U,\mathsf V\in\operatorname{Mat}_{15\times5}(A_0).
\&#93;

Write
\&#91;
A=\mathsf U_{0:10},\quad H=\mathsf V_{0:10},
\quad B=\mathsf U_{10:15}.
\&#93;
There is a constant matrix \(L\in\operatorname{Mat}_{5\times10}(\mathbf Q)\)
such that
\&#91;
\mathsf V_{10:15}=LH.
\&#93;
Explicitly, the only nonzero entries of \(L\) are
\&#91;
L_{ii}=\frac32(1,1,-1,1,1)_i,\qquad 0\le i&lt;5.
\&#93;
Put
\&#91;
G=B-LA\in\operatorname{Mat}_{5\times5}(A_0).
\&#93;

## Theorem A — global split incidence

There is an explicit polynomial matrix
\&#91;
C_u\in\operatorname{Mat}_{5\times15}(A_0),
\qquad \deg C_u\le3,
\&#93;
such that
\&#91;
C_u\mathsf U=I_5.
\&#93;
Consequently, with
\&#91;
F=C_u\mathsf V,\qquad
\mathcal R=(I_{15}-\mathsf U C_u)\mathsf V,
\&#93;
the polynomial source change
\&#91;
(u,v)\longmapsto (u+Fv,v)
\&#93;
identifies the complete homogeneous marking incidence scheme with
\&#91;
\mathcal R(a)v=0,\qquad u=-F(a)v.
\&#93;
In particular,
\&#91;
\ker\Theta(a)\simeq\ker\mathcal R(a)
\&#93;
over every field specialization for which the displayed coefficients are
defined.

### Proof

The transformation gives
\&#91;
\mathsf Uu+\mathsf Vv
 =\mathsf U(u+Fv)+(I-\mathsf U C_u)\mathsf Vv
 =\mathsf Uu'+\mathcal Rv.
\&#93;
Applying \(C_u\) gives \(u'=0\), because
\(C_u\mathsf U=I_5\) and \(C_u\mathcal R=0\).  The remaining equation is
\(\mathcal Rv=0\), and the inverse reconstruction is \(u=-Fv\).
\(\square\)

### Consequence: a certified chart cover

A nonzero marking in \(\ker\Theta(a)\) cannot have \(v=0\), because then
\(u=-Fv=0\).  Hence the projectivized marking incidence is covered by the five
intrinsic affine charts
\&#91;
D(v_0),\ldots,D(v_4).
\&#93;
The currently published normalization \(v_4=1\) is one member of this
five-chart cover; it is not by itself a global chart.

## Theorem B — determinant-boundary matrix factorization

There are explicit matrices
\&#91;
C,Q\in\operatorname{Mat}_{5\times10}(A_0),
\qquad
R\in\operatorname{Mat}_{10\times5}(A_0)
\&#93;
with row-degree bounds
\&#91;
\deg Q_{\text{rows}}\le(3,3,5,5,5),
\qquad \deg R\le3,
\&#93;
such that
\&#91;
CH=dI_5,\qquad QH=0,\qquad CR=0,\qquad QR=dI_5
\&#93;
and
\&#91;
HC+RQ=dI_{10}.
\&#93;
Equivalently, the two square matrices
\&#91;
S=&#91;\,H\mid R\,&#93;,
\qquad
T=\begin{bmatrix}C\\Q\end{bmatrix}
\&#93;
form an exact matrix factorization
\&#91;
ST=TS=dI_{10}.
\&#93;

Therefore, over \(A_0&#91;d^{-1}&#93;\), \(H\) is a split rank-five summand of
\(A_0&#91;d^{-1}&#93;^{10}\), \(Q\) is the quotient projection, and
\&#91;
S^{-1}=d^{-1}T.
\&#93;

### Exact determinant corollary

The quartic \(d\) is irreducible over \(\mathbf Q\), and the exact identities
imply
\&#91;
\det S=-\frac{256}{243}d^2,
\qquad
\det T=-\frac{243}{256}d^8.
\&#93;
Thus the matrix factorization degenerates on precisely the determinant
boundary \(d=0\).

## Theorem C — reduction to a \(10\times5\) determinantal matrix

Define
\&#91;
M(a)=
\begin{bmatrix}
G(a)\\
Q(a)A(a)
\end{bmatrix}
\in\operatorname{Mat}_{10\times5}(A_0).
\&#93;
On the intrinsic regular open \(D(d)\), the complete fifteen-equation marking
system is scheme-theoretically equivalent to
\&#91;
M(a)u=0,
\qquad
v=-d^{-1}C(a)A(a)u.
\&#93;
Moreover,
\&#91;
\operatorname{rank}\Theta(a)
 =5+\operatorname{rank}M(a),
\qquad
\ker\Theta(a)\simeq\ker M(a).
\&#93;

### Proof

Subtracting \(L\) times the top ten equations from the bottom five turns the
system into
\&#91;
Au+Hv=0,\qquad Gu=0.
\&#93;
Multiplication of the first equation by \(C\) and \(Q\) is invertible on
\(D(d)\), by Theorem B, and gives
\&#91;
CAu+dv=0,\qquad QAu=0.
\&#93;
The first equation reconstructs \(v\); the remaining equations are exactly
\(M(a)u=0\).  The block reduction also gives the rank formula.
\(\square\)

## Determinantal consequences

The regular parameter carrier is
\&#91;
\mathcal D
 =V(I_5(M))\cap D(d).
\&#93;
Put
\&#91;
 w=C(a)A(a)u,
 \qquad
 \eta_{ij}(a,u)=u_iw_j-u_jw_i.
\&#93;
Since \(v=-d^{-1}w\), the Pluecker minors of the two recovered collision
vectors satisfy
\&#91;
 u_iv_j-u_jv_i=-d^{-1}\eta_{ij}(a,u).
\&#93;
Consequently the genuine independent-marking incidence is the open subset
\&#91;
 \left\{(a,&#91;u&#93;):M(a)u=0,\quad
 \eta_{ij}(a,u)\ne0\text{ for some }i&lt;j\right\}
 \subset \mathbf P(\ker M).
\&#93;
The determinantal carrier \(\mathcal D\) alone may contain components on
which every recovered marking is collinear; any component or obstruction
calculation must retain this Pluecker-open condition or prove that it is
generically nonempty on the components being used.

On
\&#91;
\mathcal D\setminus V(I_4(M)),
\&#93;
the kernel is a line, so the marking is unique up to scalar and is reconstructed
by the displayed formula.

The unresolved nonuniqueness locus is now exactly
\&#91;
V(I_4(M))\cap D(d).
\&#93;
Thus the former certificate
\(I_9(&#91;H_u\mid H_v&#93;):d^\infty=(1)\) is equivalent to the much smaller
certificate
\&#91;
\boxed{I_4(M):d^\infty=(1).}
\&#93;

The expected codimension of \(V(I_5(M))\) is
\&#91;
(10-4)(5-4)=6,
\&#93;
so its expected dimension in the seven-dimensional parameter space is one.
Expected dimension is not used as a proof of purity.

## Smooth characteristic-zero branch

At the published point
\&#91;
a=(8,7,1,7,2,9,0)\in\mathbf F_{11}^7
\&#93;
one has \(d=1\), \(\operatorname{rank}M=4\), and the determinantal normal map
\&#91;
T_a\mathbf A^7\longrightarrow
\operatorname{Hom}(\ker M(a),\operatorname{coker}M(a))
\&#93;
has rank six.  Hence \(V(I_5(M))\) is smooth of dimension one at this point.
The tangent line is generated by
\&#91;
(8,6,5,4,3,10,1)\pmod {11}.
\&#93;
Formal smoothness gives a one-dimensional \(\mathbf Z_{11}\)-smooth germ and
therefore a characteristic-zero component through its generic fiber.

## What remains

This theorem removes the marking variables and proves the exact determinantal
architecture.  It does **not** prove:

1. \(I_4(M):d^\infty=(1)\);
2. height six or Cohen--Macaulayness of \(I_5(M):d^\infty\);
3. the absolute component decomposition, with its Pluecker-open marking
   incidence;
4. nowhere-solvability of the first-normal equation.

The next sharp algebraic targets are therefore
\&#91;
I_4(M):d^\infty=(1)
\quad\text{and}\quad
\operatorname{grade} I_5(M)=6
\ \text{on }D(d).
\&#93;
If the grade condition holds, Eagon--Northcott makes the regular carrier a
pure Cohen--Macaulay curve before radical decomposition.
</code></pre>

<a id="source-ac804ad823e1e515"></a>

## `research-notes/lane7-split-incidence-20260802-v1/reconstruct_matrices.py`

<pre><code class="language-python">
"""Reconstruct the Lane 7 polynomial matrices from the original certificate.

This is the reconstruction helper used in the source conversation.  It is
included here, together with its four data dependencies, so that the final
split-incidence checkers are standalone rather than dependent on ephemeral
notebook state.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


BASE = Path(__file__).resolve().parent
a = sp.symbols("a0:7")
u = sp.symbols("u0:5")
v = sp.symbols("v0:5")


def _load_json(path: Path) -&gt; dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def collision_matrices():
    data = _load_json(BASE / "collision-system.json")
    local_symbols = {str(x): x for x in (*a, *u, *v)}
    equations = &#91;
        sp.sympify(entry&#91;"polynomial"&#93;, locals=local_symbols)
        for entry in data&#91;"equations"&#93;
    &#93;
    matrix_u = sp.Matrix(
        &#91;&#91;sp.expand(equation).coeff(x) for x in u&#93; for equation in equations&#93;
    )
    affine_zero = {x: 0 for x in (*u, *v&#91;:4&#93;)}
    matrix_v = sp.Matrix(
        &#91;
            &#91;sp.expand(equation).coeff(x) for x in v&#91;:4&#93;&#93;
            + &#91;sp.expand(equation).subs(affine_zero)&#93;
            for equation in equations
        &#93;
    )
    determinant = sp.sympify(
        data&#91;"chart"&#93;&#91;"open_polynomial_factors"&#93;&#91;"det_T"&#93;,
        locals={str(x): x for x in a},
    )
    return matrix_u, matrix_v, sp.expand(determinant)


def _polynomial_list(vector, monomials, polynomial_count):
    monomial_basis = &#91;
        sp.prod(a&#91;i&#93; ** exponent&#91;i&#93; for i in range(7)) for exponent in monomials
    &#93;
    coefficients = &#91;
        sp.Rational(value&#91;0&#93;, value&#91;1&#93;)
        if isinstance(value, list)
        else sp.Rational(value)
        for value in vector
    &#93;
    basis_size = len(monomial_basis)
    return &#91;
        sp.expand(
            sum(
                coefficients&#91;j * basis_size + k&#93; * monomial_basis&#91;k&#93;
                for k in range(basis_size)
            )
        )
        for j in range(polynomial_count)
    &#93;


def syzygy_matrices(filename: str, coefficient_rows: int):
    data = _load_json(BASE / filename)
    left_columns = &#91;&#93;
    right_columns = &#91;&#93;
    for vector in data&#91;"basis"&#93;:
        polynomials = _polynomial_list(
            vector, data&#91;"monomials"&#93;, coefficient_rows + 15
        )
        left_columns.append(polynomials&#91;:coefficient_rows&#93;)
        right_columns.append(polynomials&#91;coefficient_rows:&#93;)
    left = sp.Matrix(
        coefficient_rows,
        len(left_columns),
        lambda i, j: left_columns&#91;j&#93;&#91;i&#93;,
    )
    right = sp.Matrix(15, len(right_columns), lambda i, j: right_columns&#91;j&#93;&#91;i&#93;)
    return left, right


def transformed():
    matrix_u, matrix_v, determinant = collision_matrices()
    coefficient_u, transformed_u = syzygy_matrices("quadratic_syzygies.json", 9)
    assert coefficient_u&#91;5:9, :&#93; == sp.zeros(4, 5)
    coefficient_v, transformed_v = syzygy_matrices(
        "V_quadratic_syzygies.json", 5
    )
    return (
        matrix_u,
        matrix_v,
        determinant,
        coefficient_u&#91;:5, :&#93;,
        transformed_u,
        coefficient_v,
        transformed_v,
    )


def decode_coeff_matrix(path: Path):
    data = _load_json(path)
    monomial_basis = &#91;
        sp.prod(a&#91;i&#93; ** exponent&#91;i&#93; for i in range(7))
        for exponent in data&#91;"monomials"&#93;
    &#93;
    rows, columns = data&#91;"matrix_shape"&#93;
    if rows != len(data&#91;"coefficients"&#93;):
        raise ValueError("coefficient row count does not match matrix_shape")
    decoded_rows = &#91;&#93;
    basis_size = len(monomial_basis)
    for flat_row in data&#91;"coefficients"&#93;:
        coefficients = &#91;
            sp.Rational(value&#91;0&#93;, value&#91;1&#93;)
            if isinstance(value, list)
            else sp.Rational(value)
            for value in flat_row
        &#93;
        if len(coefficients) != columns * basis_size:
            raise ValueError("flattened coefficient row has the wrong length")
        decoded_rows.append(
            &#91;
                sp.expand(
                    sum(
                        coefficients&#91;j * basis_size + k&#93; * monomial_basis&#91;k&#93;
                        for k in range(basis_size)
                    )
                )
                for j in range(columns)
            &#93;
        )
    return sp.Matrix(decoded_rows)
</code></pre>

<a id="source-04ef47ee7aa0d345"></a>

## `research-notes/lane7-split-incidence-20260802-v1/verify_split_determinants.py`

<pre><code class="language-python">
from __future__ import annotations
import json,sys
from pathlib import Path
import sympy as sp
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE))
from reconstruct_matrices import transformed, decode_coeff_matrix, a
def parse_matrix(path,key='entries'):
    o=json.load(open(path));loc={str(x):x for x in a}
    return sp.Matrix(&#91;&#91;sp.sympify(s,locals=loc) for s in row&#93; for row in o&#91;key&#93;&#93;)
U,V,d,Ku,Hu,Kv,Hv=transformed()
Q=parse_matrix(BASE/'Hv10_syzygies_exact.json')
R=parse_matrix(BASE/'Hv10_right_inverse_exact.json')
Cv=decode_coeff_matrix(BASE/'Hv_left_inverse.json')
E=sp.zeros(15,10)
for i in range(10):E&#91;i,i&#93;=1
for i,sgn in enumerate(&#91;1,1,-1,1,1&#93;):E&#91;10+i,i&#93;=sp.Rational(3,2)*sgn
C=(Cv*E).applyfunc(sp.expand);H=Hv&#91;:10,:&#93;
S=H.row_join(R);T=C.col_join(Q)
assert all(sp.expand(x)==0 for x in S*T-d*sp.eye(10))
assert all(sp.expand(x)==0 for x in T*S-d*sp.eye(10))
fac=sp.factor_list(d,*a)
assert len(fac&#91;1&#93;)==1 and fac&#91;1&#93;&#91;0&#93;&#91;1&#93;==1
pts=&#91;
 &#91;1,0,0,0,0,0,1&#93;,
 &#91;1,2,3,4,5,6,7&#93;,
&#93;
vals=&#91;&#93;
for pt in pts:
 sub=dict(zip(a,pt));dv=sp.Rational(d.subs(sub))
 ds=sp.Matrix(S.subs(sub)).det();dt=sp.Matrix(T.subs(sub)).det()
 vals.append({'point':pt,'d':str(dv),'detS':str(ds),'detT':str(dt)})
possible=&#91;&#93;
for k in range(11):
 r0=sp.Rational(vals&#91;0&#93;&#91;'detS'&#93;)/sp.Rational(vals&#91;0&#93;&#91;'d'&#93;)**k
 r1=sp.Rational(vals&#91;1&#93;&#91;'detS'&#93;)/sp.Rational(vals&#91;1&#93;&#91;'d'&#93;)**k
 if r0==r1:possible.append((k,r0))
assert possible==&#91;(2,sp.Rational(-256,243))&#93;
k,c=possible&#91;0&#93;
# detS detT=d^10 from the matrix factorization.
ct=sp.cancel(1/c)
assert ct==sp.Rational(-243,256)
report={
 'd_factorization_over_Q':str(fac),
 'specializations':vals,
 'deduction':{
  'detS':str(c)+' * d^'+str(k),
  'detT':str(ct)+' * d^'+str(10-k),
  'reason':'ST=dI and irreducibility of d force both determinants to be unit multiples of powers of d; two exact specializations determine the exponent and unit.'
 }
}
(BASE/'verify_split_determinants_report.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
</code></pre>

<a id="source-386d4aff08adc8e8"></a>

## `research-notes/lane7-split-incidence-20260802-v1/verify_split_determinants_report.json`

<pre><code class="language-json">
{
  "d_factorization_over_Q": "(1, &#91;(36*a0*a2*a3*a5 - 12*a0*a2*a4**2 + 108*a0*a3*a6**2 - 54*a0*a3*a6 + 6*a0*a3 - 24*a0*a4*a5*a6 + 6*a0*a4*a5 + 4*a0*a5**3 - 36*a1**2*a3*a5 + 12*a1**2*a4**2 - 216*a1*a2*a3*a6 + 54*a1*a2*a3 + 24*a1*a2*a4*a5 - 72*a1*a4*a6**2 + 36*a1*a4*a6 - 6*a1*a4 + 24*a1*a5**2*a6 - 6*a1*a5**2 + 108*a2**3*a3 + 72*a2**2*a4*a6 - 18*a2**2*a4 + 12*a2**2*a5**2 + 108*a2*a5*a6**2 - 54*a2*a5*a6 + 3*a2*a5 + 108*a6**4 - 108*a6**3 + 33*a6**2 - 3*a6, 1)&#93;)",
  "specializations": &#91;
    {
      "point": &#91;
        1,
        0,
        0,
        0,
        0,
        0,
        1
      &#93;,
      "d": "30",
      "detS": "-25600/27",
      "detT": "-622782421875"
    },
    {
      "point": &#91;
        1,
        2,
        3,
        4,
        5,
        6,
        7
      &#93;,
      "d": "313080",
      "detS": "-2788098457600/27",
      "detT": "-87621142053138996224589238992242764800000000"
    }
  &#93;,
  "deduction": {
    "detS": "-256/243 * d^2",
    "detT": "-243/256 * d^8",
    "reason": "ST=dI and irreducibility of d force both determinants to be unit multiples of powers of d; two exact specializations determine the exponent and unit."
  }
}
</code></pre>

<a id="source-a49c880a704d2b7f"></a>

## `research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_report.json`

<pre><code class="language-json">
{
  "checks": {
    "Cu_Hu_I5": true,
    "C_H_dI5": true,
    "Q_H_0": true,
    "C_R_0": true,
    "Q_R_dI5": true,
    "H_C_plus_R_Q_dI10": true,
    "lower_v_relation": true,
    "stored_M_matches": true
  },
  "elapsed_seconds": 40.143800020217896,
  "stats": {
    "Cu": {
      "shape": &#91;
        5,
        15
      &#93;,
      "nonzero_entries": 74,
      "max_total_degree": 3,
      "monomial_terms": 4116
    },
    "H": {
      "shape": &#91;
        10,
        5
      &#93;,
      "nonzero_entries": 46,
      "max_total_degree": 2,
      "monomial_terms": 123
    },
    "C": {
      "shape": &#91;
        5,
        10
      &#93;,
      "nonzero_entries": 41,
      "max_total_degree": 4,
      "monomial_terms": 537
    },
    "Q": {
      "shape": &#91;
        5,
        10
      &#93;,
      "nonzero_entries": 43,
      "max_total_degree": 5,
      "monomial_terms": 1371
    },
    "R": {
      "shape": &#91;
        10,
        5
      &#93;,
      "nonzero_entries": 42,
      "max_total_degree": 3,
      "monomial_terms": 137
    },
    "G": {
      "shape": &#91;
        5,
        5
      &#93;,
      "nonzero_entries": 25,
      "max_total_degree": 2,
      "monomial_terms": 344
    },
    "M": {
      "shape": &#91;
        10,
        5
      &#93;,
      "nonzero_entries": 50,
      "max_total_degree": 6,
      "monomial_terms": 5575
    }
  },
  "theorem": &#91;
    "Over Q&#91;a0,...,a6,1/d&#93;, &#91;C;Q&#93; and &#91;H R&#93; are inverse up to the scalar d.",
    "The regular collision incidence is isomorphic to M(a)u=0 with v=-d^{-1}CAu.",
    "rank(&#91;Hu|Hv&#93;) = 5 + rank(M) on D(d)."
  &#93;
}
</code></pre>

<a id="source-d3702b088e5916ba"></a>

## `research-notes/lane7-split-incidence-20260802-v1/verify_split_incidence_theorem.py`

<pre><code class="language-python">
from __future__ import annotations
import json, time
from pathlib import Path
import sympy as sp
BASE=Path(__file__).resolve().parent
import sys
sys.path.insert(0,str(BASE))
from reconstruct_matrices import transformed, decode_coeff_matrix, a

def parse_matrix(path,key='entries'):
    obj=json.load(open(path))
    rows=obj&#91;key&#93;
    loc={str(x):x for x in a}
    return sp.Matrix(&#91;&#91;sp.sympify(s,locals=loc) for s in row&#93; for row in rows&#93;)

def zero(M):
    return all(sp.expand(x)==0 for x in M)

t0=time.time()
U,V,d,Ku,Hu,Kv,Hv=transformed()
Cu=decode_coeff_matrix(BASE/'Hu_left_inverse_exact.json')
Cv=decode_coeff_matrix(BASE/'Hv_left_inverse.json')
Q=parse_matrix(BASE/'Hv10_syzygies_exact.json')
R=parse_matrix(BASE/'Hv10_right_inverse_exact.json')
H=Hv&#91;:10,:&#93;
A=Hu&#91;:10,:&#93;
s=&#91;1,1,-1,1,1&#93;
E=sp.zeros(15,10)
for i in range(10): E&#91;i,i&#93;=1
for i,sgn in enumerate(s): E&#91;10+i,i&#93;=sp.Rational(3,2)*sgn
C=(Cv*E).applyfunc(sp.expand)
L=sp.zeros(5,10)
for i,sgn in enumerate(s): L&#91;i,i&#93;=sp.Rational(3,2)*sgn
G=(Hu&#91;10:,:&#93;-L*A).applyfunc(sp.expand)
M=G.col_join((Q*A).applyfunc(sp.expand))
stored=json.load(open(BASE/'collision_residual_matrix_M.json'))
Mstored=sp.Matrix(&#91;&#91;sp.sympify(x,locals={str(z):z for z in a}) for x in row&#93; for row in stored&#91;'entries'&#93;&#93;)

checks={
 'Cu_Hu_I5': zero(Cu*Hu-sp.eye(5)),
 'C_H_dI5': zero(C*H-d*sp.eye(5)),
 'Q_H_0': zero(Q*H),
 'C_R_0': zero(C*R),
 'Q_R_dI5': zero(Q*R-d*sp.eye(5)),
 'H_C_plus_R_Q_dI10': zero(H*C+R*Q-d*sp.eye(10)),
 'lower_v_relation': zero(Hv&#91;10:,:&#93;-L*H),
 'stored_M_matches': zero(M-Mstored),
}
if not all(checks.values()):
    raise SystemExit('FAILED: '+repr(checks))
def stats(X):
    vals=list(X)
    non=&#91;x for x in vals if x!=0&#93;
    return {
      'shape':&#91;X.rows,X.cols&#93;,
      'nonzero_entries':len(non),
      'max_total_degree':max((sp.Poly(x,*a).total_degree() for x in non),default=-1),
      'monomial_terms':sum(len(sp.Poly(x,*a).terms()) for x in non),
    }
report={
 'checks':checks,
 'elapsed_seconds':time.time()-t0,
 'stats':{
   'Cu':stats(Cu),'H':stats(H),'C':stats(C),'Q':stats(Q),'R':stats(R),
   'G':stats(G),'M':stats(M),
 },
 'theorem':&#91;
   'Over Q&#91;a0,...,a6,1/d&#93;, &#91;C;Q&#93; and &#91;H R&#93; are inverse up to the scalar d.',
   'The regular collision incidence is isomorphic to M(a)u=0 with v=-d^{-1}CAu.',
   'rank(&#91;Hu|Hv&#93;) = 5 + rank(M) on D(d).'
 &#93;
}
(BASE/'verify_split_incidence_report.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
</code></pre>

[Back to Lane 7](five-dimensional-collision-geometry.md)
