from matplotlib import pyplot as plt
import random

dicelist = [0 for i in range(1,13)]
N = 500

for i in range(N):
    dicesum = random.randint(1,6) + random.randint(1,6)
    dicelist[dicesum-1] += 1

dicelist = [i/N for i in dicelist]
x = [i for i in range(1,13)]

print(dicelist[11])

table = [([i+j for i in range(1, 7)]) for j in range(1, 7)]
dicelist2 = []
for num in range(1,13):
    sum = 0
    for list in table:
        for val in list:
            if val == num:
                sum += 1
    print(f"Value: {num:2.0f} | Probability: {round(sum/36, 3)}")
    dicelist2.append(round(sum/36, 3))

plt.bar([(x-0.2) for x in x], dicelist, width=0.4, label="Estimated", color="blue")
plt.bar([(x+0.2) for x in x], dicelist2, width=0.4, label="Analytical", color="red")
plt.legend()
plt.show()