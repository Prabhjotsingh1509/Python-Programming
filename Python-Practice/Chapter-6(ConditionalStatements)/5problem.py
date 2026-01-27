# Wap to findout whether a student is passed or failed it requires total 40% at least 33% in each subject to pass Assume 3 subjects
a1= int(input("Enter 1st number:"))
a2= int(input("Enter 2nd number:"))
a3= int(input("Enter 3rd number:"))
per = ((a1+a2+a3)/300)*100

if(a1>33 and a2>33 and a3>33 and per>40):
    print("pass")
else:
    print("Fail")