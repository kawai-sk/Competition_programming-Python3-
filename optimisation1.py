# coding: utf-8

import sympy
from sympy import *
from scipy.optimize import fmin
from scipy import optimize
x_1 = Symbol("x_1",real=True)
x_2 = Symbol("x_2",real=True)
y = Symbol("y",real=True)

def devided_matrix(A,i,j):#余因子行列
    m = len(A)
    n = len(A[0])
    if i < 1 or j < 1 or i > m or j > n:
        return None
    else:
        B = [[0 for l in range(0,n-1)]for k in range(0,m-1)]
        for k in range(0,m):
            for l in range(0,n):
                if k < i-1 and l < j-1:
                    B[k][l] = A[k][l]
                elif k < i-1 and l > j-1:
                    B[k][l-1] = A[k][l]
                elif k > i-1 and l < j-1:
                    B[k-1][l] = A[k][l]
                elif k > i-1 and l > j-1:
                    B[k-1][l-1] = A[k][l]
        return B
def det(A):#行列式
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    else:
        if m == 1:
            return A[0][0]
        elif m == 2:
            return A[0][0]*A[1][1]-A[0][1]*A[1][0]
        else:
            d = 0
            for i in range(0,n):
                if i/2 == i//2:
                    d = d + A[i][0]*det(devided_matrix(A,i+1,1))
                else:
                    d = d - A[i][0]*det(devided_matrix(A,i+1,1))
            return d
def inversed(A):#逆行列
    if len(A) != len(A[0]):
        return None
    else:
        d = det(A)
        if d == 0:
            return None
        else:
            n = len(A)
            B = [[0 for l in range(0,n)]for k in range(0,n)]
            for i in range(0,n):
                for j in range(0,n):
                    if (i+j)/2==(i+j)//2:
                        B[i][j] = det(devided_matrix(A,j+1,i+1))/d
                    elif (i+j)/2!=(i+j)//2:
                        B[i][j] = -det(devided_matrix(A,j+1,i+1))/d
            return B
def mat_times(A,B):#行列の積
    i = len(A)
    j = len(A[0])
    k = len(B)
    l = len(B[0])
    if j != k:
        return None
    else:
        C = [[0 for p in range(0,l)]for q in range(0,i)]
        for x in range(0,i):
            for y in range(0,l):
                for m in range(0,j):
                    C[x][y] = C[x][y] + A[x][m]*B[m][y]
        return C
def mat_sum(A,B):#行列の和
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))]for i in range(len(A))]
def mat_sub(A,B):#行列の差
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))]for i in range(len(A))]
def mat_sch(A,a):#行列のスカラー倍
    return [[A[i][j]*a for j in range(len(A[0]))]for i in range(len(A))]
def t(a):#転置行列
    n = len(a)
    m = len(a[0])
    return [[a[i][j] for i in range(n)]for j in range(m)]
def I(n):#単位行列
    return [[1 if j == i else 0 for j in range(n)]for i in range(n)]

def grad(f,X):#勾配
    return [diff(f,i) for i in X]
def sub_s(f,A,X):#スカラー関数への代入
    return f.subs([(X[i],A[i])for i in range(len(X))])
def sub_v(F,A,X):#横ベクトル関数（配列）への代入
    return [F[i].subs([(X[j],A[j])for j in range(len(X))]) for i in range(len(F))]
def sub_t(F,A,X):#縦ベクトル関数（配列の配列）への代入
    return [[F[i].subs([(X[j],A[j][0])for j in range(len(X))])] for i in range(len(F))]

def norm(f,X):#横ベクトルのノルム
    return sum(f[i]**2 for i in range(len(X)))**0.5
def norm_t(f,X):#縦ベクトルのノルム
    return sum(f[i][0]**2 for i in range(len(X)))**0.5

X = [x_1,x_2]
f = 100*(x_2-x_1**2)**2+(1-x_1)**2
g = grad(f,X)
h = [grad(g[i],X) for i in range(len(g))]
h_1 = inversed(h)
h_2 = mat_times(h_1,[[g[0]],[g[1]]])
h_2 = [h_2[0][0],h_2[1][0]]

def descent(f,a_0,e,X):#最急降下法
    print("初期点",(a_0[0],a_0[1]),"許容誤差",e)
    g = grad(f,X)
    n = len(X)
    x_0 = a_0
    d = sub_v(g,x_0,X)
    xs = [[x_0[i]] for i in range(n)]
    k = 0
    while norm(d,X) >= e:
        def l(x):
            return sub_s(f,[x_0[i]-x*d[i] for i in range(n)],X)
        a = optimize.brent(l)
        for i in range(n):
            x_0[i] -= a*d[i]
        d = sub_v(g,x_0,X)
        for i in range(n):
            xs[i].append(x_0[i])
        k += 1
    print("反復数",k)
    print("停止点",(x_0[0],x_0[1]))
    return x_0,xs

descent(f,[1.2,1.2],0.01,X)[1]

descent(f,[-1.2,1],0.1,X)

def descent_ad(f,a_0,b,e,p,c,X):#最急降下法の改良
    print("初期点",(a_0[0],a_0[1]),"許容誤差",e)
    print("alpha=",b,"rho=",p,"C_1=",c)
    g = grad(f,X)
    n = len(X)
    x_0 = a_0
    d = sub_v(g,x_0,X)
    xs = [[x_0[i]] for i in range(n)]
    k = 0
    while norm(d,X) >= e:
        #print(x_0,k)
        a = b
        f_1 = sub_s(f,x_0,X)
        g_1 = sub_v(g,x_0,X)
        f_2 = -f_1*d[0]+g_1[1]*d[1]
        while True:
            f_3 = sub_s(f,[x_0[i]-a*d[i] for i in range(n)],X)
            if f_3 <= f_1+c*a*f_2:
                break
            else:
                a *= p
        for i in range(n):
            x_0[i] -= a*d[i]
        for i in range(n):
            xs[i].append(x_0[i])
        d = sub_v(g,x_0,X)
        k += 1
    print("反復数",k)
    print("停止点",(x_0[0],x_0[1]))
    return x_0,xs

descent_ad(f,[1.2,1.2],4,0.01,0.3,0.9,X)[0]

descent_ad(f,[-1.2,1],4,0.01,0.3,0.9,X)

def newton(f,a_0,e,X):#Newton法
    print("初期点",(a_0[0],a_0[1]),"許容誤差",e)
    n = len(X)
    g = grad(f,X)
    h = [grad(g[i],X) for i in range(len(g))]
    h_1 = inversed(h)
    h_2 = mat_times(h_1,[[g[i]] for i in range(n)])
    h_2 = [h_2[i][0] for i in range(n)]
    g_1 = norm(g,X)
    x_0 = a_0
    xs = [[x_0[i]] for i in range(n)]
    k = 0
    while sub_s(g_1,x_0,X) >= e:
        d = sub_v(h_2,x_0,X)
        for i in range(n):
            x_0[i] -= d[i]
        for i in range(n):
            xs[i].append(x_0[i])
        k += 1
    print("反復数",k)
    print("停止点",(x_0[0],x_0[1]))
    return x_0,xs

newton(f,[1.2,1.2],0.0001,X)[1]

newton(f,[-1.2,1],0.0001,X)

def semi_newton(f,a_0,e,X):#準Newton法
    print("初期点",(a_0[0],a_0[1]),"許容誤差",e)
    n = len(X)
    g = grad(f,X)
    B = [sub_v(grad(g[i],X),a_0,X) for i in range(n)]
    H = inversed(B)
    x_n = [[a_0[i]] for i in range(n)]
    x_p = [[0] for i in range(n)]
    y_n= sub_t(g,x_n,X)
    y_p = [[0] for i in range(n)]
    xs = [[x_n[i][0]] for i in range(n)]
    k = 0
    while norm_t(y_n,X) >= e:
        s = mat_sub(x_n,x_p)
        y = mat_sub(y_n,y_p)
        m = 1/mat_times(t(s),y)[0][0]
        r = mat_sub(I(n),mat_sch(mat_times(s,t(y)),m))
        H = mat_times(mat_times(r,H),t(r))
        H = mat_sum(H,mat_sch(mat_times(s,t(s)),m))
        x_p,y_p = x_n,y_n
        d = mat_times(H,y_n)
        def l(x):
            return sub_s(f,[x_n[i][0]-x*d[i][0] for i in range(n)],X)
        a = optimize.brent(l)
        x_n = mat_sub(x_n,mat_sch(d,a))
        for i in range(n):
            xs[i].append(x_n[i][0])
        y_n = sub_t(g,x_n,X)
        k += 1
    print("反復数",k)
    print("停止点",(x_n[0],x_n[1]))
    return x_n,xs

semi_newton(f,[1.2,1.2],0.000001,X)[0]

semi_newton(f,[-1.2,1],0.000001,X)

#描画
get_ipython().magic('matplotlib notebook')
get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.cm as cm
xs = descent(f,[1.2,1.2],0.01,X)[1]
x = xs[0]
y = xs[1]
n = len(x)
for i in range(n):
    plt.plot(x[i],y[i],".",color=((4*n-3*i)/(5*n),(4*n-3*i)/(5*n),(4*n-3*i)/(5*n)))
plt.show()
