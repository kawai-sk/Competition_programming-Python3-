
# coding: utf-8

# In[11]:


def lc(X,Y):
    x,y = len(X),len(Y)
    c = [0]*(y+1)
    for j in range(x):
        d = c[:]
        e = X[j]
        for k in range(y):
            if e == Y[k]:
                c[k+1] = d[k]+1
            elif c[k+1] < c[k]:
                c[k+1] = c[k]
    return c[-1]
q = int(input())
for i in range(q):
    X = str(input())
    Y = str(input())
    print(lc(X,Y))