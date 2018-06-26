
# coding: utf-8

# convex_cut,https://onlinejudge.u-aizu.ac.jp/problems/2442
# 右,奥

# 頂点の個数が偶数の場合,適当に頂点対を選ぶことで,それらの中点が全て等しくなるかどうかを調べます。
# ある頂点に対し,他のN-1個の頂点との中点をそれぞれ考えれば充分です。

def judge(x,S):
    i = min(S)
    for j in S:
        if i != j and not t[0]:
            if P[i]+P[j] == x:
                if len(S) == 2:
                    t[0] = True
                else:
                    judge(x,S-(set([i,j])))
N = int(input())
P = []
for i in range(N):
    a,b = map(int,input().strip().split(" "))
    P.append(complex(a,b))
t = [False]
if (N+1)%2:
    S = set([i for i in range(N)])
    for i in range(1,N):
        if not t[0]:
            x = P[0]+P[i]
            judge(x,S-(set([0,i])))
if t[0]:
    print("%.5f"%(x.real/2)+" "+ "%.5f" % (x.imag/2))
else:
    print("NA")
