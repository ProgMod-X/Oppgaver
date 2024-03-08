def deltaY(k, y, w):
    return (k * y) + w

factor = -0.25
change = 2.4
inBody = 10


while inBody > 5.5:
    inBody = 0
    factor -= 0.0001 # å endre på faktoren er det samme som å endre på hvor lenge det er mellom tablettene
    for i in range(1, 20):
        inBody += deltaY(factor, inBody, change)

#Finner ratio mellom faktor og original faktor. Ganger ratio med 24 for å finne antall timer
print(f"Mads må ta tabletten en gang per {round((factor/-0.25) * 24)} timer for å ikke få for mye i seg")

# Svar oppgave a: 9.59 mg