# coding: utf-8

# 橋,https://onlinejudge.u-aizu.ac.jp/#/problems/GRL_3_B
# 右,奥

# 関節点の求め方と概ね同様です。
# その点の深さ<子のminの場合,子の先のグラフは完結しているので,この点と子とを結ぶ辺は橋だとわかります。

import sys
sys.setrecursionlimit(100000)
def dfs(s):
    M[s] = D[s]
    for j in reversed(range(len(A[s]))):
        i = A[s][j]
        if D[i] == -1:
            A[s].pop(j)
            A[i].remove(s)
            D[i] = D[s] + 1
            dfs(i)
            if M[s] > M[i]:
                M[s] = M[i]
            if D[s] < M[i]:
                bridges.append([s,i]) if s < i else bridges.append([i,s])
        elif M[s] > D[i]:
            M[s] = D[i]
V,E = map(int,input().strip().split(" "))
A = [[] for i in range(V)]
for _ in range(E):
    s,t = map(int,input().strip().split(" "))
    A[s].append(t)
    A[t].append(s)
D = [0]+[-1]*(V-1)
M = [-1]*V
bridges = []
dfs(0)
for i in sorted(bridges,key=lambda e:(e[0],e[1])):
    print(str(i[0])+" "+str(i[1]))
