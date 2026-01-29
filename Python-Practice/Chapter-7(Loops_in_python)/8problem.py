n= int(input("Enter the number:"))

fact = 1
# while(i<=n):
#     fact*=i
#     i+=1

for i in range(1,n+1):
    fact*=i
    i+=1
print("factorial of",n,"is:",fact)