
# coding: utf-8

# Depth First Search,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_11_B
# 右,奥

# 概ね教材のとおりです。

def dfs(s):
    global t
    D[s] = t
    t += 1
    for j in range(len(A[s])):
        q = A[s][j]
        if D[q] == -1:
            dfs(q)
    F[s] = t
    t += 1
n = int(input())
A = [[]]
for i in range(n):
    a = list(map(int,input().strip().split(" ")))
    A.append(a[2:])
D = [-1]*(n+1)
F = [-1]*(n+1)
t = 1
for i in range(1,n+1):
    if D[i] == -1:
        dfs(i)
for i in range(1,n+1):
    print(str(i)+" "+str(D[i])+" "+str(F[i]))
