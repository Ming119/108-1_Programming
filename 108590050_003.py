"""
003. 數值運算

分別輸入 num1 num2 求出兩數的 Sum,Difference,Product,Quotient。

結果須輸出到小數點第二位
print("%.2f" %x1);

輸入:
25
2

NOTE:Difference為相差，並非25-2，而是兩數之間的差

輸出:
Difference:23.00
Sum:27.00
Quotient:12.50
Product:50.00
"""

num1 = int(input())
num2 = int(input())

diff = abs(num1 - num2)
sum = num1 + num2
quot = num1 / num2
prod = num1 * num2

print("Difference:" + "%.2f"%diff)
print("Sum:" + "%.2f"%sum)
print("Quotient:" + "%.2f"%quot)
print("Product:" + "%.2f"%prod)
