'''
計算最大公因數 GCD
給予三個整數，請計算出三個整數的最大公因數。

輸入說明:
一行三個整數以空格隔開，直到-1結束

輸出說明:
輸出三個整數的最大公因數。

Sample Input
18 9 6
21 42 63
-1

Sample Output
3
21
'''

def gcd(n1, n2):return n1 if n2==0 else gcd(n2,n1%n2)
while True:
    n=list(map(int,input().split(' ')))
    if n[0]==-1:break
    print(gcd(gcd(n[0],n[1]),n[2]))
