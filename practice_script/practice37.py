#对几个数进行选择排序。
a=[7,2,13,56,44,33,65,24,68,34,45,13,23,29]
l=len(a)

print('number is ',a)
for i in range(0,l):
    b=a[i:]
    s=min(b)
    j=b.index(s)
    b[0],b[j]=b[j],b[0]
    a=a[0:i]+b

print('sort',a)
