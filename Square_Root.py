while True:
    N,M = map(int,input().strip().split(" "))
    if N == M == 0:
        break
    h = []
    w = []
    s1,s2 = 0,0
    for i in range(N):
        h.append(int(input()))
        s1 = s1+h[i]
    for i in range(M):
        w.append(int(input()))
        s2 = s2+w[i]
    S = min(s1,s2)
    a = [[0,0] for i in range(0,S+1)]
    for i in range(M):
        r = 0
        j = 0
        while i+j<M:
            r = r + w[i+j]
            if r > S:
                break
            a[r][0] = a[r][0]+1
            j = j+1
    t = []
    for i in range(N):
        r = 0
        j = 0
        while i+j<N:
            r = r + h[i+j]
            if r > S:
                break
            a[r][1] = a[r][1]+1
            if a[r][0] != 0 and a[r][1] == 1:
                t.append(r)
            j = j + 1
    s = 0
    for i in range(len(t)):
        s = s + a[t[i]][0]*a[t[i]][1]
    print(s)