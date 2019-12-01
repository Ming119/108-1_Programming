'''
輸入 N ，之後輸入 N 個整數， 例如N=5，5個整數 11, 45, 8, 13, 22。
輸出其中第二大的數
輸出最大的數與最小的數相乘的結果。

Sample Input
3
1
2
3

Sample Output
2
3
'''

def calc(list):
    list.sort(reverse = True)
    print(list[1])
    sum = list[0] * list[-1]
    print(sum)

N = int(input())
list = []
for i in range(N):
    tmp = input()
    list.append(int(tmp))

calc(list)
