"""
撲克牌四種花色分別是黑桃、紅心、磚塊、梅花，定義 S, H, D, C。
牌面數字 2 ~ 14，A 為 14，J 為 11， Q 為 12，K 為 13，共有52張牌。
花色大小：黑桃>紅心>方塊>梅花。

編碼規則為數字+花色，例如 10S 表黑桃 10、7D 表磚塊 7，12C 表梅花 Q。

牌型由小到大如下：

散牌 -> 撲克牌遊戲把單一張牌命名為單張，沒有任何花色牌型，編號 0。
一對 -> 兩張數字一樣的命名為 Pair，編號 1。
兩對 -> 2 組 Pair 的牌稱為 Two pair，編號 2。
三條 -> 三張一樣數字的稱為 Three of a Kind，編號 3。
順子 -> 數字連續的 5 張牌稱為 Straight，包括 13 ,14, 2, 3, 4 或 12, 13 ,14, 2, 3 等，編號 4。
同花 -> 五張同一花色的牌稱為 Flush，編號 5。
葫蘆 -> Three of a Kind 加一個 Pair 稱為 Full House，編號 6。
四條 -> 四張一樣數字稱為 Four of a Kind，編號 7。
同花順 -> 數字連續的 5 張且花色一樣稱為 Straight Flush，編號 8。

輸入5張撲克牌，判斷哪一類型的牌形編號(0~8)。

輸入說明 ：
第一列輸入為5個編碼分別由空格分開，表示5張撲克牌。

輸出說明 ：
輸出為一個0~8的整數，代表牌型編號；注意要以「最大的牌型為輸出」。
數字連續的定義為：K(13) 和 A(14) 有相連，A(14) 和 2 有相連，依此類推。

Input:
-------------------------
9D 8C 8S 8H 9S Output:

Output
------------------------
6
"""

def StraightFlush(cardsR, cardsS):
    if Straight(cardsR) and len(set(cardsS)) == 1: return True
    else: return False

def FourOfKind(cardsR):
    for card in set(cardsR):
        if cardsR.count(card)== 4: return True
    else: return False

def FullHouse(cardsR):
    if ThreeOfKind(cardsR) and Pair(cardsR): return True
    else: return False

def Flush(cardsS):
    if len(set(cardsS)) == 1: return True
    else: return False

def Straight(cardsR):
    checking = max(set(cardsR)) - min(set(cardsR)) + 1
    if (checking == 5 or checking == 13) and len(set(cardsR)) == 5: return True
    else: return False

def ThreeOfKind(cardsR):
    for card in set(cardsR):
        if cardsR.count(card)== 3: return True
    else: return False

def TwoPair(cardsR):
    cardsCount = [cardsR.count(card) for card in set(cardsR)]
    if cardsCount.count(2) == 2: return True
    else: return False

def Pair(cardsR):
    for card in set(cardsR):
        if cardsR.count(card)== 2: return True
    else: return False

import re

cards = input()
cards_Rank = list(map(int, re.findall(r"\d+", cards)))
cards_Suit = [i for i in cards if i.isalpha()]

if StraightFlush(cards_Rank, cards_Suit): print('8')
elif FourOfKind(cards_Rank): print('7')
elif FullHouse(cards_Rank): print('6')
elif Flush(cards_Suit): print('5')
elif Straight(cards_Rank): print('4')
elif ThreeOfKind(cards_Rank): print('3')
elif TwoPair(cards_Rank): print('2')
elif Pair(cards_Rank): print('1')
else: print('0')
