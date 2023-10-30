import matplotlib.pyplot as plt

def f(x):
    return (x-1)*(x-4)

x_liste = []
y_liste = []

x = -1

while x <= 5:
    x_liste.append(x)
    y_liste.append(f(x))
    
    x += 0.01
    
print(f"Vf = [{min(y_liste)}, {max(y_liste)}]")
    
plt.plot(x_liste, y_liste)
plt.show()