
# coding: utf-8

# In[25]:

# Reverse_Polish_Notation,https://onlinejudge.u-aizu.ac.jp/#/problems/ALDS1_3_A
# 右、奥

# 文字列を左から順に処理し,数字なら保存,演算記号なら保存した数値を取り出して計算した値を改めて保存しています。


a = list(map(str,input().strip().split(" ")))
p = []
j = 0
while a != []:
    q = a.pop(0)
    if q == "+":
        p.append(p.pop()+p.pop())
    elif q == "-":
        p.append(-p.pop()+p.pop())
    elif q == "*":
        p.append(p.pop()*p.pop())
    else:
        p.append(int(q))
print(p.pop())