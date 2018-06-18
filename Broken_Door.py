# coding: utf-8

# 壊れたドア,https://onlinejudge.u-aizu.ac.jp/problems/1178
# 右,奥

# このサイト(http://kagamiz.hatenablog.com/entry/2017/09/28/233201)の説明に基づきます。
# まず,各部屋について,各ドアが壊れていた場合のゴールへの距離の最大値を求めます。
# 次に二分探索により,カードm枚でゴールまで行けるかどうかの判定を繰り返します。
# この判定は,その部屋に着くまでのカード枚数+上で求めた距離<mを満たす部屋へ順々に移動し,
# ゴールまでたどり着けるかどうかの判断によって行います。
# 部屋の番号は,縦の座標*横の長さ+横の長さを用いることで一次元的に管理しています。

from heapq import heappush,heappop
import time
INF = float("inf")
def solve():
    def ok(k):
        Q = [(0,0)]
        S = set([i for i in range(0,n)])
        while Q:
            d,s = heappop(Q)
            if s in S:
                S.discard(s)
                if s == n-1:
                    if d <= k:
                        return True
                        break
                if d + D[s] <= k:
                    for mov in maze[s]:
                        nex = s + mov
                        if nex in S:
                            heappush(Q,(d+1,nex))
        return False
    while True:
        h,w = map(int,input().strip().split(" "))
        if h == w == 0:break
        n = h*w
        maze = [[] for i in range(n)]
        D = [-1 for i in range(n-1)]+[0]
        for j in range(h):
            if j > 0:
                door = list(map(int,input().strip().split(" ")))
            line = list(map(int,input().strip().split(" ")))
            for i in range(w):
                if i < w-1 and line[i] == 0:
                    p = j*w+i
                    maze[p].append(1)
                    maze[p+1].append(-1)
                if j > 0 and door[i] == 0:
                    q = (j-1)*w+i
                    maze[q].append(w)
                    maze[q+w].append(-w)
        for i in range(n-1):
            do = maze[i]
            for b in do:
                Q = []
                for j in do:
                    if j != b:heappush(Q,(1,i+j))
                S = set([j for j in range(0,n)])
                S.discard(i)
                tf = True
                while Q:
                    d,s = heappop(Q)
                    if s in S:
                        S.discard(s)
                        if s == n-1:
                            tf = False
                            if d > D[i]:D[i] = d
                            break
                        else:
                            for mov in maze[s]:
                                nex = s + mov
                                if nex in S:
                                    heappush(Q,(d+1,nex))
                if tf:
                    D[i] = INF
                    break
        l,r,t = D[0],2*n,True
        while l+1 < r:
            m = (l+r)//2
            if ok(m):
                r,t = m,False
            else:
                l = m
        if t:
            print(-1)
        elif ok(l):
            print(l)
        else:
            print(r)
solve()
