# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
i = 0
s = []

def print_d(n):
    if n > 0:
        global i 
        i = i + 1
        print(n%10)
        s.append(n%10)
        print_d(n//10)

if __name__ == "__main__":
    print_d(1234)
    print(s)
    b = "yes"
    for i in range(0, int(len(s)/2)+1):
        if s[i] != s[-(i+1)]:
            b = "not"
            break
    
    print(b)