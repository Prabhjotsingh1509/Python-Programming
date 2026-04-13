# Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by               
# taking inputs from the user and display details of all students. 
class Student:
    def __init__(self):
        self.name = ""
        self.sap_id = 0
        self.marks = [0, 0, 0]  # phy, chem, maths

    def input(self):
        self.name = input("Enter Name: ")
        self.sap_id = int(input("Enter SAP ID: "))
        
        print("Enter marks (Physics, Chemistry, Maths):")
        for i in range(3):
            self.marks[i] = float(input())

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.marks[0])
        print("Chemistry:", self.marks[1])
        print("Maths:", self.marks[2])


# Create 3 objects
students = []

for i in range(3):
    print(f"\nStudent {i+1}:")
    s = Student()
    s.input()
    students.append(s)

# Display all students
print("\nDisplaying all student details:")
for s in students:
    s.display()