# Lane 8 exact raw-support reconstruction input

This page is the complete public executable input used to reconstruct
the two normalized Newton supports through their deficiency layers.
It is an input for auditing the generated path; it does not assert that
all complementary queue branches have been routed.

## Mathematical contract

The program generates every lattice point of the truncated and full
support polygons shown on Lane 8, applies the displayed Jacobian bracket
formula, reconstructs the exact degree-21 lower face over the pinned
quintic field, and builds the deficiency layers.  It proves the stored
truncated contradiction and regenerates the fifteen full-support
equations.  It does not prove the imported below-125 reduction or supply
a missing saturation complement or rechart unless that branch appears in
the program.

To replay without a private checkout, place the reconstruction program
and its two JSON files in `degree-twenty-one/raw-support-reconstruction/`,
place the field helper in `degree-296-compact/scripts/` under the same
parent directory, install SymPy, and run

```text
python degree-twenty-one/raw-support-reconstruction/rebuild_lower_face_reduction.py --case both --output NEW_OUTPUT_DIRECTORY
```

The program refuses to overwrite an existing output directory.

## Exact quintic-field relations

```json
{
  "minimal_polynomial": "x^5 - x^4 + 3*x^3 + 3*x^2 + 26",
  "embedding_u": "-1.664836704033281178287344837278453851243269719290529858837572849478096828874852644384604910897382528107270588725589666125991437289596384307710878098059890261343130493410462877211296943502703584967016795149926388008709045993820767368828925295297803467062290834505165029892360667316286563814009383217909009001206119886944218924363516852663481277961183375893887378030116626164422232848450401162997881175731333088917665351003224456146577545061215607292153550842648194999365814925555860277191706380521193937759311853768561692449956605459343393956285886937979108468916830887597557139471405555442317143568561030007703945169466029452958875790962020233295593809415027516528665873588817248150070604083360101791172701529772884866371569107239340307800243720844567961168920885364856474153806204746827088597876494399840726972525102913812213765932070335388899028342693458535295571615778777532940",
  "relations": {
    "2": [
      -15000285910282089504192,
      -5134565172670933272,
      137539431432626359836,
      336800193197460147624,
      -84325443098952382698,
      60579126468209266677769
    ],
    "3": [
      1226904480739913911103730491354208,
      -15145626846222632510692702532772,
      -25812205047619065763137145542294,
      -104130346741942550519886117919428,
      27200215296791514496874102142465,
      -29820471480667863369966901978929206
    ],
    "4": [
      3264449436074769519960953302867233653589648,
      -1416654536542996172285603232367200883597872,
      148725684611945953158030103823084812692216,
      -3555183783735327382944597214649722070608848,
      1011336872221928971870287510246952931988480,
      -3669830563651292540100256702722208474478817361
    ],
    "5": [
      -130944093022209528082635510047219742278592832955123904,
      -93369115961295526137992581529023299645675371941885440,
      79954620410178210879841226102250409682919462179058816,
      -80365467842144031759719494563248567280650515063467264,
      29210432611391016065746943076582124101598753403543376,
      -903249056584503071594417102016234211800722097289832510707
    ],
    "6": [
      2904537848673965560983870231505961611216484953581987843838276864,
      -27139380915905548127415137801482954552161780107413095369243631360,
      30569988840281136299540789078923076865252792222802018120348518784,
      -11515632609329406031637838793544215559406566088372742650310149376,
      5180847076984791157406962461949350630412905296285784590160733184,
      -3779357207149632914103290532850228636627298428125710781575310029109353
    ],
    "7": [
      -587985697653650203066919462433643852598998530789582860440276756960997106688,
      364163207376347068831121008237845147451532454403442608765650380506147866112,
      -330463845892243517019896878071386300101126939914921066806649929166392606464,
      99196362661811887568094595512520927061635078997619327908217427264016147968,
      -38091354056913439826730530997349571916326149522524749218571860463219329664,
      930206660129096433749475266122359445351031352517661885125550567798599734193335611
    ]
  }
}
```

## Pinned expected invariants

```json
{
  "schema": "raw-lower-face-reconstruction-expected-v1",
  "relations_sha256": "a5b5752a5f7b90d50458fe3f3949e6731e0b607981627c56e0c04a1bf89de1c2",
  "face": {
    "p_degree": 7,
    "q_degree": 10,
    "jacobian_coefficients_verified": 18
  },
  "truncated": {
    "support_sizes": {
      "P": 25,
      "Q": 47
    },
    "layer_data": [
      [1, 19, 18, 17, 2, 0],
      [2, 21, 19, 18, 3, 0],
      [3, 13, 20, 12, 1, 7],
      [4, 0, 20, 0, 0, 18],
      [5, 0, 21, 0, 0, 0]
    ],
    "macaulay_rank": 14,
    "minor_determinant_sha256": "8d495d9c4ef2c6f8843c04a4ba9e2d2473da131a92d81fbfd857c8f187ce4059"
  },
  "full": {
    "support_sizes": {
      "P": 61,
      "Q": 125
    },
    "layer_data": [
      [1, 19, 18, 17, 2, 0],
      [2, 21, 19, 18, 3, 0],
      [3, 21, 20, 18, 3, 0],
      [4, 19, 20, 18, 1, 2],
      [5, 17, 21, 17, 0, 2],
      [6, 15, 20, 15, 0, 4],
      [7, 13, 19, 13, 0, 5],
      [8, 11, 18, 11, 0, 6]
    ],
    "final_equation_counts": {
      "5": 1,
      "6": 3,
      "7": 5,
      "8": 6
    },
    "final_equation_sha256": "d2027973e307d65b782dd41146bc023903630e659ed2c3a2f51daec02194a883"
  }
}
```

## Exact quintic-field helper

This is the complete nonstandard dependency imported by the
reconstruction program. Its other imports are from the Python standard
library.

```python
"""Fast exact Q[u]/(u^5-u^4+3u^3+3u^2+26) arithmetic.

Elements use five integer numerators over one common denominator.  This avoids
per-coefficient Fraction normalization in the large polynomial replay.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd
from typing import Iterable, Union

Scalar = Union[int, Fraction]
MOD_F=[Fraction(26),Fraction(0),Fraction(3),Fraction(3),Fraction(-1),Fraction(1)]


def _gcd_many(values):
    g=0
    for v in values:
        g=gcd(g,abs(v))
        if g==1: return 1
    return g


def _trim(p):
    while p and p[-1]==0:p.pop()
    return p

def _padd(a,b):
    n=max(len(a),len(b));c=[Fraction(0)]*n
    for i in range(n):c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    return _trim(c)

def _psub(a,b):
    n=max(len(a),len(b));c=[Fraction(0)]*n
    for i in range(n):c[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
    return _trim(c)

def _pmul(a,b):
    if not a or not b:return []
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    return _trim(c)

def _pscale(s,a):return _trim([s*x for x in a]) if s else []
def _pdivmod(a,b):
    a=_trim(list(a));b=_trim(list(b))
    if not b:raise ZeroDivisionError
    if len(a)<len(b):return [],a
    q=[Fraction(0)]*(len(a)-len(b)+1)
    while a and len(a)>=len(b):
        d=len(a)-len(b);c=a[-1]/b[-1];q[d]+=c
        for j,v in enumerate(b):a[d+j]-=c*v
        _trim(a)
    return _trim(q),a

def _xgcd(a,b):
    r0,r1=_trim(list(a)),_trim(list(b));s0,s1=[Fraction(1)],[];t0,t1=[],[Fraction(1)]
    while r1:
        q,r2=_pdivmod(r0,r1)
        r0,r1=r1,r2;s0,s1=s1,_psub(s0,_pmul(q,s1));t0,t1=t1,_psub(t0,_pmul(q,t1))
    lead=r0[-1]
    return _pscale(1/lead,r0),_pscale(1/lead,s0),_pscale(1/lead,t0)


def _as_frac(x: Scalar)->Fraction:
    return x if isinstance(x,Fraction) else Fraction(x)

@dataclass(frozen=True,slots=True,init=False)
class K5:
    nums: tuple[int,int,int,int,int]
    den: int
    def __init__(self, coeffs: Iterable[Scalar]=(), den: int=1):
        vals=list(coeffs)
        if den!=1:
            # Here coeffs are interpreted as integer numerators.
            ns=[int(x) for x in vals]
            ns += [0]*(5-len(ns))
            self._set(ns[:5],den);return
        fs=[_as_frac(x) for x in vals];fs += [Fraction(0)]*(5-len(fs))
        if len(fs)>5:raise ValueError
        d=1
        for f in fs:d=d*f.denominator//gcd(d,f.denominator)
        ns=[f.numerator*(d//f.denominator) for f in fs]
        self._set(ns,d)
    def _set(self,ns,den):
        if den<0:ns=[-x for x in ns];den=-den
        g=_gcd_many([den,*ns])
        if g:den//=g;ns=[x//g for x in ns]
        object.__setattr__(self,'nums',tuple(ns));object.__setattr__(self,'den',den)
    @classmethod
    def raw(cls,ns,den=1):
        obj=object.__new__(cls);obj._set(list(ns),den);return obj
    @classmethod
    def coerce(cls,x):
        if isinstance(x,K5):return x
        f=_as_frac(x);return cls.raw([f.numerator,0,0,0,0],f.denominator)
    @property
    def coeffs(self):return tuple(Fraction(n,self.den) for n in self.nums)
    def __bool__(self):return any(self.nums)
    def __eq__(self,o):
        if isinstance(o,K5):return self.den==o.den and self.nums==o.nums
        if isinstance(o,(int,Fraction)):return self==K5.coerce(o)
        return False
    def __hash__(self):return hash((self.nums,self.den))
    def __neg__(self):return K5.raw([-x for x in self.nums],self.den)
    def __add__(self,o):
        o=K5.coerce(o)
        if not self:return o
        if not o:return self
        g=gcd(self.den,o.den);a=o.den//g;b=self.den//g;d=self.den*a
        return K5.raw([x*a+y*b for x,y in zip(self.nums,o.nums)],d)
    __radd__=__add__
    def __sub__(self,o):return self+(-K5.coerce(o))
    def __rsub__(self,o):return K5.coerce(o)-self
    def __mul__(self,o):
        if isinstance(o,(int,Fraction)):
            f=_as_frac(o)
            if not f or not self:return K5()
            return K5.raw([x*f.numerator for x in self.nums],self.den*f.denominator)
        o=K5.coerce(o)
        if not self or not o:return K5()
        c=[0]*9
        for i,a in enumerate(self.nums):
            if a:
                for j,b in enumerate(o.nums):
                    if b:c[i+j]+=a*b
        for d in range(8,4,-1):
            v=c[d]
            if v:
                c[d-1]+=v;c[d-2]-=3*v;c[d-3]-=3*v;c[d-5]-=26*v;c[d]=0
        return K5.raw(c[:5],self.den*o.den)
    def __rmul__(self,o):return self*o
    @lru_cache(maxsize=None)
    def inverse(self):
        if not self:raise ZeroDivisionError
        a=[Fraction(n,self.den) for n in self.nums];a=_trim(a)
        g,s,_=_xgcd(a,MOD_F)
        if g!=[Fraction(1)]:raise ArithmeticError(g)
        _,rem=_pdivmod(s,MOD_F);rem += [Fraction(0)]*(5-len(rem))
        return K5(rem[:5])
    def __truediv__(self,o):
        if isinstance(o,(int,Fraction)):
            f=_as_frac(o)
            if not f:raise ZeroDivisionError
            return K5.raw([x*f.denominator for x in self.nums],self.den*f.numerator)
        return self*K5.coerce(o).inverse()
    def __rtruediv__(self,o):return K5.coerce(o)*self.inverse()
    def __pow__(self,n):
        if n<0:return self.inverse()**(-n)
        out=K5([1]);base=self
        while n:
            if n&1:out=out*base
            base=base*base;n//=2
        return out
    def __repr__(self):return f"K5(nums={self.nums},den={self.den})"

class KDomain:
    zero=K5();one=K5([1]);unit=K5([0,1])
    @staticmethod
    def convert(x):return K5.coerce(x)
K=KDomain()
```

## Complete reconstruction program

```python
#!/usr/bin/env python3
"""Rebuild the two normalized (8,28) lower-face reductions from raw supports.

This is the dependency-light replacement for the unrecovered
``lower_face_layers.py`` utility.  It deliberately starts from:

* the vertices of the two normalized Newton polygons;
* one exact generic member of the degree-21 Belyi orbit; and
* the coefficient formula for a polynomial Jacobian bracket.

The legacy layer files are not inputs to the derivation.  An archived full
equation file may be supplied as an optional regression oracle.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import shutil
import sys
from typing import Any, Iterable

from sympy import Poly, QQ, Rational, Symbol, sympify


SCRIPT_DIR = Path(__file__).resolve().parent
COMMON_FIELD_DIR = (
    SCRIPT_DIR.parent.parent / "degree-296-compact" / "scripts"
)
if COMMON_FIELD_DIR.is_dir():
    sys.path.insert(0, str(COMMON_FIELD_DIR))
from quintic_field_fast import K, K5  # noqa: E402


ZERO = K.zero
ONE = K.one
U = K.unit
FIELD_POLYNOMIAL = "u^5-u^4+3*u^3+3*u^2+26"
X = Symbol("x")

KElement = K5
Monomial = tuple[int, ...]
ParamPoly = dict[Monomial, KElement]
RawTerm = tuple[int, int]

NVAR = 0
ZEXP: Monomial = ()


def set_parameter_count(count: int) -> None:
    global NVAR, ZEXP
    NVAR = count
    ZEXP = (0,) * count


def as_fraction(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    q = Rational(str(value))
    return Fraction(int(q.p), int(q.q))


def k_from_vector(values: Iterable[Any]) -> KElement:
    return K5(as_fraction(value) for value in values)


def k_vector(value: KElement) -> list[str]:
    return [str(q) for q in value.coeffs]


def k_expr(value: KElement, symbol: str = "u") -> str:
    pieces: list[str] = []
    for degree, coefficient in enumerate(value.coeffs):
        if coefficient == 0:
            continue
        c = str(coefficient)
        if degree == 0:
            pieces.append(f"({c})")
        elif degree == 1:
            pieces.append(f"({c})*{symbol}")
        else:
            pieces.append(f"({c})*{symbol}^{degree}")
    return " + ".join(pieces) if pieces else "0"


def parse_legacy_field_element(text: str) -> KElement:
    expr = sympify(text.replace("^", "**"), locals={"x": X})
    polynomial = Poly(expr, X, domain=QQ)
    out = ZERO
    for (degree,), coefficient in polynomial.terms():
        out += K.convert(
            Fraction(int(coefficient.p), int(coefficient.q))
        ) * (U**degree)
    return out


def clean(poly: ParamPoly) -> ParamPoly:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient != ZERO}


def constant(coefficient: KElement) -> ParamPoly:
    return {} if coefficient == ZERO else {ZEXP: coefficient}


def variable(index: int) -> ParamPoly:
    exponent = [0] * NVAR
    exponent[index] = 1
    return {tuple(exponent): ONE}


def add(left: ParamPoly, right: ParamPoly) -> ParamPoly:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, ZERO) + coefficient
    return clean(out)


def negate(poly: ParamPoly) -> ParamPoly:
    return {monomial: -coefficient for monomial, coefficient in poly.items()}


def scale(coefficient: KElement | int, poly: ParamPoly) -> ParamPoly:
    coefficient = K.convert(coefficient)
    if coefficient == ZERO:
        return {}
    return clean(
        {
            monomial: coefficient * value
            for monomial, value in poly.items()
        }
    )


def multiply(left: ParamPoly, right: ParamPoly) -> ParamPoly:
    out: ParamPoly = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                a + b for a, b in zip(left_monomial, right_monomial)
            )
            out[monomial] = (
                out.get(monomial, ZERO)
                + left_coefficient * right_coefficient
            )
    return clean(out)


def weighted_degree(poly: ParamPoly, weights: tuple[int, ...]) -> int:
    degrees = {
        sum(exponent * weight for exponent, weight in zip(monomial, weights))
        for monomial in poly
    }
    if len(degrees) != 1:
        raise AssertionError(degrees)
    return next(iter(degrees))


def normalized(poly: ParamPoly) -> tuple[KElement, ParamPoly]:
    first = min(poly)
    normalization = ONE / poly[first]
    return normalization, {
        monomial: normalization * coefficient
        for monomial, coefficient in poly.items()
    }


def polynomial_json(poly: ParamPoly) -> list[dict[str, Any]]:
    return [
        {
            "exp": list(monomial),
            "coeff_basis": k_vector(coefficient),
            "coeff_expr": k_expr(coefficient),
        }
        for monomial, coefficient in sorted(poly.items())
    ]


def rref_transform(
    matrix: list[list[KElement]],
) -> tuple[list[list[KElement]], list[list[KElement]], list[int]]:
    row_count = len(matrix)
    column_count = len(matrix[0]) if matrix else 0
    augmented = [
        list(matrix[row])
        + [ONE if row == identity_column else ZERO for identity_column in range(row_count)]
        for row in range(row_count)
    ]
    pivot_row = 0
    pivot_columns: list[int] = []
    for column in range(column_count):
        source_row = next(
            (
                row
                for row in range(pivot_row, row_count)
                if augmented[row][column] != ZERO
            ),
            None,
        )
        if source_row is None:
            continue
        augmented[pivot_row], augmented[source_row] = (
            augmented[source_row],
            augmented[pivot_row],
        )
        inverse = ONE / augmented[pivot_row][column]
        augmented[pivot_row] = [
            inverse * value for value in augmented[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row or augmented[row][column] == ZERO:
                continue
            factor = augmented[row][column]
            augmented[row] = [
                augmented[row][index]
                - factor * augmented[pivot_row][index]
                for index in range(column_count + row_count)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return (
        [row[:column_count] for row in augmented],
        [row[column_count:] for row in augmented],
        pivot_columns,
    )


def transform_polynomials(
    transform: list[list[KElement]], vector: list[ParamPoly]
) -> list[ParamPoly]:
    out: list[ParamPoly] = []
    for row in transform:
        value: ParamPoly = {}
        for coefficient, polynomial in zip(row, vector):
            value = add(value, scale(coefficient, polynomial))
        out.append(value)
    return out


def determinant(matrix: list[list[KElement]]) -> KElement:
    work = [list(row) for row in matrix]
    size = len(work)
    value = ONE
    sign = 1
    for column in range(size):
        source_row = next(
            row
            for row in range(column, size)
            if work[row][column] != ZERO
        )
        if source_row != column:
            work[column], work[source_row] = work[source_row], work[column]
            sign = -sign
        pivot = work[column][column]
        value *= pivot
        inverse = ONE / pivot
        for row in range(column + 1, size):
            if work[row][column] == ZERO:
                continue
            factor = work[row][column] * inverse
            for index in range(column, size):
                work[row][index] -= factor * work[column][index]
    return -value if sign < 0 else value


def hull(points: Iterable[RawTerm]) -> list[RawTerm]:
    unique = sorted(set(points))

    def cross(origin: RawTerm, first: RawTerm, second: RawTerm) -> int:
        return (
            (first[0] - origin[0]) * (second[1] - origin[1])
            - (first[1] - origin[1]) * (second[0] - origin[0])
        )

    lower: list[RawTerm] = []
    for point in unique:
        while (
            len(lower) >= 2
            and cross(lower[-2], lower[-1], point) <= 0
        ):
            lower.pop()
        lower.append(point)
    upper: list[RawTerm] = []
    for point in reversed(unique):
        while (
            len(upper) >= 2
            and cross(upper[-2], upper[-1], point) <= 0
        ):
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def inside(point: RawTerm, vertices: list[RawTerm]) -> bool:
    boundary = hull(vertices)
    crosses = [
        (
            (second[0] - first[0]) * (point[1] - first[1])
            - (second[1] - first[1]) * (point[0] - first[0])
        )
        for first, second in zip(
            boundary, boundary[1:] + boundary[:1]
        )
    ]
    return all(value >= 0 for value in crosses) or all(
        value <= 0 for value in crosses
    )


def lattice_points(vertices: list[RawTerm]) -> list[RawTerm]:
    return sorted(
        (i, j)
        for i in range(max(i for i, _ in vertices) + 1)
        for j in range(max(j for _, j in vertices) + 1)
        if inside((i, j), vertices)
    )


@dataclass(frozen=True)
class SupportCase:
    name: str
    p_vertices: list[RawTerm]
    q_vertices: list[RawTerm]
    parameter_count: int
    parameters_by_layer: dict[int, list[int]]
    last_layer: int


TRUNCATED = SupportCase(
    name="truncated",
    p_vertices=[(0, 0), (1, 0), (8, 14), (8, 16)],
    q_vertices=[(0, 0), (2, 1), (12, 21), (12, 24)],
    parameter_count=6,
    parameters_by_layer={1: [0, 1], 2: [2, 3, 4], 3: [5]},
    last_layer=5,
)
FULL = SupportCase(
    name="full",
    p_vertices=[(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)],
    q_vertices=[(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)],
    parameter_count=9,
    parameters_by_layer={
        1: [0, 1],
        2: [2, 3, 4],
        3: [5, 6, 7],
        4: [8],
    },
    last_layer=8,
)


def support_layers(
    case: SupportCase,
) -> tuple[
    list[RawTerm],
    list[RawTerm],
    defaultdict[int, list[RawTerm]],
    defaultdict[int, list[RawTerm]],
]:
    p_support = lattice_points(case.p_vertices)
    q_support = lattice_points(case.q_vertices)
    p_layers: defaultdict[int, list[RawTerm]] = defaultdict(list)
    q_layers: defaultdict[int, list[RawTerm]] = defaultdict(list)
    for i, j in p_support:
        p_layers[j - 2 * i + 2].append((i, j))
    for i, j in q_support:
        q_layers[j - 2 * i + 3].append((i, j))
    return p_support, q_support, p_layers, q_layers


def build_face(
    relation_path: Path,
) -> tuple[list[KElement], list[KElement]]:
    relation_data = json.loads(relation_path.read_text())
    relation_polynomial = (
        relation_data["minimal_polynomial"].replace(" ", "").replace("x", "u")
    )
    if relation_polynomial != FIELD_POLYNOMIAL:
        raise AssertionError(relation_data["minimal_polynomial"])
    p_coefficients = [ONE, ONE]
    for degree in range(2, 8):
        relation = relation_data["relations"][str(degree)]
        numerator = sum(
            (
                K.convert(relation[index]) * (U**index)
                for index in range(5)
            ),
            ZERO,
        )
        p_coefficients.append(-numerator / relation[5])
    q_coefficients = [ONE]
    for degree in range(1, 11):
        total = ZERO
        for p_degree in range(1, min(7, degree) + 1):
            total += (
                1 + 2 * degree - 5 * p_degree
            ) * p_coefficients[p_degree] * q_coefficients[
                degree - p_degree
            ]
        q_coefficients.append(-total / (1 + 2 * degree))

    face_residual: list[KElement] = []
    for degree in range(18):
        total = ZERO
        for p_degree in range(max(0, degree - 10), min(7, degree) + 1):
            q_degree = degree - p_degree
            total += (
                1 + 2 * q_degree - 3 * p_degree
            ) * p_coefficients[p_degree] * q_coefficients[q_degree]
        total -= ONE if degree == 0 else ZERO
        face_residual.append(total)
    if any(value != ZERO for value in face_residual):
        raise AssertionError("the exact lower face does not satisfy the Jacobian equation")
    if p_coefficients[-1] == ZERO or q_coefficients[-1] == ZERO:
        raise AssertionError("the two face endpoints must be nonzero")
    return p_coefficients, q_coefficients


def bracket(
    p_terms: dict[RawTerm, ParamPoly],
    q_terms: dict[RawTerm, ParamPoly],
) -> dict[RawTerm, ParamPoly]:
    out: dict[RawTerm, ParamPoly] = {}
    for (i, j), p_coefficient in p_terms.items():
        for (k, ell), q_coefficient in q_terms.items():
            target = (i + k - 1, j + ell - 1)
            out[target] = add(
                out.get(target, {}),
                scale(
                    i * ell - j * k,
                    multiply(p_coefficient, q_coefficient),
                ),
            )
    return out


@dataclass
class LayerRun:
    case: SupportCase
    p_support: list[RawTerm]
    q_support: list[RawTerm]
    p_layers: defaultdict[int, list[RawTerm]]
    q_layers: defaultdict[int, list[RawTerm]]
    p_solution: dict[int, dict[RawTerm, ParamPoly]]
    q_solution: dict[int, dict[RawTerm, ParamPoly]]
    equations: list[tuple[int, ParamPoly]]
    layer_data: list[list[int]]


def run_layers(
    case: SupportCase,
    p_coefficients: list[KElement],
    q_coefficients: list[KElement],
) -> LayerRun:
    set_parameter_count(case.parameter_count)
    p_support, q_support, p_layers, q_layers = support_layers(case)
    p_solution: dict[int, dict[RawTerm, ParamPoly]] = {
        0: {
            (degree + 1, 2 * degree): constant(coefficient)
            for degree, coefficient in enumerate(p_coefficients)
        }
    }
    q_solution: dict[int, dict[RawTerm, ParamPoly]] = {
        0: {
            (degree + 2, 2 * degree + 1): constant(coefficient)
            for degree, coefficient in enumerate(q_coefficients)
        }
    }
    equations: list[tuple[int, ParamPoly]] = []
    layer_data: list[list[int]] = []

    def target_rows(layer: int) -> list[RawTerm]:
        rows: set[RawTerm] = set()
        for p_layer in range(layer + 1):
            for i, j in p_layers.get(p_layer, []):
                for k, ell in q_layers.get(layer - p_layer, []):
                    rows.add((i + k - 1, j + ell - 1))
        return sorted(rows)

    for layer in range(1, case.last_layer + 1):
        rows = target_rows(layer)
        row_index = {term: index for index, term in enumerate(rows)}
        columns = [
            ("P", term) for term in p_layers.get(layer, [])
        ] + [("Q", term) for term in q_layers.get(layer, [])]
        matrix = [[ZERO] * len(columns) for _ in rows]
        for column_index, (kind, term) in enumerate(columns):
            if kind == "P":
                i, j = term
                for (k, ell), coefficient_poly in q_solution[0].items():
                    matrix[row_index[(i + k - 1, j + ell - 1)]][
                        column_index
                    ] += (
                        i * ell - j * k
                    ) * next(iter(coefficient_poly.values()))
            else:
                k, ell = term
                for (i, j), coefficient_poly in p_solution[0].items():
                    matrix[row_index[(i + k - 1, j + ell - 1)]][
                        column_index
                    ] += (
                        i * ell - j * k
                    ) * next(iter(coefficient_poly.values()))

        forcing = {row: {} for row in rows}
        for p_layer in range(1, layer):
            q_layer = layer - p_layer
            if p_layer not in p_solution or q_layer not in q_solution:
                continue
            for row, polynomial in bracket(
                p_solution[p_layer], q_solution[q_layer]
            ).items():
                forcing[row] = add(forcing[row], polynomial)
        rhs = [negate(forcing[row]) for row in rows]

        if columns:
            reduced, transform, pivots = rref_transform(matrix)
            transformed_rhs = transform_polynomials(transform, rhs)
            compatibility = transformed_rhs[len(pivots) :]
            equations.extend(
                (layer, polynomial)
                for polynomial in compatibility
                if polynomial
            )
            free_columns = [
                index
                for index in range(len(columns))
                if index not in pivots
            ]
            kernel: list[list[KElement]] = []
            for free_column in free_columns:
                vector = [ZERO] * len(columns)
                vector[free_column] = ONE
                for pivot_row, pivot_column in enumerate(pivots):
                    vector[pivot_column] = -reduced[pivot_row][free_column]
                kernel.append(vector)
            expected_parameters = case.parameters_by_layer.get(layer, [])
            if len(kernel) != len(expected_parameters):
                raise AssertionError(
                    (case.name, layer, len(kernel), len(expected_parameters))
                )
            solution = [{} for _ in columns]
            for pivot_row, pivot_column in enumerate(pivots):
                solution[pivot_column] = transformed_rhs[pivot_row]
            for parameter_index, vector in zip(
                expected_parameters, kernel
            ):
                for column_index, coefficient in enumerate(vector):
                    solution[column_index] = add(
                        solution[column_index],
                        scale(coefficient, variable(parameter_index)),
                    )
            p_solution[layer] = {}
            q_solution[layer] = {}
            for polynomial, (kind, term) in zip(solution, columns):
                (p_solution if kind == "P" else q_solution)[layer][
                    term
                ] = polynomial
            layer_data.append(
                [
                    layer,
                    len(columns),
                    len(rows),
                    len(pivots),
                    len(kernel),
                    sum(bool(polynomial) for polynomial in compatibility),
                ]
            )
        else:
            equations.extend(
                (layer, polynomial)
                for polynomial in forcing.values()
                if polynomial
            )
            layer_data.append(
                [
                    layer,
                    0,
                    len(rows),
                    0,
                    0,
                    sum(bool(polynomial) for polynomial in forcing.values()),
                ]
            )
    return LayerRun(
        case=case,
        p_support=p_support,
        q_support=q_support,
        p_layers=p_layers,
        q_layers=q_layers,
        p_solution=p_solution,
        q_solution=q_solution,
        equations=equations,
        layer_data=layer_data,
    )


def weight_monomials(total: int) -> list[tuple[int, int, int, int]]:
    out = []
    for first in range(total + 1):
        for second in range(total + 1):
            for third in range(total // 2 + 1):
                for fourth in range(total // 2 + 1):
                    if first + second + 2 * third + 2 * fourth == total:
                        out.append((first, second, third, fourth))
    return out


def analyze_truncated(run: LayerRun) -> dict[str, Any]:
    expected_layers = [
        [1, 19, 18, 17, 2, 0],
        [2, 21, 19, 18, 3, 0],
        [3, 13, 20, 12, 1, 7],
        [4, 0, 20, 0, 0, 18],
        [5, 0, 21, 0, 0, 0],
    ]
    if run.layer_data != expected_layers:
        raise AssertionError(run.layer_data)
    weights = (1, 1, 2, 2, 2, 3)
    for layer, polynomial in run.equations:
        if weighted_degree(polynomial, weights) != layer:
            raise AssertionError((layer, weighted_degree(polynomial, weights)))
        if any(monomial[2] or monomial[5] for monomial in polynomial):
            raise AssertionError("split vertex parameters entered an obstruction")

    core_indices = (0, 1, 3, 4)

    def project(poly: ParamPoly) -> ParamPoly:
        return {
            tuple(monomial[index] for index in core_indices): coefficient
            for monomial, coefficient in poly.items()
        }

    weight_three = [
        project(polynomial)
        for layer, polynomial in run.equations
        if layer == 3
    ]
    weight_four = [
        project(polynomial)
        for layer, polynomial in run.equations
        if layer == 4
    ]
    monomials = weight_monomials(4)
    monomial_index = {
        monomial: index for index, monomial in enumerate(monomials)
    }
    macaulay_rows: list[list[KElement]] = []
    labels: list[tuple[str, int]] = []
    for index, polynomial in enumerate(weight_four):
        row = [ZERO] * len(monomials)
        for monomial, coefficient in polynomial.items():
            row[monomial_index[monomial]] = coefficient
        macaulay_rows.append(row)
        labels.append(("E4", index))
    for variable_index in (0, 1):
        for index, polynomial in enumerate(weight_three):
            row = [ZERO] * len(monomials)
            for monomial, coefficient in polynomial.items():
                shifted = list(monomial)
                shifted[variable_index] += 1
                row[monomial_index[tuple(shifted)]] = coefficient
            macaulay_rows.append(row)
            labels.append((f"t1_{variable_index}*E3", index))

    _, _, pivots = rref_transform(macaulay_rows)
    if len(pivots) != len(monomials) or len(monomials) != 14:
        raise AssertionError((len(pivots), len(monomials)))
    transpose = [
        [macaulay_rows[row][column] for row in range(len(macaulay_rows))]
        for column in range(len(monomials))
    ]
    _, _, independent_rows = rref_transform(transpose)
    selected = independent_rows[:14]
    minor = [
        [macaulay_rows[row][column] for column in range(14)]
        for row in selected
    ]
    minor_determinant = determinant(minor)
    if minor_determinant == ZERO:
        raise AssertionError("selected Macaulay minor vanished")

    top_p = run.p_solution[2][(8, 16)]
    top_q = run.q_solution[3][(12, 24)]
    if not top_p or not top_q:
        raise AssertionError("top vertex coefficient vanished identically")
    if any(monomial[2] or monomial[5] for monomial in top_p):
        raise AssertionError("P top vertex depends on a split parameter")
    if any(monomial[2] or monomial[5] for monomial in top_q):
        raise AssertionError("Q top vertex depends on a split parameter")

    return {
        "support_sizes": {
            "P": len(run.p_support),
            "Q": len(run.q_support),
        },
        "layer_data": run.layer_data,
        "weight_three_equation_count": len(weight_three),
        "weight_four_equation_count": len(weight_four),
        "weight_four_monomial_count": len(monomials),
        "macaulay_rank": len(pivots),
        "selected_rows": [
            {"row_index": row, "source": list(labels[row])}
            for row in selected
        ],
        "minor_determinant_nonzero": True,
        "minor_determinant_sha256": hashlib.sha256(
            json.dumps(
                k_vector(minor_determinant),
                separators=(",", ":"),
            ).encode()
        ).hexdigest(),
        "top_vertices_nonzero_before_quotient": True,
        "conclusion": (
            "All weight-four monomials in the four effective positive-weight "
            "parameters lie in the obstruction ideal. Hence all four parameters "
            "lie in its radical, forcing the required top vertices to vanish; "
            "the vertex-saturated truncated system is empty."
        ),
    }


def specialize_full(poly: ParamPoly, alpha: KElement) -> ParamPoly:
    keep = (0, 3, 6, 7, 8)
    out: ParamPoly = {}
    for monomial, coefficient in poly.items():
        reduced = tuple(monomial[index] for index in keep)
        value = coefficient * (alpha ** monomial[4])
        out[reduced] = out.get(reduced, ZERO) + value
    return clean(out)


def endpoint_after_square(
    poly: ParamPoly, alpha: KElement
) -> tuple[int, KElement]:
    """Set t22=alpha*t11^2 and require one nonzero t11 monomial."""
    out: dict[int, KElement] = {}
    for monomial, coefficient in poly.items():
        if any(
            monomial[index]
            for index in range(NVAR)
            if index not in (1, 4)
        ):
            raise AssertionError("top endpoint uses a non-face parameter")
        exponent = monomial[1] + 2 * monomial[4]
        out[exponent] = (
            out.get(exponent, ZERO)
            + coefficient * (alpha ** monomial[4])
        )
    out = {exponent: coefficient for exponent, coefficient in out.items() if coefficient != ZERO}
    if len(out) != 1:
        raise AssertionError(out)
    exponent, coefficient = next(iter(out.items()))
    return exponent, coefficient


def analyze_full(
    run: LayerRun, legacy_path: Path | None
) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any]]:
    expected_layers = [
        [1, 19, 18, 17, 2, 0],
        [2, 21, 19, 18, 3, 0],
        [3, 21, 20, 18, 3, 0],
        [4, 19, 20, 18, 1, 2],
        [5, 17, 21, 17, 0, 2],
        [6, 15, 20, 15, 0, 4],
        [7, 13, 19, 13, 0, 5],
        [8, 11, 18, 11, 0, 6],
    ]
    if run.layer_data != expected_layers:
        raise AssertionError(run.layer_data)
    weights = (1, 1, 2, 2, 2, 3, 3, 3, 4)
    for layer, polynomial in run.equations:
        if weighted_degree(polynomial, weights) != layer:
            raise AssertionError((layer, weighted_degree(polynomial, weights)))
        if any(monomial[2] or monomial[5] for monomial in polynomial):
            raise AssertionError("split parameters entered a compatibility equation")

    normalized_weight_four: list[ParamPoly] = []
    for layer, polynomial in run.equations:
        if layer != 4:
            continue
        _, candidate = normalized(polynomial)
        if not any(candidate == existing for existing in normalized_weight_four):
            normalized_weight_four.append(candidate)
    if len(normalized_weight_four) != 1:
        raise AssertionError(len(normalized_weight_four))
    square = normalized_weight_four[0]
    if any(
        any(monomial[index] for index in range(NVAR) if index not in (1, 4))
        for monomial in square
    ):
        raise AssertionError("weight-four equation is not the expected square")
    t22_squared = (0, 0, 0, 0, 2, 0, 0, 0, 0)
    t11_squared_t22 = (0, 2, 0, 0, 1, 0, 0, 0, 0)
    t11_fourth = (0, 4, 0, 0, 0, 0, 0, 0, 0)
    c22 = square.get(t22_squared, ZERO)
    c12 = square.get(t11_squared_t22, ZERO)
    c14 = square.get(t11_fourth, ZERO)
    if c22 == ZERO:
        raise AssertionError("missing t22^2 coefficient")
    alpha = -c12 / (2 * c22)
    if c14 / c22 != alpha**2:
        raise AssertionError("weight-four obstruction is not a perfect square")

    p_exponent, p_endpoint = endpoint_after_square(
        run.p_solution[2][(8, 16)], alpha
    )
    q_exponent, q_endpoint = endpoint_after_square(
        run.q_solution[3][(12, 24)], alpha
    )
    if (p_exponent, q_exponent) != (2, 3):
        raise AssertionError((p_exponent, q_exponent))
    if p_endpoint == ZERO or q_endpoint == ZERO:
        raise AssertionError("top endpoint vanished on the square branch")

    final_polynomials: list[tuple[int, ParamPoly]] = []
    for layer, polynomial in run.equations:
        specialized = specialize_full(polynomial, alpha)
        if not specialized:
            continue
        _, candidate = normalized(specialized)
        if not any(
            layer == old_layer and candidate == old
            for old_layer, old in final_polynomials
        ):
            final_polynomials.append((layer, candidate))
    counts = {
        layer: sum(
            candidate_layer == layer
            for candidate_layer, _ in final_polynomials
        )
        for layer in (5, 6, 7, 8)
    }
    if counts != {5: 1, 6: 3, 7: 5, 8: 6}:
        raise AssertionError(counts)

    final_json = [
        {"weight": layer, "terms": polynomial_json(polynomial)}
        for layer, polynomial in final_polynomials
    ]
    canonical_bytes = (
        json.dumps(final_json, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode()
    equation_digest = hashlib.sha256(canonical_bytes).hexdigest()

    legacy_match: bool | None = None
    if legacy_path is not None:
        legacy = json.loads(legacy_path.read_text())
        if len(legacy["equations"]) != len(final_polynomials):
            raise AssertionError("legacy equation count differs")
        comparisons = []
        for (layer, generated), archived in zip(
            final_polynomials, legacy["equations"]
        ):
            archived_poly = {
                tuple(term["exp"]): parse_legacy_field_element(term["coeff"])
                for term in archived["terms"]
            }
            comparisons.append(
                layer == archived["weight"] and generated == archived_poly
            )
        legacy_match = all(comparisons)
        if not legacy_match:
            raise AssertionError(comparisons)

    legacy_compatible = {
        "field_polynomial": FIELD_POLYNOMIAL,
        "normalization": "p0=q0=p1=1; t1_1=1; t2_2=alpha",
        "variables": ["x", "a", "b", "c", "d"],
        "original_parameter_indices": [0, 3, 6, 7, 8],
        "layer_data": run.layer_data,
        "alpha": k_expr(alpha, symbol="x"),
        "Ptop": k_expr(p_endpoint, symbol="x"),
        "Qtop": k_expr(q_endpoint, symbol="x"),
        "equations": [
            {
                "weight": layer,
                "terms": [
                    {
                        "exp": list(monomial),
                        "coeff": k_expr(coefficient, symbol="x"),
                    }
                    for monomial, coefficient in sorted(polynomial.items())
                ],
            }
            for layer, polynomial in final_polynomials
        ],
    }
    return (
        {
            "support_sizes": {
                "P": len(run.p_support),
                "Q": len(run.q_support),
            },
            "layer_data": run.layer_data,
            "weight_four_is_square": True,
            "alpha_basis": k_vector(alpha),
            "top_P_after_square": {
                "t11_exponent": p_exponent,
                "coefficient_basis": k_vector(p_endpoint),
            },
            "top_Q_after_square": {
                "t11_exponent": q_exponent,
                "coefficient_basis": k_vector(q_endpoint),
            },
            "vertex_saturation_forces_t11_nonzero": True,
            "normalization": (
                "t1_1=1; t2_2=alpha; retain "
                "t1_0,t2_1,t3_1,t3_2,t4_0"
            ),
            "final_equation_counts": counts,
            "final_equation_sha256": equation_digest,
            "legacy_equations_exact_match": legacy_match,
            "conclusion": (
                "The raw full support reduces exactly to the fifteen normalized "
                "equations used by the independent residue and toric-norm audit."
            ),
        },
        final_json,
        legacy_compatible,
    )


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def validate_expected(
    summary: dict[str, Any], expected_path: Path, selected_case: str
) -> None:
    expected = json.loads(expected_path.read_text())
    checks = [
        (
            "relations_sha256",
            summary["inputs"]["relations_sha256"],
            expected["relations_sha256"],
        ),
        ("face", summary["face"]["p_degree"], expected["face"]["p_degree"]),
        ("face", summary["face"]["q_degree"], expected["face"]["q_degree"]),
        (
            "face",
            summary["face"]["jacobian_coefficients_verified"],
            expected["face"]["jacobian_coefficients_verified"],
        ),
    ]
    cases = (
        ("truncated", "full")
        if selected_case == "both"
        else (selected_case,)
    )
    for case in cases:
        for field in (
            ("support_sizes", "layer_data")
            if case == "truncated"
            else ("support_sizes", "layer_data", "final_equation_counts")
        ):
            actual = summary[case][field]
            if field == "final_equation_counts":
                actual = {str(key): value for key, value in actual.items()}
            checks.append(
                (
                    f"{case}.{field}",
                    actual,
                    expected[case][field],
                )
            )
        digest_field = (
            "minor_determinant_sha256"
            if case == "truncated"
            else "final_equation_sha256"
        )
        checks.append(
            (
                f"{case}.{digest_field}",
                summary[case][digest_field],
                expected[case][digest_field],
            )
        )
        if case == "truncated":
            checks.append(
                (
                    "truncated.macaulay_rank",
                    summary[case]["macaulay_rank"],
                    expected[case]["macaulay_rank"],
                )
            )
    failures = [
        {"field": field, "actual": actual, "expected": wanted}
        for field, actual, wanted in checks
        if actual != wanted
    ]
    if failures:
        raise AssertionError({"pinned_invariant_failures": failures})
    summary["inputs"]["expected_invariants_sha256"] = hashlib.sha256(
        expected_path.read_bytes()
    ).hexdigest()
    summary["pinned_invariants_match"] = True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--case",
        choices=("truncated", "full", "both"),
        default="both",
    )
    parser.add_argument(
        "--relations",
        type=Path,
        default=SCRIPT_DIR / "belyi_exact_field_relations.json",
    )
    parser.add_argument(
        "--expected",
        type=Path,
        default=SCRIPT_DIR / "expected_invariants.json",
    )
    parser.add_argument("--legacy-full", type=Path, default=None)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    relation_path = args.relations.resolve()
    expected_path = args.expected.resolve()
    output_dir = args.output.resolve()
    if not relation_path.is_file():
        raise FileNotFoundError(relation_path)
    if not expected_path.is_file():
        raise FileNotFoundError(expected_path)
    if args.legacy_full is not None and not args.legacy_full.is_file():
        raise FileNotFoundError(args.legacy_full)
    if output_dir.exists():
        raise FileExistsError(f"refusing to overwrite {output_dir}")
    p_coefficients, q_coefficients = build_face(relation_path)
    output_dir.mkdir(parents=True)
    summary: dict[str, Any] = {
        "schema": "raw-lower-face-reconstruction-v1",
        "field": {
            "minimal_polynomial": FIELD_POLYNOMIAL,
            "basis": ["1", "u", "u^2", "u^3", "u^4"],
        },
        "inputs": {
            "relations_sha256": hashlib.sha256(
                relation_path.read_bytes()
            ).hexdigest(),
            "legacy_full_used_only_as_oracle": (
                args.legacy_full is not None
            ),
        },
        "face": {
            "p_degree": len(p_coefficients) - 1,
            "q_degree": len(q_coefficients) - 1,
            "jacobian_coefficients_verified": 18,
            "endpoint_coefficients_nonzero": True,
        },
    }
    if args.case in ("truncated", "both"):
        truncated_run = run_layers(
            TRUNCATED, p_coefficients, q_coefficients
        )
        summary["truncated"] = analyze_truncated(truncated_run)
    if args.case in ("full", "both"):
        full_run = run_layers(FULL, p_coefficients, q_coefficients)
        full_summary, full_equations, full_legacy_handoff = analyze_full(
            full_run,
            args.legacy_full.resolve()
            if args.legacy_full is not None
            else None,
        )
        summary["full"] = full_summary
        write_json(output_dir / "full_equations.json", full_equations)
        write_json(
            output_dir / "full_exact_fivevar_w8.json",
            full_legacy_handoff,
        )
        shutil.copyfile(
            relation_path,
            output_dir / "belyi_exact_field_relations.json",
        )
    validate_expected(summary, expected_path, args.case)
    write_json(output_dir / "summary.json", summary)

    hashes = []
    for path in sorted(output_dir.iterdir()):
        if path.is_file() and path.name != "SHA256SUMS":
            hashes.append(
                f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}"
            )
    (output_dir / "SHA256SUMS").write_text("\n".join(hashes) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
```

## Source hashes

- `belyi_exact_field_relations.json`: `a5b5752a5f7b90d50458fe3f3949e6731e0b607981627c56e0c04a1bf89de1c2`
- `expected_invariants.json`: `04c0da97da9974665ca1348bf1b1736ffeb5231a1ff1dc1e3c9dea8a1ec564e0`
- `rebuild_lower_face_reduction.py`: `921ebae8828452dcb535ab81a8561c717ddd61346a04389af568fb9dcafee53f`
- `degree-296-compact/scripts/quintic_field_fast.py`: `b43871c8897512b752c9e8fa8d4f2d80571865d465940e13b36f130d07091942`

[Back to Lane 8](plane-newton-queue-terminal-certificates.md)
