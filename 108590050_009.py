'''
009.
請輸入為一個人的全名加上一組生日，
將以上資訊依下列格式輸出，
{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.

範例輸入說明:
輸入一個人的全名，
順序為FirstName LastName
輸入他的生日，
他的生日年、月、日會以/隔開
yyyy/mm/dd

範例輸出說明:
套用以下格式輸出
{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.


Sample Input:
kobe Bryant
1978/08/23

Sample Output
kobe is born at year 1978 month 08 day 23 in Bryant family.
'''

name = input()
bd = input()
name = name.split(" ")
bd = bd.split("/")

data = {'FirstName' : name[0], 'LastName' : name[1], 'yyyy' : bd[0], 'mm' : bd[1], 'dd' : bd[2]}

str = "{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.".format(**data)
print(str)
