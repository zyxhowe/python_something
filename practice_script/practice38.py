#求一个3*3矩阵对角线元素之和
#l=[[1,2,3],[2,3,4],[3,4,5]]
l=[]
for i in (0,1,2):
    l.append([])
    for j in (0,1,2):
        n=int(input('%d-%d number input'%(i+1,j+1)))
        l[i].append(n)

print(l[0])
print(l[1])
print(l[2])
sum=0
for k in (0,1,2):
    sum+=l[k][k]
print(sum)
