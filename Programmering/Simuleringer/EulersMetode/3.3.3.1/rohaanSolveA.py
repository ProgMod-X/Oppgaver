import math
import matplotlib.pyplot as plt

def f(x):
    return 10000 / (1 + 50 * math.e**(-0.5 * x))

x = -10
dx = 0.01
N = 25
area = 0

y_list = []
x_list = []

while x < N:
    area += (f(x)*dx)
    y_list.append(f(x))
    x_list.append(x)
    x += dx

print(round(area, 3))

plt.plot(x_list, y_list)
plt.grid()
plt.show()