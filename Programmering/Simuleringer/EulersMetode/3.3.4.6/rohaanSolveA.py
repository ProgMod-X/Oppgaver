import matplotlib.pyplot as plt

def f(kropp):
    return kropp * 0.75 + 20

kropp = 0
dx = 1
maxX = 40

x_list = []
y_list = []

for i in range(maxX):
    kropp = f(kropp)
    x_list.append(i)
    y_list.append(kropp)

plt.plot(x_list, y_list)
plt.hlines(80, 0, maxX, "r")
plt.show()