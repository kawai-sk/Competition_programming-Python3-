
# coding: utf-8

# In[25]:


N,m = map(int,input().strip().split(" "))
C = []
for i in range(m):
    C.append(list(map(int,input().strip().split(" "))))
for i in range(m):
    if C[i][0] > C[i][1]:
        C[i][1] = C[i][0]
C.sort(key=lambda e:e[0])
C.append([N+1,N+1])
i,l,p = 0,0,0
while p < N+1:
    a,b = C[i][0],C[i][1]
    while i < m-1 and C[i+1][0] <= b:
        if C[i+1][0] < a:
            a = C[i+1][0]
        if b < C[i+1][1]:
            b = C[i+1][1]
        i += 1
    if a != N+1:
        l += 2*b-p-a
        p = a
        i += 1
    else:
        l += a-p
        p = a
print(l)