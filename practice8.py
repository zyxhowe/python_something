#输出9*9乘法口诀表。
def mul(n):
    for i in range(1,n):
        for j in range(1,n):
            print(i,'*',j,'=',i*j)

mul(10)
