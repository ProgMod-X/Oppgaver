#Lag et program der brukeren skal taste inn et heltall. 
#Programmet skal opplyse om tallet er et partall eller et oddetall.

tall = int(input("skriv inn et tall"))
resultat = tall / 2

if float(resultat).is_integer():
    print("DU har et partall")
else:
    print("Du har et oddetall")