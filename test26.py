# 利用递归方法求5!。

def tigui(n):
    if n == 1:
        return 1
    return n * tigui(n-1)


if __name__ == "__main__":
    print(tigui(5))