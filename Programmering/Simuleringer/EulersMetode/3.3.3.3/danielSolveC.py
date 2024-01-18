import math
import matplotlib.pyplot as plt
 
def f(x):
    return 42*(1 - (math.e**-x)) + 1.05*x
 
x = 0
dx = 1
 
x_verdier = []
y_verdier = []
total = 0
 
while x <= 10:
    x_verdier.append(x)
    y_verdier.append(f(x))
    total += y_verdier[-1]
    x += dx
 
print("Samlede energiforbruk er", round(total), "kJ")
 