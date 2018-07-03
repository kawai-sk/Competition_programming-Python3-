# coding: utf-8

# 如何に汝を満足せしめむ？ いざ数え上げむ…,https://onlinejudge.u-aizu.ac.jp/problems/1155
# 右、奥

# P,Q,Rの値の組合せは,i%3,i//3%3,i//9%3(0<=i<27)によって尽くされます。
# 三値論理の否定は-i=2-i,論理和はi+j=max(i,j),論理積はi*j=min(i,j)によって表現できます。
# あとは普通に計算するだけです。

A = ["P","Q","R"]
B = ["*","+"]
def solve():
    def calc(x,t):
        q = False
        while x < len(l):
            j = l[x]
            if j in B:
                y = B.index(j)
                x,a = calc(x+1,1)
                q = [max(a[i],q[i]) if y else min(a[i],q[i]) for i in range(27)]
            else:
                if j == "(":
                    x,a = calc(x+1,-1)
                elif j == "-":
                    x,a = calc(x+1,1)
                    a = [2-a[i] for i in range(27)]
                elif j in ["0","1","2"]:
                    a = [int(j)]*27
                    x += 1
                elif j in A:
                    y = A.index(j)
                    a = [i//(3**y)%3 for i in range(27)]
                    x += 1
                elif t < 0 and l[x] == ")":
                    x += 1
                    break
                if t > 0:
                    return x,a
                else:
                    q = a
        return x,q
    while True:
        l = list(input())
        if l[0] == ".":break
        print(calc(0,0)[1].count(2))
solve()
