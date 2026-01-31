# Check whether the given number is divisible by 3 and 5 both.

n=int(input("Enter the number:"))

if n%3==0 and n%5==0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")