# coding: utf-8

# 経路,https://beta.atcoder.jp/contests/abc037/tasks/abc037_d
# 右,奥

# 各マスについて,その点で止まる場合の経路+そこからいけるマスを始点とする経路数,を考えればよいです。
# 一度調べたマスについてはその結果を保存しておきます。

# 解説を見たところ想定解どおりでしたがRE,TLEはどうしても出ます。

def dfs(i,j):
    D[i][j] = 1
    for k in range(4):
        p,q = i+x[k],j+y[k]
        if 0 <= p < H and 0 <= q < W:
            if A[i][j] < A[p][q]:
                if D[p][q] < 0:
                    dfs(p,q)
                D[i][j] += D[p][q]
    ans[0] += D[i][j]
H,W = map(int,input().split(" "))
A = []
for _ in range(H):
    A .append(list(map(int,input().split(" "))))
x = [1,0,-1,0]
y = [0,1,0,-1]
D = [[-1]*W for _ in range(H)]
ans = [0]
for i in range(H):
    for j in range(W):
        if D[i][j] < 0:
            dfs(i,j)
print(ans[0])
