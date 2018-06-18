
# coding: utf-8

# In[6]:

# Minimal Backgammon,https://onlinejudge.u-aizu.ac.jp/#/problems/1277
# 右、奥

# LとBに気をつけつつ、サイコロを振るごとに各マスを訪れる確率を更新して動的計画法しています。
# 解答を小数第六位まできちんと出力する（ために調べる）のが最難関でした。

def solve():
    while True:
        N,T,L,B = map(int,input().strip().split(" "))
        if N == 0:
            break
        l,b = [],[]
        for i in range(L):
            l.append(int(input()))
        for i in range(B):
            b.append(int(input()))
        p = 0
        P = [[0 for j in range(N)] for i in range(T+1)]
        P[0][0] = 1
        def judge(i,j,m):
            if m in l and i + 2 <= T:
                P[i+2][m] += P[i][j]/6
            elif m in b:
                P[i+1][0] += P[i][j]/6
            else:
                P[i+1][m] += P[i][j]/6
        for i in range(0,T):
            for j in range(min(6*i+1,N)):
                for k in range(1,7):
                    if j + k == N:
                        p += P[i][j]/6
                    elif j + k < N:
                        judge(i,j,j+k)
                    else:
                        judge(i,j,2*N-j-k)
        print("%0.6f" % round(p,6))
solve()
