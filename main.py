from src.linkedlist import ContactList

cl = ContactList()
print("-" * 15, "Contact List Manager", "-" * 15)
print(
    "  1. Add Contact\n"
    + "  2. Delete Contact\n"
    + "  3. Search Contact\n"
    + "  4. List All Contacts\n"
    + "  5. Exit\n"
)

while True:
    try:
        choice = int(input("Enter your choice (a number): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if choice == 1:
        print("-" * 10, "Add a Contact", "-" * 10)
        print("Fill in the fields (* is required. Press enter to skip optional fields)")
        name = input("Name: ")
        phone = input("Phone Number: ")
        other_phone = input("Other Phone Number: ")
        email = input("Email: ")
        cl.add_contact(name, phone, other_phone, email)
        new_contact = cl._get_contact(name, phone)
        if new_contact:
            print(f"{new_contact.name} is created successfully\n")
        else:
            raise "Error creating contact"
        # print(cl.search_contacts(name), "\n")

    if choice == 5:
        print("Closing")
        exit()
