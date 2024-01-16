import math
import matplotlib.pyplot as plt

def f(t):
    return (10000)/(1+(50*math.e**(-0.5*t)))

t = 0
T = 25
dt = 0.001

x_list = [t]
y_list = [f(t)]
sum = 0

while sum < 15000:
    x_list.append(t)
    y_list.append(f(t))
    sum += y_list[-1] * dt
    t += dt
    
print(f"Det er mer enn 15 000 smittede etter {t} uker")

plt.plot(x_list, y_list)
plt.grid()
plt.show()