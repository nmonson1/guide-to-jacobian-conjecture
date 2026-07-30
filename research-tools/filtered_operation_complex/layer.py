"""Layer parsing and quotient computation."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Sequence
from .fields import ContractError, ExactField
from .linear import Matrix, Vector, dot, independent_extension, left_nullspace, matrix_vector_product, nullspace, parse_generators, parse_matrix, parse_vector, row_matrix_product, serialize_vector, vector_in_span


@dataclass
class ActionSpace:
    name: str
    role: str
    parent: str | None
    labels: list[str]
    generators: list[Vector]
    basis: list[Vector]


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
    forcing: Vector | None
    obstruction_functionals: list[Vector]
    deformation_basis: list[str]
    equation_basis: list[str]
    metadata: Mapping[str, Any]


@dataclass
class LayerAudit:
    data: LayerData
    result: dict[str, Any]


def _basis_from_generators(generators: Sequence[Vector], *, ambient_dimension: int, field: ExactField) -> list[Vector]:
    basis, _ = independent_extension([], generators, ambient_dimension=ambient_dimension, field=field)
    return basis


def parse_layer(field: ExactField, raw: Mapping[str, Any], *, include_vectors: bool) -> LayerAudit:
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
    operator = parse_matrix(field, operator_values, rows=equation_dimension, columns=deformation_dimension, name=f"{identifier}.operator")
    deformation_basis = [str(value) for value in raw.get("deformation_basis", [f"e{index}" for index in range(deformation_dimension)])]
    equation_basis = [str(value) for value in raw.get("equation_basis", [f"w{index}" for index in range(equation_dimension)])]
    if len(deformation_basis) != deformation_dimension:
        raise ContractError(f"{identifier}: deformation_basis has the wrong length")
    if len(equation_basis) != equation_dimension:
        raise ContractError(f"{identifier}: equation_basis has the wrong length")

    kernel_basis = nullspace(operator, rows=equation_dimension, columns=deformation_dimension, field=field)
    left_kernel_basis = left_nullspace(operator, rows=equation_dimension, columns=deformation_dimension, field=field)

    raw_actions = raw.get("actions", [])
    if not isinstance(raw_actions, list):
        raise ContractError(f"{identifier}: actions must be a list")
    actions: dict[str, ActionSpace] = {}
    for index, action in enumerate(raw_actions):
        if not isinstance(action, Mapping):
            raise ContractError(f"{identifier}: action {index} must be an object")
        name = str(action.get("name", f"action-{index}"))
        if name in actions:
            raise ContractError(f"{identifier}: duplicate action name {name!r}")
        role = str(action.get("role", "operation"))
        parent = action.get("parent")
        if parent is not None:
            parent = str(parent)
        values = action.get("generators", [])
        if not isinstance(values, list):
            raise ContractError(f"{identifier}.{name}: generators must be a list")
        labels, generators = parse_generators(field, values, width=deformation_dimension, name=f"{identifier}.{name}")
        for generator_index, generator in enumerate(generators):
            if any(matrix_vector_product(operator, generator, field)):
                raise ContractError(f"{identifier}.{name}: generator {generator_index} is not in ker(D)")
        actions[name] = ActionSpace(name, role, parent, labels, generators, _basis_from_generators(generators, ambient_dimension=deformation_dimension, field=field))

    for action in actions.values():
        if action.parent is None:
            continue
        if action.parent not in actions:
            raise ContractError(f"{identifier}.{action.name}: unknown parent {action.parent!r}")
        for generator in action.basis:
            if not vector_in_span(generator, actions[action.parent].basis, ambient_dimension=deformation_dimension, field=field):
                raise ContractError(f"{identifier}.{action.name} is not contained in parent {action.parent}")

    raw_recharts = raw.get("recharts", [])
    if not isinstance(raw_recharts, list):
        raise ContractError(f"{identifier}: recharts must be a list")
    recharts: list[RechartSpace] = []
    for index, rechart in enumerate(raw_recharts):
        if not isinstance(rechart, Mapping):
            raise ContractError(f"{identifier}: rechart {index} must be an object")
        name = str(rechart.get("name", f"rechart-{index}"))
        values = rechart.get("generators", [])
        if not isinstance(values, list):
            raise ContractError(f"{identifier}.{name}: generators must be a list")
        labels, generators = parse_generators(field, values, width=deformation_dimension, name=f"{identifier}.{name}")
        for generator_index, generator in enumerate(generators):
            if any(matrix_vector_product(operator, generator, field)):
                raise ContractError(f"{identifier}.{name}: rechart generator {generator_index} is not in ker(D)")
        recharts.append(RechartSpace(name, labels, generators, _basis_from_generators(generators, ambient_dimension=deformation_dimension, field=field)))

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
        forcing = parse_vector(field, raw["forcing"], width=equation_dimension, name=f"{identifier}.forcing")

    raw_functionals = raw.get("obstruction_functionals", [])
    if not isinstance(raw_functionals, list):
        raise ContractError(f"{identifier}: obstruction_functionals must be a list")
    obstruction_functionals = [parse_vector(field, value.get("vector") if isinstance(value, Mapping) else value, width=equation_dimension, name=f"{identifier}.obstruction_functionals[{index}]") for index, value in enumerate(raw_functionals)]
    for index, functional in enumerate(obstruction_functionals):
        if any(row_matrix_product(functional, operator, field)):
            raise ContractError(f"{identifier}: obstruction functional {index} is not left-null")

    gauge_basis = _basis_from_generators([generator for name in gauge_actions for generator in actions[name].basis], ambient_dimension=deformation_dimension, field=field)
    rechart_generators = [generator for rechart in recharts for generator in rechart.basis]
    explained_basis, rechart_added = independent_extension(gauge_basis, rechart_generators, ambient_dimension=deformation_dimension, field=field)
    _, quotient_representatives = independent_extension(explained_basis, kernel_basis, ambient_dimension=deformation_dimension, field=field)

    action_result: list[dict[str, Any]] = []
    for action in actions.values():
        entry: dict[str, Any] = {
            "name": action.name,
            "role": action.role,
            "parent": action.parent,
            "generator_count": len(action.generators),
            "rank": len(action.basis),
            "contained_in_kernel": True,
            "parent_inclusion_verified": True,
        }
        if include_vectors:
            entry["basis"] = [serialize_vector(field, vector) for vector in action.basis]
        action_result.append(entry)

    rechart_result: list[dict[str, Any]] = []
    cumulative = list(gauge_basis)
    for rechart in recharts:
        cumulative, added = independent_extension(cumulative, rechart.basis, ambient_dimension=deformation_dimension, field=field)
        entry: dict[str, Any] = {
            "name": rechart.name,
            "generator_count": len(rechart.generators),
            "rank": len(rechart.basis),
            "increment_after_previous_spaces": len(added),
            "contained_in_kernel": True,
        }
        if include_vectors:
            entry["basis"] = [serialize_vector(field, vector) for vector in rechart.basis]
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
        result["forcing_pairings"] = [field.serialize(dot(functional, forcing, field)) for functional in obstruction_functionals]
    if include_vectors:
        result["kernel_basis"] = [serialize_vector(field, vector) for vector in kernel_basis]
        result["left_kernel_basis"] = [serialize_vector(field, vector) for vector in left_kernel_basis]
    result["quotient_representatives"] = [serialize_vector(field, vector) for vector in quotient_representatives]

    metadata = raw.get("metadata", {})
    if not isinstance(metadata, Mapping):
        raise ContractError(f"{identifier}: metadata must be an object")
    data = LayerData(identifier, deformation_dimension, equation_dimension, operator, kernel_basis, left_kernel_basis, actions, recharts, gauge_actions, forcing, obstruction_functionals, deformation_basis, equation_basis, metadata)
    return LayerAudit(data, result)
