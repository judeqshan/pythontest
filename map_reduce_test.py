from functools import reduce


def f(x):
    return x**2

print(list(map(f, [1, 2, 3])))


def add(x,y):
    return x+y

print(reduce(add, [1,2,3,5,7,9]))