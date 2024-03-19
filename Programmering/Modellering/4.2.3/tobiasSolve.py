import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np

data_år = [1980, 1990, 2000, 2010, 2018]

data_x = [(x-1980) for x in data_år]
data_y = [91.7, 211.6, 529.8, 788.1, 1000.3]

plt.plot(data_x, data_y, "o")

def f(x, a, k):
    return a*x + k

konstanter = so.curve_fit(f, data_x, data_y)[0]

a = konstanter[0]
k = konstanter[1]

print(f"f(x) = {a:0.3f}x + {k:0.3f}")

def g(x, L, a, k):
    return L/(1 + (a*np.e**(-k*x)))

konstanter = so.curve_fit(g, data_x, data_y, [1250, 10, 0.1])[0]

L = konstanter[0]
a2 = konstanter[1]
k2 = konstanter[2]

x = 2015 - 1980
df = 0
dg = 0
sumf = 0
sumg = 0
while x < (2026 - 1980):
    df = f(x, a, k) - f(x - 1, a, k)
    dg = g(x, L, a2, k2) - g(x - 1, L, a2, k2)
    
    sumf += df
    sumg += dg
    x += 1
    
print(f"Gjennomsnittlig vekst f: {sumf/(2026-2015):0.3f}")
print(f"Gjennomsnittlig vekst g: {sumg/(2026-2015):0.3f}")
    

x = np.linspace(data_x[0], 70,  1000)


plt.plot(x, f(x, a, k), color="b")
plt.plot(x, g(x, L, a2, k2), color="r")
plt.grid()
plt.show()

def v(x):
    return 91*1.057**x

plt.plot(x, g(x, L, a2, k2), color="g")
plt.plot(x, v(x), color="r")
plt.grid()
plt.show()