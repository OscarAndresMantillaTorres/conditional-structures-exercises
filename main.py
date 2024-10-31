def isleapYear(year):
    
    if year >= 1582:
        
        if (yeis_leap_yearar % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    else:
        
        return year % 4 == 0


year = int(input("Enter a year: "))
if isleapYear(year):
    print(f"The year {year} It's a leap year.")
else:
    print(f"The year {year} It is not a leap year.")
