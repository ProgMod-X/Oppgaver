
P = float(input("Protein mengde i gram: "))
F = float(input("Fett mengde i gram: "))
C = float(input("Karbohydrater mengde i gram: "))

# P = Protein, F = Fett, C = Karbohydrater
def kilojoule(P, F, C):
    return 17 * P + 38 * F + 17 * C


print(f"E = {kilojoule(P, F, C)}")