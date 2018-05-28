
# coding: utf-8

# In[15]:

# 平安京ウォーキング,https://onlinejudge.u-aizu.ac.jp/#/problems/2186
# 右、奥

# 各座標の点に、下から・左から行けるか（道のマタタビの有無）の情報をあらかじめ与えておきます。
# あとは普通の動的計画法です。

N = int(input())
for i in range(N):
    x,y = map(int,input().strip().split(" "))
    W = [[[0,True,True] for j in range(y+1)] for k in range(x+1)]
    p = int(input())
    for j in range(p):
        q = list(map(int,input().strip().split(" ")))
        if q[1] == q[3]:
            W[max(q[0],q[2])][q[1]][1] = False
        elif q[0] == q[2]:
            W[q[0]][max(q[1],q[3])][2] = False
    for j in range(x+1):
        for k in range(y+1):
            if j == k == 0:
                W[j][k][0] = 1
            else:
                if j >= 1 and W[j][k][1] == True:
                    W[j][k][0] += W[j-1][k][0]
                if k >= 1 and W[j][k][2] == True:
                    W[j][k][0] += W[j][k-1][0]
    r = W[x][y][0]
    if r == 0:
        print("Miserable Hokusai!")
    else:
        print(r)