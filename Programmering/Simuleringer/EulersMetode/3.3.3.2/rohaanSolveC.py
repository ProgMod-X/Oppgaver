import math
import matplotlib.pyplot as plt

def f(x):
    return 6.594 * math.e**(0.234 * x)

x = 0
dx = 0.0001
N = 15
area = 0

y_list = []
x_list = []

while x < N:
    area += (f(x)*dx)
    y_list.append(f(x))
    x_list.append(x)
    x += dx

print(f"Summen av inntektene til Netflix fra 2005 til 2020 er {round(area, 2)} milliarder kroner")


plt.plot(x_list, y_list)
plt.grid()
plt.show()