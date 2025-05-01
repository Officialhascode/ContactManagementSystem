import json
import os

class ContactManager:
    def __init__(self):
        # Get the directory where the script is located
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.contacts_file = os.path.join(self.script_dir, 'contacts.json')
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON file in the script directory"""
        if os.path.exists(self.contacts_file):
            with open(self.contacts_file, 'r') as file:
                self.contacts = json.load(file)
            print(f"Contacts loaded from {self.contacts_file}")
        else:
            print("No existing contact file found. Starting with empty contact list.")

    def save_contacts(self):
        """Save contacts to JSON file in the script directory"""
        with open(self.contacts_file, 'w') as file:
            json.dump(self.contacts, file, indent=4)
        print(f"Contacts saved to {self.contacts_file}")

    def add_contact(self):
        """Add a new contact"""
        print("\n--- Add New Contact ---")
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()

        if name in self.contacts:
            print("A contact with this name already exists!")
            return

        self.contacts[name] = {
            'phone': phone,
            'email': email
        }
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        """View all contacts"""
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts available.")
            return

        for name, info in self.contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        print("\n--- End of List ---")

    def edit_contact(self):
        """Edit an existing contact"""
        print("\n--- Edit Contact ---")
        name = input("Enter name of contact to edit: ").strip()

        if name not in self.contacts:
            print("Contact not found!")
            return

        print(f"\nCurrent details for {name}:")
        print(f"Phone: {self.contacts[name]['phone']}")
        print(f"Email: {self.contacts[name]['email']}")

        print("\nEnter new details (leave blank to keep current value):")
        phone = input(f"New phone [{self.contacts[name]['phone']}]: ").strip()
        email = input(f"New email [{self.contacts[name]['email']}]: ").strip()

        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email

        print(f"Contact '{name}' updated successfully!")

    def delete_contact(self):
        """Delete a contact"""
        print("\n--- Delete Contact ---")
        name = input("Enter name of contact to delete: ").strip()

        if name not in self.contacts:
            print("Contact not found!")
            return

        del self.contacts[name]
        print(f"Contact '{name}' deleted successfully!")

    def menu(self):
        """Display the main menu"""
        while True:
            print("\n--- Contact Management System ---")
            print("1. Add New Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Save Contacts to File")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.edit_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.save_contacts()
            elif choice == '6':
                self.save_contacts()  # Auto-save before exiting
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()