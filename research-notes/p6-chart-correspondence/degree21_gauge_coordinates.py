#!/usr/bin/env python3
"""Express lower-face source-operation images in the archived t_{r,j} basis.

The residue-audit source chooses the deterministic RREF kernel basis and names
its free parameters

    (t1_0,t1_1),
    (t2_0,t2_1,t2_2),
    (t3_0,t3_1,t3_2),
    (t4_0).

This program rebuilds the same exact matrices over the pinned quintic field,
recovers the identical free-column basis, and gives coordinates of:

* every individually support-admissible Laurent monomial source field;
* a deterministic basis of the full support-admissible formal source space;
* the affine-polynomial subspace under X=x^-1, Y=x^4 y.

No manuscript fixed-chart quotient is assumed.  The output is a change-of-basis
audit that makes the missing filtered subgroup explicit in the raw parameter
coordinates.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

from degree21_lower_face_full_gauge import (
    exact_source_bounds,
    linear_combination,
    source_column,
)
from degree21_lower_face_replay import (
    FieldElement,
    Matrix,
    Poly,
    QuinticField,
    Vector,
    columns_to_matrix,
    determinant_layer,
    face_equation,
    independent_columns,
    load_full_layers,
    monomial,
    nullspace,
    output_vector,
    parse_face,
    rref,
    vector_image,
)
from degree21_subgroup_ladder import affine_polynomial_exponent


PARAMETER_NAMES = {
    1: ["t1_0", "t1_1"],
    2: ["t2_0", "t2_1", "t2_2"],
    3: ["t3_0", "t3_1", "t3_2"],
    4: ["t4_0"],
}


def field_vector_json(vector: Sequence[FieldElement]) -> list[list[dict[str, str]]]:
    return [entry.as_json() for entry in vector]


def sparse_coordinate_json(
    names: Sequence[str], vector: Sequence[FieldElement]
) -> list[dict[str, Any]]:
    return [
        {"parameter": name, "coefficient": coefficient.as_json()}
        for name, coefficient in zip(names, vector)
        if coefficient
    ]


def determinant_operator(
    field: QuinticField,
    r: int,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> tuple[Matrix, list[int]]:
    columns: list[Poly] = []
    for exponent in a_support:
        columns.append(
            determinant_layer(field, r, A0, B0, monomial(field, exponent), {})
        )
    for exponent in b_support:
        columns.append(
            determinant_layer(field, r, A0, B0, {}, monomial(field, exponent))
        )
    target_exponents = sorted(
        {exponent for column in columns for exponent in column}
    )
    return columns_to_matrix(field, columns, target_exponents), target_exponents


def kernel_data(
    field: QuinticField,
    operator: Matrix,
    ambient_dimension: int,
) -> tuple[list[Vector], list[int], list[int]]:
    _, pivots = rref(operator, columns=ambient_dimension, field=field)
    free_columns = [
        column for column in range(ambient_dimension) if column not in pivots
    ]
    basis = nullspace(operator, columns=ambient_dimension, field=field)
    if len(basis) != len(free_columns):
        raise AssertionError("kernel basis and free-column count disagree")
    for index, vector in enumerate(basis):
        for other, column in enumerate(free_columns):
            expected = field.one if index == other else field.zero
            if vector[column] != expected:
                raise AssertionError("kernel basis lost deterministic free coordinates")
    return basis, pivots, free_columns


def kernel_coordinates(
    field: QuinticField,
    operator: Matrix,
    vector: Vector,
    free_columns: Sequence[int],
    kernel_basis: Sequence[Vector],
) -> Vector:
    if any(vector_image(operator, vector, field)):
        raise ValueError("the vector is not in the determinant kernel")
    coordinates = [vector[column] for column in free_columns]
    reconstructed = [field.zero for _ in vector]
    for scalar, basis_vector in zip(coordinates, kernel_basis):
        for index, value in enumerate(basis_vector):
            reconstructed[index] = reconstructed[index] + scalar * value
    if reconstructed != vector:
        raise AssertionError("free-column coordinates do not reconstruct the vector")
    return coordinates


def constrained_source_basis(
    field: QuinticField,
    r: int,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    a_support: Sequence[int],
    b_support: Sequence[int],
    source_exponents: Sequence[int],
) -> tuple[list[Vector], list[Poly], list[Poly], list[int]]:
    allowed_a = set(a_support)
    allowed_b = set(b_support)
    a_columns: list[Poly] = []
    b_columns: list[Poly] = []
    individually_admissible: list[int] = []
    for k in source_exponents:
        a, b = source_column(field, r, k, A0, B0)
        a_columns.append(a)
        b_columns.append(b)
        if all(exponent in allowed_a for exponent in a) and all(
            exponent in allowed_b for exponent in b
        ):
            individually_admissible.append(k)

    forbidden_a = sorted(
        {
            exponent
            for column in a_columns
            for exponent in column
            if exponent not in allowed_a
        }
    )
    forbidden_b = sorted(
        {
            exponent
            for column in b_columns
            for exponent in column
            if exponent not in allowed_b
        }
    )
    constraints: Matrix = []
    for exponent in forbidden_a:
        constraints.append(
            [column.get(exponent, field.zero) for column in a_columns]
        )
    for exponent in forbidden_b:
        constraints.append(
            [column.get(exponent, field.zero) for column in b_columns]
        )
    basis = nullspace(
        constraints, columns=len(source_exponents), field=field
    )
    return basis, a_columns, b_columns, individually_admissible


def source_terms(
    exponents: Sequence[int], vector: Sequence[FieldElement]
) -> list[dict[str, Any]]:
    return [
        {"k": exponent, "coefficient": coefficient.as_json()}
        for exponent, coefficient in zip(exponents, vector)
        if coefficient
    ]


def image_of_source_vector(
    field: QuinticField,
    source_vector: Sequence[FieldElement],
    a_columns: Sequence[Poly],
    b_columns: Sequence[Poly],
    a_support: Sequence[int],
    b_support: Sequence[int],
) -> Vector:
    a = linear_combination(field, a_columns, source_vector)
    b = linear_combination(field, b_columns, source_vector)
    return output_vector(field, a, b, a_support, b_support)


def analyze_layer(
    field: QuinticField,
    A0: Mapping[int, FieldElement],
    B0: Mapping[int, FieldElement],
    layer: Mapping[str, Any],
) -> dict[str, Any]:
    r = int(layer["r"])
    a_support = list(layer["a_support"])
    b_support = list(layer["b_support"])
    ambient_dimension = len(a_support) + len(b_support)
    operator, target_exponents = determinant_operator(
        field, r, A0, B0, a_support, b_support
    )
    kernel_basis, pivots, free_columns = kernel_data(
        field, operator, ambient_dimension
    )
    names = PARAMETER_NAMES[r]
    if len(names) != len(kernel_basis):
        raise ValueError(
            f"layer {r}: archived parameter count {len(names)} does not match "
            f"kernel dimension {len(kernel_basis)}"
        )

    lower, upper, _, _ = exact_source_bounds(r, a_support, b_support)
    all_exponents = list(range(lower, upper + 1))
    formal_basis, a_columns, b_columns, individually_admissible = (
        constrained_source_basis(
            field,
            r,
            A0,
            B0,
            a_support,
            b_support,
            all_exponents,
        )
    )

    monomial_records: list[dict[str, Any]] = []
    for k in individually_admissible:
        source_vector = [
            field.one if exponent == k else field.zero
            for exponent in all_exponents
        ]
        output = image_of_source_vector(
            field,
            source_vector,
            a_columns,
            b_columns,
            a_support,
            b_support,
        )
        coordinates = kernel_coordinates(
            field, operator, output, free_columns, kernel_basis
        )
        monomial_records.append(
            {
                "k": k,
                "coordinates": sparse_coordinate_json(names, coordinates),
            }
        )

    formal_records: list[dict[str, Any]] = []
    for index, source_vector in enumerate(formal_basis):
        output = image_of_source_vector(
            field,
            source_vector,
            a_columns,
            b_columns,
            a_support,
            b_support,
        )
        coordinates = kernel_coordinates(
            field, operator, output, free_columns, kernel_basis
        )
        formal_records.append(
            {
                "basis_index": index,
                "source_terms": source_terms(all_exponents, source_vector),
                "coordinates": sparse_coordinate_json(names, coordinates),
            }
        )

    polynomial_exponents = [
        exponent
        for exponent in all_exponents
        if affine_polynomial_exponent(r, exponent)
    ]
    polynomial_basis, polynomial_a_columns, polynomial_b_columns, _ = (
        constrained_source_basis(
            field,
            r,
            A0,
            B0,
            a_support,
            b_support,
            polynomial_exponents,
        )
    )
    polynomial_records: list[dict[str, Any]] = []
    for index, source_vector in enumerate(polynomial_basis):
        output = image_of_source_vector(
            field,
            source_vector,
            polynomial_a_columns,
            polynomial_b_columns,
            a_support,
            b_support,
        )
        coordinates = kernel_coordinates(
            field, operator, output, free_columns, kernel_basis
        )
        polynomial_records.append(
            {
                "basis_index": index,
                "source_terms": source_terms(polynomial_exponents, source_vector),
                "coordinates": sparse_coordinate_json(names, coordinates),
            }
        )

    formal_coordinate_vectors = [
        [record_coefficient(names, record["coordinates"], name, field) for name in names]
        for record in formal_records
    ]
    if len(independent_columns(field, formal_coordinate_vectors, len(names))) != len(names):
        raise AssertionError(f"layer {r}: formal source image does not span the kernel")

    return {
        "r": r,
        "parameter_names": names,
        "source_basis_order": [
            *({"type": "P", "z_exponent": exponent} for exponent in a_support),
            *({"type": "Q", "z_exponent": exponent} for exponent in b_support),
        ],
        "target_z_exponents": target_exponents,
        "pivot_columns": pivots,
        "free_columns": free_columns,
        "kernel_basis": [
            {
                "parameter": name,
                "vector": field_vector_json(vector),
            }
            for name, vector in zip(names, kernel_basis)
        ],
        "individually_admissible_monomials": monomial_records,
        "formal_source_basis": formal_records,
        "affine_polynomial_source_basis": polynomial_records,
    }


def record_coefficient(
    names: Sequence[str],
    sparse: Sequence[Mapping[str, Any]],
    name: str,
    field: QuinticField,
) -> FieldElement:
    for entry in sparse:
        if entry["parameter"] == name:
            return field.element(
                [
                    int(item["num"]) / int(item["den"])
                    for item in entry["coefficient"]
                ]
            )
    return field.zero


def analyze(face_path: Path, support_path: Path) -> dict[str, Any]:
    field, A0, B0 = parse_face(face_path)
    if face_equation(field, A0, B0) != {2: field.one}:
        raise ValueError("the reconstructed leading face does not satisfy Psi=z^2")
    layers = load_full_layers(support_path, [1, 2, 3, 4])
    results = [analyze_layer(field, A0, B0, layer) for layer in layers]
    return {
        "schema_version": 1,
        "name": "degree-21 source images in archived kernel coordinates",
        "parameter_order": [name for r in range(1, 5) for name in PARAMETER_NAMES[r]],
        "coordinate_basis": (
            "deterministic RREF free-column kernel basis used by the archived "
            "residue-audit source"
        ),
        "layers": results,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("face", type=Path)
    parser.add_argument("supports", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = analyze(args.face, args.supports)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"degree21_gauge_coordinates: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
