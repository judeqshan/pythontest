def main():
    buble_sort()
    #sort_lib()

def sort_lib():
    x = int(input("x:\n"))
    y = int(input("y:\n"))
    z = int(input("z:\n"))
    a = [x, y, z]
    a.sort()
    print(a)

def buble_sort():
    x = int(input("x:\n"))
    y = int(input("y:\n"))
    z = int(input("z:\n"))
    #a = [x, y, z]
    a = [2, 1, 5, 3, 6, 2]
    
    for i in range(0,len(a)-1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
            print(a)
    print(a)



if __name__ == "__main__":
    main()