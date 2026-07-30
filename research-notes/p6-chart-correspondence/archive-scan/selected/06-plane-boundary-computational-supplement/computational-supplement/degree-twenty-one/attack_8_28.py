from __future__ import annotations
import argparse, json, math
from fractions import Fraction
from pathlib import Path
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('output_dir',type=Path)
args=parser.parse_args()
OUT=args.output_dir.resolve()
if OUT.exists():
    raise FileExistsError(f'refusing to overwrite {OUT}')
OUT.mkdir(parents=True, exist_ok=True)

def hull(points):
    pts=sorted(set(points))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cross(up[-2],up[-1],p)<=0: up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]

def inside_convex(pt, verts):
    V=hull(verts)
    signs=[]
    for a,b in zip(V,V[1:]+V[:1]):
        c=(b[0]-a[0])*(pt[1]-a[1])-(b[1]-a[1])*(pt[0]-a[0])
        signs.append(c)
    return all(c>=0 for c in signs) or all(c<=0 for c in signs)

def lattice_points(verts):
    xs=[p[0] for p in verts]; ys=[p[1] for p in verts]
    return sorted((i,j) for i in range(min(xs),max(xs)+1) for j in range(min(ys),max(ys)+1) if inside_convex((i,j),verts))

CASES={
 'truncated':{
  'Pverts':[(0,0),(1,0),(8,14),(8,16)],
  'Qverts':[(0,0),(2,1),(12,21),(12,24)],
 },
 'full':{
  'Pverts':[(0,0),(1,0),(8,14),(8,16),(0,8)],
  'Qverts':[(0,0),(2,1),(12,21),(12,24),(0,12)],
 }
}

def coeff_name(prefix,ij): return f'{prefix}_{ij[0]}_{ij[1]}'

def equation_terms(Ppts,Qpts):
    eq={}
    for i,j in Ppts:
        for k,l in Qpts:
            c=i*l-j*k
            if c:
                key=(i+k-1,j+l-1)
                eq.setdefault(key,[]).append((c,coeff_name('p',(i,j)),coeff_name('q',(k,l))))
    eq.setdefault((2,0),[])
    return eq

def format_poly(terms,key):
    parts=[]
    for c,p,q in sorted(terms, key=lambda z:(z[1],z[2])):
        mon=f'{p}*{q}'
        if not parts:
            if c==-1: parts.append('-'+mon)
            elif c==1: parts.append(mon)
            else: parts.append(f'{c}*{mon}')
        else:
            if c<0:
                cc=-c; parts.append(' - '+(mon if cc==1 else f'{cc}*{mon}'))
            else:
                parts.append(' + '+(mon if c==1 else f'{c}*{mon}'))
    if key==(2,0):
        parts.append(' - 1' if parts else '-1')
    return ''.join(parts) or '0'

def write_singular(case,Ppts,Qpts,eq,verts):
    vars=[coeff_name('p',z) for z in Ppts]+[coeff_name('q',z) for z in Qpts]
    lines=[]
    lines.append('// Exact sparse coefficient ideal for the (8,28) case.')
    lines.append('// Generated over Q.  The ideal encodes [P,Q]=x^2.')
    lines.append(f'// case={case}; |supp(P)|={len(Ppts)}; |supp(Q)|={len(Qpts)}; equations={len(eq)}')
    lines.append('ring r = 0,('+','.join(vars)+'),dp;')
    gens=[]
    for key in sorted(eq):
        gens.append(format_poly(eq[key],key))
    # wrap ideal in lines, one generator per line
    lines.append('ideal I =')
    for idx,g in enumerate(gens):
        sep=',' if idx<len(gens)-1 else ';'
        lines.append('  '+g+sep)
    vp=[coeff_name('p',z) for z in verts['Pverts']]+[coeff_name('q',z) for z in verts['Qverts']]
    lines.append('poly vertex_product = '+'*'.join(vp)+';')
    lines.append('// Saturate to enforce that every listed polygon vertex is actually present:')
    lines.append('// LIB "elim.lib"; ideal Isat = sat(I,vertex_product)[1];')
    (OUT/f'{case}_coefficient_ideal.sing').write_text('\n'.join(lines)+'\n')

# polynomial coefficient ranges by x degree
def ranges_by_x(points):
    d={}
    for i,j in points: d.setdefault(i,[]).append(j)
    return {i:(min(js),max(js),len(js)) for i,js in sorted(d.items())}

# Build linearized x-degree maps exactly.
y=sp.symbols('y')
R=y**7*(y-1)
u0=sp.expand(R**2); v0=sp.expand(R**3)

def poly_from_range(prefix, lo, hi):
    coeffs=sp.symbols(' '.join(f'{prefix}{j}' for j in range(lo,hi+1)))
    if lo==hi: coeffs=(coeffs,) if not isinstance(coeffs,tuple) else coeffs
    return sp.expand(sum(c*y**j for c,j in zip(coeffs,range(lo,hi+1)))),list(coeffs)

def linear_expr(r,u,v):
    # terms (a=r,b=0) and (a=0,b=r)
    return sp.expand((8-r)*u*sp.diff(v0,y)-12*sp.diff(u,y)*v0 + 8*u0*sp.diff(v,y)-(12-r)*sp.diff(u0,y)*v)

def map_matrix(case, Ppts,Qpts,r):
    pr=ranges_by_x(Ppts); qr=ranges_by_x(Qpts)
    i=8-r; j=12-r
    urange=pr.get(i); vrange=qr.get(j)
    u=0; v=0; dom=[]; meta=[]
    if urange:
        u,uc=poly_from_range(f'u{r}_',urange[0],urange[1]); dom+=uc; meta += [('u',k) for k in range(urange[0],urange[1]+1)]
    if vrange:
        v,vc=poly_from_range(f'v{r}_',vrange[0],vrange[1]); dom+=vc; meta += [('v',k) for k in range(vrange[0],vrange[1]+1)]
    expr=linear_expr(r,u,v)
    # exact output exponents from coefficients that can be nonzero
    coeffdict=sp.Poly(expr,y,*dom).as_dict() if dom else {}
    exps=sorted({mon[0] for mon,c in coeffdict.items() if c!=0})
    # Sometimes gaps? use exps directly.
    M=sp.zeros(len(exps),len(dom))
    for row,e in enumerate(exps):
        ce=sp.expand(expr).coeff(y,e)
        for col,z in enumerate(dom):
            M[row,col]=sp.expand(ce).coeff(z)
    return M,meta,exps,sp.expand(expr)

def vec_to_functional(vec,exps):
    # Return sum coeff_e [y^e]h. Also try to recognize derivative/evaluation after common shift.
    terms=[]
    for c,e in zip(vec,exps):
        if c: terms.append((sp.factor(c),e))
    return terms

all_data={}
for case,dat in CASES.items():
    Ppts=lattice_points(dat['Pverts']); Qpts=lattice_points(dat['Qverts'])
    eq=equation_terms(Ppts,Qpts)
    # Include only actual nonzero equations and rhs. All keys from nonzero brackets or rhs.
    write_singular(case,Ppts,Qpts,eq,dat)
    info={
      'P_support':Ppts,'Q_support':Qpts,
      'P_count':len(Ppts),'Q_count':len(Qpts),'equation_count':len(eq),
      'P_ranges':ranges_by_x(Ppts),'Q_ranges':ranges_by_x(Qpts),
      'vertex_product':[coeff_name('p',z) for z in dat['Pverts']]+[coeff_name('q',z) for z in dat['Qverts']],
      'layers':[]
    }
    for r in range(1,13):
        M,meta,exps,expr=map_matrix(case,Ppts,Qpts,r)
        rank=M.rank(); left=M.T.nullspace(); right=M.nullspace()
        layer={'r':r,'domain_dim':M.cols,'codomain_support_dim':M.rows,'rank':rank,
               'kernel_dim':len(right),'cokernel_dim':len(left),'domain_basis':meta,'output_exponents':exps,
               'left_nullspace':[[str(sp.factor(c)) for c in v] for v in left],
               'right_nullspace':[[str(sp.factor(c)) for c in v] for v in right]}
        info['layers'].append(layer)
    all_data[case]=info

(OUT/'exact_data.json').write_text(json.dumps(all_data,indent=2))

# Verify and record first nonlinear obstruction.
A0,A1,A2,A3=sp.symbols('A0 A1 A2 A3')
for case,maxdeg in [('truncated',2),('full',3)]:
    coeff=[A0,A1,A2,A3][:maxdeg+1]
    A=sum(coeff[k]*y**k for k in range(maxdeg+1))
    u1=sp.Rational(2,3)*y**12*A
    v1=y**19*(y-1)*A
    # Known quadratic term at r=2: (a,b)=(1,1)
    B11=sp.expand(7*u1*sp.diff(v1,y)-11*sp.diff(u1,y)*v1)
    # Obtain left nullspace of L2 and evaluate pairing coefficient-vector dot.
    Ppts=all_data[case]['P_support'];Qpts=all_data[case]['Q_support']
    M,meta,exps,expr=map_matrix(case,Ppts,Qpts,2)
    vals=[]
    for lv in M.T.nullspace():
        vec=sp.Matrix([sp.expand(B11).coeff(y,e) for e in exps])
        vals.append(sp.factor((lv.T*vec)[0]))
    (OUT/f'{case}_first_nonlinear_obstruction.txt').write_text(
        'A(y)='+str(A)+'\nB11='+str(sp.factor(B11))+'\nleft pairings:\n'+'\n'.join(map(str,vals))+'\n')
    all_data[case]['first_nonlinear_pairings']=[str(v) for v in vals]

# Fan computations.
def primitive(v):
    g=math.gcd(abs(v[0]),abs(v[1])); return (v[0]//g,v[1]//g)
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def edge_normals(verts):
    V=hull(verts)
    # hull CCW. outward normal for edge d=(dx,dy) is (dy,-dx)
    ns=[]
    for a,b in zip(V,V[1:]+V[:1]):
        dx=b[0]-a[0];dy=b[1]-a[1]
        ns.append(primitive((dy,-dx)))
    return V,ns

def angle(v):
    return math.atan2(v[1],v[0])

def regularize_cyclic(rays):
    rays=sorted(set(rays),key=angle)
    changed=True
    while changed:
        changed=False; new=[]
        n=len(rays)
        for idx,a in enumerate(rays):
            b=rays[(idx+1)%n]
            new.append(a)
            D=det(a,b)
            if D!=1:
                # Need orientation CCW; wrap can have positive det too if sorted cyclic. Search primitive sum insertion repeatedly.
                s=primitive((a[0]+b[0],a[1]+b[1]))
                if s not in rays and s!=a and s!=b:
                    new.append(s);changed=True
                else:
                    raise RuntimeError((a,b,D,s))
        rays=sorted(set(new),key=angle)
    return rays

def fan_from_case(dat):
    rays=[]
    for verts in [dat['Pverts'],dat['Qverts']]:
        V,ns=edge_normals(verts);rays+=ns
    # Need complete toric fan with normal rays. regularize via Stern-Brocot sum; check dets.
    rays=regularize_cyclic(rays)
    # rotate to start at (0,-1), and orientation CCW
    if (0,-1) in rays:
        k=rays.index((0,-1)); rays=rays[k:]+rays[:k]
    selfints=[]
    n=len(rays)
    for i,v in enumerate(rays):
        prev=rays[(i-1)%n]; nxt=rays[(i+1)%n]
        # v^2 = -det(prev,nxt) for regular fan orientation det(prev,v)=det(v,nxt)=1
        selfints.append(-det(prev,nxt))
    return rays,selfints

def support_max(points,ray): return max(ray[0]*i+ray[1]*j for i,j in points)

fan_data={}
for case,dat in CASES.items():
    rays,selfints=fan_from_case(dat)
    Ppts=all_data[case]['P_support'];Qpts=all_data[case]['Q_support']
    hP=[support_max(Ppts,r) for r in rays];hQ=[support_max(Qpts,r) for r in rays]
    # Kbar label in original coordinates under pre->post map: final ray (r,s) -> pre (-r,4r+s), and label for toric divisor in A2 compactification is sum coordinates? derive = (-r)+(4r+s)=3r+s
    labels=[3*r+s for r,s in rays]
    pre_rays=[(-r,4*r+s) for r,s in rays]
    fan_data[case]={'rays':rays,'self_intersections':selfints,'hP':hP,'hQ':hQ,'Kbar_labels':labels,'pre_rays':pre_rays}
(OUT/'fan_data.json').write_text(json.dumps(fan_data,indent=2))

# ODE solution and quartic reduction checks.
g=2048*y**4-512*y**3+320*y**2-240*y+195
f1=-y**8*(y+1)**2*g/sp.Integer(6630)
C4=y**7*(y+1)
assert sp.simplify(8*C4*sp.diff(f1,y)-14*sp.diff(C4,y)*f1-C4**2)==0
f=sp.factor(f1/C4)
assert sp.gcd(g,sp.diff(g,y))==1
ode={'C4':str(C4),'f1':str(sp.factor(f1)),'f':str(f),'quartic_g':str(g),'g_discriminant':str(sp.discriminant(g,y)),'g_at_0':str(g.subs(y,0)),'g_at_minus1':str(g.subs(y,-1))}

# Verify quartic D equations/eliminant from summary symbolically.
a,b,c,e,d0,d1,d2,L,G,u,v=sp.symbols('a b c e d0 d1 d2 L G u v')
E1=d1*a**2+2*d2*a*b+2*a*e+2*b*c
E2=d0*a**2-d2*b**2-2*b*e-c**2
E3=6*d0*a*b+3*d1*b**2+a**3-6*c*e
E4=2*d0*a*c+d0*b**2+2*d1*b*c+d2*c**2+a**2*b-e**2-sp.Rational(2,3)*L
E5=2*d0*a*e+2*d0*b*c+2*d1*b*e+d1*c**2+2*d2*c*e+a**2*c+a*b**2-sp.Rational(2,3)*G
# eliminate d0,d1 using E1,E2 assuming a !=0
sol_d1=sp.solve(E1,d1)[0]
sol_d0=sp.solve(E2,d0)[0]
E3sub=sp.factor(E3.subs({d1:sol_d1,d0:sol_d0})*a**2)
# Compare to 6uv-a5 after u=ac-b2,v=ae-bc
uvexpr=sp.factor(6*(a*c-b**2)*(a*e-b*c)-a**5)
assert sp.factor(E3sub+uvexpr)==0
# derive d2 formula from E5 perhaps after imposing relation and E4. use substitutions c=(u+b2)/a,e=(v+bc)/a and v=a5/(6u), solve E4/E5
subs_uv={c:(u+b**2)/a}
# e=(v+b*c)/a then v=a5/(6u)
e_uv=(v+b*((u+b**2)/a))/a
subs_uv[e]=e_uv
E4uv=sp.factor(E4.subs({d1:sol_d1,d0:sol_d0}).subs(subs_uv))
E5uv=sp.factor(E5.subs({d1:sol_d1,d0:sol_d0}).subs(subs_uv))
E4uv=sp.factor(E4uv.subs(v,a**5/(6*u)))
E5uv=sp.factor(E5uv.subs(v,a**5/(6*u)))
# solve E5uv for d2
sol_d2=sp.factor(sp.solve(E5uv,d2)[0])
expected=(2*G-6*a*b**2-3*a*u)/a**3
assert sp.factor(sol_d2-expected)==0
# plug into E4 and clear denominators, compare eliminant up to scalar
elim=sp.factor(E4uv.subs(d2,sol_d2))
num=sp.factor(sp.together(elim).as_numer_denom()[0])
expected_elim=-72*G*u**4+24*L*a**5*u**2+a**13-24*a**7*b*u**2+144*a*b**2*u**4+36*a*u**5
ratio=sp.factor(num/expected_elim)
assert ratio.is_Rational or not sp.simplify(num/expected_elim).has(a,b,u,L,G)
ode['quartic_reduction']={
 'E1':str(E1),'E2':str(E2),'E3':str(E3),'E4':str(E4),'E5':str(E5),
 'compatibility':str(uvexpr),'d2':str(sol_d2),'eliminant':str(expected_elim),'computed_ratio':str(ratio)
}
(OUT/'deeper_exact_reduction.json').write_text(json.dumps(ode,indent=2))

# Re-save all data including pairings.
(OUT/'exact_data.json').write_text(json.dumps(all_data,indent=2))

# Human-readable summary.
md=['# Exact computational ledger for the open (8,28) case','']
for case in ['truncated','full']:
    i=all_data[case]
    md += [f'## {case.title()} support',f'- P lattice points: {i["P_count"]}',f'- Q lattice points: {i["Q_count"]}',f'- Raw variables: {i["P_count"]+i["Q_count"]}',f'- Nonzero coefficient equations in `[P,Q]-x^2`: {i["equation_count"]}','', '| r | domain | output | rank | kernel | cokernel |','|---:|---:|---:|---:|---:|---:|']
    for z in i['layers']:
        md.append(f'| {z["r"]} | {z["domain_dim"]} | {z["codomain_support_dim"]} | {z["rank"]} | {z["kernel_dim"]} | {z["cokernel_dim"]} |')
    md += ['',f'First nonlinear left-cokernel pairings: `{i["first_nonlinear_pairings"]}`','']
    fdat=fan_data[case]
    md += [f'### {case.title()} regular fan','| ray | self-int | h_P | h_Q | Kbar label |','|---|---:|---:|---:|---:|']
    for ray,si,hp,hq,lab in zip(fdat['rays'],fdat['self_intersections'],fdat['hP'],fdat['hQ'],fdat['Kbar_labels']):
        md.append(f'| `{tuple(ray)}` | {si} | {hp} | {hq} | {lab} |')
    md.append('')
md += ['## Exact deeper reduction','',f'- ODE quartic: `{g}`',f'- Separant discriminant: `{sp.discriminant(g,y)}`',f'- Compatibility: `{uvexpr}=0`',f'- Forced coefficient: `d2={sol_d2}`',f'- Eliminant: `{expected_elim}=0`','']
(OUT/'README.md').write_text('\n'.join(md))

print('created',OUT)
for p in sorted(OUT.iterdir()): print(p.name,p.stat().st_size)
print('fan data',fan_data)
print('tables')
for case in ['truncated','full']:
 print(case)
 for z in all_data[case]['layers']:
  print(z['r'],z['domain_dim'],z['codomain_support_dim'],z['rank'],z['kernel_dim'],z['cokernel_dim'])
 print('pairings',all_data[case]['first_nonlinear_pairings'])
