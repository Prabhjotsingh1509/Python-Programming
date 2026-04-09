# Design a GUI for student registration for a course and store these details in a database. 
# Use Tkinter for UI, SQLite/MySQL for database storage. 
import tkinter as tk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT,
    phone TEXT
)
""")
conn.commit()

def register():
    name = name_var.get()
    email = email_var.get()
    course = course_var.get()
    phone = phone_var.get()

    if name == "" or email == "" or course == "" or phone == "":
        messagebox.showwarning("Warning", "All fields are required")
        return

    cursor.execute("INSERT INTO students(name,email,course,phone) VALUES(?,?,?,?)",
                   (name, email, course, phone))
    conn.commit()

    messagebox.showinfo("Success", "Student Registered Successfully")

    name_var.set("")
    email_var.set("")
    course_var.set("")
    phone_var.set("")


root = tk.Tk()
root.title("Student Registration Form")
root.geometry("350x300")

name_var = tk.StringVar()
email_var = tk.StringVar()
course_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(root, text="Student Name").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack()

tk.Label(root, text="Course").pack()
tk.Entry(root, textvariable=course_var).pack()

tk.Label(root, text="Phone").pack()
tk.Entry(root, textvariable=phone_var).pack()

# Register Button
tk.Button(root, text="Register", command=register).pack(pady=10)

root.mainloop()