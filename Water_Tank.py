
# coding: utf-8

# In[13]:

# Water Tank,http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1133&lang=jp
# 右、奥

# 区切り板で区切られている部分それぞれについて、
# [[両端の区切り板の位置],[区切り板の高さ],その区間にある蛇口の水量,その区間の水の高さ]
# という情報をまとめたlistをsとします。高さを測定する時間を早い順にsortしておきます。

# 測定する時間までに蛇口から流れた水量を高さに加え、
# 区間両端の区切り板のうち、低い方よりも水が高いかどうかで分岐します。
# 低い方の区切り板の高さをp、その区切り板を共有する隣の区間のもう一つの区切り板の高さをqとします。
# pを越える分の水が隣に流れ込んだと仮定し、そのとき隣の区間について、
# (1)水の高さがpとqのどちらよりも低ければ、水をそのまま流して次の区間へ。
# (2)p>qなら、隣の区間に移って改めて水の高さを考察する。
# (3)この場合が最も重要なのですが、p<=q であり、かつ隣の区間でも水がpより高くなる場合。
# このとき、今考えている区間と隣の区間を一つの区間と見做し、s内の情報を更新・削除して、水の高さの平均をとります。

# 以上の過程を水が溢れるまで繰り返します。
# 水がいつ溢れるかの判定は先に済ませておき、その時刻以降の測定値には50を入れておきます。

D = int(input())
for i in range(D):
    N = int(input())
    BH = []
    for i in range(N):
        BH.append(list(map(int,input().strip().split(" "))))
    M = int(input())
    FA = []
    for i in range(M):
        FA.append(list(map(int,input().strip().split(" "))))
    L = int(input())
    PT = [[0,0,0]]
    for i in range(L):
        PT.append(list(map(int,input().strip().split(" ")))+[i])
    PT.sort(key=lambda e:e[1])
    s = [[[0,BH[0][0]],[50,BH[0][1]],0,0]]
    for i in range(N-1):
        s.append([[BH[i][0],BH[i+1][0]],[BH[i][1],BH[i+1][1]],0,0])
    s.append([[BH[N-1][0],100],[BH[N-1][1],50],0,0])
    i = 0
    j = 0
    while i < N+1 and j < M :
        if s[i][0][0] < FA[j][0] < s[i][0][1]:
            s[i][2] += FA[j][1]
            j += 1
        else:
            i += 1
    m = 0
    for i in range(M):
        m += FA[i][1]
    h = [0 for i in range(0,L)]
    t = L+1
    for i in range(1,L+1):
        if m*PT[i][1] >= 50*30*100 and t == L:
            t = i
            h[PT[i][2]] = 50
        elif i > t:
            h[PT[i][2]] = 50
    i = 1
    while i < t:
        if PT[i][1]-PT[i-1][1]!=0:
            for j in range(len(s)):
                if s[j][2] != 0:
                    s[j][3] += s[j][2]*(PT[i][1]-PT[i-1][1])/(30*(s[j][0][1]-s[j][0][0]))
            j = 0
            while 0 <= j < len(s):
                if s[j][1][0] == s[j][1][1]:
                    if s[j][3] > 50:
                        s[j][3] = 50
                    j += 1
                else:
                    k,l = 0,-1
                    if s[j][1][0] > s[j][1][1]:
                        k,l = 1,1
                    p = s[j+l][1][1-k]
                    q = s[j+l][1][k]
                    if s[j][3] <= p:
                        j += 1
                    else:
                        r = (s[j][3]-p)*(s[j][0][1]-s[j][0][0])
                        if s[j+l][3] + r/(s[j+l][0][1]-s[j+l][0][0]) <= min(p,q):
                            s[j+l][3] += r/(s[j+l][0][1]-s[j+l][0][0])
                            s[j][3] = p
                            j += 1
                        elif p > q:
                            s[j+l][3] += r/(s[j+l][0][1]-s[j+l][0][0])
                            s[j][3] = p
                            j += l
                        else:
                            r = s[j][3]*(s[j][0][1]-s[j][0][0])+s[j+l][3]*(s[j+l][0][1]-s[j+l][0][0])
                            s[j][2] += s[j+l][2]
                            if l > 0:
                                s[j][0][1] = s[j+l][0][1]
                                s[j][1][1] = s[j+l][1][1]
                            else:
                                s[j][0][0] = s[j+l][0][0]
                                s[j][1][0] = s[j+l][1][0]
                            s[j][3] = r/(s[j][0][1]-s[j][0][0])
                            s.pop(j+l)
                            j += l - k
        for j in range(len(s)):
            if s[j][0][0] < PT[i][0] < s[j][0][1]:
                h[PT[i][2]] = min(s[j][3],50)
        i += 1
    for i in range(L):
        print(h[i])