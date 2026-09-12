"""
contacts.py

Mini Project: Contact Book Manager
Covers: dictionaries | nested dictionaries | menu-driven program
Note: in-memory only — contacts reset each time the program is run.
"""

contacts = {}  # name -> {"phone": str, "email": str}


def add_contact(name, phone, email):
    if name in contacts:
        print(f"'{name}' already exists. Use update instead, or delete and re-add.")
        return
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")


def view_all_contacts():
    if len(contacts) == 0:
        print("No contacts saved yet.")
        return

    print("\nAll Contacts:")
    for name, details in contacts.items():
        print(f"  {name} - Phone: {details['phone']}, Email: {details['email']}")


def search_contact(name):
    if name in contacts:
        details = contacts[name]
        print(f"{name} - Phone: {details['phone']}, Email: {details['email']}")
    else:
        print(f"No contact found with the name '{name}'.")


def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found with the name '{name}'.")


def display_menu():
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)

        elif choice == "2":
            view_all_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == "5":
            print("Goodbye! (Note: contacts are not saved after exit)")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
