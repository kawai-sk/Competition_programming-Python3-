# coding: utf-8

# 凸包関連の問題。
# 右,奥

# Y座標によりソートしたのち,各点を凸包の候補としてQに加えていきます.
# もしQ[-2]とQ[-1]のなす辺が凸包の一部なら,その他の点はこの辺の一方の側
# （今回は反時計回りを考えているため左側）にあるはずです。そうでない場合は
# Q[-1]を除くことを繰り返します。
# Y座標最小の点を出発して最大の点に達したら,同様の手順で折り返します。

# 凸包,https://onlinejudge.u-aizu.ac.jp/problems/CGL_4_A

def cross(p,q):
    a,b = p[1]-p[0],q-p[0]
    return (a.conjugate()*b).imag
N = int(input())
P = []
for _ in range(N):
    a,b = map(int,input().strip().split(" "))
    P.append(complex(a,b))
P.sort(key=lambda e:(e.imag,e.real))
Q = [P[0],P[1]]
i = 2
while i < N:
    while len(Q) > 1 and cross(Q[-2:],P[i]) < 0:
        Q.pop()
    Q.append(P[i])
    i += 1
q = len(Q)
Q.append(P[N-2])
i = N-3
while i >= 0:
    while len(Q) > q and cross(Q[-2:],P[i]) < 0:
        Q.pop()
    if i > 0:Q.append(P[i])
    i -= 1
print(len(Q))
for i in Q:
    print(str(int(i.real)) + " " + str(int(i.imag)))

# 輪ゴム,https://onlinejudge.u-aizu.ac.jp/#/problems/0068

def cross(p,q):
    a,b = p[1]-p[0],q-p[0]
    return (a.conjugate()*b).imag
def solve():
    while True:
        N = int(input())
        if N == 0:break
        P = []
        for _ in range(N):
            a,b = map(float,input().strip().split(","))
            P.append(complex(a,b))
        P.sort(key=lambda e:(e.imag,e.real))
        Q = [P[0],P[1]]
        i = 2
        while i < N:
            while len(Q) > 1 and cross(Q[-2:],P[i]) < 0:
                Q.pop()
            Q.append(P[i])
            i += 1
        q = len(Q)
        Q.append(P[N-2])
        i = N-3
        while i >= 0:
            while len(Q) > q and cross(Q[-2:],P[i]) < 0:
                Q.pop()
            if i > 0:Q.append(P[i])
            i -= 1
        print(N-len(Q))
solve()
