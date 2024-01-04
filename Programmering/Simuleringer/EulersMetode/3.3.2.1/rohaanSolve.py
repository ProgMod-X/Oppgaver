import matplotlib.pyplot as plt
import math

# Bruker trapes metoden

a = 0
b = 2 * math.pi
n = 100
dx = (b - a) / n
z = 1

x = a + (z - 1) * dx
areal = 0
x_list = []
y_list = []

def f(x):
    return math.sin(x)

while x < b:
    areal += abs((f(a + (z - 1) * dx) + f(a + (z) * dx)) / 2 * dx)

    x_list.append(x)
    y_list.append(f(x))

    x += dx
    z += 1

print(f"Arealet under grafen er {areal}")

plt.plot(x_list, y_list)
plt.show()