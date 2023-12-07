import random
import matplotlib.pyplot as plt

N = 1000000
outcomes = 0
dic = {}

for i in range(1, 13):
    dic[i] = 0

for i in range(N):
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    dic[a + b] += 1
    # print(dic)

x = list(dic.keys())
y = []

for i in range(1, 13):
    chance = round(dic[i] / N * 100, 2)
    # print(f"Sannsynligheten for å få summen {i} av to terninger er {chance}%")
    y.append(chance)

plt.bar(x, y, width=0.4)
plt.show()