import math
import matplotlib.pyplot as plt

def f(x):
    return 42*(1 - (math.e**-x)) + 1.05*x

x = 0
dx = 0.001

x_verdier = []
y_verdier = []
total = 0

while total <= 1300:
    x_verdier.append(x)
    y_verdier.append(f(x))
    total += y_verdier[-1]
    x += dx

print("For at det samlede energiforbruket skal bli 1300kJ må hun trene i",x, "minutter")

