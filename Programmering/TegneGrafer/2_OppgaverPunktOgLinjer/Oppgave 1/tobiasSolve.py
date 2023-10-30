import random
import matplotlib.pyplot as plt

x_list = []
y_list = []

for i in range(100):
    x_list.append(random.randint(0,100))
    y_list.append(random.randint(0,100))
    
plt.plot(x_list, y_list, "o")
plt.show()