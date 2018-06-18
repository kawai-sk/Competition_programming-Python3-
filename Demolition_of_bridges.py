# coding: utf-8

# 橋の取り壊し,https://onlinejudge.u-aizu.ac.jp/#/problems/0180
# 右,奥

# 各都市を結ぶ橋が閉路となっている状況では余分な維持費が使われていることになります。
# 一度すべての橋を除いてから,全都市が共通のグラフに含まれるのに充分な橋だけ残せばよい。
# つまり最小全域木を考えます。

def solve():
    def root(x):
        r = []
        while P[x] != x:
            r.append(x)
            x = P[x]
        for u in r:
            P[u] = x
        return x
    while True:
        n,q = map(int,input().strip().split(" "))
        if n == 0:break
        d = []
        for i in range(q):
            d.append(list(map(int,input().strip().split(" "))))
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
solve()
