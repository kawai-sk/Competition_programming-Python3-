# coding: utf-8

# Slim Span,https://onlinejudge.u-aizu.ac.jp/#/problems/1280
# 右、奥

# 最小全域木の全探索です。重さ順にエッジをソートし,
# 最初に繋ぐ辺として選ぶものを軽い方から順に調べます。

def root(x):
    r = []
    while P[x] != x:
        r.append(x)
        x = P[x]
    for u in r:
        P[u] = x
    return x
def unite(x,y,n):
    a = root(x)
    c = root(y)
    if a != c:
        if a == x:
            P[x] = c
        else:
            P[c] = a
        n += 1
    return n
while True:
    n,m = map(int,input().strip().split(" "))
    if n == 0:break
    d = []
    for _ in range(m):
        d.append(list(map(int,input().strip().split(" "))))
    d.sort(key=lambda e:e[2])
    w,s = -1,0
    while s <= m - n + 1:
        P = [i for i in range(n+1)]
        t,j,v = 1,s,d[s][2]
        while t < n and j < m:
            p,q = d[j][:2]
            t = unite(p,q,t)
            if t == n:v = d[j][2]-v
            j += 1
        if t == n and (w > v or w == -1):
            w = v
        s += 1
    print(w)
