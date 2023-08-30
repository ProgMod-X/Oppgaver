'''
Lag et program der brukeren skal taste inn et heltall. Programmet skal opplyse om tallet er et partall eller et oddetall.
''' 


while True:
    try:
        tall = int(input("Skriv inn et heltall: "))
        odde_par = tall % 2

#Definer "odde_par" som resten av tall/2 

        if odde_par == 1:
            print(tall, "er et oddetall")
            break

#Hvis "odde_par" er 1 printer vi at tallet er et oddetall og bryter ut av løkken

        elif odde_par == 0:
            print(tall, "er et partall")
            break
        
#Hvis "odde_tar" er 0 printer vi at tallet er et partall og bryter ut 

        else:
            break
    except ValueError:
        print("Ugyldig input")
        
#Hvis programmet ikke aksepterer svaret skal den printe "ugyldig input" og prøve på nytt 










tall = int(input("Tall:"))
#Spør om et tall

resultat = tall / 2
#Definerer tallet delt på to som resultat

if float(resultat).is_integer():
    print(tall, "er et partall")
#Hvis resultat er en "integer" er det et partall
else:
    print(tall, "er et oddetall") 
#Hvis resultat ikke er en "integer" er det et oddetall