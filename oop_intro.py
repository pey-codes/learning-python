class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
    def call(self):
        print("Calling:", self.name)

c1 = Contact("Peyshie", "0723456677")
c2 = Contact("Amina", "0111254376")
c3 = Contact("Kenneth", "0700367534")

c1.show()
c2.show()
c3.show()
c1.call()
c2.call()
c3.call()