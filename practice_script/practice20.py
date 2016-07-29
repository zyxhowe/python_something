#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
#求它在第10次落地时，共经过多少米？第10次反弹多高？
import math

n=int(input())

def spr(x):
    y=100
    sum=0
    for i in range(1,x+1):
        sum+=y
        y*=0.5
        sum+=y
    print('%d次落地时共经过%fm,第%d次反弹%fm'%(n,sum,n,y))

spr(n)
    


        
