'''Write a lambda function to find volume of cone. '''


import math

volume_cone = lambda r, h: (1/3) * math.pi * r**2 * h

radius = int(input("Enter the radius:")) 
height = int(input("Enter the height"))

print("Volume of Cone:", volume_cone(radius, height))