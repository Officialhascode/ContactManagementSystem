# 📇 Contact Management System

## Description
A Python-based command-line application for managing personal contacts with persistent JSON storage.

## Features
- Add new contacts (name, phone, email)
- View all contacts
- Edit existing contacts
- Delete contacts
- Automatically saves to `contacts.json`
- Loads previous contacts on startup

## Program Preview
```plaintext
--- Contact Management System ---
1. Add New Contact
2. View Contacts
3. Edit Contact
4. Delete Contact
5. Save Contacts to File
6. Exit

Enter your choice (1-6): 2

--- Contact List ---
Name: John Doe
Phone: 555-1234
Email: john@example.com

Name: Jane Smith
Phone: 555-5678
Email: jane@work.com
--- End of List ---
```

## Usage
1. Adding a Contact:
   - Select option 1 from the menu
   - Enter name, phone number, and email
   - Duplicate names are prevented
2. Editing a Contact:
   - Select option 3
   - Choose contact to edit
   - Modify fields (leave blank to keep current value)
3. Data Persistence:
   - Contacts automatically save to contacts.json
   - File is created in the same directory as the script

## Data Structure

Contacts are stored in JSON format:
```contacts.json
{
  "John Doe": {
    "phone": "555-1234",
    "email": "john@example.com"
  },
  "Jane Smith": {
    "phone": "555-5678",
    "email": "jane@work.com"
  }
}
