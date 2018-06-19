# coding: utf-8

# 多角形の内部判定,https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_C
# 右,奥

# このコードを参考にしています:https://onlinejudge.u-aizu.ac.jp/solutions/problem/CGL_3_C/review/2216333/bs5lNkJ/Python3
# 各辺について,判定したい点を基準とする位置ベクトルを反時計回りに順に考えます。
# この2ベクトルがなす三角形の面積がゼロのとき,判定したい点は辺の延長線上にあります。
# このとき点が返上にあるためには,2ベクトルが正反対を向いている,つまり内積が負であればよいです
# そうでない場合。
# a=x+yi,b=z+wiとおくと,cross(a,b)=xw-yzなので,y<=0かつw>0かつcross(a,b)>=0という条件は,
# 判定したい点を原点とする座標軸で考えてみると,
# (詳しい計算は略しますが)その辺が実軸の正方向と交わることを意味しています。
# なので,この条件が成り立つたびにflagの真偽を交換し,
# 交差が奇数回なら点は内部にあり,偶数回なら外部にあることがわかります。

def dot(a, b):
    return (a.conjugate()*b).real
def cross(a,b):
    return (a.conjugate()*b).imag
def inside(t):
    flag = False
    for a,b in zip(P,P[1:]):
        a,b = a-t,b-t
        if a.imag > b.imag:
            a,b = b,a
        cr = cross(a,b)
        if cr == 0 and dot(a,b) <= 0:
            return 1
        if a.imag <= 0 and b.imag > 0 and cr >= 0:
            flag = not flag
    return 2 if flag else 0
N = int(input())
P = []
for _ in range(N):
    a,b = map(int,input().split())
    P.append(complex(a,b))
P.append(P[0])
Q = int(input())
for _ in range(Q):
    a,b = map(int,input().split())
    print(inside(complex(a,b)))
