#打印菱形
from sys import stdout
import math

def pri(x):
    for i in range(0,x):
        stdout.write(' ')
def prir(x):
    for i in range(0,x):
        stdout.write('*')
    
def rhombus(n):
    for i in range(1,2*n):
        b=int(math.fabs(n-i))
        if i<=n:
            ss=int(2*i-1)
        else:
            ss=2*(n-b)-1
        pri(b)
        prir(ss)
        print('')

m=int(input())
rhombus(m)
