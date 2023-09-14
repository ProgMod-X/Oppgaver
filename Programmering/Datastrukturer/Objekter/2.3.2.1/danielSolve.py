class Contact:
    def __init__(self, name, tlf, email):
        self.name = name
        self.tlf = tlf
        self.email = email
        
contacts = []

while True:
    print("\nVelkommen til kontaktene dine!\n")
    print("Skriv ny for ny kontakt")
    print("Skriv liste for å se kontaktene dine")
    print("Skriv avslutt for å avslutte programmet")

    svar = input("\n$ ")
    
    if svar == "ny":
        name = input("Skriv inn navn: ")
        tlf = input("Skriv inn telefonnummer: ")
        email = input("Skriv inn e-postadresse: ")
        ny_kontakt = Contact(name, tlf, email)
        contacts.append(ny_kontakt)
        print("Kontakt er lagt til.")
    
    if svar == "liste":
        if len(contacts) == 0:
            print("Ingen kontakter opprettet!")
        else:
            print("Navn:\tTelefonnummer:\tEpostadresse:")
            for i in contacts:
                print(i.name,"\t",i.tlf,"\t",i.email)
        
        
    if svar == "avslutt":
        break
    else:
        print("Skriv en gyldig kommando")