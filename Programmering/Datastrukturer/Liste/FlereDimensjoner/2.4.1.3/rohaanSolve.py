import random

n = int(input("Hvor stor er tabellen? "))

tabell = []

def positive_diagonal(tabell):
    sum = 0
    for i in range(len(tabell)):
        if tabell[i][i] > 0:
            sum += 1
    return sum

for i in range(n):
    a = []
    for j in range(n):
        a.append(random.randint(-10, 10))
    tabell.append(a)

# print(tabell)

print(f"Antall positive tall på hoved diagonalen er {positive_diagonal(tabell)}")