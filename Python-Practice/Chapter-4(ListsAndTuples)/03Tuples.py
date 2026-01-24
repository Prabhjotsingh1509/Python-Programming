a=(1,45,324,"Rohan","shivam")
# Tuple is immutable
# a[0] =7 is wrong as it cannnot be edited.

# Functions Of Tuple
# count:
tuple1=(1,2,3)
tuple2=(4,5,6)
# Repetition:
my_tuple=(1,2,3)
repeated=my_tuple*3
print(repeated)
# Membership:
print(2 in my_tuple)
# Length:
print(len(my_tuple))
# Unpacking:
a,b,c=my_tuple
print(a,b,c) #Output:1 2 3