
# coding: utf-8

# In[ ]:


while True:
    a,b,c = map(int,input().strip().split(" "))
    if a == b == c == 0:
        break
    m = 0
    i = 1
    while (i+1)*(100+a) < 100*(c+2):
        j=1 
        while (i+j)*(100+a) < 100*(c+2):
            if 100*c <= (i+j)*(100+a):
                if i*(100+a)//100 + j*(100+a)//100 == c:
                    t = i*(100+b)//100 + j*(100+b)//100
                    if t > m:
                        m = t
            j=j+1
        i=i+1 
    print(m)