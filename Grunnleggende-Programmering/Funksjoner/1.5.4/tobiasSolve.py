def toEnergy(p, f, c):
    return(17*p + 38*f + 17*c)

protein = float(input("Grams of protein: "))
fat = float(input("Grams of fat: "))
carbs = float(input("Grams of carbs: "))

print(f"Energy: {toEnergy(protein, fat, carbs)}kJ")