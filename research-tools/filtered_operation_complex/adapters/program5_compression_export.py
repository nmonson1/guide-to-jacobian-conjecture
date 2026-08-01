#!/usr/bin/env python3
"""Export the exact public Program 5 compression calculation.

This adapter reconstructs the weight-preserving quadratic source-field space
and the two exact linear systems in the public Program 5 supplement:

* the affine row-killing system for the output rows ``a,d,q,h,k``;
* the tangent system to the rank-at-most-six cubic-coordinate locus at
  ``P0=-d^2 e_a``.

It emits a generic filtered-operation-complex contract and an exact report.
The exported operation spaces are *candidate source-operation directions*.
They are deliberately not declared to be polynomial automorphisms, stable
presentation changes, or true gauge directions.

The supplement proves that the affine row-killing system has a 20-dimensional
direction space, the rank-six tangent system has dimension 22, and the
12-parameter family displayed in ``extensions_verifier.py`` lies in both.
It also verifies that the quartic functional Lambda_4 is identically one on
the affine 20-dimensional solution slice.  The latter is nonlinear metadata;
it is not represented as a linear obstruction functional in the generic
complex.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import sys
from itertools import combinations_with_replacement
from pathlib import Path
from typing import Any, Mapping, Sequence

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from ..core import ContractError, analyze_document


HERE = Path(__file__).resolve()
PACKAGE_ROOT = HERE.parents[1]
DEFAULT_SOURCE = (
    PACKAGE_ROOT
    / "intake"
    / "program5"
    / "focused"
    / "extensions_verifier.py"
)


def _load_source(path: Path) -> tuple[Any, str]:
    if not path.is_file():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location(
        "program5_public_extensions_verifier",
        path,
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        spec.loader.exec_module(module)
    return module, captured.getvalue()


def _q(value: Any) -> int | str:
    value = sp.Rational(value)
    if value.q == 1:
        return int(value.p)
    return f"{int(value.p)}/{int(value.q)}"


def _matrix_json(matrix: sp.MatrixBase) -> list[list[int | str]]:
    return [
        [_q(matrix[row, column]) for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def _columns_json(vectors: Sequence[sp.MatrixBase], rows: int) -> list[list[int | str]]:
    return [
        [_q(vector[row, 0]) for vector in vectors]
        for row in range(rows)
    ]


def _monomial_label(expression: sp.Expr) -> str:
    return str(expression).replace("**", "^").replace(" ", "")


def _rref_system(
    matrix: sp.Matrix,
    rhs: sp.Matrix | None = None,
) -> tuple[sp.Matrix, sp.Matrix | None, int]:
    if rhs is None:
        reduced, pivots = matrix.rref()
        rank = len(pivots)
        return reduced[:rank, :], None, rank

    augmented = matrix.row_join(rhs)
    reduced, pivots = augmented.rref()
    if matrix.cols in pivots:
        raise AssertionError("the exported affine system is inconsistent")
    rank = len(pivots)
    return reduced[:rank, : matrix.cols], reduced[:rank, matrix.cols], rank


def _basis_index(
    basis: Sequence[tuple[int, sp.Expr]],
    row: int,
    monomial: sp.Expr,
) -> int:
    target = sp.expand(monomial)
    for index, (candidate_row, candidate_monomial) in enumerate(basis):
        if candidate_row == row and sp.expand(candidate_monomial - target) == 0:
            return index
    raise KeyError((row, monomial))


def _coordinate_vector(dimension: int, index: int, value: Any = 1) -> sp.Matrix:
    vector = sp.zeros(dimension, 1)
    vector[index, 0] = sp.Rational(value)
    return vector


def _sparse_vector(
    vector: sp.Matrix,
    labels: Sequence[str],
) -> list[dict[str, Any]]:
    return [
        {"coordinate": labels[index], "coefficient": _q(vector[index, 0])}
        for index in range(vector.rows)
        if vector[index, 0] != 0
    ]


def build_export(source_path: Path = DEFAULT_SOURCE) -> tuple[dict[str, Any], dict[str, Any]]:
    source, source_stdout = _load_source(source_path)
    V = tuple(source.V)
    Q = sp.Matrix(source.Q)
    C = sp.Matrix(source.C)
    weights = source.weights
    variable_names = [str(value) for value in V]
    n = len(V)
    if n != 11:
        raise AssertionError(f"expected eleven variables, found {n}")

    quadratic_monomials = [
        sp.prod(V[index] for index in indices)
        for indices in combinations_with_replacement(range(n), 2)
    ]

    def weight(monomial: sp.Expr) -> int:
        exponents = sp.Poly(monomial, *V).monoms()[0]
        return sum(exponents[index] * weights[V[index]] for index in range(n))

    operation_basis: list[tuple[int, sp.Expr]] = []
    for row, variable in enumerate(V):
        for monomial in quadratic_monomials:
            if weight(monomial) == weights[variable]:
                operation_basis.append((row, monomial))
    if len(operation_basis) != 115:
        raise AssertionError(
            f"expected 115 weight-preserving quadratic fields, found {len(operation_basis)}"
        )
    operation_labels = [
        f"e_{variable_names[row]}*{_monomial_label(monomial)}"
        for row, monomial in operation_basis
    ]

    JQ = Q.jacobian(V)
    brackets: list[sp.Matrix] = []
    for row, monomial in operation_basis:
        field = sp.zeros(n, 1)
        field[row, 0] = monomial
        brackets.append(
            sp.Matrix(
                [
                    sp.expand(value)
                    for value in JQ * field - field.jacobian(V) * Q
                ]
            )
        )

    cubic_monomials = [
        sp.prod(V[index] for index in indices)
        for indices in combinations_with_replacement(range(n), 3)
    ]
    selected_rows = (3, 6, 7, 9, 10)
    selected_names = [variable_names[index] for index in selected_rows]
    constraint_rows: list[list[sp.Expr]] = []
    affine_rhs: list[sp.Expr] = []
    original_constraint_labels: list[str] = []
    for output_row in selected_rows:
        base_polynomial = sp.Poly(C[output_row], *V)
        bracket_polynomials = [
            sp.Poly(bracket[output_row], *V) for bracket in brackets
        ]
        for monomial in cubic_monomials:
            coefficients = [
                polynomial.coeff_monomial(monomial)
                for polynomial in bracket_polynomials
            ]
            base_coefficient = base_polynomial.coeff_monomial(monomial)
            if base_coefficient or any(coefficients):
                constraint_rows.append(coefficients)
                affine_rhs.append(-base_coefficient)
                original_constraint_labels.append(
                    f"{variable_names[output_row]}:{_monomial_label(monomial)}"
                )

    constraint_matrix = sp.Matrix(constraint_rows)
    rhs_vector = sp.Matrix(affine_rhs)
    constraint_rank = DomainMatrix.from_Matrix(constraint_matrix).rank()
    augmented_rank = DomainMatrix.from_Matrix(
        constraint_matrix.row_join(rhs_vector)
    ).rank()
    if (constraint_rank, augmented_rank) != (95, 95):
        raise AssertionError(
            f"unexpected row-killing ranks {(constraint_rank, augmented_rank)}"
        )

    reduced_constraints, reduced_rhs, reduced_rank = _rref_system(
        constraint_matrix,
        rhs_vector,
    )
    if reduced_rhs is None or reduced_rank != 95:
        raise AssertionError("failed to reduce the row-killing system")
    row_killing_kernel = reduced_constraints.nullspace()
    if len(row_killing_kernel) != 20:
        raise AssertionError(
            f"expected 20 row-killing directions, found {len(row_killing_kernel)}"
        )

    p0_index = _basis_index(operation_basis, 3, source.d**2)
    p0 = _coordinate_vector(115, p0_index, -1)
    if constraint_matrix * p0 != rhs_vector:
        raise AssertionError("P0=-d^2 e_a does not solve the affine system")

    sigma_monomials = list(source.Sigma)
    if len(sigma_monomials) != 12:
        raise AssertionError("the robust family no longer has twelve parameters")
    robust_directions = [
        _coordinate_vector(
            115,
            _basis_index(operation_basis, 8, monomial),
        )
        for monomial in sigma_monomials
    ]
    for vector in robust_directions:
        if constraint_matrix * vector != sp.zeros(constraint_matrix.rows, 1):
            raise AssertionError("a robust-family direction left the row-killing kernel")

    affine_solution = next(
        iter(sp.linsolve((constraint_matrix, rhs_vector)))
    )
    free_parameters = sorted(
        set().union(*(entry.free_symbols for entry in affine_solution)),
        key=str,
    )
    if len(free_parameters) != 20:
        raise AssertionError("the affine row-killing slice is not 20-dimensional")

    polynomial_field = sp.zeros(n, 1)
    for coefficient, (row, monomial) in zip(affine_solution, operation_basis):
        polynomial_field[row, 0] += coefficient * monomial
    polynomial_field = sp.Matrix(
        [sp.expand(value) for value in polynomial_field]
    )
    O4 = (
        C.jacobian(V) * polynomial_field
        - polynomial_field.jacobian(V) * C
        + sp.Rational(1, 2)
        * source.D2_11(Q, polynomial_field, polynomial_field)
        - polynomial_field.jacobian(V)
        * (JQ * polynomial_field - polynomial_field.jacobian(V) * Q)
        - sp.Rational(1, 2)
        * source.D2_11(polynomial_field, Q, Q)
    )
    quartic_value = sum(
        coefficient
        * sp.Poly(sp.expand(O4[row]), *V).coeff_monomial(monomial)
        for row, monomial, coefficient in source.terms
    )
    quartic_value = sp.factor(quartic_value)
    if quartic_value != 1:
        raise AssertionError(
            f"Lambda_4 is not constant one: {quartic_value}"
        )

    P0_polynomial = sp.zeros(n, 1)
    P0_polynomial[3, 0] = -source.d**2
    C0 = sp.Matrix(
        [
            sp.expand(value)
            for value in C + JQ * P0_polynomial - P0_polynomial.jacobian(V) * Q
        ]
    )
    coefficient_matrix = sp.zeros(n, len(cubic_monomials))
    for row, expression in enumerate(C0):
        polynomial = sp.Poly(expression, *V)
        for column, monomial in enumerate(cubic_monomials):
            coefficient_matrix[row, column] = polynomial.coeff_monomial(monomial)
    if coefficient_matrix.rank() != 6:
        raise AssertionError("the distinguished cubic jet does not have rank six")

    independent_rows = (0, 1, 2, 4, 5, 8)
    row_basis = coefficient_matrix[list(independent_rows), :]
    _, pivot_columns = row_basis.rref()
    pivot_columns = list(pivot_columns)
    pivot_minor = row_basis[:, pivot_columns]
    if pivot_minor.det() == 0:
        raise AssertionError("the selected rank-six minor vanished")
    nonpivot_columns = [
        column
        for column in range(len(cubic_monomials))
        if column not in pivot_columns
    ]
    inverse_minor = pivot_minor.inv()

    bracket_coefficient_matrices: list[sp.Matrix] = []
    for bracket in brackets:
        matrix = sp.zeros(n, len(cubic_monomials))
        for row, expression in enumerate(bracket):
            polynomial = sp.Poly(expression, *V)
            for column, monomial in enumerate(cubic_monomials):
                matrix[row, column] = polynomial.coeff_monomial(monomial)
        bracket_coefficient_matrices.append(matrix)

    tangent_entries: dict[tuple[int, int], sp.Expr] = {}
    for operation_column, matrix in enumerate(bracket_coefficient_matrices):
        offset = 0
        for zero_row in selected_rows:
            row = matrix[zero_row, :]
            residual = row - row[:, pivot_columns] * inverse_minor * row_basis
            for local_column, cubic_column in enumerate(nonpivot_columns):
                value = residual[0, cubic_column]
                if value:
                    tangent_entries[(offset + local_column, operation_column)] = value
            offset += len(nonpivot_columns)
    tangent_matrix = sp.SparseMatrix(
        len(selected_rows) * len(nonpivot_columns),
        115,
        tangent_entries,
    )
    tangent_rank = DomainMatrix.from_Matrix(
        tangent_matrix,
        fmt="sparse",
    ).rank()
    if tangent_rank != 93:
        raise AssertionError(f"expected tangent rank 93, found {tangent_rank}")
    tangent_dense = sp.Matrix(tangent_matrix)
    reduced_tangent, _, reduced_tangent_rank = _rref_system(tangent_dense)
    if reduced_tangent_rank != 93:
        raise AssertionError("failed to reduce the rank-six tangent system")
    rank_six_kernel = reduced_tangent.nullspace()
    if len(rank_six_kernel) != 22:
        raise AssertionError(
            f"expected 22 rank-six tangent directions, found {len(rank_six_kernel)}"
        )
    for vector in robust_directions:
        if tangent_dense * vector != sp.zeros(tangent_dense.rows, 1):
            raise AssertionError("a robust-family direction left the rank-six tangent")

    source_sha256 = hashlib.sha256(source_path.read_bytes()).hexdigest()
    robust_labels = [
        f"sigma_{_monomial_label(monomial)}"
        for monomial in sigma_monomials
    ]
    common_metadata = {
        "program": 5,
        "source_file": str(source_path),
        "source_sha256": source_sha256,
        "source_stdout": source_stdout.strip(),
        "operation_domain": (
            "weight-preserving quadratic vector fields in the normalized "
            "11-variable presentation"
        ),
        "operation_domain_dimension": 115,
        "selected_output_rows": selected_names,
        "classification_boundary": (
            "Candidate source-operation directions only. No claim that the "
            "full direction space consists of polynomial automorphisms or "
            "stable-presentation changes."
        ),
    }

    contract: dict[str, Any] = {
        "schema_version": 1,
        "name": "Exact Program 5 compression source-operation complex",
        "field": {"kind": "rational"},
        "report_options": {"include_vectors": False},
        "metadata": {
            "source_sha256": source_sha256,
            "quartic_functional": "Lambda_4",
            "quartic_value_on_affine_row_killing_slice": "1",
        },
        "layers": [
            {
                "id": "program5:affine-row-killing",
                "deformation_dimension": 115,
                "equation_dimension": 95,
                "deformation_basis": operation_labels,
                "equation_basis": [
                    f"row-killing-rref-{index}" for index in range(95)
                ],
                "operator": _matrix_json(reduced_constraints),
                "forcing": [_q(-reduced_rhs[row, 0]) for row in range(95)],
                "actions": [
                    {
                        "name": "row_killing_directions",
                        "role": "candidate_source_operation",
                        "source_dimension": 20,
                        "source_basis": [
                            f"row-killing-direction-{index}"
                            for index in range(20)
                        ],
                        "action_matrix": _columns_json(
                            row_killing_kernel,
                            115,
                        ),
                    },
                    {
                        "name": "robust_12_parameter_family",
                        "role": "explicit_source_operation_family",
                        "parent": "row_killing_directions",
                        "source_dimension": 12,
                        "source_basis": robust_labels,
                        "action_matrix": _columns_json(
                            robust_directions,
                            115,
                        ),
                    },
                ],
                "gauge_actions": [],
                "metadata": {
                    **common_metadata,
                    "original_equation_count": constraint_matrix.rows,
                    "original_constraint_labels": original_constraint_labels,
                    "constraint_rank": 95,
                    "augmented_rank": 95,
                    "affine_solution_dimension": 20,
                    "distinguished_particular_solution": _sparse_vector(
                        p0,
                        operation_labels,
                    ),
                    "quartic_functional": "Lambda_4",
                    "quartic_value_on_entire_affine_solution_slice": "1",
                },
            },
            {
                "id": "program5:rank-six-tangent",
                "deformation_dimension": 115,
                "equation_dimension": 93,
                "deformation_basis": operation_labels,
                "equation_basis": [
                    f"rank-six-tangent-rref-{index}" for index in range(93)
                ],
                "operator": _matrix_json(reduced_tangent),
                "actions": [
                    {
                        "name": "rank_six_tangent_directions",
                        "role": "candidate_source_operation",
                        "source_dimension": 22,
                        "source_basis": [
                            f"rank-six-tangent-direction-{index}"
                            for index in range(22)
                        ],
                        "action_matrix": _columns_json(
                            rank_six_kernel,
                            115,
                        ),
                    },
                    {
                        "name": "robust_12_parameter_family",
                        "role": "explicit_source_operation_family",
                        "parent": "rank_six_tangent_directions",
                        "source_dimension": 12,
                        "source_basis": robust_labels,
                        "action_matrix": _columns_json(
                            robust_directions,
                            115,
                        ),
                    },
                ],
                "gauge_actions": [],
                "metadata": {
                    **common_metadata,
                    "basepoint": "P0=-d^2 e_a",
                    "cubic_coordinate_rank_at_basepoint": 6,
                    "tangent_constraint_rank": 93,
                    "rank_six_tangent_dimension": 22,
                    "quartic_functional": "Lambda_4",
                    "quartic_value_at_basepoint": "1",
                },
            },
        ],
    }

    report = analyze_document(contract)
    affine_layer, tangent_layer = report["layers"]
    if not affine_layer.get("forcing_solvable"):
        raise AssertionError("generic engine rejected the affine row-killing system")
    if affine_layer["kernel_dimension"] != 20:
        raise AssertionError("generic engine lost the 20-dimensional affine direction space")
    if tangent_layer["kernel_dimension"] != 22:
        raise AssertionError("generic engine lost the 22-dimensional rank-six tangent")
    if affine_layer["actions"][0]["rank"] != 20:
        raise AssertionError("row-killing action map lost rank")
    if tangent_layer["actions"][0]["rank"] != 22:
        raise AssertionError("rank-six tangent action map lost rank")
    for layer in report["layers"]:
        if layer["actions"][1]["rank"] != 12:
            raise AssertionError("robust family lost rank")

    summary = {
        "schema_version": 1,
        "name": "Exact Program 5 compression export summary",
        "source_file": str(source_path),
        "source_sha256": source_sha256,
        "weight_preserving_quadratic_operation_dimension": 115,
        "affine_row_killing": {
            "selected_output_rows": selected_names,
            "original_equation_count": constraint_matrix.rows,
            "constraint_rank": 95,
            "augmented_rank": 95,
            "direction_dimension": 20,
            "distinguished_solution": "P0=-d^2 e_a",
        },
        "rank_six_tangent": {
            "basepoint": "P0=-d^2 e_a",
            "constraint_rank": 93,
            "tangent_dimension": 22,
        },
        "robust_family_dimension": 12,
        "quartic_functional": {
            "name": "Lambda_4",
            "value_on_entire_affine_row_killing_slice": _q(quartic_value),
        },
        "missing_input": (
            "The public supplement inspected here does not export the later "
            "109-direction/75-automorphism packet stated in the Program 5 "
            "handoff. This export must not be relabeled as that packet."
        ),
        "classification_boundary": common_metadata["classification_boundary"],
    }
    return contract, {"summary": summary, "report": report}


def _write(path: Path | None, value: Mapping[str, Any]) -> None:
    rendered = json.dumps(value, indent=2, sort_keys=True) + "\n"
    if path is None:
        sys.stdout.write(rendered)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered, encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="public extensions_verifier.py source",
    )
    parser.add_argument("--contract", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args(argv)
    try:
        contract, output = build_export(args.source)
    except (
        OSError,
        ValueError,
        TypeError,
        ImportError,
        AssertionError,
        ContractError,
    ) as exc:
        print(f"program5_compression_export: {exc}", file=sys.stderr)
        return 2

    if args.contract:
        _write(args.contract, contract)
    if args.report:
        _write(args.report, output["report"])
    if args.summary:
        _write(args.summary, output["summary"])
    if not any((args.contract, args.report, args.summary)):
        _write(None, output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
