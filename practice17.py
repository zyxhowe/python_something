#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
import string

str1=input()

wo=0
bl=0
nu=0
ot=0

for c in str1:
    if c.isalpha():
        wo+=1
    elif c.isspace():
        bl+=1
    elif c.isdigit():
        nu+=1
    else:
        ot+=1
print ('char=%d,space=%d,dight=%d,others=%d'%(wo,bl,nu,ot))
