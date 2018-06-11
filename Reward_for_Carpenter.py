# coding: utf-8

# A Reward for a Carpenter,https://onlinejudge.u-aizu.ac.jp/#/problems/0117
# 右、奥

# 二通りで解きました。AOJの方がavailableでないのでacceptedかはわかりませんが、
# Sample Inputには正答しています。

#Floyd-Warshall法で解く場合。

N = int(input())
M = int(input())
W = [[N*1000 if i != j else 0 for j in range(N)]for i in range(N)]
for _ in range(M):
    a,b,c,d = map(int,input().split(","))
    W[a-1][b-1] = c
    W[b-1][a-1] = d
s,g,V,P = map(int,input().split(","))
for k in range(N):
    for i in range(N):
        for j in range(N):
            if W[i][j] > W[i][k]+W[k][j]:
                W[i][j] = W[i][k]+W[k][j]
V -= P+W[s-1][g-1]+W[g-1][s-1]
print(V)

# S→GとG→Sのそれぞれで幅優先探索する場合。

def bfs(s,g):
    cost = 0
    C = [-1 for i in range(N)]
    C[s] = 0
    L,i  = [s],0
    while i < N:
        a = L[i]
        for j in W[a]:
            if C[j] < 0:
                C[j] = C[a] + W[a][j]
                L.append(j)
            elif C[j] > C[a] + W[a][j]:
                C[j] = C[a] + W[a][j]
        i += 1
    return C[g]
N = int(input())
M = int(input())
W = [{} for i in range(N)]
for _ in range(M):
    a,b,c,d = map(int,input().split(","))
    W[a-1][b-1] = c
    W[b-1][a-1] = d
s,g,V,P = map(int,input().split(","))
V -= P+bfs(s-1,g-1)+bfs(g-1,s-1)
print(V)
