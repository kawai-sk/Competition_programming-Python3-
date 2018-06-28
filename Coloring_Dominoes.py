# coding: utf-8

# Coloring Dominoes,https://beta.atcoder.jp/contests/arc081/tasks/arc081_b
#右,奥

# 上から下,左から右へ順々に探索していきます。
# 各ドミノに対してすでに調べ終わったドミノが隣接している場合,その名前を記録します。
# 隣接するドミノの数nが1以下の場合,塗り方はans*(3-i)通りあります。
# 隣接するドミノが2個の場合。
# それらのドミノもまた互いに隣接しているなら,塗り方は一意に定まります。
# そうでない場合は,今考えているドミノに隣接する2つのドミノは同じドミノに隣接しています。
# つまり次のような状況です。
# 　　　aabb
# 　　　ccdd(←now)
# この場合は,aaまでの塗り方がx通りの場合,ccまでの塗り方は2x通り,bbまでの塗り方はans=4x通り,と
# 動的計画法により計算されています。なのでddまでの塗り方は6x=ans*1.5通りとわかります。

def check(i,j):
    if i > 0:
        k = S[j][i-1]
        if k in checked and not k in C:
            C.append(k)
    if j > 0:
        l = S[j-1][i]
        if l in checked and not l in C:
            C.append(l)
N = int(input())
S = [list(input()) for _ in range(2)]
ans = 1
checked = {}
for i in range(N):
    for j in range(2):
        p = S[j][i]
        if not p in checked:
            C = []
            check(i,j)
            if j < 1 and S[j+1][i] == p:
                check(i,j+1)
            checked[p] = C
            if len(C) > 1:
                if not C[0] in checked[C[-1]]:
                    ans = ((ans*3)//2)
            else:
                ans = (ans*(3-len(C)))
print(ans%(10**9+7))
