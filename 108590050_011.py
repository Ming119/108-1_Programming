'''
第三周 011.
撲克牌
A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
A~10 點數為 1~10，J, K, Q 為 0.5。
X, Y 兩個人各發三張撲克牌，加總點數越接近 10.5 的贏；超過 10.5 ，爆掉且分數為 0。
程式：
輸入：X, Y 兩個人的三張撲克牌。
輸出：兩個人的點數，以及A贏或B贏或平手。

Sample Input：
A
2
3
2
3
4
Sample Output：
6
9
B贏

Sample Input：
A
2
3
A
2
3
Sample Output：
6
6
平手
'''

def changeCard(player):
  while ('A' in player):
    player[player.index('A')] = '1'
  while ('J' in player):
    player[player.index('J')] = '0.5'
  while ('Q' in player):
    player[player.index('Q')] = '0.5'
  while ('K' in player):
    player[player.index('K')] = '0.5'

X1 = input()
X2 = input()
X3 = input()
Y1 = input()
Y2 = input()
Y3 = input()

X = [X1, X2, X3]
Y = [Y1, Y2, Y3]

changeCard(X)
changeCard(Y)

X_value = float(X[0]) + float(X[1]) + float(X[2])
Y_value = float(Y[0]) + float(Y[1]) + float(Y[2])

if X_value > 10.5:
  X_value = 0
if Y_value > 10.5:
  Y_value = 0

print(int(X_value))
print(int(Y_value))

if (X_value > Y_value):
  print('A贏')
elif (Y_value > X_value):
  print('B贏')
elif (X_value == Y_value):
  print('平手')
