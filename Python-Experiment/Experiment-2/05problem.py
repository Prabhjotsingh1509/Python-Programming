# Check whether the quadratic equation has real roots or imaginary roots. Display the roots

# equation is ax^2 + bx + c

a=int(input("Coefficient of x^2:"))
if(a == 0):
    print("Wrong value of coefficient of x^2")
    quit()#exit()
b=int(input("Coefficient of x:"))
c=int(input("Constant term"))

d= b**2 -4*a*c
if(d>= 0 ):
    print("The roots are real")
    x1= (-b + (d)**0.5)/2*a
    x2= (-b - (d)**0.5)/2*a

    print("the roots of the equation are:",x1,x2)
else:
    print("The roots are imaginary")