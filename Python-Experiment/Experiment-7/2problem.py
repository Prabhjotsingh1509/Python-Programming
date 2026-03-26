'''Store integers in a file. 
a. Find the max number 
b. Find average of all numbers 
c. Count number of numbers greater than 100 '''

file= open("numbers.txt","r")
numbers=file.readlines()
file.close()

nums=[]

for n in numbers:
    nums.append(int(n.strip()))

max_num= max(nums)
print("The maximum number is :",max_num)

average=sum(nums)/len(nums)
print("The average of numbers :",average)

count = 0
for n in nums:
    if n > 100:
        count += 1

print("Numbers greater than 100 =", count)

