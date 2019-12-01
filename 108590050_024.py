'''
024.計算BMI值的function

BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺2)
例如：一個52公斤的人，身高是155公分，則BMI為 :
52(公斤)/1.55^2 ( 公尺^2 )= 21.6
正常範圍為 BMI=18.5～24
輸入說明：
一正數身高(單位公尺)
一正整數體重(單位公斤)
輸出說明：
BMI值至小數點第二位。

身高正常範圍 0.5~2.50 公尺，體重正常範圍20~300 公斤，
若輸入不在正常範圍，
身高不正常輸出"Input Error 0.5~2.50"，
體重不正常輸出"Input Error 20~300" ，
若BMI在正常範圍，則輸出BMI值(至小數點第二位)。
若BMI值太高，輸出"BMI too hight"，太低輸出"BMI too low"。

->不會有身高與體重皆不正常之情況。<-

可以接受不斷輸入計算，直到輸入-1停止。

Sample input：
3 20
1.55 52
2.4 299
-1

Sample output：
Input Error 0.5~2.50
21.64
BMI too hight
'''

def calcBMI(a):
    BMI = a[1] / a[0]**2
    if BMI<18.5:
        print("BMI too low")
    elif BMI>24:
        print("BMI too hight")
    else:
        print("%.2f"%BMI)


a = []
check = 0
while(check != -1):
    a = input()
    a = a.split(" ")
    b = set(a)
    a = list(map(float, a))
    if '-1' in b:
        break

    if(a[0]<0.5 or a[0]>2.5):
        print("Input Error 0.5~2.50")
    elif(a[1]<20 or a[1]>300):
        print("Input Error 20~300")
    else:
        calcBMI(a)
