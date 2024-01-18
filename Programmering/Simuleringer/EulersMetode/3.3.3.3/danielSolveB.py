import math
import matplotlib.pyplot as plt
 
def f(x):
    return 42*(1 - (math.e**-x)) + 1.05*x
 
x = 0
dx = 1
 
x_verdier = []
y_verdier = []
 
while x < 25:
    x_verdier.append(x)
    y_verdier.append(f(x))
    
    if x == 3:
        print("Treningseffekt etter 3 min er", round(y_verdier[-1]), "kJ/min")
    
    if y_verdier[-1] >= 50 and y_verdier[-1] <= 51:
        print("Nå er treningseffekten over 50 kJ/min på", x, "minutt")
        
    x += dx