while True:
    event_year = int(input("Enter the Year of event:"))
    if event_year > 1980:
        print("Valid Year")
        break
    else:
        print("Enter a valid year")

while True:
    event_month = int(input("Enter the month of event:"))
    if event_month >= 1 and event_month <= 12:
        print("Valid month")
        break
    else:
        print("Enter a valid month")

thirtydays = [4, 6, 9, 11]
thirtyonedays = [1, 3, 5, 7, 8, 10, 12]
while True:
    event_day = int(input("Enter a day of event:"))
    if event_year % 4 == 0 and event_year % 400 == 0:
        if event_month in thirtydays:
            if event_day >= 1 and event_day <= 30:
                print("It is a leap year and month is apr, june ,sept and nov")
                break
            else:
                print("enter a valid day")
        elif event_month in thirtyonedays:
            if event_day >= 1 and event_day <= 31:
                print("It is a leap year and the month is Jan, mar,may,july,aug,oct and Dec")
                break
            else:
                print("Enter a valid day")
        else:
            if event_day >= 1 and event_day <= 29:
                print("It is a leap year and is a month of feb")
                break
            else:
                print("Enter a valid day")
    else:
        if event_month in thirtydays:
            if event_day >= 1 and event_day <= 30:
                print("It is not a leap year and the month is apr, june ,sept and nov")
                break
            else:
                print("Enter a valid day")
        elif event_month in thirtyonedays:
            if event_day >= 1 and event_day <= 31:
                print("It is not a leap year and the month is Jan, mar,may,july,aug,oct and Dec")
                break
            else:
                print("Enter a valid day")
        else:
            if event_day >= 1 and event_day <= 28:
                print("It is not a leap year and is a month of feb")
                break
            else:
                print("Enter a valid day")
