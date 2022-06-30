# 题目：求1+2!+3!+...+20!的和。

from re import L, S


def jiecheng(n):
    s = 0 
    for i in range(1, n+1):
        jie = 1 
        for i in range(i, 1, -1):
            print(" %d *"%i, end='')
            jie *= i
        print("")
        s += jie
    print(s)

    

def jiecheng1(n):
    jie = 1 
    s = 0 
    for i in range(1, n+1):
        jie *= i
        s += jie
    print(s)

    
if __name__ == "__main__":
    jiecheng1(10)
    jiecheng(10)
    