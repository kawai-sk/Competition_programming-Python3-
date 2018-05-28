
# coding: utf-8

# In[123]:

# ほそながいところ,http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2427&lang=jp
# 右、奥

# 横軸を距離x,縦軸を時間tとする平面グラフ上の問題と等価と見做すことができます。
# つまり,j番目の馬車の出発時刻をT_jとすれば,その進行過程は直線l_j:t=x*S_j+T_jとなります。
# T_1<T_2<...<T_nであり,各直線l_jが交点を持つとすればそれはx=D_iあるいはx=dist上となるような
# T_1,...,T_nを考えればよいことになります。

# T_1=0は確定です。以後,j番目の馬車についてはひとまずT_j=T_(j-1)+1とします。
# 相異なる二直線l_j,l_kは,S_j=S_kなら交わらず,そうでなければその交点は
# t=x*S_j+T_j=x*S_k+T_k より y=(T[j]-T[k])/(S[k]-S[j]) となります。
# この点がy<0 または y>=dist または D=[D_1,...,D_m]に含まれるならばそれでよいのですが、
# そうでないような 1<=k<=j-1が一つでも存在するならばT_jを取り直す必要があります。

# つまり,D_b上で他の直線と交わるようなT_jを考えます。その点ですでに他二つの直線が交わっているならb+=1とします。
# T_jを改めてもまた上の条件を満たさないならb+=1とします。
# b>mとなってしまったら,仕方ないのでdistで他の直線と交わるようにして次に進みます。

# 以上の考えで基本的な問題は解けるのですが,AOJに提出したところ例外が見つかりました。

# たとえばS_1=4,S_2=4,S_3=2,dist=100,D_1=D_m=50の場合。
# T_1=0,T_2=1とすると,l_3がD_1でl_2と交わるようにしても,l_1とはD_1<x<distの範囲で交わってしまいます。
# l_3がdistでl_1と交わり,D_1でl_2と交わるようにするためには,T_2=100>1とする必要があります。
# つまり,T_j=T_(j-1)+1と安直に決定するよりも適切な位置を選ばなければならないcaseがあるのです。
# その点について考慮したのが,「if j >= 2 and len(A) >= 2」の分岐です。
# Aにはl_jとよくない場所で交わってしまうようなl_kのkが含まれています。
# そのなかでk=0またはT_k=T_(k-1)+1を満たすものをBとして,len(B)>=2ならT_kを考え直します。
# 詳述は言語化が面倒なので避けますが,要は考えうるすべての組合せから最良のものを探している,ということです。

# 厳密にはlen(B)>=4の場合もプログラムに組み込む必要がありますが,
# AOJのtest caseにはその場合のものがなかったのと,面倒なので省いています。


d = int(input())
n = int(input())
S = []
for i in range(n):
    S.append(int(input()))
m = int(input())
D = []
for i in range(m):
    D.append(int(input()))
D.sort()
D.append(d)
T = [0]
j = 1
t = T[0]+d*S[0]
while j < n:
    T.append(T[j-1]+1)
    b = 0
    while True:
        A = []
        for k in range(j):
            if S[k] != S[j]:
                y = (T[j]-T[k])/(S[k]-S[j])
                if 0 < y < d and (not y in D):
                    A.append(k)
        if len(A) == 0 or b == m + 1:
            y = T[j]+d*S[j]
            if y > t:
                t = y
            j += 1
            break
        X = []
        if j >= 2 and len(A) >= 2:
            B = []
            for i in A:
                if i == 0 or T[i]-T[i-1] == 1:
                    B.append(i)
            B.sort()
            if len(B) == 2:
                for l in range(0,m+1):
                    p = T[B[0]] + D[l]*S[B[0]] - D[l]*S[j]
                    for k in range(m+1):
                        if k != l:
                            q = p + D[k]*S[j] - D[k]*S[B[1]]
                            if T[B[0]] < q and q < p :
                                Y = []
                                for i in range(B[1]+1,j):
                                    Y.append(i)
                                TF = True
                                for i in range(B[1]):
                                    if not T[i] < q:
                                        TF = False
                                for i in Y:
                                    if not q < T[i] < p:
                                        TF = False
                                if TF == True:
                                    X.append([q,p])
            elif len(B) == 3:
                for i in range(m+1):
                    p = T[B[0]] + D[i]*S[B[0]] - D[i]*S[j]
                    for k in range(m+1):
                        if i != k:
                            q = p + D[k]*S[j] - D[k]*S[B[2]]
                            if T[B[2]] <= q and q < p:
                                for l in range(m+1):
                                    if l != k and i != l:
                                        r = p + D[k]*S[j] - D[k]*S[B[1]]
                                        if T[B[1]] < r  and r < q and q < p:
                                            Y,Z = [],[]
                                            for i in range(B[1]+1,B[2]):
                                                Y.append(i)
                                            for i in range(B[2]+1,j):
                                                Z.append(i)
                                            TF = True
                                            for i in range(B[0]):
                                                if not T[i] < r:
                                                    TF = False
                                            for i in Y:
                                                for j in Z:
                                                    if not r < T[i] < q < T[j] < p:
                                                        TF = False
                                            if TF == True:
                                                X.append(r,q,p)
        if X != []:
            if len(A) == 2:
                X.sort(key = lambda e:(e[1],e[0]))
                T[B[1]],T[j] = X[0][0],X[0][1]
            elif len(A) == 3:
                X.sort(key = lambda e:(e[2],e[1],e[0]))
                T[B[2]],T[B[1]],T[j] = X[0][0],X[0][1],X[0][2]
        else:
            while b < m + 1:    
                x = [D[b]*S[i]+T[i] for i in range(j)]
                x.sort(reverse = True)
                T[j] = x[0]-D[b]*S[j] 
                b += 1
                if len(x) == 1 or x[0] != x[1]:
                    break
print(t)

