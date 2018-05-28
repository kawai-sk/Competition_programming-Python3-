
# coding: utf-8

# In[7]:

# Round-Robin_Scheduling,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_3_B
# 右、奥

# 素直に順次計算するだけです。

m,q = map(int,input().strip().split(" "))
p = []
for i in range(m):
    n,t = input().strip().split(" ")
    p.append([n,int(t)])
T = 0
while p != []:
    n,t = p.pop(0)
    if t > q:
        T += q
        p.append([n,t-q])
    else:
        T += t
        print(n+" "+str(T))