#利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
#可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
#高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


sr=int(input('净利润:'))
arr=[100,60,40,20,10,0]
ddd={100:0.01,60:0.015,40:0.03,20:0.05,10:0.075,0:0.1}
sum=0
def sfuc(x,y):
    sl=x*y
    print('tax',sl)
    return sl

for i in range(0,6):
    if sr > arr[i]:
        sr-=arr[i]
        sum+=sfuc(sr,ddd[arr[i]])
        sr=arr[i]

print(sum)
