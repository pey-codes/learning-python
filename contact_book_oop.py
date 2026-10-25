class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print("Name:", self.name)
        print("Phone:", self.phone)

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone):
        self.contacts.append(Contact(name, phone))

    def show_all(self):
        for contact in self.contacts:
            contact.show()

    def search(self, search_name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                print("Contact found!")
                contact.show()
                found = True
            if not found:
                print("Contact not found.")

    def delete(self, delete_name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == delete_name.lower():
                self.contacts.remove(contact)
                print("Contact deleted.")
                found = True
                break
        if not found:
            print("Contact not found.")
        
    def save(self):
        with open("contacts.txt", "w")as file:
            for contact in self.contacts:
                file.write(contact.name + "," + contact.phone + "\n")

    def load(self):
        try:
            with open("contacts.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        self.add(parts[0], parts[1])
        except FileNotFoundError:
            pass




book = ContactBook()
book.load()

while True:
    print("\n1. Add contact")
    print("2. Show all")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = input ("Choose an option: ") 

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        book.add(name, phone)
        book.save()
    elif choice == "2":
        book.show_all()
    elif choice == "3":
        book.search(input("Enter name to search: "))
    elif choice == "4":
        book.delete(input("Enter name to delete: "))
        book.save()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")