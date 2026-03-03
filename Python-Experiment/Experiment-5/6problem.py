'''Create a contact book where users can store, search, update, and delete contacts. Use 
dictionary for storing contacts.'''
# Contact Book using Dictionary

contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Contact found!")
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def display_contacts():
    if not contacts:
        print("Contact book is empty!")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

# Menu
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")