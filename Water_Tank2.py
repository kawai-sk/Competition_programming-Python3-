
# coding: utf-8

# In[ ]:

# Water Tank,https://onlinejudge.u-aizu.ac.jp/#/problems/2180
# 右、奥

# 下限の初期値は単位時間あたりの消費水量の最大値、上限の初期値は総消費水量/1日としています。
# 関数okの判定では3日以上経過した場合も考慮するのが正確だと思いますが、今回のテストケースでは
# 「2日経過した時点で水が尽きていなければよい」という条件で充分だったので、そのように判定しています。
# これで時間制限の8secギリギリでした。


def ok(h):
    k = 0
    s = l
    for i in range(2*n):
        if k < p[i]:
            s = min(s+h*(p[i]-k),l)
        s = min(s+(h-r[i])*(q[i]-p[i]),l)
        k = q[i]
        if s <= 0:
            break
        if i == n-1 and s+h*(p[i+1]-q[i]) >= l:
            break
    return s > 0
while True:
    n,l = map(int,input().strip().split(" "))
    if n == l == 0:break
    p,q,r = [0]*2*n,[0]*2*n,[0]*2*n
    s,m = 0,1
    for i in range(n):
        P,Q,R = map(int,input().strip().split(" "))
        p[i],q[i],r[i]=P,Q,R
        p[i+n],q[i+n],r[i+n]=P+86400,Q+86400,R
        s += (Q-P)*R
        m = max(m,R)
    s = s/86400.0
    while m-s > 10**(-7):
        h = (m+s)/2.0
        if ok(h):
            m = h
        else:
            s = h
    print("%0.9f" % round(s,7))