# coding: utf-8

# Articulation Points,https://onlinejudge.u-aizu.ac.jp/#/problems/GRL_3_A
# 右、奥

# 各点におけるminの候補は深さ優先探索木での深さ,子孫のmin,元のグラフで隣接して木では隣接しない点の深さなので,
# まず深さが定まった時点で,その値をminの候補として入力します。
# 次に,各点において,それぞれの子を調べ終わった時点で,その子のminを候補として比較します。
# 子とならない点,つまり木として隣接しない点は,先に他の点の子として調べられた点なので,
# 深さはわかっています。よってその深さを候補として比較します。
# さらに再帰性により,子のminは親のminより先に定まります。
# 特に葉については,子孫のmin以外のminの候補値は上述のように定まっているので,minの値も正しく得られます。
# 加えて,孫のminの値は子のminを定める段階で考慮されています。なので子のminを調べれば充分です。
# 根として選んだ点0については子の数を別途数えあげることで関節点かどうかを考えています。

import sys
sys.setrecursionlimit(100000)
def solve():
    def dfs(s):
        M[s] = D[s]
        for j in reversed(range(len(A[s]))):
            i = A[s][j]
            if D[i] == -1:
                if s == 0 and c[0] < 2:
                    c[0] += 1
                A[s].pop(j)
                A[i].remove(s)
                D[i] = D[s] + 1
                dfs(i)
                if M[s] > M[i]:
                    M[s] = M[i]
                if s != 0 and D[s] <= M[i]:
                    P.add(s)
            elif M[s] > D[i]:
                M[s] = D[i]
    V,E = map(int,input().strip().split(" "))
    A = [[] for i in range(V)]
    for _ in range(E):
        s,t = map(int,input().strip().split(" "))
        A[s].append(t)
        A[t].append(s)
    D = [0]+[-1]*(V-1)
    M = [-1]*V
    P = set()
    c = [0]
    dfs(0)
    if c[0] > 1:
        P.add(0)
    for i in sorted(list(P)):
        print(i)
solve()
