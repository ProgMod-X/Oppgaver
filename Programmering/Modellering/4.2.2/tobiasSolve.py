import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np

data_år = [1950, 1960, 1970, 1981, 1990, 2000, 2012, 2020]

data_x = [(x-1950) for x in data_år]
data_y1 = [19624, 31121, 57606, 93397, 121848, 142816, 147716, 154197]

plt.plot(data_x, data_y1, "o")

def f(x, L, a, k):
    return L/(1 + a*np.e**(-k*(x)))

konstanter = so.curve_fit(f, data_x, data_y1, [160000, 0.1, 1])[0]

L = konstanter[0]
a = konstanter[1]
k = konstanter[2]

print(f"f(x) = {L:0.3f}/1 + {a:0.3f}*e^-{k:0.3f}x")

x = 0
maxX = 0
maxdy = 0
while x < 100:
    dy = f(x+0.001, L, a, k) - f(x, L, a, k)
    if dy > maxdy:
        maxdy = dy
        maxX = x
    x += 0.001
    
print(f"Produksjonen økte raskest i år {(maxX + 1950):0.0f}")

data_y2 = [16924, 31253, 56770, 88168, 105941, 123761, 129900, 133725]

konstanter = so.curve_fit(f, data_x, data_y2, [160000, 0.1, 1])[0]

L2 = konstanter[0]
a2 = konstanter[1]
k2 = konstanter[2]

x = np.linspace(data_x[0], 100,  1000)

plt.plot(x, f(x, L2, a2, k2), color="r")
plt.plot(x, f(x, L, a, k), color="b")
plt.grid()
plt.show()