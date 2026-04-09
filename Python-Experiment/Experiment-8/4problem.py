import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")
conn.commit()

# Load tasks
def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, task FROM tasks")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, row)

# Add task
def add_task():
    task = entry.get()

    if task == "":
        messagebox.showwarning("Warning","Enter a task")
        return

    cursor.execute("INSERT INTO tasks(task) VALUES(?)",(task,))
    conn.commit()
    entry.delete(0, tk.END)
    load_tasks()

# Delete task
def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning","Select a task")
        return

    task = listbox.get(selected)
    task_id = task[0]

    cursor.execute("DELETE FROM tasks WHERE id=?",(task_id,))
    conn.commit()
    load_tasks()

# Edit task
def edit_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning","Select a task")
        return

    new_task = entry.get()

    if new_task == "":
        messagebox.showwarning("Warning","Enter new task")
        return

    task = listbox.get(selected)
    task_id = task[0]

    cursor.execute("UPDATE tasks SET task=? WHERE id=?",(new_task,task_id))
    conn.commit()

    entry.delete(0, tk.END)
    load_tasks()

# GUI
root = tk.Tk()
root.title("Task Manager")
root.geometry("350x350")

entry = tk.Entry(root,width=30)
entry.pack(pady=10)

tk.Button(root,text="Add Task",command=add_task).pack(pady=5)
tk.Button(root,text="Edit Task",command=edit_task).pack(pady=5)
tk.Button(root,text="Delete Task",command=delete_task).pack(pady=5)

listbox = tk.Listbox(root,width=40,height=10)
listbox.pack(pady=10)

load_tasks()

root.mainloop()