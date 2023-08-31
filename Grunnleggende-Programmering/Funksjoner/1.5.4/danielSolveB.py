p = int(input("Protein: "))
f = int(input("Fett: "))
c = int(input("Karbohydrater: "))

def kilojoule(p, f, c):
    E = 17*p + 38*f + 17*c
    return E

print("Energi: ", kilojoule(p, f, c))
