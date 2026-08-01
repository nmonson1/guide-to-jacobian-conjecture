"""Exact chart-transition, operation-map, and dual-pairing checks."""
from __future__ import annotations

from typing import Any, Mapping, Sequence

from .fields import ContractError, ExactField
from .layer import LayerAudit, RechartSpace
from .linear import (
    Matrix,
    Vector,
    dot,
    independent_extension,
    matrix_product,
    matrix_vector_product,
    parse_matrix,
    parse_vector,
    rank,
    rank_of_vectors,
    row_matrix_product,
    vector_in_span,
)


def _transport_vectors(
    vectors: Sequence[Vector],
    matrix: Matrix,
    field: ExactField,
) -> list[Vector]:
    return [matrix_vector_product(matrix, vector, field) for vector in vectors]


def _rechart_by_name(recharts: Sequence[RechartSpace]) -> dict[str, RechartSpace]:
    return {rechart.name: rechart for rechart in recharts}


def audit_transition(
    field: ExactField,
    raw: Mapping[str, Any],
    layers: Mapping[str, LayerAudit],
) -> dict[str, Any]:
    name = str(raw.get("name", "unnamed-transition"))
    from_id = str(raw.get("from"))
    to_id = str(raw.get("to"))
    if from_id not in layers or to_id not in layers:
        raise ContractError(f"{name}: transition references an unknown layer")
    source = layers[from_id].data
    target = layers[to_id].data
    deformation_map = parse_matrix(
        field,
        raw.get("deformation_map", []),
        rows=target.deformation_dimension,
        columns=source.deformation_dimension,
        name=f"{name}.deformation_map",
    )
    equation_map = parse_matrix(
        field,
        raw.get("equation_map", []),
        rows=target.equation_dimension,
        columns=source.equation_dimension,
        name=f"{name}.equation_map",
    )
    left = matrix_product(
        target.operator,
        deformation_map,
        left_rows=target.equation_dimension,
        middle=target.deformation_dimension,
        right_columns=source.deformation_dimension,
        field=field,
    )
    right = matrix_product(
        equation_map,
        source.operator,
        left_rows=target.equation_dimension,
        middle=source.equation_dimension,
        right_columns=source.deformation_dimension,
        field=field,
    )
    if left != right:
        raise ContractError(f"{name}: D_to*T_E != T_W*D_from")

    require_isomorphism = bool(raw.get("require_isomorphism", False))
    deformation_rank = rank(
        deformation_map,
        rows=target.deformation_dimension,
        columns=source.deformation_dimension,
        field=field,
    )
    equation_rank = rank(
        equation_map,
        rows=target.equation_dimension,
        columns=source.equation_dimension,
        field=field,
    )
    if require_isomorphism and (
        source.deformation_dimension != target.deformation_dimension
        or deformation_rank != source.deformation_dimension
        or source.equation_dimension != target.equation_dimension
        or equation_rank != source.equation_dimension
    ):
        raise ContractError(f"{name}: declared isomorphism has deficient rank")

    span_checks: list[dict[str, Any]] = []
    raw_span_pairs = raw.get("operation_span_pairs", [])
    if not isinstance(raw_span_pairs, list):
        raise ContractError(f"{name}: operation_span_pairs must be a list")
    for index, pair in enumerate(raw_span_pairs):
        if not isinstance(pair, Mapping):
            raise ContractError(
                f"{name}: operation span pair {index} must be an object"
            )
        from_action = str(pair.get("from"))
        to_action = str(pair.get("to"))
        if from_action not in source.actions or to_action not in target.actions:
            raise ContractError(
                f"{name}: operation span pair references an unknown action"
            )
        transported = _transport_vectors(
            source.actions[from_action].basis,
            deformation_map,
            field,
        )
        for vector in transported:
            if not vector_in_span(
                vector,
                target.actions[to_action].basis,
                ambient_dimension=target.deformation_dimension,
                field=field,
            ):
                raise ContractError(
                    f"{name}: transported {from_action} is not contained in "
                    f"{to_action}"
                )
        span_checks.append(
            {
                "from": from_action,
                "to": to_action,
                "transported_rank": rank_of_vectors(
                    transported,
                    ambient_dimension=target.deformation_dimension,
                    field=field,
                ),
                "inclusion_verified": True,
            }
        )

    operation_map_checks: list[dict[str, Any]] = []
    raw_operation_maps = raw.get("operation_map_pairs", [])
    if not isinstance(raw_operation_maps, list):
        raise ContractError(f"{name}: operation_map_pairs must be a list")
    for index, pair in enumerate(raw_operation_maps):
        if not isinstance(pair, Mapping):
            raise ContractError(
                f"{name}: operation map pair {index} must be an object"
            )
        from_action_name = str(pair.get("from"))
        to_action_name = str(pair.get("to"))
        if (
            from_action_name not in source.actions
            or to_action_name not in target.actions
        ):
            raise ContractError(
                f"{name}: operation map pair references an unknown action"
            )
        from_action = source.actions[from_action_name]
        to_action = target.actions[to_action_name]
        source_map = parse_matrix(
            field,
            pair.get("source_map", []),
            rows=to_action.source_dimension,
            columns=from_action.source_dimension,
            name=f"{name}.operation_map_pairs[{index}].source_map",
        )
        transported_action = matrix_product(
            deformation_map,
            from_action.action_matrix,
            left_rows=target.deformation_dimension,
            middle=source.deformation_dimension,
            right_columns=from_action.source_dimension,
            field=field,
        )
        target_action_after_source_map = matrix_product(
            to_action.action_matrix,
            source_map,
            left_rows=target.deformation_dimension,
            middle=to_action.source_dimension,
            right_columns=from_action.source_dimension,
            field=field,
        )
        if transported_action != target_action_after_source_map:
            raise ContractError(
                f"{name}: T_E*Theta_from != Theta_to*T_G "
                f"for {from_action_name}->{to_action_name}"
            )

        source_map_rank = rank(
            source_map,
            rows=to_action.source_dimension,
            columns=from_action.source_dimension,
            field=field,
        )
        require_source_isomorphism = bool(
            pair.get("require_isomorphism", False)
        )
        if require_source_isomorphism and (
            from_action.source_dimension != to_action.source_dimension
            or source_map_rank != from_action.source_dimension
        ):
            raise ContractError(
                f"{name}: declared operation-space isomorphism has deficient rank"
            )

        for stabilizer_vector in from_action.source_stabilizer_basis:
            transported_stabilizer = matrix_vector_product(
                source_map,
                stabilizer_vector,
                field,
            )
            if any(
                matrix_vector_product(
                    to_action.action_matrix,
                    transported_stabilizer,
                    field,
                )
            ):
                raise ContractError(
                    f"{name}: source stabilizer does not transport into "
                    f"the target stabilizer"
                )

        operation_map_checks.append(
            {
                "from": from_action_name,
                "to": to_action_name,
                "source_map_rank": source_map_rank,
                "source_dimensions": [
                    from_action.source_dimension,
                    to_action.source_dimension,
                ],
                "action_square_verified": True,
                "source_stabilizer_transport_verified": True,
                "isomorphism_required": require_source_isomorphism,
            }
        )

    source_recharts = _rechart_by_name(source.recharts)
    target_recharts = _rechart_by_name(target.recharts)
    rechart_span_checks: list[dict[str, Any]] = []
    raw_rechart_pairs = raw.get("rechart_span_pairs", [])
    if not isinstance(raw_rechart_pairs, list):
        raise ContractError(f"{name}: rechart_span_pairs must be a list")
    for index, pair in enumerate(raw_rechart_pairs):
        if not isinstance(pair, Mapping):
            raise ContractError(
                f"{name}: rechart span pair {index} must be an object"
            )
        from_rechart = str(pair.get("from"))
        to_rechart = str(pair.get("to"))
        if (
            from_rechart not in source_recharts
            or to_rechart not in target_recharts
        ):
            raise ContractError(
                f"{name}: rechart span pair references an unknown rechart"
            )
        transported = _transport_vectors(
            source_recharts[from_rechart].basis,
            deformation_map,
            field,
        )
        for vector in transported:
            if not vector_in_span(
                vector,
                target_recharts[to_rechart].basis,
                ambient_dimension=target.deformation_dimension,
                field=field,
            ):
                raise ContractError(
                    f"{name}: transported rechart {from_rechart} is not "
                    f"contained in {to_rechart}"
                )
        rechart_span_checks.append(
            {
                "from": from_rechart,
                "to": to_rechart,
                "transported_rank": rank_of_vectors(
                    transported,
                    ambient_dimension=target.deformation_dimension,
                    field=field,
                ),
                "inclusion_verified": True,
            }
        )

    true_quotient_check: dict[str, Any] | None = None
    if "true_quotient_map" in raw:
        quotient_options = raw["true_quotient_map"]
        if not isinstance(quotient_options, Mapping):
            raise ContractError(f"{name}: true_quotient_map must be an object")
        transported_explained = _transport_vectors(
            source.explained_basis,
            deformation_map,
            field,
        )
        for vector in transported_explained:
            if not vector_in_span(
                vector,
                target.explained_basis,
                ambient_dimension=target.deformation_dimension,
                field=field,
            ):
                raise ContractError(
                    f"{name}: the true explained space does not transport"
                )

        transported_quotient = _transport_vectors(
            source.quotient_representatives,
            deformation_map,
            field,
        )
        for vector in transported_quotient:
            if any(matrix_vector_product(target.operator, vector, field)):
                raise ContractError(
                    f"{name}: quotient representative left the target kernel"
                )
        _, quotient_added = independent_extension(
            target.explained_basis,
            transported_quotient,
            ambient_dimension=target.deformation_dimension,
            field=field,
        )
        induced_rank = len(quotient_added)
        source_quotient_dimension = len(source.quotient_representatives)
        target_quotient_dimension = len(target.quotient_representatives)
        require_quotient_isomorphism = bool(
            quotient_options.get("require_isomorphism", False)
        )
        if require_quotient_isomorphism and (
            source_quotient_dimension != target_quotient_dimension
            or induced_rank != source_quotient_dimension
        ):
            raise ContractError(
                f"{name}: induced true-quotient map is not an isomorphism"
            )
        true_quotient_check = {
            "explained_space_transport_verified": True,
            "source_quotient_dimension": source_quotient_dimension,
            "target_quotient_dimension": target_quotient_dimension,
            "induced_quotient_rank": induced_rank,
            "isomorphism_required": require_quotient_isomorphism,
        }

    dual_checks: list[dict[str, Any]] = []
    raw_dual_pairs = raw.get("dual_pairs", [])
    if not isinstance(raw_dual_pairs, list):
        raise ContractError(f"{name}: dual_pairs must be a list")
    parsed_dual_pairs: list[tuple[Vector, Vector]] = []
    for index, pair in enumerate(raw_dual_pairs):
        if not isinstance(pair, Mapping):
            raise ContractError(f"{name}: dual pair {index} must be an object")
        source_functional = parse_vector(
            field,
            pair.get("from", []),
            width=source.equation_dimension,
            name=f"{name}.dual_pairs[{index}].from",
        )
        target_functional = parse_vector(
            field,
            pair.get("to", []),
            width=target.equation_dimension,
            name=f"{name}.dual_pairs[{index}].to",
        )
        if (
            row_matrix_product(target_functional, equation_map, field)
            != source_functional
        ):
            raise ContractError(
                f"{name}: dual functional pullback does not match"
            )
        if any(
            row_matrix_product(source_functional, source.operator, field)
        ) or any(
            row_matrix_product(target_functional, target.operator, field)
        ):
            raise ContractError(
                f"{name}: supplied dual functional is not left-null"
            )
        parsed_dual_pairs.append((source_functional, target_functional))
        dual_checks.append({"index": index, "pullback_verified": True})

    forcing_check: dict[str, Any] | None = None
    if "forcing_pair" in raw:
        pair = raw["forcing_pair"]
        if not isinstance(pair, Mapping):
            raise ContractError(f"{name}: forcing_pair must be an object")
        source_forcing = parse_vector(
            field,
            pair.get("from", []),
            width=source.equation_dimension,
            name=f"{name}.forcing_pair.from",
        )
        target_forcing = parse_vector(
            field,
            pair.get("to", []),
            width=target.equation_dimension,
            name=f"{name}.forcing_pair.to",
        )
        if (
            matrix_vector_product(equation_map, source_forcing, field)
            != target_forcing
        ):
            raise ContractError(f"{name}: forcing vector does not transport")
        pairings = []
        for source_functional, target_functional in parsed_dual_pairs:
            source_pairing = dot(source_functional, source_forcing, field)
            target_pairing = dot(target_functional, target_forcing, field)
            if source_pairing != target_pairing:
                raise ContractError(
                    f"{name}: obstruction pairing is not preserved"
                )
            pairings.append(field.serialize(source_pairing))
        forcing_check = {
            "transport_verified": True,
            "dual_pairings_preserved": True,
            "pairings": pairings,
        }

    result: dict[str, Any] = {
        "name": name,
        "from": from_id,
        "to": to_id,
        "chain_map_verified": True,
        "deformation_map_rank": deformation_rank,
        "equation_map_rank": equation_rank,
        "isomorphism_required": require_isomorphism,
        "operation_span_checks": span_checks,
        "operation_map_checks": operation_map_checks,
        "rechart_span_checks": rechart_span_checks,
        "dual_checks": dual_checks,
    }
    if true_quotient_check is not None:
        result["true_quotient_check"] = true_quotient_check
    if forcing_check is not None:
        result["forcing_check"] = forcing_check
    return result
