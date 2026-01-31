# Find whether a given year is a leap year or not. 
n= int(input("Enter the number:"))
if((n%4==0 and n%100!=0) or n%400==0):
    print("The year is leap year")
else:
    print("The year is not leap year")