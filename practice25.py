#求1+2!+3!+...+20!+...阶乘的和。
def factorial(x):
    mul=1
    for i in range(1,x+1):
        mul*=i
    return mul

n=int(input())
sum=0

for i in range(1,n+1):
    sum+=factorial(i)

print(sum)
        
