# Count total number of vowels in a given string.

str= input("Enter the string:")
count =0
for i in str:
    if i.lower() in 'aeiou':
        count=count+1
    
print("Total number of vowels:",count)