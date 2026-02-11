# Count and print all numbers divisible by 5 or 7 between 1 to 100. 
print("The number which is divisible by 5 or 7 is :")

for i in range(1,101):
    if(i%7==0 or i%5==0):
        print(i,"\t",end="")

