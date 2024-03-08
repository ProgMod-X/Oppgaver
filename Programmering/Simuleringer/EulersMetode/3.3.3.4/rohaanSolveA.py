import math
import matplotlib.pyplot as plt

def f(x):
    return 1.3 * math.sin(0.52 * x - 2) + 2.4

x = 0
dx = 0.001
N = 24

y_list = []
x_list = []
biggest_consumptions = [(0, 0)]

while x <= N:
    temp_fx = round(f(x), 7)
    if temp_fx > biggest_consumptions[0][1]:
        biggest_consumptions[0] = (x, temp_fx)
    elif temp_fx == biggest_consumptions[0][1]:
        biggest_consumptions.append((x, temp_fx))

    y_list.append(f(x))
    x_list.append(x)
    x += dx

for biggest_consumption in biggest_consumptions:
    print(f"Energiforbruket er høyest {round(biggest_consumption[0], 1)} timer etter midnatt")

plt.plot(x_list, y_list)
plt.grid()
plt.show()