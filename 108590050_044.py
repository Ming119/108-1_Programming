'''
044.解密碼

小淞是有錢大地主，他將所有金銀財寶都收藏在一個藏寶箱裡，藏寶箱要輸入正確密碼才能開啟。
寶箱密碼寫在一卷捲軸，捲軸內有一組英文句子，由數字 0~9 和大小寫英文字母、空格組成。
解碼方式為將出現在句子的連續數字取出反轉，將所有反轉後的數字相加，則得出密碼。
例如 :
Today is my 45 birthday , There are 65guest come for the 1000 party,I got789gifts t0 open.
則取出其中數字 45,65,1000,789, 和 0, 分別作反轉後相加可得 54+56+1+987+0=1098 ，密碼即為 1098 。

輸入說明 ：
輸入為一行的文章，含有 26 個英文字母 ( 大小寫 ) ，及數字 (0~9) 、空格、標點符號、特殊符號任意組合而成。

輸出說明 ：
將密碼輸出。

Sample Input
Today is my 45 birthday , There are 65guest come for the 1000 party,I got789gifts t0 open.

Sample Output
1098
'''

import re

def reverse(str):
    new_str = str[-1::-1]
    return int(new_str)

data = input()
data_list = re.findall('\d+', data)
reverse_list = [reverse(i) for i in data_list]
print(sum(reverse_list))
