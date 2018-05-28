
# coding: utf-8

# In[2]:

# 0-1 ナップザック問題,https://onlinejudge.u-aizu.ac.jp/#/problems/DPL_1_B
# 右、奥
# 重さごとの価値の最大値を順々に更新していきます。
# 同じものが二回入る可能性を排するためにW-jと逆順で調べています。


N,W = map(int,input().strip().split(" "))
V = [0]*(W+1)
for i in range(N):
    v,w = map(int,input().strip().split(" "))
    for j in range(W+1-w):
        V[W-j] = max(V[W-j],V[W-j-w]+v)
print(V[-1])