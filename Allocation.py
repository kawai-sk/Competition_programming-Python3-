
# coding: utf-8

# In[18]:

# Allocation,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_4_D
# 右、奥

# 概ね資料の説明のとおりです。lの初期値は荷物の重さの最大値-1、rの初期値は荷物の重さの総和としています。

def solve():
    def ok(l):
        a,b = 0,1
        for i in range(n):
            if a+w[i] <= l:
                a += w[i]
            else:
                a = w[i]
                b += 1
        return b <= k
    n,k = map(int,input().strip().split(" "))
    m = 0
    s = 0
    w = []
    for i in range(n):
        w.append(int(input()))
        s += w[i]
        m = max(m,w[i])
    l,r = m-1,s
    while l + 1 < r:
        h = (l+r)//2
        if ok(h):
            r = h
        else:
            l = h
    print(r)
solve()
