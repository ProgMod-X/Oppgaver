import matplotlib.pyplot as plt


def deltaY(k, y, w):
    return (k * y) + w

factor = -0.2
change = 125
inBody = 0

x_list = []
y_list = []

for i in range(100):
    inBody += deltaY(factor, inBody, change)
    x_list.append(i)
    y_list.append(inBody)
    
plt.plot(x_list, y_list, ".")
plt.hlines(inBody, 0, 100, "r")
plt.grid()
plt.show()