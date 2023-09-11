'''
Lag en funksjon som kalkulerer kilojoule energi i mat etter følgende formel.
E = 17⋅P + 38⋅F + 17⋅C

P = protein, F = fett, C = karbohydrater

Funksjonen tar tre parametre (mengde i gram) og returnerer én verdi – energi i kilojoule (kJ)

Lag et program der brukeren kan oppgi mengde protein, fett og karbohydrater, og få utregnet energimengden i maten. 
Bruk funksjonen du laget over
'''

def E(P, F, C):
    return 17 * P + 38 * F + 17 * C

P, F, C = int(input("Hvor mye protein (i gram) var det i maten:")), int(input("Hvor mye fett (i gram) var det i maten:")), int(input("Hvor mye karbohydrater (i gram) var det i maten:"))

print(E(P, F, C))