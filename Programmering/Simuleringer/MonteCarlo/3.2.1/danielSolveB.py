import matplotlib.pyplot as plt
import random

N = 100000
gunstige_utfall = [0] * 11
# print(gunstige_utfall)
n = 0

while n < N:
    terning_1 = random.randint(1, 6)
    terning_2 = random.randint(1, 6)
    sum = terning_1 + terning_2
    total = sum - 2  # På grunn av 12 - 2 blir til 10 når vi skal gjøre det om til liste
    # Legge til i guntig utfall
    gunstige_utfall[total] += 1
    n += 1

sannsynligheter = []
for i in gunstige_utfall:
    sannsynligheter.append(i / N)

fig, ax = plt.subplots()
utfall = list(range(2, 13))
sannsynlighet = sannsynligheter

ax.bar(utfall, sannsynlighet, align='center')
ax.set_xticks(utfall)
ax.set_xlabel('Sum av terningkast')
ax.set_ylabel('Sannsynlighet')

plt.show()
