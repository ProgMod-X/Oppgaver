import math
import matplotlib.pyplot as plt
 
def f(x):
    return 6.594*(math.pi**(0.234*x))
 
x = 0
dx = 1
 
x_verdier = []
y_verdier = []
 
while x < 25:
    x_verdier.append(x)
    y_verdier.append(f(x))
    if y_verdier[-1] > 160 and y_verdier[-1] < 200:
        print(x+2005)
    x += dx