contacts = []
try:
    with open("contacts.txt", "r") as file:
         for line in file:
             name, phone = line.strip().split(",")
             contacts.append({"name": name, "phone": phone})
except FileNotFoundError:
    pass
    
while True:
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = {"name": name,
           "phone": phone}
    contacts.append(contact)
    again = input("Add another contact? (yes/no): ")
    if again.lower() == "no":
        break
with open("contacts.txt", "w") as file:
     for contact in contacts:
          file.write(contact["name"] + "," + contact["phone"] + "\n")

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