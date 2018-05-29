# coding: utf-8

# Fibonacci_Sets,https://onlinejudge.u-aizu.ac.jp/#/problems/1016
# 右、奥

# フィボナッチ数を1001で割った余りをFとして先に作っておきます。
# vまでのFを取り出してソートします。隣り合う項の差がd以上なら別の木に属するものとして数えます。

F = [2,3]+[0 for i in range(2,1000)]
for i in range(2,1000):
    F[i] = F[i-1] + F[i-2]
    if F[i] >= 1001:F[i]-=1001
while True:
    try:
        v,d = map(int,input().strip().split(" "))
        s = [F[i] for i in range(v)]
        s.sort()
        n = 1
        for i in range(v-1):
            if s[i+1] - s[i] >= d:
                n += 1
        print(n)
    except:break
