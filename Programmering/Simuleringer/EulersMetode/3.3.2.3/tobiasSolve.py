import math
import matplotlib.pyplot as plt

def f(x):
    return 1/x

dx = 0.01
area = 0
k = 1.01

while area < 2:
    x = 1
    area = 0
    k += 0.01
    while x < k:
        area += (f(x)*dx)
        x += dx

print(round(area, 3))
print(round(k, 3))