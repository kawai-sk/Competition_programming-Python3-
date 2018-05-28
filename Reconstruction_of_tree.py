
# coding: utf-8

# In[14]:

# Reconstruction_of_tree,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_7_D
# 右、奥

# ある部分木がpreorderではALR,inorderではL'AR'となること,およびLとL',RとR'の長さが等しいことから,再帰的に
# postorderでのL"R"Aを求めています。


def post(a,b):
    if a == []:
        return []
    else:
        p = a[0]
        i = b.index(p)
        x,k = b[:i],b[i+1:]
        y,l = a[1:len(x)+1],a[len(x)+1:]
        return post(y,x)+post(l,k)+[p]
n = int(input())
a = list(map(int,input().strip().split(" ")))
b = list(map(int,input().strip().split(" ")))
c = post(a,b)
s = str(c[0])
for i in range(1,n):
    s += " " + str(c[i])
print(s)

