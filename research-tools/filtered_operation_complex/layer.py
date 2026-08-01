"""Layer parsing and quotient computation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from .fields import ContractError, ExactField
from .linear import (
    Matrix,
    Vector,
    dot,
    independent_extension,
    left_nullspace,
    matrix_vector_product,
    nullspace,
    parse_generators,
    parse_matrix,
    parse_vector,
    row_matrix_product,
    serialize_vector,
    vector_in_span,
    vectors_to_column_matrix,
)


@dataclass
class ActionSpace:
    name: str
    role: str
    parent: str | None
    labels: list[str]
    generators: list[Vector]
    basis: list[Vector]
    source_dimension: int
    source_basis: list[str]
    action_matrix: Matrix
    source_stabilizer_basis: list[Vector]
    input_form: str


@dataclass
class RechartSpace:
    name: str
    labels: list[str]
    generators: list[Vector]
    basis: list[Vector]


@dataclass
class LayerData:
    identifier: str
    deformation_dimension: int
    equation_dimension: int
    operator: Matrix
    kernel_basis: list[Vector]
    left_kernel_basis: list[Vector]
    actions: dict[str, ActionSpace]
    recharts: list[RechartSpace]
    gauge_actions: list[str]
    gauge_basis: list[Vector]
    explained_basis: list[Vector]
    quotient_representatives: list[Vector]
    forcing: Vector | None
    obstruction_functionals: list[Vector]
    deformation_basis: list[str]
    equation_basis: list[str]
    metadata: Mapping[str, Any]


@dataclass
class LayerAudit:
    data: LayerData
    result: dict[str, Any]


def _serialize_matrix(field: ExactField, matrix: Matrix) -> list[list[Any]]:
    return [serialize_vector(field, row) for row in matrix]


def _basis_from_generators(
    generators: Sequence[Vector],
    *,
    ambient_dimension: int,
    field: ExactField,
) -> list[Vector]:
    basis, _ = independent_extension(
        [],
        generators,
        ambient_dimension=ambient_dimension,
        field=field,
    )
    return basis


def _columns(matrix: Matrix, *, rows: int, columns: int) -> list[Vector]:
    return [
        [matrix[row][column] for row in range(rows)]
        for column in range(columns)
    ]


def _parse_source_basis(
    raw: Any,
    *,
    dimension: int,
    default: Sequence[str],
    name: str,
) -> list[str]:
    if raw is None:
        return list(default)
    if not isinstance(raw, list):
        raise ContractError(f"{name}: source_basis must be a list")
    basis = [str(value) for value in raw]
    if len(basis) != dimension:
        raise ContractError(
            f"{name}: source_basis has length {len(basis)}, expected {dimension}"
        )
    return basis


def _parse_action(
    field: ExactField,
    action: Mapping[str, Any],
    *,
    identifier: str,
    index: int,
    deformation_dimension: int,
    operator: Matrix,
) -> ActionSpace:
    name = str(action.get("name", f"action-{index}"))
    role = str(action.get("role", "operation"))
    parent = action.get("parent")
    if parent is not None:
        parent = str(parent)

    has_generators = "generators" in action
    has_matrix = "action_matrix" in action
    if has_generators == has_matrix:
        raise ContractError(
            f"{identifier}.{name}: supply exactly one of generators or action_matrix"
        )

    if has_generators:
        values = action.get("generators")
        if not isinstance(values, list):
            raise ContractError(f"{identifier}.{name}: generators must be a list")
        labels, generators = parse_generators(
            field,
            values,
            width=deformation_dimension,
            name=f"{identifier}.{name}",
        )
        source_dimension = len(generators)
        declared_dimension = action.get("source_dimension")
        if declared_dimension is not None and declared_dimension != source_dimension:
            raise ContractError(
                f"{identifier}.{name}: source_dimension does not match generators"
            )
        source_basis = _parse_source_basis(
            action.get("source_basis"),
            dimension=source_dimension,
            default=labels,
            name=f"{identifier}.{name}",
        )
        action_matrix = vectors_to_column_matrix(
            generators,
            ambient_dimension=deformation_dimension,
            field=field,
        )
        input_form = "generators"
    else:
        values = action.get("action_matrix")
        if not isinstance(values, list):
            raise ContractError(f"{identifier}.{name}: action_matrix must be a list")
        source_dimension = action.get("source_dimension")
        if not isinstance(source_dimension, int):
            if deformation_dimension:
                if len(values) != deformation_dimension or not values:
                    raise ContractError(
                        f"{identifier}.{name}: cannot infer source_dimension"
                    )
                first_row = values[0]
                if not isinstance(first_row, list):
                    raise ContractError(
                        f"{identifier}.{name}: action_matrix rows must be lists"
                    )
                source_dimension = len(first_row)
            else:
                raise ContractError(
                    f"{identifier}.{name}: source_dimension is required "
                    "for an action into the zero deformation space"
                )
        if source_dimension < 0:
            raise ContractError(
                f"{identifier}.{name}: source_dimension must be nonnegative"
            )
        source_basis = _parse_source_basis(
            action.get("source_basis"),
            dimension=source_dimension,
            default=[f"u{column}" for column in range(source_dimension)],
            name=f"{identifier}.{name}",
        )
        action_matrix = parse_matrix(
            field,
            values,
            rows=deformation_dimension,
            columns=source_dimension,
            name=f"{identifier}.{name}.action_matrix",
        )
        generators = _columns(
            action_matrix,
            rows=deformation_dimension,
            columns=source_dimension,
        )
        labels = list(source_basis)
        input_form = "action_matrix"

    for generator_index, generator in enumerate(generators):
        if any(matrix_vector_product(operator, generator, field)):
            raise ContractError(
                f"{identifier}.{name}: source basis vector {generator_index} "
                "does not map into ker(D)"
            )

    basis = _basis_from_generators(
        generators,
        ambient_dimension=deformation_dimension,
        field=field,
    )
    source_stabilizer_basis = nullspace(
        action_matrix,
        rows=deformation_dimension,
        columns=source_dimension,
        field=field,
    )
    if len(basis) + len(source_stabilizer_basis) != source_dimension:
        raise ContractError(f"{identifier}.{name}: action rank-nullity failed")

    return ActionSpace(
        name=name,
        role=role,
        parent=parent,
        labels=labels,
        generators=generators,
        basis=basis,
        source_dimension=source_dimension,
        source_basis=source_basis,
        action_matrix=action_matrix,
        source_stabilizer_basis=source_stabilizer_basis,
        input_form=input_form,
    )


def parse_layer(
    field: ExactField,
    raw: Mapping[str, Any],
    *,
    include_vectors: bool,
) -> LayerAudit:
    identifier = str(raw.get("id", raw.get("label", "unnamed-layer")))
    deformation_dimension = raw.get("deformation_dimension")
    equation_dimension = raw.get("equation_dimension")
    operator_values = raw.get("operator")
    if not isinstance(operator_values, list):
        raise ContractError(f"{identifier}: operator must be a list")
    if not isinstance(deformation_dimension, int):
        deformation_dimension = len(operator_values[0]) if operator_values else None
    if not isinstance(equation_dimension, int):
        equation_dimension = len(operator_values)
    if not isinstance(deformation_dimension, int) or deformation_dimension < 0:
        raise ContractError(f"{identifier}: deformation_dimension is required")
    if equation_dimension < 0:
        raise ContractError(f"{identifier}: equation_dimension must be nonnegative")
    operator = parse_matrix(
        field,
        operator_values,
        rows=equation_dimension,
        columns=deformation_dimension,
        name=f"{identifier}.operator",
    )
    deformation_basis = [
        str(value)
        for value in raw.get(
            "deformation_basis",
            [f"e{index}" for index in range(deformation_dimension)],
        )
    ]
    equation_basis = [
        str(value)
        for value in raw.get(
            "equation_basis",
            [f"w{index}" for index in range(equation_dimension)],
        )
    ]
    if len(deformation_basis) != deformation_dimension:
        raise ContractError(f"{identifier}: deformation_basis has the wrong length")
    if len(equation_basis) != equation_dimension:
        raise ContractError(f"{identifier}: equation_basis has the wrong length")

    kernel_basis = nullspace(
        operator,
        rows=equation_dimension,
        columns=deformation_dimension,
        field=field,
    )
    left_kernel_basis = left_nullspace(
        operator,
        rows=equation_dimension,
        columns=deformation_dimension,
        field=field,
    )

    raw_actions = raw.get("actions", [])
    if not isinstance(raw_actions, list):
        raise ContractError(f"{identifier}: actions must be a list")
    actions: dict[str, ActionSpace] = {}
    for index, action in enumerate(raw_actions):
        if not isinstance(action, Mapping):
            raise ContractError(f"{identifier}: action {index} must be an object")
        parsed = _parse_action(
            field,
            action,
            identifier=identifier,
            index=index,
            deformation_dimension=deformation_dimension,
            operator=operator,
        )
        if parsed.name in actions:
            raise ContractError(
                f"{identifier}: duplicate action name {parsed.name!r}"
            )
        actions[parsed.name] = parsed

    for action in actions.values():
        if action.parent is None:
            continue
        if action.parent not in actions:
            raise ContractError(
                f"{identifier}.{action.name}: unknown parent {action.parent!r}"
            )
        for generator in action.basis:
            if not vector_in_span(
                generator,
                actions[action.parent].basis,
                ambient_dimension=deformation_dimension,
                field=field,
            ):
                raise ContractError(
                    f"{identifier}.{action.name} is not contained in "
                    f"parent {action.parent}"
                )

    raw_recharts = raw.get("recharts", [])
    if not isinstance(raw_recharts, list):
        raise ContractError(f"{identifier}: recharts must be a list")
    recharts: list[RechartSpace] = []
    rechart_names: set[str] = set()
    for index, rechart in enumerate(raw_recharts):
        if not isinstance(rechart, Mapping):
            raise ContractError(f"{identifier}: rechart {index} must be an object")
        name = str(rechart.get("name", f"rechart-{index}"))
        if name in rechart_names:
            raise ContractError(f"{identifier}: duplicate rechart name {name!r}")
        rechart_names.add(name)
        values = rechart.get("generators", [])
        if not isinstance(values, list):
            raise ContractError(f"{identifier}.{name}: generators must be a list")
        labels, generators = parse_generators(
            field,
            values,
            width=deformation_dimension,
            name=f"{identifier}.{name}",
        )
        for generator_index, generator in enumerate(generators):
            if any(matrix_vector_product(operator, generator, field)):
                raise ContractError(
                    f"{identifier}.{name}: rechart generator {generator_index} "
                    "is not in ker(D)"
                )
        recharts.append(
            RechartSpace(
                name,
                labels,
                generators,
                _basis_from_generators(
                    generators,
                    ambient_dimension=deformation_dimension,
                    field=field,
                ),
            )
        )

    gauge_actions = raw.get("gauge_actions")
    if gauge_actions is None:
        gauge_action = raw.get("gauge_action")
        gauge_actions = [] if gauge_action is None else [gauge_action]
    if not isinstance(gauge_actions, list):
        raise ContractError(f"{identifier}: gauge_actions must be a list")
    gauge_actions = [str(name) for name in gauge_actions]
    for name in gauge_actions:
        if name not in actions:
            raise ContractError(f"{identifier}: unknown gauge action {name!r}")

    forcing: Vector | None = None
    if "forcing" in raw:
        if not isinstance(raw["forcing"], list):
            raise ContractError(f"{identifier}: forcing must be a vector")
        forcing = parse_vector(
            field,
            raw["forcing"],
            width=equation_dimension,
            name=f"{identifier}.forcing",
        )

    raw_functionals = raw.get("obstruction_functionals", [])
    if not isinstance(raw_functionals, list):
        raise ContractError(
            f"{identifier}: obstruction_functionals must be a list"
        )
    obstruction_functionals = [
        parse_vector(
            field,
            value.get("vector") if isinstance(value, Mapping) else value,
            width=equation_dimension,
            name=f"{identifier}.obstruction_functionals[{index}]",
        )
        for index, value in enumerate(raw_functionals)
    ]
    for index, functional in enumerate(obstruction_functionals):
        if any(row_matrix_product(functional, operator, field)):
            raise ContractError(
                f"{identifier}: obstruction functional {index} is not left-null"
            )

    gauge_basis = _basis_from_generators(
        [
            generator
            for name in gauge_actions
            for generator in actions[name].basis
        ],
        ambient_dimension=deformation_dimension,
        field=field,
    )
    rechart_generators = [
        generator
        for rechart in recharts
        for generator in rechart.basis
    ]
    explained_basis, rechart_added = independent_extension(
        gauge_basis,
        rechart_generators,
        ambient_dimension=deformation_dimension,
        field=field,
    )
    _, quotient_representatives = independent_extension(
        explained_basis,
        kernel_basis,
        ambient_dimension=deformation_dimension,
        field=field,
    )

    action_result: list[dict[str, Any]] = []
    for action in actions.values():
        entry: dict[str, Any] = {
            "name": action.name,
            "role": action.role,
            "parent": action.parent,
            "input_form": action.input_form,
            "source_dimension": action.source_dimension,
            "source_basis": action.source_basis,
            "source_stabilizer_dimension": len(action.source_stabilizer_basis),
            "generator_count": len(action.generators),
            "rank": len(action.basis),
            "rank_nullity_verified": True,
            "contained_in_kernel": True,
            "parent_inclusion_verified": True,
        }
        if include_vectors:
            entry["action_matrix"] = _serialize_matrix(
                field,
                action.action_matrix,
            )
            entry["source_stabilizer_basis"] = [
                serialize_vector(field, vector)
                for vector in action.source_stabilizer_basis
            ]
            entry["basis"] = [
                serialize_vector(field, vector)
                for vector in action.basis
            ]
        action_result.append(entry)

    rechart_result: list[dict[str, Any]] = []
    cumulative = list(gauge_basis)
    for rechart in recharts:
        cumulative, added = independent_extension(
            cumulative,
            rechart.basis,
            ambient_dimension=deformation_dimension,
            field=field,
        )
        entry: dict[str, Any] = {
            "name": rechart.name,
            "generator_count": len(rechart.generators),
            "rank": len(rechart.basis),
            "increment_after_previous_spaces": len(added),
            "contained_in_kernel": True,
        }
        if include_vectors:
            entry["basis"] = [
                serialize_vector(field, vector)
                for vector in rechart.basis
            ]
        rechart_result.append(entry)

    result: dict[str, Any] = {
        "id": identifier,
        "deformation_dimension": deformation_dimension,
        "equation_dimension": equation_dimension,
        "operator_rank": deformation_dimension - len(kernel_basis),
        "kernel_dimension": len(kernel_basis),
        "cokernel_dimension": len(left_kernel_basis),
        "actions": action_result,
        "gauge_actions": gauge_actions,
        "gauge_dimension": len(gauge_basis),
        "recharts": rechart_result,
        "rechart_increment": len(rechart_added),
        "explained_dimension": len(explained_basis),
        "unexplained_dimension": len(kernel_basis) - len(explained_basis),
        "obstruction_functional_count": len(obstruction_functionals),
        "obstruction_functionals_verified": True,
    }
    if forcing is not None:
        result["forcing_pairings"] = [
            field.serialize(dot(functional, forcing, field))
            for functional in obstruction_functionals
        ]
    if include_vectors:
        result["kernel_basis"] = [
            serialize_vector(field, vector)
            for vector in kernel_basis
        ]
        result["left_kernel_basis"] = [
            serialize_vector(field, vector)
            for vector in left_kernel_basis
        ]
        result["gauge_basis"] = [
            serialize_vector(field, vector)
            for vector in gauge_basis
        ]
        result["explained_basis"] = [
            serialize_vector(field, vector)
            for vector in explained_basis
        ]
    result["quotient_representatives"] = [
        serialize_vector(field, vector)
        for vector in quotient_representatives
    ]

    metadata = raw.get("metadata", {})
    if not isinstance(metadata, Mapping):
        raise ContractError(f"{identifier}: metadata must be an object")
    data = LayerData(
        identifier=identifier,
        deformation_dimension=deformation_dimension,
        equation_dimension=equation_dimension,
        operator=operator,
        kernel_basis=kernel_basis,
        left_kernel_basis=left_kernel_basis,
        actions=actions,
        recharts=recharts,
        gauge_actions=gauge_actions,
        gauge_basis=gauge_basis,
        explained_basis=explained_basis,
        quotient_representatives=quotient_representatives,
        forcing=forcing,
        obstruction_functionals=obstruction_functionals,
        deformation_basis=deformation_basis,
        equation_basis=equation_basis,
        metadata=metadata,
    )
    return LayerAudit(data, result)
