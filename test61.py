# 打印出杨辉三角形（要求打印出10行如下图）
s = []
for i in range(10):
    s.append([])
    for j in range(10):
        s[i].append(0)

for i in range(0,10):
    for j in range(0,i+1):
        if j-1 >= 0 and j < i:
            s[i][j] = s[i-1][j-1] + s[i-1][j]
        else:
            s[i][j]=1
    print(s[i])