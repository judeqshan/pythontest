def main():
    year = int(input("year:\n"))
    month = int(input('month:\n'))
    day = int(input('day:\n'))
    month_day = 0
    for i in range(1,month):
        if i % 2 == 0: 
            if i == 2:
                if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
                    month_day = month_day + 29
                else:
                    month_day = month_day + 28
            else:
                month_day = month_day + 30
        else:
            month_day = month_day + 31
    print("it is th %dth day "% (month_day + day))

if __name__ == "__main__":
    main()