import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x)


x = 0
dx = 0.0001
N = 2*math.pi
area = 0

fList = []

while x < N:
    area += (f(x)*dx)
    fList.append(f(x))
    x += dx
    
xList = [(i*dx) for i in range(len(fList))]

print(round(area, 3))

plt.plot(xList, fList)
plt.grid()
plt.show()