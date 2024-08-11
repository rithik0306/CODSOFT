contacts = []

def add_contact():
    """Add a new contact to the contact list."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Display the list of all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    """Search for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]

    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No contacts found.")

def update_contact():
    """Update the details of an existing contact."""
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("Leave the field empty if you don't want to change the current value.")
            new_phone = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
            new_email = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            new_address = input(f"Enter new address (current: {contact['address']}): ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            print(f"Contact '{name}' updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    """Delete a contact from the contact list."""
    name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print(f"Contact '{name}' deleted successfully!")

def main():
    while True:
        print("\nContact List Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
