import math
import matplotlib.pyplot as plt

def f(x):
    return 1.3 * math.sin(0.52 * x - 2) + 2.4

x = 0
dx = 0.001
N = 24

y_list = []
x_list = []
area = 0

while round(area, 3) < 17:
    area += f(x) * dx
    y_list.append(f(x))
    x_list.append(x)
    x += dx

print(f"Strømmen gikk ca {round(x, 1)} timer etter midnatt")

plt.plot(x_list, y_list)
plt.grid()
plt.show()