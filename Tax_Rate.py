
# coding: utf-8

# In[ ]:


while True:
    a,b,c = map(int,input().strip().split(" "))
    if a == b == c == 0:
        break
    m = 0
    for i in range(1,c):
        for j in range(1,c):
            s = i*(100+a)//100 + j*(100+a)//100
            if s == c:
                t = i*(100+b)//100 + j*(100+b)//100
                if t > m:
                    m = t
            elif s > c:
                break
    print(m)