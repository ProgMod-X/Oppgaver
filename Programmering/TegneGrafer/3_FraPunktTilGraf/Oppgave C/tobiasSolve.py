import matplotlib.pyplot as plt

# Øker med 0.5

x_liste = []
y_liste = []

x = -5

while x <= 5:
    y = x**2 + 2
    
    x_liste.append(x)
    y_liste.append(y)
    
    x += 0.01
    
plt.plot(x_liste, y_liste, "-")
plt.show()