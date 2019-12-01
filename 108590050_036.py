"""
036

集合操作
給予兩集合，計算兩集合的運算的結果

輸入說明：
第一行輸入要輸入幾個字串
第二行輸入數個字串(以空格隔開)
第三行輸入運算子
第四行輸入要輸入幾個字串
第五行輸入數個字串(以空格隔開)

輸出說明：
輸出兩集合的運算後的結果，須以字典排序印出

注意運算子有:&、|、-、^、>、<、>=、<=、==

Sample Input
5
abc def ghi jkl mn
|
3
abc de jk

Sample Output
{'abc', 'de', 'def', 'ghi', 'jk', 'jkl', 'mn'}

逗點後須空一格
"""

n1=int(input())
s1=set(input().split(' '))
o=input()
n2=int(input())
s2=set(input().split(' '))

if o=='&':
    if s1&s2==set():print('{}')
    else:print("{'"+"', '".join(sorted(s1&s2))+"'}")
if o=='|':
    if s1|s2==set():print('{}')
    else:print("{'"+"', '".join(sorted(s1|s2))+"'}")
if o=='-':
    if s1-s2==set():print('{}')
    else:print(sorted(s1-s2))
if o=='^':
    if s1^s2==set():print('{}')
    else:print(sorted(s1^s2))
if o=='>':print(s1>s2)
if o=='<':print(s1<s2)
if o=='>=':print(s1>=s2)
if o=='<=':print(s1 <=s2)
if o=='==':print(s1==s2)
