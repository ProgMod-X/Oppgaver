import math
import matplotlib.pyplot as plt
 
def f(t):
    return 10000 / (1+50*(math.e**(-0.5*t)))
 
t = 0
dx = 1
 
x_verdier = []
y_verdier = []
 
while t < 25:
    x_verdier.append(t)
    y_verdier.append(f(t))
    if y_verdier[-1] > 7000 and y_verdier[-1] < 7500:
        print(t)
    t += dx
 