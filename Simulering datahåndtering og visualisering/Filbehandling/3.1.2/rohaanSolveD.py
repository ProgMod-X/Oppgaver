import csv

class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

contacts = []

while True:
    print(f"Ny bruker?(ny)\nPrint ut liste av kontakter?(liste)\nAvslutt programmer?(avslutt)\nLes inn kontakt fra fil?(les inn)\nLage kontaker(lagre)\n")
    answer = input()

    if answer == "ny":
        name = input("\nNavn: ")
        number = int(input("Telefonnummer: "))
        email = input("Email: ")

        newContact = Contact(name, number, email)
        contacts.append(newContact)
    elif answer == "liste":
        for contact in contacts:
            print(f"{contact.name}\t{contact.number}\t{contact.email}")
    elif answer == "avslutt":
        break
    elif answer == "les inn":
        with open(r"Simulering datahåndtering og visualisering\Filbehandling\3.1.2\register.csv") as file:
            reader = csv.reader(file)
            for line in reader:
                contacts.append(Contact(str(line[0]), int(line[1]), str(line[2])))
    elif answer == "lagre":
        with open(r"Simulering datahåndtering og visualisering\Filbehandling\3.1.2\register.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for i in range(len(contacts)):
                writer.writerow([contacts[i].name, contacts[i].number, contacts[i].email])
    else:
        print("\n\nUgyldig input\n\n")