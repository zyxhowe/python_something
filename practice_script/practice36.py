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

for i in range(1,101):
    ss=prime(i)
    if ss>0:
        print(ss)
