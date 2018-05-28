
# coding: utf-8

# In[1]:


def adjusted_ave(A):
    t = len(A)
    Max = A[0]
    Min = A[0]
    s = A[0]
    for i in range(1,t):
        s = s + A[i]
        if A[i] > Max:
            Max = A[i]
        if A[i] < Min:
            Min = A[i]
    return (s - Max - Min)//(t-2)
while True:
    N = int(input())
    if N == 0:
        break
    S = []
    for i in range(N):
        S.append(int(input()))
    print(adjusted_ave(S))