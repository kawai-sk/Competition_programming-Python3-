# coding: utf-8

# いろはちゃんとマス目,https://beta.atcoder.jp/contests/abc042/tasks/arc058_b
# 右,奥

# 移動不可なマス目を通らないような経路は,互いに背反な場合に分けて考えると,i = 0,1,2...に対し
# (1,1)→(H-A-i,B+1+i)→(H,W)
# の形で表せます。このような経路の組合せ数は,それぞれ
# {(H+B-A-1)!/(B+i)!(H-A-1-i)}*{(W+A-B-1)!/(A+i)!(W-B-1-i)!}
# となります。分母にくる各数の階乗の逆元をあらかじめmodsに用意しておき,順々に加算します。

import sys
sys.setrecursionlimit(10000000)
p = 10**9+7
def power(a,b):
    if b == 0:
        return 1
    elif b%2 == 0:
        return (power(a,b//2)**2)%p
    else:
        return (a*power(a,b//2)**2)%p
def fact(a):
    if a <= 0:
        return 1
    else:
        return (a*fact(a-1))%p
H,W,A,B = map(int,input().strip().split(" "))
a,b = fact(H+B-A-1)%p,fact(W+A-B-1)%p
c,d = H-A-1,W-B-1
m = max(H-1,W-1)
mods = [1]*(m+1)
mods[m] = power(fact(m),p-2)
for i in range(m):
    mods[m-i-1] = (mods[m-i]*(m-i))%p
ans = 0
for i in range(min(c,d)+1):
    ans = (ans+a*b*mods[A+i]*mods[B+i]*mods[c-i]*mods[d-i])%p
print(ans)
