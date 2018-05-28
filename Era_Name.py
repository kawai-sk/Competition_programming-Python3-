
# coding: utf-8

# In[5]:

# Era Name, http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2242&lang=jp
# 右、奥

# 概ね教材のとおりです。対応表の参照には二分法を用います。


def check(y,Y):
    l,r = 0,len(Y)
    while l + 1 < r:
        m = (l+r)//2
        if y <= Y[m][1]:
            r = m
        elif y > Y[m][2]:
            l = m
        else:
            l = m
            break
    if Y[l][1] < y <= Y[l][2]:
        return Y[l][0] + " " + str(y-Y[l][1])
    else:
        return "Unknown"
while True:
    N,Q = map(int,input().strip().split(" "))
    if N == Q == 0:break
    Y = []
    for i in range(N):
        n,a,b = input().strip().split(" ")
        Y.append([n,int(b)-int(a),int(b)])
    Y.sort(key=lambda e:e[1])
    for i in range(Q):
        y = int(input())
        print(check(y,Y))