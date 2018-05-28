
# coding: utf-8

# In[60]:

# コッホ曲線、https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_5_C
# 右、奥

# ベクトル的な考えに基づく再帰的計算で頂点の座標を求め、出力しています。

import math
n = int(input())
x = [0,0]
y = [100,0]
C = [x,y]
def show(a):
    print(str(a[0])+" "+str(a[1]))
def Koch(p,q,i):
    if i < 1:
        show(p)
    r = [p[0]+(q[0]-p[0])/3,p[1]+(q[1]-p[1])/3]
    s = [p[0]+2*(q[0]-p[0])/3,p[1]+2*(q[1]-p[1])/3]
    t = [r[0]+(s[0]-r[0])/2-math.sqrt(3)*(s[1]-r[1])/2,
         r[1]+math.sqrt(3)*(s[0]-r[0])/2+(s[1]-r[1])/2]
    if i < n-1:
        Koch(p,r,i+1)
        Koch(r,t,i+1)
        Koch(t,s,i+1)
        Koch(s,q,i+1)
    elif i == n-1:
        show(r)
        show(t)
        show(s)
    if i > n-2:
        show(q)
Koch(x,y,0)
