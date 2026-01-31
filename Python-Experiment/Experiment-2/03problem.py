# Find the greatest among the two numbers. If numbers are equal than print “numbers are equal”. 

a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))

if(a>b):
    print("The greatest number is :",a)
elif(b>a):
    print("The gratest number is :",b)
else:
    print("Both a and b are equal")