# coding: utf-8

# Molecular_Formula,https://onlinejudge.u-aizu.ac.jp/problems/1244
# 右,奥

# 原子記号と原子量を対応づけて計算するだけです。
# 括弧内の分子量は先に計算し,数字がある場合は直前の原子または分子量に乗算し,最後に総和を出力します。
# 2文字以上の分子記号の判定はord関数を用いて行なっています。

def solve():
    def calc(x,t):
        if t:
            Q = []
            while x < len(a):
                if 65 <= ord(a[x]) <= 90:
                    q = a[x]
                    while x+1 < len(a) and 97 <= ord(a[x+1]) <= 122:
                        q += a[x+1]
                        x += 1
                    x += 1
                    if q in m:
                        Q.append(m[q])
                    else:
                        t = 0
                        break
                elif t > 1 and a[x] == ")":
                    x += 1
                    break
                elif a[x] == "(":
                    x,p = calc(x+1,2)
                    if p == "UNKNOWN":
                        t = 0
                        break
                    else:
                        Q.append(p)
                else:
                    q = int(a[x])
                    while x+1 < len(a) and 48 <= ord(a[x+1]) <= 57:
                        q = q*10 + int(a[x+1])
                        x += 1
                    x += 1
                    Q[-1] = Q[-1]*q
            if t:
                return x,sum(Q)
        return len(a),"UNKNOWN"
    m = {}
    while True:
        a = list(input().strip().split(" "))
        if a[0] == "END_OF_FIRST_PART":
            break
        else:
            m[a[0]] = int(a[-1])
    while True:
        a = list(input())
        if a[0] == "0":
            break
        else:
            print(calc(0,1)[1])
solve()
