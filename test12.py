from math import sqrt

def prime():
    # leap = 1
    for i in range(101,201):
        k = int(sqrt(i+1))
        for j in range(2, k+1):
            if i % j == 0:
                # leap = 0;
                print(i)
                break

        # if leap == 1:
        #     print(i)
        # leap = 1

def main():
    prime()

if __name__ == "__main__":  
    main()