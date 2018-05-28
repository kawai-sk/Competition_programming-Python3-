
# coding: utf-8

# In[16]:

# Make Purse Light, http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2007&lang=jp
# 右、奥

# 払いきれるならば何円払っても払ったあとの財布の中の金額は同じです。
# なので、財布の中身を全部出してお釣りをもらったと仮定し、お釣りに支払ったのと同じ硬貨が現れたらそれを除きます。

z = 1
while z > 0:
    N = int(input())
    TF = False
    if N == 0:
        break
    if z > 1:
        print()
    else:
        TF = True
    c = list(map(int,input().strip().split(" ")))
    d = [10,50,100,500]
    p = 0
    for i in range(0,4):
        p = c[i]*d[i] + p
    n = p - N
    e = [(n%50)//10,(n%100)//50,(n%500)//100,n//500]
    for i in range(0,4):
        if c[i]-e[i] > 0:
            print(str(d[i])+" "+str(c[i]-e[i]))
    z = z + 1