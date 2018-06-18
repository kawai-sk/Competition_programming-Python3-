# coding: utf-8

N,W = map(int,input().strip().split(" "))
V = [0]*(W+1)
for i in range(N):
    v,w = map(int,input().strip().split(" "))
    for j in range(w,W+1):
        V[j] = max(V[j],V[j-w]+v)
print(V[-1])
