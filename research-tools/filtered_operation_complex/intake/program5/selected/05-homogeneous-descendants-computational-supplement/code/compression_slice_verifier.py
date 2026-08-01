"""Exact verifier for the 20-dimensional equivariant compression slice.

Imports the formulas and basic checks from extensions_verifier.py, then verifies:
  * dim(weight-preserving quadratic vector fields) = 115;
  * the affine slice killing the a,d,q,h,k cubic rows has dimension 20;
  * Lambda_4(O_4(P)) is identically 1 on that slice;
  * the tangent space to the equivariant rank<=6 locus at P0 has dimension 22.
"""
from itertools import combinations_with_replacement
import sympy as sp
from sympy.polys.matrices import DomainMatrix
import extensions_verifier as E

V,Q,C = E.V,E.Q,E.C
x,y,z,a,b,c,d,q,s,h,k = V
weights=E.weights

quad=[sp.prod(V[i] for i in I) for I in combinations_with_replacement(range(11),2)]
def wt(mon):
    ex=sp.Poly(mon,*V).monoms()[0]
    return sum(ex[i]*weights[V[i]] for i in range(11))

basis=[]
for row,var in enumerate(V):
    for mon in quad:
        if wt(mon)==weights[var]:
            basis.append((row,mon))
assert len(basis)==115

JQ=Q.jacobian(V)
brackets=[]
for row,mon in basis:
    P=sp.zeros(11,1); P[row]=mon
    brackets.append(sp.Matrix([sp.expand(e) for e in JQ*P-P.jacobian(V)*Q]))

cubic=[sp.prod(V[i] for i in I) for I in combinations_with_replacement(range(11),3)]
selected=(3,6,7,9,10) # a,d,q,h,k
rows=[]; rhs=[]
for out in selected:
    pC=sp.Poly(C[out],*V)
    pB=[sp.Poly(B[out],*V) for B in brackets]
    for mon in cubic:
        cs=[p.coeff_monomial(mon) for p in pB]
        c0=pC.coeff_monomial(mon)
        if c0 or any(cs):
            rows.append(cs); rhs.append(-c0)
M=sp.Matrix(rows); bvec=sp.Matrix(rhs)
assert DomainMatrix.from_Matrix(M).rank()==95
assert DomainMatrix.from_Matrix(M.row_join(bvec)).rank()==95

sol=next(iter(sp.linsolve((M,bvec))))
free=sorted(set().union(*(e.free_symbols for e in sol)),key=str)
assert len(free)==20
P=sp.zeros(11,1)
for coeff,(row,mon) in zip(sol,basis):
    P[row]+=coeff*mon
P=sp.Matrix([sp.expand(e) for e in P])

O4=(C.jacobian(V)*P-P.jacobian(V)*C
    +sp.Rational(1,2)*E.D2_11(Q,P,P)
    -P.jacobian(V)*(Q.jacobian(V)*P-P.jacobian(V)*Q)
    -sp.Rational(1,2)*E.D2_11(P,Q,Q))
Lambda=sum(co*sp.Poly(sp.expand(O4[row]),*V).coeff_monomial(mon)
           for row,mon,co in E.terms)
assert sp.factor(Lambda)==1

# Tangent dimension to rank<=6 at P0=-d^2 e_a.
P0=sp.zeros(11,1); P0[3]=-d**2
C0=sp.Matrix([sp.expand(e) for e in C+JQ*P0-P0.jacobian(V)*Q])
M0=sp.zeros(11,len(cubic))
for i,expr in enumerate(C0):
    pp=sp.Poly(expr,*V)
    for j,mon in enumerate(cubic): M0[i,j]=pp.coeff_monomial(mon)
assert M0.rank()==6
ind_rows=(0,1,2,4,5,8)
R=M0[list(ind_rows),:]
_,piv=R.rref(); piv=list(piv)
RJ=R[:,piv]; assert RJ.det()!=0
nonpiv=[j for j in range(len(cubic)) if j not in piv]
RJinv=RJ.inv()

# Coefficient matrices of the 115 perturbations.
Mb=[]
for B in brackets:
    T=sp.zeros(11,len(cubic))
    for i,expr in enumerate(B):
        pp=sp.Poly(expr,*V)
        for j,mon in enumerate(cubic): T[i,j]=pp.coeff_monomial(mon)
    Mb.append(T)

entries={}
for col,T in enumerate(Mb):
    offset=0
    for zr in selected:
        r=T[zr,:]
        residual=r-r[:,piv]*RJinv*R
        for local,j in enumerate(nonpiv):
            val=residual[0,j]
            if val: entries[(offset+local,col)]=val
        offset+=len(nonpiv)
Tmat=sp.SparseMatrix(len(selected)*len(nonpiv),115,entries)
assert DomainMatrix.from_Matrix(Tmat,fmt='sparse').rank()==93
assert 115-93==22

print('20-dimensional slice and 22-dimensional tangent checks passed.')
