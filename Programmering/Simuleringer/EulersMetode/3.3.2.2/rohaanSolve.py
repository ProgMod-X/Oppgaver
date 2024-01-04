import matplotlib.pyplot as plt
import math

# Bruker trapes metoden

a = -5
b = 5

n = 100
dx = (b - a) / n
z = 1

x = a + (z - 1) * dx
areal = 0
x_list = []
y_list = []

def f(x):
    return (1 / math.sqrt(2 * math.pi)) * math.e ** (-x**2 / 2)

while x < b:
    areal += abs((f(a + (z - 1) * dx) + f(a + (z) * dx)) / 2 * dx)

    x_list.append(x)
    y_list.append(f(x))

    x += dx
    z += 1

print(f"Arealet under grafen er {areal}")

plt.plot(x_list, y_list)
plt.show()

# Desto mer vi øker intervallet desto mer tilnærmer arealet seg 1