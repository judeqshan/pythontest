# -*- coding:utf-8 -*-
# @Time      :2020/4/17

import time


def sum_int():
    start_time = time.time()
    a = (x for x in range(4*10 ** 8))
    sum_int = 0
    for i in a:
        sum_int += i

    print(sum_int)
    print(f'cost_time:{time.time() - start_time}')


if __name__ == "__main__":
    sum_int()