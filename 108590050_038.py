"""
038

請先輸入一個數n，
該數n決定後面要輸入幾個區間，
將第n個區間插入第1~n-1個區間，
並輸出最後結果。

範例輸入說明:
假設輸入n = 3
後面接著輸入三個區間，
1,3
6,9
2,5

範例輸出說明:
因2~5與6~9沒有交集，所以6,9不變
但1~3與2~5有交集，所以把2,5插入1~3中
則結果為1,5
所以最後輸出為:
1,5
6,9

sample input:
3
1,3
6,9
2,5

sample output:
1,5
6,9

------------------------------------
sample input2:
6
1,2
3,5
6,7
8,10
12,16
4,8

sample output2:
1,2
3,10
12,16

3,5 與 6,7 與8,10 它們與4,8皆有交集
但因6,7已在4,8中，所以它可忽略
且4,8剛好在3,5與8,10之間，
所以合併為3,10
"""

n=int(input())
data=sorted([list(map(int,input().split(',')))for i in range(n)])
s,e=data[0][0],data[0][1]
res=[]
for i in range(1,n):
    if data[i][0]<=e and data[i][1]>e:e=data[i][1]
    elif data[i][0]>e:
        res.append([str(s),str(e)])
        s,e=data[i][0],data[i][1]
res.append([str(s),str(e)])
for i in range(len(res)):
    print(','.join(res[i]))
