import math
#一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if i+100==x*x and i+268==y*y:
        print(i)
