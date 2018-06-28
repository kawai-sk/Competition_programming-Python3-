# coding: utf-8

# 多重ループ,https://beta.atcoder.jp/contests/abc021/tasks/abc021_d
# 右,奥

# 重複を許す組合せとして,仕切り棒の位置を考えればよいことになります。
# (N+K-1)C(K)を愚直に動的計画法で求めたのがこのコードです。
# 1<=N,K<=1000の場合までは十分に解けますが,1<=N,K<=10**5の制約下ではTLEになります。

N = int(input())-1
K = int(input())
if N < K:
    N,K = K,N
dp = [1 for i in range(N+K+1)]
for i in range(K):
    p1,p2 = dp[0],dp[1]
    for j in range(i,N+K):
        p2 = dp[j+1]
        dp[j+1] = (p1+dp[j])%(10**9+7) if i != j else 1
        p1 = p2
print(dp[-1])

# 解説(https://www.slideshare.net/chokudai/abc021)に基づくコードです。
# 逆元の考えにより(N+K-1)C(K)を直接計算します。

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
N = int(input())-1
K = int(input())
ans = fact(N+K)
if N < K:
    N,K = K,N
q = power(fact(N),p-2)
ans = (ans*q)%p
i = N
while i > K:
    q = (q*i)%p
    i -= 1
print((ans*q)%p)
