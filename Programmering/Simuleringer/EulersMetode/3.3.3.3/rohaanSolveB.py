import math

def f(x):
    return 42 * (1 - math.e**(-x) + 1.05 * x)

x = 0
dx = 0.001
N = 1

print(f"Treningseffekten etter 3 minutter er {round(f(3), 1)} kJ/min")

while x < N:
    if round(f(x), 1) == 50:
        print(f"Treningseffekten er 50 kJ/min etter {round(x * 60, 1)} sekunder")
    x += dx