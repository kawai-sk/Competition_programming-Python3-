# coding: utf-8

# 最短路問題,https://beta.atcoder.jp/contests/arc044/tasks/arc044_b
# 右,奥

# 1からの最短距離がiとなるためには,最短距離i-1の点との辺が存在する必要があります。
# 最短距離i,i-1の点がx,pre個なら,この条件を満たす組合せは((2**pre)-1)**x通りです。
# また,最短距離がiの点同士の間にはどれほど辺が繋がっていても問題ありません。
# 最短距離iの点がx個なら,この条件を満たす組合せは2**((x*(x-1))//2)通りです。
# 上記以外の辺が存在する場合は条件を満たしません。

# 一応解説を見ても想定解どおりの解法のはずなのですが,
# 階乗を効率化したり2の階乗を先に用意したりといろいろ工夫してみてもTLEは避けられませんでした。
# なので比較的簡潔なコードをひとまず置いておきます。

p = 10**9+7
N = int(input())
A = list(map(int,input().split(" ")))
ans = 0 if A[0] else 1
if ans:
    A.sort()
    A.append(A[-1]+1)
    n = 1
    x = 0
    pre = 1
    for i in range(1,N+1):
        if ans:
            if A[i] == n:
                x += 1
            elif A[i] == n+1:
                n = A[i]
                ans = (ans*((2**pre)-1)**x)%p
                ans = (ans*(2**((x*(x-1))//2)))%p
                pre,x = x,1
            else:
                ans = 0
print(ans)
