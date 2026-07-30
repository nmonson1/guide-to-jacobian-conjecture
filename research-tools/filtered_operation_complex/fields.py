"""Exact coefficient fields used by filtered-operation audits."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Mapping, Sequence


class ContractError(ValueError):
    """Raised when a filtered-operation contract is internally inconsistent."""


def _q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("booleans are not exact scalar coefficients")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(f"invalid rational coefficient {value!r}") from exc
    raise TypeError(
        f"coefficient {value!r} has type {type(value).__name__}; "
        "use integers or rational strings"
    )


class ExactField:
    kind: str

    @property
    def zero(self) -> Any:
        raise NotImplementedError

    @property
    def one(self) -> Any:
        raise NotImplementedError

    def parse(self, value: Any) -> Any:
        raise NotImplementedError

    def serialize(self, value: Any) -> Any:
        raise NotImplementedError


class RationalField(ExactField):
    kind = "rational"

    @property
    def zero(self) -> Fraction:
        return Fraction(0)

    @property
    def one(self) -> Fraction:
        return Fraction(1)

    def parse(self, value: Any) -> Fraction:
        return _q(value)

    def serialize(self, value: Fraction) -> str:
        value = _q(value)
        return str(value.numerator) if value.denominator == 1 else str(value)


@dataclass(frozen=True)
class NumberFieldElement:
    field: "NumberField"
    coefficients: tuple[Fraction, ...]

    def _coerce(self, other: Any) -> "NumberFieldElement":
        return self.field.parse(other)

    def __bool__(self) -> bool:
        return any(self.coefficients)

    def __add__(self, other: Any) -> "NumberFieldElement":
        other = self._coerce(other)
        return self.field.element(
            [left + right for left, right in zip(self.coefficients, other.coefficients)]
        )

    __radd__ = __add__

    def __neg__(self) -> "NumberFieldElement":
        return self.field.element([-value for value in self.coefficients])

    def __sub__(self, other: Any) -> "NumberFieldElement":
        return self + (-self._coerce(other))

    def __rsub__(self, other: Any) -> "NumberFieldElement":
        return self._coerce(other) - self

    def __mul__(self, other: Any) -> "NumberFieldElement":
        other = self._coerce(other)
        degree = self.field.degree
        temporary = [Fraction(0) for _ in range(2 * degree - 1)]
        for i, left in enumerate(self.coefficients):
            for j, right in enumerate(other.coefficients):
                temporary[i + j] += left * right
        modulus = self.field.modulus
        leading_modulus = modulus[degree]
        for power in range(2 * degree - 2, degree - 1, -1):
            leading = temporary[power]
            if not leading:
                continue
            temporary[power] = Fraction(0)
            for index in range(degree):
                temporary[power - degree + index] -= (
                    leading * modulus[index] / leading_modulus
                )
        return self.field.element(temporary[:degree])

    __rmul__ = __mul__

    def inverse(self) -> "NumberFieldElement":
        if not self:
            raise ZeroDivisionError("zero has no inverse")
        field = self.field
        basis = [
            field.element([field.one_rational if i == j else 0 for i in range(field.degree)])
            for j in range(field.degree)
        ]
        columns = [(self * basis_vector).coefficients for basis_vector in basis]
        matrix: list[list[Fraction]] = [
            [columns[column][row] for column in range(field.degree)]
            + [Fraction(1 if row == 0 else 0)]
            for row in range(field.degree)
        ]
        for column in range(field.degree):
            pivot = next(
                (row for row in range(column, field.degree) if matrix[row][column]),
                None,
            )
            if pivot is None:
                raise ZeroDivisionError("field element is not invertible modulo the modulus")
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            scale = matrix[column][column]
            matrix[column] = [entry / scale for entry in matrix[column]]
            for row in range(field.degree):
                if row == column:
                    continue
                factor = matrix[row][column]
                if factor:
                    matrix[row] = [
                        left - factor * right
                        for left, right in zip(matrix[row], matrix[column])
                    ]
        return field.element([matrix[row][-1] for row in range(field.degree)])

    def __truediv__(self, other: Any) -> "NumberFieldElement":
        return self * self._coerce(other).inverse()

    def __rtruediv__(self, other: Any) -> "NumberFieldElement":
        return self._coerce(other) * self.inverse()

    def __pow__(self, exponent: int) -> "NumberFieldElement":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.field.one
        base = self
        remaining = exponent
        while remaining:
            if remaining & 1:
                result = result * base
            base = base * base
            remaining //= 2
        return result


class NumberField(ExactField):
    kind = "number_field"
    one_rational = Fraction(1)

    def __init__(self, modulus: Sequence[Any], symbol: str = "u") -> None:
        if len(modulus) < 2:
            raise ContractError("number-field modulus must have positive degree")
        self.modulus = tuple(_q(value) for value in modulus)
        self.degree = len(self.modulus) - 1
        if self.modulus[-1] == 0:
            raise ContractError("number-field modulus has zero leading coefficient")
        self.symbol = symbol
        self._zero = NumberFieldElement(self, (Fraction(0),) * self.degree)
        self._one = self.element([1])

    @property
    def zero(self) -> NumberFieldElement:
        return self._zero

    @property
    def one(self) -> NumberFieldElement:
        return self._one

    def element(self, coefficients: Sequence[Any]) -> NumberFieldElement:
        parsed = [_q(value) for value in coefficients]
        if len(parsed) > self.degree:
            raise ContractError(
                f"number-field element has {len(parsed)} coefficients; "
                f"expected at most {self.degree}"
            )
        parsed.extend(Fraction(0) for _ in range(self.degree - len(parsed)))
        return NumberFieldElement(self, tuple(parsed))

    def parse(self, value: Any) -> NumberFieldElement:
        if isinstance(value, NumberFieldElement):
            if value.field.modulus != self.modulus:
                raise ContractError("number-field coefficient belongs to another field")
            return value
        if isinstance(value, (int, str, Fraction)) and not isinstance(value, bool):
            return self.element([value])
        if isinstance(value, Mapping):
            value = value.get("coefficients")
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            return self.element(value)
        raise TypeError(f"cannot parse number-field coefficient {value!r}")

    def serialize(self, value: NumberFieldElement) -> list[str]:
        value = self.parse(value)
        return [
            str(coefficient.numerator)
            if coefficient.denominator == 1
            else str(coefficient)
            for coefficient in value.coefficients
        ]


def build_field(specification: Mapping[str, Any] | None) -> ExactField:
    specification = specification or {"kind": "rational"}
    kind = specification.get("kind", "rational")
    if kind == "rational":
        return RationalField()
    if kind == "number_field":
        modulus = specification.get("modulus")
        if not isinstance(modulus, list):
            raise ContractError("number_field requires a low-to-high modulus list")
        return NumberField(modulus, str(specification.get("symbol", "u")))
    raise ContractError(f"unsupported coefficient field kind {kind!r}")
