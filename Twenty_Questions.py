
# coding: utf-8

# In[34]:


def qu(s,A):
    n = len(s)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        T = [[i,0] for i in A]
        t = len(T)
        for i in range(t):
            for j in s:
                T[i][1] += int(j[T[i][0]])
        T.sort(key=lambda e:abs(n-2*e[1]))
        while len(T) > 0 and len(A) > 0 and abs(n-2*T[-1][1]) == n:
            A.discard(T[-1][0])
            T.pop(-1)
        if T == [] or A == []:
            return 0
        else:
            U = [T[0][0]]
            for i in range(len(T)):
                if abs(len(A)-2*T[i][1]) == abs(len(A)-2*T[0][1]):
                    U.append(T[i][0])
            B = [qa(s,A,i) for i in U]
            print(T,A)
            C = [qu(i[0],i[2])+qu(i[1],i[2]) for i in B]
            return min(C)
def qa(s,A,i):
    P = set([p for p in A if p != i])
    u,v = [],[]
    for j in range(len(s)):
        if int(s[j][i]) == 0:
            u.append(s[j])
        else:
            v.append(s[j])
    return [u,v,P]
while True:
    m,n = map(int,input().strip().split(" "))
    if n == 0:break
    s = []
    for i in range(n):
        s.append(str(input()))
    A = set([i for i in range(m)])
    print(qu(s,A))