# Denne algoritmen undersøker om en trekant er rettvinklet

c = float(input("Length hypotenuse: "))
a = float(input("Length leg 1: "))
b = float(input("Length leg 2: "))

if c**2 == (a**2 + b**2):
    print("Triangle is right-angled")
    
else:
    print("Triangle is not right-angled")