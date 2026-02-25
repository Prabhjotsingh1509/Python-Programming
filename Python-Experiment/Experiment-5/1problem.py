'''Write a Python function to find the maximum and minimum numbers from a sequence of numbers.'''
def find_max_min(sequence):
    maximum = minmum = sequence[0]

    for num in sequence:
        if num > maximum:
            maximum = num
        if num < minmum:
            minmum = num

    return maximum, minmum

numbers = [10, 6, 8, 90, 12, 56]
result = find_max_min(numbers)
print("Maximum and Minimum:", result)