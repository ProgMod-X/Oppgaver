import os

class Contact:
    name = None
    tlf = None
    email = None

    def __init__(self, name, tlf, email):
        self.name = name
        self.tlf = tlf
        self.email = email

contacts = []

if os.path.exists("contacts.txt"):
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split("\t")
            if len(data) == 3:
                name, tlf, email = data
                contacts.append(Contact(name, tlf, email))

print("\nVelkommen til kontaktene dine!\n")
print("Skriv ny for ny kontakt")
print("Skriv liste for å se kontaktene dine")
print("Skriv avslutt for å avslutte programmet\n")

while True:
    svar = input("$ ")

    if svar == "ny":
        name = input("\nSkriv inn navn: ")
        tlf = input("Skriv inn telefonnummer: ")
        email = input("Skriv inn e-postadresse: ")
        ny_kontakt = Contact(name, tlf, email)
        for i in contacts:
            if i.name == name:
                eksisterer = True
                print("\nKontakten eksisterer allerede!\n")
                break
        eksisterer = False

        if not eksisterer:
            contacts.append(ny_kontakt)
            print("\nKontakt er lagt til.\n")

    if svar == "liste":
        if len(contacts) == 0:
            print("\nIngen kontakter opprettet!\n")
        else:
            print("\nNavn:\tTelefonnummer:\tEpostadresse:")
            for i in contacts:
                print(i.name, "\t", i.tlf, "\t", i.email)

    if svar == "avslutt" or svar == "exit":
        with open("contacts.txt", "w") as file:
            for i in contacts:
                file.write(f"{i.name}\t{i.tlf}\t{i.email}\n")
        print("\nAvslutter programmet!\n")
        break
