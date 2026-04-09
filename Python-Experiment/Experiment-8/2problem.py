from tkinter import *

# Functions for operations
def add():
    result.set(int(num1.get()) + int(num2.get()))

def subtract():
    result.set(int(num1.get()) - int(num2.get()))

def multiply():
    result.set(int(num1.get()) * int(num2.get()))

def divide():
    if int(num2.get()) != 0:
        result.set(int(num1.get()) / int(num2.get()))
    else:
        result.set("Error")

# Main window
root = Tk()
root.title("Basic Calculator")
root.geometry("300x250")

# Variables
num1 = StringVar()
num2 = StringVar()
result = StringVar()

# Labels and Entry boxes
Label(root, text="Enter First Number").pack()
Entry(root, textvariable=num1).pack()

Label(root, text="Enter Second Number").pack()
Entry(root, textvariable=num2).pack()

# Buttons
Button(root, text="Add", command=add).pack(pady=5)
Button(root, text="Subtract", command=subtract).pack(pady=5)
Button(root, text="Multiply", command=multiply).pack(pady=5)
Button(root, text="Divide", command=divide).pack(pady=5)

# Result
Label(root, text="Result").pack()
Entry(root, textvariable=result).pack()

root.mainloop()