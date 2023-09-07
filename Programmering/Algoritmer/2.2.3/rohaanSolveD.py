import random

difficulty = int(input("Hvilken vanskelighets grad?\nEnkel(0), Middels(1), Vanskelig(2): "))
n = int(input("Hvor mange spørsmål? "))

if difficulty == 0:
    difficulty = 10
elif difficulty == 1:
    difficulty = 25
elif difficulty == 2:
    difficulty = 100

correct = 0

for i in range(n):
    a = random.randint(1, difficulty)
    b = random.randint(1, difficulty)
    c = int(input(f"Hva er produktet av {a} og {b}: "))

    if c == a * b:
        correct += 1

if correct == n:
    print("Perfekt")
elif correct > n / 3 * 2:
    print("Bra!")
elif correct <= n / 3 * 2 and correct >= n / 3:
    print("Du trenger mer trening...")
else:
    print("Spør mattelæreren din om hjelp!")