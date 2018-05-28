
# coding: utf-8

# In[38]:

# Restrictive_Filesystem,https://onlinejudge.u-aizu.ac.jp/#/problems/2152
# 右,奥

# 内容の同じ各区間の左端の座標とサイズを保存します。中身のない区間は-1としています。
# 書き込みの際は中身のない区間を順に調べます。
# データ消去の際には各区間をすべて参照します。
# データ参照の際には二分法で当該区間を調べます。

def Bin_s(S,a,b):
    l = 0
    r = len(S)
    while l + 1 < r:
        m = (l+r)//2
        if b < S[m][0]:
            r = m
        elif a > S[m][1]:
            l = m
        else:
            l = m
            break
    return S[l][2]
while True:
    n = int(input())
    if n == 0:break
    I = [[0,10**9+1,-1]]
    for i in range(n):
        a = list(input().strip().split(" "))
        if a[0] == "W":
            p,q = int(a[1]),int(a[2])
            for i in range(len(I)):
                if I[i][2] == -1:
                    I[i][2] = p
                    if I[i][1] <= q:
                        q -= I[i][1]
                    else:
                        r = [I[i][0]+q,I[i][1]-q,-1]
                        I[i][1] = q
                        I = I[:i+1]+[r]+I[i+1:]
                        q = 0
                if q <= 0:break
        elif a[0] == "D":
            b = int(a[1])
            for i in range(len(I)):
                if I[i][2] == b:
                    I[i][2] = -1
        else:
            b = int(a[1])
            print(Bin_s(I,b,b))
    print()