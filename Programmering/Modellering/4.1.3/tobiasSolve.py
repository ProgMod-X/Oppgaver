import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np

data_år = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]

data_x = [(år - 2000) for år in data_år]
data_y = [383, 603, 832, 1081, 1193, 1352, 1667, 1905]

plt.plot(data_x, data_y, "o")

def f(x, a, b):
    return a*x + b

konstanter = so.curve_fit(f, data_x, data_y)[0]

a = konstanter[0]
b = konstanter[1]

print(f"f(x) = {a}*x + {b}")

x = np.linspace(data_x[0], 14,  1000)

data_x2 = [8, 12, 14]
data_y2 = [2432, 9580, 41051]

plt.plot(data_x2, data_y2, "o", color="g")
plt.plot(x, f(x, a, b), color="r")
plt.show()

