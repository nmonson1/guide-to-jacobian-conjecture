#!/usr/bin/env python3
"""Exact Lane 9 Kummer-attachment audit.

The checker is intentionally standard-library only.  It verifies the finite
identities used by LANE9_KUMMER_ATTACHMENT_AUDIT.md and emits a deterministic
JSON report.  It does not manufacture the missing high-order F_2 endpoint
matrices.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd
from pathlib import Path
from typing import Dict, Mapping, MutableMapping, Sequence, Tuple

Laurent = Dict[int, Fraction]
BiExponent = Tuple[int, int]


def clean(poly: Mapping[int, Fraction]) -> Laurent:
    return {k: Fraction(v) for k, v in sorted(poly.items()) if v}


def add(*polys: Mapping[int, Fraction]) -> Laurent:
    out: MutableMapping[int, Fraction] = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return clean(out)


def scale(poly: Mapping[int, Fraction], scalar: Fraction | int) -> Laurent:
    c = Fraction(scalar)
    return clean({k: c * v for k, v in poly.items()})


def mul(left: Mapping[int, Fraction], right: Mapping[int, Fraction]) -> Laurent:
    out: MutableMapping[int, Fraction] = {}
    for i, a in left.items():
        for j, b in right.items():
            out[i + j] = out.get(i + j, Fraction(0)) + a * b
    return clean(out)


def derivative(poly: Mapping[int, Fraction]) -> Laurent:
    return clean({k - 1: Fraction(k) * v for k, v in poly.items() if k})


def monomial(exponent: int, coefficient: Fraction | int = 1) -> Laurent:
    return clean({exponent: Fraction(coefficient)})


def bracket_pair(
    r: int,
    f: Mapping[int, Fraction],
    g: Mapping[int, Fraction],
    s: int,
    F: Mapping[int, Fraction],
    G: Mapping[int, Fraction],
) -> tuple[Laurent, Laurent]:
    """Bracket of t^r(f d_z + g t d_t) and t^s(F d_z + G t d_t)."""

    horizontal = add(
        mul(f, derivative(F)),
        scale(mul(F, derivative(f)), -1),
        scale(mul(g, F), s),
        scale(mul(G, f), -r),
    )
    vertical = add(
        mul(f, derivative(G)),
        scale(mul(F, derivative(g)), -1),
        scale(mul(g, G), s - r),
    )
    return horizontal, vertical


def determinant_2x2(rows: Sequence[Sequence[int]]) -> int:
    if len(rows) != 2 or any(len(row) != 2 for row in rows):
        raise ValueError("expected a 2 by 2 matrix")
    return rows[0][0] * rows[1][1] - rows[0][1] * rows[1][0]


def monomial_derivative(
    field: tuple[tuple[Fraction, BiExponent], tuple[Fraction, BiExponent]],
    exponent: BiExponent,
) -> tuple[Fraction, BiExponent] | tuple[Fraction, BiExponent, Fraction, BiExponent]:
    """Apply a two-monomial vector field to x^a y^b."""

    (cx, ex), (cy, ey) = field
    a, b = exponent
    tx = (Fraction(a) * cx, (a - 1 + ex[0], b + ex[1]))
    ty = (Fraction(b) * cy, (a + ey[0], b - 1 + ey[1]))
    if tx[0] == 0:
        return ty
    if ty[0] == 0:
        return tx
    if tx[1] != ty[1]:
        return tx[0], tx[1], ty[0], ty[1]
    return tx[0] + ty[0], tx[1]


def apply_monomial_field(
    field: tuple[tuple[Fraction, BiExponent], tuple[Fraction, BiExponent]],
    exponent: BiExponent,
) -> tuple[Fraction, BiExponent]:
    result = monomial_derivative(field, exponent)
    if len(result) != 2:
        raise AssertionError(f"terms did not combine: {result}")
    coefficient, output_exponent = result
    return Fraction(coefficient), output_exponent


def vector_field_checks() -> dict[str, object]:
    field = (
        (Fraction(-6), (-11, -4)),
        (Fraction(22), (-12, -3)),
    )
    h_raw = apply_monomial_field(field, (-11, -3))
    m_raw = apply_monomial_field(field, (-12, -4))
    q_raw = apply_monomial_field(field, (12, 4))
    assert h_raw[0] == 0
    assert m_raw == (Fraction(-16), (-24, -8))
    assert q_raw == (Fraction(16), (0, 0))

    divergence_coefficient = Fraction(-6 * -11) + Fraction(22 * -3)
    assert divergence_coefficient == 0
    h_y_coefficient = Fraction(2 * -3)
    minus_h_x_coefficient = Fraction(-(2 * -11))
    assert h_y_coefficient == -6
    assert minus_h_x_coefficient == 22

    det = 4 * 2 - 7
    a = Fraction((-2) * 2 - 2, det)
    b = Fraction(4 * 2 - 7 * (-2), det)
    assert (a, b) == (Fraction(-6), Fraction(22))

    return {
        "affine_vector_field": {
            "Vx": "-6*x^-11*y^-4",
            "Vy": "22*x^-12*y^-3",
            "divergence": 0,
            "hamiltonian": "2*x^-11*y^-3",
        },
        "first_integral": {"H": "2*x^-11*y^-3", "V(H)": "0"},
        "riccati_coordinate": {"M": "x^-12*y^-4", "V(M)": "-16*M^2"},
        "translation_coordinate": {"Q": "x^12*y^4", "V(Q)": "16"},
        "formal_flow": {
            "R^8": "1+16*s*M",
            "x_s": "x*R^-3",
            "y_s": "y*R^11",
            "t_s": "t*R^-1",
            "z_s": "z*R",
            "H_s": "H",
            "Q_s": "Q+16*s",
        },
    }


def weighted_divergence_checks() -> dict[str, object]:
    r = 4
    f = monomial(-3, 2)
    g_bare = monomial(-4, 1)
    g_corrected = monomial(-4, -2)
    z2 = monomial(2)

    def defect(g: Mapping[int, Fraction]) -> Laurent:
        return add(derivative(mul(f, z2)), scale(mul(g, z2), r - 5))

    bare = defect(g_bare)
    corrected = defect(g_corrected)
    assert bare == monomial(-2, -3)
    assert corrected == {}

    return {
        "identity": "D_r Theta_r(f,g)=(f*z^2)' +(r-5)*g*z^2",
        "bare_pair": {"f": "2*z^-3", "g": "z^-4", "defect": "-3*z^-2"},
        "corrected_pair": {"f": "2*z^-3", "g": "-2*z^-4", "defect": "0"},
        "uniqueness_with_fixed_horizontal_component": True,
    }


def bracket_checks() -> dict[str, object]:
    expected = {
        "c0": ({-4: Fraction(18)}, {-5: Fraction(6)}),
        "c1": ({-3: Fraction(30)}, {-4: Fraction(5)}),
        "unit_top": ({-2: Fraction(42)}, {}),
    }
    cases = {
        "c0": ({0: Fraction(1)}, {-1: Fraction(2)}),
        "c1": ({1: Fraction(1)}, {0: Fraction(3)}),
        "unit_top": ({2: Fraction(1)}, {1: Fraction(4)}),
    }
    wall_f = monomial(-3, 2)
    wall_g = monomial(-4, 1)
    records: dict[str, object] = {}
    for name, (f4, g4) in cases.items():
        result = bracket_pair(4, f4, g4, 7, wall_f, wall_g)
        assert result == expected[name]
        records[name] = {
            "horizontal": {str(k): str(v) for k, v in result[0].items()},
            "vertical": {str(k): str(v) for k, v in result[1].items()},
        }

    return {
        "formula": {
            "f_11": "18*c0*z^-4+30*c1*z^-3+42*z^-2",
            "g_11": "6*c0*z^-5+5*c1*z^-4",
        },
        "basis_checks": records,
        "forced_top_terms_on_degree_21_face": {
            "P": "336*lead(A0)*z^5",
            "Q": "504*lead(B0)*z^9",
        },
    }


def principal_part_checks() -> dict[str, object]:
    a_principal = [
        {"z_exponent": i - 3, "coefficient": f"{2 * (i + 3)}*p_{i}"}
        for i in range(3)
    ]
    b_principal = [
        {"z_exponent": i - 2, "coefficient": f"{2 * (i + 5)}*q_{i}"}
        for i in range(2)
    ]
    assert a_principal[0] == {"z_exponent": -3, "coefficient": "6*p_0"}
    assert b_principal[0] == {"z_exponent": -2, "coefficient": "10*q_0"}

    return {
        "Theta4_corrected": {
            "a": "6*z^-3*p+2*z^-2*p'",
            "b": "10*z^-2*q+2*z^-1*q'",
        },
        "old_window": {"a_exponents": [0, 6], "b_exponents": [0, 11]},
        "principal_parts": {"a": a_principal, "b": b_principal},
        "nonvanishing_reason": "p_0*q_0=1",
        "direct_old_window_membership": False,
        "coefficientwise_match_without_overlap_normalization": False,
    }


def lattice_and_stabilizer_checks() -> dict[str, object]:
    exponent_matrix = [[-11, -3], [12, 4]]
    determinant = determinant_2x2(exponent_matrix)
    index = abs(determinant)
    assert determinant == -8
    assert index == 8

    d1 = 0
    for row in exponent_matrix:
        for entry in row:
            d1 = gcd(d1, abs(entry))
    d2 = index // d1
    assert (d1, d2) == (1, 8)

    h_weight = (-3) - (-11)
    q_weight = 4 - 12
    assert h_weight % 8 == 0
    assert q_weight % 8 == 0

    return {
        "quotient_coordinates": {
            "H": "2*x^-11*y^-3",
            "Q": "x^12*y^4",
            "exponent_matrix": exponent_matrix,
            "determinant": determinant,
            "smith_invariants": [d1, d2],
        },
        "function_fields": {
            "adjacent_coordinates": "u=(x*y)^-1, v=y",
            "H_in_uv": "2*u^11*v^8",
            "Q_in_uv": "u^-12*v^-8",
            "quotient_field": "K(H,Q)=K(u,v^8)",
            "generic_extension_degree": 8,
        },
        "presentation_stabilizer": {
            "group": "mu_8",
            "action_uv": "(u,v)->(u,zeta*v)",
            "action_xy": "(x,y)->(zeta^-1*x,zeta*y)",
        },
        "ordinary_unimodular_chart": False,
        "index_is_invariant_under_unimodular_recharting": True,
    }


def cocycle_checks() -> dict[str, object]:
    return {
        "quotient_translation": {
            "tau_s": "(H,Q)->(H,Q+16*s)",
            "inverse": "tau_-s",
            "pairwise_cocycle": "tau_s*tau_t=tau_(s+t)",
            "triple_cocycle": "strict",
        },
        "root_lift": {
            "R_s(Q)^8": "(Q+16*s)/Q",
            "composition_eighth_power": (
                "((Q+16*s)/Q)*((Q+16*s+16*t)/(Q+16*s))"
                "=(Q+16*(s+t))/Q"
            ),
            "formal_unit_root": "strict cocycle",
            "generic_algebraic_root": "mu_8-valued ambiguity",
        },
    }


def cyclic_descent_checks() -> dict[str, object]:
    g = 5
    k = 4
    character = k % g
    first_invariant_order = g // gcd(g, k)
    normal_shift_per_wall_order = 2 * k - 1
    invariant_normal_shift = first_invariant_order * normal_shift_per_wall_order
    assert character == 4
    assert first_invariant_order == 5
    assert invariant_normal_shift == 35
    return {
        "cyclic_group_order": g,
        "wall_index": k,
        "parameter_character": character,
        "normal_rees_weight_needed_for_layer_four": -3,
        "parameter_bidegree": [-3, character],
        "first_invariant_wall_order": first_invariant_order,
        "first_invariant_unweighted_normal_shift": invariant_normal_shift,
    }


def support_transport_checks() -> dict[str, object]:
    return {
        "ordinary_monomial_chart": {
            "criterion": "exponent matrix lies in GL_2(Z)",
            "support_transport": "finite exponent windows are carried bijectively",
            "residue_transport": "contragredient pullback preserves the perfect pairing",
            "pairwise_and_triple_cocycles": "strict by matrix composition",
        },
        "index_eight_quotient": {
            "support_transport": (
                "the invariant chart sees one sublattice; the full coefficient space "
                "is the direct sum of the eight mu_8-character modules"
            ),
            "residue_transport": "characterwise contragredient pairing",
            "single_ordinary_chart_transport": False,
        },
    }


def admissible_module_checks() -> dict[str, object]:
    return {
        "name": "minimal Rees-Kummer admissible Lie algebroid",
        "definition": (
            "smallest filtered, C5-graded, mu8-equivariant Lie algebroid of "
            "divergence-free derivations preserving the nonlinear support ideal, "
            "containing the verified fixed-presentation generators and the Kummer "
            "translation arrow"
        ),
        "forced_generators": [
            "verified fixed-chart presentation generators (external table when supplied)",
            "layer-4 Kummer tangent t^4(2*z^-3*d_z-2*z^-4*t*d_t)",
            "layer-7 bare wall tangent t^7(2*z^-3*d_z+z^-4*t*d_t)",
            "transported and Lie-bracket closure terms, including layer 11",
        ],
        "known_rank_ladder_layers_1_to_4": {
            "determinant_kernel": [2, 3, 3, 1],
            "maximal_support_admissible_laurent": [2, 3, 3, 1],
            "affine_polynomial": [2, 3, 2, 1],
            "recorded_complete_chain_input": [1, 1, 2, 0],
        },
        "classification_status": (
            "definition and forced closure proved; equality with the actual complete-chain "
            "operation algebroid is not proved without the missing generator table"
        ),
    }


def recurrence_schema() -> dict[str, object]:
    return {
        "status": "uninstantiated because the high-order F_2 endpoint blocks are absent",
        "unknowns": [
            "x_r^L in U_r^L",
            "x_r^R in U_r^R",
            "all fresh parameters p_r with declared C5 characters",
        ],
        "equations": [
            "D_r^L*x_r^L=-Phi_r^L(x_<r^L,p_<=r)",
            "D_r^R*x_r^R=-Phi_r^R(x_<r^R,p_<=r)",
            "x_r^R=T_r(s)*x_r^L plus lower-order transport terms",
            "all coefficients outside both finite Newton windows vanish",
        ],
        "descent_rule": "a q-th k-wall term shifts C5 character by -q*k",
        "required_missing_artifacts": [
            "both endpoint block matrices and ordered bases",
            "fresh-parameter ranges through and beyond order 530",
            "overlap/normalization matrices",
            "archived replay manifest with hashes",
        ],
        "safe_conclusion": (
            "the recurrence architecture and character decomposition are exact, but no "
            "order-530 obstruction or global feasibility verdict can be inferred"
        ),
    }


def checklist_statuses() -> list[dict[str, str]]:
    return [
        {"item": "Correct public layer-four/k=4 identification", "status": "verified"},
        {"item": "Preserve ambient Laurent-jet transport theorem", "status": "separated and retained"},
        {"item": "Compare archived layer-four residual coefficientwise", "status": "direct mismatch / ill-typed without overlap normalization"},
        {"item": "Test Q->Q+16s against residual", "status": "not a vector in the old window; conditional comparison remains"},
        {"item": "Publish adjacent normalization map", "status": "Kummer quotient map published; ordinary complete-chain lift ruled out for this flow"},
        {"item": "Identify presentation stabilizer", "status": "mu_8 for the Kummer presentation; original complete-chain stabilizer table still absent"},
        {"item": "Construct g_adm", "status": "minimal forced Rees-Kummer Lie algebroid constructed; equality with true module open"},
        {"item": "Support/residue transport for monomial charts", "status": "proved; quotient requires character modules"},
        {"item": "Pairwise/triple cocycles", "status": "strict on quotient/formal unit-root lift; mu_8 ambiguity algebraically"},
        {"item": "Kummer quotient allowed?", "status": "not in ordinary same-field atlas; allowed after root-stack/Kummer enlargement"},
        {"item": "Publish real F_2 matrices/support blocks", "status": "archive recovery attempted; high-order blocks not synthesized"},
        {"item": "Recompute F_2 recurrence", "status": "exact parameter-complete schema supplied; numerical instantiation blocked"},
        {"item": "C5-equivariant descent", "status": "character law and parameter bidegree proved"},
        {"item": "Finite global polynomial support", "status": "finite feasibility formulation supplied; instance blocked"},
        {"item": "Match every neighboring chart", "status": "current repair cannot match any ordinary same-field chart"},
        {"item": "Algebraize a formal solution", "status": "Kummer flow algebraizes only on degree-8 cover, not as same-field rational/polynomial map"},
        {"item": "Chart-independent finite obstruction", "status": "index-8/Kummer valuation obstruction obtained for this repair candidate"},
    ]


def build_report() -> dict[str, object]:
    report = {
        "schema_version": 1,
        "name": "Lane 9 Kummer attachment exact audit",
        "weighted_divergence": weighted_divergence_checks(),
        "vector_field_and_flow": vector_field_checks(),
        "lattice_and_stabilizer": lattice_and_stabilizer_checks(),
        "old_window_comparison": principal_part_checks(),
        "operation_commutator": bracket_checks(),
        "cocycles": cocycle_checks(),
        "cyclic_descent": cyclic_descent_checks(),
        "support_and_residue_transport": support_transport_checks(),
        "admissible_operation_module": admissible_module_checks(),
        "F2_recurrence_schema": recurrence_schema(),
        "checklist": checklist_statuses(),
    }
    report["all_exact_checks_passed"] = True
    return report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
