
# coding: utf-8

# In[56]:


n = int(input())
for i in range(0,n):
    a = list(map(int,input().strip().split(" ")))
    c = input().strip().split(" ")
    r,g,b = [],[],[]
    for j in range(0,9):
        if c[j] == "R":
            r.append(a[j])
        elif c[j] == "G":
            g.append(a[j])
        else:
            b.append(a[j])
    if not(len(r)%3 == len(g)%3 == len(b)%3 == 0):
        print(0)
    else:
        def judge(p):
            p.sort()
            k = 0
            while k <= len(p)-3:
                if p[k] == p[k+1] == p[k+2]:
                    del p[k:k+3]
                else:
                    k = k + 1
            k = 0
            while k <= len(p)-3:
                if p[k]+1 in p and p[k]+2 in p:
                    p.remove(p[k]+1)
                    p.remove(p[k]+2)
                    p.pop(k)
                else:
                    k = k + 1
            if p == []:
                return 1
            else:
                return 0
        print(judge(r)*judge(g)*judge(b))

