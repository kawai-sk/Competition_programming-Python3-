
# coding: utf-8

# Marked Ancestor,https://onlinejudge.u-aizu.ac.jp/#/problems/2170
# 右、奥

# マークされた点を新たなる根として木を切り離すことで,
# マークされている最も近い祖先が根と一致するようにします。

def root(x):
    while P[x] != -1:
        x = P[x]
    return x
while True:
    n,q = map(int,input().strip().split(" "))
    if n == 0:break
    P = [-1]*(n+1)
    for i in range(2,n+1):
        P[i] = int(input())
    s = 0
    for _ in range(q):
        a,b = input().strip().split(" ")
        if a == "Q":
            s += root(int(b))
        else:
            P[int(b)] = -1
    print(s)
