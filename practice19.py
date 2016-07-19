#一个数如果恰好等于它的因子之和，这个数就称为"完数"。
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

def factor(y):
    new=[]
    for l in range(1,y):
        if y%l==0:
            new.append(l)
    return new

def wannum(z):
    fin=[]
    for k in range(2,z):
        sum=0
        ss=factor(k)
        for h in ss:
            sum+=h
        if sum == k:
            fin.append(k)
            print(ss,sum)
    return fin
            
n=1000
print(wannum(n))

