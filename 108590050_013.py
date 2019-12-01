'''
第三周 013..
輸入每月網內、網外、市話、通話時間(sec)及網內、網外 簡訊則數，求最佳資費。
費率如下表：
*月租費也要納入考量
資費類型 183型 383型 983型
月租費 183元 383元 983元
優惠內容 月租費可抵等額通信費
語音 網內 0.08 0.07 0.06
(元/秒) 網外 0.1393 0.1304 0.1087
市話(元/秒) 0.1349 0.1217 0.1018
簡訊 網內 1.1287 1.1127 0.9572
(元/則) 網外 1.4803 1.2458 1.1243

輸入 網內語音(sec)、網外語音(sec)、市話(sec)、網內簡訊數、網外簡訊數 測試資料。
Sample Input：
100
100
100
100
100

Sample Output：
183型
'''

def calcPrice(plan):
    Price = plan[1]*in_voice + plan[2]*out_voice + plan[3]*city_voice + plan[4]*in_mess + plan[5]*out_mess
    if (Price < plan[0]):
        return plan[0]
    else:
        return Price

in_voice = int(input())
out_voice = int(input())
city_voice = int(input())
in_mess = int(input())
out_mess = int(input())

plan1 = [183, 0.08, 0.1393, 0.1349, 1.1287, 1.4803]
plan2 = [383, 0.07, 0.1304, 0.1217, 1.1127, 1.2458]
plan3 = [983, 0.06, 0.1087, 0.1018, 0.9572, 1.1243]

calc1 = calcPrice(plan1)
calc2 = calcPrice(plan2)
calc3 = calcPrice(plan3)

if (calc1 < calc2):
    print('183型')
elif (calc2 < calc3):
    print('383型')
else:
    print('983型')
