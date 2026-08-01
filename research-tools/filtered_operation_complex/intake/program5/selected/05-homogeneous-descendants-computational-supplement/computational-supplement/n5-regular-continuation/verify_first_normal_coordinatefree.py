#!/usr/bin/env python3
"""Coordinate-free 175-variable first-normal extension check over F_11."""
from itertools import combinations_with_replacement
P=11
A=[[0,5,8,1,3],[0,3,5,8,6],[0,6,9,7,10],[0,5,0,5,3],[0,5,7,8,5]]
B=[[6,3,4,6,7],[8,10,9,8,6],[5,2,2,4,3],[6,6,8,1,2],[6,0,4,10,3]]
C=[[0,6,2,4,0],[7,5,8,5,0],[0,2,8,8,0],[5,9,7,9,0],[4,10,7,8,0]]
u=[7,6,3,10,4];v=[8,9,7,9,1]
trip=list(combinations_with_replacement(range(5),3));tid={(i,tr):i*len(trip)+trip.index(tr) for i in range(5) for tr in trip};NV=175

def inv(a):return pow(a%P,-1,P)
def rank(A):
    A=[[x%P for x in row] for row in A];m=len(A);n=len(A[0]) if m else 0;r=0;piv=[]
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]),None)
        if q is None:continue
        A[r],A[q]=A[q],A[r];z=inv(A[r][c]);A[r]=[x*z%P for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c];A[i]=[(A[i][j]-f*A[r][j])%P for j in range(n)]
        piv.append(c);r+=1
    return r,piv,A
def mm(X,Y):return [[sum(X[i][k]*Y[k][j] for k in range(5))%P for j in range(5)] for i in range(5)]
I=[[int(i==j) for j in range(5)] for i in range(5)]
Mpoly=[A,B,C];pows=[[I]]
for _ in range(4):
    Xs=pows[-1];out=[[[0]*5 for _ in range(5)] for __ in range(len(Xs)+2)]
    for aa,X in enumerate(Xs):
        for bb,Y in enumerate(Mpoly):
            Z=mm(X,Y)
            for i in range(5):
                for j in range(5):out[aa+bb][i][j]=(out[aa+bb][i][j]+Z[i][j])%P
    pows.append(out)
rows=[];labels=[]
for outi in range(5):
    for j in range(5):
        row=[0]*(NV+1)
        for k in range(5):
            for l in range(5):row[tid[(outi,tuple(sorted((j,k,l))))]]=(row[tid[(outi,tuple(sorted((j,k,l))))]]+3*u[k]*u[l])%P
        row[-1]=A[outi][j];rows.append(row);labels.append(('A',outi,j))
        row=[0]*(NV+1)
        for k in range(5):
            for l in range(5):row[tid[(outi,tuple(sorted((j,k,l))))]]=(row[tid[(outi,tuple(sorted((j,k,l))))]]+6*u[k]*v[l])%P
        row[-1]=B[outi][j];rows.append(row);labels.append(('B',outi,j))
        row=[0]*(NV+1)
        for k in range(5):
            for l in range(5):row[tid[(outi,tuple(sorted((j,k,l))))]]=(row[tid[(outi,tuple(sorted((j,k,l))))]]+3*v[k]*v[l])%P
        row[-1]=C[outi][j];rows.append(row);labels.append(('C',outi,j))
for m in range(5):
    for kpow in range(1,6):
        deg=2*(kpow-1)+1;coeff=[[0]*(NV+1) for _ in range(deg+1)]
        for aa,X in enumerate(pows[kpow-1]):
            for bb,base in enumerate([u,v]):
                row=coeff[aa+bb]
                for i in range(5):
                    for j in range(5):
                        c=X[i][j]
                        if not c:continue
                        for l in range(5):
                            idx=tid[(j,tuple(sorted((i,l,m))))]
                            row[idx]=(row[idx]+6*c*base[l])%P
        for q,row in enumerate(coeff):rows.append(row);labels.append(('tr',m,kpow,q))
rc=rank([r[:-1] for r in rows])[0];ra=rank(rows)[0]
rrc=rank([r[:-1] for r in rows[:75]])[0];rra=rank(rows[:75])[0]
idx=[i for i,l in enumerate(labels) if l[0]!='tr' or l[2]<=4]
tc=rank([rows[i][:-1] for i in idx])[0];ta=rank([rows[i] for i in idx])[0]
assert (len(rows),NV)==(225,175)
assert (rrc,rra)==(65,65)
assert (tc,ta)==(125,125)
assert (rc,ra)==(125,126)
print('[ok] rows=225, tensor variables=175')
print('[ok] line restrictions: coefficient/augmented ranks = 65/65')
print('[ok] through characteristic identity 4: ranks = 125/125')
print('[ok] through characteristic identity 5: ranks = 125/126')
