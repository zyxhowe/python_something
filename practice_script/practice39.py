
a=[3,5,9,13,23,31,47,49,51,57,63,69,73,85,91,97]



def mid(arr,x):
    if max(arr)<x:
        arr.append(x)
    elif min(arr)>x:
        arr.insert(0,x)
    else:
        arr_len=len(arr)
        mid_len=int(arr_len/2)
        while mid_len>1:
            print(mid_len)
            if arr[mid_len]>x:
                if x>=arr[mid_len-1]:
                    arr.insert(mid_len,x)
                    break;
                else:
                    mid_len=int(mid_len/2)
            else:
                if x<=arr[mid_len+1]:
                    arr.insert(mid_len+1,x)
                    break;
                else:
                    mid_len=int(mid_len*1.5)
    return arr

for i in range(1,200,7):
    s=a
    s=mid(s,i)
    print(s)


