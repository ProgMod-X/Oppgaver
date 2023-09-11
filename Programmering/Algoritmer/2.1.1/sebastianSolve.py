'''
Algoritmen undersøøker om en trekant er en rettvinklet trekant
'''


c = int(input(" Skriv inn lengden til den lengste siden i trekanten "))

b = int(input("Skriv inn lengden til en annen side i trekanten "))

a = int(input("Skriv inn lengden til den siste siden i trekanten "))

if a**2 + b**2 == c**2:
    print(f"En trekant med sidene {a},{b}, og {c} er en rettvinklet trekant")
else:
    print(f"En trekant med sidene {a},{b}, og {c} er ikke en rettvinklet trekant")