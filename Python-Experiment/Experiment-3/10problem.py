'''Write a program to print the following pattern 
1234554321 
1234* 4321 
123* * 321 
12* * * 21 
1 * * * *1 '''
n= int(input("Enter the number of elements you want "))

for i in range(0,n+1):
    for j in range(1,n-i+1):
        print(j,end="")
    if(i<n):
        print("* "*i,end="")
    for k in range(n-i,0,-1):
        print(k,end="")
    print("\n") 