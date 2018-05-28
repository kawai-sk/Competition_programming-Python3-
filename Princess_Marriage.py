
# coding: utf-8

# In[3]:


while True:
    N,M = map(int,input().strip().split(" "))
    if N == M == 0:
        break
    DP = []
    for i in range(N):
        DP.append(list(map(int,input().strip().split(" "))))
    DP.sort(key=lambda e:e[1],reverse=True)
    i = 0
    while M > 0 and i < N :
        if DP[i][0] < M:
            M = M - DP[i][0]
            DP[i][0] = 0
            i = i + 1
        else:
            DP[i][0] = DP[i][0] - M
            M = 0
    s = 0
    for i in range(N):
        s = s + DP[i][0]*DP[i][1]
    print(s)