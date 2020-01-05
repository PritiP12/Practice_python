def leap_years(year):
    if (year%400)==0 or (year%100!=0) and (year%4==0):
        print(year," is leap year")
    else:
        print(year," is not leap year")
leap_years(1995)
leap_years(2020)