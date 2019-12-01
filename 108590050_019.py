'''
Week 4

016.
n=1
#1
--------
n=2
##21
###1
------------
n=3
###321
####21
#####1
----------
n=4
####4321
#####321
######21
#######1
----------
n=5
#####54321
######4321
#######321
########21
#########1

input
--------------
4

output
-------------
####4321
#####321
######21
#######1
'''

n = int(input())

def printColumn(f,b):
    for i in range(f,0,-1):
        print("#",end="")
    for i in range(b,0,-1):
        print(str(i),end="")
    print()

def printRow(n):
    f = b = n
    for i in range(n):
        printColumn(f,b)
        f += 1
        b -= 1

printRow(n)
