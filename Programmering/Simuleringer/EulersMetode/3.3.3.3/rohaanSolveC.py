import math

def f(x):
    return 42 * (1 - math.e**(-x) + 1.05 * x)

x = 0
dx = 0.001
N = 10
area = 0


while x < N:
    area += f(x)*dx
    x += dx

print(f"Maria sin samlede treningseffekt etter 10 minutter er {round(area, 1)} kJ")