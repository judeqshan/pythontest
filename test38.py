# 求一个3*3矩阵主对角线元素之和。
s = 0
a = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,3):
    s += a[i][i]
    print(a[i][i])
print(s)