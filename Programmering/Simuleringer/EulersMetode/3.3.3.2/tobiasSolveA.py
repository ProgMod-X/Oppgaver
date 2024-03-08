import math
import matplotlib.pyplot as plt

def f(x):
    return 6.594*math.e**(0.234*x)

x = 0
X = 25
dx = 1

x_list = [x]
y_list = [f(x)]
sum = x

while x < X:
    x_list.append(x)
    y_list.append(f(x))
    sum += y_list[-1] * dx
    x += dx
    
for index in range(len(x_list)):
    plt.bar(x_list[index], y_list[index], align="edge", color="red")

plt.show()