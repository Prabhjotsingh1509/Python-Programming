'''Create multiple suitable exceptions for a file handling program.'''

try:
    file = open("student.txt", "r")
    
    data = file.read()
    print("File Data:")
    print(data)

    file.close()

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: Permission denied to open the file.")

except IsADirectoryError:
    print("Error: You entered a directory instead of a file.")

except IOError:
    print("Error: Problem while reading the file.")

except Exception as e:
    print("Unexpected Error:", e)