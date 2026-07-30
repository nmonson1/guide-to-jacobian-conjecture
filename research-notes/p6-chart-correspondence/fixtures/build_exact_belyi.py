import argparse
from fractions import Fraction
import json, math
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',type=Path)
args=parser.parse_args()
OUTPUT=None
if args.output_dir is not None:
    OUTPUT=args.output_dir.resolve()
    if OUTPUT.exists():
        raise FileExistsError(f'refusing to overwrite {OUTPUT}')
    OUTPUT.mkdir(parents=True)

# f(t)=f0+...+f5 t^5
f=[
-87271593441390231552,
1597839837356041961472,
-11765268269898790599288,
43543902955657595554476,
-80998237342608310849530,
60579126468209266677769,
]

class K:
    __slots__=('c',)
    def __init__(self,c=0):
        if isinstance(c,K): self.c=c.c; return
        if isinstance(c,(int,Fraction)): self.c=(Fraction(c),Fraction(0),Fraction(0),Fraction(0),Fraction(0)); return
        cc=[Fraction(x) for x in c]+[Fraction(0)]*5
        self.c=tuple(cc[:5])
    def __add__(self,o):
        o=K(o);return K([self.c[i]+o.c[i] for i in range(5)])
    __radd__=__add__
    def __neg__(self):return K([-x for x in self.c])
    def __sub__(self,o):return self+(-K(o))
    def __rsub__(self,o):return K(o)-self
    def __mul__(self,o):
        o=K(o);tmp=[Fraction(0)]*9
        for i,a in enumerate(self.c):
            for j,b in enumerate(o.c): tmp[i+j]+=a*b
        # reduce high powers using t^5 = -sum f_i/f5 t^i
        for d in range(8,4,-1):
            a=tmp[d]
            if not a: continue
            tmp[d]=0
            for i in range(5): tmp[d-5+i] -= a*Fraction(f[i],f[5])
        return K(tmp[:5])
    __rmul__=__mul__
    def inv(self):
        # solve multiplication matrix self*x=1 over Q by Gaussian elimination
        A=[]
        basis=[K([1 if i==j else 0 for i in range(5)]) for j in range(5)]
        cols=[(self*b).c for b in basis]
        for r in range(5): A.append([cols[c][r] for c in range(5)]+[Fraction(1 if r==0 else 0)])
        for col in range(5):
            piv=next(r for r in range(col,5) if A[r][col])
            A[col],A[piv]=A[piv],A[col]
            q=A[col][col]; A[col]=[x/q for x in A[col]]
            for r in range(5):
                if r==col: continue
                q=A[r][col]
                if q: A[r]=[A[r][j]-q*A[col][j] for j in range(6)]
        return K([A[i][5] for i in range(5)])
    def __truediv__(self,o):return self*K(o).inv()
    def __rtruediv__(self,o):return K(o)*self.inv()
    def __pow__(self,n):
        if n<0:return (self.inv())**(-n)
        r=K(1);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def iszero(self):return all(x==0 for x in self.c)
    def __eq__(self,o):return self.c==K(o).c
    def __repr__(self):return f'K({self.c})'

theta=K([0,1,0,0,0])
rels=[
[-673102704675979743196243860405644963865449988096, 9909608488932128601154544211588759869389519454208, -54968090629884304058793067018804814641790856513780, 135688589648080207732149635240488494719286389128536, -126906643555185508098432914418650819864566904053753, 144572487450909300718563906530095416352726879296],
[-9986787342720592590738105107632475745298959826944, 145646437338150577170626325698392993465051105984512, -801298001724494475334628652386357185532385426657540, 1974413742133088034926737441969357046079763788908904, -1845527574559619363653666257225132406888860976899187, 3289024089508186591347328873559670722024536503984],
[2314396915347963532824126765654430594699052974080, -33461752217300086292418732690403936193328483139584, 183413696034380538930126186789493541428881622635396, -452074754310290227070484925879912578654585430305516, 423407546475881497405457539207641395407699803693113, -3289024089508186591347328873559670722024536503984],
[918503115838672219966845425281534935812501667840, -13517205866981193269152583909285043636853977120768, 75602093102339096049853332779603192964429418302972, -190427332833952517550689117440522161634282390885932, 182332618649845499975583265489496618899436808380251, -20967528570614689519839221568942900852906420212898],
[-35520307649253776920433215580451354199754539008, 526563693786084773826019429122644886437178114048, -2955365808870608776506621069837839476472884386876, 7440459508433586864491054942448757739621056919076, -7090873806682664802066063862920275416639027689191, 10483764285307344759919610784471450426453210106449]
]

a=[K(0)]*8
a[0]=K(1);a[1]=K(1);a[2]=theta
for i,rel in enumerate(rels,start=3):
    poly=sum((K(rel[j])*(theta**j) for j in range(5)),K(0))
    a[i]=-poly/K(rel[5])

b=[K(0)]*11;b[0]=K(1)
for k in range(1,11):
    s=K(0)
    for i in range(1,min(7,k)+1):
        s += K(1+2*k-5*i)*a[i]*b[k-i]
    b[k]=-s/K(2*k+1)

# verify W coefficients 0..17
W=[]
for k in range(18):
    s=K(0)
    for i in range(8):
        j=k-i
        if 0<=j<=10:s+=K(1+2*j-3*i)*a[i]*b[j]
    s-=K(1 if k==0 else 0)
    W.append(s)
print('W nonzero',[(i,x) for i,x in enumerate(W) if not x.iszero()])

# polynomial helpers
def pmul(A,B):
    C=[K(0)]*(len(A)+len(B)-1)
    for i,x in enumerate(A):
        for j,y in enumerate(B):C[i+j]=C[i+j]+x*y
    return C
def psub(A,B):
    n=max(len(A),len(B));C=[K(0)]*n
    for i in range(n):C[i]=(A[i] if i<len(A) else K(0))-(B[i] if i<len(B) else K(0))
    while len(C)>1 and C[-1].iszero():C.pop()
    return C
q2=pmul(b,b);zq2=[K(0)]+q2;p3=pmul(pmul(a,a),a);H=psub(zq2,p3)
print('deg H',len(H)-1)
# verify q=pH'-3p'H
Hp=[K(i)*H[i] for i in range(1,len(H))]
ap=[K(i)*a[i] for i in range(1,len(a))]
rhs=psub(pmul(a,Hp),[K(3)*x for x in pmul(ap,H)])
while len(rhs)>1 and rhs[-1].iszero():rhs.pop()
print('q identity',len(rhs),all((rhs[i] if i<len(rhs) else K(0))==b[i] for i in range(max(len(rhs),len(b)))))

# leading tau value
L=(b[10]**2)/(a[7]**3)

def frac_json(x):return {'num':str(x.numerator),'den':str(x.denominator)}
def kel_json(x):return [frac_json(c) for c in x.c]
out={'minimal_polynomial':list(map(str,f)), 'a':[kel_json(x) for x in a], 'b':[kel_json(x) for x in b], 'H':[kel_json(x) for x in H], 'tau_infinity':kel_json(L), 'normalization':'a0=a1=b0=1; theta=a2'}
if OUTPUT is not None:
    (OUTPUT/'exact_belyi_data.json').write_text(json.dumps(out,indent=2))

# concise TeX coefficient formatter
def qtex(q):
    if q.denominator==1:return str(q.numerator)
    return r'\\frac{%d}{%d}'%(q.numerator,q.denominator)
def ktex(x):
    terms=[]
    for i,c in enumerate(x.c):
        if not c:continue
        # generic parenthesized rational coefficients, no pretty sign optimization
        if i==0:term=qtex(c)
        elif i==1:term=r'(%s)\\theta'%qtex(c)
        else:term=r'(%s)\\theta^{%d}'%(qtex(c),i)
        terms.append(term)
    return ' + '.join(terms).replace('+ -','- ') if terms else '0'
if OUTPUT is not None:
    with (OUTPUT/'exact_belyi_coefficients.tex').open('x') as g:
        g.write('%% Auto-generated exact degree-21 Belyi data.\n')
        g.write('\\[f(T)='+ ' + '.join(f'({f[i]})T^{{{i}}}' for i in range(6)) +'=0.\\]\n')
        for name,arr in [('a',a),('b',b),('h',H)]:
            g.write(f'%% {name} coefficients\n')
            for i,x in enumerate(arr):g.write(f'\\newcommand{{\\{name}coef{i}}}{{{ktex(x)}}}\n')
print('wrote data; tau infinity zero?',L.iszero())
print('coefficient max digit sizes')
for name,arr in [('a',a),('b',b),('H',H)]:
  mx=max(max(len(str(abs(c.numerator))),len(str(c.denominator))) for x in arr for c in x.c)
  print(name,mx)
