#求s=a+aa+aaa+aaaa+aa...a的值
import math
a=int(input('number is:'))
n=int(input('times:'))
s=0
sum=0
for i in range(0,n):
    s+=a*pow(10,i)
    sum+=s
    print(s)

print(sum)
