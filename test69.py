#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# nb niubia
# 注重思路，核心在于用一个标示，然后最后标示就是要找的数据。
# 还有一点，不用改变原始数组。

if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)
    print(num)
 
    i = 0
    k = 0
    m = 0
 
    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0
    i = 0
    while num[i] == 0: i += 1
    print(num[i])