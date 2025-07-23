# 👋 Welcome to the Simple Contact Book!
# This program allows you to add, view, and search contacts.

# 📚 Dictionary to store contact details
contacts = {}

# 📦 Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    
    # Check if contact already exists
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = phone
        print(f"✅ Contact '{name}' added successfully!")

# 📖 Function to display all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n📒 Contact List:")
        for name, phone in contacts.items():
            print(f"👤 {name}: 📞 {phone}")

# 🔍 Function to search a contact by name
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"🔎 Found: {name} - 📞 {contacts[name]}")
    else:
        print("❌ Contact not found.")

# 🚪 Main loop to run the contact book
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")
