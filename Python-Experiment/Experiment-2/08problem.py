'''Print the grade sheet of a student for the given range of cgpa. Scan marks of five 
subjects and calculate the percentage. 
CGPA=percentage/10 
CGPA range: 
0 to 3.4 -> F 
3.5 to 5.0->C+ 
5.1 to 6->B 
6.1 to 7-> B+ 
7.1 to 8-> A
8.1 to 9->A+ 
9.1 to 10-> O (Outstanding) 
Sample Gradesheet 
Name: Rohit Sharma 
Roll Number: R17234512   SAPID: 50005673 
Sem: 1      Course: B.Tech. CSE AI&ML
 
Subject name: Marks 
PDS:   70 
Python:  80 
Chemistry:  90 
English:  60 
Physics:  50 
Percentage: 70% 
CGPA:7.0 
Grade:   '''

name=input("Enter the Name:")
rollno=int(input("Enter the roll number"))
sapid=int(input("Enter the SAPID"))
sem=int(input("Enter the sem"))
course=input("Enter the course")

print("Subject name: Marks")
pds=int(input("PDS:"))
python=int(input("Python:"))
chemistry=int(input("Chemistry:"))
english=int(input("English:"))
physics=int(input("Physics:"))

percentage=(pds+python+chemistry+english+physics)/5
cgpa=percentage/10

if(cgpa>=0 and cgpa<=3.4):
    grade="F"
elif(cgpa>=3.5 and cgpa<=5):
    grade="C+"
elif(cgpa>=5.1 and cgpa<=6):
    grade="B"
elif(cgpa>=6.1 and cgpa<=7):
    grade="B+"
elif(cgpa>=7.1 and cgpa<=8):
    grade="A"
elif(cgpa>=8.1 and cgpa<=9):
    grade="A+"
elif(cgpa>=9.1 and cgpa<=10):
    grade="O"
else:
    grade="Invalid"

print("Name:",name)
print("Roll Number:",rollno)
print("SAPID:",sapid)
print("Sem:",sem)
print("Course:",course)
print(f"Percentage:{percentage}%")
print("CGPA:",cgpa)
print("Grade:",grade)
