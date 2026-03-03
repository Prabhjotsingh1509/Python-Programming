#Create a tuple to store n numeric values and find average of all values. 

n = int(input("Enter number of values: "))

values = tuple(float(input("Enter value: ")) for _ in range(n))

average = sum(values) / n if n > 0 else 0

print("Tuple:", values)
print("Average:", average)