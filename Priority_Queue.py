
# coding: utf-8

# In[59]:

# Priority_Queue,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_9_C
# 右、奥

# 二分法を用いて小さい順になるように数をinsertしています。最大数を取り出すのはpopで充分です。

def insert(S,k):
    l = 0
    r = len(S)
    if r == 0:
        return [k]
    elif r == 1:
        p = S[0]
        return [min(p,k),max(p,k)]
    else:
        while l < r:
            m = (l+r)//2
            if k < S[m]:
                r = m
            elif k > S[m]:
                l = m
            else:
                l = max(m-1,0)
                break
            if (l+r)//2 == m:
                break
        if S[l] <= k:
            l += 1
        return S[:l]+[k]+S[l:]
S = []
while True:
    m = input().split(" ")
    if m[0] == "insert":
        S = insert(S,int(m[1]))
    elif m[0] == "extract":
        print(S.pop())
    else:
        break