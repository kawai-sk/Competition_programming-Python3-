
# coding: utf-8

# In[11]:


N,W = map(int,input().strip().split(" "))
V = [0]*(W+1)
for i in range(N):
    v,w = map(int,input().strip().split(" "))
    for j in range(w,W+1):
        V[j] = max(V[j],V[j-w]+v)
print(V[-1])


# In[ ]:


入力例 1
4 8
4 2
5 2
2 1
8 3
出力例 1
21

入力例 2
2 20
5 9
4 10
出力例 2
10
入力例 3
3 9
2 1
3 1
5 2
出力例 3
27

