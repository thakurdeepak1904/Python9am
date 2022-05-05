month1 = [1, 3, 5, 6, 8, 10, 12]
month2 = [4, 7, 9, 11]
while True:
    year = int(input("Please enter the year of the event:"))
    if year > 1980:
        print("Valid Year")
        break
    else:
        print("Not a valid year")

while True:
    month = int(input("Please enter the months of the event, e.g. 1-12:"))
    if month >= 1 and month <= 12:
        print("valid month")
        break
    else:
        print("Not a valid month")

while True:
    day = int(input("Please enter the day of the event, e.g. 1-31:"))
    if month==2 and year%4!=0:
        if day>=1 and day<=28:
            print("The month is feb and is not a leap year")
            break
        else:
            print("Enter a valid date")
    elif month==2 and year%4==0:
        if day>=1 and day<=29:
            print("The month is feb and is a leap year")
            break
        else:
            print("Enter a valid date")
    elif month in month1:
        if day>=1 and day<=31:
            print("The month is Jan, Mar, May,Jul, Aug, Oct, Dec")
            break
        else:
            print("Invalid date")
    else:
        if month in month2:
            if day>=1 and day<=30:
                print("The month is Apr, Jun, Sept, Nov")
                break
            else:
                print("Invalid date")