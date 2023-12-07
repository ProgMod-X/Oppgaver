import random
import matplotlib.pyplot as plt

N = 1000000
outcomes = 0
dic = {}
dic_theoretical = {}
table = []

for i in range(6):
    a = []
    for j in range(6):
        a.append(i + j + 2)
    table.append(a)

for i in range(1, 13):
    dic[i] = 0
    dic_theoretical[i] = 0

for i in range(N):
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    dic[a + b] += 1

for i in range(6):
    for j in range(6):
        dic_theoretical[table[i][j]] += 1/36

x = list(dic.keys())
y = []
y_theoretical = list(dic_theoretical.values())

for i in range(1, 13):
    chance = round(dic[i] / N * 100, 2)
    y.append(chance)
    y_theoretical[i - 1] *= 100

plt.bar(x, y, width=-0.4, align="edge", label="Estimert")
plt.bar(x, y_theoretical, width=0.4, align="edge", label="Teoretisk")
plt.xlabel("Summen av to ternings kast")
plt.ylabel("Sannsuynlighet for en sum i prosent")
plt.legend()
plt.show()