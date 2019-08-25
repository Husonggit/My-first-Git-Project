#_*_coding:UTF-8_*_

def calc(n):
    print ('this is -->', n)
    if n//2 > 0:
        return calc(n/2)    #最后一次递归时跳出
    return n


print (calc(32))


