'''
Vi starter med tallet 1. Bruk en løkke til å bestemme hvor mange ganger vi må doble tallet for det skal bli større enn 4000. Hva er tallet da?
'''

antall = 0
x = 1

while x < 4000:
    x *= 2
    antall += 1 

print(antall)