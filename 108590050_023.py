'''
023. 遞增等差數列

輸入說明
輸入三個整數a1、an、d。分別代表遞增等差數列的首項、末項、公差。

輸出說明
列出此遞增等差數列，以及此等差數列之和。

Sample input：
0 30 5

Sample output：
0 5 10 15 20 25 30
105
'''

a = input()
a = a.split(" ")
a = list(map(int, a))

def Arithmetic(a):
    sum = 0
    for i in range(a[0],a[1]+1,a[2]):
        print(i,end=" ")
        sum += i
    print()
    return sum

print(Arithmetic(a))
