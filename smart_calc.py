# coding: utf-8

# スマート計算機,https://onlinejudge.u-aizu.ac.jp/problems/0109
# 右,奥

# 乗除の優先度は高いのでその場で計算することにします。
# 括弧が存在する場合は,括弧内の計算結果を先に求めることにします。
# 加減は後回しにしてよいので,ひとまず「個々の数値」「加減の記号」「加減以外の計算結果」をQに保存します。
# ）または＝にたどり着いた時点で,Q内の情報をまとめて計算します。

# AOJ内のソースが死んでいるので判定はできませんでしたが,サンプルケースについては合っていました。

def solve():
    def number(x):
        if l[x] == "(":
            return calc(x+1,True)
        else:
            a = int(l[x])
            x += 1
            while x < len(l) and not l[x] in ["+","-","*","/","=","(",")"]:
                a = 10*a+int(l[x])
                x += 1
            return x,a
    def calc(x,t):
        Q = []
        x,a = number(x)
        Q.append(a)
        while x < len(l):
            if l[x] == "+" or l[x] == "-":
                Q.append(l[x])
                x += 1
            elif l[x] == "*":
                p = Q.pop()
                x,a = number(x+1)
                Q.append(p*a)
            elif l[x] == "/":
                p = Q.pop()
                x,a = number(x+1)
                Q.append(p/a)
            elif l[x] == "(":
                x,a = calc(x+1,True)
                Q.append(a)
            elif (t and l[x] == ")") or l[x] == "=":
                x += 1
                break
            else:
                x,a = number(x)
                Q.append(a)
        i = 1
        a = Q[0]
        while i < len(Q):
            b = Q[i]
            if b == "+":
                a += Q[i+1]
            else:
                a -= Q[i+1]
            i += 2
        return x,a
    n = int(input())
    for _ in range(n):
        l = list(input())
        print(calc(0,False)[1])
solve()
