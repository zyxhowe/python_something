#将一个正整数分解质因数。
import math
def prime(x):
    if x<4:
        return x
    y=int(math.sqrt(x))
    if y<4:
        y=x
    if x!=y*y:
        for i in range(2,y):
            if x%i==0:
                break
            if i==y-1:
                return x
    return 0

def anal(y):
    new=[1]
    if y==1:
        return new
    while prime(y)==0:
        for j in range(2,y):
            if y%j==0:
                new.append(j)
                y=int(y/j)
                break
    new.append(y)
    return new
n=int(input())
print(anal(n))
    
