# 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数

a = [2, 8, 6, 1, 78, 45, 34, 2]
n = 8
m = 2

b = a[0:n-m]

a.extend(b)
print(a[-n:-1])