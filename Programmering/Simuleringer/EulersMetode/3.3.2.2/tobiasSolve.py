import math
import matplotlib.pyplot as plt

def f(x):
    return (1/(math.sqrt(2*math.pi))) * math.e**((-x**2)/2)


x = -3
dx = 0.0001
N = 3
area = 0

fList = []
xList = []

while x < N:
    area += (f(x)*dx)
    fList.append(f(x))
    xList.append(x)
    x += dx

print(round(area, 3))

plt.plot(xList, fList)
plt.grid()
plt.show()