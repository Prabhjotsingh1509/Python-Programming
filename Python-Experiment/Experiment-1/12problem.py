# Write a program to print truth table for bitwise operators (&, | and ^ operators) 

print("A B\tA&B\tA|B\tA^B")
print("-------------------------")

for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, "\t", A & B, "\t", A | B, "\t", A ^ B)