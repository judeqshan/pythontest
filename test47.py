# 题目：两个变量值互换。

def swap(x,y):
    x,y = y,x
    return x,y 
    

if __name__ == "__main__":
    a = 1
    b = 2
    print(swap(a,b))
    