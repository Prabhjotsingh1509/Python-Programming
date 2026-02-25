'''Write a Python function that takes a positive integer and returns the sum of the cube of 
all the positive integers smaller than the specified number.'''
def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total
num = 5
result = sum_of_cubes(num)
print("Sum of cubes:", result)