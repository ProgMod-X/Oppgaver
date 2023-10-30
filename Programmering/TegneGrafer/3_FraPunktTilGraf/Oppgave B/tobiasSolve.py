import matplotlib.pyplot as plt

# Øker med 0.5

x_liste = []
y_liste = []

x = -5

while x <= 5:
    y = x**2 + 2
    
    x_liste.append(x)
    y_liste.append(y)
    
    x += 0.5
    
plt.plot(x_liste, y_liste, "o")
plt.show()

# Øker med 0.1

x_liste = []
y_liste = []

x = -5

while x <= 5:
    y = x**2 + 2
    
    x_liste.append(x)
    y_liste.append(y)
    
    x += 0.1
    
plt.plot(x_liste, y_liste, "o")
plt.show()

# Øker med 0.01

x_liste = []
y_liste = []

x = -5

while x <= 5:
    y = x**2 + 2
    
    x_liste.append(x)
    y_liste.append(y)
    
    x += 0.01
    
plt.plot(x_liste, y_liste, "o")
plt.show()

# Tallet viser hvor mye vi hopper frem for hvert punkt vi plotter
# Etterhvert som tallet blir mindre, øker vi presisjonen (Grafen blir mindre hakkete)