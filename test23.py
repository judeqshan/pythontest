# 题目：打印出如下图案（菱形）:

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

def print_star1():
    for i in range(1,8):
        if i <= 4:
            for j in range(4-i,0,-1):
                print(" ", end='')
            for k in range(1,2*i):
                print("*", end='')
            print("")
        else:
            for j in range(1,i-3):
                print(" ", end='')
            for k in range(1,5-2*(i-5)+1):
                print("*", end='')
            print("")

def print_star2(n):
    up_num = round(n/2)
    down_num = int(n/2)
    for i in range(1, up_num + 1):
        for j in range(up_num-i,0,-1):
            print(" ", end='')
        for k in range(1,2*i):
            print("*", end='')
        print("")
    for i in range(1, down_num + 1):
        for k in range(1,i+1):
            print(" ", end='')
        for j in range(1, 2*(up_num-1) - 2*(i-1)):
            print("*", end='')
        print("")

if __name__ == "__main__":
    print_star2(12)