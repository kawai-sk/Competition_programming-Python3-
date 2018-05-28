
# coding: utf-8

# In[17]:


N,K,T,U,V,L = map(int,input().strip().split(" "))
D = []
for i in range(N):
    D.append(int(input()))
x = 0
k = 0
n = 0
t = 0
while x < L:
    if k == 0 and n < N:
        t = t + (D[n]-x)/U
        x = D[n]
        n = n + 1
        k = k + 1
    elif k == 0 and n == N:
        t = t + (L-x)/U
        x = L
    elif k > 0 and x + V*T <L:
        k = k - 1
        if n+(K-k) < N and x + V*T >= D[n+(K-k)]:
            t = t + (D[n+(K-k)]-x)/V
            x = D[n+(K-k)]
            n = n + (K-k) + 1
            k = K + 1
        else:
            t = t + T
            x = x + V*T
            while n < N and x >= D[n]:
                if k < K:
                    k = k + 1
                    n = n + 1
    elif k > 0 and x + V*T >= L:
        t = t + (L-x)/V
        x = L
print(t)


# In[ ]:


1 1 1 2 3 100
50
3 1 1 2 3 100
49
50
51


# In[11]:


49/2+2/3+1+1+(100-57)/2


# In[ ]:


49+2+3+3


# In[13]:


a = [1,2,3]
i = 4
i >= 4 and a[i]==1

