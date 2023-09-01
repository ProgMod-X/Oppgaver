import math


a = float(input("Hva er lengden til den ene kateten? "))
b = float(input("Hva er lengden til den andre kateten? "))
c = float(input("Hva er lengden til hypotenusen? "))


if (a**2 + b**2) == (c**2):
    print(f"Katetene: {a} og {b}, med hypotenusen: {c} danner en rettvinklet trekant")
else:
    print(f"Katetene: {a} og {b}, med hypotenusen: {c} danner ikke en rettvinklet trekant")