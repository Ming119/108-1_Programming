"""
10進制轉換

進制可設定為2~35進制

如果輸出值>9，則以a~z表示

輸入說明：
輸入一數字(代表要轉換的數字)
輸入一數字(代表要轉換的進制)

輸出說明：
輸出轉換後的結果

Sample Input：
10
4
Sample Output：
22
---------------
Sample Input：
100
16
Sample Output：
64
"""

num = int(input())
pn = int(input())

res_dict= {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}
res = []

if pn > 1 and pn < 36:
    while num >= pn:
        res.append(num % pn)
        num = num // pn
    res.append(num % pn)

    res.reverse()
    for i in res:print(res_dict[i],end="")
