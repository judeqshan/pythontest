# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

i = 0

def print_d(n):
    if n > 0:
        global i 
        i = i + 1
        print(n%10)
        print_d(n//10)

if __name__ == "__main__":
    print_d(3456789)
    print(i)