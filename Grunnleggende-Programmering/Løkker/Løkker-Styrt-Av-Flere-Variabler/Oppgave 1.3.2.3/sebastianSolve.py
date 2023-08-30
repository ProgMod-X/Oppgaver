'''
I matematikken bruker vi såkalt sigma notasjon til å beskrive en sum der hvert ledd følger en gitt formel.

På samme måte bruker vi en såkalt “stor pi”-notasjon til å beskrive et produkt.

A) Skriv et program som beregner summen av ledd på formen (2i + 1) opp til og med en brukervalgt verdi for i.

B) Skriv et program som beregner produktet av ledd på formen (2i + 1) opp til og med en brukervalgt verdi for i.
'''


tall = int(input("Tall: "))

total = 0
i = 1 

for x in range(0,tall):
    total = 2 * i + 1
#    print(x)
print(total)