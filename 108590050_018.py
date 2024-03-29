'''
018.

請使用 while loop或for loop
第一個輸入意義為選擇三種圖形:
1 三角形方尖方面向右邊
2 三角形方尖方面向左邊
3 菱形

第二個輸入意義為畫幾行
(奇數，範圍為 3,5,7,9,....,21)

input
1 (第一種圖形，三角形尖方面向右邊)
9 (共 9 行)
--------------------------
output
*
**
***
****
*****
****
***
**
*
---------------------------
input
2 (第二種圖形，三角形尖方面向左邊)
5 (共 5 行)
---------------------------
output
..*
.**
***
.**
..*
--------------------------
input
3 (第三種圖形: 菱形 )
3 (共 3 行數)

輸出
.*
***
.*

'''

graph = int(input())

if (graph > 0 and graph < 4):
    lines = int(input())
    star = lines // 2 + 1
    if (lines > 2 and line < 22 and (lines % 2 != 0)):
        if(graph == 1):
            for i in range(1, star + 1):
                print("*" * i)
            for i in range(star - 1, 0, -1):
                print("*" * i)

        elif(graph == 2):
            for i in range(1, star + 1):
                print("." * (star - i) + "*" * i)
            for i in range(star - 1, 0, -1):
                print("." * (star - i) + "*" * i)

        elif(graph ==3):
            for i in range(1, star + 1):
                print("." * (star - i) + "*"*(i*2 - 1))
            for i in range(star - 1, 0, -1):
                print("." * (star - i) + "*"*(i*2 - 1))
