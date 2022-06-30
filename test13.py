#!/user/bin/python

for n in range(100,1000):
    i = int(n / 100)
    j = int((n % 100) / 10)
    k = n % 10
    if n == i*i*i + j*j*j + k*k*k: 
        print(n)