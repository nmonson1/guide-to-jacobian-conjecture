"""Exact SymPy checks for several structural extensions.

Based solely on the formulas displayed in main(2).tex.  This is a compact
research verifier, not an independent-CAS implementation.
"""
from itertools import combinations_with_replacement
import sympy as sp

x,y,z,a,b,c,d,q,s,h,k = sp.symbols('x y z a b c d q s h k')
V = (x,y,z,a,b,c,d,q,s,h,k)
Phi = sp.Matrix([
-a*c-a*d*z-3*a*y**2-2*a*z-c*d**2+d**2*z-d*s+7*d*y**2+s*x*y+3*x*y*z+4*y**2+z,
-b*c-b*d*z-3*b*y**2-2*b*z-3*c*d*x-d*q+q*x*y+12*x*y**2+3*x*z+y,
-h*k-h*x*z+k*x**2-3*x**2*y+2*x,
a-d**2+2*d*x*y,
b+3*x**2*y,
c+x*y*z+3*y**2+2*z,
d-x*y,
b*z+3*c*x+q,
s+a*z+c*x*y-x*y*z-7*y**2+c*d-d*z,
h-x**2,
k+x*z])
zero = {v:0 for v in V}
L = Phi.jacobian(V).subs(zero)
K = L.inv()*Phi

def hpart(f, degree):
    p=sp.Poly(sp.expand(f),*V)
    return sp.Add(*[
        coeff*sp.prod(v**e for v,e in zip(V,mon))
        for mon,coeff in p.terms() if sum(mon)==degree
    ])
Q=sp.Matrix([hpart(f,2) for f in K])
C=sp.Matrix([hpart(f,3) for f in K])

w=sp.symbols('w1:8'); t=sp.symbols('t')
V19=V+w+(t,)
Bw=sp.Matrix([0]*11)
for j,row in enumerate((0,1,2,3,4,5,8)):
    Bw[row]=w[j]
qvec=sp.Matrix([C[i] for i in (0,1,2,3,4,5,8)])
H=sp.Matrix(list(t*Q+t**2*Bw)+list(-qvec)+[0])
A=H.jacobian(V19)

# Moving flag / failure of strong nilpotence.
def evaluate_matrix(M, point):
    return M.subs(dict(zip(V19,point)))
ed=[0]*19; ed[6]=1
eT=[0]*19; eT[18]=1
product=evaluate_matrix(A,ed)*evaluate_matrix(A,eT)
assert sp.factor(product.charpoly().as_expr()) == sp.Symbol('lambda')**18*(sp.Symbol('lambda')+3)
assert [(i,j,product[i,j]) for i in range(19) for j in range(19) if product[i,j]] == [
    (13,13,-1),(13,16,1),(16,13,2),(16,16,-2)]

# Kernel-vector Hessian pairing.
E=x*y*(c+2*z)+d**2*z+3*d*y**2
v1=sp.Matrix([0]*19); v1[9]=2*t*x; v1[10]=2*t*z; v1[11]=x*k+z*h
v2=sp.Matrix([0]*19); v2[3]=-t*x*y; v2[8]=-t*(d*z+3*y**2)
v2[13]=-E; v2[16]=2*E; v2[17]=x*y*z

def D2(F,U,W,variables):
    return sp.Matrix([
        sum(sp.diff(F[i],variables[j],variables[l])*U[j]*W[l]
            for j in range(len(variables)) for l in range(len(variables)))
        for i in range(len(F))])
assert D2(H,v1,v2,V19) == sp.zeros(19,1)
assert D2(H,v2,v2,V19) == sp.zeros(19,1)
expected=sp.zeros(19,1); expected[0]=-4*t**3*x*z
assert sp.simplify(D2(H,v1,v1,V19)-expected) == sp.zeros(19,1)

# Robust 12-parameter compression family.
weights=dict(zip(V,(1,-1,-2,0,1,-2,0,-1,-2,2,-1)))
def wt(mon):
    ex=sp.Poly(mon,*V).monoms()[0]
    return sum(ex[i]*weights[V[i]] for i in range(11))
quad=[sp.prod(V[i] for i in I) for I in combinations_with_replacement(range(11),2)]
Sigma=[m for m in quad if wt(m)==-2]
assert Sigma == [y**2,q*y,k*y,a*z,d*z,a*c,a*s,c*d,d*s,q**2,k*q,k**2]
u=sp.symbols('u0:12')
sigma=sum(co*m for co,m in zip(u,Sigma))
P=sp.zeros(11,1); P[3]=-d**2; P[8]=sigma
br=Q.jacobian(V)*P-P.jacobian(V)*Q
Cnew=sp.Matrix([sp.expand(e) for e in C+br])
assert all(Cnew[i]==0 for i in (3,6,7,9,10))

def D2_11(F,U,W): return D2(F,U,W,V)
O4=(C.jacobian(V)*P-P.jacobian(V)*C
    +sp.Rational(1,2)*D2_11(Q,P,P)
    -P.jacobian(V)*(Q.jacobian(V)*P-P.jacobian(V)*Q)
    -sp.Rational(1,2)*D2_11(P,Q,Q))
terms=[
(3,x**2*y**2,1),(3,x**2*a*c,4),(3,x**2*a*s,-sp.Rational(20,3)),
(3,x**2*q*k,9),(3,x*c*h*k,3),(3,x*d**2*q,-sp.Rational(1,2)),
(3,x*s*h*k,-7),(3,y**2*a*h,sp.Rational(4,3)),
(3,y*b*c*h,-sp.Rational(1,2)),(3,y*d*h*k,-1),
(3,z*a**2*h,sp.Rational(8,3)),(3,a*q*h*k,25),(6,d*q*h*k,-2)]
Lambda=sum(co*sp.Poly(sp.expand(O4[row]),*V).coeff_monomial(mon)
           for row,mon,co in terms)
assert sp.factor(Lambda)==1

# Quotient cubic, discriminant, and all-order ray coefficients.
AA,BB,qq=sp.symbols('AA BB qq')
poly=qq**3-2*qq**2+BB*qq-2*AA
assert sp.simplify(sp.discriminant(poly,qq) + 4*(27*AA**2-18*AA*BB+16*AA+BB**3-BB**2)) == 0
alpha,beta,uvar=sp.symbols('alpha beta u', positive=True)
# Check the finite coefficient formula for the first several n.
for n in range(2,13):
    coeff=sp.expand((1-2*alpha*uvar**2-2*beta*uvar**3)**sp.Rational(-1,2)).series(uvar,0,n+1).removeO().coeff(uvar,n)
    finite=sum(sp.Rational(1,2)**j*sp.binomial(2*j,j)*sp.binomial(j,n-2*j)
               *alpha**(3*j-n)*beta**(n-2*j)
               for j in range((n+2)//3,n//2+1))
    assert sp.simplify(coeff-finite)==0

print('All structural extension checks passed.')
