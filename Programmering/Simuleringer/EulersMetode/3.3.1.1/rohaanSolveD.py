import matplotlib.pyplot as plt

x_min = 1
x_maks = 4

df_liste = []
x_liste = []
y_liste = []

x = 1
y = 0
dx = 1E-3

def df(x):
    return 2 * x**3 - 15 * x**2 + 35 * x - 25

while x <= x_maks:
    x_liste.append(x)
    y_liste.append(y)
    df_liste.append(df(x))

    x += dx
    y += df(x) * dx
    

plt.plot(x_liste, y_liste, "b")
plt.plot(x_liste, df_liste, "r")
plt.show()