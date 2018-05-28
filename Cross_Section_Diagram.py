
# coding: utf-8

# In[14]:

# Areas_on_the_Cross-Section_Diagram,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_3_D
# 右、奥

# 地形を順次処理し,\ならその座標を保存,/の場合に対応する\が存在するなら面積を計算します。
# 水たまりの両端の座標と面積を別のリストに保存し,共通部分があるものは統合します。


s = list(input())
q = []
x = 0
L = []
for i in range(len(s)):
    x += 1
    if s[i] == "\\":
        q.append(x)
    elif s[i] == "/" and len(q) > 0:
        y = q.pop(-1)
        if L == []:
            L.append([y,x,x-y])
        else:
            L.append([y,x,x-y])
            while len(L) >= 2:
                if L[-2][1]+1 > L[-1][0]:
                    a,b,c = L.pop(-1)
                    k,l,m = L[-1]
                    L[-1] = [min(k,a),max(l,b),c+m]
                else:
                    break
S = 0
l = str(len(L))
for i in range(len(L)):
    S += L[i][2]
    l += " " + str(L[i][2])
print(str(S))
print(l)