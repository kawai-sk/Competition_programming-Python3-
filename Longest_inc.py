
# coding: utf-8

# In[10]:

# 最長増加部分列、https://onlinejudge.u-aizu.ac.jp/#/problems/DPL_1_D
# 右、奥

# 各段階において考えられる項数iの増加部分列について、最小の第i項をAに保存しています。
# A=[-1,0,1,2,4,...]の場合にはinput<=2ならAを更新する余地がありません。この情報をqで表しています。
# 各inputがAのどこに入り得るかは二分探索しています。


n = int(input())
A = [-1]
q = 0
for i in range(n):
    a = int(input())
    if a >= q and A[-1] < a:
        A.append(a)
    elif a >= q:
        p = len(A)-1
        j = min(p,a+1)
        k = q
        while j - k >= 0:
            l = (j+k)//2
            if a < A[l]:
                j = l
            elif a > A[l+1]:
                k = l
            else:
                if A[l] < a < A[l+1]:
                    A[l+1] = a
                break
            if l == (j+k)//2:
                if l <= p and A[l] < a < A[l+1]:
                    A[l+1] = a
                elif l >= 1 and A[l-1] < a < A[l]:
                    A[l] = a
                else:
                    break
        while q <= p and A[q+1]-A[q]==1:
            q += 1
print(len(A)-1)