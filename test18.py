n = int(input('num:'))
a = int(input('a:'))
l = []

for i in range(1, n+1):
    tmp = 0
    for j in range(1,i+1):
        tmp += a*(10 ** (j-1))
    l.append(tmp)
print(l)
s = sum(l)
print(s)
