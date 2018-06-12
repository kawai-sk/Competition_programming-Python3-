# coding: utf-8

# 崖登り,https://onlinejudge.u-aizu.ac.jp/problems/1150
# 右、奥

# ある地点に右足を移動させたときを0,左足を移動させたときを1で表します。
# それぞれについて,次に動かせる足の範囲をmovに用意しておきます。片方の足を動かせる範囲は
# もう片方の足の位置のみに依存するため,両足の位置をシミュレーションする必要はありません。
# 各点はTなら0,XまたはSなら-1,それ以外なら数値としておきます。
# Sの点に左足または右足を置いた場合のそれぞれを始状態として,
# 両足を交互に動かす変則的なDijkstra法を行います。

from heapq import heappush,heappop
INF = float("inf")
mov = [[[-2, 1], [-1, 1], [-1, 2], [0, 1], [0, 2], [0, 3], [1, 1], [1, 2], [2, 1]],
 [[-2, -1], [-1, -2], [-1, -1], [0, -3], [0, -2], [0, -1], [1, -2], [1, -1], [2, -1]]]
def solve():
    while True:
        W,H = map(int,input().strip().split(" "))
        if W == H == 0:break
        w = [[-1 for i in range(W)] for j in range(H)]
        Q = []
        D = [[[-1,-1] for j in range(W)]for i in range(H)]
        for i in range(H):
            l = list(input().strip().split(" "))
            for j in range(W):
                if l[j] == "T":
                    w[i][j] = 0
                elif l[j] == "S":
                    heappush(Q,(0,i,j,0))
                    heappush(Q,(0,i,j,1))
                    D[i][j] = [0,0]
                elif l[j] != "X":
                    w[i][j] = int(l[j])
        ans = INF
        while Q:
            t,a,b,i = heappop(Q)
            if t < ans:
                for p,q in mov[i]:
                    c,d = a+p,b+q
                    if 0 <= c < H and 0 <= d < W:
                        r = w[c][d]
                        if r == 0:
                            ans = min(ans,t)
                        elif r != -1:
                            s = t + r
                            u = D[c][d][1-i]
                            if u < 0 or u > s:
                                D[c][d][1-i] = s
                                heappush(Q,(s,c,d,1-i))
        if ans == INF:
            print(-1)
        else:
            print(ans)
solve()
