'''Write a program to check whether all the values in a dictionary are same or not using 
lambda function.'''


check_values = lambda d: len(set(d.values())) == 1
dict1 = {'a': 10, 'b': 10, 'c': 10}
dict2 = {'a': 10, 'b': 20, 'c': 10}
print("Dictionary 1 values are same:", check_values(dict1))
print("Dictionary 2 values are same:", check_values(dict2))