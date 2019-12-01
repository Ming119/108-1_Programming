'''
021.
迴圈偶數連加，輸入兩整數a、b，且a 例如輸入 a=1、b=100，則輸出結果為 2550(2+4+6+8+ ... +100 =2550)
simple input:
1
100

simple output:
2550
'''

a = int(input())
b = int(input())

def Sum(a,b):
    if (a%2)!=0:
        a += 1
    tmp = a
    for i in range(a,b+1,2):
        tmp += i
    tmp -= a
    return tmp

ans = Sum(a,b)
print(ans)
