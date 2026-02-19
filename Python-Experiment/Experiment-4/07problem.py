'''Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
a) Fruits which are in both sets s1 and s2 
b) Fruits only in s1 but not in s2 
c) Count of all fruits from s1 and s2 '''


n= int(input("Enter the value of n:"))
s1=set()
s2=set()
for i in range(0,n):
    s1.add(input("Enter the fruit name:"))
for i in range(0,n):
    s2.add(input("Enter the fruit name:"))

print("Common Fruits in both sets",s1.intersection(s2))
print("Fuit which are only in s1 but not in s2:",s1.difference(s2))
count=s1.union(s2)
print("Count all Fruits from s1and s2",len(count))



