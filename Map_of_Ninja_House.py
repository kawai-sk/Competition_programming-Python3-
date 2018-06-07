# coding: utf-8

# Map of Ninja House,https://onlinejudge.u-aizu.ac.jp/#/problems/1236
# 右、奥

# 深さ優先探索です。
# counterの番号tと部屋番号nは全体で管理しつつ再帰を行います。
# 再帰の途中でnが変わってから戻っても元の部屋の番号がわかるようs=nとします。
# 各部屋の調べていない扉の数をlに保存し,l[i]が0になったら部屋iはそれ以上調べません。
# L[t]<0の場合に算出される距離から部屋の番号を逆引きできるように,
# roomsを{距離:番号}とします。最初の部屋からの距離が等しい部屋を訪れることもあり得ますが,
# 2部屋目以降の部屋を訪れるのはそれ以前の部屋を調べ終えてからなので,情報を更新して問題ないです。

def dfs(d):
    global t,n
    s = n
    t += 1
    while l[s] > 0 and t < len(L):
        if L[t] > 0:
            n += 1
            l[s] -= 1
            l.append(L[t]-1)
            A.append([s])
            A[s].append(n)
            rooms[d+1] = n
            dfs(d+1)
        elif L[t] < 0:
            j = rooms[d+L[t]]
            l[j] -= 1
            l[s] -= 1
            A[s].append(j)
            A[j].append(s)
            t += 1
N = int(input())
for _ in range(N):
    L = list(map(int,input().strip().split(" ")))
    while L[-1] != 0:
        L += list(map(int,input().strip().split(" ")))
    A = [[],[]]
    rooms = {0:1}
    l = [0,L[0]]
    t,n = 0,1
    dfs(0)
    for i in range(1,len(A)):
        A[i].sort()
        s = str(i)
        for j in range(len(A[i])):
            s += " "+str(A[i][j])
        print(s)
