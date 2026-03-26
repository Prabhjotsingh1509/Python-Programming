'''Input two values from user where the first line contains N, the number of test cases. The  next N lines contain the space separated values of a and b.Perform integer division and print a/b.Handle exception in case of ZeroDivisionError or ValueError.Sample input 1 0 2 $ 3 1 Sample Output:
Error Code: integer division or modulo by zero  
Error Code: invalid literal for int() with base 10: '$' 3'''

n= int(input("The number of test cases:"))

for _ in range(n):
    try:
        a=int(input("Enter the number:"))
        b=int(input("Enter the number:"))
        c=a/b
        print(c)
    except ZeroDivisionError:
        print("Error code")
    except ValueError:
        print("invalid literals")