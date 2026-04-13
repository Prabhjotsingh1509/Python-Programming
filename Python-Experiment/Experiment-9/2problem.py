# Add constructor in the above class to initialize student details of n students and implement 
# following methods: 
# a) Display() student details 
# b) Find Marks_percentage() of each student 
# c)  Display result() [Note: if marks in each subject >40% than Pass else Fail] 
# d) Write a Function to find average of the class. 
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = [phy, chem, maths]

    # a) Display student details
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.marks[0])
        print("Chemistry:", self.marks[1])
        print("Maths:", self.marks[2])

    # b) Calculate percentage
    def marks_percentage(self):
        total = sum(self.marks)
        percentage = total / 3
        return percentage

    # c) Display result (Pass/Fail)
    def display_result(self):
        if all(m >= 40 for m in self.marks):
            print("Result: PASS")
        else:
            print("Result: FAIL")


# d) Function to find class average
def class_average(students):
    total = 0
    for s in students:
        total += s.marks_percentage()
    return total / len(students)


# ===== MAIN PROGRAM =====
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    sap_id = int(input("SAP ID: "))
    phy = float(input("Physics Marks: "))
    chem = float(input("Chemistry Marks: "))
    maths = float(input("Maths Marks: "))

    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)

# Display all students
for s in students:
    s.display()
    print("Percentage:", s.marks_percentage())
    s.display_result()

# Class average
avg = class_average(students)
print("\nClass Average Percentage:", avg)