#!/usr/bin/env python3
"""Exact residue/null-vector audit for the full surviving (8,28) layer system.

This is a dependency-light replay of ``full_exact_low_layers.py``.  It uses
a compact exact rational-vector implementation of the quintic field rather than cypari2, keeps the original
row/column ordering and pivot convention, and exports the intermediate data
needed for a filtered-residue audit:

* ordered source and target bases;
* sparse layer matrices and RREF pivots;
* ordered left-null bases;
* lower-layer forcing vectors;
* raw compatibility pairings;
* principal-part representatives for the null rows;
* exact filtered-adjoint checks;
* provenance from raw compatibility rows to the normalized 15 equations;
* provenance for the six equations used in the resultant/norm certificate.

Run from any directory.  Outputs are written below ``generated-residue-audit``
next to this script unless ``--output`` is supplied.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import json
import time
from typing import Any, Iterable

from fractions import Fraction
from sympy import Poly, QQ, Rational, Symbol, sympify
from quintic_field_fast import K, K5


# ---------------------------------------------------------------------------
# Exact quintic field K = Q[u]/(u^5-u^4+3u^3+3u^2+26)
# ---------------------------------------------------------------------------
X = Symbol("x")
MINPOLY_EXPR = X**5 - X**4 + 3 * X**3 + 3 * X**2 + 26
ZERO = K.zero
ONE = K.one
U = K.unit

NVAR = 9
ZEXP = (0,) * NVAR
PARAMETER_NAMES = ["t1_0", "t1_1", "t2_0", "t2_1", "t2_2", "t3_0", "t3_1", "t3_2", "t4_0"]
FINAL_VARIABLES = ["x", "a", "b", "c", "d"]
FINAL_PARAMETER_INDICES = (0, 3, 6, 7, 8)
PARAMETER_WEIGHTS = (1, 1, 2, 2, 2, 3, 3, 3, 4)
ALPHA = 2
BETA = 3
S_TOTAL = ALPHA + BETA

KElement = K5
ParamPoly = dict[tuple[int, ...], KElement]
Laurent = dict[int, KElement]


def _as_fraction(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    q = Rational(str(value))
    return Fraction(int(q.p), int(q.q))


def k_from_rational(value: Any) -> KElement:
    return K.convert(_as_fraction(value))


def k_from_vector(values: Iterable[Any]) -> KElement:
    return K5(_as_fraction(value) for value in values)


def k_to_vector(value: KElement) -> list[str]:
    """Return coefficients in the fixed ascending basis 1,u,...,u^4."""
    return [str(q) for q in value.coeffs]


def k_to_expr(value: KElement, symbol: str = "u") -> str:
    coeffs = k_to_vector(value)
    pieces: list[str] = []
    for i, c in enumerate(coeffs):
        if c == "0":
            continue
        if i == 0:
            pieces.append(f"({c})")
        elif i == 1:
            pieces.append(f"({c})*{symbol}")
        else:
            pieces.append(f"({c})*{symbol}^{i}")
    return " + ".join(pieces) if pieces else "0"


def parse_pari_lift(text: str) -> KElement:
    """Parse a PARI ``lift`` string in x and convert it to the fixed K basis."""
    expr = sympify(text.replace("^", "**"), locals={"x": X})
    poly = Poly(expr, X, domain=QQ)
    out = ZERO
    for (degree,), coeff in poly.terms():
        out += K.convert(Fraction(int(coeff.p), int(coeff.q))) * (U**degree)
    return out


# ---------------------------------------------------------------------------
# Parameter-polynomial arithmetic over K
# ---------------------------------------------------------------------------
def clean(a: ParamPoly) -> ParamPoly:
    return {m: c for m, c in a.items() if c != ZERO}


def pc(c: KElement) -> ParamPoly:
    return {} if c == ZERO else {ZEXP: c}


def pv(i: int) -> ParamPoly:
    e = [0] * NVAR
    e[i] = 1
    return {tuple(e): ONE}


def padd(a: ParamPoly, b: ParamPoly) -> ParamPoly:
    c = dict(a)
    for m, v in b.items():
        c[m] = c.get(m, ZERO) + v
    return clean(c)


def pneg(a: ParamPoly) -> ParamPoly:
    return {m: -c for m, c in a.items()}


def pscale(c: KElement, a: ParamPoly) -> ParamPoly:
    return {} if c == ZERO else clean({m: c * v for m, v in a.items()})


def pmul(a: ParamPoly, b: ParamPoly) -> ParamPoly:
    c: ParamPoly = {}
    for m, x in a.items():
        for n, y in b.items():
            q = tuple(m[i] + n[i] for i in range(NVAR))
            c[q] = c.get(q, ZERO) + x * y
    return clean(c)


def pweight(f: ParamPoly) -> int:
    ws = {sum(e * w for e, w in zip(m, PARAMETER_WEIGHTS)) for m in f}
    assert len(ws) == 1, ws
    return next(iter(ws))


def poly_to_json(f: ParamPoly, *, final: bool = False) -> list[dict[str, Any]]:
    names = FINAL_VARIABLES if final else PARAMETER_NAMES
    return [
        {
            "exp": list(m),
            "monomial": "*".join(
                name if exponent == 1 else f"{name}^{exponent}"
                for name, exponent in zip(names, m)
                if exponent
            )
            or "1",
            "coeff_basis": k_to_vector(c),
            "coeff_expr": k_to_expr(c),
        }
        for m, c in sorted(f.items())
    ]


# ---------------------------------------------------------------------------
# Linear algebra with the original deterministic pivot convention
# ---------------------------------------------------------------------------
def rref_transform(M: list[list[KElement]]) -> tuple[list[list[KElement]], list[list[KElement]], list[int]]:
    m = len(M)
    n = len(M[0]) if m else 0
    A = [
        [M[i][j] for j in range(n)] + [ONE if i == j else ZERO for j in range(m)]
        for i in range(m)
    ]
    r = 0
    piv: list[int] = []
    for col in range(n):
        q = next((i for i in range(r, m) if A[i][col] != ZERO), None)
        if q is None:
            continue
        A[r], A[q] = A[q], A[r]
        z = ONE / A[r][col]
        A[r] = [z * x for x in A[r]]
        for i in range(m):
            if i != r and A[i][col] != ZERO:
                z = A[i][col]
                A[i] = [A[i][j] - z * A[r][j] for j in range(n + m)]
        piv.append(col)
        r += 1
        if r == m:
            break
    return [row[:n] for row in A], [row[n:] for row in A], piv


def transform_poly(T: list[list[KElement]], b: list[ParamPoly]) -> list[ParamPoly]:
    out: list[ParamPoly] = []
    for row in T:
        z: ParamPoly = {}
        for c, f in zip(row, b):
            z = padd(z, pscale(c, f))
        out.append(z)
    return out


def sparse_vector_json(vec: list[KElement]) -> list[dict[str, Any]]:
    return [
        {"index": i, "coeff_basis": k_to_vector(c), "coeff_expr": k_to_expr(c)}
        for i, c in enumerate(vec)
        if c != ZERO
    ]


def sparse_matrix_json(M: list[list[KElement]]) -> dict[str, Any]:
    return {
        "shape": [len(M), len(M[0]) if M else 0],
        "entries": [
            {
                "row": i,
                "col": j,
                "coeff_basis": k_to_vector(c),
                "coeff_expr": k_to_expr(c),
            }
            for i, row in enumerate(M)
            for j, c in enumerate(row)
            if c != ZERO
        ],
    }


# ---------------------------------------------------------------------------
# Laurent-polynomial arithmetic for the residue audit
# ---------------------------------------------------------------------------
def lclean(f: Laurent) -> Laurent:
    return {e: c for e, c in f.items() if c != ZERO}


def ladd(a: Laurent, b: Laurent) -> Laurent:
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, ZERO) + c
    return lclean(out)


def lscale(c: KElement, a: Laurent) -> Laurent:
    return {} if c == ZERO else lclean({e: c * v for e, v in a.items()})


def lmul(a: Laurent, b: Laurent) -> Laurent:
    out: Laurent = {}
    for i, c in a.items():
        for j, d in b.items():
            out[i + j] = out.get(i + j, ZERO) + c * d
    return lclean(out)


def lderiv(a: Laurent) -> Laurent:
    return lclean({e - 1: c * e for e, c in a.items() if e != 0})


def lmonomial(exponent: int, coeff: KElement = ONE) -> Laurent:
    return {} if coeff == ZERO else {exponent: coeff}


def laurent_to_json(f: Laurent) -> list[dict[str, Any]]:
    return [
        {"z_exp": e, "coeff_basis": k_to_vector(c), "coeff_expr": k_to_expr(c)}
        for e, c in sorted(f.items())
    ]


def residue_of_monomial_times(z_exp: int, omega_coeff: Laurent) -> KElement:
    """Residue at z=0 of z^z_exp * omega_coeff(z) dz."""
    return omega_coeff.get(-z_exp - 1, ZERO)


# ---------------------------------------------------------------------------
# Newton supports and layer data
# ---------------------------------------------------------------------------
def hull(points: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    pts = sorted(set(points))

    def cr(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lo: list[tuple[int, int]] = []
    for q in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], q) <= 0:
            lo.pop()
        lo.append(q)
    hi: list[tuple[int, int]] = []
    for q in reversed(pts):
        while len(hi) >= 2 and cr(hi[-2], hi[-1], q) <= 0:
            hi.pop()
        hi.append(q)
    return lo[:-1] + hi[:-1]


def inside(q: tuple[int, int], vertices: list[tuple[int, int]]) -> bool:
    H = hull(vertices)
    cs = [
        (b[0] - a[0]) * (q[1] - a[1]) - (b[1] - a[1]) * (q[0] - a[0])
        for a, b in zip(H, H[1:] + H[:1])
    ]
    return all(x >= 0 for x in cs) or all(x <= 0 for x in cs)


def lattice(vertices: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(
        (i, j)
        for i in range(max(x for x, _ in vertices) + 1)
        for j in range(max(y for _, y in vertices) + 1)
        if inside((i, j), vertices)
    )


VP = [(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)]
VQ = [(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)]
SP, SQ = lattice(VP), lattice(VQ)
LP: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
LQ: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
for q in SP:
    LP[q[1] - 2 * q[0] + 2].append(q)
for q in SQ:
    LQ[q[1] - 2 * q[0] + 3].append(q)


def rows_at(r: int) -> list[tuple[int, int]]:
    rows: set[tuple[int, int]] = set()
    for s in range(r + 1):
        for i, j in LP.get(s, []):
            for k, l in LQ.get(r - s, []):
                rows.add((i + k - 1, j + l - 1))
    return sorted(rows)


def bracket(Pd: dict[tuple[int, int], ParamPoly], Qd: dict[tuple[int, int], ParamPoly]) -> dict[tuple[int, int], ParamPoly]:
    out: dict[tuple[int, int], ParamPoly] = {}
    for (i, j), a in Pd.items():
        for (k, l), b in Qd.items():
            q = (i + k - 1, j + l - 1)
            out[q] = padd(out.get(q, {}), pscale(i * l - j * k, pmul(a, b)))
    return out


@dataclass
class RawEquation:
    layer: int
    null_index: int
    transform_row_index: int
    pairing: ParamPoly


# ---------------------------------------------------------------------------
# Replay and audit
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--input-dir", type=Path, default=None,
                        help="directory containing belyi_exact_field_relations.json and full_exact_fivevar_w8.json")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    input_dir = (args.input_dir or script_dir).resolve()
    output_dir = (args.output or script_dir.parent / "generated-residue-audit").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    relation_path = input_dir / "belyi_exact_field_relations.json"
    existing_path = input_dir / "full_exact_fivevar_w8.json"
    data = json.loads(relation_path.read_text())

    # Exact lower face A_0=z p(z), B_0=z^2 q(z).
    Avec = [ONE, ONE]
    for i in range(2, 8):
        c = data["relations"][str(i)]
        Avec.append(-k_from_vector(c[:5]) / int(c[5]))
    Bvec = [ONE]
    for n in range(1, 11):
        s = ZERO
        for i in range(1, min(7, n) + 1):
            s += (1 + 2 * n - 5 * i) * Avec[i] * Bvec[n - i]
        Bvec.append(-s / (1 + 2 * n))
    for n in range(11, 18):
        s = ZERO
        for i in range(max(0, n - 10), min(7, n) + 1):
            s += (1 + 2 * n - 5 * i) * Avec[i] * Bvec[n - i]
        assert s == ZERO

    A0_laurent: Laurent = {n + 1: Avec[n] for n in range(8)}
    B0_laurent: Laurent = {n + 2: Bvec[n] for n in range(11)}
    dA0 = lderiv(A0_laurent)
    dB0 = lderiv(B0_laurent)

    P: dict[int, dict[tuple[int, int], ParamPoly]] = {
        0: {(n + 1, 2 * n): pc(Avec[n]) for n in range(8)}
    }
    Q: dict[int, dict[tuple[int, int], ParamPoly]] = {
        0: {(n + 2, 2 * n + 1): pc(Bvec[n]) for n in range(11)}
    }

    next_param = {1: [0, 1], 2: [2, 3, 4], 3: [5, 6, 7], 4: [8]}
    raw_equations: list[RawEquation] = []
    layer_exports: list[dict[str, Any]] = []
    layer_info: list[list[int]] = []

    for r in range(1, 9):
        start = time.time()
        rows = rows_at(r)
        rid = {q: i for i, q in enumerate(rows)}
        cols = [("P", q) for q in LP.get(r, [])] + [("Q", q) for q in LQ.get(r, [])]
        M = [[ZERO] * len(cols) for _ in rows]

        for c, (typ, q) in enumerate(cols):
            if typ == "P":
                i, j = q
                for (k, l), coefp in Q[0].items():
                    M[rid[(i + k - 1, j + l - 1)]][c] += (i * l - j * k) * next(iter(coefp.values()))
            else:
                k, l = q
                for (i, j), coefp in P[0].items():
                    M[rid[(i + k - 1, j + l - 1)]][c] += (i * l - j * k) * next(iter(coefp.values()))

        forcing = {q: {} for q in rows}
        for s in range(1, r):
            if s in P and r - s in Q:
                for q, e in bracket(P[s], Q[r - s]).items():
                    forcing[q] = padd(forcing[q], e)
        forcing_vector = [forcing[q] for q in rows]
        rhs = [pneg(f) for f in forcing_vector]

        if not cols:
            raise AssertionError("All audited layers have source columns")

        R, T, piv = rref_transform(M)
        bt = transform_poly(T, rhs)
        left_null = T[len(piv) :]
        compat = bt[len(piv) :]

        # Confirm the rows advertised as left-null are exactly so.
        for null_row in left_null:
            for c in range(len(cols)):
                assert sum((null_row[i] * M[i][c] for i in range(len(rows))), ZERO) == ZERO

        for null_index, pairing in enumerate(compat):
            if pairing:
                raw_equations.append(
                    RawEquation(
                        layer=r,
                        null_index=null_index,
                        transform_row_index=len(piv) + null_index,
                        pairing=pairing,
                    )
                )

        free = [j for j in range(len(cols)) if j not in piv]
        ker: list[list[KElement]] = []
        for f in free:
            v = [ZERO] * len(cols)
            v[f] = ONE
            for rr, c in enumerate(piv):
                v[c] = -R[rr][f]
            ker.append(v)
        expected = next_param.get(r, [])
        assert len(ker) == len(expected), (r, len(ker), len(expected))

        xsol: list[ParamPoly] = [{} for _ in cols]
        for rr, c in enumerate(piv):
            xsol[c] = bt[rr]
        for pind, vec in zip(expected, ker):
            for c, z in enumerate(vec):
                xsol[c] = padd(xsol[c], pscale(z, pv(pind)))
        P[r] = {}
        Q[r] = {}
        for e, (typ, q) in zip(xsol, cols):
            (P[r] if typ == "P" else Q[r])[q] = e

        info = [r, len(cols), len(rows), len(piv), len(ker), sum(bool(e) for e in compat)]
        layer_info.append(info)

        # Verify matrix columns directly from the differential operator.
        matrix_reconstruction_ok = True
        for c, (typ, q) in enumerate(cols):
            source_z_exp = q[0]
            if typ == "P":
                basis_d = ladd(
                    lscale(2 - r, lmul(lmonomial(source_z_exp), dB0)),
                    lscale(-3, lmul(B0_laurent, lderiv(lmonomial(source_z_exp)))),
                )
            else:
                basis_d = ladd(
                    lscale(2, lmul(A0_laurent, lderiv(lmonomial(source_z_exp)))),
                    lscale(r - 3, lmul(lmonomial(source_z_exp), dA0)),
                )
            for row_index, row_q in enumerate(rows):
                if basis_d.get(row_q[0], ZERO) != M[row_index][c]:
                    matrix_reconstruction_ok = False
                    raise AssertionError((r, c, row_index, basis_d.get(row_q[0], ZERO), M[row_index][c]))
            extra = set(basis_d) - {q0[0] for q0 in rows}
            if extra:
                matrix_reconstruction_ok = False
                raise AssertionError((r, "unexpected target exponents", extra))

        null_exports: list[dict[str, Any]] = []
        for null_index, (null_row, pairing) in enumerate(zip(left_null, compat)):
            # A target row (I,J) represents z^I dz.  The dual principal part at
            # z=0 is c_I z^{-I-1}.
            lambda_pp: Laurent = {}
            for coeff, row_q in zip(null_row, rows):
                if coeff != ZERO:
                    exponent = -row_q[0] - 1
                    lambda_pp[exponent] = lambda_pp.get(exponent, ZERO) + coeff
            lambda_pp = lclean(lambda_pp)
            dlambda = lderiv(lambda_pp)
            adj_A = ladd(
                lscale(3, lmul(B0_laurent, dlambda)),
                lscale(5 - r, lmul(lambda_pp, dB0)),
            )
            adj_B = ladd(
                lscale(-2, lmul(A0_laurent, dlambda)),
                lscale(r - 5, lmul(lambda_pp, dA0)),
            )

            p_checks = []
            q_checks = []
            for col_index, (typ, q) in enumerate(cols):
                z_exp = q[0]
                if typ == "P":
                    residue = residue_of_monomial_times(z_exp, adj_A)
                    p_checks.append({"column": col_index, "z_exp": z_exp, "residue_basis": k_to_vector(residue)})
                    assert residue == ZERO
                else:
                    residue = residue_of_monomial_times(z_exp, adj_B)
                    q_checks.append({"column": col_index, "z_exp": z_exp, "residue_basis": k_to_vector(residue)})
                    assert residue == ZERO

            # Pairing reconstructed directly by residue against -Phi_r.
            residue_pairing: ParamPoly = {}
            for coeff, forcing_poly in zip(null_row, rhs):
                residue_pairing = padd(residue_pairing, pscale(coeff, forcing_poly))
            assert residue_pairing == pairing

            support_poles = sorted(-e for e in lambda_pp if e < 0)
            null_exports.append(
                {
                    "null_index": null_index,
                    "transform_row_index": len(piv) + null_index,
                    "vector": sparse_vector_json(null_row),
                    "principal_part_at_z0": laurent_to_json(lambda_pp),
                    "pole_orders_at_z0": support_poles,
                    "max_pole_order_at_z0": max(support_poles) if support_poles else 0,
                    "adjoint_A": laurent_to_json(adj_A),
                    "adjoint_B": laurent_to_json(adj_B),
                    "filtered_adjoint_P_checks": p_checks,
                    "filtered_adjoint_Q_checks": q_checks,
                    "filtered_adjoint_verified": True,
                    "pairing_is_zero": not bool(pairing),
                    "pairing": poly_to_json(pairing),
                }
            )

        source_basis = [
            {
                "column_index": c,
                "type": typ,
                "lattice_exponent": list(q),
                "normal_layer": r,
                "z_exponent": q[0],
            }
            for c, (typ, q) in enumerate(cols)
        ]
        target_basis = [
            {
                "row_index": i,
                "lattice_exponent": list(q),
                "normal_layer": r,
                "differential": f"z^{q[0]} dz",
                "z_exponent": q[0],
            }
            for i, q in enumerate(rows)
        ]

        layer_exports.append(
            {
                "layer": r,
                "alpha": ALPHA,
                "beta": BETA,
                "S": S_TOTAL,
                "resonant": r == S_TOTAL,
                "source_basis": source_basis,
                "target_basis": target_basis,
                "source_z_exponents_P": [q[0] for typ, q in cols if typ == "P"],
                "source_z_exponents_Q": [q[0] for typ, q in cols if typ == "Q"],
                "target_z_exponents": [q[0] for q in rows],
                "matrix": sparse_matrix_json(M),
                "matrix_reconstruction_from_Dr_verified": matrix_reconstruction_ok,
                "rank": len(piv),
                "pivot_columns": piv,
                "kernel_dimension": len(ker),
                "cokernel_dimension": len(rows) - len(piv),
                "nonzero_compatibility_count_before_normalization": sum(bool(e) for e in compat),
                "left_null_basis": null_exports,
                "forcing_vector_Phi_r": [
                    {
                        "row_index": i,
                        "target_lattice_exponent": list(rows[i]),
                        "target_z_exponent": rows[i][0],
                        "terms": poly_to_json(f),
                    }
                    for i, f in enumerate(forcing_vector)
                    if f
                ],
                "rhs_vector_minus_Phi_r": [
                    {
                        "row_index": i,
                        "target_lattice_exponent": list(rows[i]),
                        "target_z_exponent": rows[i][0],
                        "terms": poly_to_json(f),
                    }
                    for i, f in enumerate(rhs)
                    if f
                ],
            }
        )
        print(f"layer {r}: rows={len(rows)} cols={len(cols)} rank={len(piv)} coker={len(rows)-len(piv)} nonzero={sum(bool(e) for e in compat)}", flush=True)

    # Every raw compatibility equation has the expected normal weight.
    for eq in raw_equations:
        assert pweight(eq.pairing) == eq.layer
        assert all(m[2] == 0 and m[5] == 0 for m in eq.pairing)

    # Weight-four square obstruction and normalization.
    E4 = [eq for eq in raw_equations if eq.layer == 4]
    uniq4: list[ParamPoly] = []
    for eq in E4:
        f = eq.pairing
        m0 = min(f)
        nf = {m: (ONE / f[m0]) * c for m, c in f.items()}
        if not any(nf == h for h in uniq4):
            uniq4.append(nf)
    assert len(uniq4) == 1
    f4 = uniq4[0]
    assert all(all(m[i] == 0 for i in range(NVAR) if i not in (1, 4)) for m in f4)
    c22 = f4.get((0, 0, 0, 0, 2, 0, 0, 0, 0), ZERO)
    c12 = f4.get((0, 2, 0, 0, 1, 0, 0, 0, 0), ZERO)
    c14 = f4.get((0, 4, 0, 0, 0, 0, 0, 0, 0), ZERO)
    assert c22 != ZERO
    alpha_norm = -c12 / (2 * c22)
    assert c14 / c22 == alpha_norm**2

    def subst_core(f: ParamPoly) -> ParamPoly:
        keep = FINAL_PARAMETER_INDICES
        out: ParamPoly = {}
        for m, c in f.items():
            cc = c * (alpha_norm ** m[4])  # t1_1=1, t2_2=alpha
            q = tuple(m[i] for i in keep)
            out[q] = out.get(q, ZERO) + cc
        return clean(out)

    def eval12(f: ParamPoly) -> KElement:
        total = ZERO
        for m, c in f.items():
            if any(m[i] for i in range(NVAR) if i not in (1, 4)):
                continue
            total += c * (alpha_norm ** m[4])
        return total

    Ptop = eval12(P[2][(8, 16)])
    Qtop = eval12(Q[3][(12, 24)])
    assert Ptop != ZERO and Qtop != ZERO

    # Track normalization and duplicate provenance.
    final_records: list[dict[str, Any]] = []
    final_polys: list[tuple[int, ParamPoly]] = []
    for raw_index, eq in enumerate(raw_equations):
        h = subst_core(eq.pairing)
        if not h:
            continue
        m0 = min(h)
        normalization_scalar = ONE / h[m0]
        nf = {m: normalization_scalar * c for m, c in h.items()}
        match = next((i for i, (rr, existing) in enumerate(final_polys) if rr == eq.layer and existing == nf), None)
        source_record = {
            "raw_equation_index": raw_index,
            "layer": eq.layer,
            "null_index": eq.null_index,
            "transform_row_index": eq.transform_row_index,
            "normalization_scalar_basis": k_to_vector(normalization_scalar),
            "normalization_scalar_expr": k_to_expr(normalization_scalar),
        }
        if match is None:
            final_polys.append((eq.layer, nf))
            final_records.append(
                {
                    "final_index": len(final_records),
                    "weight": eq.layer,
                    "terms": poly_to_json(nf, final=True),
                    "sources": [source_record],
                }
            )
        else:
            final_records[match]["sources"].append(source_record)

    counts = {r: sum(rr == r for rr, _ in final_polys) for r in sorted({rr for rr, _ in final_polys})}
    assert counts == {5: 1, 6: 3, 7: 5, 8: 6}, counts
    assert len(final_records) == 15

    # Compare to the archived normalized output coefficient-by-coefficient.
    existing = json.loads(existing_path.read_text())
    existing_match = len(existing["equations"]) == len(final_records)
    comparison_details = []
    if existing_match:
        for i, (record, archived) in enumerate(zip(final_records, existing["equations"])):
            archived_poly: dict[tuple[int, ...], KElement] = {
                tuple(term["exp"]): parse_pari_lift(term["coeff"])
                for term in archived["terms"]
            }
            generated_poly = final_polys[i][1]
            ok = record["weight"] == archived["weight"] and generated_poly == archived_poly
            comparison_details.append({"final_index": i, "match": ok})
            existing_match = existing_match and ok
    assert existing_match

    selected_indices = [4, 6, 8, 9, 10, 11]
    selected_roles = ["rho", "g1", "g2", "g3", "g4", "g5"]
    selected = []
    for role, index in zip(selected_roles, selected_indices):
        record = final_records[index]
        selected.append(
            {
                "role": role,
                "final_index": index,
                "weight": record["weight"],
                "sources": record["sources"],
                "terms": record["terms"],
            }
        )

    # Annotate final records by the pole orders of their source residue classes.
    layer_lookup = {entry["layer"]: entry for entry in layer_exports}
    for record in final_records:
        for source in record["sources"]:
            null_entry = layer_lookup[source["layer"]]["left_null_basis"][source["null_index"]]
            source["principal_part_pole_orders_at_z0"] = null_entry["pole_orders_at_z0"]
            source["principal_part_max_pole_order_at_z0"] = null_entry["max_pole_order_at_z0"]

    selected_pole_profile = [
        {
            "role": item["role"],
            "final_index": item["final_index"],
            "weight": item["weight"],
            "source_profiles": [
                {
                    "layer": src["layer"],
                    "null_index": src["null_index"],
                    "pole_orders": src["principal_part_pole_orders_at_z0"],
                    "max_pole_order": src["principal_part_max_pole_order_at_z0"],
                }
                for src in item["sources"]
            ],
        }
        for item in selected
    ]

    # Complete provenance for every raw nonzero compatibility pairing.
    raw_outcomes = []
    source_by_raw = {}
    for record in final_records:
        for source in record["sources"]:
            source_by_raw[source["raw_equation_index"]] = (record["final_index"], source)
    for raw_index, eq in enumerate(raw_equations):
        if raw_index in source_by_raw:
            final_index, source = source_by_raw[raw_index]
            raw_outcomes.append({
                "raw_equation_index": raw_index,
                "layer": eq.layer,
                "null_index": eq.null_index,
                "status": "survives_normalization",
                "final_index": final_index,
                "normalization_scalar_basis": source["normalization_scalar_basis"],
                "normalization_scalar_expr": source["normalization_scalar_expr"],
            })
        else:
            assert not subst_core(eq.pairing)
            raw_outcomes.append({
                "raw_equation_index": raw_index,
                "layer": eq.layer,
                "null_index": eq.null_index,
                "status": "vanishes_after_t1_1_t2_2_normalization",
                "final_index": None,
            })

    # Exact sparse matrices relating the ordered filtered-residue coordinates
    # (one column per left-null row) to the normalized final equations.  Each
    # row has one nonzero entry because no cross-null linear combination is
    # used: only substitution, scalar normalization, and duplicate removal.
    layer_change_matrices = []
    for r in range(5, 9):
        final_indices = [record["final_index"] for record in final_records if record["weight"] == r]
        coker_dim = layer_lookup[r]["cokernel_dimension"]
        entries = []
        alternatives = []
        for local_row, final_index in enumerate(final_indices):
            record = final_records[final_index]
            primary = record["sources"][0]
            entries.append({
                "row": local_row,
                "col_null_index": primary["null_index"],
                "coeff_basis": primary["normalization_scalar_basis"],
                "coeff_expr": primary["normalization_scalar_expr"],
            })
            if len(record["sources"]) > 1:
                alternatives.append({"row": local_row, "sources": record["sources"][1:]})
        layer_change_matrices.append({
            "layer": r,
            "shape": [len(final_indices), coker_dim],
            "ordered_final_indices": final_indices,
            "entries": entries,
            "alternative_duplicate_sources": alternatives,
            "interpretation": "F_row = scalar * Res_0(lambda_null * (-Phi_r)) after the stated parameter normalization",
        })

    selected_projection = {
        "shape": [6, 15],
        "entries": [{"row": i, "col_final_index": j, "value": 1} for i, j in enumerate(selected_indices)],
        "ordered_roles": selected_roles,
        "interpretation": "coordinate projection from the full 15-component reduced obstruction section to the six resultant/norm components",
    }

    # Main machine-readable layer export.
    layers_out = {
        "schema_version": 1,
        "field": {
            "name": "K",
            "generator": "u",
            "minimal_polynomial": "u^5-u^4+3*u^3+3*u^2+26",
            "basis": ["1", "u", "u^2", "u^3", "u^4"],
        },
        "operator": {
            "alpha": ALPHA,
            "beta": BETA,
            "S": S_TOTAL,
            "formula": "D_r(a,b)=(2-r)a dB0-3B0 da+2A0 db+(r-3)b dA0",
            "adjoint_formula": "(3B0 dlambda+(5-r)lambda dB0, -2A0 dlambda+(r-5)lambda dA0)",
        },
        "A0": laurent_to_json(A0_laurent),
        "B0": laurent_to_json(B0_laurent),
        "Psi": [{"z_exp": 2, "coeff_basis": k_to_vector(ONE), "coeff_expr": "1"}],
        "layers": layer_exports,
    }
    (output_dir / "residue_audit_layers.json").write_text(json.dumps(layers_out, indent=2))

    provenance_out = {
        "schema_version": 1,
        "normalization": {
            "description": "t1_1=1; t2_2=alpha; t2_0 and t3_0 split off; retain t1_0,t2_1,t3_1,t3_2,t4_0",
            "alpha_basis": k_to_vector(alpha_norm),
            "alpha_expr": k_to_expr(alpha_norm),
            "Ptop_basis": k_to_vector(Ptop),
            "Qtop_basis": k_to_vector(Qtop),
        },
        "raw_nonzero_compatibility_equations": [
            {
                "raw_equation_index": i,
                "layer": eq.layer,
                "null_index": eq.null_index,
                "transform_row_index": eq.transform_row_index,
                "terms": poly_to_json(eq.pairing),
            }
            for i, eq in enumerate(raw_equations)
        ],
        "final_equations": final_records,
        "archived_output_comparison": {
            "path": str(existing_path.name),
            "all_15_equations_match": existing_match,
            "details": comparison_details,
        },
        "raw_normalization_outcomes": raw_outcomes,
        "layer_residue_to_final_change_matrices": layer_change_matrices,
        "selected_six": selected,
        "selected_six_pole_profile": selected_pole_profile,
        "selected_six_projection_matrix": selected_projection,
    }
    (output_dir / "residue_audit_provenance.json").write_text(json.dumps(provenance_out, indent=2))

    # Compact human-readable summary, expanded after inspecting the generated profiles.
    summary = {
        "field_backend": "SymPy exact AlgebraicField/ANP",
        "layer_info": layer_info,
        "reduced_counts": counts,
        "archived_15_equations_match": existing_match,
        "all_layer_matrices_reconstructed_from_Dr": all(x["matrix_reconstruction_from_Dr_verified"] for x in layer_exports),
        "all_filtered_adjoint_checks_pass": all(
            null_entry["filtered_adjoint_verified"]
            for layer in layer_exports
            for null_entry in layer["left_null_basis"]
        ),
        "selected_six_pole_profile": selected_pole_profile,
    }
    (output_dir / "residue_audit_summary.json").write_text(json.dumps(summary, indent=2))

    print(f"wrote {output_dir / 'residue_audit_layers.json'}")
    print(f"wrote {output_dir / 'residue_audit_provenance.json'}")
    print(f"wrote {output_dir / 'residue_audit_summary.json'}")


if __name__ == "__main__":
    main()
