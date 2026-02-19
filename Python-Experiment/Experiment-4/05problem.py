'''Given a string containing both upper and lower case alphabets. Write a Python program 
to count the number of occurrences of each alphabet (case insensitive) and display the 
same. 
Sample Input 
ABaBCbGc 
Sample Output 
2A 
3B 
2C 
1G'''
s=input("Enter the string:")
count ={}
for i in s:
    if i.isalpha():
        cap=i.upper()
        count[cap]=count.get(cap,0)+1

for key in count.keys():
    print(f"{count[key]}{key}")
