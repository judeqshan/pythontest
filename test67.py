# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
from functools import reduce
a= []
for i in range(1, 4):
    a.append(int(input("input:")))
max = reduce(lambda x,y: x if x>y else y, a)
min = reduce(lambda x,y: x if x<y else y, a)
 
print(max)