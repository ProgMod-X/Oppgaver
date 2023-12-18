import matplotlib.pyplot as plt
import random

N = 1000
gunstige_utfall = 0
n = 0
target = 12
y = []
x = []

while n < N:
    terning_1 = random.randint(1, 6)
    terning_2 = random.randint(1, 6)
    sum_terninger = terning_1 + terning_2

    if sum_terninger == target:
        gunstige_utfall += 1

    n += 1
    estimat = gunstige_utfall / n
    y.append(estimat)
    x.append(n)

# Lag et linjediagram
plt.plot(x, y, label=f'Estimat for sannsynlighet ({N} kast)')
plt.axhline(y=1/36, color='r', linestyle='--', label='Ekte sannsynlighet (1/36)')
plt.xlabel('Antall kast')
plt.ylabel('Estimert sannsynlighet')
plt.legend()
plt.show()
