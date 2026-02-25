'''Write a recursive function to print Fibonacci series upto n terms. '''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

term =int(input("Enter the number:"))
print("Fibonacci Series:")
print_fibonacci(term)