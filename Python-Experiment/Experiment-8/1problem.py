#  Create a simple Tkinter window with a title and fixed size.

from tkinter import *

# Create main window
root = Tk()

# Set window title
root.title("My First Tkinter Window")

# Set fixed window size (width x height)
root.geometry("400x300")

# Prevent resizing
root.resizable(False, False)

# Run the window
root.mainloop()