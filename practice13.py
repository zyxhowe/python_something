#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。

def Narcissus():
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                n=a*a*a+b*b*b+c*c*c
                m=a*100+b*10+c
                if n>100 and n<1000 and n==m:
                    print(a,b,c,n)

Narcissus()
