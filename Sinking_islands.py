# coding: utf-8

# 沈みゆく島,https://onlinejudge.u-aizu.ac.jp/#/problems/2511
# 右,奥

# まず,各島1~nを沈むのが遅い順に並べ,改めて番号を振り直します。
# つまり,島iは最後からi番目に沈む島であるとします。
# 入力される橋の両端の情報もまた振り直された番号によって保存します。

# この番号において,島1から島iを結ぶ最小全域木が存在し,
# かつ任意のj(>i)について島1から島jを結ぶ最小全域木が存在するようなiのなかで最小のものを考えます。

# このiについて,島1から島iを結ぶ最小全域木をなす橋は必ず掛ける必要があります(問題の条件より)。
# さらにj>iに対し,「島1から島jを結ぶグラフ」と島j+1を結ぶ橋は必ず存在します(iも条件より)。
# よって,まず島1から島iを結ぶ最小全域木を求め,これを順々に拡張していくことで,
# 最終的にすべての島を結ぶグラフを構成すればよいことになります。

# 同時に複数の島が沈む可能性についてはwhile文で調整しています。

def root(x):
    r = []
    while tree[x] != x:
        r.append(x)
        x = tree[x]
    for u in r:
        tree[u] = x
    return x
def unite(x,y):
    a,b = root(x),root(y)
    tf = False
    if a != b:
        tf = True
        c,d = rank[a],rank[b]
        if c < d:
            tree[a] = b
        else:
            tree[b] = a
            if c == d:
                rank[a] += 1
    return tf
while True:
    n,m = map(int,input().strip().split(" "))
    if n == 0:break
    h = []
    for _ in range(n):
        h.append(int(input()))
    nums = [i for i in range(n)]
    nums.sort(key=lambda e:-h[e])
    origin = [i for i in range(n)]
    for i in range(n):
        origin[nums[i]] = i
    bridges = []
    for _ in range(m):
        a,b,c = map(int,input().strip().split(" "))
        bridges.append([origin[a-1],origin[b-1],c])
    bridges.sort(key=lambda e:e[2])
    s = 0
    p = 1
    while p < n:
        if s == 0:
            t = 0
            while p+1 < n and h[nums[p]] == h[nums[p+1]]:
                p += 1
            tree = [i for i in range(p+1)]
            rank = [1]*(p+1)
        else:
            tree.append(p)
            rank.append(1)
            while p+1 < n and h[nums[p]] == h[nums[p+1]]:
                p += 1
                tree.append(p)
                rank.append(1)
        i,l = 0,0
        while i < m:
            a,b,c = bridges[i]
            if a <= p and b <= p:
                tf = unite(a,b)
                if tf:
                    l += c
                    t += 1
                    if t == p:
                        break
            i += 1
        if t == p:
            s += l
        else:
            s = 0
        p += 1
    print(s)
