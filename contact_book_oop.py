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





book = ContactBook()
book.add("Peyshie", "0789654321")
book.add("Amina", "0767895423")
book.add("Griffin", "0762341785")
book.show_all()
book.search("amina")
book.search("Kingsley")

print(len(book.contacts))
print(book.contacts[0].name)