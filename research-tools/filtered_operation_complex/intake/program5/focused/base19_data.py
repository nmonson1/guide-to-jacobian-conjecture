from __future__ import annotations
import sympy as sp
from typing import Sequence

def homogeneous_part(expr, degree, variables: Sequence[sp.Symbol]):
    poly=sp.Poly(sp.expand(expr),*variables)
    ans=0
    for mon,coef in poly.terms():
        if sum(mon)==degree:
            term=coef
            for v,e in zip(variables,mon): term*=v**e
            ans+=term
    return sp.expand(ans)

x,y,z,a,b,c,d,q0,s,h,k=sp.symbols('x y z a b c d q s h k')
X=[x,y,z,a,b,c,d,q0,s,h,k]
Phi=sp.Matrix([
-a*c-a*d*z-3*a*y**2-2*a*z-c*d**2+d**2*z-d*s+7*d*y**2+s*x*y+3*x*y*z+4*y**2+z,
-b*c-b*d*z-3*b*y**2-2*b*z-3*c*d*x-d*q0+q0*x*y+12*x*y**2+3*x*z+y,
-h*k-h*x*z+k*x**2-3*x**2*y+2*x,
a-d**2+2*d*x*y,
b+3*x**2*y,
c+x*y*z+3*y**2+2*z,
d-x*y,
b*z+3*c*x+q0,
s+a*z+c*x*y-x*y*z-7*y**2+c*d-d*z,
h-x**2,
k+x*z]).applyfunc(sp.expand)
L=Phi.jacobian(X).subs({v:0 for v in X})
K=(L.inv()*Phi).applyfunc(sp.expand)
K1=sp.Matrix([homogeneous_part(f,1,X) for f in K])
K2=sp.Matrix([homogeneous_part(f,2,X) for f in K])
K3=sp.Matrix([homogeneous_part(f,3,X) for f in K])
basis_rows=[0,1,2,3,4,5,8]
q=sp.Matrix([K3[i] for i in basis_rows])
B=sp.zeros(11,7)
for j,i in enumerate(basis_rows):B[i,j]=1
w=list(sp.symbols('w1:8')); t=sp.Symbol('t'); W=sp.Matrix(w)
H=(t*K2+t**2*B*W).col_join(-q).col_join(sp.Matrix([0]))
Z=X+w+[t]
G=sp.Matrix(Z)+H
JH=H.jacobian(Z)
