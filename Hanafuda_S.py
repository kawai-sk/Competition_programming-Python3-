
# coding: utf-8

# In[11]:


while True:
    n,r = map(int,input().strip().split(" "))
    if n == r == 0:
        break
    a = [n - i for i in range(0,n)]
    for i in range(0,r):
        p,c = map(int,input().strip().split(" "))
        x = []
        y = []
        z = []
        for i in range(0,n):
            if i <= p - 2:
                x.append(a[i])
            elif p - 1 <= i <= p + c - 2:
                y.append(a[i])
            else:
                z.append(a[i])
        a = y + x + z
    print(a[0])


# In[12]:


while True:
    n,r = map(int,input().strip().split(" "))
    if n == r == 0:
        break
    a = [n - i for i in range(0,n)]
    for i in range(0,r):
        p,c = map(int,input().strip().split(" "))
        b = a[:p-1]
        d = a[p-1:p+c-1]
        if p + c != n + 1:
            a = d + b + a[p+c-1:]
        else:
            a = d + b
    print(a[0])

