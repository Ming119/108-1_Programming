'''
030.數字排序

給定一串數字，將這一連串數字分為奇數在右，偶數在左，
並且奇數按照由小到大排，偶數按照由大到小排，

Input:
1 2 3 4 5 6 7 8 9

Output:
[1, 3, 5, 7, 9, 8, 6, 4, 2]
'''

alist=list(map(int,input().split(' ')))
oddlist=sorted([i for i in alist if i%2!=0])
evenlist=sorted([i for i in alist if i%2==0])
evenlist.reverse()
print(list(map(int,(oddlist+evenlist))))
