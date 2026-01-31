# WAP to convert using Function to convert Celsius to farhenhiet?

def f_toc(f):
    return 5*(f-32)/9


f= int(input("Enter temp. in F:"))
c= f_toc(f)
print(f"temp in celsius = {c}")
