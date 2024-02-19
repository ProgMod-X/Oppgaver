import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np

data_x = [0.6, 2.5, 5.4, 7.8, 9.6]
data_y = [250, 480, 660, 920, 1140]

plt.plot(data_x, data_y, "o")

def f(x, a, b):
    return a*x + b

konstanter = so.curve_fit(f, data_x, data_y)[0]

a = konstanter[0]
b = konstanter[1]

print(f"f(x) = {a}*x + {b}")

x = np.linspace(data_x[0],  data_x[-1],  1000)

plt.plot(x, f(x, a, b), color="r")
plt.show()
