from print_test import *

cpdef int sum_of_squares(int n):
    cdef int result = 0
    cdef int i
    for i in range(1, n+1):
        result += i * i
    print_test()
    return result