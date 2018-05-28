
# coding: utf-8

# Minimum Spanning Tree,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_12_A
# 右、奥

# 重複を避けつつ,存在する辺の両端の番号と重みを記録します。これをソートします。
# あとは閉路になる可能性に注意しつつ軽い辺から調べていくだけです。

def root(x):
    r = []
    while P[x] != x:
        r.append(x)
        x = P[x]
    for u in r:
        P[u] = x
    return x
n = int(input())
d = []
for i in range(n):
    a = list(map(int,input().strip().split(" ")))
    for j in range(i+1,n):
        if a[j] != -1:
            d.append([i,j,a[j]])
d.sort(key=lambda e:-e[2])
s,t = 0,1
P = [i for i in range(n)]
while t < n:
    p,q,r = d.pop()
    a,b = root(p),root(q)
    if a != b:
        s += r
        t += 1
        P[a] = b
print(s)
