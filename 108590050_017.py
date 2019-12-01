'''
設計計算BMI值的Python function
BMI值計算公式: BMI = 體重(公斤) / 身高^2(公尺^2)，例如：一個52公斤的人，身高是155公分，則BMI為 : 52(公斤)/1.55^2 ( 公尺^2 )= 21.6。
正常範圍為BMI=18.5～24。
請設計一個 function，從鍵盤輸入姓名name、身高、體重。
當BMI太大，輸出 Hi name, Your BMI: xxx too HIGH.
當BMI太小，輸出 Hi name, Your BMI: xxx too LOW.
在正常範圍，輸出 Hi name, Your BMI: xxx.
註:BMI直接%f輸出即可。

Sample Input
Jeff
155
52

Sample Output
Hi Jeff, Your BMI: 21.644121.
'''

def calc_BMI(name, H, W):
    BMI = W / (H/100)**2
    if BMI > 24 :
        print("Hi",name+", Your BMI:","%.6f"%BMI,"too HIGH.")
    elif BMI <18.5:
        print("Hi",name+", Your BMI:","%.6f"%BMI,"too LOW.")
    else:
        print("Hi",name+", Your BMI:","%.6f"%BMI+".")

name = input()
H = int(input())
W = int(input())

calc_BMI(name, H, W)
