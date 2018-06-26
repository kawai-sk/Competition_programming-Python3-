# coding: utf-8

# 内点判定,https://onlinejudge.u-aizu.ac.jp/#/problems/0012
# 右,奥

# 点Pを中心として三角形の符号付き面積を考えるだけです。

def cross(a,b):
    return (a.conjugate()*b).imag
def solve():
    P = []
    try:
        while True:
            P.append(list(map(float,input().split())))
    except EOFError:
        pass
    P.reverse()
    while P:
        Q = P.pop()
        x,y,z,p = [complex(Q[i*2],Q[i*2+1]) for i in range(4)]
        x -= p;y -= p;z-=p
        a,b,c = cross(x,y),cross(y,z),cross(z,x)
        R = [a*b,b*c,c*a]
        t = True
        for i in R:
            if i < 0:t = False;break
        print("YES" if t else "NO")
solve()
