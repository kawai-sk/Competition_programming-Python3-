
# coding: utf-8

# In[54]:

# Eleven Lover,https://onlinejudge.u-aizu.ac.jp/#/problems/2182
# 右、奥

# 高位の方からi番目の数で終わる数列で,mod 11がjになるものの数をa[j]としています。
# N[i]一文字の数列もまたa[N[i]]に数えますが、0で始まる数列は考慮から外します。
# 各jに対し、a[j]は、i+1番目に終わる数列で,j' mod 11が10*j+N[i+1]のmod 11と一致するものに対応します。
# ここでj'≡10*j+N[i+1]mod 11はN[i+1]-j'≡j mod 11と同値です。


while True:
    N = str(input())
    if N == "0":
        break
    a,p = [0]*11,0
    for i in range(0,len(N)):
        d = int(N[i])
        a = [a[(d-j)%11] for j in range(11)]
        if d != 0:
            a[d] += 1
        p += a[0]
    print(p)