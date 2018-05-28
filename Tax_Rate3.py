# 税率変更　http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1192&lang=jp
# 右、奥

# iとjが条件を満たすとします。つまり小数点以下を考慮して
# i*(100+a)//100+j*(100+a)//100 = c
# となるとします。一方、切り捨ての定義から
# i*(100+a)/100 -1 < i*(100+a)//100 <= i*(100+a)/100
# で、jについても同様なので
# (i+j)*(100+a)/100 -2 < c <= (i+j)*(100+a)/100
# となることが必要条件です。全探索のためにiは 1 <= i <= c-1 と動かしますが、
# 上の条件を変形して、jは
# 100*c <= (i+j)*(100+a) < 100*(c+2)
# 満たすものだけ考慮すれば充分です。このようなjを求めるのには二分探索を用いました。

while True:
    a,b,c = map(int,input().strip().split(" "))
    if a == b == c == 0:
        break
    m = 0
    def binary(i):
        l,r=1,c-1
        j=(l+r)//2
        t=[]
        if 100*c<= (i+1)*(100+a) < 100*(c+2):
            t.append(1)
        elif 100*c<= (i+c-1)*(100+a) < 100*(c+2):
            t.append(c-1)
        else:
            while True:
                if (i+j)*(100+a) >= 100*(c+2):
                    r = j
                elif 100*c > (i+j)*(100+a):
                    l = j
                else:
                    t.append(j)
                    break
                if j==(l+r)//2:
                    break
                j=(l+r)//2
        if t !=[]:
            p,q=j-1,j+1
            while 100*c <= (i+p)*(100+a) < 100*(c+2) and p>=0:
                t.append(p)
                p = p-1
            while 100*c <= (i+q)*(100+a) < 100*(c+2) and q<=c-1:
                t.append(q)
                q = q+1
        return t
    i = 1
    while (i+1)*(100+a) < 100*(c+2) and i<=c-1:
        r=binary(i)
        for j in r:
            if i*(100+a)//100 + j*(100+a)//100 == c:
                    t = i*(100+b)//100 + j*(100+b)//100
                    if t > m:
                        m = t
        i=i+1 
    print(m)
