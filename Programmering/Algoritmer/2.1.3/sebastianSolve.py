import math
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Skriv inn det første tallet: "))
b = int(input("Skriv inn det siste tallet: "))

resultat = a*b/lcm(a, b)

print("Det minste felles multiplum av", a, "and", b, "er", resultat)