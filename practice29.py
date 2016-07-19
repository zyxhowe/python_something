#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
import math,sys

def decompose(x):
    if x < 100000:
        sum=[]
        while x>9:
            mid=x%10
            x=int(x/10)
            sum.append(mid)
        sum.append(x)
        return sum
    else:
        print('input error number')
        sys.exit()

n=int(input())

a=decompose(n)
l=len(a)
a.reverse()
print(l,a)
