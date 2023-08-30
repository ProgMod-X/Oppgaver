'''
Lag et “spill” basert på «sten,saks, papir» (eng.: «Rock-paper-scissors» ) der bruker skriver inn sitt valg og datamaskinen trekker tilfeldig.
Brukeren skal få beskjed om hvem som vant (eventuelt uavgjort) og hvorfor.
''' 

import random 




while True:
    try:
        spiller = str(input("Stein(r), saks(s) eller papir(p): "))
        datamaskin = random.choice(["r", "p", "s"])

        if spiller == datamaskin:
            print("Uavgjort")
            break
        elif spiller == "r":
            if datamaskin == "s":
                print("Du vant, datamaskinen spillte", datamaskin)
                break
            elif datamaskin == "p":
                print("Datamaskinen vant, han spillte", datamaskin)
                break
        elif spiller == "s":
            if datamaskin == "p":
                print("Du vant, datamaskinen spillte", datamaskin)
                break
            elif datamaskin == "r":
                print("Datamaskinen vant, han spillte", datamaskin)
                break
        elif spiller == "p":
            if datamaskin == "r":
                print("Du vant, datamaskinen spillte", datamaskin)
                break
            elif datamaskin == "s":
                print("Datamaskinen vant, han spillte", datamaskin) 
                break


    except ValueError:
        print("Ugyldig, prøv igjen: ")





