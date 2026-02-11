# Find whether the given number is Armstrong number. 

n=int(input("check whether number is :"))

temp =n
d=0
while(temp>0):
    r=temp%10
    d=d+(r*r*r)
    temp=temp//10

if(d== n):
    print("Number is amstrong.")
else:
    print("Number is not amstrong.")