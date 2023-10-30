import random
import matplotlib.pyplot as plt

x_list = []
y_list = []

for i in range(500):
    x_list.append(random.randint(0,320))
    y_list.append(random.randint(0,200))
    
plt.plot(x_list, y_list)
plt.show()