class Contact:
    name = None
    tlf = None
    email = None
    def __init__(self, name, tlf, email):
        self.name = name
        self.tlf = tlf
        self.email = email
        
contacts = []

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
        contacts.append(ny_kontakt)
        print("\nKontakt er lagt til.\n")
    
    if svar == "liste":
        if len(contacts) == 0:
            print("\nIngen kontakter opprettet!\n")
        else:
            j = 0
            for i in contacts:
                if j == 0:
                    print("\nNavn:\tTelefonnummer:\tEpostadresse:") 
                print(i.name,"\t",i.tlf,"\t",i.email)
                j += 1
            print("")
        
    if svar == "avslutt" or svar == "exit":
        print("\nAvslutter programmet!\n")
        break
    if svar == " ":
        print("\n$ ")