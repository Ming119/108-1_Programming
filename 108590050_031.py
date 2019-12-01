'''
031.

給定一串句子，而後輸入字串數字，
該數字決定這串句子的前後排序，

範例輸入說明:
參考以下Input，每個數字將對應到一個單字，
按照數字的大小，並對應輸入文章，由小到大排序。

範例輸出說明:
輸出改變後的句字順序。


Input:
A B C D E F G
7 6 5 3 1 2 4

Output:
EFDGCBA

Input:
qrqe qwer wrqe eqrw qqrf
5 9 3 2 7
Output:
eqrwwrqeqrqeqqrfqwer
'''

data=input().split(' ')
queue=list(map(int,input().split(' ')))
alist=sorted([queue[i],data[i]]for i in range(len(queue)))
for i in range(len(alist)):print(alist[i][1],end='')
