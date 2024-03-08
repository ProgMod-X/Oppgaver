import math
import matplotlib.pyplot as plt

def f(t):
    return (10000)/(1+(50*math.e**(-0.5*t)))

t = 0
T = 25
dt = 0.001
x_list = []
y_list = []

while t < T:
    x_list.append(t)
    y_list.append(f(t))
    t += dt

plt.plot(x_list, y_list)
plt.grid()
plt.show()