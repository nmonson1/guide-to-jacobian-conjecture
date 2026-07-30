"""Exact chart-transition and dual-pairing checks."""
from __future__ import annotations
from typing import Any, Mapping, Sequence
from .fields import ContractError, ExactField
from .layer import LayerAudit
from .linear import Matrix, Vector, dot, matrix_product, matrix_vector_product, parse_matrix, parse_vector, rank, rank_of_vectors, row_matrix_product, vector_in_span


def _transport_vectors(vectors: Sequence[Vector], matrix: Matrix, field: ExactField) -> list[Vector]:
    return [matrix_vector_product(matrix, vector, field) for vector in vectors]


def audit_transition(field: ExactField, raw: Mapping[str, Any], layers: Mapping[str, LayerAudit]) -> dict[str, Any]:
    name = str(raw.get("name", "unnamed-transition"))
    from_id = str(raw.get("from"))
    to_id = str(raw.get("to"))
    if from_id not in layers or to_id not in layers:
        raise ContractError(f"{name}: transition references an unknown layer")
    source = layers[from_id].data
    target = layers[to_id].data
    deformation_map = parse_matrix(field, raw.get("deformation_map", []), rows=target.deformation_dimension, columns=source.deformation_dimension, name=f"{name}.deformation_map")
    equation_map = parse_matrix(field, raw.get("equation_map", []), rows=target.equation_dimension, columns=source.equation_dimension, name=f"{name}.equation_map")
    left = matrix_product(target.operator, deformation_map, left_rows=target.equation_dimension, middle=target.deformation_dimension, right_columns=source.deformation_dimension, field=field)
    right = matrix_product(equation_map, source.operator, left_rows=target.equation_dimension, middle=source.equation_dimension, right_columns=source.deformation_dimension, field=field)
    if left != right:
        raise ContractError(f"{name}: D_to*T_E != T_W*D_from")

    require_isomorphism = bool(raw.get("require_isomorphism", False))
    deformation_rank = rank(deformation_map, rows=target.deformation_dimension, columns=source.deformation_dimension, field=field)
    equation_rank = rank(equation_map, rows=target.equation_dimension, columns=source.equation_dimension, field=field)
    if require_isomorphism and (source.deformation_dimension != target.deformation_dimension or deformation_rank != source.deformation_dimension or source.equation_dimension != target.equation_dimension or equation_rank != source.equation_dimension):
        raise ContractError(f"{name}: declared isomorphism has deficient rank")

    span_checks: list[dict[str, Any]] = []
    raw_span_pairs = raw.get("operation_span_pairs", [])
    if not isinstance(raw_span_pairs, list):
        raise ContractError(f"{name}: operation_span_pairs must be a list")
    for index, pair in enumerate(raw_span_pairs):
        if not isinstance(pair, Mapping):
            raise ContractError(f"{name}: operation span pair {index} must be an object")
        from_action = str(pair.get("from"))
        to_action = str(pair.get("to"))
        if from_action not in source.actions or to_action not in target.actions:
            raise ContractError(f"{name}: operation span pair references an unknown action")
        transported = _transport_vectors(source.actions[from_action].basis, deformation_map, field)
        for vector in transported:
            if not vector_in_span(vector, target.actions[to_action].basis, ambient_dimension=target.deformation_dimension, field=field):
                raise ContractError(f"{name}: transported {from_action} is not contained in {to_action}")
        span_checks.append({"from": from_action, "to": to_action, "transported_rank": rank_of_vectors(transported, ambient_dimension=target.deformation_dimension, field=field), "inclusion_verified": True})

    dual_checks: list[dict[str, Any]] = []
    raw_dual_pairs = raw.get("dual_pairs", [])
    if not isinstance(raw_dual_pairs, list):
        raise ContractError(f"{name}: dual_pairs must be a list")
    parsed_dual_pairs: list[tuple[Vector, Vector]] = []
    for index, pair in enumerate(raw_dual_pairs):
        if not isinstance(pair, Mapping):
            raise ContractError(f"{name}: dual pair {index} must be an object")
        source_functional = parse_vector(field, pair.get("from", []), width=source.equation_dimension, name=f"{name}.dual_pairs[{index}].from")
        target_functional = parse_vector(field, pair.get("to", []), width=target.equation_dimension, name=f"{name}.dual_pairs[{index}].to")
        if row_matrix_product(target_functional, equation_map, field) != source_functional:
            raise ContractError(f"{name}: dual functional pullback does not match")
        if any(row_matrix_product(source_functional, source.operator, field)) or any(row_matrix_product(target_functional, target.operator, field)):
            raise ContractError(f"{name}: supplied dual functional is not left-null")
        parsed_dual_pairs.append((source_functional, target_functional))
        dual_checks.append({"index": index, "pullback_verified": True})

    forcing_check: dict[str, Any] | None = None
    if "forcing_pair" in raw:
        pair = raw["forcing_pair"]
        if not isinstance(pair, Mapping):
            raise ContractError(f"{name}: forcing_pair must be an object")
        source_forcing = parse_vector(field, pair.get("from", []), width=source.equation_dimension, name=f"{name}.forcing_pair.from")
        target_forcing = parse_vector(field, pair.get("to", []), width=target.equation_dimension, name=f"{name}.forcing_pair.to")
        if matrix_vector_product(equation_map, source_forcing, field) != target_forcing:
            raise ContractError(f"{name}: forcing vector does not transport")
        pairings = []
        for source_functional, target_functional in parsed_dual_pairs:
            source_pairing = dot(source_functional, source_forcing, field)
            target_pairing = dot(target_functional, target_forcing, field)
            if source_pairing != target_pairing:
                raise ContractError(f"{name}: obstruction pairing is not preserved")
            pairings.append(field.serialize(source_pairing))
        forcing_check = {"transport_verified": True, "dual_pairings_preserved": True, "pairings": pairings}

    result: dict[str, Any] = {
        "name": name,
        "from": from_id,
        "to": to_id,
        "chain_map_verified": True,
        "deformation_map_rank": deformation_rank,
        "equation_map_rank": equation_rank,
        "isomorphism_required": require_isomorphism,
        "operation_span_checks": span_checks,
        "dual_checks": dual_checks,
    }
    if forcing_check is not None:
        result["forcing_check"] = forcing_check
    return result
