# coding: utf-8

# 単一始点最短経路,https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A
# 右、奥

# solve2()の方は単なるDijkstra法です。
# solve()の方は,ある点までの距離が更新されるたびにその点を改めて考え直すようにするだけの愚直解法です。
# 速度とコード長にほとんど差はありませんが,メモリにはsolve()の方が若干の余裕があります。

def solve():
    V,E,S = map(int,input().strip().split(" "))
    L = [{} for _ in range(V)]
    for _ in range(E):
        s,t,d = map(int,input().strip().split(" "))
        L[s][t] = d
    D = ["INF" for _ in range(V)]
    D[S] = 0
    K,i,k = [S],0,1
    while i < k:
        p = K[i]
        for j in L[p]:
            if D[j] == "INF" or D[j] > D[p]+L[p][j]:
                D[j] = D[p]+L[p][j]
                K.append(j)
                k += 1
        i += 1
    for i in range(V):
        print(D[i])
solve()

from heapq import heappop,heappush
def solve2():
    V,E,S = map(int,input().strip().split(" "))
    L = [{} for _ in range(V)]
    for _ in range(E):
        s,t,d = map(int,input().strip().split(" "))
        L[s][t] = d
    D = ["INF" for _ in range(V)]
    D[S] = 0
    Q = [(0,S)]
    A = set([i for i in range(V)])
    while A != set() and Q != []:
        d,p = heappop(Q)
        if p in A:
            for j in L[p]:
                if D[j] == "INF" or D[j] > d+L[p][j]:
                    D[j] = d+L[p][j]
                    heappush(Q,(D[j],j))
            A.discard(p)
    for i in range(V):
        print(D[i])
solve2()
