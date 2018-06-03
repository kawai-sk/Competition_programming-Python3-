# coding: utf-8

# True Liars,https://onlinejudge.u-aizu.ac.jp/#/problems/1238
# 右、奥
# このコード(https://onlinejudge.u-aizu.ac.jp/#/solutions/problem/1238/review/1148471/u_shiki/Python3)
# を参考に解きました。

# まず入力された情報を反映した木構造を作ります。
# p=p1+p2として,iは「人iは正直者である」,i+pは「人iは嘘つきである」を表すことにします。
# 「aがbを正直者と言った」とき,aが正直者ならbも正直者,aが嘘つきならbも嘘つきなので,
# (a,b)と(a+p,b+p)をグループ化すればよいことになります。
# 「aがbを嘘つきと言った」ときは(a,b+p)と(a+p,b)をグループ化すればよいわけです。

# こうして作られた各グループについて,正直者と嘘つきの組合せはただ二通りです。
# つまり,グループ中のある人物が正直者か否かが定まれば,他の人物についても一意に定まります。
# ここで,ある人物aが正直者のとき,グループ内の正直者と嘘つきはk,l人であるとすると,
# 人物aが嘘つきなら,グループ内の正直者と嘘つきはl,k人であることになります。
# よって,このグループ内のmin(k,l)人は少なくとも正直者であり,
# 残りの|k-l|人が正直者かどうかで二通りの組合せが考えられるわけです。
# このとき,k=lなら,同じ人数の正直者として複数通りの組合せが考えられるので,
# 一意性が成立しないことは明らかです。
# 各グループが k!=l を満たす場合について,残りの(rest=)p1 - sum(min(k,l)) 人の正直者を
# いかに特定するかが問題になります。

# ここからは動的計画法の出番です。
# 上で分類した各グループの代表元をrootsにまとめ,len(roots)*restのdpを考えます。
# ここで,dp[i][j]の値は,
# roots[0]からroots[i]までのグループでj人の正直者を表現できるかどうか
# を示しています。
# dp[i][j]=0なら,そのような表現は存在しません。
# dp[i][j]=3ならそのような表現が複数通り存在します。
# dp[i][j]=1,2ならそのような表現が一意に存在しますが,
# そのときグループi内の正直者と嘘つきの組合せとして考えられる二通りについて,
# どちらが適当であるかによってdp[i][j]が1か2かが決まっています。
# 正直者の人数がmin(k,l)ならdp[i][j]=1,max(k,l)ならdp[i][j]=2です。
# 現時点で考えているrestの値は全グループについてmin(k,l)を選んだ場合のものなので,
# あるグループについてmax(k,l)を選ぶ場合にはrestの値を取り直す必要があります。
# その必要性をdp[i][j]=2という情報が示しているわけです。

# ともあれ,最終的に各iについてdp[i][rest]=1,2であるなら,それに応じた正直者を出力します。
# ただし上述のように,このrestの値は場合に応じて更新していく必要があります。
# 一度でもdp[i][rest]=0,3だったならnoを出力します。

from collections import defaultdict
def root(x):
    r = []
    while tree[x] != x:
        r.append(x)
        x = tree[x]
    for u in r:
        tree[u] = x
    return x
def unite(x,y):
    a,b = root(x),root(y)
    if a != b:
        c,d = rank[a],rank[b]
        if c < d:
            tree[a] = b
        else:
            tree[b] = a
            if c == d:
                rank[a] += 1
while True:
    N,p1,p2 = map(int,input().strip().split(" "))
    if N == p1 == p2 == 0:break
    p = p1 + p2
    tree = [i for i in range(2*p+1)]
    branch = defaultdict(list)
    rank = [0] + [1]*2*p
    for _ in range(N):
        a,b,c = input().strip().split(" ")
        x,y = int(a),int(b)
        z,w = x+p,y+p
        if c == "no":
            y,w = w,y
        unite(x,y)
        unite(z,w)
    for i in range(1,p+1):
        branch[root(i)].append(i)
    roots = []
    slide = []
    diffs = []
    rest = p1
    for i in range(1,p+1):
        if i in branch:
            mem,dev = len(branch[i]),len(branch[i+p])
            if mem == dev:
                rest = -1
                break
            elif mem < dev:
                dif = dev-mem
                rest -= mem
                slide.append(0)
            else:
                dif = mem-dev
                rest -= dev
                slide.append(1)
            roots.append(i)
            diffs.append(dif)
    if rest < 0:
        print("no")
    else:
        dp = [[1]+[0]*rest for i in range(len(roots)+1)]
        for i in reversed(range(len(roots))):
            k = diffs[i]
            for j in range(1,rest+1):
                if j < k:
                    if dp[i+1][j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if dp[i+1][j] and dp[i+1][j-k]:
                        dp[i][j] = 3
                    elif dp[i+1][j-k]:
                        dp[i][j] = 2
                    elif dp[i+1][j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
        divine = []
        un = True
        for i in range(len(roots)):
            if dp[i][rest] == 1:
                divine += branch[roots[i] + p*slide[i]]
            elif dp[i][rest] == 2:
                divine += branch[roots[i] + p*(1-slide[i])]
                rest -= diffs[i]
            else:
                print("no")
                un = False
                break
        if un:
            divine.sort()
            for i in divine:
                print(i)
            print("end")
