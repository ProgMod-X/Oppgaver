import math
import matplotlib.pyplot as plt

def f(x):
    return 42 * (1 - math.e**(-x) + 1.05 * x)

x = 0
dx = 0.001
N = 25

y_list = []
x_list = []

while x < N:
    y_list.append(f(x))
    x_list.append(x)
    x += dx

plt.plot(x_list, y_list)
plt.grid()
plt.show()