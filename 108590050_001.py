"""
001. 計算總成績、平均

某一學生修國文、計算機概論、計算機程式設計三科，使用者輸入名字（一個char）、學號（int）、三科成績(int)。
(1) 計算學生總成績、平均。
(2) 印出名字、學號、總成績、平均。

Input:
K
905067
100
100
100

Output:
Name:K
ID:905067
Average:100
Total:300
"""

name = input()
ID = int(input())
D1 = int(input())
D2 = int(input())
D3 = int(input())

total = D1 + D2 + D3
avg = int(total / 3)

print("Name:" + name)
print("ID:" + str(ID))
print("Average:" + str(avg))
print("Total:" + str(total))
