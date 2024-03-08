import math
import matplotlib.pyplot as plt

def f(x):
    return 1/x

dx = 0.01
area = 0
k = 1.001

while round(area, 6) < 2:
    x = 1
    area = 0
    k += 0.001
    while x < k:
        area += abs(((f(x)+f(x+dx))/2)*dx)
        x += dx

print(round(area, 3))
print(round(k, 3))