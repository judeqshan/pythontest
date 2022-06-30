# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

def fen(n):
    s = 0
    up = 2
    down = 1
    for i in range(1,n+1):
        s += up/down
        tmp1 = up
        tmp2 = down
        down = tmp1
        up = tmp1 + tmp2
        print("%d/%d "%(up, down),end="")
    
    print(s)


if __name__ == "__main__":
    fen(20)