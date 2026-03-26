'''Add few names, one name in each row, in “name.txt file”. 
a. Count no of names 
b. Count all names starting with vowel 
c. Find longest name'''

file= open("name.txt","r")
names=file.readlines()
file.close()

count=len(names)
print("total number of names",count)

vowel_count=0
for name in names:
    name = name.strip()      # remove newline
    if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print("Names starting with vowel =", vowel_count)

# c) Find the longest name
longest_name = ""

for name in names:
    name = name.strip()
    if len(name) > len(longest_name):
        longest_name = name

print("Longest name =", longest_name)