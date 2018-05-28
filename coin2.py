
# coding: utf-8

# In[41]:

# Coin Changing Problem,https://onlinejudge.u-aizu.ac.jp/#/problems/DPL_1_A
# 右、奥

# i円払うために必要な最小の硬貨枚数を動的計画法で求めています。


n,m = map(int,input().strip().split(" "))
C = list(map(int,input().strip().split(" ")))
c = [n for _ in range(n+1)]
c[0] = 0
for i in C:
    for j in range(n-i+1):
        c[j+i] = min(c[j+i],c[j]+1)
print(c[n])