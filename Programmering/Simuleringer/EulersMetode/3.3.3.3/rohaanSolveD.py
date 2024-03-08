import math

def f(x):
    return 42 * (1 - math.e**(-x) + 1.05 * x)

x = 0
dx = 0.001
N = 10
area = 0

while area < 1300:
    area += f(x)*dx
    x += dx

print(f"For at Maria sin samlede treningseffekt skal være 1300 kJ må hun trene i  {round(x, 1)} minutter")