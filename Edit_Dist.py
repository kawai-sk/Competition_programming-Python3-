
# coding: utf-8

# In[7]:

# 編集距離、https://onlinejudge.u-aizu.ac.jp/#/problems/DPL_1_E
# 右、奥

# Xの1文字目からi文字目までとYの1文字目からj文字目までに関する編集距離をA[i][j]とします。
# A[i+1][j+1]の最小値の候補としては、A[i][j+1]とA[i+1][j]にそれぞれ1加える場合（1文字追加）と、
# X[i+1]=Y[j+1]の場合のみA[i][j]が考えられます。これらの最小値をA[i+1][j+1]として動的計画法を進めます。


X = str(input())
Y = str(input())
def edit(A,B):
    a,b = len(A),len(B)
    p = [i for i in range(a+1)]
    for j in range(b):
        x,y = 0,p[0]
        p[0] += 1
        for i in range(a):
            x,y = y,p[i+1]
            c = 0 if A[i]==B[j] else 1
            p[i+1] = min(y+1,p[i]+1,x+c)
    return p[-1]
print(edit(X,Y))