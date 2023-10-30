import matplotlib.pyplot as plt

x_liste = []
y_liste = []

x = -5
while x <= 5:
    y = x**2 + 2
    
    x_liste.append(x)
    y_liste.append(y)
    
    x += 1
    
plt.plot(x_liste, y_liste, "o")
plt.show()

Forklar med egne ord hva som skjer i while-løkken over.