
# coding: utf-8

# In[2]:


N = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        N.append(n)
M = max(N)
A = [1 for i in range(M+1)]
for i in range(2,M+1):
    if i == 2:
        A[i] = A[i-1]+A[i-2]
    elif i >= 3:
        A[i] = A[i-1]+A[i-2]+A[i-3]
for i in range(len(N)):
    p = A[N[i]]%3650
    q = (A[N[i]]-p)//3650
    if p > 0:
        print(q+1)
    else:
        print(q)

