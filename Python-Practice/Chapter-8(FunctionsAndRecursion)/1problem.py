# Wap using functions to find the greatest of three numbers?
a=10
b=20
c=74
# Defining a function Syntax
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
# Calling Function
gr=greatest(a,b,c)
print("The greatest number is :",gr)