#利用递归函数调用方式，将所输入的字符，以相反顺序打印出来。

def recursion(s,l):
    if l==0:
        return
    print(s[l-1])
    recursion(s,l-1)




nstr=input()
l=len(nstr)
recursion(nstr,l)
