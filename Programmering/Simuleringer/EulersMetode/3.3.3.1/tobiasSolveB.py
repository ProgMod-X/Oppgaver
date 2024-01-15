import math
import matplotlib.pyplot as plt

def f(t):
    return (10000)/(1+(50*math.e**(-0.5*t)))

t = 0
T = 25
dt = 1
x_list = [t]
y_list = [f(t)]

while y_list[-1] < 7000:
    x_list.append(t)
    y_list.append(f(t))
    t += dt
    
print(f"Det er mer enn 7000 nye smittede hver uke etter {t-1} uker")

plt.plot(x_list, y_list)
plt.grid()
plt.show()