# Lane 7 exact research source packet

This is the public source packet for **Five-dimensional collision geometry**. It contains the
selected proof notes, exact computation contracts, and checkers used
by the concise lane brief. Read only the files relevant to the route
you pursue. Stored outputs and very large reconstructible matrices are
omitted; the mathematical boundary of each checker remains in its
source text.

Private-source commit: `43fe2294f74c961039a5b522f27a5982d511daa3`.

## Included files

- `lane7-projective-kernel-20260803-v1/README.md` — `dd5f1cff5aadb1c681823e633e2826d193ca17364833b701dccaef757a4abccd`
- `lane7-projective-kernel-20260803-v1/generate_macaulay2_input.py` — `5e417707876d39efc5f780ba95cff9f33c9f209b8b14b76a9484e70c12eaef01`
- `lane7-projective-kernel-20260803-v1/generate_kernel_chart_input.py` — `3a5c8dd3c3aa5d57f2cbb139dad970f96c7c0eaf247b7978fef4d6c3db28dc87`
- `lane7-projective-kernel-20260803-v1/generate_kernel_chart_singular.py` — `290697bd851eecc2509b09cf440966874cf51fc9c011dc1bd9fcc7fa69af5de7`
- `lane7-projective-kernel-20260803-v1/test_plucker_transport.py` — `22ca784d94dee019eee780909e1e615b6311b4e668e140847a2f8d37f6d39e30`
- `lane7-split-incidence-20260802-v1/lane7-split-incidence-theorem.md` — `3d365808d7fc3426bbe6db5aafc981e014c654b4aea623a6c13f9ccd9d8923de`
- `lane7-split-incidence-20260802-v1/reconstruct_matrices.py` — `b6bbbbec46eeffc89f1f535cfb859d3bcb1f10b1debe39217af49b7e76fd824f`
- `lane7-split-incidence-20260802-v1/verify_split_incidence_theorem.py` — `dadd947874d8b1967a39e55e39c64b4c549574d32523d0440c4cb6ef09369495`
- `lane7-split-incidence-20260802-v1/verify_split_determinants.py` — `ca1c168da85e42dc27a19bbf40c93b5e4185f19b3ecadb2899d5f1375ebc0319`
- `lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json` — `4e1a014a6616a990ac50d255fb7426a9f8ae1d06cbf5066ba52c8415da63cbda`
- `lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json` — `a251278a145ab0cfcf249809267edb2d6529738684b5136ec5faef62c7aa3dfb`
- `lane7-split-incidence-20260802-v1/verify_split_incidence_report.json` — `f0a78dce8f1f7f65a92f0d22267dfe143cc1828fbe6f2f435644276b8f505264`
- `lane7-split-incidence-20260802-v1/verify_split_determinants_report.json` — `e5b108357cbb96c0b0e979f0242dd8f6c308cd521eb7f01827a8cd8dc6ca9421`

## `lane7-projective-kernel-20260803-v1/README.md`

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
- test_plucker_transport.py checks the five Pluecker relations, all ten
  normalized two-plane charts, and the transport identity.

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
</code></pre>

## `lane7-projective-kernel-20260803-v1/generate_macaulay2_input.py`

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

## `lane7-projective-kernel-20260803-v1/generate_kernel_chart_input.py`

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

## `lane7-projective-kernel-20260803-v1/generate_kernel_chart_singular.py`

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

## `lane7-projective-kernel-20260803-v1/test_plucker_transport.py`

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

## `lane7-split-incidence-20260802-v1/lane7-split-incidence-theorem.md`

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

## `lane7-split-incidence-20260802-v1/reconstruct_matrices.py`

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

## `lane7-split-incidence-20260802-v1/verify_split_incidence_theorem.py`

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

## `lane7-split-incidence-20260802-v1/verify_split_determinants.py`

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

## `lane7-split-incidence-20260802-v1/collision_residual_matrix_M.json`

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

## `lane7-split-incidence-20260802-v1/Hv10_split_matrix_factorization.json`

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

## `lane7-split-incidence-20260802-v1/verify_split_incidence_report.json`

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

## `lane7-split-incidence-20260802-v1/verify_split_determinants_report.json`

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

[Back to Lane 7](five-dimensional-collision-geometry.md)
