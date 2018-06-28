# coding: utf-8

# biscuits,https://beta.atcoder.jp/contests/agc017/tasks/agc017_a
# 右,奥

# 偶奇のみに注目したdpです。

N,P = map(int,input().split(" "))
A = list(map(int,input().split(" ")))
B = [1,0]
for _ in range(N):
    a = A.pop()%2
    p,q = B
    B = [p+q,q+p] if a else [2*p,2*q]
print(B[P])
