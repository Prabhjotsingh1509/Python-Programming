#  4. Create a class to implement method Overriding. 
# Parent Class
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

    def show_role(self):
        print("Role: Student")


# Child Class (Overriding methods)
class GraduateStudent(Student):
    def __init__(self, name, degree):
        super().__init__(name)   # call parent constructor
        self.degree = degree

    # Method Overriding
    def show_role(self):
        print("Role: Graduate Student")

    # Overriding display method
    def display(self):
        super().display()   # call parent display
        print("Degree:", self.degree)


# Main Program
print("Enter Student Details:")
name = input("Enter Name: ")
degree = input("Enter Degree: ")

# Create object of child class
obj = GraduateStudent(name, degree)

print("\n--- Output ---")
obj.display()        # calls overridden display()
obj.show_role()      # calls overridden method