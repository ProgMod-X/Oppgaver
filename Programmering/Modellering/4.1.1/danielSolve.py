import matplotlib.pyplot as plt
import scipy.optimize as so
 
x = [0.6, 2.5, 5.4, 7.8, 9.6]
y = [250, 480, 660, 920, 1140]
 
def mal(x, a, b):
    return a*x + b

konstanter = so.curve_fit(mal, x, y)[0]

a = konstanter[0]
b = konstanter[1]

print(type(a))
print(type(b))
print(type(x))

print(f'S(x) = {a}*x + {b}')

x_min = 0
x_maks = 9.7
dx = 0.1
x_liste = []
y_liste = []

x = x_min
def S(x):
    return a*x + b



while x < x_maks:
    x_liste.append(x)
    y_liste.append(S(x))
    x += dx

plt.plot(x_liste, y_liste, label='Tilpasset linje')
x = [0.6, 2.5, 5.4, 7.8, 9.6]
y = [250, 480, 660, 920, 1140]
plt.plot(x, y, 'o', label='Data Punkter')
plt.grid()
plt.legend()
plt.show()