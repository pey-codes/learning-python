contacts = []
contact = {"name": "Peyshie",
           "phone": "0723456789"}
contacts.append(contact)
print(contacts)

while True:
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = {"name": name,
           "phone": phone}
    contacts.append(contact)
    again = input("Add another contact? (yes/no): ")
    if again.lower() == "no":
        break

print("\n--- MY CONTACTS ---")

for contact in contacts:
        print("name", contact["name"])
        print("phone", contact["phone"])

search_name = input("\nEnter name to search: ")

found = False
for contact in contacts:
     if contact["name"].lower() == search_name.lower():
          print("contact found!")
          print("name:", contact["name"])
          print("phone:", contact["phone"])
          found = True
if found == False:
     print("contact not found.")