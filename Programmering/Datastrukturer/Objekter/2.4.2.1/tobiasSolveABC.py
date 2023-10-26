class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
        
contacts = []

contacts.append(Contact("Tobias Samsonsen", "90142974", "tobias.samsonsen@gmail.com"))
contacts.append(Contact("Børge Harboe", "90215019", "borge@harboe.org"))

for contact in contacts:
    print("--------------")
    print(contact.name)
    print(contact.number)
    print(contact.email)