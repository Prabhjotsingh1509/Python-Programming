import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")
conn.commit()

# Signup function
def signup():
    user = username.get()
    pwd = password.get()

    if user == "" or pwd == "":
        messagebox.showwarning("Warning","Fields cannot be empty")
        return

    cursor.execute("INSERT INTO users VALUES(?,?)",(user,pwd))
    conn.commit()

    messagebox.showinfo("Success","Signup Successful")

# Login function
def login():
    user = username.get()
    pwd = password.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(user,pwd))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success","Login Successful")
    else:
        messagebox.showerror("Error","Invalid Username or Password")

# GUI
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

username = tk.StringVar()
password = tk.StringVar()

tk.Label(root,text="Username").pack()
tk.Entry(root,textvariable=username).pack()

tk.Label(root,text="Password").pack()
tk.Entry(root,textvariable=password,show="*").pack()

tk.Button(root,text="Signup",command=signup).pack(pady=5)
tk.Button(root,text="Login",command=login).pack(pady=5)

root.mainloop()