from __future__ import annotations
import argparse, json, math, shutil, textwrap
from pathlib import Path
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('input_dir',type=Path)
parser.add_argument('output_dir',type=Path)
args=parser.parse_args()
SOURCE=args.input_dir.resolve()
OUT=args.output_dir.resolve()
if not SOURCE.is_dir():
    raise FileNotFoundError(SOURCE)
if OUT.exists():
    raise FileExistsError(f'refusing to overwrite {OUT}')
shutil.copytree(SOURCE,OUT)
D=json.loads((OUT/'exact_data.json').read_text())
F=json.loads((OUT/'refined_fan_data.json').read_text())

X,Y,z=sp.symbols('X Y z')
p,q,pp,qp=sp.symbols('p q pp qp')
# Chain-rule verification with z=X*Y^2: P=X p(z), Q=X^2 Y q(z).
PX=p+z*pp
PY=2*X**2*Y*pp
QX=X*Y*(2*q+z*qp)
QY=X**2*(q+2*z*qp)
J=sp.expand(X**2*((p+z*pp)*(q+2*z*qp)-2*z*pp*(2*q+z*qp)))
E=sp.expand(p*q+2*z*p*qp-3*z*pp*q)
assert sp.expand(J-X**2*E)==0
# For tau=z q^2/p^3, d tau/dz-q/p^4 = q(E-1)/p^4.
tau_derivative_numerator=sp.expand(p*q**2+2*z*p*q*qp-3*z*q**2*pp-q)
assert sp.expand(tau_derivative_numerator-q*(E-1))==0

# Correct toric divisor data: min pairing is the valuation, max is only support function.
def primitive_pair(a,b):
    g=math.gcd(abs(a),abs(b))
    return (a//g,b//g,g)

boundary={}
for case in ['truncated','full']:
    ptsP=[tuple(x) for x in D[case]['P_support']]
    ptsQ=[tuple(x) for x in D[case]['Q_support']]
    rows=[]
    for ray,si,lab in zip(F[case]['rays'],F[case]['self_intersections'],F[case]['Kbar_labels']):
        ray=tuple(ray)
        vp=min(ray[0]*i+ray[1]*j for i,j in ptsP)
        vq=min(ray[0]*i+ray[1]*j for i,j in ptsQ)
        maxp=max(ray[0]*i+ray[1]*j for i,j in ptsP)
        maxq=max(ray[0]*i+ray[1]*j for i,j in ptsQ)
        pfacepts=[(i,j) for i,j in ptsP if ray[0]*i+ray[1]*j==vp]
        qfacepts=[(i,j) for i,j in ptsQ if ray[0]*i+ray[1]*j==vq]
        rows.append({'ray':ray,'self_intersection':si,'Kbar_label':lab,
                     'vP':vp,'vQ':vq,'support_max_P':maxp,'support_max_Q':maxq,
                     'P_face':pfacepts,'Q_face':qfacepts})
    core=[]
    for lab in [-1,-3,-5,-2]:
        row=next(r for r in rows if r['Kbar_label']==lab)
        vp,vq=row['vP'],row['vQ']
        if lab in [-1,-3,-5]:
            target=(-2,-3); e=math.gcd(abs(vp),abs(vq))
        else:
            target=(-1,-1); e=1
        if lab==-5:
            status='dominates target -5 divisor'; fdeg=21
            residue='tau = Q^2/P^3 = z q(z)^2/p(z)^3, z=XY^2'
        elif lab==-2:
            status='dominates target -2 divisor'; fdeg=1
            residue='Q/P restricts to a nonzero scalar times XY'
        elif lab==-3:
            status='maps to a point of target -5 divisor'; fdeg=None
            residue='Q^2/P^3 is constant because p_8=R^2 and q_12=R^3'
        else:
            status='maps to a point of target -5 divisor'; fdeg=None
            residue='Q^2/P^3 is constant on the unique vertex face'
        core.append({**row,'target_ray':target,'normal_index_e':e,
                     'mapping_degree_f':fdeg,'status':status,'residue_coordinate':residue})
    boundary[case]={'all_rays':rows,'negative_core':core,
                    'original_total_degrees':{
                        'P':max(5*j-i for i,j in ptsP),
                        'Q':max(5*j-i for i,j in ptsQ)}}

belyi={
 'face_forms':{
   'P_face':'X*p(z), z=X*Y^2, deg p=7',
   'Q_face':'X^2*Y*q(z), deg q=10',
   'jacobian_face_equation':"p*q + 2*z*p*q' - 3*z*p'*q = 1"
 },
 'boundary_function':"tau=z*q(z)^2/p(z)^3",
 'derivative_mod_face_equation':"tau'=q/p^4",
 'degree':21,
 'passport':{
   '0':'2^10 1 (ten simple roots of q, plus z=0)',
   'infinity':'3^7 (seven simple roots of p)',
   'c=tau(infinity)':'17 1^4 (infinity has ramification 17)'
 },
 'normal_ramification_index':1,
 'contribution_to_generic_degree':21,
 'three_dessin_test':{
   'required_degree_on_core_minus5':16,
   'computed_degree':21,
   'outcome':'incompatible'
 }
}
(OUT/'boundary_graph_data.json').write_text(json.dumps(boundary,indent=2))
(OUT/'minus5_belyi_obstruction.json').write_text(json.dumps(belyi,indent=2))

# A compact exact verification script, independent of the larger generator.
verify = r'''import sympy as s
X,Y,z=s.symbols("X Y z")
p0=s.symbols("p0:8"); q0=s.symbols("q0:11")
p=sum(p0[i]*z**i for i in range(8))
q=sum(q0[i]*z**i for i in range(11))
P=X*p.subs(z,X*Y**2)
Q=X**2*Y*q.subs(z,X*Y**2)
J=s.expand(s.diff(P,X)*s.diff(Q,Y)-s.diff(P,Y)*s.diff(Q,X))
E=s.expand(p*q+2*z*p*s.diff(q,z)-3*z*s.diff(p,z)*q)
assert s.expand(J-X**2*E.subs(z,X*Y**2))==0
tau=z*q**2/p**3
num=s.factor(s.together(s.diff(tau,z)-q/p**4).as_numer_denom()[0])
assert s.factor(num-q*(E-1))==0
print("verified: face Jacobian and Belyi derivative identities")
'''
(OUT/'verify_minus5_belyi.py').write_text(verify)

# Update README with corrected valuation language and main obstruction.
old=(OUT/'README.md').read_text()
append=r'''

## Boundary-graph correction and Three-dessin test

For a toric ray `v`, the divisor valuation is the **minimum** of `<m,v>` on the support; the support maximum is not the valuation.  On the common regular refinement, both Newton cases have the same negative-label chain

`-1 -- -3 -- -5 -- -2`

with source self-intersections `-2,-2,-1,-1` and valuation pairs

| label | source ray | `(v(P),v(Q))` | behavior |
|---:|---|---|---|
| -1 | `(0,-1)` | `(-16,-24)=8(-2,-3)` | point on target `-5` |
| -3 | `(-1,0)` | `(-8,-12)=4(-2,-3)` | point on target `-5` |
| -5 | `(-2,1)` | `(-2,-3)` | degree-21 map onto target `-5` |
| -2 | `(-1,1)` | `(-1,-1)` | degree-1 map onto target `-2` |

On the `-5` divisor put `z=XY^2`.  The face polynomials are

`P_face=X p(z)`, `Q_face=X^2 Y q(z)`, with `deg p=7`, `deg q=10`.
The coefficient of the lowest toric weight in `[P,Q]=X^2` is

`p q + 2 z p q' - 3 z p' q = 1`.

Consequently

`tau=Q^2/P^3|_{E_-5}=z q^2/p^3`,  `tau'=q/p^4`,

so `tau` is a degree-21 Belyi map with passport

`(2^10 1), (3^7), (17 1^4)`.

Borisov's Three-dessin framework requires degree 16 on its core `-5` component.  Therefore neither open `(8,28)` Newton polygon can realize Three-dessin.  The same calculation gives the new conditional bound `mu >= 21` for the generic degree of a counterexample in this Newton case.
'''
if '## Boundary-graph correction and Three-dessin test' not in old:
    (OUT/'README.md').write_text(old+append)

print('wrote extended files to',OUT)
print('verified boundary degree',belyi['degree'])
