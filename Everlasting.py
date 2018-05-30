# coding: utf-8

# Everlastinc-one-,https://onlinejudge.u-aizu.ac.jp/#/problems/2568
# 右,奥

# まず,special pairの入力情報をもとに属性1からnを木構造としてグループ化します。
# この各グループについて,「全属性がlight」「どの属性もlightでない」場合を除けば,
# 残るすべての組合せは問題の条件に基づき互いに移りあうことになります。
# 複数のグループをまとめて考える場合も同様です。
# たとえば2グループをまとめて考えます。
# 一方のグループの全属性がlight,すべてlightでない,それ以外の場合を(a,b,c)と略記します。
# もう一方のグループについても同様に(x,y,z)と略記します。c,zの場合が存在するとは限りません。
#　このとき,両グループの組合せが(a,x),(b,x),(a,y),(b,y)の場合を除けば,
# 残るすべての組合せは,(存在すれば)互いに移りあうことになります。
# 以上から,出力すべき数値は,2^(互いに独立したグループの個数)を基準として,
# もしspecial pairが存在するならそこに1を足せばよいことになります。

def root(x):
    r = []
    while P[x] != x:
        r.append(x)
        x = P[x]
    for y in r:
        P[y] = x
    return x
def data(x,y,n):
    a = root(x)
    c = root(y)
    if a != c:
        if a == x:
            P[x] = c
        else:
            P[c] = a
        n -= 1
    return n
def ans():
    t = 0
    if m >= 1:t=1
    s = (2**n+t)%1000000007
    return s
while True:
    n,m = map(int,input().strip().split(" "))
    if n == 0:break
    P = [i for i in range(n+1)]
    for _ in range(m):
        p,q = map(int,input().strip().split(" "))
        n = data(p,q,n)
    print(ans())
