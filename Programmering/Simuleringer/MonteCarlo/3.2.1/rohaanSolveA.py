import random

N = 1000000
outcomes = 0


for i in range(N):
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    if a + b == 12:
        outcomes += 1

print(f"Sannsynligheten for å få summen 12 av to terninger er {outcomes / N * 100}%")