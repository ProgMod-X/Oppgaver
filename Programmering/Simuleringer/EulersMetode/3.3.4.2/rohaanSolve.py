import matplotlib.pyplot as plt

def f(kropp):
    return kropp * -0.20 + 125

kropp = 125
x_list = []
y_list = []

for i in range(1, 100):
    x_list.append(i)
    y_list.append(kropp)
    kropp += f(kropp)

plt.plot(x_list, y_list, ".")
plt.hlines(kropp, 1, 100, "r")
plt.show()