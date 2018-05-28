# coding: utf-8

# Nearest Common Ancestors,http://poj.org/problem?id=1330
# 右、奥

# 一方の点の親を根に達するまで調べてリストアップし,もう一方の親がそこに含まれるか調べていきます。
# POJはPython3に未対応なのでAcceptedかどうかは未確認ですが,
# Sample Inputからは正しい答えが得られました。

T = int(input())
for _ in range(T):
    n = int(input())
    t = [-1]*n
    for __ in range(n-1):
        a,b = map(int,input().strip().split(" "))
        t[b-1] = a
    p,q = map(int,input().strip().split(" "))
    A = set([p])
    while t[p-1] != -1:
        p = t[p-1]
        A.add(p)
    while q != -1:
        if q in A:
            print(q)
            break
        q = t[q-1]
