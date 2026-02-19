# Wap to count and display the number of capital letters in a given string.
s = input("Enter the string:")

count =0

for i in s:
    if('A'<=i and i<='Z'):
        count=count+1
        print(i)

print("Number of upper case letter:",count)