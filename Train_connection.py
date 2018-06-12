# coding: utf-8

# 電車乗り継ぎ,https://onlinejudge.u-aizu.ac.jp/problems/1182
# 右,奥

# 入力された辺の情報を路線ごとに保存します。
# 各路線について,同じ路線に乗ったまま行ける各経路のコストを求めます。
# これらのコストに関してDijkstra法を用いて最小のコストを求めます。

from heapq import heappop,heappush
from collections import defaultdict
from bisect import bisect
INF = float("inf")
def solve():
    while True:
        N,M,C,S,G = map(int,input().strip().split(" "))
        if N == 0:break
        A = [{} for i in range(N)]
        mats = [[{} for j in range(N)] for i in range(C)]
        for _ in range(M):
            x,y,d,c = map(int,input().strip().split(" "))
            x -= 1
            y -= 1
            c -= 1
            if (not y in mats[c][x]) or mats[c][x][y] > d:
                mats[c][x][y] = d
                mats[c][y][x] = d
        P = list(map(int,input().strip().split(" ")))
        for i in range(C):
            p = P[i]
            mat = mats[i]
            for m in range(N):
                for j in range(N):
                    for k in range(N):
                        if m in mat[j] and m in mat[k]:
                            d1 = mat[j][m]+mat[m][k]
                            if (not j in mat[k]) or d1 < mat[j][k]:
                                mat[j][k] = d1
                                mat[k][j] = d1
            Q = []
            if p > 1:
                Q = list(map(int,input().strip().split(" ")))
            else:
                input()
            R = list(map(int,input().strip().split(" ")))
            for j in range(N):
                for k,d in mat[j].items():
                    if k <= j:
                        c = 0
                        id = bisect(Q,d)
                        pre = 0
                        for l in range(id):
                            c += R[l]*(Q[l]-pre)
                            pre = Q[l]
                        c += R[id]*(d-pre)
                        if (not k in A[j]) or c < A[j][k]:
                            A[j][k] = c
                            A[k][j] = c
            mats[i] = 0
        D = [-1 for _ in range(N)]
        D[S-1] = 0
        Q = [(0,S-1)]
        s = set([i for i in range(N)])
        while s != set() and Q != []:
            d,p = heappop(Q)
            if p in s:
                for j in A[p]:
                    if D[j] < 0 or D[j] > d+A[p][j]:
                        D[j] = d+A[p][j]
                        heappush(Q,(D[j],j))
                s.discard(p)
        print(D[G-1])
solve()
