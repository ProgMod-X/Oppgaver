'''

Funksjonen tar tre parametre (mengde i gram) og returnerer én verdi – energi i kilojoule (kJ)

Lag et program der brukeren kan oppgi mengde protein, fett og karbohydrater, og få utregnet energimengden i maten. Bruk funksjonen du laget over
'''


P,F,C = float(input("P: ")), float(input("F: ")),float(input("C: "))

def kilojoule(P,F,C):
    return 17*P + 38*F + 17*C

print("E =", round(kilojoule(P, F, C)),"kilojoules")
