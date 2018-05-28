
# coding: utf-8

# In[46]:
# Dinner,http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2642
# 右、奥

# 以下の発想は次のサイトを参考にしています:http://mayokoex.hatenablog.com/entry/2016/04/11/212554

# 自炊する日数ごとに考えうる幸福度を求め、その中の最大値を求めています
# 全日食堂を基本とします。全体でi-1日間自炊している状態から新たにj日目も自炊にした場合、
# 外食をやめたことで幸福度がC[j]下がり、自炊したことで幸福度がP*(Q-j+2*i)上がります。
# P*(Q-j)-C[j]が最も大きい日に順に自炊していくのが最善と考えました。

# 以前提出した未完成のコードとsampleは消すのを忘れていただけなので無視してください。
# すでに目を通されてしまっていたら申し訳ないです。

N,P,Q = map(int,input().strip().split(" "))
C = []
for i in range(0,N):
    C.append(int(input()))
D = [P*(Q-i) - C[i] for i in range(0,N)]
D.sort(reverse = True)
s = 0
for i in range(0,N):
    s += C[i]
m = s
for i in range(0,N):
    s = s + 2*P*i +D[i]
    if s > m:
        m = s
print(m)