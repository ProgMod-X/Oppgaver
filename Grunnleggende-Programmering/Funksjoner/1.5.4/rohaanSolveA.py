#
# P = Protein
# F = Fett
# C = Karbohydrater
#


def kilojoule(P, F, C):
    return 17 * P + 38 * F + 17 * C


print(f"E = {kilojoule(18, 23, 50)}")