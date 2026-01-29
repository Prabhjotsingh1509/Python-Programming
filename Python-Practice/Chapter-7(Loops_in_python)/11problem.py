'''
***
* *
***
'''
n=int(input("Enter the number:"))

for i in range(1,n+1):
    if(n==i or i==1):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("\n")