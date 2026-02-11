# Check whether given number is palindrome or not. 
n= int(input("Enter the number:"))
d=0
temp =n
while(temp>0):
    r=temp%10
    d=(d*10)+r
    temp=temp//10

if(d== n):
    print("Number is palindrome.")
else:
    print("Number is not palindrome.")