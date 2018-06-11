# coding: utf-8

# 全点対最短経路,https://onlinejudge.u-aizu.ac.jp/#/problems/GRL_1_C
# 右,奥

# Floyd-Warshall法です。出力を簡単にするため,辺が存在しないことは文字列INFで表しています。


def solve():
    V,E = map(int,input().strip().split(" "))
    D = [["INF" if i != j else 0 for j in range(V)]for i in range(V)]
    for _ in range(E):
        s,t,d = map(int,input().strip().split(" "))
        D[s][t] = d
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][k] != "INF" and D[k][j] != "INF":
                    if D[i][j] == "INF" or D[i][j] > D[i][k]+D[k][j]:
                        D[i][j] = D[i][k]+D[k][j]
    for i in range(V):
        if D[i][i] < 0:
            print("NEGATIVE CYCLE")
            return
    for i in range(V):
        print(*D[i],sep=" ")
solve()
