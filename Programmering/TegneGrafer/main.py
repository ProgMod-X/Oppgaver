import matplotlib.pyplot as plt
import random

x_verdier = []
y_verdier = []

for i in range(500):
    x_verdier.append(random.randint(0,320))
    y_verdier.append(random.randint(0,200))

for i in range(500):
    plt.plot(x_verdier, y_verdier, "o-")

plt.show()