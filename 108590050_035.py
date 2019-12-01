'''
數字GCD大家都算過，那字串的呢？

字串GCD定義範例如下

GCD(ABCABC, ABC) = ABC

GCD(ABABAB, ABAB) = AB

GCD(AAAAAA, AAAAA) = A

你能幫忙求出字串的GCD嗎？

輸入說明:
每一行有兩個字串s1、s2
輸入皆為大寫英文字母
至-1結束

輸出說明:
輸出兩字串的GCD
如果兩字串沒有GCD，輸出"No GCD"

Sample Input
ABCABC ABC
ABABAB ABAB
AAAAAA AAAAA
ZERO JUDGE
-1

Sample Output
ABC
AB
A
No GCD
'''

def GCD(s1, s2):
    if len(s1)>len(s2):return GCD(s2,s1)
    res='No GCD'
    for i in range(len(s1), 0, -1):
        if len(s1)%i or len(s2)%i:continue
        tmp1,tmp2=len(s1)//i,len(s2)//i
        gcd=s1[:i]
        re1,re2=gcd*tmp1,gcd*tmp2
        if re1==s1 and re2==s2:
            res=gcd
            break
    return res
while True:
    s=input().split(' ')
    if s[0]=='-1':break
    print(GCD(s[0],s[1]))
