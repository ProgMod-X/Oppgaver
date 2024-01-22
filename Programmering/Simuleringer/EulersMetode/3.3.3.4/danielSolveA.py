import math
import matplotlib.pyplot as plt

def f(x):
    return 1.3 * math.sin(0.52 * x - 2) + 2.4

x = 0
dx = 1

x_verdier = []
y_verdier = []

while x < 24:
    x_verdier.append(x)
    y_verdier.append(f(x))
    x += dx

temp_y_verdier = y_verdier.copy()
temp_y_verdier.sort(reverse=True)

max = [i for i in range(24) if y_verdier[i] in temp_y_verdier[:2]]

print("Høyest i time", max[0], "og", max[1])
