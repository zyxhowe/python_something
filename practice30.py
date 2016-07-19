#一个5位数，判断它是不是回文数。

def Five_number_Palindrome(x):
    if x < 100000 and x>9999:
        sum=[]
        while x>9:
            mid=x%10
            x=int(x/10)
            sum.insert(0,mid)
        sum.insert(0,x)
    else:
        print('input error number')
        sys.exit()
    return sum

   

n=int(input())
s=Five_number_Palindrome(n)

if s[0]==s[4] and s[1]==s[3]:
    print('Yes,%d is palindrome'%n)
else:
    print('No,%d is not  palindrome'%n)
