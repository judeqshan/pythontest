'''
index为该数据位宽,number为待转换数据,
feature为True则进行十进制转二进制,为False则进行二进制转十进制。
'''
def intToBin(number,index,feature=True):
    if (feature==True):#十进制转换为二进制
        if(number>=0):
            b=bin(number)
            b = '0' * (index+2 - len(b)) + b
        else:
            b=2**(index)+number
            b=bin(b)
            b = '1' * (index+2 - len(b)) + b    #注意这里算出来的结果是补码
        b=b.replace("0b",'')
        b=b.replace('-','')

        return b
    elif(feature==False):#二进制转换为十进制
        i=int(str(number),2)
        if(i>=2**(index-1)):#如果是负数
            i=-(2**index-i)
            return i
        else:
            return i
# 测试代码，测intToBin
while(1):
    number=int(input("number="))
    index=int(input("index="))
    feature=int(input("feature="))
    re=intToBin(number,index,feature=feature)
    print("result=",re)
