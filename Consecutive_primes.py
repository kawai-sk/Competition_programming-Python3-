
# coding: utf-8

# In[13]:

# Sum of Consecutive Prime Numbers,https://onlinejudge.u-aizu.ac.jp/#/problems/1257
# 右、奥

# 概ね教材のとおりです。


P = [2]
p = 2
while p <= 10000:
    i = 0
    while i < len(P):
        if p%P[i] == 0:
            break
        i += 1
    if i == len(P):
        P.append(p)
    p += 1
def prim(a):
    s,i = 0,1
    q,Q = 2,[2]
    while i < len(P) and P[i-1] <= a:
        if q < a:
            Q.append(P[i])
            q += P[i]
            i += 1
        else:
            if q == a:s+= 1
            r = Q.pop(0)
            q -= r
    return s
while True:
    n = int(input())
    if n == 0:break
    print(prim(n))