'''Print the table for a given number:  
             5 * 1 = 5 
             5 * 2 = 10……….. '''

t= int(input("Number whom table you want:"))

i=1
while(i<11):
    print(f"{t} X {i} = {i*t}")
    i=i+1