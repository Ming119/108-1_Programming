'''
008.
輸入為一個英文句子以及一個單字，
請print出句子的長度，把句子以輸入的該單字進行分割。

範例輸入說明:
一個英文句子
一個英文句子中有出現的單字

範例輸出說明:
輸出句子的長度
輸出以單字進行分割後的句子

Sample Input:
Those who turn back never reach the summit.
who

Sample Output:
43
['Those ', ' turn back never reach the summit.']
'''

pp = input()
word = input()

print(len(pp))

op = pp.split(word)
print(op)
