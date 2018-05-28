
# coding: utf-8

# In[9]:

# Organize_Your_Train 2,http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1142&lang=jp
# 右、奥

# 文字列に辞書式順序で大小が定まることを利用し,考えうる列車の並びを順に保存して行きます。
# 候補が辞書式順序で小さい順になるように二分法を用い,すでに同じ文字列を考慮していた場合はそのまま返します。


def insert(S,k):
    l = 0
    r = len(S)
    if r == 0:
        return [k]
    elif r == 1:
        p = S[0]
        if p == k:
            return S
        else:
            return [min(p,k),max(p,k)]
    else:
        while l < r:
            m = (l+r)//2
            if k < S[m]:
                r = m
            elif k > S[m]:
                l = m
            else:
                return S
            if (l+r)//2 == m:
                break
        if S[l] <= k:
            l += 1
        return S[:l]+[k]+S[l:]
m = int(input())
for i in range(m):
    s = str(input())
    n = len(s)
    S = []
    for j in range(1,n):
        a,b = [s[:j]],[s[j:]]
        if len(a[0]) > len(b[0]):a,b = b,a
        if len(a[0]) != 1:
            a.append(a[0][::-1])
        if len(b[0]) != 1:
            b.append(b[0][::-1])
        for i in range(len(a)):
            for j in range(len(b)):
                S = insert(S,a[i]+b[j])
                S = insert(S,b[j]+a[i])
    print(len(S))