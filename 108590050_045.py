"""
045
輸入兩個單字w1 and w2，
請計算出將w1變成w2最少需要多少次操作。

你可進行的操作包含以下
1.插入一個字元
2.刪除一個字元
3.替換一個字元

範例輸入:
horse
ros

範例輸出:
3

範例輸出說明:
替換操作 horse -> rorse(將h換成r)
刪除操作 rorse -> rose(將中間的r刪除)
刪除操作 rose-> ros(將e刪除)
"""

def editDistance(str1, str2, m , n):
    if m==0:
         return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        return editDistance(str1,str2,m-1,n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),
                   editDistance(str1, str2, m-1, n),
                   editDistance(str1, str2, m-1, n-1)
                   )

w1 = input()
w2 = input()
print(editDistance(w1, w2, len(w1), len(w2)))
