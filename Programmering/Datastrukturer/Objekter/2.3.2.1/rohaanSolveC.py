class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

contacts = []

contacts.append(Contact("Daniel", "98132358", "Daniel@Boye.no"))
contacts.append(Contact("Evelyn", "12456789", "Evelyn@Than.com"))

for contact in contacts:
    print(f"{contact.name}\t{contact.number}\t{contact.email}")