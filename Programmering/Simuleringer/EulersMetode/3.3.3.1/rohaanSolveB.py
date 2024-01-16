import math
import matplotlib.pyplot as plt

def f(x):
    return 10000 / (1 + 50 * math.e**(-0.5 * x))

x = -10
dx = 0.0001
N = 25
area = 0

y_list = []
x_list = []

while x < N and f(x) <= 7000:
    area += (f(x)*dx)
    y_list.append(f(x))
    x_list.append(x)
    x += dx

print(f"Antall smittede per uke er {f(x)} når x er {x}")

plt.plot(x_list, y_list)
plt.grid()
plt.show()