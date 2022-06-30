# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def print_str(s):
    if len(s) > 0:
        print(s[-1], end='')
        print_str(s[:-1])

if __name__ == "__main__":
    print_str("12345678")