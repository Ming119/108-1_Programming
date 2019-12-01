'''
輸入兩個英文句子 A, B，兩個英文單字 x, y
將兩個英文句子A, B 串聯成 句子C
將 句子C 其中的 單字x 替換成 單字y，變成 句子D
輸出 句子C, 句子D 長度的加總
把句子D 前三個字以及最後三個字組合成 句子E，把 句子E重複輸出三次。

Input：
This is a book
That is a cat
is
was

Output：
57
ThwcatThwcatThwcat
'''

A = input()
B = input()
x = input()
y = input()

C = A + B

D = C.replace(x, y)

print(len(C + D))
E = D[:3] + D[-3::]
print(E * 3)
