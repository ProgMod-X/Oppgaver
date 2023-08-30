'''
Pyramidetall n er summen av alle kvadrattall fra og med 1 til og med n2. Pyramidetall 4 er  visualisert under.

Skriv et program som spør brukeren om hvilket tall hen ønsker, og bruker én løkke til å beregne tallet. Skriv ut tallet
'''

tall = int(input("Tall: "))
x = 1
total = 0
while x <=tall:  
    total += x**2
    print(x**2)
    x += 1

print("Summen av alle kvadrattallene til og med", tall, "er", total)
    
