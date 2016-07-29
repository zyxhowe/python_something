#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

n=int(input())
a1=2
a2=1
sum=0
for i in range(0,n):
    sum+=a1/a2
    print(a1,'/',a2,sum)
    c=a1
    a1+=a2
    a2=c

print(sum)
    
