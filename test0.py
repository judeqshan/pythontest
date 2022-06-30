# 编写一个函数，
# 输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n

i = int(input("input:"))
l = int(i/2)

tmp = 0
sum = 0

for i in range(1, l):
    if i % 2 == 0:
        tmp = 2*i  
    else:
        tmp = 2*i+1
    sum += 1.0/tmp
    print("1/%d "%(tmp), end="")

print(sum)