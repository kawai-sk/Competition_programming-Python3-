
# coding: utf-8

N = int(input())
for i in range(N):
    Q = int(input())
    q = Q
    t = 0
    while q > 9:
        r = 0
        p = q
        while p//10 != 0:
            p = p//10
            r = r + 1
        a = (q//10)*(q%10)
        for i in range(2,r+1):
            b = (q//(10**i))*(q%(10**i))
            if b > a:
                a = b
        q = a
        t = t + 1
    print(t)

