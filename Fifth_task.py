class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if (
                search_term.lower() in contact.name.lower() or
                search_term in contact.phone_number
            ):
                found_contacts.append(contact)

        if not found_contacts:
            print("No contacts found.")
        else:
            print("Found Contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[i] = new_contact
                print("Contact updated successfully!")
                return
        print(f"No contact found with the name {old_name}.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted successfully!")
                return
        print(f"No contact found with the name {name}.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            updated_contact = Contact(name, phone_number, email, address)
            contact_manager.update_contact(old_name, updated_contact)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
