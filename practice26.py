#利用递归方法求阶乘。


def fct(x):
    if x == 1:
        return 1
    else:
        return x*fct(x-1)

n=int(input())

print('%d!=%d'%(n,fct(n)))
