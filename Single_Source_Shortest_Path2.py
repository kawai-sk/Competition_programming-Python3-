# coding: utf-8

# 単一始点最短経路（負）,https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
# 右、奥

# ある点までの距離が更新されるたびにその点を改めて考え直すようにするだけの愚直解法です。
# D[S]<0になったとしたらSを含む負の閉路が存在することがわかります。
# また,i >= E*V > 0 の場合にはBellman-Ford法と同様の考えから負の閉路の存在がわかります。

def solve():
    V,E,S = map(int,input().strip().split(" "))
    L = [{} for _ in range(V)]
    for _ in range(E):
        s,t,d = map(int,input().strip().split(" "))
        L[s][t] = d
    D = ["INF" for _ in range(V)]
    D[S] = 0
    K,i,k = [S],0,1
    while i < k and i < E*V:
        if D[S] < 0:
            break
        p = K[i]
        for j in L[p]:
            if D[j] == "INF" or D[j] > D[p]+L[p][j]:
                D[j] = D[p]+L[p][j]
                K.append(j)
                k += 1
        i += 1
    if i >= E*V > 0 or D[S] < 0:
        print("NEGATIVE CYCLE")
    else:
        for i in range(V):
            print(D[i])
solve()
