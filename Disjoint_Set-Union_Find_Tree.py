# coding: utf-8

# 互いに素な集合,https://onlinejudge.u-aizu.ac.jp/#/problems/DSL_1_A
# 右、奥

# 概ね教材のとおりです。

def root(x):
    p = []
    while P[x] != x:
        p.append(x)
        x = P[x]
    for q in p:
        P[q] = x
    return x
def same(x,y):
    return root(x) == root(y)
def unite(x,y):
    P[root(x)] = root(y)
n,q = map(int,input().strip().split(" "))
P = [i for i in range(n)]
for _ in range(q):
    a,x,y = map(int,input().strip().split(" "))
    if a == 0:
        unite(x,y)
    else:
        if same(x,y):
            print(1)
        else:
            print(0)
