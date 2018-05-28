
# coding: utf-8

# In[15]:

# Inversion Count,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_5_D
# 右、奥

# 概ね教材のとおりです。merge中でのc(ount)の増加量は,a[p],a[p+1],...,a[x-1]のすべてがb[q]より大きく,
# これらすべての元の数列における添字はb[q]より小さいことから考えています。

def merge(a,b,c):
    x,y = len(a),len(b)
    if x == 0:
        return b
    elif y == 0:
        return c
    else:
        I = [0 for i in range(x+y)]
        p,q = 0,0
        for i in range(x+y):
            if p >= x:
                I[i] = b[q]
                q += 1
            elif q >= y:
                I[i] = a[p]
                p += 1
            elif a[p] > b[q]:
                c += x - p
                I[i] = b[q]
                q += 1
            else:
                I[i] = a[p]
                p += 1
        return I,c    
def mergesort(a,c):
    n = len(a)
    if n == 1:
        return a,c
    else:
        x,c = mergesort(a[:n//2],c)
        y,c = mergesort(a[n//2:],c)
        return merge(x,y,c)
n = int(input())
a = list(map(int,input().strip().split(" ")))
print(mergesort(a,0)[1])