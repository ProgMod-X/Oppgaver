class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
        
contacts = []

while True:
    try:
        operation = input("Command (new, list, quit): ").lower()
        print("--------------")
        if "new" != operation and "list" != operation and "quit" != operation:
            raise ValueError
    except ValueError:
        print("Input must be one of the accepted inputs")
    
    if operation == "new":
        name = input("Full name: ")
        number = input("Phone number: ")
        email = input("Email address: ")
        contacts.append(Contact(name, number, email))
    elif operation == "list":
        if len(contacts) == 0:
            print("No contacts in list")
            print("--------------")
        else:
            for contact in contacts:
                print(contact.name)
                print(contact.number)
                print(contact.email)
                print("--------------")
    elif operation == "save":
        open(r"Programmering\Filbehandling\2.8.2\tobiasRegister.csv", "w")
        
        
    elif operation == "quit":
        break