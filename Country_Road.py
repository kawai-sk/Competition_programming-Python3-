# Country Road, http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2104
# 右、奥
# 概ね配布資料の指示通りにアルゴリズムを組みました。
# 家と家の間は n-1(=len(y)) 個。そのうち発電機の配置により省略できるのは k-1 個となります

t = int(input())
for i in range(0,t):
    n,k = map(int,input().strip().split(" "))
    x = list(map(int,input().strip().split(" ")))
    y = [x[i+1]-x[i] for i in range(0,n-1)]
    y.sort()
    l = 0
    for i in range(0,len(y)-k+1):
        l = l + y[i]
    print(l)

