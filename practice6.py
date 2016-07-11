#Fibonacci sequence

#first method
#def fib(x):    
#    if x == 0:
#        y=0
#       return y
#    elif x == 1:
#        y=1
#        return y
#    elif x > 1:
#        y=fib(x-1)+fib(x-2)
#        return y
#    else:
#        print('error input')


#second method
def fib(x):
    if x>=0:
        a,b=0,1
        for i in range(x):
            a,b=b,b+a
        return a
    else:
        print('error input')


        
kk=int(input())
print(fib(kk))


