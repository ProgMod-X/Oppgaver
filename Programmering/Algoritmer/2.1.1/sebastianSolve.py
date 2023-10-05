


c = int(input("Skriv inn lengden til hypotinusen, (den lengste siden) siden i trekanten "))

b = int(input("Skriv inn lengden til den ene kateten side i trekanten "))

a = int(input("Skriv inn lengden til den siste kataten i trekanten "))


if a**2 + b**2 == c**2:
    print("En trekant med sidene", a, b, "og", c, "er en rettvinklet trekant")
else:
    print("En trekant med sidene", a, b, "og", c, "er ikke en rettvinklet trekant")