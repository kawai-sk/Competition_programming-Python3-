
# coding: utf-8

# In[4]:

# Search-Dictionary,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_4_C
# 右、奥

# 素直に集合を作るだけです。

def find(S,a):
    if a in S:
        return "yes"
    else:
        return "no"
S = set()
n = int(input())
for i in range(n):
    a,b = map(str,input().strip().split(" "))
    if a == "insert":
        S.add(b)
    else:
        print(find(S,b))