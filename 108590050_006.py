'''
英文字分析、取代、插入、刪除

輸入一篇英文文章 ，文章中單字與單字之間以一個空白間隔。另外輸入兩個單字(word) P、Q。
P為文章中所出現的單字，Q為取代或加入的單字
(1) 在文章中把 P 字串以 Q 字串取代，並輸出。
(2) 在文章中把P 字串前插入 Q 字串，並輸出。
(3) 在文章中把P 字串刪除，並輸出。

輸入範例說明:
第一行，文章
第二行，英文字 P
第三行，英文字 Q

輸出範例說明:
第一行，將文章中的 P 替換成 Q。
第二行，將Q 插入文章中的P 前面。
第三行，將文章中P單字刪除後印出


Sample Input

This is a book That is a cook
is
was

Sample Output

This was a book That was a cook
This was is a book That was is a cook
This a book That a cook
'''

pp = input()
P = input()
Q = input()

PP = pp.split(" ")
while (P in PP):
    PP[PP.index(P)] = Q
L1 = " ".join(PP)
print(L1)

PP = pp.split(" ")
while (P in PP):
    PP[PP.index(P)] = (Q + " " + P)
L2 = " ".join(PP)
print(L2)

PP = pp.split(" ")
while (P in PP):
    PP.remove(P)
L3 = " ".join(PP)
print(L3)
