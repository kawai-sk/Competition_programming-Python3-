# coding: utf-8

# トーナメント,https://beta.atcoder.jp/contests/tdpc/tasks/tdpc_tournament
# 右,奥

# まず,人iが人jに勝つ確率をリストQに用意しておきます。
# 次に,第一ラウンドで各人が(この場合は一意に定まる)相手に勝つ確率をリストPに用意しておきます。
# あとはdpです。各人の第i+1ラウンドについて,
#　(そのラウンドで戦う可能性のある相手に勝つ確率)*(その相手が勝ち上がる確率)の総和をとり,
# 最後に本人がそのラウンドまで勝ち上がる確率を掛けます。
# 人jが第iラウンドで戦いうる人kは j//(2**i)==k//(2**i)を満たしますが,
# 細かい調整はs,t,uを用いてごちゃごちゃとやっています。

K = int(input())
p = 2**K
R = [int(input()) for _ in range(p)]
Q = [[0]*p for i in range(p)]
for i in range(p):
    for j in range(p):
        if i < j:
            Q[i][j] = 1/(1+10**((R[j]-R[i])/400))
        elif i > j:
            Q[i][j] = 1 - Q[j][i]
P = [Q[i][i-1] if i%2 else Q[i][i+1] for i in range(p)]
t = 2
for i in range(1,K):
    s = 0
    nex = [0]*p
    for j in range(p):
        if j >= s+2*t:
            s += 2*t
        k = s+t if s+t > j else s
        u = k + t
        while k < u:
            nex[j] += P[k]*Q[j][k]
            k += 1
        nex[j] *= P[j]
    P = nex
    t *= 2
for i in range(p):
    print("%0.9f" % P[i])
