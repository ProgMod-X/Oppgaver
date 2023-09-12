import random

n = int(input("Hvor mange spørsmål? "))

correct = 0

for i in range(n):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
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