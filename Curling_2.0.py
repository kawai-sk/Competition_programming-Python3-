# coding: utf-8

# Curling 2.0,https://onlinejudge.u-aizu.ac.jp/#/problems/1144
# 右、奥

# 深さ優先探索です。
# ある障害物に衝突した場合はそこを0に変え,当該可能性を調べ終えたら再び1に戻すことで,
# 元データの破壊を避けています。

x = [1,0,-1,0]
y = [0,1,0,-1]
def inside(p,q):
    return (0 <= p < H and 0 <= q < W)
def dfs(p,q,times):
    for i in range(4):
        a,b = p+x[i],q+y[i]
        if inside(a,b) and area[a][b] != 1:
            while inside(a,b):
                if area[a][b] == 1:
                    if times <= 8:
                        area[a][b] = 0
                        dfs(a-x[i],b-y[i],times+1)
                        area[a][b] = 1
                    break
                elif area[a][b] == 3:
                    if ans[0] < 0 or ans[0] > times+1:
                        ans[0] = times+1
                    break
                a += x[i]
                b += y[i]
while True:
    W,H = map(int,input().strip().split(" "))
    if W == H == 0:break
    area = []
    s1,s2 = -1,-1
    for i in range(H):
        f = list(map(int,input().strip().split(" ")))
        if s1 < 0:
            for j in range(W):
                if f[j] == 2:
                    s1,s2 = i,j
        area.append(f)
    ans = [-1]
    dfs(s1,s2,0)
    print(ans[0])
