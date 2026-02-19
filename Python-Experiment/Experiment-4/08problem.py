'''Take two sets and apply various set operations on them : 
S1 = {Red ,yellow, orange , blue } 
S2 = {violet, blue , purple}'''
s1 = {"Red" ,"yellow", "orange" , "blue" }
s2 = {"violet", "blue" , "purple"}

# union of two sets
print(s1.union(s2))

# Intersection of two sets
print(s1.intersection(s2))

# difference
print(s2 - s1)