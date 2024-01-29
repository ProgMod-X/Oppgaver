import matplotlib.pyplot as plt

tank = 60
miles = 0
K = 0.01

x_list = []
y_list = []

while tank > 0:
    x_list.append(miles)
    y_list.append(tank)

    tank += -0.70 - 0.01 * tank
    miles += 1

plt.plot(x_list, y_list)
plt.show()