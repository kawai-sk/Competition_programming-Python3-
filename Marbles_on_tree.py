# coding: utf-8

# Marbles on a tree,http://poj.org/problem?id=1909
# 右、奥

# 各点における果物の数,親の番号,子の番号の集合をそれぞれ保存。
# 根から掘り進むようにして再帰的に子を調べ,末端の果物が1個になるよう直属の親と調整します。
# 形式的な計算なので親が持つ果物が負の個数になることも許容できます。
# 各点の果物が1個となるように調整しつつ根まで戻ってきます。

# POJはPython3に未対応なのでAcceptedかどうかは未確認ですが,
# Sample Inputからは正しい答えが得られました。

def z(x,a,b,c,s):
    if c[x] != []:
        for y in c[x]:
            s = z(y,a,b,c,s)
    if b[x] != -1 and a[x] != 1:
        a[b[x]] += a[x] - 1
        s += abs(a[x] - 1)
        a[x] = 1
    return s
while True:
    n = int(input())
    if n == 0:break
    a = [0]*n
    b = [-1]*n
    c = []
    for i in range(n):
        p = list(map(int,input().strip().split(" ")))
        a[i] = p[1]
        for j in range(3,3+p[2]):
            b[p[j]-1] = i
        c.append([p[j]-1 for j in range(3,3+p[2])])
    i = 0
    while b[i] != -1:
        i = b[i]
    print(z(i,a,b,c,0))
