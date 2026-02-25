'''Write functions to explain mentioned concepts: 
a. Keyword argument 
b. Default argument 
c. Variable length argument '''
def demonstrate_arguments(name, age=18, *hobbies, **details):
    print("Name:", name)
    print("Age:", age)

    print("Hobbies:")
    for hobby in hobbies:
        print("-", hobby)
    print("Other Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

demonstrate_arguments(
    name="Alice",          
    age=25,                
    city="New York",       
    profession="Engineer"
)