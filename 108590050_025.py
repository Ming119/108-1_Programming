'''
025.質因數分解

輸入一個整數，將該正整數表示成質因數乘積。

輸入說明：
輸入一正整數。

輸出說明：
將整數分解為質因數的積，由小列到大，兩質數之間以 * 符號連結。

Sample input：
90

Sample output：
2*3*3*5
'''

def divPrime(num):
    lt = []
    while num != 1:
        for i in range(2, int(num+1)):
            if num % i == 0:
                lt.append(i)
                num = num / i
                break
    for i in range(0, len(lt)-1):
        print(lt[i],end='')
        print('*',end='')
    print(lt[-1],end='')

num = int(input())
if num > 1:
    divPrime(num)
