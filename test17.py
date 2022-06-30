from pip import main


def main():
    s = input("input str:")
    char_num = num_num = space_num = other_num = 0
    for i in range(0,len(s)):
        print(s[i])
        if s[i].isalpha():
            char_num += 1
        elif s[i].isdigit():
            num_num += 1
        elif s[i].isspace():
            space_num += 1
        else:
            other_num += 1
    print("char=%d num=%d space=%d other=%d"%(char_num, num_num, space_num, other_num))

    

if __name__ == "__main__":
    main()