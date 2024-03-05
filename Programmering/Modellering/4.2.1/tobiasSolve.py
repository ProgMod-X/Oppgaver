import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy as np

data_x = [0.1, 0.3, 0.5, 0.8, 1.0, 1.3, 1.6, 2.0]
data_y = [0.69, 1.17, 1.44, 1.82, 2.08, 2.27, 2.53, 2.80]

plt.plot(data_x, data_y, "o")

def f(x, a, b):
    return a * x**b

konstanter = so.curve_fit(f, data_x, data_y)[0]

a = konstanter[0]
b = konstanter[1]

print(f"f(x) = {round(a, 3)}* x^{round(b, 3)}")

def t(x):
    return 2*np.pi * (x/9.81)**0.5

x = np.linspace(data_x[0], 10,  1000)

plt.plot(x, t(x), color="g")
plt.plot(x, f(x, a, b), color="r")
plt.grid()
plt.show()

