class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

contacts = []

while True:
    print(f"Ny bruker?(ny)\nPrint ut liste av kontakter?(liste)\nAvslutt programmer?(avslutt)\n")
    answer = input()

    if answer == "ny":
        name = input("\nNavn: ")
        number = input("Telefonnummer: ")
        email = input("Email: ")

        newContact = Contact(name, number, email)
        contacts.append(newContact)
    elif answer == "liste":
        for contact in contacts:
            print(f"\n\n{contact.name}\t{contact.number}\t{contact.email}\n\n")
    elif answer == "avslutt":
        break
    else:
        print("\n\nUgyldig input\n\n")