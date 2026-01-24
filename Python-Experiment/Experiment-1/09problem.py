# Write a program to convert given seconds into hours, minutes and remaining seconds. 

sec=int(input("Enter the time in sec"))
hours=sec//3600
min=(sec%3600)//60
remsec=(sec%3600)%60
print(hours,":",min,":",remsec)