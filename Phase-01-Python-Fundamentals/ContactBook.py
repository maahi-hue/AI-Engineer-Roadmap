#empty dictionary
contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create new contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        if name in contacts:
            print(f"Contact with {name} already exists!")
        else:
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            mobile = input("Enter your mobile: ")
            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            print(f"Contact with {name} created!")

    elif choice == 2:
        name = input("Enter contact name to view: ")
        if name in contacts:
         contact = contacts[name]
         print(f"Name: {name}, Age:{age}, Mobile Number:{mobile}")
        else:
            print(f"Contact with {name} does not exist!")
    elif choice == 3:
        name = input("Enter name to update contact: ")
        if name in contacts:
            age = int(input("Enter your updated age: "))
            email = input("Enter your updated email: ")
            mobile = input("Enter your updated mobile: ")
            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
        else:
            print(f"Contact with {name} does not exist!")
    elif choice == 4:
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact with {name} deleted!")
        else:
            print(f"Contact with {name} does not exist!")
    elif choice == 5:
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
           if search_name.lower() in name.lower():
               print(f"Found - Name: {name}, Age: {age}, Email: {email}")
               found = True
           if not found:
               print("No contact found with this name!")
    elif choice == 6:
        print(f"Total contacts in your book: {len(contacts)}")
    elif choice == 7:
        print("Goodbye...Closing the program")
        break

    else:
        print("Invalid choice!")