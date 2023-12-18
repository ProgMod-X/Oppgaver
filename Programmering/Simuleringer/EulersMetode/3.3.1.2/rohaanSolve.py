import matplotlib.pyplot as plt
import math

x_min = 0
x_maks = 4 * math.pi

df_liste = []
x_liste = []
y_liste = []

x = 0
y = 0
dx = 1E-3

def df(x):
    return math.cos(x)

while x <= x_maks:
    x_liste.append(x)
    y_liste.append(y)
    df_liste.append(df(x))

    x += dx
    y += df(x) * dx
    

plt.plot(x_liste, y_liste, "b")
plt.plot(x_liste, df_liste, "r")
plt.show()