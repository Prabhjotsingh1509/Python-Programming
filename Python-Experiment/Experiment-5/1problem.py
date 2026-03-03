# Scan n values in range 0-3 and print the number of times each value has occurred. 
n = int(input("Enter the number"))

count = [0, 0, 0, 0]  # Index represents the number (0-3)

for _ in range(n):
    num = int(input())
    if 0 <= num <= 3:
        count[num] += 1

for i in range(4):
    print(f"{i} occurred {count[i]} times")
    