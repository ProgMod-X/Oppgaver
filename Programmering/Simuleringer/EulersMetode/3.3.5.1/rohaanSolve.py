import matplotlib.pyplot as plt

def f(tank):
    return 1 - 0.0025 * tank

tank = 0
x = 0
dx = 0.001

x_list = []
y_list = []

while x < 3000:
    if int(x) % 50 == 0:
        x_list.append(x)
        y_list.append(tank)
    tank += (1 - tank * 0.0025) * dx
    x += dx

plt.plot(x_list, y_list)
plt.show()