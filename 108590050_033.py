'''
費氏數列 Fibonacci number

請用遞迴撰寫。
輸入一個整數n，輸出 Fibonacci number。

F(1) = 1 ; F(2) = 1;
F( n ) = F(n-1) + F(n-2) ;n > 2

輸入說明：

每一組一個正整數，輸入-1結束所有輸入。
數字代表第幾個數列的數字 1~100

輸出說明：

費氏數列的值。

---------------------

Sample Input:

1
2
5
-1

Sample Output:

1
1
5
'''

def F(n):
    if n==0 or n==1:return n
    else:return F(n-1)+F(n-2)
while True:
    n=int(input())
    if n==-1:break
    elif n>0 and n<101:print(F(n))
