# Write a program to find if given number is prime number or not. 
n= int(input("Enter the number:"))

for i in range(2,n):
    if(n%i==0):
        print("Number is not prime.")
        break
else :
    print("number is prime.")