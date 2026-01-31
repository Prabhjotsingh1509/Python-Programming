# wap to in recursive function to calculate the sum of first n natural number?

n= int(input("Enter the number:"))

def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

s= sum(n)
print(f"The sum of first {n} natural number: {s}")