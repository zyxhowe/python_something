import math
#判断101-200之间有多少个素数，并输出所有素数。
a=[]

def prime(x):
    y=int(math.sqrt(x))
    if y==1:
        return x
    if x!=y*y:
        for i in range(2,y):
            j=int(x/i)
            if x==j*i:
                break
            if i==y-1:
                return x
    return 0

for n in range(100,200):
    ss=prime(n)
    if ss!=0:
        a.append(ss)
        
print(a)
    
