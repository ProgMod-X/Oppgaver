import math
import matplotlib.pyplot as plt
 
def f(x):
    return 6.594*(math.pi**(0.234*x))
 
x = 0
dx = 0.0001
 
x_verdier = []
y_verdier = []
total = 0
 
while x < 15:
    x_verdier.append(x)
    y_verdier.append(f(x))
    total += y_verdier[-1]
    x += dx
 
print(round(total))
 