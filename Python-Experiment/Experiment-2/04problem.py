# Find the greatest among three numbers assuming no two values are same.  
a=int(input("Enter the first Number:"))
b=int(input("Enter the second Number:"))
c=int(input("Enter the third Number:"))

if(a>b and a>c):
    print("The greatest number is :",a)
elif(b>a and b>c):
    print("The greatest number is :",b)
else:
    print("The greatest number is :",c)