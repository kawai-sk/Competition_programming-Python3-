# coding: utf-8

# 最近点対,https://onlinejudge.u-aizu.ac.jp/problems/CGL_5_A
# 右,奥

# このコードを参考にしました：https://onlinejudge.u-aizu.ac.jp/solutions/problem/CGL_5_A/review/2257056/bs5lNkJ/Python3

# 二分探索です。
# 二分された区画ごとに相違なるx,y座標を持つ点の数を数え,相違なる点が多い方でソートし直しています.

def dis(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
def clos(P,f):
    n = len(P)
    if n <= 3:
        if n == 2:
            return dis(P[0],P[1])
        elif n == 3:
            return min(dis(P[0],P[1]),dis(P[0],P[2]),dis(P[1],P[2]))
    else:
        m = n//2
        ps = [set([p[i] for p in P]) for i in range(2)]
        f1 = 0 if len(ps[0]) > len(ps[1]) else 1
        f2 = 1 - f1
        if f != f1:
            P.sort(key=lambda e:e[f1])
        dist = min(clos(P[:m],f1),clos(P[m:],f1))
        for i in range(m):
            a = P[m-1-i]
            if P[m][f1] - a[f1] >= dist:
                break
            for j in range(m,n):
                b = P[j]
                if b[f1] - a[f1] >= dist:
                    break
                if b[f2] - dist < a[f2] < b[f2] + dist:
                    dist = min(dist,dis(a,b))
        return dist
N = int(input())
P = []
for _ in range(N):
    P.append(list(map(float,input().strip().split(" "))))
P.sort(key=lambda e:e[0])
print("%.10f" % clos(P,0))
