'''
*******
 *****
  ***
   *
'''
n= int(input("Enter the number:"))

for i in range(1,n+1):
   print(" "*(i-1),end="")
   print("*"*(2*(n-i)+1),end="")
   print("\n")
