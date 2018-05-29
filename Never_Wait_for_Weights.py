# coding: utf-8

# Never_Wait_for_Weights,https://onlinejudge.u-aizu.ac.jp/#/problems/1330
# 右,奥

# その点よりも根はどのくらい重いか,という情報を木構造として保存します。
# 入力された情報に対し,一方の点がまだ木に属していないなら,もう一方の木に繋げます。
# どちらの点も木に属しているなら,一方の根をもう一方の根に繋げます。
# 二点が同じ根を持つ場合には,根を基準として重さの差を出力します。

def root(x):
    r = []
    t = 0
    while P[x][0] != x:
        r.append([x,t])
        t += P[x][1]
        x = P[x][0]
    for y in r:
        P[y[0]] = [x,t-y[1]]
    return x,t
def data(x,y,w):
    a,b = root(x)
    c,d = root(y)
    if a != c:
        if a == x:
            P[x] = [y,w]
        elif b == x:
            P[y] = [x,-w]
        else:
            P[a] = [c,w-b+d]
    return P
def diff(x,y):
    a,b = root(x)
    c,d = root(y)
    if a == c:
        return b-d
    else:
        return "UNKNOWN"
while True:
    n,m = map(int,input().strip().split(" "))
    if n == 0:break
    P = [[i,0] for i in range(n+1)]
    for _ in range(m):
        a = list(input().strip().split(" "))
        if a[0] == "!":
            p,q,w = map(int,a[1:])
            P = data(p,q,w)
        else:
            p,q = map(int,a[1:])
            print(diff(p,q))
