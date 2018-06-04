# coding: utf-8

# Breadth First Search,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_11_C
# 右,奥

# 概ね教材のとおりです。

n = int(input())
A = [[]]
for i in range(n):
    a = list(map(int,input().strip().split(" ")))
    A.append(a[2:])
D = [-1]+[0]+[-1]*(n-1)
i = 0
Q = [1]
while i < len(Q):
    p = Q[i]
    j = 0
    while j < len(A[p]):
        q = A[p][j]
        if D[q] == -1:
            Q.append(q)
            D[q] = D[p] + 1
        j += 1
    i += 1
for i in range(1,n+1):
    print(str(i)+" "+str(D[i]))
