#将一个正整数分解质因数。
import math
def prime(x):
    y=int(math.sqrt(x))
    if y==1:
        return x
    if x!=y*y:
        for i in range(2,y):
            if x%i==0:
                break
            if i==y-1:
                return x
    return 0

def anal(y):
    for k in range(2,y):
        if y%k==0:
            return k

n=int(input())
m=int(math.sqrt(n))
a=[]
for i in range(2,m):
    s1=prime(n)
    if s1==0:
        s2=anal(n)
        n=int(n/s2)
        a.append(s2)
    else:
       a.append(s1)
       break

print(a)
    
