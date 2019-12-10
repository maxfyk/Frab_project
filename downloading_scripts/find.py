import time
def bm(string, sub):
    lenl = len(sub)
    lenstr = len(string)
    i = lenstr
    j = lenl-1
    k=0
    a=0
    try:
        while i <= lenstr:
              while j < lenl and sub[j] == string[i-j]:
                    j = j - 1
                    a=a+1
                    if a == lenl:
                       if i<=0:
                           d = ''.join('.' for l in range(lenstr+i))
                           return(True)
                       else:
                           d = ''.join('.' for l in range(i))
                           return(True)
              i=i-1
              k=k+1
    except:
        pass
    return (False)
