#输入三个整数x,y,z，请把这三个数由小到大输出。
l=[]
x=int(input('first number'))
y=int(input('second number'))
z=int(input('third number'))

l.append(x)
l.append(y)
l.append(z)
l.sort()
print(l)
