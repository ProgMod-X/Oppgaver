import math
import matplotlib.pyplot as plt
 
def f(x):
    return 42*(1 - (math.e**-x)) + 1.05*x
 
x = 0
dx = 1
 
x_verdier = []
y_verdier = []
 
while x < 25:
    x_verdier.append(x)
    y_verdier.append(f(x))
    x += dx
 
plt.plot(x_verdier, y_verdier)
plt.grid()
plt.show()