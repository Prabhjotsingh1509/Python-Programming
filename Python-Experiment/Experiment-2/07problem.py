'''Write a program which takes any date as input and display next date of the calendar 
e.g. 
I/P: day=20 month=9 year=2005  
O/P: day=21 month=9 year 2005 '''

day = int(input("Enter day: "))
if(day<1 or day>31):
    print("Invalid day")
    quit()  
month = int(input("Enter month: "))
if(month<1 or month>12):
    print("Invalid month")
    quit()
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap = True
else:
    leap = False

if month == 2:
    if leap:
        days_in_month = 29
    else:
        days_in_month = 28
elif month in (4, 6, 9, 11):
    days_in_month = 30
else:
    days_in_month = 31
day += 1

if day > days_in_month:
    day = 1
    month += 1
if month > 12:
    month = 1
    year += 1

print(f"Next Date: day={day} month={month} year={year}")
