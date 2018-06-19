# coding: utf-8

# 凸多角形の面積
# 右,奥

# 同系統の問題をまとめて。面積の算出は符号付き三角形の面積の和に依ります。

# https://onlinejudge.u-aizu.ac.jp/problems/0079

import cmath
def cross(a,b):
    return (a.conjugate()*b).imag
P = []
try:
    while True:
        x,y = map(float,input().split(","))
        P.append(complex(x,y))
except EOFError:
    pass
N = len(P)
s = 0.0
for i in range(1,N-1):
    a,b,c = P[0],P[i],P[i+1]
    b,c = b-a,c-a
    s += cross(b,c)
print("%.6f" % (abs(s)/2.0))

# https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_A

def cross(a,b):
    return (a.conjugate()*b).imag
P = []
N = int(input())
for i in range(N):
    x,y = map(float,input().split(" "))
    P.append(complex(x,y))
s = 0.0
for i in range(1,N-1):
    a,b,c = P[0],P[i],P[i+1]
    b,c = b-a,c-a
    s += cross(b,c)
print("%.1f" % (abs(s)/2.0))

# https://onlinejudge.u-aizu.ac.jp/problems/1100

def solve():
    def cross(a,b):
        return (a.conjugate()*b).imag
    t = 0
    while True:
        N = int(input())
        if N == 0:break
        t += 1
        P = []
        for i in range(N):
            x,y = map(float,input().split(" "))
            P.append(complex(x,y))
        input()
        s = 0.0
        for i in range(1,N-1):
            a,b,c = P[0],P[i],P[i+1]
            b,c = b-a,c-a
            s += cross(b,c)
        print(str(t)+" "+"%.1f" % (abs(s)/2.0))
solve()
