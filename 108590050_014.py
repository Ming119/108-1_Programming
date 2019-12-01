'''
輸入m, n 兩個整數，請計算等差為2的數列總和、等差為3的乘積，計算方式如下
1. m ~ n 之間 等差為2的和
m + (m+2) + (m+4) + (m+6) + ... + n
2. m ~ n 之間 等差為3的積
m * (m+3) * (m+6) * (m+9) * ... * n

Sample Input
2
10

Sample Output
30
80
'''

def sum_sq(m, n):
    tmp = m
    for i in range(m,n,2):
        t = (i+2)
        if t <= n:
            tmp += (i+2)
    return tmp

def prod_sq(m,n):
     tmp = m
    for i in range(m,n,3):
        t = (i+3)
        if t <= n:
            tmp *= (i+3)
    return tmp

m = int(input())
n = int(input())

print(sum_sq(m,n))
print(prod_sq(m,n))
