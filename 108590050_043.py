'''
043.Google搜尋器
讓我們來用程式模擬Google的搜尋器

輸入說明:
先輸入整數N，代表有N筆資訊(一串文字，包含特殊字元、空格...)，接著輸入N行
資訊，再輸入使用者要的關鍵字(一行以空格隔開的關鍵字詞)

輸出說明:
根據資訊中包含幾項關鍵字的多寡進行排序，由多到少印出(若一樣，則照字典印出)，並將匹配到的關鍵字全部大寫，其他保持原樣
(若拼字不完全相同，例如engineer、eng，則輸出ENGineer；大小寫不同仍視為相同，例如engINeer、NEER，則輸出engINEER)。
方便使用者找到自己想要的資料。

Sample Input:
5
National Taipei University of Technology, Taipei Tech
National Taiwan University of Science and Technology, Taiwan Tech
Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology
Department of Computer Science and Information Engineering, Taipei Tech
Department of Computer Science and Information Engineering, National Taiwan University
Taipei Tech comPuTer Science engineer

Sample Output:
Department of COMPUTER SCIENCE and Information ENGINEERing, National Taiwan University of SCIENCE and TECHnology
Department of COMPUTER SCIENCE and Information ENGINEERing, TAIPEI TECH
National TAIPEI University of TECHnology, TAIPEI TECH
Department of COMPUTER SCIENCE and Information ENGINEERing, National Taiwan University
National Taiwan University of SCIENCE and TECHnology, Taiwan TECH
'''

import re

n = int(input())
data = [input() for i in range(n)]
search = input().split(' ')

res_list = []

for d in data:
    count = 0
    for s in search:
        d = re.sub(s, s.upper(), d, flags=re.IGNORECASE)
    upper_data = re.findall('[A-Z]+', d)
    for i in upper_data:
        if len(i) > 1:count += 1
    res_list.append([count,d])

res_list = sorted(res_list, key=(lambda x:[-x[0],x[1]]))
for i in range(len(res_list)):print(res_list[i][1])
