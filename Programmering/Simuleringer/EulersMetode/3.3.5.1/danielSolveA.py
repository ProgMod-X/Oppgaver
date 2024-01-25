import matplotlib.pyplot as plt

# y' = 1 - 0.0025 * y
def f(y):
    return 1 - 0.0025 * y

# Biodisel (y)
y = 0
# Liter tappet ut (x)
x = 0
# Endringen i liter tappet
delta_x = 0.001  

# Antall liter tappet ut
x_values = []  
# Mengde biodiesel
y_values = []  

while x < 400:
    x_values.append(x)
    y_values.append(y)
    
    if round(y, 3) == 200:
        print(f"Det må tappes ut {x} liter diesel før halvparten er biodiesel")
    
    # (y' = f(y)) -> oppdatere biodieselmengden i tanken
    delta_y = f(y) * delta_x
    y += delta_y
    
    # Oppdater liter
    x += delta_x

plt.plot(x_values, y_values)
plt.xlabel('Antall liter tappet ut (x)')
plt.ylabel('Mengde biodiesel (y)')
plt.title('Utvikling i mengden biodiesel på tanken')
plt.show()
