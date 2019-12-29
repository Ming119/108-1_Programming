"""
047 解密碼2

老張是有錢大地主，他將所有金銀財寶都收藏在一個藏寶箱裡，藏寶箱要輸入正確密碼才能開啟。
寶箱密碼寫在一卷捲軸，捲軸內有一組英文句子，由數字 0~9 和大小寫英文字母、空格組成。解碼方式如下

密碼是將句子分析字元出現頻率，找出次數大於0小於10的字元，句子中所有出現的英文單子個別蒐集(有大小寫區別)，
輸出方式由句子第一個字元出現次數開始輸出，直到句子最後，其中若碰到已輸出過字元，則跳過不重複輸出，若碰到數字則直接輸出，詳見範例


例如 :
Be9tter to light one candle than to curse the darkness xxxxxxxxxxx

分析字元頻率，碰到第一個字元為大寫B，只出現過一次則為1，碰到第二個字元為小寫e，
出現次數為七次則為7，第三個碰到的字元為9則輸出9，所以密碼開頭就是179如下:
(B,1)(e,7)[9](t,7)(r,3)(o,3)(l,2)(i,1)(g,1)(h,3)(n,4)(c,2)(a,3)(d,2)(u,1)(s,3)(k,1)
，密碼即為 17973321134232131，
其中(x, 11)超過10不予計算。
空格不列入計算!
-----------------------------------------------------
輸入說明 ：

輸入一段句子，含有大小寫英文字母，數字0~9、空格。
-----------------------------------------------------

Sample Input

Be9tter to light one candle than to curse the darkness xxxxxxxxxxx
-----------------------------------------------------
Sample Output

17973321134232131
"""

str = input().split(' ')
str = ''.join(str)

counted_set = set()
pw = []

for i in range(len(str)):
    count = 0
    if str[i].isdigit(): pw.append(str[i])
    elif str[i] not in counted_set:
        count = str.count(str[i])
        if count < 10: pw.append(count)
        counted_set.add(str[i])

for i in pw: print(i, end='')
