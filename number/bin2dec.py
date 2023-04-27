def add_1(binary_inpute):#二进制编码加1
    _,out = bin(int(binary_inpute,2)+1).split("b")
    return out

def reverse(binary_inpute):#取反操作
    binary_inpute = list(binary_inpute)
    binary_out = binary_inpute
    for epoch,i in enumerate(binary_out):
        if i == "0":
            binary_out[epoch] = "1"
        else:
            binary_out[epoch] = "0"
    return "".join(binary_out)

a = "000000000011010"
a = "100000000011010"
a = "11111111"
if a[0] == "1":#判断为负数
    a_reverse = reverse(a[1:])  # 取反
    a_add_1 = add_1(a_reverse)  # 二进制加1
    a_int = -int(a_add_1, 2)
else:
    a_int = int(a[1:],2)
print(a_int)



