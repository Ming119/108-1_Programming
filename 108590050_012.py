'''
第三周 012.
檢查三門課程是否衝堂，
依序輸入課程編號(數字)、
上課小時數(1-3小時)、
上課時間(星期1-5, 第1-9節)

輸入說明
1001 (第一門課課程編號)
3 (3小時)
11 (星期1 第1節課)
59 (星期5 第9節課)
25 (星期2 第5節課)
2020 (第二門課課程編號)
2
25
16
2030 (第三門課課程編號)
…

輸出說明 (兩課程編號衝突在哪幾節)
1001 and 2020 conflict on 25

Sample Input：
1001
3
11
12
13
1002
3
21
22
23
1003
3
31
32
13
Sample Output：
1001 and 1003 confict on 13
'''

def data_input():
    lessonNo = input()
    lesson = [lessonNo]
    lessonHr = int(input())
    for i in range(lessonHr):
        lessonTime = input()
        lesson.append(lessonTime)
    return lesson

def check(lesson1, lesson2):
    set1 = set(lesson1)
    set2 = set(lesson2)
    checked = list(set1.intersection(set2))
    for i in range(len(checked)):
        print(lesson1[0],"and",lesson2[0],"confict on",checked[i])

L1 = data_input()
L2 = data_input()
L3 = data_input()

checked_lessons = check(L1,L2)
checked_lessons = check(L1,L3)
checked_lessons = check(L2,L3)
