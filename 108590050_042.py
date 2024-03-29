'''
042.對發票
阿銘是一個很喜歡對發票的男孩，這一個月他存了很多張發票，
如果要人工對發票，搞不好會漏掉千萬獎金，所以他想要寫一個
對發票的程式，請你們幫幫他吧!

發票對獎規則、獎金:
獎項-------------------條件-------------------金額

特別獎---------發票全號與特別獎號碼相同---------1000萬

特獎-----------發票全號與特獎號碼相同-----------200萬

頭獎-----------發票全號與頭獎號碼相同-----------20萬

二獎-----發票末7位號碼與頭獎號碼末7位號碼相同-----4萬

三獎-----發票末6位號碼與頭獎號碼末6位號碼相同-----1萬

四獎-----發票末5位號碼與頭獎號碼末5位號碼相同-----4千

五獎-----發票末4位號碼與頭獎號碼末4位號碼相同-----1千

六獎-----發票末3位號碼與頭獎號碼末3位號碼相同-----2百

增開六獎---發票末三位號碼與增開六獎號碼完全一樣----2百

輸入說明:
輸入的第一行為特別獎號碼(1組)，第二行為特獎號碼(1組)，第三行為頭獎號碼(3組)，第四行為增開六獎號碼(3組)，輸入對獎號碼後，輸入核對發票的筆數，再輸入核對發票的號碼。

輸出說明
輸出總累積獲得的獎金(一律寫數字，不能寫1百、千、萬....)
注意:以得獎金數最高為獎金，不能累計!例如:得二獎(末7碼)，代表三(末6碼)、四(末5碼)、五(末4碼)、六(末3碼)都有中，但是只能得二獎，以下的金額不能累計在內!

Sample Input
45698621
19614436
96182420 47464012 62781818
928 899 118
5
45698621
96182420
33364012
12341818
76588928

Sample Output
10205200
'''

S = input()
F = input()
H = input().split(' ')
A = input().split(' ')
n = int(input())
data = [input() for i in range(n)]

def H_price(num):
    for i in H:
        if num == i:return 200000
        elif num[-7:] == i[-7:]:return 40000
        elif num[-6:] == i[-6:]:return 10000
        elif num[-5:] == i[-5:]:return 4000
        elif num[-4:] == i[-4:]:return 1000
        elif num[-3:] == i[-3:]:return 200
    else:return 0

def A_price(num):
    for i in A:
        if num[-3:] == i:return 200
    else:return 0

price = 0
for i in data:
    if i == S:
        price += 10000000
        continue
    if i == F:
        price += 2000000
        continue
    price += H_price(i)
    price += A_price(i)

print(price)
