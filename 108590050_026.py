'''
026. 計算出最小公倍數

輸入說明：
兩個正整數

輸出說明：
這兩個正整數的最小公倍數。

Sample input：
2
3

Sample output：
6


((維基百科，最小公倍數：
https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%85%AC%E5%80%8D%E6%95%B8
'''

def gcd(n1, n2):
    return n1 if n2 == 0 else gcd(n2, n1 % n2)

def lcm(n1, n2):
    return n1 * n2 / gcd(n1, n2)

n1 = int(input())
n2 = int(input())
print(int(lcm(n1,n2)))
